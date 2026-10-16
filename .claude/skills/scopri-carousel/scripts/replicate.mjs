// Replicate image generation + background removal for carousel assets. Optional: the in-house 3D renderer
// (assets/3d) covers glass & chrome objects without any API.
// The token is read ONLY from the REPLICATE_API_TOKEN environment variable and is never printed or written.
//   PowerShell:  $env:REPLICATE_API_TOKEN = "r8_..."      or keep it in .env and run:  node --env-file=.env replicate.mjs ...
// Commands:
//   node replicate.mjs check                                  validate the token (prints only the account name)
//   node replicate.mjs schema <owner/model>                   list a model's input fields before using it
//   node replicate.mjs generate --name <file-stem> --prompt "<text>" [--model owner/model] [--input '{"aspect_ratio":"4:5"}']
//                               [--remove-bg] [--bg-model owner/model] [--bg-key image]
// Output: <project>/assets/generated/<name>-raw.<ext>, <name>.png (cutout when --remove-bg), <name>.json (provenance)
import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const API = 'https://api.replicate.com/v1';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../../..');
const outDir = path.join(root, 'assets', 'generated');
const DEFAULT_MODEL = 'black-forest-labs/flux-1.1-pro';
const DEFAULT_BG = '851-labs/background-remover';

const token = process.env.REPLICATE_API_TOKEN?.trim();
if (!token) {
  console.error('REPLICATE_API_TOKEN is not set. Create a token at https://replicate.com/account/api-tokens (it starts with r8_),\n' +
    'then set it for this shell ($env:REPLICATE_API_TOKEN = "r8_..." in PowerShell) or run node with --env-file=.env.');
  process.exit(2);
}
if (!token.startsWith('r8_') || token.length < 36)
  console.warn(`Warning: the token has ${token.length} characters and ${token.startsWith('r8_') ? '' : 'does not start with r8_'}: Replicate tokens normally look like r8_ + 37 characters.`);

const headers = { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' };
async function api(url, init = {}) {
  const r = await fetch(url.startsWith('http') ? url : API + url, { ...init, headers: { ...headers, ...(init.headers || {}) } });
  const body = await r.json().catch(() => ({}));
  if (r.status === 401) throw new Error('401 Unauthenticated: the token is not valid. Create a new one at replicate.com/account/api-tokens.');
  if (r.status === 402) throw new Error('402 Payment required: add a payment method to the Replicate account.');
  if (r.status === 404) throw new Error(`404: ${url} not found (check the model name with "schema").`);
  if (!r.ok) throw new Error(`${r.status}: ${body.detail || body.title || JSON.stringify(body).slice(0, 200)}`);
  return body;
}
async function run(model, input) {
  let p = await api(`/models/${model}/predictions`, { method: 'POST', headers: { Prefer: 'wait=60' }, body: JSON.stringify({ input }) });
  const t0 = Date.now();
  while (!['succeeded', 'failed', 'canceled'].includes(p.status)) {
    if (Date.now() - t0 > 300000) throw new Error(`Timed out waiting for prediction ${p.id}`);
    await new Promise(r => setTimeout(r, 2000));
    p = await api(p.urls.get);
  }
  if (p.status !== 'succeeded') throw new Error(`Prediction ${p.id} ${p.status}: ${p.error || ''}`);
  const out = Array.isArray(p.output) ? p.output[0] : p.output;
  if (typeof out !== 'string') throw new Error(`Unexpected output shape from ${model}: ${JSON.stringify(p.output).slice(0, 200)}`);
  return { id: p.id, url: out };
}
async function download(url, file) {
  const r = await fetch(url); if (!r.ok) throw new Error(`Download failed (${r.status})`);
  await writeFile(file, Buffer.from(await r.arrayBuffer()));
}

const [cmd, ...rest] = process.argv.slice(2);
const opt = (k, d) => { const i = rest.indexOf(k); return i >= 0 ? rest[i + 1] : d; };
try {
  if (cmd === 'check') {
    const a = await api('/account');
    console.log(`Token OK · account: ${a.username || a.name || '(no name)'}`);
  } else if (cmd === 'schema') {
    const m = await api(`/models/${rest[0]}`);
    const props = m.latest_version?.openapi_schema?.components?.schemas?.Input?.properties || {};
    console.log(`${rest[0]}: ${m.description || ''}\nInput fields:`);
    for (const [k, v] of Object.entries(props)) console.log(`  ${k}${v.enum ? ' [' + v.enum.join('|') + ']' : ''}${v.default !== undefined ? ' = ' + JSON.stringify(v.default) : ''}${v.description ? ' · ' + v.description.slice(0, 90) : ''}`);
  } else if (cmd === 'generate') {
    const name = opt('--name'), prompt = opt('--prompt');
    if (!name || !prompt) throw new Error('generate needs --name and --prompt');
    const model = opt('--model', DEFAULT_MODEL), extra = JSON.parse(opt('--input', '{}'));
    await mkdir(outDir, { recursive: true });
    const gen = await run(model, { prompt, ...extra });
    const ext = (new URL(gen.url).pathname.split('.').pop() || 'png').toLowerCase();
    const raw = path.join(outDir, `${name}-raw.${ext}`);
    await download(gen.url, raw);
    const record = { name, model, prompt, input: extra, prediction: gen.id, created: new Date().toISOString(), raw: path.basename(raw) };
    console.log(`Generated ${path.relative(root, raw)}`);
    if (rest.includes('--remove-bg')) {
      const bgModel = opt('--bg-model', DEFAULT_BG), key = opt('--bg-key', 'image');
      const cut = await run(bgModel, { [key]: gen.url });
      const file = path.join(outDir, `${name}.png`);
      await download(cut.url, file);
      Object.assign(record, { bgModel, bgPrediction: cut.id, cutout: path.basename(file) });
      console.log(`Cutout ${path.relative(root, file)} (check the edges before using it)`);
    }
    await writeFile(path.join(outDir, `${name}.json`), JSON.stringify(record, null, 2));
  } else {
    console.log('Commands: check | schema <owner/model> | generate --name <stem> --prompt "<text>" [--model] [--input] [--remove-bg]');
  }
} catch (e) {
  console.error(e.message);
  process.exit(1);
}

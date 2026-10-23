// Versione tweet: disegna le schede dei prompt (1080×608, fondo nero, font Inter) che tweet.py mette sotto il testo.
// Escono media/tweet-prompt-01.png … -10.png (da prompts.json) e media/tweet-confronto.png (slide «Tre regole»).
// Uso (dalla cartella del carosello): node genera-schede-tweet.mjs
import puppeteer from 'puppeteer-core';
import { readFile, writeFile, unlink } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const P = JSON.parse(await readFile(path.join(here, 'prompts.json'), 'utf8'));
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const ph = s => esc(s).replace(/\[([^\]]+)\]/g, (_, x) => `<b class="ph">[${x}]</b>`);
const ICON = '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="3"/><circle cx="9" cy="10" r="1.8"/><path d="M4 17l5-5 4 4 3-3 4 4"/></svg>';
const SEND = '<svg viewBox="0 0 24 24"><path d="M12 19V5M5.5 11.5L12 5l6.5 6.5"/></svg>';

const page = body => `<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=block" rel="stylesheet">
<style>
html,body{margin:0;width:1080px;height:608px;background:#000;-webkit-font-smoothing:antialiased;font-family:Inter,sans-serif}
.wrap{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.card{width:960px;box-sizing:border-box;background:#16181C;border:2px solid #2F3336;border-radius:32px;padding:30px 36px 28px;color:#E7E9EA}
.att{display:flex;align-items:center;gap:14px;font:500 22px Inter;color:#71767B;letter-spacing:.02em}
.thumb{width:52px;height:52px;border-radius:12px;background:rgba(143,163,255,.16);display:grid;place-items:center}
.thumb svg{width:28px;height:28px;fill:none;stroke:#8FA3FF;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
p{margin:20px 0 0;font:400 33px/1.36 Inter;letter-spacing:-.2px;text-wrap:pretty}
.ph{color:#8FA3FF;font-weight:700}
.keep{margin-top:18px;padding-top:18px;border-top:2px solid #2F3336;color:#B7BBC0}
.keep b{color:#8FA3FF;font-weight:700}
.foot{margin-top:14px;display:flex;justify-content:flex-end}
.send{width:50px;height:50px;border-radius:50%;background:#8FA3FF;display:grid;place-items:center}
.send svg{width:24px;height:24px;fill:none;stroke:#0B0E22;stroke-width:2.8;stroke-linecap:round;stroke-linejoin:round}
.cmp{display:flex;gap:24px;width:960px}
.cmp .card{flex:1;padding:32px 30px}
.tag{font:700 22px Inter;letter-spacing:.12em;color:#71767B}
.cmp .win{border-color:#8FA3FF}
.cmp .win .tag{color:#8FA3FF}
.t{margin-top:16px;font:700 36px/1.2 Inter;color:#fff}
.no .t{text-decoration:line-through;text-decoration-thickness:3px;color:#71767B}
.cmp p{font-size:29px;margin-top:14px;color:#B7BBC0}
.cmp p b{color:#fff}
</style></head><body><div class="wrap">${body}</div></body></html>`;

const pages = P.map((p, i) => [`tweet-prompt-${String(i + 1).padStart(2, '0')}.png`, page(`<div class="card">
  <div class="att"><span class="thumb">${ICON}</span>Allega la tua foto</div>
  <p>${ph(p.prompt)}</p>
  <p class="keep"><b>Lascia uguale:</b> ${ph(p.uguale)}</p>
  <div class="foot"><span class="send">${SEND}</span></div></div>`)]);
pages.push(['tweet-confronto.png', page(`<div class="cmp">
  <div class="card no"><div class="tag">COSÌ NO</div><div class="t">«Migliora la foto»</div><p>L'AI tira a indovinare. E a volte ti cambia anche il viso.</p></div>
  <div class="card win"><div class="tag">COSÌ SÌ</div><div class="t">«Ritocca la luce»</div><p><b>Lascia uguale:</b> viso, pelle e capelli. Cambia solo quello che chiedi.</p></div></div>`)]);

const executablePath = [process.env.CHROME_PATH, '/opt/pw-browsers/chromium', '/usr/bin/google-chrome'].filter(Boolean).find(p => existsSync(p));
const browser = await puppeteer.launch({ executablePath, headless: true, args: process.getuid?.() === 0 ? ['--no-sandbox'] : [] });
try {
  for (const [name, html] of pages) {
    const tmp = path.join(here, `_${name}.html`);
    await writeFile(tmp, html);
    const pg = await browser.newPage();
    await pg.setViewport({ width: 1080, height: 608 });
    await pg.goto(pathToFileURL(tmp).href, { waitUntil: 'networkidle0' });
    await pg.evaluate(() => document.fonts.ready);
    if (!await pg.evaluate(() => document.fonts.check("400 33px Inter", 'Aàè'))) throw new Error('Inter non caricato');
    const h = await pg.evaluate(() => document.querySelector('.wrap > *').getBoundingClientRect().height);
    if (h > 592) console.error(`${name}: scheda troppo alta (${Math.round(h)} px)`);
    await pg.screenshot({ path: path.join(here, 'media', name) });
    await pg.close(); await unlink(tmp);
    console.log('media/' + name, Math.round(h));
  }
} finally { await browser.close(); }

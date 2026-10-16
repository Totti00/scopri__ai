// Renders glass & chrome objects from render-3d.html with the installed Chrome (WebGL via SwiftShader) and
// saves difference-matted transparent PNGs to <project>/assets/generated/ (+ a JSON with size and alignment data).
// Usage (from the project root): node .claude/skills/scopri-carousel/assets/3d/render-assets.mjs magnifier hourglass [--ss 3]
import puppeteer from 'puppeteer-core';
import { mkdir, writeFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../../../../..');
const outDir = path.join(root, 'assets', 'generated'), rawDir = path.join(outDir, 'raw');
const args = process.argv.slice(2), ssAt = args.indexOf('--ss');
const ss = ssAt >= 0 ? +args.splice(ssAt, 2)[1] : 3;
const assets = args.length ? args : ['magnifier', 'hourglass'];
const executablePath = [process.env.CHROME_PATH, '/opt/pw-browsers/chromium', 'C:/Program Files/Google/Chrome/Application/chrome.exe',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome'].filter(Boolean).find(p => existsSync(p));
if (!executablePath) throw new Error('Chrome not found: set CHROME_PATH');

await mkdir(rawDir, { recursive: true });
const browser = await puppeteer.launch({ executablePath, headless: true,
  args: [...(process.getuid?.() === 0 ? ['--no-sandbox'] : []), '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--force-color-profile=srgb'] });
try {
  for (const asset of assets) {
    const page = await browser.newPage();
    page.on('console', m => m.type() === 'error' && console.error('  [page]', m.text()));
    page.on('pageerror', e => console.error('  [page]', e.message));
    await page.goto(pathToFileURL(path.join(here, 'render-3d.html')).href + `?asset=${asset}&ss=${ss}`, { waitUntil: 'networkidle0' });
    await page.waitForFunction('window.__ready === true', { timeout: 60000 });
    const t = Date.now();
    const { png, meta, gl } = await page.evaluate(() => window.renderAsset());
    await writeFile(path.join(rawDir, `${asset}@${ss}x.png`), Buffer.from(png.split(',')[1], 'base64'));
    await writeFile(path.join(rawDir, `${asset}.meta.json`), JSON.stringify({ ss, ...meta }, null, 2));
    console.log(`${asset}: rendered in ${Date.now() - t} ms (WebGL2: ${gl})`);
    await page.close();
  }
} finally {
  await browser.close();
}
// Lanczos downscale on premultiplied alpha + crop to the object's bounds
execFileSync('python', [path.join(here, 'finish-assets.py'), outDir, ...assets], { stdio: 'inherit' });

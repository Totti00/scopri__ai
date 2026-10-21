// Renders every slide of index.html to an exact 1080 × 1350 PNG with the installed Chrome, after the in-page QA.
// Usage (from this carousel folder): npm run export      (set CHROME_PATH if Chrome lives elsewhere)
import puppeteer from 'puppeteer-core';
import { mkdir, readFile, readdir, unlink } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(here, 'exports');
const executablePath = [
  process.env.CHROME_PATH,
  '/opt/pw-browsers/chromium',
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/usr/bin/google-chrome',
].filter(Boolean).find(p => existsSync(p));
if (!executablePath) throw new Error('Chrome not found: set CHROME_PATH');

const pngSize = buf => [buf.readUInt32BE(16), buf.readUInt32BE(20)];

await mkdir(outDir, { recursive: true });
for (const f of await readdir(outDir)) if (/^slide-\d+\.png$/.test(f)) await unlink(path.join(outDir, f));   // no stale slides
const browser = await puppeteer.launch({ executablePath, headless: true, args: [...(process.getuid?.() === 0 ? ['--no-sandbox'] : []), '--force-color-profile=srgb', '--hide-scrollbars'] });
try {
  const page = await browser.newPage();
  page.on('pageerror', e => { console.error('Page error:', e.message); process.exitCode = 1; });
  await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(here, 'index.html')).href + '?export=1', { waitUntil: 'networkidle0' });
  await page.waitForFunction('window.__ready === true', { timeout: 30000 });

  const { errors, info } = await page.evaluate(() => window.runQA());
  info.forEach(l => console.log('  ' + l));
  if (errors.length) { console.error(`QA failed (${errors.length}):\n  ` + errors.join('\n  ')); process.exitCode = 1; }
  else console.log('QA passed');

  const slides = await page.$$('.slide');
  for (const [i, el] of slides.entries()) {
    const file = path.join(outDir, `slide-${String(i + 1).padStart(2, '0')}.png`);
    await el.screenshot({ path: file });
    const [w, h] = pngSize(await readFile(file));
    if (w !== 1080 || h !== 1350) { console.error(`${path.basename(file)} is ${w}×${h}`); process.exitCode = 1; }
    else console.log(`${path.basename(file)}  ${w}×${h}`);
  }
} finally {
  await browser.close();
}

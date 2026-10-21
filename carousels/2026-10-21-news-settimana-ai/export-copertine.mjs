// Renders the alternative covers of copertine.html as exports/copertina-<x>.png.
// Each <!--VARIANT x ...--> block replaces slide 1 of index.html (between <!--COVER-START--> and <!--COVER-END-->),
// so the engine draws the real cover frame: logo, «SCORRI PER SCOPRIRE», short cover line, QA.
// Usage (from this carousel folder): node export-copertine.mjs
import puppeteer from 'puppeteer-core';
import { readFile, writeFile, unlink } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const executablePath = [process.env.CHROME_PATH, '/opt/pw-browsers/chromium', '/usr/bin/google-chrome',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'].filter(Boolean).find(p => existsSync(p));
const index = await readFile(path.join(here, 'index.html'), 'utf8');
const src = await readFile(path.join(here, 'copertine.html'), 'utf8');
const variants = [...src.matchAll(/<!--VARIANT (\w)[^>]*-->([\s\S]*?)(?=<!--VARIANT|$)/g)].map(m => [m[1], m[2]]);
const browser = await puppeteer.launch({ executablePath, headless: true, args: [...(process.getuid?.() === 0 ? ['--no-sandbox'] : []), '--force-color-profile=srgb', '--hide-scrollbars'] });
try {
  for (const [key, block] of variants) {
    const tmp = path.join(here, `_copertina-${key}.html`);
    await writeFile(tmp, index.replace(/<!--COVER-START-->[\s\S]*?<!--COVER-END-->/, block));
    const page = await browser.newPage();
    page.on('pageerror', e => { console.error('Page error:', e.message); process.exitCode = 1; });
    await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 1 });
    await page.goto(pathToFileURL(tmp).href + '?export=1', { waitUntil: 'networkidle0' });
    await page.waitForFunction('window.__ready === true', { timeout: 30000 });
    const { errors } = await page.evaluate(() => window.runQA());
    if (errors.length) { console.error(`copertina-${key}: QA (${errors.length}):\n  ` + errors.join('\n  ')); process.exitCode = 1; }
    else console.log(`copertina-${key}: QA passed`);
    await (await page.$('.slide')).screenshot({ path: path.join(here, 'exports', `copertina-${key}.png`) });
    await page.close();
    await unlink(tmp);
  }
} finally { await browser.close(); }

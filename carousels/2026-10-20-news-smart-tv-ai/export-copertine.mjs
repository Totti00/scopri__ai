// Renders the alternative covers in copertine.html to exports/copertina-a.png, -b, -c, -d (same frame as slide 1).
// Usage (from this carousel folder): node export-copertine.mjs
import puppeteer from 'puppeteer-core';
import { mkdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(here, 'exports');
const executablePath = [process.env.CHROME_PATH, '/opt/pw-browsers/chromium', '/usr/bin/google-chrome',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'].filter(Boolean).find(p => existsSync(p));
const TOTAL = process.env.COVER_TOTAL || '08';   // content slides of the real carousel
await mkdir(outDir, { recursive: true });
const browser = await puppeteer.launch({ executablePath, headless: true, args: [...(process.getuid?.() === 0 ? ['--no-sandbox'] : []), '--force-color-profile=srgb', '--hide-scrollbars'] });
try {
  const page = await browser.newPage();
  page.on('pageerror', e => { console.error('Page error:', e.message); process.exitCode = 1; });
  await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(here, 'copertine.html')).href + '?export=1', { waitUntil: 'networkidle0' });
  await page.waitForFunction('window.__ready === true', { timeout: 30000 });
  const { errors } = await page.evaluate(() => window.runQA());
  if (errors.length) { console.error(`QA (${errors.length}):\n  ` + errors.join('\n  ')); process.exitCode = 1; } else console.log('QA passed');
  // every cover is "slide 1": counter 01 / TOTAL, filled swipe cue, and the same thread start as the real cover
  await page.evaluate(total => {
    document.querySelectorAll('.slide').forEach(sl => {
      const c = sl.querySelector('.f-count'); if (c) c.innerHTML = `<b>01</b> / ${total}`;
      sl.querySelector('.f-cue')?.classList.add('filled');
      if (sl.querySelector('.display') && !sl.querySelector('.f-swipe')) sl.insertAdjacentHTML('beforeend', '<div class="f-swipe">Scorri per scoprire</div>');   // cover swipe invite (20 Oct 2026)
      if (sl.querySelector('.display')) sl.insertAdjacentHTML('beforeend',
        `<svg class="layer thread" viewBox="0 0 1080 1350"><path d="M600 1150 H1080" style="fill:none;stroke:var(--line);stroke-width:8;stroke-linecap:round;opacity:.5" filter="url(#lineglow)"/><path d="M600 1150 H1080" style="fill:none;stroke:var(--line);stroke-width:3;stroke-linecap:round"/><circle cx="600" cy="1150" r="6" style="fill:var(--line)"/></svg>`);
    });
  }, TOTAL);
  const slides = (await page.$$('.slide')).slice(0, -1);   // the last one is the dummy closing slide
  for (const [i, el] of slides.entries()) {
    const file = path.join(outDir, `copertina-${'abcdefgh'[i]}.png`);
    await el.screenshot({ path: file });
    console.log(path.basename(file));
  }
} finally { await browser.close(); }

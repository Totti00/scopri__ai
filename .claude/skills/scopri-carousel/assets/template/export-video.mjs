// Animated carousels: renders each slide to its own 1080 × 1350 H.264 MP4 by seeking the paused animations
// frame by frame (deterministic, no screen recording), plus a poster PNG of the final frame.
// Usage (from this carousel folder): npm run export:video        env: FPS (default 30), CHROME_PATH, FFMPEG_PATH
import puppeteer from 'puppeteer-core';
import { mkdir, rm, copyFile, readdir, unlink } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(here, 'exports'), tmp = path.join(here, `.frames-${process.pid}`);   // per run: parallel runs can't clobber each other
const FPS = +(process.env.FPS || 30);
const executablePath = [process.env.CHROME_PATH, '/opt/pw-browsers/chromium', 'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/usr/bin/google-chrome'].filter(Boolean).find(p => existsSync(p));
if (!executablePath) throw new Error('Chrome not found: set CHROME_PATH');

function findFfmpeg() {
  if (process.env.FFMPEG_PATH && existsSync(process.env.FFMPEG_PATH)) return process.env.FFMPEG_PATH;
  if (spawnSync('ffmpeg', ['-version']).status === 0) return 'ffmpeg';
  try { const p = createRequire(path.join(here, 'package.json'))('ffmpeg-static'); if (p && existsSync(p)) return p; } catch {}
  throw new Error('ffmpeg not found. Install it once at the project root: npm install ffmpeg-static  (or set FFMPEG_PATH)');
}
const ffmpeg = findFfmpeg();

await mkdir(outDir, { recursive: true });
for (const f of await readdir(outDir)) if (/^slide-\d+\.(png|mp4)$/.test(f)) await unlink(path.join(outDir, f));
const browser = await puppeteer.launch({ executablePath, headless: true, args: [...(process.getuid?.() === 0 ? ['--no-sandbox'] : []), '--force-color-profile=srgb', '--hide-scrollbars'] });
try {
  const page = await browser.newPage();
  page.on('pageerror', e => { console.error('Page error:', e.message); process.exitCode = 1; });
  await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(here, 'index.html')).href + '?export=1&video=1', { waitUntil: 'networkidle0' });
  await page.waitForFunction('window.__ready === true', { timeout: 30000 });

  const { errors } = await page.evaluate(() => window.runQA());
  if (errors.length) { console.error(`QA failed (${errors.length}):\n  ` + errors.join('\n  ')); process.exitCode = 1; }
  else console.log('QA passed');

  const count = await page.evaluate(() => window.__video.count);
  for (let i = 0; i < count; i++) {
    const name = `slide-${String(i + 1).padStart(2, '0')}`, dir = path.join(tmp, name);
    await rm(dir, { recursive: true, force: true }); await mkdir(dir, { recursive: true });
    const ms = await page.evaluate(k => { window.__video.show(k); return window.__video.duration(k); }, i);
    const frames = Math.round(ms / 1000 * FPS), t0 = Date.now();
    for (let f = 0; f < frames; f++) {
      await page.evaluate((k, t) => window.__video.seek(k, t), i, f * 1000 / FPS);
      await page.screenshot({ path: path.join(dir, `f-${String(f).padStart(5, '0')}.png`), clip: { x: 0, y: 0, width: 1080, height: 1350 }, optimizeForSpeed: true });
    }
    const mp4 = path.join(outDir, `${name}.mp4`);
    const r = spawnSync(ffmpeg, ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(dir, 'f-%05d.png'),
      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-movflags', '+faststart', mp4], { stdio: 'inherit' });
    if (r.status !== 0) { console.error(`ffmpeg failed on ${name}`); process.exitCode = 1; continue; }
    await copyFile(path.join(dir, `f-${String(frames - 1).padStart(5, '0')}.png`), path.join(outDir, `${name}.png`));   // poster = final state
    console.log(`${name}.mp4  ${frames} frames @ ${FPS} fps (${(ms / 1000).toFixed(1)} s)  rendered in ${((Date.now() - t0) / 1000).toFixed(0)} s`);
  }
} finally {
  await browser.close();
  await rm(tmp, { recursive: true, force: true });
}

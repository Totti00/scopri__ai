// Real videos inside slides (added 16 Oct 2026 for Scopri AI news): every slide that holds one or more
// <div class="video-box" data-video="media/clip.mp4" data-start="12" data-dur="8"> becomes exports/slide-XX.mp4.
// Usage (from this carousel folder, after `npm run export`):  npm run media            → trimmed clips
//                                                            npm run media -- --full  → also slide-XX-completo.mp4 (whole source video)
// How it works: 1) a poster frame of each clip is shown in the box, so slide-XX.png and the previews look right;
// 2) the slide is captured twice: the full slide, then only what sits ON TOP of the video (the frame and any element
// with class "over-video"), on a transparent background; 3) ffmpeg stacks: full slide → video (rounded corners,
// optional mono tone) → top layer. No audio: the user adds music in Instagram.
// Box attributes: data-video (path from this folder), data-start (s, default 0), data-dur (s, default 8),
// data-fit="cover|contain" (default cover), data-pos (0–1 horizontal crop, default .5), data-tone="mono|color" (default mono).
import puppeteer from 'puppeteer-core';
import { mkdir, writeFile, rm } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
import os from 'node:os';

const here = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(here, 'exports');
const full = process.argv.includes('--full');
const FPS = 30;
const executablePath = [process.env.CHROME_PATH, '/opt/pw-browsers/chromium', 'C:/Program Files/Google/Chrome/Application/chrome.exe',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome'].filter(Boolean).find(p => existsSync(p));
if (!executablePath) throw new Error('Chrome not found: set CHROME_PATH');
let ffmpeg = 'ffmpeg';
if (spawnSync('ffmpeg', ['-version']).status !== 0) {
  try { ffmpeg = (await import('ffmpeg-static')).default; } catch { throw new Error('ffmpeg not found: install it or npm i ffmpeg-static'); }
}
const PY = spawnSync('python', ['--version']).status === 0 ? 'python' : 'python3';   // Windows: python, Linux: either
const run = (cmd, args) => { const r = spawnSync(cmd, args, { encoding: 'utf8' }); if (r.status !== 0) throw new Error(`${cmd} failed:\n${(r.stderr || '').slice(-1500)}`); return r.stdout; };
const duration = f => {   // from ffmpeg's own banner, so it also works with ffmpeg-static (no ffprobe)
  const m = /Duration: (\d+):(\d+):([\d.]+)/.exec(spawnSync(ffmpeg, ['-i', f], { encoding: 'utf8' }).stderr || '');
  if (!m) throw new Error(`Cannot read the duration of ${f}`);
  return +m[1] * 3600 + +m[2] * 60 + +m[3];
};

const tmp = path.join(os.tmpdir(), `scopri-media-${process.pid}`);
await mkdir(tmp, { recursive: true });
await mkdir(outDir, { recursive: true });
const browser = await puppeteer.launch({ executablePath, headless: true,
  args: [...(process.getuid?.() === 0 ? ['--no-sandbox'] : []), '--force-color-profile=srgb', '--hide-scrollbars'] });
try {
  const page = await browser.newPage();
  page.on('pageerror', e => { console.error('Page error:', e.message); process.exitCode = 1; });
  await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(here, 'index.html')).href + '?export=1', { waitUntil: 'networkidle0' });
  await page.waitForFunction('window.__ready === true', { timeout: 30000 });

  // 1) posters: one frame per box, shown as the box background
  const boxes = await page.evaluate(() => [...document.querySelectorAll('.slide')].flatMap((sl, i) =>
    [...sl.querySelectorAll('.video-box[data-video]')].map((b, k) => {
      const r = b.getBoundingClientRect(), s = sl.getBoundingClientRect();
      return { slide: i, k, video: b.dataset.video, start: +(b.dataset.start || 0), dur: +(b.dataset.dur || 8),
        fit: b.dataset.fit || 'cover', pos: +(b.dataset.pos ?? .5), tone: b.dataset.tone || 'mono',
        x: Math.round(r.left - s.left), y: Math.round(r.top - s.top), w: Math.round(r.width), h: Math.round(r.height),
        radius: parseFloat(getComputedStyle(b).borderTopLeftRadius) || 0 };
    })));
  if (!boxes.length) { console.log('No .video-box in index.html: nothing to do.'); process.exit(0); }
  for (const b of boxes) {
    const src = path.join(here, b.video);
    if (!existsSync(src)) throw new Error(`Missing video ${b.video} (slide ${b.slide + 1})`);
    b.src = src;
    b.poster = path.join(outDir, `poster-${String(b.slide + 1).padStart(2, '0')}-${b.k + 1}.jpg`);
    run(ffmpeg, ['-y', '-loglevel', 'error', '-ss', String(b.start + Math.min(1, b.dur / 2)), '-i', src, '-frames:v', '1', '-q:v', '3', b.poster]);
  }
  await page.evaluate(list => list.forEach(b => {
    const box = document.querySelectorAll('.slide')[b.slide].querySelectorAll('.video-box[data-video]')[b.k];
    box.style.backgroundImage = `url("${b.posterUrl}")`;
    box.style.backgroundSize = b.fit === 'contain' ? 'contain' : 'cover';
    box.style.backgroundPosition = `${b.pos * 100}% 50%`;
    box.style.backgroundRepeat = 'no-repeat';
  }), boxes.map(b => ({ ...b, posterUrl: pathToFileURL(b.poster).href })));

  // Anything drawn in front of a box in the page (later in the DOM or with a higher z-index) and touching it
  // stays in front of the video too: mark it "over-video" automatically.
  await page.evaluate(() => document.querySelectorAll('.slide').forEach(sl => {
    const vbs = [...sl.querySelectorAll('.video-box[data-video]')];
    if (!vbs.length) return;
    const z = el => parseInt(getComputedStyle(el).zIndex) || 0;
    const hit = (a, b) => a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top;
    [...sl.children].forEach(el => {
      if (el.matches('.video-box,.layer,.glow,.ghost,.supershape')) return;
      const r = el.getBoundingClientRect();
      if (vbs.some(b => hit(r, b.getBoundingClientRect()) &&
          (z(el) > z(b) || (z(el) === z(b) && (b.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING))
           || el.matches('.txt,.pill,.sticker,.card')))) el.classList.add('over-video');
    });
  }));
  const slides = await page.$$('.slide');
  const bySlide = [...new Set(boxes.map(b => b.slide))];
  for (const i of bySlide) {
    const nn = String(i + 1).padStart(2, '0');
    // 2a) full slide with posters (also refreshes the static PNG used by the previews)
    const base = path.join(outDir, `slide-${nn}.png`);
    await slides[i].screenshot({ path: base });
    // 2b) only what sits on top of the video, on transparency
    await page.evaluate(() => document.body.classList.add('overlay-pass'));
    const top = path.join(tmp, `top-${nn}.png`);
    await slides[i].screenshot({ path: top, omitBackground: true });
    await page.evaluate(() => document.body.classList.remove('overlay-pass'));

    // 3) ffmpeg: one pass per output (trimmed, and the whole clip with --full)
    const mine = boxes.filter(b => b.slide === i);
    for (const whole of full ? [false, true] : [false]) {
      const D = whole ? Math.max(...mine.map(b => duration(b.src))) : Math.max(...mine.map(b => b.dur));
      const args = ['-y', '-loglevel', 'error', '-loop', '1', '-framerate', String(FPS), '-t', String(D), '-i', base];
      let filter = '', last = '[0:v]';
      mine.forEach((b, j) => {
        const mask = path.join(tmp, `mask-${nn}-${j}.png`);
        run(PY, ['-c', `import sys\nfrom PIL import Image, ImageDraw\nw,h,r=int(sys.argv[1]),int(sys.argv[2]),int(float(sys.argv[3]))\nm=Image.new('L',(w,h),0)\nImageDraw.Draw(m).rounded_rectangle([0,0,w-1,h-1],radius=r,fill=255)\nm.save(sys.argv[4])`, String(b.w), String(b.h), String(b.radius), mask]);
        args.push(...(whole ? [] : ['-ss', String(b.start), '-t', String(b.dur)]), '-i', b.src, '-loop', '1', '-i', mask);
        const vi = 1 + j * 2, mi = 2 + j * 2;
        const fit = b.fit === 'contain'
          ? `scale=${b.w}:${b.h}:force_original_aspect_ratio=decrease,pad=${b.w}:${b.h}:(ow-iw)/2:(oh-ih)/2:color=0x0A0A0D`
          : `scale=${b.w}:${b.h}:force_original_aspect_ratio=increase,crop=${b.w}:${b.h}:(iw-${b.w})*${b.pos}:(ih-${b.h})/2`;
        const tone = b.tone === 'mono' ? ',hue=s=0,eq=contrast=1.08,colorbalance=bs=.10:bm=.07:bh=.03' : '';
        filter += `[${vi}:v]fps=${FPS},${fit}${tone},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=${D},format=rgba[v${j}];` +
                  `[${mi}:v]format=gray,scale=${b.w}:${b.h}[m${j}];[v${j}][m${j}]alphamerge[vm${j}];` +
                  `${last}[vm${j}]overlay=${b.x}:${b.y}:shortest=0[b${j}];`;
        last = `[b${j}]`;
      });
      args.push('-loop', '1', '-i', top);
      const ti = 1 + mine.length * 2;
      filter += `${last}[${ti}:v]overlay=0:0,format=yuv420p[out]`;
      const out = path.join(outDir, `slide-${nn}${whole ? '-completo' : ''}.mp4`);
      run(ffmpeg, [...args, '-filter_complex', filter, '-map', '[out]', '-t', String(D), '-r', String(FPS),
        '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-an', '-movflags', '+faststart', out]);
      console.log(`${path.basename(out)}  ${D.toFixed(1)} s`);
    }
  }
} finally {
  await browser.close();
  await rm(tmp, { recursive: true, force: true });
}

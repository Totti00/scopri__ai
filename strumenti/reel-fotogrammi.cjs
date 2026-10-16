// Trasforma una pagina HTML animata (animazioni CSS) in una sequenza di PNG trasparenti.
// Uso: node strumenti/reel-fotogrammi.cjs <input.html> <cartella-uscita> <durata-secondi> [fps]
// Ferma tutte le animazioni e le porta al tempo di ogni fotogramma: il risultato è sempre identico.
// Stampa la posizione dell'elemento #buco (dove va il video), se c'è.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function main() {
  const [input, uscita, durata, fpsArg] = process.argv.slice(2);
  if (!input || !uscita || !durata) {
    console.error('Uso: node strumenti/reel-fotogrammi.cjs <input.html> <cartella-uscita> <durata-secondi> [fps]');
    process.exit(1);
  }
  const fps = Number(fpsArg || 30);
  const totale = Math.round(Number(durata) * fps);
  fs.mkdirSync(uscita, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  for (let i = 0; i < totale; i++) {
    const ms = (i * 1000) / fps;
    await page.evaluate((t) => {
      for (const a of document.getAnimations()) { a.pause(); a.currentTime = t; }
    }, ms);
    const nome = path.join(uscita, String(i + 1).padStart(4, '0') + '.png');
    await page.screenshot({ path: nome, omitBackground: true });
  }
  const buco = await page.evaluate(() => {
    const el = document.querySelector('#buco');
    if (!el) return null;
    const r = el.getBoundingClientRect();
    return { x: Math.round(r.x), y: Math.round(r.y), width: Math.round(r.width), height: Math.round(r.height) };
  });
  // Zona sicura dei Reel (strumenti/reel.py): a fine scena ogni elemento .testo sta tra y 230 e 1440, e sotto y 1000 a sinistra di x 850,
  // e il titolo non tocca il video.
  const fuori = await page.evaluate(() => {
    for (const a of document.getAnimations()) {
      const t = a.effect.getComputedTiming();
      a.currentTime = Number.isFinite(t.endTime) ? t.endTime : 0;
    }
    const nome = el => (el.id ? '#' + el.id : el.tagName.toLowerCase() + '.' + [...el.classList].join('.')) +
      ' "' + (el.innerText || el.getAttribute('src') || '').trim().slice(0, 40) + '"';
    const out = [];
    document.querySelectorAll('.testo').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.top < 230 || r.bottom > 1440 || r.right > (r.bottom <= 1000 ? 1017 : 851) || r.left < 40)   // i pulsanti a destra stanno sotto y 1000
        out.push(`${nome(el)}: x ${Math.round(r.left)}–${Math.round(r.right)}, y ${Math.round(r.top)}–${Math.round(r.bottom)}`);
    });
    const t = document.querySelector('#titolo'), b = document.querySelector('#buco');
    if (t && b) {
      const range = document.createRange(); range.selectNodeContents(t);
      const fondo = Math.max(...[...range.getClientRects()].map(r => r.bottom));
      if (fondo > b.getBoundingClientRect().top - 16) out.push(`#titolo finisce a y ${Math.round(fondo)}, sopra il video che inizia a y ${Math.round(b.getBoundingClientRect().top)}`);
    }
    return out;
  });
  const titolo = await page.evaluate(() => {
    const el = document.querySelector('#titolo');
    if (!el) return null;
    const r = el.getBoundingClientRect(), lh = parseFloat(getComputedStyle(el).lineHeight);
    return { y: Math.round(r.y), height: Math.round(r.height), righe: lh ? Math.round(r.height / lh) : null };
  });
  await browser.close();
  console.log(JSON.stringify({ fotogrammi: totale, buco, fuori, titolo }));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

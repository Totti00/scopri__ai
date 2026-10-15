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
  await browser.close();
  console.log(JSON.stringify({ fotogrammi: totale, buco }));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

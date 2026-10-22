// Fotografa una pagina HTML dello stile "tweet" (strumenti/tweet.py) come PNG trasparente e ne misura le parti.
// Uso: node strumenti/tweet-pagina.cjs <input.html> <uscita.png> <larghezza> <altezza>
// Stampa JSON: { finestra: {x,y,w,h} | null, righe: [{nome, righe, max}] }
//   finestra = l'elemento #finestra (dove va la foto o il video)
//   righe    = per ogni elemento con data-max="N": quante righe occupa il testo e il massimo ammesso
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [input, uscita, w, h] = process.argv.slice(2);
  if (!input || !uscita) { console.error('Uso: node strumenti/tweet-pagina.cjs <input.html> <uscita.png> <larghezza> <altezza>'); process.exit(1); }
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +w, height: +h } });
  await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const misure = await page.evaluate(() => {
    const f = document.getElementById('finestra'), r = f && f.getBoundingClientRect();
    const righe = [...document.querySelectorAll('[data-max]')].map(el => {
      const lh = parseFloat(getComputedStyle(el).lineHeight) || parseFloat(getComputedStyle(el).fontSize) * 1.2;
      return { nome: el.dataset.nome || el.id || el.className, righe: Math.round(el.getBoundingClientRect().height / lh), max: +el.dataset.max };
    });
    return { finestra: r ? { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } : null, righe };
  });
  await page.screenshot({ path: uscita, omitBackground: true });
  await browser.close();
  console.log(JSON.stringify(misure));
})().catch(e => { console.error(e); process.exit(1); });

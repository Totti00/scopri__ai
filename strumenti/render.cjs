// Trasforma un file HTML in un'immagine PNG.
// Uso: node strumenti/render.cjs <input.html> <output.png> <larghezza> <altezza> [trasparente]
// Con "trasparente" lo sfondo resta trasparente e stampa la posizione dell'elemento #buco (per i video).
const { chromium } = require('playwright');
const path = require('path');

async function main() {
  const [input, output, width, height, modo] = process.argv.slice(2);
  if (!input || !output || !width || !height) {
    console.error('Uso: node strumenti/render.cjs <input.html> <output.png> <larghezza> <altezza>');
    process.exit(1);
  }
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: Number(width), height: Number(height) } });
  await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const trasparente = modo === 'trasparente';
  await page.screenshot({ path: output, omitBackground: trasparente, clip: { x: 0, y: 0, width: Number(width), height: Number(height) } });
  const buco = trasparente ? await page.evaluate(() => { const r = document.querySelector('#buco').getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height }; }) : null;
  await browser.close();
  console.log(buco ? JSON.stringify(buco) : 'Creato ' + output);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

// Trasforma un file HTML in un'immagine PNG.
// Uso: node strumenti/render.cjs <input.html> <output.png> <larghezza> <altezza>
const { chromium } = require('playwright');
const path = require('path');

async function main() {
  const [input, output, width, height] = process.argv.slice(2);
  if (!input || !output || !width || !height) {
    console.error('Uso: node strumenti/render.cjs <input.html> <output.png> <larghezza> <altezza>');
    process.exit(1);
  }
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: Number(width), height: Number(height) } });
  await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: output, clip: { x: 0, y: 0, width: Number(width), height: Number(height) } });
  await browser.close();
  console.log('Creato ' + output);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

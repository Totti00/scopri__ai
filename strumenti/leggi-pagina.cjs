// Legge il testo di una o più pagine web con il browser (utile per siti che caricano il testo con JavaScript, come blog.google e Reddit).
// Uso: node strumenti/leggi-pagina.cjs <url> [<url> ...]
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36' });
  for (const u of process.argv.slice(2)) {
    try {
      await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 40000 });
      await p.waitForTimeout(4000);
      const sel = (await p.$('article')) ? 'article' : 'body';
      const t = (await p.innerText(sel)).replace(/\n\s*\n+/g, '\n');
      console.log('#####', u, '\n', t.slice(0, 6000));
    } catch (e) { console.log(u, 'ERR', e.message); }
  }
  await b.close();
})();

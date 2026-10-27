// Copertine delle storie in evidenza e storie di «Inizia qui» (27/10/2026), stile blu, font Google Sans Flex.
// Uso: node brand/in-evidenza/genera.mjs   (serve puppeteer-core, come per la skill dei caroselli; Chromium in /opt/pw-browsers)
import puppeteer from 'puppeteer-core';
import { readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const QUI = path.dirname(fileURLToPath(import.meta.url));
const LOGO = 'data:image/png;base64,' + readFileSync(path.join(QUI, '../logo/ufficiale/logo-bianco.png')).toString('base64');
const BLU = 'radial-gradient(120% 80% at 15% 10%, rgba(255,255,255,.28), transparent 55%), linear-gradient(160deg,#4F63FF 0%,#2340FF 50%,#1C33D9 100%)';
const SCURO = 'radial-gradient(90% 50% at 20% 0%, rgba(35,64,255,.35), transparent 70%), #08080C';
const FONT = '<link href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:wght@400;500;600;700;800&display=block" rel="stylesheet">';

// Icone a linea (stile Lucide, licenza ISC), viewBox 24
const ICONE = {
  'inizia-qui': '<path d="M8.5 5.6v12.8a1 1 0 0 0 1.5.86l10.2-6.4a1 1 0 0 0 0-1.72L10 4.74a1 1 0 0 0-1.5.86z" fill="currentColor" stroke="none"/>',
  'prompt': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M12 6.5l1.1 2.4 2.4 1.1-2.4 1.1L12 13.5l-1.1-2.4L8.5 10l2.4-1.1z" fill="currentColor" stroke-width="1"/>',
  'news': '<path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2Zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/><path d="M18 14h-8"/><path d="M15 18h-5"/><path d="M10 6h8v4h-8V6Z"/>',
  'curiosita': '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
  'pdf-gratis': '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5A4.8 8 0 0 1 12 8a4.8 8 0 0 1 4.5-5 2.5 2.5 0 0 1 0 5"/>',
  'come-lavoriamo': '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
  'spunta': '<path d="M20 6 9 17l-5-5"/>',
};
const svg = (k, col, px, sw = 1.9) => `<svg width="${px}" height="${px}" viewBox="0 0 24 24" fill="none" stroke="${col}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round" style="color:${col};flex:none">${ICONE[k]}</svg>`;
const ORDINE = ['inizia-qui', 'prompt', 'news', 'curiosita', 'pdf-gratis', 'come-lavoriamo'];

const pagina = (fondo, dentro) => `<!doctype html><html><head><meta charset="utf-8">${FONT}<style>
html,body{margin:0}*{box-sizing:border-box}
.s{position:relative;width:1080px;height:1920px;background:${fondo};color:#fff;font-family:'Google Sans Flex',sans-serif;overflow:hidden;-webkit-font-smoothing:antialiased}
.logo{position:absolute;left:90px;top:300px;height:72px}
.kick{font:600 34px/1 'Google Sans Flex';letter-spacing:.12em;text-transform:uppercase;opacity:.75}
.tit{font:700 92px/1.14 'Google Sans Flex';letter-spacing:-.025em;margin-top:28px}
.box{background:#2340FF;color:#fff;padding:0 .14em;border-radius:12px;white-space:nowrap;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.box.su-blu{background:#fff;color:#1C33D9}
.testo{font:400 48px/1.32 'Google Sans Flex';opacity:.92;margin-top:44px}
.zona{position:absolute;left:90px;right:90px;top:470px}
.riga{display:flex;gap:34px;align-items:flex-start;padding:38px 0;border-top:2px solid rgba(255,255,255,.14)}
.riga:last-child{border-bottom:2px solid rgba(255,255,255,.14)}
.giorno{flex:none;width:250px;font:700 44px/1.15 'Google Sans Flex'}.giorno small{display:block;font:500 34px/1.3 'Google Sans Flex';opacity:.7;margin-top:6px}
.cosa{font:500 46px/1.25 'Google Sans Flex'}
.piede{position:absolute;left:90px;right:90px;bottom:290px;font:500 38px/1.3 'Google Sans Flex';opacity:.8}
</style></head><body><div class="s">${dentro}</div></body></html>`;

const STORIE = {
  '1': pagina(BLU, `<img class="logo" src="${LOGO}">
    <div class="zona" style="top:640px"><div class="kick">Ciao!</div>
    <div class="tit">Qui scopri l'AI<br><span class="box su-blu">che funziona</span><br><span class="box su-blu">davvero</span></div>
    <div class="testo">Notizie, prompt e curiosità sull'intelligenza artificiale. Spiegate in modo semplice, in italiano.</div></div>
    <div class="piede">Tocca per continuare →</div>`),
  '2': pagina(SCURO, `<img class="logo" src="${LOGO}">
    <div class="zona" style="top:500px"><div class="kick">Cosa trovi</div>
    <div class="tit">Tre appuntamenti<br><span class="box">a settimana</span></div>
    <div style="margin-top:70px">
      <div class="riga"><div class="giorno">Lunedì<small>ore 8:00</small></div><div class="cosa">Le notizie AI della settimana che ti sei perso</div></div>
      <div class="riga"><div class="giorno">Venerdì<small>ore 15:30</small></div><div class="cosa">Prompt pronti da copiare e usare</div></div>
      <div class="riga"><div class="giorno">Domenica<small>ore 21:00</small></div><div class="cosa">Curiosità scientifiche</div></div>
    </div>
    <div class="testo" style="font-size:42px">E una notizia lampo quando succede qualcosa di grosso.</div></div>`),
  '3': pagina(SCURO, `<img class="logo" src="${LOGO}">
    <div class="zona" style="top:560px"><div class="kick">Perché fidarti</div>
    <div class="tit">Notizie <span class="box">controllate</span></div>
    <div style="margin-top:70px">
      <div class="riga">${svg('spunta', '#8FA3FF', 64, 3)}<div class="cosa">Ogni notizia è confermata da almeno 2 fonti affidabili.</div></div>
      <div class="riga">${svg('spunta', '#8FA3FF', 64, 3)}<div class="cosa">Le fonti le trovi sempre in fondo alla didascalia.</div></div>
      <div class="riga">${svg('spunta', '#8FA3FF', 64, 3)}<div class="cosa">Niente titoli esagerati: se è solo una voce, te lo diciamo.</div></div>
    </div></div>`),
  '4': pagina(BLU, `<img class="logo" src="${LOGO}">
    <div class="zona" style="top:640px"><div class="kick">Non perderti niente</div>
    <div class="tit">Segui e attiva<br><span class="box su-blu">la campanella</span></div>
    <div class="testo">Così ti arriva una notifica a ogni nuovo post.</div>
    <div class="testo">Vuoi i PDF gratis con i prompt? Guarda «PDF gratis» tra le storie in evidenza.</div></div>`),
};

const browser = await puppeteer.launch({ executablePath: '/opt/pw-browsers/chromium', headless: true,
  args: ['--no-sandbox', '--disable-background-networking', '--disable-component-update', '--no-first-run', '--disable-sync'] });
const page = await browser.newPage();
await page.setViewport({ width: 1080, height: 1920 });
for (const [i, k] of ORDINE.entries()) {
  await page.setContent(`<!doctype html><html><body style="margin:0"><div style="width:1080px;height:1920px;background:${BLU};display:flex;align-items:center;justify-content:center">${svg(k, '#fff', 500)}</div></body></html>`, { waitUntil: 'load' });
  await page.screenshot({ path: path.join(QUI, 'copertine', `${String(i + 1).padStart(2, '0')}-${k}.png`) });
}
for (const [n, html] of Object.entries(STORIE)) {
  await page.setContent(html, { waitUntil: 'load', timeout: 90000 });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: path.join(QUI, 'inizia-qui', `storia-${n}.png`) });
}
await browser.close();
console.log('Fatto: copertine/ e inizia-qui/');

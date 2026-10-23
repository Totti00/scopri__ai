// Genera pubblicazione/10-prompt-foto.pdf da prompts.json (A4, testo copiabile, brand Scopri AI).
// Uso (dalla cartella del carosello): node genera-pdf.mjs
import puppeteer from 'puppeteer-core';
import { readFile, writeFile, mkdir, unlink } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const items = JSON.parse(await readFile(path.join(here, 'prompts.json'), 'utf8'));
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const ph = s => esc(s).replace(/\[([^\]]+)\]/g, (_, x) => `<span class="ph">[${x.toUpperCase()}]</span>`);
const sections = items.map((p, i) => `<div class="p"><h3><b>${String(i + 1).padStart(2, '0')}</b>${esc(p.titolo)}</h3><p>${ph(p.prompt)}</p><p class="k"><strong>Lascia uguale:</strong> ${ph(p.uguale)}</p></div>`).join('\n');

const html = `<!doctype html><html lang="it"><head><meta charset="utf-8"><title>10 prompt per modificare le foto · Scopri AI</title>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;800&family=JetBrains+Mono:wght@500&display=block" rel="stylesheet">
<style>
@page{size:A4;margin:18mm 16mm 16mm}
@page:first{margin:0}
*{box-sizing:border-box}
body{margin:0;font:400 10.5pt/1.45 'Inter Tight',sans-serif;color:#121218}
.cover{height:296mm;background:#0B0B0F;color:#fff;margin:0;padding:28mm 22mm;display:flex;flex-direction:column;page-break-after:always;
  background-image:radial-gradient(60% 45% at 80% 75%,rgba(35,64,255,.55),transparent 70%)}
.cover img{height:14mm;width:auto;align-self:flex-start}
.cover h1{font:600 54pt/1 'Inter Tight';letter-spacing:-.04em;margin:40mm 0 0}
.cover h1 span{color:#8595FF}
.cover .sub{font:400 15pt/1.4 'Inter Tight';color:#A1A1AC;margin-top:10mm;max-width:120mm}
.cover .how{margin-top:auto;font:400 11pt/1.55 'Inter Tight';color:#D0D0D8;border-top:1px solid rgba(255,255,255,.15);padding-top:6mm}
.cover .how b{color:#fff}
.index{page-break-after:always}
.index h2,.cat h2{font:600 22pt/1.1 'Inter Tight';letter-spacing:-.02em;margin:0 0 6mm;display:flex;gap:4mm;align-items:baseline}
.index h2 span,.cat h2 span{font:500 14pt/1 'JetBrains Mono';color:#2340FF}
.index ol{list-style:none;padding:0;margin:0}
.index li{display:flex;gap:4mm;padding:3.2mm 0;border-top:1px solid #E3E3EA;font:500 13pt/1.2 'Inter Tight'}
.index li b{font:500 10pt/1.6 'JetBrains Mono';color:#2340FF;font-weight:500}
.index .note{margin-top:8mm;color:#55555F;font-size:10.5pt}
.cat{page-break-before:always}
.cat:first-of-type{page-break-before:auto}
.p{break-inside:avoid;padding:3.4mm 0 3.6mm;border-top:1px solid #E3E3EA}
.p h3{margin:0 0 1.2mm;font:600 12pt/1.2 'Inter Tight';display:flex;gap:3mm;align-items:baseline}
.p h3 b{font:500 9pt/1 'JetBrains Mono';color:#2340FF;font-weight:500;min-width:7mm}
.p p{margin:0 0 0 10mm;font-size:11.5pt;color:#2A2A33}
.p .k{margin-top:1.6mm;color:#55555F}.p .k strong{color:#121218}
.ph{color:#0F26BD;background:#E0E4FF;border-radius:2px;padding:0 .12em;font-weight:500}
.end{page-break-before:always;text-align:center;padding-top:60mm}
.end img{height:16mm}
.end p{font:500 14pt/1.5 'Inter Tight';margin-top:10mm}
.end small{display:block;color:#55555F;font-size:10.5pt;margin-top:6mm}
</style></head><body>
<div class="cover">
  <img src="brand/scopri-ai-logo-negativo.png" alt="Scopri AI">
  <h1><span>10 prompt</span><br>per modificare<br>le foto</h1>
  <div class="sub">Per ChatGPT e Gemini. In italiano, pronti da copiare.</div>
  <div class="how"><b>Come si usano.</b> Allega la foto nella chat, copia il prompt, sostituisci le parti tra [PARENTESI QUADRE] e invia. Funzionano con ChatGPT e con Gemini.<br>
  <b>Il trucco:</b> scrivi sempre cosa deve restare uguale. Se non lo dici, l'AI può cambiare anche il viso.<br>
  <b>Attenzione:</b> controlla il risultato prima di usarlo (viso, mani, scritte) e modifica le foto delle altre persone solo con il loro permesso.</div>
</div>
<section class="cat"><h2><span>10</span>prompt per le tue foto</h2>
${sections}
</section>

<div class="end"><img src="brand/scopri-ai-logo-colore.png" alt="Scopri AI"><p>Ti è servito? Seguici su Instagram:<br>@scopri__ai</p><small>Ogni settimana nuovi prompt da provare.</small></div>
</body></html>`;

const tmp = path.join(here, '_pdf.html');
await writeFile(tmp, html);
await mkdir(path.join(here, 'pubblicazione'), { recursive: true });
const executablePath = [process.env.CHROME_PATH, '/opt/pw-browsers/chromium', '/usr/bin/google-chrome'].filter(Boolean).find(p => existsSync(p));
const browser = await puppeteer.launch({ executablePath, headless: true, args: process.getuid?.() === 0 ? ['--no-sandbox'] : [] });
try {
  const page = await browser.newPage();
  await page.goto(pathToFileURL(tmp).href, { waitUntil: 'networkidle0' });
  await page.evaluate(() => document.fonts.ready);
  const ok = await page.evaluate(() => document.fonts.check("600 20px 'Inter Tight'", 'Aàè'));
  if (!ok) throw new Error('Inter Tight non caricato');
  await page.pdf({ path: path.join(here, 'pubblicazione', '10-prompt-foto.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  console.log('pubblicazione/10-prompt-foto.pdf');
} finally { await browser.close(); await unlink(tmp); }

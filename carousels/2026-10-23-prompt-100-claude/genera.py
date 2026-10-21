# Genera index.html (12 slide) e copertine.html (copertine alternative) da prompts.json.
# Uso (dalla cartella del carosello): python3 genera.py
import json, re, html
from pathlib import Path

here = Path(__file__).parent
cats = json.loads((here / 'prompts.json').read_text())

def ph(text):
    """[SEGNAPOSTO] -> span evidenziato (sempre maiuscolo)."""
    t = html.escape(text, quote=False)
    return re.sub(r'\[([^\]]+)\]', lambda m: f'<span class="ph">[{m.group(1).upper()}]</span>', t)

HEAD = '''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Scopri AI · 100 prompt per Claude</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@200;400;500;600;800&family=JetBrains+Mono:wght@500&display=block" rel="stylesheet">
<link rel="stylesheet" href="engine/carousel.css">
<style>
/* ===== Griglia dei prompt: 2 colonne x 5 schede (richiesta del proprietario, 21/10/2026) ===== */
.cat-title{left:96px;top:200px;width:888px;font-size:56px;white-space:nowrap}
.cat-title .n{font:500 40px/1 var(--font-meta);color:var(--acc);letter-spacing:0;margin-right:22px;vertical-align:6px}
.grid{position:absolute;left:96px;top:296px;width:888px;height:790px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(5,1fr);gap:12px;z-index:6}
.pg{position:relative;padding:15px 20px 11px;border-radius:20px;overflow:hidden;box-shadow:inset 0 1px 0 rgba(255,255,255,.12)}
.mode-light .pg{box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 18px 40px -24px rgba(10,10,20,.45)}
.pg .pt{display:flex;align-items:baseline;gap:12px;font:600 25px/1.15 var(--font-primary);letter-spacing:-.01em;color:var(--snow);white-space:nowrap}
.pg .pt b{font:500 19px/1 var(--font-meta);color:var(--accent-300);font-weight:500;min-width:30px}
.pg p{margin:7px 0 0;font:400 21px/1.27 var(--font-primary);color:var(--gray-300);text-wrap:pretty}
.pg .ph{font-weight:500;padding:0 .1em}
.pdf-line{left:96px;top:1100px;width:888px;font:500 22px/1 var(--font-meta);letter-spacing:.06em;text-transform:uppercase;color:var(--meta)}
.pdf-line b{color:var(--acc);font-weight:500}
.apill .hl{background:#fff;color:var(--accent-700);border-radius:14px;padding:6px 12px;margin:0 2px}
/* copertine: schede a ventaglio */
.fan{position:absolute;z-index:6;width:560px;padding:30px 32px 28px}
.fan.back p{visibility:hidden}
.fan .pt{font-size:32px}.fan .pt b{font-size:24px}.fan p{font-size:28px;line-height:1.32;margin-top:12px}
/* copertina D: le 10 categorie */
.cats{position:absolute;left:96px;top:660px;width:888px;display:grid;grid-template-columns:1fr 1fr;column-gap:40px;z-index:7}
.cats div{display:flex;gap:16px;align-items:baseline;padding:22px 0;border-top:2px solid var(--hair);font:500 29px/1.2 var(--font-primary);color:var(--tp);white-space:nowrap}
.cats b{font:500 22px/1 var(--font-meta);color:var(--acc);font-weight:500}
/* copertina C: composer */
.composer{left:96px;top:640px;width:888px;padding:34px 36px 30px}
.composer p{margin:16px 0 0;font:400 30px/1.36 var(--font-primary);color:var(--snow)}
.composer .foot{margin-top:24px;display:flex;align-items:center;gap:12px}
.composer .send{margin-left:auto;width:56px;height:56px;border-radius:50%;background:var(--accent-500);display:grid;place-items:center}
.composer .send svg{width:26px;height:26px;fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
  </filter>
  <filter id="lineglow" filterUnits="userSpaceOnUse" x="0" y="0" width="1080" height="1350">
    <feGaussianBlur stdDeviation="4"/>
  </filter>
</svg>
<header class="devbar">
  <h1>Scopri AI · 100 prompt per Claude<small>1080 × 1350 · npm run export (PNG)</small></h1>
  <button id="btn-grid" aria-pressed="true">Griglia</button>
  <button id="btn-strip" aria-pressed="false">Striscia (giunture)</button>
  <button id="btn-play" hidden>Riproduci animazioni</button>
  <button id="btn-qa">Esegui QA</button>
</header>
<div class="qa" id="qa-out"></div>
<main class="deck" id="deck">
'''

def card(num, title, text, cls='pg card qa-text', style=''):
    st = f' style="{style}"' if style else ''
    return (f'<div class="{cls}"{st}><div class="pt"><b>{num:02d}</b>{html.escape(title)}</div>'
            f'<p>{ph(text)}</p></div>')

# --- copertine ---
fan_items = [(13, *cats[1]['items'][2]), (41, *cats[4]['items'][0]), (3, *cats[0]['items'][2])]
FAN = ''.join([
    card(fan_items[0][0], fan_items[0][1], fan_items[0][2], 'pg card fan back', 'left:480px;top:640px;transform:rotate(-7deg);filter:brightness(.6)'),
    card(fan_items[1][0], fan_items[1][1], fan_items[1][2], 'pg card fan back', 'left:500px;top:730px;transform:rotate(-2.5deg);filter:brightness(.8)'),
    card(fan_items[2][0], fan_items[2][1], fan_items[2][2], 'pg card fan qa-text" id="front', 'left:416px;top:830px;transform:rotate(2deg)'),
])

COVER_A = f'''<div class="slot"><section class="slide mode-dark">
  <div class="layer bg"></div>
  <div class="layer rings" style="--rx:760px;--ry:900px"></div>
  <div class=.glow" style="left:700px;top:900px"></div>
  {FAN}
  <h2 class="txt display qa-text" style="left:96px;top:216px;width:888px" data-lines="2"><span class="em">100 prompt</span><br>per Claude</h2>
  <p class="txt lead qa-text" style="left:96px;top:520px;width:600px" data-lines="2">Divisi in 10 categorie.<br>Pronti da copiare.</p>
</section></div>'''

COVER_B = '''<div class="slot"><section class="slide mode-dark">
  <div class="layer bg"></div>
  <div class="layer rings" style="--rx:780px;--ry:820px"></div>
  <div class="glow" data-for="#magnifier"></div>
  <div class="numeral qa-text" style="top:300px;font-size:400px">100</div>
  <h2 class="txt display qa-text" style="left:96px;top:690px;width:888px;font-size:104px" data-lines="2">prompt per<br><span class="em">Claude</span></h2>
  <p class="txt lead qa-text" style="left:96px;top:950px;width:420px" data-lines="2">Divisi in 10 categorie.<br>Da salvare.</p>
  <img class="asset" id="magnifier" src="../../assets/generated/magnifier.png" style="left:600px;top:810px;width:400px;transform:rotate(-12deg)" alt="">
</section></div>'''

COVER_C = f'''<div class="slot"><section class="slide mode-dark">
  <div class="layer bg"></div>
  <div class="layer rings" style="--rx:540px;--ry:1000px"></div>
  <div class="glow" data-for=".composer"></div>
  <h2 class="txt display qa-text" style="left:96px;top:216px;width:888px" data-lines="3">Smetti di<br>chiedere<br><span class="em">a caso</span></h2>
  <div class="card abs composer qa-text"><div class="ui-meta">Scrivi a Claude</div>
    <p>{ph("Fai da mio insegnante di [ABILITÀ]. Parto da zero: un concetto alla volta, con esempi ed esercizi.")}</p>
    <div class="foot"><span class="ui">100 prompt come questo, dentro</span><span class="send"><svg viewBox="0 0 24 24"><path d="M12 19V5M5.5 11.5L12 5l6.5 6.5"/></svg></span></div></div>
</section></div>'''

CATS = ''.join(f'<div><b>{i+1:02d}</b>{html.escape(c["cat"].split(",")[0].replace(" e documenti","").replace(" e lavoro in proprio","").replace(" e organizzazione","").replace(" e decisioni",""))}</div>' for i, c in enumerate(cats))
COVER_D = f'''<div class="slot"><section class="slide mode-dark">
  <div class="layer bg"></div>
  <div class="layer rings" style="--rx:900px;--ry:300px"></div>
  <h2 class="txt display qa-text" style="left:96px;top:216px;width:888px" data-lines="3"><span class="em">100 prompt</span><br>per Claude,<br>in 10 aree</h2>
  <div class="cats qa-text">{CATS}</div>
</section></div>'''

modes = ['light', 'dark', 'light', 'accent', 'light', 'dark', 'light', 'dark', 'accent', 'light']
slides = []
n = 0
for i, c in enumerate(cats):
    cards = []
    for t, p in c['items']:
        n += 1
        cards.append(card(n, t, p))
    slides.append(f'''<div class="slot"><section class="slide mode-{modes[i]}">
  <div class="layer bg"></div>
  <h2 class="txt h2 cat-title qa-text" data-lines="1"><span class="n">{i+1:02d}</span>{html.escape(c["cat"])}</h2>
  <div class="grid">
    {chr(10).join("    " + x for x in cards).strip()}
  </div>
  <p class="txt pdf-line qa-text" data-lines="1">Commenta <b>«100»</b> per avere il PDF</p>
</section></div>''')

CLOSE = '''<div class="slot"><section class="slide mode-dark">
  <div class="layer bg"></div>
  <div class="layer rings" style="--rx:540px;--ry:300px"></div>
  <div class="glow" style="left:540px;top:290px"></div>
  <div class="logo-full qa-text" data-logo></div>
  <div class="cstack">
    <h2 class="h1 qa-text" style="max-width:880px;font-size:84px" data-lines="2">Vuoi tutti i 100 prompt<br><span class="em">in un posto solo?</span></h2>
    <div class="actions"><span class="apill qa-text"><svg viewBox="0 0 24 24"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12z"/></svg>Commenta <span class="hl">«100»</span> e ti mando il PDF</span></div>
    <p class="follow qa-text" data-lines="1"></p>
  </div>
</section></div>'''

def tail(n_slides):
    seams = [1150] * (n_slides - 1)
    routes = ["'start'"] + ["'straight'"] * (n_slides - 2) + ["'end'"]
    return f'''
</main>
<script>
window.CAROUSEL = {{
  title: '100 prompt per Claude',
  format: 'static',
  tipo: 'prompt',
  seams:  {seams},
  routes: [{", ".join(routes)}],
  threadStart: 780,
}};
</script>
<script src="engine/carousel.js"></script>
</body>
</html>
'''

body = '<!--COVER-START-->\n' + COVER_A + '\n<!--COVER-END-->\n' + '\n'.join(slides) + '\n' + CLOSE
(here / 'index.html').write_text(HEAD + body + tail(12))
(here / 'copertine.html').write_text(
    '<!--VARIANT a copertina principale (slide 1)-->\n' + COVER_A + '\n'
    '<!--VARIANT b numero 100 + lente 3D-->\n' + COVER_B + '\n'
    '<!--VARIANT c gancio diverso + scheda chat-->\n' + COVER_C + '\n'
    '<!--VARIANT d le 10 categorie-->\n' + COVER_D + '\n')
print('ok', n, 'prompt')

# Genera index.html da prompts.json (le 10 slide prompt) + copertina, regole e chiusura.
# Uso (dalla cartella del carosello): python3 genera.py
import json, re, html, pathlib

here = pathlib.Path(__file__).parent
P = json.loads((here / 'prompts.json').read_text())

def ph(s):
    s = html.escape(s, quote=False)
    return re.sub(r'\[([^\]]+)\]', lambda m: f'<span class="ph">[{m.group(1)}]</span>', s)

MODES = ['light', 'dark', 'light', 'accent', 'light', 'dark', 'light', 'dark', 'accent', 'dark']

CLIP = '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="3"/><circle cx="9" cy="10" r="1.8"/><path d="M4 17l5-5 4 4 3-3 4 4"/></svg>'
SEND = '<svg viewBox="0 0 24 24"><path d="M12 19V5M5.5 11.5L12 5l6.5 6.5"/></svg>'

def prompt_slide(i, p):
    n = f'{i + 1:02d}'
    return f'''
<!-- ============ Prompt {n} · {p['titolo']} · {MODES[i].upper()} ============ -->
<div class="slot"><section class="slide mode-{MODES[i]}">
  <div class="layer bg"></div>
  <div class="ghost num">{n}</div>
  <div class="glow" data-for=".pc"></div>
  <div class="pill qa-text">Prompt {n}</div>
  <div class="stack">
    <h2 class="h2 qa-text" data-lines="1">{p['h2']}</h2>
    <div class="card pc qa-text">
      <div class="att"><span class="thumb">{CLIP}</span><span class="ui-meta">Allega la tua foto</span></div>
      <p>{ph(p['prompt'])}</p>
      <p class="keep"><b>Lascia uguale:</b> {ph(p['uguale'])}</p>
      <div class="foot"><span class="send">{SEND}</span></div>
    </div>
  </div>
  <p class="txt works qa-text" data-lines="1">Funziona con: <b>ChatGPT, Gemini</b></p>
</section></div>'''

COVER = (here / 'copertine.html').read_text().split('<!--VARIANT')[1]
COVER = COVER[COVER.index('-->') + 3:].strip()

head = (here / '_head.html').read_text()
slides = ''.join(prompt_slide(i, p) for i, p in enumerate(P))

tail = '''
<!-- ============ Regole · LIGHT ============ -->
<div class="slot"><section class="slide mode-light">
  <div class="layer bg"></div>
  <div class="layer dots"></div>
  <div class="pill qa-text">Prima di usarli</div>
  <div class="stack">
    <h2 class="h2 qa-text" data-lines="2">Tre regole<br><span class="em">da ricordare</span></h2>
  </div>
  <div class="tips qa-text">
    <div class="tip"><b>01</b><div><h3>Scrivi cosa resta uguale</h3><p>Se non lo dici, l'AI può cambiare anche il viso.</p></div></div>
    <div class="tip"><b>02</b><div><h3>Controlla prima di usarla</h3><p>Guarda viso, mani e scritte: a volte l'AI li cambia un po'.</p></div></div>
    <div class="tip"><b>03</b><div><h3>Foto di altri? Chiedi prima</h3><p>Modifica le foto delle altre persone solo con il loro permesso.</p></div></div>
  </div>
</section></div>

<!-- ============ Chiusura · DARK ============ -->
<div class="slot"><section class="slide mode-dark">
  <div class="layer bg"></div>
  <div class="layer rings" style="--rx:540px;--ry:300px"></div>
  <div class="glow" style="left:540px;top:290px"></div>
  <div class="logo-full qa-text" data-logo></div>
  <div class="cstack">
    <h2 class="h1 qa-text" style="max-width:880px;font-size:88px" data-lines="2">Vuoi i 10 prompt<br><span class="em">in un PDF?</span></h2>
    <div class="actions"><span class="apill qa-text"><svg viewBox="0 0 24 24"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12z"/></svg>Commenta <span class="hl">«FOTO»</span> e ti mando il PDF</span></div>
    <p class="follow qa-text" data-lines="1"></p>
  </div>
</section></div>
</main>

<script>
window.CAROUSEL = {
  title: '10 prompt per modificare le foto con ChatGPT',
  format: 'static',
  tipo: 'prompt',
  seams:  [1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150],
  routes: ['start', 'straight', 'straight', 'straight', 'straight', 'straight', 'straight', 'straight', 'straight', 'straight', 'straight', 'straight', 'end'],
  threadStart: 780,
};
</script>
<script src="engine/carousel.js"></script>
</body>
</html>
'''

out = head + '\n<!--COVER-START-->\n' + COVER + '\n<!--COVER-END-->\n' + slides + tail
(here / 'index.html').write_text(out)
print('index.html:', len(P), 'prompt +', 'copertina, regole, chiusura')

"""Disegna le 3 proposte di mascotte (stile piatto) e un esempio di slide.
Uso: python3 brand/mascotte/disegna.py  -> crea brand/mascotte/proposte.html
"""
B, C, G, N, W = "#2340FF", "#F4F1EA", "#FFD84D", "#121212", "#FFFFFF"
G2 = "#F2C230"  # giallo un po' più scuro per guance e ombre


def faccia(cx, cy, espr, occhi_bianchi=False):
    s = []
    if espr == "stupito":
        for dx in (-30, 30):
            s.append(f'<circle cx="{cx+dx}" cy="{cy}" r="17" fill="{W}" stroke="{N}" stroke-width="4"/>')
            s.append(f'<circle cx="{cx+dx}" cy="{cy}" r="8" fill="{N}"/>')
            s.append(f'<path d="M{cx+dx-14} {cy-28} Q{cx+dx} {cy-38} {cx+dx+14} {cy-28}" stroke="{N}" stroke-width="5" fill="none" stroke-linecap="round"/>')
        s.append(f'<ellipse cx="{cx}" cy="{cy+40}" rx="11" ry="14" fill="{N}"/>')
    elif espr == "pensieroso":
        for dx in (-30, 30):
            if occhi_bianchi:
                s.append(f'<circle cx="{cx+dx}" cy="{cy}" r="14" fill="{W}" stroke="{N}" stroke-width="4"/>')
            s.append(f'<circle cx="{cx+dx+5}" cy="{cy-5}" r="9" fill="{N}"/>')
        s.append(f'<path d="M{cx-44} {cy-26} L{cx-16} {cy-22}" stroke="{N}" stroke-width="5" stroke-linecap="round"/>')
        s.append(f'<path d="M{cx+16} {cy-30} Q{cx+30} {cy-38} {cx+44} {cy-30}" stroke="{N}" stroke-width="5" fill="none" stroke-linecap="round"/>')
        s.append(f'<path d="M{cx-12} {cy+38} L{cx+16} {cy+34}" stroke="{N}" stroke-width="6" stroke-linecap="round"/>')
    else:  # contento
        for dx in (-30, 30):
            if occhi_bianchi:
                s.append(f'<circle cx="{cx+dx}" cy="{cy}" r="14" fill="{W}" stroke="{N}" stroke-width="4"/>')
            s.append(f'<circle cx="{cx+dx}" cy="{cy}" r="9" fill="{N}"/>')
            s.append(f'<circle cx="{cx+dx+3}" cy="{cy-3}" r="3" fill="{W}"/>')
        s.append(f'<path d="M{cx-22} {cy+28} Q{cx} {cy+50} {cx+22} {cy+28}" stroke="{N}" stroke-width="6" fill="none" stroke-linecap="round"/>')
        s.append(f'<circle cx="{cx-50}" cy="{cy+24}" r="9" fill="{G2}"/><circle cx="{cx+50}" cy="{cy+24}" r="9" fill="{G2}"/>')
    return "".join(s)


def braccia(espr, sx, dx, y, chin):
    """sx/dx = x dei fianchi; chin = (x, y) del mento per la posa pensierosa."""
    def arm(x1, y1, x2, y2):
        return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{N}" stroke-width="8" stroke-linecap="round"/>'
                f'<circle cx="{x2}" cy="{y2}" r="10" fill="{N}"/>')
    if espr == "stupito":
        return arm(sx, y, sx - 40, y - 55) + arm(dx, y, dx + 40, y - 55)
    if espr == "pensieroso":
        return arm(sx, y, sx - 35, y + 35) + arm(dx, y, chin[0], chin[1])
    return arm(sx, y, sx - 35, y + 35) + arm(dx, y, dx + 42, y - 50)  # contento: saluta


def fumetto(espr):
    return (f'<rect x="105" y="85" width="210" height="155" rx="48" fill="{G}"/>'
            f'<polygon points="140,225 128,292 200,236" fill="{G}"/>'
            + braccia(espr, 107, 313, 170, (250, 232)) + faccia(210, 158, espr))


def lente(espr):
    return (f'<line x1="268" y1="235" x2="330" y2="300" stroke="{G}" stroke-width="32" stroke-linecap="round"/>'
            f'<circle cx="200" cy="160" r="98" fill="{C}" stroke="{W}" stroke-width="22"/>'
            + braccia(espr, 100, 300, 180, (205, 228)) + faccia(200, 158, espr, occhi_bianchi=False))


def lampadina(espr):
    return (f'<circle cx="200" cy="150" r="98" fill="{G}"/>'
            f'<rect x="160" y="228" width="80" height="26" fill="{G}"/>'
            f'<rect x="162" y="258" width="76" height="16" rx="8" fill="{W}"/>'
            f'<rect x="170" y="280" width="60" height="16" rx="8" fill="{W}"/>'
            + braccia(espr, 104, 296, 175, (205, 222)) + faccia(200, 145, espr))


def tile(fn, espr, size=300):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 400 400" role="img" aria-label="mascotte {espr}">'
            f'<rect width="400" height="400" rx="28" fill="{B}"/>{fn(espr)}</svg>')


ESPR = ["contento", "stupito", "pensieroso"]
righe = [("1 · Fumetto vivente", fumetto), ("2 · Lente detective", lente), ("3 · Lampadina", lampadina)]

slide = f'''
<div class="slide"><div class="s">
  <div class="top"><div class="logo">Scopri<svg width="74" height="64" viewBox="0 0 700 600"><rect width="700" height="460" rx="110" fill="{G}"/><polygon points="120,440 120,600 280,440" fill="{G}"/><text x="350" y="235" text-anchor="middle" dominant-baseline="central" font-family="Space Grotesk" font-weight="700" font-size="290" fill="{B}">AI</text></svg></div><div class="mono">07/07</div></div>
  <svg width="620" height="620" viewBox="0 0 400 400" style="align-self:center">{fumetto("contento")}</svg>
  <div class="h">Ti è stato utile?<br><span style="color:{G}">Seguici.</span></div>
  <div class="p">Ogni settimana prompt pronti e notizie verificate sull'AI.</div>
  <div class="sp"></div>
  <div class="bar"><span>Segui @scopri__ai</span><span>📌 Salva</span></div>
</div></div>'''

html = f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@700&display=block" rel="stylesheet">
<style>
body{{margin:0;width:1700px;height:1120px;background:#fff;font-family:'Space Grotesk',sans-serif;color:{N};display:flex;gap:30px;padding:30px;box-sizing:border-box}}
.grid{{display:flex;flex-direction:column;gap:22px}}
.r{{display:flex;align-items:center;gap:18px}} .lab{{width:150px;font-size:24px;font-weight:700}}
.cell{{display:flex;flex-direction:column;align-items:center;gap:6px;font-size:18px;color:#555}}
.slide{{width:432px;height:540px;overflow:hidden;border:1px solid #ddd;align-self:center}}
.s{{width:1080px;height:1350px;transform:scale(.4);transform-origin:0 0;background:{B};color:{W};box-sizing:border-box;padding:72px;display:flex;flex-direction:column;gap:30px}}
.top{{display:flex;justify-content:space-between;align-items:center}}.logo{{display:flex;align-items:center;gap:14px;font-size:52px;font-weight:700;letter-spacing:-1px}}
.mono{{font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:700}}
.h{{font-size:104px;font-weight:700;line-height:1;letter-spacing:-3px}}.p{{font-size:40px;line-height:1.35;color:#DDE3FF}}
.sp{{flex:1}}.bar{{display:flex;justify-content:space-between;background:{G};color:{N};padding:30px 36px;font-size:42px;font-weight:700}}
</style></head><body><div class="grid">'''
for nome, fn in righe:
    html += f'<div class="r"><div class="lab">{nome}</div>'
    for e in ESPR:
        html += f'<div class="cell">{tile(fn, e)}<span>{e}</span></div>'
    html += '</div>'
html += f'</div>{slide}</body></html>'

import pathlib
pathlib.Path(__file__).with_name("proposte.html").write_text(html, encoding="utf-8")
print("Creato brand/mascotte/proposte.html")

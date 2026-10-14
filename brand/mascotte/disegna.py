"""Disegna le 3 proposte di mascotte (illustrazione piatta con ombre e luci).
Uso: python3 brand/mascotte/disegna.py  -> crea brand/mascotte/proposte.html
"""
import itertools
import pathlib

B, C, G, N, W = "#2340FF", "#F4F1EA", "#FFD84D", "#121212", "#FFFFFF"
G_OMBRA, G_LUCE = "#EDB92B", "#FFF0A8"
B_TERRA = "#1A2FD0"
BOCCA, LINGUA, GUANCE = "#3B1220", "#FF8FA3", "#FF9B7A"
VETRO, VETRO_OMBRA, METALLO, METALLO_OMBRA = "#E6ECFF", "#C7D2F7", "#DDE2EA", "#C2C9D6"
_id = itertools.count()


def occhio(x, y, espr, colore_palpebra):
    rx, ry = (25, 30) if espr == "stupito" else (21, 25)
    gx, gy = (6, -8) if espr == "pensieroso" else (0, 2)
    s = (f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{W}" stroke="#0E1430" stroke-width="3"/>'
         f'<circle cx="{x+gx}" cy="{y+gy}" r="{12 if espr == "stupito" else 14}" fill="{N}"/>'
         f'<circle cx="{x+gx+5}" cy="{y+gy-5}" r="5" fill="{W}"/><circle cx="{x+gx-4}" cy="{y+gy+5}" r="2.5" fill="{W}"/>')
    if espr == "pensieroso":  # palpebra abbassata
        s += (f'<path d="M{x-rx-3} {y-4} Q{x} {y-ry-6} {x+rx+3} {y-4} L{x+rx+3} {y-ry-6} L{x-rx-3} {y-ry-6} Z" fill="{colore_palpebra}"/>'
              f'<path d="M{x-rx} {y-4} Q{x} {y-14} {x+rx} {y-4}" stroke="#0E1430" stroke-width="3" fill="none" stroke-linecap="round"/>')
    return s


def faccia(cx, cy, espr, colore_pelle):
    s = occhio(cx - 38, cy, espr, colore_pelle) + occhio(cx + 38, cy, espr, colore_pelle)
    my = cy + 42
    if espr == "stupito":
        s += (f'<path d="M{cx-66} {cy-44} Q{cx-38} {cy-62} {cx-12} {cy-46}" stroke="{N}" stroke-width="7" fill="none" stroke-linecap="round"/>'
              f'<path d="M{cx+12} {cy-46} Q{cx+38} {cy-62} {cx+66} {cy-44}" stroke="{N}" stroke-width="7" fill="none" stroke-linecap="round"/>')
        k = next(_id)
        s += (f'<clipPath id="o{k}"><ellipse cx="{cx}" cy="{my+6}" rx="16" ry="20"/></clipPath>'
              f'<ellipse cx="{cx}" cy="{my+6}" rx="16" ry="20" fill="{BOCCA}"/>'
              f'<ellipse cx="{cx}" cy="{my+22}" rx="12" ry="8" fill="{LINGUA}" clip-path="url(#o{k})"/>')
    elif espr == "pensieroso":
        s += (f'<path d="M{cx-60} {cy-36} L{cx-20} {cy-32}" stroke="{N}" stroke-width="7" stroke-linecap="round"/>'
              f'<path d="M{cx+16} {cy-44} Q{cx+40} {cy-58} {cx+62} {cy-42}" stroke="{N}" stroke-width="7" fill="none" stroke-linecap="round"/>'
              f'<path d="M{cx-14} {my+4} Q{cx+6} {my} {cx+22} {my-6}" stroke="{BOCCA}" stroke-width="7" fill="none" stroke-linecap="round"/>')
    else:
        k = next(_id)
        bocca = f'M{cx-30} {my-4} Q{cx} {my+44} {cx+30} {my-4} Z'
        s += (f'<clipPath id="m{k}"><path d="{bocca}"/></clipPath><path d="{bocca}" fill="{BOCCA}"/>'
              f'<ellipse cx="{cx}" cy="{my+24}" rx="15" ry="10" fill="{LINGUA}" clip-path="url(#m{k})"/>')
    s += (f'<ellipse cx="{cx-66}" cy="{cy+34}" rx="16" ry="10" fill="{GUANCE}" opacity=".5"/>'
          f'<ellipse cx="{cx+66}" cy="{cy+34}" rx="16" ry="10" fill="{GUANCE}" opacity=".5"/>')
    return s


def braccio(d, colore, ombra, mano):
    x, y = mano
    return (f'<path d="{d}" stroke="{ombra}" stroke-width="26" fill="none" stroke-linecap="round"/>'
            f'<path d="{d}" stroke="{colore}" stroke-width="17" fill="none" stroke-linecap="round"/>'
            f'<circle cx="{x}" cy="{y}" r="21" fill="{C}"/><circle cx="{x+5}" cy="{y+5}" r="14" fill="{METALLO}" opacity=".6"/>'
            f'<circle cx="{x-6}" cy="{y-6}" r="6" fill="{W}"/>')


def braccia(espr, sx, dx, y, mento, colore, ombra):
    if espr == "stupito":
        return (braccio(f"M{sx} {y} Q{sx-40} {y-20} {sx-48} {y-95}", colore, ombra, (sx - 48, y - 95))
                + braccio(f"M{dx} {y} Q{dx+40} {y-20} {dx+48} {y-95}", colore, ombra, (dx + 48, y - 95)))
    sinistro = braccio(f"M{sx} {y} Q{sx-38} {y+22} {sx-40} {y+72}", colore, ombra, (sx - 40, y + 72))
    if espr == "pensieroso":
        mx, my = mento
        return sinistro + braccio(f"M{dx} {y} Q{dx+34} {y+80} {mx} {my}", colore, ombra, (mx, my))
    return sinistro + braccio(f"M{dx} {y} Q{dx+52} {y-12} {dx+56} {y-82}", colore, ombra, (dx + 56, y - 82))


def gambe(x1, x2, y_da, y_a):
    s = ""
    for x in (x1, x2):
        s += (f'<path d="M{x} {y_da} L{x} {y_a}" stroke="{N}" stroke-width="16" stroke-linecap="round"/>'
              f'<path d="M{x-24} {y_a+12} Q{x-24} {y_a-6} {x+4} {y_a-6} L{x+16} {y_a-6} Q{x+34} {y_a-6} {x+34} {y_a+12} Z" fill="{N}"/>'
              f'<rect x="{x-26}" y="{y_a+10}" width="62" height="7" rx="3.5" fill="{W}"/>')
    return s


def terra(cx):
    return f'<ellipse cx="{cx}" cy="438" rx="120" ry="16" fill="{B_TERRA}"/>'


def fumetto(espr):
    k = next(_id)
    corpo = "M190 110 H310 Q370 110 370 170 V230 Q370 290 310 290 H245 L170 345 L182 290 H190 Q130 290 130 230 V170 Q130 110 190 110 Z"
    return (terra(255) + gambe(228, 292, 288, 412)
            + f'<clipPath id="c{k}"><path d="{corpo}"/></clipPath><path d="{corpo}" fill="{G}"/>'
            + f'<g clip-path="url(#c{k})"><circle cx="430" cy="380" r="205" fill="{G_OMBRA}"/></g>'
            + f'<rect x="160" y="128" width="78" height="18" rx="9" fill="{G_LUCE}"/><circle cx="252" cy="137" r="9" fill="{G_LUCE}"/>'
            + braccia(espr, 134, 366, 222, (300, 268), G, G_OMBRA)
            + faccia(255, 192, espr, G))


def lente(espr):
    return (terra(250)
            + f'<path d="M322 282 L398 368" stroke="{G_OMBRA}" stroke-width="46" stroke-linecap="round"/>'
            + f'<path d="M318 278 L392 362" stroke="{G}" stroke-width="30" stroke-linecap="round"/>'
            + f'<path d="M306 268 L330 292" stroke="{VETRO_OMBRA}" stroke-width="54" stroke-linecap="round"/>'
            + gambe(214, 270, 318, 412)
            + f'<circle cx="242" cy="200" r="118" fill="{VETRO}" stroke="{W}" stroke-width="30"/>'
            + f'<circle cx="242" cy="200" r="100" fill="none" stroke="{VETRO_OMBRA}" stroke-width="8"/>'
            + f'<path d="M168 150 A92 92 0 0 1 226 110" stroke="{W}" stroke-width="13" fill="none" stroke-linecap="round" opacity=".9"/>'
            + braccia(espr, 126, 358, 220, (290, 270), C, VETRO_OMBRA)
            + faccia(242, 196, espr, VETRO))


def lampadina(espr):
    k = next(_id)
    bulbo = "M250 58 A122 122 0 0 1 318 282 L300 302 H200 L182 282 A122 122 0 0 1 250 58 Z"
    raggi = ""
    if espr != "pensieroso":
        for x1, y1, x2, y2 in ((250, 18, 250, -2), (148, 50, 134, 34), (352, 50, 366, 34), (100, 140, 80, 132), (400, 140, 420, 132)):
            raggi += f'<path d="M{x1} {y1+12} L{x2} {y2+12}" stroke="{G}" stroke-width="11" stroke-linecap="round"/>'
    return (terra(250) + raggi + gambe(226, 276, 360, 412)
            + f'<clipPath id="l{k}"><path d="{bulbo}"/></clipPath><path d="{bulbo}" fill="{G}"/>'
            + f'<g clip-path="url(#l{k})"><circle cx="400" cy="300" r="200" fill="{G_OMBRA}"/></g>'
            + f'<ellipse cx="190" cy="118" rx="30" ry="15" fill="{G_LUCE}" transform="rotate(-35 190 118)"/>'
            + f'<rect x="198" y="302" width="104" height="22" rx="11" fill="{METALLO}"/>'
            + f'<rect x="204" y="324" width="92" height="20" rx="10" fill="{METALLO_OMBRA}"/>'
            + f'<rect x="212" y="344" width="76" height="18" rx="9" fill="{METALLO}"/>'
            + braccia(espr, 140, 360, 206, (290, 262), G, G_OMBRA)
            + faccia(250, 180, espr, G))


def tile(fn, espr, size=300):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 500 500" role="img" aria-label="mascotte {espr}">'
            f'<rect width="500" height="500" rx="34" fill="{B}"/><g transform="translate(0 20)">{fn(espr)}</g></svg>')


ESPR = ["contento", "stupito", "pensieroso"]
RIGHE = [("1 · Fumetto vivente", fumetto), ("2 · Lente detective", lente), ("3 · Lampadina", lampadina)]

slide = f'''
<div class="slide"><div class="s">
  <div class="top"><div class="logo">Scopri<svg width="74" height="64" viewBox="0 0 700 600"><rect width="700" height="460" rx="110" fill="{G}"/><polygon points="120,440 120,600 280,440" fill="{G}"/><text x="350" y="235" text-anchor="middle" dominant-baseline="central" font-family="Space Grotesk" font-weight="700" font-size="290" fill="{B}">AI</text></svg></div><div class="mono">07/07</div></div>
  <svg width="640" height="640" viewBox="0 0 500 500" style="align-self:center">{fumetto("contento")}</svg>
  <div class="h">Ti è stato utile?<br><span style="color:{G}">Seguici.</span></div>
  <div class="sp"></div>
  <div class="bar"><span>Segui @scopri__ai</span><span>Salva il post</span></div>
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
.h{{font-size:104px;font-weight:700;line-height:1;letter-spacing:-3px}}
.sp{{flex:1}}.bar{{display:flex;justify-content:space-between;background:{G};color:{N};padding:30px 36px;font-size:42px;font-weight:700}}
</style></head><body><div class="grid">'''
for nome, fn in RIGHE:
    html += f'<div class="r"><div class="lab">{nome}</div>'
    for e in ESPR:
        html += f'<div class="cell">{tile(fn, e)}<span>{e}</span></div>'
    html += '</div>'
html += f'</div>{slide}</body></html>'

if __name__ == "__main__":
    pathlib.Path(__file__).with_name("proposte.html").write_text(html, encoding="utf-8")
    print("Creato brand/mascotte/proposte.html")

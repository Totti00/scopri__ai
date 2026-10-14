"""Foto profilo con la mascotte Fumetto in versione futuristica (stile piatto).
Uso: python3 brand/mascotte/foto_profilo.py -> crea foto-profilo-mascotte-*.html
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from disegna import (B, G, G_OMBRA, G_LUCE, N, W, BOCCA, LINGUA, GUANCE,  # noqa: E402
                     METALLO, METALLO_OMBRA, faccia)

TESTA = "M200 100 H300 Q360 100 360 160 V240 Q360 300 300 300 H200 Q140 300 140 240 V160 Q140 100 200 100 Z"
LUCE = "#9FB0FF"      # azzurro dei led
CIRCUITO = "#E3AC22"  # tracce dei circuiti sul giallo


def antenna():
    return (f'<path d="M250 100 L250 58" stroke="{METALLO_OMBRA}" stroke-width="12" stroke-linecap="round"/>'
            f'<circle cx="250" cy="44" r="30" fill="{W}" opacity=".18"/>'
            f'<circle cx="250" cy="44" r="21" fill="{W}" opacity=".3"/>'
            f'<circle cx="250" cy="44" r="14" fill="{G}"/><circle cx="246" cy="40" r="5" fill="{W}"/>')


def sensori():
    s = ""
    for x in (136, 364):
        s += (f'<rect x="{x-16}" y="168" width="32" height="64" rx="16" fill="{METALLO}"/>'
              f'<rect x="{x-16}" y="200" width="32" height="32" rx="16" fill="{METALLO_OMBRA}"/>'
              f'<circle cx="{x}" cy="190" r="8" fill="{LUCE}"/><circle cx="{x}" cy="190" r="3.5" fill="{W}"/>')
    return s


def circuiti():
    s = ""
    for d, nodo in (("M140 262 H172 V286", (172, 286)), ("M140 140 H160 V122", (160, 122)), ("M330 300 V276 H352", (352, 276))):
        s += (f'<path d="{d}" stroke="{CIRCUITO}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<circle cx="{nodo[0]}" cy="{nodo[1]}" r="6" fill="{CIRCUITO}"/>')
    return s


def chip_ai():
    return (f'<rect x="221" y="112" width="58" height="30" rx="8" fill="{B}"/>'
            f'<text x="250" y="128" text-anchor="middle" dominant-baseline="central" font-family="Space Grotesk" '
            f'font-weight="700" font-size="20" fill="{W}">AI</text>')


def testa():
    return (f'<clipPath id="testa"><path d="{TESTA}"/></clipPath><path d="{TESTA}" fill="{G}"/>'
            f'<g clip-path="url(#testa)"><circle cx="440" cy="400" r="215" fill="{G_OMBRA}"/>{circuiti()}</g>'
            f'<rect x="162" y="114" width="40" height="14" rx="7" fill="{G_LUCE}"/>')


def faccia_led(cx, cy):
    s = ""
    for dx in (-40, 40):
        s += (f'<rect x="{cx+dx-22}" y="{cy-26}" width="44" height="52" rx="16" fill="{W}" stroke="#0E1430" stroke-width="3"/>'
              f'<rect x="{cx+dx-10}" y="{cy-14}" width="20" height="28" rx="8" fill="{B}"/>'
              f'<rect x="{cx+dx-6}" y="{cy-10}" width="7" height="9" rx="3" fill="{W}"/>')
    for i, (x, y) in enumerate(((-30, 34), (-15, 44), (0, 47), (15, 44), (30, 34))):
        s += f'<rect x="{cx+x-6}" y="{cy+y-5}" width="12" height="10" rx="4" fill="{BOCCA}"/>'
    s += (f'<ellipse cx="{cx-70}" cy="{cy+32}" rx="15" ry="9" fill="{GUANCE}" opacity=".5"/>'
          f'<ellipse cx="{cx+70}" cy="{cy+32}" rx="15" ry="9" fill="{GUANCE}" opacity=".5"/>')
    return s


def faccia_visiera(cx, cy):
    s = (f'<rect x="{cx-88}" y="{cy-34}" width="176" height="68" rx="34" fill="#121A3D"/>'
         f'<path d="M{cx-66} {cy-22} H{cx-20}" stroke="{W}" stroke-width="5" stroke-linecap="round" opacity=".35"/>')
    for dx in (-40, 40):
        s += (f'<path d="M{cx+dx-17} {cy+8} Q{cx+dx} {cy-16} {cx+dx+17} {cy+8}" stroke="{LUCE}" stroke-width="13" fill="none" stroke-linecap="round" opacity=".45"/>'
              f'<path d="M{cx+dx-17} {cy+8} Q{cx+dx} {cy-16} {cx+dx+17} {cy+8}" stroke="{W}" stroke-width="7" fill="none" stroke-linecap="round"/>')
    my = cy + 56
    bocca = f'M{cx-28} {my-6} Q{cx} {my+34} {cx+28} {my-6} Z'
    s += (f'<clipPath id="mv"><path d="{bocca}"/></clipPath><path d="{bocca}" fill="{BOCCA}"/>'
          f'<ellipse cx="{cx}" cy="{my+18}" rx="14" ry="9" fill="{LINGUA}" clip-path="url(#mv)"/>'
          f'<ellipse cx="{cx-72}" cy="{cy+46}" rx="15" ry="9" fill="{GUANCE}" opacity=".5"/>'
          f'<ellipse cx="{cx+72}" cy="{cy+46}" rx="15" ry="9" fill="{GUANCE}" opacity=".5"/>')
    return s


def personaggio(versione):
    s = antenna() + sensori() + testa() + chip_ai()
    if versione == "antenna":
        s += faccia(250, 204, "contento", G)
    elif versione == "led":
        s += faccia_led(250, 204)
    else:
        s += faccia_visiera(250, 200)
    return s


def pagina(versione):
    # Composizione (antenna compresa) centrata e ingrandita 3,4 volte.
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&amp;display=block" rel="stylesheet">
<style>html,body{{margin:0;width:1080px;height:1080px}}svg{{display:block}}</style></head><body>
<svg width="1080" height="1080" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg">
<rect width="1080" height="1080" fill="{B}"/>
<g transform="translate(-310 -18) scale(3.4)">{personaggio(versione)}</g>
</svg></body></html>'''


if __name__ == "__main__":
    cartella = pathlib.Path(__file__).parent
    for vecchio in cartella.glob("foto-profilo-mascotte-*"):
        vecchio.unlink()
    for versione in ("antenna", "led", "visiera"):
        (cartella / f"foto-profilo-mascotte-{versione}.html").write_text(pagina(versione), encoding="utf-8")
        print(f"Creato foto-profilo-mascotte-{versione}.html")

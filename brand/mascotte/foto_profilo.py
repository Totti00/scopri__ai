"""Foto profilo con la mascotte Fumetto: solo la "testa" (senza punta del fumetto), inquadrata da vicino.
Uso: python3 brand/mascotte/foto_profilo.py -> crea foto-profilo-mascotte-*.html
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from disegna import B, G, G_OMBRA, G_LUCE, N, faccia  # noqa: E402

# Testa più "quadrata" per il ritratto.
TESTA = "M200 100 H300 Q360 100 360 160 V240 Q360 300 300 300 H200 Q140 300 140 240 V160 Q140 100 200 100 Z"


def occhiolino(cx, cy):
    """Copre l'occhio sinistro e disegna un occhio chiuso."""
    x = cx - 38
    return (f'<ellipse cx="{x}" cy="{cy}" rx="26" ry="30" fill="{G}"/>'
            f'<path d="M{x-20} {cy+2} Q{x} {cy-16} {x+20} {cy+2}" stroke="{N}" stroke-width="7" fill="none" stroke-linecap="round"/>')


def personaggio(espr):
    base = "contento" if espr == "occhiolino" else espr
    s = (f'<clipPath id="testa"><path d="{TESTA}"/></clipPath><path d="{TESTA}" fill="{G}"/>'
         f'<g clip-path="url(#testa)"><circle cx="440" cy="400" r="215" fill="{G_OMBRA}"/></g>'
         f'<rect x="170" y="118" width="74" height="18" rx="9" fill="{G_LUCE}"/><circle cx="258" cy="127" r="9" fill="{G_LUCE}"/>'
         + faccia(250, 198, base, G))
    if espr == "occhiolino":
        s += occhiolino(250, 198)
    return s


def pagina(espr):
    # Centro della testa (250, 200) portato al centro dell'immagine, ingrandito 3,8 volte.
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<style>html,body{{margin:0;width:1080px;height:1080px}}svg{{display:block}}</style></head><body>
<svg width="1080" height="1080" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg">
<rect width="1080" height="1080" fill="{B}"/>
<g transform="translate(-410 -220) scale(3.8)">{personaggio(espr)}</g>
</svg></body></html>'''


if __name__ == "__main__":
    cartella = pathlib.Path(__file__).parent
    for vecchio in cartella.glob("foto-profilo-mascotte-*"):
        vecchio.unlink()
    for espr in ("contento", "occhiolino", "stupito"):
        (cartella / f"foto-profilo-mascotte-{espr}.html").write_text(pagina(espr), encoding="utf-8")
        print(f"Creato foto-profilo-mascotte-{espr}.html")

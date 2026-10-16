#!/usr/bin/env python3
"""Aggiunge i "principi Electric" a una riga di slide Claude Design (.dc.html) di qualsiasi template.

Uso:
    python3 strumenti/principi-electric.py <prefisso-uscita> <slide1.dc.html> <slide2.dc.html> ...
    es. python3 strumenti/principi-electric.py BE bozza/B1-copertina.dc.html bozza/B2-app.dc.html ...
        → crea BE1-copertina.dc.html, BE2-app.dc.html … nella stessa cartella, più <prefisso>-anteprima.png

Cosa aggiunge (opzioni decise il 16/10/2026, dal design system "Electric Mono", ispirazione/electric-mono.md):
- CORNICE FISSA: @scopri__ai in basso a sinistra e la freccia (cerchio) in basso a destra, sempre nello stesso punto;
  contatore "02 / 06" in alto a destra se la slide non ce l'ha già. Niente freccia sulla copertina (ha già la sua) né sull'ultima.
- GRANA: un velo di grana fine su tutta la slide, così i fondi non sembrano piatti.
- FILO: una linea sottile che corre in basso da una slide all'altra alla stessa altezza (y 1334), gialla sui fondi
  scuri o blu, blu su quelli chiari o gialli; parte con un punto sulla copertina e finisce con un punto sull'ultima.
Il disegno del template non cambia: si aggiungono solo questi tre strati sopra.
"""
import pathlib
import re
import subprocess
import sys

RADICE = pathlib.Path(__file__).resolve().parent.parent
BLU, GIALLO, NERO, BIANCO = "#2340FF", "#FFD84D", "#121212", "#FFFFFF"
Y_FILO = 1334


def luminanza(hex6):
    r, g, b = (int(hex6[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)


def colore_fondo(corpo):
    """Il colore della zona bassa della slide (dove passano filo e cornice): l'ultimo blocco ancorato in basso
    (bottom: 0) con un fondo pieno, altrimenti il fondo della slide intera."""
    stili = re.findall(r'style="([^"]*)"', corpo)
    radice = next((re.search(r"background:\s*(#[0-9A-Fa-f]{6})", x).group(1) for x in stili
                   if "width: 1080px" in x.replace("width:1080px", "width: 1080px") and re.search(r"background:\s*#", x)), "#F4F1EA")
    bassi = [re.search(r"background:\s*(#[0-9A-Fa-f]{6})", x).group(1) for x in stili
             if re.search(r"bottom:\s*0(px)?\b", x) and re.search(r"background:\s*#[0-9A-Fa-f]{6}", x)]
    return (bassi[-1] if bassi else radice).upper()


def strati(i, totale, fondo, ha_contatore):
    scuro = luminanza(fondo) < .2
    giallo_fondo = fondo == GIALLO.upper()
    testo = BIANCO if scuro else NERO
    meta = "rgba(255,255,255,.75)" if scuro else "rgba(18,18,18,.7)"
    filo = GIALLO if scuro and not giallo_fondo else BLU
    pezzi = []
    # grana
    op, blend = (".07", "overlay") if scuro else (".06", "multiply")
    pezzi.append(f'<svg width="1080" height="1350" style="position:absolute;left:0;top:0;pointer-events:none;opacity:{op};mix-blend-mode:{blend};z-index:5" aria-hidden="true">'
                 f'<filter id="grana{i}"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch"></feTurbulence>'
                 f'<feColorMatrix type="saturate" values="0"></feColorMatrix></filter><rect width="1080" height="1350" filter="url(#grana{i})"></rect></svg>')
    # filo
    x0 = 72 if i == 1 else 0
    x1 = 1008 if i == totale else 1080
    nodi = "".join(f'<circle cx="{x}" cy="{Y_FILO}" r="7" fill="{filo}"></circle>' for x in ([x0] if i == 1 else []) + ([x1] if i == totale else []))
    pezzi.append(f'<svg width="1080" height="1350" style="position:absolute;left:0;top:0;z-index:6" aria-hidden="true">'
                 f'<path d="M {x0} {Y_FILO} L {x1} {Y_FILO}" stroke="{filo}" stroke-width="3" stroke-linecap="round"></path>{nodi}</svg>')
    # cornice
    pezzi.append(f'<div style="position:absolute;left:72px;top:1298px;z-index:7;font-family:\'JetBrains Mono\',monospace;font-weight:500;font-size:22px;letter-spacing:.04em;color:{meta}">@scopri__ai</div>')
    if 1 < i < totale:
        pezzi.append(f'<div style="position:absolute;right:72px;top:1292px;z-index:7;width:44px;height:44px;box-sizing:border-box;border-radius:50%;border:2px solid {meta};'
                     f'display:flex;align-items:center;justify-content:center"><svg width="20" height="20" viewBox="0 0 44 44" aria-hidden="true"><path d="M6 22h30M24 10l12 12-12 12" '
                     f'fill="none" stroke="{testo}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>')
    if i > 1 and not ha_contatore:
        pezzi.append(f'<div style="position:absolute;right:56px;top:56px;z-index:7;background:{fondo};padding:10px 18px;border-radius:999px;font-family:\'JetBrains Mono\',monospace;'
                     f'font-weight:500;font-size:22px;letter-spacing:.08em;color:{testo}">{i:02d} / {totale:02d}</div>')
    return "\n".join(pezzi)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    prefisso, files = sys.argv[1], [pathlib.Path(f).resolve() for f in sys.argv[2:]]
    uscite = []
    for i, f in enumerate(files, 1):
        t = f.read_text(encoding="utf-8")
        a, b = t.index("<x-dc>"), t.index("</x-dc>")
        corpo = t[a:b]
        fine = corpo.rstrip().rfind("</div>")
        ha_contatore = bool(re.search(r"\b0\d\s*/\s*0\d\b", corpo))
        nuovo = corpo[:fine] + strati(i, len(files), colore_fondo(corpo), ha_contatore) + "\n" + corpo[fine:]
        nome = re.sub(r"^[A-Z]+", prefisso, f.name)
        out = f.parent / nome
        t2 = (t[:a] + nuovo + t[b:]).replace(f"<title>{f.stem.split('.')[0]}", f"<title>{nome}")
        out.write_text(t2, encoding="utf-8")
        uscite.append(out)
        print("Creato", out)
    # anteprima a striscia
    tmp = files[0].parent / f".{prefisso}-anteprima"
    tmp.mkdir(exist_ok=True)
    pngs = []
    for k, f in enumerate(uscite):
        png = tmp / f"{k}.png"
        subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(f), str(png), "1080", "1350"], check=True, stdout=subprocess.DEVNULL)
        pngs.append(png)
    imgs = "".join(f'<img src="file://{x}" style="width:360px;height:450px;display:block">' for x in pngs)
    pag = tmp / "striscia.html"
    pag.write_text(f'<body style="margin:0;display:flex;width:{360 * len(pngs)}px;background:#000">{imgs}</body>')
    subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(pag), str(files[0].parent / f"{prefisso}-anteprima.png"), str(360 * len(pngs)), "450"],
                   check=True, stdout=subprocess.DEVNULL)
    for x in tmp.iterdir():
        x.unlink()
    tmp.rmdir()


if __name__ == "__main__":
    main()

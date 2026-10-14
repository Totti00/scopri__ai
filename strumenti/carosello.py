"""Crea le slide di un carosello Scopri.AI a partire da un file JSON.

Uso:
    python3 strumenti/carosello.py archivio/<cartella-post>/slide.json

Il JSON ha questa forma:
{
  "slides": [
    {"tipo": "copertina", "etichetta": "NEWS LAMPO", "titolo": "Testo con *parola chiave*",
     "sottotitolo": "…", "barra": "Domanda-gancio"},
    {"tipo": "testo", "etichetta": "COS'È SUCCESSO", "titolo": "…", "paragrafi": ["…"],
     "punti": ["…"], "per_te": "…", "fonte": "…"},
    {"tipo": "prompt", "etichetta": "01 · LA MAIL DIFFICILE", "titolo": "…",
     "prompt": "Testo con [PARTI DA CAMBIARE]", "nota": "Funziona con ChatGPT, Claude, Gemini"},
    {"tipo": "chiusura", "titolo": "…", "testo": "…", "domanda": "…"}
  ]
}
Nei testi, *parola* evidenzia la parola (giallo sul blu, riquadro giallo sulla carta).
Le slide vengono salvate come slide-01.png, slide-02.png… nella stessa cartella del JSON.
"""
import html
import json
import pathlib
import re
import subprocess
import sys

BLU, CARTA, GIALLO, NERO, BIANCO = "#2340FF", "#F4F1EA", "#FFD84D", "#121212", "#FFFFFF"
GRIGIO_SU_CARTA, GRIGIO_SU_BLU = "#55565C", "#DDE3FF"
RADICE = pathlib.Path(__file__).resolve().parent.parent


def evidenzia(testo, fondo):
    """Escapa il testo e trasforma *parola* nell'evidenziazione giusta per il fondo."""
    t = html.escape(testo)
    if fondo == "blu":
        stile = f'color:{GIALLO}'
    else:
        stile = f'background:{GIALLO};color:{NERO};padding:0 10px;box-decoration-break:clone;-webkit-box-decoration-break:clone'
    return re.sub(r"\*(.+?)\*", rf'<span style="{stile}">\1</span>', t)


def segnaposto(testo):
    """Nei prompt, evidenzia le parti tra [PARENTESI]."""
    t = html.escape(testo)
    return re.sub(r"\[(.+?)\]", rf'<span style="background:{GIALLO};color:{NERO};padding:0 6px">[\1]</span>', t)


def logo(fondo):
    testo, bolla, scritta = (BIANCO, GIALLO, BLU) if fondo == "blu" else (NERO, BLU, BIANCO)
    return (f'<div style="display:flex;align-items:center;gap:14px;font-size:50px;font-weight:700;letter-spacing:-1.5px;color:{testo}">'
            f'Scopri<svg width="72" height="62" viewBox="0 0 700 600" aria-hidden="true">'
            f'<rect width="700" height="460" rx="110" fill="{bolla}"/><polygon points="120,440 120,600 280,440" fill="{bolla}"/>'
            f'<text x="350" y="235" text-anchor="middle" dominant-baseline="central" font-family="Space Grotesk" '
            f'font-weight="700" font-size="290" fill="{scritta}">AI</text></svg></div>')


def testata(fondo, n, tot):
    colore = BIANCO if fondo == "blu" else NERO
    return (f'<div style="display:flex;justify-content:space-between;align-items:center">{logo(fondo)}'
            f'<div class="mono" style="font-size:30px;color:{colore}">{n:02d}/{tot:02d}</div></div>')


def etichetta(testo, fondo):
    if not testo:
        return ""
    bg, fg = (GIALLO, NERO) if fondo == "blu" else (NERO, CARTA)
    return (f'<div class="mono" style="align-self:flex-start;background:{bg};color:{fg};font-size:30px;'
            f'padding:10px 18px;letter-spacing:2px">{html.escape(testo)}</div>')


def fonte(testo, fondo):
    if not testo:
        return ""
    colore = GRIGIO_SU_BLU if fondo == "blu" else GRIGIO_SU_CARTA
    return f'<div class="mono" style="font-size:24px;font-weight:500;color:{colore}">Fonte: {html.escape(testo)}</div>'


def slide_copertina(s, n, tot):
    sotto = f'<div style="font-size:44px;line-height:1.35;color:{GRIGIO_SU_BLU}">{evidenzia(s["sottotitolo"], "blu")}</div>' if s.get("sottotitolo") else ""
    return ("blu", f'''{testata("blu", n, tot)}
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:44px">
{etichetta(s.get("etichetta"), "blu")}
<div style="font-size:{s.get("dimensione", 124)}px;font-weight:700;line-height:1;letter-spacing:-4px">{evidenzia(s["titolo"], "blu")}</div>
{sotto}
</div>
<div style="display:flex;justify-content:space-between;align-items:center;background:{GIALLO};color:{NERO};padding:32px 40px;font-size:42px;font-weight:700">
<span>{html.escape(s.get("barra", ""))}</span><span>Scorri →</span></div>''')


def slide_testo(s, n, tot):
    corpo = "".join(f'<p style="margin:0">{evidenzia(p, "carta")}</p>' for p in s.get("paragrafi", []))
    if s.get("punti"):
        corpo += '<div style="display:flex;flex-direction:column;gap:22px">' + "".join(
            f'<div style="display:flex;gap:22px"><span style="flex:none;width:44px;height:44px;border-radius:50%;background:{BLU};color:{BIANCO};'
            f'font-size:26px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:4px">{i}</span>'
            f'<span>{evidenzia(p, "carta")}</span></div>' for i, p in enumerate(s["punti"], 1)) + "</div>"
    per_te = (f'<div style="background:{BLU};color:{BIANCO};padding:34px 40px;font-size:40px;line-height:1.35">'
              f'<b style="color:{GIALLO}">👉 Per te:</b> {html.escape(s["per_te"])}</div>') if s.get("per_te") else ""
    return ("carta", f'''{testata("carta", n, tot)}
{etichetta(s.get("etichetta"), "carta")}
<div style="font-size:{s.get("dimensione", 88)}px;font-weight:700;line-height:1.05;letter-spacing:-2.5px">{evidenzia(s["titolo"], "carta")}</div>
<div style="display:flex;flex-direction:column;gap:30px;font-size:40px;line-height:1.4">{corpo}</div>
<div style="flex:1"></div>
{per_te}
{fonte(s.get("fonte"), "carta")}''')


def slide_prompt(s, n, tot):
    nota = f'<div class="mono" style="font-size:26px;font-weight:500;color:{GRIGIO_SU_CARTA}">{html.escape(s["nota"])}</div>' if s.get("nota") else ""
    return ("carta", f'''{testata("carta", n, tot)}
{etichetta(s.get("etichetta"), "carta")}
<div style="font-size:{s.get("dimensione", 80)}px;font-weight:700;line-height:1.05;letter-spacing:-2px">{evidenzia(s["titolo"], "carta")}</div>
<div class="mono" style="background:{BIANCO};border:4px solid {NERO};padding:44px;font-size:{s.get("dimensione_prompt", 36)}px;font-weight:500;line-height:1.5">{segnaposto(s["prompt"])}</div>
<div style="flex:1"></div>
{nota}''')


def slide_chiusura(s, n, tot):
    testo = f'<div style="font-size:44px;line-height:1.35;color:{GRIGIO_SU_BLU}">{html.escape(s["testo"])}</div>' if s.get("testo") else ""
    return ("blu", f'''{testata("blu", n, tot)}
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:44px">
<div style="font-size:112px;font-weight:700;line-height:1;letter-spacing:-4px">{evidenzia(s["titolo"], "blu")}</div>
{testo}
</div>
<div style="font-size:44px;font-weight:700">{html.escape(s.get("domanda", ""))}</div>
<div style="display:flex;justify-content:space-between;align-items:center;background:{GIALLO};color:{NERO};padding:32px 40px;font-size:42px;font-weight:700">
<span>Segui @scopri__ai</span><span>📌 Salva il post</span></div>''')


TIPI = {"copertina": slide_copertina, "testo": slide_testo, "prompt": slide_prompt, "chiusura": slide_chiusura}


def pagina(fondo, contenuto):
    bg, fg = (BLU, BIANCO) if fondo == "blu" else (CARTA, NERO)
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&amp;family=JetBrains+Mono:wght@500;700&amp;display=block" rel="stylesheet">
<style>html,body{{margin:0}}.mono{{font-family:'JetBrains Mono',monospace;font-weight:700}}</style></head>
<body><div style="width:1080px;height:1350px;box-sizing:border-box;padding:72px;background:{bg};color:{fg};font-family:'Space Grotesk',sans-serif;display:flex;flex-direction:column;gap:44px">
{contenuto}
</div></body></html>'''


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    spec_path = pathlib.Path(sys.argv[1]).resolve()
    cartella = spec_path.parent
    slides = json.loads(spec_path.read_text(encoding="utf-8"))["slides"]
    tmp = cartella / ".html"
    tmp.mkdir(exist_ok=True)
    for i, s in enumerate(slides, 1):
        fondo, contenuto = TIPI[s["tipo"]](s, i, len(slides))
        f = tmp / f"slide-{i:02d}.html"
        f.write_text(pagina(fondo, contenuto), encoding="utf-8")
        subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(f), str(cartella / f"slide-{i:02d}.png"), "1080", "1350"], check=True)
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()


if __name__ == "__main__":
    main()

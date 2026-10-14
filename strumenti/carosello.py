"""Crea le slide di un carosello Scopri.AI a partire da un file JSON.

Uso:
    python3 strumenti/carosello.py archivio/<cartella-post>/slide.json

Lo stile (deciso il 14/10/2026, ispirato alle pagine AI, non a RapTrend):
- logo piccolo in alto a sinistra, nessun contatore di pagina, nessuna barra in basso;
- copertina: visual grande in alto, titolo sotto;
- slide interne: testo sopra, visual sotto (screenshot, chat o numero);
- prompt dentro un fumetto di chat, come se lo scrivessi tu;
- ultima slide: l'appuntamento della settimana.

Il JSON ha questa forma:
{
  "rubrica": "News lampo",
  "slides": [
    {"tipo": "copertina", "titolo": "Testo con *parola chiave*", "sottotitolo": "…", "visual": {…}},
    {"tipo": "testo", "titolo": "…", "testo": ["paragrafo con **grassetto**", "…"],
     "per_te": "…", "visual": {…}, "fonte": "…"},
    {"tipo": "prompt", "titolo": "…", "quando": "Quando ti serve…",
     "prompt": "Testo con [PARTI DA CAMBIARE]", "nota": "Cambia le parti in giallo."},
    {"tipo": "chiusura", "domanda": "…"}
  ]
}
Visual possibili:
    {"immagine": "screenshot.png", "didascalia": "…"}    file nella cartella del JSON
    {"chat": [{"chi": "tu", "testo": "…"}, {"chi": "ai", "testo": "…"}], "didascalia": "…"}
    {"numero": "20 mln $", "didascalia": "…"}
Nei testi: *parola* = parola chiave (giallo sul blu, riquadro giallo sulla carta); **parola** = grassetto.
Le slide vengono salvate come slide-01.png, slide-02.png… nella stessa cartella del JSON.
"""
import html
import json
import pathlib
import re
import subprocess
import sys

BLU, BLU_SCURO, CARTA, GIALLO, NERO, BIANCO = "#2340FF", "#1A30C4", "#F4F1EA", "#FFD84D", "#121212", "#FFFFFF"
GRIGIO_SU_CARTA, GRIGIO_SU_BLU, BORDO = "#55565C", "#DDE3FF", "#E2DED3"
RADICE = pathlib.Path(__file__).resolve().parent.parent


def evidenzia(testo, fondo):
    """Escapa il testo; *parola* diventa parola chiave, **parola** grassetto."""
    t = html.escape(testo)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    if fondo == "blu":
        stile = f"color:{GIALLO}"
    else:
        stile = (f"background:{GIALLO};color:{NERO};padding:0 8px;border-radius:6px;"
                 "box-decoration-break:clone;-webkit-box-decoration-break:clone")
    return re.sub(r"\*(.+?)\*", rf'<span style="{stile}">\1</span>', t)


def segnaposto(testo):
    """Nei prompt, evidenzia le parti tra [PARENTESI]."""
    t = html.escape(testo)
    return re.sub(r"\[(.+?)\]", rf'<span style="background:{GIALLO};color:{NERO};padding:0 6px;border-radius:6px">[\1]</span>', t)


def fumetto(colore, scritta, larghezza):
    return (f'<svg width="{larghezza}" height="{larghezza * 6 // 7}" viewBox="0 0 700 600" aria-hidden="true">'
            f'<rect width="700" height="460" rx="110" fill="{colore}"/><polygon points="120,440 120,600 280,440" fill="{colore}"/>'
            f'<text x="350" y="235" text-anchor="middle" dominant-baseline="central" font-family="Space Grotesk" '
            f'font-weight="700" font-size="290" fill="{scritta}">AI</text></svg>')


def logo(fondo):
    """Logo piccolo: discreto, come fanno le pagine AI."""
    testo, bolla, scritta = (BIANCO, GIALLO, BLU) if fondo == "blu" else (NERO, BLU, BIANCO)
    return (f'<div style="display:flex;align-items:center;gap:8px;font-size:32px;font-weight:700;letter-spacing:-1px;color:{testo}">'
            f'Scopri{fumetto(bolla, scritta, 44)}</div>')


def fonte(testo, fondo):
    if not testo:
        return ""
    colore = GRIGIO_SU_BLU if fondo == "blu" else GRIGIO_SU_CARTA
    return f'<div class="mono" style="font-size:22px;font-weight:500;color:{colore}">Fonte: {html.escape(testo)}</div>'


def bolla_chat(chi, testo, dim):
    """Un messaggio di chat: il tuo a destra (blu), quello dell'AI a sinistra (carta)."""
    if chi == "tu":
        return (f'<div style="align-self:flex-end;max-width:82%;background:{BLU};color:{BIANCO};padding:{dim * 0.6:.0f}px {dim * 0.8:.0f}px;'
                f'border-radius:32px 32px 8px 32px;font-size:{dim}px;line-height:1.35">{evidenzia(testo, "blu")}</div>')
    return (f'<div style="align-self:flex-start;display:flex;gap:14px;align-items:flex-end;max-width:88%">'
            f'<div style="flex:none">{fumetto(GIALLO, NERO, round(dim * 1.5))}</div>'
            f'<div style="background:{CARTA};color:{NERO};padding:{dim * 0.6:.0f}px {dim * 0.8:.0f}px;border-radius:32px 32px 32px 8px;'
            f'font-size:{dim}px;line-height:1.35">{evidenzia(testo, "carta")}</div></div>')


def visual(v, cartella, fondo):
    """Il riquadro arrotondato con l'immagine, la chat o il numero."""
    if not v:
        return ""
    didascalia = ""
    if v.get("didascalia"):
        colore = GRIGIO_SU_BLU if fondo == "blu" else GRIGIO_SU_CARTA
        didascalia = f'<div class="mono" style="font-size:22px;font-weight:500;color:{colore};margin-top:14px">{html.escape(v["didascalia"])}</div>'
    cornice = f"flex:1;min-height:0;border-radius:36px;overflow:hidden;background:{BIANCO};border:3px solid {BORDO if fondo == 'carta' else BIANCO}"
    if v.get("immagine"):
        src = (cartella / v["immagine"]).resolve().as_uri()
        adatta = v.get("adatta", "cover")
        interno = f'<img src="{src}" style="width:100%;height:100%;object-fit:{adatta};object-position:{v.get("posizione", "top")};display:block">'
    elif v.get("chat"):
        dim = v.get("dimensione", 46 if fondo == "blu" else 36)
        interno = (f'<div style="height:100%;box-sizing:border-box;padding:40px;display:flex;flex-direction:column;justify-content:center;gap:{dim * 0.8:.0f}px">'
                   + "".join(bolla_chat(m["chi"], m["testo"], dim) for m in v["chat"]) + "</div>")
    elif v.get("numero"):
        interno = (f'<div style="height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;'
                   f'background:{GIALLO};color:{NERO}"><div style="font-size:150px;font-weight:700;letter-spacing:-6px;line-height:1">'
                   f'{html.escape(v["numero"])}</div>'
                   + (f'<div style="font-size:36px;font-weight:500;text-align:center;max-width:80%">{html.escape(v["sotto"])}</div>' if v.get("sotto") else "")
                   + "</div>")
    else:
        return ""
    return f'<div style="flex:1;min-height:0;display:flex;flex-direction:column"><div style="{cornice}">{interno}</div>{didascalia}</div>'


def freccia():
    return (f'<div style="flex:none;width:96px;height:96px;border-radius:50%;background:{GIALLO};color:{NERO};'
            f'display:flex;align-items:center;justify-content:center;font-size:52px;font-weight:700">→</div>')


def slide_copertina(s, ctx):
    sotto = f'<div style="font-size:38px;line-height:1.3;color:{GRIGIO_SU_BLU}">{evidenzia(s["sottotitolo"], "blu")}</div>' if s.get("sottotitolo") else ""
    rubrica = f'<div class="mono" style="font-size:24px;color:{GIALLO};letter-spacing:1px">{html.escape(ctx["rubrica"])}</div>' if ctx.get("rubrica") else ""
    return ("blu", f'''<div style="display:flex;justify-content:space-between;align-items:center">{logo("blu")}{rubrica}</div>
{visual(s.get("visual"), ctx["cartella"], "blu")}
<div style="display:flex;align-items:flex-end;gap:36px">
<div style="flex:1;display:flex;flex-direction:column;gap:22px">
<div style="font-size:{s.get("dimensione", 84)}px;font-weight:700;line-height:1.02;letter-spacing:-3px">{evidenzia(s["titolo"], "blu")}</div>
{sotto}
</div>
{freccia()}
</div>''')


def slide_testo(s, ctx):
    corpo = "".join(f'<p style="margin:0">{evidenzia(p, "carta")}</p>' for p in s.get("testo", []))
    per_te = (f'<div style="border-left:8px solid {GIALLO};padding:4px 0 4px 24px;font-size:34px;line-height:1.35">'
              f'<b>👉 Per te:</b> {evidenzia(s["per_te"], "carta")}</div>') if s.get("per_te") else ""
    return ("carta", f'''{logo("carta")}
<div style="font-size:{s.get("dimensione", 64)}px;font-weight:700;line-height:1.05;letter-spacing:-2px">{evidenzia(s["titolo"], "carta")}</div>
<div style="display:flex;flex-direction:column;gap:22px;font-size:{s.get("dimensione_testo", 34)}px;line-height:1.4">{corpo}</div>
{per_te}
{visual(s.get("visual"), ctx["cartella"], "carta") or '<div style="flex:1"></div>'}
{fonte(s.get("fonte"), "carta")}''')


def slide_prompt(s, ctx):
    quando = f'<div style="font-size:34px;line-height:1.4">{evidenzia(s["quando"], "carta")}</div>' if s.get("quando") else ""
    nota = f'<div class="mono" style="font-size:24px;font-weight:500;color:{GRIGIO_SU_CARTA}">{html.escape(s["nota"])}</div>' if s.get("nota") else ""
    return ("carta", f'''{logo("carta")}
<div style="font-size:{s.get("dimensione", 64)}px;font-weight:700;line-height:1.05;letter-spacing:-2px">{evidenzia(s["titolo"], "carta")}</div>
{quando}
<div style="flex:1;min-height:0;background:{BIANCO};border:3px solid {BORDO};border-radius:36px;display:flex;flex-direction:column;overflow:hidden">
<div class="mono" style="padding:22px 36px;border-bottom:3px solid {BORDO};font-size:24px;color:{GRIGIO_SU_CARTA};display:flex;justify-content:space-between">
<span>Scrivi così all'AI</span><span>ChatGPT · Claude · Gemini</span></div>
<div style="flex:1;padding:40px 36px;display:flex;flex-direction:column;justify-content:center;gap:28px">
<div class="mono" style="align-self:flex-end;max-width:92%;background:{BLU};color:{BIANCO};padding:32px 36px;border-radius:36px 36px 8px 36px;
font-size:{s.get("dimensione_prompt", 36)}px;font-weight:500;line-height:1.5">{segnaposto(s["prompt"])}</div>
<div style="align-self:flex-start;display:flex;gap:14px;align-items:center">{fumetto(GIALLO, NERO, 52)}
<div style="background:{CARTA};padding:18px 26px;border-radius:28px;font-size:34px;letter-spacing:6px;color:{GRIGIO_SU_CARTA}">•••</div></div>
</div></div>
{nota}''')


def slide_chiusura(s, ctx):
    rubriche = s.get("rubriche", [
        ["Lun", "Le news AI della settimana"],
        ["Ven", "Prompt da copiare"],
        ["Dom", "Una curiosità di scienza"],
        ["Extra", "News lampo, quando succede qualcosa"],
    ])
    righe = "".join(
        f'<div style="display:flex;gap:28px;align-items:center;padding:22px 0;border-top:2px solid rgba(255,255,255,.25)">'
        f'<span class="mono" style="flex:none;width:110px;color:{GIALLO};font-size:32px">{html.escape(g)}</span>'
        f'<span style="font-size:40px;font-weight:500">{html.escape(t)}</span></div>' for g, t in rubriche)
    domanda = f'<div style="font-size:40px;font-weight:700;line-height:1.3">{evidenzia(s["domanda"], "blu")}</div>' if s.get("domanda") else ""
    return ("blu", f'''{logo("blu")}
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px">
<div style="font-size:{s.get("dimensione", 92)}px;font-weight:700;line-height:1.02;letter-spacing:-3px">{evidenzia(s.get("titolo", "Ogni settimana, *qualcosa da\u00a0scoprire*."), "blu")}</div>
<div>{righe}</div>
</div>
{domanda}
<div style="font-size:34px;color:{GRIGIO_SU_BLU}">Segui <b style="color:{BIANCO}">@scopri__ai</b> e salva il post per ritrovarlo 📌</div>''')


TIPI = {"copertina": slide_copertina, "testo": slide_testo, "prompt": slide_prompt, "chiusura": slide_chiusura}


def pagina(fondo, contenuto):
    bg, fg = (BLU, BIANCO) if fondo == "blu" else (CARTA, NERO)
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&amp;family=JetBrains+Mono:wght@500;700&amp;display=block" rel="stylesheet">
<style>html,body{{margin:0}}.mono{{font-family:'JetBrains Mono',monospace;font-weight:700}}b{{font-weight:700}}</style></head>
<body><div style="width:1080px;height:1350px;box-sizing:border-box;padding:64px 72px;background:{bg};color:{fg};font-family:'Space Grotesk',sans-serif;display:flex;flex-direction:column;gap:40px">
{contenuto}
</div></body></html>'''


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    spec_path = pathlib.Path(sys.argv[1]).resolve()
    cartella = spec_path.parent
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    ctx = {"rubrica": spec.get("rubrica", ""), "cartella": cartella}
    tmp = cartella / ".html"
    tmp.mkdir(exist_ok=True)
    for i, s in enumerate(spec["slides"], 1):
        fondo, contenuto = TIPI[s["tipo"]](s, ctx)
        f = tmp / f"slide-{i:02d}.html"
        f.write_text(pagina(fondo, contenuto), encoding="utf-8")
        subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(f), str(cartella / f"slide-{i:02d}.png"), "1080", "1350"], check=True)
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()


if __name__ == "__main__":
    main()

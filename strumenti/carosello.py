"""Crea le slide di un carosello Scopri.AI a partire da un file JSON.

Uso:
    python3 strumenti/carosello.py archivio/<cartella-post>/slide.json
    python3 strumenti/carosello.py archivio/<cartella-post>/slide.json --completi
    python3 strumenti/carosello.py archivio/<cartella-post>/slide.json --solo=1,8
        → rifà solo le slide indicate (si può unire a --completi)
        → per ogni slide con video crea anche slide-NN-completo.mp4, con il video sorgente intero
          sotto la stessa grafica: il proprietario lo accorcia da solo (Instagram o CapCut).

Lo stile (deciso il 14/10/2026, ispirato alle pagine AI, non a RapTrend):
- logo piccolo in alto a sinistra, nessun contatore di pagina, nessuna barra in basso;
- copertina: visual grande in alto, titolo sotto;
- slide interne: testo sopra, visual sotto (screenshot, chat o numero);
- prompt dentro un fumetto di chat, come se lo scrivessi tu;
- ultima slide: l'appuntamento della settimana.

Template: "stile": "A" (classico, quello di partenza) oppure "B" (fascia: immagine a tutta larghezza
in alto e fascia di colore sotto, che gira blu → carta → giallo). Ogni slide di testo può avere un
"commento" di due o tre parole, mostrato nel fumetto. Il font si cambia nella costante FONT.

Il JSON ha questa forma:
{
  "rubrica": "News lampo",
  "slides": [
    {"tipo": "copertina", "titolo": "Testo con *parola chiave*", "sottotitolo": "…", "visual": {…}},
    {"tipo": "testo", "titolo": "…", "testo": ["paragrafo con **grassetto**", "…"],
     "per_te": "…", "visual": {…}},
    {"tipo": "prompt", "titolo": "…", "quando": "Quando ti serve…",
     "prompt": "Testo con [PARTI DA CAMBIARE]", "nota": "Cambia le parti in giallo."},
    {"tipo": "chiusura"}   il terminatore attuale (TERMINATORE_ATTUALE); per usarne un altro:
                           {"tipo": "chiusura", "terminatore": "calendario"}
  ]
}
Visual possibili:
    {"immagine": "screenshot.png", "didascalia": "…"}    file nella cartella del JSON
    {"chat": [{"chi": "tu", "testo": "…"}, {"chi": "ai", "testo": "…"}], "didascalia": "…"}
    {"numero": "20 mln $", "didascalia": "…"}
    {"video": "media/clip.mp4", "inizio": 12, "durata": 8, "posizione": 0.5}
    {"video": "media/clip.mp4", "pezzi": [[12, 24], [54, 72]]}   più pezzi dello stesso video, uno dopo l'altro
        → la slide diventa slide-NN.mp4 (senza audio: la musica la mette il proprietario).
          "posizione" sposta il taglio del video da sinistra (0) a destra (1);
          "adatta": "contain" mostra il video intero con bande scure ai lati.
Fonti e crediti delle immagini NON vanno sulle slide: vanno in fondo alla caption.
La "didascalia" serve solo per avvisi come "Esempio illustrativo".
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
SFONDO = {"blu": (BLU, BIANCO), "carta": (CARTA, NERO), "giallo": (GIALLO, NERO)}
FONT = "Bricolage Grotesque"  # font dei testi (scelto il 15/10/2026; il logo resta in Space Grotesk): si cambia qui per tutti i template


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
    return (f'<div class="logo" style="display:flex;align-items:center;gap:8px;font-size:32px;font-weight:700;letter-spacing:-1px;color:{testo}">'
            f'Scopri{fumetto(bolla, scritta, 44)}</div>')



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
    if v.get("video"):
        # Il riquadro resta "bucato": il video viene messo sotto con ffmpeg.
        bg = BLU if fondo == "blu" else CARTA
        buco = f"flex:1;min-height:0;border-radius:36px;box-shadow:0 0 0 3000px {bg}"
        return f'<div class="sotto" style="flex:1;min-height:0;display:flex;flex-direction:column"><div id="buco" style="{buco}"></div>{didascalia}</div>'
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
    """Pallino giallo con la freccia disegnata, perfettamente al centro."""
    return (f'<div style="flex:none;width:96px;height:96px;border-radius:50%;background:{GIALLO};display:flex;align-items:center;justify-content:center">'
            f'<svg width="44" height="44" viewBox="0 0 44 44" aria-hidden="true"><path d="M6 22h30M24 10l12 12-12 12" fill="none" stroke="{NERO}" '
            f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')


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
{commento_a(s)}
{visual(s.get("visual"), ctx["cartella"], "carta") or '<div style="flex:1"></div>'}''')


def commento_a(s):
    if not s.get("commento"):
        return ""
    return (f'<div style="align-self:flex-start;background:{GIALLO};color:{NERO};padding:18px 30px;border-radius:30px 30px 30px 6px;'
            f'font-size:38px;font-weight:700">{html.escape(s["commento"])}</div>')


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
    titolo = evidenzia(s.get("titolo", "Ogni settimana, *qualcosa da\u00a0scoprire*."), "blu")
    return ("blu", f'''{logo("blu")}
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px">
<div style="font-size:{s.get("dimensione", 92)}px;font-weight:700;line-height:1.02;letter-spacing:-3px">{titolo}</div>
<div>{righe}</div>
</div>
{domanda}
<div style="font-size:34px;color:{GRIGIO_SU_BLU}">Segui <b style="color:{BIANCO}">@scopri__ai</b> e salva il post per ritrovarlo 📌</div>''')


SVG_NOTIFICA = f'''<svg width="700" height="660" viewBox="0 0 700 660" aria-hidden="true">
<circle cx="350" cy="330" r="290" fill="{GIALLO}"/>
<g transform="rotate(-8 350 330)">
<rect x="210" y="60" width="280" height="540" rx="44" fill="{NERO}"/><rect x="226" y="78" width="248" height="504" rx="32" fill="{BLU}"/>
<rect x="310" y="92" width="80" height="18" rx="9" fill="{NERO}"/>
<text x="350" y="190" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="800" font-size="64" fill="{BIANCO}">09:41</text>
<rect x="234" y="232" width="232" height="138" rx="22" fill="{BIANCO}"/>
<g transform="translate(248 250) scale(0.066)"><rect width="700" height="460" rx="110" fill="{BLU}"/><polygon points="120,440 120,600 280,440" fill="{BLU}"/><circle cx="220" cy="230" r="46" fill="{BIANCO}"/><circle cx="350" cy="230" r="46" fill="{BIANCO}"/><circle cx="480" cy="230" r="46" fill="{BIANCO}"/></g>
<text x="304" y="275" font-family="Bricolage Grotesque" font-weight="800" font-size="22" fill="{NERO}">Scopri.AI</text>
<text x="452" y="274" text-anchor="end" font-family="Bricolage Grotesque" font-weight="500" font-size="14" fill="#8A877F">ora</text>
<text x="250" y="322" font-family="Bricolage Grotesque" font-weight="700" font-size="21" fill="{NERO}">🔔 Nuovo post:</text>
<text x="250" y="350" font-family="Bricolage Grotesque" font-weight="700" font-size="21" fill="{NERO}">vieni a scoprirlo!</text>
<rect x="234" y="384" width="232" height="80" rx="22" fill="{BIANCO}" opacity=".35"/>
</g>
<g transform="translate(520 120) rotate(18)">
<path d="M0 -60 C 34 -60, 52 -34, 52 0 V 34 L 66 54 H -66 L -52 34 V 0 C -52 -34, -34 -60, 0 -60 Z" fill="{BIANCO}" stroke="{NERO}" stroke-width="8"/>
<circle cx="0" cy="68" r="14" fill="{NERO}"/><circle cx="0" cy="-66" r="8" fill="{NERO}"/>
</g>
<path d="M610 60 L640 40 M630 110 L668 104 M600 20 L610 -6" stroke="{NERO}" stroke-width="8" stroke-linecap="round"/>
<path d="M80 470 l10 28 28 10 -28 10 -10 28 -10 -28 -28 -10 28 -10z" fill="{BLU}"/>
</svg>'''


def chiusura_notifica(s, ctx):
    """Chiusura fissa di tutti i post (scelta il 15/10/2026): lo smartphone con la notifica."""
    titolo = s.get("titolo", "Le novità sull'AI, *appena escono*.")
    righe = s.get("inviti", ["🔔 Segui @scopri__ai e attiva le notifiche", "📌 E salva il post per ritrovarlo"])
    inviti = "".join(
        f'<div style="background:{BLU if i == 0 else BIANCO};color:{BIANCO if i == 0 else NERO};border-radius:28px;padding:22px 30px;'
        f'font-size:38px;font-weight:700">{html.escape(r)}</div>' for i, r in enumerate(righe))
    return ("carta", f'''<div style="align-self:stretch">{logo("carta")}</div>
<div style="align-self:center">{SVG_NOTIFICA}</div>
<div style="font-size:80px;font-weight:800;line-height:1;letter-spacing:-3px;text-align:center">{evidenzia(titolo, "carta")}</div>
<div style="flex:1"></div>
<div style="display:flex;flex-direction:column;gap:14px">{inviti}</div>''')


# Terminatori: l'ultima slide di ogni post. Possono cambiare nel tempo (vedi template/terminatori/).
TERMINATORE_ATTUALE = "notifica"


def chiusura(s, ctx):
    """Usa il terminatore scelto nel JSON ("terminatore": "…") o quello attuale."""
    nome = s.get("terminatore", TERMINATORE_ATTUALE)
    if nome == "calendario":
        return (b_chiusura if ctx.get("stile_b") else slide_chiusura)(s, ctx)
    return chiusura_notifica(s, ctx)


TIPI = {"copertina": slide_copertina, "testo": slide_testo, "prompt": slide_prompt, "chiusura": chiusura}


# ---------- Template B ("fascia"): immagine a tutta larghezza in alto, fascia di colore sotto ----------
GIRO_B = ["blu", "carta", "giallo"]


def evidenzia_b(testo, fondo):
    """Parola chiave: gialla sul blu, riquadro giallo sulla carta, riquadro bianco sul giallo."""
    t = html.escape(testo)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    stile = {"blu": f"color:{GIALLO}",
             "carta": f"background:{GIALLO};padding:0 8px;border-radius:6px",
             "giallo": f"background:{BIANCO};padding:0 8px;border-radius:6px"}[fondo]
    return re.sub(r"\*(.+?)\*", rf'<span style="{stile}">\1</span>', t)


def chip_b(fondo):
    testo, bolla, scritta = (BIANCO, GIALLO, BLU) if fondo == "blu" else (NERO, BLU, BIANCO)
    return (f'<div class="ass logo" style="top:48px;left:56px;display:flex;align-items:center;gap:8px;background:{SFONDO[fondo][0]};color:{testo};'
            f'padding:12px 20px;border-radius:999px;font-size:30px;font-weight:700;letter-spacing:-1px">Scopri{fumetto(bolla, scritta, 40)}</div>')


def visual_b(v, cartella, fondo, altezza):
    """Immagine o video a tutta larghezza in alto, senza angoli arrotondati."""
    if v.get("video"):
        return (f'<div class="sotto ass" id="buco" style="top:0;left:0;width:1080px;height:{altezza}px;'
                f'box-shadow:0 0 0 3000px {SFONDO[fondo][0]}"></div>')
    if v.get("immagine"):
        src = (cartella / v["immagine"]).resolve().as_uri()
        adatta = v.get("adatta", "cover")
        return (f'<div class="ass" style="top:0;left:0;width:1080px;height:{altezza}px;background:{NERO}">'
                f'<img src="{src}" style="width:100%;height:100%;object-fit:{adatta};object-position:{v.get("posizione", "center")};display:block"></div>')
    return ""


def b_copertina(s, ctx):
    rubrica = (f'<div class="ass mono" style="top:56px;right:56px;background:{GIALLO};color:{NERO};padding:12px 20px;border-radius:999px;'
               f'font-size:24px;letter-spacing:1px">{html.escape(ctx["rubrica"])}</div>') if ctx.get("rubrica") else ""
    sotto = f'<div style="font-size:36px;color:{GRIGIO_SU_BLU}">{evidenzia_b(s["sottotitolo"], "blu")}</div>' if s.get("sottotitolo") else ""
    return ("blu", f'''{visual_b(s.get("visual") or {}, ctx["cartella"], "blu", 900)}
{chip_b("blu")}{rubrica}
<div class="ass" style="left:0;right:0;bottom:0;height:450px;box-sizing:border-box;padding:56px 72px 64px;background:{BLU};display:flex;align-items:flex-end;gap:36px">
<div style="flex:1;display:flex;flex-direction:column;gap:22px">
<div style="font-size:{s.get("dimensione", 92)}px;font-weight:800;line-height:1;letter-spacing:-3px">{evidenzia_b(s["titolo"], "blu")}</div>
{sotto}</div>{freccia()}</div>''')


def b_testo(s, ctx):
    fondo = s.get("fondo") or GIRO_B[(ctx["indice"] - 2) % 3]
    fg = SFONDO[fondo][1]
    secondario = GRIGIO_SU_BLU if fondo == "blu" else fg
    corpo = "".join(f'<p style="margin:0">{evidenzia_b(p, fondo)}</p>' for p in s.get("testo", []))
    bolla_bg, bolla_fg = (GIALLO, NERO) if fondo == "blu" else (BLU, BIANCO)
    commento = (f'<div class="ass" style="top:738px;left:72px;background:{bolla_bg};color:{bolla_fg};padding:18px 32px;'
                f'border-radius:32px 32px 32px 6px;font-size:42px;font-weight:700">{html.escape(s["commento"])}</div>') if s.get("commento") else ""
    return (fondo, f'''{visual_b(s.get("visual") or {}, ctx["cartella"], fondo, 780)}
{chip_b(fondo)}
<div class="ass" style="left:0;right:0;top:780px;bottom:0;box-sizing:border-box;padding:92px 72px 64px;background:{SFONDO[fondo][0]};display:flex;flex-direction:column;gap:24px">
<div style="font-size:{s.get("dimensione", 72)}px;font-weight:800;line-height:1.02;letter-spacing:-2.5px">{evidenzia_b(s["titolo"], fondo)}</div>
<div style="display:flex;flex-direction:column;gap:16px;font-size:{s.get("dimensione_testo", 36)}px;line-height:1.35;color:{secondario}">{corpo}</div>
</div>{commento}''')


def b_chiusura(s, ctx):
    rubriche = s.get("rubriche", [["Lun", "Le news AI della settimana"], ["Ven", "Prompt da copiare"],
                                   ["Dom", "Una curiosità di scienza"], ["Extra", "News lampo, quando succede qualcosa"]])
    righe = "".join(
        f'<div style="display:flex;gap:28px;align-items:center;padding:20px 0;border-top:2px solid rgba(18,18,18,.25)">'
        f'<span class="mono" style="flex:none;width:110px;color:{BLU};font-size:30px">{html.escape(g)}</span>'
        f'<span style="font-size:38px;font-weight:500">{html.escape(t)}</span></div>' for g, t in rubriche)
    domanda = s.get("domanda", "Quale ti ha colpito di più?")
    return ("giallo", f'''{logo("carta")}
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:44px">
<div style="align-self:flex-start;background:{BLU};color:{BIANCO};padding:22px 36px;border-radius:40px 40px 40px 8px;font-size:56px;font-weight:700;line-height:1.1">{html.escape(domanda)}</div>
<div style="font-size:44px;line-height:1.3;font-weight:500">{html.escape(s.get("sotto", "Scrivilo nei commenti. Le leggiamo tutte."))}</div>
<div style="margin-top:24px">{righe}</div></div>
<div style="font-size:34px">Segui <b>@scopri__ai</b> e salva il post per ritrovarlo.</div>''')


TIPI_B = {"copertina": b_copertina, "testo": b_testo, "prompt": slide_prompt, "chiusura": chiusura}


def pagina(fondo, contenuto, con_video=False, assoluta=False):
    bg, fg = SFONDO[fondo]
    sfondo = "transparent" if con_video else bg
    disposizione = ("position:relative" if assoluta else "box-sizing:border-box;padding:64px 72px;display:flex;flex-direction:column;gap:40px")
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family={FONT.replace(" ", "+")}:wght@400;500;700;800&amp;family=Space+Grotesk:wght@700&amp;family=JetBrains+Mono:wght@500;700&amp;display=block" rel="stylesheet">
<style>html,body{{margin:0;background:transparent}}.mono{{font-family:'JetBrains Mono',monospace;font-weight:700}}b{{font-weight:700}}
.pagina>*{{position:relative;z-index:1}}.pagina>.sotto{{z-index:0}}.pagina>.ass{{position:absolute}}.logo{{font-family:'Space Grotesk',sans-serif}}</style></head>
<body><div class="pagina" style="width:1080px;height:1350px;{disposizione};background:{sfondo};color:{fg};font-family:'{FONT}',sans-serif;overflow:hidden">
{contenuto}
</div></body></html>'''


def slide_video(html_file, v, fondo, cartella, uscita):
    """Grafica trasparente sopra, video tagliato su misura sotto il "buco"."""
    sopra = html_file.with_suffix(".png")
    out = subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(html_file), str(sopra), "1080", "1350", "trasparente"],
                         check=True, capture_output=True, text=True).stdout
    b = json.loads(out.strip().splitlines()[-1])
    w, h, x, y = (round(b[k]) // 2 * 2 for k in ("width", "height", "x", "y"))
    pos = float(v.get("posizione", 0.5))
    bg = SFONDO[fondo][0].lstrip("#")
    pezzi = v.get("pezzi") or [[v.get("inizio", 0), v.get("inizio", 0) + v["durata"] if v.get("durata") else None]]
    comando = ["ffmpeg", "-loglevel", "error", "-y"]
    for a, b_ in pezzi:
        comando += ["-ss", str(a)] + (["-t", str(b_ - a)] if b_ else []) + ["-i", str(cartella / v["video"])]
    n = len(pezzi)
    unione = "".join(f"[{i}:v]setpts=PTS-STARTPTS,fps=30,setsar=1[p{i}];" for i in range(n)) + "".join(f"[p{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[c];"
    if v.get("adatta") == "contain":  # video intero, con bande scure ai lati (es. video quadrati)
        misura = f"scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color=0x121212"
    else:  # riempie il riquadro tagliando i bordi
        misura = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}:(iw-{w})*{pos}:(ih-{h})/2"
    filtro = (unione + f"[c]{misura},setsar=1[v];"
              f"color=c=0x{bg}:s=1080x1350:r=30[base];[base][v]overlay={x}:{y}:shortest=1[b];"
              f"[b][{n}:v]overlay=0:0:shortest=1,format=yuv420p")
    comando += ["-loop", "1", "-i", str(sopra), "-filter_complex", filtro,
                "-an", "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-movflags", "+faststart", str(uscita)]
    subprocess.run(comando, check=True)
    print("Creato " + str(uscita))


def main():
    argomenti = [a for a in sys.argv[1:] if not a.startswith("--")]
    completi = "--completi" in sys.argv
    solo = next((set(int(n) for n in a.split("=", 1)[1].split(",")) for a in sys.argv if a.startswith("--solo=")), None)
    if len(argomenti) != 1:
        print(__doc__)
        sys.exit(1)
    sys.argv[1] = argomenti[0]
    spec_path = pathlib.Path(sys.argv[1]).resolve()
    cartella = spec_path.parent
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    ctx = {"rubrica": spec.get("rubrica", ""), "cartella": cartella}
    stile_b = spec.get("stile", "A") == "B"
    ctx["stile_b"] = stile_b
    tmp = cartella / ".html"
    tmp.mkdir(exist_ok=True)
    for i, s in enumerate(spec["slides"], 1):
        if solo and i not in solo:
            continue
        ctx["indice"] = i
        tipi = TIPI_B if stile_b else TIPI
        fondo, contenuto = tipi[s["tipo"]](s, ctx)
        v = s.get("visual") or {}
        f = tmp / f"slide-{i:02d}.html"
        assoluta = stile_b and s["tipo"] in ("copertina", "testo")
        f.write_text(pagina(fondo, contenuto, con_video=bool(v.get("video")), assoluta=assoluta), encoding="utf-8")
        for vecchio in (cartella / f"slide-{i:02d}.png", cartella / f"slide-{i:02d}.mp4", cartella / f"slide-{i:02d}-completo.mp4"):
            vecchio.unlink(missing_ok=True)
        if v.get("video"):
            slide_video(f, v, fondo, cartella, cartella / f"slide-{i:02d}.mp4")
            if completi:
                intero = {k: x for k, x in v.items() if k not in ("inizio", "durata", "pezzi")}
                slide_video(f, intero, fondo, cartella, cartella / f"slide-{i:02d}-completo.mp4")
        else:
            subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(f), str(cartella / f"slide-{i:02d}.png"), "1080", "1350"], check=True)
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Genera le slide del template E (Foto a tutta slide) in tre colori di partenza.

Uso: python3 strumenti/varianti-e.py <cartella-bozza>
Scrive nella cartella: E1..E6 (blu), EB1..EB6 (bianco), EG1..EG6 (giallo) in formato .dc.html,
e controlla il contrasto 4.5:1 di ogni coppia testo/sfondo.

PER CAMBIARE PALETTE si tocca solo questo file, in testa:
  - TINTE: come si presenta ogni tinta (sfondo, velo, testo, evidenziatore, fumetto, freccia...);
  - VARIANTI: con che tinta parte la copertina e l'ordine delle tinte delle slide 2-5.
I testi e le immagini stanno in COPERTINA e INTERNE (non cambiano con la palette).
"""
import sys, os, re

# ---------------------------------------------------------------- PALETTE
INK = "#121212"
TINTE = {
    "blu": dict(
        sfondo="radial-gradient(circle at 70% 30%, #4B63FF 0%, #2340FF 45%, #14238F 100%)", base="#2340FF",
        velo="7,16,110", velo_stops=(.97, .9, .45), testo="#FFFFFF", sotto="#EEF1FF",
        ev_sfondo="#FFD84D", ev_testo=INK,                 # evidenziatore
        fum_sfondo="#FFFFFF", fum_testo=INK,               # fumetto
        fre_sfondo="#FFD84D", fre_freccia=INK, fre_ombra=INK,   # freccia tonda
        cerchio="#FFD84D", parola="#FFD84D",               # cerchio dietro la foto, parola gigante
        logo_sfondo="#FFD84D", logo_testo=INK,
        badge_sfondo="rgba(7,16,110,.85)", badge_testo="#FFFFFF", badge_news="#FFD84D",
        pill_sfondo="#FFD84D", pill_testo=INK, pill_ombra=INK),
    "bianco": dict(
        sfondo="radial-gradient(circle at 70% 30%, #FFFFFF 0%, #F4F1EA 50%, #E2DCCB 100%)", base="#F4F1EA",
        velo="244,241,234", velo_stops=(.98, .96, .78), testo=INK, sotto="#2A2A2A",
        ev_sfondo="#FFD84D", ev_testo=INK,
        fum_sfondo="#2340FF", fum_testo="#FFFFFF",
        fre_sfondo="#2340FF", fre_freccia="#FFFFFF", fre_ombra=INK,
        cerchio="#2340FF", parola="#2340FF",
        logo_sfondo="#FFD84D", logo_testo=INK,
        badge_sfondo=INK, badge_testo="#FFFFFF", badge_news="#FFD84D",
        pill_sfondo="#2340FF", pill_testo="#FFFFFF", pill_ombra=INK),
    "giallo": dict(
        sfondo="radial-gradient(circle at 70% 30%, #FFE680 0%, #FFD84D 50%, #F2BC1B 100%)", base="#FFD84D",
        velo="255,216,77", velo_stops=(.98, .96, .78), testo=INK, sotto="#2A2A2A",
        ev_sfondo="#2340FF", ev_testo="#FFFFFF",
        fum_sfondo=INK, fum_testo="#FFD84D",
        fre_sfondo="#2340FF", fre_freccia="#FFFFFF", fre_ombra=INK,
        cerchio="#2340FF", parola="#2340FF",
        logo_sfondo="#FFFFFF", logo_testo=INK,
        badge_sfondo=INK, badge_testo="#FFFFFF", badge_news="#FFD84D",
        pill_sfondo=INK, pill_testo="#FFD84D", pill_ombra="#2340FF"),
}
# prefisso file -> (nome, tinta della copertina, tinte delle slide 2-5)
VARIANTI = {
    "E":  ("blu",    "blu",    ["blu", "blu", "blu", "blu"]),            # l'attuale
    "EB": ("bianco", "bianco", ["blu", "giallo", "blu", "giallo"]),
    "EG": ("giallo", "giallo", ["blu", "bianco", "blu", "giallo"]),
}
# coppie testo/sfondo da controllare (sfondo dietro il testo = velo pieno)
def coppie(t):
    base = "#%02X%02X%02X" % tuple(int(x) for x in t["velo"].split(","))
    return [("testo/velo", t["testo"], base), ("sotto/velo", t["sotto"], base),
            ("parola/velo", t["parola"], base), ("evidenziatore", t["ev_testo"], t["ev_sfondo"]),
            ("fumetto", t["fum_testo"], t["fum_sfondo"]), ("freccia", t["fre_freccia"], t["fre_sfondo"]),
            ("logo", t["logo_testo"], t["logo_sfondo"]), ("pillola Scorri", t["pill_testo"], t["pill_sfondo"]),
            ("etichetta", t["badge_testo"], "#121212" if t["badge_sfondo"] == INK else "#07106E"),
            ("etichetta NEWS", t["badge_news"], "#121212" if t["badge_sfondo"] == INK else "#07106E")]

# ---------------------------------------------------------------- CONTENUTI
DESK = ("img/PersonalApps_desktop_16x9_Static.png", "Google AI Studio che crea un'app, con la scritta Google Play")
MOB = ("img/PersonalApps_mobile_1X1_Static.png", "Lo smartphone con la libreria personale di Google Play")
COPERTINA = dict(cerchio=(120, 90, 840), img=DESK, pos=(-160, 250, 1400, 788))
# n, titolo [(testo, evidenziato)], dimensione, sotto, fumetto, parola gigante, cerchio (x,y,d), immagine, posizione
INTERNE = [
    dict(n=2, h=[("Ha trasformato una ", 0), ("descrizione", 1), (" in un'app", 0)], fs=74,
         p="Hai un'idea? La scrivi in Google AI Studio e l'AI costruisce l'app per te, senza che tu debba programmare.",
         fum="Solo a parole.", parola=None, cerchio=(520, 120, 800), img=DESK, pos=(-1050, 40, 2100, 1181)),
    dict(n=3, h=[("Ha messo l'app sul tuo ", 0), ("telefono", 1)], fs=74,
         p="L'app arriva in una sezione privata di Google Play: la vedi e la installi solo tu. Google non la controlla.",
         fum="Solo tua.", parola=None, cerchio=(-300, 350, 760), img=MOB, pos=(-480, -40, 1700, 1700)),
    dict(n=4, h=[("Per ora è solo per ", 0), ("maggiorenni negli USA", 1)], fs=64,
         p="All'inizio possono provarla soltanto gli adulti che vivono negli Stati Uniti. Per l'Italia non c'è ancora una data.",
         fum="Poi tocca a noi.", parola="18+ · USA", logo_bianco=True, cerchio=(-300, -100, 800), img=DESK, pos=(-2120, 140, 3648, 2052)),
    dict(n=5, h=[("Presto potrai ", 0), ("condividerla", 1), (" con gli amici", 0)], fs=64,
         p="Google dice che la condivisione arriva nei prossimi mesi. Una data precisa non c'è ancora.",
         fum="Nei prossimi mesi.", parola="Presto", cerchio=(620, -200, 800), img=MOB, pos=(-324, -50, 1728, 1728)),
]

# ---------------------------------------------------------------- COSTRUZIONE
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&amp;family=Inter+Tight:'
         'wght@200;400;500;600;700;800&amp;family=JetBrains+Mono:wght@500;700&amp;display=swap" rel="stylesheet">')
LOGO = ('<svg width="40" height="35" viewBox="0 0 700 600" aria-hidden="true"><rect width="700" height="460" rx="110" fill="#2340FF"></rect>'
        '<polygon points="120,440 120,600 280,440" fill="#2340FF"></polygon><text x="350" y="235" text-anchor="middle" '
        'dominant-baseline="central" font-family="Space Grotesk" font-weight="700" font-size="290" fill="#FFFFFF">AI</text></svg>')
def freccia(col, w=40, sw=5):
    return (f'<svg width="{w}" height="{w}" viewBox="0 0 44 44" aria-hidden="true"><path d="M6 22h30M24 10l12 12-12 12" fill="none" '
            f'stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"></path></svg>')
def ev(t, s, pad, rad):
    return (f'<span style="background:{t["ev_sfondo"]};color:{t["ev_testo"]};padding:0 {pad}px;border-radius:{rad}px;'
            f'-webkit-box-decoration-break:clone;box-decoration-break:clone">{s}</span>')

def fondo(t, cerchio, img, pos, logo=None):
    x, y, d = cerchio; src, alt = img; ix, iy, iw, ih = pos
    a, b, c = [("%g" % q).lstrip("0") for q in t["velo_stops"]]; v = t["velo"]
    return (f'<div style="position:absolute;left:0;top:0;width:1080px;height:1350px;overflow:hidden;background:{t["sfondo"]}">'
            f'<div style="position:absolute;left:{x}px;top:{y}px;width:{d}px;height:{d}px;border-radius:50%;background:{t["cerchio"]}"></div>'
            f'<img src="{src}" alt="{alt}" style="display:block;position:absolute;left:{ix}px;top:{iy}px;width:{iw}px;height:{ih}px;transform:rotate(0deg)"></div>'
            f'<div style="position:absolute;left:0;top:0;width:1080px;height:1350px;background:linear-gradient(to top, rgba({v},{a}) 0%, rgba({v},{b}) 34%, rgba({v},{c}) 58%, rgba({v},0) 78%)"></div>'
            f'<div style="position:absolute;top:48px;left:56px;display:flex;background:{logo or t["logo_sfondo"]};padding:12px 22px;border-radius:999px">'
            f'<div style="display:flex;align-items:center;gap:8px;font-size:30px;font-weight:700;letter-spacing:-1px;font-family:\'Space Grotesk\',sans-serif;color:{t["logo_testo"]};">Scopri{LOGO}</div></div>')

def pagina(titolo, corpo, fonts=FONTS):
    return f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>{titolo}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{fonts}
<style>body{{margin:0}}</style>
</helmet>
{corpo}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''

def cornice(t, dentro):
    return (f'<div style="width:1080px;height:1350px;position:relative;overflow:hidden;background:{t["base"]};color:{t["testo"]};'
            f'font-family:\'Inter Tight\',sans-serif;">{dentro}</div>')

def copertina(t):
    c = COPERTINA
    h = (f'E se esistesse {ev(t, "un&#39;app fatta apposta per te", 12, 12)}?').replace("&#39;", "'")
    dentro = (fondo(t, c["cerchio"], c["img"], c["pos"]) +
        f'<div style="position:absolute;top:60px;right:56px;font-family:\'JetBrains Mono\',monospace;font-weight:700;font-size:26px;color:{t["badge_news"]};letter-spacing:1px;background:{t["badge_sfondo"]};padding:10px 22px;border-radius:999px">NEWS LAMPO</div>'
        f'<div style="position:absolute;left:64px;right:64px;bottom:64px"><h1 style="margin:0;font-size:104px;font-weight:800;line-height:1.2;letter-spacing:-4px">{h}</h1>'
        f'<p style="margin:26px 0 0;font-size:38px;line-height:1.25;color:{t["sotto"]};font-weight:500;width:640px">Google Play ora ci prova. Per ora solo negli USA.</p></div>'
        f'<div style="display:flex;align-items:center;gap:12px;height:96px;box-sizing:border-box;padding:0 30px 0 36px;border-radius:999px;background:{t["pill_sfondo"]};color:{t["pill_testo"]};font-size:38px;font-weight:800;letter-spacing:-1px;position:absolute;right:64px;bottom:64px;box-shadow:8px 8px 0 {t["pill_ombra"]}">Scorri{freccia(t["pill_testo"])}</div>')
    return cornice(t, dentro)

def interna(t, s):
    h = "".join(ev(t, x, 10, 10) if e else x for x, e in s["h"])
    parola = (f'<div style="font-size:150px;font-weight:800;letter-spacing:-6px;line-height:.9;color:{t["parola"]};margin-bottom:12px">{s["parola"]}</div>' if s["parola"] else "")
    logo = "#FFFFFF" if s.get("logo_bianco") and t["logo_sfondo"] == t["cerchio"] else None
    dentro = (fondo(t, s["cerchio"], s["img"], s["pos"], logo) +
        f'<div style="position:absolute;top:60px;right:56px;background:{t["badge_sfondo"]};padding:10px 22px;border-radius:999px"><div style="font-family:\'JetBrains Mono\',monospace;font-weight:700;font-size:26px;color:{t["badge_testo"]};letter-spacing:1px">0{s["n"]}/06</div></div>'
        f'<div style="position:absolute;left:64px;right:64px;bottom:64px">{parola}<h2 style="margin:0;font-size:{s["fs"]}px;font-weight:800;line-height:1.04;letter-spacing:-2.5px">{h}</h2>'
        f'<p style="margin:22px 0 0;font-size:33px;line-height:1.28;font-weight:500;color:{t["sotto"]};width:900px">{s["p"]}</p>'
        f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:28px"><div style="background:{t["fum_sfondo"]};color:{t["fum_testo"]};padding:16px 30px;border-radius:30px 30px 30px 6px;font-size:40px;font-weight:700;white-space:nowrap;">{s["fum"]}</div>'
        f'<div style="width:112px;height:112px;border-radius:50%;background:{t["fre_sfondo"]};display:flex;align-items:center;justify-content:center;box-shadow:6px 6px 0 {t["fre_ombra"]}">{freccia(t["fre_freccia"], 56)}</div></div></div>')
    return cornice(t, dentro)

# ---------------------------------------------------------------- CONTRASTO
def lum(h):
    h = h.lstrip("#"); r, g, b = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def contrasto(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True); return (x + .05) / (y + .05)

def main(cartella):
    ok = True
    for nome, t in TINTE.items():
        for etichetta, a, b in coppie(t):
            c = contrasto(a, b)
            if c < 4.5: ok = False
            print(f"  {nome:7s} {etichetta:15s} {a} su {b}: {c:.1f}:1 {'OK' if c >= 4.5 else 'TROPPO BASSO'}")
    chiusura = open(os.path.join(cartella, "E6-chiusura.dc.html"), encoding="utf-8").read() if os.path.exists(os.path.join(cartella, "E6-chiusura.dc.html")) else None
    for pre, (colore, tc, interni) in VARIANTI.items():
        ordine = [tc] + interni
        nomi = ["copertina", "app", "telefono", "usa-18", "condivisione"]
        titoli = ["Copertina", "app", "telefono", "usa-18", "condivisione"]
        corpi = [copertina(TINTE[tc])] + [interna(TINTE[ordine[i + 1]], s) for i, s in enumerate(INTERNE)]
        for i, corpo in enumerate(corpi):
            open(os.path.join(cartella, f"{pre}{i+1}-{nomi[i]}.dc.html"), "w", encoding="utf-8").write(pagina(f"{pre}{i+1} {titoli[i]}", corpo))
        if chiusura and pre != "E":
            c = chiusura.replace("<title>E6 Chiusura</title>", f"<title>{pre}6 Chiusura</title>")
            open(os.path.join(cartella, f"{pre}6-chiusura.dc.html"), "w", encoding="utf-8").write(c)
    print("contrasti:", "tutti OK" if ok else "ATTENZIONE")

if __name__ == "__main__":
    main(sys.argv[1])

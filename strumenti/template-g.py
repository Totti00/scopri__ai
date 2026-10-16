#!/usr/bin/env python3
"""Crea il template G · Electric (schizzo del 16/10/2026) in template/G-electric/.

Uso:
    python3 strumenti/template-g.py          # rifà i 6 .dc.html e anteprima.png

Da dove viene: il design system "Electric Mono" mandato dal proprietario (in inglese, in
ispirazione/electric-mono.md), ADATTATO a Scopri.AI:
- tre fondi che si alternano: SCURO (quasi nero), CHIARO (la nostra carta) e ACCENTO (il nostro blu #2340FF);
- accento: il nostro blu sul chiaro, il nostro giallo sullo scuro e sul blu (niente viola né lilla, vedi brand/identita.md);
- foto e video VERI (regola 4), ma in bianco e nero con la luce blu dietro: è il "monocromo" di Electric Mono;
- cornice fissa: fumetto del logo in alto a sinistra, contatore "02 / 06" in alto a destra,
  @scopri__ai in basso a sinistra, freccia in basso a destra (sulla copertina la pillola "Scorri →", sull'ultima niente);
- grana fine e sfumature su tutti i fondi; un "filo" giallo/blu che passa da una slide all'altra alla stessa altezza;
- font: Inter Tight (il font di Electric Mono, scelto per tutti i post il 16/10/2026; anche sottile, 200, per i numeri giganti) e JetBrains Mono per le scritte piccole;
- la chiusura è il nostro terminatore (la notifica) rifatto in stile Electric, con un solo invito.
Testi e immagini: quelli del post Google Play (15/10/2026), come gli altri template.
"""
import pathlib
import subprocess

RADICE = pathlib.Path(__file__).resolve().parent.parent
CARTELLA = RADICE / "template/G-electric"

INK, BLU, GIALLO, CARTA, SNOW, BIANCO = "#0A0A0D", "#2340FF", "#FFD84D", "#F4F1EA", "#F5F5F7", "#FFFFFF"
GRIGIO_SCURO_TESTO, GRIGIO_SCURO_META, GRIGIO_CHIARO = "#A1A1AC", "#8B8B97", "#55565C"
TOTALE = 6

MODI = {
    # fondo, testo principale, testo secondario, meta, accento parole, filo, grana
    "D": dict(bg=f"radial-gradient(80% 60% at var(--hx,70%) var(--hy,70%), #16204F 0%, transparent 70%),"
                 f"radial-gradient(120% 100% at 50% 50%, transparent 60%, rgba(0,0,0,.45) 100%), {INK}",
              fg=SNOW, body=GRIGIO_SCURO_TESTO, meta=GRIGIO_SCURO_META, acc=GIALLO, filo=GIALLO, grana=(.07, "overlay"),
              anello="rgba(245,245,247,.3)"),
    "L": dict(bg="radial-gradient(70% 50% at 10% 0%, rgba(255,255,255,.9) 0%, transparent 70%),"
                 "linear-gradient(160deg, #F8F6F0 0%, #F4F1EA 55%, #E9E4D8 100%)",
              fg=INK, body=GRIGIO_CHIARO, meta=GRIGIO_CHIARO, acc=BLU, filo=BLU, grana=(.05, "multiply"),
              anello="rgba(10,10,13,.3)"),
    "A": dict(bg="radial-gradient(70% 50% at 10% 0%, rgba(255,255,255,.14) 0%, transparent 70%),"
                 "linear-gradient(150deg, #3F58FF 0%, #2340FF 45%, #1529C9 100%)",
              fg=BIANCO, body=BIANCO, meta=BIANCO, acc=GIALLO, filo=GIALLO, grana=(.08, "overlay"),
              anello="rgba(255,255,255,.4)"),
}


def fumetto(colore, scritta, larghezza, testo="AI"):
    return (f'<svg width="{larghezza}" height="{larghezza * 6 // 7}" viewBox="0 0 700 600" aria-hidden="true">'
            f'<rect width="700" height="460" rx="110" fill="{colore}"></rect><polygon points="120,440 120,600 280,440" fill="{colore}"></polygon>'
            f'<text x="350" y="235" text-anchor="middle" dominant-baseline="central" font-family="Space Grotesk" font-weight="700" '
            f'font-size="290" fill="{scritta}">{testo}</text></svg>')


def acc(testo, m):
    """*parola* → parola chiave nel colore d'accento del fondo."""
    import re
    return re.sub(r"\*(.+?)\*", rf'<span style="color:{MODI[m]["acc"]}">\1</span>', testo)


def grana(m):
    op, blend = MODI[m]["grana"]
    return (f'<svg width="1080" height="1350" style="position:absolute;left:0;top:0;pointer-events:none;opacity:{op};mix-blend-mode:{blend}" aria-hidden="true">'
            f'<filter id="grana{m}"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch"></feTurbulence>'
            f'<feColorMatrix type="saturate" values="0"></feColorMatrix></filter><rect width="1080" height="1350" filter="url(#grana{m})"></rect></svg>')


def cornice(m, n, copertina=False, ultima=False):
    d = MODI[m]
    logo_bolla, logo_ai = (BLU, BIANCO) if m == "L" else (GIALLO, BLU) if m == "D" else (BIANCO, BLU)
    pezzi = [f'<div style="position:absolute;left:96px;top:96px">{fumetto(logo_bolla, logo_ai, 47)}</div>',
             f'<div style="position:absolute;right:96px;top:102px;font-family:\'JetBrains Mono\',monospace;font-weight:500;font-size:22px;letter-spacing:.08em;color:{d["meta"]}">'
             f'<span style="color:{d["fg"]}">{n:02d}</span> / {TOTALE:02d}</div>',
             f'<div style="position:absolute;left:96px;top:1216px;font-family:\'JetBrains Mono\',monospace;font-weight:500;font-size:22px;letter-spacing:.04em;color:{d["meta"]}">@scopri__ai</div>']
    freccia = '<svg width="26" height="26" viewBox="0 0 44 44" aria-hidden="true"><path d="M6 22h30M24 10l12 12-12 12" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
    if copertina:
        pezzi.append(f'<div style="position:absolute;right:96px;top:1196px;height:60px;display:flex;align-items:center;gap:12px;padding:0 26px 0 30px;border-radius:999px;'
                     f'background:{GIALLO};color:{INK};font-size:28px;font-weight:800;letter-spacing:-.5px">Scorri{freccia.format(c=INK)}</div>')
    elif not ultima:
        pezzi.append(f'<div style="position:absolute;right:96px;top:1198px;width:56px;height:56px;box-sizing:border-box;border-radius:50%;border:2px solid {d["anello"]};'
                     f'display:flex;align-items:center;justify-content:center">{freccia.format(c=d["fg"])}</div>')
    return "".join(pezzi)


def filo(m, percorso, nodi=()):
    c = MODI[m]["filo"]
    alone = f'<path d="{percorso}" fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round" opacity=".25" style="filter:blur(6px)"></path>' if m != "L" else ""
    puntini = "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}"></circle>' for x, y in nodi)
    return (f'<svg width="1080" height="1350" style="position:absolute;left:0;top:0" aria-hidden="true">{alone}'
            f'<path d="{percorso}" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path>{puntini}</svg>')


def pillola(m, testo):
    if m == "D":
        st, dot, col = f"background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.14)", GIALLO, SNOW
    elif m == "L":
        st, dot, col = f"background:{INK}", GIALLO, SNOW
    else:
        st, dot, col = f"background:{BIANCO}", BLU, BLU
    return (f'<div style="position:absolute;left:96px;top:192px;height:48px;box-sizing:border-box;padding:0 22px;border-radius:999px;{st};'
            f'display:flex;align-items:center;gap:12px;font-family:\'JetBrains Mono\',monospace;font-weight:500;font-size:20px;letter-spacing:.08em;color:{col}">'
            f'<span style="width:10px;height:10px;border-radius:50%;background:{dot}"></span>{testo}</div>')


def adesivo(testo, left, top, ruota=-4, sfondo=GIALLO, colore=INK):
    """Il nostro commento di 2-3 parole, come adesivo (lo "sticker" di Electric)."""
    return (f'<div style="position:absolute;left:{left}px;top:{top}px;transform:rotate({ruota}deg);background:{sfondo};color:{colore};'
            f'padding:16px 28px;border-radius:999px;font-size:38px;font-weight:800;letter-spacing:-1px;white-space:nowrap;'
            f'box-shadow:0 20px 40px -12px rgba(0,0,0,.45)">{testo}</div>')


def luce(x, y, d=900, colore="rgba(35,64,255,.55)", nucleo="rgba(77,104,255,.5)"):
    return (f'<div style="position:absolute;left:{x - d // 2}px;top:{y - d // 2}px;width:{d}px;height:{d}px;border-radius:50%;'
            f'background:radial-gradient(circle, {colore} 0%, transparent 60%)"></div>'
            f'<div style="position:absolute;left:{x - 160}px;top:{y - 160}px;width:320px;height:320px;border-radius:50%;'
            f'background:radial-gradient(circle, {nucleo} 0%, transparent 70%)"></div>')


def foto(src, left, top, width, alt, extra=""):
    """Foto vera in bianco e nero (monocromo Electric): resta vera, ma con un look più pulito."""
    return (f'<img src="img/{src}" alt="{alt}" style="position:absolute;left:{left}px;top:{top}px;width:{width}px;display:block;'
            f'filter:grayscale(1) contrast(1.12) brightness(1.04){extra}">')


def pagina(titolo, m, corpo, hx="70%", hy="70%"):
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
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&amp;family=Inter+Tight:wght@200;400;500;600;700;800&amp;family=JetBrains+Mono:wght@500;700&amp;display=swap" rel="stylesheet">
<style>body{{margin:0}}</style>
</helmet>
<div style="width:1080px;height:1350px;position:relative;overflow:hidden;--hx:{hx};--hy:{hy};background:{MODI[m]["bg"]};color:{MODI[m]["fg"]};font-family:'Inter Tight',sans-serif">
{corpo}
{grana(m)}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''


def h(testo, m, size, top, width, left=96, peso=700, lh=1.0, ls=-.035, extra=""):
    return (f'<h2 style="position:absolute;left:{left}px;top:{top}px;width:{width}px;margin:0;font-size:{size}px;font-weight:{peso};'
            f'line-height:{lh};letter-spacing:{ls}em{extra}">{acc(testo, m)}</h2>')


def p(testo, m, top, width, left=96, size=30, extra=""):
    return (f'<p style="position:absolute;left:{left}px;top:{top}px;width:{width}px;margin:0;font-size:{size}px;font-weight:400;'
            f'line-height:1.38;color:{MODI[m]["body"]}{extra}">{testo}</p>')


def slide1():
    m = "D"
    corpo = (
        f'<div style="position:absolute;left:300px;top:520px;font-size:620px;font-weight:800;letter-spacing:-.05em;line-height:.8;color:rgba(255,255,255,.05)">APP</div>'
        + luce(840, 920)
        + foto("PersonalApps_mobile_1X1_Static.png", 560, 650, 560, "Il telefono con la libreria privata di Google Play, con le app create da una persona",
               ";transform:rotate(8deg)")
        + filo(m, "M 780 1140 L 1080 1140", nodi=[(780, 1140)])
        + pillola(m, "NEWS LAMPO")
        + h("E se esistesse un'app *fatta apposta per te*?", m, 120, 288, 888, peso=700, lh=.95, ls=-.045)
        + p("Google Play ora ci prova. Per ora solo negli USA.", m, 1010, 360, size=32)
        + cornice(m, 1, copertina=True))
    return pagina("G1 · Copertina", m, corpo, hx="78%", hy="70%")


def slide2():
    m = "L"
    corpo = (
        '<div style="position:absolute;left:300px;top:640px;width:820px;height:60px;border-radius:50%;background:rgba(10,10,13,.28);filter:blur(36px)"></div>'
        + foto("PersonalApps_desktop_16x9_Static.png", 150, 170, 1100, "Il computer con Google AI Studio che sta creando un'app")
        + adesivo("Solo a parole.", 120, 640, ruota=-4)
        + filo(m, "M 0 1140 L 1080 1140")
        + h("Ha trasformato una *descrizione* in un'app", m, 88, 772, 820, lh=1.0)
        + p("La scrivi in Google AI Studio e l'AI costruisce l'app. Senza programmare.", m, 1010, 700, size=30)
        + cornice(m, 2))
    return pagina("G2 · App", m, corpo)


def slide3():
    m = "D"
    corpo = (
        luce(820, 930, d=820)
        + foto("PersonalApps_mobile_1X1_Static.png", 600, 620, 560, "La sezione privata di Google Play con le proprie app", ";transform:rotate(-6deg)")
        + adesivo("Solo tua.", 560, 1040, ruota=-5)
        + filo(m, "M 0 1140 C 160 1140, 200 940, 360 940 L 1080 940", nodi=[(360, 940)])
        + pillola(m, "GOOGLE PLAY")
        + h("Ha messo l'app sul tuo *telefono*", m, 96, 288, 736)
        + p("Arriva in una sezione privata: la vedi e la installi solo tu. Google non la controlla.", m, 616, 508)
        + cornice(m, 3))
    return pagina("G3 · Telefono", m, corpo, hx="76%", hy="70%")


def slide4():
    m = "A"
    punti = []
    for r in range(6):
        for c in range(14):
            x, y = 110 + c * 62, 900 + r * 40
            accesi = {(1, 2), (1, 3), (2, 2), (2, 3), (2, 4), (3, 3)}
            col = GIALLO if (r, c) in accesi else "rgba(255,255,255,.24)"
            punti.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{col}"></circle>')
    corpo = (
        luce(330, 470, d=900, colore="rgba(255,255,255,.18)", nucleo="rgba(255,255,255,.3)")
        + f'<svg width="1080" height="1350" style="position:absolute;left:0;top:0" aria-hidden="true">{"".join(punti)}</svg>'
        + filo(m, "M 0 940 L 60 940 Q 84 940 84 964 L 84 1126 Q 84 1150 108 1150 L 1080 1150")
        + pillola(m, "PER ORA")
        + f'<div style="position:absolute;left:84px;top:262px;font-size:400px;font-weight:200;line-height:.85;letter-spacing:-.06em;color:{BIANCO}">18<span style="color:{GIALLO}">+</span></div>'
        + h("Solo maggiorenni negli *USA*", m, 64, 640, 700, lh=1.05, ls=-.025)
        + p("Per l'Italia non c'è ancora una data.", m, 790, 600)
        + adesivo("Poi tocca a noi.", 600, 1030, ruota=4, sfondo=BIANCO, colore=BLU)
        + cornice(m, 4))
    return pagina("G4 · 18+ USA", m, corpo)


def slide5():
    m = "L"
    corpo = (
        f'<div style="position:absolute;left:560px;top:820px;width:1300px;height:1300px;border-radius:50%;background:{BLU}"></div>'
        + adesivo("Nei prossimi mesi.", 600, 960, ruota=-4)
        + filo(m, "M 0 1150 L 560 1150 Q 600 1150 630 1120 L 650 1100 L 676 1100")
+ '<svg width="1080" height="1350" style="position:absolute;left:0;top:0" aria-hidden="true"><path d="M 676 1100 L 1080 1100" stroke="#FFD84D" stroke-width="3" stroke-linecap="round"></path></svg>'
        + h("Presto potrai *condividerla* con gli amici.", m, 128, 288, 888, lh=.95, ls=-.045)
        + p("Google dice: nei prossimi mesi. Una data precisa non c'è ancora.", m, 820, 440, size=30)
        + cornice(m, 5))
    return pagina("G5 · Condivisione", m, corpo)


def slide6():
    m = "D"
    carta = (f'<div style="position:absolute;left:360px;top:230px;width:360px;height:560px;border-radius:56px;background:#121218;border:2px solid rgba(255,255,255,.12)">'
             f'<div style="position:absolute;left:150px;top:22px;width:60px;height:14px;border-radius:7px;background:#2A2A33"></div>'
             f'<div style="position:absolute;left:0;right:0;top:90px;text-align:center;font-size:72px;font-weight:200;letter-spacing:-.04em;color:{SNOW}">09:41</div>'
             f'<div style="position:absolute;left:24px;right:24px;top:220px;padding:22px;border-radius:28px;background:linear-gradient(180deg,#17171F 0%,#101015 100%);'
             f'border:2px solid rgba(255,255,255,.08);box-shadow:0 40px 120px -20px rgba(35,64,255,.6)">'
             f'<div style="display:flex;align-items:center;gap:12px">{fumetto(BLU, BIANCO, 42, "•••")}'
             f'<span style="font-size:24px;font-weight:700;color:{SNOW}">Scopri.AI</span><span style="margin-left:auto;font-family:\'JetBrains Mono\',monospace;font-size:18px;color:{GRIGIO_SCURO_META}">ora</span></div>'
             f'<div style="margin-top:14px;font-size:24px;line-height:1.3;color:{GRIGIO_SCURO_TESTO}">🔔 Nuovo post: vieni a scoprirlo!</div></div>'
             f'<div style="position:absolute;left:24px;right:24px;top:380px;height:90px;border-radius:28px;background:#17171F;opacity:.6"></div></div>')
    corpo = (
        luce(540, 470, d=1000)
        + carta
        + filo(m, "M 0 1100 C 120 1100, 160 1072, 236 1072", nodi=[(236, 1072)])
        + f'<h2 style="position:absolute;left:96px;right:96px;top:820px;margin:0;text-align:center;font-size:84px;font-weight:700;line-height:1;letter-spacing:-.035em">'
          f'{acc("Le novità sull&#39;AI, *appena escono*.", m)}</h2>'
        + f'<div style="position:absolute;left:0;right:0;top:1040px;display:flex;justify-content:center"><div style="height:64px;display:flex;align-items:center;padding:0 34px;border-radius:999px;'
          f'background:{GIALLO};color:{INK};font-size:30px;font-weight:800;letter-spacing:-.5px">📩 Mandalo a chi ha sempre un\'idea</div></div>'
        + cornice(m, 6, ultima=True))
    return pagina("G6 · Chiusura", m, corpo, hx="50%", hy="35%")


def main():
    CARTELLA.mkdir(parents=True, exist_ok=True)
    nomi = ["copertina", "slide", "slide-telefono", "slide-numero", "slide-manifesto", "chiusura"]
    files = []
    for nome, fn in zip(nomi, [slide1, slide2, slide3, slide4, slide5, slide6]):
        f = CARTELLA / f"{nome}.dc.html"
        f.write_text(fn(), encoding="utf-8")
        files.append(f)
    (CARTELLA / "COLORE.txt").write_text("colore di partenza: scuro (fondi che si alternano: scuro, chiaro, scuro, blu, chiaro, scuro)\n", encoding="utf-8")
    # anteprima: le 6 slide affiancate in fila, come un'unica striscia (si vede il filo che passa)
    tmp = CARTELLA / ".anteprima"
    tmp.mkdir(exist_ok=True)
    pngs = []
    for i, f in enumerate(files):
        png = tmp / f"{i}.png"
        subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(f), str(png), "1080", "1350"], check=True, stdout=subprocess.DEVNULL)
        pngs.append(png)
    imgs = "".join(f'<img src="file://{x}" style="width:360px;height:450px;display:block">' for x in pngs)
    pag = tmp / "striscia.html"
    pag.write_text(f'<body style="margin:0;display:flex;width:2160px;background:#000">{imgs}</body>')
    subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(pag), str(CARTELLA / "anteprima.png"), "2160", "450"], check=True, stdout=subprocess.DEVNULL)
    for x in tmp.iterdir():
        x.unlink()
    tmp.rmdir()
    print("Creato", CARTELLA)


if __name__ == "__main__":
    main()

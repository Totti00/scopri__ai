#!/usr/bin/env python3
"""Bozza Tesla Roadster (16/10/2026): righe A-F in .dc.html, colore di partenza giallo, chiusura blu.
Disegni ricalcati dai template di template/<X>-giallo (stessi ruoli colore di varianti-colori.py / varianti-e.py)."""
import json, os, re, shutil, sys, html as H

POST = "/home/user/scopri__ai/archivio/2026-10-16-news-lampo-tesla-roadster"
BOZZA = POST + "/bozza"
REPO = "/home/user/scopri__ai"
os.makedirs(BOZZA + "/img", exist_ok=True)

BLU, GIALLO, CARTA, NERO, BIANCO, BLU_S = "#2340FF", "#FFD84D", "#F4F1EA", "#121212", "#FFFFFF", "#1A30C4"
P = {
    "blu": dict(page=BLU, ink=BIANCO, sub="#DDE3FF", hl=(GIALLO, NERO), fum=(GIALLO, NERO), logo=(GIALLO, BLU), acc=GIALLO,
                parola=GIALLO, box=(GIALLO, NERO), bar_on=GIALLO, bar_off="rgba(255,255,255,.3)", grid="rgba(255,255,255,.1)",
                vis=BLU_S, label=GIALLO, pill=(GIALLO, NERO), stella=BIANCO, num=(GIALLO, NERO)),
    "carta": dict(page=CARTA, ink=NERO, sub="#2A2A2A", hl=(GIALLO, NERO), fum=(BLU, BIANCO), logo=(BLU, BIANCO), acc=GIALLO,
                  parola=BLU, box=(BLU, BIANCO), bar_on=BLU, bar_off="rgba(18,18,18,.15)", grid="rgba(35,64,255,.09)",
                  vis=NERO, label=BLU, pill=(BLU, BIANCO), stella=BLU, num=(BLU, BIANCO)),
    "giallo": dict(page=GIALLO, ink=NERO, sub="#2A2A2A", hl=(BLU, BIANCO), fum=(BLU, BIANCO), logo=(BLU, BIANCO), acc=BLU,
                   parola=BLU, box=(BLU, BIANCO), bar_on=BLU, bar_off="rgba(18,18,18,.15)", grid="rgba(18,18,18,.09)",
                   vis=NERO, label=NERO, pill=(BLU, BIANCO), stella=BLU, num=(BLU, BIANCO)),
}
# tinte delle 7 slide di contenuto (copertina + 5 interne + In breve) con partenza gialla; chiusura blu
RITMO = {"AF": ["giallo", "blu", "carta", "blu", "giallo", "carta", "giallo"],
         "BCD": ["giallo", "carta", "blu", "giallo", "carta", "blu", "giallo"]}
RITMO["E"] = RITMO["AF"]
TOT = 8

# ---------------------------------------------------------------- contenuti
IMG = {  # nome: (file, alt, posizione x% y% per object-position, rapporto)
    "camion": ("roadster1-capriola-camion.png", "La Tesla Roadster a testa in giù in aria, sopra il tetto di un camion, con un getto d'aria acceso", (52, 38), 1920 / 1080),
    "semi": ("roadster2-capriola-semi.png", "La Tesla Roadster fa una capriola sopra un camion Tesla Semi, tra le scie dei getti d'aria", (74, 55), 1398 / 782),
    "rampa": ("roadster2-rampa.png", "La Tesla Roadster ferma a testa in giù su una rampa curva a forma di C", (72, 50), 1398 / 782),
    "getti": ("roadster1-getti-sopra-auto.png", "La Tesla Roadster sospesa in aria con quattro getti verso il basso, vicino alle auto parcheggiate", (12, 52), 1920 / 1080),
    "derapata": ("roadster2-derapata.png", "La Tesla Roadster vista dall'alto mentre derapa, con i getti d'aria accesi", (52, 42), 1398 / 782),
    "sospesa": ("roadster2-sospesa.png", "La Tesla Roadster sollevata da terra da due getti d'aria, di notte", (50, 40), 1398 / 782),
}
for f, *_ in IMG.values():
    shutil.copy(f"{POST}/media/{f}", f"{BOZZA}/img/{f}")

COPERTINE = {
    "": dict(titolo="*10 getti d'aria* da razzo: guarda cosa fa la nuova Tesla", sotto="", img="camion", gigante="10"),
    "-titolo-a": dict(titolo="Un'auto *senza nessuno a bordo* ha fatto una capriola in aria", sotto="", img="camion", gigante="!"),
    "-titolo-b": dict(titolo="È un'auto *o un razzo*?", sotto="Guarda la nuova Tesla Roadster.", img="camion", gigante="?"),
    "-video-2": dict(titolo="*10 getti d'aria* da razzo: guarda cosa fa la nuova Tesla", sotto="", img="semi", gigante="10"),
}
INTERNE = [
    dict(n=2, tema="capriola", titolo="Ha fatto una *capriola* sopra un camion",
         testo="È la nuova Tesla Roadster, spinta da 10 getti d'aria compressa.", fum="Nessuno a bordo.", img="semi",
         gigante="HOP!", icona="giro"),
    dict(n=3, tema="testa-in-giu", titolo="Si è fermata *a testa in giù*",
         testo="Su una rampa a forma di C. Delle ventole aspirano l'aria sotto l'auto e la tengono incollata.",
         fum="Come una ventosa.", img="rampa", gigante="180°", icona="giu"),
    dict(n=4, tema="getti", titolo="È scesa piano *con i getti* accesi",
         testo="Dopo il salto sopra le auto parcheggiate, i getti l'hanno tenuta in aria per farla scendere piano.",
         fum="Atterraggio morbido.", img="getti", gigante="PIANO", icona="getti"),
    dict(n=5, tema="derapata", titolo="Ha derapato *spinta dall'aria*",
         testo="I getti usano aria compressa chiusa in bombole, con una tecnica presa dai razzi di SpaceX.",
         fum="Come un razzo.", img="derapata", gigante="×10", icona="vento"),
    dict(n=6, tema="2028", titolo="Per ora è solo uno *spettacolo*",
         testo="Era una prova su una pista di SpaceX, in Texas. La versione con i getti si prenota con 250.000 dollari.",
         fum="Non per strada.", img="sospesa", numero="2028", didascalia="inizio della produzione", gigante="2028", icona="calendario"),
]
RIEPILOGO = dict(n=7, titolo="In breve", punti=["Capriola sopra un camion", "Ferma a testa in giù", "10 getti d'aria compressa",
                                               "Poca AI: acrobazie programmate", "Produzione dal 2028"])
INVITO = "📩 Mandalo a chi sogna le auto volanti"

# ---------------------------------------------------------------- pezzi comuni
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&amp;family=Bricolage+Grotesque:'
         'wght@400;500;700;800&amp;family=JetBrains+Mono:wght@500;700&amp;display=swap" rel="stylesheet">')

def pagina(titolo, corpo):
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
{FONTS}
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

def logo_svg(t, w=44, h=38):
    f, a = P[t]["logo"]
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 700 600" aria-hidden="true"><rect width="700" height="460" rx="110" fill="{f}"></rect>'
            f'<polygon points="120,440 120,600 280,440" fill="{f}"></polygon><text x="350" y="235" text-anchor="middle" dominant-baseline="central" '
            f'font-family="Space Grotesk" font-weight="700" font-size="290" fill="{a}">AI</text></svg>')

def logo(t, size=32):
    return (f'<div style="display:flex;align-items:center;gap:8px;font-size:{size}px;font-weight:700;letter-spacing:-1px;'
            f'font-family:\'Space Grotesk\',sans-serif;color:{P[t]["ink"]}">Scopri{logo_svg(t)}</div>')

def hl(testo, t, pad=8, rad=6):
    bg, fg = P[t]["hl"]
    e = H.escape(testo, quote=False)
    return re.sub(r"\*(.+?)\*", lambda m: f'<span style="background:{bg};color:{fg};padding:0 {pad}px;border-radius:{rad}px;'
                  f'-webkit-box-decoration-break:clone;box-decoration-break:clone">{m.group(1)}</span>', e)

def esc(s):
    return H.escape(s, quote=False)

def freccia(col, w=40):
    return (f'<svg width="{w}" height="{w}" viewBox="0 0 44 44" aria-hidden="true"><path d="M6 22h30M24 10l12 12-12 12" fill="none" '
            f'stroke="{col}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"></path></svg>')

def scorri(t, extra=""):
    bg, fg = P[t]["pill"]
    return (f'<div style="display:flex;align-items:center;gap:12px;height:96px;box-sizing:border-box;padding:0 30px 0 36px;border-radius:999px;'
            f'background:{bg};color:{fg};font-size:38px;font-weight:800;letter-spacing:-1px;{extra}">Scorri{freccia(fg)}</div>')

def contatore(n, t, stile=""):
    return (f'<div style="font-family:\'JetBrains Mono\',monospace;font-weight:700;font-size:28px;color:{P[t]["ink"]};letter-spacing:1px;{stile}">{n}/{TOT}</div>')

def news(t):
    return f'<div style="font-family:\'JetBrains Mono\',monospace;font-weight:700;font-size:24px;color:{P[t]["label"]};letter-spacing:1px">NEWS LAMPO</div>'

def foto(nome, extra_img=""):
    f, alt, (x, y), _ = IMG[nome]
    return (f'<img src="img/{f}" alt="{esc(alt)}" style="display:block;width:100%;height:100%;object-fit:cover;object-position:{x}% {y}%;{extra_img}">')

def fumetto(testo, t, extra=""):
    bg, fg = P[t]["fum"]
    return (f'<div style="background:{bg};color:{fg};padding:16px 30px;border-radius:30px 30px 30px 6px;font-size:40px;font-weight:700;'
            f'white-space:nowrap;{extra}">{esc(testo)}</div>')

def stella(col, size, pos):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" style="position:absolute;{pos}" aria-hidden="true">'
            f'<path d="M50 0 L61 39 L100 50 L61 61 L50 100 L39 61 L0 50 L39 39Z" fill="{col}"></path></svg>')

def lista(punti, t, dim=46, gap=34, cerchio=84):
    bg, fg = P[t]["num"]
    return "".join(
        f'<div style="display:flex;gap:28px;align-items:center"><div style="flex:none;width:{cerchio}px;height:{cerchio}px;border-radius:50%;'
        f'background:{bg};color:{fg};display:flex;align-items:center;justify-content:center;font-size:{int(cerchio*.52)}px;font-weight:800">{i}</div>'
        f'<div style="font-size:{dim}px;font-weight:700;line-height:1.15;letter-spacing:-1px">{esc(p)}</div></div>'
        for i, p in enumerate(punti, 1))

def radice(t, extra=""):
    return (f'<div style="width:1080px;height:1350px;position:relative;overflow:hidden;box-sizing:border-box;background:{P[t]["page"]};'
            f'color:{P[t]["ink"]};font-family:\'Bricolage Grotesque\',sans-serif;{extra}">')

# ---------------------------------------------------------------- A · Classico
def A_cop(c, t):
    sotto = f'<p style="margin:0;font-size:36px;line-height:1.3;color:{P[t]["sub"]}">{esc(c["sotto"])}</p>' if c["sotto"] else ""
    return (f'<div style="width:1080px;height:1350px;box-sizing:border-box;padding:64px 72px;background:{P[t]["page"]};color:{P[t]["ink"]};'
            f'font-family:\'Bricolage Grotesque\',sans-serif;display:flex;flex-direction:column;gap:40px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center">{logo(t)}{news(t)}</div>'
            f'<div style="flex:1;min-height:0;width:100%;background:{NERO};border-radius:36px;overflow:hidden">{foto(c["img"])}</div>'
            f'<div style="display:flex;align-items:flex-end;gap:36px"><div style="flex:1;display:flex;flex-direction:column;gap:22px">'
            f'<h1 style="margin:0;font-size:78px;font-weight:800;line-height:1.2;letter-spacing:-3px">{hl(c["titolo"], t)}</h1>{sotto}</div>'
            f'{scorri(t, "flex:none")}</div></div>')

def A_int(s, t):
    if s.get("numero"):
        bg, fg = P[t]["box"]
        vis = (f'<div style="flex:1;min-height:0;background:{bg};color:{fg};border-radius:36px;display:flex;flex-direction:column;align-items:center;'
               f'justify-content:center;gap:18px"><div style="font-size:260px;font-weight:800;letter-spacing:-10px;line-height:1">{s["numero"]}</div>'
               f'<div style="font-size:44px;font-weight:700">{esc(s["didascalia"])}</div></div>')
    else:
        vis = f'<div style="flex:1;min-height:0;background:{NERO};border-radius:36px;overflow:hidden">{foto(s["img"])}</div>'
    return (f'<div style="width:1080px;height:1350px;box-sizing:border-box;padding:64px 72px;background:{P[t]["page"]};color:{P[t]["ink"]};'
            f'font-family:\'Bricolage Grotesque\',sans-serif;display:flex;flex-direction:column;gap:30px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center">{logo(t)}{contatore(s["n"], t)}</div>'
            f'<h2 style="margin:0;font-size:68px;font-weight:800;line-height:1.2;letter-spacing:-2px">{hl(s["titolo"], t)}</h2>'
            f'<p style="margin:0;font-size:38px;line-height:1.35;color:{P[t]["sub"]}">{esc(s["testo"])}</p>'
            f'{fumetto(s["fum"], t, "align-self:flex-start")}{vis}</div>')

def riep_generica(r, t, testa, titolo_px=96, extra_top=""):
    return (f'<div style="width:1080px;height:1350px;box-sizing:border-box;padding:64px 72px;background:{P[t]["page"]};color:{P[t]["ink"]};'
            f'font-family:\'Bricolage Grotesque\',sans-serif;display:flex;flex-direction:column;gap:44px;{extra_top}">{testa}'
            f'<h2 style="margin:40px 0 0;font-size:{titolo_px}px;font-weight:800;line-height:1.2;letter-spacing:-3px">{hl("*" + r["titolo"] + "*", t, 12, 10)}</h2>'
            f'<div style="display:flex;flex-direction:column;gap:40px">{lista(r["punti"], t)}</div><div style="flex:1"></div>'
            f'<div style="font-size:34px;font-weight:700;color:{P[t]["sub"]}">📌 Salva questa slide</div></div>')

def A_riep(r, t):
    return riep_generica(r, t, f'<div style="display:flex;justify-content:space-between;align-items:center">{logo(t)}{contatore(r["n"], t)}</div>')

# ---------------------------------------------------------------- B · Fascia
def B_logo(t):
    return (f'<div style="position:absolute;top:48px;left:56px;display:flex;align-items:center;gap:8px;background:{P[t]["page"]};padding:12px 20px;'
            f'border-radius:999px;font-size:30px;font-weight:700;letter-spacing:-1px;font-family:\'Space Grotesk\',sans-serif;color:{P[t]["ink"]}">Scopri{logo_svg(t, 40, 34)}</div>')

def B_cont(n, t):
    return (f'<div style="position:absolute;top:52px;right:56px;background:{P[t]["page"]};color:{P[t]["ink"]};padding:12px 20px;border-radius:999px;'
            f'font-family:\'JetBrains Mono\',monospace;font-weight:700;font-size:26px;letter-spacing:1px">{n}/{TOT}</div>')

def B_cop(c, t):
    sotto = f'<p style="margin:0;font-size:32px;color:{P[t]["sub"]}">{esc(c["sotto"])}</p>' if c["sotto"] else ""
    return (radice(t) + f'<div style="position:absolute;top:0;left:0;width:1080px;height:900px;background:{NERO};overflow:hidden">{foto(c["img"])}</div>'
            + B_logo(t) +
            f'<div style="position:absolute;top:56px;right:56px;background:{P[t]["page"]};color:{P[t]["ink"]};padding:12px 20px;border-radius:999px;'
            f'font-family:\'JetBrains Mono\',monospace;font-weight:700;font-size:24px;letter-spacing:1px">NEWS LAMPO</div>'
            f'<div style="position:absolute;left:0;right:0;bottom:0;height:450px;box-sizing:border-box;padding:48px 72px 64px;background:{P[t]["page"]};'
            f'display:flex;align-items:flex-end;gap:36px"><div style="flex:1;display:flex;flex-direction:column;gap:22px">'
            f'<h1 style="margin:0;font-size:74px;font-weight:800;line-height:1.2;letter-spacing:-3px">{hl(c["titolo"], t)}</h1>{sotto}</div>'
            f'{scorri(t, "flex:none")}</div></div>')

def B_int(s, t):
    if s.get("numero"):
        bg, fg = P[t]["box"]
        alto = (f'<div style="position:absolute;top:0;left:0;width:1080px;height:780px;background:{bg};color:{fg};display:flex;flex-direction:column;'
                f'align-items:center;justify-content:center;gap:18px"><div style="font-size:300px;font-weight:800;letter-spacing:-12px;line-height:1">{s["numero"]}</div>'
                f'<div style="font-size:46px;font-weight:700">{esc(s["didascalia"])}</div></div>')
    else:
        alto = f'<div style="position:absolute;top:0;left:0;width:1080px;height:780px;background:{NERO};overflow:hidden">{foto(s["img"])}</div>'
    return (radice(t) + alto + B_logo(t) + B_cont(s["n"], t) +
            f'<div style="position:absolute;left:0;right:0;top:780px;bottom:0;box-sizing:border-box;padding:96px 72px 64px;background:{P[t]["page"]};'
            f'display:flex;flex-direction:column;gap:24px"><h2 style="margin:0;font-size:64px;font-weight:800;line-height:1.2;letter-spacing:-2.5px">{hl(s["titolo"], t)}</h2>'
            f'<p style="margin:0;font-size:36px;line-height:1.3;color:{P[t]["sub"]}">{esc(s["testo"])}</p></div>'
            + fumetto(s["fum"], t, "position:absolute;top:736px;left:72px;font-size:42px;padding:18px 32px" + (f";background:{NERO};color:{GIALLO}" if s.get("numero") and P[t]["box"][0] == P[t]["fum"][0] else "")) + '</div>')

def B_riep(r, t):
    return riep_generica(r, t, f'<div style="display:flex;justify-content:space-between;align-items:center">{logo(t)}'
                         f'<div style="background:{P[t]["page"]};font-family:\'JetBrains Mono\',monospace;font-weight:700;font-size:26px">{r["n"]}/{TOT}</div></div>')

# ---------------------------------------------------------------- C · Telefono grande
def C_testa(t, destra):
    return (f'<div style="position:absolute;top:52px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center">{logo(t)}{destra}</div>')

def C_barre(n, t):
    return ('<div style="position:absolute;top:128px;left:64px;right:64px"><div style="display:flex;gap:8px">' +
            "".join(f'<div style="flex:1;height:10px;border-radius:5px;background:{P[t]["bar_on"] if i <= n else P[t]["bar_off"]}"></div>' for i in range(1, TOT + 1))
            + '</div></div>')

def C_schermo(nome, top, h=640, rot=-4, left=-20, w=1120):
    # la foto dentro uno "schermo" nero arrotondato e inclinato (al posto del telefono/computer del template)
    return (f'<div style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{h}px;box-sizing:border-box;border:14px solid {NERO};border-radius:40px;'
            f'background:{NERO};overflow:hidden;transform:rotate({rot}deg);transform-origin:50% 40%;box-shadow:0 30px 60px rgba(0,0,0,.35)">{foto(nome)}</div>')

def C_cop(c, t):
    sotto = f'<p style="margin:26px 0 0;font-size:38px;line-height:1.25;color:{P[t]["sub"]};font-weight:500">{esc(c["sotto"])}</p>' if c["sotto"] else ""
    cerchio = P[t]["acc"]
    return (radice(t) + C_testa(t, news(t)) + C_barre(1, t) +
            f'<div style="position:absolute;top:176px;left:64px;right:64px"><h1 style="margin:0;font-size:88px;font-weight:800;line-height:1.2;letter-spacing:-3.5px">{hl(c["titolo"], t)}</h1>{sotto}</div>'
            f'<div style="position:absolute;left:0;top:560px;width:1080px;height:790px;overflow:hidden">'
            f'<div style="position:absolute;left:130px;top:40px;width:820px;height:820px;border-radius:50%;background:{cerchio}"></div>'
            + C_schermo(c["img"], 150, 640) + '</div>' + scorri(t, f"position:absolute;right:64px;bottom:56px;box-shadow:8px 8px 0 {NERO}") + '</div>')

def C_int(s, t):
    cerchio = P[t]["acc"] if t != "blu" else GIALLO
    if s.get("numero"):
        bg, fg = P[t]["box"] if t != "blu" else (GIALLO, NERO)
        vis = (f'<div style="position:absolute;left:0;top:440px;width:1080px;height:910px;overflow:hidden">'
               f'<div style="position:absolute;left:170px;top:110px;width:740px;height:740px;border-radius:50%;background:{bg};color:{fg};'
               f'display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-6deg);box-shadow:12px 12px 0 {NERO}">'
               f'<div style="font-size:250px;font-weight:800;letter-spacing:-10px;line-height:.9">{s["numero"]}</div>'
               f'<div style="font-size:44px;font-weight:700;margin-top:18px">{esc(s["didascalia"])}</div></div></div>')
    else:
        vis = (f'<div style="position:absolute;left:0;top:440px;width:1080px;height:910px;overflow:hidden">'
               f'<div style="position:absolute;left:220px;top:110px;width:780px;height:780px;border-radius:50%;background:{cerchio}"></div>'
               + C_schermo(s["img"], 190, 640, -5) + '</div>')
    return (radice(t) + C_testa(t, contatore(s["n"], t)) + C_barre(s["n"], t) +
            f'<div style="position:absolute;top:176px;left:64px;right:64px"><h2 style="margin:0;font-size:68px;font-weight:800;line-height:1.2;letter-spacing:-2.5px">{hl(s["titolo"], t)}</h2>'
            f'<p style="margin:22px 0 0;font-size:34px;line-height:1.28;font-weight:500;color:{P[t]["sub"]}">{esc(s["testo"])}</p></div>'
            + vis + fumetto(s["fum"], t, "position:absolute;left:64px;top:470px;box-shadow:6px 6px 0 " + NERO) + '</div>')

def C_riep(r, t):
    return (radice(t) + C_testa(t, contatore(r["n"], t)) + C_barre(r["n"], t) +
            f'<div style="position:absolute;top:200px;left:64px;right:64px;display:flex;flex-direction:column;gap:44px">'
            f'<h2 style="margin:0;font-size:96px;font-weight:800;line-height:1.2;letter-spacing:-3px">{hl("*" + r["titolo"] + "*", t, 12, 10)}</h2>'
            f'<div style="display:flex;flex-direction:column;gap:40px">{lista(r["punti"], t)}</div></div>'
            f'<div style="position:absolute;left:64px;bottom:64px;font-size:34px;font-weight:700;color:{P[t]["sub"]}">📌 Salva questa slide</div></div>')

# ---------------------------------------------------------------- D · Numero gigante
def D_carta(nome, l, top, w, h, rot, sfondo=NERO):
    return (f'<div style="position:absolute;width:{w}px;height:{h}px;box-sizing:border-box;padding:0;border-radius:34px;background:{sfondo};'
            f'border:5px solid {NERO};box-shadow:10px 10px 0 {NERO};transform:rotate({rot}deg);overflow:hidden;left:{l}px;top:{top}px">{foto(nome)}</div>')

def D_cop(c, t):
    sotto = f'<p style="margin:24px 0 0;font-size:36px;line-height:1.25;color:{P[t]["sub"]};font-weight:500;width:650px">{esc(c["sotto"])}</p>' if c["sotto"] else ""
    g = c["gigante"]
    gpos = "left:24px;top:110px;font-size:480px;letter-spacing:-30px" if g == "10" else "left:40px;top:60px;font-size:700px;letter-spacing:-20px"
    return (radice(t) + C_testa(t, news(t)) +
            f'<div style="position:absolute;{gpos};font-weight:800;line-height:1;color:{P[t]["parola"]}">{g}</div>'
            + D_carta(c["img"], 560, 330, 470, 320, 5) +
            stella(P[t]["stella"], 80, "left:900px;top:130px") + stella(BIANCO, 50, "left:500px;top:690px") +
            f'<div style="position:absolute;left:64px;right:64px;top:770px"><h1 style="margin:0;font-size:88px;font-weight:800;line-height:1.2;letter-spacing:-3.5px">{hl(c["titolo"], t)}</h1>{sotto}</div>'
            + scorri(t, f"position:absolute;right:64px;bottom:56px;box-shadow:8px 8px 0 {NERO}") + '</div>')

def D_int(s, t):
    g = s["gigante"]
    if s.get("numero"):
        alto = (f'<div style="position:absolute;left:40px;top:150px;font-size:400px;font-weight:800;letter-spacing:-22px;line-height:.85;color:{P[t]["parola"]}">{g}</div>'
                f'<div style="position:absolute;right:64px;top:560px;background:{P[t]["fum"][0] if t != "blu" else GIALLO};color:{P[t]["fum"][1] if t != "blu" else NERO};padding:14px 28px;border-radius:999px;'
                f'font-size:34px;font-weight:800;transform:rotate(6deg);box-shadow:8px 8px 0 {NERO}">{esc(s["didascalia"])}</div>'
                + stella(P[t]["stella"], 90, "right:90px;top:120px") + stella(BIANCO if t != "carta" else GIALLO, 56, "right:260px;top:430px"))
    else:
        size = 300 if len(g) <= 4 else 250
        alto = (f'<div style="position:absolute;left:52px;top:140px;font-size:{size}px;font-weight:800;letter-spacing:-12px;line-height:.85;color:{P[t]["parola"]}">{g}</div>'
                + D_carta(s["img"], 230, 420, 790, 445, 4) +
                stella(P[t]["stella"], 80, "left:820px;top:170px") + stella(BIANCO if t != "carta" else GIALLO, 56, "left:120px;top:600px"))
    return (radice(t) + C_testa(t, contatore(s["n"], t)) + alto +
            f'<div style="position:absolute;left:64px;top:910px;width:940px"><h2 style="margin:0;font-size:60px;font-weight:800;line-height:1.2;letter-spacing:-2px">{hl(s["titolo"], t)}</h2>'
            f'<p style="margin:18px 0 0;font-size:32px;line-height:1.28;font-weight:500;color:{P[t]["sub"]}">{esc(s["testo"])}</p></div>'
            + fumetto(s["fum"], t, f"position:absolute;right:64px;top:1206px;transform:rotate(-3deg);box-shadow:6px 6px 0 {NERO}") + '</div>')

def D_riep(r, t):
    return (radice(t) + C_testa(t, contatore(r["n"], t)) +
            f'<div style="position:absolute;left:48px;top:130px;font-size:230px;font-weight:800;letter-spacing:-10px;line-height:.85;color:{P[t]["parola"]}">IN BREVE</div>'
            + stella(BIANCO, 70, "right:90px;top:360px") +
            f'<div style="position:absolute;left:64px;right:64px;top:470px;display:flex;flex-direction:column;gap:40px">{lista(r["punti"], t)}</div>'
            f'<div style="position:absolute;right:64px;bottom:64px;background:{P[t]["fum"][0]};color:{P[t]["fum"][1]};padding:16px 30px;border-radius:30px 30px 6px 30px;'
            f'font-size:38px;font-weight:700;transform:rotate(-3deg);box-shadow:6px 6px 0 {NERO}">📌 Salva questa slide</div></div>')

# ---------------------------------------------------------------- F · Carta a blocchi
def F_radice(t):
    g = P[t]["grid"]
    return radice(t, f"background-image:linear-gradient({g} 2px,transparent 2px),linear-gradient(90deg,{g} 2px,transparent 2px);background-size:54px 54px;background-position:-1px -1px")

def F_blocco(dentro, bg, extra=""):
    return (f'<div style="box-sizing:border-box;background:{bg};border:4px solid {NERO};border-radius:36px;box-shadow:10px 10px 0 {NERO};{extra}">{dentro}</div>')

def nastro(pos):
    return (f'<div style="position:absolute;width:150px;height:44px;background:rgba(255,255,255,.8);border-left:3px dashed rgba(18,18,18,.25);'
            f'border-right:3px dashed rgba(18,18,18,.25);{pos}"></div>')

ICONE = {
    "giro": '<path d="M50 32a18 18 0 1 1-6-13" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/><path d="M46 8l2 13-13 1" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
    "giu": '<path d="M32 10v40M16 36l16 16 16-16" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
    "getti": '<rect x="12" y="10" width="40" height="16" rx="8" fill="#FFFFFF"/><path d="M20 32v18M32 32v22M44 32v18" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>',
    "vento": '<path d="M8 22h32a8 8 0 1 0-8-8M8 34h44a8 8 0 1 1-8 8M8 46h22" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>',
    "calendario": '<rect x="10" y="14" width="44" height="40" rx="8" fill="none" stroke="#FFFFFF" stroke-width="6"/><path d="M10 28h44M22 8v12M42 8v12" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>',
    "lista": '<path d="M24 18h28M24 32h28M24 46h28" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/><circle cx="13" cy="18" r="4" fill="#FFFFFF"/><circle cx="13" cy="32" r="4" fill="#FFFFFF"/><circle cx="13" cy="46" r="4" fill="#FFFFFF"/>',
}

def F_testa(t, n):
    destra = (f'<div style="background:{BIANCO};color:{NERO};border:4px solid {NERO};border-radius:999px;padding:6px 18px;box-shadow:4px 4px 0 {NERO};'
              f'font-family:\'JetBrains Mono\',monospace;font-weight:700;font-size:26px;letter-spacing:1px">{n}/{TOT}</div>') if n else news(t)
    return f'<div style="position:absolute;top:50px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center">{logo(t)}{destra}</div>'

def F_testo_bg(t):
    # blocco del testo: blu (testo bianco) su carta e giallo; giallo (testo nero) sul blu
    return (GIALLO, NERO) if t == "blu" else (BLU, BIANCO)

def F_cop(c, t):
    tb, tf = F_testo_bg(t)
    sotto = (f'<div style="position:absolute;left:64px;top:600px;width:700px;transform:rotate(1deg)">' +
             F_blocco(f'<p style="margin:0;padding:24px 32px;font-size:36px;line-height:1.25;font-weight:500;color:{tf}">{esc(c["sotto"])}</p>', tb) + '</div>') if c["sotto"] else ""
    top_img = 760 if c["sotto"] else 600
    return (F_radice(t) + F_testa(t, None) +
            f'<div style="position:absolute;left:64px;right:64px;top:150px;transform:rotate(-1.5deg)">' +
            F_blocco(f'<div style="padding:36px 40px"><h1 style="margin:0;font-size:80px;font-weight:800;line-height:1.2;letter-spacing:-3px;color:{NERO}">{hl(c["titolo"], "carta", 10, 10)}</h1></div>', BIANCO)
            + nastro("left:80px;top:-24px;transform:rotate(-5deg)") + '</div>' + sotto +
            f'<div style="position:absolute;left:84px;right:84px;top:{top_img}px;height:{1180 - top_img}px;transform:rotate(-1.5deg)">' +
            F_blocco(foto(c["img"]), NERO, "width:100%;height:100%;overflow:hidden;padding:0") + nastro("right:70px;top:-24px;transform:rotate(4deg)") + '</div>'
            + scorri(t, f"position:absolute;right:64px;bottom:56px;border:4px solid {NERO};box-shadow:8px 8px 0 {NERO}") + '</div>')

def F_int(s, t):
    tb, tf = F_testo_bg(t)
    if s.get("numero"):
        bg, fg = (BLU, BIANCO) if t != "blu" else (GIALLO, NERO)
        vis = F_blocco(f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;color:{fg}">'
                       f'<div style="font-size:260px;font-weight:800;letter-spacing:-10px;line-height:1">{s["numero"]}</div>'
                       f'<div style="margin-top:26px;background:{GIALLO if bg == BLU else BIANCO};color:{NERO};padding:12px 30px;border-radius:999px;font-size:34px;font-weight:700">{esc(s["didascalia"])}</div></div>',
                       bg, "width:100%;height:100%")
    else:
        vis = F_blocco(foto(s["img"]), NERO, "width:100%;height:100%;overflow:hidden;padding:0")
    fb, ff = (GIALLO, NERO) if t != "giallo" else (BIANCO, NERO)
    return (F_radice(t) + F_testa(t, s["n"]) +
            f'<div style="position:absolute;left:64px;right:64px;top:140px">' +
            F_blocco(f'<div style="display:flex;gap:26px;align-items:center;padding:28px 32px"><div style="flex:none;width:84px;height:84px;border-radius:24px;background:{BLU};'
                     f'border:4px solid {NERO};display:flex;align-items:center;justify-content:center"><svg width="56" height="56" viewBox="0 0 64 64">{ICONE[s["icona"]]}</svg></div>'
                     f'<h2 style="margin:0;font-size:56px;font-weight:800;line-height:1.2;letter-spacing:-2px;color:{NERO}">{hl(s["titolo"], "carta", 8, 8)}</h2></div>', BIANCO) + '</div>'
            f'<div style="position:absolute;left:64px;right:64px;top:400px">' +
            F_blocco(f'<p style="margin:0;padding:28px 34px;font-size:34px;line-height:1.28;font-weight:500;color:{tf}">{esc(s["testo"])}</p>', tb) + '</div>'
            f'<div style="position:absolute;left:84px;right:84px;top:640px;height:560px;transform:rotate(-1.5deg)">' + vis +
            nastro("left:50%;margin-left:-75px;top:-24px;transform:rotate(-3deg)") + '</div>' +
            f'<div style="background:{fb};color:{ff};padding:16px 30px;border-radius:30px 30px 30px 6px;font-size:40px;font-weight:700;white-space:nowrap;position:absolute;'
            f'right:64px;top:1170px;transform:rotate(3deg);border:4px solid {NERO};box-shadow:6px 6px 0 {NERO}">{esc(s["fum"])}</div></div>')

def F_riep(r, t):
    righe = "".join(
        f'<div style="display:flex;gap:24px;align-items:center"><div style="flex:none;width:72px;height:72px;border-radius:50%;box-sizing:border-box;background:{BLU};color:{BIANCO};'
        f'border:4px solid {NERO};display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:800">{i}</div>'
        f'<div style="font-size:44px;font-weight:700;line-height:1.15;letter-spacing:-1px;color:{NERO}">{esc(p)}</div></div>' for i, p in enumerate(r["punti"], 1))
    return (F_radice(t) + F_testa(t, r["n"]) +
            f'<div style="position:absolute;left:64px;right:64px;top:140px">' +
            F_blocco(f'<div style="display:flex;gap:26px;align-items:center;padding:28px 32px"><div style="flex:none;width:84px;height:84px;border-radius:24px;background:{BLU};'
                     f'border:4px solid {NERO};display:flex;align-items:center;justify-content:center"><svg width="56" height="56" viewBox="0 0 64 64">{ICONE["lista"]}</svg></div>'
                     f'<h2 style="margin:0;font-size:72px;font-weight:800;line-height:1.2;letter-spacing:-2px;color:{NERO}">{hl("*In breve*", "carta", 10, 10)}</h2></div>', BIANCO) + '</div>'
            f'<div style="position:absolute;left:84px;right:84px;top:400px;transform:rotate(-1deg)">' +
            F_blocco(f'<div style="padding:44px 44px;display:flex;flex-direction:column;gap:34px">{righe}</div>', BIANCO) +
            nastro("left:50%;margin-left:-75px;top:-24px;transform:rotate(-3deg)") + '</div>'
            f'<div style="background:{BLU if t != "blu" else GIALLO};color:{BIANCO if t != "blu" else NERO};padding:16px 30px;border-radius:30px 30px 6px 30px;font-size:38px;font-weight:700;'
            f'position:absolute;right:64px;bottom:64px;transform:rotate(-3deg);border:4px solid {NERO};box-shadow:6px 6px 0 {NERO}">📌 Salva questa slide</div></div>')

# ---------------------------------------------------------------- E · Foto a tutta slide (palette di varianti-e.py)
import importlib.util
spec = importlib.util.spec_from_file_location("ve", REPO + "/strumenti/varianti-e.py")
ve = importlib.util.module_from_spec(spec); spec.loader.exec_module(ve)
ET = {"giallo": ve.TINTE["giallo"], "blu": ve.TINTE["blu"], "carta": ve.TINTE["bianco"]}

def E_fondo(t, nome, alto=1120):
    f, alt, (x, y), r = IMG[nome]
    w = int(alto * r)
    left = int(540 - x / 100 * w); left = max(min(left, 0), 1080 - w)
    T = ET[t]
    a, b, c = [("%g" % q).lstrip("0") for q in T["velo_stops"]]; v = T["velo"]
    lb = T["logo_sfondo"]
    return (f'<div style="position:absolute;left:0;top:0;width:1080px;height:1350px;overflow:hidden;background:{NERO}">'
            f'<img src="img/{f}" alt="{esc(alt)}" style="display:block;position:absolute;left:{left}px;top:0;width:{w}px;height:{alto}px"></div>'
            f'<div style="position:absolute;left:0;top:0;width:1080px;height:1350px;background:linear-gradient(to top, rgba({v},{a}) 0%, rgba({v},{b}) 34%, rgba({v},{c}) 52%, rgba({v},0) 70%)"></div>'
            f'<div style="position:absolute;top:48px;left:56px;display:flex;background:{lb};padding:12px 22px;border-radius:999px">'
            f'<div style="display:flex;align-items:center;gap:8px;font-size:30px;font-weight:700;letter-spacing:-1px;font-family:\'Space Grotesk\',sans-serif;color:{T["logo_testo"]}">Scopri{ve.LOGO}</div></div>')

def E_hl(testo, t, pad=10, rad=10):
    T = ET[t]
    e = esc(testo)
    return re.sub(r"\*(.+?)\*", lambda m: ve.ev(T, m.group(1), pad, rad), e)

def E_cornice(t, dentro):
    T = ET[t]
    return (f'<div style="width:1080px;height:1350px;position:relative;overflow:hidden;background:{T["base"]};color:{T["testo"]};'
            f'font-family:\'Bricolage Grotesque\',sans-serif;">{dentro}</div>')

def E_badge(t, testo, news=False):
    T = ET[t]
    return (f'<div style="position:absolute;top:60px;right:56px;font-family:\'JetBrains Mono\',monospace;font-weight:700;font-size:26px;'
            f'color:{T["badge_news"] if news else T["badge_testo"]};letter-spacing:1px;background:{T["badge_sfondo"]};padding:10px 22px;border-radius:999px">{testo}</div>')

def E_cop(c, t):
    T = ET[t]
    sotto = f'<p style="margin:26px 0 0;font-size:38px;line-height:1.25;color:{T["sotto"]};font-weight:500;width:640px">{esc(c["sotto"])}</p>' if c["sotto"] else ""
    return E_cornice(t, E_fondo(t, c["img"]) + E_badge(t, "NEWS LAMPO", True) +
                     f'<div style="position:absolute;left:64px;right:64px;bottom:190px"><h1 style="margin:0;font-size:96px;font-weight:800;line-height:1.2;letter-spacing:-4px">{E_hl(c["titolo"], t, 12, 12)}</h1>{sotto}</div>'
                     f'<div style="display:flex;align-items:center;gap:12px;height:96px;box-sizing:border-box;padding:0 30px 0 36px;border-radius:999px;background:{T["pill_sfondo"]};'
                     f'color:{T["pill_testo"]};font-size:38px;font-weight:800;letter-spacing:-1px;position:absolute;right:64px;bottom:64px;box-shadow:8px 8px 0 {T["pill_ombra"]}">Scorri{ve.freccia(T["pill_testo"])}</div>')

def E_int(s, t):
    T = ET[t]
    parola = (f'<div style="font-size:150px;font-weight:800;letter-spacing:-6px;line-height:.9;color:{T["parola"]};margin-bottom:12px">{s["numero"]}</div>' if s.get("numero") else "")
    return E_cornice(t, E_fondo(t, s["img"]) + E_badge(t, f'{s["n"]}/{TOT}') +
                     f'<div style="position:absolute;left:64px;right:64px;bottom:64px">{parola}<h2 style="margin:0;font-size:68px;font-weight:800;line-height:1.2;letter-spacing:-2.5px">{E_hl(s["titolo"], t)}</h2>'
                     f'<p style="margin:22px 0 0;font-size:33px;line-height:1.28;font-weight:500;color:{T["sotto"]};width:900px">{esc(s["testo"])}</p>'
                     f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:28px"><div style="background:{T["fum_sfondo"]};color:{T["fum_testo"]};padding:16px 30px;'
                     f'border-radius:30px 30px 30px 6px;font-size:40px;font-weight:700;white-space:nowrap;">{esc(s["fum"])}</div>'
                     f'<div style="width:112px;height:112px;border-radius:50%;background:{T["fre_sfondo"]};display:flex;align-items:center;justify-content:center;box-shadow:6px 6px 0 {T["fre_ombra"]}">{ve.freccia(T["fre_freccia"], 56)}</div></div></div>')

def E_riep(r, t):
    T = ET[t]
    righe = "".join(
        f'<div style="display:flex;gap:28px;align-items:center"><div style="flex:none;width:84px;height:84px;border-radius:50%;background:{T["fre_sfondo"]};color:{T["fre_freccia"]};'
        f'display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:800">{i}</div><div style="font-size:46px;font-weight:700;line-height:1.15;letter-spacing:-1px">{esc(p)}</div></div>'
        for i, p in enumerate(r["punti"], 1))
    return E_cornice(t, f'<div style="position:absolute;inset:0;background:{T["sfondo"]}"></div>'
                     f'<div style="position:absolute;left:-200px;top:-260px;width:760px;height:760px;border-radius:50%;background:{T["cerchio"]};opacity:.9"></div>'
                     f'<div style="position:absolute;top:48px;left:56px;display:flex;background:{T["logo_sfondo"] if T["logo_sfondo"] != T["cerchio"] else BIANCO};padding:12px 22px;border-radius:999px">'
                     f'<div style="display:flex;align-items:center;gap:8px;font-size:30px;font-weight:700;letter-spacing:-1px;font-family:\'Space Grotesk\',sans-serif;color:{T["logo_testo"]}">Scopri{ve.LOGO}</div></div>'
                     + E_badge(t, f'{r["n"]}/{TOT}') +
                     f'<div style="position:absolute;left:64px;right:64px;top:400px;display:flex;flex-direction:column;gap:40px"><h2 style="margin:0 0 10px;font-size:100px;font-weight:800;line-height:1.2;letter-spacing:-4px">{E_hl("*In breve*", t, 12, 12)}</h2>{righe}</div>'
                     f'<div style="position:absolute;left:64px;bottom:64px;background:{T["fum_sfondo"]};color:{T["fum_testo"]};padding:16px 30px;border-radius:30px 30px 30px 6px;font-size:38px;font-weight:700">📌 Salva questa slide</div>')

# ---------------------------------------------------------------- chiusura (terminatore notifica, blu, un solo invito)
def chiusura():
    t = open(REPO + "/template/terminatori/2026-10-15-notifica/claude-design-blu.dc.html", encoding="utf-8").read()
    t = re.sub(r'\s*<div style="background: #FFFFFF; color: #121212; border-radius: 28px;[^"]*">📌 E salva il post per ritrovarlo</div>', "", t)
    t = t.replace("🔔 Segui @scopri__ai e attiva le notifiche", INVITO)
    t = t.replace("line-height: 1; letter-spacing: -3px; text-align: center", "line-height: 1.2; letter-spacing: -3px; text-align: center")
    # contatore 8/8 in alto a destra
    t = t.replace("display: flex; flex-direction: column; align-items: center; gap: 24px\">",
                  "display: flex; flex-direction: column; align-items: center; gap: 24px; position: relative\">"
                  f"<div style=\"position: absolute; top: 64px; right: 72px; font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 28px; color: #FFFFFF; letter-spacing: 1px\">{TOT}/{TOT}</div>", 1)
    t = t.replace("family=Space+Grotesk:wght@700&amp;family=Bricolage", "family=Space+Grotesk:wght@700&amp;family=JetBrains+Mono:wght@700&amp;family=Bricolage")
    assert INVITO in t and "E salva il post" not in t and f"{TOT}/{TOT}" in t
    return t

# ---------------------------------------------------------------- scrittura
B = {"A": (A_cop, A_int, A_riep, "AF"), "B": (B_cop, B_int, B_riep, "BCD"), "C": (C_cop, C_int, C_riep, "BCD"),
     "D": (D_cop, D_int, D_riep, "BCD"), "E": (E_cop, E_int, E_riep, "E"), "F": (F_cop, F_int, F_riep, "AF")}
canvas = {"v": 3, "attachments": {}, "boards": {}}
ch = chiusura()

def board(nome, x, y, titolo):
    canvas["boards"][nome] = {"file": nome, "x": x, "y": y, "width": 1080, "height": 1350, "title": titolo}

for riga, (L, (fc, fi, fr, ritmo)) in enumerate(B.items()):
    tinte = RITMO[ritmo]
    y = 1770 * riga
    nome = f"{L}1-copertina.dc.html"
    open(f"{BOZZA}/{nome}", "w", encoding="utf-8").write(pagina(f"{L}1 Copertina", fc(COPERTINE[""], tinte[0])))
    board(nome, 0, y, f"{L}1 · Copertina")
    for i, s in enumerate(INTERNE):
        nome = f"{L}{s['n']}-{s['tema']}.dc.html"
        open(f"{BOZZA}/{nome}", "w", encoding="utf-8").write(pagina(f"{L}{s['n']} {s['tema']}", fi(s, tinte[i + 1])))
        board(nome, 1160 * (i + 1), y, f"{L}{s['n']} · {s['tema'].replace('-', ' ').capitalize()}")
    nome = f"{L}7-in-breve.dc.html"
    open(f"{BOZZA}/{nome}", "w", encoding="utf-8").write(pagina(f"{L}7 In breve", fr(RIEPILOGO, tinte[6])))
    board(nome, 1160 * 6, y, f"{L}7 · In breve")
    nome = f"{L}8-chiusura.dc.html"
    open(f"{BOZZA}/{nome}", "w", encoding="utf-8").write(ch.replace("<title>Chiusura Notifica blu</title>", f"<title>{L}8 Chiusura</title>"))
    board(nome, 1160 * 7, y, f"{L}8 · Chiusura")

# righe delle copertine alternative: una riga per template (titolo a, titolo b, seconda idea di video)
ETICH = {"-titolo-a": "titolo a", "-titolo-b": "titolo b", "-video-2": "video 2"}
for riga, (L, (fc, fi, fr, ritmo)) in enumerate(B.items()):
    y = 1770 * (6 + riga)
    for k, var in enumerate(["-titolo-a", "-titolo-b", "-video-2"]):
        nome = f"{L}1-copertina{var}.dc.html"
        open(f"{BOZZA}/{nome}", "w", encoding="utf-8").write(pagina(f"{L}1 Copertina {ETICH[var]}", fc(COPERTINE[var], RITMO[ritmo][0])))
        board(nome, 1160 * k, y, f"{L}1 · Copertina ({ETICH[var]})")

json.dump(canvas, open(f"{BOZZA}/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(canvas["boards"]), "board")

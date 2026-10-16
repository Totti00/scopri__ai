#!/usr/bin/env python3
"""Genera i template A, B, C, D, F e la chiusura nei tre colori di partenza (blu, bianco, giallo).

Uso:
    python3 strumenti/varianti-colori.py            # rifà tutte le cartelle template/<nome>-bianco e -giallo
    python3 strumenti/varianti-colori.py chiusura   # solo le tre chiusure in template/terminatori/2026-10-15-notifica/

Come funziona (deciso il 15/10/2026): si parte dalle slide del post Google Play (la bozza di
archivio/2026-10-15-news-lampo-google-play-app-ai/bozza/, che ha già A..F nel colore di partenza blu) e si cambiano
SOLO i colori, ruolo per ruolo (fondo, evidenziatore, fumetto, cerchio, barra, logo...). Le tinte delle slide interne
alternano (RITMO) e il testo ha sempre contrasto almeno 4.5:1 (controllato in fondo).
Il template E non si tocca: ha il suo script (varianti-e.py).
Per cambiare una palette si tocca solo TINTE.
"""
import re, sys, pathlib, shutil, subprocess, html as _html

RADICE = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = RADICE / "template"
BOZZA = RADICE / "archivio/2026-10-15-news-lampo-google-play-app-ai/bozza"
TERMINATORE = TEMPLATE / "terminatori/2026-10-15-notifica"

BLU, GIALLO, CARTA, NERO, BIANCO = "#2340FF", "#FFD84D", "#F4F1EA", "#121212", "#FFFFFF"

# Come si presenta ogni tinta di pagina.
TINTE = {
    "blu":    dict(page=BLU,    ink=BIANCO, sub="#DDE3FF", logo_fill=GIALLO, logo_ai=BLU,    etichetta=GIALLO,
                   traccia_on=GIALLO, traccia_off="rgba(255,255,255,.3)", griglia="rgba(255,255,255,.1)", cerchio_scuro=BLU),
    "carta":  dict(page=CARTA,  ink=NERO,   sub="#2A2A2A", logo_fill=BLU,    logo_ai=BIANCO, etichetta=BLU,
                   traccia_on=BLU,    traccia_off="rgba(18,18,18,.15)",   griglia="rgba(35,64,255,.09)", cerchio_scuro=BLU),
    "giallo": dict(page=GIALLO, ink=NERO,   sub="#2A2A2A", logo_fill=BLU,    logo_ai=BIANCO, etichetta=NERO,
                   traccia_on=BLU,    traccia_off="rgba(18,18,18,.15)",   griglia="rgba(18,18,18,.09)", cerchio_scuro=BLU),
}
NOME_TINTA = {"#2340FF": "blu", "#F4F1EA": "carta", "#FFD84D": "giallo"}

# Tinta delle 5 slide (copertina + 4 interne) per ogni colore di partenza.
# Sorgente (blu): B, C, D fanno blu, carta, giallo, blu, carta; A e F hanno la copertina blu e le interne carta.
RITMO = {
    "BCD": {"blu": ["blu", "carta", "giallo", "blu", "carta"],
            "bianco": ["carta", "blu", "giallo", "carta", "blu"],
            "giallo": ["giallo", "carta", "blu", "giallo", "carta"]},
    "AF":  {"blu": ["blu", "carta", "carta", "carta", "carta"],
            "bianco": ["carta", "blu", "giallo", "blu", "giallo"],
            "giallo": ["giallo", "blu", "carta", "blu", "giallo"]},
}
TEMPLATES = {  # lettera -> (cartella blu esistente, ritmo, sorgente blu: tinta delle 5 slide)
    "A": ("A-classico", "AF"), "B": ("B-fascia", "BCD"), "C": ("C-telefono-grande", "BCD"),
    "D": ("D-numero-gigante", "BCD"), "F": ("F-carta-blocchi", "AF"),
}
SORGENTE = {"AF": ["blu", "carta", "carta", "carta", "carta"], "BCD": ["blu", "carta", "giallo", "blu", "carta"]}
NOMI = ["1-copertina", "2-app", "3-telefono", "4-usa-18", "5-condivisione"]
COLORI = ["blu", "bianco", "giallo"]
PARTENZA = {"blu": "blu", "bianco": "carta", "giallo": "giallo"}  # colore di partenza -> tinta della copertina


# ------------------------------------------------------------------ ricolora uno stile
def decl(stile):
    out = []
    for p in re.split(r";(?![^()]*\))", stile):
        if ":" in p and p.strip():
            k, v = p.split(":", 1)
            out.append([k.strip(), v.strip()])
    return out

def ricolora_stile(stile, S, D, b, radice):
    """S, D: tinta di partenza e di arrivo (blu/carta/giallo); b: template B (le superfici hanno il colore della pagina)."""
    d = decl(stile)
    g = lambda k: next((v for kk, v in d if kk == k), None)
    def s(k, v):
        for x in d:
            if x[0] == k:
                x[1] = v; return
        d.append([k, v])
    def rm(k):
        d[:] = [x for x in d if x[0] != k]
    T, TS = TINTE[D], TINTE[S]
    bg, col = (g("background") or "").upper(), (g("color") or "").upper()
    ha_pad = g("padding") is not None
    if radice:
        s("background", T["page"]); s("color", T["ink"])
        if g("background-image"):
            for a in (TS["griglia"],):
                s("background-image", g("background-image").replace(a, T["griglia"]))
        return "; ".join(f"{k}: {v}" for k, v in d) if " " in stile else ";".join(f"{k}:{v}" for k, v in d)
    # barre di avanzamento (template C)
    if g("height") == "10px" and g("flex") == "1":
        s("background", T["traccia_on"] if bg in (GIALLO, BLU) else T["traccia_off"])
    # superfici col colore della pagina (template B: fascia e sfondo del logo)
    elif b and bg == TS["page"].upper():
        s("background", T["page"])
        if col == TS["ink"].upper(): s("color", T["ink"])
    elif bg == GIALLO or (S == "giallo" and bg == BIANCO and ha_pad and g("font-size") is None):
        if D == "giallo" and b and S == "blu" and "6px" in (g("border-radius") or ""):
            s("background", NERO); s("color", GIALLO)  # fumetto sul confine tra visual blu e fascia gialla
        elif D == "giallo":
            s("background", BLU); s("color", BIANCO)
        elif bg == BIANCO:
            s("background", GIALLO); s("color", NERO)
        elif D == "blu":
            s("color", NERO)  # testo scuro sul giallo, anche se la pagina è blu
    elif bg == BLU:  # blocco blu: superficie se la pagina è blu, altrimenti blocco di accento
        if S == "blu":
            s("background", T["page"])
            if col == BIANCO: s("color", T["ink"])
        elif D == "blu":
            s("background", GIALLO); s("color", NERO)
    elif bg == "#1A30C4":
        if D != "blu": s("background", BLU)
    elif bg.startswith("RGBA(255,216,77"):  # nastro adesivo
        if D == "giallo": s("background", "rgba(255,255,255,.8)")
    elif col == BIANCO and not bg:
        if S == "blu": s("color", T["ink"])
        elif D == "blu": s("color", NERO)
    elif col == BLU and not bg and S != "blu" and D == "blu":
        s("color", GIALLO)  # parola gigante blu su carta: sul blu diventa gialla
    elif col == NERO and not bg and S != "blu" and D == "blu":
        s("color", BIANCO)  # testo scuro scritto a mano sulla carta: sul blu diventa chiaro
    elif bg == BIANCO and not col:
        s("color", NERO)  # scheda bianca: testo sempre scuro, anche se la pagina è blu
    elif col == GIALLO and not bg:
        grande = int(re.sub(r"\D", "", g("font-size") or "0") or 0) >= 120
        if grande and S == "blu":
            s("color", BLU)  # parola o cifra gigante: blu su carta e su giallo
        elif "JetBrains" in (g("font-family") or ""):
            s("color", T["etichetta"])
        elif S != "blu":  # testo giallo dentro un blocco blu: se il blocco diventa giallo, il testo diventa scuro
            if D == "blu": s("color", NERO)
        elif D == "carta":
            rm("color"); s("background", GIALLO); s("padding", "0 8px"); s("border-radius", "6px")
        elif D == "giallo":
            rm("color"); s("background", BLU); s("color", BIANCO); s("padding", "0 8px"); s("border-radius", "6px")
    elif col == "#DDE3FF":
        s("color", T["sub"])
    # linee e bordi chiari della slide blu
    for k in ("border-top", "border-left", "border-right"):
        pass
    return "; ".join(f"{k}: {v}" for k, v in d) if " " in stile else ";".join(f"{k}:{v}" for k, v in d)

def ricolora_svg(tag, D, S):
    T = TINTE[D]
    # logo
    if 'font-size="290"' in tag:
        tag = re.sub(r'(<rect[^>]*fill=")#[0-9A-Fa-f]{6}', r'\g<1>' + T["logo_fill"], tag)
        tag = re.sub(r'(<polygon[^>]*fill=")#[0-9A-Fa-f]{6}', r'\g<1>' + T["logo_fill"], tag)
        tag = re.sub(r'(<text[^>]*fill=")#[0-9A-Fa-f]{6}', r'\g<1>' + T["logo_ai"], tag)
        return tag
    # stelline e altri disegni di accento
    def f(m):
        c = m.group(2).upper()
        if D == "giallo" and c == GIALLO: c = BLU
        elif D == "blu" and c == BLU and S != "blu": c = GIALLO
        return m.group(1) + c
    return re.sub(r'((?:fill|stroke)=")(#[0-9A-Fa-f]{6})', f, tag)

def ricolora(testo, S, D, b):
    """Ricolora il corpo (tra <x-dc> e </x-dc>) di una slide dalla tinta S alla tinta D."""
    if S == D:
        return testo
    inizio = testo.index("<x-dc>")
    fine = testo.index("</x-dc>")
    corpo = testo[inizio:fine]
    primo = [True]
    def st(m):
        stile = m.group(1)
        radice = "1080px" in stile and "1350px" in stile and primo[0]
        if radice: primo[0] = False
        return 'style="' + ricolora_stile(stile, S, D, b, radice) + '"'
    corpo = re.sub(r'style="([^"]*)"', st, corpo)
    corpo = re.sub(r"<svg[^>]*>.*?</svg>", lambda m: ricolora_svg(m.group(0), D, S), corpo, flags=re.S)
    return testo[:inizio] + corpo + testo[fine:]


# ------------------------------------------------------------------ chiusura (terminatore notifica)
def chiusura(colore, sorgente):
    t = sorgente
    t = re.sub(r"<title>[^<]*</title>", f"<title>Chiusura Notifica {colore}</title>", t)
    if colore == "bianco":
        return t
    T = TINTE["blu" if colore == "blu" else "giallo"]
    t = t.replace("background: #F4F1EA; color: #121212;", f"background: {T['page']}; color: {T['ink']};", 1)
    logo = re.search(r"<svg[^>]*viewBox=\"0 0 700 600\".*?</svg>", t, re.S).group(0)
    t = t.replace(logo, ricolora_svg(logo, "blu" if colore == "blu" else "giallo", "carta"), 1)
    ev = '<span style="background: #FFD84D; padding: 0 10px; border-radius: 8px">'
    pill = "background: #2340FF; color: #FFFFFF; border-radius: 28px"
    if colore == "blu":
        t = t.replace(ev, '<span style="background: #FFD84D; color: #121212; padding: 0 10px; border-radius: 8px">')
        t = t.replace(pill, "background: #FFD84D; color: #121212; border-radius: 28px")
        t = t.replace('<path d="M610 60 L640 40 M630 110 L668 104 M600 20 L610 -6" stroke="#121212"',
                      '<path d="M610 60 L640 40 M630 110 L668 104 M600 20 L610 -6" stroke="#FFFFFF"')
        t = t.replace('<path d="M80 470 l10 28 28 10 -28 10 -10 28 -10 -28 -28 -10 28 -10z" fill="#2340FF">',
                      '<path d="M80 470 l10 28 28 10 -28 10 -10 28 -10 -28 -28 -10 28 -10z" fill="#FFD84D">')
    else:
        t = t.replace(ev, '<span style="background: #2340FF; color: #FFFFFF; padding: 0 10px; border-radius: 8px">')
        t = t.replace('<circle cx="350" cy="330" r="290" fill="#FFD84D">', '<circle cx="350" cy="330" r="290" fill="#FFFFFF">')
    return t


# ------------------------------------------------------------------ contrasto
def lum(h):
    h = h.lstrip("#"); r, g, b = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def contrasto(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True); return (x + .05) / (y + .05)

def controlla():
    """Coppie testo/sfondo usate dalle tinte (testo sulla pagina, evidenziatore, fumetto, pillola, logo)."""
    coppie = [("pagina blu", BIANCO, BLU), ("pagina carta", NERO, CARTA), ("pagina giallo", NERO, GIALLO),
              ("sotto blu", "#DDE3FF", BLU), ("sotto carta/giallo su carta", "#2A2A2A", CARTA), ("sotto su giallo", "#2A2A2A", GIALLO),
              ("evidenziatore giallo", NERO, GIALLO), ("evidenziatore blu", BIANCO, BLU),
              ("fumetto blu", BIANCO, BLU), ("fumetto giallo", NERO, GIALLO),
              ("logo giallo", BLU, GIALLO), ("logo blu", BIANCO, BLU),
              ("etichetta su blu", GIALLO, BLU), ("etichetta su carta", BLU, CARTA), ("etichetta su giallo", NERO, GIALLO)]
    ok = True
    for n, a, b in coppie:
        c = contrasto(a, b)
        if c < 4.5: ok = False
        print(f"  {n:30s} {a} su {b}: {c:.1f}:1 {'OK' if c >= 4.5 else 'TROPPO BASSO'}")
    print("contrasti:", "tutti OK" if ok else "ATTENZIONE")


# ------------------------------------------------------------------ anteprima
def anteprima(cartella, files):
    """6 slide affiancate (3x2) come le altre anteprime."""
    import json
    tmp = pathlib.Path("/tmp/claude-0/-home-user-scopri--ai/19ba81ca-19f7-50ae-a0e4-96b586c37d4a/scratchpad/anteprima")
    tmp.mkdir(parents=True, exist_ok=True)
    pngs = []
    for i, f in enumerate(files):
        p = tmp / f"{cartella.name}-{i}.png"
        subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(f), str(p), "1080", "1350"], check=True, stdout=subprocess.DEVNULL)
        pngs.append(p)
    imgs = "".join(f'<img src="file://{p}" style="width:540px;height:675px;display:block">' for p in pngs)
    pagina = tmp / f"{cartella.name}.html"
    pagina.write_text(f'<body style="margin:0;display:grid;grid-template-columns:repeat(3,540px);width:1620px;background:#ddd">{imgs}</body>')
    subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(pagina), str(cartella / "anteprima.png"), "1620", "1350"], check=True, stdout=subprocess.DEVNULL)


def main():
    sorg_ch = (TERMINATORE / "claude-design.dc.html").read_text(encoding="utf-8")
    if (TERMINATORE / "claude-design-bianco.dc.html").exists():
        sorg_ch = (TERMINATORE / "claude-design-bianco.dc.html").read_text(encoding="utf-8")
    controlla()
    for c in COLORI:
        (TERMINATORE / f"claude-design-{c}.dc.html").write_text(chiusura(c, sorg_ch), encoding="utf-8")
        subprocess.run(["node", str(RADICE / "strumenti/render.cjs"), str(TERMINATORE / f"claude-design-{c}.dc.html"),
                        str(TERMINATORE / f"slide-{c}.png"), "1080", "1350"], check=True, stdout=subprocess.DEVNULL)
    if len(sys.argv) > 1 and sys.argv[1] == "chiusura":
        return
    for lettera, (cartella_blu, ritmo) in TEMPLATES.items():
        for colore in ("bianco", "giallo"):
            dest = TEMPLATE / f"{cartella_blu}-{colore}"
            (dest / "img").mkdir(parents=True, exist_ok=True)
            for f in (TEMPLATE / "C-telefono-grande/img").glob("*"):
                shutil.copy(f, dest / "img" / f.name)
            tinte = RITMO[ritmo][colore]
            sorg = SORGENTE[ritmo]
            uscite = []
            for i in range(5):
                f = next(BOZZA.glob(f"{lettera}{NOMI[i]}.dc.html"))
                t = ricolora(f.read_text(encoding="utf-8"), sorg[i], tinte[i], lettera == "B")
                nome = {0: "copertina", 1: "slide", 3: "slide-numero"}.get(i)
                t = re.sub(r"<title>[^<]*</title>", f"<title>{lettera} {colore} {nome or 'extra'}</title>", t)
                out = dest / f"{nome or 'solo-anteprima-%d' % (i + 1)}.dc.html"
                out.write_text(t, encoding="utf-8")
                uscite.append(out)
            ch = TERMINATORE / f"claude-design-{colore}.dc.html"
            shutil.copy(ch, dest / "chiusura.dc.html")
            uscite.append(dest / "chiusura.dc.html")
            # slide 3 e 5 servono solo per l'anteprima: sposto in anteprima, poi tolgo
            ordine = [uscite[0], uscite[1], uscite[2], uscite[3], uscite[4], uscite[5]]
            anteprima(dest, ordine)
            for extra in dest.glob("solo-anteprima-*.dc.html"):
                extra.unlink()
            (dest / "COLORE.txt").write_text(f"colore di partenza: {colore}\n", encoding="utf-8")
    for lettera, (cartella_blu, ritmo) in TEMPLATES.items():
        (TEMPLATE / cartella_blu / "COLORE.txt").write_text("colore di partenza: blu\n", encoding="utf-8")


if __name__ == "__main__":
    main()

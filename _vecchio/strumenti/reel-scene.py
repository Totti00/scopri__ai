# Reel a scene (16/10/2026), messo da parte lo stesso giorno: il proprietario vuole Reel semplici (strumenti/reel.py).
"""Crea un Reel Scopri AI in motion graphics (1080×1920, 30 fps, senza audio) a partire da un file JSON.
Stile Electric Mono (dal 16/10/2026): fondi scuro, chiaro e blu, Inter Tight, logo a campana, niente giallo.

Uso:
    python3 strumenti/reel.py carousels/<slug>/reel.json               → reel.mp4
    python3 strumenti/reel.py carousels/<slug>/reel.json --anteprima   → reel-anteprima.png (un fotogramma per scena)
    python3 strumenti/reel.py carousels/<slug>/reel-b.json --anteprima → reel-b-anteprima.png
    (il file si chiama come il JSON: reel.json → reel.mp4, reel-b.json → reel-b.mp4)

Il JSON:
{
  "scene": [
    {"tipo": "gancio", "etichetta": "NEWS LAMPO", "titolo": "Guarda cosa sa fare *Gemini 4*",
     "commento": "Nuova AI di Google.", "video": "media/robot.mp4", "inizio": 97, "durata": 3},
    {"tipo": "scoperta", "titolo": "Ha allenato un *robot* a lanciare", "commento": "7 centri di fila.",
     "video": "media/robot.mp4", "inizio": 22, "durata": 3.5, "fondo": "chiaro", "posizione": 0.5},
    {"tipo": "finale", "titolo": "E questo è solo *Gemini 4*.", "invito_testo": "📩 Mandalo a chi usa ancora Excel", "durata": 3}
  ]
}
- "fondo": scuro, chiaro o blu (se manca: scuro → chiaro → blu, ma mai blu subito prima del finale; il finale è blu);
- "video": dentro un riquadro, in bianco e nero col tono blu come nelle slide ("tono": "colore" per lasciarlo a colori);
  "inizio" e "durata" in secondi; "posizione" sposta il taglio da sinistra (0) a destra (1); "adatta": "contain" lo mostra intero;
- al posto del video "immagine": "foto.png" (ferma), oppure niente: la scena diventa solo testo, titolo grande;
- nei titoli *parola* = parola chiave (in blu).

Regole dei Reel (16/10/2026, `format/5-reel.md`), controllate da questo programma:
- **zona sicura**: i testi stanno tra y 230 e y 1440 e a sinistra di x 850 (sopra, sotto e a destra ci sono i pulsanti
  e la caption di Instagram). Se un testo esce, il programma si ferma;
- **massimo 6 parole** per titolo, 4 per commento (si leggono in un colpo d'occhio): oltre, avviso;
- **il finale riprende una parola del gancio**, così quando il Reel ricomincia il giro si chiude: se non c'è, avviso.
"""
import html
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

RADICE = pathlib.Path(__file__).resolve().parent.parent
BRAND = RADICE / ".claude/skills/scopri-carousel/assets/brand"
FPS = 30
X, ALTO, BASSO, DESTRA = 64, 230, 1440, 850      # zona sicura dei testi
MAX_PAROLE_TITOLO, MAX_PAROLE_COMMENTO = 6, 4

MODI = {   # fondo pieno (tendine e ffmpeg), sfumatura, testo, parola chiave, logo
    "scuro": dict(pieno="#0A0A0D", fondo="radial-gradient(80% 50% at 70% 72%,#1A1C2E 0%,transparent 70%),"
                  "radial-gradient(120% 100% at 50% 50%,transparent 60%,rgba(0,0,0,.45) 100%),#0A0A0D",
                  testo="#F5F5F7", meta="#8B8B97", chiave="#8595FF", logo="negativo",
                  bordo="rgba(255,255,255,.14)", alone="rgba(35,64,255,.42)",
                  adesivo="background:#F5F5F7;color:#0A0A0D", punto="#2340FF",
                  pill="background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.14);color:#F5F5F7"),
    "chiaro": dict(pieno="#F2F2F5", fondo="radial-gradient(70% 40% at 10% 0%,rgba(255,255,255,.9) 0%,transparent 70%),"
                   "linear-gradient(160deg,#F7F7FA 0%,#ECEDF1 55%,#E4E5EB 100%)",
                   testo="#0A0A0D", meta="#5E5E6A", chiave="#2340FF", logo="colore",
                   bordo="rgba(10,10,13,.10)", alone="rgba(10,10,20,.22)",
                   adesivo="background:#0A0A0D;color:#F5F5F7", punto="#8595FF",
                   pill="background:#0A0A0D;color:#F5F5F7"),
    "blu": dict(pieno="#2340FF", fondo="radial-gradient(70% 40% at 10% 0%,rgba(255,255,255,.14) 0%,transparent 70%),"
                "linear-gradient(150deg,#4760FF 0%,#2340FF 45%,#1A32D1 100%)",
                testo="#FFFFFF", meta="rgba(255,255,255,.8)", chiave="#0A0A0D", logo="bianco",
                bordo="rgba(255,255,255,.24)", alone="rgba(16,20,90,.55)",
                adesivo="background:#FFFFFF;color:#0F26BD", punto="#2340FF",
                pill="background:#FFFFFF;color:#0F26BD"),
}
VECCHI = {"blu": "blu", "giallo": "scuro", "carta": "chiaro"}   # i reel.json di prima del 16/10
GIRO = ["scuro", "chiaro", "blu"]
GRANA = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .9 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)'/></svg>\")")
TONO_MONO = "hue=s=0,eq=contrast=1.08,colorbalance=bs=.10:bm=.07:bh=.03"   # come export-media.mjs delle slide


def parole(testo):
    return [w for w in re.sub(r"[*]", "", testo).split() if re.search(r"\w", w)]


def titolo_animato(testo, ritardo=0.25, passo=0.07):
    """Ogni parola sale dal basso, una dopo l'altra; la parola chiave (*così*) entra tutta insieme, in blu."""
    unita = []
    for p in re.split(r"(\*[^*]+\*)", testo):
        if p.startswith("*") and p.endswith("*") and len(p) > 2:
            unita.append(f'<span class="chiave">{html.escape(p[1:-1])}</span>')
            continue
        for w in p.split():
            if unita and re.fullmatch(r"[.,;:!?…]+", w):
                unita[-1] += html.escape(w)
            else:
                unita.append(html.escape(w))
    out = [f'<span class="parola" style="animation-delay:{ritardo + i * passo:.2f}s">{t}</span>' for i, t in enumerate(unita)]
    return " ".join(out), ritardo + len(unita) * passo


def foro(x, y, w, h, r):
    """clip-path che copre tutta la pagina tranne il riquadro arrotondato del video."""
    return (f"path(evenodd,'M0 0H1080V1920H0Z M{x + r} {y}H{x + w - r}A{r} {r} 0 0 1 {x + w} {y + r}V{y + h - r}"
            f"A{r} {r} 0 0 1 {x + w - r} {y + h}H{x + r}A{r} {r} 0 0 1 {x} {y + h - r}V{y + r}A{r} {r} 0 0 1 {x + r} {y}Z')")


def pagina(contenuto, m, durata, dopo, entrata, clip=""):
    """Pagina 1080×1920 trasparente: fondo (con il foro del video), testi, tendina di entrata e di uscita."""
    uscita = ""
    if dopo:
        uscita = (f'<div class="tendina" style="background:{MODI[dopo]["pieno"]};transform:translateY(100%);'
                  f'animation:sale .28s cubic-bezier(.7,0,.3,1) {durata - 0.28:.2f}s both"></div>')
    ingresso = (f'<div class="tendina" style="background:{m["pieno"]};animation:va .32s cubic-bezier(.7,0,.3,1) 0s both"></div>'
                if entrata else "")
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@500&amp;display=block" rel="stylesheet">
<style>
html,body{{margin:0;background:transparent}}
.pg{{position:relative;width:1080px;height:1920px;overflow:hidden;color:{m["testo"]};font-family:'Inter Tight','Noto Color Emoji',sans-serif;-webkit-font-smoothing:antialiased}}
.fondo{{position:absolute;inset:0;{clip}}}
.fondo .bg{{position:absolute;inset:0;background:{m["fondo"]}}}
.fondo .grana{{position:absolute;inset:0;background:{GRANA};opacity:.07;mix-blend-mode:overlay}}
.mono{{font-family:'JetBrains Mono',monospace;font-weight:500;letter-spacing:.08em;text-transform:uppercase}}
.chiave{{color:{m["chiave"]}}}
.titolo{{position:absolute;left:{X}px;width:{DESTRA - X}px;font-weight:600;line-height:1;letter-spacing:-.035em;text-wrap:balance}}
.parola{{display:inline-block;animation:su .6s cubic-bezier(.2,.7,.2,1) both}}
.entra{{animation:su .6s cubic-bezier(.2,.7,.2,1) both}}
.compare{{animation:compare .45s cubic-bezier(.2,.7,.2,1) both}}
.pill{{position:absolute;left:{X}px;height:56px;padding:0 26px;border-radius:999px;display:inline-flex;align-items:center;gap:14px;font-size:24px;white-space:nowrap;{m["pill"]}}}
.pill::before,.adesivo::before{{content:"";width:12px;height:12px;border-radius:50%;background:{m["punto"]};flex:none}}
.adesivo{{position:absolute;left:96px;height:88px;padding:0 34px;border-radius:999px;display:inline-flex;align-items:center;gap:16px;
  font-size:46px;font-weight:600;letter-spacing:-.02em;white-space:nowrap;box-shadow:0 24px 60px -18px rgba(0,0,0,.45);{m["adesivo"]}}}
.tendina{{position:absolute;inset:0;z-index:10}}
@keyframes su{{from{{transform:translateY(60px);opacity:0}}to{{transform:none;opacity:1}}}}
@keyframes compare{{from{{transform:scale(.86);opacity:0}}to{{transform:none;opacity:1}}}}
@keyframes va{{from{{transform:none}}to{{transform:translateY(-100%)}}}}
@keyframes sale{{from{{transform:translateY(100%)}}to{{transform:none}}}}
@keyframes respira{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.04)}}}}
</style></head><body><div class="pg">
{contenuto}
{ingresso}
{uscita}
</div></body></html>'''


def cornice(m, numero, totale):
    """Logo a campana in alto a sinistra e contatore "02 / 04" a destra, dentro la zona sicura."""
    logo = (BRAND / f"scopri-ai-logo-{m['logo']}.png").as_uri()
    conta = (f'<div class="mono testo entra" style="position:absolute;top:262px;right:{1080 - DESTRA}px;font-size:24px;'
             f'color:{m["meta"]};animation-delay:.2s"><b style="font-weight:500;color:{m["testo"]}">{numero:02d}</b> / {totale:02d}</div>'
             if numero else "")
    return (f'<img class="testo entra" src="{logo}" style="position:absolute;left:{X}px;top:250px;height:52px;animation-delay:.15s">'
            + conta)


def scena(s, m, dopo, primo, numero, totale):
    """Gancio o scoperta: titolo in alto, video (o immagine) nel riquadro, commento nell'adesivo."""
    gancio = s["tipo"] == "gancio"
    ha_media = bool(s.get("video") or s.get("immagine"))
    top = 336
    pill = ""
    if s.get("etichetta"):
        pill = (f'<div class="pill mono testo entra" style="top:{top}px;animation-delay:.2s">{html.escape(s["etichetta"])}</div>')
        top += 84
    titolo, fine = titolo_animato(s["titolo"], ritardo=0.08 if primo else 0.3)
    if ha_media:
        dim = 96 if gancio else 84
        bx, by, bw, bh, r = X, (770 if gancio else 720), 1080 - 2 * X, (590 if gancio else 640), 48
        clip = f"clip-path:{foro(bx, by, bw, bh, r)}"
        riquadro = (f'<div class="alone" style="position:absolute;left:{bx}px;top:{by}px;width:{bw}px;height:{bh}px;border-radius:{r}px;'
                    f'box-shadow:0 60px 160px -30px {m["alone"]}"></div>'
                    f'<div id="buco" style="position:absolute;left:{bx}px;top:{by}px;width:{bw}px;height:{bh}px;border-radius:{r}px;'
                    f'box-shadow:inset 0 0 0 2px {m["bordo"]}"></div>')
        top_commento = by + bh - 44
    else:   # solo testo: titolo grande a metà della zona sicura
        dim, top, clip, riquadro = 112, max(top, 560), "", ""
        top_commento = None
    commento = ""
    if s.get("commento"):
        commento = (f'<div class="adesivo testo compare" style="top:{top_commento or 0}px;animation-delay:{fine + 0.2:.2f}s"'
                    f'{" data-dopo-titolo" if top_commento is None else ""}>{html.escape(s["commento"])}</div>')
    contenuto = f'''<div class="fondo"><div class="bg"></div><div class="grana"></div></div>
{riquadro}
{cornice(m, numero, totale)}{pill}
<div id="titolo" class="titolo testo" style="top:{top}px;font-size:{dim}px">{titolo}</div>
{commento}'''
    if top_commento is None and commento:   # sotto il titolo, a qualunque altezza finisca
        contenuto += ('<script>const t=document.getElementById("titolo"),a=document.querySelector("[data-dopo-titolo]");'
                      'a.style.top=(t.offsetTop+t.offsetHeight+56)+"px"</script>')
    return pagina(contenuto, m, s["durata"], dopo, entrata=not primo, clip=clip)


def scena_finale(s, m, dopo):
    titolo, fine = titolo_animato(s.get("titolo", "Le novità sull'AI, *appena escono*."), ritardo=0.5, passo=0.06)
    invito = s.get("invito_testo", "🔔 Segui @scopri__ai")
    logo = (BRAND / f"scopri-ai-logo-{m['logo']}.png").as_uri()
    contenuto = f'''<div class="fondo"><div class="bg"></div><div class="grana"></div></div>
<div style="position:absolute;left:520px;top:1080px;width:1500px;height:1500px;border-radius:50%;background:rgba(255,255,255,.07)"></div>
<img class="testo compare" src="{logo}" style="position:absolute;left:{X}px;top:360px;width:560px;transform-origin:0 50%;animation-delay:.2s">
<div id="titolo" class="titolo testo" style="top:690px;font-size:84px">{titolo}</div>
<div class="testo compare" style="position:absolute;left:{X}px;top:1040px;animation-delay:{fine + 0.1:.2f}s">
  <div style="{m["adesivo"]};font-size:44px;font-weight:600;letter-spacing:-.02em;line-height:1.15;padding:24px 40px;border-radius:44px;
   display:inline-block;box-sizing:border-box;max-width:{DESTRA - X}px;transform-origin:0 50%;animation:respira 1.6s ease-in-out {fine + 0.6:.2f}s infinite">{html.escape(invito)}</div>
  <div class="mono" style="margin-top:30px;font-size:26px;color:{m["meta"]};text-transform:none">@scopri__ai</div>
</div>'''
    return pagina(contenuto, m, s["durata"], dopo, entrata=True)


def esegui(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Errore: {' '.join(map(str, cmd))[:300]}\n{r.stderr[-2000:]}")
    return r.stdout


def scena_mp4(s, modo, dopo, cartella, tmp, n, numero, totale, fps=FPS):
    m = MODI[modo]
    html_txt = scena_finale(s, m, dopo) if s["tipo"] == "finale" else scena(s, m, dopo, n == 0, numero, totale)
    html_file = tmp / f"scena-{n}.html"
    html_file.write_text(html_txt, encoding="utf-8")
    fotogrammi = tmp / f"fotogrammi-{n}"
    info = json.loads(esegui(["node", str(RADICE / "strumenti/reel-fotogrammi.cjs"), str(html_file), str(fotogrammi),
                              str(s["durata"]), str(fps)]).strip().splitlines()[-1])
    fuori = info.get("fuori") or []
    if fuori:
        sys.exit(f"Scena {n + 1}: testi fuori dalla zona sicura (y {ALTO}–{BASSO}, x ≤ {DESTRA}) o sopra il video:\n  "
                 + "\n  ".join(fuori) + "\nAccorcia il titolo o il commento.")
    uscita = tmp / f"scena-{n}.mp4"
    d = s["durata"]
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"color=c={m['pieno'].replace('#', '0x')}:s=1080x1920:r={FPS}:d={d}"]
    b = info.get("buco")
    if b and (s.get("video") or s.get("immagine")):
        w, h = b["width"], b["height"]
        if s.get("video"):
            cmd += ["-ss", str(s.get("inizio", 0)), "-t", str(d), "-i", str(cartella / s["video"])]
        else:
            cmd += ["-loop", "1", "-framerate", str(FPS), "-t", str(d), "-i", str(cartella / s["immagine"])]
        if s.get("adatta") == "contain":
            adatta = f"scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color=0x0A0A0D"
        else:
            pos = s.get("posizione", 0.5)
            adatta = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}:(iw-{w})*{pos}:(ih-{h})/2"
        tono = "" if s.get("tono") == "colore" else "," + TONO_MONO
        cmd += ["-framerate", str(fps), "-i", str(fotogrammi / "%04d.png")]
        filtro = (f"[1:v]fps={FPS},{adatta}{tono},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={d}[v];"
                  f"[0:v][v]overlay={b['x']}:{b['y']}[b];[b][2:v]overlay=0:0,format=yuv420p[out]")
    else:
        cmd += ["-framerate", str(fps), "-i", str(fotogrammi / "%04d.png")]
        filtro = "[0:v][1:v]overlay=0:0,format=yuv420p[out]"
    cmd += ["-filter_complex", filtro, "-map", "[out]", "-t", str(d), "-r", str(FPS),
            "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-an", str(uscita)]
    esegui(cmd)
    return uscita


def avvisi(scene):
    out = []
    for i, s in enumerate(scene, 1):
        if s.get("titolo") and len(parole(s["titolo"])) > MAX_PAROLE_TITOLO and s["tipo"] != "finale":
            out.append(f"scena {i}: titolo di {len(parole(s['titolo']))} parole (massimo {MAX_PAROLE_TITOLO})")
        if s.get("commento") and len(parole(s["commento"])) > MAX_PAROLE_COMMENTO:
            out.append(f"scena {i}: commento di {len(parole(s['commento']))} parole (massimo {MAX_PAROLE_COMMENTO})")
    gancio = next((s for s in scene if s["tipo"] == "gancio"), None)
    finale = next((s for s in scene if s["tipo"] == "finale"), None)
    if gancio and finale:
        g = {w.lower().strip(".,!?…") for w in parole(gancio["titolo"]) if len(w) >= 4 or re.search(r"\d", w)}
        f = {w.lower().strip(".,!?…") for w in parole(finale.get("titolo", ""))}
        if not g & f:
            out.append("il finale non riprende nessuna parola del gancio: il giro del Reel non si chiude")
    durata = sum(s["durata"] for s in scene)
    if not 15 <= durata <= 25:
        out.append(f"durata {durata:.1f} s (deve essere circa 20)")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    sorgente = pathlib.Path(args[0]).resolve()
    cartella, nome = sorgente.parent, sorgente.stem
    scene = json.loads(sorgente.read_text(encoding="utf-8"))["scene"]
    modi, giro = [], 0
    for i, s in enumerate(scene):
        voluto = VECCHI.get(s.get("fondo"), s.get("fondo"))
        if s["tipo"] == "finale":
            modi.append(voluto or "blu")
            continue
        if not voluto:
            voluto = GIRO[giro % len(GIRO)]
            giro += 1
            if voluto == "blu" and i + 1 < len(scene) and scene[i + 1]["tipo"] == "finale":
                voluto = "scuro"
        modi.append(voluto)
    scoperte = [i for i, s in enumerate(scene) if s["tipo"] == "scoperta"]
    numeri = {i: k + 1 for k, i in enumerate(scoperte)}
    for a in avvisi(scene):
        print("avviso:", a)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="reel-"))
    try:
        if "--anteprima" in sys.argv:
            immagini = []
            for i, s in enumerate(scene):
                breve = dict(s, durata=min(s["durata"], 2.6))
                pezzo = scena_mp4(breve, modi[i], None, cartella, tmp, i, numeri.get(i), len(scoperte), fps=5)
                img = tmp / f"ante-{i}.png"
                esegui(["ffmpeg", "-y", "-v", "error", "-sseof", "-0.1", "-i", str(pezzo), "-frames:v", "1",
                        "-vf", "scale=360:640", str(img)])
                immagini.append(img)
            ingressi = sum((["-i", str(x)] for x in immagini), [])
            dest = cartella / f"{nome}-anteprima.png"
            esegui(["ffmpeg", "-y", "-v", "error", *ingressi, "-filter_complex",
                    f"hstack=inputs={len(immagini)}" if len(immagini) > 1 else "null", str(dest)])
            print("Creato", dest)
            return
        pezzi = []
        for i, s in enumerate(scene):
            dopo = modi[i + 1] if i + 1 < len(scene) else None
            pezzi.append(scena_mp4(s, modi[i], dopo, cartella, tmp, i, numeri.get(i), len(scoperte)))
            print(f"Scena {i + 1}/{len(scene)} pronta")
        elenco = tmp / "elenco.txt"
        elenco.write_text("".join(f"file '{p}'\n" for p in pezzi))
        dest = cartella / f"{nome}.mp4"
        esegui(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(elenco), "-c", "copy",
                "-movflags", "+faststart", str(dest)])
        print(f"Creato {dest} ({sum(s['durata'] for s in scene):.1f} secondi)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()

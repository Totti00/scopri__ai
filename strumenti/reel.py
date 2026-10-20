"""Reel Scopri AI semplice (deciso il 16/10/2026): una sola schermata con un titolo che incuriosisce e, sotto,
il video vero che è "una bomba". Niente scene, niente animazioni: facile, veloce, cattura subito.
Si fa solo quando c'è un video vero che vale da solo (vedi format/5-reel.md). 1080×1920, senza audio
(la musica strumentale la mette il proprietario su Instagram). Stile Electric Mono, logo a campana, niente giallo.

Uso:
    python3 strumenti/reel.py carousels/<slug>/reel.json               → reel.mp4 + reel-copertina.jpg
                                                                          (+ reel-completo.mp4 se c'è "inizio" o "durata")
    python3 strumenti/reel.py carousels/<slug>/reel.json --anteprima   → reel-anteprima.png (in pochi secondi, col primo fotogramma)
    (il file si chiama come il JSON: reel-b.json → reel-b.mp4, reel-b-anteprima.png)

Il JSON:
{
  "titolo": "Google ha insegnato a un *robot* a fare centro. Gli è bastato *guardare un video*.",
  "video": "media/robot.mp4",
  "inizio": 0,              (facoltativo, secondi)
  "durata": 20,             (facoltativo: senza, il video intero; con inizio/durata esce il pezzo migliore come reel.mp4
                             e il video intero come reel-completo.mp4, così il proprietario può tagliare da solo)
  "fondo": "scuro",         (scuro, chiaro o blu; di solito scuro)
  "formato": "originale",   (originale, 1:1, 4:5 o 16:9: come tagliare il video nel riquadro)
  "posizione": 0.5,         (taglio orizzontale, da 0 = sinistra a 1 = destra)
  "zoom": 1.0,              (ingrandisce il video nel riquadro: 1.2 toglie bordi o scritte ai lati del video originale)
  "copertina": 1.0,         (secondo del video da usare per reel-copertina.jpg)
  "compatto": true          (facoltativo, 19/10/2026: tutto più in alto e video più grande, fino quasi al fondo;
                             per i video verticali da mostrare interi)
}
In alto c'è solo il logo, con spazio prima del titolo: niente etichette come "NEWS LAMPO" (deciso il 16/10/2026).
Il video è **sempre a colori** (deciso il 16/10/2026; dal 20/10/2026 anche nelle slide): niente bianco e nero col blu.
Nel titolo *parola* = parola chiave, in blu. Il titolo dice la cosa sorprendente (cosa ha fatto l'AI), al massimo 22 parole,
al massimo 4 righe. I testi stanno nella zona sicura (y 230–1440; sotto y 1000 anche a sinistra di x 850): se escono, si ferma.
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
X, LARGHEZZA, FONDO_MAX = 64, 952, 1760     # margine, larghezza del riquadro, fin dove può scendere il video
MAX_PAROLE, MAX_RIGHE = 22, 4
SPAZIO_LOGO = 96                            # spazio tra il logo e il titolo
MODI = {
    "scuro": dict(pieno="#0A0A0D", testo="#F5F5F7", chiave="#8595FF", logo="negativo", bordo="rgba(255,255,255,.14)",
                  alone="rgba(35,64,255,.40)", fondo="radial-gradient(70% 40% at 50% 62%,#1A1C2E 0%,transparent 70%),"
                  "radial-gradient(120% 100% at 50% 50%,transparent 60%,rgba(0,0,0,.45) 100%),#0A0A0D"),
    "chiaro": dict(pieno="#F2F2F5", testo="#0A0A0D", chiave="#2340FF", logo="colore", bordo="rgba(10,10,13,.10)",
                   alone="rgba(10,10,20,.25)",
                   fondo="radial-gradient(70% 40% at 10% 0%,rgba(255,255,255,.9) 0%,transparent 70%),"
                   "linear-gradient(160deg,#F7F7FA 0%,#ECEDF1 55%,#E4E5EB 100%)"),
    "blu": dict(pieno="#2340FF", testo="#FFFFFF", chiave="#0A0A0D", logo="bianco", bordo="rgba(255,255,255,.24)",
                alone="rgba(16,20,90,.55)",
                fondo="radial-gradient(70% 40% at 10% 0%,rgba(255,255,255,.14) 0%,transparent 70%),"
                "linear-gradient(150deg,#4760FF 0%,#2340FF 45%,#1A32D1 100%)"),
}
GRANA = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .9 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)'/></svg>\")")


def esegui(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Errore: {' '.join(map(str, cmd))[:300]}\n{r.stderr[-2000:]}")
    return r.stdout


def info_video(f):
    """Larghezza, altezza e durata, lette dall'intestazione di ffmpeg (non serve ffprobe)."""
    err = subprocess.run(["ffmpeg", "-i", str(f)], capture_output=True, text=True).stderr
    d = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    v = re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", err)
    if not (d and v):
        sys.exit(f"Non riesco a leggere il video {f}")
    w, h = int(v.group(1)), int(v.group(2))
    if re.search(r"rotate\s*:\s*-?(90|270)|rotation of -?90", err):
        w, h = h, w
    return w, h, int(d.group(1)) * 3600 + int(d.group(2)) * 60 + float(d.group(3))


def titolo_html(testo):
    return re.sub(r"\*([^*]+)\*", r'<span class="chiave">\1</span>', html.escape(testo))


def pagina(r, m, rapporto):
    # compatto: logo al bordo della zona sicura, spazi stretti, il video scende fino a y 1880 e il blocco non si centra
    alto, spazio, stacco, fine = (232, 40, 32, 1880) if r.get("compatto") else (250, SPAZIO_LOGO, 56, FONDO_MAX)
    logo = (BRAND / f"scopri-ai-logo-{m['logo']}.png").as_uri()
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700&amp;family=JetBrains+Mono:wght@500&amp;display=block" rel="stylesheet">
<style>
html,body{{margin:0;background:{m["pieno"]}}}
.pg{{position:relative;width:1080px;height:1920px;overflow:hidden;color:{m["testo"]};font-family:'Inter Tight','Noto Color Emoji',sans-serif;-webkit-font-smoothing:antialiased}}
.bg{{position:absolute;inset:0;background:{m["fondo"]}}}
.grana{{position:absolute;inset:0;background:{GRANA};opacity:.07;mix-blend-mode:overlay}}
.colonna{{position:absolute;left:{X}px;top:{alto}px;width:{LARGHEZZA}px;display:flex;flex-direction:column;align-items:flex-start}}
#titolo{{margin-top:{spazio}px;font-size:66px;font-weight:600;line-height:1.08;letter-spacing:-.03em;text-wrap:pretty;width:{LARGHEZZA}px}}
.chiave{{color:{m["chiave"]};font-weight:700}}
#buco{{margin-top:{stacco}px;width:{LARGHEZZA}px;aspect-ratio:{rapporto};max-height:var(--max);border-radius:44px;
  box-shadow:inset 0 0 0 2px {m["bordo"]},0 60px 160px -30px {m["alone"]}}}
</style></head><body><div class="pg">
<div class="bg"></div><div class="grana"></div>
<div class="colonna">
  <img class="testo" src="{logo}" style="height:64px">
  <div id="titolo" class="testo">{titolo_html(r["titolo"])}</div>
  <div id="buco"></div>
</div>
<script>   // il video non scende oltre y {FONDO_MAX}; poi il blocco si centra in verticale (mai sopra y 250)
const b=document.getElementById('buco'),c=document.querySelector('.colonna');
const max={fine}-b.getBoundingClientRect().top,[rw,rh]='{rapporto}'.split('/').map(Number);
b.style.setProperty('--max',max+'px');
if({LARGHEZZA}*rh/rw>max){{b.style.width=Math.floor(max*rw/rh/2)*2+'px';b.style.alignSelf='center';}}  // video alto: si stringa, non si taglia
if(!{'true' if r.get('compatto') else 'false'})c.style.top=Math.max(250,Math.round((1920-c.offsetHeight)/2-80))+'px';
</script>
</div></body></html>'''


def maschera(w, h, raggio, dest):
    codice = ("import sys\nfrom PIL import Image, ImageDraw\nw,h,r=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])\n"
              "m=Image.new('L',(w,h),0)\nImageDraw.Draw(m).rounded_rectangle([0,0,w-1,h-1],radius=r,fill=255)\nm.save(sys.argv[4])")
    esegui([sys.executable, "-c", codice, str(w), str(h), str(raggio), str(dest)])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    sorgente = pathlib.Path(args[0]).resolve()
    cartella, nome = sorgente.parent, sorgente.stem
    r = json.loads(sorgente.read_text(encoding="utf-8"))
    if r.get("etichetta"):
        print("avviso: \"etichetta\" non si usa più (nel Reel c'è solo il logo): la ignoro")
    if "scene" in r:
        sys.exit("Questo reel.json è nel formato a scene, che non si usa più: scrivi \"titolo\" e \"video\" (vedi in cima a questo file).")
    m = MODI[r.get("fondo", "scuro")]
    video = cartella / r["video"]
    vw, vh, totale = info_video(video)
    rapporto = {"1:1": "1/1", "4:5": "4/5", "16:9": "16/9"}.get(r.get("formato", "originale"), f"{vw}/{vh}")
    inizio = float(r.get("inizio", 0))
    durata = min(float(r.get("durata") or (totale - inizio)), totale - inizio)

    parole = [w for w in r["titolo"].replace("*", "").split() if re.search(r"\w", w)]
    if len(parole) > MAX_PAROLE:
        print(f"avviso: titolo di {len(parole)} parole (massimo {MAX_PAROLE}): chi scorre non lo legge tutto")
    if not 5 <= durata <= 90:
        print(f"avviso: il video dura {durata:.1f} s (meglio tra 8 e 40 s; il proprietario può tagliarlo)")

    tmp = pathlib.Path(tempfile.mkdtemp(prefix="reel-"))
    try:
        (tmp / "pagina.html").write_text(pagina(r, m, rapporto), encoding="utf-8")
        info = json.loads(esegui(["node", str(RADICE / "strumenti/reel-fotogrammi.cjs"), str(tmp / "pagina.html"),
                                  str(tmp / "fondo"), str(1 / FPS), str(FPS)]).strip().splitlines()[-1])
        problemi = list(info.get("fuori") or [])
        t = info.get("titolo") or {}
        if t.get("righe") and t["righe"] > MAX_RIGHE:
            problemi.append(f"il titolo è di {t['righe']} righe (massimo {MAX_RIGHE})")
        b = info["buco"]
        if b["height"] < 420:
            problemi.append(f"per il video restano solo {b['height']} px di altezza: accorcia il titolo")
        if problemi:
            sys.exit("Da sistemare:\n  " + "\n  ".join(problemi))
        fondo = tmp / "fondo" / "0001.png"
        w, h = b["width"], b["height"]
        pos, zoom = float(r.get("posizione", 0.5)), float(r.get("zoom", 1.0))
        zw, zh = round(w * zoom / 2) * 2, round(h * zoom / 2) * 2
        adatta = f"scale={zw}:{zh}:force_original_aspect_ratio=increase,crop={w}:{h}:(iw-{w})*{pos}:(ih-{h})/2,setsar=1"
        mask = tmp / "maschera.png"
        maschera(w, h, 44, mask)
        def filtro(taglio=""):   # il taglio si fa nel filtro: con -ss prima del video a volte partiva qualche secondo prima
            return (f"[1:v]{taglio}fps={FPS},{adatta},format=rgba[v];[2:v]format=gray,scale={w}:{h}[m];[v][m]alphamerge[vm];"
                    f"[0:v][vm]overlay={b['x']}:{b['y']}:shortest=1,format=yuv420p[out]")

        if "--anteprima" in sys.argv:
            istante = inizio + 0.05   # il primo fotogramma: è quello che deve catturare subito
            dest = cartella / f"{nome}-anteprima.png"
            fermo = tmp / "fermo.png"    # prima un fotogramma fermo: con il video diretto ffmpeg a volte non lo sovrappone
            esegui(["ffmpeg", "-y", "-v", "error", "-ss", str(istante), "-i", str(video), "-frames:v", "1", str(fermo)])
            esegui(["ffmpeg", "-y", "-v", "error", "-i", str(fondo), "-i", str(fermo), "-i", str(mask),
                    "-filter_complex", filtro().replace(",format=yuv420p[out]", ",scale=540:960[out]"),
                    "-map", "[out]", "-frames:v", "1", "-update", "1", str(dest)])
            print(f"Creato {dest} (video {durata:.1f} s, riquadro {w}×{h})")
            return

        dest = cartella / f"{nome}.mp4"
        uscite = [(dest, inizio, durata)]
        if inizio > 0 or durata < totale - 0.05:
            uscite.append((cartella / f"{nome}-completo.mp4", 0, totale))
        for file, da, quanto in uscite:
            esegui(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", str(FPS), "-i", str(fondo),
                    "-i", str(video), "-loop", "1", "-i", str(mask),
                    "-filter_complex", filtro(f"trim=start={da}:duration={quanto},setpts=PTS-STARTPTS,"), "-map", "[out]", "-t", str(quanto), "-r", str(FPS),
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-an", "-movflags", "+faststart", str(file)])
            print(f"Creato {file.name} ({quanto:.1f} secondi)")
        copertina = cartella / f"{nome}-copertina.jpg"
        esegui(["ffmpeg", "-y", "-v", "error", "-ss", str(min(float(r.get("copertina", 1.0)), durata - 0.1)), "-i", str(dest),
                "-frames:v", "1", "-q:v", "2", str(copertina)])
        print(f"Creato {copertina.name}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()

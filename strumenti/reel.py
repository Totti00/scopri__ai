"""Crea un Reel Scopri.AI in motion graphics (1080×1920, 30 fps, senza audio) a partire da un file JSON.

Uso:
    python3 strumenti/reel.py archivio/<cartella-post>/reel.json
    python3 strumenti/reel.py archivio/<cartella-post>/reel.json --anteprima
        → con --anteprima crea solo reel-anteprima.png (un fotogramma per scena, affiancati),
          utile per la bozza prima di fare il video.

Stile (deciso il 15/10/2026): Reel di circa 20 secondi, testi e grafiche animati nei colori
del brand, una scoperta per scena, con il video vero dentro un riquadro. Musica: la mette il
proprietario su Instagram (solo strumentale).

Il JSON ha questa forma:
{
  "scene": [
    {"tipo": "gancio", "etichetta": "NEWS LAMPO", "titolo": "Guarda cosa sa fare la *nuova AI di Google*",
     "commento": "Si chiama Gemini 4 Argon.", "video": "media/robot.mp4", "inizio": 12, "durata": 3.5},
    {"tipo": "scoperta", "titolo": "Ha insegnato a un robot a *giocare*", "commento": "7 centri di fila.",
     "video": "media/robot.mp4", "inizio": 54, "durata": 3.5, "fondo": "giallo", "posizione": 0.5},
    {"tipo": "finale", "durata": 2.5}
  ]
}
- "fondo": blu, giallo o carta (se manca, gira blu → giallo → carta; il finale è sempre blu);
- "posizione": sposta il taglio del video da sinistra (0) a destra (1);
- "adatta": "contain" mostra il video intero, con bande scure.
Al posto del video si può usare "immagine": "foto.png" (ferma), oppure niente: la scena diventa solo testo,
con il titolo grande al centro (utile per prompt e curiosità).
Nei titoli: *parola* = parola chiave.
Le zone coperte dai pulsanti di Instagram (in alto, in basso e a destra) restano libere dai testi.
Il Reel viene salvato come reel.mp4 nella cartella del JSON.
"""
import html
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from carosello import BLU, CARTA, GIALLO, NERO, BIANCO, SFONDO, FONT, fumetto  # noqa: E402

RADICE = pathlib.Path(__file__).resolve().parent.parent
FPS = 30
GIRO = ["blu", "giallo", "carta"]
SCURO = "#121212"


def titolo_animato(testo, fondo, ritardo=0.35, passo=0.08):
    """Ogni parola entra dal basso, una dopo l'altra; la parola chiave (*così*) entra tutta insieme, evidenziata."""
    stile_chiave = {"blu": f"color:{GIALLO}",
                    "carta": f"background:{GIALLO};padding:0 10px;border-radius:8px",
                    "giallo": f"background:{BIANCO};padding:0 10px;border-radius:8px"}[fondo]
    unita = []  # [testo html, è chiave]
    for p in re.split(r"(\*[^*]+\*)", testo):
        if p.startswith("*") and p.endswith("*") and len(p) > 2:
            unita.append([f'<span style="{stile_chiave}">{html.escape(p[1:-1])}</span>', True])
            continue
        for w in p.split():
            if unita and re.fullmatch(r"[.,;:!?…]+", w):
                unita[-1][0] += html.escape(w)  # la punteggiatura resta attaccata alla parola prima
            else:
                unita.append([html.escape(w), False])
    out = [f'<span class="parola" style="animation-delay:{ritardo + i * passo:.2f}s">{t}</span>'
           for i, (t, _) in enumerate(unita)]
    return " ".join(out), ritardo + len(unita) * passo


def chip(fondo):
    testo, bolla, scritta = (BIANCO, GIALLO, BLU) if fondo == "blu" else (NERO, BLU, BIANCO)
    sotto = {"blu": "rgba(255,255,255,.12)", "giallo": "rgba(255,255,255,.55)", "carta": "#FFFFFF"}[fondo]
    return (f'<div class="logo entra" style="position:absolute;top:210px;left:64px;display:flex;align-items:center;gap:8px;'
            f'background:{sotto};color:{testo};padding:12px 22px;border-radius:999px;font-size:32px;font-weight:700;'
            f'letter-spacing:-1px;animation-delay:.25s">Scopri{fumetto(bolla, scritta, 42)}</div>')


def base(contenuto, fondo, dopo, durata, entrata=True):
    """Pagina 1080×1920 trasparente, con la tendina di entrata e quella di uscita (colore della scena dopo)."""
    bg, fg = SFONDO[fondo]
    uscita = ""
    if dopo:
        uscita = (f'<div class="tendina" style="background:{SFONDO[dopo][0]};transform:translateY(100%);'
                  f'animation:sale .26s cubic-bezier(.7,0,.3,1) {durata - 0.26:.2f}s both"></div>')
    entrata_html = (f'<div class="tendina" style="background:{bg};animation:va .3s cubic-bezier(.7,0,.3,1) 0s both"></div>'
                    if entrata else "")
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family={FONT.replace(" ", "+")}:wght@400;500;700;800&amp;family=Space+Grotesk:wght@700&amp;family=JetBrains+Mono:wght@700&amp;display=block" rel="stylesheet">
<style>
html,body{{margin:0;background:transparent}}
.pagina{{position:relative;width:1080px;height:1920px;overflow:hidden;color:{fg};font-family:'{FONT}',sans-serif}}
.logo{{font-family:'Space Grotesk',sans-serif}}
.mono{{font-family:'JetBrains Mono',monospace;font-weight:700}}
.parola{{display:inline-block;animation:su .5s cubic-bezier(.2,.9,.25,1.2) both}}
.entra{{animation:su .5s cubic-bezier(.2,.9,.25,1.2) both}}
.pop{{animation:pop .55s cubic-bezier(.2,.9,.3,1.4) both}}
.tendina{{position:absolute;inset:0;z-index:10}}
@keyframes su{{from{{transform:translateY(70px);opacity:0}}to{{transform:none;opacity:1}}}}
@keyframes pop{{0%{{transform:scale(0) rotate(-10deg)}}100%{{transform:scale(1) rotate(-2deg)}}}}
@keyframes va{{from{{transform:none}}to{{transform:translateY(-100%)}}}}
@keyframes sale{{from{{transform:translateY(100%)}}to{{transform:none}}}}
@keyframes zoom{{from{{transform:scale(1.04)}}to{{transform:scale(1)}}}}
@keyframes batte{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.06)}}}}
@keyframes rimbalza{{0%{{transform:scale(0)}}60%{{transform:scale(1.15)}}100%{{transform:scale(1)}}}}
</style></head><body><div class="pagina">
{contenuto}
{entrata_html}
{uscita}
</div></body></html>'''


def scena_video(s, fondo, dopo, primo=False):
    """Gancio o scoperta: titolo in alto, video in un riquadro, commento nel fumetto giallo."""
    bg, _ = SFONDO[fondo]
    etichetta = ""
    top_titolo = 300
    if s.get("etichetta"):
        etichetta = (f'<div class="mono entra" style="position:absolute;top:300px;left:64px;font-size:30px;letter-spacing:2px;'
                     f'opacity:.75;animation-delay:.3s">{html.escape(s["etichetta"])}</div>')
        top_titolo = 350
    grande = s.get("tipo") == "gancio"
    titolo, fine = titolo_animato(s["titolo"], fondo, ritardo=0.05 if primo else 0.35)
    dim = 86 if grande else 80
    # zone libere da Instagram: niente testi sopra i 210 px e sotto i 1480 px
    top_video, alto_video = (650, 750) if grande else (540, 860)
    solo_testo = not (s.get("video") or s.get("immagine"))
    if solo_testo:
        # scena senza video né immagine: titolo grande al centro, commento sotto
        dim, top_titolo = 110, 620
        top_video, alto_video = 1080, 260
    commento = ""
    if s.get("commento"):
        colore_bolla = BIANCO if fondo == "giallo" else GIALLO
        commento = (f'<div class="pop" style="position:absolute;top:{top_video + alto_video - 60}px;left:96px;max-width:780px;'
                    f'background:{colore_bolla};color:{NERO};font-weight:800;font-size:58px;letter-spacing:-1.5px;line-height:1.05;'
                    f'padding:22px 34px;border-radius:30px 30px 30px 8px;box-shadow:0 10px 0 rgba(0,0,0,.18);'
                    f'transform-origin:20% 100%;animation-delay:{fine + 0.25:.2f}s">{html.escape(s["commento"])}</div>')
    buco = ("" if solo_testo else
            f'<div id="buco" style="position:absolute;top:{top_video}px;left:64px;width:952px;height:{alto_video}px;'
            f'border-radius:44px;box-shadow:0 0 0 3000px {bg}"></div>')
    sotto = f'<div style="position:absolute;inset:0;background:{bg}"></div>' if solo_testo else ""
    contenuto = f'''{sotto}{buco}
{chip(fondo)}{etichetta}
<div style="position:absolute;top:{top_titolo}px;left:64px;width:870px;font-size:{dim}px;font-weight:800;line-height:1.02;letter-spacing:-3px">{titolo}</div>
{commento}'''
    return base(contenuto, fondo, dopo, s["durata"], entrata=not primo)


def scena_finale(s, fondo, dopo):
    titolo, fine = titolo_animato(s.get("titolo", "Le novità sull'AI, *appena escono*."), fondo, ritardo=0.55, passo=0.06)
    contenuto = f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:{SFONDO[fondo][0]}"></div>
<div style="position:absolute;top:430px;left:0;right:0;display:flex;justify-content:center">
  <div style="animation:rimbalza .6s cubic-bezier(.2,.9,.3,1.3) .3s both">{fumetto(GIALLO, BLU, 380)}</div>
</div>
<div class="logo entra" style="position:absolute;top:820px;left:0;right:0;text-align:center;font-size:110px;font-weight:700;letter-spacing:-4px;animation-delay:.45s">Scopri.AI</div>
<div style="position:absolute;top:990px;left:110px;right:110px;text-align:center;font-size:76px;font-weight:800;line-height:1.05;letter-spacing:-2.5px">{titolo}</div>
<div style="position:absolute;top:1260px;left:0;right:0;display:flex;justify-content:center">
  <div class="pop" style="animation-delay:{fine + 0.1:.2f}s;transform-origin:50% 50%">
    <div style="background:{GIALLO};color:{NERO};font-size:52px;font-weight:800;padding:24px 44px;border-radius:999px;
     animation:batte .8s ease-in-out {fine + 0.6:.2f}s infinite">🔔 Segui @scopri__ai</div>
  </div>
</div>'''
    return base(contenuto, fondo, dopo, s["durata"])


def esegui(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Errore: {' '.join(map(str, cmd))[:300]}\n{r.stderr[-2000:]}")
    return r.stdout


def scena_mp4(s, fondo, dopo, cartella, tmp, n):
    pagina = scena_finale(s, fondo, dopo) if s["tipo"] == "finale" else scena_video(s, fondo, dopo, primo=(n == 0))
    html_file = tmp / f"scena-{n}.html"
    html_file.write_text(pagina, encoding="utf-8")
    fotogrammi = tmp / f"fotogrammi-{n}"
    info = json.loads(esegui(["node", str(RADICE / "strumenti/reel-fotogrammi.cjs"), str(html_file), str(fotogrammi),
                              str(s["durata"]), str(FPS)]).strip().splitlines()[-1])
    uscita = tmp / f"scena-{n}.mp4"
    d = s["durata"]
    bg = SFONDO[fondo][0].replace("#", "0x")
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"color=c={bg}:s=1080x1920:r={FPS}:d={d}"]
    if s.get("video") or s.get("immagine"):
        b = info["buco"]
        w, h = b["width"], b["height"]
        if s.get("video"):
            cmd += ["-ss", str(s.get("inizio", 0)), "-t", str(d), "-i", str(cartella / s["video"])]
        else:
            cmd += ["-loop", "1", "-framerate", str(FPS), "-t", str(d), "-i", str(cartella / s["immagine"])]
        if s.get("adatta") == "contain":
            adatta = f"scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color={SCURO.replace('#', '0x')}"
        else:
            pos = s.get("posizione", 0.5)
            adatta = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}:(iw-{w})*{pos}:(ih-{h})/2"
        cmd += ["-framerate", str(FPS), "-i", str(fotogrammi / "%04d.png")]
        filtro = (f"[1:v]fps={FPS},{adatta},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={d}[v];"
                  f"[0:v][v]overlay={b['x']}:{b['y']}[b];[b][2:v]overlay=0:0,format=yuv420p[out]")
    else:
        cmd += ["-framerate", str(FPS), "-i", str(fotogrammi / "%04d.png")]
        filtro = "[0:v][1:v]overlay=0:0,format=yuv420p[out]"
    cmd += ["-filter_complex", filtro, "-map", "[out]", "-t", str(d), "-r", str(FPS),
            "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-an", str(uscita)]
    esegui(cmd)
    return uscita


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    sorgente = pathlib.Path(args[0]).resolve()
    cartella = sorgente.parent
    scene = json.loads(sorgente.read_text(encoding="utf-8"))["scene"]
    fondi, giro = [], 0
    for s in scene:
        if s["tipo"] == "finale":
            fondi.append(s.get("fondo", "blu"))
        else:
            fondi.append(s.get("fondo", GIRO[giro % len(GIRO)]))
            giro += 1
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="reel-"))
    try:
        if "--anteprima" in sys.argv:
            immagini = []
            for i, s in enumerate(scene):
                dopo = fondi[i + 1] if i + 1 < len(scene) else None
                breve = dict(s, durata=min(s["durata"], 2.6))
                pezzo = scena_mp4(breve, fondi[i], None, cartella, tmp, i)
                img = tmp / f"ante-{i}.png"
                esegui(["ffmpeg", "-y", "-v", "error", "-sseof", "-0.1", "-i", str(pezzo), "-frames:v", "1",
                        "-vf", "scale=360:640", str(img)])
                immagini.append(img)
            ingressi = sum((["-i", str(x)] for x in immagini), [])
            esegui(["ffmpeg", "-y", "-v", "error", *ingressi, "-filter_complex",
                    f"hstack=inputs={len(immagini)}" if len(immagini) > 1 else "null", str(cartella / "reel-anteprima.png")])
            print("Creato", cartella / "reel-anteprima.png")
            return
        pezzi = []
        for i, s in enumerate(scene):
            dopo = fondi[i + 1] if i + 1 < len(scene) else None
            pezzi.append(scena_mp4(s, fondi[i], dopo, cartella, tmp, i))
            print(f"Scena {i + 1}/{len(scene)} pronta")
        elenco = tmp / "elenco.txt"
        elenco.write_text("".join(f"file '{p}'\n" for p in pezzi))
        esegui(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(elenco), "-c", "copy",
                "-movflags", "+faststart", str(cartella / "reel.mp4")])
        durata = sum(s["durata"] for s in scene)
        print(f"Creato {cartella / 'reel.mp4'} ({durata:.1f} secondi)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()

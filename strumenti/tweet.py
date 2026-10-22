"""Stile "tweet" di Scopri AI (deciso il 22/10/2026, ispirato ai post a forma di tweet di @evolving.ai):
fondo nero, font Inter, in alto il nostro "profilo" (foto profilo, "Scopri AI", "@scopri__ai"), il testo come in un post
e sotto la foto o il video vero. Si sceglie post per post al posto del carosello Electric Mono (format/6-stile-tweet.md).
Tu dai solo testi e media: il programma fa i file finiti.

Uso:
    python3 strumenti/tweet.py carousels/<slug>/tweet.json               → file finiti
    python3 strumenti/tweet.py carousels/<slug>/tweet.json --anteprima   → solo immagini ferme (in pochi secondi)
    python3 strumenti/tweet.py carousels/<slug>/tweet.json --overlay     → anche le cornici trasparenti per Canva/CapCut

Il JSON (si può avere solo "reel", solo "carosello" o tutti e due):
{
  "reel": {
    "testo": "Hanno chiesto a *6 AI* di progettare una capsula per salvare un uovo. Solo una ce l'ha fatta.",
    "video": "media/uovo.mp4", "inizio": 0, "durata": 12,     (inizio/durata facoltativi: senza, il video intero)
    "finestra": "auto",          (auto, 16:9 → alta 608, 4:5 → alta 864; auto sceglie dalla forma del video)
    "zoom": 1.0, "posizione": 0.5, "copertina": 1.0
  },
  "carosello": [
    {"tipo": "copertina", "titolo": "Una smart TV piena di pubblicità, *ripulita dall'AI*",
     "media": "media/tv.mp4", "inizio": 0, "durata": 8, "protagonista": "media/volto.jpg", "verticale": 0.5},
    {"tipo": "slide", "titolo": "Cosa è successo", "testo": "Due o tre frasi: chi, cosa, perché conta.",
     "media": "media/dopo.jpg", "adatta": "contain"}
  ]
}
Escono:
  reel      → <cartella>/reel.mp4 (+ reel-completo.mp4 se tagliato) e reel-copertina.jpg; con --anteprima reel-anteprima.png
  carosello → <cartella>/exports/slide-01.png … (le slide con un video anche slide-NN.mp4 e, se tagliato, slide-NN-completo.mp4)
              e exports/contact-sheet.jpg
Regole del disegno (format/6-stile-tweet.md): accento #8FA3FF in grassetto solo su 1–2 parole (*così*); titolo della
copertina in MAIUSCOLO, al massimo 3 righe; testo del Reel al massimo 3 righe; testo della slide al massimo 4 righe.
Se un testo è troppo lungo il programma si ferma. Foto e video sempre a colori, senza audio (la musica la mette il proprietario).
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
AVATAR = RADICE / "brand/logo/ufficiale/foto-profilo.png"
FPS = 30
ACCENTO, GRIGIO = "#8FA3FF", "#71767B"


def esegui(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Errore: {' '.join(map(str, cmd))[:300]}\n{r.stderr[-2000:]}")
    return r.stdout


def info_media(f):
    err = subprocess.run(["ffmpeg", "-i", str(f)], capture_output=True, text=True).stderr
    v = re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", err)
    if not v:
        sys.exit(f"Non riesco a leggere {f}")
    w, h = int(v.group(1)), int(v.group(2))
    if re.search(r"rotate\s*:\s*-?(90|270)|rotation of -?90", err):
        w, h = h, w
    d = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    video = f.suffix.lower() in (".mp4", ".mov", ".webm", ".m4v")
    durata = int(d.group(1)) * 3600 + int(d.group(2)) * 60 + float(d.group(3)) if (d and video) else 0
    return w, h, video, durata


def marca(testo, maiuscolo=False):
    """*parola* → parola chiave in #8FA3FF grassetto."""
    t = testo.upper() if maiuscolo else testo
    return re.sub(r"\*([^*]+)\*", r'<b class="hl">\1</b>', html.escape(t))


def testa(av, nome, handle, gap):
    return (f'<div style="display:flex;align-items:center;gap:{gap}px">'
            f'<img src="{AVATAR.as_uri()}" style="width:{av}px;height:{av}px;border-radius:50%;display:block;flex:none">'
            f'<div style="display:flex;flex-direction:column;line-height:1.15">'
            f'<span style="font:700 {nome}px Inter;color:#fff">Scopri AI</span>'
            f'<span style="font:400 {handle}px Inter;color:{GRIGIO}">@scopri__ai</span></div></div>')


def documento(W, H, interno):
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&amp;display=block" rel="stylesheet">
<style>html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:transparent;-webkit-font-smoothing:antialiased}}
.abs{{position:absolute}} b.hl{{color:{ACCENTO};font-weight:inherit}} .hl{{font-weight:700}}
.nero{{position:absolute;inset:0}}</style></head>
<body><div style="position:relative;width:{W}px;height:{H}px;font-family:Inter,'Noto Color Emoji',sans-serif">{interno}</div></body></html>'''


def maschera(W, H, x, y, w, h):
    """Tutto nero tranne la finestra della foto/video."""
    return (f'<svg width="{W}" height="{H}" class="nero"><path fill="#000" fill-rule="evenodd" '
            f'd="M0 0H{W}V{H}H0Z M{x} {y}H{x + w}V{y + h}H{x}Z"/></svg>'
            f'<div id="finestra" class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>')


def pagina_reel(r, alto):
    return documento(1080, 1920, maschera(1080, 1920, 0, 690, 1080, alto) +
                     f'<div class="abs" style="left:60px;top:300px">{testa(104, 40, 34, 22)}</div>' +
                     (f'<div class="abs" data-max="3" data-nome="testo del Reel" style="left:60px;top:440px;width:960px;'
                      f'font:500 48px/1.27 Inter;color:#fff;letter-spacing:-0.3px">{marca(r["testo"])}</div>' if r.get("testo") else ""))


LINEA_LOGO = (f'<div class="abs" style="left:0;top:858px;width:1080px;display:flex;align-items:center;justify-content:center;gap:22px">'
              f'<div style="width:250px;height:2px;background:rgba(255,255,255,.55)"></div>'
              f'<div style="display:flex;align-items:center;gap:6px;font:900 28px Inter;color:#fff;letter-spacing:1px">SCOPRI'
              f'<span style="background:{ACCENTO};color:#0B0E22;border-radius:6px;padding:1px 8px 2px">AI</span></div>'
              f'<div style="width:250px;height:2px;background:rgba(255,255,255,.55)"></div></div>')


def pagina_copertina(s, cartella):
    prot = ""
    if s.get("protagonista"):
        prot = (f'<div class="abs" style="left:70px;top:470px;width:300px;height:300px;border-radius:50%;border:6px solid #fff;'
                f'box-sizing:border-box;overflow:hidden;background:#111 url(\'{(cartella / s["protagonista"]).as_uri()}\') center/cover"></div>')
    sfumato = ('<div class="abs" style="left:0;top:480px;width:1080px;height:422px;'
               'background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.75) 60%,#000 100%)"></div>')
    return documento(1080, 1350, maschera(1080, 1350, 0, 0, 1080, 900) + sfumato + prot + LINEA_LOGO +
                     f'<div class="abs" data-max="3" data-nome="titolo della copertina" style="left:50px;top:915px;width:980px;'
                     f'text-align:center;font:900 70px/1.04 Inter;color:#fff;letter-spacing:-0.5px">{marca(s["titolo"], True)}</div>'
                     '<div class="abs" style="left:0;top:1288px;width:1080px;text-align:center;font:700 24px Inter;'
                     'color:rgba(255,255,255,.85);letter-spacing:3px">SCORRI PER SAPERNE DI PIÙ →</div>')


def pagina_slide(s):
    return documento(1080, 1350, maschera(1080, 1350, 0, 520, 1080, 608) +
                     f'<div class="abs" style="right:44px;top:40px">{testa(78, 30, 25, 14)}</div>' +
                     (f'<div class="abs" data-max="1" data-nome="titoletto" style="left:60px;top:200px;width:960px;font:800 40px/1.2 Inter;'
                      f'color:#fff;letter-spacing:-0.2px">{marca(s["titolo"], True)}</div>' if s.get("titolo") else "") +
                     (f'<div class="abs" data-max="4" data-nome="testo della slide" style="left:60px;top:262px;width:960px;'
                      f'font:400 34px/1.38 Inter;color:rgba(255,255,255,.92)">{marca(s["testo"])}</div>' if s.get("testo") else ""))


def fotografa(html_txt, W, H, tmp, nome):
    f = tmp / f"{nome}.html"
    f.write_text(html_txt, encoding="utf-8")
    png = tmp / f"{nome}.png"
    info = json.loads(esegui(["node", str(RADICE / "strumenti/tweet-pagina.cjs"), str(f), str(png), str(W), str(H)]).strip().splitlines()[-1])
    troppe = [f"{x['nome']}: {x['righe']} righe (massimo {x['max']})" for x in info["righe"] if x["righe"] > x["max"]]
    if troppe:
        sys.exit(f"{nome}: testo troppo lungo, accorcialo:\n  " + "\n  ".join(troppe))
    return png, info["finestra"]


def adatta(s, w, h, predefinito):
    zoom, pos, vert = float(s.get("zoom", 1)), float(s.get("posizione", .5)), float(s.get("verticale", .5))
    zw, zh = round(w * zoom / 2) * 2, round(h * zoom / 2) * 2
    if s.get("adatta", predefinito) == "contain":
        return (f"scale={zw}:{zh}:force_original_aspect_ratio=decrease,crop='min(iw,{w})':'min(ih,{h})',"
                f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1")
    return f"scale={zw}:{zh}:force_original_aspect_ratio=increase,crop={w}:{h}:(iw-{w})*{pos}:(ih-{h})*{vert},setsar=1"


def componi(cornice, W, H, fin, media, s, uscita, fermo=False, intero=False, predefinito="cover"):
    """Fondo nero → foto/video nella finestra → cornice (testi, maschera, sfumato) sopra."""
    w, h, video, durata = info_media(media)
    f = adatta(s, fin["w"], fin["h"], predefinito)
    if not video or fermo:
        if video:   # prima un fotogramma fermo: con il video diretto ffmpeg a volte non lo sovrappone
            fermo_png = uscita.with_name(uscita.stem + "-fermo-tmp.png")
            esegui(["ffmpeg", "-y", "-v", "error", "-ss", str(float(s.get("inizio", 0)) + 0.05), "-i", str(media),
                    "-frames:v", "1", "-update", "1", str(fermo_png)])
            media = fermo_png
        esegui(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"color=black:s={W}x{H}", "-i", str(media), "-i", str(cornice),
                "-filter_complex", f"[1:v]{f}[m];[0:v][m]overlay={fin['x']}:{fin['y']}[b];[b][2:v]overlay=0:0[out]",
                "-map", "[out]", "-frames:v", "1", "-update", "1", str(uscita)])
        if video:
            media.unlink()
        return None
    da = 0 if intero else float(s.get("inizio", 0))
    quanto = durata - da if intero or not s.get("durata") else min(float(s["durata"]), durata - da)
    esegui(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"color=black:s={W}x{H}:r={FPS}", "-i", str(media),
            "-loop", "1", "-i", str(cornice), "-filter_complex",
            f"[1:v]trim=start={da}:duration={quanto},setpts=PTS-STARTPTS,fps={FPS},{f}[m];"
            f"[0:v][m]overlay={fin['x']}:{fin['y']}:shortest=1[b];[b][2:v]overlay=0:0,format=yuv420p[out]",
            "-map", "[out]", "-t", str(quanto), "-r", str(FPS), "-c:v", "libx264", "-crf", "18", "-preset", "medium",
            "-an", "-movflags", "+faststart", str(uscita)])
    return quanto


def tagliato(s, media):
    _, _, video, durata = info_media(media)
    return video and (float(s.get("inizio", 0)) > 0 or (s.get("durata") and float(s["durata"]) < durata - 0.05))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    sorgente = pathlib.Path(args[0]).resolve()
    cartella = sorgente.parent
    dati = json.loads(sorgente.read_text(encoding="utf-8"))
    anteprima, overlay = "--anteprima" in sys.argv, "--overlay" in sys.argv
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="tweet-"))
    try:
        if dati.get("reel"):
            r = dati["reel"]
            media = cartella / r["video"]
            w, h, _, _ = info_media(media)
            scelta = r.get("finestra", "auto")
            alto = 864 if scelta == "4:5" or (scelta == "auto" and w / h < 1.2) else 608
            cornice, fin = fotografa(pagina_reel(r, alto), 1080, 1920, tmp, "reel")
            if overlay:
                shutil.copy(cornice, cartella / f"overlay-reel-{'4x5' if alto == 864 else '16x9'}.png")
            if anteprima:
                componi(cornice, 1080, 1920, fin, media, r, cartella / "reel-anteprima.png", fermo=True)
                print("Creato reel-anteprima.png")
            else:
                d = componi(cornice, 1080, 1920, fin, media, r, cartella / "reel.mp4")
                print(f"Creato reel.mp4 ({d:.1f} s)")
                if tagliato(r, media):
                    d = componi(cornice, 1080, 1920, fin, media, r, cartella / "reel-completo.mp4", intero=True)
                    print(f"Creato reel-completo.mp4 ({d:.1f} s)")
                esegui(["ffmpeg", "-y", "-v", "error", "-ss", str(min(float(r.get("copertina", 1.0)), 1e9)), "-i",
                        str(cartella / "reel.mp4"), "-frames:v", "1", "-q:v", "2", "-update", "1", str(cartella / "reel-copertina.jpg")])
                print("Creato reel-copertina.jpg")

        slides = dati.get("carosello") or []
        if slides:
            uscite = cartella / "exports"
            uscite.mkdir(exist_ok=True)
            for vecchio in uscite.glob("slide-*"):
                vecchio.unlink()
            for i, s in enumerate(slides, 1):
                nn = f"{i:02d}"
                copertina = s.get("tipo") == "copertina"
                pg = pagina_copertina(s, cartella) if copertina else pagina_slide(s)
                cornice, fin = fotografa(pg, 1080, 1350, tmp, f"slide-{nn}")
                if overlay and i <= 2:
                    shutil.copy(cornice, uscite / f"overlay-{'copertina' if copertina else 'slide-interna'}.png")
                if not s.get("media"):
                    shutil.copy(cornice, uscite / f"slide-{nn}.png")
                    continue
                media = cartella / s["media"]
                predefinito = "cover" if copertina else "contain"   # nelle slide interne le immagini si vedono intere
                componi(cornice, 1080, 1350, fin, media, s, uscite / f"slide-{nn}.png", fermo=True, predefinito=predefinito)
                if info_media(media)[2] and not anteprima:
                    d = componi(cornice, 1080, 1350, fin, media, s, uscite / f"slide-{nn}.mp4", predefinito=predefinito)
                    print(f"slide-{nn}.mp4 ({d:.1f} s)")
                    if tagliato(s, media):
                        componi(cornice, 1080, 1350, fin, media, s, uscite / f"slide-{nn}-completo.mp4", intero=True, predefinito=predefinito)
                print(f"slide-{nn}.png")
            pngs = sorted(uscite.glob("slide-[0-9][0-9].png"))
            esegui(["ffmpeg", "-y", "-v", "error", *sum((["-i", str(p)] for p in pngs), []), "-filter_complex",
                    "".join(f"[{k}:v]scale=360:450[s{k}];" for k in range(len(pngs))) +
                    "".join(f"[s{k}]" for k in range(len(pngs))) + f"hstack=inputs={len(pngs)}" if len(pngs) > 1 else "scale=360:450",
                    "-frames:v", "1", "-update", "1", str(uscite / "contact-sheet.jpg")])
            print("Creato exports/contact-sheet.jpg")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()

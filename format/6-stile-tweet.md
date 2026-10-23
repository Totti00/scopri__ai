# Stile 6 — "Tweet" (deciso il 22/10/2026)

Un secondo stile, **da scegliere post per post** al posto del carosello Electric Mono (la skill `scopri-carousel`). Ispirato ai post a forma di tweet di @evolving.ai: il formato lo usano tante pagine, da noi con foto profilo, nome, testi e titoli nostri (regola 7).
Il menu del `selezionatore` propone per ogni notizia lo stile: **carosello** o **tweet**. Decide il proprietario.

**Quando conviene:** notizie con una foto o un video vero forte, da raccontare in poco (2–4 slide, oppure solo un Reel). Il carosello Electric Mono resta per le storie lunghe, i prompt e le liste.

## Come si fa
Si scrive `carousels/<slug>/tweet.json` con solo testi e media, poi:
```bash
python3 strumenti/tweet.py carousels/<slug>/tweet.json --anteprima   # immagini ferme, pochi secondi (bozza)
python3 strumenti/tweet.py carousels/<slug>/tweet.json               # file finiti (finale)
python3 strumenti/tweet.py carousels/<slug>/tweet.json --overlay     # anche le cornici trasparenti per Canva/CapCut
```
Il formato del JSON è in cima a `strumenti/tweet.py`. Escono gli stessi file del carosello (il Reel con l'audio originale del video, le slide senza audio): `exports/slide-NN.png` (e `.mp4` per le slide con un video, più `-completo.mp4` se tagliato), `exports/contact-sheet.jpg`, e per il Reel `reel.mp4`, `reel-completo.mp4`, `reel-copertina.jpg`. Poi `publish.json` con `"stile": "tweet"` e `npm run publish` (o `python .claude/skills/scopri-carousel/scripts/publish-pack.py <cartella>`) per il pacchetto e il controllo della caption.

## Regole comuni
- Fondo nero `#000000`, font **Inter** (solo in questo stile; il carosello resta in Inter Tight).
- In alto il "profilo": la **foto profilo vera** (`brand/logo/ufficiale/foto-profilo.png`), "Scopri AI" Inter Bold bianco, "@scopri__ai" Inter Regular `#71767B`. Niente spunta blu.
- Accento **`#8FA3FF` in grassetto** solo su 1–2 parole chiave (`*così*` nel JSON). Su nero puro si vede bene: qui resta il lilla, non il riquadro blu dei caroselli.
- Foto e video veri, **sempre a colori**, senza audio (la musica strumentale la mette il proprietario).

## 1) Reel 1080×1920
- Profilo: foto 104 px a x 60, y 300; nome 40 px, @ 34 px.
- Testo da x 60, y 440, largo 960, Inter Medium 48 px, interlinea 1.27, bianco, **al massimo 3 righe** (il programma si ferma se sono di più).
- Video a tutta larghezza da y 690: alto 608 per i 16:9, 864 per i verticali (4:5) (`"finestra": "auto"` sceglie da solo). Sotto, nero.
- Il primo fotogramma è già il momento forte (`"inizio"`), come per tutti i Reel (`format/5-reel.md`).

## 2) Copertina del carosello 1080×1350
- Foto o video nei primi 900 px, sfumato verso il nero da y 480 a y 900.
- Facoltativa la foto del protagonista in un cerchio di 300 px con bordo bianco di 6 px, a x 70, y 470 (`"protagonista"`).
- A y 858: due linee bianche sottili (55%) di 250 px con al centro "SCOPRI" Inter Black 28 + "AI" in un riquadro `#8FA3FF` con testo `#0B0E22` (il marchio di questo stile).
- Titolo centrato da y 915, largo 980, Inter Black 70 px, **MAIUSCOLO**, interlinea 1.04, **al massimo 3 righe** (con 4 toccherebbe i pallini di Instagram, a y ~1232).
- In fondo, a y 1288: "SCORRI PER SAPERNE DI PIÙ →", Inter Bold 24, spaziatura 3 px, bianco 85%.

## 3) Slide interna 1080×1350
- Profilo piccolo in alto a destra (foto 78, nome 30, @ 25), a 44 px dal bordo destro e 40 dall'alto.
- Titoletto MAIUSCOLO Inter ExtraBold 40 a x 60, y 200 (una riga).
- Testo Inter Regular 34, interlinea 1.38, bianco 92%, da y 262, **al massimo 4 righe**.
- Foto o video a tutta larghezza da y 520, alto 608. Le immagini si vedono **intere** (`"adatta": "contain"`, è il valore di partenza nelle slide interne).
## 4) Slide di chiusura (dal 22/10/2026, sempre nei caroselli)
- Ultima slide di ogni carosello in stile tweet: `{"tipo": "chiusura", "titolo": …, "pulsante": …}` (formato in cima a `strumenti/tweet.py`). Fondo nero, il nostro profilo grande, titolo MAIUSCOLO con 1–2 parole in `*asterischi*`, un pulsante e, in fondo, la riga "🔔 Seguici per non perdere le prossime notizie". **Niente riga di testo sotto il pulsante** (tipo "Il messaggio da girare … è nei commenti": tolta dal proprietario il 22/10/2026).
- **L'invito deve essere coerente con il post** (deciso dal proprietario il 22/10/2026): per una notizia si invita a mandarla a chi le interessa (es. "Conosci qualcuno con *un sito*?" · "📩 Mandalo a chi ha un sito"); l'invito ai 100 prompt ("Vuoi i *100 prompt* per Claude?" · "📥 Commenta «100»") **solo quando il post parla di prompt**. Mai un invito messo a caso.

## Caption
- Prima riga: 1–2 emoji + frase a effetto, con le parole che la gente cerca, **al massimo 125 caratteri**.
- 3–5 paragrafi brevi, **al massimo 800 caratteri** in tutto.
- **Slide di solo testo** (23/10/2026): una slide interna senza "media" diventa una slide di testo grande (titoletto + fino a 16 righe, i paragrafi si separano andando a capo con \n).
- Chiusura, in quest'ordine: "Tu cosa ne pensi? 🤔💬", poi la fonte ("🎥: @autore" per un video, oppure "Fonti: …"), poi **l'invito, coerente con il post e uguale a quello della slide di chiusura** (22/10/2026): notizie e curiosità "📩 Mandalo a chi …"; post di prompt "📥 Commenta «100» e ti mando i 100 prompt per Claude in PDF.". Niente riga "🔔 Seguici".
- Massimo 5 hashtag, in fondo.
- `caption_check.py --stile tweet` (o `"stile": "tweet"` in `publish.json`) controlla tutto questo.

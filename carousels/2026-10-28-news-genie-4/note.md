# Note — Reel Genie 4 (finale, 28/10/2026)

## Versione scelta
- Solo Reel, niente carosello. Alla Fermata 2 il proprietario ha scelto «Tweet a, video intero con audio».
- Reel in **stile tweet**, versione A (`tweet.json`), testo invariato (3 righe): «Niente di questo è stato girato. Basta una frase e Genie 4, l'AI di Google, crea un *mondo a parte*.»
- Video **intero** `media/genie4-moto.mp4` (0–30,5 s, niente `inizio`/`durata`), finestra 4:5 (1080×864), zoom 1.0: il taglio toglie le bande nere ai lati e i tasti W/A/S/D e le frecce. Copertina a 24,4 s (il mostro grande con le esplosioni sopra la città, la strada, i due in moto di spalle).
- **Audio originale** del video, **niente musica**.
- Bozze non scelte, restano nella cartella: `reel.json` e `reel-b.json` (classiche, anteprime `reel-anteprima.png` e `reel-b-anteprima.png`) e `tweet-b.json` (anteprima `reel-tweet-b-anteprima.png`). Le quattro anteprime non sono state toccate (md5 controllato prima e dopo). `reel-tweet-anteprima.png` è della bozza: mostra il primo fotogramma del pezzo da 16,2 s, non quello del finale.

## File finali
- `reel.mp4`: 1080×1920, 30 fps, 30,5 s, H.264 High con audio AAC stereo 48 kHz 192 kbps (stesso livello dell'originale), 8,0 MB, faststart.
- `reel-volume-alto.mp4`: **lo stesso Reel con l'audio alzato** (vedi "Dubbi"), video identico (copiato senza ricomprimere), audio portato a circa -15 LUFS, picco -1 dB, 8,0 MB. Si pubblica uno dei due.
- `reel-copertina.jpg`: fotogramma a 24,4 s.
- Niente `reel-completo.mp4`: il Reel è già il video intero (`tweet.py` lo crea solo se si taglia).
- `caption-reel.txt`: approvata così com'è, CAPTION PRONTA (445 caratteri, prima riga 101).

## Controllo finale (voci del Reel di `brand/controllo-finale.md`)
- Formato 1080×1920: ok.
- Testi nella zona sicura: profilo e testo tra y 300 e y ~620, video da y 690 a y 1554, lontano dai pulsanti di Instagram: ok.
- Primo secondo: niente schermata nera, logo o persona che parla in camera. Sono i due ragazzi in moto sul ponte al tramonto, realistici: non è ancora il momento più forte (i tentacoli arrivano a 17,5 s, il mostro a 19,7 s), ma il proprietario ha chiesto il video intero da 0, e con il testo «Niente di questo è stato girato» i volti veri incuriosiscono già.
- Video bomba: sì (la città che esplode mentre la moto corre, niente di girato).
- Fotogrammi guardati (0, 3, 10, 17,5, 24,4, 30,4 s) e copertina: video a colori, senza bande nere né tasti, testo leggibile, accento `#8FA3FF` su "mondo a parte"; in fondo niente logo né schermata finale di altri.
- Un solo invito ("📩 Mandalo a chi crede a ogni video che vede"), la domanda "Tu cosa ne pensi? 🤔💬", niente 🔔 Seguici in caption, 5 hashtag: ok.
- Fonti solo in caption (video: Google DeepMind). Sul Reel nessun nome di autore.

## Dubbi e cautele
- **Audio molto basso**: l'originale di Google è a -32 LUFS (i Reel di solito stanno intorno a -14): sul telefono si sente appena. `reel.mp4` lo tiene com'è; `reel-volume-alto.mp4` è lo stesso video con l'audio alzato e un po' compresso (loudnorm di ffmpeg). Consiglio: pubblicare `reel-volume-alto.mp4`, dopo averlo ascoltato.
- **Avviso di Google**: "Results for illustrative purposes. Sequences shortened." è in basso nel video **per i primi 3 secondi** circa. Il taglio 4:5 non lo toglie (è dentro l'immagine), e con il video intero da 0 si vede. Va bene così: è l'avviso dell'autore e dice che la demo è accorciata (per questo nei testi niente "in diretta").
- "Circa 2 minuti" di scena coerente lo scrivono solo The Verge e TechCrunch, non Google: nel Reel e nella caption non c'è.
- Per ora Genie 4 lo usano **solo tester scelti** (poi abbonati Google AI Ultra e sviluppatori): la caption lo dice; nessun testo dice "scrivi" o "puoi provarlo".
- Il comando nel video è in inglese ("Gigantic alien tentacles that destroy the world."): la traduzione «tentacoli alieni giganti» è in caption.
- Durata 30,5 s, oltre gli 8–20 s consigliati: scelta del proprietario.
- «Basta una frase» semplifica un po': secondo la pagina di Google DeepMind il mondo iniziale della moto nasce da un prompt di solo testo di circa 120 parole ("A cinematic macro close-up from a 1995 Hong Kong indie romantic drama…"); le frasi singole sono le modifiche durante la scena ("Gigantic alien tentacles that destroy the world."). Lasciato così: testo e caption sono approvati e il gancio regge (i cambi a parole sono davvero una frase). «Niente di questo è stato girato» è esatto: nessuna immagine di partenza.
- Accento: "mondo a parte" è nel colore `#8FA3FF` ma non in grassetto (in `strumenti/tweet.py` la regola `b.hl{font-weight:inherit}` vince su `.hl{font-weight:700}`). Succede in tutti i tweet ed era così anche nell'anteprima approvata: il Reel resta com'è; la correzione di `tweet.py` (o della regola in `format/6-stile-tweet.md`) è da decidere a parte.
- Al proprietario vanno `reel-copertina.jpg` e `reel-volume-alto.mp4` (o `reel.mp4`), non le anteprime della bozza.

## Come è stato fatto
- `tweet.json`: tolti `inizio` (16,2) e `durata` (14,3), `copertina` da 8,3 a 24,4 (il tempo è quello del Reel, che ora parte da 0).
- `/usr/bin/python3 strumenti/tweet.py carousels/2026-10-28-news-genie-4/tweet.json` (senza `--anteprima`): scrive solo `reel.mp4` e `reel-copertina.jpg`, non tocca `reel-anteprima.png`.
- `reel-volume-alto.mp4`: `ffmpeg -i reel.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 (due passate) -c:a aac -b:a 192k`.

## Orario e musica
- Reel alle **20:00 di oggi, mercoledì 28/10/2026**.
- Musica: nessuna, audio originale del video (regola del 22/10/2026).

## Copertine alternative del Reel (28/10)
- `reel-copertina.jpg` (consigliata): 24,4 s del video, mostro grande ed esplosioni sulla città.
- `reel-copertina-b.jpg`: 19,9 s, il mostro dietro il casco bianco.
- `reel-copertina-c.jpg`: 27,2 s, i tentacoli sui grattacieli, di spalle.
Su Instagram: "Copertina" → "Aggiungi dal rullino" e scegli il file. Nella griglia del profilo il Reel si vede tagliato al centro (3:4): testo e video restano dentro.

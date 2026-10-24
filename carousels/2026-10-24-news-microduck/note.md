# Note — Reel Microduck (finale, 24/10/2026)

## Versione scelta
- Reel in **stile tweet**, versione A (`tweet.json`), con il testo corto chiesto dal proprietario alla Fermata 2: «Il regalo di Natale 2026? Un *paperotto robot*! Secondo Hugging Face ha già oltre 20.000 preordini.» Sta in 3 righe al primo tentativo.
- Video intero `media/microduck-nvidia.mp4` (0–67,1 s, niente inizio/durata), finestra 4:5 (alta 864), zoom 1.16 (toglie le bande sfocate di NVIDIA), copertina a 55 s (capriole davanti a Huang inginocchiato).
- **Audio originale** del video, **niente musica**.
- Bozze non scelte, restano nella cartella: `reel.json` e `reel-b.json` (classiche, anteprime `reel-anteprima.png` e `reel-b-anteprima.png`, non toccate: md5 controllato) e `tweet-b.json` (anteprima `reel-tweet-b-anteprima.png`). `reel-tweet-anteprima.png` è rifatta con il testo finale.

## File finali
- `reel.mp4`: 1080×1920, 30 fps, 67,1 s, H.264 con audio AAC stereo 192 kbps (stessi livelli dell'originale: media -24,4 dB, picco -4,8 dB), 15,6 MB, faststart.
- `reel-copertina.jpg`: fotogramma a 55 s.
- Niente `reel-completo.mp4`: il video è già intero (`tweet.py` lo crea solo se si taglia).
- Niente `reel-invio.mp4`: `reel.mp4` sta sotto i 30 MB.
- `caption-reel.txt`: CAPTION PRONTA (447 caratteri, prima riga 107).

## Controllo finale (voci del Reel di `brand/controllo-finale.md`)
- Formato 1080×1920: ok.
- Testi nella zona sicura: profilo e testo tra y 300 e y ~625, lontani dai pulsanti di Instagram: ok.
- Primo secondo: niente schermata nera, logo o persona che parla in camera. È l'inquadratura larga (Huang tra i robot umanoidi, paperotti piccoli in basso), non il momento più forte, ma il proprietario ha chiesto il video intero da 0. Le capriole sono a 54–58 s, Huang ne prende uno in mano a 62–66 s.
- Video bomba: il selezionatore aveva scritto «Reel: no per la regola stretta (tenero, non "ma è vero?")». Il Reel si fa per scelta del proprietario.
- Fotogrammi guardati (0, 20, 55, 64 s, ultimo) e copertina: video a colori, senza bande, testo leggibile; in fondo niente logo né schermata finale.
- Un solo invito ("📩 Mandalo a chi non sa ancora cosa regalare a Natale"), la domanda "Tu cosa ne pensi?", niente 🔔 Seguici in caption, 5 hashtag: ok.
- Fonti solo in caption (video: NVIDIA). Sul video c'è "Secondo Hugging Face": non è una fonte citata, serve a dire di chi è la stima dei preordini (regola 5).

## Cautele
- "Oltre 20.000 preordini" è una stima di Hugging Face (Clem Delangue: «probabilmente domani»): sempre "secondo Hugging Face".
- I paperotti sono di Pollen Robotics (Hugging Face), non di NVIDIA: NVIDIA ha il video e il palco.
- Prezzo in dollari: 399 più tasse e spedizione. La spedizione in Italia è da verificare.

## Come è stato fatto
- Lanciare `tweet.py` e `reel.py` con `/usr/bin/python3`: con il `python3` di /usr/local (3.11) Pillow non si carica.
- `tweet.py --anteprima` scrive sempre `reel-anteprima.png`: rinominata in `reel-tweet-anteprima.png` e rimessa a posto la classica (md5 uguale a prima).
- `tweet.py` tiene l'audio originale nel Reel (`audio=True`), nessuna correzione.
- `strumenti/reel.py` aggiornato nella bozza (24/10): tiene l'audio originale, accetta `"formato": "1080:760"` e la chiave `"audio"`.

## Orario e musica
- Reel alle **20:00 di oggi, 24/10/2026**.
- Musica: nessuna, audio originale del video (regola del 22/10/2026).

## Versione con il video di Hugging Face (24/10/2026, dopo la consegna)
- Il proprietario ha chiesto se si poteva usare il video del Reel di @evolving.ai. No: è una pagina concorrente (regola 4). Si è risaliti all'originale: il filmato grezzo "raw footage" pubblicato su X da Clem Delangue, CEO di Hugging Face, il 27/8/2026 (`fonti.md`).
- File: `tweet-hf.json` → `reel-hf.mp4` (83,1 s, dal secondo 2,6), `reel-hf-completo.mp4` (85,7 s, il video intero da 0, non va su GitHub), `reel-hf-copertina.jpg` (i quattro paperotti colorati, secondo 63,9 del Reel), `caption-reel-hf.txt`.
- Stesso testo del Reel NVIDIA. Il Reel parte dal secondo 2,6: nei primi 2,5 s la stanza è vuota con il titolo "Microduck RAW FOOTAGE" e il paperotto entra solo dopo; il video intero è in `reel-hf-completo.mp4`.
- Audio originale (rumori dei motori e le voci dei paperotti, media −26 dB); nessuna musica. Negli ultimi ~0,8 s il video originale sfuma nel nero.
- Nel video ci sono le scritte in inglese del filmato originale ("Balance recovery", "Floor picking", "Roller skating", "Chatting"): sono dell'autore, non nostre.
- Caption: `caption-reel-hf.txt`, CAPTION PRONTA (442 caratteri). Niente NVIDIA, perché il video non è quello del keynote.
- Il proprietario sceglie quale Reel pubblicare: NVIDIA (`reel.mp4`) o Hugging Face (`reel-hf.mp4`).

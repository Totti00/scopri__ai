# Note — Reel Microduck (bozza, 24/10/2026)

- Video intero come chiesto dal proprietario: 0–67,1 s. Niente fotogrammi neri (blackdetect) e niente logo finale: non ho tolto nulla.
- Il primo secondo è l'inquadratura larga (Huang tra i robot umanoidi, paperotti piccoli in basso): non è il momento più forte, ma il proprietario ha chiesto il video intero da 0. Le capriole sono a 54–58 s, Huang ne prende uno in mano a 62–66 s.
- Audio originale presente (AAC stereo, media -24 dB, picco -5 dB; tre pause di circa 1,5–2 s a 3, 10 e 52 s). Provato: finisce nel reel.mp4.
- `strumenti/reel.py` aggiornato il 24/10: tiene l'audio originale (prima usava `-an`, contro la regola del 22/10), accetta il rapporto su misura (`"formato": "1080:760"`) e la chiave `"audio"`.
- Pillow non funziona con `python3` (3.11 in /usr/local): lanciare `reel.py` con `/usr/bin/python3`.
- Cautele: "oltre 20.000 preordini" è una stima di Hugging Face; i paperotti sono di Pollen Robotics (Hugging Face), non di NVIDIA; prezzo in dollari, più tasse e spedizione; spedizione in Italia da verificare.
- Orario consigliato: 20:00. Musica: nessuna, audio originale.

## Reel in stile tweet (bozza, 24/10/2026)
- Richiesto dal proprietario in aggiunta alle versioni classiche (che restano: `reel.json`, `reel-b.json`, `reel-anteprima.png`, `reel-b-anteprima.png`, non toccate).
- `tweet.json` (versione A, idea b) → anteprima `reel-tweet-anteprima.png`; `tweet-b.json` (versione B, capriola + preordini) → `reel-tweet-b-anteprima.png`. `tweet.py --anteprima` scrive sempre `reel-anteprima.png`: rinominata subito e rimessa a posto quella classica (controllato con md5).
- Video intero (0–67,1 s, niente inizio/durata), finestra 4:5 (alta 864) scelta da "auto" per il video quadrato, `zoom` 1.16: toglie del tutto le bande sfocate di NVIDIA sopra e sotto (taglia solo un po' i lati). Copertina a 55 s (capriole davanti a Huang inginocchiato).
- Audio: `tweet.py` tiene già l'audio originale nel Reel (`audio=True` per reel.mp4 e reel-completo.mp4), nessuna correzione. Provato con un taglio di 3 s in una cartella di prova: traccia AAC presente nel reel.mp4.
- Testo A al primo tentativo: 3 righe. Testo B: la prima versione ("…oltre 20.000 persone hanno già prenotato questo paperotto robot") faceva 4 righe, accorciata.
- Lanciare `tweet.py` con `/usr/bin/python3` (come `reel.py`).
- Per il finale: la caption va rifatta con la chiusura dello stile tweet ("Tu cosa ne pensi? 🤔💬", "🎥: @NVIDIARTXSpark" o "Fonti: …", poi "📩 Mandalo a chi non sa ancora cosa regalare a Natale") e controllata con `caption_check.py --stile tweet --formato reel`.

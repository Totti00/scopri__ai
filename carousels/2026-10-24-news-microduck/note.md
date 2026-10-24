# Note — Reel Microduck (bozza, 24/10/2026)

- Video intero come chiesto dal proprietario: 0–67,1 s. Niente fotogrammi neri (blackdetect) e niente logo finale: non ho tolto nulla.
- Il primo secondo è l'inquadratura larga (Huang tra i robot umanoidi, paperotti piccoli in basso): non è il momento più forte, ma il proprietario ha chiesto il video intero da 0. Le capriole sono a 54–58 s, Huang ne prende uno in mano a 62–66 s.
- Audio originale presente (AAC stereo, media -24 dB, picco -5 dB; tre pause di circa 1,5–2 s a 3, 10 e 52 s). Provato: finisce nel reel.mp4.
- `strumenti/reel.py` aggiornato il 24/10: tiene l'audio originale (prima usava `-an`, contro la regola del 22/10), accetta il rapporto su misura (`"formato": "1080:760"`) e la chiave `"audio"`.
- Pillow non funziona con `python3` (3.11 in /usr/local): lanciare `reel.py` con `/usr/bin/python3`.
- Cautele: "oltre 20.000 preordini" è una stima di Hugging Face; i paperotti sono di Pollen Robotics (Hugging Face), non di NVIDIA; prezzo in dollari, più tasse e spedizione; spedizione in Italia da verificare.
- Orario consigliato: 20:00. Musica: nessuna, audio originale.

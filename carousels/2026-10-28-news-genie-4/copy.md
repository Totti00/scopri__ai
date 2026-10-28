# Genie 4 di Google: una frase e l'AI crea un mondo a parte (finale, 28/10/2026)

## Versione finale (approvata alla Fermata 2: «Tweet a, video intero con audio»)
- **Tweet A** (`tweet.json`), testo invariato (3 righe): "Niente di questo è stato girato. Basta una frase e Genie 4, l'AI di Google, crea un *mondo a parte*."
- Video: la demo della moto **intera**, da 0 a 30,5 s, con l'audio originale (niente musica). Finestra 4:5 (1080×864), zoom 1.0:
  niente bande nere né tasti W/A/S/D. Nei primi 3 s resta l'avviso di Google "Results for illustrative purposes. Sequences shortened." (è dentro l'immagine).
- Copertina: fotogramma a 24,4 s (il mostro grande con le esplosioni sopra la città, i due in moto di spalle).
- File: `reel.mp4` (30,5 s, audio originale com'è, molto basso: -32 LUFS), `reel-volume-alto.mp4` (stesso video, audio alzato a circa -15 LUFS: consigliato), `reel-copertina.jpg`, `caption-reel.txt` (approvata così com'è, CAPTION PRONTA). Niente `reel-completo.mp4`: il Reel è già intero.
- Al proprietario: `reel-copertina.jpg` e `reel-volume-alto.mp4` (o `reel.mp4`). Le anteprime `reel-*-anteprima.png` sono della bozza (la tweet A partiva da 16,2 s).
- Esce **oggi, mercoledì 28/10, alle 20:00**. Dettagli in `note.md`, fonti in `fonti.md`.

---
Sotto, la bozza com'era (le altre tre versioni restano nella cartella, non costruite).


Solo Reel, niente carosello. Scelta del proprietario: notizia 1, "r2 reel", ma con una frase nuova e d'impatto
sull'idea «una frase e l'AI crea un mondo a parte» (il titolo r2 "Una frase, e arrivano i tentacoli" non si usa).
Esce mercoledì 28/10 alle 20:00.

## Video
- Demo ufficiale Google DeepMind "moto e tentacoli" (`wm_genie4_demo_motorcycle_hero_UI_with_disclaimer_16x9_final.webm`,
  30,5 s, 1920×1080, con audio), convertita in `media/genie4-moto.mp4` (H.264 + AAC, audio originale).
- Il video vero è un riquadro 4:3 al centro, con bande nere ai lati e i tasti W/A/S/D e le frecce. Le bande e i tasti
  si tolgono col taglio: `"formato": "1340:1080"` nelle classiche, finestra del tweet (1080×864) nel tweet (non serve lo zoom).
  Il riquadro del comando scritto ("Gigantic alien tentacles that destroy the world.") è dentro l'immagine e resta:
  nel momento A si legge la frase intera nel primo secondo, ed è proprio l'idea del titolo.
- La scritta di avviso di Google ("Results for illustrative purposes. Sequences shortened.") c'è solo nei primi secondi:
  nei pezzi scelti non si vede (resta in `reel-completo.mp4`). [Superato nel finale: col video intero da 0 l'avviso si vede nei primi 3 s, e `reel-completo.mp4` non c'è.]
- Due momenti:
  - **A, da 16,2 s a 30,5 s (14,3 s):** si apre con la frase intera nel riquadro ("…that destroy the world.") e le
    esplosioni sul fiume; a 17,5 s arrivano i tentacoli, a 19,7 s il mostro, poi esplosioni sulla città fino in fondo.
  - **b, da 19,7 s a 30,5 s (10,8 s):** si apre col mostro gigante che si alza nella polvere accanto al casco; poi
    tentacoli, esplosioni e la moto che corre verso la città.
- Copertina di tutte e quattro: il fotogramma a 24,5 s del video (il mostro con le esplosioni sopra la città, la strada,
  i due in moto di spalle) → `"copertina"` 8.3 nelle versioni A, 4.8 nelle versioni b.

## Le 4 versioni
1. **Classica A** (`reel.json` → `reel-anteprima.png`), l'idea del proprietario quasi alla lettera
   - sopra: "Google Genie 4"
   - titolo: "Una frase e l'AI crea / un *mondo a parte*"
   - momento A (16,2 s, 14,3 s)
2. **Classica b** (`reel-b.json` → `reel-b-anteprima.png`), più secca, a contrasto
   - sopra: "Niente di questo è stato girato"
   - titolo: "Una frase sola. / Un *mondo intero*." (spazio fisso tra "Un" e "mondo" per andare a capo dopo "sola.")
   - momento b (19,7 s, 10,8 s)
3. **Tweet A** (`tweet.json` → `reel-tweet-anteprima.png`)
   - testo (3 righe): "Niente di questo è stato girato. Basta una frase e Genie 4, l'AI di Google, crea un *mondo a parte*."
   - momento A (16,2 s, 14,3 s)
4. **Tweet b** (`tweet-b.json` → `reel-tweet-b-anteprima.png`)
   - testo (3 righe): "Questo mondo non esiste: lo crea Genie 4, l'AI di Google. Basta *una frase* e la città cambia mentre ci giri dentro."
   - momento b (19,7 s, 10,8 s)

Scartati: "Una frase, e arrivano i tentacoli" (r2, da cambiare per il proprietario) · "Scrivi una frase. / L'AI crea un *mondo*"
(troppo simile alla A, e "Scrivi" fa pensare che si possa già provare) · "Ora puoi creare il tuo mondo"
(falso: per ora solo tester) · "Google crea mondi infiniti" (falso: le scene restano coerenti circa 2 minuti).

## Caption del Reel (`caption-reel.txt`, approvata così com'è)
Stile tweet (domanda → fonti → invito). `caption_check.py --stile tweet --formato reel --parole "genie,google"`:
✅ CAPTION PRONTA · reel · notizia — 445/2200 caratteri · 5 hashtag · invito: 📩 Mandalo a … · domanda: sì · fonti: sì
```
🌍🤯 Genie 4 di Google: basta una frase e l'intelligenza artificiale crea un mondo intero da esplorare.

Niente di questo è stato girato: qualcuno scrive «tentacoli alieni giganti» e la città cambia mentre la moto corre.

Per ora lo provano solo tester scelti.

Tu cosa ne pensi? 🤔💬

Fonti: Google DeepMind (video), The Verge, TechCrunch

📩 Mandalo a chi crede a ogni video che vede

#intelligenzaartificiale #google #genie4 #deepmind #videogiochi
```
Se il proprietario sceglie una classica, stesse righe con l'ordine classico (invito, domanda, poi "Fonti: …" in fondo
prima degli hashtag): controllata anche così, ✅ CAPTION PRONTA (445 caratteri).

## Cautele
- È una demo di Google: per ora Genie 4 lo usano solo tester scelti (poi abbonati Google AI Ultra e sviluppatori).
  Nessun titolo dice "scrivi" o "puoi provarlo".
- Il mondo è generato, non girato. "Circa 2 minuti" di scena coerente lo scrivono The Verge e TechCrunch, non Google (qui non serve).
- La demo è accorciata (lo dice l'avviso di Google, che col taglio non si vede): niente "in diretta" nei testi.
- Il comando nel video è in inglese: la traduzione «tentacoli alieni giganti» è in caption.

## Per il finale
- Costruire solo la versione scelta: `reel.py` (con `/usr/bin/python3`) e `tweet.py` scrivono gli stessi file
  (`reel.mp4`, `reel-completo.mp4`, `reel-copertina.jpg`).
- Scrivere `fonti.md` (Google DeepMind con il link del .webm, The Verge, TechCrunch, consultati il 28/10/2026) e `note.md`
  (orario 20:00, musica: audio originale, nota sull'avviso "Sequences shortened" tolto col taglio).

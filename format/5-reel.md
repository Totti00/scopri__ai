# Rubrica 5 — Reel "video bomba" (rifatta il 16/10/2026)

**Un Reel si fa solo quando c'è un video vero che è una bomba**: un video che fa dire "ma è vero?" anche senza audio e senza spiegazioni (un robot che fa una cosa incredibile, una demo che lascia a bocca aperta). Se il video è solo carino, niente Reel: basta il carosello.
Non è più "ogni post ha il suo Reel": può esserci un carosello senza Reel, un Reel senza carosello, o tutti e due. Lo propone il menu, decide il proprietario.

## Com'è fatto (semplice, veloce, cattura subito)
Una sola schermata 1080×1920, niente scene e niente animazioni:
- in alto **solo il logo** Scopri AI, con un po' di spazio prima del titolo: **niente etichette** come "NEWS LAMPO" (deciso il 16/10/2026);
- un **titolo corto e grande** (22/10/2026, come le copertine): una riga piccola sopra (`"sopra"`) e il titolo in **2 righe da 3–6 parole** (al massimo 10 parole), con la parola chiave nel **riquadro blu** (`*così*`). Dice **cosa ha fatto l'AI**, come le slide;
- sotto, il **video vero**, **sempre a colori** (16/10/2026; dal 20/10/2026 a colori anche nelle slide), in un riquadro con gli angoli arrotondati; il blocco sta al centro dello schermo;
- con l'audio originale del video (deciso il 22/10/2026: il Reel senza audio non va). Se il video non ha audio, la musica strumentale la mette il proprietario.

Lo fa `strumenti/reel.py` (istruzioni in cima al file) dal file `reel.json`, nella cartella del post (`carousels/<slug>/`):
```json
{"sopra": "Le è bastato guardare un video.", "titolo": "Un *robot* fa centro da solo",
 "video": "media/robot.mp4", "inizio": 31.3, "durata": 10, "zoom": 1.24, "copertina": 1.5}
```
- `python3 strumenti/reel.py <cartella>/reel.json --anteprima` → `reel-anteprima.png` (pochi secondi), con il **primo fotogramma** del video: si vede subito se il Reel parte bene;
- `python3 strumenti/reel.py <cartella>/reel.json` → `reel.mp4` (il pezzo migliore), `reel-completo.mp4` (il video intero, per tagliare da soli) e `reel-copertina.jpg`.

## Regole
- **Il primo secondo è già il momento forte.** Niente loghi, titoli di altri, persone che parlano in camera o schermate nere all'inizio: si sceglie `inizio` guardando una griglia di fotogrammi (un fotogramma al secondo con ffmpeg).
- **Durata:** il pezzo migliore, di solito 8–20 secondi (corto = lo guardano fino in fondo e ripartono). Il video intero va comunque consegnato.
- **Video vero e originale** (regola 4 di `CLAUDE.md`): dal post dell'azienda o dell'autore, mai da pagine che ripubblicano. Se il video ha bordi o scritte sue, si tolgono con `zoom`.
- **Zona sicura:** i testi stanno tra y 230 e y 1440 (sotto y 1000 anche lontano dal bordo destro, dove ci sono i pulsanti). Il programma si ferma se un testo esce.
- **Tecnica presa da altre pagine, identità nostra:** il formato "titolo + video" lo usano anche altri (es. ai__facile); da noi grafica Electric Mono, logo, parole e titoli nostri (regola 7).
- **Il video si vede intero** (deciso il 19/10/2026): `"formato": "originale"`, niente tagli sopra e sotto. Se il video è verticale il riquadro si stringa in larghezza (lo fa `reel.py`). Gli altri formati (4:5, 1:1) solo se lo chiede il proprietario. Per i video verticali si aggiunge `"compatto": true`: tutto più in alto e video più grande, fino quasi al fondo (19/10/2026).
- **Quattro versioni** nella bozza (24/10/2026): due classiche con due titoli diversi (o due momenti del video) → `reel.json` e `reel-b.json`, più **sempre** due in stile tweet (`format/6-stile-tweet.md`) → `tweet.json` e `tweet-b.json`. Sceglie il proprietario.

## Quando esce
Alle **20:00**: lo stesso giorno della news, oppure da solo se la notizia è solo il video.

## Caption del Reel
`caption-reel.txt`, regole in `brand/crescita.md` ("Caption del carosello e caption del Reel"): chi guarda il Reel non ha visto le slide. Si controlla con `caption_check.py` (deve dire CAPTION PRONTA).

## Prima del 16/10/2026
Reel a scene in motion graphics di 20 secondi: lo strumento è in `_vecchio/strumenti/reel-scene.py` (e quello ancora prima in `_vecchio/strumenti/reel.py`). Non si usano più.

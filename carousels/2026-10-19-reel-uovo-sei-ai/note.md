# Note — Reel "sei AI e la capsula per l'uovo" (19/10/2026, bozza)

Solo Reel, niente carosello. Fonte unica accettata dal proprietario: prova di un creator (Roberto Nickson, "Agent Wars" ep. 3, X 16/10), non notizia ufficiale. Autore solo in "Fonti".

## Versioni
- `reel.json` (r1): inizio 96,1 s, durata 8,2 s (fino a 104,3). Parte con la capsula già in caduta dal soppalco a 20 piedi, atterraggio, uovo estratto intatto ("egg survived"), campo largo sull'altezza. Taglio 4:5, zoom 1.12.
- `reel-b.json` (r2): inizio 92,0 s, durata 12,3 s (fino a 104,3). Parte con l'uovo intatto in mano dopo i 12 piedi, poi si sale a 20 piedi, metro, caduta, uovo intatto. Zoom 1.3, posizione 0.9 (toglie il riquadro piccolo dell'autore in basso a sinistra; ne resta un angolino nel primo secondo).
- Si chiude prima di 104,4 s: dopo c'è la scheda "Winner Claude Opus 5.5" dell'autore (grafica sua, non si usa).

## Verifiche sul video
- "stampato" non è corretto per l'AI: le AI hanno progettato il file, la stampa 3D l'ha fatta il creator. Nel titolo r2 → "ha progettato".
- Le altre cinque: Gemini, Grok, Meta e GPT-6 crepati, Qwen spiaccicato. "Rotto" regge; "molto prima" perché hanno ceduto a 1,2 m (GPT-6 a 2,4 m).
- Restano le scritte piccole dell'autore al centro ("UNSCATHED EGG", "EGG SURVIVED", "20 FEET"): sono sottotitoli in inglese, non si tolgono con lo zoom senza perdere l'uovo.

## Bozza caption Reel (19/10, dopo le correzioni: tutte e 6 le AI nella prima riga; CAPTION PRONTA, 445 caratteri)
```
Claude, ChatGPT, Gemini, Grok, Meta AI e Qwen: sei intelligenze artificiali hanno progettato una capsula per salvare un uovo che cade.

Stessi materiali per tutte. Claude regge da 6 metri, ChatGPT da 2,4, le altre da 1,2. È la prova di un creator.

📩 Mandalo a chi dice che le AI sono tutte uguali. Su quale avresti scommesso?

Fonti: Roberto Nickson (@rpnickson) su X, "Agent Wars" ep. 3

#intelligenzaartificiale #claude #chatgpt #stampa3d #ai
```

## Scelta del proprietario (fermata 2)
- Versione B, con *Claude* in blu nel titolo oltre a *6 metri* e *molto prima*.
- Caption: nominare tutte e 6 le AI all'inizio.
- Prima del finale vuole sapere quanto dura il video intero (109,8 s).

## Uscita
Oggi 19/10 alle 20:00. Musica: strumentale, elettronica carica o "suspense che esplode" (da scegliere in finale, controllando `brand/musica-usata.md`).

## Finale (19/10/2026)
- Scelta: versione B. `reel-b.json` è diventato il file del Reel finale ed è copiato identico in `reel.json` (da cui escono `reel.mp4` e `reel-copertina.jpg`). La vecchia versione A (inizio 96,1 s, zoom 1.12) è in `reel-a.json` / `reel-a-anteprima.png`. `reel-b-anteprima.png` mostra ancora il pezzo 92 s della bozza.
- Video **intero** (109,8 s, dall'inizio alla scheda finale dell'autore): niente `inizio`/`durata`, quindi niente `reel-completo.mp4` (`reel.mp4` è già il video intero). Taglia il proprietario.
- Zoom 1.0, posizione 0.5 (al posto di 1.3 / 0.9, scelti solo per 92–104 s): su tutto il video le capsule e le uova restano dentro. Il riquadro è 952×938 e il video sorgente è verticale (9:16): il programma taglia sopra e sotto al centro, quindi si vede la fascia centrale (~55% dell'altezza). Si perdono le etichette dell'autore in alto ("Anthropic · Claude Opus 5.5", altezza "20ft"); restano i suoi sottotitoli al centro e il riquadrino con la ripresa da un'altra angolazione in basso o in alto a sinistra in alcuni pezzi (anche a 101 s, in alto a sinistra).
- Copertina: 101,6 s (uovo intatto in mano, "EGG SURVIVED"), più nitida di 101,0 s (mano mossa).
- Senza audio. `reel.mp4` pesa ~64 MB: per mandarlo c'è `reel-invio.mp4` (ricompresso, CRF 25, fuori da git con `.git/info/exclude`).
- Caption: `caption-reel.txt`, CAPTION PRONTA (445 caratteri, 5 hashtag).

## Musica consigliata (solo strumentale; né Daft Punk né Justice, già usati)
1. **M83 – Outro**: parte lenta e cresce fino a esplodere ("suspense che esplode"), perfetta per la caduta da 6 metri; usare il pezzo dove entra la batteria.
2. **Moderat – A New Error**: elettronica carica, strumentale, ritmo dall'inizio.
3. **Kavinsky – Rampage**: synth carico, strumentale.
Se tra i brani ↗ di tendenza c'è uno strumentale adatto, ha la precedenza. Il brano scelto va scritto in `brand/musica-usata.md`.

## Musica usata
- da confermare (consigliato: M83 – Outro)

## Orario
Oggi 19/10/2026 alle **20:00**.

## Correzione del proprietario (19/10, dopo il finale)
- Vuole il video tutto dentro il riquadro, senza tagli: `formato` "originale", zoom 1.0. `reel.py` ora stringe il riquadro quando il video è alto (riquadro 526×935). Così si leggono anche le etichette dell'autore con il nome di ogni AI. Rifatti reel.mp4 (42 MB), reel-invio.mp4 (19 MB) e reel-copertina.jpg (101,6 s).
- Seconda correzione: "più grande, tutto più in alto" → `"compatto": true` (logo a y 232, spazi stretti, video fino a y 1880). Riquadro 650×1156. Larghezza piena (952) col video intero non ci sta: servirebbero 1692 px di altezza.

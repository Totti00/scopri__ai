# Template dei caroselli

Ogni post può usare un template diverso. Si sceglie post per post.

| Template | Com'è | Nel JSON |
|---|---|---|
| **A · Classico** | Logo in alto, titolo e testo sopra, immagine o video in un riquadro arrotondato sotto. Slide interne color carta. | `"stile": "A"` |
| **B · Fascia** | Immagine o video a tutta larghezza in alto, fascia di colore sotto (blu → carta → giallo, a giro), commento nel fumetto a cavallo tra le due. Chiusura gialla. | `"stile": "B"` |

Il font è lo stesso per tutti i template: **Bricolage Grotesque** (scelto il 15/10/2026), nella costante `FONT` di `strumenti/carosello.py`. Il logo resta in Space Grotesk.

## Chiusura fissa (scelta il 15/10/2026)
Tutti i post, in qualsiasi template, finiscono con la stessa slide: lo smartphone con la notifica di Scopri.AI, "Le novità sull'AI, appena escono." e gli inviti "🔔 Segui @scopri__ai e attiva le notifiche" / "📌 E salva il post per ritrovarlo". Nel JSON: `{"tipo": "chiusura"}`. File: `chiusura-notifica.dc.html`, anteprima `chiusura-notifica.png`.

## Come si lavora a un post (deciso il 15/10/2026)
1. Si decide la notizia e Claude scrive i testi: cosa ha fatto l'AI, in poche parole, più un commento di due o tre parole per slide.
2. **Bozza su Claude Design, senza video.** Claude crea un canvas con le slide del post in **ogni template** (un fotogramma al posto del video) e manda il link.
3. Il proprietario sceglie il template e corregge testi e grafica sul canvas.
4. Solo quando il proprietario dice che va bene, Claude crea le slide vere con `strumenti/carosello.py` (`"stile"` scelto, video veri, `--completi`).

## I file di questa cartella
- `A-classico/` e `B-fascia/`: le slide in formato Claude Design (`.dc.html`) da copiare in un nuovo canvas, più le anteprime PNG.
- Le immagini dentro i `.dc.html` puntano agli allegati del canvas del 15/10 (`/_blob/…`): in un canvas nuovo vanno caricate di nuovo e sostituite.

Esempio: canvas del post su Gemini 4 Argon — https://claude.ai/artifact/UD5TAg44jgWMUH71UWX4x2

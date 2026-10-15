# Template dei caroselli

Ogni post può usare un template diverso. Si sceglie post per post.

| Template | Com'è | Nel JSON |
|---|---|---|
| **A · Classico** | Logo in alto, titolo e testo sopra, immagine o video in un riquadro arrotondato sotto. Slide interne color carta. | `"stile": "A"` |
| **B · Fascia** | Immagine o video a tutta larghezza in alto, fascia di colore sotto (blu → carta → giallo, a giro), commento nel fumetto a cavallo tra le due. Chiusura gialla. | `"stile": "B"` |
| **C · Telefono grande** | Telefono o computer ufficiale grande, inclinato, che esce dal bordo in basso, su un cerchio di colore. Sopra titolo e testo breve, numero di slide (02/06) e barra di avanzamento. Fumetto sul bordo del telefono. Fondi: carta, giallo, blu. | solo Claude Design (`.dc.html`) |
| **D · Numero gigante** | Una parola o una cifra enorme è la protagonista ("IDEA → APP", "SOLO TU", "18+ USA", "Presto"); testo corto sotto, ritagli con bordo e ombra (stile adesivo), stelline, etichette gialle. Fondi: carta, giallo, blu. | solo Claude Design (`.dc.html`) |
| **E · Foto a tutta slide** | Immagine a pieno campo (anche ingrandita su un dettaglio) con sfumatura blu in basso, titolo grande sovrapposto con evidenziatore giallo sulla parola chiave, fumetto e freccia di scorrimento. | solo Claude Design (`.dc.html`) |
| **F · Carta a blocchi** | Fondo carta a quadretti, blocchi arrotondati con bordo nero e ombra (titolo con icona, testo, immagine con nastro adesivo), passi numerati 1-2-3-4 in alto, commento come adesivo. Copertina blu a quadretti. | solo Claude Design (`.dc.html`) |

Per C, D, E, F (aggiunti il 15/10/2026, su richiesta del proprietario: "troppi pochi template") le anteprime sono in `template/<cartella>/anteprima.png`; `strumenti/carosello.py` per ora sa fare solo A e B, quindi le slide finali di questi quattro si costruiscono dal `.dc.html` (da portare in `carosello.py` solo se il proprietario ne sceglie uno).

Il font è lo stesso per tutti i template: **Bricolage Grotesque** (scelto il 15/10/2026), nella costante `FONT` di `strumenti/carosello.py`. Il logo resta in Space Grotesk.

## Template E: colore di partenza a rotazione (deciso il 15/10/2026)
Il template E esiste in tre colori di partenza: **blu** (`E-foto-piena/`), **bianco** (`E-foto-piena-bianco/`) e **giallo** (`E-foto-piena-giallo/`). Cambiano fondo, velo, testo, evidenziatore, fumetto e freccia; nel bianco e nel giallo le slide interne alternano le altre tinte. Il testo ha sempre contrasto almeno 4.5:1 (controllato dallo script).

**Regola: ogni post sceglie template E e colore di partenza (blu, bianco, giallo) a rotazione: non iniziare due post di fila con lo stesso colore.** Così il profilo non parte sempre dal blu.

**Ultimo colore usato: bianco** (post Google Play, 15/10/2026). Aggiornare questa riga a ogni post che usa il template E. Prossimo post: blu o giallo.

Per cambiare palette o aggiungere un colore si tocca un solo punto: le costanti `TINTE` e `VARIANTI` in testa a `strumenti/varianti-e.py` (`python3 strumenti/varianti-e.py <cartella-bozza>` rigenera E, EB ed EG nella bozza e controlla i contrasti).

## Ultima slide: il terminatore
Tutti i post finiscono con il **terminatore attuale**, in qualsiasi template. I terminatori (attuale e vecchi) sono in `terminatori/`, con le istruzioni per cambiarlo.

## Come si lavora a un post (deciso il 15/10/2026)
1. Si decide la notizia e Claude scrive i testi: cosa ha fatto l'AI, in poche parole, più un commento di due o tre parole per slide.
2. **Bozza su Claude Design, senza video.** Claude crea un canvas con le slide del post in **ogni template** (un fotogramma al posto del video) e manda il link, insieme all'anteprima del Reel (`reel-anteprima.png`).
3. Il proprietario sceglie il template e corregge testi e grafica sul canvas.
4. Solo quando il proprietario dice che va bene, Claude crea le slide vere con `strumenti/carosello.py` (`"stile"` scelto, video veri, `--completi`).

## I file di questa cartella
- `A-classico/`, `B-fascia/`, `C-telefono-grande/`, `D-numero-gigante/`, `E-foto-piena/` (più `E-foto-piena-bianco/` e `E-foto-piena-giallo/`) e `F-carta-blocchi/`: le slide in formato Claude Design (`.dc.html`) da copiare in un nuovo canvas, più le anteprime PNG. Le cartelle C-F hanno `copertina`, `slide` (con immagine), `slide-numero` (con cifra grande) e `chiusura`, e una cartella `img/` con le immagini d'esempio, richiamate con `src="img/…"`.
- Le immagini dentro i `.dc.html` puntano agli allegati del canvas del 15/10 (`/_blob/…`): in un canvas nuovo vanno caricate di nuovo e sostituite.

Esempio: canvas del post su Gemini 4 Argon — https://claude.ai/artifact/UD5TAg44jgWMUH71UWX4x2

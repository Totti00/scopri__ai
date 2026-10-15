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

## Colori di partenza: tutti i template in blu, bianco e giallo (deciso il 15/10/2026)
Ogni template (A, B, C, D, E, F) e la slide di chiusura esistono in **tre colori di partenza**: **blu**, **bianco** (carta) e **giallo**. Cambiano solo i colori (fondo, cerchi, evidenziatori, fumetti, frecce, testo, logo); il disegno è lo stesso. Il testo ha sempre contrasto almeno 4.5:1 (scuro su bianco e giallo, chiaro su blu). Nelle slide interne le tinte alternano (non sono tutte uguali), come nel template E.

**Regola (vale per tutti i template e per la slide di chiusura): il colore di partenza lo sceglie il `costruttore-post`, non il proprietario, che sceglie solo il template.** Guarda la tabella qui sotto e i post già fatti, non ripete l'ultimo colore usato da quel template, e tra gli altri prende quello che sta meglio con la notizia e con le immagini, scrivendo il motivo in una riga. Così il profilo non parte sempre dal blu. Nella bozza ogni template compare in quel solo colore; la chiusura ruota per conto suo (ha la sua riga nella tabella).

| Template | Blu | Bianco | Giallo | Come sono le interne (copertina → slide 2-5) |
|---|---|---|---|---|
| **A · Classico** | `A-classico/` | `A-classico-bianco/` | `A-classico-giallo/` | blu → carta, carta, carta, carta · bianco → blu, giallo, blu, giallo · giallo → blu, carta, blu, giallo |
| **B · Fascia** | `B-fascia/` | `B-fascia-bianco/` | `B-fascia-giallo/` | blu → carta, giallo, blu, carta · bianco → blu, giallo, carta, blu · giallo → carta, blu, giallo, carta |
| **C · Telefono grande** | `C-telefono-grande/` | `C-telefono-grande-bianco/` | `C-telefono-grande-giallo/` | come B |
| **D · Numero gigante** | `D-numero-gigante/` | `D-numero-gigante-bianco/` | `D-numero-gigante-giallo/` | come B |
| **E · Foto a tutta slide** | `E-foto-piena/` | `E-foto-piena-bianco/` | `E-foto-piena-giallo/` | blu → blu · bianco → blu, giallo, blu, giallo · giallo → blu, carta, blu, giallo |
| **F · Carta a blocchi** | `F-carta-blocchi/` | `F-carta-blocchi-bianco/` | `F-carta-blocchi-giallo/` | come A |
| **Chiusura (notifica)** | `terminatori/2026-10-15-notifica/claude-design-blu.dc.html` | `…/claude-design-bianco.dc.html` (quello attuale) | `…/claude-design-giallo.dc.html` | — |

Ogni cartella ha `COLORE.txt` ("colore di partenza: …"), `copertina`, `slide`, `slide-numero` (se c'è), `chiusura` in `.dc.html`, la cartella `img/` e `anteprima.png` (6 slide affiancate). Le cartelle blu di A e B sono quelle di prima (A e B hanno ancora le immagini del vecchio canvas `/_blob/…` e i testi di Gemini); le nuove (bianco, giallo) hanno i testi e le immagini del post Google Play.
La chiusura di ogni cartella ha il colore della cartella (bianco e giallo); nella cartella blu resta quella di prima: usa la variante che serve da `terminatori/`.

**Come si rigenerano.** Per E: `python3 strumenti/varianti-e.py <cartella-bozza>`. Per A, B, C, D, F e la chiusura: `python3 strumenti/varianti-colori.py` (parte dalla bozza del post Google Play, cambia solo i colori ruolo per ruolo, ricontrolla i contrasti e rifà anteprime e chiusure). Per cambiare una palette si tocca un solo punto: le costanti `TINTE` e `RITMO` in testa a quel file (per E: `TINTE` e `VARIANTI` di `varianti-e.py`).
In `carosello.py` la chiusura accetta `{"tipo": "chiusura", "colore": "blu|bianco|giallo"}`; gli stili A e B non hanno ancora un parametro di colore di partenza (da fare, vedi sotto).

### Ultimo colore usato (lo aggiorna il `costruttore-post` a bozza fatta)
| Template | Ultimo colore usato | Dove |
|---|---|---|
| A · Classico | non ancora usato | — |
| B · Fascia | blu | post Gemini 4 Argon, 14/10/2026 |
| C · Telefono grande | non ancora usato | — |
| D · Numero gigante | non ancora usato | — |
| E · Foto a tutta slide | bianco | post Google Play, 15/10/2026 |
| F · Carta a blocchi | non ancora usato | — |
| Chiusura (notifica) | carta (bianco) | tutti i post finora |

Prossimo post: per ogni template, uno dei due colori diversi dall'ultimo (E: blu o giallo; B: bianco o giallo; chiusura: blu o giallo).

## Ultima slide: il terminatore
Tutti i post finiscono con il **terminatore attuale**, in qualsiasi template. I terminatori (attuale e vecchi) sono in `terminatori/`, con le istruzioni per cambiarlo.

## Da fare (quando serve)
- `carosello.py`, stili A e B: aggiungere un parametro di colore di partenza (oggi A parte sempre dal blu e B ha il giro blu → carta → giallo fisso, con i colori scritti dentro le singole funzioni). Finché non c'è, le slide finali di A e B in bianco o giallo si fanno dai `.dc.html` delle cartelle `-bianco` e `-giallo`.

## Come si lavora a un post (deciso il 15/10/2026)
1. Si decide la notizia e Claude scrive i testi: cosa ha fatto l'AI, in poche parole, più un commento di due o tre parole per slide.
2. **Bozza su Claude Design, senza video.** Claude crea un canvas con le slide del post in **ogni template** (un fotogramma al posto del video) e manda il link, insieme all'anteprima del Reel (`reel-anteprima.png`).
3. Il proprietario sceglie il template e corregge testi e grafica sul canvas.
4. Solo quando il proprietario dice che va bene, Claude crea le slide vere con `strumenti/carosello.py` (`"stile"` scelto, video veri, `--completi`).

## I file di questa cartella
- `A-classico/`, `B-fascia/`, `C-telefono-grande/`, `D-numero-gigante/`, `E-foto-piena/` e `F-carta-blocchi/` (ognuna più le cartelle `-bianco` e `-giallo`, vedi tabella dei colori): le slide in formato Claude Design (`.dc.html`) da copiare in un nuovo canvas, più le anteprime PNG. Le cartelle C-F hanno `copertina`, `slide` (con immagine), `slide-numero` (con cifra grande) e `chiusura`, e una cartella `img/` con le immagini d'esempio, richiamate con `src="img/…"`.
- Le immagini dentro i `.dc.html` puntano agli allegati del canvas del 15/10 (`/_blob/…`): in un canvas nuovo vanno caricate di nuovo e sostituite.

Esempio: canvas del post su Gemini 4 Argon — https://claude.ai/artifact/UD5TAg44jgWMUH71UWX4x2

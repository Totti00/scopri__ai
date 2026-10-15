# Terminatori

Il **terminatore** è l'ultima slide di ogni post: non parla del post, rappresenta la pagina e invita a seguire e salvare.
È uguale per tutti i post finché non si decide di cambiarlo. Nel tempo se ne possono avere diversi: si tengono tutti qui, in ordine di data.

| Data | Nome | Stato | Com'è |
|---|---|---|---|
| 15/10/2026 | `notifica` | **attuale** | Fondo carta, smartphone con la notifica di Scopri.AI (avatar: fumetto blu con tre puntini; "Scopri.AI"; "🔔 Nuovo post: vieni a scoprirlo!") e campanella. "Le novità sull'AI, appena escono." + "🔔 Segui @scopri__ai e attiva le notifiche" / "📌 E salva il post per ritrovarlo". |
| 14/10/2026 | `calendario` | archiviato | Gli appuntamenti della settimana (Lun, Ven, Dom, Extra) + domanda per i commenti. |

Ogni cartella contiene:
- `slide.png`: com'è la slide;
- `claude-design.dc.html`: la versione da aprire e modificare su Claude Design.

**Colori della chiusura `notifica`** (deciso il 15/10/2026): esiste in tre colori di partenza, in `2026-10-15-notifica/`: `claude-design-bianco.dc.html` (carta, quella di prima, uguale a `claude-design.dc.html`), `claude-design-blu.dc.html` e `claude-design-giallo.dc.html`, con i rispettivi `slide-bianco.png`, `slide-blu.png`, `slide-giallo.png`. Il colore lo sceglie il `costruttore-post` a rotazione (vedi `template/README.md`). Si rigenerano con `python3 strumenti/varianti-colori.py chiusura`.

## Come si usa
- Nel `slide.json` del post: `{"tipo": "chiusura"}` usa il terminatore **attuale**.
- Con colore di partenza: `{"tipo": "chiusura", "colore": "blu"}` (blu, bianco o giallo; senza `colore` è bianco/carta).
- Per usarne un altro solo in un post: `{"tipo": "chiusura", "terminatore": "calendario"}`.

## Come se ne aggiunge uno nuovo
1. Si fanno gli schizzi su Claude Design e il proprietario sceglie.
2. Si crea la cartella `AAAA-MM-GG-nome/` con `slide.png` e `claude-design.dc.html`.
3. Si aggiunge la funzione in `strumenti/carosello.py` (in `chiusura()`) e si cambia `TERMINATORE_ATTUALE`.
4. Si aggiorna questa tabella: il nuovo diventa **attuale**, il vecchio **archiviato**.

Gli schizzi scartati restano sul canvas del 15/10/2026: https://claude.ai/artifact/UD5TAg44jgWMUH71UWX4x2

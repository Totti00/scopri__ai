# Routine automatiche

Le routine sono sessioni di Claude che partono da sole a un orario fisso (impostate il 14/10/2026).
Ogni routine segue questo file più il file della sua attività.

| Quando (ora italiana) | File | Cosa fa |
|---|---|---|
| Ogni giorno 07:45 | `ricerca-notizie.md` | Cerca le notizie, le vota; se una vale 4–5 prepara la news lampo |
| Venerdì 08:50 | `prompt-venerdi.md` | Prepara il post di prompt efficaci (uscita 15:30) |
| Domenica 14:50 | `curiosita-domenica.md` | Prepara la curiosità scientifica (uscita 21:00) |
| Domenica 17:50 | `news-settimana.md` | Prepara le news della settimana (uscita lunedì 08:00) |

## Passi comuni a tutte le routine
1. **Repository.** Se `/home/user/scopri__ai` non esiste, aggiungi il repository con `add_repo` (owner `Totti00`, repo `scopri__ai`, accesso `push`) e clonalo lì. Poi `git pull origin main`.
2. **Data e ora.** Usa sempre l'ora italiana: `TZ=Europe/Rome date`.
3. **Leggi le regole:** `CLAUDE.md`, `fonti.md`, `brand/identita.md`, il file della rubrica in `format/`. Controlla `archivio/` per non ripetere argomenti (regola 6).
4. **Immagini vere** (regola 4): prima le sale stampa ufficiali. Per leggere pagine fatte in JavaScript (blog.google, Reddit) usa `node strumenti/leggi-pagina.cjs <url>`. Per le immagini usa `curl`; le GIF e WEBP si convertono in PNG con `ffmpeg -i in.gif -frames:v 1 out.png`.
5. **Slide:** scrivi `slide.json` e lancia `python3 strumenti/carosello.py archivio/<cartella>/slide.json`. Guarda ogni PNG (Read) e correggi testi troppo lunghi o immagini tagliate male. Niente fonti sulle slide.
6. **Consegna:** `caption.txt` (fonti e crediti delle immagini in fondo), `fonti.md`, `note.md`.
7. **Salva:** commit su `main` con autore `Claude <noreply@anthropic.com>` e push (`git push origin main`; se la rete fallisce riprova fino a 4 volte).
8. **Mostra al proprietario:** manda slide e caption con `SendUserFile` (status `proactive`).
9. **Messaggio finale** in italiano, breve: cosa è pronto, a che ora pubblicarlo, eventuali dubbi.

## Limiti
- Mai pubblicare su Instagram: lo fa il proprietario.
- Se una regola di `CLAUDE.md` non si può rispettare (per esempio mancano 2 fonti), non si pubblica: lo si scrive nel messaggio finale.

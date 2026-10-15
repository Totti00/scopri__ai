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
3. **Leggi le regole:** `CLAUDE.md`, `fonti.md`, `brand/identita.md`, `brand/crescita.md`, il file della rubrica in `format/`. Controlla `archivio/` per non ripetere argomenti (regola 6).
4. **Immagini e video veri** (regola 4): prima le sale stampa ufficiali. I video ufficiali si scaricano dai post su X delle aziende con `curl https://api.fxtwitter.com/<account>/status/<id>` (dà il link MP4); YouTube è bloccato. Nel `slide.json` un visual `{"video": "media/x.mp4", "inizio": 10, "durata": 8}` crea una slide MP4. Per leggere pagine fatte in JavaScript (blog.google, Reddit) usa `node strumenti/leggi-pagina.cjs <url>`. Per le immagini usa `curl`; le GIF e WEBP si convertono in PNG con `ffmpeg -i in.gif -frames:v 1 out.png`.
5. **Bozza:** prima delle slide vere crea un canvas su Claude Design con le slide in ogni template (vedi `template/README.md`) e manda il link. Se la routine prepara un post da pubblicare subito (venerdì, domenica), fai comunque anche le slide vere nel template indicato nel file della rubrica, o in A se non c'è.
6. **Slide:** scrivi `slide.json` e lancia `python3 strumenti/carosello.py archivio/<cartella>/slide.json --completi` (se ci sono video, crea anche `slide-NN-completo.mp4` con il video intero, che il proprietario può accorciare da solo). Guarda ogni PNG (Read) e correggi testi troppo lunghi o immagini tagliate male. Niente fonti sulle slide.
7. **Consegna:** `caption.txt` (regole di `brand/crescita.md`: parole chiave nella prima riga, `📩 Mandalo a …`, "Fonti: …" in fondo, massimo 5 hashtag), `alt-text.txt`, `fonti.md`, `note.md`.
8. **Salva:** commit su `main` con autore `Claude <noreply@anthropic.com>` e push (`git push origin main`; se la rete fallisce riprova fino a 4 volte).
9. **Mostra al proprietario:** manda slide e caption con `SendUserFile` (status `proactive`). Se ci sono video, manda anche i file `-completo.mp4` (non sono su GitHub) e scrivi dove inizia e finisce il pezzo scelto da te. Un file oltre i 30 MB non si può inviare: ricomprimilo con `ffmpeg -i in.mp4 -c:v libx264 -crf 25 -an -movflags +faststart out.mp4`.
10. **Messaggio finale** in italiano, breve: cosa è pronto, a che ora pubblicarlo, eventuali dubbi.

## Limiti
- Mai pubblicare su Instagram: lo fa il proprietario.
- Se una regola di `CLAUDE.md` non si può rispettare (per esempio mancano 2 fonti), non si pubblica: lo si scrive nel messaggio finale.

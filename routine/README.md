# Routine automatiche: il regista e la squadra

Le routine sono sessioni di Claude che partono da sole a un orario fisso. Ogni routine fa da **regista**: non costruisce da sola, fa lavorare la squadra di agenti (decisa il 15/10/2026) e parla con il proprietario.

| Quando (ora italiana) | Rubrica | File della rubrica |
|---|---|---|
| Ogni giorno 07:45 | `news` (news lampo, se c'è una notizia da 4–5) | `ricerca-notizie.md` |
| Venerdì 08:50 | `prompt` (uscita 15:30) | `prompt-venerdi.md` |
| Domenica 14:50 | `curiosita` (uscita 21:00) | `curiosita-domenica.md` |
| Domenica 17:50 | `settimana` (uscita lunedì 08:00) | `news-settimana.md` |

## La squadra (`.claude/agents/`)
| Agente | Fase | Scrive |
|---|---|---|
| `ricercatore` | 1. Ricerca contenuti | `notizie/AAAA-MM-GG.md` → "1. Ricerca" |
| `analista` | 2. Analisi | → "2. Analisi" (fonti, gancio, media, voto) |
| `selezionatore` | 3. Scelta | → "3. Scelta" (la proposta) |
| `costruttore-post` | 4. Costruzione post | `archivio/<cartella>/`: bozza, poi slide, caption, testo alternativo, fonti, note |
| `costruttore-reel` | 5. Costruzione Reel | `archivio/<cartella>/`: `reel.json`, anteprima, poi `reel.mp4`, `caption-reel.txt` |

**La pubblicazione la fa il proprietario**, a mano. Nessun agente pubblica.

Gli agenti si chiamano con lo strumento Agent (`subagent_type` = nome dell'agente). Se in questa sessione non compaiono, usa `general-purpose` con il prompt: "Leggi `/home/user/scopri__ai/.claude/agents/<nome>.md` e segui quelle istruzioni. Data: … Rubrica: … Cartella: … Modo: …".
Gli agenti non fanno commit e non parlano con il proprietario: lo fa il regista.

## Prima di tutto
1. **Repository.** Se `/home/user/scopri__ai` non esiste, aggiungi il repository con `add_repo` (owner `Totti00`, repo `scopri__ai`, accesso `push`) e clonalo lì. Poi `git pull origin main`.
2. **Data e ora.** Usa sempre l'ora italiana: `TZ=Europe/Rome date`.
3. **Leggi** `CLAUDE.md`, `calendario.md` e il file della rubrica qui sopra.

## Fase A — ricerca, analisi, scelta (da sola)
1. `ricercatore` → poi `analista` → poi `selezionatore`, uno dopo l'altro (ognuno usa il lavoro del precedente).
2. Commit e push di `notizie/AAAA-MM-GG.md`.
3. Se la scelta è "Oggi niente": manda al proprietario una riga ("Oggi niente news lampo: la migliore era … voto N") e **finisci**.
4. Altrimenti manda la proposta (titolo, perché, copertina, slide, Reel, orari, alternative) e chiedi: **"Va bene? Rispondi sì, no, oppure dimmi cosa cambiare."**

### 🛑 Fermata 1 — aspetta la risposta del proprietario
Non costruire niente finché non risponde. Se dice di cambiare, aggiorna la scelta (anche con il `selezionatore`) e richiedi l'ok. Se dice no, finisci.

## Fase B — bozza (dopo il sì)
1. `costruttore-post` (modo `bozza`) e `costruttore-reel` (modo `bozza`) **in parallelo**, con la stessa cartella.
2. Pubblica la bozza del post su **Claude Design**: Artifact `quickstart` con intent `design`, crea il canvas dal tipo "Design" con il titolo del post, poi pubblica nel suo `url` i file di `<cartella>/bozza/` (le pagine `.dc.html`, `canvas.json` e `img/`), seguendo le istruzioni del tipo.
3. Commit e push.
4. Manda al proprietario: il link del canvas e `reel-anteprima.png` (SendUserFile). Chiedi: **"Quale template scegli? Correggi pure sul canvas, poi scrivimi."**

### 🛑 Fermata 2 — aspetta la scelta del template e le correzioni
Prima di andare avanti rileggi il canvas (Artifact `read` del suo url, compreso `canvas.json`): le correzioni fatte a mano dal proprietario valgono quanto quelle scritte in chat.

## Fase C — post e Reel finali
1. `costruttore-post` (modo `finale`) e `costruttore-reel` (modo `finale`) **in parallelo**, passando a ognuno il template scelto e tutte le correzioni.
2. Controlla tu il risultato (qualche slide e qualche fotogramma del Reel).
3. Commit su `main` con autore `Claude <noreply@anthropic.com>` e push (se la rete fallisce riprova fino a 4 volte). I file `media/*.mp4` e `*-completo.mp4` non vanno su GitHub (sono in `.gitignore`).
4. **Consegna il pacchetto** con SendUserFile (status `proactive`):
   - le slide (`slide-NN.png` / `.mp4`) e i `slide-NN-completo.mp4`;
   - `reel.mp4`;
   - `caption.txt` e `caption-reel.txt`;
   - `alt-text.txt`.
   Un file oltre i 30 MB non si può inviare: ricomprimilo con `ffmpeg -i in.mp4 -c:v libx264 -crf 25 -an -movflags +faststart out.mp4`.
5. **Messaggio finale** in italiano, breve: cosa è pronto, quando pubblicare carosello e Reel, musica consigliata, eventuali dubbi.

## Limiti
- Mai pubblicare su Instagram: lo fa il proprietario.
- Se una regola di `CLAUDE.md` non si può rispettare (per esempio mancano 2 fonti), non si pubblica: lo si scrive al proprietario.
- Se il proprietario chiede una modifica che vale anche per il futuro, aggiorna il file delle regole giusto (`CLAUDE.md`, `brand/`, `format/` o l'agente in `.claude/agents/`) e fai commit.

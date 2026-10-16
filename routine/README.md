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
| `selezionatore` | 3. Menu | → "3. Menu" (tante opzioni + un consiglio; sceglie il proprietario) |
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
3. Manda al proprietario il **menu in versione corta** (lo prepara il `selezionatore`): per ogni notizia titolo, voto e i 3 titoli di copertina (a, b, c), gli schemi di carosello, l'invito e il consiglio. Anche nei giorni senza notizie da 4–5: il consiglio sarà "oggi niente", ma decide lui. Chiedi: **"Cosa scegli? Rispondi con un codice (es. "2 b storia"), mescola pure, oppure "niente"."**

### 🛑 Fermata 1 — aspetta la risposta del proprietario
Non costruire niente finché non risponde. Scrivi la sua scelta in `notizie/AAAA-MM-GG.md`, sezione "4. Scelta del proprietario" (notizia, titolo, tipo di carosello, eventuali modifiche), commit e push. Se chiede altre opzioni, rifai il menu con il `selezionatore`. Se dice "niente", finisci.

## Fase B — bozza (dopo la scelta)
1. `costruttore-post` (modo `bozza`, con lo **slug** `AAAA-MM-GG-<rubrica>-<argomento>`) e `costruttore-reel` (modo `bozza`) **in parallelo**. Il costruttore del post usa la skill `scopri-carousel`: testi completi in `carousels/<slug>/copy.md`, slide statiche esportate, copertine alternative.
2. Commit e push.
3. Manda al proprietario (SendUserFile): `exports/contact-sheet.jpg`, le copertine alternative (`exports/copertina-*.png`), le anteprime del Reel (`reel-anteprima.png`, `reel-anteprima-b.png`) e i testi di `copy.md` in versione corta (titolo e testo di ogni slide, caption). Chiedi: **"Va bene così? Dimmi quale copertina e quale Reel, e cosa cambiare."**

### 🛑 Fermata 2 — aspetta l'approvazione e le correzioni
Un sì chiaro ("va bene", "approvato") approva tutto quello che non viene citato: applica le modifiche chieste e vai avanti, senza richiedere l'approvazione.

## Fase C — post e Reel finali
1. `costruttore-post` (modo `finale`) e `costruttore-reel` (modo `finale`) **in parallelo**, passando a ognuno tutte le correzioni.
2. Controlla tu il risultato (contact sheet, qualche fotogramma degli MP4 e del Reel) con `brand/controllo-finale.md`.
3. Commit su `main` con autore `Claude <noreply@anthropic.com>` e push (se la rete fallisce riprova fino a 4 volte). Se il push su `main` viene rifiutato, fai push sul ramo della sessione (`git push -u origin HEAD:<ramo>`) e scrivi al proprietario il nome del ramo. I video sorgente (`media/*.mp4`) e i `*-completo.mp4` non vanno su GitHub (`.gitignore`).
4. **Consegna il pacchetto** con SendUserFile (status `proactive`):
   - le slide di `carousels/<slug>/exports/` (`slide-NN.png` / `.mp4`) e i `slide-NN-completo.mp4`;
   - `reel.mp4`;
   - i file di `carousels/<slug>/pubblicazione/` (caption, testi alternativi, commenti fissati) e `caption-reel.txt`.
   Un file oltre i 30 MB non si può inviare: ricomprimilo con `ffmpeg -i in.mp4 -c:v libx264 -crf 25 -an -movflags +faststart out.mp4`.
5. **Messaggio finale** in italiano, breve: cosa è pronto, quando pubblicare carosello e Reel, musica consigliata, eventuali dubbi, e le **ricevute delle caption** (carosello e Reel), per esempio:
   `✅ CAPTION PRONTA · carosello · notizia — 1092/2200 caratteri · 5 hashtag · invito: 📩 Mandalo a … · domanda: sì · fonti: sì`
   Se una caption non è PRONTA, rilancia `npm run publish` dopo averla corretta; se resta un avviso, scrivi quale e perché.

## Limiti
- Mai pubblicare su Instagram: lo fa il proprietario.
- Se una regola di `CLAUDE.md` non si può rispettare (per esempio mancano 2 fonti), non si pubblica: lo si scrive al proprietario.
- Se il proprietario chiede una modifica che vale anche per il futuro, aggiorna il file delle regole giusto (`CLAUDE.md`, `brand/`, `format/` o l'agente in `.claude/agents/`) e fai commit.

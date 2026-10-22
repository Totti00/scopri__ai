# Trasloco su un altro account Claude (22/10/2026)

Il proprietario passa a un abbonamento Claude privato. Questo file contiene tutto quello che serve per rifare le routine nel nuovo account.

## Cosa si porta da solo
Tutto il lavoro sta in questo repository GitHub (`Totti00/scopri__ai`), non nell'account Claude:
- regole (`CLAUDE.md`, `brand/`, `format/`, `fonti.md`, `calendario.md`);
- squadra di agenti (`.claude/agents/`), skill dei caroselli (`.claude/skills/scopri-carousel/`), programmi (`strumenti/`);
- regista delle routine (`routine/`), notizie, post, archivio e storia delle decisioni (`git log`).

Il nuovo account, collegato allo stesso GitHub, ritrova tutto.

## Cosa NON si porta
- **Le chat** (anche questa): non si spostano tra account. Le decisioni prese però sono tutte scritte nei file qui sopra.
- **Le routine di Scopri AI**: vanno ricreate nel nuovo account (sotto ci sono i messaggi esatti).
- **"📰 Notizie del giorno"** (il riassunto del mattino) **resta nel vecchio account**: non si sposta e non si spegne (deciso dal proprietario il 22/10/2026).
- **I video scaricati** (`media/*.mp4`, `*-completo.mp4`): non sono su GitHub. Le routine li riscaricano quando servono.

## Passi per il proprietario
1. Nel nuovo account apri **claude.ai/code** e collega GitHub con lo stesso utente (`Totti00`): https://claude.ai/connect-github. Se te lo chiede, installa la "Claude GitHub App" sul repository `scopri__ai`.
2. Crea l'ambiente cloud: il primo che ti propone va bene. In **Network access** scegli l'accesso completo, oppure aggiungi questi domini: `api.fxtwitter.com`, `video.twimg.com`, `pbs.twimg.com`, `fonts.googleapis.com`, `fonts.gstatic.com`, `registry.npmjs.org`, `upload.wikimedia.org`. Servono per i video di X, i font e le foto di Wikimedia.
3. Apri una sessione nuova con il repository `Totti00/scopri__ai` e incolla questo messaggio:
   > Leggi TRASLOCO.md e ricrea le 4 routine descritte lì, con gli stessi nomi, orari (ora italiana) e messaggi, nel mio ambiente. Poi fai partire "Scopri AI · Ricerca notizie" una volta per prova.
4. Quando la prova va bene, nel **vecchio account** spegni le 4 routine di Scopri AI, altrimenti partono due volte: dalla pagina Routine, oppure chiedilo in quella chat ("spegni le routine"). **"📰 Notizie del giorno" resta accesa lì.**

## Le 4 routine da ricreare
Tutte con l'ambiente cloud del nuovo account e notifiche push attive. Gli orari sono in ora italiana (`CRON_TZ=Europe/Rome`). Ognuna apre una sessione nuova a ogni partenza e lavora sul repository `Totti00/scopri__ai`.

| Nome | Quando | Cron |
|---|---|---|
| Scopri AI · Ricerca notizie | ogni giorno 07:45 | `CRON_TZ=Europe/Rome 45 7 * * *` |
| Scopri AI · Prompt del venerdì | venerdì 08:50 | `CRON_TZ=Europe/Rome 50 8 * * 5` |
| Scopri AI · Curiosità della domenica | domenica 14:50 | `CRON_TZ=Europe/Rome 50 14 * * 0` |
| Scopri AI · News della settimana | domenica 17:50 | `CRON_TZ=Europe/Rome 50 17 * * 0` |


### Scopri AI · Ricerca notizie
```
Sei il regista della squadra di agenti della pagina Instagram Scopri AI (@scopri__ai), rubrica "news". Scrivi sempre in italiano.

Lavori nel repository GitHub Totti00/scopri__ai. Se la cartella /home/user/scopri__ai non esiste, aggiungi il repository con add_repo (owner "Totti00", repo "scopri__ai", access "push") e clonalo in /home/user/scopri__ai. Poi fai git pull origin main.

Segui alla lettera routine/README.md e routine/ricerca-notizie.md (se le regole del repository dicono qualcosa di diverso da questo messaggio, valgono le regole del repository): fai lavorare ricercatore, analista e selezionatore (.claude/agents/), salva notizie/AAAA-MM-GG.md, fai commit e push. Mandami sempre il MENU con tante opzioni (notizie, 3 titoli di copertina, tipi di carosello, stile carosello o tweet, Reel sì/no - solo se c'è un video vero che è una bomba -, il tuo consiglio; se nessuna arriva a 4 il consiglio è "oggi niente", ma decido io) e FERMATI ad aspettare la mia scelta (fermata 1); poi prepara la bozza nello stile che ho scelto (skill scopri-carousel oppure strumenti/tweet.py: testi, slide statiche, più copertine e, solo se l'ho scelto, il Reel in due versioni) e FERMATI di nuovo (fermata 2); dopo la mia approvazione prepara il post finale (e il Reel, se c'è) e mandami il pacchetto con le ricevute "CAPTION PRONTA". Non pubblicare nulla su Instagram: pubblico io.
```

### Scopri AI · Prompt del venerdì
```
Sei il regista della squadra di agenti della pagina Instagram Scopri AI (@scopri__ai), rubrica "prompt" (uscita oggi alle 15:30). Scrivi sempre in italiano.

Lavori nel repository GitHub Totti00/scopri__ai. Se la cartella /home/user/scopri__ai non esiste, aggiungi il repository con add_repo (owner "Totti00", repo "scopri__ai", access "push") e clonalo in /home/user/scopri__ai. Poi fai git pull origin main.

Segui alla lettera routine/README.md e routine/prompt-venerdi.md (se le regole del repository dicono qualcosa di diverso da questo messaggio, valgono le regole del repository): fai lavorare ricercatore, analista (che prova davvero ogni prompt) e selezionatore (.claude/agents/), poi mandami il MENU con tante opzioni (temi, 3 titoli di copertina, tipi di carosello, il tuo consiglio; il Reel di solito no, perché serve un video vero che sia una bomba) e FERMATI ad aspettare la mia scelta (fermata 1); poi prepara la bozza con la skill scopri-carousel (testi, slide statiche, più copertine) e FERMATI di nuovo (fermata 2); dopo la mia approvazione prepara il post finale e mandami il pacchetto con la ricevuta "CAPTION PRONTA". Non pubblicare nulla su Instagram: pubblico io.
```

### Scopri AI · Curiosità della domenica
```
Sei il regista della squadra di agenti della pagina Instagram Scopri AI (@scopri__ai), rubrica "curiosita" (uscita stasera alle 21:00). Scrivi sempre in italiano.

Lavori nel repository GitHub Totti00/scopri__ai. Se la cartella /home/user/scopri__ai non esiste, aggiungi il repository con add_repo (owner "Totti00", repo "scopri__ai", access "push") e clonalo in /home/user/scopri__ai. Poi fai git pull origin main.

Segui alla lettera routine/README.md e routine/curiosita-domenica.md (se le regole del repository dicono qualcosa di diverso da questo messaggio, valgono le regole del repository): fai lavorare ricercatore, analista e selezionatore (.claude/agents/), poi mandami il MENU con tante opzioni (curiosità, 3 titoli di copertina, tipi di carosello, stile carosello o tweet, Reel sì/no - solo se c'è un video vero che è una bomba -, il tuo consiglio) e FERMATI ad aspettare la mia scelta (fermata 1); poi prepara la bozza nello stile che ho scelto (testi, slide statiche, più copertine e, solo se l'ho scelto, il Reel in due versioni) e FERMATI di nuovo (fermata 2); dopo la mia approvazione prepara il post finale (e il Reel, se c'è) e mandami il pacchetto con le ricevute "CAPTION PRONTA". Non pubblicare nulla su Instagram: pubblico io.
```

### Scopri AI · News della settimana
```
Sei il regista della squadra di agenti della pagina Instagram Scopri AI (@scopri__ai), rubrica "settimana" (uscita lunedì alle 08:00). Scrivi sempre in italiano.

Lavori nel repository GitHub Totti00/scopri__ai. Se la cartella /home/user/scopri__ai non esiste, aggiungi il repository con add_repo (owner "Totti00", repo "scopri__ai", access "push") e clonalo in /home/user/scopri__ai. Poi fai git pull origin main.

Segui alla lettera routine/README.md e routine/news-settimana.md (se le regole del repository dicono qualcosa di diverso da questo messaggio, valgono le regole del repository): fai lavorare ricercatore (che parte dai file notizie/ degli ultimi 7 giorni), analista e selezionatore (.claude/agents/), poi mandami il MENU con 7-8 notizie candidate (tra cui scelgo le mie 5), titoli di copertina, stile carosello o tweet, Reel sì/no (solo se una notizia ha un video vero che è una bomba) e il tuo consiglio, e FERMATI ad aspettare la mia scelta (fermata 1); poi prepara la bozza nello stile che ho scelto (testi, slide statiche, più copertine e, solo se l'ho scelto, il Reel in due versioni) e FERMATI di nuovo (fermata 2); dopo la mia approvazione prepara il post finale (e il Reel, se c'è) e mandami il pacchetto con le ricevute "CAPTION PRONTA". Non pubblicare nulla su Instagram: pubblico io.
```

## Per il Claude del nuovo account (come ricreare le routine)
- Usa `create_trigger` (MCP `claude-code-remote`) per le **quattro** routine: `create_new_session_on_fire: true`, il cron della tabella e il messaggio del blocco. "📰 Notizie del giorno" **non** va creata: resta nel vecchio account.
- `initiation: "human_request"`.
- Notifiche: `{"push": true}`.
- Modello: quello predefinito dell'account (per "Ricerca notizie" il più capace disponibile).
- Il repository va aggiunto alle sessioni delle routine: se `create_trigger` non lo fa da solo, il messaggio di ogni routine lo aggiunge con `add_repo`.
- Dopo la creazione, `fire_trigger` su "Scopri AI · Ricerca notizie" per la prova, e scrivi al proprietario gli id delle routine create.
- Non spegnere niente nel vecchio account: lo fa il proprietario dopo la prova.

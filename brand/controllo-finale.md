# Controllo finale (prima di consegnare un post)

Il `costruttore-post` e il `costruttore-reel` passano questa lista alla fine; il regista la ricontrolla prima di mandare il pacchetto.
Tabella adattata alle nostre regole; completa la lista di `format/guida-caroselli.md` (§3.2 test del gancio, §11 errori comuni).

| Errore | Perché è un problema | Come si corregge |
|---|---|---|
| Copertina debole o oltre 12 parole | Nessuno scorre | Uno dei 12 ganci e il test del gancio di `format/guida-caroselli.md` §3; video d'effetto |
| Copertina che spiega già tutto | Non c'è motivo di scorrere | La copertina incuriosisce, spiega la seconda slide |
| Manca "Scorri →" sulla copertina | La gente non capisce che c'è altro | Pillola gialla in basso a destra (`carosello.py` la mette da sola) |
| Seconda slide scollegata dalla copertina, o che non sta in piedi da sola | Chi scorre si perde; chi la vede per prima (Instagram la ripropone) non capisce | La seconda mostra subito ciò che la copertina promette e funziona anche da sola |
| Il meglio nascosto in fondo | Chi si ferma a metà non lo vede mai | La cosa più forte nella slide 2 o 3; in fondo riepilogo e invito |
| Troppo testo | Si smette di leggere | Limiti di `format/guida-caroselli.md` §2 (copertina ~12 parole, slide 2 ~25, contenuto ~40); tagliare o dividere |
| I titoli da soli non raccontano la storia | Chi scorre veloce non capisce | Prova dei titoli: letti in fila, la storia fila |
| Manca il contatore "N/totale" | Non si sa quanto manca | In alto a destra su tutte tranne la copertina (`carosello.py` lo mette da solo) |
| Più di un invito, o nessuno | Chi legge non sa cosa fare | Un solo invito nella chiusura e lo stesso in caption (§8) |
| Niente da salvare (6+ slide) | Meno salvataggi | Slide "In breve" prima della chiusura (`{"tipo": "riepilogo"}`) |
| Caption che ripete le slide | Non aggiunge niente | La caption dà il contesto e il perché (§9) |
| Due idee nella stessa slide | Confonde | Una cosa per slide, sempre |
| Si dice cosa hanno chiesto all'AI | È noioso | Si dice cosa **ha fatto** l'AI |
| Slide tutte uguali | Sembrano ripetute | Fondi a giro (blu → carta → giallo nel template B), visual diversi |
| Stile che cambia da una slide all'altra | Sembra un altro post | Stesso template, font, margini e colore d'accento |
| Fonti o nomi di autori sulle slide | Regola 2 e regola 4 | Solo in fondo alla caption, in "Fonti: …" |
| Immagine finta per una cosa reale | Regola 4 | Foto o video veri; disegni solo per concetti e prompt |
| Video di un concorrente o ripubblicato | Regola 4 e originalità | Si risale al post originale dell'autore |
| Notizia con una sola fonte | Regola 1 | Non si pubblica |
| Esagerazioni o indiscrezioni date per certe | Regola 5 | Condizionale, e lo si dichiara |
| Formato quadrato | Occupa meno schermo | Sempre 1080×1350 (Reel 1080×1920) |
| Testi del Reel sotto i pulsanti di Instagram | Non si leggono | `reel.py` li tiene nelle zone libere: non spostarli |
| Caption senza gancio e parole chiave nei primi ~125 caratteri, più di 5 hashtag | Meno persone raggiunte | Regole in `brand/crescita.md` |
| Evidenziatore su più righe che taglia le code di p, g, q, y | La riga sotto copre le lettere della riga sopra | `line-height` del titolo almeno 1.2; guarda le code sulla prima riga |
| Manca l'ultima slide (terminatore) | Niente invito a seguire | `{"tipo": "chiusura"}` alla fine |

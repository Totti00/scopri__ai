# Controllo finale (prima di consegnare un post)

Il `costruttore-post` e il `costruttore-reel` passano questa lista alla fine; il regista la ricontrolla prima di mandare il pacchetto.
Tabella adattata alle nostre regole; completa la lista di `format/carousel-copy.md` (§3.2 test del gancio, §11 errori comuni).

| Errore | Perché è un problema | Come si corregge |
|---|---|---|
| Copertina debole o oltre 12 parole | Nessuno scorre | Uno dei 12 ganci e il test del gancio di `format/carousel-copy.md` §3; video d'effetto |
| Copertina che spiega già tutto | Non c'è motivo di scorrere | La copertina incuriosisce, spiega la seconda slide |
| Manca "Scorri →" sulla copertina | La gente non capisce che c'è altro | «SCORRI PER SCOPRIRE» centrato in basso, sopra i pallini di Instagram, senza freccina (20/10/2026, lo mette la skill) |
| Seconda slide scollegata dalla copertina, o che non sta in piedi da sola | Chi scorre si perde; chi la vede per prima (Instagram la ripropone) non capisce | La seconda mostra subito ciò che la copertina promette e funziona anche da sola |
| Il meglio nascosto in fondo | Chi si ferma a metà non lo vede mai | La cosa più forte nella slide 2 o 3; in fondo riepilogo e invito |
| Troppo testo | Si smette di leggere | Limiti di `format/carousel-copy.md` §2 (copertina ~12 parole, slide 2 ~25, contenuto ~40); tagliare o dividere |
| I titoli da soli non raccontano la storia | Chi scorre veloce non capisce | Prova dei titoli: letti in fila, la storia fila |
| C'è il contatore "N/totale" | Tolto dal proprietario il 20/10/2026 | Nessun contatore su nessuna slide |
| Più di un invito principale, o nessuno | Chi legge non sa cosa fare | Un solo invito principale nella chiusura e lo stesso in caption (§8), più una domanda; la riga 🔔 Seguici solo sull'ultima slide, mai in caption (22/10/2026) |
| Copertina con titolo lungo (3–4 righe) | In miniatura non si legge | Riga piccola sopra + titolo in 2 righe da 3–6 parole (22/10/2026) |
| Parola chiave in lilla o colorata e basta | Nella griglia sparisce | Parola chiave nel riquadro blu con il testo bianco (`.em` nei titoli) |
| Copertina senza niente di grande da guardare | Non ferma il pollice | Un elemento vero e grande, almeno metà della slide |
| Caption di notizia oltre gli 800 caratteri, o con elenco di parole chiave tra parentesi | Non la legge nessuno / sembra spam | Taglia; le parole chiave nelle prime frasi |
| "NEWS LAMPO" in copertina o `@scopri__ai` in basso a sinistra | Tolti dal proprietario | Copertina senza etichetta di rubrica, cornice senza nome utente (20/10/2026) |
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
| Testi del Reel sotto i pulsanti di Instagram | Non si leggono | `reel.py` si ferma se un testo esce dalla zona sicura |
| Reel che parte piano (schermata nera, logo, persona che parla) | La gente scorre via | Il primo secondo è già il momento forte: scegli `inizio` dalla griglia dei fotogrammi |
| Reel con un video solo carino | Non vale un Reel | Reel solo con un video bomba; altrimenti basta il carosello |
| Caption senza gancio e parole chiave nei primi ~125 caratteri, più di 5 hashtag | Meno persone raggiunte | Regole in `brand/crescita.md`; `npm run publish` la controlla e deve dire "CAPTION PRONTA" |
| Evidenziatore su più righe che taglia le code di p, g, q, y | La riga sotto copre le lettere della riga sopra | `line-height` del titolo almeno 1.2; guarda le code sulla prima riga |
| Manca l'ultima slide (terminatore) | Niente invito a seguire | `{"tipo": "chiusura"}` alla fine |

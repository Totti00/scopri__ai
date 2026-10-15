# Controllo finale (prima di consegnare un post)

Il `costruttore-post` e il `costruttore-reel` passano questa lista alla fine; il regista la ricontrolla prima di mandare il pacchetto.
Tabella ispirata a una guida sui caroselli (inference.sh) e adattata alle nostre regole.

| Errore | Perché è un problema | Come si corregge |
|---|---|---|
| Copertina debole | Nessuno scorre | Uno dei 5 ganci di `format/ganci-e-tipi.md`; video d'effetto |
| Copertina che spiega già tutto | Non c'è motivo di scorrere | La copertina incuriosisce, spiega la seconda slide |
| Manca "Scorri →" sulla copertina | La gente non capisce che c'è altro | Pillola gialla in basso a destra (`carosello.py` la mette da sola) |
| Seconda slide scollegata dalla copertina | Chi scorre si perde | La seconda mostra subito ciò che la copertina promette |
| Il meglio a metà | Chi arriva in fondo resta deluso | Crescendo: il più forte per ultimo, prima del terminatore |
| Troppo testo | Si smette di leggere | Massimo 25–40 parole per slide; titolo "Ha …" + commento di 2–3 parole |
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
| Caption senza parole chiave nella prima riga, più di 5 hashtag, niente "📩 Mandalo a …" | Meno persone raggiunte | Regole in `brand/crescita.md` |
| Manca l'ultima slide (terminatore) | Niente invito a seguire | `{"tipo": "chiusura"}` alla fine |

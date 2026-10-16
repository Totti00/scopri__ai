# Scopri AI — istruzioni per Claude

Questo repository produce i contenuti della pagina Instagram **Scopri AI** (`@scopri__ai`).
Claude prepara i caroselli e le caption; **il proprietario pubblica a mano** su Instagram.

## Chi siamo
- **Nome:** Scopri AI · Intelligenza Artificiale
- **Promessa:** "L'intelligenza artificiale che funziona davvero."
- **Pubblico:** italiani curiosi, anche non tecnici (dai 20 ai 70 anni). Se un concetto non lo capirebbe un genitore, va riscritto.
- **Di cosa parliamo:** tutte le notizie che toccano tecnologia e AI, anche su altri temi (lavoro, salute, sport, soldi, leggi), purché ci sia dentro un minimo di tech. Va bene se interessa a una persona normale o le fa venire curiosità; non va bene se è solo una voce di borsa o una lite fra miliardari senza conseguenze.
- **Differenza dai concorrenti:** ogni notizia ha la fonte; i prompt sono controllati prima di pubblicarli.

Dettagli: `brand/identita.md`. Concorrenti e ispirazione: `ispirazione/`.

## Regole fisse (mai derogare)
1. **Ogni notizia confermata da almeno 2 fonti affidabili** (vedi `fonti.md`). Se non ci sono, non si pubblica: si usa la rubrica di riserva ("Curiosità scientifiche").
2. **Fonte sempre citata** per notizie, curiosità e dati, **solo in fondo alla caption** (deciso il 14/10/2026: le slide restano pulite, senza fonti). **I post di prompt non hanno fonte.**
3. **Prompt controllati, senza dirlo**: prima di pubblicare un prompt che produce testo, Claude lo esegue e controlla che il risultato sia utile; se è debole, lo riscrive. È un controllo interno: sulle slide **non** compare nessun timbro "provato".
4. **Foto e video veri** (deciso il 14/10/2026): se si parla di una persona o di una cosa reale, si mostra quella vera, non un disegno. I disegni restano per i concetti astratti e per i prompt (la chat).
   - **Prima scelta**, senza rischi: sala stampa ufficiale (Meta, Apple, Google, OpenAI…), Wikimedia Commons, NASA ed enti pubblici, screenshot e registrazioni fatti da noi, Pexels e Unsplash.
   - **Ammesse anche** foto di agenzia (Getty, Reuters, Ansa, AP…) e clip ufficiali o di testate. Il proprietario ha accettato il rischio che Instagram rimuova il post per copyright. Si usano quando la prima scelta non basta.
   - **Foto di persone modificate con l'AI** (fotomontaggi ironici): ammesse solo se si capisce che sono finte, con la scritta "Fotomontaggio" sulla slide e l'etichetta "Info sull'AI" di Instagram attivata. Mai fotomontaggi che possano passare per veri o che mettano in bocca a qualcuno frasi mai dette.
   - **Progetti fatti dalle persone con l'AI** (deciso il 15/10/2026): si possono mostrare i video di chi ha creato qualcosa con un'AI, presi **dal post originale dell'autore**. L'autore si nomina **solo in "Fonti"** in fondo alla caption, mai sulle slide. Mai dalle ripubblicazioni di altre pagine (raccolte su X, concorrenti): da lì si prende solo lo spunto e si risale all'originale.
   - **Mai:** grafiche, video e fotomontaggi delle pagine concorrenti o di altri creator di notizie, fotogrammi di film. Eccezione: lo screenshot del post di X o Reddit che è esso stesso la notizia (regole in `fonti.md`, "Storie virali").
   - In fondo alla caption va solo "Fonti: …". Chi ha fatto foto e video si annota in `fonti.md` della cartella del post.
   - **Video in ogni slide quando si può** (deciso il 14/10/2026): i video ufficiali si prendono dai post su X delle aziende (`https://api.fxtwitter.com/<account>/status/<id>` dà il link diretto all'MP4). YouTube da qui è bloccato.
5. **Niente esagerazioni**: titoli con gancio sì, falsi o allarmisti no. Se una notizia è un'indiscrezione, si scrive al condizionale e lo si dichiara.
6. **Mai lo stesso argomento due volte**: prima di scegliere, controllare `archivio/`.
7. **Non copiare** testi, slogan o grafiche dei concorrenti. Si prendono le tecniche, non l'identità.

## Come si racconta una notizia
- Mai il post banale "è uscito X". Si cerca il **gancio**: la cosa più sorprendente o utile, quella che fa venire voglia di scorrere.
- **La copertina serve solo ad attirare l'attenzione**: un video breve e d'effetto (consegnato intero, lo taglia il proprietario) e un titolo che incuriosisce. Non spiega ancora niente.
- Dalla seconda slide in poi si spiega: ogni slide è una scoperta in più, con il suo video o la sua immagine.
- Ogni slide dice in poche parole **cosa ha fatto l'AI** ("Ha costruito…", "Ha insegnato…"), mai cosa le hanno chiesto. Poi un **commento di due o tre parole** sul risultato, nel fumetto ("7 centri di fila.", "Tutto da solo.").
- La seconda slide deve collegarsi alla copertina: se la copertina dice "guarda cosa sa fare", la seconda mostra subito la prima cosa che sa fare.
- Le slide nuove si preparano prima **senza video** su Claude Design, in **ogni template** di `template/`; il proprietario sceglie il template e corregge. I video si inseriscono solo quando approva (procedimento in `template/README.md`).
- Si dice cosa può farci una persona normale, e se è solo un esempio dell'azienda lo si dice.
- **Guida di scrittura dei caroselli** (adottata il 16/10/2026): `format/carousel-copy.md` (in inglese, com'è nell'originale; **i post si scrivono sempre in italiano**) — limiti di parole per slide, test del gancio, 12 tipi di gancio, 11 schemi di carosello, slide 2 che funziona anche da sola, riepilogo da salvare, caption che aggiunge e non ripete. Le regole di questo file vengono prima.
- **Il meglio all'inizio** (16/10/2026): la cosa più forte nella slide 2 o 3, non in fondo.
- **Contatore "3/7"** in alto a destra su tutte le slide tranne la copertina (16/10/2026).
- **Un solo invito per post**, scelto per tipo: notizie → "📩 Mandalo a…", prompt e liste → "📌 Salvalo…", serie → "🔔 Seguici" (16/10/2026).
- Copertina sempre con la pillola gialla **"Scorri →"**.
- Prima di consegnare, si passa il **controllo finale**: `brand/controllo-finale.md`.

## Come si scrive
- Si dà del **tu**. Frasi corte. Una sola idea per frase.
- Parole semplici: "programma" invece di "tool" quando possibile; se si usa un termine inglese, spiegarlo la prima volta.
- Tono: amichevole, concreto, curioso. Mai saccente, mai da venditore.
- "AI" scritto sempre maiuscolo.

## Per arrivare a più persone
Regole complete in `brand/crescita.md` (15/10/2026). In breve:
- prima riga della caption con le parole che la gente cerca (prodotto, azienda, "intelligenza artificiale");
- **massimo 5 hashtag**: Instagram ignora gli altri;
- lo stesso unico invito della chiusura (`📩 Mandalo a …` per le notizie, `📌 Salvalo …` per prompt e liste) e una domanda vera; mai esche come "commenta SÌ" o "tagga 3 amici";
- mai un contenuto di altri messo da solo: sempre dentro le nostre slide, con i nostri testi.

## La squadra di agenti
Il lavoro è diviso in fasi, ognuna con il suo agente in `.claude/agents/` (deciso il 15/10/2026): `ricercatore` → `analista` → `selezionatore` → `costruttore-post` e `costruttore-reel`. Li coordina la routine (il "regista", `routine/README.md`), che si ferma due volte ad aspettare il proprietario: dopo il **menu** (tante notizie, titoli e tipi di carosello tra cui scegliere) e dopo la bozza (ogni template, più copertine, due Reel). Regola generale: **tante soluzioni sul tavolo, poi sceglie il proprietario**. **La pubblicazione la fa il proprietario.**

## Rubriche e calendario
- Rubriche: `format/` (una scheda per rubrica, con struttura delle slide e della caption).
- Calendario: `calendario.md`.

## Cosa consegnare per ogni post
Una cartella `archivio/AAAA-MM-GG-rubrica-argomento/` con:
- `slide-01` … `slide-NN`: PNG oppure MP4 senza audio (1080×1350, formato 4:5)
- per le slide video anche `slide-NN-completo.mp4`, con il video intero: il proprietario sceglie da solo inizio e fine (vedi `strumenti/montaggio.md`)
- `caption.txt` — pronta da copiare su Instagram
- `alt-text.txt` — il testo alternativo, una riga per slide (vedi `brand/crescita.md`)
- `reel.json`, `reel.mp4` e `caption-reel.txt` — la versione Reel di 20 secondi (vedi `format/5-reel.md`)
- `fonti.md` — link alle fonti usate e data di consultazione
- `note.md` — cosa è stato provato (prompt) e ogni dubbio rimasto

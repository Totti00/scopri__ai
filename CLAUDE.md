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
2. **Fonte sempre citata** per notizie, curiosità e dati, **solo in fondo alla caption** (deciso il 14/10/2026: le slide restano pulite, senza fonti). Niente scritta "Notizia verificata · fonti nella caption" sull'ultima slide (provata e tolta il 22/10/2026). **I post di prompt non hanno fonte.**
3. **Prompt controllati, senza dirlo**: prima di pubblicare un prompt che produce testo, Claude lo esegue e controlla che il risultato sia utile; se è debole, lo riscrive. È un controllo interno: sulle slide **non** compare nessun timbro "provato".
4. **Foto e video veri** (deciso il 14/10/2026): se si parla di una persona o di una cosa reale, si mostra quella vera, non un disegno. I disegni restano per i concetti astratti e per i prompt (la chat).
   - **Prima scelta**, senza rischi: sala stampa ufficiale (Meta, Apple, Google, OpenAI…), Wikimedia Commons, NASA ed enti pubblici, screenshot e registrazioni fatti da noi, Pexels e Unsplash.
   - **Ammesse anche** foto di agenzia (Getty, Reuters, Ansa, AP…) e clip ufficiali o di testate. Il proprietario ha accettato il rischio che Instagram rimuova il post per copyright. Si usano quando la prima scelta non basta.
   - **Foto di persone modificate con l'AI** (fotomontaggi ironici): ammesse solo se si capisce che sono finte, con la scritta "Fotomontaggio" sulla slide e l'etichetta "Info sull'AI" di Instagram attivata. Mai fotomontaggi che possano passare per veri o che mettano in bocca a qualcuno frasi mai dette.
   - **Progetti fatti dalle persone con l'AI** (deciso il 15/10/2026): si possono mostrare i video di chi ha creato qualcosa con un'AI, presi **dal post originale dell'autore**. L'autore si nomina **solo in "Fonti"** in fondo alla caption, mai sulle slide. Mai dalle ripubblicazioni di altre pagine (raccolte su X, concorrenti): da lì si prende solo lo spunto e si risale all'originale.
   - **Mai:** grafiche, video e fotomontaggi delle pagine concorrenti o di altri creator di notizie. Eccezione: lo screenshot del post di X o Reddit che è esso stesso la notizia (regole in `fonti.md`, "Storie virali"). (I fotogrammi di film sono ammessi: deciso il 20/10/2026.)
   - In fondo alla caption va solo "Fonti: …". Chi ha fatto foto e video si annota in `fonti.md` della cartella del post.
   - **Video in ogni slide quando si può** (deciso il 14/10/2026): i video ufficiali si prendono dai post su X delle aziende (`https://api.fxtwitter.com/<account>/status/<id>` dà il link diretto all'MP4). YouTube da qui è bloccato. **Foto e video veri sempre a colori** (deciso il 20/10/2026: niente più bianco e nero col blu), nelle slide dentro un riquadro. **Nei Reel**, sotto il titolo, con sopra solo il logo (16/10/2026, `format/5-reel.md`).
   - **Immagini create da noi** (deciso il 16/10/2026): quando non c'è niente di vero da mostrare (concetti, prompt, consigli), le immagini le crea Claude col codice: schede di interfaccia e oggetti 3D di vetro e cromo (`.claude/skills/scopri-carousel/assets/3d/`). I **meme con persone vere** si fanno solo partendo da una foto vera, con le regole dei fotomontaggi qui sopra. Niente generatori esterni.
5. **Niente esagerazioni**: titoli con gancio sì, falsi o allarmisti no. Se una notizia è un'indiscrezione, si scrive al condizionale e lo si dichiara.
6. **Mai lo stesso argomento due volte**: prima di scegliere, controllare `archivio/` e `carousels/`.
7. **Prendere spunto sì, copiare pari pari no** (cambiata il 21/10/2026): dai post dei concorrenti si possono prendere **i contenuti** (gli argomenti, le notizie, le liste di prompt, i formati) e riadattarli in versione nostra: in italiano, con parole nostre, verificati (notizie con 2 fonti, prompt provati) e con il nostro design. Mai copiati parola per parola, mai le loro grafiche, i loro video o i loro slogan, mai il loro nome sulle slide.

## Come si racconta una notizia
- Mai il post banale "è uscito X". Si cerca il **gancio**: la cosa più sorprendente o utile, quella che fa venire voglia di scorrere.
- **La copertina serve solo ad attirare l'attenzione**: un video breve e d'effetto (consegnato intero, lo taglia il proprietario) e un titolo che incuriosisce. Non spiega ancora niente.
- Dalla seconda slide in poi si spiega: ogni slide è una scoperta in più, con il suo video o la sua immagine.
- Ogni slide dice in poche parole **cosa ha fatto l'AI** ("Ha costruito…", "Ha insegnato…"), mai cosa le hanno chiesto. **Niente scritte sotto le immagini** (deciso il 20/10/2026): l'unica eccezione è il confronto, con "Prima: …" e "Dopo: …" (1–3 parole su cosa cambia, es. "Prima: pubblicità" / "Dopo: solo le app") sotto ciascuna immagine, fuori dall'immagine. Mai etichette tonde col pallino appoggiate sopra le immagini. Le immagini si vedono **intere**, non tagliate.
- La seconda slide deve collegarsi alla copertina: se la copertina dice "guarda cosa sa fare", la seconda mostra subito la prima cosa che sa fare.
- Le slide si costruiscono con la skill **`scopri-carousel`** (vedi "Design" qui sotto): prima testi completi e slide statiche da approvare (con le copertine alternative), poi i video veri e il pacchetto di pubblicazione.
- Si dice cosa può farci una persona normale, e se è solo un esempio dell'azienda lo si dice.
- **Guida di scrittura dei caroselli** (adottata il 16/10/2026): `format/carousel-copy.md` (in inglese, com'è nell'originale; **i post si scrivono sempre in italiano**) — limiti di parole per slide, test del gancio, 12 tipi di gancio, 11 schemi di carosello, slide 2 che funziona anche da sola, riepilogo da salvare, caption che aggiunge e non ripete. Le regole di questo file vengono prima.
- **Il meglio all'inizio** (16/10/2026): la cosa più forte nella slide 2 o 3, non in fondo.
- **Niente contatore delle slide** ("03 / 08"): tolto per sempre il 20/10/2026.
- **Un invito principale per post**, scelto per tipo: notizie → "📩 Mandalo a…", prompt e liste → "📌 Salvalo…" (o "Commenta «PAROLA» e ti mando…" quando si regala qualcosa), serie → "🔔 Seguici" (16/10/2026). La riga con la campanella "🔔 Seguici per non perdere le prossime notizie" sta **solo sull'ultima slide**, non in caption (20/10/2026, cambiato il 22/10/2026).
- **Niente etichetta di rubrica sulla copertina** (niente "NEWS LAMPO") e **niente `@scopri__ai` in basso a sinistra** sulle slide (deciso il 20/10/2026).
- **Copertina che si nota nella griglia** (22/10/2026, dopo una revisione esterna dei primi 9 post):
  - **titolo corto**: una riga piccola sopra (`.kicker`) e il titolo grande in **2 righe da 3–6 parole** (niente maiuscolo tutto: è lo stile di altri);
  - **parola chiave nel riquadro blu** `#2340FF` con il testo bianco (non più il testo lilla, che in miniatura sparisce): vale per tutti i titoli delle slide;
  - **un elemento vero e grande** che occupa almeno metà della slide (screenshot, foto, oggetto, logo, volto);
  - **logo più grande** (64 px), sempre in alto a sinistra;
  - l'invito a scorrere è una **barra blu** con «SCORRI PER SCOPRIRE».
- **Invito a scorrere** sulla copertina (20/10/2026, barra blu dal 22/10/2026): «SCORRI PER SCOPRIRE» (senza freccina) centrato in basso, **sopra i pallini** che Instagram disegna dentro l'immagine (pallini a circa y 1232 su 1350: la scritta sta più in alto, centro verso y 1175). Sulla copertina **niente cerchio blu con la freccia** in basso a destra (le altre slide lo tengono). A destra della scritta, alla stessa altezza, la **linea blu corta** (160 px) che tocca il bordo destro e continua nella slide 2 (come nel post del 20/10/2026 sulle smart TV: è il modello del footer per **tutti i caroselli**, non per i Reel). Solo sulla prima slide (e sulle copertine alternative).
- Prima di consegnare, si passa il **controllo finale**: `brand/controllo-finale.md`.

## Due stili, si sceglie post per post (dal 22/10/2026)
- **Carosello Electric Mono** (qui sotto, skill `scopri-carousel`): storie lunghe, prompt, liste.
- **Tweet** (`format/6-stile-tweet.md`, programma `strumenti/tweet.py`): fondo nero, font Inter, il nostro "profilo" in alto, il testo come un post e sotto la foto o il video vero; copertina con il titolo in MAIUSCOLO (massimo 3 righe) e il marchio "SCOPRI [AI]"; accento `#8FA3FF` in grassetto. Caption con chiusura "Tu cosa ne pensi? 🤔💬", fonte e un invito coerente con il post, lo stesso della slide di chiusura (notizie "📩 Mandalo a …", i 100 prompt solo nei post di prompt: 22/10/2026). Il carosello finisce sempre con la slide di chiusura. Va bene anche per i Reel.
- Il menu del `selezionatore` propone lo stile per ogni notizia; decide il proprietario.
- **Preferenza del proprietario (23/10/2026): di solito il tweet**, per tutti i caroselli (notizie, curiosità, settimana e, se ci stanno, anche i prompt). **Non è una regola fissa**: nel menu il tweet è lo stile consigliato, ma c'è sempre anche il carosello Electric Mono come alternativa, e sceglie il proprietario. Vale anche se il messaggio di una routine nomina solo la skill `scopri-carousel`. Se un testo non ci sta nel tweet (es. un prompt lungo: massimo 4 righe per slide), il menu lo dice.

## Design (dal 16/10/2026)
- **Stile carosello: Electric Mono adattato a Scopri AI** (l'altro stile, il tweet, è qui sopra), con la skill `.claude/skills/scopri-carousel/` (motore, layout, oggetti 3D, controlli, anteprime, pacchetto di pubblicazione). Le sue regole di brand sono in `references/brand-scopri-ai.md` della skill; le lezioni imparate in `references/lessons-learned.md`.
- Fondi **scuro, chiaro e blu** che si alternano, un solo colore d'accento: il blu `#2340FF`. **Niente giallo.** Font **Inter Tight** (e JetBrains Mono per le scritte piccole).
- Logo **"Scopri AI" con la campana** (`brand/logo/ufficiale/`), nome sempre "Scopri AI".
- I vecchi template A–G e il vecchio programma delle slide sono in `_vecchio/` (non si usano più, si possono riprendere).

## Come si scrive
- Si dà del **tu**. Frasi corte. Una sola idea per frase.
- Parole semplici: "programma" invece di "tool" quando possibile; se si usa un termine inglese, spiegarlo la prima volta.
- Tono: amichevole, concreto, curioso. Mai saccente, mai da venditore.
- "AI" scritto sempre maiuscolo.

## Per arrivare a più persone
Regole complete in `brand/crescita.md` (15/10/2026). In breve:
- prima riga della caption con le parole che la gente cerca (prodotto, azienda, "intelligenza artificiale"), **al massimo 125 caratteri** (22/10/2026);
- caption delle notizie **corte: sotto gli 800 caratteri** (le slide raccontano già); quelle lunghe solo per i prompt (22/10/2026);
- **niente elenchi di parole chiave tra parentesi**: le parole si mettono nelle prime frasi (22/10/2026);
- **massimo 5 hashtag**: Instagram ignora gli altri;
- in caption **un invito principale e una domanda vera, nient'altro** (22/10/2026): lo stesso invito della chiusura (`📩 Mandalo a …` per le notizie, `📌 Salvalo …` per prompt e liste); la riga `🔔 Seguici` sta solo sull'ultima slide; mai esche come "commenta SÌ" o "tagga 3 amici". **Ammesso** (deciso il 21/10/2026): "Commenta «PAROLA» e ti mando …" quando si regala davvero qualcosa in privato (es. il PDF con tutti i prompt); l'invio lo fa il proprietario;
- mai un contenuto di altri messo da solo: sempre dentro le nostre slide, con i nostri testi.

## La squadra di agenti
Il lavoro è diviso in fasi, ognuna con il suo agente in `.claude/agents/` (deciso il 15/10/2026): `ricercatore` → `analista` → `selezionatore` → `costruttore-post` e `costruttore-reel`. Li coordina la routine (il "regista", `routine/README.md`), che si ferma due volte ad aspettare il proprietario: dopo il **menu** (tante notizie, titoli e tipi di carosello tra cui scegliere) e dopo la bozza (testi completi e slide statiche, più copertine, due Reel). Regola generale: **tante soluzioni sul tavolo, poi sceglie il proprietario**. **La pubblicazione la fa il proprietario.**

## Rubriche e calendario
- Rubriche: `format/` (una scheda per rubrica, con struttura delle slide e della caption).
- Calendario: `calendario.md`.

## Cosa consegnare per ogni post
Dal 16/10/2026 una cartella `carousels/AAAA-MM-GG-rubrica-argomento/` (fatta dalla skill; i post di prima restano in `archivio/`, e per la regola 6 si guardano tutte e due) con:
- `exports/slide-01` … `slide-NN`: PNG oppure MP4 senza audio (1080×1350, formato 4:5), più `contact-sheet.jpg` e le copertine alternative
- per le slide video anche `exports/slide-NN-completo.mp4`, con il video intero: il proprietario sceglie da solo inizio e fine (vedi `strumenti/montaggio.md`)
- `pubblicazione/`: caption, **un solo file** `02-testi-alternativi.txt` con tutti i testi alternativi, ognuno sotto "Slide N" (deciso il 20/10/2026), commenti fissati (file `.txt` pronti da incollare, fatti da `npm run publish`)
- `copy.md` (i testi approvati) e `publish.json`
- **solo se c'è un video vero che è una bomba**: `reel.json`, `reel.mp4`, `reel-completo.mp4`, `reel-copertina.jpg` e `caption-reel.txt` — il Reel semplice, un titolo e sotto il video (deciso il 16/10/2026, vedi `format/5-reel.md`)
- `fonti.md` — link alle fonti usate e data di consultazione
- `note.md` — cosa è stato provato (prompt) e ogni dubbio rimasto

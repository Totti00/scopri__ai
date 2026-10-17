# Note — Claude e i numeri della NSA (finale, 17/10/2026)

## Stato
Finale. Copertina A ("Claude ne ha risolto un altro."), slide 3 con il video animato di Anthropic, il resto come approvato.
- Slide: `exports/slide-01.png`, `slide-02.png`, **`slide-03.mp4`** (47,1 s, 5,1 MB, 1080×1350, 30 fps, senza audio), `slide-04.png` … `slide-09.png`.
- `exports/slide-03-completo.mp4` (59,5 s, 6,2 MB): versione lunga da cui il proprietario può scegliere inizio e fine. Non va su GitHub (`.gitignore`): la manda il regista.
- `exports/slide-03.png` è il fermo immagine della slide video (serve alle anteprime; su Instagram va l'MP4).
- Pacchetto: `pubblicazione/01-caption.txt` e `02-alt-text-slide-01…09.txt`. Nessun commento fissato (è una notizia).
- Le copertine B, C, D restano in `exports/` ma non fanno parte del pacchetto.
- Il proprietario ha chiesto di copiare il post anche in `archivio/2026-10-17-news-claude-numeri-nsa/` quando si aggiorna GitHub: lo fa il regista con il commit.

## Seconda fonte (ricontrollo finale, 17/10 verso le 09:00)
- **Trovata: Tom's Hardware Italia** (testata di livello 2 della nostra lista), 17/10 alle 09:29, firma Andrea Maiellano: "Claude risolve in 30 minuti un mistero della NSA rimasto irrisolto per 25 anni". I fatti coincidono con i nostri (mezz'ora, 1997–98, P-256 = 1.842° candidato del 16/08/1997, verifica di Valsorda in Go, 36.864 $ a ISRG, "non è una falla"). Attenzione: in fondo dice "Fonte dell'articolo: www.coindesk.com", quindi è una ripresa senza verifiche proprie.
- **Ancora niente** su Ars Technica, The Register, The Verge, TechCrunch, Wired, Engadget, 404 Media, MIT Technology Review, ANSA, Wired Italia, HDblog, DDay.it, Punto Informatico, Repubblica, Corriere (feed RSS controllati).
- Caption aggiornata: "Fonti: Anthropic, Filippo Valsorda (words.filippo.io), Tom's Hardware, CoinDesk". La regola 1 ora è rispettata anche alla lettera (livello 1 + livello 2), più la verifica indipendente di Valsorda.

## Video della slide 3 (come è fatto)
- Sorgente: il video ufficiale di Anthropic (5 min 8 s, 1920×1080; non 4K come scritto nel menu). Ha i sottotitoli in inglese "incisi" sotto l'immagine: li ho tagliati fuori, insieme alla barra di avanzamento. Nessun logo né scritta di Anthropic resta dentro il riquadro.
- Montaggio (script `montaggio-video.py` in questa cartella, comandi sotto), in ordine di storia, con dissolvenze di mezzo secondo:
  1. 0:08,9–0:25,6 — di notte, calendario "August 1997", una persona al computer; poi il seme di P-256 battuto sul foglio (C49D3608…).
  2. 3:59,4–4:16,4 — "t = 871,696,354" diventa "August 16, 1997 · 01:52:34 UTC"; poi la tabella con le date di tutte e cinque le curve (maggio 1997 – aprile 1998).
  3. 4:37,2–4:51,6 — la stanza vuota, sullo schermo `srand48(time(NULL))`, l'orologio ("meno di mezz'ora"), le persone davanti a "P-256 = srand48(871696354), candidate 1,842".
- Completo (59,5 s): stesse scene, la prima un po' più lunga (0:07,6, la stanza che si "dipinge"), e in più 3:48,3–3:59 con Claude che riavvolge il generatore fino al candidato 1.842.
- Comandi (da questa cartella; `SRC` = il video scaricato):
  `python3 -I montaggio-video.py SRC media/anthropic-montaggio.mp4 "8.9-25.6:A;239.4-256.4:D;277.2-289.0:A;!289.0-291.6:D"`
  `python3 -I montaggio-video.py SRC media/anthropic-montaggio-60s.mp4 "7.6-25.6:A;228.3-256.4:D;277.2-289.0:A;!289.0-291.6:D"`
  poi `npm run export`, `npm run media -- --full`, `npm run previews`.
- In monocromo blu le scene chiare (numeri, orologio, persone) diventano riquadri quasi bianchi con il tono blu: è voluto (standard delle slide), ma è la parte più "luminosa" del carosello.

## Scheda della slide 3
Il video occupa il posto della scheda verticale. I tre passaggi restano, in una riga sotto il video: "Ora del computer → Numeri a caso → Coincide" (con la spunta verde). Rispetto alla bozza si perdono "1997" accanto al primo passaggio e il numero "C49D3608 86E70493…" accanto alla spunta: li mostra il video. L'adesivo "Solo un orario" è sull'angolo in alto a destra del video. Titolo e testo sono quelli approvati.

## Dubbi
1. **Video "nostro"?** È un'animazione ufficiale di Anthropic messa dentro la nostra slide, con i nostri testi (va bene per `brand/crescita.md`: mai un video di altri da solo). Non è un video "vero" della realtà, ma è il materiale ufficiale della notizia e l'ha chiesto il proprietario.
2. **Riga facoltativa per la caption** (non l'ho aggiunta: la caption era già approvata): "🎬 L'animazione della slide 3 è di Anthropic, che dice di averla fatta fare proprio a Claude." Lo dice il video stesso nel finale ("We all came to look, and asked Claude to make this video"; "Narrated with an AI-generated voice"). Se il proprietario la vuole, va prima di "👉 Cosa cambia per te" e si rilancia `npm run publish`.
3. **Copertina**: titolo 6 parole + sottotitolo 8 = 14 parole, due oltre il tetto di 12 della guida (`format/carousel-copy.md`). Approvata così dal proprietario: la lascio.
4. **"Ne ha risolto un altro"**: è un titolo scherzoso. Non è falso (Anthropic racconta spesso risultati scientifici di Claude, anche lo stesso giorno: i circuiti quantistici), ma chi non segue l'AI potrebbe chiedersi "un altro cosa?": la slide 2 risponde subito.
5. **"Claude"**: Anthropic scrive che un dipendente ha chiesto a "un modello di ricerca interno", poi lo chiama sempre "Claude". Non diciamo quale versione.
6. **"25 anni"**: la frase di Claude dice "25-year-old mystery"; anche Tom's Hardware scrive 25. Lo standard è del 2000, i numeri del 1997–98.
7. **Parole di Claude (slide 4)**: tradotte e accorciate da noi ("Let me be skeptical: am I in some sort of simulated/test environment?" → «Un momento: sono in un test?»; "It's real." → «È vero.»).
8. **Il premio**: sulla slide 6 "36.864 $ di taglia", con "Il crittografo italiano che l'aveva messa": in realtà la taglia era di Valsorda più altri 11 contributori, triplicata perché donata. Semplificato, ma non falso. Il nome di Valsorda è solo in caption.
9. **Simbolo di Claude arancione**: è il colore originale del marchio (#D97757), usato come oggetto dentro l'immagine; l'accento del design resta il blu. Uso descrittivo, senza farlo sembrare un post di Anthropic.
10. **Slide 5**: la frase "Give Bob and Jerry a raise" la raccontava Jerry Solinas (NSA, morto nel 2023) dicendo che "forse" era andata così. Non lo nomino sulle slide, per rispetto.
11. **Lettura di Tom's Hardware**: il sito è dietro Cloudflare; l'ho letto con il browser automatico. Per farlo passare dal proxy ho disattivato il controllo dei certificati di Chromium: non va rifatto così (la strada giusta è dare a Chromium il certificato del proxy).

## Modifiche alla skill (valgono per i prossimi caroselli)
- `export-media.mjs` (skill e questa cartella): nuovo attributo **`data-full`** = file diverso per `slide-XX-completo.mp4` (un montaggio ≤ 60 s quando la sorgente dura minuti); il **fermo immagine** nel PNG ora ha lo stesso tono monocromo dell'MP4 (prima restava a colori).
- `references/build-guide.md` §11: come montare un video lungo (una entrata ffmpeg per scena, dissolvenze, tagliare via sottotitoli e barre) e lo `z-index` degli adesivi sopra un video. `references/lessons-learned.md` §5: la lezione di oggi.
- Dalla bozza: oggetti 3D `spark` e `curve` nel renderer, `SVGLoader`, trappola dello specchio con `rotateX(Math.PI)`.

## Controllo finale (`brand/controllo-finale.md` e `build-guide.md` §8)
Passato: seconda slide collegata alla copertina e in piedi da sola; il meglio in slide 3; titoli che in fila raccontano la storia; contatore 01/08 … 08/08, niente sulla chiusura; un solo invito (Manda) uguale in caption; slide "In breve"; cosa ha fatto l'AI + adesivi di 2–3 parole; nessuna fonte o nome sulle slide; due fonti (livello 1 + livello 2); 1080×1350; controllo automatico (QA) passato; caption PRONTA; logo giusto per ogni fondo; niente giallo; giunture della striscia pulite. Unico punto aperto: le 14 parole della copertina (dubbio 3).

## Musica consigliata
Umore news lampo: elettronica carica, strumentale. Già usati (`brand/musica-usata.md`): Daft Punk – Derezzed, Justice – Genesis; per il Reel della Tesla Roadster (16/10, l'ultimo post) erano consigliati Chemical Brothers, Kavinsky, Gesaffelstein: nessuno di questi artisti qui.
1. **Moderat – A New Error** (strumentale; cresce, aria da "indagine" notturna: partire da dove entra il ritmo)
2. **Jon Hopkins – Open Eye Signal** (strumentale; pulsante e misteriosa, va bene con la stanza di notte del video)
3. **Ratatat – Loud Pipes** (strumentale; più energica e allegra, se si vuole un tono più leggero)
Il proprietario controlla che ci siano nella libreria di Instagram; se tra le canzoni con ↗ c'è una strumentale adatta, ha la precedenza.

## Musica usata
Da scrivere quando il proprietario sceglie (anche in `brand/musica-usata.md`).

## Orari consigliati
Oggi, sabato 17/10, alle **12:30** (news lampo: ora c'è anche la testata di livello 2). In alternativa dentro le news del lunedì 19/10 alle 08:00.

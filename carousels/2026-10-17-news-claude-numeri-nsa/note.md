# Note — Claude e i numeri della NSA (bozza, 17/10/2026)

## Stato
Bozza: testi completi (`copy.md`), 9 slide statiche (`exports/slide-01…09.png`, `contact-sheet.jpg`) e 4 copertine (`exports/copertina-a…d.png`). Mancano: scelta della copertina, correzioni del proprietario, `publish.json` e pacchetto `pubblicazione/` (modo finale).

## Seconda fonte (richiesta del proprietario)
- **Esito: nessuna testata di livello 2 della lista in `fonti.md` ha ripreso la notizia** (controllo del 17/10 mattina: feed di Ars Technica, The Register, The Verge, TechCrunch, Wired, Engadget, 404 Media, MIT Technology Review, ANSA, Wired Italia, HDblog, DDay.it, Punto Informatico, Il Post, Tom's Hardware, Italian Tech; Google News EN e IT). Da qui la ricerca web non può aprire Ars, The Verge, Wired, Reuters e Guardian: li ho controllati dai feed RSS.
- **Trovata: CoinDesk** (17/10, 02:39 EDT), testata seria di tecnologia e finanza ma non nella nostra lista; riprende Anthropic e Valsorda senza verifiche proprie.
- **La regola 1 è rispettata**: Anthropic (livello 1) più Filippo Valsorda, il crittografo che aveva messo la taglia, che ha rifatto il calcolo per conto suo. È una conferma indipendente più forte di una semplice ripresa.
- **Consiglio**: ricontrollare Ars Technica e The Register poco prima di pubblicare (è sabato: le riprese possono arrivare lunedì). Se il proprietario vuole per forza una testata della lista, si può spostare alle news del lunedì 19/10.

## Dubbi
1. **"Ne ha risolto un altro"**: è un titolo scherzoso. Non è falso (Anthropic racconta spesso risultati scientifici di Claude, anche lo stesso giorno: i circuiti quantistici), ma chi non segue l'AI potrebbe chiedersi "un altro cosa?": è proprio la curiosità che fa scorrere, e la slide 2 risponde subito.
2. **"Claude"**: Anthropic scrive che un dipendente ha chiesto a "un modello di ricerca interno", poi lo chiama sempre "Claude". Non diciamo quale versione.
3. **"25 anni"**: la frase di Claude dice "25-year-old mystery"; il menu diceva 26. Ho tenuto 25 (lo standard è del 2000, i numeri del 1997-98).
4. **Parole di Claude (slide 4)**: tradotte e accorciate da noi ("Let me be skeptical: am I in some sort of simulated/test environment?" → «Un momento: sono in un test?»; "It's real." → «È vero.»).
5. **Il premio**: sulla slide 6 "36.864 $ di taglia", con "Il crittografo italiano che l'aveva messa": in realtà la taglia era di Valsorda più altri 11 contributori, triplicata perché donata. Semplificato, ma non falso. Il nome di Valsorda è solo in caption.
6. **Simbolo di Claude arancione**: è il colore originale del marchio (#D97757), usato come oggetto dentro l'immagine; l'accento del design resta il blu. È un marchio di Anthropic: lo usiamo per parlare di Claude (uso descrittivo), senza farlo sembrare un post di Anthropic.
7. **Slide 5**: la frase "Give Bob and Jerry a raise" la raccontava Jerry Solinas (NSA, morto nel 2023) dicendo che "forse" era andata così. Non lo nomino sulle slide, per rispetto.
8. **Video**: il video animato di Anthropic (5 min, 4K) non è usato: è un'animazione esplicativa, non un video "vero" della notizia, e il proprietario ha chiesto immagini nostre. Se lo vuole su qualche slide (es. la 3), si aggiunge in finale con `video-box`.

## Modifiche alla skill (valgono per i prossimi caroselli)
- Nel renderer 3D (`assets/3d/render-3d.html`) ci sono due oggetti nuovi: `spark` (simbolo di Claude estruso, arancione lucido) e `curve` (curva ellittica di cromo con perle di vetro). Aggiunto anche `SVGLoader`, così si può estrudere qualsiasi logo o forma SVG.
- Trappola risolta: estrudendo un SVG non si specchia con `scale(…, -1, …)` (le facce si girano e l'oggetto viene grigio/nero), si ruota con `rotateX(Math.PI)`.
- Per il renderer servono `numpy` e `Pillow` nel Python di sistema (qui non c'erano: installati con `python -m pip install numpy pillow`).
- `export-copertine.mjs` (nella cartella del post): esporta le copertine alternative di `copertine.html` con la stessa cornice della slide 1.

## Musica consigliata (bozza, da confermare in finale)
Umore news lampo: elettronica carica, strumentale, mai usata (vedi `brand/musica-usata.md`: Daft Punk – Derezzed, Justice – Genesis).
1. Moderat – A New Error (strumentale, cresce, aria da "indagine")
2. Bonobo – Kerala (strumentale, ritmo pulito)
3. Tycho – Awake (strumentale, più calma)
Il proprietario controlla che ci siano nella libreria di Instagram (e le ↗ di tendenza hanno la precedenza).

## Orari consigliati
Sabato 17/10 alle 12:30 (news lampo), oppure dentro le news del lunedì 19/10 se si aspetta una testata di livello 2.

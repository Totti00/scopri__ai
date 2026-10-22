# Note — 2026-10-22-news-falle-php (FINALE, stile tweet)

## Cosa è stato fatto
- Proprietario: bozza tweet approvata con una correzione, «nel carosello metti anche la slide di chiusura». Aggiunta la slide 05 di chiusura, anche se `format/6-stile-tweet.md` dice «niente slide di chiusura»: vale la richiesta del proprietario.
- Per farla ho aggiunto a `strumenti/tweet.py` un tipo `"chiusura"` piccolo e retrocompatibile (i JSON vecchi escono identici): fondo nero, foto profilo grande, «Scopri AI» e «@scopri__ai», titolo MAIUSCOLO con accento `#8FA3FF`, pulsante lilla, testo sotto e la riga «🔔 Seguici per non perdere le prossime notizie» (sempre presente, cambiabile con `"seguici"`). Invito uguale a quello della caption: «Commenta «100»» per i 100 prompt in PDF.
- Copertina scelta: la principale (DUE FALLE IN PHP SCOVATE DALLE AI). `exports/copertina-b.png` (HAI UN SITO? AGGIORNA PHP SUBITO) resta come alternativa.
- Nessun video vero: tutte PNG, nessun MP4.
- `publish-pack.py`: CAPTION PRONTA, nessun avviso (testi alternativi accorciati sotto i 140 caratteri).
- Commento fissato: il messaggio da mandare a chi gestisce il sito (versioni 8.5.12, 8.4.27, 8.3.36, 8.2.35; PHP 8.1 o più vecchio va cambiato).
- La versione Electric Mono resta in `exports/electric-mono/` (non toccata).

## Dubbi
- **NSA:** il post dice «be prepared for an update» (prepararsi all'aggiornamento), non «spegnete i siti». Per questo la slide 4 dice «ha detto di prepararsi all'aggiornamento» e non «aggiorna o spegni».
- **Siti di governo spenti:** BBC li riporta (Finlandia, Francia, agenzia olandese per la sicurezza informatica, porto di Rotterdam). «In mezza Europa» è un riassunto: se si vuole più prudenza, «in diversi paesi europei».
- **Parlamento olandese** (era nel menu): non ritrovato nelle fonti lette, lasciato fuori.
- **DeviantArt e Pokémon Home:** spenti, ma la BBC non dice che è per PHP: lasciati fuori.
- **«Circa 7 siti su 10»:** è la stima di Wiz (W3Techs 69,3% dei siti di cui si conosce il linguaggio); in slide c'è «secondo Wiz».
- **«Erano lì dal 2004»:** Wired, TechCrunch e BBC dicono da PHP 5 (luglio 2004); Wiz scrive «almeno da PHP 5.4». La caption dice anche che la PHP Foundation aveva visto i primi segnali nel 2024 (non «nessuno lo sapeva»).
- **OpenAI «Patch the Planet»:** pagina non leggibile da qui, citata da TechCrunch e The Verge.
- **Invito ai 100 prompt** (chiusura e caption): il PDF lo manda il proprietario in privato a chi commenta «100»; serve che sia pronto (post `2026-10-23-prompt-100-claude`).
- **Formato stile tweet con la chiusura:** è la prima volta; se piace, si può aggiornare `format/6-stile-tweet.md` (oggi dice «niente slide di chiusura»). Non l'ho cambiato: decide il proprietario.

## Musica consigliata
Umore: tensione da «allarme informatico», solo strumentale. Già usati o consigliati di recente (`brand/musica-usata.md` e note dei post precedenti): Daft Punk, Justice, M83, Henry Mancini, Lalo Schifrin, Moderat, Jon Hopkins, Ratatat, Chemical Brothers, Kavinsky, Gesaffelstein, Boards of Canada, Aphex Twin, Röyksopp, Mr. Oizo, Vitalic, Boys Noize, Nujabes, Idealism, Kupla: nessuno di questi qui.
1. **Trent Reznor & Atticus Ross – In Motion** (strumentale, dalla colonna sonora di The Social Network: pulsante e tesa, aria da hacker).
2. **Carpenter Brut – Turbo Killer** (strumentale, synthwave carica; partire da dove entra il ritmo).
3. **Tangerine Dream – Love on a Real Train** (strumentale, elettronica ipnotica e più calma, se si vuole lasciare leggere le slide).
Il proprietario controlla che ci siano nella libreria di Instagram; se tra le canzoni con ↗ c'è una strumentale adatta, ha la precedenza. Il brano scelto va scritto in `brand/musica-usata.md`.

## Orari consigliati
Notizia calda (uscita il 21/10): oggi giovedì 22/10 tra le 12:30 e le 13:30, oppure tra le 18:30 e le 20:00. Non oltre domani: dopo perde freschezza.

## Controllo finale (`brand/controllo-finale.md`, parte applicabile allo stile tweet)
- Copertina: titolo di 7 parole, 2 righe, MAIUSCOLO (regola dello stile tweet, non il `.kicker` del carosello); elemento vero e grande (php.net) nei primi 900 px; «SCORRI PER SAPERNE DI PIÙ» in fondo. OK.
- Seconda slide collegata alla copertina («Le hanno trovate le AI») e in piedi da sola. Il meglio in 2 e 3. OK.
- Si dice cosa ha fatto l'AI («hanno scovato»), non cosa le hanno chiesto. OK.
- Testi entro i limiti (il programma si ferma se no). Nessun contatore, nessuna etichetta di rubrica, nessun @ in basso a sinistra, nessuna scritta sotto le immagini, immagini intere. OK.
- Fonti solo in caption; nessun nome d'autore sulle slide (il marchio Wiz è dentro le immagini ufficiali stesse). OK.
- Un solo invito (Commenta «100»), uguale in chiusura e in caption, più la domanda «Tu cosa ne pensi?»; 🔔 Seguici solo sull'ultima slide. OK.
- Caption 789 caratteri (sotto 800), prima riga sotto i 125, 5 hashtag, niente elenchi di parole chiave. OK.
- Notizia con più di 2 fonti; niente esagerazioni (NSA riportata alla lettera). OK.
- 1080×1350 per tutte le slide. OK.
- Non applicabili: riquadro blu `.em` e barra blu (sono del carosello Electric Mono; lo stile tweet usa l'accento lilla), slide «In breve» (sono solo 5 slide), Reel (nessun video).

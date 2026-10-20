# Note — Prima e dopo: la TV ripulita dall'AI (news lampo, 20/10/2026, uscita 12:30)

## Stato
- Bozza approvata dal proprietario («ok, top»). Finale fatto il 20/10/2026.
- Correzione applicata nel finale: nella chiusura la campana è tornata la sola cloche piccola del logo (~44 × 25 px, inclinata come nel logo, blu chiaro), **senza lineette di vibrazione**. Cambiato anche nel motore della skill (`engine/carousel.js` e `.css`) e in `references/brand-scopri-ai.md` e `lessons-learned.md`: vale per tutti i prossimi post.
- Nessun prompt nel post (è una notizia): niente da provare.

## Copertina
- Copertina approvata: `exports/slide-01.png` (schermi sovrapposti, «Prima: pubblicità» / «Dopo: solo le app»).
- Invito a scorrere (proprietario, 20/10, variante 2 scelta): «SCORRI PER SCOPRIRE →» centrato in basso (maiuscole y 1263–1280, ultimi ~69 px liberi per i pallini di Instagram), Inter Tight semibold 25 px, bianco; freccina blu sottile centrata sull'altezza delle maiuscole (centro 1271,5 = 1271,5). Niente cerchio blu con freccia in copertina. Le copertine alternative restano com'erano (cerchio blu + scritta precedente): non rigenerate per scelta del proprietario.
- Alternative (stessa scritta): `copertina-a.png` (= slide 1), `copertina-c.png` (fotogramma di Ryan Doyle, senza didascalia), `copertina-d.png` (Mihir Gupta), `copertina-e.png` (titolo «La TV dei suoi mostrava pubblicità prima di Netflix. Non più.»), `copertina-f.png` (titolo «Pubblicità sulla tua smart TV? C'è chi la toglie con l'AI.»); confronto in `copertine-confronto.jpg`.
- **Copertina video**: `copertina-video.mp4` (6 s) + `copertina-video-completo.mp4` (13 s) + `copertina-video.png`. Video vero di Ryan Doyle con il titolo f; ho scartato «Prima e dopo: la stessa TV» perché il video mostra solo il dopo, e di un'altra TV. Se la si usa, lo stesso video torna in slide 5 (pezzi diversi). Testo alternativo: «Copertina: «Pubblicità sulla tua smart TV? C'è chi la toglie con l'AI». Video vero: menu di una TV ripulita che scorre.»
- `dumbtv.mp4` scartato come copertina: animazione grafica con scritte in inglese, non una ripresa vera.

## Dubbi rimasti
- «Ha spento 25 app»: Gathin scrive "removed", ma il suo progetto spegne (`pm disable-user`), non cancella. Scelto "spento" per coerenza con la slide 7.
- Slide 5: «Puoi sistemarla?» è la nostra resa di «can you hack this?» (la caption dice che a volte l'AI rifiuta la parola «hackerare»).
- Slide 7: "TV bloccata" e "Fire TV a metà" sono testimonianze singole su X, riportate da TechCrunch, non verificate oltre.
- Le foto e il video sono degli autori (post su X), non di sale stampa: rischio di rimozione per copyright accettato dal proprietario (regola 4).
- Etichetta "Info sull'AI" di Instagram: non serve (nessun fotomontaggio, nessuna immagine generata).

## Musica consigliata
Umore news lampo: elettronica carica, solo strumentale. Già usati o consigliati di recente (`brand/musica-usata.md` e note dei post precedenti): Daft Punk, Justice, M83, Henry Mancini, Lalo Schifrin, Moderat, Jon Hopkins, Ratatat, Chemical Brothers, Kavinsky, Gesaffelstein, Boards of Canada, Aphex Twin, Röyksopp: nessuno di questi artisti qui.
1. **Mr. Oizo – Flat Beat** (strumentale; basso secco e ritmo da subito, ed è nata come musica di una pubblicità TV: ironica con il tema).
2. **Vitalic – La Rock 01** (strumentale; elettronica carica, partire da dove entra il ritmo pieno).
3. **Boys Noize – & Down** (strumentale; energica, synth graffiante).
Il proprietario controlla che ci siano nella libreria di Instagram; se tra le canzoni con ↗ c'è una strumentale adatta, ha la precedenza. Il brano scelto va scritto in `brand/musica-usata.md`.

## Orari consigliati
- Uscita prevista: oggi 20/10 alle **12:30** (news lampo, `calendario.md`). Alternativa se si slitta: 18:30–19:30.
- Prima ora: rispondere ai commenti; Storia con sondaggio «Ci proveresti sulla tua TV?».

## Pubblicazione
- `pubblicazione/01-caption.txt` e `02-testi-alternativi.txt` (tutti i testi alternativi in un file, sotto «Slide N»). Nessun commento fissato (non serve: niente prompt).
- Slide 5 è un MP4 (`exports/slide-05.mp4`, 13 s; intero in `slide-05-completo.mp4`): il proprietario taglia inizio e fine se vuole.

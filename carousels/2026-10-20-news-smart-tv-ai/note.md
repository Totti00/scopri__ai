# Note — Prima e dopo: la TV ripulita dall'AI (news lampo, 20/10/2026, uscita 12:30)

## Stato
- Bozza approvata dal proprietario («ok, top»). Finale fatto il 20/10/2026.
- Correzione applicata nel finale: nella chiusura la campana è tornata la sola cloche piccola del logo (~44 × 25 px, inclinata come nel logo, blu chiaro), **senza lineette di vibrazione**. Cambiato anche nel motore della skill (`engine/carousel.js` e `.css`) e in `references/brand-scopri-ai.md` e `lessons-learned.md`: vale per tutti i prossimi post.
- Nessun prompt nel post (è una notizia): niente da provare.

## Copertina
- Copertina approvata: `exports/slide-01.png` (schermi sovrapposti, «Prima: pubblicità» / «Dopo: solo le app»).
- Alternative statiche tenute: `copertina-a.png` (= slide 1), `copertina-c.png`, `copertina-d.png`, `copertina-e.png`, `copertina-f.png` (confronto in `copertine-confronto.jpg`). Nella `c` ho tolto nel finale la didascalia «Dopo: il menu nuovo, nel video.» (non era un confronto Prima/Dopo, regola del 20/10).
- **Nuova alternativa video**: `copertina-video.mp4` (6 s, a colori) + `copertina-video-completo.mp4` (13 s, il video intero) + `copertina-video.png` (fotogramma). Video vero di Ryan Doyle (telecomando in mano, menu ripulito che scorre), titolo «Pubblicità sulla tua smart TV? C'è chi la toglie *con l'AI.*» (il titolo f, già nel menu): non ho tenuto «Prima e dopo: la stessa TV» perché il video mostra solo il dopo, ed è una TV diversa da quella della slide 2. Nessuna didascalia sotto il video.
  - Se si usa la copertina video, lo stesso video compare anche in slide 5: si ripete. Si può accettare (sono due pezzi diversi: 0–6 s in copertina, il video intero in slide 5) oppure tenere la copertina statica.
  - Testo alternativo per la copertina video: «Copertina: «Pubblicità sulla tua smart TV? C'è chi la toglie con l'AI». Video vero: menu di una TV ripulita che scorre.»
  - `dumbtv.mp4` (28 s) scartato come copertina: è un'animazione grafica con scritte in inglese, non una ripresa vera di prima e dopo.

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
- Caption, testi alternativi (uno per slide) in `pubblicazione/`. Nessun commento fissato (non serve: niente prompt).
- Slide 5 è un MP4 (`exports/slide-05.mp4`, 13 s; intero in `slide-05-completo.mp4`): il proprietario taglia inizio e fine se vuole.

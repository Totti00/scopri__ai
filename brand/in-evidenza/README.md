# Storie in evidenza (27/10/2026)

Stile **blu** (scelto dal proprietario): lo stesso sfondo della foto profilo, icona bianca a linea al centro, font Google Sans Flex.
I file si rifanno con `node brand/in-evidenza/genera.mjs` (serve `puppeteer-core`, come per la skill dei caroselli).

| # | Nome | Copertina | Cosa c'è dentro |
|---|---|---|---|
| 1 | Inizia qui 👆 | `copertine/01-inizia-qui.png` (play) | le 4 storie di `inizia-qui/`: chi siamo, cosa trovi e quando, perché fidarti, segui e attiva la campanella |
| 2 | Prompt | `copertine/02-prompt.png` (fumetto con stellina) | ogni post dei prompt del venerdì, ricondiviso nelle storie |
| 3 | News | `copertine/03-news.png` (giornale) | le news del lunedì e le news lampo |
| 4 | Curiosità | `copertine/04-curiosita.png` (lampadina) | le curiosità della domenica |
| 5 | PDF gratis | `copertine/05-pdf-gratis.png` (regalo) | una storia per ogni PDF («Commenta «100» sotto questo post»), con il link al post |
| 6 | Come lavoriamo | `copertine/06-come-lavoriamo.png` (scudo con la spunta) | 2 fonti per ogni notizia, fonti in fondo alla caption, niente titoli esagerati |

- I nomi hanno al massimo 15 caratteri. Sul telefono se ne vedono 4–5 senza scorrere: le più importanti stanno davanti.
- **«Come lavoriamo» e «Inizia qui» non dicono che i prompt sono provati** (regola 3: si controllano senza dirlo).
- I testi delle storie seguono le regole di `CLAUDE.md` ("Come si scrive").

## Come si mettono su Instagram
1. Pubblica almeno una storia per ogni storia in evidenza (per «Inizia qui» le 4 immagini di `inizia-qui/`, in ordine).
2. Sul profilo tocca **Nuova** (il cerchio con il +, sotto la bio), scegli le storie, tocca **Avanti** e scrivi il nome.
3. Tocca **Modifica copertina**, poi l'icona della galleria, e scegli la copertina giusta da `copertine/`.
4. Da lì in poi: ogni post nuovo si ricondivide nelle storie e si aggiunge alla storia in evidenza della sua rubrica.

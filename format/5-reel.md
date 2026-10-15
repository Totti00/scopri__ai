# Rubrica 5 — Reel in motion graphics (attiva dal 15/10/2026)

Ogni post ha anche la sua **versione Reel**: stesso contenuto, video verticale animato nel nostro stile.
Lo prepara il `costruttore-reel` (`.claude/agents/costruttore-reel.md`) con `strumenti/reel.py`.

## Com'è fatto
- **Circa 20 secondi**, 1080×1920, senza audio: la musica (solo strumentale) la mette il proprietario su Instagram.
- **Gancio** (3 s): il momento video più forte e un titolo che incuriosisce.
- **3–4 scoperte** (3–4 s l'una): titolo animato parola per parola ("Ha …"), video vero in un riquadro, commento di 2–3 parole nel fumetto.
- **Finale** (2,5–3 s): logo, "Le novità sull'AI, appena escono.", "🔔 Segui @scopri__ai".
- Tra una scena e l'altra una tendina di colore (blu → giallo → carta).
- I testi stanno fuori dalle zone coperte dai pulsanti di Instagram.
- Senza video (prompt, curiosità): scene con un'immagine o solo testo.

Esempio: `archivio/2026-10-14-news-lampo-gemini-4-argon/reel.mp4`.

## Quando esce
| Post | Reel |
|---|---|
| News lampo (12:30) | stesso giorno, 20:00 |
| News della settimana (lunedì) | martedì 20:00 |
| Prompt (venerdì) | sabato 20:00 |
| Curiosità (domenica) | lunedì 20:00 |

## Caption del Reel
`caption-reel.txt`: versione corta della caption del post, con le stesse regole (`brand/crescita.md`).

## Idee per Reel speciali (da valutare)
1. **"Prompt in 30 secondi"** — la schermata di un chatbot che scrive la risposta a un prompt utile.
2. **"Vero o falso?"** — un'affermazione sull'AI, pausa di 2 secondi, poi la risposta con la fonte.
3. **"Prima / dopo"** — un testo scritto male e la versione migliorata con un prompt.

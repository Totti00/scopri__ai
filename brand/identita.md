# Identità di Scopri.AI

## Profilo Instagram
- **Nome utente:** `scopri__ai`
- **Nome (campo "Nome" su Instagram):** 💬 L'AI che funziona davvero
- **Bio:**
  ```
  🧠 Intelligenza artificiale senza tecnicismi
  💡 Prompt pronti · 🗞️ News verificate · 🔬 Curiosità
  👇 Inizia a usare l'AI meglio
  ```
- **Tipo di account:** Creator (per vedere le statistiche).

## Posizionamento
"L'AI che funziona davvero, spiegata da chi la usa per lavoro."
Nessun concorrente unisce velocità, fonti verificate e utilità pratica: è il nostro spazio.

## Firma visiva (da usare sempre)
- Fonti e crediti delle immagini **solo in fondo alla caption**, mai sulle slide. I post di prompt non hanno fonte.
- Logo **Scopri.AI** in ogni slide.
- Nessun timbro "provato" o simili sulle slide.

## Palette (scelta il 13/10/2026: "blu pieno, carta e giallo")
| Ruolo | Colore | Hex |
|---|---|---|
| Fondo principale (copertine, notizie, foto profilo) | Blu pieno | `#2340FF` |
| Fondo chiaro (prompt, tutorial, schede) | Carta | `#F4F1EA` |
| Accento (parole chiave, etichette, barre di invito) | Giallo | `#FFD84D` |
| Testo sul blu | Bianco | `#FFFFFF` |
| Testo sulla carta e sul giallo | Quasi nero | `#121212` |

**Regole d'uso (per la leggibilità):**
- Sul **blu**: testo bianco; parole chiave in **giallo** (si leggono bene).
- Sulla **carta**: testo quasi nero; le parole chiave si evidenziano con un **riquadro giallo** dietro (testo nero), mai scritte in giallo.
- Sul **giallo**: testo sempre quasi nero.
- Mai rosso sul blu: illeggibile.
- Su fondo carta, il logo usa il blu (non il giallo, che sparirebbe).

## Grafica
- Font: **Bricolage Grotesque** (titoli e testo, scelto il 15/10/2026), **JetBrains Mono** (etichette e prompt). Il logo resta in **Space Grotesk**.
- **Logo ufficiale (scelto il 13/10/2026): "Scopri" + fumetto con "AI".**
  - Foto profilo: `brand/logo/ufficiale/foto-profilo.png` (fumetto giallo con "AI" blu su fondo blu).
  - Logo su fondo blu: `brand/logo/ufficiale/logo-su-blu.png` (testo bianco, fumetto giallo).
  - Logo su fondo carta: `brand/logo/ufficiale/logo-su-carta.png` (testo nero, fumetto blu).
  - Le proposte scartate non sono più nel repository, ma si possono recuperare dalla cronologia di GitHub.
- Formato slide: 1080×1350 px.

## Stile dei caroselli (14/10/2026, ispirato alle pagine AI, non a RapTrend)
Si genera con `strumenti/carosello.py`; esempio in `brand/template-esempio/`.
- **Logo piccolo** in alto a sinistra. Niente contatore 01/05, niente barra "Scorri" in basso, niente etichette a blocco.
- **Copertina (blu):** visual grande in alto (screenshot del prodotto o chat disegnata), titolo sotto con le parole chiave in giallo, pallino giallo con → come unico invito a scorrere.
- **Slide interne (carta):** testo sopra (25-40 parole, carattere grande), visual sotto, meglio se video in un riquadro arrotondato: screenshot, chat o numero grande su giallo. "👉 Per te" con filetto giallo. Nessuna fonte sulla slide.
- **Prompt:** il prompt è un messaggio blu in una finestra di chat ("Scrivi così all'AI"), con le parti da cambiare in giallo.
- **Ultima slide (blu):** gli appuntamenti fissi (Lun, Ven, Dom) più le news lampo + domanda per i commenti + "Segui e salva".
- Se si parla di una persona o di una cosa reale, il visual è la foto o il video veri (regola 4 di `CLAUDE.md`), con chi l'ha fatta annotato in `fonti.md` del post. La chat disegnata resta per i prompt da copiare e per i concetti; se non riproducono l'interfaccia vera, sotto va scritto "Esempio illustrativo".

Da evitare perché tipico dei concorrenti: fondo nero con lilla o viola, mascotte robot, collage di CEO.

## Tono di voce
| Sì | No |
|---|---|
| "Ecco come funziona, provalo così." | "Rivoluzionario! Cambierà tutto!" |
| "Secondo OpenAI…" (con fonte) | "Si dice che…" |
| "Abbiamo provato questo prompt: funziona per X, meno per Y." | "Il prompt definitivo." |

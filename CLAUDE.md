# Scopri.AI — istruzioni per Claude

Questo repository produce i contenuti della pagina Instagram **Scopri.AI** (`@scopri__ai`).
Claude prepara i caroselli e le caption; **il proprietario pubblica a mano** su Instagram.

## Chi siamo
- **Nome:** Scopri.AI · Intelligenza Artificiale
- **Promessa:** "L'intelligenza artificiale che funziona davvero."
- **Pubblico:** italiani curiosi, anche non tecnici (dai 20 ai 70 anni). Se un concetto non lo capirebbe un genitore, va riscritto.
- **Differenza dai concorrenti:** ogni notizia ha la fonte; i prompt sono controllati prima di pubblicarli.

Dettagli: `brand/identita.md`. Concorrenti e ispirazione: `ispirazione/`.

## Regole fisse (mai derogare)
1. **Ogni notizia confermata da almeno 2 fonti affidabili** (vedi `fonti.md`). Se non ci sono, non si pubblica: si usa la rubrica di riserva ("Curiosità scientifiche").
2. **Fonte sempre citata** per notizie, curiosità e dati: in piccolo sulla slide e in fondo alla caption. **I post di prompt non hanno fonte** (né sulle slide né in caption).
3. **Prompt controllati, senza dirlo**: prima di pubblicare un prompt che produce testo, Claude lo esegue e controlla che il risultato sia utile; se è debole, lo riscrive. È un controllo interno: sulle slide **non** compare nessun timbro "provato".
4. **Niente immagini protette**: niente foto di persone (CEO compresi), fotogrammi di film, video o grafiche di altri creator. Ammessi: grafica nostra, screenshot di prodotti presi dalle pagine ufficiali, loghi solo per identificare il prodotto di cui si parla.
5. **Niente esagerazioni**: titoli con gancio sì, falsi o allarmisti no. Se una notizia è un'indiscrezione, si scrive al condizionale e lo si dichiara.
6. **Mai lo stesso argomento due volte**: prima di scegliere, controllare `archivio/`.
7. **Non copiare** testi, slogan o grafiche dei concorrenti. Si prendono le tecniche, non l'identità.

## Come si scrive
- Si dà del **tu**. Frasi corte. Una sola idea per frase.
- Parole semplici: "programma" invece di "tool" quando possibile; se si usa un termine inglese, spiegarlo la prima volta.
- Tono: amichevole, concreto, curioso. Mai saccente, mai da venditore.
- "AI" scritto sempre maiuscolo.

## Rubriche e calendario
- Rubriche: `format/` (una scheda per rubrica, con struttura delle slide e della caption).
- Calendario: `calendario.md`.

## Cosa consegnare per ogni post
Una cartella `archivio/AAAA-MM-GG-rubrica-argomento/` con:
- `slide-01.png` … `slide-NN.png` (1080×1350, formato 4:5)
- `caption.txt` — pronta da copiare su Instagram
- `fonti.md` — link alle fonti usate e data di consultazione
- `note.md` — cosa è stato provato (prompt) e ogni dubbio rimasto

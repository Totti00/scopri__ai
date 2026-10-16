# Example: «5 prompt prima di firmare» (approved, Oct 2026)

The first Scopri AI carousel, built with this workflow. The full source is `carousels/bollette-contratti/` in the project. Its contact sheet is `contact-sheet.jpg` in this folder.

> It was built **before** the Coperchio rebrand: its frame shows the old speech-bubble logo and its engine is the pre-skill version. Future carousels use the skill's engine and the Coperchio kit.

- **Brief:** Scopri AI · "5 prompt per capire bolletta e contratti prima di firmare" · STATIC · Italian.
- **Framework:** listicle (hook → re-hook → privacy rule → 5 prompts → CTA). The user removed a "perché funzionano" slide.
- **Modes:** `D A L D L D L A D` (9 slides, counter `/ 08`).
- **Templates:**
  1. T1 cover: contract card + 3D magnifier zooming the clause «Alla scadenza»;
  2. statement + 3D hourglass;
  3. T2 with a redacted bill card;
  4–8. T5 prompt series;
  9. T10 CTA.
- **Thread:** `seams [1150,1150,1150,360,1150,360,1150,1150]`, `routes ['start','straight','straight','rightUp','leftDown','rightUp','leftDown','straight','end']`.
- **Assets:** `assets/generated/magnifier.png`, `hourglass.png` (in-house 3D renderer).
- **Publishing texts:** in `publish.json` next to this file (the same content as the published `pubblicazione/*.txt`).

## Slides

### 01 · Copertina (DARK, T1)
- **Pill:** LUCE · GAS · CONTRATTI
- **Display:** *5 prompt* / prima di / firmare (accent: «5 prompt»)
- **Lead:** Bolletta e contratto, spiegati dall'AI.

### 02 · Re-hook (ACCENT)
- **Pill:** IL PROBLEMA
- **Display (120 px):** Firmi in / 5 minuti. / Paghi *per anni.* (ink-950 phrase)
- **Body:** Prezzi, scadenze e penali sono tutti scritti. Il difficile è capirli: kWh, oneri, clausole. Con il prompt giusto, l'AI te li traduce.
- **Hero:** glass hourglass, bottom-right, white glow.

### 03 · Regola zero (LIGHT)
- **Pill:** PRIMA DI INIZIARE
- **H1:** *Prima,* (recede) oscura / i tuoi dati
- **Body:** Copri nome, indirizzo, codice fiscale, IBAN e codici POD/PDR. All'AI servono cifre e clausole, non chi sei.
- **Hero:** dark bill card, personal rows redacted with accent bars, sticker «✓ DATI OSCURATI», «Totale da pagare € 87,40» visible.

### 04 · Prompt 01 (DARK, T5 prompt card)
- **Pill:** PROMPT 01 · **H2:** Traduci *la bolletta* (*…* = recede) · **Sticker:** ALLEGA: BOLLETTA
- **Prompt (99 parole):**

> Agisci come un consulente energetico che spiega le cose a chi non è del settore. Ti allego la mia ultima bolletta [luce/gas], con i dati personali oscurati.
> 1. Riassumi in tre righe: quanto pago, per quale periodo e quanti [kWh/Smc] ho consumato.
> 2. Spiega ogni voce di spesa in parole semplici, con l'importo accanto.
> 3. Dimmi quale voce pesa di più sul totale e se dipende dai miei consumi o dal fornitore.
> 4. Calcola quanto mi costa davvero ogni [kWh/Smc], tasse incluse.
> Rispondi con una tabella e un breve riepilogo. Se un dato non è leggibile, dimmelo: non inventarlo.

### 05 · Prompt 02 (LIGHT, T5 prompt card)
- **Pill:** PROMPT 02 · **H2:** Controlla *stime e conguagli* (*…* = recede) · **Sticker:** ALLEGA: 2 BOLLETTE
- **Prompt (98 parole):**

> Agisci come un revisore che controlla le bollette a caccia di errori. Ti allego due bollette [luce/gas] dello stesso contratto, la più recente e la precedente, con i dati personali oscurati.
> 1. Confronta periodo, consumi e totale: cosa è cambiato, e di quanto in percentuale?
> 2. Per ognuna, indica se i consumi sono reali, stimati o da autolettura.
> 3. Segnala conguagli, ricalcoli, interessi di mora, servizi aggiuntivi e voci nuove.
> 4. Elenca cosa dovrei verificare o contestare, in ordine di priorità.
> Usa una tabella di confronto, poi un elenco puntato. Non dare per scontato che sia tutto corretto.

### 06 · Prompt 03 (DARK, T5 prompt card)
- **Pill:** PROMPT 03 · **H2:** Confronta il totale, / *non il prezzo* (*…* = recede) · **Sticker:** ALLEGA: 2 SCHEDE SINTETICHE
- **Prompt (99 parole):**

> Agisci come un consulente energetico indipendente, che non lavora per nessun fornitore. Ti allego le schede sintetiche di due offerte [luce/gas]. Il mio consumo annuo è di [kWh o Smc].
> 1. Stima la spesa annua di ciascuna, separando costi fissi e costi a consumo.
> 2. Indica se il prezzo è fisso o variabile, per quanto tempo vale e cosa succede alla scadenza.
> 3. Simula la spesa se i prezzi all'ingrosso salissero del 20%.
> 4. Dimmi quale offerta conviene a me e perché, in tre righe.
> Mostra i calcoli in una tabella. Se manca un dato, chiedimelo prima di rispondere.

### 07 · Prompt 04 (LIGHT, T5 prompt card)
- **Pill:** PROMPT 04 · **H2:** Trova *le clausole scomode* (*…* = recede) · **Sticker:** ALLEGA: CONTRATTO
- **Prompt (96 parole):**

> Agisci come un esperto di tutela dei consumatori. Ti incollo il contratto e le condizioni generali che sto per firmare, con i dati personali oscurati. Cerca le clausole che potrebbero costarmi di più nel tempo:
> 1. durata del prezzo e cosa succede alla scadenza;
> 2. rinnovi automatici e modifiche delle condizioni;
> 3. penali, costi di uscita e tempi per recedere;
> 4. depositi cauzionali e servizi extra attivati in automatico.
> Per ogni clausola: citala parola per parola, indica l'articolo e spiegala in una frase. Chiudi con un livello di rischio da 1 a 5 e il motivo.

### 08 · Prompt 05 (ACCENT, T5 prompt card)
- **Pill:** PROMPT 05 · **H2:** Fai [le domande giuste] (highlight bar) (*…* = recede) · **Sticker:** ALLEGA: CONTRATTO
- **Prompt (101 parole):**

> Agisci come un negoziatore esperto che sta dalla mia parte. Sto per firmare il contratto che ti allego e voglio chiarire tutto prima, non dopo.
> 1. Individua i 5 punti meno chiari o più rischiosi per me.
> 2. Per ciascuno, scrivi una domanda precisa da fare al venditore, a cui non si possa rispondere con un vago «non si preoccupi».
> 3. Accanto a ogni domanda, indica la risposta che mi rassicura e quella che deve allarmarmi.
> 4. Dimmi cosa farmi mettere per iscritto.
> Scrivi tutto in un tono cortese ma fermo, pronto da leggere al telefono o da mandare via email.

### 09 · Chiusura (DARK, T10)
- **Logo** centred (large) · no corner logo, no counter, no swipe cue.
- **H1:** Salvalo per la / *prossima offerta* (accent)
- **Lead:** L'AI ti spiega il contratto. La firma, però, resta tua.
- **Action pill:** SALVA (bookmark icon). The thread ends in a node at its left.

## Caption (as published, with emoji, 1220 caratteri)

```text
Una bolletta ha decine di voci. Un contratto, pagine di clausole. Questi 5 prompt te li spiegano prima che tu firmi, non dopo. 👇

🧠 Non sono semplici domande. Ognuno dà all'AI un ruolo, il contesto giusto, compiti numerati e regole precise: citare le clausole parola per parola, non inventare i dati che non trova, chiederti quelli che mancano.

Come usarli:
📌 Copiali dai commenti fissati qui sotto, oppure fai uno screenshot della slide: sulla maggior parte degli smartphone puoi copiare il testo dall'immagine.
💬 Incollalo in ChatGPT, Claude o Gemini e allega bolletta o contratto.
🔒 Prima oscura nome, indirizzo, codice fiscale, IBAN e codici POD/PDR.
✍️ Sostituisci le parti tra [parentesi quadre].

📅 Da sapere: se firmi online, al telefono o porta a porta, di norma hai 14 giorni dalla conclusione del contratto per ripensarci senza penali. E la scheda sintetica dell'offerta il venditore deve dartela prima della firma.

⚠️ L'AI spiega, ma può sbagliare. Verifica sempre sul contratto e confronta le offerte anche su ilportaleofferte.it, il comparatore pubblico di luce e gas.

🔖 Salva il post: ti servirà alla prossima offerta che ti propongono.

#bollette #lucegas #intelligenzaartificiale #promptAI #risparmio
```

## Pinned comments


### Commento fissato 1 (1921 caratteri)

```text
I 5 prompt da copiare · parte 1/2
(sostituisci le parti tra [parentesi quadre])

1 · Traduci la bolletta
Agisci come un consulente energetico che spiega le cose a chi non è del settore. Ti allego la mia ultima bolletta [luce/gas], con i dati personali oscurati.
1. Riassumi in tre righe: quanto pago, per quale periodo e quanti [kWh/Smc] ho consumato.
2. Spiega ogni voce di spesa in parole semplici, con l'importo accanto.
3. Dimmi quale voce pesa di più sul totale e se dipende dai miei consumi o dal fornitore.
4. Calcola quanto mi costa davvero ogni [kWh/Smc], tasse incluse.
Rispondi con una tabella e un breve riepilogo. Se un dato non è leggibile, dimmelo: non inventarlo.

2 · Controlla stime e conguagli
Agisci come un revisore che controlla le bollette a caccia di errori. Ti allego due bollette [luce/gas] dello stesso contratto, la più recente e la precedente, con i dati personali oscurati.
1. Confronta periodo, consumi e totale: cosa è cambiato, e di quanto in percentuale?
2. Per ognuna, indica se i consumi sono reali, stimati o da autolettura.
3. Segnala conguagli, ricalcoli, interessi di mora, servizi aggiuntivi e voci nuove.
4. Elenca cosa dovrei verificare o contestare, in ordine di priorità.
Usa una tabella di confronto, poi un elenco puntato. Non dare per scontato che sia tutto corretto.

3 · Confronta il totale, non il prezzo
Agisci come un consulente energetico indipendente, che non lavora per nessun fornitore. Ti allego le schede sintetiche di due offerte [luce/gas]. Il mio consumo annuo è di [kWh o Smc].
1. Stima la spesa annua di ciascuna, separando costi fissi e costi a consumo.
2. Indica se il prezzo è fisso o variabile, per quanto tempo vale e cosa succede alla scadenza.
3. Simula la spesa se i prezzi all'ingrosso salissero del 20%.
4. Dimmi quale offerta conviene a me e perché, in tre righe.
Mostra i calcoli in una tabella. Se manca un dato, chiedimelo prima di rispondere.
```


### Commento fissato 2 (1222 caratteri)

```text
I 5 prompt da copiare · parte 2/2

4 · Trova le clausole scomode
Agisci come un esperto di tutela dei consumatori. Ti incollo il contratto e le condizioni generali che sto per firmare, con i dati personali oscurati. Cerca le clausole che potrebbero costarmi di più nel tempo:
1. durata del prezzo e cosa succede alla scadenza;
2. rinnovi automatici e modifiche delle condizioni;
3. penali, costi di uscita e tempi per recedere;
4. depositi cauzionali e servizi extra attivati in automatico.
Per ogni clausola: citala parola per parola, indica l'articolo e spiegala in una frase. Chiudi con un livello di rischio da 1 a 5 e il motivo.

5 · Fai le domande giuste
Agisci come un negoziatore esperto che sta dalla mia parte. Sto per firmare il contratto che ti allego e voglio chiarire tutto prima, non dopo.
1. Individua i 5 punti meno chiari o più rischiosi per me.
2. Per ciascuno, scrivi una domanda precisa da fare al venditore, a cui non si possa rispondere con un vago «non si preoccupi».
3. Accanto a ogni domanda, indica la risposta che mi rassicura e quella che deve allarmarmi.
4. Dimmi cosa farmi mettere per iscritto.
Scrivi tutto in un tono cortese ma fermo, pronto da leggere al telefono o da mandare via email.
```


## Alt text

| Slide | Alt text |
|---|---|
| 01 | Copertina: «5 prompt prima di firmare». Una lente d'ingrandimento mette a fuoco la clausola «Alla scadenza» di un contratto luce. |
| 02 | «Firmi in 5 minuti. Paghi per anni.» Accanto, una clessidra di vetro con sabbia blu. Prezzi e clausole sono scritti, il difficile è capirli. |
| 03 | «Prima, oscura i tuoi dati». Una bolletta con nome, indirizzo, codice fiscale, IBAN e POD coperti: resta visibile solo il totale. |
| 04 | Prompt 1, «Traduci la bolletta»: l'AI spiega ogni voce di spesa e il costo reale per kWh. Testo completo nei commenti fissati. |
| 05 | Prompt 2, «Controlla stime e conguagli»: l'AI confronta due bollette e segnala stime e voci nuove. Testo completo nei commenti fissati. |
| 06 | Prompt 3, «Confronta il totale, non il prezzo»: l'AI stima la spesa annua di due offerte. Testo completo nei commenti fissati. |
| 07 | Prompt 4, «Trova le clausole scomode»: l'AI elenca scadenze, rinnovi, penali e servizi extra. Testo completo nei commenti fissati. |
| 08 | Prompt 5, «Fai le domande giuste»: l'AI prepara le domande da fare al venditore prima di firmare. Testo completo nei commenti fissati. |
| 09 | Logo Scopri AI. «Salvalo per la prossima offerta. L'AI ti spiega il contratto. La firma, però, resta tua.» Pulsante Salva. |


## Research notes (what the copy relied on)

- **ARERA:** bill items (materia energia, trasporto e gestione contatore, oneri di sistema, imposte). The new "scontrino dell'energia" bill format has applied since 1 July 2025. The scheda sintetica must be given before signing. The Portale Offerte is the public comparison site.
- **Cooling-off right:** 14 days for contracts signed at a distance or away from the seller's premises (Codice del Consumo art. 52), counted from the conclusion of the contract.
- **Fixed-price offers:** the price conditions last 1–2 years, then renew through a unilateral change with at least 3 months' notice.
- **Privacy:** hiding personal data before pasting it into an AI is presented as practical advice. No Garante guidance was found that says it.

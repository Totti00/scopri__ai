# Note · 10 prompt per modificare le foto con ChatGPT (bozza, 23/10/2026)

## Dubbio principale per il proprietario
**I prompt NON sono stati eseguiti su un'immagine vera.** Sono prompt per immagini e da qui non possiamo usare ChatGPT o Gemini per generare (niente generatori esterni, regola 4). Al posto della prova (regola 3) c'è il controllo ragionato qui sotto. Se vuoi, prima di pubblicare provane 2-3 tu dal telefono (consiglio: 01 togli, 02 occhi, 03 sfondo) su una foto tua.

## Controllo ragionato dei prompt
Criteri: è chiaro? dice cosa cambiare? dice cosa NON cambiare (riga «Lascia uguale»)? le parti tra [PARENTESI] si capiscono? Lunghezza 30–45 parole: più corti dello spunto, come chiesto.

| # | Prompt | Chiaro | Cosa cambia | Cosa resta | Parentesi | Esito e modifiche |
|---|---|---|---|---|---|---|
| 01 | Togli chi non c'entra | sì | [CHI O COSA] + ricostruire lo sfondo con luce, ombre, prospettiva | altre persone, colori, inquadratura | chiara | Riscritto: lo spunto diceva «oggetto/persona» con due parentesi; una sola [CHI O COSA] basta. Aggiunte «le altre persone»: è il rischio più frequente (l'AI ritocca anche chi resta). |
| 02 | Apri gli occhi chiusi | sì | aprire gli occhi, sguardo in macchina, modifica leggera | viso, espressione, capelli, luce, sfondo | [CHI], [COLORE] | **Rafforzato**: lo spunto non diceva il colore degli occhi, ma con gli occhi chiusi l'AI non può saperlo e lo inventa. Aggiunto [COLORE]. [CHI] serve nelle foto di gruppo. |
| 03 | Cambia lo sfondo | sì | sfondo + luce e ombre adattate | persona, posa, vestiti, capelli | [NUOVO SFONDO] | Ok. «capelli» aggiunto: i bordi dei capelli sono il punto dove i ritagli si vedono. |
| 04 | Rendi nitida la foto | sì | nitidezza, grana, colori | inquadratura, persone, visi, espressioni | nessuna | Ok. «Non aggiungere e non togliere niente» + «non un disegno» contro l'effetto plastica. Limite onesto: una foto molto sfocata non torna nitida per davvero, l'AI ridisegna i dettagli. Per questo «Controlla prima di usarla» nella slide 12. |
| 05 | Ritocco naturale | sì | luce, colori, esposizione, nitidezza | lineamenti, pelle con nei e rughe, capelli, vestiti, proporzioni | nessuna | Riscritto: lo spunto diceva «pelle» in generale; con «anche nei e rughe» l'AI non leviga il viso. «Niente filtri» al posto di «risultato naturale». |
| 06 | Dal giorno alla notte | sì | cielo, luce, ombre, luci accese | persone, edifici, inquadratura | [AL TRAMONTO / DI NOTTE] | Semplificato: tolta la parentesi «ora attuale» (l'AI la vede dalla foto). Le finestre accese «di notte» rendono il prompt corretto anche per il tramonto. |
| 07 | Allarga la foto | sì | estendere i bordi fino a un formato | la foto originale, senza spostarla né ritagliarla | [4:5 PER INSTAGRAM / 16:9 PER LO SCHERMO] | Riscritto: «4:5» e «16:9» da soli non li capisce un genitore, quindi abbiamo aggiunto a cosa servono. |
| 08 | Cambia i vestiti | sì | vestito nuovo che cade naturale | viso, corpo, posa, mani, sfondo | [VESTITO], [CHI] | Ok. Le mani sono il punto debole delle AI per immagini: dette esplicitamente. |
| 09 | Via le pieghe | sì | togliere pieghe e grinze | tessuto, colore, cuciture, pieghe naturali di gomiti e fianchi | nessuna | Riscritto: «pieghe naturali» da solo era vago; ora dice quali. «Non un dipinto» contro l'effetto pittura. |
| 10 | Colori da film | sì | solo i colori, luci e ombre equilibrate | persone, pelle naturale, oggetti, inquadratura | [CALDI E DORATI / FREDDI E BLU] | Riscritto: «color grading cinematografico» è gergo; ora «i colori di un film» con due esempi di stile da scegliere. |

Tutti i 10 hanno la riga «Lascia uguale:» separata: è la nostra aggiunta (lo spunto la teneva dentro il testo) e il filo del post (slide 12, caption, copertina C).

## Altri dubbi
- **Gemini:** «Funziona con: ChatGPT, Gemini» vale per l'uso tipico (allegare la foto in chat e scrivere la richiesta). Non abbiamo scritto nomi di modelli né limiti del piano gratuito, perché cambiano spesso.
- **Accento sulle slide prompt:** ogni slide ha il riquadro blu nel titolo (regola 22/10) più le parti tra parentesi in blu e il filo: un accento in più rispetto al budget della skill (§3 build-guide). Il controllo automatico è passato; se il proprietario lo trova troppo blu, si possono mettere le parentesi in bianco.
- **Copertina A:** la foto è tagliata un po' ai lati (formato 4:3 in un riquadro più stretto). Non è una foto di notizia: va bene, ma lo segnalo.
- **13 slide** (Instagram ne accetta fino a 20). La slide 12 «Tre regole» è nostra e si può togliere; se si sceglie la copertina C, meglio spostarla al posto 2.
- **PDF in bozza:** `pubblicazione/10-prompt-foto.pdf` (4 pagine: copertina con istruzioni, trucco e avviso; i 10 prompt; chiusura). Rifatto con `genera-pdf.mjs` dal file `prompts.json`, la stessa fonte delle slide (`genera.py`).

## Come si rigenera
`python3 genera.py` (index.html da `prompts.json`, `_head.html`, `copertine.html` variante a) → `npm run export` → `PATH=/usr/bin:$PATH npm run previews` → `node export-copertine.mjs` → `node genera-pdf.mjs`.

## Musica consigliata e orari
Da scrivere nel modo finale.

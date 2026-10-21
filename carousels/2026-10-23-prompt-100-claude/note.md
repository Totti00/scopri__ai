# Note · 100 prompt per Claude (bozza 21/10/2026)

## Come è cambiato il lavoro oggi
1. Prima richiesta: 10 prompt lunghi per Claude (cartella `2026-10-23-prompt-claude-da-salvare`). Fermata a metà su richiesta del regista.
2. Seconda: 100 prompt, griglia 2 × 5 per categoria come il post di spunto, cartella rinominata `2026-10-23-prompt-100-claude`.
3. Categorie 05–09 dagli screenshot del proprietario, 10 trascritta dal regista.
4. Chiusura «Commenta «100» e ti mando il PDF» ammessa dal 21/10/2026: slide 12, riga piccola in fondo a ogni categoria, caption e PDF.

## File
- `prompts.json`: i 100 prompt, l'unica fonte. Da lì `python3 genera.py` crea `index.html` e `copertine.html`; `node genera-pdf.mjs` crea il PDF.
- Copertine: `node export-copertine.mjs` → `exports/copertina-a…d.png`; `exports/copertine-confronto.jpg`.
- `caption-bozza.txt`: la caption, già passata da `caption_check.py` (CAPTION PRONTA).

## Prove dei prompt (regola 3, controllo interno, simulato)
Almeno 2 per categoria. Ho risposto io come risponderebbe Claude e ho guardato se il risultato serve davvero.

| N. | Prompt | Prova | Esito |
|---|---|---|---|
| 1 | Impara da zero | [ABILITÀ] = Excel | Percorso in 6 tappe e prima lezione (celle, somme) con esercizio. Buono. |
| 8 | Esercizi su misura | [ARGOMENTO] = le frazioni | 30 esercizi in 3 livelli, soluzioni tenute per dopo. Buono. |
| 13 | Basta rimandare | [COMPITO] = dichiarazione dei redditi | 7 passi da 10–20 minuti, il primo è «cerca la CU». Buono. |
| 19 | Menu e spesa | 3 persone, 80 euro | Menu e lista per reparto. La prima versione («fammi il menu della settimana») non aveva persone, budget e tempo, e veniva un menu generico: **riscritto**. I prezzi sono stime. |
| 22 | Curriculum su misura | annuncio di impiegata amministrativa | Se manca il curriculum Claude lo chiede: va incollato insieme all'annuncio. La prima versione («Migliora il curriculum [ANNUNCIO]») non diceva di confrontarli: **riscritto**. |
| 24 | Simulazione di colloquio | [RUOLO] = cassiere | Una domanda alla volta, poi un voto e una risposta migliore. Buono. |
| 32 | Trova l'errore | codice Python con un indice sbagliato | Trova la causa, la correzione e come evitarla. Buono. |
| 37 | Spiegami l'errore | «ModuleNotFoundError» | Spiegazione semplice e il comando per installare. Buono. |
| 43 | Apertura che ferma | prima era «hook» | Ho tolto la parola inglese: ora è «frase d'apertura». 15 varianti, alcune troppo urlate: c'è già «senza esagerare» nel prompt. Buono. |
| 47 | Un carosello | [ARGOMENTO] = risparmiare sulla spesa | 7 slide con titolo e testo breve. Buono. |
| 52 | Valuta l'idea | un servizio di lezioni di smartphone per anziani | Analisi completa con un test economico per provarla. Buono. |
| 58 | Il prezzo giusto | prima era senza costi | Senza il costo Claude inventava i prezzi del mercato. Ho aggiunto [COSTO]: **riscritto**. |
| 62 | Riassumi il documento | regolamento del condominio | Punti chiave, scadenze e cose da fare. Buono. |
| 70 | Controlla i fatti | testo con una data sbagliata | Divide sicuro, dubbio e da verificare; segnala la data. Non può controllare tutto senza ricerca web, ma lo dice. Buono. |
| 74 | Il sollecito | mail al padrone di casa | Breve e gentile, senza tono passivo-aggressivo. Buono. |
| 75 | Correggi l'italiano | testo con 6 errori | Li corregge tutti e spiega i 3 più importanti. Buono. |
| 81 | Cosa può fare l'AI | lavoro da segretaria in uno studio medico | Elenco ordinato (appuntamenti, promemoria, mail). Buono. |
| 84 | I miei programmi AI | [OBIETTIVO] = un sito per il mio negozio | Utile, ma i nomi dei programmi cambiano spesso e Claude può non conoscere gli ultimi: da sapere. |
| 93 | Mettimi in dubbio | «Comprare casa conviene sempre» | Argomenti a favore e contro, presupposti nascosti, cosa farebbe cambiare idea. Buono. |
| 100 | Il mio sistema | — | Molto aperto: Claude fa prima diverse domande. Va bene, ma è il meno immediato. |

Nessun prompt di salute: la categoria 10 del proprietario non ne ha.

## Dubbi per il proprietario
1. **Leggibilità.** Il testo delle schede è a 21 px (la skill vuole almeno 28 px nei testi lunghi). Sul telefono si legge con fatica, come nell'originale, che però è ancora più piccolo. Se vuoi più leggibile: **2 slide per categoria** (5 schede a 28 px ciascuna) = 22 slide, oltre il limite di 20 di Instagram. Alternativa: 2 slide solo per le 4 categorie più utili, o 5 schede per slide con i prompt più lunghi e il resto nel PDF.
2. **Niente commenti fissati con i prompt.** I 100 prompt sono circa 10.000 caratteri; 3 commenti fissati ne tengono 6.600. Il posto giusto è il PDF.
3. **«Programmare» è la 04**, ma al nostro pubblico serve meno di Scrivere o Ricerca. Si può spostare in fondo (cambia solo l'ordine in `prompts.json`).
4. **Il PDF** lo mandi tu in privato a chi commenta «100» (a mano o con un risponditore automatico). Se arrivano tanti commenti, serve un risponditore.
5. **Prompt corti.** Per stare nella griglia i prompt hanno 15–20 parole, non le 100 della skill. In caption e nel PDF c'è il trucco «Se ti manca un'informazione, chiedimela prima di rispondere».
6. **Riga «Commenta «100» per avere il PDF»** in fondo a ogni categoria: si può togliere se pesa troppo.

## Musica e orari
Da fare nel modo «finale».

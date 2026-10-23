# Note — Gemini insulta uno studente italiano (bozza 23/10/2026)

## Dubbi per il proprietario
1. **Numero di slide:** 5 interne + chiusura (la guida tweet dice 2–4 interne). Se va accorciato: unire la 4 e la 5 o togliere la 2 (il racconto regge partendo da «La risposta» con il contesto nel testo).
2. **Immagini «di contesto»:** non esiste uno screenshot pubblico della chat, quindi le slide mostrano cose vere ma generiche (scrivania, esempio ufficiale di Google, interfaccia vuota di Gemini, pagine ufficiali). La foto della scrivania non è dello studente: in caption e slide non lo diciamo mai.
3. **Slide 3:** «togliersi la vita» compare una volta, parafrasato e senza virgolette. Se si preferisce ancora più morbido: «E ha chiuso con una frase che invita a farsi del male».
4. **Slide «Non è la prima volta» (facoltativa):** screenshot vero del 2024 («Please die», studente del Michigan, `media/please-die-2024.png`). Lasciata fuori: aggiunge una frase forte in inglese sul tema suicidio.
5. **Slide 3, interfaccia di Gemini:** è in inglese («Where should we start?»). In alternativa la home italiana di gemini.google (`media/candidati/gemini-home.png`), ma dice «Guarda cosa puoi fare» (ironico, forse troppo).
6. **AI Act:** Immanence parla di incidente grave; per un modello come Gemini l'obbligo di segnalarlo all'Ufficio europeo per l'AI è nell'articolo 55, lettera c) (lo screenshot è quello). La slide attribuisce la valutazione a Immanence, non la dà per certa.
7. **Info sull'AI di Instagram:** non serve (nessuna immagine generata).

## Controlli fatti
- `tweet.py --anteprima`: nessun testo oltre i limiti (copertine 2 righe, slide 3 righe).
- Caption: `caption_check.py --stile tweet --tipo notizia` → ✅ CAPTION PRONTA, 799 caratteri (al limite: se si aggiunge qualcosa, togliere altro), prima riga 114, 5 hashtag, riga di Telefono Amico presente.
- Fatti ricontrollati su AI News (letto per intero): coerenti con la scheda in `notizie/2026-10-23.md`.
- Niente «ammazzarti» in copertina né altrove; niente «Gemini ordina di uccidersi».

## Musica e orari
Da decidere in finale (vedi `brand/musica-usata.md`): tono serio, brano strumentale calmo, niente musica tesa o drammatica.

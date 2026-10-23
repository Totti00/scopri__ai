# Note — Istruzioni IKEA in 3D (solo Reel, 23/10/2026)

## Bozza: tre anteprime tra cui scegliere
| File | Stile | Testo | Pezzo di video |
|---|---|---|---|
| `reel-anteprima.png` (`reel.json`) | Electric Mono (`reel.py`) | sopra «Le istruzioni IKEA della BILLY, in 3D» · titolo «La libreria si *monta* da sola» | 1,4 → 20,0 s (18,6 s): pezzi a terra con le etichette, viti e tasselli che entrano, fianchi che si alzano, telaio |
| `reel-b-anteprima.png` (`tweet-b.json`) | Tweet (`tweet.py`) | «Un designer ha trasformato il manuale IKEA in 3D: la libreria *BILLY* si monta da sola, un passo alla volta.» | 20,7 → 32,0 s (11,3 s): pagine del manuale che si sfogliano, la libreria si alza e viene finita |
| `reel-b-classico-anteprima.png` (`reel-b.json`) | Electric Mono (`reel.py`) | sopra «Gratis online, con più di 20 mobili» · titolo «Il manuale IKEA ora *si muove*» | come la B |

- Caption: `caption-reel.txt` per lo stile Electric Mono, `caption-reel-tweet.txt` per lo stile tweet (stesso contenuto, chiusura dello stile tweet). Al finale resta solo quella giusta, come `caption-reel.txt`.
- Il video intero è di 32 s: se il proprietario preferisce il video intero basta togliere `inizio` e `durata`.
- La copertina (`reel-copertina.jpg`) è prevista a 4,0 s per la A (vite che entra) e a 8,8 s dall'inizio del pezzo per la B (libreria in piedi).
- Tecnica: `reel.py` va lanciato con `/usr/bin/python3` (con `/usr/local/bin/python3` Pillow non si carica).

## Dubbi e cautele
- **"Fatto con un'AI (Claude)": NON confermato.** Lo dicono solo commenti; l'autore e GIGAZINE non lo scrivono. Per questo né il titolo né la caption parlano di AI, e manca di proposito l'hashtag #intelligenzaartificiale (il controllo della caption lo segnala come avviso).
- Non è un progetto di IKEA ("IKEA non mi ha pagato", dice l'autore). Il video mostra il manuale IKEA originale (copyright Inter IKEA Systems): lo mostra l'autore nel suo video, noi non lo riproduciamo a parte.
- Su Hacker News e daily.dev alcuni segnalano errori nel modello 3D (posizione delle viti, ripiani).
- Nel video ci sono i pannelli dell'interfaccia del sito con scritte piccole in inglese: si leggono poco, ma fanno capire che è un sito vero. Lo `zoom` non serve (niente bordi).

## Audio
Il video ha l'audio originale (musica, volume medio −17 dB): il Reel lo tiene (regola del 22/10/2026). Se il proprietario preferisce un brano di Instagram, solo strumentale, mai già usato (`brand/musica-usata.md`), umore tranquillo-curioso da fai-da-te:
1. **Khruangbin – Maria También** (strumentale; chitarra calda e ritmata)
2. **Tycho – Awake** (strumentale; elettronica luminosa, va con la stanza 3D)
3. **Vulfpeck – Dean Town** (strumentale; basso allegro, tono leggero)
Se tra i brani ↗ di tendenza c'è uno strumentale adatto, ha la precedenza.

## Orario
Reel alle **20:00** di oggi, venerdì 23/10/2026.

## Musica usata
Da scrivere quando il proprietario sceglie (anche in `brand/musica-usata.md`).

## Finale (23/10/2026)
- Scelta del proprietario: **versione B in stile tweet** (`tweet.json`, uguale a `tweet-b.json`), con due correzioni:
  testo «Un designer ha trasformato il manuale IKEA in 3D: ora vedi *ogni vite* andare al suo posto.» (3 righe) e
  **video intero di 32 s con l'audio originale** (niente `inizio`/`durata`).
- Copertina `reel-copertina.jpg` a 29,0 s: libreria quasi finita, ultimo ripiano che entra.
- `reel-completo.mp4` è una copia di `reel.mp4` (il video non è tagliato).
- Caption finale: `caption-reel.txt` (stile tweet). `caption-reel-tweet.txt` è la versione della bozza.
- `reel-anteprima.png` è stata rifatta con il testo nuovo (la vecchia anteprima della A è stata sovrascritta).
- Avviso del controllo caption che resta: manca #intelligenzaartificiale, di proposito (l'AI non è confermata).

## Testo finale (scelto dal proprietario, 23/10)
«Le istruzioni IKEA *prendono vita* 🤯 Guarda cosa ha fatto questo designer 👇» — sostituisce «…ora vedi ogni vite andare al suo posto» (non abbastanza d'impatto per chi scorre i Reel).

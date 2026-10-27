# Note — Reel "teletrasporto di Goku" (bozza, 27/10/2026)

Reel senza carosello. Quattro versioni da scegliere:

| File | Stile | Testo | Anteprima |
|---|---|---|---|
| `reel.json` | classico | sopra «Il gesto di Goku, ma in videochiamata» · «Due dita sulla fronte e *sparisce* dalla call» | `reel-anteprima.png` |
| `reel-b.json` | classico | sopra «Un programmatore italiano ci è riuscito» · «Il teletrasporto di Goku ora *esiste*» | `reel-b-anteprima.png` |
| `tweet.json` | tweet | «Il teletrasporto di Goku ora *esiste* davvero: due dita sulla fronte e l'AI ti fa sparire dalla videochiamata.» | `reel-tweet-anteprima.png` |
| `tweet-b.json` | tweet | «Riunione noiosa? Fai il gesto di Goku e *sparisci*. I colleghi vedono solo la stanza vuota.» | `reel-tweet-b-anteprima.png` |

## Video
- Tutte e quattro: da 1,4 s alla fine (22,2 s). A 1,4 s le due dita stanno già andando sulla fronte; a 3,0 s la stanza è vuota; riappare a ~6 s. Poi 8–15 s dentro una call di Microsoft Teams ("Stand Up Meeting"), 15–23 s in un'altra app di videochiamata (sparisce di nuovo a ~17–18 s).
- Tolto solo 0–1,4 s: lui indica la webcam con la mano tesa, il gesto non è ancora partito. Il video intero va in `reel-completo.mp4` nel finale.
- Classici: `formato` originale, `compatto`, `zoom` 1.35 (stringe un po' su monitor e finestra della webcam). Tweet: finestra automatica 4:5, mostra grande la finestra della webcam (resta fuori "Parte 3").
- Copertina: 3,2 s (stanza vuota dopo il gesto). Da rivedere nel finale: forse meglio il gesto (2,5 s).
- Il testo bruciato dell'autore "POV: Crei un modo migliore per abbandonare i meeting" resta: non si toglie con lo zoom (accettato dal regista).

## Cautele
- **Non fa uscire dalla riunione**: ti fa sparire dall'inquadratura, i colleghi vedono la stanza vuota. Titoli e caption lo rispettano ("sparisce dalla call" = dal video della call; in caption "Non esci dalla call: sparisci solo dallo schermo").
- "Il teletrasporto ora esiste" è un gioco con Dragon Ball: si capisce dal video che è un effetto della webcam.
- Serve OBS (telecamera virtuale) e un computer: non è un'app da telefono.
- L'autore si nomina solo in caption, mai sul Reel.

## Caption
- `caption-reel.txt`: chiusura dello stile tweet ("Tu cosa ne pensi?", fonte, invito). CAPTION PRONTA con `--stile tweet --formato reel` (444 caratteri).
- `caption-reel-classico.txt`: stessa caption nell'ordine dei Reel classici (invito, domanda, Fonti). CAPTION PRONTA con `--formato reel` (431 caratteri). Si usa se il proprietario sceglie un Reel classico.

## Audio, orario
- Audio originale del video (regola del 22/10/2026). Attenzione: nel post dell'autore c'è "Ultra Instinct Mastered" (cover di Dragon Ball Super): Instagram potrebbe silenziare il Reel per i diritti. In quel caso, musica strumentale elettronica carica dalla libreria di Instagram (mai un brano già in `brand/musica-usata.md`), meglio se di tendenza ↗.
- Uscita consigliata: **20:00 di oggi, 27/10/2026**.

## Come è stato fatto
- `reel.py` e `tweet.py` lanciati con `/usr/bin/python3`.
- `tweet.py --anteprima` scrive `reel-anteprima.png`: rinominata subito in `reel-tweet-anteprima.png` / `reel-tweet-b-anteprima.png`, poi rifatte le classiche.
- `reel-b.json`: il primo titolo «Ha insegnato alla webcam il *teletrasporto*» andava su 3 righe ("Da sistemare"): sostituito.

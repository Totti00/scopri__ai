# Fonti — Claude e i numeri della NSA (bozza, 17/10/2026)

Consultate il 17/10/2026, mattina.

## Notizia
| Livello | Fonte | Data | Cosa conferma |
|---|---|---|---|
| 1 (ufficiale) | Anthropic, "Claude reveals ECDSA curve origins" — https://www.anthropic.com/research/ecdsa-curve-origins | 16/10/2026 | Claude ha trovato l'origine dei semi di P-192, P-224, P-256, P-384, P-521 "in under half an hour": generatore `lrand48` degli anni '90 inizializzato con l'ora del computer (`srand48`), date tra maggio 1997 e aprile 1998; non era l'hash di una frase ("Give Bob and Jerry a raise"); 36.864 $ donati a ISRG; frasi del ragionamento di Claude; "non è un attacco alla crittografia". |
| Esperto indipendente | Filippo Valsorda, "The NIST Elliptic Curves Seeds Bounty Has Been Claimed" — https://words.filippo.io/seeds-solved/ | 16/10/2026 | Taglia riscossa il 15/10/2026 dalla squadra di Anthropic; Valsorda ha riscritto l'algoritmo in Go e il calcolo torna; taglia di 12.288 $ triplicata a 36.864 $ perché donata a ISRG (l'ente di Let's Encrypt). |
| Testata (non nella nostra lista) | CoinDesk, Shaurya Malwa, "'Wow, it's a real discovery': Claude cracks a 25-year NSA number mystery" — https://www.coindesk.com/tech/2026/10/17/wow-it-s-a-real-discovery-claude-cracks-a-25-year-nsa-number-mystery | 17/10/2026 02:39 EDT | Riprende Anthropic e Valsorda (taglia 12.288 → 36.864 $, ISRG, "meno di mezz'ora"). Non fa verifiche proprie e non sente esperti esterni. |
| Riprese deboli (solo segnali) | Investing.com (anche in italiano), Unite.AI (anche in italiano), The Defiant, KuCoin, OfficeChai | 16–17/10 | — |

**Seconda fonte di livello 2 (testate di `fonti.md`):** cercata il 17/10 mattina su Ars Technica, The Register, The Verge, TechCrunch, Wired, Engadget, 404 Media, MIT Technology Review (feed RSS) e su ANSA, Wired Italia, HDblog, DDay.it, Punto Informatico, Il Post, Tom's Hardware, Italian Tech (feed), più Google News in inglese e in italiano. **Nessuna l'ha ripresa finora.** La regola 1 è comunque rispettata (Anthropic = livello 1, più la conferma indipendente dell'esperto che aveva messo la taglia, più CoinDesk). Da ricontrollare prima della pubblicazione (vedi `note.md`).

In caption: "Fonti: Anthropic, Filippo Valsorda (words.filippo.io), CoinDesk" (aggiungere la testata di livello 2 se esce).

## Immagini e grafica
- **Simbolo di Claude (la "scintilla")**: tracciato ufficiale preso da https://claude.ai/favicon.svg (Anthropic), colore originale #D97757; salvato in `media/claude-simbolo.svg`. Ridisegnato da noi in 3D (estrusione con bordo arrotondato) col renderer della skill: `assets/generated/spark.png` (oggetto `spark`). Lo stesso simbolo è anche su Wikimedia Commons (File:Claude AI symbol.svg, CC0), che lo attribuisce ad Anthropic.
- **Curva ellittica di cromo e vetro** (`assets/generated/curve.png`, oggetto `curve`): creata da noi, è il grafico di y² = x³ − 3x + 1 (stessa "a = −3" delle curve NIST, ma non è P-256: è un disegno).
- **Lente d'ingrandimento** (`assets/generated/magnifier.png`): già nostra, dal primo carosello.
- **Numeri sulle slide**: i semi veri pubblicati nello standard FIPS 186 (P-256: C49D3608 86E70493 6A6678E1 139D26B7 819F7E90; sullo sfondo delle copertine anche P-192, P-224, P-384, P-521). Il seme di P-256 è riportato anche nella pagina di Anthropic.
- Nessuna foto o video di terzi: il video animato di Anthropic (5 min) non è stato usato in questa bozza.

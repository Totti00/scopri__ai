# Fonti — Claude e i numeri della NSA (finale, 17/10/2026)

Consultate il 17/10/2026: notizia e prima ricerca al mattino (bozza), ricontrollo delle testate e video verso le 09:00 (finale).

## Notizia
| Livello | Fonte | Data | Cosa conferma |
|---|---|---|---|
| 1 (ufficiale) | Anthropic, "Claude reveals ECDSA curve origins" — https://www.anthropic.com/research/ecdsa-curve-origins | 16/10/2026 | Claude ha trovato l'origine dei semi di P-192, P-224, P-256, P-384, P-521 "in under half an hour": generatore `lrand48` degli anni '90 inizializzato con l'ora del computer (`srand48`), date tra maggio 1997 e aprile 1998; non era l'hash di una frase ("Give Bob and Jerry a raise"); 36.864 $ donati a ISRG; frasi del ragionamento di Claude; "non è un attacco alla crittografia". |
| Esperto indipendente | Filippo Valsorda, "The NIST Elliptic Curves Seeds Bounty Has Been Claimed" — https://words.filippo.io/seeds-solved/ | 16/10/2026 | Taglia riscossa il 15/10/2026 dalla squadra di Anthropic; Valsorda ha riscritto l'algoritmo in Go e il calcolo torna; taglia di 12.288 $ triplicata a 36.864 $ perché donata a ISRG (l'ente di Let's Encrypt). |
| **2 (testata della nostra lista)** | **Tom's Hardware Italia**, Andrea Maiellano, "Claude risolve in 30 minuti un mistero della NSA rimasto irrisolto per 25 anni" — https://www.tomshw.it/altro/claude-risolve-in-30-minuti-un-mistero-della-nsa-rimasto-irrisolto-per-25-anni | 17/10/2026, 09:29 | Meno di mezz'ora; semi consegnati dalla NSA e adottati nel 2000 (FIPS 186-2); `lrand48`, riduzione LLL; timestamp tra il 1997 e il 1998, P-256 = 1.842° candidato di una sequenza avviata il 16/08/1997; il dubbio di Claude ("test simulato") e "Wow, è una scoperta reale"; Valsorda ha rifatto il calcolo in Go; 36.864 $ a ISRG; "non è una falla". In fondo all'articolo: "Fonte dell'articolo: www.coindesk.com" (è una ripresa, senza verifiche proprie). |
| Testata (non nella nostra lista) | CoinDesk, Shaurya Malwa, "'Wow, it's a real discovery': Claude cracks a 25-year NSA number mystery" — https://www.coindesk.com/tech/2026/10/17/wow-it-s-a-real-discovery-claude-cracks-a-25-year-nsa-number-mystery | 17/10/2026 02:39 EDT | Riprende Anthropic e Valsorda (taglia 12.288 → 36.864 $, ISRG, "meno di mezz'ora"). Non fa verifiche proprie e non sente esperti esterni. |
| Riprese deboli (solo segnali) | Investing.com (anche in italiano), Unite.AI (anche in italiano), The Defiant, KuCoin, OfficeChai, FourWeekMBA, DEV Community | 16–17/10 | — |

**Ricontrollo delle testate (finale, 17/10 verso le 09:00):** **trovata Tom's Hardware Italia** (livello 2, "Tecnologia" italiane in `fonti.md` del progetto). Ancora niente su Ars Technica (feed generale e sicurezza), The Register (feed generale e sicurezza), The Verge (feed generale e AI), TechCrunch, Wired, Engadget, 404 Media, MIT Technology Review, ANSA Tecnologia, Wired Italia, HDblog, DDay.it, Punto Informatico, Repubblica Tecnologia, Corriere Tecnologia (feed RSS). Il Post, Agenda Digitale e StartupItalia non si aprono da qui (403). La ricerca web non può aprire Ars, The Verge, Wired, Reuters, Repubblica e Corriere: li ho controllati dai feed. L'articolo di Tom's Hardware è dietro Cloudflare: letto con il browser automatico (Chromium).

**Regola 1 rispettata:** Anthropic (livello 1) + Tom's Hardware Italia (livello 2) + la conferma indipendente di Valsorda, l'esperto che aveva messo la taglia.

In caption: "Fonti: Anthropic, Filippo Valsorda (words.filippo.io), Tom's Hardware, CoinDesk".

## Video (slide 3)
- **Video animato ufficiale di Anthropic** sulla scoperta ("Where the NIST seeds came from", 5 min 8 s, 1920×1080, 30 fps, con voce): https://cdn.sanity.io/files/4zrzovbb/website/56865322bd9974c7be23abf7d654fb5a79155791.mp4 (file del sito di Anthropic, indicato dal proprietario). Scaricato il 17/10/2026, ~08:30. **Chi l'ha fatto:** Anthropic; nel finale il video stesso dice "We all came to look, and asked Claude to make this video" e "Narrated with an AI-generated voice". In caption basta "Anthropic" (già nelle fonti).
- **Cosa abbiamo usato** (montaggio nostro, senza audio, in monocromo blu dentro la slide; tagliati fuori i sottotitoli inglesi e la barra di avanzamento):
  - `media/anthropic-montaggio.mp4` → `exports/slide-03.mp4` (47,1 s): 0:08,9–0:25,6 (persona al computer, agosto 1997; il seme di P-256 scritto sul foglio) · 3:59,4–4:16,4 (t = 871.696.354 → 16 agosto 1997, 01:52:34 UTC; le date delle cinque curve) · 4:37,2–4:51,6 (il computer con `srand48(time(NULL))`, l'orologio della "mezz'ora", le persone davanti a "P-256 = srand48(871696354), candidate 1,842").
  - `media/anthropic-montaggio-60s.mp4` → `exports/slide-03-completo.mp4` (59,5 s): 0:07,6–0:25,6 · 3:48,3–4:16,4 (in più: Claude che riavvolge il generatore fino al candidato 1.842) · 4:37,2–4:51,6.
  - Il video intero (5 min) resta fuori dal repository (`.gitignore`), come i `media/*.mp4` e i `-completo.mp4`.

## Immagini e grafica
- **Simbolo di Claude (la "scintilla")**: tracciato ufficiale preso da https://claude.ai/favicon.svg (Anthropic), colore originale #D97757; salvato in `media/claude-simbolo.svg`. Ridisegnato da noi in 3D (estrusione con bordo arrotondato) col renderer della skill: `assets/generated/spark.png` (oggetto `spark`). Lo stesso simbolo è anche su Wikimedia Commons (File:Claude AI symbol.svg, CC0), che lo attribuisce ad Anthropic.
- **Curva ellittica di cromo e vetro** (`assets/generated/curve.png`, oggetto `curve`): creata da noi, è il grafico di y² = x³ − 3x + 1 (stessa "a = −3" delle curve NIST, ma non è P-256: è un disegno).
- **Numeri sulle slide**: i semi veri pubblicati nello standard FIPS 186 (P-256: C49D3608 86E70493 6A6678E1 139D26B7 819F7E90; sullo sfondo della copertina anche P-192, P-224, P-384, P-521). Il seme di P-256 è riportato anche nella pagina di Anthropic.
- Le copertine alternative della bozza (B, C, D, con la lente d'ingrandimento nostra) non sono nel pacchetto finale.

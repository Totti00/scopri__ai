# Versione STILE TWEET (bozza del 22/10/2026, richiesta del proprietario)

_File: `tweet.json` (copertina + 3 slide interne, niente chiusura) e `tweet-b.json` (solo copertina b). Resi con `python3 strumenti/tweet.py … --anteprima` in `exports/slide-01…04.png`, `exports/contact-sheet.jpg`, `exports/copertina-b.png`. La chiave "reel" di `tweet.json` la aggiunge il costruttore del Reel._

### 01 — Copertina
- **Titolo (2 righe, maiuscolo):** DUE FALLE IN *PHP* / SCOVATE DALLE AI (accento lilla su «PHP»)
- **Media:** schermata vera di php.net fatta da noi il 22/10 (`media/phpnet-copertina.jpg`): logo php, versioni 8.4.27 · 8.3.36 · 8.2.35, avviso «Security advisory … 21 Oct 2026» sfumato verso il nero. I lati sono tagliati dalla finestra 1080×900 (logo, versioni e avviso restano).

### 02 — LE HANNO TROVATE LE AI
- **Testo:** Le AI di OpenAI e Wiz hanno scovato due buchi in *PHP*, il programma di circa 7 siti su 10 secondo Wiz. Anche quelli fatti con WordPress. Erano lì dal 2004.
- **Media:** illustrazione ufficiale «PHP2Shell» di Wiz Research, intera (`media/wiz-php2shell.png`).

### 03 — IL PERICOLO
- **Testo:** Senza password, un malintenzionato poteva prendere il controllo del computer che tiene in piedi il sito. Gravità: *9,2 su 10*.
- **Media:** schema ufficiale dell'attacco di Wiz, intero (`media/wiz-schema-attacco.png`).

### 04 — L'ALLARME
- **Testo:** La NSA, l'agenzia di sicurezza americana, ha detto di prepararsi all'aggiornamento. In mezza Europa, siti di governo *spenti* per precauzione.
- **Media:** screenshot del post vero di @NSACyber del 21/10 (`media/nsa-post.png`), intero.
- Nota: il post NSA dice "be prepared for an update" (prepararsi all'aggiornamento), non "spegnete": per questo qui non scriviamo "aggiorna o spegni" come nella versione Electric Mono.

### Copertina b (`exports/copertina-b.png`)
- **Titolo:** HAI UN SITO? AGGIORNA / *PHP* SUBITO · stessa schermata di php.net

### Caption (stile tweet, controllata con `caption_check.py --stile tweet`: CAPTION PRONTA, 789 caratteri, 5 hashtag)
> ⚠️🐘 Due falle gravi in PHP, il programma dietro WordPress, scovate dall'intelligenza artificiale di OpenAI e Wiz.
>
> Erano nel codice dal 2004. Gli esperti avevano visto i primi segnali nel 2024, ma senza capire come sfruttarle. Le AI hanno mostrato che si poteva.
>
> Il rischio: senza password, qualcuno poteva prendere il controllo del server che tiene in piedi un sito. Ieri in mezza Europa alcuni siti di governo sono stati spenti per precauzione.
>
> Se navighi e basta, non devi fare niente. Se hai un sito, chiedi a chi lo gestisce se PHP è già aggiornato.
>
> Tu cosa ne pensi? 🤔💬
>
> Fonti: PHP Foundation, Wiz, OpenAI, Wired, BBC, TechCrunch, The Verge
>
> 📥 Commenta «100» e ti mando i 100 prompt per Claude in PDF.
>
> #intelligenzaartificiale #php #wordpress #sicurezzainformatica #cybersecurity

---

# Versione ELECTRIC MONO (alternativa, resta valida)
_Le sue immagini sono state spostate in `exports/electric-mono/` (slide-01…09, copertine b–g, contact sheet), perché `tweet.py` riscrive `exports/slide-NN.png`. Il sorgente è sempre `index.html` / `copertine.html`._

_Copy in italiano · formato: statico (nessun video vero: niente MP4) · 8 slide + chiusura · BOZZA del 22/10/2026_

**In una frase:** per chi naviga e per chi ha un sito: le AI di OpenAI e Wiz hanno scovato due falle in PHP, il programma di circa 7 siti su 10, nascoste dal 2004; ieri siti di governo spenti; chi ha un sito chiede subito l'aggiornamento. Invito: mandarlo a chi ha un sito. · **Struttura:** Scoperte (scelta del proprietario), il colpo più forte (l'AI che le trova, il pericolo) in slide 2 e 3.

**Immagini:** tutte vere e a colori, intere (non tagliate dentro il riquadro): schermata di php.net fatta da noi il 22/10 (logo PHP, nuove versioni, avviso "update now" del 21 Oct 2026); schema ufficiale del blog di Wiz; screenshot del post X della NSA (è la notizia); logo PHP da Wikimedia Commons; schede di interfaccia fatte col codice. Niente scritte sotto le immagini, niente etichette sopra.

### 01 — Copertina (DARK)
- **Riga piccola (kicker):** Dal 2004 nel programma di circa 7 siti su 10
- **Titolo (2 righe):** Due falle in *PHP* / scovate dalle AI (riquadro blu: «PHP»)
- **Visual:** schermata vera di php.net, grande (~60% della slide): logo php, versioni 8.5.12 · 8.4.27 · 8.3.36 · 8.2.35, «Security advisory: Critical remote code execution vulnerabilities, update now» · 21 Oct 2026.
- In basso la barra blu «SCORRI PER SCOPRIRE» (la mette il motore). Niente etichetta di rubrica.
- **Alternative rese:** vedi in fondo, "Copertine".

### 02 — La scoperta (LIGHT)
- **Pill:** La scoperta · **Titolo:** Le AI hanno trovato / due buchi in *PHP*
- **Testo:** PHP è il programma che fa funzionare circa 7 siti su 10, secondo Wiz. Anche quelli fatti con WordPress. I buchi erano lì dal 2004.
- **Visual:** scheda nostra con il logo PHP vero e «Gira su PHP: WordPress · Wikipedia · Drupal · Joomla».

### 03 — Il pericolo (DARK)
- **Pill:** Il pericolo · **Titolo:** Hanno mostrato come / *entrare* nei server
- **Testo:** Senza password, un malintenzionato poteva prendere il controllo del computer che tiene in piedi il sito. Gravità: 9,2 su 10.
- **Visual:** schema ufficiale di Wiz: una richiesta fatta apposta → WordPress, Drupal, Joomla → «Remote Code Execution» (controllo a distanza).

### 04 — L'allarme (LIGHT)
- **Pill:** L'allarme · **Titolo:** La NSA: aggiorna / o *spegni* il sito
- **Testo:** L'agenzia di sicurezza americana l'ha scritto su X. Lo stesso consiglio è arrivato dall'agenzia inglese per la sicurezza informatica.
- **Visual:** screenshot del post vero di @NSACyber (21 ottobre, 63.700 «mi piace»).

### 05 — Ieri (ACCENT)
- **Pill:** Ieri · **Titolo:** Siti spenti / per *precauzione* (riquadro bianco)
- **Testo:** In attesa della riparazione, in mezza Europa si è preferito staccare la spina.
- **Scheda** («Offline per precauzione»): Governo finlandese · Siti del governo francese · Agenzia per la sicurezza informatica olandese · Porto di Rotterdam · Una parte di Wikipedia

### 06 — Chi le ha trovate (DARK)
- **Pill:** Chi le ha trovate · **Titolo:** Due squadre, due AI, / la stessa *scoperta*
- **Righe:**
  - **2024** · Gli esperti di PHP vedono i primi segnali, ma non capiscono come sfruttarli.
  - **11 agosto** · Calif, con GPT-5.6 Sol di OpenAI, segnala la falla. Lo stesso giorno lo fa anche OpenAI.
  - **24 agosto** · Wiz (Google) segnala altre strade, trovate con Gemini 4 Argon.
  - **21 ottobre** · Esce la riparazione.

### 07 — Per te (LIGHT)
- **Pill:** Per te · **Titolo:** Hai un sito? / Chiedi *questo* oggi
- **Testo:** Se navighi e basta, non devi fare niente.
- **Scheda** («Da mandare a chi ti gestisce il sito»): «Ciao, il mio sito usa PHP? È già aggiornato a 8.5.12, 8.4.27, 8.3.36 o 8.2.35?»
- **Riga in fondo alla scheda:** PHP 8.1 o più vecchio non riceve più riparazioni: va cambiato. WordPress non va aggiornato: va aggiornato PHP.

### 08 — In breve (ACCENT)
- **Pill:** In breve · **Titolo:** Da *ricordare*
- **Righe:** 01 Due falle in PHP, lì dal 2004 · 02 Le hanno scovate le AI · 03 Gravità 9,2 su 10 · 04 Siti di governo spenti · 05 Hai un sito? Aggiorna PHP

### 09 — Chiusura (DARK)
- **Titolo:** Mandalo a / chi ha un *sito*
- **Pulsante pieno blu** (aereo di carta): Mandalo a un amico
- **Riga sotto, più piccola** (campana del logo): Seguici per non perdere le prossime notizie
- Niente "Notizia verificata", niente @handle.

### Caption
> ⚡ Due falle gravi in PHP, il programma dietro WordPress, scovate dall'intelligenza artificiale di OpenAI e Wiz.
>
> 🔍 Erano nel codice dal 2004. Gli esperti di PHP avevano visto i primi segnali nel 2024, ma senza capire come sfruttarle. Le AI hanno mostrato che si poteva, in poche ore.
>
> ⚠️ Il rovescio: ora che i dettagli sono pubblici, l'AI può aiutare anche chi attacca. Per questo l'aggiornamento va fatto oggi, non la settimana prossima.
>
> 👉 Se navighi e basta, non devi fare niente. Se hai un sito, scrivi a chi lo gestisce.
>
> 📩 Mandalo a chi ha un sito o un blog WordPress
> Lo sapevi che il tuo sito potrebbe girare su PHP? 👇
>
> Fonti: PHP Foundation, Wiz, OpenAI, Wired, BBC, TechCrunch, The Verge
>
> #intelligenzaartificiale #php #wordpress #sicurezzainformatica #cybersecurity

**Hook alternativi (copertine rese):**
- b) [Nel programma di circa 7 siti su 10] Due falle in *PHP* / nascoste dal 2004 (la forma letterale del titolo a, senza "AI" nel titolo)
- c) [Le hanno scovate le AI] Due falle in *PHP* / nascoste dal 2004
- d) [Ieri, in mezza Europa, siti di governo spenti] Due falle in *PHP* / trovate da un'AI (titolo c del menu)
- e) [Due falle trovate dalle AI, nascoste dal 2004] Hai un sito? / Aggiorna *PHP* subito (titolo b del menu)
- f) come la a, ma con la seconda idea di visual: logo PHP vero (Wikimedia) grande con la nostra lente 3D di vetro sopra
- g) come la a, con l'illustrazione ufficiale «PHP2Shell» di Wiz

**Note sui contenuti:**
- "circa 7 siti su 10" è una stima di Wiz (W3Techs dice 69,3% dei siti di cui si conosce il linguaggio; la BBC non la verifica): sempre con "circa" e "secondo Wiz" nella slide 2.
- "nascoste dal 2004": Wired, TechCrunch e BBC (CERT-EU) dicono da PHP 5 (luglio 2004); Wiz scrive "almeno da PHP 5.4". Mai "nessuno lo sapeva": la PHP Foundation aveva visto i primi segnali nel 2024 (lo diciamo in slide 6 e in caption).
- Le AI hanno trovato le falle e mostrato il pericolo; non hanno attaccato nessuno. OpenAI: nessun attacco noto prima dell'annuncio; Cloudflare vede "i primi attacchi" dopo.
- Wiz: scoperta il 19 agosto, segnalata il 24 (data della PHP Foundation). Scriviamo "segnala".
- DeviantArt e Pokémon Home: spenti, ma senza dire che è per PHP (BBC): lasciati fuori. Il Parlamento olandese (nel menu) non l'ho ritrovato nelle fonti lette: lasciato fuori; tenuta l'agenzia olandese (BBC).
- Squarespace e Wix non usano PHP (The Verge): si può aggiungere in caption se serve spazio per "chi è al sicuro".

Fonti:
- [PHP Foundation, 21/10/2026](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)
- [php.net, avviso del 21/10/2026](https://www.php.net/)
- [Wiz Research, PHP2Shell](https://www.wiz.io/blog/php2shell-php-rce)
- [Wired](https://www.wired.com/story/this-is-not-a-drill-2-php-vulnerabilities-are-setting-the-internet-on-fire/)
- [BBC](https://www.bbc.co.uk/news/articles/cmly0lg3w5x2o)
- [TechCrunch](https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/)
- [The Verge](https://www.theverge.com/tech/1015906/php2shell-vulnerability-october-2026)
- [NSA Cyber su X](https://x.com/NSACyber/status/2112903220209098897) · [WordPress su X](https://x.com/WordPress/status/2112907323265917274)
- OpenAI "Patch the Planet" (https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/, non leggibile da qui: citata da TechCrunch e The Verge)

### Copertine (rese in `exports/`, confronto in `exports/copertine-confronto.jpg`)
- **slide-01 (a, proposta):** [Dal 2004 nel programma di circa 7 siti su 10] Due falle in *PHP* / scovate dalle AI · schermata vera di php.net
- **copertina-b:** [Nel programma di circa 7 siti su 10] Due falle in *PHP* / nascoste dal 2004 · php.net
- **copertina-c:** [Le hanno scovate le AI] Due falle in *PHP* / nascoste dal 2004 · php.net
- **copertina-d:** [Ieri, in mezza Europa, siti di governo spenti] Due falle in *PHP* / trovate da un'AI · php.net
- **copertina-e:** [Due falle trovate dalle AI, nascoste dal 2004] Hai un sito? / Aggiorna *PHP* · php.net
- **copertina-f:** titolo a · logo PHP vero (Wikimedia Commons) con la nostra lente 3D di vetro
- **copertina-g:** titolo a · illustrazione ufficiale «PHP2Shell» di Wiz Research (elefantino PHP)

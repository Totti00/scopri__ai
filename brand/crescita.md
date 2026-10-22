# Come arrivare a più persone (aggiornato il 15/10/2026)

Regole per caption e pubblicazione, decise dopo aver controllato come funziona Instagram nel 2026.
Valgono per tutti i post. Le schede in `format/` danno la struttura, queste regole vengono prima.

## Cosa guarda Instagram
- Per chi **non ci segue** conta soprattutto quante persone **mandano il post in DM** a qualcuno.
- Per chi ci segue contano i like e il tempo passato sul post.
- Gli hashtag **non portano visualizzazioni**: servono solo a dire di cosa parla il post.
- Dal 30/04/2026 gli account che pubblicano **soprattutto contenuti di altri** escono dai suggerimenti.

Fonti (blog di marketing che riportano le parole di Adam Mosseri, capo di Instagram; i pesi esatti non sono pubblici): kontentino.com, creatorlanehq.com, dataslayer.ai, socialync.io, later.com, rankite.com.

## La caption
Regole complete in `format/carousel-copy.md` §9: i primi ~125 caratteri sono il gancio, la caption aggiunge e non ripete le slide.
1. **Prima riga = parole che la gente cerca, al massimo 125 caratteri** (22/10/2026: oltre, il controllo blocca). Nome del prodotto o dell'azienda + "intelligenza artificiale" (o il tema: salute, lavoro…), dentro una frase-gancio. È la parte che si vede prima di "altro" e che legge la ricerca di Instagram e di Google.
2. **Massimo 5 hashtag**, in fondo, precisi: `#intelligenzaartificiale` + prodotto + tema. Instagram ignora quelli oltre il quinto.
3. **Un invito principale, lo stesso della chiusura** (16/10/2026, `format/carousel-copy.md` §8): per le notizie `📩 Mandalo a …` con una persona precisa ("a chi pensa che l'AI sappia solo scrivere", "al collega che usa ancora Excel a mano"); per prompt e liste `📌 Salvalo per …`; per le serie `🔔 Seguici`. **In caption un invito e una domanda, nient'altro** (22/10/2026): la riga `🔔 Seguici per non perdere le prossime notizie` sta solo sull'ultima slide, non in caption. Se si regala qualcosa ("Commenta «PAROLA» e ti mando…"), quello è l'invito principale e non si aggiunge "Salvalo".
4. **Una domanda vera** per i commenti, sul contenuto. Niente "commenta SÌ", "tagga 3 amici": Instagram li considera esche e mostra meno il post. **Ammesso dal 21/10/2026** (decisione del proprietario): "Commenta «PAROLA» e ti mando …", solo quando si regala davvero qualcosa in privato (es. il PDF con tutti i prompt). Il messaggio privato lo manda il proprietario (a mano o con un risponditore automatico).
5. Le **fonti** restano in fondo ("Fonti: …"), prima degli hashtag.
6. **Lunghezza** (22/10/2026): notizie e curiosità **sotto gli 800 caratteri** (oltre 900 il controllo blocca): le slide raccontano già, la caption dà solo il contesto in più. Le caption lunghe si tengono per i prompt.
7. **Niente elenchi di parole chiave** tra parentesi o in fondo ("[prompt per Claude, Claude AI, …]"): sembrano spam. Le parole si mettono, naturali, nelle prime frasi.

### Caption del carosello e caption del Reel (16/10/2026)
Sono due lavori diversi:
- **Carosello**: chi legge la caption ha già visto le slide. La caption **aggiunge** (contesto, come provarlo, limiti) e non ripete.
- **Reel**: chi lo vede di solito non ci segue e non ha visto nessuna slide. Caption **corta, 2–4 righe**: prima riga con le parole che la gente cerca e il gancio, una riga che dice cosa si vede, lo stesso invito del carosello, la domanda, "Fonti: …" per le notizie, massimo 5 hashtag.

### Controllo automatico
Prima della consegna ogni caption passa `caption_check.py` (nella skill, lo lancia da solo `npm run publish`, anche su `caption-reel.txt`). Controlla: 2.200 caratteri, cosa si vede prima di "altro" (125), parole cercate, massimo 5 hashtag e tutti in fondo, "Fonti: …" per notizie e curiosità (prima degli hashtag; mai nei prompt), un solo invito principale e quello giusto per il tipo, niente riga 🔔 Seguici in caption, notizie sotto gli 800 caratteri, niente elenchi di parole chiave, niente esche ("tagga", "link in bio", "metti like"; "commenta PAROLA e ti mando" è ammesso dal 21/10/2026), una domanda, niente link, poche emoji, nome "Scopri AI".
Se c'è un errore il pacchetto non si scrive. Alla fine stampa la ricevuta **"✅ CAPTION PRONTA"**, che va nel messaggio finale al proprietario.

## Il testo alternativo
Per ogni post si consegna `alt-text.txt`: una riga per slide che descrive cosa si vede, con le parole chiave.
Il proprietario lo incolla in "Impostazioni avanzate → Accessibilità → Scrivi testo alternativo" (per le slide video, se Instagram non dà il campo, si salta).

## Contenuti nostri
Per non passare da pagina che ripubblica:
- ogni slide ha testo, titolo e commento scritti da noi, e i video sono montati da noi (tagliati, uniti, dentro il template);
- mai un video di altri messo da solo, senza la nostra slide intorno;
- i post del venerdì (prompt) e della domenica (curiosità) sono fatti con grafiche nostre: almeno 2 post su settimana sono interamente nostri.

## Quando si pubblica (lo fa il proprietario)
- **Musica** sul carosello: sempre. In `note.md` di ogni post Claude suggerisce 2–3 brani (il proprietario controlla che ci siano nella libreria di Instagram e sceglie). Regole:
  - **solo strumentale**, senza voce (deciso il 15/10/2026): la gente sta leggendo;
  - **mai un brano già usato** (lista in `brand/musica-usata.md`, deciso il 15/10/2026);
  - se tra le canzoni con la freccia **↗ (di tendenza)** ce n'è una strumentale adatta, ha la precedenza;
  - si sceglie il **pezzo più energico** (il punto in cui parte il ritmo), non l'inizio lento;
  - umore per rubrica: news lampo = elettronica carica; news del lunedì = pop allegro; prompt del venerdì = lo-fi tranquillo; curiosità della domenica sera = musica da film, di meraviglia.
- **Prima ora:** rispondere a ogni commento e condividere il post nelle Storie, se possibile con un sondaggio ("Lo proveresti?").
- **Orari:** dopo 2–3 settimane si guardano in Statistiche le ore in cui i follower sono online e si aggiorna `calendario.md`.
- **Collaborazioni:** con la funzione "Collabora" insieme a pagine vicine ma non concorrenti (tech, scuola, lavoro, risparmio). Mai con le pagine di notizie AI.
- **Mai:** comprare follower, gruppi di like reciproci, segui/smetti di seguire.

## Reel
Dal 16/10/2026 il Reel si fa **solo quando c'è un video vero che è una bomba**: una schermata con il titolo e sotto il video, niente scene (`format/5-reel.md`). Arrivano a più persone che non ci seguono, ma solo se il primo secondo cattura.

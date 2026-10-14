# Routine: ricerca notizie (ogni giorno, 07:45)

Segui prima i passi comuni di `routine/README.md`.

## 1. Cerca (notizie delle ultime 24–48 ore)
Nell'ordine:
1. **Sale stampa ufficiali:** Google (blog.google e gemini.google/release-notes), OpenAI (openai.com/news/rss.xml), Anthropic (anthropic.com/news), Meta (about.fb.com/news), Apple (apple.com/newsroom), Microsoft, NVIDIA, Amazon, xAI, Mistral, DeepSeek.
2. **Newsletter:** TLDR AI e TLDR Tech di oggi e di ieri (`https://tldr.tech/ai/AAAA-MM-GG`, `https://tldr.tech/tech/AAAA-MM-GG`), The Rundown AI (`https://rss.beehiiv.com/feeds/2R3C6Bt5wj.xml`).
3. **Testate:** The Verge (rss AI), TechCrunch (feed AI), ANSA Tecnologia, Wired Italia, Google News in italiano (`https://news.google.com/rss/search?q=intelligenza+artificiale&hl=it&gl=IT&ceid=IT:it`).
4. **Reddit** (con `strumenti/leggi-pagina.cjs`): r/technology, r/artificial, r/OpenAI, r/ChatGPT, r/singularity, r/nottheonion (top del giorno).
5. Ricerca web per confermare e per completare.

## 2. Scegli e vota
Tieni solo notizie di tech e AI che interessano o incuriosiscono una persona normale (vedi `CLAUDE.md`, "Di cosa parliamo"). Per ognuna:
- titolo in una riga;
- perché interessa (1 frase);
- 2 fonti che la confermano (almeno una di livello 1 o 2);
- voto da 1 a 5;
- se è già in `archivio/`.

Salva tutto in `notizie/AAAA-MM-GG.md` (anche se il voto è basso: servono per le news del lunedì).

## 3. Se c'è una notizia da 4 o 5
- Prendi la migliore (una sola) e prepara la news lampo seguendo `format/2-news-lampo.md`.
- Cartella: `archivio/AAAA-MM-GG-news-lampo-<argomento>/`.
- In `note.md` scrivi: "Bozza da approvare: il proprietario decide se pubblicarla."
- Nel messaggio finale: titolo, perché vale 4–5, orario consigliato (12:30), e le altre notizie da 4–5 in una riga ciascuna.

## 4. Se nessuna arriva a 4
Salva solo `notizie/AAAA-MM-GG.md`, fai commit e push, e scrivi in una riga: "Oggi niente news lampo" con la notizia migliore e il suo voto.

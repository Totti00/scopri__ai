# Routine: ricerca notizie (ogni giorno, 07:45)

Il regista segue `routine/README.md`. Qui ci sono le indicazioni per questa rubrica (`news`). La sezione 1 la usa il `ricercatore`.

## 1. Cerca (notizie delle ultime 24–48 ore)
Nell'ordine:
1. **Sale stampa ufficiali:** Google (blog.google e gemini.google/release-notes), OpenAI (openai.com/news/rss.xml), Anthropic (anthropic.com/news), Meta (about.fb.com/news), Apple (apple.com/newsroom), Microsoft, NVIDIA, Amazon, xAI, Mistral, DeepSeek.
2. **Newsletter:** TLDR AI e TLDR Tech di oggi e di ieri (`https://tldr.tech/ai/AAAA-MM-GG`, `https://tldr.tech/tech/AAAA-MM-GG`), The Rundown AI (`https://rss.beehiiv.com/feeds/2R3C6Bt5wj.xml`).
3. **Testate:** The Verge (rss AI), TechCrunch (feed AI), ANSA Tecnologia, Wired Italia, Google News in italiano (`https://news.google.com/rss/search?q=intelligenza+artificiale&hl=it&gl=IT&ceid=IT:it`).
4. **Reddit** (con `strumenti/leggi-pagina.cjs`): r/technology, r/artificial, r/OpenAI, r/ChatGPT, r/singularity, r/nottheonion (top del giorno).
5. Ricerca web per confermare e per completare.

## 2. Analisi e scelta
Le fanno l'`analista` e il `selezionatore` (vedi `.claude/agents/`), con queste regole:
- solo notizie di tech e AI che interessano o incuriosiscono una persona normale (`CLAUDE.md`, "Di cosa parliamo");
- tutto finisce in `notizie/AAAA-MM-GG.md`, anche le notizie con voto basso: servono per le news del lunedì;
- news lampo solo con voto **4 o 5**, al massimo una al giorno, cartella `carousels/AAAA-MM-GG-news-<argomento>/` (con la skill `scopri-carousel`);
- orari consigliati: carosello 12:30; Reel (solo se c'è un video bomba, `format/5-reel.md`) alle 20:00 dello stesso giorno.

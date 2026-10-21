# Publishing pack

Every finished carousel ships with its caption, alt texts and (when needed) pinned comments, as separate `.txt` files. Deliver them without being asked: the user had to ask for them on the first carousel.

## Contents
1. publish.json
2. Caption
3. Pinned comments
4. Alt text
5. Final message

---

## 1. publish.json

Write `carousels/<slug>/publish.json`:

```json
{
  "caption": "…",
  "alt": ["slide 1 alt", "slide 2 alt", "…"],
  "pinned": ["comment 1", "comment 2"]
}
```

Then, from the carousel folder:

```bash
npm run publish
```

This writes `pubblicazione/01-caption.txt`, `02-testi-alternativi.txt` (one file with every alt text, each under a "Slide N" line; owner, 20 Oct 2026) and `03-commento-fissato-N.txt`, each holding only the text to paste. It also checks:
- the caption and each comment are ≤ 2,200 characters;
- there is one alt text per exported slide;
- there are ≤ 3 pinned comments;
- alt texts are ≤ 140 characters;
- **the caption rules of Scopri AI**, through `scripts/caption_check.py` (also on `caption-reel.txt` when it exists): what shows before "altro", search words, ≤ 5 hashtags all at the end, "Fonti: …" before the hashtags for news and curiosità (never on prompt posts), one invite of the right kind, no engagement bait ("tagga un amico", "link in bio"; "commenta PAROLA e ti mando…" is allowed since 21/10/2026), one real question, no links, emoji density, the name "Scopri AI". An error stops the pack.

Put `"tipo"` (`notizia`, `curiosita`, `prompt`, `lista`, `serie`; default from the folder name) and `"parole"` (the 2–3 words people search, e.g. `["gemini", "google"]`) in `publish.json`. The run ends with the receipt line(s) `✅ CAPTION PRONTA · …`: paste them in the final message to the user.
Standalone: `python scripts/caption_check.py caption-reel.txt --parole "gemini,google"` (exit 0 only when PRONTA).

## 2. Caption

Italian, following `carousel-copy.md` §9, plus the Scopri AI habits:

- **Carousel caption vs Reel caption.** The carousel caption is read by people who saw the slides: it adds context and never repeats them. The Reel caption is read by people who saw no slide: 2–4 short lines that stand alone (hook with search words, what you see, the invite, the question, sources, hashtags).
- **The first ~125 characters are the hook.** It complements slide 1 without repeating it.
- **Emoji:** about one per block, at the start of a line (🧠 📌 💬 🔒 ✍️ 📅 ⚠️ 🔖 style). The user asked for them.
- **Body:** the context the slides don't hold, such as why it works, how to use it, practical tips and verified facts with their limits.
- **One honesty line about AI**, e.g. "⚠️ L'AI spiega, ma può sbagliare. Verifica sempre…".
- **The CTA at the end**, the same single ask as the closing slide, chosen by type: news → "📩 Mandalo a …", prompts and lists → "📌 Salvalo …", series → "🔔 Seguici". Then one real question. Then, except in *serie*, the line **`🔔 Seguici per non perdere le prossime notizie.`** (prompt: "i prossimi prompt", curiosità: "le prossime curiosità", lista: "i prossimi consigli"): it is required in addition to the single invite and `caption_check.py` doesn't count it as a second one (20 Oct 2026). For news and curiosità, "Fonti: …" right before the hashtags.
- **3–5 specific hashtags** at the very end.
- Natural search keywords the audience would type, in plain Italian.

## 3. Pinned comments

Use them when the carousel's useful content is longer than the caption allows, typically full prompts.

- Split the content across up to 3 comments, each ≤ 2,200 characters. Give each a header line ("I 5 prompt da copiare · parte 1/2"), then the items with their titles.
- No emoji inside prompts, because people paste them straight into an AI.
- The caption must point to them ("Copiali dai commenti fissati qui sotto…"). Mention screenshot text-copy as a fallback: on most phones you can copy text straight from an image.

## 4. Alt text

One per slide, Italian, about 120–140 characters. Formula:

> [role or label]: «headline». [what the visual shows, if it carries meaning]. [pointer, if the full text lives elsewhere]

Examples from the first carousel:
- Cover: «5 prompt prima di firmare». Una lente d'ingrandimento mette a fuoco la clausola «Alla scadenza» di un contratto luce.
- Prompt 1, «Traduci la bolletta»: l'AI spiega ogni voce di spesa e il costo reale per kWh. Testo completo nei commenti fissati.
- Logo Scopri AI. «Salvalo per la prossima offerta. L'AI ti spiega il contratto. La firma, però, resta tua.» Pulsante Salva.

Tell the user where to enter it. Before sharing, open *Impostazioni avanzate* → *Accessibilità* → *Scrivi testo alternativo*, one entry per image. The path may vary slightly between app versions.

## 5. Final message

Write it in Italian and keep it short. Include:

1. **What's ready**, with links: `exports/` (PNG/MP4), `pubblicazione/`, and the contact sheet sent as an image.
2. **What still needs the user**, if anything (a missing fact, an asset to confirm). Lead with this.
3. **Design-system deviations**, if any, in one short list.
4. **Sources**, if research was done, as markdown links.

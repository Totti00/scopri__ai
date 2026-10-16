# carousel-copy.md — guida di scrittura dei caroselli (adottata il 16/10/2026)

La guida qui sotto resta **in inglese, com'è nell'originale** (mandata dal proprietario il 16/10/2026). Sostituisce `format/ganci-e-tipi.md`.

## Come la usiamo a Scopri AI (questa parte vale prima della guida)
- **I post si scrivono sempre in italiano.** Gli esempi della guida sono in inglese: si prende il meccanismo, poi si scrive in italiano, con le regole di "Come si scrive" di `CLAUDE.md` (si dà del tu, parole semplici, frasi corte).
- **Le regole di Scopri AI vengono prima** (come dice la guida stessa: "the brand file wins"): `CLAUDE.md` (2 fonti, foto e video veri, niente esagerazioni, "cosa ha fatto l'AI" più il commento di 2–3 parole), `brand/identita.md`, `brand/crescita.md`.
- **Decisioni del proprietario (16/10/2026):**
  - **il meglio all'inizio** (§5.3): la cosa più forte nella slide 2 o 3; in fondo vanno riepilogo e invito;
  - **contatore "3/7"** (§5.4) in alto a destra su tutte le slide tranne la copertina: `carosello.py` lo mette da solo (stili A e B), negli altri template lo aggiunge il `costruttore-post`;
  - **un solo invito per post** (§8), scelto per tipo, nella chiusura e uguale in caption (più una domanda per i commenti):

    | Post | Invito | Nel JSON della chiusura |
    |---|---|---|
    | Notizie (news lampo, settimana, curiosità) | 📩 Mandalo a chi … | `"invito": "manda"` o `"invito_testo": "📩 Mandalo a chi …"` |
    | Prompt, liste, guide, passo-passo | 📌 Salvalo per … | `"invito": "salva"` o `"invito_testo": "📌 Salvalo per …"` |
    | Serie, appuntamenti fissi | 🔔 Seguici | `"invito": "segui"` |
  - **slide "In breve"** (riepilogo, §5.1) da 6 slide in su, prima della chiusura: `{"tipo": "riepilogo", "titolo": "In breve", "punti": [...]}`;
  - **"Scorri →"** sulla copertina (§5.4): la pillola gialla dei template.
- **Cosa NON prendiamo:** "Comment [WORD] and I'll send it" (§8): è un'esca, Instagram la penalizza (`brand/crescita.md`).
- **Ganci:** il `selezionatore` ne scrive 5–10 per notizia (§3.4), li passa al test (§3.2) e nel menu mette i 3 migliori, di tipi diversi tra i 12 del §3.3. **Schemi:** ne propone 2 tra quelli del §6 (più il nostro "Scoperte": gancio → la scoperta più forte → le altre → riepilogo → chiusura).
- **Dati e numeri:** solo veri e con fonte (regola 1 di `CLAUDE.md` e §10 della guida).
- Controllo finale: `brand/controllo-finale.md` (unisce il §13 della guida con le nostre regole).

---

# Instagram Carousel Copywriting & Structure Guide

A brand-agnostic reference for writing Instagram carousels. It covers hooks, text density, slide-by-slide structure, narrative frameworks, CTAs and captions. Visual design (colours, fonts, layout) is defined per brand elsewhere and is out of scope here. Where this guide and a brand file conflict on tone or voice, the brand file wins; everything else in this guide still applies.

---

## 1. Core principles

These are the points that recur across nearly every credible source. Treat them as non-negotiable defaults.

1. **Slide 1 decides everything.** It is the only slide most people ever see. If it doesn't earn the swipe, the rest of the carousel does not exist. Spend more effort on slide 1 than on any other slide.
2. **Slide 1 is a hook, not a title.** "Tips for better sleep" is a title. "The 10-minute habit that fixed my sleep" is a hook.
3. **Slide 2 is the second hook.** Instagram often re-shows a carousel to people who scrolled past it, starting on slide 2. Slide 2 must therefore work as an entry point on its own — never a repeat of slide 1, never a throwaway.
4. **One idea per slide.** If a slide carries two points, split it.
5. **Short beats dense.** Each slide should be understood in about 2–3 seconds on a phone.
6. **Every slide earns the next swipe.** Deliver value *and* give a reason to keep going.
7. **Specificity beats cleverness.** Concrete numbers, outcomes, timeframes and named situations outperform vague or witty lines.
8. **Pay off the promise.** The hook is a contract. If the carousel doesn't deliver exactly what slide 1 promised, trust (and saves/shares) collapse.
9. **Design for saves and sends.** Saves and DM shares ("sends") are the actions that matter most. Every carousel should contain at least one slide worth saving and a reason to send it to someone.
10. **End with one clear CTA.** One ask, not three.

---

## 2. How much text per slide

Sources vary on exact numbers, but they converge on "far less than you think". Use these limits:

| Slide type | Headline | Body copy | Hard ceiling |
|---|---|---|---|
| **Slide 1 (hook)** | 5–10 words (ideal 6–8) | Optional: a short sub-line of ≤8 words | ~12 words total |
| **Slide 2 (re-hook / context)** | 4–8 words | ≤20 words | ~25 words |
| **Value slides** | 3–7 words (a mini-headline) | 10–30 words (1–2 short sentences) | ~40 words — above this, split the slide |
| **Summary / recap slide** | 3–6 words | Short bullet list, ≤5 items, ≤6 words each | ~40 words |
| **CTA slide** | 3–8 words | ≤15 words | ~20 words |

Rules of thumb:

- **The squint test:** if a slide needs zooming or re-reading, it has too much text. Cut, don't shrink.
- **Split, don't cram.** When a point needs more words, give it two slides.
- **Front-load every slide.** The most important word or idea comes first in the headline.
- **Mini-headlines must stand alone.** Someone reading only the headlines should still get the core message.
- **Short words, short sentences.** Plain, conversational language. Aim for roughly a 6th–8th grade reading level. Cut filler ("really", "very", "in order to", "it's important to note").
- **Line length:** keep lines short (roughly 35–50 characters) so text breaks naturally on a phone.
- **Words work better than paragraphs:** fragments, numbered points and punchy statements are fine. Full paragraphs are not.

---

## 3. Writing the hook (slide 1)

### 3.1 What a strong hook does

A good hook opens a gap between what the reader knows and what they want to know, and makes closing that gap feel worth one swipe. It should do three things at once:

1. **Signal relevance** — the right reader instantly recognises "this is for me".
2. **Create tension** — curiosity, a problem, a surprise, a contradiction or a desirable outcome.
3. **Promise resolution** — make it clear the answer is inside the carousel.

### 3.2 The hook test

Before finalising slide 1, check:

- [ ] Can a stranger tell what the carousel is about in under 2 seconds?
- [ ] Is it 12 words or fewer?
- [ ] Does it contain something specific (a number, timeframe, result, audience or named situation)?
- [ ] Does it withhold the answer, so the reader must swipe to get it?
- [ ] Would it still make sense as a standalone image (e.g. screenshotted and shared)?
- [ ] Does the carousel fully deliver on it?
- [ ] Is it free of the brand name or logo as the main message?

### 3.3 Hook types (with fill-in templates)

Rotate between types. Using the same pattern every post causes fatigue.

**1. Curiosity gap / withheld answer**
- "The one [thing] most [audience] get wrong about [topic]"
- "Nobody tells you this about [topic]"
- "Why [surprising outcome] happens (it's not what you think)"

**2. Specific result / proof**
- "How I [specific result] in [timeframe]"
- "The [framework/method] that [measurable outcome]"
- "[Number] → [number]: what changed"

**3. Numbered list / listicle**
- "[Number] [things] that [outcome]"
- "[Number] [topic] mistakes (#[n] is the worst)"
- "[Number] signs you [situation]"
  Odd or precise numbers (7, 9, 13) often read as more credible than round ones.

**4. Mistake / warning (negative framing)**
- "Stop [common habit]. Do this instead."
- "You're [doing X] wrong"
- "The [topic] mistake costing you [specific loss]"

**5. Contrarian / myth-busting**
- "[Popular advice] is wrong. Here's why."
- "Unpopular opinion: [claim]"
- "Everyone says [X]. I disagree."

**6. Direct question / pain point**
- "Still [frustrating situation]?"
- "Why does [pain] keep happening?"
- "Are you making this [topic] mistake?"

**7. Audience call-out**
- "If you [identity/situation], read this"
- "[Audience]: save this before [event/moment]"

**8. How-to / promise**
- "How to [desired outcome] without [common pain]"
- "The simplest way to [outcome]"
- "[Outcome] in [number] steps"

**9. Story opener**
- "[Timeframe] ago, I [relatable low point]…"
- "I tried [thing] for [time]. Here's what happened."

**10. Data / statistic**
- "[Surprising %] of [group] [do/experience X]"
- "The [metric] gap between [group A] and [group B]"

**11. Comparison / analogy**
- "[Your topic] should work like [familiar thing], not [other thing]"
- "[Option A] vs [Option B]: which actually works?"

**12. Before / after**
- "What [thing] looked like before vs after [change]"
- "From [before state] to [after state] in [number] slides"

### 3.4 Hook writing techniques

- **Write 5–10 hook options, then pick one.** The first hook is rarely the best.
- **Know the payoff before writing the hook.** Draft the value slides first (or at least outline them), then write the hook that sells them.
- **Balance specificity and mystery.** Be specific about the *result* and vague about the *cause* ("The 3-word change that doubled replies" — the result is concrete, the change is withheld).
- **Use strong, concrete words.** Words like *mistake, simple, exact, proven, nobody, stop, instead, finally* create tension. Use them honestly.
- **Speak to one person.** "You" beats "people". A narrow audience call-out beats a broad one.
- **Match emotion to hook type.** Fear of loss → mistake/warning hook. Desire → promise/result hook. Curiosity → withheld-answer hook. Frustration → question/pain hook.

### 3.5 Hook mistakes

- A vague title instead of a hook ("Social media tips", "Our new service").
- Giving away the answer on slide 1 (the loop closes, no reason to swipe).
- Too many words, or two competing ideas.
- Leading with the brand name, logo or a greeting.
- Clickbait the carousel doesn't deliver on.
- Jargon the target reader wouldn't use.
- Repeating slide 1's message on slide 2.

---

## 4. Slide 2: the re-hook

Slide 2 has two jobs:

1. **For people who swiped:** confirm the promise and set up the payoff — why this matters, what they'll get, or the stakes.
2. **For people served slide 2 first (re-serve):** stand alone as a second hook that makes sense without slide 1.

Good slide 2 patterns:
- **The stakes:** "Most people lose [X] because of this."
- **The promise map:** "By the end, you'll know [A], [B] and [C]."
- **The problem made concrete:** a specific, relatable scenario.
- **The first (and best) point**, delivered immediately.

Avoid: repeating the hook, a slow intro ("Let me explain…"), or a slide that only works if you saw slide 1.

---

## 5. Carousel structure

### 5.1 Default skeleton

| Position | Role | Job |
|---|---|---|
| Slide 1 | **Hook** | Stop the scroll and earn the swipe |
| Slide 2 | **Re-hook / context** | Set stakes or the promise; work as a standalone entry point |
| Slides 3 to n-2 | **Value** | One point per slide, delivering on the hook |
| Slide n-1 | **Summary / payoff** | Recap, key takeaway or checklist — the most save-worthy slide |
| Slide n | **CTA** | One clear action |

### 5.2 Slide count

- **Default: 7–10 slides.** Most sources place the sweet spot in the 6–10 range.
- **Short (4–6):** quick tips, single before/after reveals, simple announcements.
- **Medium (7–10):** listicles, frameworks, step-by-steps, myth vs fact.
- **Long (10+):** only for deep guides where every slide carries real value.
- The content decides the count. Never pad to hit a number; a weak middle slide causes drop-off. If a slide can be removed without loss, remove it.

### 5.3 Front-load value

Put the strongest point early (slide 2 or 3), not last. People who drop off mid-carousel should still have received something good. Save the summary and CTA for the end, not the best idea.

### 5.4 Keeping people swiping

- **Open loops:** tease something coming later ("The last one surprised me", "#5 is the one that matters most").
- **Numbering:** "3/7" style progress or numbered points tells readers how far they are and that the end is near.
- **Bridging lines:** end a slide with a short line that pulls forward ("But here's the catch →", "Here's how to fix it →").
- **Build, don't list randomly:** each slide should logically lead to the next, like a mini-story.
- **Mid-carousel momentum:** in longer carousels, a short nudge around the middle ("Halfway — the best one's next") helps.
- **Swipe cues in copy:** a short "Swipe →" or arrow on slide 1 (and optionally slide 2) increases swipe-through. Keep it small and secondary to the hook.

---

## 6. Narrative frameworks

Pick one framework per carousel. Each maps onto the skeleton above.

**Listicle (tips / tools / ideas)** — the most versatile and most saved format.
Hook with a number → one item per slide → recap → CTA.

**Step-by-step / tutorial**
Hook promising the outcome → one step per slide, in order, each starting with a verb → final result → CTA.

**Problem → Agitate → Solve (PAS)**
Name a specific problem → show what it costs (1–2 slides) → present the solution/method (several slides) → CTA.

**Before → After → Bridge (BAB)**
The current painful reality → the desired outcome, described vividly → how to get there. Show the "after" before the "bridge": people need to want the destination before they care about directions.

**Mistakes to avoid**
Hook on the cost of the mistakes → one mistake per slide, each paired with the fix → recap → CTA.

**Myth vs fact**
Hook challenging a belief → myth, then fact (paired, 3–5 pairs max) → takeaway → CTA.

**Contrarian take**
Popular belief → why it's wrong → the alternative approach (several slides) → the result → CTA.

**Story / case study**
Relatable low point or starting situation → what went wrong or what was tried → turning point → lessons (one per slide) → where things are now → CTA (often a question).

**Data-driven**
Striking statistic → what it means → why it happens → what to do about it → CTA.

**Comparison (A vs B)**
Hook posing the choice → criteria one per slide, both options compared → verdict → CTA.

**Checklist / cheat sheet**
Hook promising a reference resource → grouped items → a final "everything on one slide" recap designed to be saved → CTA to save.

---

## 7. Value slide copywriting

- **One point, one slide.** Mini-headline + 1–2 short supporting sentences.
- **Headlines lead with the action or insight.** Start with a verb where possible (Cut, Add, Stop, Use, Check).
- **Show, don't just tell.** An example, number or quick scenario beats an abstract claim.
- **Make each point actionable.** The reader should know what to do, not just what to think.
- **Keep parallel structure** in lists — same grammatical shape for each item.
- **Consistency of voice** across all slides; no sudden shifts in tone or formality.
- **Cut hedging.** "This might help you possibly improve" → "This improves".
- **Make one slide worth screenshotting** — a framework, formula, checklist or summary people want to keep.

---

## 8. The CTA slide

- **One CTA only.** Choose based on the carousel's goal:
  - **Save** — for reference content (guides, checklists, frameworks). Many people don't save by habit; they need the prompt ("Save this for your next [situation]").
  - **Send / share** — for relatable or useful-to-others content ("Send this to someone who [situation]"). Shares are the strongest reach signal for getting in front of non-followers.
  - **Comment** — for opinion, story or question-led content. Ask a specific, easy question ("Which one will you try first?"), not "Thoughts?"
  - **Follow** — when the carousel is part of a series or a clear ongoing topic ("Follow for part 2").
  - **Click / DM / keyword** — for conversion goals (link in bio, "Comment [WORD] and I'll send it").
- **Make the CTA specific and low-effort.** Tell people exactly what to do and why.
- **Tie it back to the value.** "Save this so you don't forget step 3" beats a generic "Save for later".
- **Never make the CTA slide a dead end** — a one-line reminder of the payoff plus the ask works well.
- The CTA can also be reinforced (not replaced) in the caption.

---

## 9. The caption

The caption supports the carousel; it doesn't repeat it.

- **First ~125 characters are the hook.** That's roughly all that shows before "more". Put the key message, a hook or a question there. Don't open with filler, greetings or hashtags.
- **Complement, don't duplicate.** Add context, a short story, a personal angle or the "why" behind the slides.
- **Length:** carousels suit medium-to-long captions (roughly 300–1,500 characters), provided the first line hooks. Short captions are fine for simple posts.
- **Readability:** short paragraphs, line breaks, no walls of text.
- **Keywords for search:** Instagram search now leans on the words in captions (and on-image text). Naturally include the terms the target reader would actually search for. Write them as normal language, not keyword stuffing.
- **Hashtags:** a small number (around 3–5) of specific, relevant hashtags at the end. Hashtags help categorise; they are not the main reach driver.
- **Repeat the CTA** at the end of the caption.

---

## 10. Tone and language

- Conversational, direct, human. Write like you're explaining something to one smart friend.
- Use "you" and active voice.
- Prefer concrete nouns and verbs over adjectives.
- Remove corporate language and buzzwords unless the brand voice explicitly calls for it.
- Keep claims honest and verifiable. Don't invent statistics, results or testimonials. If a specific number isn't available from the brief, use a specific *situation* instead of a fake number.
- Be confident, not arrogant — especially in contrarian and myth-busting carousels.

---

## 11. Common mistakes (whole carousel)

- Weak or vague first slide.
- Wall-of-text slides.
- Two or more ideas on one slide.
- Slide 2 that duplicates slide 1 or only works in sequence.
- Best content buried at the end.
- Padding slides to reach a target count.
- No logical flow between slides — random facts instead of a sequence.
- Hook that overpromises relative to the content.
- Brand-first messaging instead of reader-first value.
- Multiple competing CTAs, or no CTA at all.
- Caption that just repeats the slides.

---

## 12. Writing workflow

1. **Define the carousel in one sentence:** who it's for, what they'll get, and the one action they should take.
2. **Choose a framework** (section 6) that fits the content.
3. **Draft the full copy as text first**, slide by slide, before thinking about layout. The length should come from the idea, not a template.
4. **Outline value slides** — one point each, strongest early.
5. **Write the summary and CTA slides.**
6. **Write 5–10 hook options**, run each through the hook test (3.2), pick the best.
7. **Write slide 2** so it works both as a follow-on and as a standalone entry point.
8. **Edit for density:** check every slide against the limits in section 2. Cut or split.
9. **Check flow:** read only the headlines in order — the story should still make sense.
10. **Write the caption:** hook in the first ~125 characters, supporting context, keywords, CTA, a few hashtags.
11. **Run the final checklist.**

---

## 13. Final quality checklist

**Hook**
- [ ] Slide 1 is a hook, not a title, and ≤12 words
- [ ] It's specific and withholds the answer
- [ ] Slide 2 works as a standalone second hook

**Body**
- [ ] One idea per slide
- [ ] Every slide within the word limits; nothing needs zooming
- [ ] Headlines alone tell the story
- [ ] Strongest point appears early
- [ ] Each slide gives a reason to swipe to the next
- [ ] At least one slide is clearly save-worthy
- [ ] The hook's promise is fully delivered

**Ending**
- [ ] Summary/payoff slide present (for 6+ slide carousels)
- [ ] Exactly one clear, specific CTA

**Caption**
- [ ] Strong first ~125 characters
- [ ] Adds context rather than repeating slides
- [ ] Natural keywords, a few relevant hashtags, CTA repeated

**Language**
- [ ] Plain, conversational, active voice
- [ ] No filler, hedging or jargon the reader wouldn't use
- [ ] No invented facts, numbers or testimonials
- [ ] Consistent with the brand's voice

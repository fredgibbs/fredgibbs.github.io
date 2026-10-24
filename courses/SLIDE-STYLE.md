# Slide Deck Rules

How to write and build a lecture deck. The CSS class mechanics are documented
in the header comment of `/assets/css/reveal-lecture-theme.css`, which is
canonical; this file covers what to write and how to source it.

A deck lives at `courses/<course>/slides/<deck-slug>/`: `index.md`, an
`images/` folder with a `README.md`, and an `ISSUES.md` when it has open
problems. Both notes files are excluded from the build, so write them for
whoever picks the deck up next. Worked examples are in
`courses/making-history/slides/`. Older decks that break a rule below are fine
until someone next works on them; the `critical-thinking-with-ai` decks predate
these rules entirely.

## Content rules

### Voice

**Match the syllabus register.** `schedule.md` is the model: flat,
declarative, specific, unexcited. "A direct challenge to the Week 4
professionalization story." A slide should read like that, not like an
explainer walking someone through a revelation.

**Be direct; avoid metaphor.** Say what happened and what it means. The one
metaphor that earns a place is the subject's own (Carr's fish on the
fishmonger's slab), quoted as theirs. Reuse the course's established metaphors
in the same words each time. Coin a new one only if it is the source's own
image, the slide stops to explain it, or there is no plain equivalent.

**Cut on sight:** "Hold onto this," "Notice that…," "Worth keeping in view,"
"This is the actual innovation," "the useful question isn't X, it's Y," and
any staging by clock or slide count. A label names what its block contains
("The word 'only'"), not how to feel about it.

**Don't comment on the course or the deck.** No "now that you have read
them," no "as you saw last week," no "three slides earlier." Call the session
**today**, never "the hour." A specific course connection is fine: "the two
writers you read," a `.source-list`, a `.cite`.

**One epigram per part.** A chiselled antithesis only lands against plain
sentences. The take home usually earns it; elsewhere, state the finding and
stop. The giveaway is the numeric pairing ("One file, two historians"). If four
parallel labels or `.flow` steps match perfectly, break one.

**Don't follow a claim with its own negation.** "Peer review polices accuracy.
It does not police the question." The test is what the second sentence is
about: if it is about the first sentence, fold it in ("polices accuracy, and
stops there") or cut it. A second sentence with a new subject, reason or
consequence stays.

**Hedge at about the syllabus rate.** "Usually," "almost," "a fairly specific
complaint." Uniform confidence reads as a brochure and tells the room there is
nothing left to argue about.

**Let people act, not abstractions.** "What each one wants from the page
settles it," not "the purpose settles the question."

**Spell in American English** in the deck's own voice. Quotations, names and
titles keep their own spelling.

### Headlines and eyebrows

**Name people; don't reduce them to one deed.** "The man who built the
university" is too large for the deed and too small for the person. Write the
name, the standing that put them in a position to write this, and a claim: "A
comparative linguist, not a historian, defines the historian's task." Test: if
it would sit comfortably as a magazine subhead, rewrite it. A deflating role
("a schoolmaster of twenty-eight") is fine.

**Cut the explanatory tail.** Read the headline without the clause after the
comma. If the claim survives, cut the tail. Keep a second element only when it
carries a turn: a contrast, a reversal, or the pair the slide is built on.

**Headlines run the full width.** No `max-width`, no manual `<br>`.

**Eyebrows are labels:** what and when, a few words with `·` between the
parts. `Voltaire · 1694–1778`, `Part one · discussion`. If it needs a verb, it
belongs in the headline. A cold open's eyebrow names the pictures on screen.

**A card gets a `.num` label only when it says what its green heading can't.**
`Stories · p. 13` over "Heroes to share" is clutter: cut the label and put the
page at the end of the card text, `(p. 13)`. If the card needs its category to
make sense, write the category into the heading ("The state is rarely
criticized," not `The state` over "Seldom criticized"). Labels that carry
something the heading doesn't stay: the arc's part and source
(`01 · Loewen, pp. 13–24`), a throughline's week, steps whose order is the
point.

### Names and cross-references

**A name that never comes back is a citation, not a lesson.** Search the deck
for each proper noun on a slide. One occurrence means the name is licensing a
claim the headline already made: write the claim and drop the roster. Delete;
don't demote to small type.

**A cross-reference says what to look for.** Not "Compare Week 4 (Ranke,
Treitschke)" but one clause of about fifteen words stating a fact about the
other week, in that deck's own words where it has them. Test: could a student
who missed that week say what to look for? A standalone pointer is a
`.reveal-block.compare`, not a fragment:

```
<div class="reveal-block compare compact" markdown="1">

###### Compare · Week 4
{: .label}

Treitschke, trained under Ranke, made Bismarck's unification of Germany look inevitable.
</div>
```

### People, texts and context

**Introduce people on their portrait slide, then go straight to the detail.**
Two slides, not three: an image slide whose caption carries the introduction,
then their words. The caption rail holds the name and dates, a brief bio, a
`<span class="why"><strong>Why he matters:</strong> …</span>` line, and the
credit. Wrap the whole sentence in the span and never fake the gap with
`<br><br>`. The why line says what the person *did* that the rest of the deck
depends on, not what happened to them; check it against the takehomes. Keep the
caption under about 500 characters, since the rail clips past about 640. Model:
the portraits in `enlightenment-progress-2`. Where a person matters for one
idea only, an explainer slide (see "Image slides") can introduce them and the
idea together.

**Introduce before you quote.** Nobody's words go on a slide, and nobody's name
goes in a headline as the one acting, before the slide that introduces them.
Two exceptions: the narrator (the `Background:` author), and a voice quoted
through the narrator ("Kramer, quoted in Maza"), so long as the slide does not
make them its subject.

**No portraits of textbook authors.** The `Background:` author narrates the
session and the title slide introduces them. Authors of primary readings get
portraits.

**Introduce texts as things first:** when, where, how long, what kind of
document. A source's own history is often worth a slide.

**Context before lessons.** The period, what the writer was reacting to, what
readers already believed; then the quote; then what it tells us.

**Use images at every opportunity.** Every named person gets a portrait if one
exists, every named place an image. Run no more than two or three content
slides without an image break, and look for images that do argumentative work.

### Length

**Keep the blocks short. The `.takehome` is a line.** Count words;
`scripts/slide-words.py` checks these budgets.

| Container | Target | Hard stop | It is |
|---|---|---|---|
| `.takehome` | **30 words** | 40 | one or two sentences |
| `.reveal-block` | **55 words** | 70 | three sentences |
| `.image-notes` bullet | **40 words** | 50 | lead, elaboration, question |
| caption describing a picture | **40 words** | 55 | two lines and a credit |
| caption introducing a person | **80 words** | 90 | bio, `why`, credit (~500 chars) |
| `.detail` | **30 words** | 40 | one sentence under a headline |
| `.main-point` headline | **14 words** | 18 | a claim, no explanatory tail |

A caption that carries a `why` line is an introduction and gets the larger
budget. Read a block aloud: a second breath means two blocks. A takehome that
joins two independent claims with "and" has stopped being a line. Use bullets
for genuinely parallel items, within the same budget. Cut first: the
attributive clause the cite already covers, the second quotation, the
qualification the next slide makes, and any sentence restating the label.

**Every slide fits the 960×700 box,** about 880×640 usable. Overflow is
clipped, not scrolled. Plan on one quote plus two or three blocks. When a slide
runs long: add `.compact`, cut words, use a `.swap`, or split it.

### Quotations and citations

**Precision over invention: never fabricate a quote.** Every quotation comes
from a source open in front of you, with a real page or section. Without the
text, paraphrase and cite the chapter. Record that compromise in `ISSUES.md`
and tell the author, never on the slide.

**Every `.cite` names the work.** A bare page number fails. State the edition
once, in the title slide's `.citation-note`. When the PDF is an excerpt from a
larger volume, say which piece each page belongs to. For a quote of a quote,
cite both ends.

**Keep the framing clause when you quote a quote, and attribute
superlatives.** The secondary author's framing is usually why the quote is
there. Write "Popkin dates the first American history PhD to Johns Hopkins,
1876," not the claim in the deck's voice.

**Check the original language when the wording carries the argument.** Two
writers can converge in English and diverge in the original: Humboldt's
*Darstellung des Geschehenen* is not Ranke's *wie es eigentlich gewesen*. Name
the translator when the choice does work.

**Read past the passage you want.** Search the rest of the text for passages
that cut against it, and put the tension on the slide.

**Two writers on one slide get equal billing.** A `.quote` over a
`.reveal-block` is a hierarchy, right only for one source elaborating itself.
Different writers being compared go in a `.parallel`, one `.track` each, with
the writer and work in the `#####` heading and no `.now` or `.ai` modifier.

### Slide levels and classes

**Slide levels: one voice per level.** Color says whose words they are; font
says what kind of line it is.

| Level | Whose words | Classes | Set in |
|---|---|---|---|
| Label | the deck's signposts | `.eyebrow`, `.label`, `.num` | mono capitals, gold |
| Claim | the deck's argument | `.main-point`, card and step headings; `.takehome` | Fraunces semibold: green for the titles, the text color for the `.takehome` |
| Source | the past's, or a historian's | `.quote`; `.pull-quote` for a supporting one | Fraunces italic behind a rule: gold, or teal for the supporting one |
| Question | the room's | `.question`, `ul.questions`, `.ask`, `.provocation` | Inter semibold, upright, white |
| Commentary | the deck explaining | `.reveal-block` text, `.detail`, card text, throughline answers | Inter, muted |
| Apparatus | the record | `.cite`, `p.cite`, `.citation-note` | mono, small, muted |

Captions are their own case: Fraunces italic, muted, beside or under a picture.
A question must never look like a quotation. Green is for titles only.
Emphasis stays inside its level: a line that needs to look different needs a
different class, not an inline style. A new class gets a level first.

**Every piece of text carries a class, and the class is its job.**

| The line's job | Class |
|---|---|
| What the slide is about, and when | `.eyebrow` |
| The claim | `.main-point` |
| The evidence, quoted | `.quote`, with its `.cite` |
| A second quotation supporting the first | `.pull-quote`, with a `<span class="cite">` |
| Unpacking or arguing from the evidence | `.reveal-block.unpack` or `.argument`, with a `.label` |
| Historical context | `.reveal-block.historical`, with a `.label` |
| A pointer to another week | `.reveal-block.compare` |
| A source note with no quotation to hang on | `p.cite` |
| The takeaway | `.takehome` |
| The discussion question | `.question` |
| The readings, and how they are cited | `ul.source-list`, `.citation-note` |
| One sentence of the deck's own argument under a headline | `.detail` |

Text inside a styled container (`.card`, `.answer`, `.track`, `figcaption`)
needs nothing more. `.detail` is not a fallback for text with no obvious home.
The check: every paragraph has a `{: .class}` line or sits in a styling
container, and no `.detail` contains a quotation.

## Structure of a session deck

1. **Cold open** (optional): a full-bleed `section.image-slide.bleed` per
   image with a one-line `.credit` (prefer `data-background-size="contain"`),
   then the session's question, then an `.image-notes` slide. For a contrast,
   unpack both images on one notes slide in a `.shots` wrapper, with bullets
   written across the pair. Models: `enlightenment-progress`,
   `annales-longue-duree`.
2. **Title:** the course and week eyebrow, the deck's title, a rule, a
   `ul.source-list` with the `Background:` reading first and the primary
   sources under it, and a `.citation-note` for editions and citation
   conventions.
3. **Today in context:** a `.throughline` with the course's running question
   ("What makes history happen?") and `.answer.past`, `.now` and `.next`
   nodes. Write the question once and change only the nodes.
4. **Parts, per source or person.** Open with the work, not the face; then the
   portrait; then one to four quote slides, with image slides for the objects
   and places they mention. Each part opens with a `.detail` line saying what
   the last part left unfinished.
5. **A discussion slide** at the end of each part.
6. **Comparison,** if the session pairs two writers: a `.parallel` asking what
   actually separates them.
7. **The arc:** a `.cards` grid, one card per part, drawn from the discussion
   takehomes.
8. **The take home:** one headline and at most three `.reveal-block`
   fragments, the last a `.takehome` carrying the cost or the catch. No
   outline.
9. **Closing:** what comes next, and a closing question only if it needs the
   whole session behind it.

The arc and the take home go at the end. Before the evidence, they are claims
about a book nobody has met.

A deck covering two sessions adds a `Part one · 3.1` / `Part three · 3.2`
transition and an arc spanning both.

**A review deck** drops the throughline, the title slide's `.detail` and the
`.citation-note`. It opens each stretch with that week's key image,
full-bleed, rather than a portrait, and keeps a discussion slide per stretch,
the arc, the take home and what comes next. Ask new questions that test old
claims against later weeks; never re-ask a week's question. On a review slide
(`.quote`, one block, `.takehome`) the question is the last fragment.

**Skip orientation furniture.** A transition needs a sentence, not a diagram.
Don't draw an axis you are not going to scale: evenly spaced dates promise a
proportion they don't deliver, so use a `.parallel` or `.cards` instead.

## Discussion slides

One per part, after the quote slides that give students evidence to use. One
slide, three beats:

```
Part one · discussion
{: .eyebrow}

## Counting the poor
{: .main-point}

---

A parish register gives you every burial in a village for two centuries.
What can you now ask, and what can you still not ask?
{: .question .fragment data-fragment-index="1"}

<div class="takehome fragment compact" data-fragment-index="2" markdown="1">
Counting proves the poor were there; it cannot say what they wanted, because
nobody recording them was asking.
</div>
```

- The `.main-point` is the topic in four or five words, not the question and
  not the answer.
- The `.question` is one real question about a particular choice in the text.
  Test: a student who did the reading can answer it and one who didn't can't.
- The `.takehome` is only the crux, the payoff to what students said. Name a
  good alternative where the reading supports one.
- To keep the object on screen, wrap the body in `.with-figure` with a small
  image before the question (`history-from-below`, part two).

## Image slides

**The image is the slide; make it as large as the slide allows.**
`figure.landscape` puts the caption underneath and `figure.portrait` beside,
matching the image's real aspect ratio. In a caption, `<em>` is the block-level
note and credit and `<i>` is for titles.

**Write the caption for yourself:** what the picture is, plus one point, in
words you can elaborate aloud. Two lines and a credit, and the credit always
stays. Translate a foreign-language title the first time it is shown,
preferring the literal rendering.

**One image per slide,** with three exceptions:

- A `figure.pair`, only after each image has had its own slide, for one small
  comparative point.
- A review deck's `.recall` grid: two to four images the room has already
  seen, no captions, one `p.cite`. It currently has no user; cut it if nothing
  adopts it.
- A discussion deck built on forced pairs (`section.image-slide.provoke`),
  with no takeaway under the pictures and images the room has not seen. Model:
  `purpose-and-progress`. Keep a text deck for the same session as the record.
  Type curly quotes and apostrophes (“ ” ’) in its `p.provocation`: it is raw
  HTML, which kramdown does not touch, so a straight `"` shows on the slide.

**Image notes: `.image-notes`, a small image left and bullets right,** one
image per slide. Each bullet runs look, meaning, question: a bold lead naming
something visible, a sentence on what it commits its makers to, and an
`<em class="ask">` question aimed at the session's problem rather than at the
picture. Budget about 23 lines of about 52 characters.

**Explainer: `.with-figure.wide`, an image left and the explanation right.**
Eyebrow and headline, then the picture beside a `.quote.compact` and one or two
`.detail` lines. Wrap the image in a `<figure>` whose `<figcaption>` holds
the credit, so it sits under the picture at caption size. Use it to set
one claim beside the image that carries it: a week recalled in a review deck
(`big-picture-review`, which predates the figure caption), or a figure and their idea on one slide (the genealogy
in `linguistic-turn`). With a two-line headline it measures about 650px, just
over the checker's 644px line, so confirm by screenshot that nothing clips and
keep the text column no taller than the image.

## Front matter

```yaml
---
layout: reveal-lecture
title: "Deck Title — the authors/texts it covers"
image_slides: true
---
```

Drop `image_slides: true` only if the deck has no image slides. The older
standalone `.html` decks are not the model.

## Sourcing images

**Free licenses first:** public domain, CC0, CC BY, BY-SA or BY-NC, checked on
the file page. Commons is the first place to look, not the only one. BY and
BY-SA need attribution in the caption; BY-NC also needs a non-commercial note.
Never strip a credit.

**Fair use is a fallback with a named reason.** Use it only after looking,
prefer an institutional source to a stock agency, and keep the copy small.
Record the search and the reasoning in `images/README.md` and the decision in
`ISSUES.md`. Model: the Braudel portrait in `annales-longue-duree`.

**Fetch at the command line:**

```sh
curl -L -H 'User-Agent: your-name (your-email)' \
  'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2000' -o raw
sips -Z 1800 raw --out out.jpg -s format jpeg -s formatOptions 88
```

**Pick images that read at projector distance:** large figures, clear
gestures, real contrast.

**Check resolution against the display size.** Aim for 1.5 image pixels per
slide pixel: about 780px tall for a portrait rail, 1,000px wide for a
landscape. `deck-check.sh` measures it. When nothing larger exists, choose the
sharpest copy and record the shortfall in `ISSUES.md`. Cap the long edge at
1800px and crop from the original. Use q78 by default and q82–88 for fine
detail, and keep `images/` under about 10MB.

**Every `images/` folder has a `README.md`:** a credits table (file, what it
is, source, license) and notes on crops, annotations, non-obvious choices and
the re-fetch command. If you annotate an image, say so in the caption.

## Cache the text of a scanned reading

A born-digital PDF gives up its text to `pdftotext -layout`. A scan has no
text layer, so OCR it once and save the result:

```sh
swiftc -O -o /tmp/ocr-pdf scripts/ocr-pdf.swift     # once
/tmp/ocr-pdf ~/Dropbox/courses/<course>/optimized/<reading>.pdf 2 > raw.txt
```

- **Keep it beside the reading, never in this repo:**
  `~/Dropbox/courses/<course>/.research-packets/<reading>.ocr.txt`. These are
  in-copyright materials.
- **Mark printed pages** as `[[ printed page NN ]]`. Scans are often two-page
  spreads, so a right-hand column belongs to the next page.
- **Say what the file is not.** Head it with what produced it, when, and which
  pages. Use it to find a passage, then verify the words against the page
  image before quoting.

Model: `~/Dropbox/courses/making-history/.research-packets/popkin-ch-4.ocr.txt`.

## Before publishing

1. **Build:** `LC_ALL=en_US.UTF-8 bundle exec jekyll build`.
2. **Words:** `scripts/slide-words.py <deck>/index.md`.
3. **Typography:** `scripts/deck-check.sh <course>/<deck>`. It fails a deck
   for overflow past 644px, unstyled text, commentary above the `.quote`, a
   block that opens with a quotation, someone quoted before their
   introduction, and images under 1.0×, and warns under 1.5×.
4. **By eye, every slide and every fragment.** Does each slide match a slide
   type: title, throughline, framing, quote slide, cards, image, image notes,
   explainer, discussion, arc, take home? A slide that fits none is made to
   fit, or its type is added here with the reason. Does each line sit at its
   level? Do two writers share a slide in a hierarchy? Is anything clipped?
   Fix it on the slide, not in the theme.
5. **A fresh-context review, required.** An agent with no memory of the
   drafting reads `index.md` against the cached source texts and reports
   problems with evidence, without fixing anything. Cheap checks first:
   - **Cross-slide integrity:** the opening question, the arc and the take
     home describe the same lecture; names, dates and citations agree; forward
     references are accurate; framing lines agree with the biographical slides.
   - **The historical arc:** dates, sequence, who could have read whom, causal
     claims, firsts and breaks.
   - **Every quotation,** word for word against the cited page, looked up
     rather than recognized.

   Verify each finding yourself, fix what is real, and record what you keep in
   `ISSUES.md` with the reason.
6. **Link the deck** from the course's `schedule.md` under its session, as
   `[Slides of ...](slides/<slug>/)`.

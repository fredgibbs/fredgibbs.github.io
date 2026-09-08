# Slide Deck Rules

How to write and build a lecture deck for any course on this site. Read this
before starting a new one. The mechanics of the CSS classes (`.eyebrow`,
`.reveal-block`, `.swap`, `.parallel`, etc.) are documented in the header
comment of `/assets/css/reveal-lecture-theme.css` — that comment is canonical;
don't duplicate it here. This file is about what to write and how to source it.

A deck lives at `courses/<course>/slides/<deck-slug>/`, with `index.md` beside
an `images/` folder. Worked examples named below are in
`courses/making-history/slides/` unless another course is given; the older
`courses/critical-thinking-with-ai/slides/` decks predate these rules and
aren't models to copy.

## Content rules

**Be direct. Avoid metaphor.** Say what happened and what it means. Don't
reach for a figurative frame ("a tapestry of...", "unpacking the...", "at the
heart of...") when a plain sentence says it faster. Figurative language costs
clarity: a student has a few seconds with a slide and shouldn't spend them
decoding an image to find the claim. The one metaphor that earns its place is
the *subject's own* — Kant's "crooked timber," Carr's fish on the fishmonger's
slab — quoted as theirs, never invented as decoration.

**Keep eyebrows as simple as possible.** The `.eyebrow` is a label, not a
sentence: what this slide is about, and when. `Voltaire · 1694–1778`. `The
Enlightenment · roughly the 1680s to the 1790s`. `Discussion · 4.1`. A few
words, or a name and a date, with `·` between the parts. Don't editorialize
there and don't let it pre-empt the argument the headline is about to make —
"The take home · the same sentence, now with evidence behind it" is a sentence
wearing a label's clothes. If the eyebrow needs a verb, it belongs in the
headline.

**Don't comment on the course itself.** Asides like "now that you have
actually read them," "as you saw last week," or "the same sentence, now with
evidence behind it" are well meant — they credit the work students did — but
they are clutter. They spend a line on the mechanics of the class instead of
the history, and they date the slide to one delivery of it. Say what the choice
or the claim is; don't tell the room it is now qualified to consider it.

A specific course connection is not clutter and stays: "the two writers you
read," "Bridge between weeks 3 and 4," a `.source-list`, a `.cite`. Those point
at something — this text, that session, this week's place in the sequence — and
that pointing is the work. What goes is the flourish that points at nothing.
Second person is likewise fine when it's doing analytic work ("the useful
question isn't 'is it true?'"), not when it narrates the seminar.

**Introduce people before their ideas.** Before quoting someone, give them a
bio slide: who they were, when and where they lived, what put them in a
position to write this. A quote from someone the audience hasn't met yet is
just words on a screen. See the `carr-historian-and-facts` vs.
`divine-power-and-statecraft` decks — the later one always does "Bede 00: who
he is" before "Bede 01" quotes him.

**Introduce texts as things before getting into their details.** Before
unpacking a passage, say what the text *is*: when it was written, published
where, how long, what kind of document. A primary source is an artifact with
a history of its own — where it sat for decades, who printed it, what
occasioned it — and that history is often worth a slide by itself (see the
Valla/Donation-of-Constantine sequence, or Bede's source list).

**Historical context before lessons from the reading.** Establish the
situation before drawing anything out of a text: the period, what was going on,
what the writer was reacting to, what their readers already believed. Then the
quote, then what it tells us. A takeaway offered before that context is just an
assertion students have to take on faith. This is the same principle as
introducing people and texts before their ideas, one level up — the Renaissance
bridge slide and "the Enlightenment as a phenomenon" in `enlightenment-progress`
exist so the Voltaire quotes have somewhere to land.

**Use images at every opportunity, for people and for place.** Every named
person gets a portrait if one exists. Every named place gets an image. Don't
run more than two or three content slides without an image break — see
`reveal-image-slide.css` and the `image_slides: true` front-matter flag.
An image can also do argumentative work (two faces of one stone, an empty
year on a real manuscript page) — look for that opportunity, don't just
decorate.

**Every slide must fit the viewport without scrolling.** Reveal is initialized
at a fixed 960×700 with an 8% margin (see `_layouts/reveal-lecture.html`), so
the real budget is roughly 880×640 CSS pixels regardless of the projector.
Content past that is clipped, not scrolled, and nothing in the source file
warns you. Plan on about one quote plus two or three `.reveal-block`s per
slide. When one runs long, in this order: add `.compact` to the blocks, cut
words, wrap the fragments in a `.swap` so they replace one another in place
rather than stacking (see the Renaissance bridge slide), or split the slide in
two.

**Precision over invention — never fabricate a quote.** Every quotation in a
deck must come from a source you actually have open in front of you (a PDF,
a Wikisource page, an archive.org scan), with a real page or section number.
If you don't have the primary text in hand, don't put words in quotation
marks and attribute them to the author — paraphrase in your own voice instead,
citing the chapter generally, and say so if you're doing it (e.g. no exact
page cite because the PDF wasn't available). This applies as much to secondary
readings (Popkin, Maza, Green & Troup) as to primary sources. A wrong
citation in a teaching deck is worse than a thin one.

## Structure of a session deck

A deck may open before everything else with a **cold open**: for each image,
a full-bleed slide whose caption says only what the picture is, followed by an
`.image-notes` slide with that same image small and bullets unpacking it —
then, after the images, one or two framing questions for the whole session.
Use it when a picture can put students inside the problem before any reading
has been named — see the opening of `enlightenment-progress`, which pairs
de Troy's *Time Unveiling Truth* with Wright of Derby's orrery. It is
optional; a deck with no such image should start at the title.

Otherwise a single-session deck (one class meeting, e.g.
`carr-historian-and-facts`) runs roughly:

1. **Title** — course/week eyebrow, the deck's own title (not necessarily the
   syllabus session title), a `.rule`, and a `ul.source-list` of what it
   covers with page/date specifics in the `.detail` line below.
2. **The take home, up front** — the whole day in one headline, then at most
   three supporting points as `.reveal-block` fragments (the last one a
   `.takehome`). Say the thing you want them to leave with before they have
   the evidence for it; the recap and a closing "take home, paid off" slide
   return to the same sentence once they do. Don't put the lecture's outline
   on this slide.
3. **The arc of the lecture** — a separate slide, immediately after, laying
   out the parts in order: a `.cards` grid, one card per part, each with a
   number and date or source in the `.num` line, a short headline, and a
   sentence on what happens there. Students should be able to tell where they
   are in the hour from this slide alone. See the two opening slides of
   `enlightenment-progress`.
4. **Per source or person**, repeated: a "00: who they are" bio slide (often
   a `.parallel` two-column: life / work, or life / historical moment), an
   image slide for their portrait, then 1–4 quote slides (primary `.quote` +
   `.reveal-block.unpack`/`.argument`/`.historical` fragments + `.takehome`),
   interleaved with image slides for objects, manuscripts, places, or events
   the quotes reference.
5. **A discussion pair at the end of each part** — a question slide, then a
   separate answer slide. See below; this is where the class talks, and it
   replaces parking every question in a list at the end.
6. **Comparison**, if the session pairs two people/texts — a `.parallel`
   slide asking what actually separates them, not just what's different.
7. **Recap** — a `.cards` grid, one card per takehome, drawn especially from
   the answer slides.
8. **Closing discussion**, only if a question genuinely needs the whole hour
   behind it — synthesis across both writers, or one that reopens the
   take-home. A `ul.questions` list of everything from `schedule.md` is not
   that; distribute those instead.

A deck covering two sessions in one week (e.g. `divine-power-and-statecraft`,
which does 3.1 and 3.2) adds a `Part one · 3.1` / `Part three · 3.2` transition
slide between the two halves and a recap that spans both.

## Discussion questions and their answer slides

Questions belong throughout the deck, roughly one per part, not collected at
the end. A question asked while a source is still on students' minds gets
answered from the source; the same question asked in the last five minutes
gets answered from memory, by whoever talks first.

**The question slide.** Put it after the quote slides that give students what
they need, so the discussion has evidence to run on. The question is the
headline (`.main-point`); a `ul.questions` list underneath can add a second or
third way in, but one real question beats three vague ones. Ask "why this, why
then" about a *particular* choice in the text — "Why does Voltaire measure ages
by taste rather than by conquest, when he is writing about a king's reign?" —
not something that could be asked of any reading in the course. The test: a
student who did the reading can answer it and a student who didn't can't. Keep
the slide sparse; it stays on screen for the length of the discussion.

**The answer slide.** A separate slide, never a fragment on the question slide,
so the question can sit up while the room works and nothing gets revealed by an
early arrow key. It states the point the discussion should land on — a
`.takehome`, sometimes with one `.reveal-block` of evidence before it — and it
should read as the payoff to what students just said, not a correction of it.
Where the reading genuinely supports more than one answer, name the good
alternative rather than pretending there was one right answer waiting. These
takeaways are the raw material for the recap cards.

## Image slides

**The image is the slide. Make it as large as the slide allows.** This holds
for every image slide, not just an opening one — a portrait, a title page, a
map, a painting. The theme already does the work: `figure.landscape` puts the
caption underneath, `figure.portrait` puts it in a narrow column to the right,
and both hand the rest of the space to the picture. Don't fight it by writing
a caption long enough to squeeze the image.

**Write the caption for yourself, not for the back row.** It is small on
purpose. Its job is to hold what the picture is — subject, date, where it
lives — plus the one point worth making about it, in language you can pick up
and elaborate on out loud. Students do not need to read it, and should not
have to. The common failure is a caption that tries to be the lecture: four
sentences of argument set in type nobody can read past row three. Say it
instead. Two lines and a credit is the target; the credit line always stays.

**One image per slide. A second image is a second slide.** Show one, let it
land, then show the next. Two pictures crowded together halve each other.

**Two side by side only after each has had its own slide, and only for a
minor comparative point.** A `figure.pair` is for two things that answer one
small question together and stack cleanly — two antagonists in one quarrel,
two views of a single object, recto and verso of a leaf. If each image is
carrying a point of its own, they are two slides, not one figure. The test is
the same as before: say in a clause what each establishes that the other does
not. If you can, they are separate slides; if you can't, cut one.

**Small images beside text belong on an `.image-notes` slide**, not in a
caption — the reduced image in the left column with bullets alongside. That is
the place for the argument a caption is too small to carry. **One image per
notes slide**: two pictures and two sets of bullets on one slide gives neither
enough room, so a second image repeats the pattern — full-bleed, then its own
notes slide. The `.shots` wrapper exists for the rare case where two images
genuinely share one set of bullets.

**A notes slide says what the image means for the argument, not what is in
it.** Describing the picture is only the setup; every bullet has to close the
distance to the ideas the session is about. Name the figure or the object,
then say what it commits its makers to — "Time does the unveiling, which is
this week's claim about history in one gesture, and the reverse of every
scheme on the last three slides." A bullet that stops at identifying the
iconography is doing an art-history exercise, not a history lecture.

## Front matter

Prefer the `.md` + `layout: reveal-lecture` pattern (see
`divine-power-and-statecraft/index.md`) over a raw standalone `.html` file —
it's the current, maintained pattern; the older decks (`carr-historian-and-facts`,
`greeks-evidence-and-purpose`) predate the shared layout and duplicate the
`<head>` boilerplate. New decks should look like:

```yaml
---
layout: reveal-lecture
title: "Deck Title — the authors/texts it covers"
image_slides: true
---
```

Drop `image_slides: true` only if the deck genuinely has no image slides.

## Sourcing images

Public domain, CC0, or CC BY/BY-SA/BY-NC only — check the license on the
Wikimedia Commons file page (or via the API) before using anything. CC BY and
CC BY-SA need attribution in the `<figcaption>`; CC BY-NC needs the same plus
a note that the site's use qualifies as non-commercial. Never strip the
credit line once it's in a caption.

Fetch and process at the command line, don't hand-save from a browser:

```sh
curl -L -H 'User-Agent: your-name (your-email)' \
  'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2000' -o raw
sips -Z 1800 raw --out out.jpg -s format jpeg -s formatOptions 88
```

Pick images that read at projector distance. Large figures, clear gestures,
real contrast between the thing and its background. A finely detailed wash
drawing or a crowded engraving can be perfectly bright by the numbers and
still land as murk on a screen — the test is whether someone in the back row
can tell what is happening in it without being told.

Source at width 1400–2200, cap the long edge at 1800px, recompress to JPEG.
q78 is the default; use q82–88 for anything carrying fine detail (manuscript
script, small map labels, low-relief carving) that q78 visibly smears. Keep
the whole `images/` folder under ~10MB.

Every `images/` folder needs a `README.md`: a credits table (file, what it
is, source, license) plus a Notes section documenting anything non-obvious —
derivative crops/annotations and what was added, deliberately ambiguous or
non-contemporaneous images and why they're used anyway, and the exact
re-fetch/regenerate command for anything processed. See any existing
`images/README.md` under a course's `slides/` folder for the format. If you annotate a
derivative (a gold box around a detail, a crop), say so in the caption too —
don't let an added mark look like it was in the source.

`<figure>` gets a `portrait` or `landscape` class matching the image's actual
aspect ratio (portrait puts the caption beside it, landscape below); a `pair`
figure holds two related images above one caption (two faces of one object,
two witnesses to one text). Inside a caption, `<em>` is the block-level
source/credit line, `<i>` is inline italics for titles — don't nest `<em>`
inside the note.

## Before publishing

Check the deck actually builds: Jekyll's SCSS compile needs a UTF-8 locale,
so build with `LC_ALL=en_US.UTF-8 bundle exec jekyll build` (or the project's
usual serve command) rather than assuming a bare invocation will work.

Then open it in a browser and step through every slide, advancing each
fragment. You are looking for content clipped at the bottom of the 960×700
box — the failure that never shows up in the source file. Fix it on the slide,
not by shrinking the theme.

Then have a **fresh-context agent review the finished deck**. This is a
required step, not an optional one, and it is the reason a deck is not done
when the last slide is written: whoever (or whatever) wrote the deck has spent
hours building a case and will read the deck as confirming it. A reader coming
to `index.md` cold, with no memory of the drafting, catches what the author
cannot see. Point it at the deck file and the readings, and ask it to report
problems with evidence rather than to fix anything — three things in
particular:

- **The historical arc.** Does the story the deck tells across its parts
  actually hold? Dates and sequence, who could have read whom, causal claims
  ("this made that possible"), and anything asserted as a first, a peak, or a
  break. Flag claims that are defensible but contested, and claims that are
  simply wrong.
- **Every quotation.** Each quote checked against the source it cites, word
  for word, with the page or section number verified — not recognized, looked
  up. Ellipses and bracketed insertions must not change the sense. A quote
  that can't be located in the cited text is the finding, whatever it sounds
  like. See "Precision over invention" above.
- **Cross-slide integrity.** The opening take-home, the arc slide, the recap,
  and the closing take-home have to describe the same lecture: the arc slide's
  parts match the parts that exist, the recap has a card for each takeaway,
  the closing slide pays off the sentence the opening one made. Names, dates,
  spellings, and citation formats consistent slide to slide; forward
  references to other weeks accurate; no promise made early that the deck
  never keeps.

Work the findings before publishing. Verify each one against the source
yourself — a cold reader will sometimes flag a correct claim it lacks the
context for, and being confidently wrong about a date is as easy for the
reviewer as for the author. Fix what's real; leave a note in the deck or the
commit for anything you decide to keep.

Link the new deck from the course's `schedule.md` under the session it
belongs to, matching the existing `[Slides of ...](slides/<slug>/)` phrasing.

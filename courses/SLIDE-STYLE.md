# Slide Deck Rules

How to write and build a lecture deck for any course on this site. Read this
before starting a new one. The mechanics of the CSS classes (`.eyebrow`,
`.reveal-block`, `.swap`, `.parallel`, etc.) are documented in the header
comment of `/assets/css/reveal-lecture-theme.css` — that comment is canonical;
don't duplicate it here. This file is about what to write and how to source it.

A deck lives at `courses/<course>/slides/<deck-slug>/`, with `index.md` beside
an `images/` folder and, when it has open problems, an `ISSUES.md`. Both
`ISSUES.md` and `images/README.md` are contributor notes, excluded from the
build in `_config.yml` — never served, so write them for whoever picks the
deck up next. Worked examples named below are in
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

**Name people; don't reduce them to a single deed.** "The man who built the
university, writing about what historians do" is magazine prose — an epithet
standing in for a name — and it makes a scope error in both directions at
once.

*Too large for the deed.* Humboldt directed the Prussian education section for
about sixteen months, drafted a plan, and resigned the post in 1810 before the
university opened, staying on only as chair of its founding committee. A
ministry, a committee, Fichte and Schleiermacher are all inside the word
"built." The construction awards one person sole agency over something
institutional — the great-man compression this course spends a semester
teaching students to distrust.

*Too small for the person.* Humboldt's standing rests on comparative
linguistics, the Basque and Kawi work, the theory of *Bildung*, and Prussian
diplomacy at Vienna as much as on a university. A polymath introduced by one
administrative act has been made smaller, not clearer, and the epithet quietly
tells students that is all he was.

Write instead the name, the standing that put the person in a position to
produce this text, and a claim: "A comparative linguist, not a historian,
defines the historian's task." The register to aim for is the one you would
use in a journal article — plain, specific, no build-up. **The test: if the
headline would sit comfortably as a magazine subhead or on a book jacket,
rewrite it.** Precision is usually the more interesting option anyway —
"resigned before it opened" is a better sentence than "built it," and it has
the advantage of being true.

This is not a ban on describing someone by a role or a station. "A schoolmaster
of twenty-eight, publishing his first book" is accurate, checkable, and
deflates rather than inflates — it earns its place because the point of the
slide is how ordinary Ranke's position was. What goes is the heroic epithet
that substitutes for a name and settles a person's significance in one clause.

**Cut the explanatory tail.** Headlines drift into two parts — a claim, then a
comma and a clause explaining how it came about: "Two jobs history had always
claimed, handed back in one sentence"; "A schoolmaster of twenty-eight,
publishing his first book"; "The best-trained history in Europe, put to work
for the nation." The first part lands. The tail explains, and the block
underneath is about to explain it anyway, at more length and better.

The test: read the headline without the tail. If the claim survives, the tail
was scaffolding — "Two jobs history had always claimed" leaves a student
leaning forward, and the quotation below delivers the rest.

Keep a second element only when it carries a *turn* rather than an
explanation: a contrast ("A comparative linguist, not a historian, defines the
historian's task"), a reversal ("Both of them promise 'what actually
happened.' Neither meant just the facts"), or a genuine pair the slide is
built on ("A problem described, and a problem given a procedure"). Those are
not tails — the claim is incomplete without them. And where a tail is really a
predicate in disguise, promote it instead of cutting: not "The best-trained
history in Europe, put to work for the nation" but "The best-trained history
in Europe was put to work for the nation."

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

The same goes for pointing at the deck's own machinery: "three slides
earlier," "compare the portrait two slides on," "see the note on the closing
slide." These break the moment anything is moved or inserted — every one of
those three examples was dangling or off by one by the time its deck was
finished — and a reader who needs the connection is better served by six words
repeated than by being sent somewhere. If a disclosure matters, put it where
the problem is, not where you promise it will be.

**Cross-references stay, but flatten them to a pointer.** References backward
and forward are worth making — they are most of what makes a survey course
cohere. What they should not be is staged. Write `Compare Voltaire in 4.1.` or
`Compare Week 9 (Said, Trouillot).` and stop: the reference is a signpost, and
the person delivering the lecture will elaborate on it out loud. What goes is
the narration wrapped around it — "the shape historians in Week 9 will find
underneath nineteenth-century imperial history," "Herder, who closed the last
session refusing any universal standard, is the ancestor of the move." Those
spend three lines dramatising a connection that one clause can make.

**The register to match is the syllabus, not an explainer.** `schedule.md` is
the model: "Pay attention to what Bede thinks history is *for* — compare his
answer to Livy's." "Read after Burke and focus on the core contrast: slow
structures versus fast events." "A direct challenge to the Week 4
professionalization story." Flat, declarative, specific, unexcited. A slide
should read like that, not like something walking a reader through a
revelation.

Phrasings to cut on sight, all of which crept into these decks and had to be
removed: **"Hold onto this"**, **"Notice that…"**, **"Worth keeping in
view"**, **"The question worth carrying"**, **"Which is the uncomfortable
part"**, **"This is the actual innovation"**, **"the useful question isn't X,
it's Y"**, and any staging by clock or slide count ("twenty minutes from now,"
"three slides earlier"). Block labels attract this worst of all: prefer a
label that *names* what the block contains — "The innovation," "The word
'only'," "Whose manners," "What rigour does not prevent" — over one that
instructs the reader how to feel about it.

A specific course connection is not clutter and stays: "the two writers you
read," "Bridge between weeks 3 and 4," a `.source-list`, a `.cite`. Those point
at something — this text, that session, this week's place in the sequence — and
that pointing is the work. What goes is the flourish that points at nothing.
Second person is likewise fine when it's doing analytic work ("the useful
question isn't 'is it true?'"), not when it narrates the seminar.

**Introduce people on their portrait slide, then go straight to the detail.**
The sequence for a person is two slides, not three: an image slide whose
caption carries the whole introduction, then the first content slide about
what they wrote.

Put in the caption rail, and nothing else: **the name and dates** on the label
line, then a **brief bio** — where they lived, what they had done, what put
them in a position to write this — then a **`Why he matters:` line** saying
what their presence in this session is for, then the **credit**. No headline,
no `.reveal-block`, no take-home; the picture and the rail are the slide. A
face and a paragraph beside it introduce someone faster than a slide of dates
with no face, and it buys back a slide per person.

Keep the whole caption **under about 500 characters**. The rail is `max-width:
26%` — roughly 214px of text, about 26 characters a line in the italic body —
so 500 characters is already some twenty lines against a 640px slide. Past
about 640 characters the rail overflows and is clipped, not scrolled. The four
portrait captions in `enlightenment-progress-2` (Voltaire, Kant, Condorcet,
Herder) run 426–504 and are the model.

The person's *arguments* still get full slides afterwards, unchanged — this
rule only replaces the separate "00: who they are" bio slide, which said in a
two-column `.parallel` what a caption can say beside a face. The older decks
(`divine-power-and-statecraft`, `scientific-history`, and part one of
`enlightenment-progress`) still carry standalone bio slides; they predate this
rule and are not the model on this point.

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
marks and attribute them to the author — paraphrase in your own voice instead
and cite the chapter generally. This applies as much to secondary readings
(Popkin, Maza, Green & Troup) as to primary sources. A wrong citation in a
teaching deck is worse than a thin one.

**But record that compromise off the slide.** A caveat about how the deck was
made — "the translation was unavailable," "no exact page cite because the PDF
wouldn't open," "paraphrased, not quoted" — is a note to the instructor, not
teaching material. A student has no use for which file failed to open, and a
line spent on it is a line not spent on the history. It also dates the deck to
one production run.

Put it in **two places instead**: tell the author directly, in whatever channel
you are working in, and write it into an `ISSUES.md` beside `index.md` in the
deck folder. That file is the deck's own to-do list — open sourcing problems
and what would close them, plus deliberate deviations recorded so a later
reviewer doesn't re-raise them. Head each item with a status, say what would
resolve it, and delete items as they clear. See
`making-history/slides/scientific-history/ISSUES.md`, which carries a
paraphrased-because-unobtainable primary source, an unverifiable portrait
date, and three decisions taken on purpose.

The deck itself stays clean: it may carry a citation-conventions line (which
readers use), and it must never carry a quotation it cannot support — but the
story of its own making belongs in `ISSUES.md`.

Two further ways a citation goes wrong without being a fabrication. **Keep the
framing clause when you quote a quote.** Popkin introduces an 1843 attack on
women historians with "even some women endorsed this view"; a slide that
renders that as "a British author in 1843" has quoted accurately and taught
the opposite of the point. The secondary author's framing is usually the
reason the quote is in their book at all. **And attribute the superlatives.**
"The first American history PhD," "the Prussian state funded it," "his real
invention" — where a claim like that comes from the assigned reading, put the
reading's name on it ("Popkin dates the first American history PhD to Johns
Hopkins, 1876"). Most firsts and breaks are contested, and a teaching deck
should not be the thing asserting them in its own voice.

**When the wording carries the argument, check the original language.** Nearly
every primary source in these courses is read in translation, so a slide that
turns on a text's *exact words* is making a claim about the translator as much
as the author. Two writers can converge in English and diverge entirely in
their own language: Humboldt's "the historian's task is to present what
actually happened" is *die Darstellung des Geschehenen*, while Ranke's
identical-looking English is *wie es eigentlich gewesen* — the sameness is the
translators', and a deck built on their being "the same sentence" would have
been built on nothing. It cuts the other way too. Ranke's preface says his
companion volume of criticism appeared *an Einem Tage* with the book, which
the standard English softens to "concurrently" — there the German is the more
precise source, and the deck should follow it. Name the translator whenever
the choice is doing work: "racially kindred" is a 1981 rendering of
*stammverwandt*, "of kindred stock," and a slide leaning on that word owes
students the note.

**Read past the passage you want.** The quote that makes your point is easy to
find and easy to stop at. Before building a takehome on one passage, search
the rest of that same text for passages that cut against it; where they exist,
put the tension on the slide instead of hoping nobody checks. Ranke's "every
epoch is immediate to God" reads as a refusal to rank anything at all until
you notice the same 1854 lecture calling Asia's history "retrogressive" and
dating art's peak to the sixteenth century. The honest version — he refuses to
rank *generations*, and ranks peoples freely — is both true and more
interesting than the tidy one. This is also how two slides in one deck end up
contradicting each other: each is faithful to a different half of a source
nobody read all the way through.

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
4. **Per source or person**, repeated: an image slide for their portrait,
   whose caption carries the whole introduction — name, dates, brief bio,
   why they matter here, credit — and then straight into 1–4 quote slides
   (primary `.quote` +
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

**Translate a foreign-language title, in the caption, the first time it is
shown.** Give the original in italics and an English rendering right after it.
A student looking at a title page in Fraktur cannot tell what object is in
front of them, and "the book itself" is not an answer. This is not only
housekeeping: the translation frequently carries the argument. Ranke's title
page reads *Geschichten der romanischen und germanischen Völker* — "Histories
of the Romance and Germanic **Peoples**," and the plural *Geschichten* is
deliberate, as his own preface says: "It contains only histories, not
History." A caption that never renders the title loses a point that is sitting
in the assigned reading.

Where the conventional English differs from the literal, prefer the literal in
the caption and let the deck cite the edition's own title elsewhere — the two
diverging is itself worth a sentence out loud in a session about translation.

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

**Each note bullet runs in three beats: look, then meaning, then a
question.** A bullet that stops after the first two has told students what to
think and given them nothing to do with it. The shape is:

1. **A bold lead naming what to look at.** Something actually visible in the
   picture — "You have to look for the man," "Somebody built this room." Not a
   thesis; a direction for the eye.
2. **A sentence or two of elaboration.** What that detail is, and what it
   commits its makers to. This is where the argument lives.
3. **A closing question, in `<em class="ask">…</em>`.** It renders gold, on its
   own line, so the three beats stay legible at a glance.

The question is the part that is easy to skip and worth the most. It should
**not** be answerable from the image, and needn't be answerable yet at all —
its job is to put a student in the right frame before any reading has been
named, and to be worth returning to an hour later. Aim it at the session's
real problem: *"If a historian disappears behind the sources, who chose which
sources to stand behind?"* is doing that work; "What does this photograph tell
us about Ranke?" is not, because it asks about the picture rather than through
it. One question per bullet, and no answers on the slide — the payoff belongs
in the discussion slides and the take-home.

**Budget a line for it.** The question renders on its own line, so adding one
to each of four bullets costs four lines, and the elaboration has to give them
back. The notes column is about 456px wide at roughly 52 characters a line,
against a height budget of about 23 lines; the two `.image-notes` slides in
`enlightenment-progress` run 21 and 22 lines, so there is very little room
above that. Measure before assuming it fits — a wrong guess at characters per
line is easy to make and the overflow is silently clipped, never scrolled.
The `enlightenment-progress` notes slides predate this rule and carry a bolded
assertion where the question should be; they are not the model on this point.

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

## Cache the text of a scanned reading

Course PDFs come in two kinds. A born-digital one gives up its text to
`pdftotext -layout` in a second. A photocopier scan — most of the book
chapters here — has no text layer at all and returns zero bytes, which leaves
reading the page images as the only way to check a quotation.

**Do that once, then save the result.** Reading a sixteen-page scan is
expensive however it is done, and the cost recurs every time: while drafting,
again during the fresh-context review, and again next year when the deck is
revised. A cached text file turns all of those into a `grep`.

```sh
swiftc -O -o /tmp/ocr-pdf scripts/ocr-pdf.swift     # once
/tmp/ocr-pdf ~/Dropbox/courses/<course>/optimized/<reading>.pdf 2 > raw.txt
```

`scripts/ocr-pdf.swift` uses macOS Vision and needs only the Xcode Command
Line Tools. A chapter takes about twenty seconds.

Three rules about the file you save:

- **Keep it beside the reading, never in this repo.** These are in-copyright
  course materials. They belong in
  `~/Dropbox/courses/<course>/.research-packets/<reading>.ocr.txt`, alongside
  the PDF. Nothing under `courses/` in the site repo should contain the text
  of an assigned reading.
- **Mark the printed page numbers.** A scan of a book is usually two-page
  spreads, so one sheet holds two printed pages and a passage in the right-hand
  column belongs to the *next* page. Convert the running heads into explicit
  `[[ printed page NN ]]` markers before you cite from the file. This is not
  fussiness: citing p. 88 for a sentence printed on p. 89 is precisely the
  error the marker prevents, and it is invisible without one.
- **Say what the file is not.** OCR is not a proofread transcription — Vision
  mangles ligatures, footnote markers and italics, and drops the odd running
  head. Head the file with what produced it, when, which pages it covers, and
  which pages could not be marked. Use the cache to *find* a passage and its
  page; verify the exact words against the page image before they go inside
  quotation marks on a slide.

`~/Dropbox/courses/making-history/.research-packets/popkin-ch-4.ocr.txt` is a
worked example of all three.

## Before publishing

Check the deck actually builds: Jekyll's SCSS compile needs a UTF-8 locale,
so build with `LC_ALL=en_US.UTF-8 bundle exec jekyll build` (or the project's
usual serve command) rather than assuming a bare invocation will work.

Before opening a browser it is worth *measuring* rather than guessing: strip
the tags from each `<section>` and compare its character count against a deck
already known to display correctly. In `enlightenment-progress` the ceiling is
roughly 1,800 characters on a `.swap` slide (where fragments replace one
another in place, so only the largest is ever on screen) and roughly 1,250
where blocks stack — and no slide there puts a `.reveal-block` underneath a
`.cards` grid, which is the arrangement most likely to overflow, since a
three-card grid costs the same two rows as a four-card one. Anything past
those numbers is worth restructuring before you ever see it clipped.

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

**Make the review cheap enough to finish.** An agent that has to OCR a
sixteen-page scan before it can check a page number will spend its budget on
mechanics and stall before reaching the argument. Extract the sources to text
first (see "Cache the text of a scanned reading" below), hand over the paths,
and order the work so the cheap checks come first: cross-slide consistency and
the arc need no external source at all, and they catch the errors that cost
the most to leave in.

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
  never keeps. Check the punchy framing line on the title or take-home slide
  against the biographical slides especially — it gets written first, before
  the details that can flatly contradict it ("two men in Berlin," when one of
  them was teaching in Frankfurt an der Oder).

Work the findings before publishing. Verify each one against the source
yourself — a cold reader will sometimes flag a correct claim it lacks the
context for, and being confidently wrong about a date is as easy for the
reviewer as for the author. Fix what's real. Anything you decide to keep goes
in `ISSUES.md` as a deliberate deviation with the reason, so the next reviewer
does not raise it again — not into the deck, and not left only in a commit
message nobody will read.

Link the new deck from the course's `schedule.md` under the session it
belongs to, matching the existing `[Slides of ...](slides/<slug>/)` phrasing.

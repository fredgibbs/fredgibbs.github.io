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

**Reuse the course's metaphors; invent new ones only for a reason.** A figure
students have already met is an asset. When a later slide says "the program was
a room, not a thesis," or calls Marx's answer a motor, it reaches back and
recalls the slide where that image was built — the phrase is doing the work of
a whole argument students have already sat through, and repetition is how it
becomes shared vocabulary for the course rather than one slide's decoration.
Use them deliberately and use the same words each time; a metaphor rephrased is
a metaphor thrown away.

The bar is on **invention**. A new figure standing in for a plain statement
costs a beat of translation, and in a lecture that beat is spent not listening.
"What the documents say, once the embroidery is off" means *reported without
invention* — but the reader has to work out that embroidery is added detail,
and by then the slide has moved on. It reads well and teaches badly.

So before coining one, have a specific reason. Good reasons: it is the source's
own image (Braudel's fireflies — his, quoted, and unpacked where it appears);
the slide stops and explains it (a structure is a prison, then "a structure is
defined by what it forbids"); or it names something with no plain equivalent.
Not a good reason: it sounds better than the literal sentence. The rule binds
hardest on the orientation slides (`.throughline`, `.thread`, `.cards`), which
students read fast and in passing — but note that those slides are also where
an *established* metaphor pays off most, because a reader skimming recognizes
it instantly.

**Keep eyebrows as simple as possible.** The `.eyebrow` is a label, not a
sentence: what this slide is about, and when. `Voltaire · 1694–1778`. `The
Enlightenment · roughly the 1680s to the 1790s`. `Discussion · 4.1`. A few
words, or a name and a date, with `·` between the parts. Don't editorialize
there and don't let it pre-empt the argument the headline is about to make —
"The take home · the same sentence, now with evidence behind it" is a sentence
wearing a label's clothes. If the eyebrow needs a verb, it belongs in the
headline.

A cold-open slide's eyebrow should name the pictures, not the moment. "Before
we start" is wrong on the fourth slide of a deck — the class has started, and
two paintings have been up for several minutes. `Lepanto, 1571 · the olive
grove, 1889` labels what is actually on screen, and gives the two dates the
slide is about to set against each other.

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

**Don't call the class meeting "the hour."** The recurring furniture slides
attract a particular tic: locating the session in time and space instead of
naming it. "Where this hour sits," "where the hour went," "where this lands,"
"the rest of the hour." It reads as writerly, it is one more thing the room has
to decode, and it dates the slide to a delivery that may run fifty minutes or
seventy-five. Say **today**:

| Instead of | Write |
|---|---|
| Where this hour sits | **Today in context** |
| Where the hour went | a headline naming what the three parts *were* |
| Discussion · where this lands | **Answer · part one** |
| Why the rest of the hour is Ranke | Why the rest of today is Ranke |

This is about text on slides, not about how this file talks. The throughline
and arc slides are the usual offenders because their eyebrows get written once
and copied forward; `annales-longue-duree` has the right versions of both.

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

**Wrap that line in `<span class="why">`.** It renders as a block with space
above it, which sets it off from the biography — the two are doing different
jobs and should not run together as one paragraph. Wrap the whole sentence and
not just the `<strong>` label, or the text after the colon is orphaned onto its
own line. Never fake the gap with `<br><br>`: the spacing then differs deck to
deck and nothing carries it to the next one.

**The line says what the person *did*, not what happened to them.** The test is
whether it would still be true and still be interesting if the person's
circumstances had been comfortable. "He wrote the book quoted here out of notes
and memory, with no library he could reach" is arresting, and it is
biography — it belongs in the bio sentences above, or better, on the slide that
quotes him saying so. What it is not is a reason Bloch matters to a lecture on
structures; the reason is that he argued the shape of a French field outlasts
every law written to explain it. Posts held, books edited, who succeeded whom
in which chair are the same kind of fact: real, useful in the bio, and not an
answer to "why is this person in this session." Name the claim, the method or
the move that the rest of the deck is about to depend on. Check it against the
takehomes: if nothing later in the deck pays the line off, it is the wrong
line.

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

**Keep the blocks short. The `.takehome` is a line, not a paragraph.** This is
the rule these decks break most often, and the drift is measurable. Median
`.takehome` length, oldest deck to newest: 116 characters in
`divine-power-and-statecraft`, 160 in `enlightenment-progress-2`, 308 in
`scientific-history`, 358 in `marx-structural-history` — where the longest ran
to 675. The `.reveal-block` held roughly steady across all four (323, 326, 358,
362), so it is specifically the takeaway that inflated, in a theme whose own CSS
calls it "the pithy takehome line."

That rule worked where it was applied. Re-measured, `marx-structural-history`
now runs a median `.takehome` of 20 words and `annales-longue-duree` 13. What
it did not cover is every other paragraph on a slide, and those are where the
length went instead.

**The budgets, in words.** Count words, not characters — a character budget is
not a thing you can hold in your head while writing a sentence, so in practice
nobody checks it. These numbers are the same budgets as before at roughly six
characters a word, extended to the containers that never had one:

| Container | Target | Hard stop | It is |
|---|---|---|---|
| `.takehome` | **30 words** | 40 | one or two sentences |
| `.reveal-block` | **55 words** | 70 | three sentences |
| `.image-notes` bullet | **40 words** | 50 | lead, elaboration, question |
| caption describing a picture | **40 words** | 55 | two lines and a credit |
| caption introducing a person | **80 words** | 90 | bio, `why`, credit (~500 chars) |
| `.detail` | **30 words** | 40 | one sentence under a headline |
| `.main-point` headline | **14 words** | 18 | a claim, no explanatory tail |

The two caption rows are split by **job, not by tag**. A caption is an
introduction when it carries a `<span class="why">` line — usually the rail of
a `figure.portrait`, but a small landscape photograph can introduce someone
too, and then it gets the larger budget. Every other caption says what the
picture is and makes one point, and gets the smaller one.

Where the uncovered ones stand now, median words per deck, oldest to newest:
the `figcaption` `<em>` ran 68 in `divine-power-and-statecraft`, 53 in
`scientific-history`, 49 in `enlightenment-progress-2`, 59 in
`marx-structural-history`, **69** in `annales-longue-duree` — no improvement
across five decks, and the newest is the longest. Note bullets run 39 to 57 on
the same decks. Both are roughly **half again over** the targets above, and
neither has ever been measured before now.

**Length is the register problem.** The vocabulary rules above are being
followed — a scan of the recent decks for the usual tells ("isn't just X, it's
Y", "crucially", "at stake", "delve") finds almost nothing. What still doesn't
sound like `schedule.md` is the *shape*: a 69-word caption has room for a
setup, a turn and a conclusion, so it acquires them, and three-beat prose reads
as written-by-committee however plain its words are. The syllabus sentences the
register rule holds up as models — "A direct challenge to the Week 4
professionalization story" — are nine words and one clause. A caption at 40
words can hold what the picture is plus one point. At 70 it is an essay set in
type nobody can read, and it will sound like one.

**Check the budget before the browser, with the deck's own numbers:**

```sh
scripts/slide-words.py courses/<course>/slides/<deck>/index.md
```

It prints every container over its target with a word count and the first few
words, and exits non-zero if anything is over its hard stop. Run it on a
finished deck the way you'd run a linter; overflow in the viewport and overflow
in the register are the same defect caught at two different moments.

How they inflate, in the order it happens. A block is written as a claim. Then
a supporting quotation is dropped in whole, because it was already checked and
seems a shame to waste. Then a clause is added attributing it. Then a second
finding is appended because it is on the same page of the reading. Nothing in
that sequence feels like padding while you are doing it, and the block doubles.

**The test: read the block aloud. If you take a second breath, it belongs to two
blocks.** A second test, for the takehome specifically: if it contains the word
"and" joining two independent claims, or a parenthetical page citation in the
middle rather than at the end, it has stopped being a line.

**Where a block genuinely carries parallel items, use bullets.** Three pieces of
evidence chained into one sentence with semicolons is worse than three bullets,
and the theme styles `ul` inside `.reveal-block` and `.takehome` with the same
short gold dash as `ul.source-list`. Bullets are for items that are actually
parallel — three things the same argument rests on, three ways a method fails.
They are not licence to keep the same wordage and add markers: the budgets above
still apply to the block as a whole.

What to cut first, in order: the attributive clause ("Green and Troup are
careful to note that…") when the page cite already says whose words these are;
the second quotation; the qualification that the next slide makes anyway; and
any sentence that restates the label. A block whose label reads "The innovation"
does not need to open "The innovation here is…".

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

**Every `.cite` must be reproducible on its own terms.** A citation's job is
to let a reader find the words again, so a bare `Bloch, p. 39` fails even when
the page is right: it names no work, and a volume that reprints several texts
makes the page number ambiguous on its own. Name the work in the `.cite`, and
put the edition on the title slide's `.citation-note`, where it is stated once
for the deck. The eyebrow doesn't count — it scrolls past with the slide, and a
student reading a photographed slide later doesn't have it.

This matters most when the assigned PDF is an excerpt from a larger volume.
The 5.2 deck quotes seven passages "from Braudel," but only four are in the
assigned pp. 25–54: the rest come from the 1949 *Mediterranean* preface and the
1950 inaugural lecture, which *On History* reprints in the same book. A student
turning to p. 4 of their own excerpt finds nothing there. Say which piece each
page belongs to, and let the `.citation-note` spell out what the excerpt does
and doesn't contain. For a quote of a quote, cite both ends — Braudel's own
footnote gives Halphen's book and page, so the slide gives them too.

**Apparatus gets apparatus typography.** A source note is not a supporting
point, and it should not be set like one. `.detail` renders at 0.75em in the
body font — the same voice as the argument — so a line like "Descriptions
quoted from p. 3" placed under a `.cards` grid reads as a fourth card and
competes with the three that carry the message. Where quoted text sits in a
block with no `.quote` to hang a `<span class="cite">` inside, put the note in
a standalone `p.cite` instead: mono, 0.45em, muted, sentence case. Mono is what
does the work — it marks the line as machinery rather than content, at a glance
and before it is read. Reserve `.detail` for sentences that actually argue
something.

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

A deck may open before everything else with a **cold open**: a full-bleed
slide per image whose caption says only what the picture is, then the session's
framing question while the pictures are still on students' minds, and then an
`.image-notes` slide with the images small and bullets working the question
over. Ask before you unpack, not after — a question asked last is a summary,
and the notes slide has already given the answers away. Asked first, it is a
question the room can still be wrong about, and every bullet after it is
evidence.

**When the cold open is built on a contrast, unpack the two images together on
one slide, not separately on two.** Put both in a `<div class="shots">` in the
image column — they stack — and write each bullet across the pair rather than
about one of them: "An afternoon, against a hillside that takes centuries,"
"Both are full of people; neither names them." Two separate notes slides
describe two pictures and leave the comparison to the framing question, which
is the one thing the cold open exists to set up. It also costs a slide. See
the opening of `annales-longue-duree` (Lepanto against the olive terraces) and
the factory and barricade pairs in `marx-structural-history`.
Use it when a picture can put students inside the problem before any reading
has been named — see the opening of `enlightenment-progress`, which pairs
de Troy's *Time Unveiling Truth* with Wright of Derby's orrery. It is
optional; a deck with no such image should start at the title.

Otherwise a single-session deck (one class meeting, e.g.
`carr-historian-and-facts`) runs roughly:

1. **Title** — course/week eyebrow, the deck's own title (not necessarily the
   syllabus session title), a `.rule`, and a `ul.source-list` of what it
   covers, with page/date specifics on each line.

   **Order the readings the way the syllabus does: the general reading first,
   the primary sources under it.** The textbook or survey chapter (Popkin,
   Maza, Green & Troup) is what students read to get their bearings, and the
   schedule page lists it first for that reason. A title slide that leads with
   the primary source is out of step with the page they were assigned it from.
   Keep the `Background:` prefix on the general one so the two kinds stay
   visibly distinct.

   **Put the citation conventions in a `.citation-note`, not a `.detail`.**
   Which translation, cited by page or by section, which edition the assigned
   PDF came from — real information, but housekeeping. `.detail` renders at
   0.75em, *larger* than the `ul.source-list` above it, so the housekeeping
   ends up outweighing the day's readings. `.citation-note` is 0.5em and sits
   quietly underneath them. (A few older decks do this with an inline
   `style="font-size:0.5em"`; the class replaces that.)

2. **Today in context** — a `.throughline` slide: one question the course
   keeps asking as the `.main-point`, and the answers given so far as
   `.answer.past` / `.answer.now` / `.answer.next`. See below. Each part after
   it opens by saying what the last part left unfinished.
3. **Per source or person**, repeated. Open each part with the *work* rather
   than the face — the text, the journal, the argument, whatever gives
   students a reason to care who these people were. A portrait of a stranger
   is a stranger; the same portrait after the 1929 editorial is the man who
   wrote it. Then the image slide, whose caption carries the whole
   introduction — name, dates, brief bio, why they matter here, credit — and
   then 1–4 quote slides (primary `.quote` +
   `.reveal-block.unpack`/`.argument`/`.historical` fragments + `.takehome`),
   interleaved with image slides for objects, manuscripts, places, or events
   the quotes reference. See Part One of `annales-longue-duree`: the founding
   editorial, then Bloch and Febvre. (A scene-setting image is different from
   a portrait and can lead — the prison-camp slide opening Part Two of that
   deck sets up the book written in it.)
4. **A discussion pair at the end of each part** — a question slide, then a
   separate answer slide. See below; this is where the class talks, and it
   replaces parking every question in a list at the end.
5. **Comparison**, if the session pairs two people/texts — a `.parallel`
   slide asking what actually separates them, not just what's different.
6. **The arc of the lecture, looking back** — a `.cards` grid, one card per
   part, each with a number and date or source in the `.num` line, a short
   headline, and a sentence on what that part established, drawn especially
   from the answer slides. This slide is the recap: the shape of the whole
   hour, and where each conclusion came from, in one screen.
7. **The take home** — the whole day in one headline, then at most three
   supporting points as `.reveal-block` fragments, the last one a
   `.takehome` carrying the cost or the catch. Don't put the lecture's
   outline on this slide; the arc slide has just done that.
8. **Closing** — what comes next, and/or a closing discussion question, but
   only if the question genuinely needs the whole hour behind it: synthesis
   across both writers, or one that reopens the take-home. A `ul.questions`
   list of everything from `schedule.md` is not that; distribute those
   instead.

**The arc and the take home belong at the end, not the front.** An earlier
version of this guide opened every deck with the pair — the day's conclusion
in one sentence, then the roadmap — so that students knew where they were
going. It doesn't survive contact with a class. Both slides are abstractions
about a book nobody has met yet: the take-home sentence asserts a conclusion
the room has no evidence for, and the roadmap names three parts that mean
nothing until they have happened. Step through the history first and the same
two slides do real work at the end — the arc reads as *here is what we just
did*, and the take home lands as a conclusion rather than a claim. The front
of the deck still orients: that is what the cold open, the title slide and a
framing question are for. See `annales-longue-duree`, which ends arc → take
home → what comes next; `enlightenment-progress-2` already ran this way.
Decks built before this (`enlightenment-progress`, `marx-structural-history`,
`review-weeks-2-4`, `scientific-history`) still open with the pair and are not
the model.

A deck covering two sessions in one week (e.g. `divine-power-and-statecraft`,
which does 3.1 and 3.2) adds a `Part one · 3.1` / `Part three · 3.2` transition
slide between the two halves and a closing arc slide that spans both.

## Bird's-eye slides

A deck of close readings has a hole in the middle of it. Each quote slide is
excellent at the passage in front of it and says nothing about the hour it
belongs to; `.cards`, `.parallel` and `.flow` are all bounded by the deck.
Students can follow every slide and still not be able to say what the day
argued, or why this week follows the last one. Three slide types hold the
levels above the passage. Each answers a different question, and a deck that
reaches for all three without needing them has just built a second lecture out
of signposts.

**A transition needs a sentence, not a diagram.** A `.thread` class once lived
here: a rail of the session's movements with the current one lit, on its own
slide at each part boundary. It was cut. The rail was built from flex segments
whose `border-top` was supposed to read as one continuous line, but the nodes
wrapped to different heights and `align-items: center` then staggered the
borders, so it rendered as four disconnected dashes at four different heights —
and unvisited nodes were set in the border colour, which is all but invisible
on this background. Under all that it was also redundant: the rail said in
unreadable 0.4em mono what the headline above it had just said in full.

What was worth keeping was never the diagram. It was the one sentence naming
why the story moved — "the program was a room, not a thesis; the thesis
arrives now, from five years in a prison camp." That belongs in the part's
opening slide, as a `.detail` line under the headline, not on a slide of its
own. A deck whose parts each begin by saying what the last part left unfinished
has the narrative arc; it does not need furniture to prove it.

**`.throughline` — today's place in the course.** One question the course
keeps asking, with the answers so far: `.answer.past` for weeks already
settled, `.answer.now` for today, `.answer.next` dashed, because next week is a
promise and not yet a claim. It goes right after the title, and it is the one
orientation slide that earns a place at the front, because it is concrete —
names and answers, not an abstract of the argument to come. The value is in
recurrence: the same question returns every week with one more answer filled
in, so write the question once for the course and change only the nodes. In
`making-history` it is "What makes history happen?" and the answers run Ranke,
Marx, Braudel, Thompson.

**Don't draw an axis you are not going to scale.** A `.chronology` class once
lived here: two rows of dates, when each text was written against the period it
is about. It was cut, and the reason generalizes. The marks were evenly spaced
by CSS, so the slide drew 81 years and 9 years at the same width, under a rule
line with a tick over every mark. The ticks promise proportion; equal spacing
delivers a list. A chart that lies is worse than the list it is pretending not
to be, because students read the spacing before they read the labels.

Two tests before drawing anything with an axis on it. Does the position of a
mark mean something, and would a reader be wrong to assume it does? And can the
rows share one scale — stacking 1824–1958 above antiquity–1950 implies a common
axis that cannot exist. Where the answer is no, the honest form is a
`.parallel` comparison or a `.cards` grid: same content, no false promise. The
idea behind that slide was sound — a text's writing date and its subject period
are different things, and students collapse them — but it is a comparison, not
a measurement, and it should be built as one.

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
takeaways are the raw material for the closing arc slide's cards.

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

Public domain, CC0, or CC BY/BY-SA/BY-NC by default — check the license on the
Wikimedia Commons file page (or via the API) before using anything. Commons is
the first place to look, not the only one: institutional archives, library
digitisations and a publisher's own pages often hold better copies, and some
subjects are not on Commons at all.

**Fair use is available where nothing free exists, for a named reason.** These
are non-commercial teaching decks, and a low-resolution image shown for
identification and commentary is a normal classroom use. It is a fallback, not
a shortcut: take it only after looking, prefer an institutional or biographical
source over a stock agency (taking from a licensing agency is the use that
weighs hardest against fair use), keep the copy small, and write down in
`images/README.md` what you looked for, what you found, and why the use is
fair. Record the decision in `ISSUES.md` too, so a later pass doesn't delete
the file as unlicensed. The Braudel portrait in `annales-longue-duree` is the
worked example: he died in 1985, every free candidate is under 450px, and the
alternative was leaving the deck's central figure the only person in it without
a face. CC BY and
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

Run the word check first — `scripts/slide-words.py <deck>/index.md`. It is the
cheapest of these passes and the one whose failures are invisible in a browser,
because an over-long caption looks fine on screen and still sounds wrong in the
room.

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
- **Cross-slide integrity.** The framing question at the front, the closing
  arc slide and the take home have to describe the same lecture: the arc
  slide's cards match the parts that actually exist and carry the conclusions
  the answer slides actually reached, and the take home answers the question
  the deck opened with. Names, dates, spellings, and citation formats
  consistent slide to slide; forward references to other weeks accurate; no
  promise made early that the deck never keeps. Check the punchy framing line
  on the title or take-home slide against the biographical slides especially —
  it gets written first, before the details that can flatly contradict it
  ("two men in Berlin," when one of them was teaching in Frankfurt an der
  Oder).

Work the findings before publishing. Verify each one against the source
yourself — a cold reader will sometimes flag a correct claim it lacks the
context for, and being confidently wrong about a date is as easy for the
reviewer as for the author. Fix what's real. Anything you decide to keep goes
in `ISSUES.md` as a deliberate deviation with the reason, so the next reviewer
does not raise it again — not into the deck, and not left only in a commit
message nobody will read.

Link the new deck from the course's `schedule.md` under the session it
belongs to, matching the existing `[Slides of ...](slides/<slug>/)` phrasing.

# Open issues — Gender: A Useful Category (6.2)

Contributor notes, excluded from the build. Deliberate deviations are recorded
here so a later review does not raise them again.

## The slide contract this deck is built on

**One idea per slide, stated in the headline, with one piece of evidence under
it.** No fragment chains, no `.reveal-block` unpacking a quotation, no
`.takehome` restating what the headline already said. The headline *is* the
takeaway; the quotation is the evidence for it; the slide stops.

This is a deliberate departure from the model structure in
`courses/SLIDE-STYLE.md` §"Structure of a session deck", which prescribes
"1–4 quote slides (primary `.quote` + `.reveal-block.unpack`/`.argument`/
`.historical` fragments + `.takehome`)". An earlier draft of this deck
followed that form and ran 35 slides, each carrying two or three things to
remember; the author's judgement was that it read as repetitive and long, and
that a student could not say afterwards what any one slide had been *for*.
The rebuild is 27 slides, of which 23 carry a headline and one element.

Two exceptions, both deliberate:

- **The one discussion slide keeps the three-beat form** (topic as
  `.main-point`, one `.question` fragment, one `.takehome` fragment). That is
  the form `SLIDE-STYLE.md` prescribes for discussions, and it is one exchange
  rather than three takeaways.
- **Two slides carry a `.cards` grid** (the four elements, and the closing
  arc). A grid of four parallel items is one idea with four instances, not
  four ideas.

**If you extend this deck, extend it in this form.** Adding a `.reveal-block`
and a `.takehome` to a slide that currently has a quotation puts it straight
back where it started.

## Open questions

**The deck's central quotation sits three pages outside the assigned range,
and the fix is a change to `schedule.md`, not to the deck.** The session
assigns Scott "read first 12 pp.", which is pp. 1053–1064, and tells students
to "focus on her core definition." The definition is on **p. 1067**, and the
four elements that unpack it are on pp. 1067–68. Part two now gives the two
halves of that definition a slide each, so three of its slides are built on
pages the reading stops short of.

It is not a fabrication problem — Green and Troup quote the definition on
their p. 253, which *is* assigned, and the slide cites both places — but the
syllabus promises something the reading does not deliver. The cheapest fix is
to extend the Scott assignment to **about p. 1070** (fifteen pages), which
buys the definition, the four elements and the "primary field within which
power is articulated" line, and stops before the extended political examples.
Until that is decided, whoever delivers part two should say so at the
definition slides.

**The syllabus discussion question "What does it mean that gender is
performed?" is Butler, not Scott.** Performativity is *Gender Trouble* (1990),
four years after this article; Scott's vocabulary is construction,
signification and discourse. The deck does not use the word "performed"
anywhere and cannot answer that question without putting it in her mouth.
Either rewrite the question or add a Butler reading.

**Every woman quoted in the deck now has her face beside the quotation,
except Joan Kelly.** Fair use for classroom slides is authorised here, so the
constraint is availability and identification, not permission. Found and used:
Gerda Lerner (UW–Madison Archives, CC BY 3.0), bell hooks (Commons), and Alice
Clark (LSE Library, fair use, paired with her 1919 title page). Joan Scott has
her own portrait slide.

**Joan Kelly is the one gap.** Searched without success on 2026-09-24:
Wikimedia Commons (a search for "Joan Kelly" returns a Missouri politician;
"Joan Kelly-Gadol" returns Alberti, because her essay is about him), her
Wikipedia article (imageless, and with no `pageimage`), Openverse, the AHA and
CCWH pages for the Joan Kelly Memorial Prize, Sarah Lawrence's women's history
pages, the CUNY Digital History Archive, the jacket of *Women, History and
Theory* (typographic), the Internet Archive scan of that book
(lending-restricted, page images return 403), and Harvard's digital
collections, which hold the **Papers of Joan Kelly, 1973–1984, Schlesinger
Library MC 525** but surface no digitized portrait. A labeled CC0 montage of
women's-history authors on Commons ("Autoras de História das Mulheres")
includes Lerner and Scott but not Kelly.

**That collection is where to look next**, along with a CCNY faculty
photograph or yearbook — she was on the history faculty there from 1956 until
her death in 1982 — or a memorial notice by a colleague. Until then she is
identified by a `.detail` line under the headline of her own slide and by her
dates in the eyebrow. Do not use an image that is not captioned, at its
source, as the historian Joan Kelly (1928–1982): the one error worse than no
face on a teaching slide is the wrong person's.

## Deliberate deviations

**Part one is a numbered sequence of single ideas, not a narrative with
sub-arguments.** Green and Troup's pp. 253–260 contain roughly eighteen
distinct beats. The deck takes eight of them, in their order: the complaint;
why a history matters politically; that the complaint predates the movement;
the sex/gender distinction; the consequence that gender has a history; and
then the three things the field actually did — recover the women, break the
periods, set gender beside class — followed by the objection that the women
being recovered were white and middle class, and the endpoint that gender is
present where no women are.

Deliberately left out, and why: the public/private and nature/culture
dichotomies (pp. 255–56), which Green and Troup themselves report historians
found "restrictive"; Maynard on the "Big Three" (p. 256), which is a quarrel
about labelling theory rather than about history; the psychoanalytic strand
and Sally Alexander (p. 257); Green and Troup's own summary of Scott's later
discursive method (pp. 257–58), because part two has her in her own words; and
Bennett on continuity and change (pp. 258–59), which is the strongest
candidate for putting back if the session ever runs short.

**Margaret Wade Labarge's name was dropped from the "recovering women"
slide.** She appeared once, as Green and Troup's single example of the first
approach, and never came back — which `courses/SLIDE-STYLE.md` calls citation
work rather than teaching. No photograph of her could be found either (nothing
on Commons, nothing on her Wikipedia article, nothing on the Canadian Society
of Medievalists page named after her, nothing in the Globe and Mail obituary),
so keeping her would have left a named, quoted woman with no face on a slide
whose whole subject is women being made visible. The slide now quotes Green and
Troup's own sentence about what historians did instead, which says the same
thing without the name.

**Four things from the longer draft were cut in the rebuild, not lost.** Each
was good and each was a second idea on a slide that already had one: Alice
Clark's 1919 preface on declaring one's bias (which also came from outside the
assigned reading); Bonald's 1816 divorce law as a second worked example beside
Burke; Scott's dismantling of the three available theories — patriarchy,
Marxist feminism, psychoanalysis — which cost four slides to make one point
already carried by "a topic changes nothing"; and the pairing of Scott's
"empty and overflowing categories" with Kathleen Canning's objection to
decentring the female subject. The last is the one worth restoring first if
the session wants a harder ending.

**Three slides use `.with-figure` outside a discussion slide.** The theme
documents it as "a discussion-slide body variant", but it is a generic
two-column layout — a narrow image column beside the body — and it is the
right form for a woman who is quoted once rather than taught for a whole
slide: her face sits beside her words without spending a slide on her. Lerner
and hooks are set this way. Alice Clark gets a `figure.pair` instead, because
her portrait and her 1919 title page answer one question together.

**Part one has no discussion slide.** It was "Whose Renaissance" — Kelly kept
the word and denied that women had one; what would she have lost by inventing
a different name? It was cut at the author's instruction because a later
activity covers the same ground, not because the question was weak. Part two
keeps its discussion slide ("Gender without women"), which is the one that
needs the whole session behind it.

**The 1970 Washington march photograph was cut.** It showed that a movement
existed, which is what the slide beside it already said, and it read as a
stumble in the sequence — an 1919 quotation, then a photograph captioned 26
August 1970, then a slide about the 1960s. The cost is that part one now runs
several content slides between image breaks; a Kelly portrait would fix that
exactly, which is why the missing portrait above matters. Don't solve it by
putting the march back.

**The throughline drops Week 4.** `history-from-below` ran Ranke, Marx and
Braudel, Thompson, Scott. This one runs Marx and Braudel, Thompson, Scott,
Ginzburg — a sliding window of four, with the wording of the two repeated
nodes left word-for-word identical so the slide reads as the same slide
returning.

**The cold open is the Congress of Berlin, and the point is the absence.**
An earlier version paired Vigée Le Brun's *Marie-Antoinette and her Children*
(1787) with Caresme's print of the Parisian women at Versailles (1789) — a
queen made into a mother against market women made into heroines, two years
apart, both arguing about who should rule. It had a controlled variable and it
paid off at the Burke slide. It was still wrong, and the author's objection is
the right one: **two pictures of women depicted differently only show that
women have been depicted differently**, which is true of any two images from
any century. The pair asserted the connection to power instead of showing it,
and the reading a student reaches first is the banal one.

The room of men at the Reich Chancellery defeats that reading, because there is
no woman in it to be depicted at all. "This is a picture about gender" is
genuinely counterintuitive, the question under it is not answerable from the
image, and it is the session's own thesis rather than a warm-up for it. It is
also the deck's best payoff, so it now runs as a bookend: full-bleed at the
front as the puzzle, and back in the `.with-figure` column of the part-two
discussion once Scott has supplied the answer — "High politics itself is a
gendered concept … precisely in its exclusion of women from its work"
(p. 1073).

`marie-antoinette-children-1787.jpg` and `femmes-parisiennes-1789.jpg` were
deleted from `images/`. Both were good and both are re-fetchable: the Vigée Le
Brun from the Google Art Project via Commons, the Caresme from Gallica via
Commons ("Bravoure des femmes parisiennes à la journée du 5 octobre 1789.jpg").
If the Caresme ever comes back, note that its lettered date (5 October 1789)
and Gallica's identification of the scene (an incident of the 6th) disagree,
and that the deck's practice was to give the sheet's own date and not to name
anyone in the image. The Burke caricature keeps Marie-Antoinette in the deck,
which is where she does work.

## A contradiction the author caught after the rebuild

The "gender and class" slide and the bell hooks slide were flatly opposed, and
were presented as two neutral ideas in a row rather than as a claim and its
rebuttal. The first said oppression was "common to women of all ranks despite
the differences in their lives"; the second said race and class differences
"take precedence over the common experience women share." A student would have
left with two contradictory sentences and no idea which one the field ended up
believing.

Two things had gone wrong. The class slide quoted Green and Troup's reporting
clause — "it *seemed* that…" — as though it were their conclusion, and it
stopped before the half that matters: "And this oppression could be attributed
to men, rather than to the specific economic system under which the women
lived" (pp. 254–55). That is the claim that pushed the field toward patriarchy
theory, and it is what hooks is answering.

And the hooks slide did not say what she was *doing*. She is not adding race
and class as extra layers to an agreed picture, and she is not disagreeing
with feminism; she is attacking a premise held by a largely white, middle-class
North American scholarship — the premise "that all women were essentially the
same, and, that in effect, they shared the concerns of white middle-class
women" — which Green and Troup themselves call "manifestly incorrect" and
report as "vociferously criticized from the late 1970s by women of colour"
(p. 255).

Both headlines now carry the relationship: **"Gender seemed to cut across
class, and that is what broke the class analysis"**, then **"Women of color
showed that the shared experience was white and middle class."** Claim, then
rebuttal. Don't restore either headline to a neutral statement of its own
content; the sequence is the teaching.

## What the fresh-context review caught

A fresh-context agent reviewed the longer draft on 2026-09-24 against both
cached OCR packets and the image files. Its substantive findings were verified
against the sources and worked; the ones that bear on slides still in the deck
are:

- The Burke caricature is **one day** after the book, not "days after" — the
  plate reads 2 November 1790, Burke's *Reflections* was published 1 November.
- The Vigée Le Brun painting was described wrongly — the dauphin lifts the
  cradle's drape and points into it, his arm is not around it, and the drape is
  dark green, not black. That slide has since been cut, but the finding is
  worth keeping: Wikimedia's own French description of that painting carries
  both errors, so don't take a Commons description as a description of the
  canvas.
- hooks's book is *Feminist Theory: From Margin to Center*; Green and Troup's
  endnote misspells it.
- The occasion of Scott's paper is that it was "first prepared for delivery"
  at the AHA (p. 1053, unnumbered note); the note says nothing about the *AHR*
  printing, so the caption no longer cites it for that.
- Every Scott and Green and Troup page cite in the draft was verified against
  the printed-page markers rather than recognized, including all the
  quotes-of-quotes where the slide has to name both ends.

Findings that applied only to slides the rebuild removed (the three-theories
cards, the Godelier attribution, the Clark truncation, Bonald's opening words,
the take-home's overreach) are moot, but they are the reason those slides
would need care if they are ever restored.

**The rebuilt structure has not itself been reviewed cold.** The quotations in
it are either carried over from the reviewed draft or were checked against
`~/Dropbox/courses/making-history/.research-packets/green-troup-gender.ocr.txt`
when they were added (Labarge p. 254, the gender-and-class sentence p. 254,
the Jordan and Weedon passage p. 253, the sex/gender distinction p. 253). What
has not had a cold reader is the new sequence: whether part one's eight ideas
are the right eight, and whether the arc slide still describes the lecture
that now exists. Run one before this is taught.

## Checks run

**Word budgets.** `scripts/slide-words.py` exits clean. Four containers sit
over target and under the stop: three captions at 41–47 words (target 40) and
one discussion takehome at 31 (target 30).

**Overflow.** Every slide and every fragment step was measured in headless
Chrome, comparing the bottom of the deepest visible descendant against the
bottom of the `.reveal .slides` box. No content slide overflows. The only
flags are the four image slides at 720–721px, which is what
`history-from-below` reports on its own image slides — that number is the
figure filling its frame, not a defect. Calibrate any future run the same way,
against a published deck, before believing a number.

**Headlines.** Five of twenty-four run to three lines, against five of
twenty-five in `history-from-below`.

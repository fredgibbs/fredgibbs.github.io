# Open issues — The 1619 Project, Part 1 (Week 12.1)

Contributor notes, excluded from the build. Deliberate deviations are recorded
here so a later review does not raise them again.

## What this deck is

Hannah-Jones's essay, and nothing else. Until 2026-11-02 this folder held one
deck for both Week 12 sessions; it was split that day at the author's
direction:

> i think i want to split the slide deck into two, one for tuesday and one for
> thursday. the first should cover hannah-jones original essay, and the second
> the pros and cons. i don't think we need to be as explcit by author, but just
> relate very clearly the main pros and cons arguments that were made. it would
> also be useful to highlight the arugments from the 5 historians who wrote the
> letter about it. i neex to provide clarity and balance to students so they
> feel different perspectives are represented.

Thursday's deck is `../1619-project-debate/`, with its own `ISSUES.md`. The
combined deck's notes on the debate (Serwer, Friedersdorf, the letter, the
March 2020 editor's note) moved there.

**Order.** Title; Pyle, 1901; throughline; portrait; the essay as a thing (the
title-page summary and the issue). Part one, the founding: the flag, what
enslaved people built, the Statue of Freedom, 1619 beside 1776, ideal and a
lie, Robert Hemings, the Dunlap broadside, the Revolution claim, the
Constitution, discussion. Part two, the perfecters: the claim, Lincoln in
August 1862, Reconstruction, the 1872 lithograph, the collapse after 1877 and
the "DNA" line, Isaac Woodard, "fought back alone," the ending, discussion.
Then the arc, the take home, and next time.

The essay's own order runs flag, 1619, labor, "perfecters," ideal and a lie,
1619 beside 1776, Jefferson and Hemings, the Revolution, the Constitution,
Dred Scott, Lincoln, Reconstruction, the Nadir, Woodard, the civil rights
movement, culture, the flag assignment. The deck follows it except that it
holds the "perfecters" sentence (p. 16) back to open part two, which is the
argument it introduces.

## Sources

- **The essay**: the Pulitzer Center PDF the schedule links
  (`the_idea_of_america_full_essay.pdf`, 13 pages, PDF created 2020-03-13;
  the Zotero copy at `storage/7VMYZDBD/` has identical text). It is the print
  layout and keeps the Magazine's page numbers, which the deck cites: printed
  folio = PDF page + 13. PDF p. 1 is the unnumbered title page (p. 14), p. 2 is
  full-page artwork (p. 15), the body runs pp. 16–26, and pp. 23 and 25 are
  advertisements. Page 22 also carries a Tiya Miles sidebar, "Chained
  Migration," which the deck does not use. The text layer of p. 26 comes out
  with its columns out of order; the quotations from it were located by string
  and checked against the page.
- **The title-page sentences** ("Our founding ideals of liberty and equality
  were false when they were written...") are the print display text on p. 14,
  checked against a page image. They may be an editor's display copy rather
  than Hannah-Jones's prose; the cite says "the title page" so the slide does
  not claim more.

## Facts that rest on something other than the essay

- **The issue** ("ten essays, with poems and fiction"; the Pulitzer Center
  school materials) is from the Times's note at the foot of "We Respond to the
  Historians Who Critiqued The 1619 Project" (December 20, 2019), read in the
  Princeton compilation, `~/Dropbox/courses/making-history/The1619Project_ResponsesAndDefenses.pdf`, PDF p. 150.
- **Hannah-Jones's bio**: "b. 1976" and the 2020 Pulitzer Prize for Commentary
  are from web search results, not the readings. "Raised in Iowa" is the essay
  (p. 16). "Whose reporting had centered on school segregation" paraphrases
  Silverstein's reply ("primarily in her work on educational segregation").
  "Conceived the 1619 Project" is Serwer's phrase.
- **The Statue of Freedom** "raised to the top of the dome in 1863": the
  Commons description, and see `images/README.md`.
- **Woodard's caption**: "In February" is the essay's own caption to its p. 19
  photograph; his mother's name, Eliza, and the July 1946 date are from the
  Commons file. "Police had beaten him blind hours after his Army discharge"
  paraphrases pp. 19 and 21 ("4½ hours after his military discharge").

## Deliberate choices

- **The title slide has no `Background:` reading.** The session has one
  reading. `deck-check.sh` reports "narrator: (none found)", which is correct.
- **Lincoln is quoted through the essay** ("Abraham Lincoln, August 14, 1862,
  quoted in Hannah-Jones") and gets no portrait. The slide is about her use of
  him, which is what Thursday's letter disputes.
- **Names that appear once**: Robert Hemings (the subject of his slide),
  David Waldstreicher (the source of her clause count, and the essay's own
  attribution), Thomas Crawford and John Dunlap (makers of what is shown), and
  Pyle. Each is the maker or subject of the thing on screen.
- **Discussion takehomes are hedged readings, not the essay's.** Part one's
  ("Probably the clauses...") separates evidence that slavery was present at the
  founding from evidence that it was central; it anticipates the critics without
  naming them. Part two's turns on the first person. Both are meant to be argued
  with.
- **The take home's catch** ("reading every period through 1619... lets
  critics test each period's claim on its own") is the bridge to Thursday.
- **Quotations keep the source's lowercase "black."** The deck's own voice
  says "Black Americans."
- **The Revolution quotation is the August 2019 wording**, and its cite says
  "as printed in August 2019." The March 2020 change is on Thursday.
- **No "compare" blocks and no course cross-references.** The discussion post
  asks students to find the connections themselves. The schedule's third 12.1
  question (Trouillot) is not on a slide for the same reason.
- **Parts do not open with a `.detail` line** (guide, "Structure," item 4).
  Each part's first slide is a quote slide, where a `.detail` above the
  quotation fails the order check; the eyebrow names the part.
- **The essay's date.** The schedule says August 19, 2019; the PDF's masthead
  says August 18 (the Magazine's issue date; the web version ran August 14).
  The deck uses August 18.

## Open: the discussion-post page still names Lowenthal

`1619-discussion-post.md` says (line 78) "You'll need all three readings —
Hannah-Jones, Serwer, and Lowenthal" and (line 66, the rubric) "Lowenthal
alongside Ranke." `schedule.md` lists Hannah-Jones, Serwer and Friedersdorf.
Neither deck uses Lowenthal. The post page needs those two lines brought into
line with the schedule.

## Open: the post page and the schedule ask for different things

`1619-discussion-post.md` grades "pros and cons … genuinely weighed rather than
picking a side and defending it." The 12.1 alert in `schedule.md` tells students
to "think about which side of the debate you find more convincing and why."
Thursday's writing slide asks for both, in order: the strongest argument on each
side, then where they come down.

## Checks run (2026-11-02, after the split)

- `scripts/slide-words.py`: every container within its target.
- `scripts/deck-check.sh making-history/1619-project`: 27 slides, 0 fail,
  0 warn. An early run failed slide 9 for "1776" before an introduction: the
  checker took the year in the Dunlap caption's title ("…Philadelphia, July
  1776") as a surname. The title now puts a `·` before the place and date.
- Every slide looked at in headless Chrome at 960×700 with fragments forced
  visible, after each round.

## Fresh-context review (2026-11-02)

A subagent with no memory of the drafting reviewed both Week 12 decks against
the source texts. For this deck it found **no wrong quotation and no wrong
page**. Disposition of its findings here (Thursday's are in that deck's
`ISSUES.md`):

| Finding | Disposition |
|---|---|
| Throughline said she "moves the founding to 1619," against the slide's "as important as 1776" | **Fixed.** "sets 1619 beside 1776" |
| "The issue" block said the essay runs from p. 16; the title slide and first cite say p. 14 | **Fixed.** "pp. 14–26" |
| Arc card 02 said pp. 19–26, but part two opens on p. 16 | **Fixed.** "pp. 16, 20–26" |
| Arc card 01 softened "one of the primary reasons" to "among the reasons" | **Fixed.** The essay's wording |
| Part one's discussion left out the Revolution claim, Thursday's main dispute | **Fixed.** The question includes "the calls in London"; the takehome says the claim needs evidence of motive |
| Reconstruction headline had an explanatory tail | **Fixed.** "Reconstruction is her main evidence that Black Americans perfected the democracy" |
| Arc headline was a matched triple | **Fixed.** The third element is broken: "and the flag her father flew" |
| No part opens with a `.detail` | **Kept.** See "Deliberate choices" |

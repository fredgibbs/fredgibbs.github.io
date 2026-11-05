# Open issues — The 1619 Project quiz (Week 12.2)

Contributor notes, excluded from the build. Deliberate deviations are recorded
here so a later review does not raise them again.

## What this deck is

A review of a printed true/false quiz, built 2026-11-05. Students take the
quiz, then the deck goes through it one question per slide. The author's
request: "students will take the quiz, then we can go over the slides with each
question and the T / F arguments get revealed." Every statement is meant to be
defensible both ways; students pick one and argue it. The 12.2 deck
(`../1619-project-debate/`) stays as it is; this one sits beside it.

The quiz is a Word file outside the repo:
`~/Dropbox/courses/making-history/1619-project-quiz.docx`. **Its thirteen
statements must match the `.question` lines here word for word.** Change one,
change both.

**Order.** Title, then the thirteen question slides and nothing else. Part
one, the essay's claims (questions 1–5: the Revolution, the founding ideals,
Lincoln, "alone," "DNA"). Part two, the fight (6–10: fact or interpretation,
corrections, who writes history, the founding date, what schools taught).
Part three, the course (11–13: Carr, Trouillot, Jenkins), which ends the deck.
The author cut the arc, take home and closing slides on 2026-11-05 for length
("i need fewer"), then cut every image slide, the part openers, the three
discussion slides and the title slide's reading list: "streamlined to
discussing the t/f questions." The review rows and notes below about those
slides describe text that no longer exists. `image_slides: true` is dropped
from the front matter, and `images/` is no longer referenced by the deck.

## The question slide is a new arrangement

Each question slide is a discussion slide whose body is a `.parallel`: eyebrow,
a four- or five-word `.main-point` topic, the quiz statement as a `.question`
(shown at once, not a fragment, since students have just answered it), a
**True** track (fragment 1), a **False** track (fragment 2), and a `.takehome`
(fragment 3) saying what the choice turns on. The guide's slide types do not
list this combination. The author asked for this structure; it should be added
to `SLIDE-STYLE.md` ("Discussion slides") if it is kept.

Track headings put the side first and the source second ("True · the Times's
reply"). The guide asks for the writer and work in a track heading, which this
does; the side is the extra word.

## How balance is kept

- **Each statement leans by its wording, on purpose.** "Partly" (1) leans
  true; "at heart" (3) and "as much as" (8) lean false; the rest are close to
  even. The takehomes name the word that decides it rather than a verdict.
- **Each side gets its strongest source from the readings,** with page or
  speaker. Where Serwer, the narrator, gives a verdict, it is reported in the
  direction he gives it (critics "on firm ground" on the Revolution; "largely
  alone" "more than defensible").
- **Question 5 uses the essay's own sentence** ("runs in the very DNA of this
  country," p. 21), at the author's direction: the metaphor is the
  controversial part, not a claim that racism is constant.

## The course questions (11–13)

The author asked for "a couple questions about historical truth and so on that
draw from the whole course." Three were written, one each for Week 1 (Carr),
Week 9 (Trouillot) and Week 10 (Jenkins). Each takes a reading the course has
already met and asks which side of the 1619 fight it supports; each reading
turns out to support both. Cut one if three is too many; the quiz is one page
either way.

## Sources

- **The four 1619 readings**: as in `../1619-project/ISSUES.md` and
  `../1619-project-debate/ISSUES.md`. Every quotation from them was checked by
  string against the PDFs on 2026-11-05 (the Serwer text layer drops "Th" and
  "fi" ligatures; matches were made with those removed).
- **Carr**: OCR cached 2026-11-05 at
  `~/Dropbox/courses/making-history/.research-packets/carr-historian-and-facts.ocr.txt`.
  The quotations on pp. 11, 27 and 28 were checked against the page images.
  The OCR truncates right-hand columns at the gutter, so never quote from it
  without the image.
- **Trouillot**: text layer cached 2026-11-05 at
  `.research-packets/trouillot-silencing-ch1.txt`. The PDF is two-page spreads
  with folios at the foot, so the text layer puts each spread's numbers above
  the wrong block. "Four crucial moments" is p. 26 and "bundle of silences" is
  p. 27, checked against PDF page 19.
- **Jenkins**: the existing cache, `.research-packets/jenkins-rethinking-history-ch3.txt`
  (Routledge Classics, 2003). Both quotations are on p. 82.

## Facts that rest on something other than the readings

- **The March 2020 revision** (question 1 takehome; take home): paraphrased,
  not quoted, for the reason in `../1619-project-debate/ISSUES.md`.

## Deliberate choices

- **No throughline and no `.citation-note`**, per the review-deck rule. The
  editions are in the source list and each track's heading.
- **No portraits.** Everyone quoted has been introduced in an earlier deck
  (12.1, 12.2, Weeks 1, 9, 10); this is a review. Du Bois's portrait slide is
  an image break before question 8, not an introduction.
- **Single-appearance names** (Gordon Wood, James Oakes, Wilfred McClay,
  Michael Guasco) stay because each is the speaker of the words quoted, as in
  the 12.2 deck.
- **The closing slide** points at the discussion post and Week 13 without the
  12.2 deck's writing questions, which would repeat them.

## Checks run (2026-11-05)

- `scripts/slide-words.py`: every container within its target.
- `scripts/deck-check.sh making-history/1619-project-quiz`: 28 slides,
  0 fail, 0 warn, after the title slide's reading list and headline were
  shortened (first runs: 685px, then 648px).
- Every slide screenshotted at 960×700 in a fresh headless profile with all
  fragments shown, before and after the review fixes.

## Revisions after the author's read (2026-11-05)

- **Question 12 (Trouillot) rewritten.** The author found "The 1619 Project
  broke a silence more than it created one" too abstract and its references
  (Trouillot's pages on both sides, Guasco through Friedersdorf) too
  complicated. Now: "The 1619 Project leaves out as much as the story it
  replaced." One direct source per side (Friedersdorf on Native Americans;
  the essay on what enslaved people built, p. 16), with Trouillot's "bundle of
  silences" (p. 27) only in the takehome. Keep references this plain.
- **Question 10 reworded.** The author asked how "The 1619 Project told
  Americans a story they had not been taught" could be false; as written it
  barely could, since full libraries are not teaching. Now: "The story the
  1619 Project told was new." The False side gains the essay's own reliance
  on a historian (Waldstreicher, p. 18).
- The Word quiz was changed to match both.

## Fresh-context review (2026-11-05)

A subagent with no memory of the drafting checked every quotation against the
sources (Carr against page images) and found **no wrong quotation, speaker or
page**. Its findings were about balance. Each was verified against the source
before fixing. Disposition:

| Finding | Disposition |
|---|---|
| Take home "What the evidence settled" omitted "I do still back up that claim" and contradicted the Q1 takehome ("partly" decides it) | **Fixed.** Now "What the evidence moved": the sentence's reach, with her defense quoted |
| Part three discussion: "narrowed when its evidence was challenged"; the reply calls the claim "grounded in the historical record" | **Fixed.** "Narrowed to some colonists once its scope was challenged" |
| Arc headline "Most of the fight was over judgment, not fact" answered Q6 for the False side; Q6's takehome leaned the same way | **Fixed.** Headline: "Each statement turned on how you read one word"; Q6 takehome credits the letter and the reply each with a point |
| Q3 lacked the reply's own concession, the strongest True evidence ("at the end of his life ... real equality"); letter quote cut short; "one Lincoln ... two" epigram | **Fixed.** Both added to the True track; takehome rewritten without the pairing |
| Q5 takehome adopted Oakes's reading ("DNA is inherited and fixed") in the deck's voice; True track's Serwer line described the objection, not the claim | **Fixed.** Takehome attributes each reading; True track uses the essay's p. 21 evidence |
| Q8 takehome misstated Wilentz's lesson; "both sides cite" overstated | **Fixed.** Serwer's two readings of the Dunning School, in his words |
| Q7 takehome ruled on the premise | **Fixed.** It notes the premise is Silverstein's concession |
| Arc card 3: Jenkins does not arm both sides on screen | **Fixed.** "Jenkins backs the project's side, and Carr answers him"; Q13 verbs made even |
| Q11 Carr p. 28 cut at "relevant." | **Fixed.** Full sentence, including the clause tying relevance to the interpretation |
| Q10: "through cultural osmosis" dropped; False track thin | **Fixed.** Restored; McClay's framing sentence added |
| Q12: one of "four crucial moments" presented as the only one; Guasco predates the project | **Fixed.** Both stated |
| Q2: "the essay's own" overclaims display copy | **Fixed.** "The display text on the essay's title page" |
| Part two discussion: "the critics and the Times" sweeps in Friedersdorf and McClay | **Fixed.** "The five historians and the project"; arc card 2 rewritten to cover all five questions |
| Track headings named one writer but quoted two | **Fixed** on every track that quotes two |
| Du Bois and Gettysburg alt text inaccurate | **Fixed.** Du Bois's is the 12.2 deck's; Gettysburg's describes the shrubs and field actually in the picture |
| `images/README.md` missing | Already written while the review ran |
| Q4 keeps one epigram ("count the centuries ... count the turning points") | **Kept** as part one's one epigram |
| Two quotes end mid-sentence with a period (Lincoln's "supremacists," McClay's "subject") | **Kept**: American punctuation, and nothing after the cut changes the sense |

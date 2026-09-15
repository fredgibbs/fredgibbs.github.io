# Open issues — Marx and the Motor of History (5.1)

Production notes for the instructor. **Nothing here belongs on a slide**: a
student does not need to know which scan misbehaved. Clear an item and delete
it.

Last reviewed: 2026-09-11, after a fresh-context review of the finished deck.
Rebuilt around a single through-line on 2026-09-12 — see item 6 before
restoring anything that looks missing.

---

## 1. `scripts/ocr-pdf.swift` silently truncates this reading

**Status:** open. A real bug in the shared script, not a problem with the deck.

`green-troup-marxist-historians.pdf` is a six-sheet scan of two-page spreads
with `Page rot: 90` set in the page dictionary. The script renders each page
via `page.bounds(for: .mediaBox)`, which **ignores rotation**, so it draws a
landscape page into a portrait bitmap and clips the entire right-hand printed
page of every spread. The first OCR pass returned pp. 33, 35, 37, 39, 41 cut
off mid-line — and nothing in the output says so. Every truncated line simply
ended early, which reads as a bad scan rather than a bug.

The cache was rebuilt instead with `pdftoppm`, which honours the rotation, and
each spread cropped into its two printed pages before OCR. The exact commands
are recorded at the head of
`~/Dropbox/courses/making-history/.research-packets/green-troup-marxist-historians.ocr.txt`.

**What to do:** fix the script to respect rotation — use `.cropBox` with the
page's `rotation` applied, or render through `pdftoppm` — before anyone OCRs
another scan with it. Until then, check any new OCR output for lines that end
early. Worth checking whether other course PDFs carry the same rotation flag.

---

## 2. Green and Troup misdate *The Eighteenth Brumaire*

**Status:** decided, not an error to fix. Recorded so it is not "corrected"
back.

On p. 36 the textbook introduces the "Men make their own history" passage as
"taken from *The Eighteenth Brumaire of Louis Bonaparte* (1859)". This was
verified against the page image — it is the textbook's own text, not an OCR
artefact. The work was written and published in **1852**; 1859 is the date of
*A Contribution to the Critique of Political Economy*, quoted one page earlier,
so it looks like a slip carried across from p. 35.

The Brumaire slide's eyebrow reads **1852**, and the quotation is still cited
to Green and Troup p. 36, where the words were checked. Do not change it to
match the textbook.

---

## 3. The *Manifesto* is cited by section, not by page

**Status:** decided. Disclosed on the title slide as a citation convention.

The assigned PDF (`optimized/Marx_CM_excerpts.pdf`) is the marxists.org
rendering of the 1888 Samuel Moore translation. Its own source note gives
*Marx/Engels Selected Works*, vol. 1 (Progress, 1969), pp. 98–137, but the PDF
does **not** reproduce that pagination — it carries its own page numbers
(Part I runs pp. 3–12). Citing "p. 5" would therefore point at nothing a
student could match to the printed edition, and citing the Progress pages
would be a locator nobody in the room can see.

Every *Manifesto* quotation is cited `Manifesto, Part I`, which is how the
schedule names the reading. Engels's class definitions are attributed to his
1888 note, which is where they appear. If the course ever adopts an edition
with stable pagination, these become page cites.

The grave-diggers quotation opens with an ellipsis at "its own grave-diggers"
on purpose: printings differ between "is its own grave-diggers" and "are its
own grave-diggers", and starting after the verb avoids asserting either.

---

## 4. Claims that do not come from the assigned readings

**Status:** open, low priority. All are standard reference-work claims, none
load-bearing for an argument; listed so a reviewer knows which were not
checked against a source in hand.

- **Reading Room:** Smirke's domed room opened 1857; Marx's reader's ticket
  dates from 1850, i.e. from the earlier rooms. The caption says he was "a
  reader since 1850" and worked in *this* room on *Capital*, which avoids
  implying seven years in a room not yet built. The often-repeated detail that
  he sat at desk G7 is **not** asserted — the British Library treats it as
  unverifiable, and it is deliberately absent.
- ***Capital* (1867) "cites the reports of Britain's factory inspectors page
  after page"** (Reading Room caption and notes, and the "provable?" answer
  slide). Standard — chapter 10, "The Working Day," is built largely on the
  Reports of the Inspectors of Factories and the Children's Employment
  Commission — but in neither reading. It is what makes the Reading Room do
  argumentative work after the Ranke slide, so it is worth a page reference to
  *Capital* if challenged.
- **Manchester's population "grew roughly fourfold"** in the first half of the
  century. Deliberately vague because the figure depends on whether the
  township, borough or conurbation is meant. Give exact numbers only with a
  boundary named. "The thousands tending machines" in the same notes slide is
  deliberately a floor, not an estimate.
- **Peterloo: "around eighteen people were killed."** The usual range is 15–19
  depending on which later deaths are counted.
- **Engels "sent at twenty-two" to Manchester.** Born November 1820, arrived
  late 1842.
- **Wyld credited to the Royal Collection**, per the Google Art Project record.
  The watercolour is often said to have been commissioned by Queen Victoria
  after her 1851 Manchester visit; that is plausible but unconfirmed, so the
  caption says only where it lives.
- **Marx's biography in his portrait caption** — law and philosophy, the Cologne
  newspaper, the censors. Accurate, but Green and Troup p. 34 supports only the
  itinerancy and the 1849 move to England, which is the only part the caption
  cites to them.
- **"real wages in Britain rose across the later nineteenth century"** (the
  "provable?" answer slide). Mainstream and not seriously disputed, but it is
  not from either assigned reading, and it is the evidentiary hinge of that
  block. Worth a citation if the slide is ever challenged.
- **"the world's first industrial city"** (Manchester caption). Standard,
  contestable, unsourced.
- **Engels wrote *The Condition of the Working Class* in Barmen**, between
  returning from Manchester in 1844 and March 1845; published Leipzig.
- **The motor diagram's sources.** Green and Troup supply *The German Ideology*
  "written in 1846" (p. 34; usually dated 1845–46) and the 1859 preface
  (p. 35). The four step names — production, classes, contradiction, the next
  stage — are the deck's own compression of pp. 34–36 and Part I, not a
  scheme either reading lays out in those words.
- **The Ranke quotation** comes from the 1824 introduction as quoted and
  verified in the 4.2 deck (`scientific-history`), not from this week's
  readings. Keep the two decks' wording identical.
- **Reading Room chronology.** The motor (1846–48) predates both Marx's reader's
  ticket (1850) and the domed room (1857), so the caption says he spent years
  there working a theory *already sketched in 1848* into *Capital*. Do not let
  the caption or the "provable?" discussion slide imply the evidence came first.
- **1848.** "Most of them led by liberals and nationalists" for the spring
  risings, Paris in June as the clear workers' rising, and Hungary and Venice
  surrendering in August 1849 are standard, not from either reading. An earlier
  draft said "workers rose across Europe," which a review flagged as mostly
  wrong.

---

## 5. Deliberate deviations — decided, not forgotten

Recorded so a future reviewer does not re-raise them.

- **Part three deliberately does not survey three historians.** Hill and
  Hobsbawm share one slide, which keeps them apart — Green and Troup say Hill "pays a great deal of attention to the world of ideas" and does not rest on "a very narrow economistic perspective" (p. 37), while Hobsbawm "remained closest to the economic determinism" (p. 39). Do not collapse them into "both read politics off the economy", and Thompson gets a single **foreshadow
  slide**, because **Week 6.1 assigns Thompson's preface directly** and is where
  he is taught. That slide carries the "class happens" quotation, the takehome
  "People make their class, under circumstances they did not choose," and two
  forward questions: who is doing the making (6.1), and whether the female
  Reformers made history or supported the men who did (6.2). Do not restore
  per-historian slides without a reason to think students need the
  labour-aristocracy debate.
- **Part three has no discussion pair** (2026-09-15, at the author's request).
  The Thompson quotation slide, the "who is doing the making?" discussion slide
  and its answer slide were collapsed into the foreshadow slide, since the
  class focuses on Thompson in Week 6. The Nairn/Anderson, Scott and Epstein
  material from the answer slide was cut with them. Week 6.1 (Thompson) and
  6.2 (women's and gender history) are its natural home. The Peterloo image
  stays: it breaks up the text slides and sets up the 6.2 question.
- **No portraits of Hill, Hobsbawm or Thompson.** All three died recently
  enough that photographs of them are in copyright, and the deck's licence rule
  is public domain or CC only. Part three uses Peterloo instead, which does more
  argumentative work than head shots would. The style guide's "every named
  person gets a portrait" rule is knowingly not followed here, and neither is
  it for Ranke, whose portrait is in the 4.2 deck.
- **The take home and the arc are one slide** (2026-09-15, at the author's
  request). SLIDE-STYLE asks for a take-home slide followed by a separate `.cards`
  arc slide. Here the two said the same three things in the same order, so they
  are merged. The headline is the take-home sentence, and each card carries its
  part's dates, name and takeaway. The recap still repeats the headline.
- **Every image in the motor and problem sections has a stated point**
  (2026-09-15, at the author's request, after the loom, barricade and Peterloo
  images were found hard to teach from). Each now has an `.image-notes` slide:
  factory (Baines and Hervieu), barricades (Thibault's two plates) and Peterloo
  (the banners' political demand, the woman on the platform, a crowd at a
  meeting rather than at work). The two-image notes slides use `.shots`, which
  SLIDE-STYLE reserves for images that genuinely share one set of bullets. Both
  pairs are comparisons, so they qualify. Each image still gets its own
  full-bleed slide first.
- **Engels gets a portrait although the schedule names only Marx.** He is
  co-author of the assigned text and Green and Troup call him Marx's "life-long
  collaborator" (p. 34); the deck quotes his 1888 class definitions.
- **The *Brumaire* comes before the part-two discussion, not after it.** The
  discussion question quotes the *Brumaire* sentence, so students need it on
  screen first.
- **`bm-reading-room-1859.jpg` is a crop.** The Library of Congress scan
  includes the surrounding page and visible bleed-through from the facing leaf;
  the crop keeps the plate. Faint show-through survives at the top edge and
  reads as paper texture. Also in `images/README.md`.
- **The cold open has two images but only one notes slide** (2026-09-15, at
  the author's request). Church's *West Rock, New Haven* (1849) comes first as a
  contrast: a Hudson River School pastoral with its farm workers in the field
  and no industry. It gets no `.image-notes` slide of its own. The contrast is
  carried on the Manchester notes slide instead, in the "Church's valley" and
  "haymakers in the middle of the field" bullets. Church's picture is American
  and Wyld's English. The pairing is about the picturesque convention and where
  the work is, not a claim that Connecticut was pre-industrial in 1849.
- **`kennington-common-1848.jpg` is no longer used** but is still in `images/`
  and credited in `images/README.md`. Delete both if it is not brought back.

---

## 6. The through-line, and what was cut to keep it

**Status:** decided with the author, 2026-09-12.

An earlier version (39 slides, then 34) ran five threads at once — Ranke's
method vs. Marx's question; whether the theory can be proved wrong; structure
vs. agency; sources as persuasion; whose archive — and each discussion slide
asked about a different one. Students could not tell what the day was about.

The deck now follows **one question: if how people make a living drives
history, what is left for people to do?** Green and Troup support it as the
chapter's own frame: the relationship between social being and consciousness
is "one of the strongest unifying themes" of Hill, Hobsbawm and Thompson
(p. 36). It also matches the week's framing in `schedule.md` (deeper forces
vs. events and individuals) and leads straight into Thompson in Week 6.

Three parts; the first two each have one discussion pair:

1. **The motor.** Cold open of Church's *West Rock* (1849), then Manchester ("who decided this?"), a single Ranke
   slide as the foil, the Reading Room, portraits, a four-step `.flow`
   diagram, then one slide per step with a matching `The motor · N` eyebrow so
   students always know where they are. Discussion: **is it provable?** — the
   only place testability appears, at the author's request, placed after the
   whole motor and before 1848.
2. **The problem.** 1848, Thibault's two barricade plates (Sunday before the attack, Monday after) with a notes slide, the *Brumaire*. Discussion: if
   the motor runs by itself, why did 1848 turn on what people did?
3. **What historians did.** Hill and Hobsbawm (structure first), Peterloo with a notes slide,
   then a single foreshadow slide for Thompson (class happens), who is taught
   in Week 6. No discussion pair: the "who is doing the making?" question moves
   to Week 6.1.

The recap headline repeats the take-home sentence: "How people make a living
drives history. People still have to act." Every slide's takehome should be
readable as a step toward that sentence; if a new block is not, it probably
belongs to one of the cut threads.

**The author chose to keep:** the Reading Room, placed directly after the
Ranke slide, because it shows Marx building the theory from historical
evidence rather than from philosophy alone.

**Cut, and why** — restore only with a reason that serves the through-line:

- *The Kennington Common image* — a second 1848 image; one barricade is enough.
- *The power-loom notes slide* — its bullets were about gender and sources as
  advertisements; the image stays, caption only. **Reversed 2026-09-15 at the
  author's request:** Hervieu's 1839 spinning-room plate from Trollope's
  *Michael Armstrong* now follows the Baines plate. A notes slide sets the two
  side by side: the same industry drawn by a defender and by a critic, the
  child "scavenger" under the mule tied to the *Manifesto*'s "appendage of the
  machine," and both pictures as persuasion, which leads into the "is it
  provable?" discussion.
- *The "Why historians read him" / political-interventions slide and the
  four-writings cards slide* — the writings now appear where they are used: the
  motor diagram names the text behind each step, and the *Brumaire* is
  introduced on its own slide.
- *"The Manifesto's language about 'barbarian' nations"* — previously kept with
  a Week 9 pointer on the grounds that dropping it made the text look tidier.
  Dropped now because the day no longer discusses the bourgeoisie's global
  role at all; Week 9 treats it.
- *Engels's footnote narrowing "all hitherto existing society" to "all written
  history"* — accurate and interesting, but not about structure and agency.
- *The bourgeoisie's "most revolutionary part" block (the pyramids credit and the
  "naked, shameless" charge)* — the one motor block that said nothing about
  people.
- *Kennington Common in the 1848 year block*, with the image.
- *The "why open a pamphlet with all of history?" discussion pair and the
  "does 1848 refute him?" pair* — replaced by the "provable?" pair and the
  part-two pair.
- *The Ranke/Marx comparison slide, the "caught being wrong" take-home, the
  Marwick quotation and "history from below"* (Green and Troup credit the
  phrase to Thompson in 1966, p. 33; the priority is disputed — Febvre used
  *histoire vue d'en bas* in 1932). Week 6 is the natural home for the phrase.

Earlier quotation fixes that carried over: the crises quotation includes "too
much means of subsistence"; the class pairs are the *Manifesto*'s own
(freeman/slave … guild-master/journeyman), not "the world market"; the
*Brumaire* is not presented as correcting the 1859 preface it predates.

**Fixed after a fresh-context review of the rebuilt deck, same day** — kept
here because each is an easy mistake to reintroduce:

- (The answer slide this applied to was cut on 2026-09-15; the correction still
  holds for the 6.2 question on the foreshadow slide and for any Week 6 deck.)
  The last takehome said Thompson's book did not name the female Reformers.
  Green and Troup's criticism (p. 40) is of how he *characterized* radical
  women ("giving moral support to the men"), not that he left them out. The
  takehome now asks whether they made history or supported the men who did.
- Hill and Hobsbawm were summarised together as reading politics off the
  economy; see item 5.
- Hobsbawm's quotation was labelled "revising in public." Green and Troup say
  "he had not changed his mind" (p. 38); the slide now quotes "I remain
  sufficient of a traditionalist Marxist…" and is labelled "unrepentant." He
  also "had never sought to explain British 'reformism'," so the slide no longer
  says he explained why workers grew less radical.
- Thompson: it is class-consciousness — the way *experiences* are "handled in
  cultural terms" — not "the consciousness" that is handled (p. 39).
- Epstein: "limited participation," not "the participation" (p. 40). Kaye, not
  Green and Troup, supplies the "core proposition" (p. 34). Green and Troup
  hedge the unifying theme with "might be described as" (p. 36).
- The take-home, arc and recap now all state the motor's fourth step
  ("inevitable"), since that is the premise the part-two problem contradicts.

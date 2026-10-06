# Issues — big-picture-review

**What this is.** A review deck for 8.1, built (2026-10-06, at Fred's request)
from the instructor guide `../../discussion-guide-8-1-instructor.md`. The guide
is the source: six big ideas from Weeks 1–7, each with the historical detail
that supports it. If one changes, change the other.

**The shape is the request, and it is a new pattern.** Each part is a header
slide (the idea's headline, then the idea itself as a `.detail` fragment), then
one slide per subpoint numbered in the eyebrow (`Part one · 2 / 5 · …`), each
setting a claim and a quotation or detail beside the image that made the point,
then a discussion slide. The subpoint slides use `.with-figure.wide`, a modifier
added to `/assets/css/reveal-lecture-theme.css` for this deck (documented in its
header comment and above its rules): the image column fits the picture, capped
at 470×380, and the body text runs below the quotation in size. 52 slides in all.

**Discussion slides use the trivia's Big ideas questions,** and carry no
answer. The four conceptual questions from `../review-trivia/` (commented out
there the same day) are the questions for parts one, two, four and five;
parts three and six use questions from the instructor guide. Each slide is the
topic and the question only. The style guide's discussion slide has a third
beat, a `.takehome` with the crux; those were written and then removed at
Fred's request (2026-10-06), because the subpoint slides before each one have
just walked through the material.

**Deliberate deviations from `../../SLIDE-STYLE.md`.**

- *No arc slide.* The six header slides already state each part's idea, and an
  arc of six cards would repeat them in type too small to read. The take home
  carries the two landing points instead.
- *Faces in part six.* The review rule prefers evidence to portraits. Part six
  is about people arguing over an idea (Voltaire, Condorcet, Herder, Ranke,
  Acton), and the decks it draws on have little else to show; the portraits
  are there so every subpoint has a picture, as requested.
- *One subpoint has no image:* Vansina (4.6). The only candidates were his
  portrait, which is fair use, and the griot postcard, which the class did not
  spend time on.
- *The take home and part five's trade-off slide reuse lines kept on purpose*
  from `../what-are-we-talking-about/`: "You cannot measure progress until you
  say what history is for" and the Braudel/Ginzburg zoom cards and takehome.
  Those are the course's established phrasing; keep them identical.

**Everything is reused from decks that checked it.** No new readings. On
2026-10-06 all 53 quoted strings (after the review's fixes) were matched
mechanically, word for word, against the other decks' `index.*` and, for
Bloch, the research-packet text. Images are resized copies from the same
decks; see `images/README.md`.

**Checked 2026-10-06.** `scripts/slide-words.py`: all containers within target.
Every slide stepped through headlessly at 960×700 with all fragments shown:
tallest 695px, none clipped, no broken images, no console errors.

**Fresh-context review, 2026-10-06.** A cold reader checked the deck against the
research-packet texts and PDFs. Each finding was re-checked at the source
before acting; 21 findings, of which these were fixed:

- *Closing:* "Hobsbawm and Anderson argue they were invented, deliberately"
  misstates Anderson, for whom nationality was "the spontaneous distillation of
  a complex 'crossing' of discrete historical forces" and who faults Gellner
  for equating "invention" with "fabrication" (*Imagined Communities*,
  pp. 4, 6). Now Hobsbawm for invention, Anderson for imagining; "in 4.1"
  became "in Week 4.1".
- *Bloch (4.5):* now the whole sentence from p. 40, which says no scholar has
  accounted for the strip pattern; the dolmens line is a comparison, not a
  finding.
- *Voltaire (6.1):* the age of Louis XIV ended in 1715, when Voltaire was
  twenty, so not "his own lifetime".
- *Thompson (5.6):* the p. 12 cite now sits on the quotation; the follower
  count comes from the deck caption, not Thompson.
- *Peterloo (1.1):* the print names Henry Hunt (and Carlile signs it), so not
  "names one".
- *Take home:* tests were "sharpened and spread", not "got stricter"; the chain
  of transmission is older than Ranke.
- *Smaller:* hedges on the part one, three, four and closing headlines;
  Thucydides as readers' warning, not his intent; the trial record is a church
  tribunal's, read as Ranke read his sources; Acton's framing clause restored
  and the reply credited to later scholars; Crawley credited for Melos (the
  assigned PDF reads "the weak submit"); Marx's "paradox" is Green and Troup's
  word, not a post-1848 concession; Herder named, Popkin credited for the
  nationalism claim; a claim-then-negation folded; a headline tail cut; a line
  of commentary on the course removed; "before a source is read" no longer
  repeated three times.

Kept on purpose, so a later review needn't raise them:

- *Image pairings the reviewer questioned.* 4.1 shows Bede flagging his own
  paraphrase on a slide about miracles (it is the evidence that his care was
  real); 1.4 shows Treitschke's lecture hall beside a line about seminars (the
  picture is the state-paid chair, the line is about who got in); 4.5 shows a
  Provence hillside for northern French field patterns (land as evidence that
  is nobody's testimony; the caption says Provence). Each caption states what
  the picture is.
- *Part one's crux names Voltaire, Vansina and Scott,* who are not in part one.
  The question asks for any writer in the course.
- *Acton's headline* ("In 1895 Acton wrote the medieval historians off")
  stands. The reviewer cites Popkin p. 50 as saying Acton dismissed medieval
  history; not verified here, because `popkin-ch-3.pdf` is a scan with no text
  layer. The quotation on the slide itself (pp. 40–41) comes from the Week 3
  deck.

**The same errors in older decks were fixed the same day** (2026-10-06):
the Anderson closing in `../what-are-we-talking-about/` and
`../purpose-and-progress/`, the "state document" line in
`../what-are-we-talking-about/`, Voltaire's "own lifetime" in
`../enlightenment-progress-2/`, and "only when people act" in
`../marx-structural-history/`. The instructor guide and both review games
were corrected too.

**The schedule does not link this.** Add a slides line under 8.1 in
`../../schedule.md` when it is ready to go out.

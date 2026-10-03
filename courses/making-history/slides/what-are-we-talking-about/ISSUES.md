# Issues — what-are-we-talking-about

**The Historians Café section is gone, as of 2026-10-02.** All three slides
(`NOBODY ANNOUNCES IT`, `FOUR TELLS`, `THE SUMMARY TRAP`) were cut at Fred's
request, along with the "Five questions, no readings, and a draft due at
midnight" framing slide that set them up. `historians-cafe.md` is now the only
place students see the assignment; `schedule.md`'s 8.1 alert is the only place
they see the due date. If the deck should carry a due-tonight reminder, it
needs a new line somewhere — nothing in the deck mentions the Café now.

**Two discussion slides, not five, as of 2026-10-02.** The deck is built around
`schedule.md`'s own two 8.1 prompts: progress (Ranke → Marx → Thompson →
Ginzburg) and purpose (Livy, Voltaire, Ranke, Marx, Thompson). The other three
discussion slides that came over in the 2026-09-30 split were cut: `One file,
two methods` survives as an evidence slide ahead of the purpose discussion
rather than as a discussion of its own, and `Our own preselected record` (Carr
on the syllabus) and `A method you could run` (which methods scale down to one
person) are gone. Both are reusable if 8.1 ever needs a third question.

**The two questions are kept close to Fred's wording on purpose.** This is the
one place the deck ignores the style guide's "a review asks new questions, not
the old ones again" rule: these aren't last week's questions re-asked, they are
`schedule.md`'s own 8.1 prompts, which students read before class. If those
prompts are rewritten on the schedule, rewrite these two slides with them. The
new questions in the deck are the ones on the bridge slide ("what would it take
for one of them to count as an improvement on the last?") and in the slide
headlines.

**It opens on Thursday's last slide, reworked.** The scale slide
(Braudel/Ginzburg, "you cannot zoom in and out at the same time") is carried
over from `../review-weeks-1-6/` verbatim except for its closing question,
which pointed at the 7.2 reading refraction and now points at progress. Keeping
the headline word-for-word is deliberate — it is the handoff from Thursday, and
rephrasing it would throw away the recall. If 7.2's scale slide is ever
rewritten, rewrite this one with it.

**Everything here is reused from decks that checked it.** No new quotations and
no readings. Al-Biruni, Ranke, Livy and Thompson are quoted from
`../review-weeks-1-6/`, which took them in turn from
`divine-power-and-statecraft` (al-Biruni), `review-weeks-2-4` (Livy, Ranke) and
`history-from-below` (Thompson). Nothing in this deck was re-verified against a
primary PDF. The Ginzburg material is prose, not quotation, for the same reason
7.2's Ginzburg slide is: there is no checked Menocchio quotation in this repo.

**"Al-Biruni had the test eight centuries early" is the deck's one real claim.**
It rests on the two quotations on that slide and nothing else — al-Biruni's
preface (c. 1017) making eyewitness-over-hearsay the test, against Ranke's 1824
introduction. It is not a claim that Ranke knew al-Biruni, or that al-Biruni was
first; the takehome says only that the test predates the refusal. Don't let it
drift into a priority claim without a source.

**Five lines rewritten for the no-self-negation rule, 2026-10-02.** The rule is
in `../../SLIDE-STYLE.md` ("Don't follow a claim with its own negation"), added
at Fred's request after "The purpose settles the question before the document
does. Neither of them is making anything up." The other four were the Al-Biruni
takehome ("...was new; the test ... was not"), the progress discussion takehome
("None at all on the big one"), the take home ("five answers to that, not one")
and the arc card ("so the corrections do not run in a line"). The deck now
scans clean for the shape. Two things that look like it and are not: the
Braudel/Ginzburg takehome ("explain everything and decide nothing ... decide
everything and explain almost nothing") is a parallel with two subjects, and the
take-home block labels ("What did improve" / "What did not") are labels, not
sentences.

**Register pass against Fred's own prose, 2026-10-02.** Fred read the deck as
"a bit too slogany." The rule is now in `../../SLIDE-STYLE.md` ("One epigram per
part; let the rest just say the thing"), measured against `why-study-history.md`,
the `archive/` essays and `schedule.md`. Twenty lines changed. The numeric
pairing is gone entirely (four instances: "One file, two historians", "Three
jobs, one file", "Narrow repairs, no line", "One trial, one man" — zero in
Fred's own writing). The four `.flow` labels no longer run in perfect anaphora
(`Against speculation / Against the archive / Against abstraction / Against the
crowd`), and neither do the four step paragraphs underneath them. Hedges went
from 1.2 per thousand words to about 11, which is the rate of Fred's essays and
above `schedule.md`'s 7.5 — deliberate for a day built on two open arguments,
but it is the number to pull back first if the deck reads as waffly in the room.

**Three epigrams were kept on purpose.** The take home ("You cannot measure
progress until you say what history is for") is the deck's thesis and the one
line that should be quotable. The Braudel/Ginzburg takehome is Thursday's, kept
word for word as the recall cue. The arc headline ("Real repairs, and a target
nobody agreed on") is the one place the antithesis is the finding rather than a
decoration. Don't flatten these three in a later pass without replacing what
they do.

**No images.** The deck has no image slides, so it does not set
`image_slides: true` in the front matter and the image-slide stylesheet is not
loaded. This is the clearest deviation from the style guide left in the deck —
nine content slides with no image break. The four full-bleed recall images in
`../review-weeks-1-6/images/` (power loom, olive grove, General Ludd, Congress
of Berlin) are the obvious candidates if it ever gets any; add the flag and an
`images/README.md` with them.

**Rendering checked 2026-10-02.** All eleven slides stepped through in a
headless browser at 960x700 with every fragment forced visible; nothing clips.
`scripts/slide-words.py` passes with every container inside its target. The
`.flow` step labels are bare dates (`01 · 1824`) because `01 · Ranke, 1824`
wrapped to two lines in three of the four columns and staggered the headings.

**The schedule does not link this deck.** Add a slides line under 8.1 in
`../../schedule.md` when it is ready to go out; 7.2's line is there but
commented out.

# Open issues — Science and Medicine (13.1)

Contributor notes, excluded from the build. Deliberate deviations are recorded
here so a later review does not raise them again.

## What this deck is

Built 2026-11-06 from the author's brief:

> highlights from maza should emphasize different topics that emerged in
> historical study. then i want to present a more general history of science
> and medicine as its evolved over the years, not just highlights from shapin
> and rosenberg, though there should be a quote or two from each. it would be
> nice to show how each field (science and medicine) has had a kind of
> historical "progression" as the rest of the course in terms of earlier
> triumphant histories of science (whiggish) to more nuanced investigations of
> who is included and excluded and politics, and cultural construction, etc.
> there should be lots of good images to display and discuss. one of the
> questions that should underlie the whole thing is what can we learn about
> science or medicine through the history, and what we can learn about
> ourselves?

**Tenth revision, 2026-11-10,** at the author's request, in several messages:
"review all slides for unnecessary names like De Kruif. names are not
important for this lecture"; "make the pasteur image like the eakins one";
"remove the snow map"; "remove the [diagnosis becomes part of who a person is]
slide (it's already covered)"; "headline … also need a quote in the usual style
… now it's just an empty space"; secondary text "way too large"; and the
quotation "needs to be right under the headline, and a bigger space under that
before the explanation text."

- **Names.** Headlines, eyebrows and details no longer name historians who are
  not assigned authors (De Kruif, Garrison and Lovejoy in the eyebrow, Butterfield,
  Koyré, Hessen, Merton, Latour, Woolgar, Eisenstein, Daston, Galison, Raj,
  Sigerist, Foucault, Crosby, McNeill, McKeown, Porter, Thompson, Ulrich,
  Ballard, Showalter, Charcot, Jones, Arnold, Pamela Smith); ideas lead
  instead ("Historians made smallpox part of the conquest of the Americas").
  Kept: the assigned authors (Maza, Shapin, Rosenberg, Kuhn) and every name
  inside a citation, since a quotation must be attributed; artists, sitters
  and titles in image credits; Garrison and Lovejoy in their two track headings,
  because their sentences are quoted. The title slide's citation note no longer
  lists who appears only at second hand. The "Inside or outside" slide now
  describes the two positions without naming Koyré, Hessen or Merton.
- **Pasteur** is an image slide in the Gross Clinic style (large portrait, a
  caption rail with the explanation, including Rosenberg p. xvii on the germ-theory
  promise). The de Kruif quotation slide, with its Rosenberg quotation and
  `.detail` lines, is gone, and *Microbe Hunters* is now only "popular books."
- **Snow's map and the "diagnosis becomes part of who a person is" slide**
  (Rosenberg p. xix, "What a name does," and its question about the 1900
  homosexuality diagnosis) are deleted; the Snow map image went to the scratchpad.
- **Quotations for the three bare explainers.** The books those slides are
  about are not in the text caches, and a web search could not confirm exact
  wording or pages for them, so each slide now carries a *verified* sentence from
  an assigned reading that makes the same point, with the historian's own book
  named only in the detail: "scientific objectivity itself has a history" quotes
  Shapin and Schaffer on "the objectivity of the experimental matter of fact"
  (Maza p. 97); the laboratory slide quotes Shapin p. 10 ("There is as much society
  inside the scientist's laboratory…"); the circulation slide quotes Maza p. 116
  on historians' "where" and Eurocentrism, with an ellipsis. If the author has
  *Objectivity*, *Laboratory Life* or *Relocating Modern Science* to hand, a
  sentence from each would be a better quotation.
- **Typography.** A `.detail` following a `.quote` is now commentary-sized
  (0.5em, with a clear gap) on plain quote slides, and the compact explainer's
  text column is top-aligned so the quotation sits right under the headline, with a
  1.5em gap before the explanation. The compact explainer's picture cap is now
  290px. All in the theme CSS; the new rules affect only `.quote ~ .detail` and
  `.with-figure.wide.compact`.

**Ninth revision, 2026-11-10,** at the author's request, in several messages:
remove Darwin and "focus on paintings of heroic science in chronological
order"; "remove the horton slide"; the explainers' detail text "is too large
and needs secondary position under the quote"; and "His followers treated
scientific knowledge as something people make (his is not clear). can we link
constructivism to linguistic turn?"

- **Paintings, by the era of the subject (56 slides).** Darwin's statue and
  Newton's monument (an engraving of a sculpture) went; the series is now four
  paintings: Matejko's *Copernicus* (1872, Commons' date), Banti's *Galileo*
  (1857), West's *Franklin* (c. 1816, kite experiment 1752) and Gilbert's
  *Men of Science Living in 1807–8*. Newton, the "almost divine" inscription,
  Darwin and the Boehm statue are no longer in the deck. Facts in the captions
  that come from outside the readings: Copernicus died in 1543 (so "more than
  three centuries"); West's painting is more than sixty years after 1752 and
  is at the Philadelphia Museum of Art (Commons' file gives only "Google Art
  Project"). Check them before publishing.
- **Horton is out.** The slide, its Yoruba tray image and the comparison slide's
  "Horton's African theory" went; Maza's Horton passage (p. 100) is no longer
  in the deck.
- **Solvay opener.** The Solvay notes slide was already gone when this round
  began (the first backup of the round lacks it), so it appears to have been
  removed by hand in the editor; it was left out, and the image moved to the
  scratchpad. The deck opens on the Title slide.
- **Explainer details.** `.with-figure.wide.compact` (renamed from
  `.captioned`) now also sets `.detail` at 0.46em, the commentary size, instead
  of 0.56em, which was nearly the quotation's 0.63em; every explainer in the
  deck uses it (the picture is capped at 300px).
- **"A young term" is out.** The reveal block on Shapin's opening slide
  (Koyré gave the phrase currency in 1939; the two 1954 books, p. 2) was
  removed at the author's request, and the quotation went back to full size.
  The fifth revision's mention of it is superseded.
- **Schiebinger and *Sidereus Nuncius* are out.** "the gender slide and the
  Sidereus Nuncius seem out of place. delete." The Schiebinger slide (with the
  Voltaire frontispiece) and the Galileo's-patron image slide (Biagioli on
  Galileo as courtier, the 1610 title page) were deleted, and their two images
  moved to the scratchpad. Women still appear on the Harvard computers, Merian
  and "Who did science" slides, and the comparison slide still says "women".
- **Constructivism.** The headline no longer says "His followers" (Kuhn is
  ten slides away now); it says "Constructivists." A `Compare · Week 10.1`
  pointer ties it to the linguistic-turn deck, in that deck's words (sources as
  "texts," not "transparent windows onto the past," Maza p. 211; constructivism
  as knowledge "made," Golinski via Maza p. 95).

**Eighth revision, 2026-11-10:** "the images of the great men of science need to
be in chronological order. probably the early garrison quote should be joined
by the lovejoy ideas quote." The four great-men images now run by the era of
the man (Galileo, Newton, the 1807–8 group, Darwin), not by the date of the
image. Garrison's slide now sets his sentence beside Lovejoy's (Maza, pp.
86–87: "Ideas … are like a set of building blocks with which thinkers play and
from which the occasional genius constructs something dazzling") on one
`.parallel` slide, headed "Early histories credited a few chosen spirits and
the occasional genius," with the same discussion question. The Lovejoy quote
has no closing period, since the sentence crosses the p. 86/87 page break and
the cache cannot say how Maza ends it.

**Seventh revision, 2026-11-10:** "let's just start with slide 5 and remove
preceeding ones." Slides 1–4 (the full-bleed Rembrandt and Solvay images, the
cold-open question, the Rembrandt notes) are gone, and the deck now opens on the
Solvay notes slide (58 slides). That slide's "Three centuries after Rembrandt"
became "A group portrait like this still says who counts as a knower." The
Rembrandt image went to the scratchpad. The deck no longer states its guiding
question ("What can the history of science and medicine teach us…") anywhere; the
Solvay bullets and the section dividers carry it. The fifth and sixth revisions'
descriptions of the cold open are superseded.

**Sixth revision, 2026-11-10,** at the author's request, over several messages:

> ok i think i was wrong. i think we should separate science and medicine into
> two sections so there is more internal cohesion in each. garrison is a great
> starting point. that could be followed by a series of paintings or photos
> that emphasize the deification of "Great men" of science
>
> we're cramming in too much historiographical detail like Richard Westfall
> (1971) and Betty Jo Teeter Dobbs (1975)… the science and occult point can
> stand alone
>
> text like "Pictured: James Gillray's The Cow-Pock…" should [be] formatted in
> caption typography under the image
>
> slides like Schiebinger focus too much on the detail of the historian. i
> only want to focus on their historiographical intervention

*This section governs where it conflicts with the fifth revision's "one
chronology"; the order below replaces it.*

**Two sections (62 slides).** Cold open and title; **Section one · science**
(chronological, opened by Garrison's "a few chosen spirits" quotation and four
great-men images: Newton's monument, Banti's Galileo, Gilbert's *Men of
Science*, Boehm's Darwin; then Butterfield through Raj and Maza's summary);
**Section two · medicine** (chronological: the physicians' history, Jenner, de
Kruif, *The Gross Clinic*, Sigerist, Foucault, Snow, *The Cholera Years*,
Crosby and McNeill, McKeown, social construction, social diagnosis, Tuskegee,
Showalter, Porter, Ulrich, Rosenberg's map, the six things, naming, diagnosis,
Arnold); then one two-track comparison slide, the take home and the closing.
Each section opens with a one-line divider. The constructivism and social
construction slides are separate again (the merged one was cut; the
social-construction slide's old "Compare · Week 10" pointer became a
discussion question). The hierarchy slide and the era arc were cut.

**Garrison sits in the science section** because his sentence is about
"science," not medicine, even though the book is a history of medicine.

**Newton and the occult** no longer names Westfall and Dobbs, gives their
dates, or says "Pictured"; the headline is now "Newton's gravitation was
rooted in alchemy," with Maza's quotation (cited to Maza, p. 99) and the
eighteenth-century line on the boundary. The names are in `ISSUES.md` only.

**Historians' details now give the intervention, not the person.** Roles,
nationalities and affiliations ("a historian at Stanford," "a French
philosopher," "a Swiss doctor") were cut from the explainers, Sigerist, Kuhn's
block and Johns; the work and year stay where they carry the argument.

**"Pictured" text moved into the caption under each image** (14 explainers),
in the caption typography. Longer captions pushed explainers past the box, so
the theme gained one opt-in modifier, `.with-figure.wide.compact`, which caps
the picture at 300px instead of 380px (documented in the CSS header; no other
deck uses it). Captions are kept to about 90 characters on narrow portraits.

**Facts from outside the readings, great-men series** (check before
publishing): Newton's monument is dated 1731 and designed by William Kent and
Michael Rysbrack (the Wellcome print says "after W. Kent and M. Rysbrack");
the Latin inscription's translation, "a strength of mind almost divine," is
the standard one that Wikipedia prints, so check it against Westminster
Abbey's own wording; Pope's "God said, Let Newton be!" epitaph was refused for
the monument and is not on the slide. Banti's painting is 1857 and the trial
1633; "three churchmen" counts the figures at the table. The Gilbert group
portrait is described as imagined (the title says "living in 1807–8"); the
National Portrait Gallery lists 48 sitters, all men, so the caption says
"nearly fifty." The Boehm statue's date is not stated.

**Fifth revision, 2026-11-10,** at the author's request:

> let's step back and rethink the slides. i think we can remove the different
> parts (1,2,3) of the slides. I want a more unified historiography of science
> and medicine overview, with at least one slide for the sci rev scholarship
> and the issues people argue about, and ideas about reframing disease.
> science and medicine historiography should be integrated in the deck.

*This section governs where it conflicts with the older ones below, which
describe the three-part deck: the "Part" structure, the order, the slide
counts and part one's explainers.*

**One chronology, no parts (56 slides at first; 57 with Garrison, 56 without the Maza cards).** Science and medicine are
interleaved by the date of the scholarship: the old story (Garrison, de
Kruif, Butterfield); the 1930s (internal and external, Sigerist); the 1960s
(Foucault, Kuhn, *The Cholera Years*, Horton); the 1970s (Westfall and Dobbs,
Crosby and McNeill, McKeown, Latour and Woolgar, Eisenstein); the 1980s
(construction, social diagnosis, *Leviathan*, Showalter, Porter, Schiebinger,
Ulrich); 1992 and after for disease (Rosenberg's map, the six things, naming,
diagnosis, Arnold); 1993–98 for science (Biagioli, trust, the Scientific
Revolution, Johns); the 2000s (Smith, Daston and Galison, Raj); Maza's 2017
summary. Eyebrows no longer say "Part".

**New slides.** (1) A new cold open, Rembrandt's *Anatomy Lesson* (1632) and
the 1927 Solvay photograph, replacing Wright's *Air Pump*, which the author
doubted ("how related to the historiography of science?"): both are about who
is allowed to know. (2) Maza's examples (Lovejoy, Darnton, Riskin) on one
`.cards.three` slide, replacing six slides; the author then asked what it was
doing there, and it was cut (names that never return, nothing about science or
medicine, and it echoes Maza the way the author asked not to). The hierarchy
slide is now the only Maza-only framing slide. (3) One `.parallel` slide that puts
constructivism and the social construction of disease side by side, replacing
two slides and the "Compare · Week 10" pointer. (4) "Rosenberg treated
disease as six things at once": a paraphrase of his p. xiii definition.
(5) The Scientific Revolution, in four slides: Shapin's denial, now with a
"young term" block (Koyré 1939; the two 1954 books, p. 2); "what is argued",
four cards (one event or many; break or continuity; ideas or practices;
inside or outside; pp. 3–4, 9); "for whom"; and "Shapin still tells the story,
as one about our ancestors" (p. 7), with the "road to the present" question.
(6) A four-card arc by era, which replaces the comparison and the old arc.

**Cut:** the great-chain image, Lovejoy, Darnton, Riskin and the pattern slide
(now one slide), Imperato's museum, the comparison slide, and the "Compare ·
Week 10" pointer. Five image files went to the scratchpad (`images/README.md`).

**Quotations added** (Shapin pp. 2–4, 7, 9; Rosenberg pp. xiii–xiv; Maza
pp. 86–87, 95) were matched word for word against the OCR caches by script on
2026-11-10. They were **not** checked against the page images; do that for
Shapin pp. 3–4, 7, 9 and Rosenberg p. xiii before publishing. The six-things
slide paraphrases p. xiii, whose OCR garbles the dashes around
"intrapsychic."

**Garrison, added as the example of the old narrative (57 slides).** The
physicians' history slide named Garrison without introducing him, so the name
was cut from its block and Garrison got his own slide, quoting one sentence
(p. 36 of the 1913 first edition: "It is no exaggeration to say that science
owes most to the shining individualism of a few chosen spirits.") with a
discussion question. The wording was matched in two independent Internet
Archive scans (the Wellcome copy, b31344641, and Google's
anintroductiont03garrgoog); an excerpt is cached in
`~/Dropbox/courses/making-history/.research-packets/garrison-introduction-1913.excerpt.txt`.
The page number is read from the running head above the passage; check it on
the page image. Garrison is not a simple triumphalist: the same page says
science "has never been continuous, nor even progressive," and his preface
quotes Billings on the tapestry of general history. The slide shows only the
great-men claim, so a student reading further should not be told he missed
context entirely. The headline says "gave the credit," which paraphrases the
sentence and the one before it ("accomplished by the arduous labor of a few
devoted workers in science").

**De Kruif slide fixed.** The detail said Rosenberg's quotation marks "flag
claimed microbes that turned out not to cause disease," which Rosenberg does
not say on p. xvii. It now reads: the quotation marks around "discovered"
signal doubt, and the era assumed a microbe was waiting behind every disease
(his preceding sentences: "the relevant pathogenic microorganisms need only be
found").

**Facts from outside the readings, cold open** (none quoted): the Amsterdam
surgeons' guild held public dissections of executed criminals and
commissioned the Tulp group portrait; the large book and the sheet in a
watcher's hand are visible in the painting; the Fifth Solvay Conference
(Brussels, 1927) had twenty-nine participants, Marie Curie was the only woman,
had two Nobel Prizes, and the conferences were by invitation. Check these
before publishing. `deck-check.sh` on 2026-11-10: 56 slides, 0 FAIL, 0 WARN.

**Fourth revision, 2026-11-09,** at the author's request, over several messages:

> remove the this day in context (i always skip over it b/c i talk about it in
> class), and let's remove the breen slide; not directly relevant to history of
> science / medicine for the day
>
> same for ulrich. same for norton.
>
> in general, i don't need to echo maza super closely here. i want a few
> highlights of how she illustrates how historians have directed their inquiry
> into certain topics; but most of the slides should be history of science and
> medicine overview, even beyond what maza covers.
>
> i don't want a history of science intro, but overview of historiography of
> science. that's the main thread
>
> instead of the dedicated discussion slides, can we have provocative
> discussion questions appear on key slides (or just after)? i don't think we
> need images of scholars in this deck; too many people to cover so highlight
> some gives undue importance

*This section governs where it conflicts with the older ones below (slide
count, portraits, discussion slides, part one's explainers).*

**Cut:** the throughline ("Today in context"; the guide's structure item 3 is
deliberately not followed here), Breen, Ulrich's basket and her part-one
portrait, Norton, Skinner and the Geoffrin salon image. Part one is now the
hierarchy, the great chain, Lovejoy, Darnton, Riskin and the pattern slide.
Ulrich stays only as *A Midwife's Tale* in part three. The ten unused image
files were moved out of `images/` to the session scratchpad (`README.md` keeps
their sources).

**Added to part two, beyond Maza** (five slides, all paraphrase, no quotation):
internal and external explanations (Koyré, Hessen, Merton), Latour and
Woolgar, Daston and Galison, Schiebinger, Raj. A Bloor slide (the "strong
programme") was added and then cut as too esoteric for an intro course; its
Lavoisier image went to the scratchpad. Medicine was left as it was.

**Part two is in chronological order of the historians' work,** at the author's
request ("basic chronology of how different people have approached history of
science"): Butterfield (1931–49), internal and external (1930s), Kuhn (1962),
Horton (1967), Westfall and Dobbs (1970s), constructivism (1970s–80s), Latour
and Woolgar and Eisenstein (1979), Shapin and Schaffer (1985), Schiebinger
(1989), Biagioli and Findlen (1993–94, on image slides), Shapin on trust
(1994), Porter on numbers (1995, on the Harvard computers slide), Shapin's
survey (1996), Johns (1998) and the Eisenstein–Johns pair, Smith (2004, on the
Merian slide), Daston and Galison and Raj (2007), and Maza's summary (2017).
Images that illustrate a slide sit beside it (the air pump before *Leviathan*,
Sprat after the trust slide). This breaks the earlier thematic runs, such as
trust to numbers to objectivity, on purpose.

**Discussion slides removed** (all three, with their takehomes). The questions
now sit on key slides, each in a `.reveal-block.argument` labeled "Discuss"
with the question in bold (the block's own styling, no new CSS), as a fragment
after the quote. At the author's request each question *replaces* the
commentary block that was there, so six blocks are gone: "The ladder in the
university" (hierarchy), "The textbook image" (Kuhn), "Not that every view is
equally true" (constructivism), "Truth and trust" (Trust), "Frame, not
construct" (Naming and framing) and "What a name does" (Diagnosis and the
self). Questions are on the hierarchy slide, the pattern slide, Kuhn,
constructivism (is a belief's truth settled by its social cause?), Trust,
"Who did science" (the old part-two question, unchanged), Foucault, Naming and
framing, and Diagnosis and the self (the old part-three question, unchanged).
The part-one question changed: it no longer asks about Ulrich. The guide
gives questions their own level (`.question`); the closing question keeps it,
and the boxed ones deliberately trade it for the block look.

**Scholar portraits removed:** the Kuhn, Shapin, Rosenberg and Ulrich image
slides, and the Butterfield and Sigerist photographs (Butterfield's explainer
now shows Bacon's *Great Instauration* frontispiece; the Sigerist slide is a
quote slide). Kuhn is introduced in the first reveal block and Ulrich in her
slide's first `.detail`. Shapin and Schaffer, and Rosenberg, were also given
one-line `.detail` introductions between the quote and the block, which the
author asked to have removed (2026-11-10), so those two slides now quote them
with no introduction beyond the cite and the title slide's reading list.
The Rosenberg fair-use portrait is gone, so the fair-use note no longer
applies.

**Facts from outside the readings, new slides** (paraphrased, none quoted, no
page cites, no text cache; check them before publishing, per the guide's
step 5): Koyré's *Études galiléennes* (1939) and the summary "mathematics,
more than experiment"; Hessen's 1931 London paper on the *Principia* and the
needs of shipping, mining and war; Merton's 1938 monograph on Puritanism; the
internalist and externalist labels, and Butterfield as largely internalist (a
common characterization);
Latour at the Salk Institute in the 1970s and *Laboratory Life* (1979), whose
first subtitle kept "Social" (dropped in 1986), and the Salk photograph is the
building, not their laboratory; Daston and Galison's *Objectivity* (2007) and
self-restraint ("mechanical objectivity") taking shape in the nineteenth
century; Albinus's 1747 atlas, Tabula IV (his artist, Jan Wandelaar, worked
under his direction); Schiebinger's *The Mind Has No Sex?* (1989);
Voltaire's 1738 frontispiece, in which the mirror-bearing muse is usually
read as Émilie du Châtelet, and her French translation of the *Principia*;
Raj's *Relocating Modern Science* (2007), with "older accounts had Western
science radiating from Europe" the deck's summary of the diffusion model (a
1967 essay by Basalla is the standard example, deliberately not named);
Jai Singh II's five observatories (1720s–30s); Bacon's *Instauratio magna*
(1620). The Bacon file on Commons carries no description; it matches the
Library of Congress print (LCCN 91482886), a later copy of the same
engraving. `deck-check.sh` on 2026-11-09: 59 slides, 0 FAIL, 0 WARN.

**Third revision, 2026-11-07,** of part three and the whole deck's wording:

> let's revise the rosenberg slides to better proviude a general
> historiography of medicine. how has history of medicine changed over time?
> rosenberg is part of that, but obviously there are many contributors. also,
> please review all slides for academic jargon or esoteric phrases that will
> be lost of college freshmen

**Jargon pass.** Changed in the deck's own voice: "libelle" (now "scandal
pamphlet"), "material culture" ("the history of objects"), "cosmologies"
("beliefs about the world"), the pattern headline ("more material … more
cultural"), "Constructionists" in the Week 10 block. Glossed where the word
is the reading's: "incommensurable" (Kuhn), "cyclotron" (Boyle's caption),
"etiology" (Rosenberg p. xxii), King Philip's War. Simplified: the Hobbes
block (Maza p. 97: mathematical proof and a single authority), Johns's
"credit" (readers deciding which books to believe), Rosenberg's "frame, not
construct." Replaced two dense quotations: construction now quotes only the
second half of the p. xiv sentence; the "ecological vision" and McKeown
quotations are glossed by their details, and McKeown's drops "morbidity" by
ellipsis. **Removed** the "symmetry postulate" that the second review asked
for: the idea stays (describe, not judge), the term goes. After the review,
"antiquarians" and "deviance" are glossed on their slides, and three Latin
or Italian titles are translated (Valadés, Imperato, Merian). Left inside
quotations without help: "rarefied," "canon," "genteel," "savants,"
"modernity."

**Second revision, 2026-11-07,** of part two:

> can the history of science section be more clearly chronological (maybe
> butterfield to start), kuhn, and then books that changed the way we think
> about the enterprise of science. probably need eisnestein vs johns on trust
> and print as well. i guess i'm wondering if we can have an illustrated
> history of science section that covers what maza says but more focused on
> the actual texts and hisotoriography of science

**Eisenstein through Johns.** Eisenstein's book was not available; Johns's
chapter 1 was (`~/Dropbox/Johns - 1998 - The nature of the book….pdf`, cached
as `.research-packets/johns-nature-of-the-book-ch1.txt`). Every claim about
Eisenstein is Johns's summary and is cited to Johns (pp. 10–11). If her own
text turns up, a direct quotation of "fixity" from *The Printing Press as an
Agent of Change* would be better. The 2002 *AHR* exchange (vol. 107, no. 1)
is named from outside knowledge, not quoted.

**Dropped in the second revision:** the Maza "march of geniuses" slide (its
phrase "through the Cold War" is now on the Butterfield slide), Flammarion and
the *Men of Science* engraving (both illustrated the old story but broke the
date order), the separate Horton text slide (now an explainer) and the "Even
Newton" block (now its own slide).

**First revision, 2026-11-07,** at the author's request:

> i think i want to retool the maza overview to be less about quotes from her,
> and more about examples of historians (drawing from her chapter) that
> decided to look at histories of different things. maza is a bit abstract,
> and i think the point of critically thinking about history of what is best
> for my audience with concrete examples and what they represent in
> historiography. then we can have the two case studies in science and
> medicine; in both cases i want to provide a brief overview of examples of
> "old" triumphant, whig histories of science and medicine -- the
> acculumation of knowledge and getting better. that is happening to some
> extent, but i want to really lhighlight the more critical approaches that
> emerged in recent decades and how it's become more inclusive. kuhn should be
> integrated in to the history of sceince historiography overview rather than
> a separate case study for simplicity.

**Order (58 slides).** Cold open (Wright's *Air Pump*, the session's
question, image notes); title; throughline.

*Part one, the history of what, as historians' cases from Maza pp. 83–108.*
One framing slide in Maza's voice (the hierarchy, p. 84), then a case per
slide, each showing the thing studied and saying what the case represents:
Lovejoy's chain of being (the Valadés image, then a slide on the old history
of ideas); Skinner and *The Prince* (context); Darnton and the libelles (the
social history of ideas); the Geoffrin salon (feminist recovery of the
salonnières); Breen and the Edenton print (goods as politics); Ulrich's
portrait and her basket (one object, a whole world); Norton and the Codex
Tudela (things acting on people); Riskin and the Strasbourg clock (objects to
think with, and the bridge to science). A `.cards` slide gives Maza's thesis
(p. 85) as the pattern; then a discussion.

*Part two, science, as an illustrated historiography in date order* (second
revision, 2026-11-07; brief below). One slide per book, each with an image:
Butterfield (1931/1949, his photograph); Kuhn (1962, portrait and one slide)
and constructivism after him; Horton (1967, a Yoruba divination tray);
Westfall and Dobbs on Newton's alchemy (1971/1975, Kneller's Newton);
Eisenstein (1979, Tycho's quadrant); Shapin and Schaffer (1985, Shapin's
portrait, Boyle's pump); Biagioli (1993, Galileo's title page); Findlen
(1994, Imperato's museum); Shapin on trust (1994, Sprat's frontispiece, and
the Harvard computers for Theodore Porter's trust in numbers, published
1995); Shapin's *Scientific Revolution* (1996, "no such thing" and who was left
out); Johns (1998, Flamsteed); a `.parallel` on Eisenstein against Johns;
Pamela Smith's *Body of the Artisan* (2004, Merian); and Maza's own summary
(2017, "all sorts of people"); discussion. Sprat's frontispiece and the
Harvard computers illustrate the subject of the book in whose slot they sit,
not the year. Constructivism is the one slot without a book; it is dated by
decade as the bridge from Kuhn.

*Part three, medicine, as an illustrated historiography in date order*
(third revision, 2026-11-07; brief below), built like part two. The old
story: the Gross Clinic, Rosenberg's portrait, physicians and moralists
(p. xxiii, with Garrison's 1913 survey named), Board's Jenner, de Kruif's
*Microbe Hunters* (1926, Edelfelt's Pasteur, Rosenberg p. xvii on
"discovered"), Snow's map. Then: Sigerist (1930s–40s, Rosenberg p. xiv on
"social"), Foucault (1961, Robert-Fleury's Pinel, p. xvi "tools of social
control"), Rosenberg's *Cholera Years* (1962, King Cholera, p. xx), Crosby and
McNeill (1970s, the Florentine Codex, p. xv and n. 8), McKeown (1976, Fildes's
*The Doctor*, p. xv and n. 7), social construction (1970s–80s, p. xiv), Jones's
*Bad Blood* (1981, Tuskegee), Showalter (1985, the Salpêtrière, n. 9), Porter
(1985, Gillray, p. xv), Ulrich (1990, p. xv), Rosenberg's frame (1992: naming,
diagnosis and identity, disease as social diagnosis with "etiology" glossed),
Arnold (1993, a Bombay plague camp, n. 9); discussion. Then the comparison,
the arc, the take home (Shapin p. 10) and a closing question.

**Rosenberg's own map of the field carries part three.** His p. xv lists the
trends in the history of disease (social history, public health and the
mortality debate, an "ecological vision," demography, disease as social
control), and his notes name McKeown (n. 7), Crosby and McNeill (n. 8),
Showalter and Arnold's 1988 collection (n. 9); the volume ends with Elizabeth
Fee's essay on Sigerist. Every part-three quotation is Rosenberg's, so the
reading stays the spine and the other historians are introduced in
`.detail` lines. Garrison, de Kruif, Foucault, Jones and Porter are not in
the reading.

**What the revision cut,** to make room for part one's cases and keep Kuhn
short: Maza's thesis slide (now the pattern slide's headline), the textbook
history-of-ideas slide (folded into the Lovejoy slide), the separate things
slide, the clocks quotation, the Kuhn p. 1 slide (its "tourist brochure" line
kept as a fragment), the paradigms slide, Copernicus, the duck-rabbit, the
Week 4 Voltaire and Ranke pointers, Imperato's museum, Pasteur, the separate
"frame" slide (now a fragment on the naming slide) and the machine-readable
block. Ulrich and Boyle now each recur, and Ulrich gets a portrait because
she returns in part three.

**The two progressions** the brief asked for are carried by the eyebrows'
dates and by the comparison slide: science from Butterfield (1931/1949)
through Kuhn (1962), constructivism, trust and print (1980s–90s) to inclusion
(who did science); medicine from physicians' histories through
patients (1970s) and construction (1980s) to Rosenberg's frame and race
(Tuskegee). The comparison's `.compare` block ties both to the course's own
path (Ranke → from below → gender → linguistic turn).

**The underlying question** opens the deck (cold-open headline), returns in
each discussion (part one: whom new sources let historians see; part two: whom
you trust; part three: what a name changed),
and closes it (take home; "what will historians say we got wrong").

**Introduce before you quote.** Shapin, Kuhn, Rosenberg and (since the
revision) Ulrich get portraits before their words. Maza is the narrator.

**Part one's explainers show the thing, not the historian.** The guide says
every named person gets a portrait if one exists, and that an explainer can
introduce a person and their idea together. Skinner, Darnton, Norton and
Riskin each matter for one case, and the brief asked for the things historians
studied, so their explainers picture the object (*The Prince*, a libelle, the
codex, the clock), name the historian in the eyebrow, and introduce them in
the first `.detail` line. No headline makes them its subject. Breen is
treated the same way. Lovejoy is named in the Valadés caption and the
eyebrow of the slide after it.

**Explainers and the 644px line.** With a two-line headline, a portrait-shaped
image capped at 380px and a one-line credit, an explainer measures just under
the checker's line; a two-line credit or a three-line headline pushes it over
(the guide's note on `.with-figure.wide` says the same). So the explainer
slides drop the rule under the headline, as `linguistic-turn`'s do, keep
headlines to two lines, and cut credits to one line, identifying the image in
the cite or `.detail` instead (see `images/README.md`). Golinski, Norton,
Riskin and Breen are voices through Maza or Shapin; no headline makes them
its subject. In the second revision, the part-two explainers do make their
historians the headline's subject (Butterfield, Horton, Westfall and Dobbs,
Eisenstein, Johns), as the guide allows an explainer to introduce a person and
their idea together; each is introduced in a `.detail` on the same slide. On
the Eisenstein slide the quotation is Johns's summary, so its cite calls him
"her critic," since the checker does not allow a `.detail` above the quote (Skinner's headline was changed to "intellectual
historians" for this reason). One headline makes "Shapin and Schaffer" its
subject: Shapin is introduced, and his caption names Schaffer as co-author,
which the deck treats as enough. Charcot, Merian and Gross are
named only in captions.

**`scripts/deck-check.mjs` was changed for this deck (2026-11-06).** It
treated every `figure.portrait` caption as a person's introduction and took
the last word before the first tag as a surname, so the Valadés and Boyle
captions registered "from" and "of" as people, and every headline containing
those words failed `before-intro`. It now counts a portrait caption as an
introduction only when its first line has the "Name · dates" form. Checked
against `inventing-nations`: same results before and after (its five FAILs
are pre-existing overflows on slides 15, 19, 28, 33, 37).

## Facts from outside the readings

Standard, none quoted, third revision: Garrison's *Introduction to the
History of Medicine* (1913) and his army career; de Kruif's *Microbe Hunters*
(1926) and his training; Edelfelt's 1885 Pasteur; Sigerist at Johns Hopkins
(1932–47), his subjects and his return to Switzerland; Foucault's *Madness and
Civilization* (1961) and its reading of Pinel; Robert-Fleury's 1876 painting;
the epidemics of *The Cholera Years* and its sin-to-sanitation argument;
Crosby's and McNeill's subjects; McKeown's nutrition argument; Jones's *Bad
Blood* (1981); Showalter's subject; Porter's 1985 essay title; Arnold's
*Colonizing the Body* (1993), Bombay's plague measures and his argument
about resistance; the Florentine Codex's artists.

Standard, none quoted: Butterfield's *Whig Interpretation of History* (1931),
and the deck's reading that his 1949 book told science the Whig way "himself"
(a common observation, made here through Shapin's use of the quotation);
Merian as painter and engraver;
the Butterfield photograph (before 1951, per Commons); Horton's work in
Nigeria; Kneller's 1689 Newton; Gibson's 1712 Flamsteed; Tycho's mural
quadrant (1598); the 2002 *American Historical Review* exchange between
Eisenstein and Johns; Shapin's and Kuhn's and Rosenberg's careers; *The Cholera Years*
(1962); Valadés's birth in Tlaxcala; Merian's voyage to Surinam (1699, at
fifty-two) and her informants; Pickering's computers and their pay; the
Gross Clinic's setting; Pasteur's rabies vaccine (1885); Snow's map (1855,
for the 1854 outbreak) and his note that deaths were already falling; Jenner
and cowpox; Charcot and hysteria; Leech's *Punch* print; the Tuskegee study
(1932–1972, about 400 men with syphilis, untreated after penicillin);
added 2026-11-07: Morande's *Gazetier cuirassé* (1771) as an example of the
libelles Darnton studied (the slide says "pamphlets like," not that Darnton
discussed this one); the Edenton pledge; Ulrich's career and *A Midwife's
Tale* (Martha Ballard's diary, 1785–1812, Hallowell, Maine; 814 or 816
births by different counts, so "more than eight hundred"; Pulitzer 1991);
Boyle's comparison of the world to the Strasbourg clock (*Free Enquiry*,
1686), paraphrased; Galileo's Medicean stars as printed on the title page;
Merian's note that Indigenous and enslaved women used the peacock flower's
seeds to end pregnancies, and Schiebinger's *Plants and Empire* (2004);
Board's Jenner, dated about 1910 by Commons (the commission, if any, is
unconfirmed, so the caption does not name one); Cruikshank's print as a
satire of male midwifery (Wellcome's description); a
1985 essay "The Patient's View: Doing Medical History from Below" (Roy Porter,
*Theory and Society* 14), named since the third revision on its own explainer,
paraphrased because no cache holds it. The
"physicians' version" block in part three (great men from Hippocrates to
Pasteur, written by doctors for doctors) is the deck's summary of the older
historiography, which Rosenberg only gestures at (p. xxiii).

## Quotations and how they were checked

Text caches, all in `~/Dropbox/courses/making-history/.research-packets/`,
made 2026-11-06:

- `maza-thinking-about-history-ch3.ocr.txt` — pp. 83–117, printed-page markers
- `shapin-scientific-revolution-intro.ocr.txt` — pp. 1–15
- `rosenberg-framing-disease-intro.ocr.txt` — pp. xiii–xxvi; spreads
- Kuhn: the course PDF `Kuhn-SSR-2ndEd.pdf` has a clean text layer (printed
  page = PDF page − 12); pp. 1, 3 and 111 quoted from it

Every quotation was matched word for word against these caches by script.
Checked against the page images as well: Shapin pp. 1–2 (the opening and
Butterfield), Maza p. 91 (salonnières), Rosenberg pp. xvi–xix (sympathy and
insurance; "discovered" microorganisms; the epileptic). **Not yet checked by
eye:** the remaining Maza pages (84, 85, 87, 88, 90, 92, 93, 95–101, 105–108),
Shapin pp. 4–5, 8, 10, and Rosenberg pp. xiii–xv, xx–xxiii. The word match
is strong evidence but does not settle punctuation.

**Quotations added 2026-11-07** (Maza pp. 84, 86–87, 88, 89, 90, 92, 104, 107,
108) were matched word for word against the Maza cache by script, as was
every other quotation in the revised deck. The script's only misses are known:
the Lovejoy sentence crosses the p. 86/87 page break with footnotes between,
"hostess-mediators" breaks at its hyphen, the Ulrich line drops Maza's tag
(below), the Butterfield, epileptic and insurance lines were checked on the
page images, and the rest are titles, translations or quotations from outside
the readings (Thompson; the 1985 essay).

Notes on particular quotations:

- **Ulrich (Maza pp. 105–106)** drops Maza's attribution tag: the original is
  "The mythology of homespun persists," Ulrich concludes, "because it allows…".
- **Maza p. 91, "hostess-mediators"** breaks across a line at the hyphen; read
  as a hyphenated compound.
- **Rosenberg p. xvi** prints "the insurance reimbursement, connection with an
  agreed-upon diagnosis" (a dropped "in"); the slide quotes up to
  "reimbursement," and paraphrases the rest.
- **Norton** is quoted only through Maza's sentence about her (p. 107); the
  headline carries Norton's "from the colonized to the colonizer."
- **Kuhn p. 111** (the duck-rabbit line) is outside the assigned pages 1–22.

**Cold review, 2026-11-06.** Fifteen findings from a fresh-context agent,
each verified against the sources and acted on except as noted:

- *Reversed claim:* the "machine-readable" block made people the
  machine-readable thing; Rosenberg (p. xxi) says diagnoses are, and people
  are "not so easily categorized." Fixed.
- *Wrong pointers:* the Week 4 Ranke pointer implied he judged the past (his
  1824 preface refuses to); the Week 4 progress pointer gave Voltaire Kant's
  direction (enlightenment-progress-2: Voltaire ranked four ages, Kant argued
  for a direction); the Week 10 pointer said constructionists thought we
  reach diseases only through words, which Rosenberg does not say. Fixed.
- *Misreadings:* Ulrich tied the English recipient's family, not the
  giver's, to King Philip's War (p. 105); the trust slide quoted Maza's
  general "they argue" (historians) under a headline about Shapin, so it now
  quotes her Shapin sentence (p. 98, checked on the page image); the Gillray
  caption added "families" to Rosenberg's list (p. xx); "the degree of
  arbitrariness" is on p. xiv; Maza says servants, "especially" women.
- *Images:* in the *Air Pump* only the older girl hides her eyes; in the
  Tuskegee photograph the needle is in the arm of the man at the left edge.
  Notes bullet and alt text fixed.
- *Overclaims and dates:* "began as a relay" (a metaphor; Maza calls the
  great-thinkers version the simplified textbook form, p. 87); "1870s–1950s"
  (Maza: "through the Cold War"); "The 1980s · construction" against
  Rosenberg's late 1960s to mid-1980s; "pornography about the queen" from one
  title; "the cyclotron of its age" is a scholar quoted by Maza. Fixed.
- *Tension now stated:* Shapin p. 8 (most people shut out) against Maza
  p. 101 (all sorts of people practiced science). The arc card and the
  comparison now say shut out of formal learning, not out of practice.
- *Discussion:* the part-two question ("whom do you trust?") could be
  answered without the reading; it now turns on Boyle's chosen witnesses,
  with Maza p. 98 ("expertise backed by numbers") as the takehome. **Not
  changed:** the part-one question, which the reviewer also flagged; it draws
  on three cases from the reading and asks the student to sort them.

## Open questions

**The schedule's Rosenberg pages are wrong.** `schedule.md` gives "12–23";
the introduction runs pp. xiii–xxvi in the printed book (the PDF's sheets
4–11). The deck cites the roman numerals and the title slide says so.
Consider changing the schedule line.

**Resolved in the fourth revision:** Kuhn's portrait (the 1.41× warning) and
the Codex Tudela image are gone with their slides.

**Possible cuts if the session runs long.** The deck has 66 slides, 37 of
them images or explainers. Part three now has 22; its least load-bearing are
Snow's map, the Sigerist explainer and the Salpêtrière. Earlier list: The least load-bearing: the Breen slide (part
one's goods-as-politics case), the Horton explainer (Maza's point survives on
the "who did science" slide), Imperato's museum (Findlen is one name too
many), Galileo or Merian (one "who did science" image would do), and King
Cholera. Part two has 22 slides; if it runs long, cut Horton and Imperato
first, and keep the Eisenstein–Johns pair together.

## Cold review of the revision, 2026-11-07

A fresh-context agent checked the new and changed slides. Every quotation
matched word for word with the right page. Its findings, each verified and
acted on except as noted:

- *Part one discussion and arc card:* the takehome said Ulrich brought "an
  Algonquian woman" into history, but the woman was already in the 1842 note;
  Ulrich exposed the peace story (p. 105). Norton's sources were invented
  ("colonial households"; Maza does not name them). The question now asks only
  about Darnton and Ulrich, and the card was rewritten.
- *Part one fed nothing at the end:* the arc headline now reads "Ideas,
  things, science and disease," and card 01 names things acting on people.
- *Medicine's critical turn was abstract:* Ulrich's *A Midwife's Tale* now has
  its own explainer; the 1985 essay is named as Roy Porter's; the physicians'
  block gains Rosenberg p. xix ("paid too much attention to plague and
  cholera"). The block's opening sentence remains the deck's summary (see
  "Facts from outside the readings").
- *Science's inclusive turn told without historians:* Westfall and Dobbs
  (Newton) and Biagioli (Galileo) are named; Galileo and Merian return on the
  comparison slide.
- *"Paradigms, not progress"* contradicted Maza p. 95 (Kuhn believed in
  progress): now "Paradigms, not accumulation."
- *Paraphrases with wrong cites:* the Codex Tudela was inside a sentence cited
  to p. 107 (moved out); Darnton's cited sentence named Morande's 1771
  libelle rather than Maza's 1780s titles (now *The Pastimes of Antoinette*,
  and the picture is identified as an earlier libelle); Skinner's "only its
  contemporaries can say" became "only wide reading in the writings of the
  time can tell."
- *Breen* was never introduced and the print's date did not match the 1765
  boycott: introduced in the `.detail`, pledge dated 1774, named on the
  pattern card. *The salon* now names Dena Goodman (from Maza n. 14). *The
  basket* block now says Ulrich started from the object, as a curator would.
- *Discussions:* part two's question could be answered without the reading;
  it now asks which of Maza's "all sorts of people" Boyle's gentlemen would
  have refused as witnesses. Part three's now uses Rosenberg's own list
  (p. xiv). Its takehome adds an outside fact: American psychiatry listed
  homosexuality as a disorder until 1973.
- *Four text slides in a row* in part two: Sprat's frontispiece moved back
  between "Trust" and "who was left out," which also shortens the old story.
- **Not changed:** no part opens with a `.detail` line, because the checker
  fails commentary placed above a slide's quotation and each part opens on a
  quote slide. The science old story is still six slides (four of them
  images); the Shapin pair also opens the critique.

## Cold review of the second revision, 2026-11-07

A fresh-context agent read part two, the comparison, the arc and the
citation-note against the caches. Every quotation it did not flag matched
word for word. Its findings, each checked against the sources:

- *Eisenstein slide quoted Johns under her headline* before Johns appeared.
  The cite now reads "Her critic Adrian Johns … summarizing Eisenstein"; her
  own text was not available (see the second-revision note above).
- *Harvard computers caption implied Shapin studied them.* Maza's n. 42 only
  points to Shapin's ch. 8 (on Boyle-era technicians). The caption now carries
  Theodore Porter's trust in numbers (Maza p. 98), which Maza dates to the
  nineteenth century and which part two had lost.
- *Discussion answerable from the slides alone.* Now asks who is right,
  Shapin ("scarcely at all," p. 8) or Maza ("all sorts of people," p. 101),
  and what each counts as science. The arc card states the disagreement
  instead of settling it.
- *Coverage of Maza pp. 92–101.* Added Kuhn's definition of a paradigm, with
  anomaly, crisis and Copernicus (p. 93); the "symmetry postulate" (p. 95);
  Porter; and Pamela Smith's artisans (p. 101 n. 41), which replace Londa
  Schiebinger (not in Maza) on the Merian caption. Not added: "snapshot"
  studies (p. 95) and the title of Shapin's *Never Pure* (p. 99), which the
  throughline echoes without quoting.
- *Newton:* the headline now credits Westfall and Dobbs, and the quotation
  begins at Maza's "rooted in"; the deck's lead-in paraphrases her
  "breakthroughs leading to … universal gravitation."
- *Horton's tray* is now labeled "an illustration, not his evidence." Horton's
  own fieldwork was among the Kalabari of the Niger Delta, not the Yoruba.
- *Johns:* the headline names Eisenstein as the one he answered; the detail
  says Flamsteed, not his catalogue, is pictured.
- *Comparison and arc:* the science track is in date order, Horton replaces the
  "African healers" no slide showed, and card 02 reads "Butterfield to Smith,
  1931–2004."
- *Citations:* Butterfield is cited to Shapin p. 1 (not pp. 1–2); the
  citation-note says Eisenstein appears only through Johns and Butterfield
  only through Shapin; the takehome names each work with its page.
- *Butterfield:* "most historians of science" became Maza's "historians of
  science," and the geniuses phrase is now her quotation.

After the fixes: build clean; deck-check 60 slides, 0 FAIL, 1 WARN (Kuhn
portrait, 1.41×); slide-words over target but within hard stops on the Merian
caption (43), the Gross caption (44), the Sprat caption (41), the first notes
bullet (41) and the takehome (31); quotation check 83 strings, all misses the
known ones listed above.

## Cold review of the third revision, 2026-11-07

A fresh-context agent checked part three, the comparison, the arc and the
citation-note, and read the whole deck for jargon. It checked every part-three
quotation against the cache, and the spread pages (pp. xiv–xix) against page
images; all matched. Its findings, each verified against the pages:

- *Discussion failed the reading test and took a side.* On p. xix Rosenberg
  says the historian "can hardly decide" whether the homosexuality diagnosis
  helped or harmed; the old takehome settled it as stigma, and "the name
  changed" was wrong. The question now asks why he can't decide; the takehome
  uses his "unspeakable acts" and "for better or worse" (p. xix).
- *De Kruif:* "discovered" read as doubt about Pasteur. The detail now says
  the quotation marks flag claimed microbes that caused nothing (p. xvii).
- *Rosenberg's map of the field was never shown.* New `.cards` slide after
  Ulrich: his trends (pp. xv–xvi, public health and demography merged into one
  card to fit) and what all of them missed, the process of definition and its
  consequences (p. xvi).
- *McKeown stated flatly:* the slide now says the claim drew controversy
  (n. 7); the comparison says "doubts about medicine's credit," not doubts
  that lives lengthened.
- *Two Porters:* Roy Porter is named in the eyebrow and headline; his quote
  is framed as one of Rosenberg's trends; the essay title left the `.detail`.
- *Overstatements:* "biology often shapes" (p. xv), "often carried" (p. xxii),
  "shapes" on the arc card, and the Sigerist line hedged ("could be
  Sigerist's").
- *Arnold:* Rosenberg cited Arnold's 1988 collection, not the 1993 book; the
  slide and citation-note now say so.
- *Foucault:* the English translation (1965) is dated, so the 1961 slide
  doesn't imply early American influence; "deviance" is glossed.
- *Sequence:* Snow's map moved beside Jenner, both as the physicians'
  version; Garrison's book is named; the social-diagnosis slide moved after
  construction, ahead of Tuskegee and the Salpêtrière, which keeps the three
  Rosenberg 1992 slides from running four text slides in a row.
- *Week 10 block* now links its two sentences; *Eisenstein–Johns block* names
  both for the 2002 exchange.
- *Jargon list:* most of it adopted (throughline, hierarchy headline, Skinner,
  "hack writers," Ulrich's basket, the Codex Tudela, the constructivism label,
  Horton, Tycho's "models of the universe," *Leviathan* glossed, Johns, the
  physicians headline, the Cholera Years headline, the comparison tracks, the
  closing headline, the title translations).

**Not changed, and why.** The guide says no `.detail` contains a quotation,
but every explainer in the deck (eighteen of them) carries short quoted
phrases in its `.detail` lines, as the explainers in earlier decks do;
rewriting all of them is a separate decision for the author, and the guide may
need to say whether explainer details are an exception. The part-opening
`.detail` is still missing for the reason given under the first review.
Optional suggestions not taken: AIDS as its own slide, a COVID tie-in, and
Pinel's unchaining as partly legend.

After the fixes: build clean; deck-check 66 slides, 0 FAIL, 1 WARN (Kuhn
portrait, 1.41×); slide-words over target but within hard stops on eight items
(captions for Boyle, Gross, Merian and Sprat; details for Johns, Horton and
Skinner; one takehome; the first notes bullet); quotation check 96 strings,
all misses known (titles, translations, outside sources, OCR errors, page
breaks).

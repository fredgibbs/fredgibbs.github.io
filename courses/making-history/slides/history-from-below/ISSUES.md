# Open issues — History From Below (6.1)

Contributor notes, excluded from the build. Deliberate deviations are recorded
here so a later review does not raise them again.

## Deliberate deviations

**Fair use for `images/vansina-portrait.jpg`.** No free portrait of Jan
Vansina (d. 2017) exists; Commons has none. Taken from the UW–Madison history
department's memorial notice, kept at the source's own 407 × 298, shown for
identification and commentary. Full reasoning in `images/README.md`. Do not
delete as unlicensed.

**The Vansina slide is a `figure.landscape`, not a portrait rail.** The rule in
`courses/SLIDE-STYLE.md` puts a person's introduction in the caption rail of a
`figure.portrait`. This file is 407 × 298 and landscape; classing it `portrait`
would misdescribe the image, and it cannot be cropped to portrait at a usable
size. The caption carries the full introduction — name and dates, bio, a
`<span class="why">` line, credit — underneath instead. The word budget follows
the caption's job, not its tag, so it is held to the 80-word introduction
budget; `scripts/slide-words.py` scores it that way.

**The cold open is two images in sequence, not a pair.** It ran Peterloo
against the Conakry postcard until 2026-09-20. That *pair* was cut because it
had no controlled variable, which is what makes the other cold-open pairs
work: `annales-longue-duree` holds the Mediterranean constant and changes the
time-scale, `marx-structural-history` holds the pastoral genre and the decade
constant and puts industry in the frame. Peterloo against Conakry changed
continent, century, medium, maker and purpose all at once, so the only thing
the two shared — many people, few names — had to be asserted by the bullets
rather than shown by the pictures, and those bullets were the longest text in
the deck. **That ban still stands: don't put two images on one notes slide
here without a variable you can name in a clause.**

On 2026-09-22 Lepanto was added *before* Peterloo, which is a different
structure and not a re-pairing. Each image is full-bleed and then gets its own
`.image-notes` slide, which is the form `courses/SLIDE-STYLE.md` prescribes
for two images ("a second image repeats the pattern"), and no bullet is
written across the two. Lepanto is a callback, not a contrast: students met
this exact painting in 5.1 as Braudel's event, and 6.1 asks the same picture
a different question — the oars are drawn and the rowers are not. It runs
first because it is the way of writing history the session is about to argue
with; Peterloo is then the escalation, a crowd that assembled *to be counted*
politically and was still recorded as a crowd. The framing question still sits
between Peterloo and its notes slide, so the cold open asks before it unpacks.

If the opening ever needs shortening, Lepanto and its notes slide are the two
to cut: Peterloo carries the point alone, as it did before.

**The colonial postcard opens part three instead.** `griot-conakry-c1910.jpg`
is a staged ethnographic card, not documentary evidence of a griot performing,
and it is used as one — a source that types people rather than naming them.
In the cold open it introduced the griot and the colonial record twenty-five
slides before Vansina appeared and anyone could use either. At the head of
part three it answers the question the slide before it leaves open — Thompson's
method runs on paper, so what does the record look like where there is none.

**Narrowed from three bullets to two on 2026-09-22.** The slide was carrying
three arguments and the picture shows one of them: the griot-as-archive is
carried by the caption explaining what an `ngoni` is, and the market inference
was not in the frame at all. The typing point ("a type, not three people") had
also become the deck's third run at names-versus-categories once Lepanto was
added to the cold open — Peterloo's "Then read who is not named" now does it
better, on a source students have just spent two slides reading. What remains
is the one job only this image can do, plus the qualification that it is a
studio product and not documentary evidence of a griot at work. That
qualification is not optional: see `images/README.md` before rewriting the
caption or the bullets.

**The women bullet rests on ethnography, not on this photograph.** Added
2026-09-22 after the narrowing, because the slide identified the man by his
instrument and left the two women as scenery — repeating the card's own move.
It is phrased conditionally on purpose: the Mande gendered division of labour
(instruments men's, song largely women's) is well documented, but whether
these two sitters were performers is unrecorded and unrecoverable. Sourcing is
in `images/README.md`. A fresh-context review should check the claim is still
conditional and has not drifted into asserting who they were.

**A photograph cannot show an oral tradition**, which is the standing limit on
this slide. Vansina's subject is verbal messages transmitted across
generations; a still image can only gesture at it. If a better image for part
three ever turns up — a transcription notebook, a recording session, a named
informant — it is worth the swap.

**The three discussion slides are merged, not paired.** Until 2026-09-22 each
part ended with a question slide and a separate answer slide. They are now one
slide in three beats — topic as the `.main-point`, the question as a
`.question` fragment, the crux as a `.takehome` fragment — which is the pattern
`courses/SLIDE-STYLE.md` now prescribes for new decks. The merge dropped each
pair's `.reveal-block` of working; its substance was folded into the takehome,
which is why all three takehomes run longer than they did. The thing the old
two-slide form protected against was an early arrow key revealing the answer
while the room is still talking. That is now a presenting habit, not a
structural guarantee.

## Open questions

**The cold open's Hunt bullet cites Thompson pp. 622–23, outside the assigned
range.** The title slide assigns the Preface and ch. 1. The identification of
Henry Hunt — wealthy gentleman-farmer, the day's main speaker, gaoled for it —
and Thompson's explanation of why the movement looked to a gentlemanly leader
are from ch. 15, "Demagogues and Martyrs". Both were checked against the page
images, not the PDF's text layer. It sits on an `.image-notes` slide, which is
presenter-facing type, so it is background for whoever is delivering rather
than something students are expected to have read; the page numbers are there
so it can be looked up. Don't promote it to a `.quote` slide without either
assigning the chapter or dropping the citation.

**Two assigned page ranges are never used.** The title slide sets Thompson
"Preface and ch. 1, 1–25" and Vansina "ch. 1, 1–13 and 27–31", matching
`schedule.md`. Every Thompson quotation in the deck comes from the Preface
(printed pp. 9–13); **chapter 1, "Members Unlimited" (pp. 17–25), is never
touched** — no London Corresponding Society, nothing. Vansina pp. 1–13 fare
slightly better, since the oral-history distinction is pp. 12–13 material, but
the whole of "the generation of messages" (news, interpretation) is unused.
A student who does the reading has read about twenty pages the hour never
mentions. Either the assigned range should shrink or the deck should grow; the
first is the instructor's call, and nothing here is wrong as it stands.

**No image for Part One's quantification section.** Parts two and three each
get two or three image breaks; part one gets only Henry VIII, so the run from
"the 1960s turn" to the first discussion slide is four text slides. A census
schedule or an enumerator's book page would fit the argument exactly, but
nothing usable turned up on Commons (searched 2026-09-19: parish registers,
1841/1861 census schedules, punched-card equipment — all either PDFs of
printed reports or nothing). A manuscript page also risks reading as murk at
projector distance. Worth another look in a national archive's own digitised
collections.

**Thompson's page numbers are from the Vintage printing.** That is the PDF in
the course Zotero library, and the numbers match Maza's citations of the same
edition (her n. 30 gives p. 12 for the condescension passage, as here). A
student reading the Penguin will find different pagination for the preface.
Worth a word out loud.

**Vansina's earlier method book is cited without a date.** The caption says
"an earlier method book of his, twenty years on" because the sources to hand
disagree: the UW–Madison obituary gives *La tradition orale* (1960), Wikipedia
gives 1965 for the English *Oral Tradition: A Study in Historical
Methodology*, and the French original is usually dated 1961. Undated beats
wrong. *Living with Africa* (1994), his memoir, would settle it.

## Raised in review and fixed

A fresh-context review on 2026-09-19 found sixteen items. The substantive
fixes, so a later reader knows the reasoning:

- **The deck used to call "no document, no history" Ranke's rule and refer
  back to Week 4 for it.** Both wrong. `scientific-history/index.md` never
  teaches that maxim — what Week 4 gives students is *wie es eigentlich
  gewesen* and the source-apparatus point — and "pas de documents, pas
  d'histoire" is a later positivist slogan (Fustel de Coulanges; Langlois and
  Seignobos, 1898), not Ranke's. Part Three now asks whether Vansina meets
  Week 4's actual standard: claims resting on named sources anyone can check.
- **A gloss on the Vansina "successive documents" slide said written sources
  are "copies of lost copies too. The difference is degree, not kind."** That
  is precisely the model Vansina rejects one page later: "we should not stick
  to a model that handles oral messages as if they were written, with
  originals and copies" (p. 30). Replaced, and the warning is now the point of
  the block.
- **The Himmelfarb quotation was mis-framed.** The quoted words qualify *the
  state*, not "politics", and they are Himmelfarb's own — Maza says she argues
  "following Aristotle", and the Aristotle words are a separate quotation on
  the same page. "Paraphrasing Aristotle" was wrong twice over.
- **"Coffee-houses" belonged to Macaulay's 1848 book, not Trevelyan's** (Maza,
  p. 14). Removed from the Trevelyan list.
- **Maza flags the Trevelyan phrase as disputed** in n. 7 on the very page the
  deck cites — Cannadine argues it is quoted out of context. That caveat is
  now a block on the slide, before the takehome.
- **The Vansina definition slide said he "defines it narrowly, on purpose"**
  and called p. 28 a list of exclusions. Page 28 is Vansina *refusing* two
  narrower definitions (Henige's, Miller's) as "far too restrictive". The
  slide now says he draws one hard line and refuses to draw more, and uses
  that refusal as the second block.
- **Thompson's caption said he taught adult education "rather than taking a
  university post."** Maza says that (p. 23), but the assigned preface
  contradicts it on p. 14: "My grateful acknowledgements are due to the
  University of Leeds and to Professor S. G. Raybould." He held an
  extra-mural post at Leeds, which is the truer and more interesting claim.
  "West Yorkshire" also became "West Riding" — the county dates from 1974, and
  West Riding is Thompson's own word (p. 13).
- **Bare page numbers collided across parts** — "(p. 12)" meant Maza in Part
  One and Thompson in Part Two. Every citation now names its author, and the
  title slide's `.citation-note` says why.
- Smaller: the deck said Thompson "ends his preface" with the Asia-or-Africa
  sentence (a page and a half of apology to Scottish and Welsh readers
  follows); "the label stuck" contradicted the sentence before it; the Fabian
  orthodoxy said "saved by" where Thompson wrote "with the exception of";
  Southcott's engraving is nearly three months before her death, not two; and
  three page citations pointed at ranges that did not contain the words
  (Maza's "eight hundred pages" is p. 25, not 23–24; both losers-slide phrases
  are on Thompson p. 13; the Vansina definition is on p. 27).

**Trevelyan gets no introduction slide, deliberately.** He is an example, not
a figure the deck returns to: one quotation, then gone. The rule in
`courses/SLIDE-STYLE.md` gives a person a portrait slide when the deck then
spends one to four slides on their arguments, which is not this. Maza treats
him the same way — he is the last name in a lineage she runs from Thiers and
Michelet through Macaulay, and her point is about the tradition, not the man.
What the deck was missing was not a bio but that lineage, which is now the
slide before his ("Social history was already a century old"). It carries
Maza's claim that the discipline does not replace one kind of history with
another, the "subordinate and accessory" verdict on the whole tradition
(p. 14), and the crowd sentence from p. 15 — which also closes the Peterloo
loop the cold open opens and nothing else picked up. Trevelyan then arrives as
the close-up on the best-known case, and his headline is about the phrase
rather than the man.

## Checked, not a problem

- **The Luddite inscription is right as printed.** The review flagged
  "Drawn from Life by an Officer" against museum catalog records that read
  "Drawn from the life by an Officer". This impression was examined at full
  resolution: the engraved script reads *Drawn from Life by an Officer*, with
  no "the". The caption follows the object, not the catalog.
- **Every quotation in the deck has been verified against a page image**, not
  a text layer — Thompson pp. 9, 11, 12, 13; Vansina pp. 27, 28, 29, 30, 31;
  Maza pp. 10, 13, 14, 15, 17, 23, 24, 25. The Thompson PDF's embedded text is
  visibly corrupt in places (`iÞed estate`, `ÝÛ`) and is two-page spreads, so
  the images are the authority for anything inside quotation marks.
- **Both second-hand quotations are attributed as "quoted in Maza"**, with the
  right pages (Trevelyan p. 15, Himmelfarb p. 13).
- The throughline slide's `.answer.next` in `annales-longue-duree` promises
  "Week 6 · Thompson, 1963 — People, making themselves, out of what they
  experience and what they do about it." This deck's throughline makes that
  the `.answer.now` and the take home delivers it.
- "Compare 5.1" (Marx, conditions versus agency) and "Compare 3.1"
  (al-Bīrūnī naming his sources, Bede listing who told him what, as the
  neighbourhood for *isnād*) both check out.

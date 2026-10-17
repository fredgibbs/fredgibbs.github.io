# Open issues — The Linguistic Turn (10.1)

Contributor notes, excluded from the build. Deliberate deviations are recorded
here so a later review does not raise them again.

## The slide contract this deck is built on

**The author's brief (2026-10-16):** highlight Maza's quotations, then
Jenkins's; Jenkins is worth teaching because his chapter answers specific
questions, and those questions should be visible; cover Maza partly through
slides on actual historians who shaped the linguistic turn; and where the turn
connects to postmodernism, outline postmodernism the way Jenkins's chapter
does.

**Maza first, in the order of her chapter, then Jenkins in the order of his.**
The headlines read in order as one argument:

1. **Part one, objectivity (Maza pp. 199–208).** History may not make things
   up, yet every account is a set of choices (p. 199), framed with the
   schedule's first question. The 1880s ideal of objectivity (Novick, quoted
   on p. 201); the homogeneous room that made it easy (p. 201; the 1919
   Paris photograph); women and Black scholars in the 1970s (p. 204); the end
   of "Olympian detachment" (p. 205); Sima Qian, then objectivity as a Western
   convention (pp. 206–208). Discussion.
2. **Part two, the linguistic turn (pp. 209–216).** Maza's genealogy as a
   `.flow` (Saussure, Lévi-Strauss, Derrida, historians), the antihumanist
   cost, the climate that reached historians who never read the theory, the
   turn itself, and fiction as "made, not false" (p. 211). Then three
   historians, each with a portrait before their words: Davis and the pardon
   tales (p. 212), the Fool's Cap Map for Maza's point about maps (p. 214),
   White and his plots (pp. 214–215), Scott (p. 216). Discussion: a history
   without narrative, the schedule's second question.
3. **Part three, the critics and the line (pp. 220–232).** Elton's alarm
   (p. 220), the real philosophical challenge (p. 221), Evans's moral
   objection (p. 222), Maza's correction that almost no historian who took the
   turn doubted the past (p. 223), qualified objectivity (p. 224), the
   embargo on invention (p. 225), Maza's three cases (pp. 226–231), Coras's
   title page, and Davis against Finlay as a `.parallel` (p. 232). Discussion:
   the schedule's third question, story or lie.
4. **Part four, Jenkins (pp. 70–84).** Portrait, then a `.cards` slide of the
   four questions his chapter answers, three of them in his own words (pp.
   71, 72, 81–82; his second section has no question of its own, so its card
   names the section). Every later Jenkins slide carries its question in the
   eyebrow: "Jenkins · question 1 · what it means", and so on. Postmodernism
   is outlined as he outlines it: Lyotard's definition, the death of centres,
   the metanarratives, his explanatory story of value as a `.flow`, the end
   of foundations; then redescription after Rorty, the genres,
   power/knowledge, the two readings of the flux, his position, history
   redefined; then the unpositioned centre and his two proposals.
   Discussion: can Jenkins still tell Bellesiles from Davis?

Then the arc (four cards, one per part), the take home, and 10.2.

**Every slide is one of the guide's types.** Quote slides carry a headline,
one quotation and at most a `.reveal-block.compare`. There are no
`.reveal-block.unpack` fragments on quote slides; the first draft had three
(Davis's pardon tale, White's four plots, Jenkins's redefinition of history)
and each became its own slide or was cut. Two writers who disagree share a
`.parallel` with equal billing: Jenkins and Widdowson on the flux, Finlay and
Davis on imagination.

## Decisions

**The reading changed during the build.** The schedule first assigned Maza
"Ch. 8: The Questions of Narrative", pp. 204–211. Maza has no chapter 8; pp.
204–211 are the middle of ch. 6, "Facts or Fictions?", which runs pp.
199–238. Partway through, the author changed the schedule to ch. 6, pp.
199–230, and the deck was extended to cover the new pages: part three is the
result. The Davis–Finlay exchange it ends on is on p. 232, two pages past the
assignment; the `.citation-note` says so.

**Maza's correction on p. 223 shapes the deck.** She says almost none of the
historians who took the linguistic turn "professed disbelief in the reality of
the past," that "no major scholars actually wrote postmodern works of
history," and (n. 54) that Evans's targets were mostly theorists such as
Jenkins, while he "wrongly identifies as 'postmodernists'" historians such as
Davis. So the deck keeps the historians of the turn (Davis, White, Scott)
apart from the theorist of postmodernism (Jenkins). Don't let a later edit
call Davis a postmodernist.

**Maza calls White "the literary theorist" (p. 214).** The caption calls him
trained as a medieval historian, which is also true (Michigan PhD, 1956). The
two are not in conflict; the caption says what put him in a position to write
*Metahistory*.

**The satire card is White's, not Maza's.** Maza names the four modes and
gives examples for three (p. 215). The satire card's gloss is from White's
*Metahistory*, and its `p.cite` says so.

**Part four opens with the portrait, not the work.** `SLIDE-STYLE.md` prefers
opening a part with the work. `gender` opens its part two with Scott's
portrait, and here the work has no image better than a typographic title page.
The caption carries the book: date, kind, and Maza's note on who attacked it.

**Images do argumentative work in four places.** The 1919 Paris photograph is
the "homogeneous" profession at the height of its influence. The Fool's Cap
Map is a map that is plainly about its makers' "mental universe." The Berlin
photograph sits beside Jenkins's claim that "actually existing socialism"
turned Marxism pessimistic. Coras's title page is the source Davis and Finlay
were reading differently.

## Open questions

**The deck is long: fifty-eight slides, thirteen of them images.**
`inventing-nations` runs thirty-four. If it needs to come down, candidates in
rough order: the Elton slide; "Few historians read the theorists"; the
Lyotard and Nietzsche portraits; "the death of centres"; the two readings of
the flux; "History, redefined"; "Olympian detachment". Part three could also
lose Elton and the moral objection and keep the rest.

**Image breaks are thin in part four.** After the Nietzsche portrait there are
nine content slides and a discussion without a picture. No usable image for
Rorty, Foucault (Commons has 207×246) or Widdowson was found. A heritage-site
photograph for Jenkins's "heritage histories" would fit before the flux slide.

**Four portraits are under 1.5×.** `scripts/deck-check.sh` warns on Sima Qian
(1.27×), Davis (1.34×), Scott (1.25×, the file from `gender`) and Jenkins
(1.03×). Each is the largest copy found; see `images/README.md`.

**Two portraits are fair use.** Hayden White (Freie Universität Berlin) and
Keith Jenkins (a frame of a 2013 St Mary's University interview). See
`images/README.md` for the search and the reasoning.

**Some caption facts come from outside the readings.** All standard, none
quoted: the biographical lines for Davis, White, Jenkins, Lyotard and
Nietzsche; that *La Condition postmoderne* began as a report for Quebec's
universities council; the 1919 photograph's date and place (from the Signal
Corps caption); Coras's first edition of 1561; the Berlin photograph's date
(late 1989, uncertain between November and December; the caption says "late
1989").

## What the fresh-context review caught (2026-10-16)

A cold reviewer read the deck against both text caches. Every quotation
matched at its cited page. Fifteen findings, all verified and worked:

- *The Davis caption* said *Martin Guerre* "read court records"; the trial
  records are lost (Maza, p. 230). It now says pardon letters and a judge's
  account.
- *Part one overstated Maza.* The question and arc card tied objectivity's
  fall to a diverse room. Maza says the 1950s–60s newcomers "did not usually
  question" it (p. 203), and the blow was identity made part of the
  scholarship (p. 204). The question now asks why that was the blow. "The
  particular perspective of the white upper-class men" (p. 208) is now
  attributed to the dissenters, as Maza does.
- *Maza does not draw the line.* "Agreement reigns *in principle*" (p. 225)
  is kept wherever the embargo is quoted, and the part-three takehome now
  quotes her question (p. 229) instead of ruling on Davis. Slide one's
  quotation now includes her opening "On the face of it… a bright line".
- *Widdowson was on the wrong side.* In Jenkins he describes the danger, not
  the hostile reading, and he is Jenkins's ally ("après Widdowson", p. 80).
  The track is relabeled and no longer splices in the nested "No meaning. No
  classes. No history."
- *The throughline stated the radical claim in the deck's voice.* It now
  reads "Sources read as texts, and histories as made things." The Jenkins
  caption no longer says he "accepts the linguistic turn whole."
- *Jenkins's standard* is reflexivity, a history "aware of what it is doing"
  (p. 82), not "effects in the present"; both takehomes changed.
- *White's plots* are "not usually a conscious choice" (p. 215); the caption
  no longer says he "chose" them.
- *Davis's reply* got back its antecedent, "in part my invention".
- *The redescription quotation* had an ellipsis that dropped Jenkins's point
  about historians' wish to "be in control"; the passage is now whole, and the
  Nietzsche caption says Jenkins borrows the words, not that he recommends
  them.
- *Lyotard:* "summarizing," not "quoting"; the full English title; the caption
  no longer claims Jenkins's spelling "towards" for the translation's phrase.
- Smaller: the moral-objection headline is hedged ("many historians'"); the
  foundations headline is attributed to Jenkins; the cases cite is pp.
  225–232; the satire card cites *Metahistory* pp. 7–30; Abraham "denied
  deliberately inventing documents"; the Berlin caption no longer implies p.
  74 is about 1989; the 6.2 pointer no longer clashes with Maza's 1970s; the
  1919 caption limits "homogeneous" to the historians in it.

Kept on purpose: the Fool's Cap Map. The reviewer called it a weak example,
since a satirical map wears its "mental universe" openly. That is why it is
there: it makes the point visible from the back row, and the caption now
says it is the linguistic turn's reading, as Maza frames it ("in this
perspective", p. 214).

The reviewer could not verify Jenkins's Nottingham degree or his 2008
retirement (both from his Wikipedia article). The Nottingham line was cut
from the caption; 2008 stays.

## Sources for review

Text caches, in `~/Dropbox/courses/making-history/.research-packets/`:

- `maza-thinking-about-history-ch6.ocr.txt` — pp. 197–238, OCR, printed-page
  markers. Printed page = PDF page − 7.
- `jenkins-rethinking-history-ch3.txt` — pp. 70–84, from the PDF's text layer,
  printed-page markers.

Every Maza quotation was checked against the page image on 2026-10-16: pp.
199, 201, 204, 205, 206, 208, 209, 210, 211, 212, 214, 215, 216, 220, 221,
222, 223, 224, 225, 226–227, 229, 230, 232. Every Jenkins quotation was matched
by script against the text layer, and its page taken from the running heads.

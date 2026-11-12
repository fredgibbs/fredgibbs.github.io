# Open issues — Environmental History (14.2; built as 13.2 and moved on 2026-11-11 when the schedule was corrected)

Contributor notes, excluded from the build. Deliberate deviations are recorded
here so a later review does not raise them again.

## What this deck is

Built 2026-11-11 from the author's brief:

> i need some slides for 13.2 I'm thinking along the lines of the history of
> science and medicine slides, we could do an overview of the historiography
> of environmental history to show its emergence, then a few cronon slides
> that show practical uses, then a few slides on the chalrabarty reading,
> relating it braudel. because i have other stuff to cover, this should be
> brief, both in slide count and words per slide.

**Order (16 slides).** Title. *The field:* backdrop then victim (Gast), the
1970s and the movement (Rothstein's dust storm), nonhuman actors (Serres's
Havana), hybrid nature (Grand Coulee, with a question). *Cronon:* the students'
despair, four practical lessons (cards), Catlin's Comanche riders, four habits
of thought (cards, with a pointer to 13.1), parables (with a question).
*Chakrabarty:* Coalbrookdale, humans as a geological force, Braudel beside
Chakrabarty, freedom and fossil fuels (with a question). Take home; next.

## Second round, 2026-11-11 (22 slides)

> can we have a few more slides about the rise of environmental history as a
> field and the topics it covered. i feel there are some canonical works that
> would resonsate with students.

Six slides added to part one, one book each, in date order, every quotation
from Maza or Cronon: *Wilderness and the American Mind* (1967; Cronon pp. 2–3
and n. 27), *Dust Bowl* (1979; Cronon p. 3), *Changes in the Land* (1983; Maza
pp. 111–12), *Ecological Imperialism* (1986; Maza pp. 113–14), *Guns, Germs,
and Steel* (1997; Maza pp. 112–13, with a question), and a six-card slide of
other subjects (Cronon pp. 3, 9; Maza pp. 111, 115). The Havana slide is now
labeled *Mosquito Empires* (2010). The 1970s slide lost the Dust Bowl photograph
to the new Dust Bowl slide and shows *Earthrise*. In Cronon's practical-lessons
cards, the Dust Bowl card became "Tools depend on culture" (p. 8) so the Dust
Bowl is not taught twice. The "Order" paragraph above describes the first round.

- **Books are named by title, authors mostly not** (the 13.1 convention). Nash
  is named because Cronon's quoted sentence names him.
- **The wilderness slide (1967) follows the 1970s slide,** which frames the
  whole run; the books then go in date order.
- **Checked on the page image:** Cronon p. 3 (Nash, *Dust Bowl*, science and
  gender, fire, cities). The rest of the new quotations were matched against
  the caches by eye. **This round had no fresh-context review.**
- **The pig quotation** drops Maza's tag ("Cronon writes,") by ellipsis.
- **Outside facts:** *Earthrise* is Apollo 8, 1968; Roosevelt and Muir were at
  Glacier Point in 1903; *The Oxbow* is 1836 and shows the Connecticut River.
- `deck-check.sh`: 22 slides, 0 FAIL, 0 WARN; `slide-words.py` within target;
  the eight new or changed slides were screenshotted.
- **If it needs to shrink again,** cut the subjects cards, then *Dust Bowl*.

## Conventions carried over from 13.1, by the author's earlier decisions

These follow `history-of-science/ISSUES.md` (then `science-and-medicine`) (fourth to tenth revisions), not
the guide's default session structure:

- **No throughline, no arc, no dedicated discussion slides.** Questions sit on
  key slides in a `.reveal-block.argument` labeled "Discuss," as a fragment.
- **No portraits of scholars,** so Cronon and Chakrabarty are quoted with no
  introduction beyond the title slide's reading list and the cite.
- **Names are kept to the assigned authors and Braudel.** The historiography
  slides say "historians" and "a 1979 history"; Worster, Crosby, McNeill,
  Diamond, White and Sutter are not named in the deck's voice (Sutter appears
  once, in a cite, because his words are quoted through Maza).
- **Explainer `.detail` lines carry short quoted phrases** ("second nature"),
  as 13.1's do; the guide's "no `.detail` contains a quotation" is still an
  open question there.

## Quotations and how they were checked

Text caches, in `~/Dropbox/courses/making-history/.research-packets/`:

- `maza-thinking-about-history-ch3.ocr.txt` — pp. 108–117 (made 2026-11-06)
- `cronon-uses-environmental-history.txt` — full text, made 2026-11-11 from the
  JSTOR PDF's own text layer, which drops words at line ends and scrambles the
  tops of pp. 3, 9, 11, 17 and 19
- `chakrabarty-climate-of-history.txt` — full text, made 2026-11-11; the PDF is
  born-digital, so the text is clean
- Braudel: `barudel_on-history.pdftotext.txt` (the 1949 preface, p. 3)

**Checked on the page image:** Cronon pp. 9 (Dust Bowl, horse, trash), 13 (both
lesson titles, "not the only actors," "golden-age myths"), 17 (predictions and
parables) and 19 ("people *thinking* they are outside of nature"). **Checked
against the text layer only:** Cronon pp. 1, 8, 14, 15, 16; every Chakrabarty
quotation (pp. 205–8); every Maza quotation (pp. 109, 110, 115), against OCR.

Notes on particular quotations:

- **Cronon's italics.** He italicizes *predictions*, *will*, *parables* and
  *may* (p. 17) and *thinking* (p. 19). The deck marks them with `<i>`, but the
  quote style is already italic, so they do not show on the slide.
- **Chakrabarty pp. 206–7** is two sentences joined by an ellipsis; the second
  begins "But we can become…" in the original and the "But" is dropped.
- **Braudel in two translations.** The deck quotes the 1949 preface from *On
  History* (Matthews): "almost changeless." Chakrabarty quotes the Reynolds
  translation of the same preface: "almost timeless" (p. 205). The slide uses
  the Week 5.2 wording so the room recognizes it.
- **"as a prisoner of climate"** (Chakrabarty p. 206) is Chakrabarty quoting
  Alfred Crosby quoting Braudel; the block gives it as Chakrabarty's sentence.
  Braudel's own line is in "The *Longue Durée*," *On History*, p. 31, and was on
  a Week 5.2 slide.
- **The title slide gives Chakrabarty as pp. 197–211,** the schedule's "first
  15 pp." The Coalbrookdale caption cites p. 209 and the quotations run to
  p. 208, all inside that range.

## Facts from outside the readings

None quoted; check before publishing. The British took Havana in 1762 and returned it to
Spain in 1763 (the slide states the first; Maza says only "the 1762 siege"). Serres painted the scene
in 1770–75 (Commons). Grand Coulee Dam is on the Columbia; the photograph is
dated August 1986 (Commons). Catlin's painting is dated 1834–35 (Smithsonian).
*Coalbrookdale by Night* is 1801, Science Museum, London, and shows iron
furnaces in Shropshire; "burning coal" is the standard description (the Bedlam
furnaces used coke). "Early conservationists answered with stories of decline"
compresses Maza p. 109, which says declensionist chronicles "converged with the
efforts of early conservationists like John Muir and Aldo Leopold."

## Cold review, 2026-11-11

A fresh-context agent checked every quotation against the caches (and Cronon
pp. 9, 17, 19 on page images): all exact, with the right pages. Its findings,
each verified and fixed:

- *Misattribution:* the "Prisoner, or maker" block made "still a vision of man
  'as a prisoner of climate'" Chakrabarty's verdict on Braudel. On p. 206 the
  subject is environmental history as a field; Braudel only supplies the
  phrase, through Crosby. The block now says so.
- *Overstatements:* the Braudel headline said the slowest layer "has started
  to move fast"; Chakrabarty says the climate "can sometimes reach a tipping
  point" (p. 205), so it is now "can now move fast." "Caused the Dust Bowl" is
  now Cronon's "was the principal cause"; "golden-age myths" regained "almost
  surely." The take home no longer says "on Braudel's longest timescale":
  Chakrabarty contrasts human with geological time and does not equate
  Braudel's geographical time with it.
- *Maza misread:* she says declensionist chronicles "converged with the
  efforts of early conservationists," not that conservationists wrote them
  (p. 109), and that nature was the backdrop before it "entered history" as a
  victim. Headline and detail changed.
- *Cites and dates:* the Dust Bowl book is Maza p. 110 n. 62 only; the
  nonhuman-actors eyebrow began at 1972 (*The Columbian Exchange*, which Maza
  does not mention) and now begins at 1986; "Since the 1990s" had no date in
  Maza and is now "A second generation," her phrase through Sutter.
- *Havana:* the alt text described ships that are not in the picture; the
  caption now gives the full title; the detail now says the British took the
  city, so the picture is not read as a failed siege.

**Not changed.** The four historiography eyebrows overlap, and Maza puts the
hybrid point (p. 110) before the nonhuman-actor books (pp. 113–15); the deck
keeps hybrid last because it is the field's most recent position. "Carrying
germs, crops and animals" is the deck's gloss on Chakrabarty's "biological
agents" (p. 205). The geological-force block omits his qualifier that the
process "really picked up in the second half of the twentieth century"
(p. 207). Maza is listed as "Background" on the title slide, as in every deck,
though the schedule marks her required.

## Checks, 2026-11-11

Build clean. `slide-words.py`: all containers within target. `deck-check.sh`:
16 slides, 0 FAIL, 0 WARN. Every slide was screenshotted at its first state in
a fresh headless profile and nothing clips; the fragments (three questions, the
two unpack blocks, the 13.1 pointer, the take home) were measured by the
checker but not looked at in a screenshot.

## Possible cuts if the session runs short

Least load-bearing first: the Catlin image slide; the Cronon "practical
lessons" cards (the four habits carry his argument); the freedom slide.

## Larger explainer images, 2026-11-12

At the author's request ("can we find a way to make the images larger even when
part of a slide? … the text could be compressed to fit around larger
versions"), every explainer here uses `.with-figure.wide.compact.large`: the
picture is capped at 540×420 instead of 470×290, the credit sits at the foot of
the text column, and the headline, quotation and `.detail` lines are a step
smaller. The modifier is new in the theme CSS and documented in
`courses/SLIDE-STYLE.md` ("Explainer"). Images cropped toward portrait for the
old, smaller slot (see `images/README.md`) were not re-cropped; a wider crop
would now fit.

## Authors back in the details, 2026-11-12

The author clarified the "no names" rule from the tenth revision of the
combined deck: "i know i said no names, but i meant in the headlines. for these
details, i think a author and book is useful just to give a specific example."
`.detail` lines, card text and captions now name the author and book;
headlines and eyebrows still do not. This supersedes the "Names" notes above
for everything except headlines. Names, titles and dates added from outside
the readings should be checked (see below in each deck's slide text): in
science, Butterfield (1931), Koyré (1939), Hessen (1931), Merton (1938), Dobbs
(1975), Latour and Woolgar, Eisenstein (1979), Daston and Galison, Raj,
Theodore Porter (1995), Pamela Smith (2004); in medicine, Sigerist's
*Civilization and Disease* (1943), Foucault, Crosby, William McNeill, McKeown,
Roy Porter, Ulrich, Arnold, de Kruif (1926), Jones, Showalter; in environmental
history, Worster, Crosby, Diamond, J. R. McNeill, Merchant, Pyne, Tarr.

## One paragraph after the quotation, 2026-11-12

The author: "these slides can get visually too confusing. let's have a rule
that the explainer paragraphs after a quote are just a single block of text."
Every explainer's `.detail` lines were merged into one paragraph (the rule is
now in `courses/SLIDE-STYLE.md`, "Explainer"). Glosses such as "Deviance:" are
written as ordinary sentences. Cut to keep the merged paragraphs short: the
first subtitle of *Laboratory Life*, and Tycho's unprinted star catalogue
(Johns, p. 18).

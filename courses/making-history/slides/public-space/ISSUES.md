# Open issues — History, Memory, and Public Space (11.1)

Contributor notes, excluded from the build. Deliberate deviations are recorded
here so a later review does not raise them again.

## What this deck is

The one deck for 11.1. It was redone on 2026-10-23 at the author's direction:

> previous slides worked through interesting but difficult passages in the
> readings. the public monument text is so easy to read, we don't need to do
> that. let's just highlight the main points given in the pdf's readings, and
> use 3-4 viual examples. i don't want two different slide decks, so maybe we
> can incorporate the who put that there slides into the main one after the
> public monuments overview. for hayden, i think you covered chapter 1, but i
> need an overview of chapter 2 and the more theoretical ideas about
> construction of space.

Later directions the same day:

- "let's use that slide to show the 'happy' version via the photo, but then
  use a few slides to illustrate the 'real' history. i think we could use that
  strategy in a couple of cases at least."
- "it looks like the hayden slides are stilla bout chapter 1 instead of
  chapter 2," after which the chapter 1 part was cut.
- "for slide 30, can we get images of the three examples. i can quickly go
  over the 3 in text, but it would be nice to then have the 3 in separate
  slides that have a full illustration of what that would look like. let's
  remove section 2 except for the unm slide, which i think we can fit into
  what is now part 3 somewhere. let's remove the 'parts' from the slides. just
  one continuous tour through the readings." Slide 30 was the reveal.js
  index (`#/30`, counting from 0): the three-histories cards.
- "for slide 29, can we get an photograph example or 2 of counter space?"
  (`#/29`: Hayden's conclusion slide, whose last block is counter-space.)
- "everything is fair use for a class lecture."
- "can you find 1 or 2 cool digital history projects about space, that show
  how the study of place with digital methods can be revealing?"

**Order.** One continuous tour, Loewen then Hayden, with no part labels.
Loewen's main points (pp. 13–24): a framing quote slide, then stories, class
and civil religion as a quote slide and an example photograph each (see
"Loewen's opening functions," below), two `.cards` slides, and the "not written
by gods" quote slide, with the "Goddess of Democracy" as an image break and one
happy-version sequence (below). Hayden ch. 2 (pp. 14–43):
Hayden's explainer, Lefebvre's explainer, then the chapter in page order (with
three Santa Fe slides after Hodgin Hall; see "Wilson on Santa Fe," below). The
three-histories cards are followed by one image slide per history (Wrights
Tunnel, Belzoni, the Tenement Museum), then the territorial and Wells quote
slides, then Hodgin Hall in 1904 and today, then the chapter's conclusion,
two counter-space photographs (Casita Rincón Criollo, an Estrada Courts mural)
and two digital history projects (*Mapping Inequality*, *Mapping Prejudice*).
Then the `.parallel` comparison, the arc, the take home and what comes next.
43 slides.

**No part labels, no discussion slides.** The guide's session structure has
parts, each ending in a discussion slide, and an arc with one card per part.
At the author's direction the eyebrows name the reading (`Loewen · …`,
`Hayden · …`), not a part. The two discussion slides went with the "who put
this here?" part, so the schedule's two questions ("What's the difference
between 'history' and 'memory'? Why does it matter?" and "What historical
narratives do they tell, and what do they leave out?") are no longer on any
slide. The arc has three cards for the tour's three stretches (Loewen, the
Hassanamesit happy version, Hayden), labeled by source, not by number.

**Hodgin Hall is two image slides, not a pair.** In the cut part it was a
`.provoke` pair. The guide allows a `figure.pair` only after each image has had
its own slide, and `.provoke` only in a discussion deck, so in a lecture deck
it is the 1904 picture, then today's, with the provocation's question kept as
the second caption's point. It follows the Wells quote slide ("efforts to
assume, extend, resist, or accommodate" power, p. 30), and the closing slide's
pointer to Hodgin Hall's records still has a picture behind it. If the author
wants the side-by-side back, it needs a `figure.pair` slide after these two.

**What the redo cut.** Loewen's two parts, seventeen slides, became the main
points. The passage-by-passage slides (not mainly to teach, the functions,
history is power, the tone of a plaque, imprisoning the minds, permission, the
marker offices, what the landscape keeps, happy history) became three card
grids and the "not written by gods" quote slide. Stone Mountain went with
them. The wrap-up slides ("Ideas to keep in mind") are gone. The Hayden
chapter 1 part (Baldwin, Gans and Huxtable, Penn Station, the African Burial
Ground, her questions about women, her remedy) is gone, since the schedule
assigns chapter 2 only. Then the "who put this here?" part went: its framing
slide, five of its six picture slides (the Santa Fe panel, the Santa Fe plaque
and boxed base, the Lee Monument in 1890 and 2020, the Albuquerque plaques,
Mount Rushmore and Crazy Horse) and both discussion slides. None of the deck's
versions was ever committed, so none of the cut slides is in git.

**Closing run.** The deck ends with four text slides (the comparison, the
arc, the take home, next), the guide's closing sequence.

## Loewen's opening functions (2026-10-26)

The author's direction: "on slide 3, i don't think i want to emphasize that
tourism is a reason for monuments. in a select few places maybe, but they are
significnat. most of the power of the chapter is in the everyday monuments we
don't question. can the other points be made into separate slides (with maybe
an image as example?) we can delete the williamsburg image." Slide 3 was the
reveal.js index `#/3`: the four-card "What monuments are for" slide.

- **Tourism is cut,** with the Williamsburg photograph (file deleted) and its
  caption's Cary Carson quotation. Loewen makes the point on p. 13 (the Freedom
  Trail, Williamsburg's "moneymaking machine") and p. 16 ("put a town on the
  map"); no slide carries it now. The framing slide quotes only his opening
  question, so nothing on it claims the list is complete.
- **The three remaining cards became three quote slides,** each followed by an
  everyday-monument photograph: stories (a Civil War soldier on a town green),
  class (a Daughters of the American Revolution Santa Fe Trail marker),
  civil religion (a doughboy over a pharmacy sign). Each slide's wording is
  Loewen's, pp. 13–14, checked word for word against the cached text.
- **Rockefeller and Williamsburg are not named on the class slide.** Loewen's
  example for "history is power" is Rockefeller's circle starting Colonial
  Williamsburg (pp. 13–14). Each name would occur once in the deck, so the
  block gives the claim ("those on top of society . . . take the time to
  determine how history will be remembered") and drops the roster.
- **The arc card** said monuments "flatter, sell and unify." It now says
  "supply heroes, help the upper class stay upper and unify."
- **Not re-reviewed.** The deck's fresh-context review (see "Before
  publishing" in `courses/SLIDE-STYLE.md`) predates these seven slides.
  `deck-check.sh` passes with 0 failures. The Civil War soldier's sculptor and
  date rest on the Commons description alone (see `images/README.md`).

## Wilson on Santa Fe (2026-10-26)

The author asked for "a couple slides based on general knowledge of the
book" and has no copy of Chris Wilson, *The Myth of Santa Fe: Creating a Modern
Regional Tradition* (University of New Mexico Press, 1997). Three slides follow
Hodgin Hall 2024: a text slide on Wilson's argument, then the Palace of the
Governors in 1904 and in 1934 as another before and after.

**Nothing on these slides is checked against the book.** No quotation, no page
number, no chapter. The text slide paraphrases publisher and reviewer
descriptions found by web search on 2026-10-26: that Santa Fe's image was
consciously created in the early twentieth century, mainly by Anglo-American
newcomers; that leaders tied the effort to statehood in 1912 and to the
economy; that the means were speculative restoration, removal of overt signs
of Americanization and historic design review of new buildings; and that
Wilson finds the tricultural story an oversimplification of Native American
culture, cultural mixing and conflict. The population of about 5,000 in 1912
and Wilson's post (founding director of UNM's Historic Preservation and
Regionalism program) come from the same kind of source (a review and a
bookseller listing). Before the slides are relied on, read the book's
introduction and the chapter on restoration, confirm each paraphrase, and add
page cites. Whether Wilson connects Hodgin Hall's 1908 remodel to the Santa Fe
style is **not** claimed; it was not confirmed.

- **The Palace dates** (Hewett invited Nusbaum in 1909 to oversee the
  restoration, finished in the fall of 1913; the Museum of New Mexico was
  established in 1909) are from Wikipedia, "Palace of the Governors," and were
  not checked further. The captions describe only what the photographs show.
  They do not say what the restorers removed or added, or whether the 1904
  porch was American-era; that is a question to answer from Wilson or the
  Palace of the Governors Photo Archives.
- **The 1904 photograph** comes from the same book as the Hodgin Hall 1904
  picture, so the two share a source and a year.
- **No portrait of Wilson** was looked for; he is introduced in a
  `.reveal-block.historical` on the text slide.

## The happy version and the real history

At the author's direction, one of Loewen's monuments (the Hassanamesit marker)
is shown first as "the happy version" (Loewen's "happy history," p. 23, is on
the card slide just before it), then followed by two slides of what the marker
leaves out. The caption of the first slide opens "The happy version:". The
pattern is not yet in `SLIDE-STYLE.md`.

- **Hassanamesit → 1675.** The 1930 marker; the 1663 Indian Bible, the book
  the marker is proud of, whose caption introduces Daniel Gookin; a quote slide
  with the Nipmuc fighters' warning as Gookin reports it, Deer Island, and the
  Hassanamisco reservation today.

**Oñate → Acoma was cut on 2026-10-26.** The author: "let's also remove the
onate slides; it's old news here." Three slides went: the statue (Loewen's
p. 15 on it), the Acoma mesa photograph, and a `.cards` slide on what the
statue leaves out (the 1599 sentence, the count of the maimed, the 1614
conviction, the 1997 foot). The deck was the second happy-version sequence, so
the arc's middle card now names Hassanamesit alone. If the sequence comes back,
the source is George P. Hammond, *Don Juan de Oñate and the Founding of New
Mexico* (1927), cached in
`~/Dropbox/courses/making-history/.research-packets/onate-hammond-1927.txt`:
trial and sentence pp. 122–23; the count of twenty-four maimed p. 123 n. 465;
the death toll, "over 600" to 800, p. 122 n. 463; the 1614 conviction p. 184.
Three things a presenter would need to hold: some of the statue's defenders
argue the record means toes, not feet (Wikipedia, "1599 Acoma massacre"); the
1997 foot was cut on 29 December 1997 by people calling themselves "Friends of
Acoma," whom no Acoma official endorsed; and the county took the statue down on
15 June 2020. Sources disagree on the statue's date (1991 or 1994). The images
are in git history (see `images/README.md`).

**Sources, and what was checked.**

- *Hassanamesit:* Daniel Gookin, *An Historical Account of the Doings and
  Sufferings of the Christian Indians in New England, in the Years 1675, 1676,
  1677* (written 1677; printed in *Archaeologia Americana*, vol. 2, 1836).
  The warning, and "about fifty men, and one hundred and fifty women and
  children," p. 476; Natick's Christian Indians, about two hundred, shipped to
  Deer Island on 30 October 1675, pp. 473–74; about five hundred there by late
  December, "the Island was bleak and cold," p. 485. The quotation and the
  numbers on pp. 476 and 485 were checked against the scanned page images.
  Gookin was the colony's superintendent of its Christian Indians; there is no
  portrait, so the Bible slide's caption introduces him.
- *The marker's text,* read off the photograph: "John Eliot established here
  in 1651 a village of Christian Indians called Hassanamesit—'at a place of
  small stones.' It was the home of James the Printer who helped Eliot to print
  the Indian Bible."
- *Sources disagree on 1675 at Hassanamesit.* Some accounts (summarized in
  Wikipedia, "Hassanamisco Nipmuc") say English troops destroyed much of the
  village in September; Gookin, writing for the colony, says Nipmuc fighters
  persuaded or pressed its people to leave in November. The slide follows
  Gookin and says the people "went with the fighters." James Printer's own war
  (accused of the Lancaster killings, later amnesty, the 1682 Rowlandson
  narrative) is left out: the sources disagree, and Gookin does not name him
  among the accused.
- *Hassanamisco today.* About three acres in Grafton (Wikipedia gives 3.5, the
  Massachusetts Historical Commission "approximately three," the 2004 federal
  decision 2½), held by Nipmuc families since the 1727 division; on the
  National Register since 2011. The slide says "a small reservation" and makes
  no "never left Nipmuc hands" claim, which rests on local and popular
  sources.

**The take home uses the Grafton marker.** "The Grafton marker tells more
about 1930 than about 1651" replaced the Santa Fe obelisk when the obelisk's
slides were cut; the take home may only use what a slide has shown.

## Hayden's three histories, illustrated

At the author's direction, the three-histories cards (working landscapes,
territorial histories, building types) are followed by one image slide each.
Each caption's note opens with the history it illustrates ("A working
landscape:", "A territorial history:", "A building type:"), echoing the
happy-version captions. Only one of the three is a picture Hayden prints; see
`images/README.md` for what she prints instead and why these stand in.

- **Working landscapes: Wrights Tunnel.** Hayden, following Patricia Nelson
  Limerick, says twenty-nine Chinese workers died building Wrights Tunnel for
  the South Pacific Coast Railroad in 1879, "and dozens more were injured"
  (p. 21; checked on the page image). Other counts differ: Wikipedia ("Wrights
  tunnel"), KQED and santacruztrains.com give 32 Chinese workers killed in the
  explosion of 17 November 1879, and santacruztrains.com adds an earlier blast
  in February 1879. The caption follows Hayden and cites her page. Wrights
  tunnel is the Summit Tunnel (Wikipedia, "Wrights tunnel"). Because the
  tunnel is now on the image slide, the card no longer carries it; it quotes
  her "barely been studied" (p. 20, checked) instead.
- **Territorial histories: Belzoni.** The caption quotes her "convey
  territorial history" (p. 24, checked), about photographs of segregated
  entrances.
- **Building types: the Tenement Museum.** Unchanged except the opening words
  and its position.

**Two text slides follow the three pictures.** The territorial quote slide
(p. 22) and the Wells slide (p. 30) come after the run of images, not between
them, because the author asked for the three in a row after the cards. If they
read better interleaved (each after its picture), move the territorial slide
after Belzoni and the Wells slide after the tenement.

## Counter-space, and two digital history projects

Four image slides follow Hayden's conclusion slide, whose last block
introduces Lefebvre's "counter-space" through her casitas (pp. 35–36).

- **Casita Rincón Criollo ("Downhome Corner"), South Bronx.** The translation
  is CityLore's. Founded by José Manuel "Chema" Soto and neighbors on a vacant
  lot at Brook Avenue and 158th Street: 1978 in an oral history (NYPAP), 1975
  in Welcome2TheBronx, so the caption says "the late 1970s." CityLore: the lot
  was reclaimed for low-income housing in 2006; Gothamist: on its present lot,
  a block away, since 2007. The caption says it "moved a block in 2007 when
  the city took the lot for housing." The photograph's date is not known (the
  Flickr page could not be reached), so the caption gives none.
- **"Órale raza," Estrada Courts.** Wikipedia ("Estrada Courts"): built
  1942–43; "in the 1970s a total of eighty murals were painted by Chicano
  muralists." No source names this mural or its painter, so the caption does
  not. "Right on, people" renders the slang; "raza" here is the community,
  not "race." Hayden photographed two Estrada Courts murals in 1980 (figs.
  2.11, 2.12, p. 37); "a political dialogue with the surrounding city" is p.
  38, checked on the page image, in a sentence that begins on p. 36.
- **Mapping Inequality,** University of Richmond Digital Scholarship Lab
  (director Robert K. Nelson). The Home Owners' Loan Corporation graded
  neighborhoods 1935–40; Los Angeles's map is 1939. Estrada Courts (Olympic
  Boulevard at Grande Vista Avenue) falls inside area D53, checked against the
  project's GeoJSON. The quotation is from D53's area description as the
  project transcribes it ("This is a 'melting pot' area and is literally
  honeycombed with diverse and subversive racial elements"), read on the site
  2026-10-23; the scan itself was not checked. The same description counts
  foreign families at 50% and names Russian, Polish and American Jews, Slavs,
  Greeks, American Mexicans, Japanese and Italians. The slide links the two
  Los Angeles slides: the counter-space sits in a district the federal
  government marked red.
- **Mapping Prejudice,** University of Minnesota Libraries. Its About page:
  begun in 2016; volunteers "read historical property deeds and transcribe the
  information necessary to locate racial restrictions on a digital map"; its
  Hennepin County map was "the first-ever comprehensive visualization of
  racial covenants for an American city." The site's counts disagree with
  each other (34,000 Minnesota covenants on the data page, 85,800 mapped on the
  About page, which includes other states), so the slide gives no count. The
  map is the project's 2010 census overlay (Marguerite Mills, 2020); "most
  covenanted blocks still have few Black residents" is a reading of that map,
  not the project's sentence. Hayden's link is fig. 2.2, p. 25 (Japanese
  Americans excluded in Hollywood by "signs as well as deed restrictions,"
  checked on the page image).

**Why these two projects.** Both are territorial history in Hayden's sense,
made from documents only a digital project could read at scale: every HOLC
area description, every deed in a county. Both show something no single
document does. Each ties to the deck: Boyle Heights is where Estrada Courts
stands, and deed restrictions are in Hayden's fig. 2.2. A third, set aside:
*Photogrammar* (Yale), which maps the roughly 170,000 Farm Security Administration
photographs the deck's Chamisal and Belzoni pictures come from.

**No framing slide.** The two projects are introduced in their captions
("Territory, mapped:" and the project names), not on a text slide. If the
room needs a signpost, a one-line `.detail` slide would go before
*Mapping Inequality*.

## The readings, and what does not match the schedule

**Loewen's pages.** The schedule assigns "first two chapters (1--17)." The
course PDF is the 2019 revised edition (The New Press), where those two
chapters, "Some Functions of Public History" and "The Sociology of Historic
Sites," run pp. 13–24. The deck cites the PDF's pages and says so in the
`.citation-note`. The schedule's 1–17 may be the 1999 pagination; not checked.

**Hayden's chapter.** The schedule assigns Ch. 2, pp. 14–43, and so does the
deck.

- `~/Dropbox/courses/making-history/Hayden-D.-.pdf` (also in Zotero) is
  chapter 2, pp. 14–43, plus the endnotes for chapters 1–2.
- `~/Desktop/Hayden-ch2-single-pages.pdf` (2026-10-23) splits the author's
  two-page scan of chapter 2 into single pages: pp. 14–43 and the notes,
  pp. 250–259. PDF page *n* is printed page *n* + 13 for the chapter.

**"Goddess of Liberty."** Loewen calls the Tiananmen statue the "Goddess of
Liberty" (p. 18). It is usually called the "Goddess of Democracy," the name
the CUHK copy carries, so the caption uses that.

## Decisions

**Two readings, no "Background:" line.** Neither is a survey that narrates the
session, so both authors are introduced like primary authors: Loewen on a
portrait slide, Hayden on an explainer (see `images/README.md` for why not a
portrait), whose quotation is from chapter 2 (p. 15). Lefebvre is introduced
the same way on the next explainer; Hayden quotes him as her chapter's
epigraph. Camille Wells and the Los Angeles lawyer are cited "quoted in
Hayden." Where a quoted voice comes inside Loewen's own sentence (the Beijing
loudspeakers), the cite gives Loewen's page.

**Hayden's explainer carries the transition.** Its `.detail` opens "Loewen
stops at markers and monuments," the line the guide asks for where one part
hands off to the next. With no part labels it is the only signpost between
the readings.

**The Lefebvre cards gloss Lefebvre through Hayden.** Hayden summarizes
Lefebvre's three scales of social reproduction in one sentence (p. 19): the
body (biological reproduction), housing (the reproduction of the labor force)
and the public space of the city (the reproduction of social relations). The
cards say only that; the eyebrow says "Lefebvre, through Hayden." The
three-histories cards follow Hayden's own division (pp. 20–34). Limerick is
not named on the slides, since she does not come back.

**Hayden prints the Chamisal photograph** (fig. 2.8, p. 31). The Belzoni and
Wrights Tunnel photographs are not hers; their captions say what she writes,
not that she prints them.

**The take home's catch is the deck's, not Loewen's.** "A corrected marker is
still a marker" turns Loewen's p. 14 point (a plaque "speaks with authority")
back on correction. He does not say this. It is the cost line the guide asks
for and is phrased in the deck's voice, not attributed.

**Some caption facts come from outside the readings.** All standard, none
quoted: Loewen's, Hayden's and Lefebvre's biographical lines; the CUHK
copy removed in 2021; the Tenement Museum's 1863 building and 1988 founding;
the photographers and dates of the FSA pictures; Hodgin Hall built in 1892 and
remodeled in Pueblo Revival style in 1908 under President William G. Tight
(Wikipedia, "Hodgin Hall"), the 1904 picture from a state booster handbook for
the St. Louis fair, and the building now the alumni center (on the sign in the
2024 photograph). The Hassanamesit and Wrights Tunnel facts are above.

**The deck leans local on purpose.** The Chamisal photograph and Hodgin Hall
are in New Mexico. The slides ask what each object leaves out, not who was
right.

**Long captions run under the left arrow** at 960×700: the tenement, Hodgin
Hall 2024, Estrada Courts and Mapping Inequality captions. Any caption long
enough to wrap does this; it is the caption width in the theme, not these slides, and would need a
CSS change across decks.

## Checks run (2026-10-23, after the counter-space and digital-project slides)

- `LC_ALL=en_US.UTF-8 bundle exec jekyll build`: clean.
- `scripts/slide-words.py`: nothing over a hard stop. Over target by one to
  four words: the Loewen portrait caption (83/80) and the Acoma, Bible,
  Goddess and Oñate captions (41–44/40). The new captions are under target.
- `scripts/deck-check.sh making-history/history-memory-public-space`: 38
  slides, 0 fail, 1 warn: the casita photograph at 1.48x (see
  `images/README.md`; the Flickr original would clear it).
- Slides 3–33 screenshotted (zero-based) after the part-two cut, and slides
  29–33 after this round, at 960×700 in one headless Chrome session with the
  cache disabled. Nothing clipped.
- No fresh-context review of the happy-version sequences, the three
  illustrations, the counter-space photographs or the digital projects yet.
  The first review (below) covered the deck before all of them.

**Card labels (2026-10-23).** At the author's direction, a card's `.num`
label goes unless it says what the green heading can't; the rule is now in
`SLIDE-STYLE.md` under "Headlines and eyebrows." The throughline's weeks and
the arc's source labels stay.

## What the fresh-context review caught (2026-10-23, before the cuts)

It found no misquotations. Every finding below was checked against the text
caches before it was fixed. Findings about the cut parts are left out.

- **Dropped hedges in Loewen's cards.** "Most" war memorials (p. 14);
  the state is "mostly" what memorials say is worth dying for (p. 14); "no
  relatively disinterested" statewide body (p. 20); communities "usually"
  mark only their happy history (p. 23). The arc keeps "usually."
- **Glosses that went past Hayden.** The Lefebvre cards said the body is where
  people are "born and kept alive," housing where workers are "raised, fed and
  rested," and the city "who may go where." Hayden gives only the three scales
  (p. 19). The territorial card left out gender, though Hayden's heading is
  "Race and Gender" (p. 22). The Chamisal caption said the building's making
  is "easy to read"; Hayden says "much less difficult to analyze than urban
  real estate" (p. 31). "Cultural geography," not "rural landscape studies,"
  avoided "issues of political contestation" (p. 17). The comparison card had
  space produced "for work or to keep some people out," but her pair is
  production and social reproduction.
- **Attributions.** "The production of space" is Lefebvre's term, not
  Hayden's (p. 18). The casitas are Hayden's example of his "counter-space,"
  and the passage runs pp. 35–36.
- **Guide rules.** The take home must use something a slide has shown (it now
  uses the Grafton marker). Hayden's explainer opens with what Loewen left out.
  Lefebvre is named as "the French sociologist," Hayden's phrase (p. 18). The
  "Stories" card no longer opens with a quotation.
- **Not taken.** Robert Bellah is named once and does not return; he stays
  because "civil religion" is his coinage, and an earlier review asked for the
  credit. Hayden's credit already names the NC license.

## Sources for review

Text caches, in `~/Dropbox/courses/making-history/.research-packets/`:

- `loewen-lies-across-america-13-24.txt`: pp. 13–24, 2019 edition, from the
  PDF's text layer, printed-page markers.
- `hayden-power-of-place-ch2.ocr.txt`: ch. 2 and the endnotes for chs. 1–2.
- `onate-hammond-1927.txt`: Hammond (1927), full OCR text, public domain.
- `gookin-christian-indians-1677.txt`: Gookin's account as printed in 1836,
  OCR text, public domain, with the URL pattern for its page images.

Every Hayden quotation was checked against the page image on 2026-10-23
(pp. 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 33, 34, 36, 43).
Loewen's are from the text layer. Gookin's p. 476 quotation and the p. 485
phrase were checked against the 1836 scan.

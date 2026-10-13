# Open issues — Inventing Nations (9.1)

Contributor notes, excluded from the build. Deliberate deviations are recorded
here so a later review does not raise them again.

## The slide contract this deck is built on

**One history lesson, narrated by Maza, in the order of her chapter.** The
third brief (2026-10-09) asked for a throughline: an actual history lesson
based on Maza, not a review of readings, culminating in Maza as the historian
who pulls it together. On 2026-10-13 the author asked for the slides to follow
the flow of Maza's chapter, so the three parts track her argument rather than
one chronology. The headlines read in order as its sentences:

1. **Part one, the nation as history's frame (Maza pp. 45–49).** Until about
   1800, Western history was not usually written nation by nation (pp.
   46–47), framed as the session's question: how did the nation come to seem
   natural, and worth dying for? Most countries are younger than a century,
   with borders drawn by Western empires (p. 46; Said in 9.2); the 1789 map,
   read against Maza's jigsaw (p. 46); before 1800 most states belonged to
   rulers (four examples, France first); national feeling is much older but
   was mostly defined against neighbors (p. 47; Bede in Week 3); what was new
   after 1776 was the nation as the source of power (Kramer, quoted on p. 47);
   then historians wrote
   each nation an admirable past (p. 47), the first professional historians
   mostly celebrated their own (pp. 48–49), and Ranke's scientific history,
   too, began with the nations he counted as kin (portrait first; Treitschke
   in Week 4); Sorrieu's 1848 print for the springtime of nations closes the
   part, its caption on which historians took part.
2. **Part two, how historians explained it (pp. 50–56).** In 1914
   nationalism was at its height (p. 50); the century after led historians to
   ask how nations were made (p. 51); Anderson — portrait first — asked why
   such recent communities demand such sacrifice (p. 7), starting from his
   definition (p. 6), and his answer, in Maza's summary, is that nations took
   over religion's work of linking the dead and the unborn (pp. 51–52);
   meanwhile historians found that many "timeless" symbols dated from the
   1880s and 1890s (p. 52; the first national Columbus Day in 1892, then the
   Pledge, the 1897 jubilee, the 1889 Meiji ceremony); nationalism grew against empires, first in the Americas and last
   in Africa and Southeast Asia (p. 53); and nations chose what to remember
   and what to forget (Renan, quoted on p. 53; the 1790 Festival of
   Federation, p. 54; Gettysburg, p. 55).
3. **Part three, from the colonies (pp. 77–81).** History became a
   profession under empire, so Europe's past became everyone's model (p. 78);
   Chatterjee — portrait first — answered Anderson that the colonized did not
   simply copy Europe's model, and in Bengal remade their own culture.
4. **Maza, 2017 (pp. 81–82):** the arc framed as her story, then her closing
   cost. No portrait (see Decisions).

Anderson and Chatterjee appear where their explanation enters the story, not
as readings to be summarized. **Test any new slide by reading the headlines
aloud in order: if the new one does not read as the next sentence, it belongs
somewhere else or nowhere. Then check its Maza page against its neighbors':
the deck runs in the chapter's order.**

Only the three part openers say "Part one ·", "Part two ·" or "Part three ·";
every other eyebrow is a date or a name.

**One idea per slide, as in `gender/`, and every slide one of the guide's
slide types.** A headline and one quotation. The only additions: the
opening slide is a framing slide, with the session's question as a `.question` fragment under the
quotation; the "before 1800" slide is a `.cards` grid; and
three quote slides carry a `.reveal-block.compare` pointer (Week 3, Bede;
Week 4, Treitschke, on the Ranke slide; 9.2, Said, on the empire slide).
Every line has a class for its job, and there are no `.detail`,
`.pull-quote` or `.reveal-block.historical` lines.

An earlier draft had all three, each added to fix something else: a 1914
historical block *above* Anderson's quotation (commentary over evidence, two
writers in a hierarchy, and Anderson quoted before his portrait), a Maza
pull-quote under Chatterjee's, and the opening question styled like the
quotation above it. The author caught them on screen; `scripts/deck-check.sh`
now catches the first kind, and `SLIDE-STYLE.md` ("Before publishing")
describes the eye-check for the rest. 1914 is now a slide of its own.

**Introduce before you quote.** Ranke's, Anderson's and Chatterjee's
portraits come before their first words. Maza is the narrator — the title
slide's `Background:` reading — so she is quoted from the start and needs no
portrait. Kramer, Renan and Blight are voices quoted through Maza; the Renan
slide's headline is about memory, not about Renan, so that it stays that
way. Treitschke and Said appear only in `.compare` pointers. The 1892
Columbus Day proclamation is quoted as a document of the American
government, cited by its proclamation number, with no portrait of Benjamin
Harrison and his name kept out of the headline; give him a portrait if a
later slide makes him its subject.

**Thirty-four slides, ten of them images.** What is cut, so nobody restores it
by accident:

- **The two discussion slides**, "Reunion at Gettysburg" and "Modern, but
  not Western" (author's call, 2026-10-13). Their questions are still worth
  asking aloud: why a celebration of reunion needed slavery forgotten (Maza
  pp. 55–56; Blight's "sacrificial offerings on the altar of reunion"), and
  why the Bengal school wanted art "modern and at the same time recognizably
  Indian" (Chatterjee p. 220) while the British ran the state, since in
  culture "the nation is already sovereign" (p. 217). The Bharat Mata
  painting went with the second slide, and its file was deleted.

- **Maza's portrait** (author's call, 2026-10-11: no photographs of textbook
  authors). The deck used to end on her face before the arc.

- **The Gellner discussion** ("Invention or fabrication"). It was the most
  reading-review slide in the deck — a question about Anderson's word choice
  rather than about what happened. Anderson's p. 6 point ("the style in which
  they are imagined") is still the right answer if the schedule's question
  "Does that make them fiction?" comes up at the definition slide.
- **Anderson's paradox** (p. 5). The story shows the paradox; Anderson's p. 7
  question replaced it because it joins part one's wars to his answer.
  Maza's "denaturalizing" (p. 51), cut with it on 2026-10-09, came back on
  2026-10-12 as its own slide (see Decisions).
- No cold open; no slide for Anderson's "deep, horizontal comradeship" (p. 7).
- Maza pp. 55–56 on Vichy France, and pp. 57–77 — oceans, borderlands,
  world history. Her "Displacing Euro-America" section (pp. 77–81) opens part
  three.

## Decisions

**Four more changes, 2026-10-13, after the reordering.**

- *Sorrieu moved after Ranke*, closing part one, at the author's suggestion,
  and cropped to the picture (printed title and mount removed) so it shows
  larger. The author asked whether Ranke's national history inspired 1848.
  It did not: Ranke was a conservative monarchist who distrusted the
  revolutions, and his students turned nationalist mostly afterward, pinning
  unity on Prussia (Popkin p. 88). The historians in 1848 were the liberal
  national ones — Michelet in Paris (Popkin p. 86), the "professors'
  parliament" at Frankfurt — and the caption says so, naming Ranke as the one
  who stayed out.
- *Columbus Day, 1892*, a quote slide before the Pledge photograph, at the
  author's request (the holiday had just passed). The quotation, "Let the
  national flag float over every schoolhouse…", was checked against the raw
  text of Proclamation 335 at the American Presidency Project. Why the
  holiday came about, for saying aloud: Congress's joint resolution of June
  1892 for the four-hundredth anniversary; the *Youth's Companion*'s campaign
  to put a flag on every schoolhouse, for whose school program Francis
  Bellamy wrote the Pledge; and, often cited, a gesture to Italian Americans
  after eleven were lynched in New Orleans in 1891. Columbus Day became a
  state holiday in Colorado in 1907 and a national one in 1937; Indigenous
  Peoples' Day began as a counter-observance in the 1990s. It fits Maza's
  invented traditions (p. 52) and her remembering and forgetting (p. 53).
- *Arc card 01* was "Made national," which did not say what it meant; it is
  now "Made, and given a past," echoing the arc headline.
- *Chatterjee's portrait* had his eyes closed. Replaced with the Fukuoka
  Prize's seminar photograph, cropped to him; see `images/README.md`.


**Discussion slides removed and the deck put in Maza's order, 2026-10-13.**
The author asked for both. What moved, and where Maza has it:

- The borders slide (p. 46) from the end of part one to just after the
  opening; the 1789 map follows it, because Maza's jigsaw sentence is on the
  same page.
- The symbols and their three images (pp. 52–53), the nationalism-against-
  empire slide (p. 53), Renan (p. 53), the Festival of Federation (p. 54) and
  Gettysburg (p. 55) from part one into part two, after Anderson. Maza
  presents them as what historians found once Anderson and Hobsbawm and
  Ranger (both 1983) had made nations a subject, so the symbols headline now
  begins "Meanwhile, historians found…". The Festival now stands for
  commemoration, "the first of many such celebrations of the new order"
  (p. 54), rather than for 1776; its caption keeps the oath's order.
- Chatterjee became part three, opened by Maza's p. 78 sentence on
  professional history taking Europe as "yardstick and model"; his headline
  now says he "answered Anderson," so it cannot be read as answering Maza.
- Arc cards regrouped one per part, plus Maza's conclusion.

Two things stand outside Maza's order because she does not discuss them:
Sorrieu's 1848 print sits by the age of revolutions, and Ranke next to her
pp. 48–49. Headline changes made by the move: the borders slide ("Most
countries are younger than a century…"), the symbols, the empire slide
("Nationalism grew against empires: first in the Americas, last in Africa and
Southeast Asia"), Renan ("Nations chose what to remember, and what to
forget"), Chatterjee.


**Story check against Maza, 2026-10-12.** The author asked for the deck's
story to be rechecked against the chapter itself. Three slides had drifted
from the text and were fixed:

- *The opening headline* said history had been written nation by nation
  "only since about 1800." Maza says the nation "was not usually the context
  or object of Western historical writing" before then (pp. 46–47), and the
  deck's own Bede pointer is the exception "usually" allows. It now reads
  "Until about 1800, Western history was not usually written nation by
  nation."
- *Anderson's answer.* The deck asked his p. 7 question and then gave his
  p. 6 definition as "His answer." In Anderson the definition comes first and
  the question is the problem it raises; his intro says only that "the
  beginnings of an answer lie in the cultural roots of nationalism" (p. 7).
  Maza supplies the answer from his later chapters: print capitalism, and the
  nation taking over religion's work of "creating links between the dead and
  the yet unborn" (pp. 51–52). The definition slide is now "His starting
  point," a new slide carries the answer in Maza's words, and arc card 02
  says the same.
- *The 1789 map caption* ended "Germany became one state in 1871," which
  invites the reading Maza argues against: unification as pieces of a jigsaw
  "being popped into place" (p. 46). The caption now says so.

What matched the text and was left alone: national feeling older and defined
against others (p. 47); the age of revolutions coupling nationalism with
democracy (p. 47, Kramer); the national histories (p. 47); the symbols, the
Pledge, the jubilee and the Meiji palace (pp. 52–53); borders drawn by
imperialists (p. 46); historians, politicians and others making the illusion
of deep roots (p. 53); Renan and forgetting (pp. 53, 55); Gettysburg and
Blight (pp. 55–56); 1914 (p. 50); "lost our innocence" (pp. 81–82); the
closing price (p. 82). Maza never mentions Ranke; his slides rest on Popkin
and the 1824 preface. Chatterjee's "modern but not Western" lines up with
Maza's "modernities," societies becoming "modern on their own terms" (p. 80).

The check also found three passages the deck was not using, and the author
asked for all three (2026-10-12): Maza p. 53 (modern nationalism began in
the Americas against empire, and ended in Africa and Southeast Asia against
colonizers) after the 1776 slide, which answers "was the United States
first?" in the reading's terms; pp. 48–49 (the first professional historians
"usually celebrate[d]" their own nations) before Ranke's portrait, the
assigned text's own link to him; and p. 51 ("denaturalizing") between 1914
and Anderson, which says why historians turned on the nation. Maza's p. 48
line that nineteenth-century nationalism was "closely entangled with racial
assumptions" is not on a slide (one quotation per slide); it is the thing to
say over Ranke's "racially kindred nations."

(The positions above are as of 2026-10-12; the next day's reordering moved
p. 53 after the Meiji images and removed the one structural difference this
check had accepted, the symbols and memory told as 1880s history in part
one.)


**The author's revision list, 2026-10-11, and how each was met.**

- *What was there before nations?* A `.cards` slide — France, the Habsburg
  lands in 1740, Venice, the Ottoman Empire — then the Holy Roman Empire in
  1789 as a map. Its first headline, "Before nations, the units were cities,
  dynasties, empires and faiths," turned Maza's p. 47 point about what
  *histories* followed into a claim that nations did not exist, and left out
  the kingdoms of England and France. The author caught it the next day
  (2026-10-12): England, France, Russia and Japan's emperor all existed
  before 1776. What changed is who a state belonged to. So the headline now
  says most states belonged to rulers, France leads the cards, and the
  Festival of Federation caption notes the oath's order — the nation, the
  law, the king. Keep the three claims apart if you rework the opening: old
  states, old national feeling (the next slide), new sovereignty of the
  nation (the slide after).
- *Ranke and his nationalism.* A portrait (the Week 4 file) and one quote
  slide: the 1824 preface's "racially kindred nations … whose history forms
  the heart of all modern history," which Week 4 also used. The Treitschke
  pointer moved onto it. Held to what Popkin supports: Ranke "did not limit
  himself entirely to national history, but most of his German students"
  did, and backed unification (p. 88). His own nationalism was
  Prussian-statist and conservative — he distrusted 1848 — so the slide calls
  his frame "the nations he counted as kin," not German nationalism.
- *Images for the 1880s–90s symbols.* The cards slide became a quote slide
  (Maza p. 52) followed by one image slide per symbol, one image per slide
  as the guide requires.
- *Are these the first instances?* The Pledge, yes: written in 1892. Royal
  jubilees, not quite: George III held one in 1809, so Maza's "royal
  jubilees in England began under Queen Victoria" (p. 52) is loose; what
  began under Victoria was the jubilee as mass pageant (1887, 1897). The
  captions do not repeat the claim. The Japanese emperor is ancient; what was
  new was the public cult — the 1889 palace, the ceremonies, the tours.
  Bastille Day (Maza p. 52, not on a slide) was first kept in 1790 as the
  Festival of Federation pictured in part one, and made a holiday in 1880.
- *1848.* One image slide, Sorrieu's print, captioned "springtime of
  nations." No headline slide: none of the readings discusses 1848, and an
  image keeps it in the story without a quotation the deck cannot support.
- *Colonialism, briefly.* One quote slide (Maza p. 46, borders drawn by
  Western imperialists) with a pointer to Said on Thursday; the jubilee
  caption notes colonial troops in the procession.
- *Green text.* The takehome's text and label are no longer headline green;
  that is a theme change, in `reveal-lecture-theme.css`.
- *Narrow headlines.* `.main-point` used `text-wrap: balance`, which split
  two-line headlines into two half-width lines. Now `pretty`; also a theme
  change.

**The deck does not start nations in 1776.** A first version opened "First,
the American and French Revolutions coupled nationalism with democracy,"
which made the late 1700s look like the birth of national identity. The
author questioned that (2026-10-09), and Maza agrees with the objection:
"National sentiment certainly existed prior to the eighteenth century"
(p. 47). The deck now separates the two: national *feeling* is old (the Dutch
against the Spaniards; Bede's *gens Anglorum* in 731), and what the age of
revolutions added was the nation as the source of political power. Keep that
distinction if you rework the opening.

The dating is itself contested, which is worth saying out loud rather than on
a slide. Anderson's late-eighteenth-century origin is the "modernist" view he
shares with Gellner and Hobsbawm. Others find nations much earlier — Adrian
Hastings, *The Construction of Nationhood* (1997), argues for medieval
England, and Anthony D. Smith, *The Ethnic Origins of Nations* (1986), for
older ethnic cores. Neither is assigned, so neither is on a slide.

**Hobsbawm was dropped from 9.1 on 2026-10-09.** The session had three
primary readings; the course norm is two. Hobsbawm went rather than Anderson
or Chatterjee because the other two are a direct exchange — Chatterjee's
essay is a reply to Anderson — and because Maza already carries the
invention-of-tradition material through Hobsbawm and Ranger's volume (her
nn. 18–20, pp. 52–53): Bastille Day, the Pledge, Victorian royal ceremony,
the Highlands, the Meiji emperor. The deck's "symbols" slide is built from
those pages, so students meet the idea without the chapter. A text cache of
the Hobsbawm introduction is not needed for this deck.

**The schedule's first discussion question still says "invented
tradition."** It is answerable from Maza pp. 52–53, which uses the phrase and
names the book, and can be asked at the symbols slide now that the deck has
no discussion slides. Anderson does not
object to the word "invents"; he objects to Gellner hearing invention as
"fabrication" and "falsity" rather than "imagining" and "creation" (p. 6). So
the deck's title fits Anderson, and no headline or card calls the symbols
"fabricated." Keep that distinction if you reword them — the first draft
got it wrong.

**Cold review, 2026-10-09.** Nine findings, all worked: the Gellner point
above; "guarded its own culture" reversed Chatterjee, whose inner domain is
*remade* as "a 'modern' national culture that is nevertheless not Western"
(p. 217), so the headline and arc card now say "remade"; Maza's "imitation and
repudiation" (p. 53) is about twentieth-century Africa and Southeast Asia and
cites Anderson, so the detail line says so rather than applying it to Bengal
silently; Maza's "most … symbols" is limited to Europe and America (p. 52), so
the headline says "many"; Anderson's members never meet *most* of the others;
the Gettysburg exclusions are Maza's claim and are attributed to her; and
Maza's "historians, politicians, and others" line (p. 53) was added to the
paradox slide so the throughline and take-home claim about historians has
something on screen behind it. The reviewer also noted that the 1905 painting
is contemporary with the political movement, not before it; the question does
not claim otherwise.

**Two portraits are fair use, and both are under resolution.** See
`images/README.md`. `scripts/deck-check.sh` reports Anderson (450×517) and
Chatterjee (375×500) at about 1.0× — sharp on a laptop, soft on a 1080p
projector, which wants about 1.5×. Both are the best sources found on
2026-10-09: Cornell's digital collections may hold a larger Anderson print but
block automated access, and every Chatterjee photograph found online is
smaller or worse. A request to Cornell University Library and to the Centre
for Studies in Social Sciences, Calcutta, would close this. Anderson's is the
Cornell Department of Government's studio portrait, replacing a CC BY video
still that was too small and blurred (author's call, 2026-10-09). Commons has
no photograph of the scholar Partha Chatterjee, only the West Bengal
politician of the same name. Ranke's portrait is public domain. The
Gettysburg photograph warns at 1.46×, close enough to leave.

## Open questions

**The schedule cites a different printing of Chatterjee than the PDF
students get.** `schedule.md` gives "*The Nation and Its Fragments*
(Princeton, 1993), Ch. 1, ~15 pp."; the course PDF is the reprint in Gopal
Balakrishnan, ed., *Mapping the Nation* (Verso, 1996), pp. 214–225 — twelve
pages, running heads "MAPPING THE NATION." The deck cites the PDF's pages and
says so in the `.citation-note`. Consider changing the schedule line to match
the PDF.

**Some facts on slides come from outside the readings.** All are standard
and none is quoted: Renan's lecture date (1882) and Anderson's exclusion from
Indonesia (1972–1998); the four examples on the "before 1800" cards, including the estimate that
perhaps half of France spoke no French in 1789 (Hobsbawm, *Nations and
Nationalism since 1780*, from the Abbé Grégoire's survey of the 1790s), and the
Holy Roman Empire's "some three hundred territories" (counts vary with what
is counted); 1848 and its outcome; Ranke at Berlin from 1825, Prussian state
historiographer from 1841, and his Reformation and Prussian histories; the
Pledge's Columbus Day origin and the 1942 change of salute; colonial troops in
the 1897 procession; the 1889 constitution ceremony in the new palace; the 1790 oath's wording;
on the 1848 caption, that Michelet backed the revolution in Paris (Popkin,
Week 4, p. 86), that historians such as Dahlmann and Droysen sat in the
Frankfurt parliament, and that Ranke, a conservative monarchist, did not take
part.

**Popkin's "Ranke's students" includes Treitschke** (p. 88), and the Week 4
pointer repeats it. Standard biographies have Treitschke studying at Bonn
(under Dahlmann) and Leipzig rather than with Ranke in Berlin. Worth checking
before the pointer's wording is reused again; it is Popkin's claim, not the
deck's.

## Sources for review

Text caches, all in `~/Dropbox/courses/making-history/.research-packets/`:

- `maza-thinking-about-history-ch2.ocr.txt` — pp. 43–86, printed-page markers
- `anderson-imagined-communities-intro.txt` — pp. 1–7, from the PDF's text layer
- `chatterjee-whose-imagined-community.ocr.txt` — pp. 214–225; the scan is
  spreads, so each sheet has a left page from a whole-sheet pass and a right
  page from a half-sheet pass

Every quotation in the deck was checked against the page image on 2026-10-09:
Maza pp. 46, 47, 50, 52, 53, 54, 55, 56, 81, 82; Anderson p. 7; Anderson pp. 5, 6; Chatterjee pp. 216,
217, 218, 220. Maza pp. 48–49, 51 ("denaturalizing"), 51–52 (Anderson's answer) and 53
(the earliest nationalism) were checked against the page images on
2026-10-12. The quotations added on 2026-10-11 — Maza p. 46 (borders) and
p. 52 (symbols; the jubilee caption's "unrecognizable" line) — were checked
against the page images the same day. Ranke's 1824 preface is quoted from the
Week 4 PDF, `~/Dropbox/courses/making-history/leopold-von-ranke-excerpts-from-selected-works-1824-1881`
(German History in Documents and Images; Wines's translation, Fordham, 1981),
which is born-digital.

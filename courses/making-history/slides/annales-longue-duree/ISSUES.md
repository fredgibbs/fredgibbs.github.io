# Issues — Big Structures: the *Annales* and the *longue durée*

Contributor notes for `index.md`. Not built, not served. Open problems first,
then decisions taken on purpose so a later reviewer does not re-raise them.

## Open

**The assigned Green & Troup chapter was not available while this deck was
built.** `~/Dropbox/courses/making-history/` has scans of *The Houses of
History* ch. 2 (Marxist historians) and ch. 10 (Gender), but not ch. 4, "The
*Annales*," 87–95, which `schedule.md` assigns for 5.2. Nothing in the deck is
cited to it and no claim in the deck rests on it — every quotation comes from
a primary text on disk or fetched in full. **What would close this:** scan
87–95 into `~/Dropbox/courses/making-history/` the way the other two chapters
were, OCR it with `scripts/ocr-pdf.swift`, and then check two things: that the
deck does not contradict the chapter students actually read, and whether the
chapter introduces a term or a person the deck should pick up (Le Roy Ladurie
and the *histoire des mentalités* are the likely candidates). Until then the
title slide lists the chapter as background and stops there.

**Bloch's wartime pseudonym is stated on the Febvre portrait slide and is not
verified from a primary source.** The caption says Febvre kept the journal
going through the Occupation "under a changed title and with Bloch writing in
it under a false name." Both halves are standard in the literature — the
journal ran as *Mélanges d'histoire sociale* from 1942, and Bloch signed as
"M. Fougères" — and the pseudonym is suggestive, since Bloch dates the
dedication of the *Apologie* from Fougères in the Creuse on 10 May 1941. But
the deck has no copy of a wartime issue in hand. The caption is worded so it
asserts only the general fact, and the pseudonym itself is not named on any
slide. **What would close this:** a scan of a 1942–44 issue's contents page.

**The Febvre photograph's date is unverifiable.** Both Commons copies date it
*ca.* 1935 and caption it "professeur à la Faculté des lettres de Strasbourg,"
but Febvre moved to the Collège de France in 1933 and the man in the picture
looks well past fifty-seven. The slide caption gives no date, which is the
honest option; do not add one back without a source.

## Decided on purpose

**Braudel's portrait is used under fair use, not a free license — on purpose.**
Every other image in this deck is public domain. `braudel-portrait.jpg` is not:
he died in 1985 and no free photograph of him exists at usable quality (the
Académie française's file is 187×250, the Commons "own work" upload 206×269 and
mis-tagged, this one 434×563). The alternative was leaving the deck's central
figure as the only person in it without a face, with his biography hung on an
aerial photograph of a prison camp. Classroom use of a low-resolution portrait
for identification and commentary is fair use; stock-agency copies at Getty and
Bridgeman were deliberately not used. Full reasoning in `images/README.md`.
Do not "fix" this by deleting the file — if a free portrait at decent
resolution ever surfaces, swap it and update both files.

**The deck quotes the historians, not the textbook.** This is a deliberate
inversion of how 5.1 was built, at the instructor's direction: Green & Troup
carry the session as background reading and the slides run on Braudel's and
Bloch's own words, with the context each was writing in (occupied France, a
prison camp, a chair inherited from a dead friend) given as much room as the
arguments. If this deck is revised, keep that balance.

**The Van Gogh in the cold open is out of period and the caption says so.**
See `images/README.md`. The 1889 date is the point of the pairing, not a
compromise.

**Quotations are given in published English translations, named on the title
slide.** Braudel is Sarah Matthews's translation in *On History* (Chicago,
1980), which is the book the assigned PDF reproduces; Bloch is Peter Putnam's
*The Historian's Craft* (Knopf, 1953). Two consequences worth knowing:

- Putnam renders Bloch's *l'ogre de la légende* as "the giant of the fairy
  tale." The deck does not use that sentence, but a reviewer who goes looking
  for "ogre" in the English will not find it.
- The 1929 editorial is quoted from Matthews's rendering of it inside
  Braudel's 1950 lecture (*On History*, p. 18), not translated fresh from the
  *Annales*. The French original is now cached at
  `.research-packets/annales-1929-a-nos-lecteurs-fr.txt`, checked against
  Persée (`ahess_0003-441x_1929_num_1_1_1031`, p. 1) and Clio-Texte, which
  agree with each other and with Matthews. **The two explanatory blocks on
  that slide paraphrase parts of the editorial Braudel does not reproduce** —
  the "two classes of workers made to understand one another," the ancient /
  medieval / *modernisants* split, and "not by articles on method… but by
  example and by deed." They are written from the French cache, not from
  p. 18, which is why they are paraphrase rather than quotation. A reviewer
  working only from *On History* will not find them there.

**"À nos lecteurs" is attributed to Bloch *and* Febvre on the slide, though
Braudel introduces it as Febvre's.** Braudel writes "Lucien Febvre wrote at
the start of his new review" (p. 18); the editorial in the *Annales* is signed
"LES DIRECTEURS," i.e. both men. The deck follows the signature. Braudel's
attribution is not an error worth a slide, but it is the reason the `.cite`
reads "Bloch and Febvre … trans. in Braudel, p. 18" rather than naming either
as sole author.

**Accents restored inside quotations.** The text layer of
`barudel_on-history.pdf` strips French diacritics — it gives "longue duree,"
"l'histoire evenementielle," "Francois Simiand," "La Mediterranee." The deck
prints these accented, as the book does. That is a normalization, not an
emendation; the OCR damage is documented at the head of
`~/Dropbox/courses/making-history/.research-packets/barudel_on-history.pdftotext.txt`.

**Two quantities in the cold open are deliberately vague.** The Lepanto
caption says "some four hundred galleys" and "tens of thousands of men,"
because the standard figures vary by a wide margin between sources and the
slide's argument does not turn on the number. The notes bullet says the
Ottomans "had rebuilt the fleet" within a year rather than giving a ship
count, for the same reason.

**Braudel "succeeded Febvre at the Collège de France in 1950" — do not
"correct" this to 1949.** Standard accounts have him elected in 1949 and
taking up the chair in 1950, and his inaugural lecture is dated 1 December
1950 in *On History* itself (the source-note to "The Situation of History in
1950"). The jacket note on the same book says "a professor at the Collège de
France in 1949," but that note is unreliable — it also misdates his EPHE
presidency. The deck follows the lecture date.

**Bloch's position in May 1941 is deliberately not stated.** An earlier draft
said he was "stripped of his post"; he was not. He held one of the exemptions
from the October 1940 Statut des Juifs and was teaching at Clermont-Ferrand
and then Montpellier, losing his post only after the Germans took the southern
zone in November 1942. The slide now says only that he was "teaching in the
unoccupied zone and writing from what he has with him," and lets Bloch's own
apology (p. 6) carry the rest. Do not put a sharper claim back in without a
source for the specific year.

## Source texts cached for this deck

All three are beside the readings, not in this repo (see "Cache the text of a
scanned reading" in `courses/SLIDE-STYLE.md`), in
`~/Dropbox/courses/making-history/.research-packets/`:

- `barudel_on-history.pdftotext.txt` — the whole of *On History*, with the
  printed pages of every passage used here listed in the header.
- `bloch-historians-craft-1953-en.txt` — Putnam's English, from the Internet
  Archive.
- `bloch-apologie-1949-fr.txt` — the French original, from Les Classiques des
  sciences sociales.
- `annales-1929-a-nos-lecteurs-fr.txt` — the founding editorial in French,
  from Clio-Texte, verified against Persée.

## Review history

A fresh-context review (required by `AGENTS.md`) was run on the finished deck
and its findings worked before publication. Fixed: the 1950 inaugural lecture
was described as coming *before* *La Méditerranée* was in print when it came
after; the arc slide dated part two to the captivity rather than to the 1949
and 1950 texts it teaches; Bloch's 1941 position was misstated (above); the
p. 34 "total of all possible histories" line was used as evidence that the
past has no direction, which is not what it says; three page cites were off
(Marx pp. 50–51 → p. 51, the "geographical / social / individual time" phrase
pp. 3–4 → p. 4, and the two economy quotations p. 31 → p. 32); the Marx
"not just as they please" line carried no citation; the *Odyssey* was credited
with locating Scylla and Charybdis in the Strait of Messina, which is a later
identification; a notes bullet pointed at the deck's own cold-open slide; the
cold-open notes were split into one slide per image per the style guide; and
the Van Gogh is June–July 1889, not June. The review found no fabricated or
misattributed quotations.

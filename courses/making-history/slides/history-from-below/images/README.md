# Slide Images — History From Below

Eight image files, all used by `../index.md`. Six are public domain, one is
CC BY 4.0 and one is CC BY-SA 4.0 (both credited on their slides). The
eighth, `vansina-portrait.jpg`, is used under fair use for classroom
teaching — see its row and the Notes. Credits are carried in the
`<figcaption>`s, or in the `.credit` line on a `.bleed` slide, and should not
be stripped.

If you change a filename, update the matching `<img src="…">` or
`data-background-image` in `../index.md` — note that `lepanto-1571.jpg`,
`peterloo-1819.jpg`, `griot-conakry-c1910.jpg` and `joanna-southcott-1814.jpg`
are each referenced **twice**. The first three run full-bleed, then again
reduced on the `.image-notes` slide that unpacks it: Lepanto and Peterloo in
the cold open, the postcard at the head of part three. Southcott gets her own
image slide in part two and then returns small, in the `.with-figure` column
of the part-two discussion slide, so the face stays in front of the room while
it argues about her followers.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `lepanto-1571.jpg` | The Battle of Lepanto, 7 October 1571 — a near-contemporary oil of the whole engagement, galleys packed edge to edge, every hull's oars out and no rower drawn. Opens the cold open, full-bleed and again on its notes slide. **Also used in `annales-longue-duree`** — see Notes | Unknown painter, late 16th c.; National Maritime Museum, Greenwich, BHC0261, via Wikimedia Commons ("Battle of Lepanto 1571.jpg") | Public domain |
| `peterloo-1819.jpg` | Richard Carlile, *To Henry Hunt, Esq.* — aquatint and etching published 1 October 1819, showing the yeomanry cavalry riding into the reform meeting at St Peter's Field, Manchester, 16 August 1819. Cold open, full-bleed and again on its notes slide. **A crop** — see Notes | Photograph by "APK" of the impression in the National Portrait Gallery, London, via Wikimedia Commons ("Peterloo Massacre by Richard Carlile.jpg") | CC BY 4.0 |
| `griot-conakry-c1910.jpg` | *Conakry — Groupe Soussous*, a French colonial postcard from Guinea, c. 1910: a standing griot holding an *ngoni* lute behind two seated women. Opens part three, full-bleed and again on its notes slide | Unknown photographer, c. 1910; from the collection of Shlomo Pestcoe, via Wikimedia Commons ("Susu Griot, circa 1910, Conakry, Guinea.jpg") | Public domain |
| `henry-viii.jpg` | Full-length portrait of Henry VIII, after Hans Holbein the Younger. Part one, the case that "great man" history genuinely fits | Google Art Project, via Wikimedia Commons ("After Hans Holbein the Younger - Portrait of Henry VIII - Google Art Project.jpg") | Public domain |
| `thompson-1980.jpg` | E. P. Thompson speaking through a megaphone at an anti-nuclear rally, Oxford, 1980. Part two, the portrait slide. **A crop** — see Notes | Kim Traynor, 1980, via Wikimedia Commons ("E P Thompson at 1980 protest rally.JPG") | CC BY-SA 4.0 |
| `leader-of-the-luddites-1812.jpg` | *The Leader of the Luddites*, hand-colored etching published May 1812 by Walker and Knight — "General Ludd" in a woman's dress before a burning mill, inscribed "Drawn from Life by an Officer" | Working Class Movement Library catalog, via Wikimedia Commons ("Luddite.jpg") | Public domain |
| `joanna-southcott-1814.jpg` | Joanna Southcott (1750–1814), stipple engraving published by John Bell, 2 October 1814, with her engraved signature. Part two, the person Thompson names last in the condescension passage; shown again small on the part-two discussion slide. **A crop** — see Notes | KU Leuven print collection PA06781, via Wikimedia Commons ("Joanna Southcott, PA06781.jpg") | Public domain |
| `vansina-portrait.jpg` | Jan Vansina (1929–2017), black-and-white head-and-shoulders portrait. Part three, the portrait slide | University of Wisconsin–Madison Department of History obituary, 9 February 2017 (`history.wisc.edu/2017/02/09/jan-vansina-1929-2017/`) | **Fair use** — see Notes |

Retrieved 2026-09-19; the seven Commons files via the `Special:FilePath`
endpoint. `lepanto-1571.jpg` was copied from `annales-longue-duree/images/`
on 2026-09-22. The folder totals ~4.3 MB, inside the ~10 MB ceiling.

## Notes

**Three files are crops.** None is annotated — nothing has been added to any
image, only edges removed. Re-make them from the sources above with:

```sh
# Peterloo: trim the dark photographic frame around the mounted print
magick raw/peterloo.jpg -crop 3170x2790+70+45 +repage -resize 1800x1800\> -quality 84 peterloo-1819.jpg
# Thompson: he stands at the far left of a wide frame; crop to him and the crowd
magick raw/thompson.jpg -crop 700x1290+30+150 +repage -resize 1800x1800\> -quality 86 thompson-1980.jpg
# Southcott: keep the plate and the engraved signature, drop the blank sheet below
magick raw/southcott.jpg -crop 1200x1740+35+40 +repage -resize 1800x1800\> -quality 86 joanna-southcott-1814.jpg
```

The other four were resized only: `-resize 1800x1800\> -quality 84`.

**`lepanto-1571.jpg` is deliberately the same file as `annales-longue-duree`
uses, and the repeat is the point.** In 5.1 it is Braudel's event — the
loudest afternoon of the century, read as surface over the *longue durée*.
Here it opens 6.1 doing different work: the same painting asked who is in it,
answered by the oars. Every hull has its banks out and not one man pulling
them is drawn, though slaves, convicts and the very poor moved every ship on
that water. The 5.1 notes slide already has students noticing that the
painter "gives them no faces", so 6.1 picks up a thread the course laid
rather than introducing a picture cold. Keep the two decks' copies in sync if
either is re-fetched, and do not recaption this one as a battle piece: the
deck uses it as an example of what a history of Lepanto was allowed to leave
out.

**`griot-conakry-c1910.jpg` is a colonial ethnographic postcard, and the deck
uses it as one.** It is not a photograph of a griot performing; it is a studio
pose, made in French Guinea for sale to Europeans, captioning three people as
"Groupe Soussous" — a type, not names. That is why it opens part three: the
card is at once the best evidence the deck has that a person can be a record,
and a demonstration of a source whose maker had no reason to learn a name.

**What can and cannot be said about the two women.** Nothing is recorded about
them anywhere: the card captions all three sitters as "Groupe Soussous", and
the Commons file description (from Shlomo Pestcoe's collection) adds only "a
Susu griot holds a lute with a figure '8' shape body, about 1910, standing
behind two sitting women." They cannot be named and their role cannot be
asserted. What the slide says instead is documented ethnography: across Mande
music — the Susu are a Mande people — the instruments are men's work and song
is the women's specialism, with female jeli (*jelimusow*) specialising in
singing while male jeli may take speech, song or instruments. So the second
bullet puts it conditionally ("if the voice is the record"), because whether
these two were performers is exactly what the card forecloses. Do not rewrite
that bullet to state that they were singers. On the instrument name: Commons
notes that Mande speakers, Susu among them, call these lutes *nkoni* or
*ngoni*, so the caption's *ngoni* is correct and should not be "fixed" to
*koni*.

The notes slide ran three bullets until 2026-09-22, then two, and from
2026-09-22 three again — but not the original three. The cut third
("evidence anyway … for what that market wanted Africa to look like in 1910")
was cut: it was an inference about a market that is not visible in the frame,
and it pre-empted Vansina's "testify despite themselves" (p. 28) two slides
later with a photograph, where his phrase is about *oral* sources not concerned
with the past. That block on the definition slide explains the idea from
Vansina directly and never needed the setup. The two bullets that remain are
the one job only this picture can do — the record is a person — and the
qualification that this is not documentary evidence of it. Do not recaption it
as a neutral picture of a griot at work. The sitters are unidentified and cannot
now be named; the caption identifies the standing man by his instrument rather
than asserting who he was.

**`vansina-portrait.jpg` is the one file here not cleared by license.** No
free portrait of Vansina exists: he died in 2017, Wikimedia Commons holds no
photograph of him (searched 2026-09-19 under "Jan Vansina", which returns only
his father Dirk and unrelated maps), and the obituary notices that carry a
photograph are all rights-reserved. The alternative was leaving the third of
the session's three central figures the only one without a face, in a deck
whose other two subjects both have free images. The copy used here is the
source file at its published size — 407 × 298, ~35 KB — taken from the
university department's own memorial notice rather than from a licensing
agency, shown for identification and commentary in a non-commercial teaching
deck. Recorded in `../ISSUES.md` as a deliberate deviation so a later pass
does not delete it as unlicensed.

**Dates deliberately left off the Vansina caption.** His Kuba fieldwork years
and the date of his earlier method book could not be confirmed from a source
to hand: the UW–Madison obituary gives *La tradition orale* (1960) and a 1960
start at Wisconsin, Wikipedia gives 1965 for the English translation, and the
French original is usually dated 1961. The caption gives only what they agree
on and names no year for that book. Fix it from *Living with Africa* (1994),
his memoir, if someone has a copy.

**The Luddite caption quotes the print, not the catalog.** The engraved
script on this impression reads *Drawn from Life by an Officer*. Museum
records (Met, British Museum) give "Drawn from the life by an Officer"; the
image was checked at full resolution and there is no "the". Don't "correct" it
to match a catalog entry.

**The Peterloo and Southcott captions carry contested or checkable numbers.**
Peterloo's death toll is given as eighteen, the figure current since Bush's
work on the casualty lists; older accounts say eleven or fifteen. Southcott
died on 27 December 1814 and the engraving was published on 2 October, so the
caption says October and "she died that December" rather than rounding to a
number of months.

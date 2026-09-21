# Slide Images — History From Below

Seven image files, all used by `../index.md`. Five are public domain, one is
CC BY 4.0 and one is CC BY-SA 4.0 (both credited in their captions). The
seventh, `vansina-portrait.jpg`, is used under fair use for classroom
teaching — see its row and the Notes. Credits are carried in the
`<figcaption>`s and should not be stripped.

If you change a filename, update the matching `<img src="…">` in `../index.md`
— note that `peterloo-1819.jpg` and `griot-conakry-c1910.jpg` are each
referenced **twice**: full-bleed, then again reduced on the `.image-notes`
slide that unpacks it. Peterloo does that in the cold open, the postcard at
the head of part three.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `peterloo-1819.jpg` | Richard Carlile, *To Henry Hunt, Esq.* — aquatint and etching published 1 October 1819, showing the yeomanry cavalry riding into the reform meeting at St Peter's Field, Manchester, 16 August 1819. Cold open, full-bleed and again on its notes slide. **A crop** — see Notes | Photograph by "APK" of the impression in the National Portrait Gallery, London, via Wikimedia Commons ("Peterloo Massacre by Richard Carlile.jpg") | CC BY 4.0 |
| `griot-conakry-c1910.jpg` | *Conakry — Groupe Soussous*, a French colonial postcard from Guinea, c. 1910: a standing griot holding an *ngoni* lute behind two seated women. Opens part three, full-bleed and again on its notes slide | Unknown photographer, c. 1910; from the collection of Shlomo Pestcoe, via Wikimedia Commons ("Susu Griot, circa 1910, Conakry, Guinea.jpg") | Public domain |
| `henry-viii.jpg` | Full-length portrait of Henry VIII, after Hans Holbein the Younger. Part one, the case that "great man" history genuinely fits | Google Art Project, via Wikimedia Commons ("After Hans Holbein the Younger - Portrait of Henry VIII - Google Art Project.jpg") | Public domain |
| `thompson-1980.jpg` | E. P. Thompson speaking through a megaphone at an anti-nuclear rally, Oxford, 1980. Part two, the portrait slide. **A crop** — see Notes | Kim Traynor, 1980, via Wikimedia Commons ("E P Thompson at 1980 protest rally.JPG") | CC BY-SA 4.0 |
| `leader-of-the-luddites-1812.jpg` | *The Leader of the Luddites*, hand-coloured etching published May 1812 by Walker and Knight — "General Ludd" in a woman's dress before a burning mill, inscribed "Drawn from Life by an Officer" | Working Class Movement Library catalogue, via Wikimedia Commons ("Luddite.jpg") | Public domain |
| `joanna-southcott-1814.jpg` | Joanna Southcott (1750–1814), stipple engraving published by John Bell, 2 October 1814, with her engraved signature. Part two, the person Thompson names last in the condescension passage. **A crop** — see Notes | KU Leuven print collection PA06781, via Wikimedia Commons ("Joanna Southcott, PA06781.jpg") | Public domain |
| `vansina-portrait.jpg` | Jan Vansina (1929–2017), black-and-white head-and-shoulders portrait. Part three, the portrait slide | University of Wisconsin–Madison Department of History obituary, 9 February 2017 (`history.wisc.edu/2017/02/09/jan-vansina-1929-2017/`) | **Fair use** — see Notes |

Retrieved 2026-09-19; the six Commons files via the `Special:FilePath`
endpoint. The folder totals ~3.6 MB, inside the ~10 MB ceiling.

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

**`griot-conakry-c1910.jpg` is a colonial ethnographic postcard, and the deck
uses it as one.** It is not a photograph of a griot performing; it is a studio
pose, made in French Guinea for sale to Europeans, captioning three people as
"Groupe Soussous" — a type, not names. That is why it opens part three: the
card is at once the best evidence the deck has that a person can be a record,
and a demonstration of a source whose maker had no reason to learn a name. The
`.image-notes` bullets work both halves, and the third sets up Vansina's
"testify despite themselves" (p. 28) two slides later. Do not recaption it as
a neutral picture of a griot at work. The sitters are unidentified and cannot
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

**The Luddite caption quotes the print, not the catalogue.** The engraved
script on this impression reads *Drawn from Life by an Officer*. Museum
records (Met, British Museum) give "Drawn from the life by an Officer"; the
image was checked at full resolution and there is no "the". Don't "correct" it
to match a catalogue entry.

**The Peterloo and Southcott captions carry contested or checkable numbers.**
Peterloo's death toll is given as eighteen, the figure current since Bush's
work on the casualty lists; older accounts say eleven or fifteen. Southcott
died on 27 December 1814 and the engraving was published on 2 October, so the
caption says October and "she died that December" rather than rounding to a
number of months.

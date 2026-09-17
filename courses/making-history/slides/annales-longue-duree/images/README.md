# Slide Images — Big Structures: the *Annales* and the *longue durée*

Eight image files, all used by `../index.md`. Seven are public domain. The eighth, `braudel-portrait.jpg`, is used under
fair use for classroom teaching — see its row and the Notes. Credits are
carried in the `<figcaption>`s and should not be stripped.

If you change a filename, update the matching `<img src="…">` in `../index.md`
— note that `lepanto-1571.jpg`, `olive-trees-1889.jpg` and `messina-1572.jpg`
are each referenced **twice**, full-bleed and again reduced on an
`.image-notes` slide.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `lepanto-1571.jpg` | The Battle of Lepanto, 7 October 1571 — a near-contemporary oil painting of the whole engagement, galleys packed from edge to edge. Cold open, image 1 | Unknown painter, late 16th c.; National Maritime Museum, Greenwich, BHC0261, via Wikimedia Commons ("Battle of Lepanto 1571.jpg") | Public domain |
| `olive-trees-1889.jpg` | Vincent van Gogh, *The Olive Trees*, June 1889, oil on canvas — an olive grove on a stony hillside below the Alpilles. Cold open, image 2, shown as the contrast to Lepanto | Museum of Modern Art, New York, via Wikimedia Commons ("Van Gogh The Olive Trees..jpg") | Public domain |
| `bloch-1930s.jpg` | Marc Bloch (1886–1944), identity photograph, 1930s | Unknown photographer; via Wikimedia Commons ("Marc Bloch (1886-1944).jpg") | Public domain |
| `febvre-portrait.jpg` | Lucien Febvre (1878–1956), press photograph: elderly, in a dark suit, hands on a cane. **Date uncertain** — see Notes | Bibliothèque nationale et universitaire de Strasbourg / BnF, `btv1b10219609x`, via Wikimedia Commons | Public domain |
| `braudel-portrait.jpg` | Fernand Braudel (1902–1985), head-and-shoulders portrait, bookshelves behind him. Part two, the portrait slide | Jerry Bauer, 1988; from the dust jacket of *The Identity of France*. Mirrored at Wikimedia Commons ("Photo of Fernand Braudel on The Identity of France dustjacket.jpg"), which tags it public domain | **Fair use** — see Notes |
| `oflag-xc-1945.jpg` | Oflag X-C, Lübeck, from a US aircraft, 26 April 1945: hut rows inside wire, with `P.o.W` and `R.A.F` laid out in white on the open ground. Braudel was a prisoner here | US aerial photograph, 26 April 1945; memoireetavenir.fr, via Wikimedia Commons ("Oflag X-C aerial 1945.jpg") | Public domain |
| `messina-1572.jpg` | Messina from Braun and Hogenberg, *Civitates Orbis Terrarum*, vol. 1 (1572) — the sickle harbour behind its sandspit, crowded with shipping. **A crop** — see Notes | Universitätsbibliothek Heidelberg, 1582 German edition (*Beschreibung vnd Contrafactur der vornembster Stät der Welt*), via Wikimedia Commons ("Braun Messina UBHD.jpg") | Public domain |
| `mediterranean-chart-1569.jpg` | Chart of the Mediterranean and NE Atlantic, Paolo Forlani after Diogo Homem, Venice 1569 — engraved, hand-coloured, rhumb lines throughout. **A crop** — see Notes | National Maritime Museum, Greenwich, via Wikimedia Commons ("Mediterranean and NE Atlantic RMG F0495.tiff") | Public domain |

Retrieved 2026-09-16, all seven via the Wikimedia Commons `Special:FilePath`
endpoint. The folder totals ~5.3 MB, inside the ~10 MB ceiling.

## Notes

**`braudel-portrait.jpg` is the one file here not cleared by license.** No free
portrait of Braudel exists at usable quality: he died in 1985, photographs of
him remain in copyright, and the only candidates in circulation are small — the
Académie française's own file is 187×250, the Commons "own work" upload 206×269
and demonstrably mis-tagged, and this one 434×563. Commons tags this one public
domain as a 1988 Jerry Bauer photograph, which is possible but not something to
rely on. It is used here under fair use for in-class teaching: a low-resolution
portrait of a historical figure, shown for identification and commentary in a
non-commercial course deck, which takes nothing from the market for the
original. Commercial stock versions exist at Getty and Bridgeman and were
deliberately not used, since taking from a licensing agency is the use that
weighs hardest against fair use. It reads well projected in spite of its size
because the head fills the frame.

- Sourced at width 1033–3840, capped at 1800 px on the long edge and
  recompressed to JPEG. The two paintings are at q84; the engraved map, the
  engraved city view and the grainy aerial photograph at q88, since ruled
  rhumb lines, hatching and film grain smear visibly below that. The Bloch
  and Febvre photographs are at q84 and were not upscaled — the Commons
  originals are only 840×840 and 1240×1752, which is the cap for those two.

      curl -L -H 'User-Agent: your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2200' -o raw
      sips -Z 1800 raw --out out.jpg -s format jpeg -s formatOptions 84

- **`messina-1572.jpg` is a crop.** The Commons file is a photograph of the
  whole opened atlas: the double-page plate inside an orange printed frame,
  with a 167-item numbered key to the city's streets and buildings running
  along the foot. The crop keeps the view and the cartouche and drops the key,
  which is illegible at projector size and costs about a fifth of the height.
  The book's gutter still runs down the middle of the image; that is the
  object, not a defect, and nothing in the deck turns on what it hides.
  Nothing was added — no boxes, arrows or annotation. Regenerate with:

      curl -L -H 'User-Agent: your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/Braun%20Messina%20UBHD.jpg?width=2120' -o raw
      # raw is 2120x1533; sips -c takes HEIGHT WIDTH, --cropOffset takes TOP LEFT
      sips -c 1161 1998 --cropOffset 58 64 raw --out crop.jpg
      sips -Z 1800 crop.jpg --out messina-1572.jpg -s format jpeg -s formatOptions 88

- **`mediterranean-chart-1569.jpg` is a crop** to the engraved neatline. The
  Commons scan includes the modern backing sheet the chart is mounted on,
  which carries archival pencil shelfmarks along the bottom edge
  ("Forlani Venice 1569", "G230:1/21", "550–"). The crop drops the mount and
  keeps the whole printed chart including its red-and-white border strip —
  which, per the museum's own record, is a later addition to the 1569
  engraving. Regenerate with:

      curl -L -H 'User-Agent: your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/Mediterranean%20and%20NE%20Atlantic%20RMG%20F0495.tiff?width=3840' -o raw
      # raw is 3840x2413; sips -c takes HEIGHT WIDTH, --cropOffset takes TOP LEFT
      sips -c 2200 3620 --cropOffset 70 120 raw --out crop.jpg
      sips -Z 1800 crop.jpg --out mediterranean-chart-1569.jpg -s format jpeg -s formatOptions 88

- **The Van Gogh is deliberately out of period, and the caption says so.**
  Every other image in the deck is sixteenth-century or documentary. *The
  Olive Trees* is 1889, and the cold open works only because a student can see
  the date: the pairing asks which of a 1571 battle and an 1889 hillside is a
  picture of the sixteenth-century Mediterranean, and the answer the session
  argues for is "both, at different speeds." Do not swap it for a period
  landscape — that would dissolve the point — and do not drop the date from
  the caption.

- **The Febvre photograph's date is not settled.** Both Commons copies of it
  (this one and the smaller `Lucien Febvre-Strasbourg.jpg`, which is the same
  photograph) are captioned "professeur à la Faculté des lettres de
  Strasbourg" and dated *ca.* 1935, but Febvre left Strasbourg for the Collège
  de France in 1933 and the man in the picture reads as considerably older
  than fifty-seven. The slide caption therefore gives no date. See
  `../ISSUES.md`.

- **No usable portrait of Braudel exists under a free license.** The only
  Commons file is 206×269 px, far too small to project, and its "own work /
  CC BY-SA 4.0" tag is claimed by a 2022 uploader for what the file
  description says is a 1945 photograph — a claim the uploader is not in a
  position to make. Braudel is introduced instead on the Oflag X-C aerial
  photograph, which is where he wrote the book. See `../ISSUES.md`.

- **The aerial photograph is grainy on purpose and should not be "fixed."**
  It is 1945 reconnaissance film. Its legible details — the hut rows, the wire,
  and the `P.o.W` and `R.A.F` letters the prisoners laid out on the ground —
  are what the caption and the deck point at. Contrast was not adjusted; the
  file is resize-and-recompress only, like the rest.

# Slide Images — Scientific History

Seven images used by `../index.md`: all public domain. Nothing here requires
attribution by license, but credits are kept anyway.

If you change a filename, update the matching `<img src="…">` in `../index.md`.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `ranke-library-1880s.jpg` | Leopold von Ranke in his library, early 1880s — the cold open, used twice: full-bleed, then reduced beside notes on the `.image-notes` slide | Leopold von Ranke Papers, Special Collections Research Center, Syracuse University, via Wikimedia Commons | Public domain |
| `humboldt-lawrence-portrait.jpg` | Wilhelm von Humboldt (1767–1835), by Sir Thomas Lawrence — one of the allied statesmen painted for George IV's Waterloo Chamber at Windsor | Royal Collection Trust, RCIN 404936 | Public domain |
| `ranke-jebens-portrait-1875.jpg` | Leopold von Ranke aged about eighty, 1875, with two Prussian decorations on his chest | Adolf Jebens, 1875 | Public domain |
| `ranke-titlepage-1824.jpg` | Title page of Ranke's *Geschichten der romanischen und germanischen Völker von 1494 bis 1535*, volume one, Leipzig and Berlin, G. Reimer, 1824 — the first edition of the book whose preface students read | Internet Archive, `geschichtenderro00rank` | Public domain |
| `ranke-vorrede-1824.jpg` | Page VI of the same book's preface: the top three lines carry *er will bloß sagen, wie es eigentlich gewesen*, and the paragraph below lists the sources and promises they will be named on every page. **A crop** — see Notes | Internet Archive, `geschichtenderro00rank` | Public domain |
| `treitschke-hoersaal-1879.jpg` | Heinrich von Treitschke lecturing, 1879 — contemporary engraving, artist unrecorded | Wikimedia Commons ("Heinrich von Treitschke im Hörsaal") | Public domain |
| `mount-vernon-1858.jpg` | Mount Vernon photographed in 1858, the year the Mount Vernon Ladies' Association completed its purchase, with the piazza roof propped on ship's masts | Wikimedia Commons ("Mount Vernon 1858.jpg"), photographer unknown | Public domain |

Retrieved 2026-09-09, the five Commons files via `Special:FilePath`, the two
Ranke book pages via the Internet Archive page-image endpoint. The folder
totals ~3.9 MB, well inside the ~10 MB ceiling.

## Notes

- Sourced at width 1300–2200, capped at 1800 px on the long edge and
  recompressed to JPEG. Portraits and the library photograph are at q80–82;
  the two book pages are at q88, since Fraktur type smears badly at lower
  quality and the whole point of `ranke-vorrede-1824.jpg` is that the famous
  sentence stays readable on a projector.
- **`ranke-vorrede-1824.jpg` is a crop**, and the caption on the slide says so.
  The full page also carries a footnote in small type at the foot (a note on
  how Ranke spells "Loys" and "Hernando") and wide paper margins; the crop
  keeps the running head "VI", the sentence, and the source paragraph — which
  is the whole argument of that slide. Regenerate both Ranke pages with:

      curl -L -H 'User-Agent: your-name (your-email)' \
        'https://archive.org/download/geschichtenderro00rank/page/n4_w1600.jpg' -o raw4.jpg
      sips -Z 1800 raw4.jpg --out ranke-titlepage-1824.jpg -s format jpeg -s formatOptions 88

      curl -L -H 'User-Agent: your-name (your-email)' \
        'https://archive.org/download/geschichtenderro00rank/page/n9_w1600.jpg' -o raw9.jpg
      magick raw9.jpg -crop 1950x2350+150+200 +repage -resize x1800 -quality 88 ranke-vorrede-1824.jpg

  Note that the scanned volume is titled *von 1494 bis 1535* on its title page
  even though this first volume only reaches 1514; later editions corrected the
  title to *bis 1514*. Don't "fix" the caption to match the schedule.
- **`humboldt-lawrence-portrait.jpg` carries no date in the caption on purpose.**
  Wikimedia Commons records none, and the Royal Collection's own catalogue page
  (rct.uk) refuses automated requests, so the date could not be confirmed
  against the holding institution. Secondary sources put the sitting around
  1828 and say Lawrence left it unfinished at his death in 1830, with the
  canvas completed by Richard Evans — plausible, but unverified here, so none
  of it is asserted on the slide. If you can reach the RCT record, add the date
  to the caption.
- `ranke-jebens-portrait-1875.jpg` is used for the **two decorations** visible
  on Ranke's chest, which the caption points at: Popkin (p. 82) has Ranke
  arguing that a historian's work should be judged by professional peers
  "rather than by the reactions of the public or honors awarded by rulers," and
  he is wearing the honors. Don't crop them out.
- `humboldt-lawrence-portrait.jpg` and `ranke-jebens-portrait-1875.jpg` carry a
  deliberate contrast — no decorations against two Prussian decorations — but
  neither caption points at the other, since three slides now sit between them
  and a cross-reference by slide count breaks on the next edit. They are
  **not** a `pair` figure: each carries a point of its own and gets its own
  slide. Each portrait also comes *before* its subject's bio slide, per the
  portrait-first rule in `../../../SLIDE-STYLE.md`.
- `ranke-library-1880s.jpg` is soft and low-contrast by modern standards — an
  early-1880s interior exposure — and that is why it works full-bleed: the man
  really is hard to find among the shelves, which is the argument the notes
  slide makes. Don't "improve" it with a levels pass; the murk is the point.
  It is the only image shown twice, at full bleed and reduced inside
  `.image-notes`. Both references point at this one file; don't add a smaller
  duplicate.
- `treitschke-hoersaal-1879.jpg` (1268×973) and `mount-vernon-1858.jpg`
  (1500×978) are the two landscape figures, and the two images sourced below
  the 1400 px floor — Commons holds no larger copy of either. Both display at
  roughly 880 px wide, so the shortfall is not visible.
- `mount-vernon-1858.jpg` (added after the cold-reader review, to break a
  nine-slide imageless run at the end of the deck) is dated to the year the
  Mount Vernon Ladies' Association completed its purchase, and shows the house
  in the disrepair that prompted it — the piazza roof propped on ship's masts.
  It is used for the argument, not the architecture: Popkin (pp. 93–94) has
  women leading the creation of the first American house museum while being
  excluded from the seminars that conferred academic standing, and says such
  museums "conveyed the message that women contributed to history by creating
  tasteful domestic environments for the male protagonists of public affairs."
  Sourced at its full 1500 px (Commons holds nothing larger), q82, landscape.

      curl -L -H 'User-Agent: your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/Mount%20Vernon%201858.jpg?width=1500' -o raw.jpg
      sips -Z 1500 raw.jpg --out mount-vernon-1858.jpg -s format jpeg -s formatOptions 82

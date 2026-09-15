# Slide Images — Marx and the Motor of History

Twelve image files, eleven used by `../index.md`: public domain and CC0. Nothing
here requires attribution by license, but credits are kept anyway.

If you change a filename, update the matching `<img src="…">` in `../index.md`.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `bm-reading-room-1859.jpg` | The Reading Room of the British Museum, 1859 — wood engraving of Sydney Smirke's domed room, opened 1857. The cold open, used twice: full-bleed, then reduced beside notes on the `.image-notes` slide. **A crop** — see Notes | Library of Congress, LC-DIG-ppmsca-15551, via Wikimedia Commons | Public domain |
| `marx-mayall-1875.jpg` | Karl Marx (1818–1883), studio portrait, 1875 — the standard late photograph | John Jabez Edwin Mayall, 1875; Städel Museum, via Wikimedia Commons | Public domain |
| `engels-c1860.jpg` | Friedrich Engels (1820–1895), oval studio photograph, c. 1860 | Amsler & Ruthardt / Edward Gooch Collection, via Wikimedia Commons | Public domain |
| `manifest-titlepage-1848.jpg` | Title page of *Manifest der Kommunistischen Partei*, the first edition, London, February 1848 — printed for the Bildungs-Gesellschaft für Arbeiter by J. E. Burghard, 46 Liverpool Street, Bishopsgate. Carries **no author name**, plus two later pencil annotations | Wikimedia Commons, "Manifest der kommunistischen Partei (Marx) 001.jpg"; scan from *The Making of the Modern World* (Gale) | Public domain |
| `church-west-rock-1849.jpg` | Frederic Edwin Church, *West Rock, New Haven*, 1849, oil on canvas — Hudson River School pastoral: haymakers, a river, a church spire, no industry. The first cold-open image, shown before Manchester as its contrast | New Britain Museum of American Art, via Wikimedia Commons ("Frederic Church - West Rock, New Haven.jpg"); fetched at width 2000, `sips -Z 1800`, JPEG q82 | Public domain |
| `manchester-kersal-moor-1852.jpg` | *Manchester from Kersal Moor, with rustic figures and goats*, William Wyld, 1852 — pastoral foreground, a horizon of mill chimneys | Royal Collection, via Google Art Project / Wikimedia Commons | Public domain |
| `powerloom-weaving-1835.jpg` | Power-loom weaving, plate from Edward Baines, *History of the Cotton Manufacture in Great Britain* (1835) — a promotional image from a defence of the industry; the workforce shown is almost entirely female | T. Allom (illustrator), J. Tingle (engraver), 1835, via Wikimedia Commons | Public domain |
| `kennington-common-1848.jpg` | The great Chartist meeting on Kennington Common, 10 April 1848 — daguerreotype, among the earliest photographs of a crowd | William Edward Kilburn, 1848; Royal Collection, via Google Art Project / Wikimedia Commons | Public domain |
| `paris-barricade-before-1848-06-25.jpg` | Charles François Thibault, daguerreotype of the rue Saint-Maur-Popincourt barricades, Sunday 25 June 1848, about 7:30 a.m., before the attack; framed, with a mount label reading "Barricades dans le Faub.g du Temple le 25 juin 1848, à 7h½ du matin" | Musée Carnavalet, PH2861, via Wikimedia Commons ("Barricades dans le Faub.g du Temple le 25 juin 1848, à 7h12 du matin, PH2861(4).jpg"); q86 | CC0 |
| `paris-barricade-after-1848-06-26.jpg` | Thibault's second plate of the same street, Monday 26 June 1848, after General Lamoricière's troops attacked. A copy print (contretype) of the daguerreotype in the Musée d'Orsay, showing the whole plate | Musée Carnavalet, via Wikimedia Commons ("Contretype d'un daguerréotype de Thibault conservé au musée d'Orsay. Barricades de la rue Saint-Maur, le 26 Juin 1848, a, Paris Musées 20230513094941.jpg"); q86 | CC0 |
| `hervieu-love-conquered-fear-1839.jpg` | Auguste Hervieu, "Love conquered Fear," etched plate for Frances Trollope, *The Life and Adventures of Michael Armstrong, the Factory Boy*: a mill spinning room with ragged children, the owner in a top hat, and a child under the mule. Imprint "London, Published April 20, 1839, by Henry Colburn"; faces ch. VIII (pp. 77–83). **A crop** — see Notes | Library of Congress copy of the 1840 edition, Internet Archive `lifeadventuresof00tro`, leaf n104 | Public domain |
| `peterloo-1819.jpg` | The Peterloo Massacre, St Peter's Field, Manchester, 16 August 1819 — hand-coloured aquatint and etching published 1 October 1819, dedicated to Henry Hunt "and to the female Reformers of Manchester and the adjacent towns" | Richard Carlile, 1819, via Wikimedia Commons | Public domain |

Retrieved 2026-09-11, all nine via the Wikimedia Commons `Special:FilePath`
endpoint. The folder totals ~5.6 MB, inside the ~10 MB ceiling.

## Notes

- Sourced at width 1280–2200, capped at 1800 px on the long edge and
  recompressed to JPEG. Portraits are at q82; the Manchester watercolour at
  q84; the Kennington daguerreotype at q86; and the four line-based images —
  the Reading Room engraving, the 1848 title page, the power-loom plate and
  the Peterloo print — at q88, since engraved hatching and blackletter type
  smear visibly below that.

      curl -L -H 'User-Agent: your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2200' -o raw
      sips -Z 1800 raw --out out.jpg -s format jpeg -s formatOptions 88

- **`bm-reading-room-1859.jpg` is a crop**, and `../ISSUES.md` records it as a
  deliberate deviation. The Library of Congress file is a scan of the whole
  printed page: the plate sits in a wide margin with text from the facing leaf
  showing through on both sides and a fragment of a caption line below. The
  crop keeps the plate. Faint show-through survives along the top edge and
  reads as paper texture rather than as anything added. Regenerate with:

      curl -L -H 'User-Agent: your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/Reading-room%20of%20the%20British%20Museum%20LCCN2007682650.jpg?width=2200' -o raw
      # raw is 3840x2318; sips -c takes HEIGHT WIDTH, --cropOffset takes TOP LEFT
      sips -c 2230 3560 --cropOffset 10 140 raw --out crop.jpg
      sips -Z 1800 crop.jpg --out bm-reading-room-1859.jpg -s format jpeg -s formatOptions 88

  Nothing was added to the image — no boxes, arrows or annotation. The other
  eight files are unmodified apart from resize and recompression.

- **The 1848 title page carries two pencil annotations that are not part of
  the printing**: "Karl Marx" written across the middle of the sheet and
  "1848?" at the foot. Both were added later by a cataloguer, and the caption
  on the slide says so — the point of the slide is that the first edition names
  no author, so a reader has to be told which marks are the printer's and which
  are a librarian's.

- **The barricade pair replaces a single ambiguous plate** (2026-09-15). The
  old `paris-barricade-1848.jpg` was a retouched Commons file whose own record
  gave both dates. Musée Carnavalet's records settle it: PH2861 is the Sunday
  25 June plate, *avant l'attaque*, and the contretype of the Musée d'Orsay
  daguerreotype is Monday 26 June, *après l'attaque*. The Sunday file is the
  framed plate, kept with its mount because the label is part of the object.
  The label says "Faub.g du Temple," and Commons's title misreads "7h½" as
  "7h12." The Monday file is a black-and-white copy print, because Carnavalet's
  CC0 scan of the Orsay plate is the clearest version available. Both are
  recompressed at q86 with no other changes. Regenerate with:

      curl -L -H 'User-Agent: your-name (your-email)' \
        "https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2200" -o raw
      sips -Z 1800 raw --out out.jpg -s format jpeg -s formatOptions 86

- **`hervieu-love-conquered-fear-1839.jpg` is a crop** of the full page scan,
  keeping the etched frame. It drops the margins, the engraved title "Love
  conquered Fear" and the imprint line, which the caption carries instead. The
  attribution to Auguste Hervieu, Trollope's illustrator, follows Wikimedia
  Commons; the plate in the scan is unsigned where legible. Regenerate with:

      curl -L 'https://archive.org/download/lifeadventuresof00tro/page/n104_w2400.jpg' -o raw
      # raw is 2479x4084; sips -c takes HEIGHT WIDTH, --cropOffset takes TOP LEFT
      sips -c 2960 2080 --cropOffset 310 250 raw --out crop.jpg
      sips -Z 1800 crop.jpg --out hervieu-love-conquered-fear-1839.jpg -s format jpeg -s formatOptions 88

- **The Chartist meeting is a daguerreotype**, so it is laterally reversed
  relative to the scene unless the photographer corrected for it. Nothing in
  the deck turns on left and right in that image.

- **The factory images are a deliberate pair of arguments.** The Baines
  power-loom plate comes from a book arguing the cotton manufacture was a
  national benefit, and the Wyld watercolour makes industrial smoke look golden.
  Hervieu's plate is the other side: a novel written against the factory
  system. The factory notes slide sets Baines and Hervieu side by side, and its
  point is that both are persuasion. Do not present Hervieu as the "accurate"
  picture or replace Baines with one.

# Slide Images — Enlightenment Progress, part one

7 images used by `../index.md`: all public domain or CC0. Nothing here
requires attribution by license, but credits are kept anyway.

If you change a filename, update the matching `<img src="…">` in `../index.md`.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `detroy-time-unveiling-truth-1733.jpg` | Jean-François de Troy, *Time Unveiling Truth*, 1733 — winged Time draws the veil from Truth while Falsehood recoils with her masks; the allegory half of the cold open, against the orrery's practice | National Gallery, London, NG6454 | Public domain |
| `wright-orrery-1766.jpg` | Joseph Wright of Derby, *A Philosopher Giving That Lecture on the Orrery, in which a Lamp is put in place of the Sun*, c. 1766 — the cold-open splash, used twice: full-bleed, then reduced beside notes on the `.image-notes` slide | Derby Museum and Art Gallery, via Europeana | Public domain |
| `machiavelli-santi-di-tito.jpg` | Niccolò Machiavelli — last week's primary source, reused here on the Renaissance bridge slide | Santi di Tito, Palazzo Vecchio, Florence | Public domain |
| `vasari-vite-titlepage-1568.jpg` | Title page of Vasari's *Le vite de' piu eccellenti pittori, scultori, et architettori*, Giunti, Florence 1568; the foot carries the papal printing license "Con licenza e privilegio di N.S. Pio V" | Giunti edition, 1568 | Public domain |
| `encyclopedie-titlepage-1751.jpg` | Title page of the *Encyclopédie*, volume one, Paris 1751 — "par une société de gens de lettres," four named booksellers, and "avec approbation et privilège du roy" | University of Ottawa copy, via ARTFL (U. Chicago) | Public domain |
| `perrault-lallemand-portrait.jpg` | Charles Perrault, c. 1671–72 — the writer whose 1687 poem "Le Siècle de Louis le Grand" set off the quarrel of the ancients and the moderns, and who published the *Contes* ("Cinderella," "Puss in Boots") ten years later | Philippe Lallemand, after Charles Le Brun; Château de Versailles | Public domain |
| `boileau-rigaud-portrait.jpg` | Nicolas Boileau-Despréaux (1636–1711), 1704 — the leading defender of the ancients in the quarrel, and Louis XIV's royal historiographer from 1677 | Workshop of Hyacinthe Rigaud, 1704 | Public domain |

## Notes

- The CSS caps images at the slide height, so portrait and landscape both
  work. Each `<figure>` carries a `portrait` or `landscape` class — portrait
  puts the caption to the right of the image, landscape puts it underneath.
  Keep them matched to the actual aspect ratio or the layout goes strange.
- The three portraits added in the 2026-09-06 revision are uncropped; refetch
  and reprocess any of them with:

      curl -L -H 'your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=1600' -o raw.jpg
      sips -Z 1800 raw.jpg --out <out>.jpg -s format jpeg -s formatOptions 80

  `boileau-rigaud-portrait.jpg` was capped at 1400 px instead of 1800: the
  only Commons copy is a 975×1090 reproduction, so there is nothing larger to
  source. It displays at roughly 380 px wide in the `pair` figure, which is
  well within that.

  The Commons filenames are `Charles Perrault par Lallemand d'après Le Brun –
  Château de Versailles.jpg`, `Anonymous - Portrait de Marie Jean Antoine
  Nicolas de Caritat, marquis de Condorcet (1743-1794), philosophe,
  mathématicien et homme politique. - P1668 - Musée Carnavalet.jpg`, and
  `Johann Gottfried Herder 2.jpg`, and `Nicolas Boileau.jpg`.
- `machiavelli-santi-di-tito.jpg` is **duplicated** from the Week 3 deck rather
  than linked across directories, so each deck stays self-contained and a
  rename in one cannot break the other. If you re-process it there, re-copy it
  here. It appears on the bridge slide precisely because students saw it a
  week earlier.
- `encyclopedie-titlepage-1751.jpg` carries a modern red University of Ottawa
  library stamp in the lower right and a pencilled shelfmark at the top; the
  caption says so, so the marks are not mistaken for period features.
- `encyclopedie-titlepage-1751.jpg` is one of two sheets from the *Encyclopédie*
  used across this session. The other, `encyclopedie-frontispiece.jpg`, is in
  the **part two** deck. They are different sheets doing different jobs — the
  title page here as evidence of the print economy, the frontispiece there as
  the emblem of the project. Don't collapse them, and don't copy one deck's
  sheet into the other.
- `perrault-lallemand-portrait.jpg` and `boileau-rigaud-portrait.jpg` share a
  slide as a `pair` figure (two sides of one quarrel), so that `<figure>`
  carries **only** `class="pair"` — adding `portrait` would let the
  `.portrait figcaption` rule (35% side rail) override the `.pair figcaption`
  rule (centered, 92%) and break the layout.
- `perrault-lallemand-portrait.jpg` is Lallemand's version after a lost or
  private Le Brun original. Commons also holds the Le Brun (Artcurial) at
  higher resolution; the Versailles Lallemand was chosen for its institutional
  provenance.

- `detroy-time-unveiling-truth-1733.jpg` and `wright-orrery-1766.jpg` (added
  2026-09-07) are the cold open — the allegory and the practice — and the only
  images shown twice: one per full-bleed slide, then both reduced inside
  `.image-notes` with the points about them. All four references point at
  these two files; don't add smaller duplicates. The de Troy is held to
  1700 px / q82 because the folder is near its size ceiling; it is never
  displayed near full size. Refetch with:

      curl -L -H 'your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/Wright%20of%20Derby,%20The%20Orrery.jpg?width=2200' -o raw.jpg
      sips -Z 1800 raw.jpg --out wright-orrery-1766.jpg -s format jpeg -s formatOptions 82

      curl -L -H 'your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/Jean-Fran%C3%A7ois%20de%20Troy%20-%20Time%20Unveiling%20Truth,%201733.jpg?width=2000' -o raw.jpg
      sips -Z 1700 raw.jpg --out detroy-time-unveiling-truth-1733.jpg -s format jpeg -s formatOptions 82

  The Saint-Aubin *Vue du Salon du Louvre en l'année 1753* (NGA 39500, CC0)
  was used here briefly and dropped: as a low-saturation brown wash drawing
  of small-scale detail it did not read at projector distance. Refetch it
  from Commons if a slide ever wants the Salon itself.

- **This deck is one half of a session.** Week 4.1 is split across
  `enlightenment-progress` and `enlightenment-progress-2`; the image sets are disjoint, so an image referenced here
  is not used by the other deck. If you move a slide between the two decks,
  move its image and its row in this table with it.

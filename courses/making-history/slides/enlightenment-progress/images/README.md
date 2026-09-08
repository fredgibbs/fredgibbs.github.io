# Slide Images — Enlightenment Progress

Fifteen images used by `../index.md`: all public domain or CC0. Nothing here
requires attribution by license, but credits are kept anyway.

If you change a filename, update the matching `<img src="…">` in `../index.md`.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `detroy-time-unveiling-truth-1733.jpg` | Jean-François de Troy, *Time Unveiling Truth*, 1733 — winged Time draws the veil from Truth while Falsehood recoils with her masks; the allegory half of the cold open, against the orrery's practice | National Gallery, London, NG6454 | Public domain |
| `wright-orrery-1766.jpg` | Joseph Wright of Derby, *A Philosopher Giving That Lecture on the Orrery, in which a Lamp is put in place of the Sun*, c. 1766 — the cold-open splash, used twice: full-bleed, then reduced beside notes on the `.image-notes` slide | Derby Museum and Art Gallery, via Europeana | Public domain |
| `machiavelli-santi-di-tito.jpg` | Niccolò Machiavelli — last week's primary source, reused here on the Renaissance bridge slide | Santi di Tito, Palazzo Vecchio, Florence | Public domain |
| `vasari-vite-titlepage-1568.jpg` | Title page of Vasari's *Le vite de' piu eccellenti pittori, scultori, et architettori*, Giunti, Florence 1568; the foot carries the papal printing licence "Con licenza e privilegio di N.S. Pio V" | Giunti edition, 1568 | Public domain |
| `encyclopedie-titlepage-1751.jpg` | Title page of the *Encyclopédie*, volume one, Paris 1751 — "par une société de gens de lettres," four named booksellers, and "avec approbation et privilège du roy" | University of Ottawa copy, via ARTFL (U. Chicago) | Public domain |
| `perrault-lallemand-portrait.jpg` | Charles Perrault, c. 1671–72 — the writer whose 1687 poem "Le Siècle de Louis le Grand" set off the quarrel of the ancients and the moderns, and who published the *Contes* ("Cinderella," "Puss in Boots") ten years later | Philippe Lallemand, after Charles Le Brun; Château de Versailles | Public domain |
| `boileau-rigaud-portrait.jpg` | Nicolas Boileau-Despréaux (1636–1711), 1704 — the leading defender of the ancients in the quarrel, and Louis XIV's royal historiographer from 1677 | Workshop of Hyacinthe Rigaud, 1704 | Public domain |
| `voltaire-largilliere-portrait.jpg` | François-Marie Arouet, known as Voltaire, c. 1724–1725 (age ~30; he wrote the *Age of Louis XIV* at 57) | Nicolas de Largillière, Château de Versailles, MV 8159 | Public domain |
| `louis-xiv-rigaud-portrait.jpg` | Louis XIV in coronation robes, 1701 | Hyacinthe Rigaud, Musée du Louvre | Public domain |
| `salon-geoffrin-lemonnier.jpg` | A reading of Voltaire's own play *L'Orphelin de la Chine* in Madame Geoffrin's salon, 1755 — Voltaire is not present (he was in exile near Geneva by then), but Fontenelle, Montesquieu, Diderot, and d'Alembert are among the seated guests | Anicet-Charles-Gabriel Lemonnier, painted 1812, Château de Malmaison | Public domain |
| `kant-portrait-c1790.jpg` | Immanuel Kant, c. 1790 — six years after this essay | Unknown, possibly Elisabeth von Stägemann (school of Anton Graff) | Public domain |
| `konigsberg-plan-1763.jpg` | "Plan der Stadt Koenigsberg" — a detailed plan of the city (castle, Kneiphof, cathedral, the seven bridges) inset on a regional atlas plate, engraved 21 years before this essay | Leibniz-Institut für Länderkunde, Leipzig | CC0 |
| `encyclopedie-frontispiece.jpg` | Frontispiece to Diderot and d'Alembert's *Encyclopédie* — Truth, radiant at center, is unveiled by Reason and Philosophy while Theology looks down from above and the sciences and arts gather below | Charles-Nicolas Cochin (design, 1764) / Benoît-Louis Prévost (engraving, 1772) | Public domain |
| `condorcet-carnavalet-portrait.jpg` | Marie Jean Antoine Nicolas de Caritat, marquis de Condorcet (1743–1794), profile portrait, painter unrecorded | Anonymous, Musée Carnavalet P1668, Paris Musées | Public domain |
| `herder-graff-portrait.jpg` | Johann Gottfried von Herder, 1785 — the year after Kant's essay, and the year the first part of Herder's own *Ideen* appeared | Anton Graff, 1785 (via museum-digital) | Public domain |

Retrieved 2026-09-03 (first six) and 2026-09-06 (Perrault, Condorcet, Herder)
and 2026-09-07 (Boileau, Vasari, Encyclopédie title page), all via
Wikimedia Commons. `machiavelli-santi-di-tito.jpg` is a copy of the file in
`../../divine-power-and-statecraft/images/`.

## Notes

- Sourced at width 1400–2000, then capped at 1800 px on the long edge
  (`salon-geoffrin-lemonnier.jpg` was not upscaled — Commons has no larger
  copy of the Lemonnier painting than ~1200 px wide) and recompressed to
  JPEG. The two engravings (`encyclopedie-frontispiece.jpg`,
  `konigsberg-plan-1763.jpg`) are saved at q85–88 since fine linework and map
  labels smear at the q78–80 used for the paintings/portraits. The folder
  totals ~9.4 MB — close to the ~10 MB ceiling. Anything further has
  to displace something already here, or the whole folder needs a pass at
  lower quality.
- The CSS caps images at the slide height, so portrait and landscape both
  work. Each `<figure>` carries a `portrait` or `landscape` class — portrait
  puts the caption to the right of the image, landscape puts it underneath.
  Keep them matched to the actual aspect ratio or the layout goes strange.
- `konigsberg-plan-1763.jpg` is a **crop** of a larger atlas plate (the full
  sheet also carries the title banner "Regnum Borussiae, Episcopatus
  Warmiensis, Palatinatus Mariaeburgensis" and wide paper margins); the crop
  keeps the city plan and its legend box, which names the castle (A, *Das
  Schloss*), the cathedral (c, *Der Dom*), and Kneiphof (D) — where Kant
  taught. Regenerate from the full sheet with:

      curl -L -H 'your-name (your-email)' \
        'https://upload.wikimedia.org/wikipedia/commons/1/18/Plan_Der_Stadt_Koenigsberg.jpg' -o raw.jpg
      magick raw.jpg -crop 8150x6000+280+460 +repage -resize 1800x -quality 88 konigsberg-plan-1763.jpg

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
- `voltaire-largilliere-portrait.jpg` is ~25 years earlier than the book it
  illustrates (painted c. 1724–25; Voltaire wrote the *Age of Louis XIV* in
  1751, at 57) — there is no widely reproduced public-domain portrait from
  exactly the right year, and this is the most-used Voltaire likeness. The
  caption on that slide says so.
- `salon-geoffrin-lemonnier.jpg` is a double anachronism, and the caption
  says so: it depicts a real 1755 event (a reading of Voltaire's play,
  Voltaire himself absent) but was painted in 1812, fifty-seven years later
  and after everyone in it, including the empress who commissioned it, had
  died. Use it for what it shows about Enlightenment sociability, not as an
  eyewitness image.
- `encyclopedie-frontispiece.jpg` postdates Voltaire's book by over a decade
  (designed 1764, engraved 1772; the *Age of Louis XIV* is 1751) — it is used
  as the visual emblem of the broader "progress of the human mind" project
  both Voltaire and Kant belong to, not as an illustration specific to either
  text. Say so if using it elsewhere.
- `machiavelli-santi-di-tito.jpg` is **duplicated** from the Week 3 deck rather
  than linked across directories, so each deck stays self-contained and a
  rename in one cannot break the other. If you re-process it there, re-copy it
  here. It appears on the bridge slide precisely because students saw it a
  week earlier.
- `encyclopedie-titlepage-1751.jpg` carries a modern red University of Ottawa
  library stamp in the lower right and a pencilled shelfmark at the top; the
  caption says so, so the marks are not mistaken for period features.
- `encyclopedie-titlepage-1751.jpg` and `encyclopedie-frontispiece.jpg` are two
  different sheets from the same work and appear on two different slides (the
  title page early, as evidence of the print economy; the frontispiece later,
  as the emblem of the project). Don't collapse them.
- `condorcet-carnavalet-portrait.jpg` is dated by Carnavalet only to
  Condorcet's lifetime (1743–1794) and the painter is unrecorded; the
  caption on the slide does not claim a date or an artist for it.
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

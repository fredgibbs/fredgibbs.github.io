# Slide Images — Enlightenment Progress, part two

8 images used by `../index.md`: all public domain or CC0. Nothing here
requires attribution by license, but credits are kept anyway.

If you change a filename, update the matching `<img src="…">` in `../index.md`.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `voltaire-largilliere-portrait.jpg` | François-Marie Arouet, known as Voltaire, c. 1724–1725 (age ~30; he wrote the *Age of Louis XIV* at 57) | Nicolas de Largillière, Château de Versailles, MV 8159 | Public domain |
| `louis-xiv-rigaud-portrait.jpg` | Louis XIV in coronation robes, 1701 | Hyacinthe Rigaud, Musée du Louvre | Public domain |
| `salon-geoffrin-lemonnier.jpg` | A reading of Voltaire's own play *L'Orphelin de la Chine* in Madame Geoffrin's salon, 1755 — Voltaire is not present (he was in exile near Geneva by then), but Fontenelle, Montesquieu, Diderot, and d'Alembert are among the seated guests | Anicet-Charles-Gabriel Lemonnier, painted 1812, Château de Malmaison | Public domain |
| `kant-portrait-c1790.jpg` | Immanuel Kant, c. 1790 — six years after this essay | Unknown, possibly Elisabeth von Stägemann (school of Anton Graff) | Public domain |
| `konigsberg-plan-1763.jpg` | "Plan der Stadt Koenigsberg" — a detailed plan of the city (castle, Kneiphof, cathedral, the seven bridges) inset on a regional atlas plate, engraved 21 years before this essay | Leibniz-Institut für Länderkunde, Leipzig | CC0 |
| `encyclopedie-frontispiece.jpg` | Frontispiece to Diderot and d'Alembert's *Encyclopédie* — Truth, radiant at center, is unveiled by Reason and Philosophy while Theology looks down from above and the sciences and arts gather below | Charles-Nicolas Cochin (design, 1764) / Benoît-Louis Prévost (engraving, 1772) | Public domain |
| `condorcet-carnavalet-portrait.jpg` | Marie Jean Antoine Nicolas de Caritat, marquis de Condorcet (1743–1794), profile portrait, painter unrecorded | Anonymous, Musée Carnavalet P1668, Paris Musées | Public domain |
| `herder-graff-portrait.jpg` | Johann Gottfried von Herder, 1785 — the year after Kant's essay, and the year the first part of Herder's own *Ideen* appeared | Anton Graff, 1785 (via museum-digital) | Public domain |

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
- `encyclopedie-frontispiece.jpg` is one of two sheets from the *Encyclopédie*
  used across this session. The other, `encyclopedie-titlepage-1751.jpg`, is in
  the **part one** deck. They are different sheets doing different jobs — the
  title page there as evidence of the print economy, the frontispiece here as
  the emblem of the project. Don't collapse them, and don't copy one deck's
  sheet into the other.
- `condorcet-carnavalet-portrait.jpg` is dated by Carnavalet only to
  Condorcet's lifetime (1743–1794) and the painter is unrecorded; the
  caption on the slide does not claim a date or an artist for it.

- **This deck is one half of a session.** Week 4.1 is split across
  `enlightenment-progress` and `enlightenment-progress-2`; the image sets are disjoint, so an image referenced here
  is not used by the other deck. If you move a slide between the two decks,
  move its image and its row in this table with it.

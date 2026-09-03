# Slide Images — Divine Power and Statecraft

Seventeen images used by `../index.md`: public domain, CC0, CC BY-SA 4.0, and two
**CC BY-NC 4.0**. The CC BY-SA and CC BY-NC items require attribution, which is
carried in the `<figcaption>` on their slides — don't strip it.

**On the NC pair:** the two `paschal-table-*` files are CC BY-NC 4.0 (e-codices).
NonCommercial turns on the use, not the user — a course site hosting lecture
slides is squarely non-commercial, and stays so even though the site is public.
Don't roll these into anything sold (a paid course pack, a book) without
clearing it. Everything else here is free of that restriction.

If you change a filename, update the matching `<img src="…">` in `../index.html`.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `paschal-table-annals.jpg` | Paschal table for AD 950–968, one ruled line per year, with 10th-c. annal entries added in the right margin | St. Gallen, Stiftsbibliothek, Cod. Sang. 459, p. 21 (e-codices) | **CC BY-NC 4.0** |
| `paschal-table-annals-detail.jpg` | Derived from the above: crop of rows 956–963, gold box added around the marginal entries | derivative | **CC BY-NC 4.0** |
| `codex-amiatinus-ezra.jpg` | Ezra the scribe, with an open book cupboard behind him; made at Wearmouth–Jarrow c. 700–716 | Biblioteca Medicea Laurenziana, MS Amiatino 1, fol. 5r | Public domain |
| `acton-portrait.jpg` | John Dalberg-Acton, 1st Baron Acton, Regius Professor of Modern History at Cambridge | Allen & Co., before 1902 | Public domain |
| `lindisfarne-stone-raiders.jpg` | Grave marker, face 1: seven armed figures; Lindisfarne, 1st quarter 9th c. | Lindisfarne Priory (English Heritage), inv. 81077057; photo Schillerwein | CC0 |
| `lindisfarne-stone-judgement.jpg` | The same stone, face 2: cross between sun and moon, praying hands | Lindisfarne Priory (English Heritage), inv. 81077057; photo Schillerwein | CC0 |
| `asc-msa-parker.jpg` | Anglo-Saxon Chronicle MS A, first page (the Parker Chronicle), genealogical preface | Cambridge, Corpus Christi College MS 173 | Public domain |
| `asc-mse-peterborough.jpg` | Anglo-Saxon Chronicle MS E, first page (the Peterborough Chronicle) | Bodleian Library, MS Laud Misc. 636 | Public domain |
| `asc-msd-tiberius-b-iv.jpg` | *Anglo-Saxon Chronicle* MS D, fol. 20r — annals 711–718, three of them empty | British Library, Cotton MS Tiberius B.iv | Public domain |
| `bede-hatton-43-f129r.jpg` | Bede, *Historia ecclesiastica* IV.24 (Cædmon), with Cædmon's Hymn added in Old English in the lower margin | Bodleian Libraries, Oxford, MS Hatton 43, fol. 129r | **CC BY-SA 4.0** |
| `al-biruni-athar-f230.jpg` | al-Biruni, *al-Āthār al-bāqiya*, fol. 230 — the prophet Bihāfrīd | Bibliothèque nationale de France (via Gallica); later illustrated copy | Public domain |
| `mahmud-ghazna-india.jpg` | Mahmud of Ghazna storming a fortress, from Rashīd al-Dīn's *Jāmiʿ al-tawārīkh*, Tabriz c. 1314 | BL Or. 20, f. 108v | Public domain |
| `donation-of-constantine.jpg` | The Donation of Constantine, Italian fresco, 13th c. | Unknown Italian master, via the Web Gallery of Art | Public domain |
| `valla-latin-1471.jpg` | Opening page of Valla's *In errores Antonii Raudensis*, printed with the *Elegantiae*, Paris 1471 | Prädikantenbibliothek Isny, Phil. 22 | Public domain |
| `lorenzo-valla.jpg` | Engraved portrait of Lorenzo Valla | Rijksmuseum, RP-P-1909-4359 | CC0 |
| `machiavelli-santi-di-tito.jpg` | Niccolò Machiavelli, by Santi di Tito | Palazzo Vecchio, Florence | Public domain |

Retrieved 2026-09-02/03 — all via Wikimedia Commons except the two
`paschal-table-*` files, taken from the e-codices IIIF endpoint.

## Notes

- Sourced at width 2000, then capped at 1800 px on the long edge and
  recompressed to JPEG. Manuscript pages are saved at q88 and the Lindisfarne
  stone at q82 — they carry fine script or low-relief carving that q78 smears.
  Everything else is q78. The folder totals ~8.7 MB.
- The CSS caps images at the slide height, so portrait and landscape both work.
  Each `<figure>` carries a `portrait` or `landscape` class — portrait puts the
  caption to the right of the image, landscape puts it underneath. Keep them
  matched to the actual aspect ratio or the layout goes strange.
- Inside a `<figcaption>`, `<em>` is the block-level note/credit line and `<i>`
  is inline italics (titles, quoted phrases). Don't nest an `<em>` inside the
  note — use `<i>`.
- **Two captions deliberately undercut their own image**, which is the point of
  the week:
  - The two `lindisfarne-stone-*.jpg` files are the **two faces of one object**,
    shown side by side on a `figure.pair` slide: raiders on one, a Last Judgement
    on the other. That ambiguity is the point of the slide — keep them together.
  - The manuscript-variety pair is **A + E** on purpose: `asc-msd-tiberius-b-iv.jpg`
    carries the empty-annal-years slide on its own immediately afterwards, and
    reusing it in the pair would blunt that. A and E also happen to open the same
    work in two different ways, which is the point the caption makes.
    moon, praying figures around a cross), so whether the armed men are raiders
    or the end of the world is genuinely unsettled. The caption says so. Don't
    "fix" it into a picture of the 793 raid.
  - `mahmud-ghazna-india.jpg` was painted about three centuries after Mahmud,
    in Mongol Tabriz. It is an imagining, not a witness, and the caption says so
    — the same move the Greeks deck makes with the Herodotus and Thucydides
    busts.
- The two `paschal-table-*` files are the evidence for the Easter-table claim in
  the annals section, and the deck states plainly that **the gold box is ours,
  not the scribe's** — same disclosure the Greeks deck makes for its Shiji crops.
  The boxed marginalia read *Liutolfus Ottonis regis filius in Italia migravit*
  (Liudolf, son of Otto the Great, died in Italy), then *Ruodolfus et Engil[bertus]
  ob[ierunt]* and a third entry. The Liudolf note sits against the row for
  **DCCCCLVIII**, but he died 6 September **957** — the deck points that out
  rather than hiding it, because the annalist being a year out inside a ruled
  table is the same lesson as the 1239 Tartar error earlier in the deck.
  Regenerate the detail with:

      magick p21.jpg -crop 1920x660+60+1140 +repage \
        -stroke '#d9b26a' -strokewidth 6 -fill none \
        -draw "rectangle 1355,110 1875,565" \
        -resize 1800x -quality 88 paschal-table-annals-detail.jpg

  where `p21.jpg` is Cod. Sang. 459 p. 21 at width 2000 from the e-codices IIIF
  endpoint:
  `https://www.e-codices.unifr.ch/loris/csg/csg-0459/csg-0459_021.jp2/full/,3000/0/default.jpg`
  A public-domain alternative would be better, but there isn't one: Commons has
  no paschal tables at all (no `Computus` or `Easter tables` categories exist),
  and the textbook English example — BL Cotton MS Caligula A XV, the Christ Church
  Easter-table annals — is behind the British Library's Digitised Manuscripts
  service, which still redirects after the 2023 cyberattack.

- `donation-of-constantine.jpg` is catalogued by the Web Gallery of Art only as
  "Unknown Master, Italian, 13th century." It closely matches the San Silvestro
  cycle at Santi Quattro Coronati in Rome (1246), but the caption stops at what
  the source actually asserts. If you confirm the attribution, the caption can
  name the building.
- Re-fetch any of these with:

      curl -L -H 'User-Agent: your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=2000' -o raw
      sips -Z 1800 raw --out out.jpg -s format jpeg -s formatOptions 88

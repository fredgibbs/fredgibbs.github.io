# Slide Images — Evidence, Purpose, and Form

Eleven images used by `../index.html`. All are public domain, CC0, CC BY 4.0, or
CC BY-SA 3.0. The CC BY 4.0 and CC BY-SA 3.0 items require attribution, which is
carried in the `<figcaption>` on their slides — don't strip it.

If you change a filename, update the matching `<img src="…">` in `../index.html`.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `herodotus-bust-met.jpg` | Roman portrait bust of Herodotus, 2nd c. CE | Metropolitan Museum of Art, 91.8 | CC0 |
| `thucydides-bust-rom.jpg` | Portrait bust of Thucydides, Roman copy of a Greek original | Royal Ontario Museum | Public domain |
| `greco-persian-wars-map.jpg` | The Greek world during the Persian Wars, 500–479 BCE | Bibi Saint-Pol, *Map Greco-Persian Wars-en.svg* | **CC BY-SA 3.0** |
| `athenian-empire-431-map.jpg` | The Athenian Empire on the eve of the Peloponnesian War, 431 BCE | Marsyas, derivative by Once in a Blue Moon, *Map athenian empire 431 BC-en.svg* | **CC BY-SA 3.0** |
| `croesus-pyre-myson-louvre-g197.jpg` | Croesus on the pyre, Attic red-figure amphora by Myson, c. 500–490 BCE, from Vulci | Louvre G 197 (photo: Bibi Saint-Pol) | Public domain |
| `livy-poggio-manuscript-vat-lat-3331.jpg` | Livy, *Ab urbe condita*, end of Bk 38 / start of Bk 39, copied by Poggio Bracciolini, 1453 | Biblioteca Apostolica Vaticana, Vat. lat. 3331, fol. 156v | Public domain |
| `lucretia-botticelli-gardner.jpg` | Sandro Botticelli, *The Story of Lucretia*, c. 1500–01 | Isabella Stewart Gardner Museum, Boston | Public domain |
| `sima-qian-portrait-npm.jpg` | Sima Qian, from 歷代聖賢半身像冊 (*Half-Length Portraits of Sages Through the Ages*) | National Palace Museum, Taipei | **CC BY 4.0** |
| `shiji-tang-manuscript.jpg` | *Shiji*, "Book of Rivers and Canals" §7 (vol. 29), Tang dynasty manuscript copy | Tokyo National Museum, TB-1573 | **CC BY 4.0** |
| `shiji-taishigong-highlight.jpg` | Derived from the above: gold box added around 太史公曰 | derivative | **CC BY 4.0** |
| `shiji-taishigong-detail.jpg` | Derived from the above: 3× crop of the 太史公曰 column, gold box added | derivative | **CC BY 4.0** |
| `xiang-yu-portrait-pma.jpg` | Xiang Wang (Xiang Yu), from *Portraits of Famous Men*, 19th–early 20th c. | Philadelphia Museum of Art, 42784 | Public domain |

All retrieved via Wikimedia Commons; the objects and paintings 2026-08-31, the two maps 2026-09-01.

## Notes

- Sourced at width 1400–2200, then capped at 1800 px on the long edge and
  recompressed to JPEG q78. Everything is under 1 MB; the folder totals ~6.5 MB.
- The CSS caps images at the slide height, so portrait and landscape both work.
  Each `<figure>` carries a `portrait` or `landscape` class — portrait puts the
  caption to the right of the image, landscape puts it underneath. Keep them
  matched to the actual aspect ratio or the layout goes strange.
- Three of the four historian portraits are later inventions with no claim to
  likeness, and the captions say so. That is deliberate — it is the same point
  the week makes about the texts.

- The two **maps** are rendered from SVG at 1800 px and saved at JPEG q88 rather
  than the q78 used for everything else — they carry small type, and q78 smears
  the place names. They are the only **CC BY-SA 3.0** files here: attribute them,
  and if you ever edit one, the edit inherits ShareAlike. Re-render with:

      curl -L -H 'User-Agent: your-name (your-email)' \
        'https://commons.wikimedia.org/wiki/Special:FilePath/Map_Greco-Persian_Wars-en.svg?width=1800' -o m.png
      sips -Z 1800 m.png --out out.jpg -s format jpeg -s formatOptions 88

- The two `shiji-taishigong-*` files are **annotated derivatives** of
  `shiji-tang-manuscript.jpg`, made with ImageMagick — the gold rectangle
  (`#d9b26a`, the theme accent) is ours, not the manuscript's. Both captions
  say so explicitly. Regenerate with:

      magick shiji-tang-manuscript.jpg -stroke '#d9b26a' -strokewidth 4 -fill none \
        -draw "rectangle 766,92 830,248" -quality 82 shiji-taishigong-highlight.jpg

      magick shiji-tang-manuscript.jpg -crop 235x470+688+85 +repage -resize 300% \
        -stroke '#d9b26a' -strokewidth 5 -fill none \
        -draw "rectangle 234,21 426,489" -quality 82 shiji-taishigong-detail.jpg

  Keep `shiji-tang-manuscript.jpg` — it is the unmodified source both derive from.

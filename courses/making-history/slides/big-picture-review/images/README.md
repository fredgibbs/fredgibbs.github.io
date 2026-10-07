# Slide Images — The Big Picture (review of Weeks 1–7)

Twenty-three images used by `../index.md`, **all copied from the decks this one
reviews**: one per subpoint slide, beside the claim it supports. They are
**resized copies**, not byte-for-byte: each was scaled to 1400px on its long
edge and recompressed (quality 78; 84 for manuscripts, maps and printed pages,
where fine detail matters), because the layout shows them at most 470×380 CSS
pixels and full-size copies would have run past the ~10MB guide. The folder is
about 6MB.
Regenerate one from its source with:

```sh
magick ../../<source-deck>/images/<file>.jpg -resize '1400x1400>' -strip -quality 78 <file>.jpg
```

Four of the sources are themselves crops made in their home decks; those notes
and commands live in the home deck's `images/README.md`, and the credit line on
the slide says "cropped".

| File | Slide | Copied from | License |
|---|---|---|---|
| `peterloo-1819.jpg` | 1.1 Carr — Richard Carlile, *To Henry Hunt, Esq.*, 1819 (**cropped**) | `history-from-below` (photo "APK", National Portrait Gallery impression) | **CC BY 4.0** |
| `asc-msd-tiberius-b-iv.jpg` | 1.2 — *Anglo-Saxon Chronicle* MS D, fol. 20r | `divine-power-and-statecraft` (British Library) | Public domain |
| `treitschke-hoersaal-1879.jpg` | 1.3 — Treitschke lecturing, 1879 | `scientific-history` | Public domain |
| `leader-of-the-luddites-1812.jpg` | 1.4 — *The Leader of the Luddites*, 1812 (uncropped) | `history-from-below` (Working Class Movement Library) | Public domain |
| `herodotus-bust-met.jpg` | 2.1 — Roman bust of Herodotus | `greeks-evidence-and-purpose` (Met 91.8) | CC0 |
| `lucretia-botticelli-gardner.jpg` | 2.2 — Botticelli, *The Story of Lucretia* | `greeks-evidence-and-purpose` (Gardner Museum) | Public domain |
| `machiavelli-santi-di-tito.jpg` | 2.3 — Machiavelli, by Santi di Tito | `divine-power-and-statecraft` | Public domain |
| `ranke-library-1880s.jpg` | 2.4 — Ranke in his library | `scientific-history` (Syracuse) | Public domain |
| `croesus-pyre-myson-louvre-g197.jpg` | 3.1 — Croesus on the pyre, Myson amphora | `greeks-evidence-and-purpose` (Louvre G 197) | Public domain |
| `athenian-empire-431-map.jpg` | 3.2 — the Athenian Empire, 431 BCE | `greeks-evidence-and-purpose` (Marsyas / Once in a Blue Moon) | **CC BY-SA 3.0** |
| `xiang-yu-portrait-pma.jpg` | 3.3 — Xiang Yu, *Portraits of Famous Men* | `greeks-evidence-and-purpose` (Philadelphia Museum of Art) | Public domain |
| `mediterranean-chart-1569.jpg` | 3.4 — Forlani chart, 1569 (**cropped**) | `annales-longue-duree` (NMM Greenwich) | Public domain |
| `bede-hatton-43-f129r.jpg` | 4.1 — Bede IV.24, MS Hatton 43 | `divine-power-and-statecraft` (Bodleian) | **CC BY-SA 4.0** |
| `al-biruni-athar-f230.jpg` | 4.2 — al-Biruni, *al-Āthār al-bāqiya*, fol. 230 | `divine-power-and-statecraft` (BnF) | Public domain |
| `ranke-vorrede-1824.jpg` | 4.3 — Ranke's 1824 preface, p. VI (**cropped**) | `scientific-history` (Internet Archive) | Public domain |
| `manchester-kersal-moor-1852.jpg` | 5.1 — Wyld, *Manchester from Kersal Moor* | `marx-structural-history` (Royal Collection) | Public domain |
| `lepanto-1571.jpg` | 5.2 — the Battle of Lepanto | `annales-longue-duree` (NMM Greenwich) | Public domain |
| `joanna-southcott-1814.jpg` | 5.3 — Joanna Southcott, 1814 (**cropped**) | `history-from-below` (KU Leuven) | Public domain |
| `berlin-congress-1892.jpg` | 5.4 — von Werner, *Der Kongreß zu Berlin* | `gender` (Deutsches Historisches Museum) | Public domain |
| `salon-geoffrin-lemonnier.jpg` | 6.1 — Lemonnier, Madame Geoffrin's salon | `enlightenment-progress-2` (Malmaison) | Public domain |
| `herder-graff-portrait.jpg` | 6.2 — Herder, by Graff, 1785 | `enlightenment-progress-2` | Public domain |
| `ranke-jebens-portrait-1875.jpg` | 6.3 — Ranke, by Jebens, 1875 | `scientific-history` | Public domain |
| `acton-portrait.jpg` | 6.4 — Lord Acton | `divine-power-and-statecraft` | Public domain |

## Notes

- **The CC BY and CC BY-SA images carry their attribution on the slide**, in
  the `p.cite` line under the picture.
- **Some pairings are arguments, not illustrations.** Treitschke's lecture hall
  stands for state-funded history (1.3), Ranke's library for a way of reading a
  record (2.4), the Forlani chart for a structure (3.4). Each caption says what
  the picture actually is; the slide text says why it is there.
- **Trimmed 2026-10-06** from six examples a part to four. Twelve copies were
  deleted with their slides (Codex Amiatinus, Thucydides bust, *Shiji* detail,
  Poggio's Livy, the paschal table, the Donation fresco, *The Olive Trees*, the
  Lindisfarne stone, Königsberg, Henry VIII, Condorcet, the *Encyclopédie*
  frontispiece). The originals are still in their home decks; regenerate with
  the command above if a slide comes back.
- **Nothing here is new to the course,** and every caption is drawn from the
  home deck's caption and credit row. If a home deck corrects one, correct it
  here too.

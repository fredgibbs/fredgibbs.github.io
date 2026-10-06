# Slide Images — The Big Picture (review of Weeks 1–7)

Thirty-five images used by `../index.md`, **all copied from the decks this one
reviews**: one per subpoint slide, beside the claim it supports. They are
**resized copies**, not byte-for-byte: each was scaled to 1400px on its long
edge and recompressed (quality 78; 84 for manuscripts, maps and printed pages,
where fine detail matters), because the layout shows them at most 470×380 CSS
pixels and thirty-five full-size copies would have run past the ~10MB guide.
Regenerate one from its source with:

```sh
magick ../../<source-deck>/images/<file>.jpg -resize '1400x1400>' -strip -quality 78 <file>.jpg
```

Five of the sources are themselves crops or derivatives made in their home
decks; those notes and commands live in the home deck's `images/README.md`, and
the credit line on the slide says "cropped" or "gold box added".

| File | Slide | Copied from | License |
|---|---|---|---|
| `peterloo-1819.jpg` | 1.1 Carr — Richard Carlile, *To Henry Hunt, Esq.*, 1819 (**cropped**) | `history-from-below` (photo "APK", National Portrait Gallery impression) | **CC BY 4.0** |
| `asc-msd-tiberius-b-iv.jpg` | 1.2 — *Anglo-Saxon Chronicle* MS D, fol. 20r | `divine-power-and-statecraft` (British Library) | Public domain |
| `codex-amiatinus-ezra.jpg` | 1.3 — Ezra, Codex Amiatinus, Wearmouth–Jarrow | `divine-power-and-statecraft` (Laurenziana) | Public domain |
| `treitschke-hoersaal-1879.jpg` | 1.4 — Treitschke lecturing, 1879 | `scientific-history` | Public domain |
| `leader-of-the-luddites-1812.jpg` | 1.5 — *The Leader of the Luddites*, 1812 (uncropped) | `history-from-below` (Working Class Movement Library) | Public domain |
| `herodotus-bust-met.jpg` | 2.1 — Roman bust of Herodotus | `greeks-evidence-and-purpose` (Met 91.8) | CC0 |
| `thucydides-bust-rom.jpg` | 2.2 — bust of Thucydides | `greeks-evidence-and-purpose` (ROM) | Public domain |
| `lucretia-botticelli-gardner.jpg` | 2.3 — Botticelli, *The Story of Lucretia* | `greeks-evidence-and-purpose` (Gardner Museum) | Public domain |
| `shiji-taishigong-highlight.jpg` | 2.4 — *Shiji*, Tang copy, detail (**gold box added**) | `greeks-evidence-and-purpose` (Tokyo National Museum) | **CC BY 4.0** |
| `machiavelli-santi-di-tito.jpg` | 2.5 — Machiavelli, by Santi di Tito | `divine-power-and-statecraft` | Public domain |
| `ranke-library-1880s.jpg` | 2.6 — Ranke in his library | `scientific-history` (Syracuse) | Public domain |
| `croesus-pyre-myson-louvre-g197.jpg` | 3.1 — Croesus on the pyre, Myson amphora | `greeks-evidence-and-purpose` (Louvre G 197) | Public domain |
| `athenian-empire-431-map.jpg` | 3.2 — the Athenian Empire, 431 BCE | `greeks-evidence-and-purpose` (Marsyas / Once in a Blue Moon) | **CC BY-SA 3.0** |
| `livy-poggio-manuscript-vat-lat-3331.jpg` | 3.3 — Livy, copied by Poggio, 1453 | `greeks-evidence-and-purpose` (Vatican) | Public domain |
| `xiang-yu-portrait-pma.jpg` | 3.4 — Xiang Yu, *Portraits of Famous Men* | `greeks-evidence-and-purpose` (Philadelphia Museum of Art) | Public domain |
| `paschal-table-annals.jpg` | 3.5 — paschal table, Cod. Sang. 459 | `divine-power-and-statecraft` (e-codices) | **CC BY-NC 4.0** |
| `mediterranean-chart-1569.jpg` | 3.6 — Forlani chart, 1569 (**cropped**) | `annales-longue-duree` (NMM Greenwich) | Public domain |
| `bede-hatton-43-f129r.jpg` | 4.1 — Bede IV.24, MS Hatton 43 | `divine-power-and-statecraft` (Bodleian) | **CC BY-SA 4.0** |
| `al-biruni-athar-f230.jpg` | 4.2 — al-Biruni, *al-Āthār al-bāqiya*, fol. 230 | `divine-power-and-statecraft` (BnF) | Public domain |
| `donation-of-constantine.jpg` | 4.3 — the Donation, 13th-c. fresco | `divine-power-and-statecraft` (Web Gallery of Art) | Public domain |
| `ranke-vorrede-1824.jpg` | 4.4 — Ranke's 1824 preface, p. VI (**cropped**) | `scientific-history` (Internet Archive) | Public domain |
| `olive-trees-1889.jpg` | 4.5 — Van Gogh, *The Olive Trees* | `annales-longue-duree` (MoMA) | Public domain |
| `lindisfarne-stone-raiders.jpg` | 5.1 — Lindisfarne grave marker | `divine-power-and-statecraft` (English Heritage; photo Schillerwein) | CC0 |
| `konigsberg-plan-1763.jpg` | 5.2 — plan of Königsberg, 1763 | `enlightenment-progress-2` (Leibniz-Institut) | CC0 |
| `henry-viii.jpg` | 5.3 — Henry VIII, after Holbein | `history-from-below` (Google Art Project) | Public domain |
| `manchester-kersal-moor-1852.jpg` | 5.4 — Wyld, *Manchester from Kersal Moor* | `marx-structural-history` (Royal Collection) | Public domain |
| `lepanto-1571.jpg` | 5.5 — the Battle of Lepanto | `annales-longue-duree` (NMM Greenwich) | Public domain |
| `joanna-southcott-1814.jpg` | 5.6 — Joanna Southcott, 1814 (**cropped**) | `history-from-below` (KU Leuven) | Public domain |
| `berlin-congress-1892.jpg` | 5.7 — von Werner, *Der Kongreß zu Berlin* | `gender` (Deutsches Historisches Museum) | Public domain |
| `salon-geoffrin-lemonnier.jpg` | 6.1 — Lemonnier, Madame Geoffrin's salon | `enlightenment-progress-2` (Malmaison) | Public domain |
| `condorcet-carnavalet-portrait.jpg` | 6.2 — Condorcet | `enlightenment-progress-2` (Carnavalet) | Public domain |
| `herder-graff-portrait.jpg` | 6.3 — Herder, by Graff, 1785 | `enlightenment-progress-2` | Public domain |
| `ranke-jebens-portrait-1875.jpg` | 6.4 — Ranke, by Jebens, 1875 | `scientific-history` | Public domain |
| `acton-portrait.jpg` | 6.5 — Lord Acton | `divine-power-and-statecraft` | Public domain |
| `encyclopedie-frontispiece.jpg` | 6.6 — *Encyclopédie* frontispiece | `enlightenment-progress-2` | Public domain |

## Notes

- **The CC BY and CC BY-SA images carry their attribution on the slide**, in
  the `p.cite` line under the picture. The paschal table is **CC BY-NC 4.0**;
  the use is non-commercial teaching, as in the Week 3 deck it comes from.
- **Some pairings are arguments, not illustrations.** Treitschke's lecture hall
  stands for state-funded history (1.4), Henry VIII for history moved by a
  decision (5.3), the Lindisfarne stone for history read through God (5.1),
  Königsberg for Kant's plan argued from one town (5.2). Each caption says what
  the picture actually is; the slide text says why it is there.
- **Nothing here is new to the course,** and every caption is drawn from the
  home deck's caption and credit row. If a home deck corrects one, correct it
  here too.

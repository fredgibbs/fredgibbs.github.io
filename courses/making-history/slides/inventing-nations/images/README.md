# Slide Images — Inventing Nations (9.1)

Ten image files, all used by `../index.md`. Eight are public domain, CC0 or
CC BY-SA; the two scholars' portraits, `anderson-cornell.jpg` and
`chatterjee-fukuoka.jpg`, are **fair use** for classroom teaching — see their
rows and the Notes. Credits are carried in the `<figcaption>`s and should not
be stripped.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `holy-roman-empire-1789.jpg` | Map of the Holy Roman Empire in 1789, English labels. Part one, after the "before 1800" cards. 1800×1467, from the 2650×2160 PNG at q88 | Robert Alfers (ziegelbrenner), 2008, after F. W. Putzger, *Historischer Weltatlas*; Wikimedia Commons ("Map of the Holy Roman Empire, 1789 en.png") | **CC BY-SA 3.0** — attribution in the caption |
| `fete-federation-1790.jpg` | Charles Thévenin, *La Fête de la Fédération, le 14 juillet 1790, au Champ-de-Mars*, oil on canvas, 1792. Part one, after the age-of-revolutions slide | Musée Carnavalet, Paris, via Wikimedia Commons (the "Musée Carnavalet - 2" file, 5688×3845); fetched at width 2000, long edge capped at 1800, q80 | CC0 |
| `sorrieu-pacte-1848.jpg` | Frédéric Sorrieu, *La République universelle démocratique et sociale: le pacte*, hand-colored lithograph, 1848 (printed by Lemercier). The last slide of part one. **A crop** to the picture: 2940×2050 from offset (30, 15) of the 3000×2432 file, removing the printed title and the mount, resized to 1800×1255 at q82 | Musée Carnavalet / Paris Musées, G.33112, via Wikimedia Commons ("1848 République universelle démocratique et sociale. Le Pacte. G.33112.jpg") | CC0 |
| `ranke-jebens-portrait-1875.jpg` | Leopold von Ranke aged about eighty, 1875, with two Prussian decorations on his chest. Part one, the Ranke portrait slide. 1332×1800 | Copied unchanged from `../../scientific-history/images/`, where its source is recorded (Adolf Jebens, 1875) | Public domain |
| `pledge-whittier-1899.jpg` | Frances Benjamin Johnston, "Saluting the flag at the Whittier Primary School," Hampton Normal and Agricultural Institute, Virginia, 1899 or 1900. The children are giving the outstretched-arm salute used with the Pledge until 1942. 1536×1204, re-encoded at q85 | Library of Congress, LCCN 2001703861 (cph 3b13292), via Wikimedia Commons | Public domain; LOC: no known restrictions |
| `jubilee-1897.jpg` | Queen Victoria's Diamond Jubilee procession passing the National Gallery, Trafalgar Square, 22 June 1897; photographer unrecorded. 1800×1430, from 2250×1788 at q82 | Royal Collection Trust, RCIN 2109693, via Wikimedia Commons ("Queen Victoria's Diamond Jubilee procession in front of the National Gallery.jpg") | Public domain |
| `constitution-1889.jpg` | Toyohara Chikanobu, *Kenpō happu shiki no zu* ("Illustration of the Ceremony Issuing the Constitution"), woodblock triptych, 1889. **A crop**: 1925×948 from offset (40, 36) of the 2000×1099 file, removing the museum's color bar and most of the margin, q85 | Metropolitan Museum of Art, DP147647, via Wikimedia Commons | CC0 |
| `gettysburg-reunion-1913.jpg` | Union and Confederate veterans shaking hands across the stone wall at the "Bloody Angle," Gettysburg reunion, July 1913. International News Service press photograph. Part one | Library of Congress, ppmsca.58372 (Liljenquist gift, 2018), via Wikimedia Commons ("Reunion of Confederate and Federal veterans at Gettysburg.jpg") | Public domain; LOC: no known restrictions |
| `anderson-cornell.jpg` | Benedict Anderson (1936–2015), black-and-white studio portrait, undated. Part two, the portrait slide. 450×517, used as downloaded | Cornell University, Department of Government, news page "Benedict Anderson, who wrote 'Imagined Communities,' dies" (`/sites/default/files/2026-05/ba.jpg`) | **Fair use** — see Notes |
| `chatterjee-fukuoka.jpg` | Partha Chatterjee (b. 1947), speaking at a seminar in Japan, in a dark jacket, bookshelves behind; undated, on the Fukuoka Prize's 2009 laureate page. Part three, the portrait slide. **A crop**, 352×500 from offset (248, 0) of a 600×500 photograph | Fukuoka Prize, laureate page for Partha Chatterjee (`/files/download/en/LaureatesI18n/laureate_blocks/a8739f58-4a4d-4bf4-b888-110aba18da1f/value21/value22/o`) | **Fair use** — see Notes |

Retrieved 2026-10-09, except the map, Sorrieu, Ranke, the Pledge, the jubilee
and the Meiji print, 2026-10-11. The folder totals about 6 MB.

Re-fetch the Commons files with
`curl -L 'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=<W>'`
and the processing given in each row (`sips -Z 1800 … -s formatOptions <q>`;
the Meiji crop is `magick in.jpg -crop 1925x948+40+36 +repage -quality 85`;
the Sorrieu crop is `magick in.jpg -crop 2940x2050+30+15 +repage -resize 1800x -quality 82`
on the 3000-pixel file).

## Notes

**No portrait of Maza.** The deck once ended on a fair-use crop of
Northwestern's photograph from her 2024 retirement celebration. The author
removed it on 2026-10-11 — no photographs of textbook authors — and the file
was deleted.

**The Pledge photograph does argumentative work, and is loaded.** Black
children at Hampton's practice school, photographed for the Hampton Album,
saluting a flag whose pledge promised "liberty and justice for all," fourteen
years before the Gettysburg reunion shut black veterans out. The salute looks
like the fascist one to a modern room; the caption says it was replaced in
1942 so the slide can be about the Pledge rather than the gesture.

**The jubilee photograph shows no colonial troops.** The caption's point that
they marched comes from the procession's order, not from this frame.

**The Anderson portrait is fair use.** The only freely licensed photographs
of him on Commons are frames from a 2012 UCD lecture video (854×480, CC BY
3.0); the cropped still used in the first draft was 300×400 and blurred, and
the author replaced it on 2026-10-09. The Cornell Department of Government's
portrait is the same studio photograph Times Higher Education ran with its
obituary, so it is probably a Cornell University Photography print; Cornell's
department page is the institutional source, which is why it is used rather
than the THE copy. Small, shown to identify the author of an assigned reading,
in a non-commercial teaching deck. Recorded in `../ISSUES.md`.

**The Chatterjee photograph is fair use, and the best of a poor field.**
Commons has no photograph of the scholar; every "Partha Chatterjee" file there
shows the West Bengal politician of the same name, so do not swap one in. The
first draft used Columbia's 300×300 faculty snapshot (flash, heavy JPEG), which
was unusable on a projector. Found on 2026-10-09: Columbia Law's copy of the
same snapshot (350×448); a 2020 webcam still (World Humanities Report,
800×718, blurred, mid-word); and the Fukuoka Prize laureate page's three
photographs (a youthful passport-style portrait, 460×500; a seminar in Japan,
600×500; and him at a desk in a kurta and shawl, 600×500). The deck used the
desk photograph until 2026-10-13, when the author noticed his eyes were
closed in it; it is now the seminar photograph, cropped to him at full
height (paper cups on the table are the cost of keeping 500 pixels). The
passport portrait is sharper but shows him as a student, decades before the
work in the deck. Searched again on 2026-10-13 with nothing better: the
Centre for Humanities Research at the University of the Western Cape has a
2013 lecture photograph at 300×197, a Columbia Law blog one at 225×225,
Commons only a 2020 Zoom recording at 854×480, and Columbia's own pages
block automated access. It is still about 1.0× in the portrait rail; see
`../ISSUES.md`.

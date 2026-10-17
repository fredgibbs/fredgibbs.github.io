# Slide Images — The Linguistic Turn (10.1)

Eleven image files, all used by `../index.md`. Nine are public domain or CC
licensed; the portraits of **Hayden White** and **Keith Jenkins** are **fair
use** for classroom teaching (see Notes). Credits are carried in the
`<figcaption>`s and should not be stripped.

## Credits

| File | What it is | Source | License |
|---|---|---|---|
| `inquiry-paris-1919.jpg` | The American Commission to Negotiate Peace's technical advisors (the Inquiry), Hotel Crillon, Paris, 5 April 1919. Part one, after the "room" slide. **A crop** to the print: 2071×1589 from offset (1591, 186) of the 3840-wide copy, removing the Signal Corps mount and its typed caption, resized to 1800 wide at q84 | Chas. Stern, U.S. Army Signal Corps, 111-SC-155707, National Archives, via Wikimedia Commons ("111-SC-155707 Technical Advisors, American Commission to Negotiate Peace…jpg") | Public domain (U.S. government work) |
| `sima-qian-portrait.jpg` | A later painted portrait of Sima Qian. 877×889, as downloaded | Wikimedia Commons, "Sima Qian (painted portrait).jpg" | Public domain |
| `davis-holberg-2010.jpg` | Natalie Zemon Davis speaking at the Holberg Prize events, Bergen, 8 June 2010. **A crop**, 500×940 from offset (505, 40) of the 1500×998 file, removing the two men beside her | Holbergprisen on Flickr; photograph Marit Hommedal/Scanpix; Wikimedia Commons ("Natalie Zemon Davis.jpg") | CC BY 2.0 — attribution in the caption |
| `fools-cap-map-c1590.jpg` | *Fool's Cap Map of the World*, engraving, about 1580–1590, the map after Oronce Finé's heart-shaped projection. 1800×1375 from the 3840-wide file at q84 | Wikimedia Commons ("Fool's Cap Map of the World.jpg") | Public domain |
| `hayden-white.jpg` | Hayden White speaking at a lectern at the Freie Universität Berlin, undated. **A crop**, 1000×1180 from offset (1360, 290) of a 2464×1640 photograph | John F. Kennedy Institute, Freie Universität Berlin, news page on Hayden White; photograph Bernd Wannenmacher | **Fair use** — see Notes |
| `scott-2013-portrait.jpg` | Joan Wallach Scott, 2013 | Copied unchanged from `../../gender/images/`, where its source is recorded | CC BY-SA 3.0 |
| `coras-arrest-memorable-1618.jpg` | Title page of Jean de Coras, *Arrest memorable du Parlement de Tolose*, Lyon: Barthelemy Vincent, 1618. **A crop** removing the "Digitized by Google" mark at the foot, resized to 1187×1800 at q82 | Biblioteca Nazionale Centrale, Rome, copy digitized by Google; Internet Archive `bub_gb_N57dWHm1RHEC`, page n4 | Public domain |
| `jenkins-2013.jpg` | Keith Jenkins, a frame from "Interview with Professor of Historical Theory Keith Jenkins (University of Chichester)", St Mary's University, Twickenham, December 2013. **A crop**, 600×720 from offset (330, 0) of the 1280×720 frame | YouTube video `cu2znmjTgvM`, frame `maxres2.jpg` | **Fair use** — see Notes |
| `lyotard.jpg` | Jean-François Lyotard, photographed by Bracha L. Ettinger, retouched. 868×1182, as downloaded | Wikimedia Commons ("Jean-Francois Lyotard cropped.jpg") | CC BY-SA 2.0 — attribution in the caption |
| `berlin-brandenburg-gate-1989.jpg` | Crowds at the Wall before the Brandenburg Gate, late 1989 (the uploader says November; Commons notes it may be 22 December). 1800×1173 from the 3840-wide file at q80 | Raphaël Thiémard on Flickr, via Wikimedia Commons ("Berlin 1989, Fall der Mauer, Chute du mur 19.jpg") | CC BY-SA 2.0 — attribution in the caption |
| `nietzsche-c1875.jpg` | Friedrich Nietzsche, about 1875. 1327×1800 from the 1464×1986 file at q85 | F. Hartmann, via Wikimedia Commons ("Nietzsche187a.jpg") | Public domain |

Retrieved 2026-10-16. The folder totals about 4 MB.

Re-fetch the Commons files with
`curl -L 'https://commons.wikimedia.org/wiki/Special:FilePath/<FILE>?width=<W>'`
and the processing in each row (`magick in.jpg -crop WxH+X+Y +repage -resize … -quality …`).

## Notes

**The Hayden White photograph is fair use.** Commons has two images of him:
a 498×400 black-and-white desk photograph from the UC Santa Cruz Special
Collections (CC BY-SA 3.0, roughly 1980s), and a 220×293 Stanford snapshot.
Both are far too small for a portrait slide. UC Santa Cruz's obituary images
are 250 pixels wide, and the AHA's obituary image refused automated download.
The Freie Universität photograph is 2464×1640, captioned at its source as
Hayden White and credited to Bernd Wannenmacher. Its face matches the Santa
Cruz photograph. Small, shown to identify a historian discussed in an assigned
reading, in a non-commercial teaching deck.

**The Keith Jenkins still is fair use, and under resolution.** There is no
photograph of him on Commons or on his Wikipedia article, and the only author
photograph found online is an 80×80 thumbnail at Akal México. The St Mary's
interview is the one usable source. The frame chosen is the one with his eyes
open; the other two `maxres` frames catch him looking down. It is 720 pixels
tall, about 1.0× in the portrait rail. A better copy would need the original
video file from St Mary's University (Centre for Philosophy of History).

**The Davis, Scott and Sima Qian files are under 1.5×.** Each is the largest
free copy found. `scripts/deck-check.sh` warns on them; see `../ISSUES.md`.

**No portrait of Maza.** She is the textbook author, per `SLIDE-STYLE.md`.

**Images considered and not used.** A Johns Hopkins seminar-room photograph
from about 1887–1890 (the Ferdinand Hamburger Archives; its old
`digital.library.jhu.edu` links now redirect to a new platform that could
not be searched automatically) would make the "room" point better than the
1919 Paris photograph; worth fetching by hand. The Commons scan of the 1561
first edition of Coras is 329×514, too small; the 1618 Lyon edition stands in.
A 2022 photograph of the Jorvik Viking Centre ride was considered for
Jenkins's "heritage histories" and dropped as too dark to read on a projector.

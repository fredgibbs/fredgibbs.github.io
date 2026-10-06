# Images — purpose-and-progress

Every image here is new to the course: none of them appears in another deck,
and none is from an assigned reading. That is the point of the deck — students
bring Carr, Ranke, Marx, Thompson, Scott and Ginzburg to material they have
never seen, instead of recognising a picture they were shown in Week 5.

All eleven were fetched from Wikimedia Commons on 2026-10-03, long edge capped
at 1200px and recompressed at q82. 1200 rather than the usual 1800 because
every one of them is shown at roughly half the slide width in a pair, or
height-constrained in a single; 1200 is still about three times the rendered
size. Folder total 4.2MB.

| File | What it is | Source | License |
|---|---|---|---|
| `mappa-mundi-hereford-c1300.jpg` | The Hereford *Mappa Mundi*, c. 1300, east at the top and Jerusalem at the centre | Hereford Cathedral, via unesco.org.uk, Wikimedia Commons (`Hereford-Karte.jpg`) | Public domain |
| `blue-marble-1972.jpg` | *The Blue Marble*, Apollo 17, 7 December 1972 | Harrison Schmitt / NASA, AS17-148-22727, via Wikimedia Commons | Public domain |
| `phrenology-chart-wellcome.jpg` | French wall chart *Phrénologie, physiognomonie, chiromancie*, 19th c. — brain maps, profile heads and read palms on one sheet | Wellcome Collection V0009525, via Wikimedia Commons | **CC BY 4.0** |
| `fmri-basal-ganglia.jpg` | Basal ganglia activation, fMRI, figure from a 2014 paper | Miller AH et al., *PLOS ONE* 9(5), 2014, via Wikimedia Commons (`CFS-brain-scan-basal-ganglia-fMRI.png`) | **CC BY 4.0** |
| `knossos-blue-boy-restored.jpg` | The "Saffron Gatherer" from Knossos as restored under Arthur Evans by Émile Gilliéron; the flat fields between the surviving fragments are modern | Photograph Zde, Archaeological Museum of Heraklion, via Wikimedia Commons | Public domain |
| `torlino-before-after-1882.jpg` | Tom Torlino, Diné, on arrival at the Carlisle Indian Industrial School and after about three years, mounted as one before-and-after plate | John N. Choate; Beinecke Rare Book & Manuscript Library, Yale University, via Wikimedia Commons | Public domain |
| `vietnam-wall-names.jpg` | A visitor taking a pencil rubbing of a name at the Vietnam Veterans Memorial, 2003 | U.S. Navy photo by CWO Seth Rossman, 030616-N-9593R-145, via Wikimedia Commons | Public domain |
| `tomb-of-the-unknown-soldier.jpg` | The Tomb of the Unknown Soldier, Arlington National Cemetery | SNik7Real, via Wikimedia Commons | **CC BY 4.0** |
| `lascaux-replica-brno.jpg` | A painted horse in the Lascaux replica at the Anthropos Museum, Brno — **a replica, not the cave** | HTO, via Wikimedia Commons (`Lascaux, horse.JPG`) | Public domain |
| `lascaux-2-montignac.jpg` | The interior of Lascaux II at Montignac, the full-scale facsimile built 200 m from the original | Raimond Spekking, via Wikimedia Commons | **CC BY-SA 4.0** |
| `firdos-square-2003.jpg` | The statue of Saddam Hussein pulled down in Firdos Square, Baghdad, 9 April 2003 | U.S. Department of Defense, via Wikimedia Commons (`SaddamStatue.jpg`) | Public domain |

## Notes

**Attribution is on the slide, not only here.** The three CC BY and the one
CC BY-SA file name their creator in the deck's own `figcaption` credit line, as
the license requires. Don't strip those lines when editing captions. This site's
use is non-commercial teaching, which also covers the CC BY-NC material in other
decks; nothing here is NC.

**Both "Lascaux" images are replicas, and the deck says so.** The cave has been
closed since 1963. Commons has several files captioned simply "Lascaux" that are
in fact photographs of one replica or another — `Lascaux, horse.JPG` is the Brno
museum copy, which its own file description states and its title does not. The
slide is built on that fact rather than tripping over it. If either file is ever
swapped, check the description, not the filename.

**Re-fetch command.** Each file came from Commons `Special:FilePath` at
`?width=1600`, then:

```sh
sips -Z 1200 raw.jpg --out <name>.jpg -s format jpeg -s formatOptions 82
```

**Two images are smaller than the rest at source.** `fmri-basal-ganglia.jpg`
(1483x921 on Commons) and `firdos-square-2003.jpg` (1700x1072) were near the
1200 cap already, so they gained little from the resize. Both still read at
projector distance; the fMRI figure is the weakest of the eleven and would be
the first to replace if a larger CC-licensed scan turns up.

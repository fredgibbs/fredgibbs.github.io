# Open problems — Expertise and Trust in Humanities AI

Excluded from the build. Notes for whoever picks this deck up next.

## Image attribution to confirm

The printing-house engraving on slide 03 (`images/printing-house.jpg`) came
from the Amaranth header library with no recorded credit. The detail is
consistent burin work, not a generated pastiche, but the exact plate is
unidentified — it resembles the printing-house scene from Stradanus's *Nova
Reperta* (c. 1600) without being confirmed as it. The caption claims nothing
about artist or date for that reason. Identify it before publishing the deck,
or swap in a plate with a known source.

Slide 04 is settled: Joseph Wright of Derby, *An Experiment on a Bird in an
Air Pump*, 1768, National Gallery, London. Downloaded from Wikimedia Commons,
which records it as public domain; the credit is in the speaker note.

## Claims to confirm before presenting

- **The stewardship slide (14) describes a policy as if it is settled practice.**
  The wording follows amaranth.unm.edu/projects/ai-humanities ("talk with us
  before uploading anything... who has a stake in the material, what
  permissions matter"). Confirm it is what actually happens before saying it to
  a room.
- **"a machine in the room"** (slide 14). The Amaranth site says a local AI
  workstation is being built, but the page it links to for that no longer
  mentions it. Either it shipped, it slipped, or the link is stale — check
  which before claiming it.
- **Named credits on slide 15.** The three-name credit block is visible on the
  page, so that claim is safe. The consent process behind it is not stated
  anywhere public; the slide says "attribution is the visible half" to stay
  inside what can be shown.
- **Year-one figures** (slide 10 notes): 14 courses, ~180 students, nine class
  websites. **Maxwell Museum scanning and high-school 3D printing** (slide 18
  notes). Both from Amaranth's own future-directions page — fine to repeat, but
  they are a year old and the numbers will have moved.

- **Alvarado Hotel** (slide 09 notes): Whittlesey, Santa Fe Railway, Mission
  Revival, largest of the Harvey hotels, demolished 1970 over citizen protest.
  Sourced from Wikipedia only. Confirm before saying any of it from the stage.
- **"Some of the sites have not been touched in years"** (slide 14 notes).
  True of the older Xanthan sites in the gallery; check which ones, and drop
  the line rather than guess at a number.
- **"Two courses — qualitative methods and local food systems"** (slide 12).
  Confirm the course titles.

## Images

Websites are captured with `scripts/deck-shot.sh` at **1400x1900** — the
capitals poster's proportion — and set in an `.s-column` beside their text.

Two findings behind that, both worth not re-learning:

**The viewport has to stay 900 tall.** These sites size their heroes in `vh`,
so capturing at `--window-size=1400,1900` made the hero 1900 tall and showed
nothing else. The script pins the layout viewport at 1400x900 over CDP and
captures beyond it. An earlier round of these images has the giant-hero bug;
anything captured with a plain `--window-size` will too.

**The whole page is the wrong unit.** Real heights at a 900px viewport:

| page | full height | screens | ratio | width at 640 tall |
|---|---|---|---|---|
| Oral histories (farming) | 2,864 | 3.2 | 0.49 | 313px |
| AI Sketchbook | 2,942 | 3.3 | 0.48 | 306px |
| Farmer profiles | 3,390 | 3.8 | 0.41 | 264px |
| Campus Histories | 3,464 | 3.8 | 0.40 | 259px |
| Xanthan gallery | 3,616 | 4.0 | 0.39 | 249px |
| Amaranth home | 5,609 | 6.2 | 0.25 | 160px |
| capitals poster | 1,827 | — | **0.77** | **490px** |

A page is only poster-shaped for its first screen and a half. (An earlier
version of this table gave the gallery as 12,630 tall and the Amaranth home as
16,000 — those were the `vh` bug measuring itself, not real heights.)

`xanthan-gallery` (y=700) and `farmer-profiles` (y=800) use a scroll offset:
the top of those pages is not the part worth showing. `campus-hero`, `farming`
and `farmer-profiles` come from the live sites and cannot be rebuilt locally.
`galileo-moons` is a composite: the Moon plate from the Venice first edition
(Baglioni, 1610 — Smithsonian Libraries copy, Internet Archive
`Sidereusnuncius00Gali`, leaf 22) beside the same plate from the Frankfurt
piracy (Palthenius, 1610 — Boston Public Library copy, Internet Archive
`sidereusnunciusm00gali_0`, leaf 20), cropped square on each moon and set on
the theme ground. Both 1610 printings are public domain. The edition history
and the upside-down woodcuts are from Linda Hall Library, "The Face of the
Moon," section B. `printing-house.jpg` is the image this slide used before and
is now unused — keep it or delete it.

`capitals-poster` is downscaled from the 10800x14100 export at
`~/Desktop/8-20-stash/Capitals Poster 4.png`. `sandia` and `cliff-model` are
not screenshots.

## Deck grammar

Title, then strict alternation: `.s-statement` introduces a topic, `.s-plate`
shows it. Keep it. If a topic needs two pictures, it needs two claims.

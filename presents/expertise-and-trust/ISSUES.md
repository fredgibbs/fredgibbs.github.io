# Open problems — Expertise and Trust in Humanities AI

Excluded from the build. Notes for whoever picks this deck up next.

## MemoryTour is a guess

Nothing called MemoryTour exists in any repo on this machine, so slide 07's
scene was drawn from what the name and the surrounding work imply: oral
history indexed by place, a walking route with numbered stops, a card holding
one recording and its unchecked draft transcript.

**If that is wrong, the fix is in the SVG on slide 07, not in the theme.** The
map, the route, the stops and the card are all plain shapes in the deck's own
`.pv-scene` block. The speaker note already tells you to cut to the live demo
here if there is one; if there is, a screenshot is better than a drawing and
this scene should go.

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

Every plate is 1920x1080, so reveal never re-crops one. Sites are shot at a
1600x1200 viewport and set on the theme ground at their own proportions, so a
slide shows a page with its own margins instead of a magnified fragment. The
script and the reasoning are in `presents/AGENTS.md`. Sources:

- `sketchbook.jpg` — local build, `/ai-sketchbook/research/`
- `amaranth-home.jpg` — local build of amaranth-unm.github.io
- `campus-hero.jpg` — live, https://amaranth.unm.edu/campus-history/
- `farming.jpg` — live, https://oral-histories-mrg.github.io/oral-histories-of-farming/
- `xanthan-gallery.jpg` — the card grid from amaranth's `/websites/gallery`,
  windowed out of a full-page capture at the same viewport
- `farmer-profiles.jpg` — live, the farmer-profiles page of the Rio Grande site
- `capitals-poster.jpg` — the poster's top band only, at 80% on the theme
  ground, so the stripe never lands on the poster's own body text
- `sandia.jpg`, `cliff-model.jpg` — not screenshots; left at their own size

The two remote sites cannot be rebuilt locally, so re-shooting them needs
network access.

## Deck grammar

Title, then strict alternation: `.s-statement` introduces a topic, `.s-plate`
shows it. Keep it. If a topic needs two pictures, it needs two claims.

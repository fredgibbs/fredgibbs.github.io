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

## Claims to confirm — the CHM section (slides A1–A5, D1)

These slides were drafted from the working files in
`~/Dropbox/projects/chm-food-health-medicine`. Everything below is accurate as
of 2026-09-23 and most of it will drift, because the project is live.

- **Counts.** All from counting on 2026-09-23: 54 dated `## 2026-` entries in
  `methods-log.md` ("fifty-four entries," A4 notes + D1), 63 PDFs under
  `sources/` ("sixty-odd," A2 and A3 notes), 56 notes, 15 interrogation passes,
  9 lenses. The instruction word count in A3's notes ("about seven thousand four
  hundred") is `AGENTS.md` + `synthesis/reading-protocol.md` +
  `synthesis/style-guide.md` = 7,368, and excludes the nine lenses in
  `interrogation-log.md` — so it is conservative, which is the right direction.
  **Recount the morning of the talk** — these numbers are spoken from the stage,
  so a stale one is the exact kind of unchecked claim this deck is about.
- **The Müldner quotation** (A2 notes): "focused on individual sites or
  cemeteries… the number of individuals analysed often relatively small." Taken
  from `notes/Muldner-2009-investigating-medieval-diet-isotopes.md`, which cites
  Müldner 2009 in *Reflections: 50 Years of Medieval Archaeology*. The note is a
  reading record, not the page. Check it against the PDF before quoting it aloud.
- **A5's two catches** are paraphrased, not quoted. Catch 01 (the invented
  opponent) compresses `methods-log.md` 2026-06-29, "A worked example of the
  auditability argument" — which records two foils retired in one exchange, the
  anti-Whig debate and then wellness-culture presentism. Catch 02 (the premature
  verdict) is `methods-log.md` 2026-06-30, the provisionality principle. Both log
  entries were drafted by the model recording corrections the author made, so the
  *judgement* is the author's and the *wording* is not — worth owning if asked,
  and it is the honest limit of the colophon analogy at the end: the log is a
  record kept by the thing being recorded.
- **"Within the hour"** (A5, catch 01) dramatizes the log, which says the second
  foil came in the same exchange on the same day but gives no interval. Either
  soften to "in the same conversation" or check the timestamps.
- **"Dozens of studies out of hundreds"** (A5, catch 02) follows the log's own
  wording; elsewhere the project says ~40 studies read. Consistent, but do not
  sharpen it into a figure on stage without recounting.
- **P1 claims two precedents** because the deck shows two (print, the air pump).
  That is a claim about what this talk covers, not about the history — do not let
  it harden into "there have only ever been two."

- **Naming the venue** (A1 slide + notes): the chapter is under contract to CUP
  for *The Cambridge History of Medicine* vol. 2, and the proposed title change
  is still pending editor approval. Confirm it is appropriate to name the volume
  and the editors publicly before the chapter is delivered.
- **B1's second example is unsourced.** Print inventing the corrector, editor and
  bibliographer rests on Johns, already credited on slide 03. The photography /
  draughtsmanship / caption claim is the author's own formulation with no source
  behind it — either ground it or soften it to a gesture.

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

# Conference Decks

Rules for decks in `presentations/`. These are conference and symposium talks
for outside audiences — a different genre from the course decks in `courses/`,
which have their own rules in `courses/SLIDE-STYLE.md`.

**Read that file too.** Its content rules apply here in full: be direct, avoid
metaphor, name people rather than reducing them to an epithet, cite what you
claim. What changes below is the form, not the standards.

A deck lives at `presentations/<talk-slug>/`, with `index.md` beside an
`images/` folder.

---

## How a conference deck differs from a lecture deck

| | Lecture deck | Conference deck |
|---|---|---|
| Runs | 50–75 min, you stop and discuss | 5–20 min, timed, no stopping |
| Carries | A source students read closely | An argument the room hasn't heard |
| Slide does | Holds text you talk *through* | Shows a picture you talk *over* |
| Audience | Knows the course | Knows their field, not your work |

The practical consequence: **a conference slide is a composition, not a page.**
One idea per slide, most of the words spoken rather than shown, and the deck
paced so a slide can go by in ten seconds without anyone feeling cheated.

---

## Rules

**Put the timing in the speaker notes and make it add up.** Every `<section>`
gets an `<aside class="notes">` opening with its window (`**2:25–2:50**`).
The last one must end at the time you were given. A ten-minute talk that runs
fourteen is a worse talk, and the only way to know is to write the budget down.

**No inline styles. Ever.** No `style="..."` attributes and no `<style>` block
in `index.md`. Every measurement is a named class in the deck's theme CSS —
the same rule the lecture theme follows ("the class replaces that" in
`courses/SLIDE-STYLE.md`). If a slide needs a width or a position the theme
doesn't have, add a modifier to the CSS with a comment saying what it's for.
Older decks (`presentations/ai-student-success`) carry a large inline `<style>`
block; that predates this rule and is not a model to copy.

**Write slides in Markdown.** The `<section>` is the composition surface —
it carries the sheet margin, the layout grid and the scrim — so a slide is one
tag wrapping prose, and type styling comes from where an element sits rather
than from a class on it. A heading is the headline, a paragraph is the
supporting line, `---` is the dimension rule, `**`/`*` are the two emphases.
The deck turns this on with one line below its front matter:

```
{::options parse_block_html="true" auto_ids="false" /}
```

Reach for a class only where position can't say it — an eyebrow, a caption, a
tag — using a kramdown IAL on the line after: `{: .pv-eyebrow .terra}`.

**No `<br>` and no `&nbsp;`, anywhere in a deck.** Headlines flow. Don't hand-
break a line and don't hold words apart with hard spaces — both put layout in
the prose, where it can't be changed without editing the words.

Where a headline should turn is a function of its measure: tune the
`max-width` on that slide type in the theme. Where a label needs air around a
separator (`01 / GENERATE`, `a · b`), that's `word-spacing` in the theme. A
label/value pair is a definition list, which kramdown writes natively:

```
Speaker
: Fred Gibbs
```

A short headline stranding its last word on a line of its own usually means
the measure is too wide by a little; narrow it until the turn falls where the
sense does.

**Guard raw-HTML blocks with `markdown="0"`.** A `<div>` holding inline tags
(`<i>`, `<span>`, `<img>`, `<svg>`) makes kramdown switch that block to span
parsing, lose the closing tag, and silently nest every following `<section>`
inside it — the deck still builds, and the slide count quietly drops. Any
structural block (`.pv-device`, `.pv-phone`, `.pv-key`, `.art`) carries
`markdown="0"`. Check the count after a build:

```sh
grep -c '<section' _site/presentations/<talk>/index.html
```

**Three cascade traps, all of which fail silently.** Each cost a full
build-and-look cycle; check them first when a slide lays out wrong:

1. *Reveal writes `display` inline on every slide*, from its `display` config
   option. No stylesheet can override it. The layout sets `display: 'grid'`;
   every slide type is shaped as a grid because of that.
2. *`.reveal .slides section` (two classes + an element) out-specifies
   `.reveal .s-title`*, so per-type padding is discarded. Slide-type rules are
   written `.reveal .slides section.s-title`.
3. *The generic `.reveal .slides section p` rule out-specifies `.reveal
   .pv-cap`*, so a named part set on a Markdown paragraph loses its type.
   Named parts are written `.reveal .slides section .pv-cap`.

Don't force `position: relative` on every child to lift content above the
scrim — it overrides `position: absolute` on the pinned caption bars. The
scrim is a `::before` at `z-index: -1` inside the section's own stacking
context instead.

**Front matter is the layout, nothing else:**

```yaml
---
layout: reveal-provocation
title: "Deck Title"
---
```

**One theme per genre, not per deck.** `assets/css/reveal-provocation-theme.css`
is the image-forward theme; its header comment is canonical for the class
mechanics and slide types, and this file does not duplicate it. A new talk
reuses it. Only fork a theme when the *genre* changes — and then write the
new theme's header comment as carefully as the existing ones.

**Say where a picture came from.** Screenshots of live sites are fine and are
the best evidence a talk about web publishing can have; capture them fresh
rather than reusing stale ones. Caption an AI-generated image as AI-generated,
on the slide, in a `.pv-cap`. In a talk that argues about machine fabrication,
an unlabelled generated image is a hole in your own argument.

**Capture a screenshot at 1600x1200, not at the slide's size.** A page shot at
a 1000px viewport and shown full-bleed on a 1280px slide is magnified 1.28x:
its nav is enormous, and the part of the page you wanted runs off the bottom
of the slide. Shoot the site's *desktop* layout at a viewport wider than the
slide, take a tall slice of it, and set that on the theme ground:

```sh
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=1600,1200 \
  --virtual-time-budget=9000 --screenshot=page.png "https://example.org/"
```

Then frame it — a 960x540 box at `background: #1c1814`, the shot as an `<img>`
inset 12px from the top at `height: 528px; width: auto`, centred — and shoot
that box at `--force-device-scale-factor=2` for a 1920x1080 plate.

1600 is the width to hold: below about 1400 a responsive site collapses to its
tablet layout, which is a different site than the one you are talking about.
The height is how much page you get, and 900 is not much — shoot **1600x1200**
and set the result on the theme ground inside the 16:9 frame at its own
proportions, rather than filling the slide with it. The page then lands at
roughly 0.6x with its own margins showing, and reads as *a website* instead of
a page you are standing inside. Full-bleed is for photographs, not for pages.

Deliver every image at 1920x1080 for the same reason: reveal re-crops anything
that isn't 16:9, silently and from the centre, which is never where the
interesting part is. `sips --cropOffset` does not fix this — it is accepted and
ignored. Compose crops in headless Chrome instead, with the image as a
`background` on a 16:9 box.

**Check every claim about a real building, person, or quotation**, and put the
source in the notes under a `{: .sources}` line. Conference audiences contain
the specialist. Undated is better than wrong: if you can't confirm a year,
write around it.

---

## Before you call it done

1. `LC_ALL=en_US.UTF-8 bundle exec jekyll build` — a non-UTF-8 locale fails the
   SCSS compile (see the root `AGENTS.md`).
2. **Look at every slide rendered**, at 1280×720, not just the source. This is
   not optional and it is not satisfied by reading the file: every failure
   listed above builds cleanly and looks fine in the source. Serve `_site/` and
   screenshot the deck slide by slide, then view the shots — a montage of all
   of them is enough to catch layout breakage, with a full-size look at any
   slide that carries a screenshot behind type.
3. **Check for collisions with a screenshot's own headline.** A site's hero
   title sits exactly where a slide's headline wants to go. Either use a
   `.heavy` scrim, or drop your headline to `.sm` and let the page's own title
   be the title.
4. Read the notes end to end as a script. If the words only make sense with the
   slide on screen, the slide is carrying argument it should be carrying alone.
5. Confirm the last note's end time is the time you were given.

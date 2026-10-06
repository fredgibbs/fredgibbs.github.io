# Issues — review-jeopardy

**What this is.** A Jeopardy board for the 8.1 review before fall break: six
categories of five clues, two Daily Doubles, and a Final Jeopardy that hands
off to 8.1's second discussion question ("Which purpose is most defensible?").
It is an alternative to presenting `../what-are-we-talking-about/` or
`../purpose-and-progress/`. Those stay the written record of 8.1. This one
records nothing after class, because the argument happens out loud.

**It is not a reveal deck.** Three files, none with front matter, so Jekyll
copies them as-is:

- `clues.yml` — every category, clue, response, source and image. **Edit this
  one.** Its header comment says what each field does.
- `jeopardy.css` — the look, in the lecture decks' palette and fonts.
- `index.html` — the game. It reads `clues.yml` on load and parses it with the
  copy of js-yaml vendored at `/assets/vendor/js-yaml-4.1.0/` (MIT, license
  beside it), so the classroom needs no CDN for the board to work.

A mistake in `clues.yml` shows on screen instead of the board: a YAML error
gives its line and column with the lines around it, and a board that can't be
built (a category with four clues, a clue with no response) is listed in
words. The likeliest mistake is a colon followed by a space in an unquoted
value, such as a source citing "Gender: A Useful Category"; quote the whole
value.

**It no longer opens straight from Finder.** Browsers won't let a `file://`
page read the `clues.yml` beside it, so open it through
`LC_ALL=en_US.UTF-8 bundle exec jekyll serve` or on the live site. Opened from
Finder, the page says so and gives the localhost address. That was the price of
moving the clues into YAML (2026-10-05); the alternative that keeps Finder
working is a `clues.js` file of JavaScript, which is harder to edit.

The style guide's mechanics (`scripts/slide-words.py`, the 960×700 box) don't
apply: clue text is shrunk to fit the screen in JavaScript. After the split,
the game was played end to end headlessly over HTTP at 1920×1080, 1280×720 and
1024×768 with no clipping and no console errors, and every field of
`clues.yml` was compared against the inline data it replaced: 150 fields, no
differences.

**Presenting.** Space (or a clicker's right arrow) reveals the response, then
returns to the board. Esc also returns. F is full screen, M mutes the
synthesized sounds. After a reveal, ✓/✗ per team adds or subtracts the value;
clicking a mark again takes it back. Team names and scores in the footer are
click-to-edit. "Put back" returns a clue that was opened by mistake. The game
saves to the browser's local storage, so a reload offers "Resume game"; use a
private window for a clean run. Daily Doubles land at random each new game,
never on the $200 row and never two in one category.

**Everything is reused from decks that checked it.** No new quotations and no
readings. On 2026-10-05 all 40 quoted strings in the game were matched
mechanically, word for word, against the deck sources in `../`: pull every
“…” out of `clues.yml`, split on ellipses, and search the other decks'
`index.*` for each fragment. Rerun that after editing a clue. Nothing was re-verified
against a primary PDF. Where each clue comes from:

- *Who said it?* — Marx (`../marx-structural-history/`), Carr
  (`../carr-historian-and-facts/`), Ranke and al-Biruni (`../review-weeks-1-6/`),
  Braudel's fireflies (`../annales-longue-duree/`).
- *Job descriptions* — Livy and Herodotus (`../review-weeks-1-6/`), Machiavelli
  (`../divine-power-and-statecraft/`), Thompson (`../history-from-below/`), Sima
  Qian (`../greeks-evidence-and-purpose/`).
- *Show your sources* — Bede, Valla and the paschal table
  (`../divine-power-and-statecraft/`), Thucydides 1.22
  (`../greeks-evidence-and-purpose/`), Vansina (`../history-from-below/`).
- *Progress?* — Voltaire, Kant, Condorcet, Herder
  (`../enlightenment-progress-2/`), Ranke 1854 (`../scientific-history/`).
- *Zoom out* — `../annales-longue-duree/` and `../marx-structural-history/`.
- *Who counts?* — Ginzburg (`../review-weeks-1-6/`), the Luddite print and
  Thompson p. 9 (`../history-from-below/`), Scott (`../gender/`).
- *Final* — the five purposes are `../../schedule.md`'s 8.1 prompt, with one
  change: the schedule gives Ranke "truth", which would fit Thucydides or
  al-Biruni as well, so the clue uses his own "what actually happened".

**Two clues are worded around a problem on purpose.**

- *Herder ($1000, Progress?)* quotes Popkin's paraphrase, not Herder: the
  "universal standard of civilization derived from the experience of Western
  Europe" line is Popkin p. 68 describing Herder's objection. The clue says
  "Popkin says" so it is not passed off as Herder's own words.
- *al-Biruni ($1000, Who said it?)* carries no date, because the decks disagree
  on one. `../what-are-we-talking-about/` (and `../../schedule.md`) date the
  *Kitab al-Hind* "c. 1017"; `../divine-power-and-statecraft/` dates it "c. 1030"
  and gives 1017 as the year he was taken to Mahmud's court. The 1030 date looks
  like the right one for the book. If it is, the 8.1 deck's "c. 1017" is the
  one to fix, and its "eight centuries early" still holds (1030 to 1824).

**Not done yet: a fresh-context review.** `../../SLIDE-STYLE.md` requires one
before a deck is published. Since every clue is lifted from a deck that has
had one, the risk is mainly in the new framing sentences around the quotes;
those are the thing to point a reviewer at.

**The schedule does not link this.** The page contains every answer, so link
it under 8.1 in `../../schedule.md` only after class, if at all. Once pushed,
it is public at its URL whether linked or not.

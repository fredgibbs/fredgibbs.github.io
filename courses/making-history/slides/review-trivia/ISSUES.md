# Issues — review-trivia

**Big ideas is commented out (2026-10-06).** Its four conceptual questions
became `../big-picture-review/`, a separate slide deck built from the 8.1
instructor discussion guide. The round is still in `rounds.yml`, commented line
by line; remove the leading `# ` to restore it. The game now runs four rounds,
the tie-breaker prints on the round-4 sheet, and the timed questions take about
21 minutes. Notes below that mention Big ideas describe the round as it was.

**Jokers are off (2026-10-06)** for the first run, as one rule too many.
`jokers: false` at the top of `rounds.yml` hides them everywhere: the title
cards, the ×2 buttons and hint in the scores table, the standings label and
the box on the answer sheets, and any joker already recorded is ignored in the
totals. `jokers: true` brings all of it back; tested both ways, with the
jokers-on totals matching a hand count. The notes on jokers below describe it
switched on.

**What this is.** Pub trivia for the 8.1 review before fall break: five rounds
of written answers, done in groups, with one joker per team. It sits beside
`../review-jeopardy/`, which stays as the fast, buzz-in alternative. Trivia is
slower on purpose: no timer, answers written on a sheet, and a closing round of
judged conceptual questions. Neither game is the written record of 8.1; that is
`../what-are-we-talking-about/`.

**Three files, none with front matter**, so Jekyll copies them as-is:

- `rounds.yml` — every round, question, answer, context note and image.
  **Edit this one.** Its header comment says what each field does.
- `trivia.css` — the look, in the Jeopardy board's palette and fonts, plus the
  printable answer sheets.
- `index.html` — the game. It reads `rounds.yml` on load with the js-yaml copy
  vendored at `/assets/vendor/js-yaml-4.1.0/`.

Like the Jeopardy board, it does not open straight from Finder: browsers won't
let a `file://` page read the YAML beside it. Open it through
`LC_ALL=en_US.UTF-8 bundle exec jekyll serve` or on the live site; from Finder
the page says so. A mistake in `rounds.yml` shows on screen with its line
number, or as a list of what can't be built.

**How a round runs.** Title card (teams decide on their joker) → questions one
at a time → "pencils down" while the sheets come in → the same questions again
with answers, context notes and sources, which is where the review discussion
happens. Mark that round's sheets while the next round plays and type the
scores into the table (S). There are no standings slides between rounds
(removed 2026-10-06); "Show standings" in the scores table puts them up on
demand. After the tie-breaker, the final standings are revealed one team per
press, last place first. Keys: Space/→ forward, ← back, S scores, F full
screen, M mute. The menu in the bottom bar jumps to the start of any round's
questions or answers, the tie-breaker, or the final standings, and shows which
section is on screen.

**Scoring.**

- Points per question are set per round in `rounds.yml`; half points are
  allowed in the table (step 0.5), for the judged round.
- **Joker:** each team doubles one round (`joker_multiplier: 2`), ticked on
  that round's sheet before question 1 and recorded with the ×2 button in the
  scores table. The table allows one per team: clicking another round's ×2
  moves it.
- **No joker on Big ideas** (`joker: false`). Those answers are judged, and
  doubling them doubles the marker's judgment call rather than the team's
  knowledge. Delete the line to allow it.
- **Tie-breaker:** a number each team writes at the bottom of its last sheet
  (Livy: 142 books, 35 survive), entered in the table. Equal totals are ranked
  by whose guess is closer.

**Timers.** Set per round in `rounds.yml`: 30 seconds a question for rounds 1,
2 and 4, 60 for the pictures, and one 10-minute clock for the whole Big ideas
round, which keeps running as you move between its questions. A slim bar on
question screens only; gold for the last five seconds, a soft chime at zero,
and the game never moves on by itself. T (or a click on the bar) pauses,
resumes, or restarts it. `timers: false` at the top of the file hides them
all. They are pacing, not a speed game, which is why the answer screens have
none. At these lengths the timed questions take about 31 minutes before answers and
discussion.

**Answer sheets.** "Answer sheets" (or the page URL with `?sheets`) shows one
letter page per round: team name, joker box, numbered lines, the name bank for
round 4, and the Big ideas questions printed in full with writing boxes, the
tie-breaker at its foot. Print one set per team. Checked as a PDF: exactly five
pages.

**Everything is reused from decks that checked it.** No new quotations and no
readings. On 2026-10-05 all 27 quoted strings in `rounds.yml` were matched
mechanically, word for word, against the other decks' `index.*` (pull every
“…”, split on ellipses, search for each fragment). Rerun that after editing a
question. Nothing was re-verified against a primary PDF. Where the rounds come
from:

- *Who said it?* — the Jeopardy quotations, plus Thompson p. 9
  (`../history-from-below/`), Voltaire p. 5 (`../enlightenment-progress-2/`),
  Thucydides 5.89 (`../greeks-evidence-and-purpose/`), Bede's preface and
  Scott p. 1067 (`../review-weeks-1-6/`).
- *Name that thing* — terms each deck taught: *istoria* (`../greeks-evidence-and-purpose/`),
  the *longue durée* and the *Annales* (`../annales-longue-duree/`), the Donation
  and the paschal table (`../divine-power-and-statecraft/`), *wie es eigentlich
  gewesen* (`../scientific-history/`), unsocial sociability
  (`../enlightenment-progress-2/`), grave-diggers (`../marx-structural-history/`),
  the cheese (`../review-weeks-1-6/`). A griot question (the *ngoni* postcard
  from `../history-from-below/`) was cut on 2026-10-06; the class hadn't spent
  much time on it.
- *Picture round* — the images and captions of the decks named in
  `images/README.md`.
- *Where were they?* — the portrait captions: Kant and Voltaire
  (`../enlightenment-progress-2/`), Braudel's Oflag X-C slide
  (`../annales-longue-duree/`), Bede and Machiavelli
  (`../divine-power-and-statecraft/`), Marx's Reading Room slide
  (`../marx-structural-history/`), Thompson (`../history-from-below/`), Ranke
  (`../scientific-history/`). Herodotus and Condorcet are decoys.
- *Big ideas* — model answers built from the decks' takehomes:
  `../scientific-history/` (Ranke's preface, the seminar, the 1854 lecture),
  `../review-weeks-1-6/` and `../what-are-we-talking-about/` (scale, purpose,
  the inquisition record read twice).

**The model answers are examples, not the only right answers.** The answers
to the picture round and Big ideas say what a strong response draws on; the
context line under each gives background only and never mentions points
(changed at Fred's request, 2026-10-06). Points are on the title cards: two a
picture, a partial answer getting one, and up to three per Big ideas question.
A group that argues something the model doesn't list can still earn full
marks. That is deliberate: the round exists to reward argument.

**Tested 2026-10-05.** Played end to end headlessly over HTTP at 1920×1080,
1280×720 and 1024×768: 97 screens, none clipped, no console errors. Scores and
jokers entered through the real table matched a hand count, a forced 56–56 tie
went to the closer tie-breaker guess, and a reload offered "Resume game".

**Not done yet: a fresh-context review.** `../../SLIDE-STYLE.md` requires one
before a deck is published. Every quotation comes from a deck that has had
one; what is new is the question wording and the Big ideas model answers, and
those are what to point a reviewer at.

**The schedule does not link this.** The page carries every answer. Link it
under 8.1 in `../../schedule.md` only after class, if at all; once pushed, it is
public at its URL whether linked or not.

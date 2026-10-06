# Issues — review-questions

**What this is.** The pub trivia's questions as a plain walkthrough for 8.1:
each question on its own screen, then the same question with its answer,
context and source, then the next. Meant to run beside `../big-picture-review/`
as a content review, not as a game. Cloned on 2026-10-06 from
`../review-trivia/`, which is untouched and still runs as the game.

**What was left behind.** Teams, scoring, the scores table and standings,
jokers, timers, sound, the printable answer sheets and the tie-breaker. The
Big ideas round, already commented out in the trivia, was not carried over:
its questions are the discussion questions in `../big-picture-review/`.
`rounds.yml` here has only the fields this page reads (its header lists them),
and the four section descriptions were reworded for a walkthrough.

**Three files, none with front matter,** so Jekyll copies them as-is:
`rounds.yml` (edit this one), `review.css` (cut down from the trivia's
`trivia.css` to what this page uses) and `index.html` (a smaller rewrite of the
trivia page). Like the trivia, it reads `rounds.yml` on load with the js-yaml
copy in `/assets/vendor/js-yaml-4.1.0/`, so it opens through
`bundle exec jekyll serve` or the live site, not from Finder.

**Presenting.** Space or → forward, ← back, Home to the start, F full screen.
The bottom bar's menu jumps to the start of any section. The page remembers
its place, so a reload resumes; Home starts over.

**Questions are the trivia's, checked there.** Every quotation was matched
against the earlier decks when the trivia was built; nothing new was added
here. If a question changes in one folder, decide whether the other should
follow; they are separate copies now.

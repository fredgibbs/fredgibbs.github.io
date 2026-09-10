# fredgibbs.net

Jekyll site for http://fredgibbs.net. Course pages, lecture slide decks,
projects, tutorials, and a CV.

## Building

Jekyll's SCSS compile fails on an encoding error under a non-UTF-8 locale, so
always build with the locale set:

```sh
LC_ALL=en_US.UTF-8 bundle exec jekyll build
```

`bash scripts/a11y.sh` runs the accessibility audit (see `README.md`).

`scripts/ocr-pdf.swift` OCRs a scanned course reading that has no text layer,
so a quotation or page number can be checked with `grep` instead of by reading
page images. Cache the output beside the PDF, never in this repo — see "Cache
the text of a scanned reading" in `courses/SLIDE-STYLE.md`.

## Lecture slide decks

**Read `courses/SLIDE-STYLE.md` before creating or editing any deck.** It is
the source of truth for content rules, deck structure, front matter, image
sourcing and licensing, and the pre-publish checks. The CSS class mechanics it
refers to are documented in the header comment of
`assets/css/reveal-lecture-theme.css`.

Decks live at `courses/<course>/slides/<deck-slug>/index.md` and use
`layout: reveal-lecture`.

A finished deck is not done until a **fresh-context agent** has reviewed it for
historical accuracy, quotation accuracy, and cross-slide consistency. Spawning
that subagent is expected here — see "Before publishing" in
`courses/SLIDE-STYLE.md` for what to ask it and what to do with the findings.

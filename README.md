The repository for http://fredgibbs.net

## Accessibility workflow (beginner-friendly)

This project has a repeatable accessibility check that runs your Jekyll site locally, then audits key pages.
It does not require keeping `node_modules/` in this repo.

### 1) One-time setup

```bash
cd /Users/fwgibbs/Dropbox/projects/mysite
bundle install
```

### 2) Run the automated checks

```bash
bash scripts/a11y.sh
```

What this does:
- Starts Jekyll on `http://127.0.0.1:4000`
- Runs `pa11y-ci` via `npx` against core pages (WCAG 2 AA)
- Runs Lighthouse accessibility checks via `npx`
- Stops everything automatically when complete

### 3) Read results

- Terminal output shows pass/fail and specific issues.
- Lighthouse reports are saved in `.lighthouseci/`.

### 4) Keep it repeatable

- Update page list in `.pa11yci.json` and `lighthouserc.json` whenever you add important pages.
- Run `bash scripts/a11y.sh` before publishing major content or style changes.

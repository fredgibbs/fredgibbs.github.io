#!/usr/bin/env python3
"""Word-budget check for a lecture deck.

Usage:  scripts/slide-words.py courses/<course>/slides/<deck>/index.md [...]
        scripts/slide-words.py courses/making-history/slides/*/index.md

Prints every prose container over its target word count, and exits 1 if any
container is over its hard stop. Budgets and rationale live in
courses/SLIDE-STYLE.md, "Keep the blocks short" — this script is only the
measurement; that file is the rule.
"""
import re
import sys

# container -> (target, hard stop)
BUDGET = {
    "takehome":      (30, 40),
    "reveal-block":  (55, 70),
    "notes bullet":  (40, 50),
    "caption":       (40, 55),
    "intro caption": (80, 90),
    "detail":        (30, 40),
    "main-point":    (14, 18),
    "question":      (35, 45),
}


def words(raw):
    """Visible words in a chunk of deck markdown."""
    t = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)          # tags
    t = re.sub(r"\{:[^}]*\}", " ", t)       # kramdown IALs
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", t)  # links, keep text
    t = re.sub(r"^\s*#{1,6}\s*", " ", t, flags=re.M)  # heading markers
    t = re.sub(r"^\s*[-*]\s+", " ", t, flags=re.M)    # bullet markers
    t = re.sub(r"[*_`]", "", t)
    return [w for w in t.split() if re.search(r"[\wÀ-ɏ]", w)]


def blocks(src):
    """Yield (kind, text) for every budgeted container in a deck."""
    # div-based blocks: .takehome and .reveal-block
    for kind in ("takehome", "reveal-block"):
        pat = r'<div class="[^"]*\b' + kind + r'\b[^"]*"[^>]*>(.*?)</div>'
        for m in re.finditer(pat, src, re.S):
            body = re.sub(r"^\s*######.*?$", "", m.group(1), flags=re.M)  # label
            yield kind, body

    # figcaptions are budgeted by job, not by tag: a caption carrying a
    # <span class="why"> line is introducing a person and gets the larger
    # budget, whole; any other caption is described by its <em> note.
    for fig in re.finditer(r"<figure[^>]*>(.*?)</figure>", src, re.S):
        cap = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", fig.group(1), re.S)
        if not cap:
            continue
        if 'class="why"' in cap.group(1):
            yield "intro caption", cap.group(1)
        else:
            for em in re.finditer(r"<em>(.*?)</em>", cap.group(1), re.S):
                yield "caption", em.group(1)

    # bullets inside an .image-notes notes column
    for notes in re.finditer(r'<div class="notes"[^>]*>(.*?)</div>', src, re.S):
        for line in notes.group(1).split("\n"):
            if line.lstrip().startswith(("- ", "* ")):
                yield "notes bullet", line

    # IAL-tagged paragraphs and headlines
    for kind in ("detail", "main-point", "question"):
        pat = r"^(.*?)\n\{:[^}]*\." + kind + r"\b[^}]*\}"
        for m in re.finditer(pat, src, re.M):
            yield kind, m.group(1)


def check(path):
    try:
        src = open(path, encoding="utf-8").read()
    except OSError as e:
        print(f"{path}: {e}", file=sys.stderr)
        return 2

    over, worst = [], 0
    counts = {}
    for kind, raw in blocks(src):
        n = len(words(raw))
        if n == 0:
            continue
        counts.setdefault(kind, []).append(n)
        target, stop = BUDGET[kind]
        if n > target:
            snippet = " ".join(words(raw)[:9])
            over.append((n - target, kind, n, target, stop, snippet))
            worst = max(worst, 1 if n <= stop else 2)

    print(f"\n{path}")
    if counts:
        summary = "  ".join(
            f"{k} n={len(v)} med={sorted(v)[len(v)//2]}/{BUDGET[k][0]}"
            for k, v in sorted(counts.items())
        )
        print(f"  {summary}")
    if not over:
        print("  all containers within target")
        return 0

    for _, kind, n, target, stop, snippet in sorted(over, reverse=True):
        flag = "OVER STOP" if n > stop else "over     "
        print(f"  {flag} {kind:14} {n:3}w (target {target}, stop {stop})  {snippet}…")
    return worst


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    rc = 0
    for path in sys.argv[1:]:
        rc = max(rc, check(path))
    print()
    return 1 if rc >= 2 else 0


if __name__ == "__main__":
    sys.exit(main())

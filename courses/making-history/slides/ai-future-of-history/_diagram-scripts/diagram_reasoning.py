"""Build the reasoning-trace diagram for the AI deck from reason-Qwen3-1.7B.json,
in the same page style as diagrams.py. Every excerpt is asserted to be a verbatim
substring of the saved output; cuts are marked with an ellipsis."""
import json, html, os, re

# The shared page style, read from diagrams.py without running it (its probe JSON may be absent).
CSS = re.search(r'CSS = """(.*?)"""', open("diagrams.py").read(), re.S).group(1)

R = json.load(open("reason-Qwen3-1.7B.json"))["runs"]["zimmerman"]
MORE = json.load(open("reason-more-Qwen3-1.7B.json"))

def verbatim(src, s):
    assert s in src, f"not verbatim: {s[:60]}"
    return html.escape(s)

def mark(s, words, cls):
    for w in words:
        s = s.replace(html.escape(w), f'<b class="{cls}">{html.escape(w)}</b>')
    return s

NOTES = [
    "I think the main library, which is the Zimmerman Library, was built in the 1950s. But I'm not sure about the exact year. Maybe it was constructed in 1952? Wait, I should check if there's a specific year mentioned in any official sources.",
    "I think the library was built in 1952. However, I should verify this.",
    "The Zimmerman Library is the main library, and it was built in 1952. Yes, that's a common fact.",
    "Let me confirm once more. Yes, the Zimmerman Library at the University of New Mexico was constructed in 1952.",
]
CHECKING = ["I should check", "I should verify this", "Yes, that's a common fact", "Let me confirm once more"]
ANSWER = [
    "The Zimmerman Library at the University of New Mexico was built in **1952**.",
    "The library was designed by the architectural firm H. H. Richardson & Company",
]
CLAIMS = ["1952", "H. H. Richardson &amp; Company"]

notes = " <span class=cut>…</span> ".join(mark(verbatim(R["notes"], n), CHECKING, "chk") for n in NOTES)
ans = " <span class=cut>…</span> ".join(verbatim(R["answer"], a) for a in ANSWER).replace("**", "")
for c in CLAIMS:
    ans = ans.replace(c, f'<b class="claim">{c}</b>')
ans += " <span class=cut>…</span>"
ys = [re.search(r"\*\*(\d{4})\*\*", m["answer"]).group(1) for m in MORE]
years = ", ".join(ys[:-1]) + " and " + ys[-1]

PAGE_CSS = """
.ask { font-family: 'JetBrains Mono', monospace; font-size: 25px; line-height: 1.3; margin: 12px 0 20px; color: #e9ebf3; max-width: 730px; }
.panel { border-left: 2px solid #3a4160; padding: 4px 0 6px 20px; margin-top: 14px; }
.panel.answer { border-left-color: #a78bfa; margin-top: 20px; }
.lab { font-family: 'JetBrains Mono', monospace; font-size: 15px; letter-spacing: .14em; color: #949cb3; text-transform: uppercase; margin-bottom: 8px; }
.panel.answer .lab { color: #c4b5fd; }
.txt { font-size: 24px; line-height: 1.42; color: #aab1c7; }
.panel.answer .txt { font-size: 27px; color: #e9ebf3; }
b.chk { color: #c4b5fd; font-weight: 600; }
b.claim { color: #f9a8c0; font-weight: 600; }
.cut { color: #6b7390; }
.fact { position: absolute; right: 52px; top: 34px; font-family: 'JetBrains Mono', monospace; font-size: 17px; line-height: 1.4;
  color: #f4c27a; border: 1px solid rgba(244,194,122,.5); border-radius: 6px; padding: 9px 14px; text-align: right; }
"""
body = ('<div class="k">Qwen3 1.7B · thinking mode · one run</div>'
        '<div class="fact">Begun Dec. 1936 · opened Apr. 1938<br>Architect: John Gaw Meem</div>'
        f'<div class="ask">{html.escape(R["prompt"])}</div>'
        f'<div class="panel"><div class="lab">Notes · {R["notes_tokens"]} tokens</div><div class="txt">{notes}</div></div>'
        f'<div class="panel answer"><div class="lab">Answer · {R["answer_tokens"]} tokens</div><div class="txt">{ans}</div></div>'
        '<div class="foot">Temperature 0.6, seed 1105, no search. Excerpts verbatim; … marks a cut. '
        f'Four more runs (seeds 1106–1109) answered {years}.</div>')

H = 620
os.makedirs("diagrams", exist_ok=True)
with open("diagrams/reasoning.html", "w") as f:
    f.write(f"<!doctype html><meta charset=utf-8><style>:root{{--h:{H}px}}{CSS}{PAGE_CSS}</style><body>{body}</body>")
open("diagrams/reasoning.h", "w").write(str(H))
print("ok", years)

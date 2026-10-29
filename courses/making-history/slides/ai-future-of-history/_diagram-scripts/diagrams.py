"""Build the AI deck's diagrams as HTML pages, from the probe JSON, for
headless Chrome to screenshot. Writes diagrams/<name>.html."""
import json, html, os

G = json.load(open("probe-gpt2.json"))
O = json.load(open("probe-OLMo-2-0425-1B.json"))
os.makedirs("diagrams", exist_ok=True)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { width: 1200px; height: var(--h); background: #0b0d15; color: #e9ebf3;
  font-family: Inter, sans-serif; }
body { padding: 40px 52px; position: relative; overflow: hidden;
  background-image: radial-gradient(900px 500px at 92% -10%, rgba(139,92,246,.20), transparent 62%),
                    radial-gradient(rgba(255,255,255,.05) 1px, transparent 1.3px);
  background-size: auto, 24px 24px; }
.k { font-family: 'JetBrains Mono', monospace; text-transform: uppercase; letter-spacing: .16em;
  font-size: 16px; color: #67e8f9; }
.k::before { content: '› '; color: #a78bfa; }
.prompt { font-family: 'JetBrains Mono', monospace; font-size: 31px; line-height: 1.3; margin: 12px 0 22px;
  color: #e9ebf3; }
.prompt .cursor { display: inline-block; width: 16px; height: 36px; background: #e9a8fb; vertical-align: -6px; margin-left: 6px; }
.row { display: grid; grid-template-columns: 150px 1fr 100px; align-items: center; gap: 22px; margin: 9px 0; }
.tokname { font-family: 'JetBrains Mono', monospace; font-size: 28px; text-align: right; color: #c9cee0; white-space: pre; }
.bar { height: 34px; border-radius: 3px; background: linear-gradient(90deg, #3a4160, #4b5378); }
.bar.hi { background: linear-gradient(90deg, #5fdcf2, #a78bfa); }
.bar.true { background: linear-gradient(90deg, #f4c27a, #f9a8c0); }
.pct { font-family: 'JetBrains Mono', monospace; font-size: 26px; color: #949cb3; }
.pct.true { color: #f4c27a; }
.note { font-family: 'JetBrains Mono', monospace; font-size: 19px; color: #949cb3; letter-spacing: .04em; }
.model { font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: 30px; color: #bcc6ff; margin-bottom: 4px; }
.model small { font-family: 'JetBrains Mono', monospace; font-weight: 400; font-size: 18px; color: #949cb3; letter-spacing: .08em; margin-left: 10px; }
.foot { position: absolute; left: 52px; right: 52px; bottom: 24px; font-family: 'JetBrains Mono', monospace;
  font-size: 15px; color: #7d859e; letter-spacing: .03em; }
"""

def page(name, body, extra_css="", h=600):
    with open(f"diagrams/{name}.html", "w") as f:
        f.write(f"<!doctype html><meta charset=utf-8><style>:root{{--h:{h}px}}{CSS}{extra_css}</style><body>{body}</body>")
    open(f"diagrams/{name}.h", "w").write(str(h))

def esc(s):
    return html.escape(s)

def show_tok(t):
    # make a leading space visible as a middle dot, as tokenizer viewers do
    return esc(t).replace(" ", "·")

# ---- 1. tokens ------------------------------------------------------------
TOKCSS = """
.sent { margin: 20px 0 30px; }
.chips { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 18px; }
.chip { border-radius: 8px; padding: 10px 14px 8px; min-width: 60px; text-align: center; }
.chip b { display: block; font-family: 'JetBrains Mono', monospace; font-weight: 500; font-size: 28px; white-space: pre; color: #0b0d15; }
.chip i { display: block; font-style: normal; font-family: 'JetBrains Mono', monospace; font-size: 17px; margin-top: 6px; color: rgba(11,13,21,.72); }
.c0 { background: #7fe3f8; } .c1 { background: #a5b4fc; } .c2 { background: #e9a8fb; } .c3 { background: #f4c27a; } .c4 { background: #86efac; }
.src { font-size: 23px; color: #949cb3; font-family: Inter, sans-serif; }
"""
body = '<div class="k">How GPT-2 reads a sentence · one chip per token, its number below</div>'
for sent in G["tokens"][:2]:
    chips = "".join(
        f'<div class="chip c{i % 5}"><b>{show_tok(t)}</b><i>{n}</i></div>'
        for i, (t, n) in enumerate(sent["tokens"]))
    body += f'<div class="sent"><div class="src">“{esc(sent["text"])}”</div><div class="chips">{chips}</div></div>'
body += ('<div class="foot">· marks a space, which belongs to the token after it. '
         f'GPT-2 knows {G["vocab"]:,} tokens. OLMo 2 (2025) cuts the year into “·”, “188”, “9”.</div>')
page("tokens", body, TOKCSS, 600)

# ---- 2. next-token list ---------------------------------------------------
def bars(items, scale, true_tok=None, hi=()):
    out = ""
    for t, p in items:
        cls = "true" if t == true_tok else ("hi" if t in hi else "")
        w = max(0.8, p / scale * 100)
        pct = f"{p*100:.1f}%" if p >= 0.01 else f"{p*100:.2f}%"
        out += (f'<div class="row"><div class="tokname">{show_tok(t)}</div>'
                f'<div><div class="bar {cls}" style="width:{w:.1f}%"></div></div>'
                f'<div class="pct {cls}">{pct}</div></div>')
    return out

top = G["unm"]["top"]
body = ('<div class="k">GPT-2 · the ten most probable next tokens</div>'
        f'<div class="prompt">{esc(G["unm"]["prompt"])}<span class="cursor"></span></div>'
        + bars(top, top[0][1], true_tok=" 1889", hi=(" 18",))
        + f'<div class="foot">The other {G["vocab"] - len(top):,} tokens share the remaining '
          f'{(1 - sum(p for _, p in top)) * 100:.0f}%. Amber: the correct year.</div>')
page("next-token", body, ".row{margin:5px 0}.bar{height:28px}.tokname{font-size:26px}.pct{font-size:24px}", 590)

# ---- 3. three runs ---------------------------------------------------------
RUNCSS = """
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 4px; }
.run { font-size: 23px; line-height: 1.36; color: #c9cee0; padding: 14px 0 14px 18px; border-left: 2px solid #3a4160; margin-top: 16px; }
.run b { color: #f9a8c0; font-weight: 600; }
.fact { position: absolute; right: 52px; top: 34px; font-family: 'JetBrains Mono', monospace; font-size: 18px;
  color: #f4c27a; border: 1px solid rgba(244,194,122,.5); border-radius: 6px; padding: 10px 16px; }
"""
def cut(s, n=22):
    words = s.strip().replace("\n", " ").split()
    out = []
    for w in words:
        out.append(w)
        if len(out) >= 8 and w.endswith(".") and not w[:-1].isdigit():
            return " ".join(out)
        if len(out) >= n:
            break
    return " ".join(out) + " …"

def runs(d):
    out = ""
    for s in d["samples"]["texts"]:
        t = cut(s)
        head, _, rest = t.partition(" ")
        if head == "the":  # "the 1970s"
            h2, _, rest = rest.partition(" ")
            head = "the " + h2
        out += f'<div class="run"><b>{esc(head)}</b> {esc(rest)}</div>'
    return out

body = ('<div class="k">One prompt · three runs per model</div>'
        f'<div class="prompt">{esc(G["samples"]["prompt"])}<span class="cursor"></span></div>'
        '<div class="fact">Begun Dec. 1936 · opened Apr. 1938</div>'
        '<div class="cols">'
        f'<div><div class="model">GPT-2<small>OPENAI · 2019</small></div>{runs(G)}</div>'
        f'<div><div class="model">OLMo 2 1B<small>AI2 · 2025</small></div>{runs(O)}</div>'
        '</div>'
        '<div class="foot">Sampled at temperature 0.8, seed 1105. Each run cut at its first full sentence, or after 22 words (…).</div>')
page("three-runs", body, RUNCSS, 700)

# ---- 4. 1791 ---------------------------------------------------------------
PCSS = """
.block { margin-top: 26px; }
.prompt.small { font-size: 25px; margin: 6px 0 12px; }
.pair { display: grid; grid-template-columns: 1fr 1fr; gap: 44px; }
.row { grid-template-columns: 160px 1fr 96px; margin: 6px 0; }
.bar { height: 30px; }
"""
def probe_rows(d, key, words, scale, hi):
    items = []
    for w in words:
        p = d[key]["probes"].get(w, [None])[0]
        if p is None:
            p = dict(d[key]["top"]).get(w, 0.0)
        items.append((w, p))
    return bars(items, scale, hi=hi)

body = ('<div class="k">Next-word probabilities · two prompts, two models</div>'
        '<div class="block">'
        f'<div class="prompt small">{esc(G["rev1791"]["prompt"])} …</div>'
        '<div class="pair">'
        f'<div><div class="model">GPT-2<small>2019</small></div>{probe_rows(G, "rev1791", [" France", " Haiti"], 0.40, (" Haiti",))}</div>'
        f'<div><div class="model">OLMo 2 1B<small>2025</small></div>{probe_rows(O, "rev1791", [" France", " Haiti"], 0.40, (" Haiti",))}</div>'
        '</div></div>'
        '<div class="block">'
        f'<div class="prompt small">{esc(G["slaverev"]["prompt"])} …</div>'
        '<div class="pair">'
        f'<div><div class="model">GPT-2<small>2019</small></div>{probe_rows(G, "slaverev", [" Haiti", " Virginia"], 0.40, (" Haiti",))}</div>'
        f'<div><div class="model">OLMo 2 1B<small>2025</small></div>{probe_rows(O, "slaverev", [" Haiti", " Brazil"], 0.40, (" Haiti",))}</div>'
        '</div></div>'
        '<div class="foot">Bars on one scale, 0–40%. Each model\'s other choices are not shown.</div>')
page("1791", body, PCSS, 540)

# ---- 5. pronouns -----------------------------------------------------------
body = '<div class="k">Next-word probabilities · “he” or “she”</div>'
for key in ("historian", "nurse"):
    body += ('<div class="block">'
             f'<div class="prompt small">{esc(G[key]["prompt"])} …</div>'
             '<div class="pair">'
             f'<div><div class="model">GPT-2<small>2019</small></div>{probe_rows(G, key, [" he", " she"], 0.16, ())}</div>'
             f'<div><div class="model">OLMo 2 1B<small>2025</small></div>{probe_rows(O, key, [" he", " she"], 0.16, ())}</div>'
             '</div></div>')
body += '<div class="foot">Bars on one scale, 0–16%. The rest of each list, mostly “the”, is not shown.</div>'
page("pronouns", body, PCSS + ".block{margin-top:30px}", 540)
print("ok")

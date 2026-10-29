"""Next-token probabilities from a small open language model, for the AI deck.

usage: probe.py MODEL_ID
Prints, for each prompt, the top-k next tokens with probabilities, and the
probability of a few named tokens of interest.
"""
import sys, json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = sys.argv[1]
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=(torch.bfloat16 if "OLMo" in model_id else torch.float32))
model.eval()

PROMPTS = {
    "unm": ("The University of New Mexico was founded in", []),
    "historian": ("The historian said that", [" he", " she", " they"]),
    "nurse": ("The nurse said that", [" he", " she", " they"]),
    "professor": ("The professor said that", [" he", " she", " they"]),
    "rev1791": ("In 1791, a great revolution began in", [" France", " Haiti", " Saint", " the"]),
    "slaverev": ("The largest and most successful slave revolt in history took place in", [" Haiti", " the", " Saint", " Jamaica", " Brazil"]),
    "historyof": ("The history of the United States begins with", []),
}

def topk(prompt, k=10, probe=()):
    ids = tok(prompt, return_tensors="pt").input_ids
    with torch.no_grad():
        logits = model(ids).logits[0, -1]
    p = torch.softmax(logits.float(), -1)
    vals, idx = p.topk(k)
    top = [(tok.decode([int(i)]), float(v)) for v, i in zip(vals, idx)]
    probes = {}
    for w in probe:
        wid = tok(w, add_special_tokens=False).input_ids
        probes[w] = (float(p[wid[0]]), [tok.decode([t]) for t in wid])
    return top, probes

out = {"model": model_id, "vocab": len(tok)}
for key, (prompt, probe) in PROMPTS.items():
    top, probes = topk(prompt, probe=probe)
    out[key] = {"prompt": prompt, "top": top, "probes": probes}
    print(f"\n== {key}: {prompt!r}")
    for t, v in top:
        print(f"   {t!r:16} {v:.4f}")
    for w, (v, pieces) in probes.items():
        print(f"   probe {w!r:10} {v:.4f}  pieces={pieces}")

# tokenization examples
for s in ["The University of New Mexico was founded in 1889.",
          "Zimmerman Library, Albuquerque, New Mexico",
          "Silences enter the process of historical production"]:
    ids = tok(s, add_special_tokens=False).input_ids
    print("\nTOKENS", s)
    print("  ", [(tok.decode([i]), i) for i in ids])
    out.setdefault("tokens", []).append({"text": s, "tokens": [(tok.decode([i]), i) for i in ids]})

# three sampled continuations of a history prompt
torch.manual_seed(1105)
prompt = "Zimmerman Library at the University of New Mexico was built in"
ids = tok(prompt, return_tensors="pt").input_ids
samples = []
for _ in range(3):
    g = model.generate(ids, do_sample=True, temperature=0.8, top_p=0.95, max_new_tokens=30,
                       pad_token_id=tok.eos_token_id)
    samples.append(tok.decode(g[0][ids.shape[1]:]))
print("\nSAMPLES", prompt)
for s in samples:
    print("   ->", repr(s))
out["samples"] = {"prompt": prompt, "seed": 1105, "temperature": 0.8, "top_p": 0.95, "texts": samples}

with open(f"probe-{model_id.split('/')[-1]}.json", "w") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)

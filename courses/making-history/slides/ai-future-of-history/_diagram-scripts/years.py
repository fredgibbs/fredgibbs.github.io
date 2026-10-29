"""Probability of each whole year as the continuation of a prompt.

usage: years.py MODEL_ID
Scores " 1850" ... " 1960" by multiplying the model's token probabilities
along the year's canonical tokenization, so models whose tokenizers split
years differently can be compared. Also scores whole words for the 1791 prompt.
"""
import sys, json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = sys.argv[1]
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, dtype=(torch.bfloat16 if "OLMo" in model_id else torch.float32))
model.eval()

def seq_prob(prompt, cont):
    p_ids = tok(prompt, add_special_tokens=False).input_ids
    c_ids = tok(prompt + cont, add_special_tokens=False).input_ids[len(p_ids):]
    ids = torch.tensor([p_ids + c_ids])
    with torch.no_grad():
        logp = torch.log_softmax(model(ids).logits[0].float(), -1)
    total = 0.0
    for k, t in enumerate(c_ids):
        total += float(logp[len(p_ids) + k - 1, t])
    return float(torch.exp(torch.tensor(total))), [tok.decode([t]) for t in c_ids]

out = {"model": model_id}
prompt = "The University of New Mexico was founded in"
years = {}
for y in range(1850, 1961):
    p, pieces = seq_prob(prompt, f" {y}")
    years[y] = p
top = sorted(years.items(), key=lambda kv: -kv[1])[:10]
print("YEARS", prompt, "sum 1850-1960 =", round(sum(years.values()), 4))
for y, p in top:
    print(f"   {y}  {p:.4f}")
print("   1889 rank", sorted(years, key=lambda y: -years[y]).index(1889) + 1, f"p={years[1889]:.4f}")
out["years"] = {"prompt": prompt, "top": top, "p1889": years[1889], "sum": sum(years.values())}

prompt = "In 1791, a great revolution began in"
words = {}
for w in [" France", " Haiti", " Saint-Domingue", " America", " Poland", " Paris"]:
    p, pieces = seq_prob(prompt, w)
    words[w] = (p, pieces)
    print(f"1791 {w!r:20} {p:.5f} {pieces}")
out["rev1791"] = {"prompt": prompt, "words": words}

with open(f"years-{model_id.split('/')[-1]}.json", "w") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)

"""Four more Zimmerman runs (seeds 1106-1109), answers only, to show the 1105 run is typical or not."""
import json, re, torch
from transformers import AutoTokenizer, AutoModelForCausalLM
mid = "Qwen/Qwen3-1.7B"
tok = AutoTokenizer.from_pretrained(mid)
model = AutoModelForCausalLM.from_pretrained(mid, dtype=torch.bfloat16).to("mps").eval()
q = "When was Zimmerman Library at the University of New Mexico built?"
text = tok.apply_chat_template([{"role": "user", "content": q}], tokenize=False, add_generation_prompt=True, enable_thinking=True)
ids = tok(text, return_tensors="pt").input_ids.to("mps")
END = tok.convert_tokens_to_ids("</think>")
out = []
for seed in (1106, 1107, 1108, 1109):
    torch.manual_seed(seed)
    with torch.no_grad():
        g = model.generate(ids, do_sample=True, temperature=0.6, top_p=0.95, top_k=20, max_new_tokens=1500)
    new = g[0, ids.shape[1]:].tolist()
    cut = new.index(END) + 1 if END in new else 0
    ans = tok.decode(new[cut:], skip_special_tokens=True).strip()
    out.append({"seed": seed, "notes_tokens": cut, "answer": ans})
    print(seed, cut, "|", ans[:400].replace("\n", " "), "\n")
json.dump(out, open("reason-more-Qwen3-1.7B.json", "w"), indent=1, ensure_ascii=False)

"""The Zimmerman question as a careful user would ask it, for comparison with the
bare question in reason.py and reason_more.py (seeds 1105-1109). Same model,
settings and seeds; two conditions:
  rule   - a custom instruction to say "I don't know" rather than guess
  source - the Wikipedia article's lead paragraph supplied, answer to quote it
"""
import json, torch
from transformers import AutoTokenizer, AutoModelForCausalLM
mid = "Qwen/Qwen3-1.7B"
tok = AutoTokenizer.from_pretrained(mid)
model = AutoModelForCausalLM.from_pretrained(mid, dtype=torch.bfloat16).to("mps").eval()
END = tok.convert_tokens_to_ids("</think>")

Q = "When was Zimmerman Library at the University of New Mexico built?"
RULE = "If you are not sure of a fact, say that you don't know instead of guessing."
# Wikipedia, "Zimmerman Library", lead paragraph, fetched 2026-10-29.
PASSAGE = ("Zimmerman Library is the historic main library of the University of New Mexico, located near the center of "
           "the university campus in Albuquerque, New Mexico. It is one of the largest and most notable buildings designed "
           "by New Mexico architect John Gaw Meem and is the centerpiece of the UNM Libraries, the largest library system in "
           "New Mexico with almost 4 million print volumes. It was built in 1936–38 with funding from the Public Works "
           "Administration and Works Progress Administration, with further additions completed in 1966 and 1973. The "
           "building was named for former university president James Fulton Zimmerman in 1961. It was added to the New "
           "Mexico State Register of Cultural Properties and the National Register of Historic Places in 2016.")
CONDITIONS = {
    "rule": [{"role": "system", "content": RULE}, {"role": "user", "content": Q}],
    "source": [{"role": "user", "content": "Answer using only the passage below, and quote the sentence your answer comes from.\n\n"
                                            f"Passage:\n{PASSAGE}\n\nQuestion: {Q}"}],
}

out = {"model": mid, "settings": "thinking mode, temperature 0.6, top_p 0.95, top_k 20, max_new_tokens 1500, bfloat16, mps",
       "question": Q, "rule": RULE, "passage": PASSAGE, "runs": {}}
for name, msgs in CONDITIONS.items():
    text = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=True)
    ids = tok(text, return_tensors="pt").input_ids.to("mps")
    out["runs"][name] = []
    for seed in (1105, 1106, 1107, 1108, 1109):
        torch.manual_seed(seed)
        with torch.no_grad():
            g = model.generate(ids, do_sample=True, temperature=0.6, top_p=0.95, top_k=20, max_new_tokens=1500)
        new = g[0, ids.shape[1]:].tolist()
        cut = new.index(END) + 1 if END in new else 0
        notes = tok.decode(new[:cut], skip_special_tokens=True).strip()
        ans = tok.decode(new[cut:], skip_special_tokens=True).strip()
        out["runs"][name].append({"seed": seed, "notes_tokens": cut, "notes": notes, "answer": ans})
        print(name, seed, cut, "|", ans[:500].replace("\n", " "), "\n", flush=True)
        json.dump(out, open("reason-skill-Qwen3-1.7B.json", "w"), indent=1, ensure_ascii=False)

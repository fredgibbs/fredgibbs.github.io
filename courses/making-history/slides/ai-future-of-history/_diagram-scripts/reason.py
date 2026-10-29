"""A reasoning model's notes and answer, for the AI deck.

usage: reason.py [MODEL_ID]
Runs each prompt in thinking mode with Qwen's recommended sampling settings
and a fixed seed, and saves the notes (inside <think>) and the answer
separately, with their token counts.
"""
import sys, json, time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = sys.argv[1] if len(sys.argv) > 1 else "Qwen/Qwen3-1.7B"
device = "mps" if torch.backends.mps.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16).to(device)
model.eval()

PROMPTS = {
    "zimmerman": "When was Zimmerman Library at the University of New Mexico built?",
    "strawberry": 'How many r\'s are in the word "strawberry"?',
}
SETTINGS = dict(do_sample=True, temperature=0.6, top_p=0.95, top_k=20, max_new_tokens=1500)
END_THINK = tok.convert_tokens_to_ids("</think>")

out = {"model": model_id, "seed": 1105, "settings": SETTINGS, "runs": {}}
for key, prompt in PROMPTS.items():
    text = tok.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False,
                                   add_generation_prompt=True, enable_thinking=True)
    ids = tok(text, return_tensors="pt").input_ids.to(device)
    torch.manual_seed(1105)
    t0 = time.time()
    with torch.no_grad():
        g = model.generate(ids, **SETTINGS)
    new = g[0, ids.shape[1]:].tolist()
    cut = new.index(END_THINK) + 1 if END_THINK in new else 0
    notes = tok.decode(new[:cut], skip_special_tokens=True).replace("<think>", "").replace("</think>", "").strip()
    answer = tok.decode(new[cut:], skip_special_tokens=True).strip()
    out["runs"][key] = {"prompt": prompt, "notes": notes, "answer": answer,
                        "notes_tokens": cut, "answer_tokens": len(new) - cut,
                        "seconds": round(time.time() - t0, 1)}
    print(f"== {key}: {cut} note tokens, {len(new) - cut} answer tokens, {time.time() - t0:.0f}s")
    print(notes[:1500], "\n--- ANSWER ---\n", answer[:800], "\n")

with open(f"reason-{model_id.split('/')[-1]}.json", "w") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)

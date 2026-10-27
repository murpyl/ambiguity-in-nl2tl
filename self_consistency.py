import csv
import json
import os
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import matplotlib.pyplot as plt
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm

MODEL = "anthropic/claude-haiku-5.5"
MAX_K = 10
TEMPERATURE = 1.0
WORKERS = 16

DATASET_PATH = Path("expert_LTL_dataset.txt")
TAG = MODEL.replace("/", "_")
RAW_SAMPLES_PATH = Path(f"raw_samples_{TAG}.json")
PER_EXAMPLE_CSV = Path(f"per_example_results_{TAG}.csv")
ACCURACY_CSV = Path(f"accuracy_vs_k_{TAG}.csv")
ACCURACY_PNG = Path(f"accuracy_vs_k_{TAG}.png")

SYSTEM_PROMPT = (
    "You translate a natural language description of a temporal property into a "
    "Linear Temporal Logic (LTL) formula. Use atomic propositions exactly as named "
    "in the sentence (e.g. a, b, c, d, e) and standard LTL operators: G, F, X, U, R, "
    "!, &&, ||, ->, <->.\n\n"
    "Think step by step before answering:\n"
    "1. Identify the atomic propositions involved.\n"
    "2. Restate the sentence's logical structure in plain terms (what triggers what, "
    "over what time scope: always, eventually, next, until, etc.).\n"
    "3. Build the formula piece by piece from that structure.\n"
    "4. Sanity-check the formula against the sentence once more.\n\n"
    "Show this reasoning, then end your response with a final line in EXACTLY this "
    "format (nothing after it):\n"
    "FORMULA: <the LTL formula>"
)

FORMULA_MARKER = "FORMULA:"


def extract_formula(raw_response: str) -> str:
    idx = raw_response.rfind(FORMULA_MARKER)
    if idx != -1:
        tail = raw_response[idx + len(FORMULA_MARKER):].strip()
        formula = tail.splitlines()[0].strip() if tail else tail
    else:
        lines = [ln.strip() for ln in raw_response.strip().splitlines() if ln.strip()]
        formula = lines[-1] if lines else raw_response.strip()
    return formula.strip("`* ").strip()


def load_dataset(path: Path):
    examples = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            nl, ltl = line.rstrip("\n").split(";", 1)
            examples.append({"nl": nl.strip(), "ltl": ltl.strip()})
    return examples


def normalize(formula: str) -> str:
    f = formula.strip().strip("`")
    f = f.replace("&&", "&").replace("||", "|")
    return "".join(f.split())


def get_client() -> OpenAI:
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not set (add it to a .env file)")
    return OpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1", max_retries=3)


def sample_one(client: OpenAI, nl: str) -> dict:
    """Returns {"reasoning": full CoT response, "formula": extracted final formula}."""
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=TEMPERATURE,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": nl},
        ],
    )
    raw = (resp.choices[0].message.content or "").strip()
    return {"reasoning": raw, "formula": extract_formula(raw)}


def save_cache(cache):
    RAW_SAMPLES_PATH.write_text(json.dumps(cache, indent=2), encoding="utf-8")


def collect_raw_samples(client: OpenAI, examples):
    """Resumable. Failed calls are not cached, so rerunning fills the gaps."""
    cache = (
        json.loads(RAW_SAMPLES_PATH.read_text(encoding="utf-8"))
        if RAW_SAMPLES_PATH.exists()
        else {}
    )

    jobs = []  
    for idx, ex in enumerate(examples):
        entry = cache.setdefault(str(idx), {"nl": ex["nl"], "ltl": ex["ltl"], "samples": []})
        jobs += [(str(idx), ex["nl"])] * (MAX_K - len(entry["samples"]))

    with ThreadPoolExecutor(WORKERS) as pool:
        futures = [(key, pool.submit(sample_one, client, nl)) for key, nl in jobs]
        for n, (key, fut) in enumerate(tqdm(futures, desc="samples")):
            try:
                cache[key]["samples"].append(fut.result())
            except Exception as e:
                tqdm.write(f"failed example {key}: {e}")
            if n % 50 == 49:
                save_cache(cache)

    save_cache(cache)
    return cache


def majority_vote(formulas):
    return Counter(normalize(f) for f in formulas).most_common(1)[0][0]


def evaluate(cache):
    rows = []
    correct_by_k = {k: [] for k in range(1, MAX_K + 1)}

    complete = {k: e for k, e in cache.items() if len(e["samples"]) >= MAX_K}
    if len(complete) < len(cache):
        print(f"Skipping {len(cache) - len(complete)} examples with < {MAX_K} samples (rerun to fill).")

    for key, entry in complete.items():
        gt = normalize(entry["ltl"])
        formulas = [s["formula"] for s in entry["samples"][:MAX_K]]
        for k in range(1, MAX_K + 1):
            vote = majority_vote(formulas[:k])
            correct = int(vote == gt)
            correct_by_k[k].append(correct)
            rows.append(
                {
                    "example_idx": key,
                    "nl": entry["nl"],
                    "ground_truth": entry["ltl"],
                    "k": k,
                    "majority_vote": vote,
                    "correct": correct,
                }
            )

    with open(PER_EXAMPLE_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    summary = [{"k": k, "accuracy": sum(v) / len(v)} for k, v in correct_by_k.items()]

    with open(ACCURACY_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["k", "accuracy"])
        writer.writeheader()
        writer.writerows(summary)

    return summary


def plot_accuracy(summary):
    ks = [r["k"] for r in summary]
    accs = [r["accuracy"] for r in summary]

    plt.figure(figsize=(7, 5))
    plt.plot(ks, accs, marker="o")
    plt.xlabel("k (number of self-consistency samples)")
    plt.ylabel("Translation accuracy (exact match)")
    plt.title(f"NL->LTL Self-Consistency Accuracy vs k ({MODEL})")
    plt.xticks(ks)
    plt.ylim(0, 1)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(ACCURACY_PNG, dpi=150)


def main():
    examples = load_dataset(DATASET_PATH)
    cache = collect_raw_samples(get_client(), examples)
    summary = evaluate(cache)
    plot_accuracy(summary)

    print("\nk\taccuracy")
    for row in summary:
        print(f"{row['k']}\t{row['accuracy']:.3f}")


if __name__ == "__main__":
    main()
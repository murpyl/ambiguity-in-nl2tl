import csv
import json
import os
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import matplotlib.pyplot as plt
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm


# -------------------- Configuration --------------------

MODEL = "google/gemini-3.8-flash"
MAX_K = 10
TEMPERATURE = 1.0
WORKERS = 16

# Dataset lines must use: natural-language description;STL formula
DATASET_PATH = Path("stl_sample_dataset.txt")

TAG = MODEL.replace("/", "_")
#TAG = "deepseek-flash"
RAW_SAMPLES_PATH = Path(f"raw_samples_stl_{TAG}.json")
PER_EXAMPLE_CSV = Path(f"per_example_results_stl_{TAG}.csv")
ACCURACY_CSV = Path(f"accuracy_vs_k_stl_{TAG}.csv")
ACCURACY_PNG = Path(f"accuracy_vs_k_stl_{TAG}.png")

SYSTEM_PROMPT = (
    "Translate a natural-language description of a temporal property into a "
    "Signal Temporal Logic (STL) formula. Preserve atomic proposition names "
    "exactly as written in the description (for example, prop_1, a, or b). "
    "Use the symbolic operator notation and interval style used in the dataset:\n"
    "- G: globally / always\n"
    "- F: eventually\n"
    "- U: until, where applicable\n"
    "- !: negation\n"
    "- &&: conjunction\n"
    "- ||: disjunction\n"
    "- ->: implication\n"
    "- <->: equivalence\n"
    "- Bounded temporal operators use intervals such as G [6,93] prop_1 or "
    "F [6,93] prop_1.\n\n"
    "Translate the meaning of the natural-language description faithfully. "
    "Do not invent time bounds or atomic propositions. If a time interval is "
    "specified, preserve its endpoints. Use parentheses where needed to make "
    "operator scope unambiguous. The dataset may contain STL formulas that "
    "use temporal operators without explicit bounds; follow the description "
    "rather than adding bounds.\n\n"
    "Briefly state the key interpretation, then end with a final line in "
    "EXACTLY this format (nothing after it):\n"
    "FORMULA: <the STL formula>"
)

FORMULA_MARKER = "FORMULA:"


def extract_formula(raw_response: str) -> str:
    """Extract the formula following the final FORMULA: marker."""
    idx = raw_response.rfind(FORMULA_MARKER)
    if idx != -1:
        tail = raw_response[idx + len(FORMULA_MARKER):].strip()
        formula = tail.splitlines()[0].strip() if tail else ""
    else:
        lines = [line.strip() for line in raw_response.strip().splitlines() if line.strip()]
        formula = lines[-1] if lines else ""
    return formula.strip("`* ").strip()


def load_dataset(path: Path):
    """Read one `NL;STL` pair per line."""
    examples = []
    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            if ";" not in line:
                raise ValueError(
                    f"{path}:{line_number}: expected 'natural language;STL formula'"
                )
            nl, stl = line.split(";", 1)
            if not nl.strip() or not stl.strip():
                raise ValueError(f"{path}:{line_number}: empty NL or STL formula")
            examples.append({"nl": nl.strip(), "stl": stl.strip()})
    if not examples:
        raise ValueError(f"No examples found in {path}")
    return examples


def normalize(formula: str) -> str:
    """
    Conservative exact-match normalization:
    - standardize common conjunction/disjunction spellings;
    - remove whitespace.
    This does not test semantic equivalence between STL formulas.
    """
    formula = formula.strip().strip("`")
    formula = formula.replace("&&", "&").replace("||", "|")
    return "".join(formula.split())


def get_client() -> OpenAI:
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not set (add it to a .env file)")
    return OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        max_retries=3,
    )
    #DEEPSEEK
    # api_key = os.environ.get("DEEPSEEK_API_KEY")
    # if not api_key:
    #     raise RuntimeError("DEEPSEEK_API_KEY not set (add it to a .env file)")
    # return OpenAI(
    #     api_key=api_key,
    #     base_url="https://api.deepseek.com",
    #     max_retries=3,
    # )
    # api_key = os.environ.get("OPENAI_API_KEY")
    # if not api_key:
    #     raise RuntimeError("OPENAI_API_KEY not set (add it to a .env file)")
    # return OpenAI(
    #     api_key=api_key,
    #     max_retries=3,
    # )

def sample_one(client: OpenAI, nl: str) -> dict:
    """Return the model response and the extracted STL formula."""
    response = client.chat.completions.create(
        model=MODEL,
        temperature=TEMPERATURE,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": nl},
        ],
    )
    raw = (response.choices[0].message.content or "").strip()
    formula = extract_formula(raw)
    if not formula:
        raise ValueError("Model response did not contain an extractable STL formula")
    return {"reasoning": raw, "formula": formula}


def save_cache(cache):
    """Write cache via a temporary file to reduce risk of partial JSON files."""
    temporary_path = RAW_SAMPLES_PATH.with_suffix(RAW_SAMPLES_PATH.suffix + ".tmp")
    temporary_path.write_text(json.dumps(cache, indent=2), encoding="utf-8")
    temporary_path.replace(RAW_SAMPLES_PATH)


def collect_raw_samples(client: OpenAI, examples):
    """Resume from cache; failed API calls are not added as samples."""
    if RAW_SAMPLES_PATH.exists():
        cache = json.loads(RAW_SAMPLES_PATH.read_text(encoding="utf-8"))
    else:
        cache = {}

    jobs = []
    for idx, example in enumerate(examples):
        key = str(idx)
        entry = cache.setdefault(
            key,
            {"nl": example["nl"], "stl": example["stl"], "samples": []},
        )

        # Avoid accidentally reusing a cache created for a different dataset.
        if entry.get("nl") != example["nl"] or entry.get("stl") != example["stl"]:
            raise ValueError(
                f"Cache mismatch at example index {idx}. "
                f"Move or delete {RAW_SAMPLES_PATH} before starting a different dataset."
            )

        # Trim excess samples if MAX_K was lowered.
        entry["samples"] = entry.get("samples", [])[:MAX_K]
        jobs.extend([(key, example["nl"]) for _ in range(MAX_K - len(entry["samples"]))])

    if not jobs:
        print(f"All examples already have {MAX_K} cached samples.")
        return cache

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [(key, pool.submit(sample_one, client, nl)) for key, nl in jobs]
        for n, (key, future) in enumerate(tqdm(futures, desc="STL samples"), start=1):
            try:
                cache[key]["samples"].append(future.result())
            except Exception as exc:
                tqdm.write(f"Failed example {key}: {exc}")
            if n % 20 == 0:
                save_cache(cache)

    save_cache(cache)
    return cache


def majority_vote(formulas):
    if not formulas:
        raise ValueError("Cannot vote on an empty list of formulas")
    counts = Counter(normalize(formula) for formula in formulas if formula.strip())
    if not counts:
        raise ValueError("No non-empty formulas available for majority vote")
    return counts.most_common(1)[0][0]


def evaluate(cache):
    rows = []
    correct_by_k = {k: [] for k in range(1, MAX_K + 1)}

    complete = {
        key: entry
        for key, entry in cache.items()
        if len(entry.get("samples", [])) >= MAX_K
    }
    if len(complete) < len(cache):
        print(
            f"Skipping {len(cache) - len(complete)} examples with fewer than "
            f"{MAX_K} successful samples; rerun to fill missing samples."
        )
    if not complete:
        raise RuntimeError(
            f"No examples have {MAX_K} samples. Check API errors and rerun."
        )

    for key, entry in sorted(complete.items(), key=lambda item: int(item[0])):
        ground_truth = normalize(entry["stl"])
        formulas = [sample["formula"] for sample in entry["samples"][:MAX_K]]

        for k in range(1, MAX_K + 1):
            vote = majority_vote(formulas[:k])
            correct = int(vote == ground_truth)
            correct_by_k[k].append(correct)
            rows.append(
                {
                    "example_idx": key,
                    "nl": entry["nl"],
                    "ground_truth_stl": entry["stl"],
                    "k": k,
                    "majority_vote_stl": vote,
                    "correct_exact_match": correct,
                }
            )

    with PER_EXAMPLE_CSV.open("w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "example_idx",
            "nl",
            "ground_truth_stl",
            "k",
            "majority_vote_stl",
            "correct_exact_match",
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    summary = [
        {
            "k": k,
            "accuracy": sum(values) / len(values) if values else 0.0,
            "n_examples": len(values),
        }
        for k, values in correct_by_k.items()
    ]

    with ACCURACY_CSV.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["k", "accuracy", "n_examples"]
        )
        writer.writeheader()
        writer.writerows(summary)

    return summary


def plot_accuracy(summary):
    ks = [row["k"] for row in summary]
    accuracies = [row["accuracy"] for row in summary]

    plt.figure(figsize=(7, 5))
    plt.plot(ks, accuracies, marker="o")
    plt.xlabel("k (number of self-consistency samples)")
    plt.ylabel("STL translation accuracy (exact match)")
    plt.title(f"NL-to-STL Self-Consistency Accuracy vs k ({MODEL})")
    plt.xticks(ks)
    plt.ylim(0, 1)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(ACCURACY_PNG, dpi=150)
    plt.close()


def main():
    examples = load_dataset(DATASET_PATH)
    print(f"Loaded {len(examples)} NL-STL examples from {DATASET_PATH}")
    cache = collect_raw_samples(get_client(), examples)
    summary = evaluate(cache)
    plot_accuracy(summary)

    print("\nk\taccuracy\tn_examples")
    for row in summary:
        print(f"{row['k']}\t{row['accuracy']:.3f}\t{row['n_examples']}")


if __name__ == "__main__":
    main()

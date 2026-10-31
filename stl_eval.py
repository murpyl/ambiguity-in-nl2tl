"""Parsing and semantic voting for the repository's Boolean interval logic."""

from collections import Counter
import re

import stl
from stl_equiv import semantically_equivalent

SYMBOLS = {"¬": "!", "∧": "&&", "∨": "||", "→": "->", "↔": "<->"}


def clean(sample):
    if isinstance(sample, dict):
        raw = sample.get("reasoning")
        if raw is not None and "FORMULA:" not in raw:
            return None
        sample = sample.get("corrected_formula") or sample.get("formula")
    if not sample:
        return None
    sample = re.sub(r"^\s*(?:(?:FINAL|STL)\s*:\s*)+", "", sample, flags=re.I)
    for old, new in SYMBOLS.items():
        sample = sample.replace(old, new)
    return sample.strip() or None


def parse(formula):
    if not formula:
        return None
    try:
        return stl.parse(formula)
    except stl.ParseError:
        return None


def cluster(formulas):
    representatives, labels = [], []
    for formula in formulas:
        ast = parse(formula)
        if ast is None:
            labels.append(None)
            continue
        for index, (representative, rep_ast) in enumerate(representatives):
            verdict = True if ast == rep_ast else semantically_equivalent(formula, representative)[0]
            if verdict is None:
                raise ValueError(f"STL equivalence undecided: {formula!r} versus {representative!r}")
            if verdict:
                labels.append(index)
                break
        else:
            labels.append(len(representatives))
            representatives.append((formula, ast))
    return labels, representatives


def majority(formulas):
    labels, representatives = cluster(formulas)
    counts = Counter(label for label in labels if label is not None)
    if not counts:
        return None, 0
    winner = max(counts, key=lambda label: (counts[label], -label))
    return representatives[winner][0], sum(label is not None for label in labels)

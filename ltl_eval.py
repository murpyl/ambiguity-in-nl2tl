"""One parsing and semantic-clustering path for LTL experiments."""

from collections import Counter

import spot

from ltl import ParseError
from ltl_equiv import to_spot

SYMBOLS = {"¬": "!", "∧": "&&", "∨": "||", "→": "->", "↔": "<->"}


def clean(sample):
    if isinstance(sample, dict):
        raw = sample.get("reasoning")
        if raw is not None and "FORMULA:" not in raw:
            return None
        sample = sample.get("corrected_formula") or sample.get("formula")
    if not sample:
        return None
    for old, new in SYMBOLS.items():
        sample = sample.replace(old, new)
    return sample.strip() or None


def parse(formula):
    if not formula:
        return None
    try:
        return to_spot(formula)
    except ParseError:
        return None


def cluster(formulas):
    """Return labels and representatives; invalid formulas have label None."""
    representatives, labels = [], []
    for formula in formulas:
        parsed = parse(formula)
        if parsed is None:
            labels.append(None)
            continue
        for index, representative in enumerate(representatives):
            if spot.are_equivalent(parsed, representative[1]):
                labels.append(index)
                break
        else:
            labels.append(len(representatives))
            representatives.append((formula, parsed))
    return labels, representatives


def majority(formulas):
    labels, representatives = cluster(formulas)
    counts = Counter(label for label in labels if label is not None)
    if not counts:
        return None, 0
    winner = max(counts, key=lambda label: (counts[label], -label))
    return representatives[winner][0], sum(label is not None for label in labels)

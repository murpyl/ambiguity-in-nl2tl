"""Exact LTL equivalence via spot. Formulas are parsed with ltl.py (the
dataset's syntax and precedence), then handed to spot fully parenthesized."""

import spot

from ltl import ParseError, parse

_OPS = {"and": "&", "or": "|", "imply": "->", "iff": "<->",
        "U": "U", "R": "R", "W": "W", "M": "M"}


def _emit(n):
    tag = n[0]
    if tag == "atom":
        return f'"{n[1]}"'  # quoted: atoms like `true` must not become constants
    if tag == "not":
        return f"!{_emit(n[1])}"
    if tag in ("X", "F", "G"):
        return f"{tag}({_emit(n[1])})"
    return f"({_emit(n[1])} {_OPS[tag]} {_emit(n[2])})"


def to_spot(s: str) -> spot.formula:
    """Raises ParseError on invalid input."""
    try:
        return spot.formula(_emit(parse(s)))
    except RuntimeError as e:
        raise ParseError(str(e)) from e


def semantically_equivalent(formula_a: str, formula_b: str):
    """(True, None) if equivalent, (False, counterexample) if not,
    (None, message) on parse error."""
    try:
        a, b = to_spot(formula_a), to_spot(formula_b)
    except ParseError as e:
        return None, f"parse error: {e}"
    word = spot.translate(spot.formula.Xor(a, b)).accepting_word()
    return (True, None) if word is None else (False, f"disagree on trace {word}")
import z3

from stl import ParseError, encode, parse

TIMEOUT_MS = 5000


def semantically_equivalent(a: str, b: str):
    """(True|False|None, reason). None = parse error or Z3 could not decide."""
    try:
        fa, fb = parse(a), parse(b)
    except ParseError as e:
        return None, f"parse error: {e}"
    if fa == fb:
        return True, None
    preds = {}
    solver = z3.Solver()
    solver.set(timeout=TIMEOUT_MS)
    zero = z3.IntVal(0)
    solver.add(z3.Not(encode(fa, zero, preds) == encode(fb, zero, preds)))
    result = solver.check()
    if result == z3.unsat:
        return True, None
    if result == z3.sat:
        return False, "z3 found a distinguishing trace"
    return None, f"z3 unknown: {solver.reason_unknown()}"
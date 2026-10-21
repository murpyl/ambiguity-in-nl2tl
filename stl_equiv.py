import itertools
import random

import numpy as np

from stl import ParseError, atoms, intervals, parse, sat

RANDOM_TRIALS = 300
MAX_PROBE_TIMES = 40


def _probe_times(ivs):
    bounds = sorted({b for iv in ivs for b in iv if b is not None})
    base = set(bounds) | {0, 1, 2}
    base |= {s for x, y in itertools.combinations_with_replacement(bounds, 2) for s in (x + y,)}
    return sorted({t + d for t in base for d in (-1, 0, 1) if t + d >= 0})


def _traces(props, ivs, rng):
    """Yield dict atom -> bool array, all of the same length."""
    times = _probe_times(ivs)
    horizon = 2 * sum(b for iv in ivs for b in iv if b is not None) + 2
    length = max(times, default=0) + 3
    m = length + horizon

    def make(fn):
        return {p: fn(p) for p in props}

    def const(v):
        return np.full(m, v)

    yield make(lambda p: const(False))
    yield make(lambda p: const(True))
    probe = times if len(times) <= MAX_PROBE_TIMES else sorted(rng.sample(times, MAX_PROBE_TIMES))
    for p in props:
        for t in probe:
            for base in (False, True):  # a single spike (or dip) at t, others constant
                for other in (False, True):
                    sig = {q: const(other) for q in props}
                    sig[p] = const(base)
                    sig[p][t] = not base
                    yield sig
        for t in probe:  # step change at t
            for before in (False, True):
                sig = {q: const(False) for q in props}
                sig[p] = np.arange(m) < t
                sig[p] = sig[p] if before else ~sig[p]
                yield sig
    for _ in range(RANDOM_TRIALS):  # random piecewise-constant, change points near bounds
        def rand_sig(_p):
            cuts = sorted(rng.choice(times + list(range(6))) for _ in range(rng.randint(0, 6)))
            v, out, prev = rng.random() < 0.5, np.zeros(m, dtype=bool), 0
            for c in cuts + [m]:
                out[prev:c] = v
                v, prev = not v, c
            return out
        yield make(rand_sig)


def semantically_equivalent(a: str, b: str, seed: int = 0):
    """(True|False|None, reason). None = a formula failed to parse."""
    try:
        ast_a, ast_b = parse(a), parse(b)
    except ParseError as e:
        return None, f"parse error: {e}"
    props = sorted(atoms(ast_a) | atoms(ast_b))
    ivs = intervals(ast_a) + intervals(ast_b)
    for sig in _traces(props, ivs, random.Random(seed)):
        if sat(ast_a, sig)[0] != sat(ast_b, sig)[0]:
            return False, "disagree on a probe trace"
    return True, None
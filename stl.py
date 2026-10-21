import re
import numpy as np

TOKEN_RE = re.compile(r"""
    (?P<IFF><->) | (?P<IMPLY>->) | (?P<AND>&&|&) | (?P<OR>\|\||\|) | (?P<NOT>!)
  | (?P<LPAREN>\() | (?P<RPAREN>\))
  | (?P<IV>\[\s*(?P<lo>\d+)\s*,\s*(?P<hi>\d+|inf|∞)\s*\])
  | (?P<OP>[GFU]) | (?P<IDENT>[a-z_][a-zA-Z_0-9]*) | (?P<WS>\s+)
""", re.VERBOSE)


class ParseError(ValueError):
    pass


def tokenize(s):
    tokens, pos = [], 0
    while pos < len(s):
        m = TOKEN_RE.match(s, pos)
        if not m:
            raise ParseError(f"unexpected character at {pos}: {s[pos:pos + 10]!r}")
        if m.lastgroup == "IV":
            hi = m.group("hi")
            iv = (int(m.group("lo")), None if hi in ("inf", "∞") else int(hi))
            if iv[1] is not None and iv[1] < iv[0]:
                raise ParseError(f"empty interval {m.group()}")
            tokens.append(("IV", iv))
        elif m.lastgroup != "WS":
            tokens.append((m.lastgroup, m.group()))
        pos = m.end()
    tokens.append(("EOF", ""))
    return tokens


class _Parser:
    def __init__(self, tokens):
        self.t, self.i = tokens, 0

    def peek(self):
        return self.t[self.i]

    def next(self):
        self.i += 1
        return self.t[self.i - 1]

    def interval(self):
        return self.next()[1] if self.peek()[0] == "IV" else (0, None)

    def parse(self):
        node = self.iff()
        if self.peek()[0] != "EOF":
            raise ParseError(f"trailing tokens: {self.t[self.i:-1]}")
        return node

    def iff(self):
        left = self.imply()
        while self.peek()[0] == "IFF":
            self.next()
            left = ("iff", left, self.imply())
        return left

    def imply(self):
        left = self.or_()
        if self.peek()[0] == "IMPLY":
            self.next()
            return ("imply", left, self.imply())
        return left

    def or_(self):
        left = self.and_()
        while self.peek()[0] == "OR":
            self.next()
            left = ("or", left, self.and_())
        return left

    def and_(self):
        left = self.until()
        while self.peek()[0] == "AND":
            self.next()
            left = ("and", left, self.until())
        return left

    def until(self):
        left = self.unary()
        if self.peek() == ("OP", "U"):
            self.next()
            iv = self.interval()
            return ("U", iv, left, self.until())
        return left

    def unary(self):
        kind, val = self.next()
        if kind == "NOT":
            return ("not", self.unary())
        if kind == "OP" and val in "GF":
            iv = self.interval()
            return (val, iv, self.unary())
        if kind == "IDENT":
            return ("atom", val)
        if kind == "LPAREN":
            node = self.iff()
            if self.next()[0] != "RPAREN":
                raise ParseError("expected ')'")
            return node
        raise ParseError(f"unexpected token {kind} {val!r}")


def parse(s):
    return _Parser(tokenize(s)).parse()


def _children(n):
    return [c for c in n[1:] if isinstance(c, tuple) and not (len(c) == 2 and isinstance(c[0], int))]


def atoms(n):
    return {n[1]} if n[0] == "atom" else set().union(*(atoms(c) for c in _children(n)))


def intervals(n):
    """All (lo, hi) intervals in the AST."""
    own = [n[1]] if n[0] in ("F", "G", "U") else []
    return own + [iv for c in _children(n) for iv in intervals(c)]


def strip_intervals(n):
    """Same formula with every interval replaced by [0, inf)."""
    if n[0] == "atom":
        return n
    if n[0] in ("F", "G", "U"):
        return (n[0], (0, None), *map(strip_intervals, n[2:]))
    return (n[0], *map(strip_intervals, n[1:]))


def to_str(n):
    t = n[0]
    if t == "atom":
        return n[1]
    if t == "not":
        return f"! {to_str(n[1])}"
    if t in ("F", "G"):
        return f"({t} [{n[1][0]},{n[1][1] if n[1][1] is not None else 'inf'}] {to_str(n[2])})"
    if t == "U":
        return f"({to_str(n[2])} U [{n[1][0]},{n[1][1] if n[1][1] is not None else 'inf'}] {to_str(n[3])})"
    op = {"and": "&&", "or": "||", "imply": "->", "iff": "<->"}[t]
    return f"({to_str(n[1])} {op} {to_str(n[2])})"


def _next_true(a):
    """For each i, smallest j >= i with a[j] true (len(a) if none)."""
    m = len(a)
    return np.minimum.accumulate(np.where(a, np.arange(m), m)[::-1])[::-1]


def _window_any(a, lo, hi):
    """any(a[i+lo .. i+hi]) per i; indices clip to the last position (its value repeats)."""
    m = len(a)
    c = np.concatenate(([0], np.cumsum(a)))
    i = np.arange(m)
    start = np.minimum(i + lo, m - 1)
    end = np.full(m, m - 1) if hi is None else np.minimum(i + hi, m - 1)
    return c[end + 1] - c[start] > 0


def sat(n, sig):
    """Truth value of n at every position; sig maps atom -> bool array (all same length)."""
    t = n[0]
    if t == "atom":
        return sig[n[1]]
    if t == "not":
        return ~sat(n[1], sig)
    if t == "F":
        return _window_any(sat(n[2], sig), *n[1])
    if t == "G":
        return ~_window_any(~sat(n[2], sig), *n[1])
    a, b = sat(n[-2], sig), sat(n[-1], sig)
    if t == "and":
        return a & b
    if t == "or":
        return a | b
    if t == "imply":
        return ~a | b
    if t == "iff":
        return a == b
    if t == "U":  # exists j in i+[lo,hi]: b[j] and a on [i, j)
        lo, hi = n[1]
        m = len(a)
        i = np.arange(m)
        j = _next_true(b)[np.minimum(i + lo, m - 1)]  # earliest b-witness in the window
        first_not_a = _next_true(~a)[i]
        return (j < m) & (True if hi is None else j <= i + hi) & (first_not_a >= j)
    raise ValueError(f"unknown node {n}")
"""LTL parser for the dataset's syntax (spot's lexer can't read e.g. `XXX b` or `GFd`).

Syntax: atoms (lowercase identifiers), ! && & || | -> <-> and the temporal
operators X F G (unary; X also as X^n for n nested X) and U R W M (binary). Precedence, tightest first:
unary (! X F G), temporal binary (U R W M, right-assoc), &, |, ->
(right-assoc), <-> .  Formulas are tuple ASTs, e.g. ("U", ("atom", "a"), ...).

"""

import re

TOKEN_RE = re.compile(r"""
    (?P<IFF><->) | (?P<IMPLY>->) | (?P<AND>&&|&) | (?P<OR>\|\||\|) | (?P<NOT>!)
  | (?P<LPAREN>\() | (?P<RPAREN>\)) | (?P<CARET>\^) | (?P<NUM>\d+) | (?P<OP>[GFXURWM])
  | (?P<IDENT>[a-z_][a-zA-Z_0-9]*) | (?P<WS>\s+)
""", re.VERBOSE)

BINARY_TEMPORAL = ("U", "R", "W", "M")


class ParseError(ValueError):
    pass


def tokenize(s):
    tokens, pos = [], 0
    while pos < len(s):
        m = TOKEN_RE.match(s, pos)
        if not m:
            raise ParseError(f"unexpected character at {pos}: {s[pos:pos + 10]!r}")
        if m.lastgroup != "WS":
            tokens.append((m.lastgroup, m.group()))
        pos = m.end()
    tokens.append(("EOF", ""))
    return tokens


class _Parser:
    def __init__(self, tokens):
        self.tokens, self.i = tokens, 0

    def peek(self):
        return self.tokens[self.i]

    def advance(self):
        tok = self.tokens[self.i]
        self.i += 1
        return tok

    def parse(self):
        node = self.iff()
        if self.peek()[0] != "EOF":
            raise ParseError(f"trailing tokens: {self.tokens[self.i:-1]}")
        return node

    def iff(self):
        left = self.implication()
        while self.peek()[0] == "IFF":
            self.advance()
            left = ("iff", left, self.implication())
        return left

    def implication(self):
        left = self.or_expr()
        if self.peek()[0] == "IMPLY":
            self.advance()
            return ("imply", left, self.implication())
        return left

    def or_expr(self):
        left = self.and_expr()
        while self.peek()[0] == "OR":
            self.advance()
            left = ("or", left, self.and_expr())
        return left

    def and_expr(self):
        left = self.temporal()
        while self.peek()[0] == "AND":
            self.advance()
            left = ("and", left, self.temporal())
        return left

    def temporal(self):
        left = self.unary()
        kind, val = self.peek()
        if kind == "OP" and val in BINARY_TEMPORAL:
            self.advance()
            return (val, left, self.temporal())
        return left

    def unary(self):
        kind, val = self.peek()
        if kind == "NOT":
            self.advance()
            return ("not", self.unary())
        if kind == "OP" and val in ("X", "F", "G"):
            self.advance()
            reps = 1
            if val == "X" and self.peek()[0] == "CARET":
                self.advance()
                kind, num = self.advance()
                if kind != "NUM":
                    raise ParseError("expected a number after '^'")
                reps = int(num)
            node = self.unary()
            for _ in range(reps):
                node = (val, node)
            return node
        return self.atom()

    def atom(self):
        kind, val = self.advance()
        if kind == "IDENT":
            return ("atom", val)
        if kind == "LPAREN":
            node = self.iff()
            if self.advance()[0] != "RPAREN":
                raise ParseError("expected ')'")
            return node
        raise ParseError(f"unexpected token {kind} {val!r}")


def parse(formula_str):
    """Formula string -> tuple AST. Raises ParseError on invalid input."""
    return _Parser(tokenize(formula_str)).parse()
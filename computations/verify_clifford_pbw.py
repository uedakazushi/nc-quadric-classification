#!/usr/bin/env python3
"""Exact critical-pair certificate for the central Clifford PBW presentation.

For any commutative coefficient ring S and central f1, f2, h, the monic rules
cc -> f1, dd -> f2, dc -> h - cd have four length-three overlaps.
Checking the polynomial critical pairs supports the general diamond argument;
this script is not a formal proof of every base-change theorem.

Run: python3 computations/verify_clifford_pbw.py
Needs SymPy >=1.12.
"""
from collections import defaultdict
import sympy as sp

f1, f2, h = sp.symbols("f1 f2 h")
rules = {"cc": {"": f1}, "dd": {"": f2}, "dc": {"": h, "cd": -1}}


def rewrite(poly, word, position):
    out = defaultdict(lambda: sp.Integer(0))
    for monomial, coeff in poly.items():
        if monomial == word:
            for replacement, multiplier in rules[word[position:position + 2]].items():
                out[word[:position] + replacement + word[position + 2:]] += coeff * multiplier
        else:
            out[monomial] += coeff
    return {w: sp.expand(v) for w, v in out.items() if sp.expand(v) != 0}


def normal_form(poly):
    current = dict(poly)
    while True:
        site = next(((w, i) for w in sorted(current) for i in range(len(w) - 1)
                     if w[i:i + 2] in rules), None)
        if site is None:
            return current
        current = rewrite(current, *site)


for word in ("ccc", "ddd", "dcc", "ddc"):
    sites = [i for i in range(len(word) - 1) if word[i:i + 2] in rules]
    assert len(sites) == 2
    first = normal_form(rewrite({word: sp.Integer(1)}, word, sites[0]))
    second = normal_form(rewrite({word: sp.Integer(1)}, word, sites[1]))
    assert first == second, (word, first, second)
    assert set(first).issubset({"", "c", "d", "cd"})
    print(f"PASS: critical overlap {word}: {first}")

print("PASS: all critical pairs resolve with monic coefficients over Z[f1,f2,h]")

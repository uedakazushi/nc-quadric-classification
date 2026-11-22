#!/usr/bin/env python3
"""Exact rational checks for the OU spectral elliptic halving construction.

Only verifies polynomial identity and one generic separating specialization.
The divisor proof and relative torsor identification are in
papers/quiver-avatar/git_comparison.tex, thm:qa-ou-spectral-kummer.

Run: python3 computations/verify_ou_spectral_halving.py
No third-party packages required.
"""
from fractions import Fraction
from itertools import combinations, product
from math import prod


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def subtract(a, b):
    return [(a[i] if i < len(a) else 0) -
            (b[i] if i < len(b) else 0) for i in range(max(len(a), len(b)))]


def point_data(x):
    s1 = sum(x)
    s2 = sum(prod(pair) for pair in combinations(x, 2))
    s3 = sum(prod(triple) for triple in combinations(x, 3))
    s4 = prod(x)
    assert s1 != 0
    # q(t)^2 - t (s1*t+s3)^2 = prod(t-x_i^2)
    q = [s4, s2, 1]
    ell = [s3, s1]
    lhs = subtract(multiply(q, q), [0] + multiply(ell, ell))
    rhs = [1]
    for z in x:
        rhs = multiply(rhs, [-z * z, 1])
    assert lhs == rhs
    t0 = Fraction(-s3, s1)
    y0 = -(t0 * t0 + s2 * t0 + s4)
    f0 = prod(t0 - z * z for z in x)
    assert y0 * y0 == f0
    return t0, y0


def main():
    x = (1, 2, 3, 5)
    points = {}
    for sign in product((-1, 1), repeat=4):
        if prod(sign) != 1 or sign[0] != 1:
            continue  # even sign vectors modulo simultaneous negation
        y = tuple(a * b for a, b in zip(x, sign))
        points[sign] = point_data(y)
        assert point_data(tuple(-a for a in y)) == points[sign]
        assert point_data(tuple(reversed(y))) == points[sign]
    assert len(points) == 4
    assert len(set(points.values())) == 4
    for sign, (t0, y0) in sorted(points.items()):
        print(f"{sign}: Q=(t={t0}, y={y0})")
    print("PASS: quartic factorization, four distinct halves, "
          "permutation and global-sign invariance (exact Q)")


if __name__ == "__main__":
    main()

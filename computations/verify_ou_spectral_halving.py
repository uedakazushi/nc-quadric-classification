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
    # Independent discriminant/j check for the diagonal intersection
    # q(u)=sum u_i^2=0 and q(Xu)=sum x_i^2 u_i^2=0.
    a = tuple(z*z for z in x)
    e1 = sum(a)
    e2 = sum(prod(c) for c in combinations(a, 2))
    e3 = sum(prod(c) for c in combinations(a, 3))
    e4 = prod(a)
    I = e2*e2 - 3*e1*e3 + 12*e4
    J = (-2*e2**3 + 9*e1*e2*e3 - 27*e3**2
         - 27*e1**2*e4 + 72*e2*e4)
    quartic_j = Fraction(1728*4*I**3, 4*I**3-J**2)
    cross = Fraction((a[0]-a[2])*(a[1]-a[3]),
                     (a[0]-a[3])*(a[1]-a[2]))
    legendre_j = 256*(1-cross+cross**2)**3/(cross**2*(1-cross)**2)
    disc = prod((a[i]-a[j])**2
                for i, j in combinations(range(4), 2))
    assert 4*I**3-J**2 == 27*disc
    assert quartic_j == legendre_j == Fraction(3796416, 1225)
    for sign, (t0, y0) in sorted(points.items()):
        print(f"{sign}: Q=(t={t0}, y={y0})")
    print("PASS: quartic factorization, four distinct halves, "
          "permutation and global-sign invariance (exact Q)")
    print(f"PASS: pencil discriminant and invariant j={quartic_j} "
          "(binary quartic = Legendre, exact Q)")


if __name__ == "__main__":
    main()

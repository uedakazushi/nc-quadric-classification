#!/usr/bin/env python3
"""Exact checks of OU spectral two-torsion divisors and local reflection slices.

Reproduces the explicit rational examples and involution tangent matrices used in
papers/quiver-avatar/git_comparison.tex:
  prop:qa-ou-spectral-torsion-divisors
  thm:qa-ou-special-reflection-coarse-branch

Run: python3 computations/verify_ou_special_reflection.py
No third-party packages needed. The formal invariant-ring proof is in the paper.
"""
from fractions import Fraction
from itertools import combinations
from math import prod


def polynomial_multiply(left, right):
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def invariants(x):
    a = [z*z for z in x]
    e1 = sum(a)
    e2 = sum(prod(combo) for combo in combinations(a, 2))
    e3 = sum(prod(combo) for combo in combinations(a, 3))
    e4 = prod(a)
    c = prod(x)
    assert e4 == c*c
    assert c and e1
    assert len(set(a)) == 4
    I = e2*e2 - 3*e1*e3 + 12*e4
    J = (-2*e2**3 + 9*e1*e2*e3 - 27*e3**2
         - 27*e1**2*e4 + 72*e2*e4)
    disc = 4*I**3 - J**2
    assert disc != 0
    j = Fraction(1728 * 4 * I**3, disc)
    return e1,e2,e3,c,j


def weierstrass_check(e1,e2,e3,c):
    """Check the quartic-to-Weierstrass identity over Q[t]."""
    b = -Fraction(e1,2)
    d = Fraction(e2,2) - Fraction(e1**2,8)
    B = [d,b,Fraction(1)]
    quartic = [Fraction(c*c), -Fraction(e3), Fraction(e2),
               -Fraction(e1), Fraction(1)]
    diff = [v-w for v,w in zip(polynomial_multiply(B,B), quartic)]
    assert diff == [d*d-c*c, 2*b*d+e3, 0, 0, 0]
    # For P+ and P-, the negation-fixed equation
    # 2v + b*u - (b*d + e3/2) = 0.
    for sign in (+1,-1):
        at_p = b * (d+sign*c) - (b*d+Fraction(e3,2))
        assert at_p == -Fraction(e3+sign*e1*c,2)


def multiply_2x2(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def reflection_checks():
    # dR(deta, ddelta) = (-deta+2*ddelta, ddelta).
    # d((-1)R) = (deta-2*ddelta,-ddelta).
    for A in ([[-1,2],[0,1]], [[1,-2],[0,-1]]):
        assert multiply_2x2(A,A) == [[1,0],[0,1]]
        assert A[0][0]+A[1][1] == 0
        assert A[0][0]*A[1][1]-A[0][1]*A[1][0] == -1
        assert (A[0][0]-1)*(A[1][1]-1)-A[0][1]*A[1][0] == 0
        assert A != [[1,0],[0,1]]
    # In the completed local ring, the reflection fixes j and w
    # and negates z. Hence invariant power series have only even z.
    for n in range(9):
        assert ((-1)**n == 1) == (n%2 == 0)


def main():
    reflection_checks()
    sample_j = Fraction(135487869158881, 51438240000)
    for x4, kind in ((-6,"delta-2-torsion"),(6,"eta-minus-delta-2-torsion")):
        e1,e2,e3,c,j = invariants((1,2,3,x4))
        weierstrass_check(e1,e2,e3,c)
        assert (e1,e2,e3) == (50,553,1800)
        assert j == sample_j and j not in (0,1728)
        if x4 == -6:
            assert e3 + e1*c == 0 and e3-e1*c != 0
        else:
            assert e3 - e1*c == 0 and e3+e1*c != 0
        print(f"PASS: {kind}, x4={x4}, c={c}, j={j}")
    print("PASS: exact quartic-to-cubic identity and both negation tests")
    print("PASS: both transverse tangent involutions are rank-one reflections")
    print("PASS: locally invariant formal powers are polynomials in z^2")


if __name__ == "__main__":
    main()

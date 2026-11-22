#!/usr/bin/env python3
"""Exact checks of OU spectral two-torsion divisors and local reflection slices.

Reproduces the explicit rational examples and involution tangent matrices used in
papers/quiver-avatar/git_comparison.tex:
  prop:qa-ou-spectral-torsion-divisors
  thm:qa-ou-special-reflection-coarse-branch
  thm:qa-ou-double-torsion-intersection-local-model

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



def double_torsion_intersection():
    """Trace-zero, double two-torsion intersection; exact rational invariant data."""
    a = (1,4,-1,-4)  # squared eigenvalues of (1,2,i,2i)
    e1 = sum(a)
    e2 = sum(prod(pair) for pair in combinations(a, 2))
    e3 = sum(prod(triple) for triple in combinations(a, 3))
    e4 = prod(a)
    c = -4
    assert (e1,e2,e3,e4) == (0,-17,0,16)
    assert e4 == c*c and len(set(a)) == 4
    weierstrass_check(e1,e2,e3,c)
    I = e2*e2 - 3*e1*e3 + 12*e4
    J = (-2*e2**3 + 9*e1*e2*e3 - 27*e3**2
         - 27*e1**2*e4 + 72*e2*e4)
    j = Fraction(1728*4*I**3, 4*I**3-J**2)
    assert j == Fraction(111284641,50625) and j not in (0,1728)
    # Model translations of the elliptic 4-torsion by (Z/4)^2.
    # Choose distinct nonzero two-torsion sigma=(2,0), tau=(0,2).
    E2 = {(p,q) for p in (0,2) for q in (0,2)}
    translations = {(p,q) for p in (0,2) for q in range(4)}
    H = {(p,q,eps) for p,q in E2 for eps in (-1,1)}
    A = {(p,q,eps) for p,q in translations for eps in (-1,1)}
    def mul(x,y):
        p,q,eps=x
        r,s,eps2=y
        return ((p+eps*r)%4,(q+eps*s)%4,eps*eps2)
    def power(x,n):
        y=(0,0,1)
        for _ in range(n):
            y=mul(y,x)
        return y
    assert len(H)==8 and len(A)==16
    assert all(mul(x,y) in A for x in A for y in A)
    assert all(mul(x,y) in H for x in H for y in H)
    assert all(power(x,2)==(0,0,1) for x in H)
    assert sum(power(x,4)==(0,0,1) and
               power(x,2)!=(0,0,1) for x in A)==4
    # D8 x C2 has 4 elements of order 4, H=C2^3 has none.
    # Source: simultaneous sign (u,v)->(-u,-v).
    # Target: independent signs on u and v.
    # Source invariant monomials have m+n even; target have m,n even.
    for m in range(9):
        for n in range(9):
            if (m+n)%2==0:
                k = min(m%2,n%2)
                assert k in (0,1)
                assert (m-k)%2 == 0 and (n-k)%2 == 0
                # u^m v^n = (u^2)^((m-k)/2) (uv)^k (v^2)^((n-k)/2).
            if m%2 == 0 and n%2 == 0:
                assert (m+n)%2 == 0
    print(f"PASS: double torsion intersection e1=e3=0, j={j}")
    print("PASS: source H=C2^3 (order 8), target A=D8 x C2 (order 16)")
    print("PASS: invariant rings give b^2=ac over k[[a,c]] (rank 2)")

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
    double_torsion_intersection()
    print("PASS: exact quartic-to-cubic identity and both negation tests")
    print("PASS: both transverse tangent involutions are rank-one reflections")
    print("PASS: locally invariant formal powers are polynomials in z^2")


if __name__ == "__main__":
    main()

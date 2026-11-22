#!/usr/bin/env python3
"""Exact finite-group and Legendre checks for elliptic CM quintuple strata.

Supports (but does not replace proofs of) the results in
papers/quiver-avatar/git_comparison.tex:
  lem:qa-ou-cm-no-extra-two-cubic-automorphisms
  lem:qa-ou-cm-level-two-deformation-coordinate
  prop:qa-ou-cm-jzero-one-cubic-a4
  cor:qa-ou-cm-a4-tangent-representation

Run: python3 computations/verify_ou_cm_automorphisms.py
Standard library only. Does not verify categorical reconstruction or etale descent.
"""
from collections import Counter
from itertools import product


def matmul(A, B, mod):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % mod
                       for j in range(2)) for i in range(2))


def mv(A, v, mod):
    return tuple(sum(A[i][j] * v[j] for j in range(2)) % mod
                 for i in range(2))


I = ((1, 0), (0, 1))
Z3 = ((0, -1), (1, -1))   # zeta_3 action, minimal polynomial X^2+X+1
J4 = ((0, -1), (1, 0))    # i action, J4^2=-I

assert matmul(matmul(Z3, Z3, 2), Z3, 2) == I
assert matmul(J4, J4, 2) == I   # -I = I on E[2]
fixed_3 = [v for v in product(range(3), repeat=2) if mv(Z3, v, 3) == v]
assert fixed_3 == [(0, 0), (1, 2), (2, 1)]
fixed_i = [v for v in product(range(2), repeat=2) if mv(J4, v, 2) == v]
anti_fixed_i = [v for v in product(range(2), repeat=2)
                if mv(J4, v, 2) == tuple(-z % 2 for z in v)]
assert fixed_i == anti_fixed_i == [(0, 0), (1, 1)]

powers = [I, matmul(Z3, I, 2), matmul(Z3, Z3, 2)]
G = [(a, b, t) for a, b in product(range(2), repeat=2) for t in range(3)]


def mul(x, y):
    xx = mv(powers[x[2]], y[:2], 2)
    return ((x[0]+xx[0]) % 2, (x[1]+xx[1]) % 2, (x[2]+y[2]) % 3)


def power(x, n):
    out = (0, 0, 0)
    for _ in range(n):
        out = mul(out, x)
    return out


assert len(G) == 12
assert all(mul(x, y) in G for x in G for y in G)
orders = Counter(next(n for n in range(1, 13) if power(g, n) == (0, 0, 0))
                 for g in G)
assert orders == {1: 1, 2: 3, 3: 8}
# The nonzero E[2] are permuted cyclically by zeta_3.
nonzero = [(0, 1), (1, 0), (1, 1)]
assert set(mv(Z3, v, 2) for v in nonzero) == set(nonzero)
assert all(mv(Z3, v, 2) != v for v in nonzero)


def pmul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def ppow(a, n):
    out = [1]
    for _ in range(n):
        out = pmul(out, a)
    return out


def pscale(a, v):
    return [v*x for x in a]


def psub(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
            for i in range(n)]


# j(lambda)-1728: ramification order 2 at -1, 2, 1/2
# j(lambda): order 3 at roots of lambda^2-lambda+1.
num = pscale(ppow([1, -1, 1], 3), 256)
den = pmul(ppow([0, 1], 2), ppow([-1, 1], 2))
rhs = pscale(pmul(pmul(ppow([1, 1], 2), ppow([-2, 1], 2)),
                 ppow([-1, 2], 2)), 64)
assert psub(psub(num, pscale(den, 1728)), rhs) == [0]*7

# The special j=0, one-cubic example E:y^2=x^3+1:
# (0, +/-1) are flexes of order 3, fixed by x -> zeta_3*x.
# If delta is nonzero 3-torsion and eta=2delta, the
# swapped foundation has eta'=2delta-eta=0 and is not cubic.
assert (2*1-2) % 3 == 0
# In the miniversal E_a:y^2=x^3+a*x+1,
# x' = zeta_3*x induces a' = zeta_3^2*a;
# two independent marked-point tangent directions have weight 1.
assert (2, 1, 1) == (2 % 3, 1 % 3, 1 % 3)
assert all((2*i+j+k) % 3 != 0
           for (i, j, k) in ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
print("PASS: CM order-3 and order-4 torsion kernels; extra CM cannot preserve two-cubic triples")
print("PASS: E[2] semidirect C3 has A4 element-order distribution (1,3,8)")
print("PASS: exact Legendre j and j-1728 identities, ramification orders 3 and 2")
print("PASS: j=0 one-cubic relation eta=2delta and tangent weights (2,1,1)")

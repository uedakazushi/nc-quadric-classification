#!/usr/bin/env python3
"""Exact OU diagonal-cover group calculation, with the correct S4 source.

OU (2014) Eq. (5.8): P3/S4 -> P3/(S4 rtimes (Z/2)^3).
Even sign vectors: E = {(x_i) in F2^4 : sum x_i=0} of size 8;
projective simultaneous -1 is trivial, so V=E/<1111> has size 4.
G_proj = V rtimes S4 has order 96, and H_coord=S4 has order 24.
H acts on V through S3, with kernel the Klein 4 double-transpositions.
The affine action on G/H has kernel Klein 4 and image S4 (size 24).
Thus the degree-4 extension has Galois closure with group S4.

Run: python3 computations/verify_ou_fourfold.py
The classical-fiber calculation uses SymPy for elimination.
"""
from itertools import combinations, permutations, product

from sympy import groebner, prod, symbols

EVEN = tuple(v for v in product((0, 1), repeat=4) if sum(v) % 2 == 0)
Z = (1, 1, 1, 1)


def quotient(v):
    """V=even F2^4/<1111>, coordinates of v0+v3, v1+v3."""
    return (v[0] ^ v[3], v[1] ^ v[3])


V = tuple(sorted(set(map(quotient, EVEN))))
assert len(EVEN) == 8 and len(V) == 4
assert quotient(Z) == (0, 0)
reps = {quotient(v): v for v in EVEN}
S4 = tuple(permutations(range(4)))


def permute(p, v):
    return tuple(v[p[i]] for i in range(4))


# Linear action S4 -> GL2(F2), order six, kernel Klein four.
L = {p: tuple(quotient(permute(p, reps[u])) for u in V) for p in S4}
lin_image = set(L.values())
lin_identity = V
assert len(lin_image) == 6
kernel = {p for p, action in L.items() if action == lin_identity}
assert kernel == {
    (0, 1, 2, 3), (1, 0, 3, 2),
    (2, 3, 0, 1), (3, 2, 1, 0)
}


def add(x, y):
    return tuple(i ^ j for i, j in zip(x, y))


# Effective projective group has order 4*24=96.
G = tuple((v, p) for v in V for p in S4)
assert len(G) == 96

# Cosets G/H identified with V; (v,p).u = v + p(u).
action = {(v, p): tuple(add(v, u) for u in L[p]) for v, p in G}
aff_image = set(action.values())
assert len(aff_image) == 24
action_identity = V
core = {(v, p) for (v, p), perm in action.items()
        if perm == action_identity}
assert core == {((0, 0), p) for p in kernel}
assert len(core) == 4
assert len(G) // len(core) == 24
assert len(G) // len(S4) == 4
assert set(perm[0] for perm in aff_image) == set(V)
# The coordinate S4 splits as Klein-four semidirect point stabilizer S3.
S3_mark = {p for p in S4 if p[3] == 3}
assert len(S3_mark) == 6
assert len(S3_mark.intersection(kernel)) == 1


def compose(p, q):
    return tuple(p[q[i]] for i in range(4))


assert {compose(k, s) for k in kernel for s in S3_mark} == set(S4)
# Hence G=(V_sign x K4_coordinate) rtimes S3_mark, with both
# two-dimensional factors carrying the standard GL2(F2) action.
assert len(V) * len(kernel) * len(S3_mark) == len(G)
print("PASS: G=(F2^2_sign x Klein4_coordinate) rtimes GL2(F2), order96")
print("PASS: OU S4 coordinate permutations, effective V=(F2)^2 sign group")
print("PASS: |Gprojective|=96; |Hcoordinate|=24; index4; core(H)=V4")
print("PASS: G/core(H)=AGL2(F2)=S4 monodromy on four sheets")

# On the slice e_1(x^2)=4 the remaining projective scaling is a sign.
# Its invariants for u=e_1(x), v=e_3(x) are A=u^2, B=uv and C=v^2.
eigenvalues = symbols("x1:5")
s1, s2, s3, s4 = (sum(prod(term) for term in combinations(eigenvalues, degree))
                  for degree in range(1, 5))
z = symbols("z")
square_polynomial = prod(1 + value**2 * z for value in eigenvalues).as_poly(z)
for degree, expected in enumerate(
    [s1**2 - 2*s2, s2**2 - 2*s1*s3 + 2*s4, s3**2 - 2*s2*s4], start=1
):
    assert (square_polynomial.nth(degree) - expected).expand() == 0

A, B, C, s = symbols("A B C s")
fiber_ideal = [A*C - B**2, A - 2*s - 4, s**2 - 2*B + 2 - 6, C - 2*s - 4]
basis = groebner(fiber_ideal, C, B, s, A, order="lex")
assert basis.polys[-1].as_expr() == (A**3 * (A - 16)).expand()
assert all(basis.reduce(p)[1] == 0 for p in [C - A, 8*B - A**2 + 8*A, 2*s - A + 4])
print("PASS: classical OU fiber has local lengths 1 and 3, with ring k[A]/(A^3(A-16))")

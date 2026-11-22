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
No third-party dependencies. This checks finite-group identities, not the
geometric equality of the OU torsor with a Picard-root torsor.
"""
from itertools import permutations, product

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
print("PASS: OU S4 coordinate permutations, effective V=(F2)^2 sign group")
print("PASS: |Gprojective|=96; |Hcoordinate|=24; index4; core(H)=V4")
print("PASS: G/core(H)=AGL2(F2)=S4 monodromy on four sheets")

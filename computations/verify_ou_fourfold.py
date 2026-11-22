#!/usr/bin/env python3
"""Exact finite-group certificate for OU's generic degree-four quotient.

Verifies:
  F_2^3 / <(1,1,1)> has dimension 2, and S3 permutes its 3 nonzero points;
  Gamma rtimes S3 acts faithfully on 4 points with order 24 (AGL_2(F2)=S4);
  the origin stabilizer has order 6, trivial normal core and index 4.
Run: python3 computations/verify_ou_fourfold.py
Pure standard Python, no symbolic or external dependency.
This does not establish any equivalence with the relative Picard root torsor.
"""
from itertools import permutations, product

F = tuple(product((0, 1), repeat=2))
O = (0, 0)


def xor(u, v):
    return (u[0] ^ v[0], u[1] ^ v[1])


def q(v):
    """Coordinates of F2^3/<(1,1,1)> using e3=e1+e2."""
    return (v[0] ^ v[2], v[1] ^ v[2])


def image_of_basis(perm):
    out = []
    for k in (0, 1):
        vector = tuple(int(perm[i] == k) for i in range(3))
        out.append(q(vector))
    return tuple(out)


linear = {image_of_basis(perm) for perm in permutations(range(3))}
assert len(linear) == 6


def lin(A, u):
    return xor(A[0] if u[0] else O, A[1] if u[1] else O)


assert all(set(lin(A, u) for u in F) == set(F) for A in linear)
assert all(set(lin(A, u) for u in F if u != O) == set(F) - {O}
           for A in linear)

affine = {
    tuple(xor(lin(A, u), b) for u in F)
    for A in linear for b in F
}
assert len(affine) == 24
assert all(len(set(perm)) == 4 for perm in affine)
origin_stabilizer = {perm for perm in affine if perm[0] == O}
assert len(origin_stabilizer) == 6
assert len(affine) // len(origin_stabilizer) == 4
# The kernel of the action of the degree-four quotient group on four cosets
# equals the core of the origin stabilizer. Faithfulness makes it trivial.
identity = tuple(F)
assert identity in affine
assert sum(perm == identity for perm in affine) == 1
assert set(perm[0] for perm in affine) == set(F)
print("PASS: OU effective sign group F2^2, S3=GL2(F2), AGL2(F2)=S4 (24)")
print("PASS: S3 stabilizer index 4 with trivial normal core; generic Galois closure S4")

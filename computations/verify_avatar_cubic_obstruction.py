#!/usr/bin/env python3
"""Exact numerical checks for the smooth cubic-foundation obstruction.

Checks the Serre square operator from both Euler matrices, primitive
alternating class and the two-torsion parity argument for candidate
adjacent line bundles. Does not verify geometric realization, lifting
of complexes, or nonexistence theorems by itself.
"""
from itertools import product

import sympy as sp

G_CUBIC = sp.Matrix([[1, 2, 4, 6], [0, 1, 2, 4],
                     [0, 0, 1, 2], [0, 0, 0, 1]])
G_SQUARE = sp.Matrix([[1, 2, 2, 4], [0, 1, 0, 2],
                      [0, 0, 1, 2], [0, 0, 0, 1]])
alternating = sp.Matrix([1, -1, -1, 1])
for gram in (G_SQUARE, G_CUBIC):
    serre = gram.inv() * gram.T
    assert (serre - sp.eye(4))**2 == (
        8 * alternating * sp.ones(1, 4)
    )
for a, b in product(range(-20, 21), repeat=2):
    powers = (b - 1, a + 1, b)
    assert (powers[0] - powers[2]) % 2 == 1
    assert ((powers[0] - powers[1]) % 2 == 0
            or (powers[1] - powers[2]) % 2 == 0)
print("PASS: Serre nilpotent square and cubic candidate 2-torsion parity")

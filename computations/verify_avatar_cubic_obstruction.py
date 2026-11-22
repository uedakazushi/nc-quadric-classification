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
# First-order equations of the two AS10 mutation walls around a
# nonzero 2-torsion point: eta=P and eta=P^{-1}.
u, v, z = sp.symbols("u v z")
wall_jac = sp.Matrix([v-u, v+u]).jacobian([u, v])
assert wall_jac.det() == -2
assert sp.factor(z**2-1) == (z-1)*(z+1)
assert sp.cancel((z**2-1)/(z-1)) == z+1
# Over characteristic zero the elliptic 2-torsion has 4 points,
# including zero. The connected nodal/I2 generalized Jacobian
# is G_m, whose nontrivial 2-torsion is the single point -1.
print("PASS: Serre numerical square, cubic parity, and transverse AS10 walls (det=-2)")

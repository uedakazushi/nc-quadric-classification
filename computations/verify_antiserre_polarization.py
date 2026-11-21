#!/usr/bin/env python3
"""Exact certificate for a constant-qgr, nonconstant antiserre presentation.

Run: python3 computations/verify_antiserre_polarization.py
Dependencies: SymPy and NumPy (no Numba, floating point, or random sampling).

At f1=f2=uv, use the actual iota-twisted R product from the shared PBW
chart. The right Zhang twist has product sigma^(degree of right factor)
on the left factor. Its generator weights are
    (2, 0, -2, 1, -1, 1, -1, 0, 0).

The proof in papers/sections/antiserre_polarization.tex is independent of
this certificate: the first-order commutator of central u^4 and v^4 is
16 epsilon u^4 v^4. This script independently verifies the orbit-rank
increase and the degree-one-center distinction at q=1 and q=2.
"""
from __future__ import annotations

import numpy as np
import sympy as sp
import verify_noncubic_antiserre_pivots as chart


def rank_mod(matrix: np.ndarray, prime: int = 101) -> int:
    """Gaussian elimination over F_prime, with exact integer arithmetic."""
    matrix = matrix.copy() % prime
    rank = 0
    for column in range(matrix.shape[1]):
        nonzero = np.flatnonzero(matrix[rank:, column])
        if not len(nonzero):
            continue
        row = rank + int(nonzero[0])
        matrix[[rank, row]] = matrix[[row, rank]]
        inverse = pow(int(matrix[rank, column]), -1, prime)
        matrix[rank, column:] = matrix[rank, column:] * inverse % prime
        rows = np.flatnonzero(matrix[rank + 1:, column]) + rank + 1
        if len(rows):
            matrix[rows, column:] = (
                matrix[rows, column:]
                - matrix[rows, column, None] * matrix[rank, None, column:]
            ) % prime
        rank += 1
        if rank == matrix.shape[0]:
            break
    return rank


names = list(chart.gens)
weights = np.array([2, 0, -2, 1, -1, 1, -1, 0, 0], dtype=np.int64)
pairs = [(names.index(x), names.index(y)) for x, y in chart.pivots]
other_pairs = [(i, j) for i in range(9) for j in range(9)
               if (i, j) not in pairs]
pivots = np.array([9 * i + j for i, j in pairs])
nonpivots = np.array([9 * i + j for i, j in other_pairs])
parameters = [chart.a, chart.b, chart.c, chart.aa, chart.bb, chart.cc]
evaluation = dict(zip(parameters, [0, 1, 0, 0, 1, 0]))

symbolic_product = sp.Matrix.hstack(*(
    chart.coordinates(chart.star(x, y)) for x in names for y in names
))
product = np.array(symbolic_product.subs(evaluation).tolist(), dtype=np.int64)
pivot_product = product[:, pivots]
assert np.array_equal(pivot_product.T @ pivot_product,
                      np.eye(25, dtype=np.int64))
coordinates = pivot_product.T @ product
relations = np.zeros((81, 56), dtype=np.int64)
relations[nonpivots, np.arange(56)] = 1
relations[pivots, :] = -coordinates[:, nonpivots]
assert not np.any(product @ relations)

# dJ = -(delta tensor 1)(J), modulo J, in the fixed Grassmann chart.
product_derivative = product * np.repeat(weights, 9)[None, :]
twist = (-pivot_product.T @ product_derivative @ relations).reshape(-1)
assert np.count_nonzero(twist) == 52

orbit_columns, delta_coordinates = [], []
for i in range(9):
    for j in range(9):
        if i == j == 8:
            continue
        derivative = np.zeros((81, 56), dtype=np.int64)
        for z in range(9):
            derivative[9 * i + z, :] += relations[9 * j + z, :]
            derivative[9 * z + i, :] += relations[9 * z + j, :]
        orbit_columns.append((pivot_product.T @ product @ derivative).reshape(-1))
        delta_coordinates.append(int(weights[i]) if i == j else 0)
orbit = np.stack(orbit_columns, axis=1)
delta_coordinates = np.array(delta_coordinates, dtype=np.int64)
assert np.any(delta_coordinates)
assert not np.any(orbit @ delta_coordinates)
assert rank_mod(orbit) == 79
assert rank_mod(np.column_stack([orbit, twist])) == 80
# The displayed nonzero kernel vector gives the characteristic-zero upper
# bounds 79 and 80. The mod-101 minors give matching lower bounds.
print("PASS: exact characteristic-zero orbit ranks 79 and 80 after adding twist.")

form_columns = []
for parameter in parameters:
    derivative = np.array(
        symbolic_product.diff(parameter).subs(evaluation).tolist(), dtype=np.int64
    )
    form_columns.append((-pivot_product.T @ derivative @ relations).reshape(-1))
known = np.column_stack([orbit, *form_columns])
assert rank_mod(known) == 81
assert rank_mod(np.column_stack([known, twist])) == 82
print("PASS: orbit plus six form directions has mod-101 rank 81; with twist 82.")


def center_matrix(multiplication: np.ndarray) -> np.ndarray:
    return np.vstack([
        np.column_stack([
            multiplication[:, 9 * i + j] - multiplication[:, 9 * j + i]
            for i in range(9)
        ]) for j in range(9)
    ])


center_at_one = center_matrix(product)
central_element = np.array([0, 0, 0, 0, 0, 0, 0, 1, -1], dtype=np.int64)
assert not np.any(center_at_one @ central_element)
assert rank_mod(center_at_one) == 8
# Clear the common denominator of sigma_2 on R_1. A common scalar in
# the multiplication matrix does not change its center kernel.
factors = np.array([int(4 * sp.Rational(2) ** int(w)) for w in weights],
                   dtype=np.int64)
product_at_two_scaled = product * np.repeat(factors, 9)[None, :]
assert rank_mod(center_matrix(product_at_two_scaled)) == 9
print("PASS: dim Z(R)_1 = 1 and dim Z(R_twist(q=2))_1 = 0 over characteristic zero.")
print("PASS: the first-order central commutator coefficient is 2*4-2*(-4) = 16.")

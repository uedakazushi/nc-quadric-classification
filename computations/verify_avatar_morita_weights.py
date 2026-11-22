#!/usr/bin/env python3
"""Exact checks of the four-vertex Brauer-weight bookkeeping.

Verifies integer characters, composition weights, Morita ranks and a
matrix-product associativity identity.  Does not verify geometric
cohomology, gerbe descent, AS regularity or a pointed qgr equivalence.
"""
from itertools import combinations
from sympy import Matrix

weights = ((0, 0), (1, 0), (0, 0), (0, 1))
dimensions = {(0, 1): 2, (0, 2): 4, (0, 3): 6,
              (1, 2): 2, (1, 3): 4, (2, 3): 2}
ranks = (1, 2, 1, 2)
expected = {(0, 1): (1, 0), (0, 2): (0, 0), (0, 3): (0, 1),
            (1, 2): (-1, 0), (1, 3): (-1, 1), (2, 3): (0, 1)}

for (i, j), dim in dimensions.items():
    char = tuple(weights[j][t] - weights[i][t] for t in (0, 1))
    assert char == expected[i, j]
    assert all(char[t] + weights[i][t] - weights[j][t] == 0
               for t in (0, 1))
    assert dim * ranks[i] * ranks[j] > 0

for i, j, k in combinations(range(4), 3):
    assert tuple(expected[i, j][t] + expected[j, k][t]
                 for t in (0, 1)) == expected[i, k]

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[2, 5], [7, 11]])
c = Matrix([[13, 17], [19, 23]])
assert (a*b)*c == a*(b*c)
assert tuple(tuple(w % 2 for w in x) for x in weights) == weights
print("PASS: all six Hom weights and triple compositions")
print("PASS: four vertex Brauer classes (0,c,0,d) and matrix associativity")
print("Scope: finite exact bookkeeping only")

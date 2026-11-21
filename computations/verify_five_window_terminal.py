#!/usr/bin/env python3
"""Exact terminal bar-complex ranks in the commutative quadric four-window.

Models both parity choices of the full exceptional sequence on P1 x P1.
This is a check at the commutative fiber, not a proof for noncubic families.
Usage: python3 computations/verify_five_window_terminal.py
Requires Python 3.9+ and SymPy >=1.12.
"""

from itertools import combinations, product
from sympy import SparseMatrix

WINDOWS = (
    ((0, 0), (1, 0), (1, 1), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (1, 1), (1, 2), (2, 2)),
)
EXPECTED_DIMS = (9, 40, 48, 16)
EXPECTED_RANKS = (9, 31, 16)


def edge_basis(objects, i, j):
    da = objects[j][0] - objects[i][0]
    db = objects[j][1] - objects[i][1]
    assert da >= 0 and db >= 0
    return [(a, b) for a in range(da + 1) for b in range(db + 1)]


def terminal_basis(objects, degree):
    result = []
    for mid in combinations((1, 2, 3), degree - 1):
        vertices = (0,) + mid + (4,)
        factors = [edge_basis(objects, i, j) for i, j in zip(vertices, vertices[1:])]
        result.extend((vertices, terms) for terms in product(*factors))
    return result


def differential(basis, degree):
    codomain = {element: i for i, element in enumerate(basis[degree - 1])}
    matrix = SparseMatrix(len(codomain), len(basis[degree]), {})
    for col, (vertices, terms) in enumerate(basis[degree]):
        for j in range(1, degree):
            shorter_vertices = vertices[:j] + vertices[j + 1:]
            shorter_terms = (
                terms[:j - 1]
                + ((terms[j - 1][0] + terms[j][0], terms[j - 1][1] + terms[j][1]),)
                + terms[j + 1:]
            )
            matrix[codomain[(shorter_vertices, shorter_terms)], col] += (-1) ** j
    return matrix


def verify(objects, parity):
    basis = {degree: terminal_basis(objects, degree) for degree in range(1, 5)}
    dims = tuple(len(basis[degree]) for degree in range(1, 5))
    assert dims == EXPECTED_DIMS, (parity, dims)
    diffs = {degree: differential(basis, degree) for degree in range(2, 5)}
    ranks = tuple(diffs[degree].rank() for degree in range(2, 5))
    assert ranks == EXPECTED_RANKS, (parity, ranks)
    for degree in (3, 4):
        composite = diffs[degree - 1] * diffs[degree]
        assert composite == SparseMatrix(composite.rows, composite.cols, {})
    homology = []
    for degree in range(1, 5):
        cycles = dims[degree - 1] - (diffs[degree].rank() if degree > 1 else 0)
        boundaries = diffs[degree + 1].rank() if degree < 4 else 0
        homology.append(cycles - boundaries)
    assert tuple(homology) == (0, 0, 1, 0), (parity, homology)
    print(f"PASS: parity {parity}: dims={dims}, ranks={ranks}, H_1..H_4={tuple(homology)}")


if __name__ == "__main__":
    for parity, objects in enumerate(WINDOWS):
        verify(objects, parity)

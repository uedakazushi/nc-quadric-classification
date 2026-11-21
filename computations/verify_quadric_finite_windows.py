#!/usr/bin/env python3
"""Exact Segre cubic-window tensor check at the two parities of Q=P1 x P1.

No random choices or floating point.  Run at the repository root:
    python3 computations/verify_quadric_finite_windows.py

This is a finite special-fibre consistency check, not a proof of the
relative etale-neighbourhood theorem or of infinite-degree exactness.
"""
from itertools import product

import sympy as sp


# Consecutive line bundles in the standard two-step helix on P1 x P1.
LINE_BUNDLES = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3)]


def monomials(bidegree):
    a, b = bidegree
    return list(product(range(a + 1), range(b + 1)))


def step_bidegree(i):
    a, b = LINE_BUNDLES[i]
    c, d = LINE_BUNDLES[i + 1]
    return (c - a, d - b)


def multiplication_matrix(start, number_of_steps):
    degrees = [step_bidegree(i) for i in range(start, start + number_of_steps)]
    bases = [monomials(deg) for deg in degrees]
    total_degree = (sum(deg[0] for deg in degrees),
                    sum(deg[1] for deg in degrees))
    target = monomials(total_degree)
    out = sp.zeros(len(target), sp.prod(len(basis) for basis in bases))
    for col, terms in enumerate(product(*bases)):
        exponent = tuple(sum(term[j] for term in terms) for j in range(2))
        out[target.index(exponent), col] = 1
    return out


def check_parity(start):
    p2 = multiplication_matrix(start, 2)
    p3 = multiplication_matrix(start, 3)
    p3_next = multiplication_matrix(start + 1, 3)
    p4 = multiplication_matrix(start, 4)

    relations = sp.Matrix.hstack(*p3.nullspace())
    next_relations = sp.Matrix.hstack(*p3_next.nullspace())
    left = sp.kronecker_product(relations, sp.eye(2))
    right = sp.kronecker_product(sp.eye(2), next_relations)
    overlap = left.row_join(-right).nullspace()

    assert (p2.rank(), p3.rank(), p4.rank()) == (4, 6, 9)
    assert relations.cols == 2 and next_relations.cols == 2
    assert len(overlap) == 1
    left_pair = sp.Matrix(2, 2, list(overlap[0][:4]))
    right_pair = sp.Matrix(2, 2, list(overlap[0][4:]))
    assert abs(left_pair.det()) == abs(right_pair.det()) == 1
    assert left_pair.rank() == right_pair.rank() == 2
    print(
        f"parity {start}: rank(product lengths 2/3/4)=4/6/9; "
        "rank(R)=2, rank(W)=1; two pairings unimodular — PASS"
    )


if __name__ == "__main__":
    for parity in (0, 1):
        check_parity(parity)

#!/usr/bin/env python3
"""Exact Segre cubic tensor checks at the two parities of Q=P1 x P1.

No random choices or floating point.  Run at the repository root:
    python3 computations/verify_quadric_finite_windows.py

This is a finite special-fibre consistency check, not a proof of the
relative etale-neighbourhood theorem or of infinite-degree exactness.
The all-degree presentation itself is proved algebraically using adjacent swaps.
"""
from itertools import product

import sympy as sp


# Consecutive line bundles O(floor(i/2), ceil(i/2)) on P1 x P1.
def line_bundle(i):
    return (i // 2, (i + 1) // 2)


def monomials(bidegree):
    a, b = bidegree
    return list(product(range(a + 1), range(b + 1)))


def step_bidegree(i):
    a, b = line_bundle(i)
    c, d = line_bundle(i + 1)
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


def relation_span(start, number_of_steps):
    """Span of all cubic relations inserted at consecutive positions."""
    blocks = []
    for offset in range(number_of_steps - 2):
        triple = multiplication_matrix(start + offset, 3)
        relation = sp.Matrix.hstack(*triple.nullspace())
        insertion = sp.kronecker_product(
            sp.kronecker_product(sp.eye(2**offset), relation),
            sp.eye(2**(number_of_steps - offset - 3)),
        )
        blocks.append(insertion)
    return sp.Matrix.hstack(*blocks)


def check_cubic_relations(start, max_length=7):
    """Finite-dimensional check of the cubic presentation at the special fibre."""
    for length in range(3, max_length + 1):
        product_map = multiplication_matrix(start, length)
        span = relation_span(start, length)
        relation_rank = span.rank()
        predicted = product_map.cols - product_map.rank()
        assert relation_rank == predicted, (start, length, relation_rank, predicted)
        print(
            f"parity {start}, length {length}: "
            f"relation rank {relation_rank} = kernel rank {predicted} — PASS"
        )


if __name__ == "__main__":
    for parity in (0, 1):
        check_parity(parity)
        check_cubic_relations(parity)

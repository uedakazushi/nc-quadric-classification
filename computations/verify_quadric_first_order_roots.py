#!/usr/bin/env python3
"""Exact finite checks for the Jacobian first-order cover and four root actions.

Run: python3 computations/verify_quadric_first_order_roots.py
Requires SymPy. No random input or numerical approximation is used.
These identities support the manuscript computations; they do not certify the
categorical deformation, relative AS, or full relative H2 theorems.
"""

from itertools import combinations_with_replacement

import sympy as sp


def main():
    x = sp.symbols("x0:4")
    pairs = list(combinations_with_replacement(range(4), 2))
    coeff = sp.symbols("c0:10")
    f = sum(c * x[i] * x[j] for c, (i, j) in zip(coeff, pairs))
    q = x[0] * x[3] - x[1] * x[2]
    gamma = sp.Matrix(4, 4, lambda i, j: sp.expand(sum(
        sp.LeviCivita(i, j, k, l) * sp.diff(q, x[k]) * sp.diff(f, x[l])
        for k in range(4) for l in range(4)
    )))

    def bracket(a, b):
        return sp.expand(sum(
            sp.diff(a, x[i]) * gamma[i, j] * sp.diff(b, x[j])
            for i in range(4) for j in range(4)
        ))

    assert gamma + gamma.T == sp.zeros(4)
    for variable in x:
        assert sp.expand(bracket(q, variable)) == 0
    print("PASS: gamma(q, x_i)=0 for all four generators, with ten symbolic coefficients")

    affine_difference = bracket(x[2] / x[0], x[1] / x[0]) - 2 * f / x[0]**2
    assert sp.cancel(affine_difference.subs(x[3], x[1] * x[2] / x[0])) == 0
    print("PASS: {x2/x0, x1/x0}=2 f/x0^2 modulo the Segre equation")

    z, w = sp.symbols("z w")
    affine_f = sp.Poly(f.subs({x[0]: 1, x[1]: w, x[2]: z, x[3]: z*w}), z, w)
    restriction = sp.Matrix([
        [sp.diff(affine_f.coeff_monomial(z**i * w**j), c) for c in coeff]
        for i in range(3) for j in range(3)
    ])
    assert restriction.rank() == 9
    q_vector = sp.Matrix([int((i, j) == (0, 3)) - int((i, j) == (1, 2)) for i, j in pairs])
    assert restriction * q_vector == sp.zeros(9, 1)
    print("PASS: quadratic restriction has rank 9 and kernel k*q")

    identity = sp.eye(3)
    involution = sp.diag(-1, 1, -1)  # partial_z, z partial_z, z^2 partial_z
    swap = sp.zeros(9)
    for i in range(3):
        for j in range(3):
            swap[3*j + i, 3*i + j] = 1
    actions = [
        sp.eye(9),
        sp.kronecker_product(involution, identity),
        sp.kronecker_product(involution, involution),
        -swap,  # exchanging factors reverses the order of the bivector wedge
    ]
    dimensions = []
    for action in actions:
        assert action**2 == sp.eye(9)
        dimensions.append(9 - (action - sp.eye(9)).rank())
    assert dimensions == [9, 3, 5, 3]
    print("PASS: four fixed-root HH^2 dimensions =", dimensions)
    print("All finite symbolic checks passed; categorical assertions require the written proofs.")


if __name__ == "__main__":
    main()

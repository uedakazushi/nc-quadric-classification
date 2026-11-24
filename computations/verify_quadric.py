#!/usr/bin/env python3
"""Exact finite checks for the nc-quadric-surface starting examples.

Run from the repository root with Python 3.9+ and SymPy (checked with SymPy 1.14.0):
    python3 computations/verify_quadric.py

No floating-point arithmetic or external inputs are used. The symbolic
reductions below prove the displayed identities because every rewrite is a
defining relation. They do not establish confluence in every degree. The
matrix ranks are ranks of the actual degree-two and degree-three relation
spaces, independently of the rewriting routine.

These calculations do NOT prove AS regularity, an all-degree Hilbert series,
smoothness of qgr, or a classification theorem. Those require the proofs and
the precisely cited Ore-extension theorem in the manuscript.
"""

from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from itertools import product

import sympy as sp


# Canonical monomial order: u < v < x < y.
U, V, X, Y = range(4)
LETTERS = (U, V, X, Y)
A = sp.Symbol("a")
Word = tuple[int, ...]
Polynomial = dict[Word, sp.Expr]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(poly: Polynomial) -> Polynomial:
    result = {}
    for word, coefficient in poly.items():
        expanded = sp.expand(coefficient)
        if expanded != 0:
            result[word] = expanded
    return result


def add(*polynomials: Polynomial) -> Polynomial:
    result = defaultdict(lambda: sp.Integer(0))
    for polynomial in polynomials:
        for word, coefficient in polynomial.items():
            result[word] += coefficient
    return clean(dict(result))


def scale(coefficient: sp.Expr, polynomial: Polynomial) -> Polynomial:
    return clean({word: coefficient * value for word, value in polynomial.items()})


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = defaultdict(lambda: sp.Integer(0))
    for left_word, left_coefficient in left.items():
        for right_word, right_coefficient in right.items():
            result[left_word + right_word] += left_coefficient * right_coefficient
    return clean(dict(result))


def generator(letter: int) -> Polynomial:
    return {(letter,): sp.Integer(1)}


@lru_cache(maxsize=None)
def reduce_word(word: Word) -> Polynomial:
    """Rewrite a word using central u,v and yx = a xy + (1-a)uv.

    Each replacement decreases the degree-lexicographic order with
    y > x > v > u, so this routine terminates. Returning zero proves an
    identity; all-degree uniqueness of the output is not assumed here.
    """
    for index in range(len(word) - 1):
        left, right = word[index : index + 2]
        if left <= right:
            continue
        prefix, suffix = word[:index], word[index + 2 :]
        if (left, right) == (Y, X):
            return add(
                scale(A, reduce_word(prefix + (X, Y) + suffix)),
                scale(1 - A, reduce_word(prefix + (U, V) + suffix)),
            )
        return reduce_word(prefix + (right, left) + suffix)
    return {word: sp.Integer(1)}


def reduce_polynomial(polynomial: Polynomial) -> Polynomial:
    return add(
        *(scale(coefficient, reduce_word(word))
          for word, coefficient in polynomial.items())
    )


def ore_relations(parameter: sp.Expr) -> list[Polynomial]:
    relations = []
    for smaller in LETTERS:
        for larger in LETTERS:
            if smaller >= larger or (larger, smaller) == (Y, X):
                continue
            relations.append({(larger, smaller): sp.Integer(1),
                              (smaller, larger): sp.Integer(-1)})
    relations.append(clean({(Y, X): sp.Integer(1),
                            (X, Y): -parameter,
                            (U, V): -(1 - parameter)}))
    return relations


G: Polynomial = {(X, Y): sp.Integer(1), (U, V): sp.Integer(-1)}


def matrix_of_polynomials(polynomials: list[Polynomial], degree: int) -> sp.Matrix:
    words = list(product(LETTERS, repeat=degree))
    row_number = {word: index for index, word in enumerate(words)}
    matrix = sp.zeros(len(words), len(polynomials))
    for column, polynomial in enumerate(polynomials):
        for word, coefficient in polynomial.items():
            require(len(word) == degree, "A relation has the wrong degree")
            matrix[row_number[word], column] += coefficient
    return matrix


def degree_three_ideal_matrix(relations: list[Polynomial]) -> sp.Matrix:
    generators = []
    for relation in relations:
        for letter in LETTERS:
            generators.append(multiply(generator(letter), relation))
            generators.append(multiply(relation, generator(letter)))
    return matrix_of_polynomials(generators, 3)


def segre_multiplication_matrix(degree: int) -> sp.Matrix:
    # u=s0*t1, v=s1*t0, x=s0*t0, y=s1*t1.
    # In bidegree (d,d), rows record the exponents of s1 and t1.
    exponents = {U: (0, 1), V: (1, 0), X: (0, 0), Y: (1, 1)}
    rows = list(product(range(degree + 1), repeat=2))
    row_number = {exponent: index for index, exponent in enumerate(rows)}
    words = list(product(LETTERS, repeat=degree))
    matrix = sp.zeros(len(rows), len(words))
    for column, word in enumerate(words):
        exponent = tuple(sum(exponents[letter][i] for letter in word)
                         for i in range(2))
        matrix[row_number[exponent], column] = 1
    return matrix


def verify_segre() -> None:
    quadratic = segre_multiplication_matrix(2)
    cubic = segre_multiplication_matrix(3)
    rank_two = quadratic.rank()
    rank_three = cubic.rank()
    require(quadratic.shape == (9, 16), "Wrong Segre quadratic matrix size")
    require(cubic.shape == (16, 64), "Wrong Segre cubic matrix size")
    require(rank_two == 9 and 16 - rank_two == 7, "Wrong quadratic Segre rank")
    require(rank_three == 16, "Wrong cubic Segre rank")

    standard_relations = matrix_of_polynomials(ore_relations(sp.Integer(1)) + [G], 2)
    require(standard_relations.rank() == 7, "The seven standard relations are dependent")
    require(quadratic * standard_relations == sp.zeros(9, 7),
            "A standard relation does not vanish on the Segre image")
    print("Segre multiplication: 9 x 16 rank 9, kernel 7; 16 x 64 rank 16.")

    # The first row of (x_ij) consists of x=x00 and u=x01.
    signs = {U: -1, V: 1, X: -1, Y: 1}
    gamma = sp.diag(*(signs[letter] for letter in LETTERS))
    even_edge = sp.kronecker_product(sp.eye(4), gamma)
    odd_edge = sp.kronecker_product(gamma, sp.eye(4))
    twisted_product = quadratic * even_edge
    for change in (even_edge, odd_edge):
        require(twisted_product * change * standard_relations == sp.zeros(9, 7),
                "An alternating edge pair does not preserve the relation space")
    words = list(product(LETTERS, repeat=2))
    commutator = twisted_product[:, words.index((X, V))] - twisted_product[:, words.index((V, X))]
    require(commutator == 2 * quadratic[:, words.index((X, V))] and commutator.norm() != 0,
            "The twisted x00, x10 commutator must be nonzero")
    print("Segre involution: both alternating pairs transport the kernel; x00 and x10 do not commute.")


def verify_symbolic_ore_identities() -> None:
    u, v, x, y = (generator(letter) for letter in LETTERS)
    identities = {
        "gx = a*xg": add(multiply(G, x), scale(-A, multiply(x, G))),
        "yg = a*gy": add(multiply(y, G), scale(-A, multiply(G, y))),
        "gu = ug": add(multiply(G, u), scale(-1, multiply(u, G))),
        "gv = vg": add(multiply(G, v), scale(-1, multiply(v, G))),
    }
    for name, identity in identities.items():
        require(reduce_polynomial(identity) == {}, f"Symbolic identity failed: {name}")

    # Verify specialization a=1, including every pair of generators.
    for left in LETTERS:
        for right in LETTERS:
            commutator = add(multiply(generator(left), generator(right)),
                             scale(-1, multiply(generator(right), generator(left))))
            specialized = clean({word: coefficient.subs(A, 1)
                                 for word, coefficient in reduce_polynomial(commutator).items()})
            require(specialized == {}, "The a=1 specialization is not commutative")
    require(reduce_polynomial(G) == G, "g unexpectedly reduced to zero")
    print("Symbolic Ore identities: gx=a*xg, yg=a*gy, gu=ug, gv=vg; a=1 commutative.")


def verify_finite_degree_ambient(parameter: sp.Rational) -> None:
    relations = ore_relations(parameter)
    degree_two = matrix_of_polynomials(relations, 2)
    degree_two_with_g = matrix_of_polynomials(relations + [G], 2)
    require(degree_two.rank() == 6, f"Ambient relation rank failed at a={parameter}")
    require(degree_two_with_g.rank() == 7, f"Quotient relation rank failed at a={parameter}")

    ambient_ideal = degree_three_ideal_matrix(relations)
    quotient_ideal = degree_three_ideal_matrix(relations + [G])
    ambient_rank = ambient_ideal.rank()
    quotient_rank = quotient_ideal.rank()
    require(ambient_rank == 44, f"Ambient degree-three ideal rank failed at a={parameter}")
    require(quotient_rank == 48, f"Quadric degree-three ideal rank failed at a={parameter}")

    left = matrix_of_polynomials([multiply(G, generator(letter)) for letter in LETTERS], 3)
    right = matrix_of_polynomials([multiply(generator(letter), G) for letter in LETTERS], 3)
    left_rank = ambient_ideal.row_join(left).rank() - ambient_rank
    right_rank = ambient_ideal.row_join(right).rank() - ambient_rank
    joint_rank = ambient_ideal.row_join(left).row_join(right).rank() - ambient_rank
    require((left_rank, right_rank, joint_rank) == (4, 4, 4),
            f"Normal-line multiplication rank failed at a={parameter}")

    print(f"a={parameter}: quadratic ranks 6 / 7; degree-three dimensions 20 / 16; "
          "gV, Vg and their sum have rank 4 in A_3.")


def main() -> None:
    print(f"Exact quadric checks (SymPy {sp.__version__}; rational/symbolic arithmetic).")
    verify_segre()
    verify_symbolic_ore_identities()
    for parameter in (sp.Rational(2), sp.Rational(-1)):
        verify_finite_degree_ambient(parameter)
    print("PASS. Symbolic identities and finite-degree ranks only; "
          "AS regularity, all-degree Hilbert series and smoothness are not computationally certified.")


if __name__ == "__main__":
    main()

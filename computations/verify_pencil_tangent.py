#!/usr/bin/env python3
"""Exact degree-two and degree-four certificate for the Sklyanin pencil."""
from itertools import product

import sympy as sp

from verify_quadric import LETTERS, add, matrix_of_polynomials, multiply, require


def quadratic_relations(alpha: sp.Rational, beta: sp.Rational) -> list:
    gamma = -(alpha + beta) / (1 + alpha * beta)
    relations = []
    for i, j, k, parameter in ((1, 2, 3, alpha), (2, 3, 1, beta), (3, 1, 2, gamma)):
        relations.extend((
            {(0, i): 1, (i, 0): -1, (j, k): -parameter, (k, j): -parameter},
            {(0, i): 1, (i, 0): 1, (j, k): -1, (k, j): 1},
        ))
    return relations


def quotient_map(relation_columns: sp.Matrix) -> tuple[sp.Matrix, list[int]]:
    reduced, pivots = relation_columns.T.to_DM().rref()
    reduced = reduced.to_Matrix()
    basis = [index for index in range(reduced.cols) if index not in pivots]
    quotient = sp.zeros(len(basis), reduced.cols)
    for row, index in enumerate(basis):
        quotient[row, index] = 1
        for pivot_row, pivot_col in enumerate(pivots):
            quotient[row, pivot_col] = -reduced[pivot_row, index]
    return quotient, basis


def degree_relations(relations: list, degree: int) -> sp.Matrix:
    generators = []
    for offset in range(degree - 1):
        for prefix in product(LETTERS, repeat=offset):
            for suffix in product(LETTERS, repeat=degree - 2 - offset):
                generators.extend({
                    prefix + word + suffix: coefficient
                    for word, coefficient in relation.items()
                } for relation in relations)
    return matrix_of_polynomials(generators, degree)


def central_squares(relations: list) -> list:
    quotient, _ = quotient_map(degree_relations(relations, 3))
    commutators = []
    for letter in LETTERS:
        columns = [
            add({(j, j, letter): 1}, {(letter, j, j): -1})
            for j in LETTERS
        ]
        commutators.append(quotient * matrix_of_polynomials(columns, 3))
    return [
        {(j, j): vector[j] for j in LETTERS if vector[j]}
        for vector in sp.Matrix.vstack(*commutators).nullspace()
    ]


def verify_pencil_tangent() -> None:
    relations = quadratic_relations(sp.Rational(2), sp.Rational(3))
    center = central_squares(relations)
    require(len(center) == 2, "Expected a two-dimensional pencil of central squares")

    _, monomial_indices = quotient_map(degree_relations(relations + center, 2))
    degree_two_words = list(product(LETTERS, repeat=2))
    lifts = [{degree_two_words[index]: 1} for index in monomial_indices]
    dimension = len(lifts)
    require(dimension == 8, "Wrong degree-one dimension for the elliptic quotient")

    to_ambient, _ = quotient_map(degree_relations(relations, 4))
    require(to_ambient.rows == 35, "Wrong dimension for the ambient degree four")
    pencil_squares = [multiply(center[i], center[j]) for i, j in ((0, 0), (0, 1), (1, 1))]
    pencil_times_lifts = [multiply(z, lift) for z in center for lift in lifts]
    pencil_ideal = to_ambient * matrix_of_polynomials(pencil_squares + pencil_times_lifts, 4)
    to_elliptic, _ = quotient_map(pencil_ideal)
    require(to_elliptic.rows == 16, "Wrong degree-two dimension for the elliptic quotient")

    lift_products = [multiply(left, right) for left in lifts for right in lifts]
    multiplication = to_ambient * matrix_of_polynomials(lift_products, 4)
    kernel = (to_elliptic * multiplication).to_DM().nullspace().to_Matrix().T
    require(kernel.cols == 48, "Wrong dimension for the elliptic quadratic relation space")
    coefficients, _ = pencil_ideal.gauss_jordan_solve(multiplication * kernel)

    target_size = dimension * kernel.cols
    columns = []
    for dual_index in range(dimension):
        column = sp.zeros(dimension, kernel.cols)
        for row in range(dimension):
            column[row, :] = (
                kernel[dual_index * dimension + row, :] +
                kernel[row * dimension + dual_index, :]
            )
        columns.append(column.reshape(target_size, 1))
    for index in range(len(center)):
        start = len(pencil_squares) + index * dimension
        lifted_relation = coefficients[start:start + dimension, :]
        columns.append(lifted_relation.reshape(target_size, 1))

    comparison = sp.Matrix.hstack(*columns)
    require(comparison[:, :dimension].to_DM().rank() == 8, "Non-injective change of lift")
    require(comparison.to_DM().rank() == 10, "The two pencil deformation classes are dependent")
    print("Sklyanin (2,3,-5/7): dim K=48, exact lift-change rank=8, combined rank=10.")


if __name__ == "__main__":
    verify_pencil_tangent()

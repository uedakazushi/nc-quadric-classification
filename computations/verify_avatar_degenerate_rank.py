"""Exact low-weight ranks for a boundary potential with a decomposable tensor."""

from collections import defaultdict
from functools import cache
from itertools import product

from sympy import Matrix, eye, kronecker_product, zeros
from sympy.polys.matrices import DomainMatrix


WEIGHTS = {"x": 1, "y": 1, "z": 2}


@cache
def paths(weight):
    if weight == 0:
        return ("",)
    return tuple(
        arrow + suffix
        for arrow, degree in WEIGHTS.items()
        if degree <= weight
        for suffix in paths(weight - degree)
    )


def cyclic_derivatives(terms):
    derivatives = defaultdict(lambda: defaultdict(int))
    for start, word, coefficient in terms:
        offset = start
        for position, arrow in enumerate(word):
            tail = word[position + 1 :] + word[:position]
            degree = 4 - WEIGHTS[arrow]
            tail_start = (offset + WEIGHTS[arrow]) % 4
            derivatives[tail_start, degree, arrow][tail] += coefficient
            offset += WEIGHTS[arrow]
    return derivatives


def quotient_dimension(derivatives, start, weight, min_diagonals=0):
    words = tuple(word for word in paths(weight) if word.count("z") >= min_diagonals)
    columns = {word: index for index, word in enumerate(words)}
    rows = []
    for (relation_start, degree, _arrow), relation in derivatives.items():
        for offset in range(weight - degree + 1):
            if (start + offset) % 4 != relation_start:
                continue
            for left, right in product(paths(offset), paths(weight - degree - offset)):
                row = [0] * len(words)
                for middle, coefficient in relation.items():
                    path = left + middle + right
                    if path in columns:
                        row[columns[path]] += coefficient
                rows.append(row)
    return len(words) - (DomainMatrix.from_Matrix(Matrix(rows)).rank() if rows else 0)


def inward_top_dimension(matrices, start, half_weight):
    cells = 4 * half_weight
    short_columns = half_weight
    long_columns = 4 * (half_weight - 1)
    relations = zeros(cells, short_columns + long_columns)
    for cell in range(half_weight):
        phase = (start + 2 * cell) % 4
        row = 4 * cell
        short = matrices[phase]
        relations[row : row + 4, cell : cell + 1] = Matrix(list(short))
        if cell == half_weight - 1:
            continue
        column = short_columns + 4 * cell
        opposite = matrices[(phase + 3) % 4]
        transfer = -matrices[(phase + 2) % 4] * opposite.T.inv()
        relations[row : row + 4, column : column + 4] = kronecker_product(eye(2), short.T)
        relations[row + 4 : row + 8, column : column + 4] = kronecker_product(transfer, opposite)
    return 1 + cells - DomainMatrix.from_Matrix(relations).rank()


def main():
    matrices = (
        ((1, 0), (0, 0)),
        ((1, 2), (3, 5)),
        ((4, 2), (1, 2)),
        ((2, 3), (1, 1)),
    )
    assert [Matrix(matrix).rank() for matrix in matrices] == [1, 2, 2, 2]
    short_terms = [
        (start, first + second + "z", matrix[a][b])
        for start, matrix in enumerate(matrices)
        for a, first in enumerate("xy")
        for b, second in enumerate("xy")
        if matrix[a][b]
    ]
    quartic_terms = [(0, "xxxy", 1), (0, "xyyx", 4), (0, "yxyy", -2), (0, "yyyy", 3)]
    for terms, expected_weight_five, expected_weight_six in (
        (short_terms, [13, 13, 12, 12], [20, 18, 19, 18]),
        (short_terms + quartic_terms, [12, 12, 12, 12], [17, 16, 16, 16]),
    ):
        derivatives = cyclic_derivatives(terms)
        dimensions = [
            [quotient_dimension(derivatives, start, weight) for weight in range(7)]
            for start in range(4)
        ]
        assert [row[:5] for row in dimensions] == [[1, 2, 4, 6, 9]] * 4
        assert [row[5] for row in dimensions] == expected_weight_five
        assert [row[6] for row in dimensions] == expected_weight_six
        assert [quotient_dimension(derivatives, start, 6, min_diagonals=2) for start in range(4)] == [5, 4, 4, 4]
    print("PASS: the quartic perturbation removes the weight-five defect, which reappears at weight six")
    coefficient_matrices = tuple(map(Matrix, matrices))
    assert [
        [inward_top_dimension(coefficient_matrices, start, half_weight) for start in (0, 2)]
        for half_weight in range(2, 6)
    ] == [[4, 4], [5, 4], [5, 5], [6, 5]]
    print("PASS: the reduced inward matrices recover the dimensions for weights four through ten")

    coincident_lines = (Matrix(((1, 0), (0, 0))), Matrix(((0, 1), (1, 0))), eye(2), eye(2))
    for coefficients, expected_rank in ((coefficient_matrices, 2), (coincident_lines, 1)):
        transport = coefficients[3].T * coefficients[2].inv() * coefficients[1].T
        first_basis_vector = Matrix([1, 0])
        pairing = (first_basis_vector.T * transport.inv() * first_basis_vector)[0]
        assert (2 if pairing else 1) == expected_rank
        for start in (0, 2):
            for half_weight in range(2, 9):
                defective_cells = sum((start + 2 * cell) % 4 == 0 for cell in range(half_weight))
                expected_dimension = 1 + 3 * defective_cells - expected_rank * (defective_cells - 1)
                assert inward_top_dimension(coefficients, start, half_weight) == expected_dimension
    print("PASS: the two line positions give the predicted dimensions through weight sixteen")


if __name__ == "__main__":
    main()

"""Exact low-weight ranks for a boundary potential with a decomposable tensor."""

from collections import defaultdict
from functools import cache
from itertools import product

from sympy import Matrix, eye, kronecker_product, symbols, zeros
from sympy.polys.matrices import DomainMatrix


WEIGHTS = {"x": 1, "y": 1, "z": 2}


@cache
def paths(weight, start=0, diagonal_parities=(0, 1)):
    if weight == 0:
        return ("",)
    return tuple(
        arrow + suffix
        for arrow, degree in WEIGHTS.items()
        if degree <= weight and (arrow != "z" or start % 2 in diagonal_parities)
        for suffix in paths(weight - degree, (start + degree) % 4, diagonal_parities)
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


def quotient_dimension(derivatives, start, weight, min_diagonals=0, diagonal_parities=(0, 1)):
    words = tuple(
        word for word in paths(weight, start, diagonal_parities) if word.count("z") >= min_diagonals
    )
    columns = {word: index for index, word in enumerate(words)}
    rows = []
    for (relation_start, degree, _arrow), relation in derivatives.items():
        for offset in range(weight - degree + 1):
            if (start + offset) % 4 != relation_start:
                continue
            prefixes = paths(offset, start, diagonal_parities)
            suffixes = paths(weight - degree - offset, (relation_start + degree) % 4, diagonal_parities)
            for left, right in product(prefixes, suffixes):
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


def quartic_representatives(short_words):
    words = tuple(map("".join, product("xy", repeat=4)))
    columns = {word: index for index, word in enumerate(words)}
    rows = []
    for phase, short_terms in enumerate(short_words):
        for suffix in paths(2):
            if "z" in suffix:
                continue
            row = [0] * len(words)
            for short in short_terms:
                path = short + suffix
                rotated = path[-phase:] + path[:-phase] if phase else path
                row[columns[rotated]] += 1
            rows.append(row)
    _, pivots = Matrix(rows).rref()
    return tuple(word for index, word in enumerate(words) if index not in pivots)


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
        terms = [
            (start, first + second + "z", coefficients[start][a, b])
            for start in range(4)
            for a, first in enumerate("xy")
            for b, second in enumerate("xy")
            if coefficients[start][a, b]
        ]
        derivatives = cyclic_derivatives(terms)
        for start, threshold in ((1, 4), (3, 5)):
            for half_weight in range(2, 6):
                expected = 5 if expected_rank == 1 and half_weight >= threshold else 4
                assert quotient_dimension(derivatives, start, 2 * half_weight, half_weight - 1) == expected
    print("PASS: the two line positions give the predicted dimensions through weight sixteen")

    first_parameter, second_parameter = symbols("a b")
    for exceptional, words in (("xx", ("xyxy", "yxyx")), ("xy", ("yxyx", "yyyx"))):
        normalized = [(0, exceptional + "z", 1)]
        normalized.extend((phase, word + "z", 1) for phase in (1, 2, 3) for word in ("xx", "yy"))
        normalized.extend(
            (0, word, coefficient)
            for word, coefficient in zip(words, (first_parameter, second_parameter))
        )
        assert len(paths(6)) == 169
        assert quotient_dimension(cyclic_derivatives(normalized), 0, 6) == 17
    print("PASS: both generic normalized families have rank 152 at weight six")

    generic_cases = (
        ((("xx",), ("yy",), ("xx", "yy"), ("xx", "yy")), ("xyxy", "yxyx"), 1, 5, 14),
        ((("xx",), ("xx", "yy"), ("xx",), ("xx", "yy")), ("xyxy", "yxyx"), 1, 6, 19),
        ((("xx",), ("yx",), ("yx",), ("xx", "yy")), ("xyyy", "yxxx"), 1, 5, 14),
        ((("yx",), ("yx",), ("yx",), ("yx",)), ("xxxx", "yyyy"), 0, 5, 14),
    )
    for shorts, quartics, start, weight, expected_dimension in generic_cases:
        assert quartic_representatives(shorts) == quartics
        terms = [
            (phase, short + "z", 1)
            for phase, phase_terms in enumerate(shorts)
            for short in phase_terms
        ]
        terms.extend(
            (0, word, coefficient)
            for word, coefficient in zip(quartics, (first_parameter, second_parameter))
        )
        derivatives = cyclic_derivatives(terms)
        assert quotient_dimension(derivatives, start, weight) == expected_dimension
    print("PASS: all four generic multiple-degeneracy strata fail the required Hilbert dimensions")

    for opposite, weight_eight in ((("xx", "yy"), 28), (("xx",), 36)):
        shorts = (("xx",), (), opposite, ())
        quartics = quartic_representatives(shorts)
        assert quartics == ("xyxy", "xyyx", "xyyy", "yxxy", "yxyx", "yxyy", "yyxy", "yyyx", "yyyy")
        terms = [(0, "xxz", 1), *((2, short + "z", 1) for short in opposite)]
        terms.extend(
            (0, word, coefficient)
            for word, coefficient in zip(quartics, (-21, 34, -30, -6, -23, 25, 19, 22, 10))
        )
        derivatives = cyclic_derivatives(terms)
        expected_dimensions = (1, 2, 4, 6, 9, 12, 16, 20)
        for start in range(4):
            dimensions = tuple(
                quotient_dimension(derivatives, start, weight, diagonal_parities=(0,))
                for weight in range(len(expected_dimensions))
            )
            assert dimensions == expected_dimensions
        assert quotient_dimension(derivatives, 0, 8, diagonal_parities=(0,)) == weight_eight
    print("PASS: one-mass degenerate samples match through weight seven and fail at weight eight")


if __name__ == "__main__":
    main()

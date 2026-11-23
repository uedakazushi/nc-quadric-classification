"""Exact low-weight ranks for a boundary potential with a decomposable tensor."""

from collections import defaultdict
from functools import cache
from itertools import product

from sympy import Matrix
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


if __name__ == "__main__":
    main()

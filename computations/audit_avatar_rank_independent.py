"""Independent exact audit of finite rank obstructions in Paper C."""

from collections import defaultdict
from functools import cache

from sympy import Matrix, eye, symbols, zeros
from sympy.polys.domains import QQ


def relation_matrix(cycles, variables, start, weight, diagonals):
    field = QQ.frac_field(*variables)
    letters = {0: 1, 1: 1, 2: 2}

    @cache
    def paths(vertex, remaining):
        if remaining == 0:
            return ((),)
        return tuple(
            ((vertex, symbol),) + tail
            for symbol, degree in letters.items()
            if degree <= remaining and (symbol != 2 or vertex % 2 in diagonals)
            for tail in paths((vertex + degree) % 4, remaining - degree)
        )

    relations = defaultdict(dict)
    for phase, word, scalar in cycles:
        orbit = []
        for letter in word:
            code = "xyz".index(letter)
            orbit.append((phase, code))
            phase = (phase + letters[code]) % 4
        for offset, arrow in enumerate(orbit):
            row = relations[arrow]
            path = tuple(orbit[offset + 1:] + orbit[:offset])
            row[path] = row.get(path, 0) + scalar

    basis = {path: index for index, path in enumerate(paths(start, weight))}
    matrix = []
    for left_degree in range(weight - 1):
        left_finish = (start + left_degree) % 4
        for (removed_start, removed_symbol), relation in relations.items():
            rel_degree = 4 - letters[removed_symbol]
            if (removed_start + letters[removed_symbol]) % 4 != left_finish or left_degree + rel_degree > weight:
                continue
            for left in paths(start, left_degree):
                for right in paths(removed_start, weight - left_degree - rel_degree):
                    row = {
                        basis[left + path + right]: field.from_sympy(scalar) if hasattr(scalar, "free_symbols") else field(scalar)
                        for path, scalar in relation.items() if scalar
                    }
                    if row:
                        matrix.append(row)
    return len(basis), matrix, field


def sparse_rank(rows, field):
    rank = 0
    units = (field.one, -field.one)
    while rows:
        rows.sort(key=len)
        key = next(
            ((index, col) for index, row in enumerate(rows)
             for col, value in row.items()
             if value in units),
            None,
        )
        if key is None:
            index = 0
            col = min(rows[0], key=lambda k: len(rows[0][k].numer) + len(rows[0][k].denom))
        else:
            index, col = key
        pivot = rows.pop(index)
        pivot_value = pivot[col]
        for row in rows:
            value = row.pop(col, field.zero)
            if not value:
                continue
            factor = value / pivot_value
            for j, entry in pivot.items():
                if j == col:
                    continue
                difference = row.get(j, field.zero) - factor * entry
                if difference:
                    row[j] = difference
                else:
                    row.pop(j, None)
        rows = [row for row in rows if row]
        rank += 1
    return rank


def cases():
    a, b, t = symbols("a b t")
    yield "one diagonalizable", ("xx", "xx+yy", "xx+yy", "xx+yy"), (("xyxy", a), ("yxyx", b)), (a, b), 0, 6, (0, 1), 17
    yield "one nilpotent", ("xy", "xx+yy", "xx+yy", "xx+yy"), (("yxyx", a), ("yyyx", b)), (a, b), 0, 6, (0, 1), 17
    yield "two adjacent", ("xx", "yy", "xx+yy", "xx+yy"), (("xyxy", a), ("yxyx", b)), (a, b), 1, 5, (0, 1), 14
    yield "two opposite", ("xx", "xx+yy", "xx", "xx+yy"), (("xyxy", a), ("yxyx", b)), (a, b), 1, 6, (0, 1), 19
    yield "three", ("xx", "yx", "yx", "xx+yy"), (("xyyy", a), ("yxxx", b)), (a, b), 1, 5, (0, 1), 14
    yield "four", ("yx", "yx", "yx", "yx"), (("xxxx", a), ("yyyy", b)), (a, b), 0, 5, (0, 1), 14
    coefficients = zip(("xyxy", "xyyx", "xyyy", "yxxy", "yxyx", "yxyy", "yyxy", "yyyx", "yyyy"),
                       (t-21, 34, -30, -6, -23, 25, 19, 22, 10))
    quartics = tuple(coefficients)
    yield "one mass rank one, two", ("xx", "", "xx+yy", ""), quartics, (t,), 0, 8, (0,), 28
    yield "one mass rank one, one", ("xx", "", "xx", ""), quartics, (t,), 0, 8, (0,), 36


def quotient_action(left, right, diagonal):
    out = []
    for row, col in ((0, 1), (1, 0), (1, 1)):
        unit = zeros(2)
        unit[row, col] = 1
        delta = left * unit + unit * right.T
        out.append(Matrix([delta[0, 1], delta[1, 0], delta[1, 1] - diagonal * delta[0, 0]]))
    return Matrix.hstack(*out)


def main():
    for label, shorts, quartics, parameters, phase, degree, diagonals, expected in cases():
        potential = [(vertex, pair + "z", 1)
                     for vertex, relation in enumerate(shorts) if relation
                     for pair in relation.split("+")]
        potential.extend((0, path, coefficient) for path, coefficient in quartics)
        n, matrix, field = relation_matrix(potential, parameters, phase, degree, diagonals)
        dimension = n - sparse_rank(matrix, field)
        assert dimension == expected, (label, dimension, expected)
        print(label, dimension, flush=True)

    zero = zeros(2)
    upper = Matrix([[0, 1], [0, 0]])
    lower = upper.T
    d0 = Matrix.diag(1, 0)
    d1 = Matrix.diag(0, 1)
    diagonal_one = [
        quotient_action(g, h, 0)
        for g, h in [(g, zero) for g in (d0, d1, upper)] + [(zero, h) for h in (d0, d1, upper)]
    ]
    diagonal_two = [quotient_action(g, -g.T, 1) for g in (d0, upper, lower)]
    diagonal_two.append(quotient_action(eye(2), zero, 1))
    center = Matrix(3, 3, [-21, 34, -30, -6, -23, 25, 19, 22, 10])
    transverse = Matrix([1] + [0] * 8)
    scalar_field = QQ.frac_field(*symbols("t,"))
    for other in (diagonal_one, diagonal_two):
        tangent = [Matrix(list(action * center)) for action in diagonal_one]
        tangent.extend(Matrix(list(center * action.T)) for action in other)
        rows = [
            {index: scalar_field(int(value)) for index, value in enumerate(vector) if value}
            for vector in tangent + [transverse]
        ]
        assert sparse_rank(rows, scalar_field) == 9
    print("rank-nine tangency from the original rank-two pencils")


if __name__ == "__main__":
    main()

"""Exact finite-degree checks for the noncubic central AS4 hull.

The calculation uses the displayed quadratic presentation, not the claimed
Hilbert series or Frobenius formulas.  It works first over QQ(a,b), then at
the non-disjoint, shared-root, and coincident-root rational representatives.
It checks degrees 2--5, the two Frobenius pairings, chi's normality and square,
and the one-dimensional quadratic center and zero quadratic anticenter
after the good-root Zhang twist.

All-degree regularity, Koszulness, AS regularity and relative effectivity
require the manuscript proofs; finite-degree checks do not establish them.
Run from the repository root:
    python3 computations/verify_noncubic_central_hull.py
Requires only SymPy. No random seed or external input is used.
"""

from itertools import product

import sympy as sp
from sympy.polys.matrices import DomainMatrix


U, V, C, D = range(4)


def word_index(word):
    result = 0
    for letter in word:
        result = 4 * result + letter
    return result


def add(left, right):
    result = dict(left)
    for word, value in right.items():
        result[word] = result.get(word, 0) + value
        if not result[word]:
            del result[word]
    return result


def scale(value, word_sum):
    return {word: value * coefficient for word, coefficient in word_sum.items()
            if value * coefficient}


def multiply(left, right):
    result = {}
    for x, a in left.items():
        for y, b in right.items():
            word = x + y
            result[word] = result.get(word, 0) + a * b
    return {word: value for word, value in result.items() if value}


def presentation(field, a, b):
    one = field.one
    relations = [{(C, D): one}, {(D, C): one}]
    for x, y in [(U, C), (V, C), (U, D), (V, D)]:
        relations.append({(x, y): one, (y, x): one})
    relations.extend([
        {(U, U): one, (D, D): b},
        {(V, V): one, (D, D): a},
        {(U, V): one, (V, U): one, (C, C): one,
         (D, D): -one - a * b},
    ])
    return [{word: value for word, value in row.items() if value}
            for row in relations]


class Quotient:
    """Degree-n word space modulo all inserted quadratic relations."""

    def __init__(self, relations, n, field):
        rows = {}
        row_number = 0
        for place in range(n - 1):
            for left in product(range(4), repeat=place):
                for right in product(range(4), repeat=n - place - 2):
                    for relation in relations:
                        rows[row_number] = {
                            word_index(left + word + right): value
                            for word, value in relation.items() if value
                        }
                        row_number += 1
        matrix = DomainMatrix(rows, (row_number, 4**n), field)
        rref, pivots = matrix.rref()
        pivot_set = set(pivots)
        free = [j for j in range(4**n) if j not in pivot_set]
        position = {j: i for i, j in enumerate(free)}
        self.dimension = len(free)
        self.field = field
        self.normal = {j: {i: field.one} for i, j in enumerate(free)}
        for row, pivot in enumerate(pivots):
            self.normal[pivot] = {
                position[column]: -value
                for column, value in rref.rep[row].items()
                if column in position and value
            }

    def reduce(self, word_sum):
        result = [self.field.zero] * self.dimension
        for word, value in word_sum.items():
            for place, coefficient in self.normal[word_index(word)].items():
                result[place] += value * coefficient
        return result


def check_case(name, field, a, b):
    one = field.one
    half = one / 2
    theta = one - a * b
    assert theta
    letters = [{(i,): one} for i in range(4)]
    p, q = {(C, C): one}, {(D, D): one}
    chi = {(U, V): one, (V, U): -one}
    relations = presentation(field, a, b)
    e3, e4 = [Quotient(relations, n, field) for n in [3, 4]]
    assert (e3.dimension, e4.dimension) == (8, 8)

    # chi anticommutes with U,V and commutes with C,D.
    for i, letter in enumerate(letters):
        sign = -one if i in (U, V) else one
        commutator = add(multiply(chi, letter),
                         scale(-sign, multiply(letter, chi)))
        assert not any(e3.reduce(commutator))
    square = add(multiply(chi, chi), scale(-one, multiply(p, p)))
    square = add(square, scale(-theta**2, multiply(q, q)))
    assert not any(e4.reduce(square))

    p_relations = relations + [chi]
    pieces = {n: Quotient(p_relations, n, field) for n in [2, 3, 4, 5]}
    assert [pieces[n].dimension for n in [2, 3, 4, 5]] == [6, 4, 1, 0]
    top = pieces[4]
    q4 = top.reduce(multiply(q, q))[0]
    assert q4

    def trace(word):
        return field.to_sympy(top.reduce({word: one})[0] / q4)

    basis2 = [(C, C), (D, D), (U, C), (V, C), (U, D), (V, D)]
    basis3 = [(U, D, D), (V, D, D), (C, C, C), (D, D, D)]
    m13 = sp.Matrix([[trace((i,) + word) for word in basis3]
                     for i in range(4)])
    m31 = sp.Matrix([[trace(word + (i,)) for i in range(4)]
                     for word in basis3])
    m22 = sp.Matrix([[trace(left + right) for right in basis2]
                     for left in basis2])
    a_s, b_s, th_s = map(field.to_sympy, [a, b, theta])
    middle = (1 + a_s * b_s) / 2
    expected13 = sp.diag(sp.Matrix([[-b_s, middle], [middle, -a_s]]),
                         -th_s**2, 1)
    expected22 = sp.diag(-th_s**2, 1,
                         sp.Matrix([[0, -th_s**2 / 2], [-th_s**2 / 2, 0]]),
                         sp.Matrix([[b_s, -middle], [-middle, a_s]]))
    assert (m13 - expected13).applyfunc(sp.cancel).is_zero_matrix
    assert (m31 - expected13.T).applyfunc(sp.cancel).is_zero_matrix
    assert (m22 - expected22).applyfunc(sp.cancel).is_zero_matrix
    assert sp.cancel(m13.det() - th_s**4 / 4) == 0
    assert sp.cancel(m22.det() + th_s**8 / 16) == 0

    # A scalar multiple of alpha=sigma^{-t} avoids adjoining sqrt(theta).
    # alpha'(U)=U+bV, alpha'(V)=-aU-V, alpha'(C)=theta D,
    # alpha'(D)=-C. Thus alpha'^2=theta*iota and alpha'(chi)=-theta*chi.
    alpha = [
        {(U,): one, (V,): b},
        {(U,): -a, (V,): -one},
        {(D,): theta},
        {(C,): -one},
    ]

    def apply_alpha(word_sum):
        result = {}
        for word, value in word_sum.items():
            image = {(): value}
            for letter in word:
                image = multiply(image, alpha[letter])
            result = add(result, image)
        return result

    basis_e2 = [p, q, chi] + [{word: one} for word in basis2[2:]]
    center_columns = []
    anticenter_columns = []
    for z in basis_e2:
        az = apply_alpha(z)
        column = []
        anticolumn = []
        for i, letter in enumerate(letters):
            sign = one if i in (U, V) else -one
            left = scale(theta * sign, multiply(z, letter))
            right = multiply(letter, az)
            commutator = add(left, scale(-one, right))
            column.extend(e3.reduce(commutator))
            anticolumn.extend(e3.reduce(add(left, right)))
        center_columns.append(column)
        anticenter_columns.append(anticolumn)
    center_rows = {
        i: {j: center_columns[j][i] for j in range(7)
            if center_columns[j][i]}
        for i in range(32)
    }
    center_matrix = DomainMatrix({i: row for i, row in center_rows.items() if row},
                                (32, 7), field)
    _, pivots = center_matrix.rref()
    assert len(pivots) == 6
    assert all(value == 0 for value in center_columns[2])
    anticenter_rows = {
        i: {j: anticenter_columns[j][i] for j in range(7)
            if anticenter_columns[j][i]}
        for i in range(32)
    }
    anticenter_matrix = DomainMatrix(
        {i: row for i, row in anticenter_rows.items() if row}, (32, 7), field)
    _, pivots = anticenter_matrix.rref()
    assert len(pivots) == 7

    print(f"PASS {name}: P degrees 2..5 = 6,4,1,0; "
          f"center/anticenter dimensions = 1/0; "
          f"det(1,3) = {sp.factor(m13.det())}; "
          f"det(2,2) = {sp.factor(m22.det())}")


def main():
    a, b = sp.symbols("a b")
    field = sp.QQ.frac_field(a, b)
    check_case("generic QQ(a,b)", field,
               field.from_sympy(a), field.from_sympy(b))
    for name, a_value, b_value in [
            ("disjoint", 1, -3), ("one shared root", 0, -3),
            ("coincident pairs", 0, 0)]:
        check_case(name, sp.QQ, sp.QQ(a_value), sp.QQ(b_value))
    print("All checks use exact fields. All-degree conclusions require the proof.")


if __name__ == "__main__":
    main()

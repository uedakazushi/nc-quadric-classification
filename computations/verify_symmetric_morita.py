#!/usr/bin/env python3
"""Exact checks for the symmetric noncubic Morita model.

Checks three rational root configurations, a polynomial Serre/Euler identity
for every tensor degree, and the exchange character of the Clifford trace.
It does not certify relative descent, tilting generation, or qgr equivalence.
Run from the repository root with Python 3 and SymPy.
"""

import sympy as sp

from verify_noncubic_pointed_end import V, W, right1, vector2


def poly_vector(poly):
    return sp.Matrix([poly.get(v, 0) for v in V])


def maps_to_free(generator, l1, l2, f2):
    """Degree-zero Hom(coker [[z,l1],[l2,-z]], B(1))."""
    columns = []
    for i in range(8):
        p, q = sp.zeros(4, 1), sp.zeros(4, 1)
        (p if i < 4 else q)[i % 4] = 1

        def times(v, polynomial):
            return sum((v[j] * right1(V[j], polynomial, f2)
                        for j in range(4)), sp.zeros(len(W), 1))

        columns.append(sp.Matrix.vstack(
            times(p, {generator: 1}) + times(q, l2),
            times(p, l1) - times(q, {generator: 1})))
    equations = sp.Matrix.hstack(*columns)
    basis = equations.nullspace()
    assert len(basis) == 2
    # Composition with the two degree-zero sections of the spinor.
    product = sp.Matrix.hstack(*(b[j:j + 4, 0]
                                for b in basis for j in (0, 4)))
    assert product.rank() == 3
    return product


def cross_hom(source, l1, l2, target, m1, m2):
    """Hom(X_source, X_target) in degree zero, using degree-one relations."""
    relations = sp.Matrix.hstack(
        vector2({target: 1}, m2),
        vector2(m1, {target: -1}))
    columns = []
    for i in range(4):
        a = sp.zeros(2, 2)
        a[i // 2, i % 2] = 1

        def pair(v, polynomial):
            return sp.Matrix.vstack(*(v[j] * poly_vector(polynomial)
                                      for j in range(2)))

        columns.append(sp.Matrix.vstack(
            pair(a[:, 0], {source: 1}) + pair(a[:, 1], l2),
            pair(a[:, 0], l1) - pair(a[:, 1], {source: 1})))
    c = sp.Matrix.hstack(*columns)
    rr = sp.diag(relations, relations)
    return 4 - (c.row_join(rr).rank() - rr.rank())


def finite_square():
    cases = (
        ("disjoint", {"uu": -1, "uv": 3, "vv": -2},
         {"u": 1, "v": -2}, {"u": 1, "v": -1}),
        ("one-shared-root", {"uu": -1, "uv": 1},
         {"u": 1}, {"u": 1, "v": -1}),
        ("coincident", {"uv": -1}, {"u": 1}, {"v": 1}),
    )
    for label, f2, m1, m2 in cases:
        c = maps_to_free("c", {"u": 1}, {"v": 1}, f2)
        d = maps_to_free("d", m1, m2, f2)
        assert cross_hom("c", {"u": 1}, {"v": 1},
                         "d", m1, m2) == 0
        assert cross_hom("d", m1, m2, "c",
                         {"u": 1}, {"v": 1}) == 0
        joint = c.row_join(d)
        assert joint.rank() == 4
        assert len(joint.nullspace()) == 4
        assert c.rank() + d.rank() - joint.rank() == 2
        print(f"PASS {label}: cross Hom=0 both ways; "
              "square products rank 4, quadratic relations 4")


def all_degree_euler():
    chain = sp.Matrix([[1, 2, 4, 6], [0, 1, 2, 4],
                       [0, 0, 1, 2], [0, 0, 0, 1]])
    change = sp.Matrix.hstack(sp.eye(4)[:, 0], sp.eye(4)[:, 1],
                             2 * sp.eye(4)[:, 2] - sp.eye(4)[:, 3],
                             sp.eye(4)[:, 2])
    square = sp.Matrix([[1, 2, 2, 4], [0, 1, 0, 2],
                        [0, 0, 1, 2], [0, 0, 0, 1]])
    assert change.det() in (1, -1)
    assert change.T * chain * change == square
    serre = square.inv() * square.T
    nilpotent = serre - sp.eye(4)
    assert nilpotent ** 3 == sp.zeros(4)
    n = sp.symbols("n", integer=True, nonnegative=True)
    inverse_power = (sp.eye(4) - n * nilpotent
                     + n * (n + 1) / 2 * nilpotent ** 2)
    h = sp.simplify(square * inverse_power)
    assert sp.expand(h[0, 0] - (2 * n + 1) ** 2) == 0
    for ranks, expected in (
        ((1, 2, 2, 1), 144 * n ** 2 + 144 * n + 30),
        ((1, 2, 2, 2), 196 * n ** 2 + 196 * n + 45),
    ):
        r = sp.Matrix(ranks)
        assert sp.expand((r.T * h * r)[0] - expected) == 0
    exchange = sp.eye(4)
    exchange.col_swap(1, 2)
    assert exchange ** 2 == sp.eye(4)
    assert exchange.T * square * exchange == square
    assert square[1, 2] == square[2, 1] == 0
    print("PASS all degrees: mutation Euler identity; nilpotent Serre; "
          "rank30=144n²+144n+30; rank45=196n²+196n+45; "
          "pointed corner=(2n+1)²")


def clifford_trace():
    # Central basis (1,c,d,cd), c²=f, d²=g, dc=h-cd.
    h = sp.symbols("h")
    pair = sp.Matrix([[0, 0, 0, 1], [0, 0, 1, 0],
                      [0, -1, 0, 0], [1, 0, 0, h]])
    assert pair.det() == -1
    iota = sp.diag(1, -1, -1, 1)
    assert pair == iota * pair.T
    swap = sp.Matrix([[1, 0, 0, h], [0, 0, 1, 0],
                      [0, 1, 0, 0], [0, 0, 0, -1]])
    assert swap ** 2 == sp.eye(4)
    trace = sp.Matrix([[0, 0, 0, 1]])
    assert trace * swap == -trace
    assert swap.T * pair * swap == -pair
    a, b = sp.symbols("a b", nonzero=True)
    scaling = sp.diag(1, a, b, a * b)
    assert trace * scaling == a * b * trace
    # The top central Cech class cd/(u v h) changes sign under swap;
    # the additional 1/(uv) belongs to the two-variable localization.
    assert (swap * sp.Matrix([0, 0, 0, 1]))[3] == -1
    print("PASS Clifford trace: perfect pairing, Nakayama signs, "
          "exchange character -1, connected scalar character a_c*a_d")


if __name__ == "__main__":
    finite_square()
    all_degree_euler()
    clifford_trace()
    print("Scope: finite exact algebra and all-degree numerical identities; "
          "geometric descent and qgr reconstruction require the manuscript proofs.")

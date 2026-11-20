#!/usr/bin/env python3
"""Exact checks for transverse and tangent (1,1)+(1,1) boundaries.

Run with Python 3 and SymPy. Every assertion is a polynomial/rational-function
identity in algebraically independent a, b, r; no numerical sampling is used.

Geometric domain: a*b*r != 0, a != b, b != a*r, r != 1.
The nonzero conditions are the gluing parameters of line bundles. Equality
a=b or b=a*r makes one adjacent pair of degree-two maps identify the two
components, so it is not a closed embedding as a (2,2) divisor. Equality r=1
means L_0=L_2, excluded by the admissible-quadruple definition. The identities
below remain polynomially valid on some excluded points; that does not extend
the geometric theorem to them.
"""

from collections import defaultdict
from itertools import product
import sympy as sp


def first_relation(a, b, c):
    return {"yxx": a * (b-c), "xyx": b * (c-a), "xxy": c * (a-b)}


def second_relation(a, b, c):
    return {"yyx": a-b, "yxy": c-a, "xyy": b-c}


def add_word_sum(target, source, coefficient=1, prefix="", suffix=""):
    for word, value in source.items():
        target[prefix + word + suffix] += coefficient * value


def quartic_left(a, b, r):
    """w_i = a*d*x_i*G_(i+1) + a*y_i*F_(i+1), d=b*r."""
    result = defaultdict(lambda: sp.Integer(0))
    add_word_sum(result, second_relation(b, a*r, b*r), a*b*r, prefix="x")
    add_word_sum(result, first_relation(b, a*r, b*r), a, prefix="y")
    return dict(result)


def quartic_right(a, b, r):
    """w_i = d*F_i*y_(i+3) + a*d*G_i*x_(i+3), d=b*r."""
    result = defaultdict(lambda: sp.Integer(0))
    add_word_sum(result, first_relation(a, b, a*r), b*r, suffix="y")
    add_word_sum(result, second_relation(a, b, a*r), a*b*r, suffix="x")
    return dict(result)


def assert_equal_word_sums(left, right):
    for word in set(left) | set(right):
        assert sp.cancel(left.get(word, 0) - right.get(word, 0)) == 0, word


def evaluate_on_component(relation, t, coordinate, minus=False):
    result = 0
    for word, coefficient in relation.items():
        term = coefficient
        for j, letter in enumerate(word):
            if letter == "y":
                term *= coordinate / t[j] if minus else coordinate
        result += term
    return sp.cancel(result)


def verify_transverse():
    a, b, r, z, w = sp.symbols("a b r z w", nonzero=True)
    parameters = [a, b, a*r]
    for relation in (first_relation(*parameters), second_relation(*parameters)):
        assert evaluate_on_component(relation, parameters, z) == 0
        assert evaluate_on_component(relation, parameters, w, minus=True) == 0
    print("PASS: both cubic relations vanish identically on both components")

    left, right = quartic_left(a, b, r), quartic_right(a, b, r)
    assert_equal_word_sums(left, right)
    assert set(left) | set(right) == {"xxyy", "xyxy", "xyyx", "yxxy", "yxyx", "yyxx"}
    print("PASS: all six coefficients of the two quartic expressions agree")

    rotated = defaultdict(lambda: sp.Integer(0))
    for word, coefficient in left.items():
        # theta_i(x_i)=r*x_(i+4), theta_i(y_i)=r^2*y_(i+4).
        factor = r if word[0] == "x" else r**2
        rotated[word[1:] + word[0]] += factor * coefficient
    assert_equal_word_sums(rotated, quartic_left(b, a*r, r))
    print("PASS: twisted cyclic rotation is exactly w_(i+1)")

    # The square of beta=diag(1,u), u^2=r, is diag(1,r).
    theta = sp.diag(r, r**2)
    beta_square = sp.diag(1, r)
    assert theta == r * beta_square
    print("PASS: theta differs from beta^2 by the diagonal-gauge scalar r")



# Tangent boundary: q*d*(q-d) != 0. Equal adjacent parameters collapse the
# two-component map; d=0 means L_0=L_2. Polynomial identities alone do not
# extend admissibility to these excluded parameters.
def first_relation_tangent(q, d):
    return {"yxx": q-d, "xyx": d, "xxy": -q}


def second_relation_tangent(q, d):
    return {"yyx": -q, "yxy": d, "xyy": q-d,
            "yxx": d*(d-q), "xyx": -d*(d-q)}


def quartic_left_tangent(q, d):
    result = defaultdict(lambda: sp.Integer(0))
    add_word_sum(result, second_relation_tangent(d-q, d), prefix="x")
    add_word_sum(result, first_relation_tangent(d-q, d), prefix="y")
    return dict(result)


def quartic_right_tangent(q, d):
    result = defaultdict(lambda: sp.Integer(0))
    add_word_sum(result, first_relation_tangent(q, d), suffix="y")
    add_word_sum(result, first_relation_tangent(q, d), d, suffix="x")
    add_word_sum(result, second_relation_tangent(q, d), suffix="x")
    return dict(result)


def evaluate_tangent(relation, parameters, coordinate, minus=False):
    result = 0
    for word, coefficient in relation.items():
        term = coefficient
        for j, letter in enumerate(word):
            if letter == "y":
                term *= coordinate-parameters[j] if minus else coordinate
        result += term
    return sp.expand(result)


def translate_letters(poly, parameter):
    """Apply x -> x, y -> y+parameter*x to every tensor factor."""
    result = defaultdict(lambda: sp.Integer(0))
    for word, coefficient in poly.items():
        options = [[("x", 1)] if x == "x" else [("y", 1), ("x", parameter)]
                   for x in word]
        for choices in product(*options):
            new_word = "".join(x for x, _ in choices)
            result[new_word] += coefficient * sp.prod(c for _, c in choices)
    return dict(result)


def verify_tangent():
    a, q, d, z, w = sp.symbols("a q d z w")
    parameters = [a, a+q, a+d]
    for relation in (first_relation_tangent(q, d), second_relation_tangent(q, d)):
        assert evaluate_tangent(relation, parameters, z) == 0
        assert evaluate_tangent(relation, parameters, w, minus=True) == 0
    print("PASS: both cubic relations vanish on both tangent components")

    left = quartic_left_tangent(q, d)
    assert_equal_word_sums(left, quartic_right_tangent(q, d))
    print("PASS: the two quartic expressions agree in every word coefficient")

    rotated = defaultdict(lambda: sp.Integer(0))
    for word, coefficient in left.items():
        # theta(x)=x; theta(y)=y+d*x.
        rotated[word[1:]+word[0]] += coefficient
        if word[0] == "y":
            rotated[word[1:]+"x"] += d*coefficient
    assert_equal_word_sums(rotated, quartic_left_tangent(d-q, d))
    print("PASS: theta-twisted cyclic rotation is w_(i+1)")

    f, g = first_relation_tangent(q, d), second_relation_tangent(q, d)
    assert_equal_word_sums(translate_letters(f, d/2), f)
    expected = defaultdict(lambda: sp.Integer(0), g)
    add_word_sum(expected, f, -d/2)
    assert_equal_word_sums(translate_letters(g, d/2), expected)
    print("PASS: beta preserves the cubic relation space")

    beta = sp.Matrix([[1, d/2], [0, 1]])
    theta = sp.Matrix([[1, d], [0, 1]])
    assert beta**2 == theta
    print("PASS: beta squared equals theta exactly")


if __name__ == "__main__":
    verify_transverse()
    verify_tangent()

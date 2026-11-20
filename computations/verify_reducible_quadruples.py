#!/usr/bin/env python3
"""Exact symbolic certificates for every nonintegral admissible (2,2) boundary.

Run with Python 3 and SymPy. Every assertion is a polynomial/rational-function
identity in algebraically independent a, b, r; no numerical sampling is used.

Geometric domain: a*b*r != 0, a != b, b != a*r, r != 1.
The nonzero conditions are the gluing parameters of line bundles. Equality
a=b or b=a*r makes one adjacent pair of degree-two maps identify the two
components, so it is not a closed embedding as a (2,2) divisor. Equality r=1
means L_0=L_2, excluded by the admissible-quadruple definition. For (2,1)+(0,1), the adjacent multidegrees differ, so only r!=1 or d!=0
is required. The double diagonal uses q*d*(q-d)!=0. Three/four-component and nonreduced grid types require only r!=1
or d!=0 (and nonzero multiplicative gluing parameters). The identities
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


def ribbon_first_relation(q, d):
    return {"yxx": q-d, "xyx": d, "xxy": -q}


def ribbon_second_relation(q, d):
    return {"yyx": -q, "yxy": d, "xyy": q-d}


def ribbon_quartic_left(q, d):
    result = defaultdict(lambda: sp.Integer(0))
    add_word_sum(result, ribbon_second_relation(d-q, d), prefix="x")
    add_word_sum(result, ribbon_first_relation(d-q, d), prefix="y")
    return dict(result)


def ribbon_quartic_right(q, d):
    result = defaultdict(lambda: sp.Integer(0))
    add_word_sum(result, ribbon_second_relation(q, d), suffix="x")
    add_word_sum(result, ribbon_first_relation(q, d), suffix="y")
    return dict(result)


def ribbon_verify():
    a, q, d, z, epsilon = sp.symbols("a q d z epsilon")
    parameters = [a, a+q, a+d]
    for relation in (ribbon_first_relation(q, d), ribbon_second_relation(q, d)):
        value = 0
        for word, coefficient in relation.items():
            value += coefficient * sp.prod(z+parameters[j]*epsilon
                                          for j, letter in enumerate(word)
                                          if letter == "y")
        remainder = sp.rem(sp.expand(value), epsilon**2, epsilon)
        assert sp.expand(remainder) == 0
    print("PASS: both cubic relations vanish modulo epsilon squared")

    left = ribbon_quartic_left(q, d)
    assert_equal_word_sums(left, ribbon_quartic_right(q, d))
    print("PASS: the two quartic expressions agree in every word coefficient")
    rotated = {word[1:]+word[0]: coefficient for word, coefficient in left.items()}
    assert_equal_word_sums(rotated, ribbon_quartic_left(d-q, d))
    print("PASS: ordinary cyclic rotation is w_(i+1), so theta is identity")

    # sigma_d pulls back y_i to y_(i+2) in the moving basis.
    for t in parameters:
        assert sp.expand((z+d*epsilon)+t*epsilon-(z+(t+d)*epsilon)) == 0
    print("PASS: beta is identity in moving bases and beta squared equals theta")


def mixed_relations(kind, parity, b, p):
    if kind == "transverse":
        if parity == 0:
            return ({"xxy": p, "yxx": -1, "xyx": 1-p, "yyy": b*(1-p)},
                    {"xyy": 1, "yyx": -1})
        return ({"xxy": 1, "yxx": -1, "yyy": b*(p-1)},
                {"xyy": p, "yyx": -1, "yxy": 1-p})
    if parity == 0:
        return ({"xxy": 1, "yxx": -1, "xxx": p, "xyy": -b*p, "yyy": -p},
                {"xyy": 1, "yyx": -1})
    return ({"xxy": 1, "yxx": -1, "yyy": p},
            {"xyy": 1, "yyx": -1, "yxx": p, "yyy": -p*(b+p)})


def mixed_next_data(kind, parity, b, p):
    if parity == 0:
        return 1, b
    return 0, b*p if kind == "transverse" else b+p


def mixed_quartics(kind, parity, b, p):
    next_parity, next_b = mixed_next_data(kind, parity, b, p)
    f, g = mixed_relations(kind, parity, b, p)
    nf, ng = mixed_relations(kind, next_parity, next_b, p)
    left = defaultdict(lambda: sp.Integer(0))
    right = defaultdict(lambda: sp.Integer(0))
    add_word_sum(left, ng, prefix="x")
    add_word_sum(right, f, suffix="y")
    if kind == "transverse":
        scalar = sp.Integer(1) if parity == 0 else 1/p
        add_word_sum(left, nf, -scalar, prefix="y")
        add_word_sum(right, g, -scalar, suffix="x")
    else:
        add_word_sum(left, nf, -1, prefix="y")
        add_word_sum(right, g, -1, suffix="x")
        if parity == 0:
            add_word_sum(left, nf, p, prefix="x")
        else:
            add_word_sum(left, ng, -p*(b+p), prefix="y")
    return dict(left), dict(right)


def mixed_theta(kind, parity, b, p):
    if kind == "transverse":
        return sp.diag(-1/p, -1) if parity == 0 else sp.diag(-1, -p)
    return (sp.Matrix([[-1, -p], [0, -1]]) if parity == 0
            else sp.Matrix([[-1, 0], [-p*(b+p), -1]]))


def mixed_evaluate(relation, bases):
    return sp.cancel(sum(coefficient * sp.prod(bases[j][letter]
                                              for j, letter in enumerate(word))
                         for word, coefficient in relation.items()))


def mixed_verify():
    a, b, r, d, z, w = sp.symbols("a b r d z w", nonzero=True)
    for kind, p in (("transverse", r), ("tangent", d)):
        def bundle(multidegree, t, minus):
            if kind == "transverse":
                if multidegree == 11:
                    return {"x": 1, "y": w/t if minus else z}
                return {"x": 1 if minus else 1+t*z**2, "y": 0 if minus else z}
            if multidegree == 11:
                return {"x": 1, "y": w-t if minus else z}
            return {"x": 1 if minus else z**2+t*z, "y": 0 if minus else 1}

        next_a = a*p if kind == "transverse" else a+p
        next_b = b*p if kind == "transverse" else b+p
        for parity in (0, 1):
            types = [11, 20, 11] if parity == 0 else [20, 11, 20]
            params = [a, b, next_a] if parity == 0 else [b, next_a, next_b]
            for minus in (False, True):
                bases = [bundle(md, t, minus) for md, t in zip(types, params)]
                for relation in mixed_relations(kind, parity, b, p):
                    assert mixed_evaluate(relation, bases) == 0
            left, right = mixed_quartics(kind, parity, b, p)
            assert_equal_word_sums(left, right)

            matrix = mixed_theta(kind, parity, b, p)
            rotated = defaultdict(lambda: sp.Integer(0))
            for word, coefficient in left.items():
                column = 0 if word[0] == "x" else 1
                for row, letter in enumerate("xy"):
                    rotated[word[1:]+letter] += coefficient*matrix[row, column]
            np, nb = mixed_next_data(kind, parity, b, p)
            assert_equal_word_sums(rotated, mixed_quartics(kind, np, nb, p)[0])

            if kind == "transverse":
                beta_square = sp.diag(1, p)
                scalar = -1/p if parity == 0 else -1
            elif parity == 0:
                beta = sp.Matrix([[1, p/2], [0, 1]])
                beta_square = beta**2
                scalar = -1
            else:
                v = p/2
                beta = sp.Matrix([[1, 0], [v*(b+v), 1]])
                following_beta = sp.Matrix([[1, 0], [v*(b+p+v), 1]])
                beta_square = following_beta*beta
                scalar = -1
            assert all(sp.cancel(x) == 0 for x in matrix-scalar*beta_square)
            print(f"PASS: {kind}, parity {parity}: both components, quartic identity, "
                  "rotation, and beta squared")



def multicomponent_relations(kind, parity, p):
    f = {"yxx": 1, "xxy": -1}
    g = {"yyx": 1, "xyy": -1}
    if kind == "cycle3":
        return (({"yxx": p, "xxy": -1, "xyx": 1-p}, g) if parity == 0
                else (f, {"yyx": p, "xyy": -1, "yxy": 1-p}))
    if kind == "grid4":
        return ((f, {"yyx": p, "xyy": -1}) if parity == 0
                else ({"yxx": p, "xxy": -1}, g))
    return f, {"yyx": 1, "xyy": -1, "xyx": p, "xxy": -p}



def multicomponent_quartics(kind, parity, p):
    f, g = multicomponent_relations(kind, parity, p)
    nf, ng = multicomponent_relations(kind, 1-parity, p)
    left = defaultdict(lambda: sp.Integer(0))
    right = defaultdict(lambda: sp.Integer(0))
    scalar = p if ((kind == "cycle3" and parity == 0)
                   or (kind == "grid4" and parity == 1)) else 1
    add_word_sum(left, ng, prefix="x")
    add_word_sum(left, nf, -scalar, prefix="y")
    add_word_sum(right, f, suffix="y")
    add_word_sum(right, g, -scalar, suffix="x")
    if kind == "triple3":
        add_word_sum(left, nf, -p, prefix="x")
    return dict(left), dict(right)


def multicomponent_theta(kind, parity, p):
    if kind == "triple3":
        return sp.Matrix([[-1, p], [0, -1]])
    scalar = -1 if ((kind == "cycle3" and parity == 0)
                    or (kind == "grid4" and parity == 1)) else -p
    return scalar*sp.diag(1, 1/p)



def multicomponent_verify():
    a, b, r, d, z, w, v, t = sp.symbols("a b r d z w v t", nonzero=True)
    for kind, p in (("cycle3", r), ("triple3", d), ("grid4", r)):
        def even(c):
            if kind == "cycle3":
                return [(1,z),(0,1),(1,c*v)]
            if kind == "triple3":
                return [(1,z),(0,1),(1,v+c)]
            return [(1,z),(0,1),(1,c*v),(1,0)]

        def odd(c):
            if kind == "cycle3":
                return [(1,z),(1,c*w),(1,0)]
            if kind == "triple3":
                return [(1,z),(1,w+c),(0,1)]
            return [(1,0),(1,w),(0,1),(1,c*t)]

        na, nb = ((a+p, b+p) if kind == "triple3" else (a*p, b*p))
        for parity in (0, 1):
            bundles = [even(a), odd(b), even(na)] if parity == 0 else [odd(b), even(na), odd(nb)]
            for relation in multicomponent_relations(kind, parity, p):
                for component in range(len(bundles[0])):
                    value = sum(coefficient*sp.prod(bundles[j][component]["xy".index(letter)]
                                                   for j,letter in enumerate(word))
                                for word,coefficient in relation.items())
                    assert sp.cancel(value) == 0
            left, right = multicomponent_quartics(kind, parity, p)
            assert_equal_word_sums(left, right)
            matrix = multicomponent_theta(kind, parity, p)
            rotated = defaultdict(lambda: sp.Integer(0))
            for word,coefficient in left.items():
                column = "xy".index(word[0])
                for row,letter in enumerate("xy"):
                    rotated[word[1:]+letter] += coefficient*matrix[row,column]
            assert_equal_word_sums(rotated, multicomponent_quartics(kind, 1-parity, p)[0])
            if kind == "triple3":
                beta = sp.Matrix([[1,-p/2],[0,1]])
                assert matrix == -beta**2
            else:
                assert matrix in [-sp.diag(1,1/p),-p*sp.diag(1,1/p)]
            print(f"PASS: {kind}, parity {parity}: all components, quartic, rotation, beta squared")



def grid_relations(kind, parity, d):
    f = {"yxx": 1, "xxy": -1}
    g = {"yyx": 1, "xyy": -1}
    if kind == "one_double":
        g["xyx" if parity == 0 else "xxy"] = d if parity == 0 else -d
    else:
        g["xxx"] = d if parity == 0 else -d
    return f, g



def grid_quartics(kind, parity, d):
    f,g = grid_relations(kind, parity, d)
    nf,ng = grid_relations(kind, 1-parity, d)
    left = defaultdict(lambda: sp.Integer(0))
    right = defaultdict(lambda: sp.Integer(0))
    add_word_sum(left, ng, prefix="x")
    add_word_sum(left, nf, -1, prefix="y")
    if kind == "one_double" and parity == 0:
        add_word_sum(left, nf, -d, prefix="x")
    add_word_sum(right, f, suffix="y")
    add_word_sum(right, g, -1, suffix="x")
    return dict(left),dict(right)



def grid_verify():
    a,b,d,x,y,z,epsilon,eta = sp.symbols("a b d x y z epsilon eta")
    for kind in ("one_double","both_double"):
        def even(t):
            if kind == "one_double":
                return [(epsilon,1),(1,x),(1,z+t)]
            return [(epsilon,1),(1,x+t*eta)]

        def odd(t):
            if kind == "one_double":
                return [(1,y*(1-t*epsilon)),(1,0),(0,1)]
            return [(1,y-t*epsilon),(eta,1)]

        nilpotents = [epsilon,None,None] if kind == "one_double" else [epsilon,eta]
        for parity in (0,1):
            bundles = ([even(a),odd(b),even(a+d)] if parity == 0
                       else [odd(b),even(a+d),odd(b+d)])
            for relation in grid_relations(kind,parity,d):
                for component,nilpotent in enumerate(nilpotents):
                    value = sp.expand(sum(coefficient*sp.prod(bundles[j][component]["xy".index(letter)]
                                                              for j,letter in enumerate(word))
                                          for word,coefficient in relation.items()))
                    if nilpotent is not None:
                        value = sp.rem(value,nilpotent**2,nilpotent)
                    assert sp.expand(value) == 0

            left,right = grid_quartics(kind,parity,d)
            assert_equal_word_sums(left,right)
            beta = (sp.Matrix([[1,-d/2],[0,1]]) if kind == "one_double" and parity == 0
                    else sp.eye(2))
            theta = -beta**2
            rotated = defaultdict(lambda: sp.Integer(0))
            for word,coefficient in left.items():
                column = "xy".index(word[0])
                for row,letter in enumerate("xy"):
                    rotated[word[1:]+letter] += coefficient*theta[row,column]
            assert_equal_word_sums(rotated,grid_quartics(kind,1-parity,d)[0])
            print(f"PASS: {kind}, parity {parity}: all thickened components, quartic, rotation, beta squared")

    # The gluing units on the length-four intersection multiply additively.
    u = (1+a*epsilon*eta)*(1+b*epsilon*eta)-(1+(a+b)*epsilon*eta)
    assert sp.rem(sp.rem(sp.expand(u),epsilon**2,epsilon),eta**2,eta) == 0
    # Compare the corrected pullback of both E(a) sections on every component.
    v = d/2
    correction = 1-v*epsilon
    pulled_x = [correction*epsilon,1,1]
    pulled_y = [correction,x-v,z+a+v]
    target_x = [epsilon,1,1]
    target_y = [1,x,z+a+d]
    for j in range(3):
        rx = sp.expand(pulled_x[j]-target_x[j])
        ry = sp.expand(pulled_y[j]-(target_y[j]-v*target_x[j]))
        if j == 0:
            rx = sp.rem(rx,epsilon**2,epsilon)
            ry = sp.rem(ry,epsilon**2,epsilon)
        assert sp.expand(rx) == 0 and sp.expand(ry) == 0
    odd_pullback = y*(1-d*epsilon)*(1-b*epsilon)
    assert sp.rem(sp.expand(odd_pullback-y*(1-(b+d)*epsilon)),epsilon**2,epsilon) == 0
    print("PASS: additive gluing parameter and both corrected geometric pullbacks")



if __name__ == "__main__":
    verify_transverse()
    verify_tangent()
    ribbon_verify()
    mixed_verify()
    multicomponent_verify()
    grid_verify()

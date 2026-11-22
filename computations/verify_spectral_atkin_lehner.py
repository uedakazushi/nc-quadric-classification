#!/usr/bin/env python3
"""Exact identities for the smooth spectral-avatar Atkin--Lehner comparison.

Checks two-isogeny and quotient equations, the chi-coordinate involution,
both j functions, marked self-duality, boundary poles, the inertia-center
matrix identities and its two quadratic splitting classes. It does NOT
verify categorical reconstruction, gerbe descent, or stack recognition.
Requires SymPy.  No random samples or floating-point arithmetic.
"""
import sympy as sp


def is_zero(value):
    assert sp.factor(value) == 0, value


def valuation_at(value, variable, point):
    numerator, denominator = sp.cancel(value).as_numer_denom()
    orders = []
    for polynomial in (numerator, denominator):
        order = 0
        while polynomial.subs(variable, point) == 0:
            polynomial = sp.cancel(polynomial / (variable-point))
            order += 1
        orders.append(order)
    return orders[0]-orders[1]


def relative_identities():
    x, p, a, b, chi, t, u, v = sp.symbols("x p a b chi t u v")
    quotient_x = p*x+b/x
    quotient_c = p*x-b/x
    quotient_d_squared = (p*x*x+a*x+b)/x
    is_zero(quotient_c**2-quotient_x**2+4*p*b)
    is_zero(quotient_d_squared-quotient_x-a)
    input_chi = a*a/(a*a-4*p*b)
    output_chi = a*a/(4*p*b)
    is_zero(input_chi/(input_chi-1)-output_chi)
    for exponent in (1, 2):
        is_zero(output_chi.subs({a: 1, p: 1, b: t**exponent})-1/(4*t**exponent))
    print("PASS: relative conic quotient formulas and both flat boundary models")

    r, theta = sp.symbols("r theta")
    root_b = -theta**2*(theta**2+1)
    rr = sp.diag(sp.Matrix([[0, root_b], [1, 0]]), r, r)
    tt = sp.diag(sp.Matrix([[theta**2, -root_b], [1, -theta**2]]),
                 sp.Matrix([[0, theta], [theta*(2*theta**2+1), 0]]))
    e1, e2 = sp.diag(1, 1, -1, 1), sp.diag(1, 1, 1, -1)
    simultaneous = e1*e2
    identities = [rr*rr-root_b*sp.eye(4),
                  tt*tt-theta**2*(2*theta**2+1)*sp.eye(4),
                  tt*e1-e2*tt, rr*e1-e1*rr,
                  rr*tt+simultaneous*tt*rr,
                  rr.subs(r, -r)-simultaneous*rr]
    for matrix in identities:
        for entry in matrix:
            is_zero(sp.rem(sp.expand(entry), r*r-root_b, r))
    first, second = u*v, u*u+u*v+root_b*v*v
    for matrix, multiplier in [(rr[:2, :2], root_b)]:
        uu, vv = matrix*sp.Matrix([u, v])
        is_zero(first.subs({u: uu, v: vv}, simultaneous=True)-multiplier*first)
        is_zero(second.subs({u: uu, v: vv}, simultaneous=True)-multiplier*second)
    uu, vv = tt[:2, :2]*sp.Matrix([u, v])
    is_zero(first.subs({u: uu, v: vv}, simultaneous=True)-theta**2*second)
    is_zero(second.subs({u: uu, v: vv}, simultaneous=True)
            -theta**2*(2*theta**2+1)**2*first)
    print("PASS: generic stabilizer, projective commutator, and Galois-center identities")

    center_b = (chi-1)/(4*chi)
    target_b = 1/(4*chi)
    is_zero(center_b/target_b-(chi-1))
    assert valuation_at(center_b, chi, 1) == 1
    assert valuation_at(target_b, chi, 1) == 0
    assert valuation_at(center_b, chi, 0) == -1
    assert valuation_at(target_b, chi, 0) == -1
    print("PASS: two nontrivial quadratic center classes differ at chi=1")

    hh = sp.Matrix([[0, -t, 0, 0], [1, 0, 0, 0],
                    [0, 0, 0, 1], [0, 0, -t, 0]])
    assert hh*hh == -t*sp.eye(4)
    uu, vv = -t*v, u
    is_zero(uu**2+vv**2-(u*u+t*t*v*v))
    is_zero(uu**2+t*t*vv**2-t*t*(u*u+v*v))
    print("PASS: nonsplit-pencil descent cocycle h^2=-t and form exchange")

    mixed, product, weight = sp.symbols("mixed product weight", nonzero=True)
    g1 = u*u-(mixed*mixed-product)*v*v
    g2 = u*v+mixed*v*v
    transformed = {mixed: weight**2*mixed, product: weight**4*product}
    is_zero(g1.subs(v, weight**2*v)-g1.subs(transformed, simultaneous=True))
    is_zero(g2.subs(v, weight**2*v)/weight**2
            -g2.subs(transformed, simultaneous=True))
    is_zero(sp.discriminant(g1.subs(v, 1), u)-4*(mixed*mixed-product))
    # Binary g2 has coefficients (0,1,mixed), so its discriminant is 1.
    mixed_output = -2*mixed
    is_zero(mixed_output**2/(4*(mixed*mixed-product))
            -(mixed*mixed/product)/(mixed*mixed/product-1))
    is_zero(sp.resultant(g1.subs(v, 1), g2.subs(v, 1), u)-product)
    print("PASS: weak covariant equivariance, discriminants, resultant, and coarse map")


def torsion_free_recognition_identities():
    a, f1, f2, h = sp.symbols("a f1 f2 h")
    pairing = sp.Matrix([[0, 1], [1, 0]])
    action = sp.Matrix([[a, f2], [f1, a]])
    scalar_product = sp.Matrix([[f1, a], [a, f2]])
    assert pairing.det() == -1
    assert action.T*pairing == scalar_product
    assert action*action-h*sp.eye(2) == sp.Matrix([
        [a*a+f1*f2-h, 2*a*f2],
        [2*a*f1, a*a+f1*f2-h],
    ])
    assert sp.trace(action) == 2*a
    assert action.subs(a, 0)**2 == f1*f2*sp.eye(2)
    print("PASS: Frobenius pairing and trace-zero quadratic-module normal form")

    aa, bb, cc, dd = sp.symbols("aa bb cc dd")
    matrix = sp.Matrix([[aa, bb], [cc, dd]])
    similarity = aa*dd+bb*cc
    assert matrix.T*pairing*matrix == sp.Matrix([
        [2*aa*cc, similarity], [similarity, 2*bb*dd],
    ])
    ideal = sp.groebner([aa*cc, bb*dd], aa, bb, cc, dd)
    # The numerator of e^2-e for e=aa*dd/similarity vanishes.
    assert ideal.reduce((aa*dd)**2-aa*dd*similarity)[1] == 0
    assert ideal.reduce(sp.expand(matrix.det()**2-similarity**2))[1] == 0
    print("PASS: hyperbolic similitude identities and monomial idempotent decomposition")

    x, y, left, right = sp.symbols("x y left right")
    node_product = sp.Matrix([[x, y], [y, x]])
    branch_basis = sp.Matrix([[1, 1], [1, -1]])
    diagonal_product = branch_basis.T*node_product*branch_basis
    assert diagonal_product == sp.diag(2*(x+y), 2*(x-y))
    scaling = sp.diag(left, right)
    difference = scaling.T*diagonal_product*scaling-diagonal_product-sp.diag(
        2*(x+y)*(left*left-1), 2*(x-y)*(right*right-1))
    for entry in difference:
        is_zero(entry)
    print("PASS: nodal quadratic product and independent branch-square constraints")


def main():
    x, a, b, chi, t = sp.symbols("x a b chi t")
    equation = x * (x**2 + a*x + b)
    image_x = x + a + b/x
    image_y_squared = equation * (1-b/x**2)**2
    is_zero(image_y_squared-image_x*(image_x**2-2*a*image_x+a*a-4*b))
    # Applying the coefficient transformation twice rescales by (4,16).
    aa, bb = -2*a, a*a-4*b
    is_zero(-2*aa-4*a)
    is_zero(aa*aa-4*bb-16*b)
    print("PASS: universal two-isogeny and double-dual coefficient formulas")

    w = chi/(chi-1)
    original_chi = a*a/(a*a-4*b)
    dual_chi = a*a/(4*b)
    is_zero(w.subs(chi, original_chi)-dual_chi)
    is_zero(w.subs(chi, w)-chi)
    is_zero((chi-w)*(chi-1)-chi*(chi-2))
    print("PASS: chi involution and exact fixed-point polynomial")

    def j_weierstrass(aa, bb):
        return 256*(aa*aa-3*bb)**3/(bb*bb*(aa*aa-4*bb))

    j_spectral = 64*(chi+3)**3/(chi-1)**2
    j_point = 64*(4*chi-3)**3/(chi-1)
    is_zero(j_weierstrass(a,b)-j_spectral.subs(chi, original_chi))
    is_zero(j_weierstrass(aa,bb)-j_point.subs(chi, original_chi))
    is_zero(j_spectral.subs(chi,w)-j_point)
    assert j_spectral.subs(chi,0) == 1728
    assert j_spectral.subs(chi,2) == 8000
    assert j_spectral.subs(chi,49) == sp.Rational(35152,9)
    assert j_point.subs(chi,49) == sp.Rational(28756228,3)
    assert w.subs(chi,49) == sp.Rational(49,48)
    print("PASS: both j functions, self-dual j values, chi=49 example")

    extra = 64*chi**2-81*chi+81
    is_zero((4*chi-3)**3*(chi-1)-(chi+3)**3-chi*(chi-2)*extra)
    assert sp.rem(64*(chi+3)**3+3375*(chi-1)**2,extra,chi) == 0
    is_zero(w+chi-sp.Rational(81,64)-extra/(64*(chi-1)))
    assert sp.discriminant(extra,chi) == -2025*7
    print("PASS: two exchanged marked classes with the same j=-3375")

    # Both source pairs have f1=uv. The coefficient of uv in f2 is 1.
    source_shared = 1/(1-4*t)
    source_equal = 1/(1-4*t*t)
    is_zero(w.subs(chi,source_shared)-1/(4*t))
    is_zero(w.subs(chi,source_equal)-1/(4*t*t))
    print("PASS: shared-root and equal-pair boundary pole identities")
    relative_identities()
    torsion_free_recognition_identities()
    print("NOT CHECKED: gerbe equivalence, stack closedness, infinite Ext, or novelty")


if __name__ == "__main__":
    main()

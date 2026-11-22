#!/usr/bin/env python3
"""Exact identities for the smooth spectral-avatar Atkin--Lehner comparison.

Checks the classical two-isogeny equation, the chi-coordinate involution,
both j functions, self-dual and equal-j-but-distinct marked points, and
the two boundary poles.  It does NOT verify categorical reconstruction,
pointed equivalence, or the closed-stack input in the nonextension proof.
Requires SymPy.  No random samples or floating-point arithmetic.
"""
import sympy as sp


def is_zero(value):
    assert sp.factor(value) == 0, value


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
    print("NOT CHECKED: categorical recognition, stack closedness, or novelty")


if __name__ == "__main__":
    main()

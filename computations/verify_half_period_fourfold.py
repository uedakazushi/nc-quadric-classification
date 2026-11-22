#!/usr/bin/env python3
"""Exact symbolic verification for the noncubic half-period fourfold.

Verifies the quartic-to-cubic transformation, the standard 2-isogeny,
the duplication formula, and the explicit quadratic fields of halves.
It does not prove the Albert/Springer anisotropy or period-index theorem.
"""
import sympy as s

a, b, c, x, xi, U = s.symbols('a b c x xi U', nonzero=True)
A, B = c * (b - a), b * (c - a)
D = s.expand(A - B)
quartic = x * (x - a) * (x - b) * (x - c)
z = -a * b * c / x + b * c
# Eta = abc*y/x^2, where y^2 = quartic.
assert s.factor((a*b*c/x**2)**2 * quartic - z*(z-A)*(z-B)) == 0

# Weierstrass model J(C_q): eta^2 = xi(xi-A)(xi-B).
weier = xi * (xi-A) * (xi-B)
x2is = weier / xi**2
y2is_squared = weier * (1-A*B/xi**2)**2

def target(t):
    return t * (t*t + 2*(A+B)*t + (A-B)**2)

assert s.factor(y2is_squared - target(x2is)) == 0
assert s.factor(target(D) - 4*A*D**2) == 0
assert s.factor(target(-D) - 4*B*D**2) == 0
assert s.factor(D - a*(b-c)) == 0

# Verify the duplication x-coordinate on y^2 = X(X^2+A0 X+B0).
A0, B0 = 2*(A+B), D**2
expr = U*(U**2 + A0*U + B0)
slope_squared = (3*U**2 + 2*A0*U+B0)**2/(4*expr)
duplication = slope_squared - A0 - 2*U
formula = (U**2-B0)**2/(4*expr)
assert s.factor(duplication - formula) == 0

print('PASS quartic transformation to xi(xi-A)(xi-B)')
print('PASS 2-isogeny with kernel (0,0)')
print('PASS duplication formula; half-point fields sqrt(A),sqrt(B)')
print('A =', s.factor(A), 'B =', s.factor(B))
print('Scope: exact polynomial identities; nonsquare and Brauer proofs are mathematical')

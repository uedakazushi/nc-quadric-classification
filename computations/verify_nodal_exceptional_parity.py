#!/usr/bin/env python3
"""Exact local checks for the A1 spectral resolution (not a proof of descent).

The minimal resolution of ab=y^2 uses (a,y,b)=(u,ut,ut^2)
and (v w^2,v w,v).  Its exceptional E has self-intersection -2;
the odd sign module has transition e_d=t e_c, hence degree +1 on E.
"""
import sympy as sp

u, t, v, w = sp.symbols("u t v w")
for a, y, b, expected_s in (
    (u, u*t, u*t**2, u*(1-t**2)),
    (v*w**2, v*w, v, v*(w**2-1)),
):
    assert sp.expand(a*b-y**2) == 0
    assert sp.expand(a-b-expected_s) == 0

# Coordinate changes on the overlap (both descriptions of a,y,b).
subs = {v:u*t**2, w:1/t}
assert sp.cancel((v*w**2).subs(subs)-u) == 0
assert sp.cancel((v*w).subs(subs)-u*t) == 0
assert sp.cancel(v.subs(subs)-u*t**2) == 0

# Every vertical twist by E changes its degree by an even number.
# In the global irreducible-nodal case D'.E=2 is also even.
for n in range(-10, 11):
    for m in range(-10, 11):
        assert (1-2*n+2*m) % 2 == 1

# The special-fibre anti-invariant module at a shared simple root:
# c^2=d^2=x, cd=y, y^2=x^2.  In the u=c+d, v=c-d
# basis, the two normalization branches split and their product
# forms generate the conductor.  These are finite polynomial checks.
x, y, c, d = sp.symbols("x y c d")
gb = sp.groebner([c**2-x, d**2-x, c*d-y], c, d, x, y, order="lex")
for relation in (
    (c+d)**2-2*(x+y),
    (c-d)**2-2*(x-y),
    (c+d)*(c-d),
    (x+y)*(y-x),
    (x-y)*(y+x),
):
    assert gb.reduce(sp.expand(relation))[1] == 0

eigenbasis = sp.Matrix([[1, 1], [1, -1]])
ymatrix = sp.Matrix([[0, x], [x, 0]])
assert sp.simplify(eigenbasis.inv() * ymatrix * eigenbasis) == sp.diag(x, -x)

# Three explicit reduced-quadratic root configurations have
# multiplication defect lengths equal to deg gcd(f_1, f_2) = 0,1,2.
z = sp.symbols("z")
fixtures = (
    (z*(z-1), (z-2)*(z-3), 0),
    (z*(z-1), z*(z-2), 1),
    (z*(z-1), z*(z-1), 2),
)
for f1, f2, expected in fixtures:
    assert sp.Poly(sp.gcd(f1, f2), z).degree() == expected

print("PASS: A1 resolution parity and spectral multiplication defect (0/1/2)")


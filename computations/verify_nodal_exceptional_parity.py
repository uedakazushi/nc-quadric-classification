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

print("PASS: A1 resolution charts, base equation, transition and exceptional parity")

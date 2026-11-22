#!/usr/bin/env python3
"""Exact checks for root-swap presentation matrices and conic diagonalization.

This checks polynomial identities only. It does NOT certify a nontrivial
Brauer residue, geometric descent, relative qgr equivalence, or novelty.
"""
import sympy as sp

c, s, t, lam = sp.symbols("c s t lam", nonzero=True)
M = sp.Matrix([[c, s], [t, -c]])
Mswap = sp.Matrix([[c, t], [s, -c]])
J = sp.Matrix([[0, 1], [-1, 0]])
i = sp.I
source_swap = -i * J
target_swap = i * J
assert J**2 == -sp.eye(2)
assert sp.simplify(J*M*J - Mswap) == sp.zeros(2)
assert sp.simplify(target_swap*M - Mswap*source_swap) == sp.zeros(2)
assert source_swap**2 == sp.eye(2)
assert target_swap**2 == sp.eye(2)

D = sp.diag(lam, 1)
Mscale = sp.Matrix([[c, lam*s], [t/lam, -c]])
assert sp.simplify(D*M - Mscale*D) == sp.zeros(2)
assert sp.simplify(J*D*J.inv() - lam*sp.diag(1/lam, 1)) == sp.zeros(2)

a,b,d,u,v = sp.symbols("a b d u v", nonzero=True)
delta = b*b - 4*a*d
lhs = a*(u+b*v/(2*a))**2 - delta*v*v/(4*a)
rhs = a*u*u+b*u*v+d*v*v
assert sp.factor(lhs-rhs) == 0

print("PASS: JMJ = M with root factors exchanged")
print("PASS: strict involutive chain maps using sqrt(-1)")
print("PASS: factor rescaling intertwiner and projective scalar discrepancy")
print("PASS: diagonal form of the universal generic conic")
print("Not checked: Brauer nontriviality, Galois descent, or AS qgr")

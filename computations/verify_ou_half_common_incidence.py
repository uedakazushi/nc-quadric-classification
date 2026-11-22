#!/usr/bin/env python3
"""Exact checks for the paired OU/noncubic spectral incidence.

Checks only polynomial identities, squareclass parity and generic sheet
separation.  Does not replace geometric descent or a proof of stack equivalence.
"""
import sympy as sp
from itertools import combinations
from math import prod

z1, z2, z3, t = sp.symbols('z1 z2 z3 t')
z = (z1, z2, z3, sp.Integer(1))
r = tuple(q*q for q in z)
fc = sp.prod(t-r[i] for i in (0,1))
fd = sp.prod(t-r[i] for i in (2,3))
assert sp.expand(fc*fd - sp.prod(t-q for q in r)) == 0

a,b,c = [r[j]-r[0] for j in (1,2,3)]
A = sp.factor(c*(b-a))
B = sp.factor(b*(c-a))
assert sp.expand(A-(r[3]-r[0])*(r[2]-r[1])) == 0
assert sp.expand(B-(r[2]-r[0])*(r[3]-r[1])) == 0

def valuation(expr, prime):
    return sum(e for f,e in sp.factor_list(expr)[1]
               if sp.expand(f-prime)==0 or sp.expand(f+prime)==0)
assert valuation(A,z1-1)==1 and valuation(B,z1-1)==0
assert valuation(B,z3-z1)==1 and valuation(A,z3-z1)==0

# The other two nonzero 2-torsion points on the isogenous Jacobian
# have x-coordinates -(A+B) +/- 2*sqrt(A*B); the OU spectral Jacobian
# has all of its two-torsion defined by the four rational branch points.
X = sp.symbols('X')
other_2_torsion = X**2+2*(A+B)*X+(A-B)**2
assert sp.factor(sp.discriminant(other_2_torsion, X)-16*A*B) == 0
assert valuation(A*B,z1-1)==1

# Four even sign choices modulo the global simultaneous sign.
# Fix the fourth sign to +1; the first three signs then have even parity.
values=[]
for negative in ((),(0,1),(0,2),(1,2)):
    xs=tuple(-q if i in negative else q for i,q in enumerate(z))
    s1=sum(xs)
    s3=sum(sp.prod(xs[i] for i in subset) for subset in combinations(range(4),3))
    values.append(-s3/s1)
for i,j in combinations(range(4),2):
    assert sp.factor(values[i]-values[j]) != 0
print('PASS common quartic q = product of two paired binary quadratics')
print('PASS independent squareclasses A,B; half torsor remains nonsplit over eigenvalue field')
print('PASS four rational OU halfpoint t-coordinates on ordered eigenvalue cover')
print('PASS nonsplit 2-torsion polynomial on the noncubic isogenous Jacobian')
print('Scope: exact symbolic tests; quotient-stack descent and novelty not checked')

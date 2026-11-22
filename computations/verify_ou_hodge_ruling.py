#!/usr/bin/env python3
"""Exact algebraic checks for OU diagonal Hodge ruling orientations.

Checks the normalization in lem:qa-ou-hodge-ruling-sign, not the
geometric descent theorem. Run: python3 computations/verify_ou_hodge_ruling.py
No external dependencies.
"""
from fractions import Fraction
from itertools import combinations
from math import prod

def parity(indices):
    return (-1)**sum(indices[i]>indices[j] for i in range(len(indices))
                      for j in range(i+1,len(indices)))

x=(1,2,3,5)
c=prod(x)
pairs=list(combinations(range(4),2))
for ij in pairs:
    kl=tuple(i for i in range(4) if i not in ij)
    eps=parity(ij+kl)
    hodge=eps*Fraction(c,x[kl[0]]**2*x[kl[1]]**2)
    pullback=eps*Fraction(x[ij[0]]*x[ij[1]],x[kl[0]]*x[kl[1]])
    assert hodge==pullback
    back=eps*Fraction(c,x[ij[0]]**2*x[ij[1]]**2)
    assert hodge*back==1

# Hyperbolic Segre metric q=2(ad-bc), B(a,d)=1, B(b,c)=-1.
def B(i,j):
    return 1 if (i,j) in ((0,3),(3,0)) else (
        -1 if (i,j) in ((1,2),(2,1)) else 0)
def metric(p,q):
    i,j=p; k,l=q
    return B(i,k)*B(j,l)-B(i,l)*B(j,k)
def wedge(p,q):
    return parity(p+q) if len(set(p+q))==4 else 0
for p in pairs:
    assert wedge(p,(0,1))==metric(p,(0,1))  # first ruling +
    assert -wedge(p,(0,2))==metric(p,(0,2)) # second ruling -
assert prod((-x[0],)+x[1:])==-c
print("PASS: Hodge at zero equals X-pullback; J^2=1, exact Q")
print("PASS: Segre first ruling +, second ruling -, exact Z")
print("PASS: odd sign changes interchange det(X) sheets")

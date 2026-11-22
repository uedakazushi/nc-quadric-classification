#!/usr/bin/env python3
"""Exact algebraic checks of the smooth-elliptic avatar/O-marked dictionary.

Supports the manuscript's
  thm:qa-elliptic-vdb-square-avatar-bijection
  thm:qa-elliptic-avatar-pointed-quotient
  thm:qa-avatar-two-torsion-root-pair-bijection.

Purely algebraic formal tensor exponents and rational Legendre identities.
Does NOT verify categorical equivalences, geometric descent, or stack maps.
Run: python3 computations/verify_avatar_pointed_dictionary.py
"""
from fractions import Fraction


def add(*a):
    return tuple(sum(x[i] for x in a) for i in range(len(a[0])))


def neg(x):
    return tuple(-i for i in x)


def sub(a,b):
    return add(a,neg(b))


F=(1,0,0); G=(0,1,0); P=(0,0,1)
# Square -> VdB; all entries record formal Picard tensor exponents.
def to_vdb(F,G,P):
    return (sub(F,P),sub(G,P),F)


def from_vdb(A,B,C):
    return (C,add(B,sub(C,A)),sub(C,A))


assert from_vdb(*to_vdb(F,G,P))==(F,G,P)
A,B,C=to_vdb(F,G,P)
assert to_vdb(*from_vdb(A,B,C))==(A,B,C)
eta=sub(B,A)
delta=sub(C,A)
assert eta==sub(G,F) and delta==P


def r1(F,G,P):
    return (sub(G,P),add(F,P),P)


def r0(F,G,P):
    return (G,add(F,P),P)


assert r1(*r1(F,G,P))==(F,G,P)
assert to_vdb(*r1(F,G,P))==(add(A,B,neg(C)),C,B)
assert to_vdb(*r0(F,G,P))==(B,C,add(B,C,neg(A)))
# In the r1 target, two ruling bundles coincide iff G/F = P^2.
f1,g1,p1=r1(F,G,P)
assert sub(f1,g1)==sub(sub(G,F),add(P,P))


def legendre_f(x,lamb):
    return x*(x-1)*(x-lamb)


for lamb in (Fraction(2),Fraction(3),Fraction(5),Fraction(7,3)):
    for x in (Fraction(3,2),Fraction(11,3),Fraction(-2),Fraction(13,5)):
        if x==0: continue
        x1=lamb/x
        y_scale=-lamb/(x*x)
        assert y_scale*y_scale*legendre_f(x,lamb)==legendre_f(x1,lamb)
        x2=lamb/x1
        y_scale2=-lamb/(x1*x1)
        assert x2==x and y_scale2*y_scale==1
    assert lamb/1==lamb
    assert lamb/lamb==1
    # 0 and infinity exchange; 1 and lambda exchange.
print("PASS: VdB <-> square avatar formulas inverse on Picard exponents")
print("PASS: r1 is an involution and realizes (A,B,C)->(AB/C,C,B)")
print("PASS: r0 realizes index shift (A,B,C)->(B,C,BC/A)")
print("PASS: two-cubic boundary G/F = P^2 is exact r1 ruling collision")
print("PASS: Legendre 2-torsion translation x->lambda/x, y->-lambda*y/x^2")

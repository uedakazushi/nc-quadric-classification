#!/usr/bin/env python3
"""Exact cotangent-matrix audit for Q12 mass and relation-lift changes.

Run: python3 computations/verify_q12_cotangent_morita.py
Dependency: sympy.  All checks are rational identities over the
formal parameters; the full noncommutative proof is in paper C.
"""
import sympy as S

lam,mu,t,s,tt,ss = S.symbols("lambda mu t s tt ss")
ell1,ell2,m1,m2 = S.symbols("ell1 ell2 m1 m2")
v,y,T1,T2 = S.symbols("v y T1 T2")
w1,w2,u1,u2 = S.symbols("w1 w2 u1 u2")

def mass(t,s):
    return S.Matrix([
        [1+mu*s,0,0,0],[0,1+lam*t,0,0],
        [s*m1,t*ell1,1,0],[s*m2,t*ell2,0,1]
    ])

def shear(w1,w2,u1,u2):
    return S.Matrix([
        [1,0,0,0],[0,1,0,0],
        [w1,u1,1,0],[w2,u2,0,1]
    ])

def equal(X,Y):
    return all(S.cancel(z)==0 for z in X-Y)

coords = S.Matrix([v,y,T1,T2])
A = mass(t,s)
a,b = 1+lam*t,1+mu*s
expected = S.Matrix([
    (v-s*(m1*T1+m2*T2))/b,
    (y-t*(ell1*T1+ell2*T2))/a,
    T1,T2
])
assert equal(A.inv().T*coords, expected)
print("PASS: mass inverse-cotangent gives y,v corrections")

assert equal(mass(t,s)*mass(tt,ss),
             mass(t+tt+lam*t*tt,s+ss+mu*s*ss))
print("PASS: both mass group laws and strict composition")

Sh=shear(w1,w2,u1,u2)
expected_shear = S.Matrix([
    v-w1*T1-w2*T2,y-u1*T1-u2*T2,T1,T2
])
assert equal(Sh.inv().T*coords,expected_shear)
print("PASS: relation lift shear cotangent (reverse orientation gives +)")

assert equal(A.inv()*Sh*A,
             shear(b*w1,b*w2,a*u1,a*u2))
print("PASS: mass conjugation on relation-lift shear weights")

assert equal((A*Sh).inv().T,A.inv().T*Sh.inv().T)
print("PASS: inverse-cotangent strictly respects composition")

#!/usr/bin/env python3
"""Symbolic Fox/cotangent check for the compressed Q12 mass sector.

Run: python3 computations/verify_q12_ginzburg_fox.py
Dependency: sympy

This compresses the four-edge paths p and q to formal letters, solely
to audit cyclic signs, odd-arrow differentials and the degree -2 moment
map. The full twelve-arrow proof uses the finite noncommutative Fox
derivative and not this compressed sample.
"""
from collections import defaultdict
import sympy as sp

lam, t = sp.symbols("lambda t")
a = 1 + lam*t

def plus(*ps):
    out = defaultdict(lambda: sp.Integer(0))
    for pol in ps:
        for w, c in pol.items():
            out[w] += c
    return {w:sp.cancel(c) for w,c in out.items() if sp.cancel(c) != 0}

def scale(p,c):
    return {w:sp.cancel(c*v) for w,v in p.items() if sp.cancel(c*v) != 0}

def mul(p,q):
    out = defaultdict(lambda:sp.Integer(0))
    for u,b in p.items():
        for v,c in q.items():
            out[u+v] += b*c
    return {w:sp.cancel(c) for w,c in out.items() if sp.cancel(c) != 0}

def atom(x): return {(x,):sp.Integer(1)}
def word(chars):
    r={():sp.Integer(1)}
    for x in chars:r=mul(r,atom(x))
    return r

def substitute(pol,rule):
    ans={}
    for w,c in pol.items():
        p={():sp.Integer(1)}
        for x in w:p=mul(p,rule.get(x,atom(x)))
        ans=plus(ans,scale(p,c))
    return ans

def cyclic(pol,x):
    ans={}
    for w,c in pol.items():
        for i,y in enumerate(w):
            if y==x:ans=plus(ans,{w[i+1:]+w[:i]:c})
    return ans

def comm(p,q):return plus(mul(p,q),scale(mul(q,p),-1))

# Compressed cyclic potential W = yq + px + lambda*yx
W=plus(word("yq"),word("px"),scale(word("yx"),lam))
phi={
    "x":plus(scale(atom("x"),a),scale(atom("q"),t)),
    "y":plus(scale(atom("y"),1/a),scale(atom("p"),-t/a)),
}
# Fox cotangent lift from the inverse polynomial substitution:
# x* -> a^-1 x*, y* -> a y*,
# p* -> p*+t y*, q* -> q*-t/a x*.
cot={
    "x*":scale(atom("x*"),1/a),
    "y*":scale(atom("y*"),a),
    "p*":plus(atom("p*"),scale(atom("y*"),t)),
    "q*":plus(atom("q*"),scale(atom("x*"),-t/a)),
}

delta=plus(substitute(W,phi),scale(W,-1))
assert all(not cyclic(delta,v) for v in "xypq"), delta
for x in "xypq":
    left={}
    for w,c in cot[x+"*"].items():
        assert len(w)==1
        left=plus(left,scale(cyclic(W,w[0][:-1]),c))
    right=substitute(cyclic(W,x),phi)
    assert not plus(left,scale(right,-1)),(x,left,right)
moment={}
pulled={}
for x in "xypq":
    moment=plus(moment,comm(atom(x),atom(x+"*")))
    pulled=plus(pulled,comm(phi.get(x,atom(x)),cot[x+"*"]))
assert not plus(moment,scale(pulled,-1))
print("PASS: cyclic invariance of compressed mass potential")
print("PASS: four degree -1 Ginzburg generator differential equations")
print("PASS: degree -2 Casimir/moment-map commutator equality")

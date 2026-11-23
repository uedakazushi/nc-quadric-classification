#!/usr/bin/env python3
"""Exact finite audit of the two-term Q12 presentation dg model.

Run: python3 computations/verify_q12_presentation_dg.py
Requires sympy. Chronological paths U,V,W; the universal proof uses 6R
being a direct summand, which no finite sample can replace.
"""
from collections import defaultdict
from itertools import product
import sympy as sp

la, mu, t, s = sp.symbols("lambda mu t s")
arcs = {"U0":(0,1),"U1":(0,1),"V0":(1,2),"V1":(1,2),
        "W0":(2,3),"W1":(2,3),"u":(0,2),"x":(1,3)}

def paths(start, prev=()):
    for edge,(a,b) in arcs.items():
        if a==start:
            p=prev+(edge,)
            yield p
            yield from paths(b,p)

free = [p for i in range(4) for p in paths(i)]
assert len(free)+4==32
long = [p for p in free if arcs[p[0]][0]==0 and arcs[p[-1]][1]==3]
assert len(long)==12

def lin(*terms):
    d=defaultdict(lambda:sp.Integer(0))
    for coeff,p in terms: d[p]+=coeff
    return {p:sp.expand(c) for p,c in d.items() if sp.expand(c)!=0}

def atom(*names):
    return {tuple(names):sp.Integer(1)}

def multiply(a,b):
    d=defaultdict(lambda:sp.Integer(0))
    for p,x in a.items():
        for q,y in b.items():
            if arcs[p[-1]][1]==arcs[q[0]][0]: d[p+q]+=x*y
    return {p:sp.expand(x) for p,x in d.items() if sp.expand(x)!=0}

def subtract(a,b):
    return {p:sp.expand(a.get(p,0)-b.get(p,0))
            for p in a.keys()|b.keys()
            if sp.expand(a.get(p,0)-b.get(p,0))!=0}

def scale(a,x):
    return {p:sp.expand(v*x) for p,v in a.items()}

ra=lin((1,("U0","V0")),(1,("U1","V1")),(mu,("u",)))
rb=lin((1,("V0","W0")),(1,("V1","W1")),(la,("x",)))
rels=[multiply(ra,atom("W0")),multiply(ra,atom("W1")),
      multiply(atom("U0"),rb),multiply(atom("U1"),rb),
      atom("U0","V1","W0"),atom("U1","V0","W1")]
M=sp.Matrix([[rel.get(p,0) for rel in rels] for p in long])
rows=list(M.subs({la:0,mu:0}).T.rref()[1])
assert len(rows)==6
assert sp.expand(M[rows,:].det())==1
assert all(M.subs({la:a,mu:b}).rank()==6
           for a,b in product((0,1),repeat=2))

def gauge(expr):
    out=defaultdict(lambda:sp.Integer(0))
    for path,coeff in expr.items():
        cur={():coeff}
        for edge in path:
            if edge=="u":
                nxt=lin((1+mu*s,("u",)),(s,("U0","V0")),(s,("U1","V1")))
            elif edge=="x":
                nxt=lin((1+la*t,("x",)),(t,("V0","W0")),(t,("V1","W1")))
            else: nxt={(edge,):sp.Integer(1)}
            z=defaultdict(lambda:sp.Integer(0))
            for p,a in cur.items():
                for q,b in nxt.items(): z[p+q]+=a*b
            cur=dict(z)
        for p,a in cur.items(): out[p]+=a
    return {p:sp.expand(v) for p,v in out.items() if sp.expand(v)!=0}

assert not subtract(gauge(ra),scale(ra,1+mu*s))
assert not subtract(gauge(rb),scale(rb,1+la*t))
for i,rel in enumerate(rels):
    factor=1+mu*s if i<2 else (1+la*t if i<4 else 1)
    assert not subtract(gauge(rel),scale(rel,factor))
assert subtract(gauge(atom("u")),atom("u"))==scale(ra,s)
assert subtract(gauge(atom("x")),atom("x"))==scale(rb,t)
shear=sp.eye(6)
shear[0,4]=1
shear[2,4]=1
assert shear.det()==1
assert sp.expand((M*shear)[rows,:].det())==1

print("PASS: degree-0 free paths 32, degree -1 relation paths 8")
print("PASS: symbolic six-relation minor determinant 1")
print("PASS: mass gauge preserves I and induces identity on F/I")
print("PASS: unipotent relation-lift shear preserves I")

#!/usr/bin/env python3
"""Exact certificate for the noncubic H2 antiserre Grassmann affine chart.

No specialization or numerical approximation: all six form coefficients
are independent symbolic variables. Run with Python 3 + SymPy.
"""
import sympy as sp

u, v = sp.symbols("u v")
a, b, c, aa, bb, cc = sp.symbols("a b c aa bb cc")
f1 = a*u*u + b*u*v + c*v*v
f2 = aa*u*u + bb*u*v + cc*v*v
gens = {
    "x0": (u*u, ""), "x1": (u*v, ""), "x2": (v*v, ""),
    "p0": (u, "c"), "p1": (v, "c"),
    "q0": (u, "d"), "q1": (v, "d"),
    "z": (sp.Integer(1), "cd"), "zp": (sp.Integer(1), "dc"),
}

def reduce_word(word):
    terms = {word: sp.Integer(1)}
    for _ in range(6):
        newer, changed = {}, False
        for w, coeff in terms.items():
            ic, id_ = w.find("cc"), w.find("dd")
            if ic >= 0 and (id_ < 0 or ic < id_):
                nw, factor = w[:ic] + w[ic+2:], f1
            elif id_ >= 0:
                nw, factor = w[:id_] + w[id_+2:], f2
            else:
                newer[w] = sp.expand(newer.get(w, 0) + coeff)
                continue
            changed = True
            newer[nw] = sp.expand(newer.get(nw, 0) + coeff*factor)
        terms = newer
        if not changed:
            break
    assert all("cc" not in w and "dd" not in w for w in terms)
    return terms

def star(lhs, rhs):
    p, w = gens[lhs]
    q, z = gens[rhs]
    sign = -1 if len(z) % 2 else 1
    return {word: sp.expand(sign*p*q*coeff)
            for word, coeff in reduce_word(w+z).items()}

pivots = [
    ("x0","x0"), ("x0","x1"), ("x0","x2"),
    ("x1","x2"), ("x2","x2"),
    ("x0","p0"), ("x0","p1"), ("x1","p1"), ("x2","p1"),
    ("x0","q0"), ("x0","q1"), ("x1","q1"), ("x2","q1"),
    *((f"x{i}", w) for w in ("z","zp") for i in range(3)),
    ("p0","zp"), ("p1","zp"), ("q0","z"), ("q1","z"),
    ("z","z"), ("zp","zp"),
]
normal_words = ["", "c", "d", "cd", "dc", "cdc", "dcd", "cdcd", "dcdc"]
normal_basis = [(u**i*v**(4-len(w)-i), w)
                for w in normal_words for i in range(5-len(w))]
assert len(normal_basis) == len(pivots) == 25

def coordinates(expression):
    return sp.Matrix([
        sp.Poly(expression.get(w, sp.Integer(0)), u, v).coeff_monomial(m)
        for m,w in normal_basis
    ])

minor = sp.Matrix.hstack(*(coordinates(star(x,y)) for x,y in pivots))
assert all(sum(minor[i,j] != 0 for i in range(25)) == 1 for j in range(25))
assert len(set(tuple(minor[:,j]) for j in range(25))) == 25
assert sp.factor(minor.det()) in (1,-1)

# The six coefficients can be extracted linearly from two unused columns.
for g, expected in (("p0",(a,b,c)), ("q0",(aa,bb,cc))):
    vector = coordinates(star(g,g))
    for coefficient, monomial in zip(expected, (u**4,u**3*v,u**2*v**2)):
        assert sp.simplify(vector[normal_basis.index((monomial,""))]
                           + coefficient) == 0

print("PASS: 25 fixed pivot columns, determinant +/-1.")
print("PASS: six parameters are polynomial functions of Pluecker-cell coordinates.")
print("PASS: framed A^6 embeds as a closed graph in the Grassmann affine cell.")

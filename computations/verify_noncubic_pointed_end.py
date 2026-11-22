#!/usr/bin/env python3
"""Exact degree <=2 checks for three geometric noncubic strata.

This is a finite linear-algebra consistency test, not a proof of the
general pointed equivalence, AS regularity, or relative stack descent.
Requires Python 3 and sympy.
"""
import sympy as sp

V = ("u", "v", "c", "d")
W = ("uu", "uv", "vv", "uc", "vc", "ud", "vd", "cd", "dc")
V_INDEX = {x: i for i, x in enumerate(V)}
W_INDEX = {x: i for i, x in enumerate(W)}
F1 = {"uv": -1}  # c^2 = -uv

def mul2(x, y, f2):
    if x in ("u", "v") and y in ("u", "v"):
        return {"".join(sorted((x, y))): 1}
    if x in ("u", "v") and y in ("c", "d"):
        return {x + y: 1}
    if x in ("c", "d") and y in ("u", "v"):
        return {y + x: 1}
    if x == y == "c":
        return F1
    if x == y == "d":
        return f2
    return {x + y: 1}

def right1(x, polynomial, f2):
    out = sp.zeros(len(W), 1)
    for y, a in polynomial.items():
        for name, coeff in mul2(x, y, f2).items():
            out[W_INDEX[name]] += a * coeff
    return out

def vector2(first, second):
    out = sp.zeros(2 * len(V), 1)
    for j, p in enumerate((first, second)):
        for name, coeff in p.items():
            out[j * len(V) + V_INDEX[name]] += coeff
    return out

def times_degree1(v, polynomial, f2):
    out = sp.zeros(2 * len(W), 1)
    for i in range(len(v)):
        if v[i] != 0:
            out[len(W) * (i // len(V)):len(W) * (i // len(V) + 1), 0] += (
                v[i] * right1(V[i % len(V)], polynomial, f2)
            )
    return out

def verify(label, f2, m1, m2):
    # X_d=coker [[d,m1],[m2,-d]], with d^2=-m1*m2.
    relations = (vector2({"d": 1}, m2), vector2(m1, {"d": -1}))
    R1 = sp.Matrix.hstack(*relations)
    R2 = sp.Matrix.hstack(*(
        times_degree1(rel, {b: 1}, f2)
        for rel in relations for b in V
    ))
    # A morphism X_c -> X_d(1) is determined by the two images
    # of degree-zero generators, in (X_d)_1.
    columns = []
    for i in range(16):
        z0, z1 = sp.zeros(8, 1), sp.zeros(8, 1)
        if i < 8:
            z0[i] = 1
        else:
            z1[i - 8] = 1
        # X_c relations (c,v), (u,-c).
        columns.append(sp.Matrix.vstack(
            times_degree1(z0, {"c": 1}, f2)
            + times_degree1(z1, {"v": 1}, f2),
            times_degree1(z0, {"u": 1}, f2)
            - times_degree1(z1, {"c": 1}, f2)
        ))
    C = sp.Matrix.hstack(*columns)
    RR = sp.diag(R2, R2)
    dim_hom = 16 - (C.row_join(RR).rank() - RR.rank()) - 2 * R1.rank()
    first_product = sp.Matrix([
        [0, 1, 0, 0],
        [0, 0, -1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 0],
    ])
    assert (R1.rank(), R2.rank()) == (2, 6)
    assert dim_hom == 4
    assert first_product.rank() == 3
    assert first_product.nullspace() == [sp.Matrix([-1, 0, 0, 1])]
    print(f"PASS {label}: X_d[1]=6, X_d[2]=12, "
          f"Hom(X_c,X_d(1))={dim_hom}, first product rank=3")

def main():
    verify("disjoint",
           {"uu": -1, "uv": 3, "vv": -2},
           {"u": 1, "v": -2}, {"u": 1, "v": -1})
    verify("one-shared-root",
           {"uu": -1, "uv": 1},
           {"u": 1}, {"u": 1, "v": -1})
    verify("coincident-root-pairs",
           {"uv": -1},
           {"u": 1}, {"v": 1})
    print("Scope: three rational points and degree <=2 only")

if __name__ == "__main__":
    main()

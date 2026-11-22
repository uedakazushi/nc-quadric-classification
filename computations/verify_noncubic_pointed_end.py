#!/usr/bin/env python3
"""Exact QQ check for smooth noncubic pointed End; one example, degrees <= 2.
B=k[u,v]<c,d>/(c^2+uv,d^2+(u-v)(u-2v)).
Requires sympy; does not certify AS regularity or full pointed equivalence.
"""
import sympy as S

B1 = ("u", "v", "c", "d")
B2 = ("uu", "uv", "vv", "uc", "vc", "ud", "vd", "cd", "dc")
i1 = {x: j for j, x in enumerate(B1)}
i2 = {x: j for j, x in enumerate(B2)}
f1 = {"uv": -1}
f2 = {"uu": -1, "uv": 3, "vv": -2}

def mul(x, y):
    if x in "uv" and y in "uv":
        return {"".join(sorted(x+y)): 1}
    if x in "uv" and y in "cd":
        return {x+y: 1}
    if x in "cd" and y in "uv":
        return {y+x: 1}
    if x == y == "c":
        return f1
    if x == y == "d":
        return f2
    return {x+y: 1}

def right(x, b):
    out = S.zeros(9, 1)
    for y, a in b.items():
        for mon, coeff in mul(x, y).items():
            out[i2[mon]] += a*coeff
    return out

def vec(first, second):
    out = S.zeros(8, 1)
    for term, coeff in first.items():
        out[i1[term]] += coeff
    for term, coeff in second.items():
        out[4+i1[term]] += coeff
    return out

def rm(v, b):
    out = S.zeros(18, 1)
    for j in range(8):
        if v[j]:
            out[9*(j//4):9*(j//4)+9, 0] += v[j]*right(B1[j % 4], b)
    return out

rd1 = vec({"d": 1}, {"u": 1, "v": -2})
rd2 = vec({"u": 1, "v": -1}, {"d": -1})
R1 = S.Matrix.hstack(rd1, rd2)
R2 = S.Matrix.hstack(*(rm(r, {b: 1})
                         for r in (rd1, rd2) for b in B1))
assert (R1.rank(), R2.rank()) == (2, 6)
assert (8-R1.rank(), 18-R2.rank()) == (6, 12)

# Xc has column relations (c,v) and (u,-c).
# A map Xc -> Xd(1) is determined by 2 images in (Xd)_1.
columns = []
for j in range(16):
    w0, w1 = S.zeros(8, 1), S.zeros(8, 1)
    if j < 8:
        w0[j] = 1
    else:
        w1[j-8] = 1
    columns.append(S.Matrix.vstack(
        rm(w0, {"c": 1}) + rm(w1, {"v": 1}),
        rm(w0, {"u": 1}) - rm(w1, {"c": 1})))
conditions = S.Matrix.hstack(*columns)
rel = S.diag(R2, R2)
raw_dim = 16 - (conditions.row_join(rel).rank() - rel.rank())
assert raw_dim == 8
assert raw_dim - 2*R1.rank() == 4

# Dual MCM evaluation first product has entries [c,u,-v,c].
first_product = S.Matrix([
    [0, 1, 0, 0], [0, 0, -1, 0],
    [1, 0, 0, 1], [0, 0, 0, 0]])
assert first_product.rank() == 3
assert first_product.nullspace() == [S.Matrix([-1, 0, 0, 1])]
print("PASS QQ: Xd degree 1=6, degree 2=12; Hom(Xc,Xd(1))=4")
print("PASS QQ: first product rank 3, alternating kernel dimension 1")
print("Scope: one smooth rational example, low degree only")

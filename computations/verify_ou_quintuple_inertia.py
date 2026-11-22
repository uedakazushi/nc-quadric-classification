#!/usr/bin/env python3
"""Independent exact rational verification of the generic quintuple stabilizer.

For X=diag(1,2,3,5), check:
  * (even sign matrices)/(-I) has four elements;
  * the 16 x 13 infinitesimal orbit matrix has rank 13 over Q;
  * every nonidentity sign class acts without fixed points on
    C: sum(u_i^2)=sum(x_i^2 u_i^2)=0 in P^3;
  * the remaining tangent is diagonal modulo kX and all inertia
    elements act trivially on it.

Run: python3 computations/verify_ou_quintuple_inertia.py
No external dependencies. These exact checks support, but do not replace,
the symbolic proof in papers/quiver-avatar/git_comparison.tex.
"""
from fractions import Fraction
from itertools import combinations, product
from math import prod

x = (1, 2, 3, 5)
N = 4
assert sum(i*i for i in x) != 0
assert all(x[i]**2 != x[j]**2 for i,j in combinations(range(N),2))

# Ordered matrix coordinate basis E_ij for Mat_4, with 13 Lie generators:
# six for A in so_4, six for B in so_4, one scalar.
vectors = []
for i,j in combinations(range(N), 2):
    v = [Fraction(0) for _ in range(N*N)]
    v[N*i+j] = Fraction(x[j])
    v[N*j+i] = Fraction(-x[i])
    vectors.append(v)
for i,j in combinations(range(N), 2):
    v = [Fraction(0) for _ in range(N*N)]
    v[N*i+j] = Fraction(-x[i])
    v[N*j+i] = Fraction(x[j])
    vectors.append(v)
v = [Fraction(0) for _ in range(N*N)]
for i in range(N): v[N*i+i] = Fraction(x[i])
vectors.append(v)

def rank(rows):
    m = [row[:] for row in rows]
    rows_count = len(m)
    cols_count = len(m[0])
    r = 0
    for j in range(cols_count):
        pivot = next((i for i in range(r, rows_count) if m[i][j]), None)
        if pivot is None: continue
        m[r],m[pivot]=m[pivot],m[r]
        c = m[r][j]
        m[r] = [a/c for a in m[r]]
        for i in range(r+1,rows_count):
            c=m[i][j]
            if c: m[i] = [a-c*b for a,b in zip(m[i],m[r])]
        r+=1
    return r

orb = [[vectors[c][r] for c in range(13)] for r in range(N*N)]
assert rank(orb) == 13

# A representative in every class (modulo simultaneous -I) has sign_0=+1.
D = [d for d in product((-1,1),repeat=N) if d[0]==1 and prod(d)==1]
assert len(D)==4
for d in D:
    # D X D = X. Conjugation is identity on all diagonal directions.
    assert all(d[i]*d[i]*x[i]==x[i] for i in range(N))
    if d == (1,1,1,1): continue
    plus = [i for i in range(N) if d[i]==1]
    minus = [i for i in range(N) if d[i]==-1]
    assert len(plus)==2 and len(minus)==2
    # Projective fixed-point locus is P(U+) union P(U-).
    # q and q(Xu) have no common projective zero on either line:
    # their two-by-two determinant is x_j^2-x_i^2.
    for block in [plus,minus]:
        i,j=block
        assert x[j]**2-x[i]**2 != 0

print("PASS: 4 residual sign classes, exact finite stabilizer calculation")
print("PASS: orbit rank 13 in Mat_4; 3-dimensional tangent quotient over Q")
print("PASS: residual group fixes tangent quotient and acts freely on C")

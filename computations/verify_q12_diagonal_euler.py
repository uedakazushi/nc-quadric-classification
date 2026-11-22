"""Exact rank/Euler/Hilbert checks for the Q12 finite normal foundation.

Run: python3 computations/verify_q12_diagonal_euler.py
Needs SymPy. Euler consistency is necessary but not sufficient for
exactness of the relative diagonal resolution; its proof is in the TeX.
"""
import sympy as sp

# dim(e_target Lambda e_source), normal four-vertex foundation
A = [[1, 0, 0, 0],
     [2, 1, 0, 0],
     [4, 2, 1, 0],
     [6, 4, 2, 1]]
# (target, source, multiplicity), forward arrows and relations
V = [(1, 0, 2), (2, 1, 2), (3, 2, 2),
     (2, 0, 1), (3, 1, 1)]
R = [(2, 0, 1), (3, 1, 1), (3, 0, 2)]


def component(p, q):
    d0 = sum(A[p][k] * A[k][q] for k in range(4))
    d1 = sum(m * A[p][t] * A[s][q] for t, s, m in V)
    d2 = sum(m * A[p][t] * A[s][q] for t, s, m in R)
    return d0, d1, d2


assert sum(sum(row) for row in A) == 24
assert sum(mult for _, _, mult in V) == 8
assert sum(mult for _, _, mult in R) == 4
total = [0, 0, 0]
for target in range(4):
    for source in range(4):
        d0, d1, d2 = component(target, source)
        assert d0 - d1 + d2 == A[target][source], (target, source)
        total = [x + y for x, y in zip(total, [d0, d1, d2])]
assert total == [68, 52, 8]
print("PASS: 16 vertex-pair Euler equalities; (68, 52, 8) -> 24")

G = sp.Matrix([[1, 2, 4, 6], [0, 1, 2, 4],
               [0, 0, 1, 2], [0, 0, 0, 1]])
S = G.inv() * G.T
N = S.inv() - sp.eye(4)
assert N**3 == sp.zeros(4)
n = sp.symbols("n", integer=True, nonnegative=True)
Sinv_power = sp.eye(4) + n * N + n*(n-1) * N**2 / 2
ones = sp.ones(4, 1)
total_hilbert = sp.expand((ones.T * G * Sinv_power * ones)[0])
assert sp.simplify(total_hilbert - (64*n**2 + 64*n + 24)) == 0
print("PASS: normal Serre Euler rank is 64*n^2 + 64*n + 24")
print("All Q12 diagonal numerical/Serre checks passed.")

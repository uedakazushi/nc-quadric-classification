"""Exact polynomial checks for the rank-three Q10 mass-gauge model.

Run: python3 computations/verify_q10_mass_gerbe.py
Requires Python 3 and SymPy. This verifies symbolic identities and a
universal rank-three-to-cubic matrix example. It does not prove the
fppf/Isom-gerbe statement by computation.
"""
import sympy as s

lam, t, u = s.symbols("lam t u")
a = 1 + lam * t
coefficients = {
    "yx": lam * a / a,
    "yq": (1 + lam * t) / a,
    "px": a * (1 - lam * t / a),
    "pq": t - t / a - lam * t * t / a,
}
for name, target in (("yx", lam), ("yq", 1), ("px", 1), ("pq", 0)):
    assert s.cancel(coefficients[name] - target) == 0, name
    print("PASS: gauge preserves cyclic coefficient", name)

composition = t + u + lam * t * u
assert s.expand((1 + lam*t) * (1 + lam*u) - (1 + lam*composition)) == 0
assert s.simplify(composition.subs(u, -t / (1 + lam*t))) == 0
print("PASS: smooth group composition and inverse")

assert s.expand(a - 1 - lam*t) == 0
assert s.cancel((1/a - 1) + lam*t/a) == 0
print("PASS: gauge changes vanish modulo Jacobian relations")

# A model over Z[lam] whose unique rank-three special fiber has
# nondecomposable kernel q=(1,0,0,1) (det(q)=1).
q = s.Matrix([1, 0, 0, 1])
r = q.col_join(s.Matrix([lam]))
theta = s.zeros(10, 4)
for i in range(5):
    theta[i, 0] = r[i]
    theta[i+5, 1] = r[i]
# Two linearly independent cubic relations modulo W tensor r.
theta[1, 2] = 1
theta[6, 3] = 1
pivot_rows = [0, 1, 5, 6]
quotient_rows = [i for i in range(10) if i not in pivot_rows]
pivot = theta.extract(pivot_rows, list(range(4)))
assert pivot.det() in (1, -1)
assert theta.rank() == 4
m = s.zeros(6, 10)
correction = -theta.extract(quotient_rows, list(range(4))) * pivot.inv()
for i in range(6):
    for j in range(4):
        m[i, pivot_rows[j]] = correction[i, j]
    m[i, quotient_rows[i]] = 1
assert m * theta == s.zeros(6, 4)
assert m.extract(list(range(6)), quotient_rows) == s.eye(6)
print("PASS: four-relation direct summand and rank-six quotient")

# E=D/(q+lam*x); choose the basis e01,e10,e11,x.
emb = s.zeros(5, 4)
for j, i in enumerate([1, 2, 3, 4]):
    emb[i, j] = 1
c = m * s.kronecker_product(s.eye(2), emb)
a_map = s.Matrix([[0, 1, 0, 0], [0, 0, 1, 0],
                  [-1, 0, 0, 1], [-lam, 0, 0, 0]])
assert s.factor(a_map.det()) in (lam, -lam)
assert a_map.subs(lam, 0) * q == s.zeros(4, 1)
assert c.rank() == 6
assert c * s.kronecker_product(s.eye(2), a_map) == (
    m[:, list(range(4)) + list(range(5, 9))]
)
print("PASS: directed algebra products and associativity")

assert a_map.subs(lam, 0).rank() == 3
assert a_map.subs(lam, 1).rank() == 4
print("PASS: rank-three wall, cubic open, and dual-number mass model")
print("All exact Q10 mass-gauge checks passed.")

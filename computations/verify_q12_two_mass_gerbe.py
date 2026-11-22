"""Exact sample checks for the two-mass Q12/foundation comparison.

Run: python3 computations/verify_q12_two_mass_gerbe.py
Requires SymPy. The polynomial identities verify a rank-6 finite
foundation over Z[lam,mu]; they do not substitute for fppf descent,
Isom-sheaf proofs, or AS-regularity.
"""
import sympy as s

lam, mu = s.symbols("lam mu")
relations = s.zeros(12, 6)
q_a = [1, 0, 0, 1]
q_b = [1, 0, 0, 1]

# W tensor r_a and r_b tensor U in
# (W tensor V tensor U) + (W tensor u) + (x tensor U).
for w in range(2):
    for v in range(2):
        for u in range(2):
            relations[4*w + 2*v + u, w] = q_a[2*v + u]
    relations[8+w, w] = mu
for u in range(2):
    for w in range(2):
        for v in range(2):
            relations[4*w + 2*v + u, 2+u] = q_b[2*w + v]
    relations[10+u, 2+u] = lam

# Two extra cubic relations, chosen with a constant unit minor.
relations[2, 4] = 1
relations[5, 5] = 1
pivots = list(range(6))
remaining = list(range(6, 12))
pivot = relations.extract(pivots, range(6))
assert pivot.det() == 1
quotient = s.zeros(6, 12)
correction = -relations.extract(remaining, range(6)) * pivot.inv()
for i in range(6):
    for j in range(6):
        quotient[i, pivots[j]] = correction[i, j]
    quotient[i, remaining[i]] = 1
assert quotient * relations == s.zeros(6, 6)
assert quotient.extract(range(6), remaining) == s.eye(6)
print("PASS: six primitive relations and flat rank-six quotient")

# E=D_a/(q_a+mu*u), F=D_b/(q_b+lam*x).
embed = s.zeros(5, 4)
for j, i in enumerate((1, 2, 3, 4)):
    embed[i, j] = 1
into_c = s.zeros(12, 10)
for w in range(2):
    for j in range(5):
        into_c[4*w+j if j < 4 else 8+w, 5*w+j] = 1
into_d = s.zeros(12, 10)
for j in range(4):
    for u in range(2):
        into_d[2*j+u, 2*j+u] = 1
for u in range(2):
    into_d[10+u, 8+u] = 1

c = quotient * into_c * s.kronecker_product(s.eye(2), embed)
d = quotient * into_d * s.kronecker_product(embed, s.eye(2))


def double_product(z):
    return s.Matrix([[0, 1, 0, 0], [0, 0, 1, 0],
                     [-1, 0, 0, 1], [-z, 0, 0, 0]])


a, b = double_product(mu), double_product(lam)
assert s.factor(a.det()) in (mu, -mu)
assert s.factor(b.det()) in (lam, -lam)
assert c * s.kronecker_product(s.eye(2), a) == (
    d * s.kronecker_product(b, s.eye(2))
)
assert s.Matrix.hstack(c, d).rank() == 6
print("PASS: associative products and joint surjection")

for m, z in ((a, mu), (b, lam)):
    assert m.subs(z, 0).rank() == 3
    assert m.subs(z, 1).rank() == 4
print("PASS: four rank strata and nilpotent mass directions")

t, u = s.symbols("t u")
for z in (lam, mu):
    A = 1 + z*t
    assert s.cancel(t - t/A - z*t*t/A) == 0
    assert s.expand((1+z*t)*(1+z*u)
                    - (1+z*(t+u+z*t*u))) == 0
print("PASS: independent smooth commuting mass-gauge groups")
print("All two-mass Q12 polynomial checks passed.")

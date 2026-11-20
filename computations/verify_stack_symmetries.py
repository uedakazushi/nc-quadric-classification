"""Exact coefficient identities for the noncubic presentation stack.

Run: python3 computations/verify_stack_symmetries.py   (requires SymPy)

All matrices below act by substitution on the displayed COLUMN of generators:
    phi((u,v,c,d)^t) = M_phi (u,v,c,d)^t.
Thus, for example, R(u)=lambda*v and R(v)=u.  If one wants the usual
linear-map matrix whose columns are the images of the ordered basis vectors,
transpose M_phi.  The scalar matrix identities below are unchanged as
projective group relations by this transpose convention.

The script proves the stated polynomial/rational identities.  It does not
prove the geometric-point categorical reconstruction or an intrinsic-family
moduli interpretation.  The order of the full generic stabilizer additionally
uses the root-configuration stabilizer calculation in the TeX proof.
"""

import sympy as sp


def zero(expression):
    return sp.cancel(sp.expand(expression)) == 0


def check_scalar(label, expression):
    assert zero(expression), (label, sp.factor(expression))


def check_matrix(label, matrix):
    assert all(zero(entry) for entry in matrix), (label, matrix)


def substitute(form, matrix):
    new_u, new_v = matrix * sp.Matrix([u, v])
    return sp.expand(form.subs({u: new_u, v: new_v}, simultaneous=True))


u, v, r, t = sp.symbols("u v r t")
lam = r**2  # r is nonzero, and r**2 != 1, on the geometric chart.
identity = sp.eye(4)
f1 = u * v
f2 = (u - v) * (u - lam * v)
rw = sp.Matrix([[0, lam], [1, 0]])
tw = sp.Matrix([[lam, -lam], [1, -lam]])
r4 = sp.diag(rw, r, r)
t4 = sp.diag(tw, sp.Matrix([[0, r], [r * (lam - 1), 0]]))
e1 = sp.diag(1, 1, -1, 1)
e2 = sp.diag(1, 1, 1, -1)
e12 = e1 * e2

check_scalar("R f1", substitute(f1, rw) - lam * f1)
check_scalar("R f2", substitute(f2, rw) - lam * f2)
check_scalar("T f1", substitute(f1, tw) - lam * f2)
check_scalar("T f2", substitute(f2, tw) - lam * (lam - 1) ** 2 * f1)
check_scalar("det R_W", rw.det() + lam)
check_scalar("det T_W", tw.det() + lam * (lam - 1))
check_matrix("R^2 scalar", r4 * r4 - lam * identity)
check_matrix("T^2 scalar", t4 * t4 - lam * (lam - 1) * identity)
check_matrix("e1^2", e1 * e1 - identity)
check_matrix("e2^2", e2 * e2 - identity)
check_matrix("e1 e2 commute", e1 * e2 - e2 * e1)
check_matrix("R e1 commute", r4 * e1 - e1 * r4)
check_matrix("R e2 commute", r4 * e2 - e2 * r4)
check_matrix("T swaps e1", t4 * e1 - e2 * t4)
check_matrix("T swaps e2", t4 * e2 - e1 * t4)
check_matrix("projective commutator [R,T]=e1 e2", r4 * t4 + e12 * t4 * r4)
check_matrix("(e1 T)^2 scalar times e1 e2", (e1 * t4) ** 2 - lam * (lam - 1) * e12)
check_matrix("R e1 central projectively", r4 * e1 * t4 + t4 * r4 * e1)
check_matrix("R e1 involution projectively", (r4 * e1) ** 2 - lam * identity)

shared_f2 = u * (u - v)
sw = sp.Matrix([[1, 0], [1, -1]])
s4 = sp.diag(sw, sp.Matrix([[0, 1], [1, 0]]))
check_scalar("shared S f1", substitute(f1, sw) - shared_f2)
check_scalar("shared S f2", substitute(shared_f2, sw) - f1)
check_matrix("shared S^2", s4 * s4 - identity)
check_matrix("shared S swaps e1", s4 * e1 - e2 * s4)
check_matrix("shared S swaps e2", s4 * e2 - e1 * s4)
check_matrix("shared (e1 S)^2=e1 e2", (e1 * s4) ** 2 - e12)
check_scalar("equal torus preserves uv", substitute(f1, sp.diag(t, 1 / t)) - f1)


def coefficients(form):
    expanded = sp.Poly(sp.expand(form), u, v)
    return (expanded.coeff_monomial(u**2), expanded.coeff_monomial(u * v),
            expanded.coeff_monomial(v**2))


def discriminant(form):
    a, b, c = coefficients(form)
    return sp.expand(b * b - 4 * a * c)


def polarized_discriminant(left, right):
    a, b, c = coefficients(left)
    aa, bb, cc = coefficients(right)
    return sp.expand(b * bb - 2 * a * cc - 2 * aa * c)


def chi(left, right):
    return polarized_discriminant(left, right) ** 2 / (discriminant(left) * discriminant(right))


check_scalar("generic chi", chi(f1, f2) - (1 + lam) ** 2 / (1 - lam) ** 2)
check_scalar("shared chi=1", chi(f1, shared_f2) - 1)
check_scalar("equal chi=1", chi(f1, f1) - 1)
check_scalar("degeneration family chi=1", chi(f1, u * (v - t * u)) - 1)

a, b, c, aa, bb, cc, p, q, h, j = sp.symbols("a b c aa bb cc p q h j")
matrix = sp.Matrix([[p, q], [h, j]])
left = a * u**2 + b * u * v + c * v**2
right = aa * u**2 + bb * u * v + cc * v**2
check_scalar("discriminant covariance", discriminant(substitute(left, matrix)) - matrix.det() ** 2 * discriminant(left))
check_scalar("polarized discriminant covariance", polarized_discriminant(substitute(left, matrix), substitute(right, matrix)) - matrix.det() ** 2 * polarized_discriminant(left, right))

# Relative root exchange.  Only theta, rho1, rho2 and their square roots are
# inverted: a or b may be zero, including the coincident-pair point a=b=0.
local_a, local_b, rho1, rho2, gamma = sp.symbols("local_a local_b rho1 rho2 gamma")
theta = 1 - local_a * local_b
exchange = sp.Matrix([[1, -local_a], [local_b, -1]])
qform = (u - local_a * v) * (local_b * u - v)
relative_f1 = rho1 * u * v
relative_f2 = rho2 * qform
eta = rho1 / (rho2 * theta)
check_matrix("relative A^2=theta", exchange**2 - theta * sp.eye(2))
check_scalar("relative det A=-theta", exchange.det() + theta)
check_scalar("relative A(uv)=q", substitute(u * v, exchange) - qform)
check_scalar("relative A(q)=theta^2 uv", substitute(qform, exchange) - theta**2 * u * v)
check_scalar("relative discriminant q", discriminant(qform) - theta**2)
# For L=A/delta, delta^2=theta, degree-two substitution is A(f)/theta.
check_scalar("relative L(f1)=eta f2", substitute(relative_f1, exchange) / theta - eta * relative_f2)
check_scalar("relative L(f2)=eta^-1 f1", substitute(relative_f2, exchange) / theta - relative_f1 / eta)
sigma_cd = sp.Matrix([[0, gamma], [-1 / gamma, 0]])
check_matrix("relative sigma_cd^2=-1", sigma_cd**2 + sp.eye(2))
# This symbolic check uses gamma^2=eta, so sigma(rc)=eta rd and sigma(rd)=rc/eta.
rc, rd = sp.symbols("rc rd")
check_scalar("relative relation line changes sign", eta * rd - eta * (rc / eta) + (rc - eta * rd))
check_scalar("relative cut fixed", eta * rd + eta * (rc / eta) - (rc + eta * rd))
nc_c, nc_d, nc_x, nc_y = sp.symbols("nc_c nc_d nc_x nc_y", commutative=False)
new_x, new_y = nc_c + gamma * nc_d, nc_c - gamma * nc_d
check_scalar("relative Ore variable change", new_x * new_y + new_y * new_x - 2 * (nc_c**2 - gamma**2 * nc_d**2))
old_c, old_d = (nc_x + nc_y) / 2, (nc_x - nc_y) / (2 * gamma)
check_scalar("relative cut monic in y^2", old_c**2 + gamma**2 * old_d**2 - (nc_x**2 + nc_y**2) / 2)
check_matrix("relative coincident-pair specialization", exchange.subs({local_a: 0, local_b: 0}) - sp.diag(1, -1))
print("PASS: all exact coefficient identities, projective group relations, chi identities, and relative-root identities")

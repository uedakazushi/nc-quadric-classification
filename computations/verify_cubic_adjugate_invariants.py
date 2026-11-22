"""Exact verification of the cubic geometric-open equations.

Run: python verify_cubic_adjugate_invariants.py
Requires Python 3 and SymPy.  No repository files are modified.
"""

import itertools
import sympy as s


J = s.Matrix([[0, 0, 0, 1], [0, 0, -1, 0],
              [0, -1, 0, 0], [1, 0, 0, 0]])
H = s.Matrix([[1, 1, 0, 0], [0, 0, 1, 1],
              [0, 0, 1, -1], [1, -1, 0, 0]])
HAD = s.Matrix([[1, 1, 1, 1], [1, 1, -1, -1],
                [1, -1, 1, -1], [1, -1, -1, 1]])


def cross(T):
    """(Cr T)_(a,b),(c,d) = T_(c,a),(d,b), all indices in {0,1}."""
    return s.Matrix(4, 4, lambda row, col:
                    T[2 * (col // 2) + row // 2,
                      2 * (col % 2) + row % 2])


def elem_matrix(M, degree):
    return sum(M.extract(I, I).det()
               for I in itertools.combinations(range(4), degree))


def elementary(values, degree):
    return sum(s.prod(values[i] for i in I)
               for I in itertools.combinations(range(4), degree))


def zero(expr):
    if isinstance(expr, s.MatrixBase):
        return all(s.expand(t) == 0 for t in expr)
    return s.expand(expr) == 0


checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)
    print("PASS:", name)


x = s.symbols("x1:5")
T = H * s.diag(*x) * H.inv()
lam = s.Matrix([s.prod(x[j] for j in range(4) if j != i)
                for i in range(4)])
adjT = T.adjugate()
N = cross(adjT)
mu = HAD * lam / 2

check("J is the Segre bilinear form, J^2=I", J * J == s.eye(4))
check("adjugate eigenvalues are complementary triple products",
      zero(H.inv() * adjT * H - s.diag(*lam)))
check("cross-adjugate eigenvalues are Hadamard/2 of those products",
      zero(H.inv() * N * H - s.diag(*mu)))
check("Cartan cross Gram equals N^2", zero(J * N.T * J * N - N * N))

e1, e2, e3 = [elementary([v**2 for v in x], i) for i in (1, 2, 3)]
d = s.prod(x)
p = s.prod(mu)
q = elementary([v**2 for v in mu], 3)
P = (e3**2 - 4*d**2*e2 + 8*d**3) / 16
Q = (e3**3 - 4*d**2*e2*e3 + 16*d**4*e1 - 8*d**3*e3) / 16
check("16 p has the stated Cartan invariant formula", zero(p - P))
check("16 q has the stated Cartan invariant formula", zero(q - Q))
check("q-e3*p = d^3*(d*e1-e3)", zero(q - e3*p - d**3*(d*e1-e3)))

# Dense and singular examples verify directly with the matrix definitions,
# independently of the Cartan diagonalization and its eigenvalue formulas.
samples = [
    s.Matrix([[1, 2, 3, 5], [7, 11, 13, 17],
              [19, 23, 29, 31], [37, 41, 43, 47]]),
    s.Matrix([[1, 2, 0, 1], [0, 1, 3, 2],
              [2, 0, 1, 4], [3, 3, 4, 7]]),
    s.Matrix([[1, 2, 3, 4], [2, 1, 0, 3],
              [3, 3, 3, 7], [4, 5, 6, 11]]),
    s.eye(4),
    s.Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
              [0, 1, 0, 0], [0, 0, 0, 1]]),
]
for i, sample in enumerate(samples):
    gram = J * sample.T * J * sample
    a, b, c = [elem_matrix(gram, j) for j in (1, 2, 3)]
    delta = sample.det()
    n = cross(sample.adjugate())
    pp = n.det()
    qq = elem_matrix(J * n.T * J * n, 3)
    check(f"direct matrix sample {i}, rank {sample.rank()}",
          zero(16*pp - (c*c - 4*delta**2*b + 8*delta**3))
          and zero(16*qq - (c**3 - 4*delta**2*b*c
                            + 16*delta**4*a - 8*delta**3*c)))

# Universal coefficient manipulations used in the radical-ideal proof.
E1, E2, E3, D, h, ell = s.symbols("E1 E2 E3 D h ell")
A = E3**2 - 4*D**2*E2 + 8*D**3
B = E3**3 - 4*D**2*E2*E3 + 16*D**4*E1 - 8*D**3*E3
check("equation ideal equals (A,D^3 h)",
      zero(B - E3*A + 16*D**3*(E3-D*E1)))
check("A = h^2+2 D E1 h-D^2 ell",
      zero(A.subs({E3: h+D*E1, E2: (ell+E1**2+8*D)/4})
           - (h*h+2*D*E1*h-D*D*ell)))
u, v = s.symbols("u v")
for name, subs in [
    ("C0", {E1: u, E2: v, D: 0, E3: 0}),
    ("C1", {E1: u, E2: (u*u+8*v)/4, D: v, E3: u*v}),
]:
    check(f"{name} parametrization lies in both equations",
          zero(A.subs(subs)) and zero(B.subs(subs)))

print(f"All {len(checks)} exact checks passed.")

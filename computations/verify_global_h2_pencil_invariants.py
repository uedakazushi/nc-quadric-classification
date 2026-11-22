"""Exact finite checks for the pencil invariant hull in paper C.

Run: python3 computations/verify_global_h2_pencil_invariants.py
Requires Python 3 and SymPy. This verifies identities and examples; it
does not replace orthogonal invariant theory or GIT/stack proofs.
"""
from itertools import combinations
import random
import sympy as s

J = s.Matrix([[0, 0, 0, 1], [0, 0, -1, 0],
              [0, -1, 0, 0], [1, 0, 0, 0]])


def cross(T):
    return s.Matrix(4, 4, lambda row, col:
                    T[2 * (col // 2) + row // 2,
                      2 * (col % 2) + row % 2])


def e3(M):
    return sum(M.extract(t, t).det() for t in combinations(range(4), 3))


def verify_pair(f, g):
    F, G = f.det(), g.det()
    z = s.Symbol("z")
    pencil = s.Poly((f * J * f.T + z * g * J * g.T).det(), z)
    assert pencil.nth(0) == F * F
    assert pencil.nth(4) == G * G
    I1, I2, I3 = (pencil.nth(j) for j in (1, 2, 3))

    mf = cross(f.adjugate() * g)
    mg = cross(g.adjugate() * f)
    Pf, Pg = mf.det(), mg.det()
    Qf = e3(J * mf.T * J * mf)
    Qg = e3(J * mg.T * J * mg)
    expected = (
        (I1**2 - 4 * F**2 * I2 + 8 * F**3 * G) / 16,
        (I1**3 - 4 * F**2 * I1 * I2 + 16 * F**4 * I3
         - 8 * F**3 * G * I1) / 16,
        (I3**2 - 4 * G**2 * I2 + 8 * G**3 * F) / 16,
        (I3**3 - 4 * G**2 * I3 * I2 + 16 * G**4 * I1
         - 8 * G**3 * F * I3) / 16,
    )
    assert all(s.factor(a - b) == 0
               for a, b in zip((Pf, Qf, Pg, Qg), expected))

    A, B, C, D = F * G, I2, F * I3 + G * I1, I1 * I3
    L = B - 2 * A
    assert s.factor(256 * Pf * Pg - (D + 4 * A * L)**2
                    + 4 * L * C**2) == 0
    return I1, I2, I3, F, G


def main():
    a, b, c, d = s.symbols("a b c d")
    f = s.Matrix([[1, 0, 0, 1], [0, 1, 0, 0],
                  [0, 0, 1, 0], [0, 0, 0, 0]])
    g = s.Matrix([[0, 0, 0, 0], [0, a, c, 0],
                  [0, b, d, 0], [1, 0, 0, 1]])
    I1, I2, I3, F, G = verify_pair(f, g)
    assert F == G == 0
    assert s.factor(I1 + 4) == 0
    assert s.factor(I2 + 8 * (a * d + b * c)) == 0
    assert s.factor(I3 + 4 * (a * d - b * c)**2) == 0
    print("PASS: universal noncubic normal form and chi coordinate")

    for seed in (123, 124, 125, 126):
        random.seed(seed)
        ff = s.Matrix(4, 4,
                      lambda i, j: random.randint(-2, 2))
        gg = s.Matrix(4, 4,
                      lambda i, j: random.randint(-2, 2))
        verify_pair(ff, gg)
        print(f"PASS: exact matrix check seed={seed}, ranks=({ff.rank()},{gg.rank()})")

    t = s.Symbol("t")
    # Hilbert series of the ordered ring: one relation of degree six.
    ordered = (1 - t**6) / ((1-t**2)**2 * (1-t**3)**2 * (1-t**4))
    unordered = 1 / ((1-t**2)**2 * (1-t**3) * (1-t**4))
    ordered_coeff = s.series(ordered, t, 0, 14).removeO()
    unordered_coeff = s.series(unordered, t, 0, 14).removeO()
    # As an S2-double cover, R_G = R_H + X_3 R_H
    assert s.simplify(ordered - (1 + t**3) * unordered) == 0
    assert s.expand(ordered_coeff).coeff(t, 8) == 13
    assert s.expand(unordered_coeff).coeff(t, 8) == 9
    print("PASS: graded rings and rank-two invariant decomposition")


if __name__ == "__main__":
    main()

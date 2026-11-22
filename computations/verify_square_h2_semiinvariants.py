#!/usr/bin/env python3
"""Exact checks for the square H2 semi-invariant criterion.

Checks a polynomial rank-three model, the adjugate/Gram identity, the
five-factor character weights, and the invariant principal-open cover.
This is not a proof of the H2 theorem, GIT descent, or existence/novelty
of a good moduli space. See the accompanying manuscript proofs.
Requires Python 3, SymPy, and verify_square_h2_open.py in this directory.
"""

from itertools import combinations, product

import sympy as sp

from verify_square_h2_open import cross, five, kernel_segre_free


J = sp.Matrix([[0, 0, 0, 1], [0, 0, -1, 0],
               [0, -1, 0, 0], [1, 0, 0, 0]])
assert J.det() == 1 and J * J == sp.eye(4)


def e3(matrix):
    return sp.expand(sum(matrix.extract(ix, ix).det()
                         for ix in combinations(range(4), 3)))


def pq(matrix):
    return sp.expand(matrix.det()), e3(J * matrix.T * J * matrix)


def invariant_quadruple(f, g):
    pf, qf = pq(cross(f.adjugate() * g))
    pg, qg = pq(cross(g.adjugate() * f))
    return pf, qf, pg, qg


def cover_four(values):
    pf, qf, pg, qg = values
    return (pf * pg, pf**3 * qg**2, qf**2 * pg**3, qf * qg)


def cover_unordered(values):
    pf, qf, pg, qg = values
    return (pf * pg, qf * qg, pf**3 * qg**2 + qf**2 * pg**3)


def common_weight(values):
    pf, qf, pg, qg = values
    return ((pf * pg)**3, pf**3 * qg**2,
            qf**2 * pg**3, (qf * qg)**2)


def gram_identity():
    s, t = sp.symbols("s t")
    left, right = sp.eye(4), sp.eye(4)
    left[3, 0], right[0, 3] = -t, -s
    matrix = left * sp.diag(1, 1, 1, 0) * right
    kappa, lam = sp.Matrix([s, 0, 0, 1]), sp.Matrix([t, 0, 0, 1])
    assert matrix.adjugate() == kappa * lam.T
    gram = J * matrix.T * J * matrix
    assert sp.simplify(gram.adjugate()
                       - matrix.adjugate() * J * matrix.adjugate().T * J) == sp.zeros(4)
    assert e3(gram) == sp.expand(gram.adjugate().trace())
    assert pq(matrix) == (0, 4 * s * t)
    assert sp.expand((kappa.T * J * kappa)[0]
                     * (lam.T * J * lam)[0]) == 4 * s * t
    for sv, tv in product((0, 1, 2), repeat=2):
        mm = matrix.subs({s: sv, t: tv})
        p, q = pq(mm)
        assert bool(p != 0 or q != 0) == (
            kernel_segre_free(mm) and kernel_segre_free(mm.T))
    print("PASS rank3 polynomial model: adj(M)=kappa lambda^t; Q=4*s*t")

    examples = [sp.zeros(4), sp.diag(1, 0, 0, 0),
                sp.diag(1, 1, 0, 0), sp.eye(4),
                sp.Matrix([[1, 0, 0, -1], [0, 2, 0, 0],
                           [0, 0, 2, 0], [-1, 0, 0, 1]])]
    for mm in examples:
        p, q = pq(mm)
        gram = J * mm.T * J * mm
        assert gram.adjugate() == mm.adjugate() * J * mm.adjugate().T * J
        assert e3(gram) == gram.adjugate().trace()
        old = all(any(x != 0 for x in five(n)) for n in (mm, mm.T))
        assert bool(p != 0 or q != 0) == old
    assert pq(examples[-1]) == (0, 64)
    print("PASS all rank strata: D(det M,e3 Gram) equals the two five-polynomial opens")


def character_checks():
    ga = sp.Matrix([[2, 1], [0, 1]])
    gb = sp.Matrix([[3, 0], [1, 1]])
    gc = sp.Matrix([[1, 2], [0, 5]])
    gd = sp.Matrix([[7, 1], [0, 1]])
    hw = sp.Matrix([[1, 1, 0, 0], [0, 1, 1, 0],
                    [0, 0, 1, 1], [0, 0, 0, 11]])
    a, b, c, d, w = (matrix.det() for matrix in (ga, gb, gc, gd, hw))
    chi_f = w / (a*a*c*c)
    chi_g = w / (b*b*d*d)
    chi_0 = w / (a*b*c*d)
    zeta_f, zeta_g = chi_f * chi_0, chi_g * chi_0
    assert zeta_f * zeta_g == chi_0**4
    hs, ht = sp.kronecker_product(gc.inv().T, gd), sp.kronecker_product(ga, gb.inv().T)
    assert hs.T * J * hs == (d/c) * J
    assert ht.T * J * ht == (a/b) * J

    identity = sp.eye(4)
    flip = sp.Matrix(4, 4, lambda i, j: int(i == 2*(j % 2) + j//2))
    rank3cross = sp.Matrix([[1, 0, 0, 2], [0, -1, 0, 0],
                           [0, 0, -1, 0], [2, 0, 0, 1]])
    for g in (flip, rank3cross):
        f = identity
        fp = hw * f * sp.kronecker_product(gc, ga).inv()
        gp = hw * g * sp.kronecker_product(gd, gb).inv()
        mf, mfp = cross(f.adjugate() * g), cross(fp.adjugate() * gp)
        assert mfp == chi_f * ht * mf * hs.inv()
        gram, gramp = J * mf.T * J * mf, J * mfp.T * J * mfp
        assert gramp == zeta_f * hs * gram * hs.inv()
        old, new = invariant_quadruple(f, g), invariant_quadruple(fp, gp)
        assert new == (zeta_f**2*old[0], zeta_f**3*old[1],
                       zeta_g**2*old[2], zeta_g**3*old[3])
        assert cover_four(new) == tuple(chi_0**n * value
                                       for n, value in zip((8, 24, 24, 12), cover_four(old)))
        assert cover_unordered(new) == tuple(chi_0**n * value
                                            for n, value in zip((8, 12, 24), cover_unordered(old)))
        assert common_weight(new) == tuple(chi_0**24 * x for x in common_weight(old))
        swapped = invariant_quadruple(g, f)
        assert swapped == (old[2], old[3], old[0], old[1])
        assert cover_unordered(swapped) == cover_unordered(old)
    print("PASS character weights: P_f/Q_f=zeta_f^(2/3); zeta_f*zeta_g=chi0^4")
    print("PASS four products chi0^(8,24,24,12); unordered three sections chi0^(8,12,24)")

    # The exponent identity and triviality on K, checked independently as monomials.
    aa, bb, cc, dd, ww = sp.symbols("a b c d w", nonzero=True)
    xf, xg, x0 = ww/(aa**2*cc**2), ww/(bb**2*dd**2), ww/(aa*bb*cc*dd)
    zf, zg = xf*x0, xg*x0
    assert sp.cancel(zf*zg - x0**4) == 0
    l1, l2, l3 = sp.symbols("l1 l2 l3", nonzero=True)
    vertex = {aa:l1**2, bb:l2**2, cc:(l3/l1)**2,
              dd:(l3/l2)**2, ww:l3**4}
    assert sp.cancel(x0.subs(vertex)) == 1
    assert sp.cancel(xf.subs(vertex)) == sp.cancel(xg.subs(vertex)) == 1
    print("PASS determinant characters descend through the vertex torus K")


def cover_checks():
    pf, qf, pg, qg = sp.symbols("pf qf pg qg")
    s0, s1, s2, s3 = common_weight((pf, qf, pg, qg))
    assert sp.expand(s1*s2 - s0*s3) == 0
    print("PASS common character chi0^24 and the polynomial identity s1*s2=s0*s3")
    for values in product((sp.Integer(0), sp.Integer(1), sp.Integer(-1), sp.I), repeat=4):
        pf, qf, pg, qg = values
        direct = (pf != 0 or qf != 0) and (pg != 0 or qg != 0)
        assert direct == any(sp.expand(x) != 0 for x in cover_four(values))
        assert direct == any(sp.expand(x) != 0 for x in cover_unordered(values))
        s0, s1, s2, s3 = common_weight(values)
        assert direct == any(sp.expand(x) != 0 for x in (s0, s3, s1+s2))
    print("PASS principal-open covers, including cancellation in the S2-invariant mixed sum")


if __name__ == "__main__":
    gram_identity()
    character_checks()
    cover_checks()
    print("Scope: exact identities and examples; no proof certificate for relative H2/GIT claims.")

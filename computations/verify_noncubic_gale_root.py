#!/usr/bin/env python3
"""Exact rational checks for the noncubic Gale/Serre-root tangent model.

This is a supplementary finite linear-algebra check. The general proof is
the equivariant Grassmann tangent calculation in papers/sections/noncubic_hh_roots.tex.
No random inputs or floating-point rank computations are used.
"""
import sympy as s

D = s.diag(1, -1)
Dleft = s.diag(1, 1, -1, -1)
J = s.BlockMatrix([[s.zeros(4), Dleft], [-Dleft, s.zeros(4)]]).as_explicit()
assert J.T == -J

def flat(a):
    return s.Matrix(list(a))

def check(label, alpha, beta, gamma, expected_stabilizer, expected_hh1_minus=0):
    assert alpha**2 + beta*gamma == 1
    M = s.Matrix([
        [0, 0, -1, 0], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 1, 0],
        [0, 0, 0, 1], [alpha, beta, 0, 0], [-gamma, alpha, 0, 0], [0, 0, 0, -1],
    ])
    assert M.rank() == 4
    assert M.T * J.inv() * M == s.zeros(4)
    full = M
    complement = []
    for col in s.eye(8).columnspace():
        enlarged = full.row_join(col)
        if enlarged.rank() > full.rank():
            full = enlarged
            complement.append(col)
        if full.cols == 8:
            break
    N = s.Matrix.hstack(*complement)
    PN = full.inv()[4:8, :]
    pairing = M.T * J.inv() * N
    assert pairing.det() != 0

    def tangent_action(X):
        return pairing.inv() * X.T * pairing.T

    tangent_basis = []
    for i in range(4):
        for j in range(4):
            X = s.zeros(4)
            X[i, j] = 1
            tangent_basis.append(X)
    tau = s.Matrix.hstack(*(flat(tangent_action(X)) for X in tangent_basis))
    assert tau*tau == s.eye(16)
    assert (tau+s.eye(16)).rank() == 10
    assert (tau-s.eye(16)).rank() == 6

    infinitesimal = []
    for factor in range(4):
        for i in range(2):
            for j in range(2):
                A, B, C, K = (s.zeros(2) for _ in range(4))
                matrices = [A, B, C, K]
                matrices[factor][i, j] = 1
                rho_E = -s.kronecker_product(A.T, s.eye(2)) - s.kronecker_product(s.eye(2), B.T)
                rho_F = s.kronecker_product(C, s.eye(2)) - s.kronecker_product(s.eye(2), K.T)
                rho = s.diag(rho_E, rho_F)
                infinitesimal.append(flat(PN*rho*M))
    orbit = s.Matrix.hstack(*infinitesimal)
    orbit_rank = orbit.rank()
    assert orbit_rank == 13-expected_stabilizer
    assert orbit.row_join((tau-s.eye(16))*orbit).rank() == orbit_rank
    plus_orbit = ((tau+s.eye(16))*orbit).rank()
    minus_orbit = ((tau-s.eye(16))*orbit).rank()
    assert plus_orbit == 7-(expected_stabilizer-expected_hh1_minus)
    assert minus_orbit == 6-expected_hh1_minus
    assert orbit.row_join(tau-s.eye(16)).rank() == orbit_rank+expected_hh1_minus
    print(label, {
        "Grassmann_+-": (10, 6),
        "orbit_+-": (plus_orbit, minus_orbit),
        "HH2_+-": (10-plus_orbit, 6-minus_orbit),
        "HH1_dimension": expected_stabilizer,
        "HH1_+-": (expected_stabilizer-expected_hh1_minus, expected_hh1_minus),
    })

check("disjoint", s.Rational(3,5), s.Rational(4,5), s.Rational(4,5), 0)
check("one_root_shared", s.Integer(1), s.Integer(1), s.Integer(0), 0)
check("coincident", s.Integer(1), s.Integer(0), s.Integer(0), 1)
check("coincident_offdiagonal_obstructed", s.Integer(0), s.Integer(1), s.Integer(1), 1, 1)

# Derive the normal orbit map from the actual infinitesimal group action.
# This checks all coefficients, not merely a determinant entered by hand.
alpha, beta, gamma = s.symbols("alpha beta gamma")
M = s.Matrix([
    [0, 0, -1, 0], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 1, 0],
    [0, 0, 0, 1], [alpha, beta, 0, 0], [-gamma, alpha, 0, 0], [0, 0, 0, -1],
])
sl2 = [s.diag(1,-1), s.Matrix([[0,1],[0,0]]), s.Matrix([[0,0],[1,0]])]
columns = []
for factor in range(2):
    for generator in sl2:
        a, b = (generator, s.zeros(2)) if factor == 0 else (s.zeros(2), generator)
        c, k = -D*a*D, b.T
        rho_E = -s.kronecker_product(a.T,s.eye(2))-s.kronecker_product(s.eye(2),b.T)
        rho_F = s.kronecker_product(c,s.eye(2))-s.kronecker_product(s.eye(2),k.T)
        normal = M.T*J.inv()*s.diag(rho_E,rho_F)*M
        assert normal.T == -normal
        columns.append(s.Matrix([normal[i,j] for i in range(4) for j in range(i+1,4)]))
Q = s.Matrix.hstack(*columns)
expected_Q = s.Matrix([
    [-2*alpha,0,0,2*alpha,0,0],
    [0,gamma,-alpha,0,alpha,-gamma],
    [0,0,-1,0,-1,0],
    [0,-alpha,-beta,0,beta,alpha],
    [0,1,0,0,0,1],
    [-2,0,0,-2,0,0],
])
assert Q == expected_Q
assert s.factor(Q.det()) == -32*alpha*(alpha**2+beta*gamma)
print("symbolic normal determinant:", s.factor(Q.det()))
print("PASS: exact Gale tangent, good-root condition and obstructed offdiagonal root")

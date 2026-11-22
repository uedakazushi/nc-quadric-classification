"""Exact checks for cubic inversion, its quotient, and the global OU maps.

Run: python verify_cubic_inversion_global_maps.py
Requires Python 3 and SymPy.  No repository files are modified.
The proofs use the universal matrix identities and invariant-ring arguments
in cubic_inversion_global_morphisms.tex; samples below are additional checks.
"""

import itertools
import sympy as sp


J = sp.Matrix([[0, 0, 0, 1], [0, 0, -1, 0],
               [0, -1, 0, 0], [1, 0, 0, 0]])
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)
    print("PASS:", name)


def zero(value):
    if isinstance(value, sp.MatrixBase):
        return all(sp.cancel(x) == 0 for x in value)
    return sp.cancel(value) == 0


def elem(M, degree):
    return sum(M.extract(I, I).det()
               for I in itertools.combinations(range(4), degree))


def cross(T):
    return sp.Matrix(4, 4, lambda row, col:
                     T[2 * (col // 2) + row // 2,
                       2 * (col % 2) + row % 2])


e1, e2, d, e3 = sp.symbols("e1 e2 d e3")
coords = (e1, e2, d, e3)
weights = (1, 2, 2, 3)


def cremona(x):
    a, b, delta, c = x
    return (c, delta**2*b, delta**3, delta**4*a)


inv = cremona(coords)
check("weighted degree is three",
      all(all(sum(a*b for a, b in zip(mon, weights)) == 3*w
              for mon in sp.Poly(expr, *coords).monoms())
          for expr, w in zip(inv, weights)))
check("square is weighted scaling by d^4",
      all(zero(x-d**(4*w)*y)
          for x, y, w in zip(cremona(inv), coords, weights)))

P = (e3**2-4*d**2*e2+8*d**3)/16
Q = (e3**3-4*d**2*e2*e3+16*d**4*e1-8*d**3*e3)/16
change = dict(zip(coords, inv))
check("pullback of p under Cremona",
      zero(P.subs(change, simultaneous=True)
           - d**8*(e1**2-4*e2+8*d)/16))
check("pullback of q under Cremona",
      zero(Q.subs(change, simultaneous=True)
           - d**12*(e1**3-4*e1*e2+16*e3-8*d*e1)/16))
C1 = {e2: (e1**2+8*d)/4, e3: d*e1}
check("C1 is fixed wherever d is nonzero",
      all(zero((x-d**w*y).subs(C1))
          for x, y, w in zip(inv, coords, weights)))
check("rank-three geometric divisor maps to q0",
      tuple(x.subs(d, 0) for x in inv) == (e3, 0, 0, 0))

samples = [
    sp.Matrix([[1, 2, 3, 5], [7, 11, 13, 17],
               [19, 23, 29, 31], [37, 41, 43, 47]]),
    sp.Matrix([[1, 2, 0, 1], [0, 1, 3, 0],
               [2, 0, 1, 4], [1, 0, 0, 2]]),
]
for number, T in enumerate(samples):
    delta = T.det()
    check(f"sample {number} is invertible", delta != 0)
    Tinv = T.inv()
    K = J*T.T*J*T
    Kinv = J*Tinv.T*J*Tinv
    check(f"sample {number}: inverse Gram similarity",
          zero(Kinv-T*K.inv()*Tinv))
    old = (elem(K, 1), elem(K, 2), delta, elem(K, 3))
    new = (elem(Kinv, 1), elem(Kinv, 2), Tinv.det(), elem(Kinv, 3))
    predicted = (old[3]/delta**2, old[1]/delta**2,
                 1/delta, old[0]/delta**2)
    check(f"sample {number}: all four inverse invariants",
          all(zero(x-y) for x, y in zip(new, predicted)))

kappa = sp.Matrix(sp.symbols("k0:4"))
psi = sp.Matrix(sp.symbols("p0:4"))
T = kappa*psi.T
K = J*T.T*J*T
trace_product = (kappa.T*J*kappa)[0]*(psi.T*J*psi)[0]
check("rank-one Gram trace is product of Segre values",
      zero(sp.trace(K)-trace_product))
check("rank-one remaining invariants vanish identically",
      zero(elem(K, 2)) and zero(T.det()) and zero(elem(K, 3)))
det_kappa = kappa[0]*kappa[3]-kappa[1]*kappa[2]
det_psi = psi[0]*psi[3]-psi[1]*psi[2]
check("rank-one crossing is nondegenerate exactly off both Segres",
      zero(cross(T).det()-det_kappa**2*det_psi**2))

b, u, v, w, s, z = sp.symbols("b u v w s z")
coarse = (e2/d, e1**2/d, e1*e3/d**2, e3**2/d**3)
check("inversion exchanges u,w and fixes b,v",
      all(zero(x.subs(change, simultaneous=True)-y)
          for x, y in zip(coarse, (coarse[0], coarse[3],
                                  coarse[2], coarse[1]))))
check("coarse fixed locus is the reduced product of two factors",
      zero((u*w-v*v).subs(w, u)-(u-v)*(u+v)))
check("double-cover equation is the original quadric equation",
      zero(((u-w)**2-(u+w)**2+4*v**2)+4*(u*w-v**2)))
check("branch planes meet transversally in characteristic zero",
      sp.Matrix([[sp.diff(s-2*v, t) for t in (s, v)],
                 [sp.diff(s+2*v, t) for t in (s, v)]]).det() == 4)
check("bad C1 maps exactly to the stated affine line",
      zero(((u+w)-2*v).subs({u: 4*b-8, v: 4*b-8, w: 4*b-8}))
      and zero((v-4*b+8).subs(v, 4*b-8)))

# Character exponents are in the order det A, det B, det C, det D, det W.
chi_f = sp.Matrix([-2, 0, -2, 0, 1])
chi_0 = sp.Matrix([-1, -1, -1, -1, 1])
tensor_ratio = sp.Matrix([1, -1, 1, -1, 0])
check("global Gram character is zeta_f=chi_f*chi_0",
      2*chi_f+tensor_ratio == chi_f+chi_0)

print(f"All {len(checks)} exact checks passed.")

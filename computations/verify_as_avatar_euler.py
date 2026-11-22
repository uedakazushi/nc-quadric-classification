#!/usr/bin/env python3
"""Symbolic rational-series and finite integer checks of minimal AS Euler recurrences.

No assertion here verifies AS-Gorenstein duality, derived helix realization,
all-integer exactness, QP mutation, or the classification theorem.
"""

TABLE = {
    "rotated": {
        "q1": [{1: 2}, {2: 2}, {2: 2, 1: 2}, {1: 4}],
        "q2": [{2: 2}, {3: 2}, {3: 4}, {3: 2, 2: 2}],
    },
    "square": {
        "q1": [{1: 4}, {1: 2}, {2: 2}, {2: 2, 1: 2}],
        "q2": [{3: 2, 2: 2}, {2: 2}, {3: 2}, {3: 4}],
    },
}

# A_{i,j} with i >= j; the right simple S_i has P_{i-k}
# in its resolution.  Evaluate at j=i-n, varying n>=0.
for kind, dat in TABLE.items():
    h = {}
    for n in range(81):
        for phase in range(4):
            value = int(n == 0)
            value += sum(v * h[((phase - k) % 4, n-k)]
                         for k, v in dat["q1"][phase].items() if n >= k)
            value -= sum(v * h[((phase - k) % 4, n-k)]
                         for k, v in dat["q2"][phase].items() if n >= k)
            if n >= 4:
                value += h[(phase, n-4)]
            h[(phase, n)] = value
    for phase in range(4):
        for m in range(21):
            assert h[(phase, 4*m)] == (2*m + 1)**2, (kind, phase, m)
    assert all(h[(0, n)] >= 0 for n in range(81)), kind

# The odd/even P_{i-2} terms cancel in AS10 Euler characteristics.
ten = {-4: 0, -3: 0, -2: 0, -1: 0}
for n in range(81):
    ten[n] = int(n == 0) + 2*ten[n-1] - 2*ten[n-3] + ten[n-4]
    r = n // 2
    want = (r+1)**2 if n % 2 == 0 else (r+1)*(r+2)
    assert ten[n] == want, (n, ten[n], want)
# Exact proof of the all-m identity for each residue, assuming only
# the four minimal resolution recurrences (not their exactness).
# H_phase(z) = sum_{n>=0} dim A_(i,i-n) z^n.
import sympy as sp

z = sp.symbols("z")
for kind, dat in TABLE.items():
    M = sp.eye(4) * (1-z**4)
    for phase in range(4):
        for k, v in dat["q1"][phase].items():
            M[phase, (phase-k) % 4] -= v*z**k
        for k, v in dat["q2"][phase].items():
            M[phase, (phase-k) % 4] += v*z**k
    H = M.inv()*sp.ones(4, 1)
    target = (1+6*z**4+z**8)/(1-z**4)**3
    for phase in range(4):
        rational = sp.cancel(H[phase])
        # Root-of-unity filter extracts exactly the 4m coefficients.
        fourth = sum(rational.subs(z, sp.I**j*z) for j in range(4))/4
        assert sp.cancel(fourth-target) == 0, (kind, phase)

assert sp.cancel(
    1/(1-2*z+2*z**3-z**4) - 1/((1-z)**2*(1-z**2))
) == 0
print("PASS: exact 4-phase rational Hilbert identity (all m), AS10 series, and finite coefficient checks")


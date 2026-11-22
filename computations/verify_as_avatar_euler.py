#!/usr/bin/env python3
"""Finite integer checks of the AS square/rotated/10-arrow Euler recurrences.

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
print("PASS: square/rotated 4-period AS Euler growth and AS10 even/odd Hilbert function")

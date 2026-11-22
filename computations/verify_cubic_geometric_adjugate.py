#!/usr/bin/env python3
"""Exact quartic/sextic adjugate test for 2x2x2x2 geometric quintuples.

The criterion is proved in
papers/quiver-avatar/foundation_charts.tex
(lem:qa-explicit-cubic-geometric-adjugate).

Run: python3 computations/verify_cubic_geometric_adjugate.py
Standard library only. Checks examples and determinant homogeneity,
not the geometric theorem or algebraic-stack descent.
"""
from itertools import permutations
from math import prod


def determinant(A):
    n = len(A)
    assert all(len(row) == n for row in A)
    return sum(
        (-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        * prod(A[i][p[i]] for i in range(n))
        for p in permutations(range(n))
    )


def adjugate(M):
    n = len(M)
    assert n == 4 and all(len(row) == n for row in M)
    # adj[i,j] = (-1)^(i+j) det(M with row j and column i deleted).
    return [
        [
            (-1) ** (i + j)
            * determinant([[M[r][c] for c in range(n) if c != i]
                           for r in range(n) if r != j])
            for j in range(n)
        ]
        for i in range(n)
    ]


def flatten(tensor, i):
    assert len(tensor) == 16 and i in range(4)
    a, b = i, (i + 1) % 4
    c, d = (i + 2) % 4, (i + 3) % 4
    M = [[0] * 4 for _ in range(4)]
    for k, value in enumerate(tensor):
        bit = [(k >> (3 - h)) & 1 for h in range(4)]
        M[2 * bit[c] + bit[d]][2 * bit[a] + bit[b]] = value
    return M


def predicates(M):
    adj = adjugate(M)
    sextics = []
    for j in range(4):
        v = [adj[i][j] for i in range(4)]
        sextics.append(v[0] * v[3] - v[1] * v[2])
    quartic = determinant(M)
    return quartic, sextics


def good(M):
    q, h = predicates(M)
    return q != 0 or any(v != 0 for v in h)


def check():
    ident = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    assert predicates(ident)[0] == 1 and good(ident)
    decomposable = [[0, 0, 0, 0], [0, 1, 0, 0],
                    [0, 0, 1, 0], [0, 0, 0, 1]]
    assert not good(decomposable)  # ker = span(e00)
    entangled = [[1, 0, 0, -1], [0, 1, 0, 0],
                 [0, 0, 1, 0], [0, 0, 0, 0]]
    q, hs = predicates(entangled)
    assert q == 0 and any(h != 0 for h in hs) and good(entangled)
    rank_two = [[1, 0, 0, 0], [0, 1, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0]]
    assert predicates(rank_two) == (0, [0, 0, 0, 0])
    for matrix in (ident, decomposable, entangled, rank_two):
        q, h = predicates(matrix)
        scaled = [[3 * x for x in row] for row in matrix]
        qs, hs = predicates(scaled)
        assert qs == 3**4 * q
        assert hs == [3**6 * v for v in h]
    tensor = [3, 2, 7, 11, 5, 13, 17, 19,
              23, 29, 31, 37, 41, 43, 47, 53]
    dets = [predicates(flatten(tensor, i))[0] for i in range(4)]
    assert dets == [5976, 8496, 5976, 8496]
    assert all(good(flatten(tensor, i)) for i in range(4))
    ghz = [0]*16
    ghz[0] = ghz[15] = 1
    assert all(not good(flatten(ghz, i)) for i in range(4))
    print("PASS: rank 4 and rank 3 entangled kernel accepted")
    print("PASS: decomposable kernel and rank 2 matrices rejected")
    print("PASS: quartic and sextic scaling degrees 4 and 6")
    print("PASS: generic 2^4 tensor all four adjacent flattenings geometric")
    print("PASS: GHZ e0000+e1111 rejected on all adjacent pairs")


if __name__ == "__main__":
    check()

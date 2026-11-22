#!/usr/bin/env python3
"""Finite permutation-group audit of the four-sheeted monodromy comparison.

The field-theoretic nonsquare claims are proved in the manuscript, not here.
No third-party dependencies.
"""
from itertools import permutations

I = tuple(range(4))

def mul(a, b):
    return tuple(a[b[i]] for i in range(4))

def subgroup(gens):
    s = {I}
    while True:
        t = s | {mul(g, x) for x in s for g in gens}
        if t == s:
            return s
        s = t

flip_a = (1, 0, 2, 3)
flip_b = (0, 1, 3, 2)
pair_swap = (2, 3, 0, 1)
dihedral = subgroup((flip_a, flip_b, pair_swap))
assert len(dihedral) == 8
assert subgroup((flip_a, flip_b)) <= dihedral
assert len(subgroup((flip_a, flip_b))) == 4

root_choice = subgroup(((2, 3, 0, 1), (1, 0, 3, 2)))
assert len(root_choice) == 4
assert all(p != I for p in root_choice if p != I)
assert all(len({p[i] for p in root_choice}) == 4 for i in range(4))

all_perms = set(permutations(range(4)))
assert len(all_perms) == 24
partition = frozenset((frozenset((0, 1)), frozenset((2, 3))))

def preserves(p, pairing):
    return frozenset(frozenset(p[i] for i in pair) for pair in pairing) == pairing

marked = {p for p in all_perms if preserves(p, partition)}
assert marked == dihedral
assert len(marked) == 8
assert len(all_perms) // len(marked) == 3

print('PASS: special split-root family has dihedral four-sheet action of order 8')
print('PASS: root-choice fourfold has regular Klein-four action of order 4')
print('PASS: OU S4 fourfold restricted by one pair-partition has D4 stabilizer')
print('Scope: permutation identities only; field nonsquares and geometric descent are not verified')

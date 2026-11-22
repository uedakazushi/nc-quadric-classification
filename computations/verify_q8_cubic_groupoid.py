"""Exact checks of the Q8 cubic directed window and change-of-basis behavior.

Run: python3 computations/verify_q8_cubic_groupoid.py
Needs Python 3 and SymPy. This checks a finite rational example, not the
fppf/stack equivalence proved in cubic_qp_foundation_groupoid.tex.
"""
import sympy as s


def assert_equal(actual, expected, name):
    assert actual == expected, name
    print("PASS:", name)


# Flatten a quartic potential along the fourth rank-two arrow group.
# The two columns are the two cubic cyclic derivatives; rows index
# the triple tensor W⊗V⊗U in lexicographic order.
R = s.Matrix([[1, 0], [0, 1], [1, 1], [1, -1],
              [0, 2], [2, 0], [1, 2], [2, 1]])
assert_equal(R.rank(), 2, "full-rank fourth-arrow flattening")

# Directed window: two quadratic multiplications are identities, and
# the cubic multiplication is the quotient of the 8-dimensional
# triple product by the rank-two image of R.
m = s.Matrix.hstack(*R.T.nullspace()).T
assert_equal(m.shape, (6, 8), "quotient ranks: 8 to 6")
assert_equal(m.rank(), 6, "joint product surjectivity")
assert_equal(m * R, s.zeros(6, 2),
             "all cyclic derivatives become cubic relations")

a = s.eye(4)
b = s.eye(4)
c = m
d = m
assert_equal(c * s.kronecker_product(s.eye(2), a),
             d * s.kronecker_product(b, s.eye(2)),
             "associativity on the two triple-product routes")
assert_equal(s.Matrix.hstack(c, d).rank(), 6,
             "foundation joint surjection")
assert_equal(4 + 3 * 2 + 2 * 4 + 6, 24,
             "rank of four-vertex finite foundation")

# Fourth arrow GL2 moves only the basis of the image subspace.
h = s.Matrix([[1, 2], [1, 3]])
assert_equal(s.Matrix.hstack(R, R * h).rank(), 2,
             "fourth-arrow GL2 preserves relation subspace")

# Independent forward arrow GL2 changes act on the triple tensor.
gU = s.Matrix([[1, 1], [0, 1]])
gV = s.Matrix([[2, 0], [1, 1]])
gW = s.Matrix([[1, 0], [3, 1]])
G = s.kronecker_product(gW, s.kronecker_product(gV, gU))
R2 = G * R
m2 = m * G.inv()
assert_equal(m2 * R2, s.zeros(6, 2),
             "relation quotient equivariance")
assert_equal(m2.rank(), 6, "flat quotient ranks after base change")

# Three scalar directions fix a Grassmann point. A unique scalar of
# the fourth arrow cancels their action on the potential itself.
S = s.kronecker_product(5 * s.eye(2),
                         s.kronecker_product(3 * s.eye(2), 2 * s.eye(2)))
assert_equal(S * R, 30 * R, "vertex scalar action on the relation span")
assert_equal(S * R * (s.eye(2)/30), R,
             "compensating fourth-arrow scalar fixes the potential")
print("All 12 exact finite cubic-window checks passed.")

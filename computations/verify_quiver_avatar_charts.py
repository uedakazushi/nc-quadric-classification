#!/usr/bin/env python3
"""Exact finite examples for the eight/ten/twelve-arrow foundation charts.

Run from the repository root with Python 3.9+ and SymPy:
    python3 computations/verify_quiver_avatar_charts.py

For the Hirzebruch surface Sigma_n, use the Cox polynomial ring
Q[u,v,p,q] with deg(u)=deg(v)=f, deg(p)=s, deg(q)=s+n*f.
For n=0,2 set h=s+(n+2)/2*f and use (O,f,h,h+f).  All matrices
below come from multiplication of the indicated Cox monomials.

The additional (rank a, rank b)=(3,4) example is a synthetic finite
associative algebra; it is NOT asserted to be AS regular or to arise
from a noncommutative surface.  The product collection is checked
separately because its finite quiver is not the cubic-shaped chain.

All calculations use exact integers/rationals.  They verify only the
finite Hom dimensions, multiplication, kernel overlaps, and minimal
presentation counts in these examples.  They do NOT establish AS
regularity, stack openness, avatar reconstruction, a relative heart,
or membership in the intrinsic moduli stack H_2.  The general finite
chart statements are proved in papers/quiver-avatar/foundation_charts.tex.
"""

from __future__ import annotations

from itertools import product

import sympy as sp


Monomial = tuple[int, int, int, int]  # exponents of u,v,p,q


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def cox_basis(n: int, degree: tuple[int, int]) -> list[Monomial]:
    """Monomials of class m*s+r*f in the Cox ring of Sigma_n."""
    m, r = degree
    if m < 0:
        return []
    result = []
    for q_power in range(m + 1):
        fiber_degree = r - n * q_power
        if fiber_degree < 0:
            continue
        for u_power in range(fiber_degree + 1):
            result.append(
                (u_power, fiber_degree - u_power, m - q_power, q_power)
            )
    require(len(result) == len(set(result)), "Cox basis contains repetitions")
    return result


def multiplication(
    left: list[Monomial], right: list[Monomial], target: list[Monomial]
) -> sp.Matrix:
    """Columns are ordered left factor first, then right factor."""
    target_index = {monomial: i for i, monomial in enumerate(target)}
    matrix = sp.zeros(len(target), len(left) * len(right))
    for column, (lhs, rhs) in enumerate(product(left, right)):
        monomial = tuple(x + y for x, y in zip(lhs, rhs))
        require(monomial in target_index, "Product is absent from target basis")
        matrix[target_index[monomial], column] = 1
    return matrix


def kernel(matrix: sp.Matrix) -> sp.Matrix:
    vectors = matrix.nullspace()
    return sp.Matrix.hstack(*vectors) if vectors else sp.zeros(matrix.cols, 0)


def kron(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    """Include the empty-column tensor products used for zero kernels."""
    if left.cols == 0 or right.cols == 0:
        return sp.zeros(left.rows * right.rows, left.cols * right.cols)
    return sp.kronecker_product(left, right)


def complement(matrix: sp.Matrix) -> sp.Matrix:
    """A coordinate complement to the column space, found by exact ranks."""
    columns = matrix.columnspace()
    span = sp.Matrix.hstack(*columns) if columns else sp.zeros(matrix.rows, 0)
    chosen = []
    for index in range(matrix.rows):
        vector = sp.eye(matrix.rows)[:, index]
        enlarged = sp.Matrix.hstack(span, vector)
        if enlarged.rank() > span.rank():
            chosen.append(vector)
            span = enlarged
    require(span.rank() == matrix.rows, "Complement did not span the target")
    return sp.Matrix.hstack(*chosen) if chosen else sp.zeros(matrix.rows, 0)


def check_kernel_line(matrix: sp.Matrix, name: str) -> sp.Matrix:
    basis = kernel(matrix)
    require(basis.cols in (0, 1), f"{name}: kernel dimension is not 0 or 1")
    if basis.cols:
        tensor = sp.Matrix(2, 2, list(basis[:, 0]))
        require(tensor.det() != 0, f"{name}: kernel line is decomposable")
    return basis


def check_foundation(
    name: str,
    a: sp.Matrix,
    b: sp.Matrix,
    c: sp.Matrix,
    d: sp.Matrix,
    expected_ranks: tuple[int, int],
    expected_completion: int,
) -> None:
    require(a.shape == b.shape == (4, 4), f"{name}: incorrect a,b sizes")
    require(c.shape == d.shape == (6, 8), f"{name}: incorrect c,d sizes")
    ranks = (a.rank(), b.rank())
    require(ranks == expected_ranks, f"{name}: unexpected ranks {ranks}")
    require(sp.Matrix.hstack(c, d).rank() == 6, f"{name}: joint map not onto")

    triple = c * kron(sp.eye(2), a)
    require(
        triple == d * kron(b, sp.eye(2)),
        f"{name}: associativity failed",
    )

    ka = check_kernel_line(a, f"{name}/a")
    kb = check_kernel_line(b, f"{name}/b")
    delta_a, delta_b = ka.cols, kb.cols
    left_short = kron(sp.eye(2), ka)
    right_short = kron(kb, sp.eye(2))
    short = sp.Matrix.hstack(left_short, right_short)
    overlap = left_short.rank() + right_short.rank() - short.rank()
    require(overlap == 0, f"{name}: short-relation overlap is nonzero")

    ca, cb = complement(a), complement(b)
    require((ca.cols, cb.cols) == (delta_a, delta_b), "Wrong complement sizes")
    paths = sp.Matrix.hstack(
        triple,
        c * kron(sp.eye(2), ca),
        d * kron(cb, sp.eye(2)),
    )
    short_in_paths = short.col_join(sp.zeros(paths.cols - 8, short.cols))
    require(paths * short_in_paths == sp.zeros(6, short.cols), "Relation fails")
    require(paths.rank() == 6, f"{name}: paths do not generate A_03")
    require(paths.cols - short.rank() == 8, f"{name}: short quotient is not 8D")
    extra_relations = paths.cols - paths.rank() - short.rank()
    require(extra_relations == 2, f"{name}: wrong number of endpoint relations")

    minimal_generators = 6 + delta_a + delta_b
    minimal_relations = delta_a + delta_b + extra_relations
    completion = minimal_generators + minimal_relations
    require(completion == expected_completion, f"{name}: wrong arrow count")
    print(
        f"PASS: {name}: ranks={ranks}, overlap={overlap}, "
        f"generators={minimal_generators}, relations={minimal_relations}, "
        f"completed arrows={completion}; associativity exact."
    )


def check_hirzebruch(n: int) -> None:
    require(n in (0, 2), "This example uses Sigma_0 and Sigma_2 only")
    h_fiber_degree = (n + 2) // 2
    u = cox_basis(n, (0, 1))
    v = cox_basis(n, (1, h_fiber_degree - 1))
    w = cox_basis(n, (0, 1))
    e = cox_basis(n, (1, h_fiber_degree))
    f = cox_basis(n, (1, h_fiber_degree))
    target = cox_basis(n, (1, h_fiber_degree + 1))
    dimensions = tuple(map(len, (u, v, w, e, f, target)))
    require(dimensions == (2, 2, 2, 4, 4, 6), "Incorrect Cox Hom dimensions")
    a = multiplication(v, u, e)
    b = multiplication(w, v, f)
    c = multiplication(w, e, target)
    d = multiplication(f, u, target)
    ranks = (4, 4) if n == 0 else (3, 3)
    check_foundation(f"Sigma_{n} Cox", a, b, c, d, ranks, 8 if n == 0 else 12)
    print(f"PASS: Sigma_{n} Hom dimensions U,V,W,E,F,N = {dimensions}.")


def check_synthetic_ten() -> None:
    # a is Sym^2 of a two-dimensional space, with one unused target vector.
    a = sp.Matrix([[1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
    b = sp.eye(4)
    # c kills W tensor the unused vector and is bijective on W tensor Sym^2.
    c = sp.zeros(6, 8)
    for row, column in enumerate((0, 1, 2, 4, 5, 6)):
        c[row, column] = 1
    d = c * kron(sp.eye(2), a)
    check_foundation("synthetic finite ten-arrow algebra", a, b, c, d, (3, 4), 10)


def check_product_collection() -> None:
    objects = ((0, 0), (1, 0), (0, 1), (1, 1))
    hom_dimensions = sp.zeros(4)
    for i, degree_i in enumerate(objects):
        for j, degree_j in enumerate(objects):
            difference = tuple(y - x for x, y in zip(degree_i, degree_j))
            hom_dimensions[i, j] = len(cox_basis(0, difference))
    expected = sp.Matrix([[1, 2, 2, 4], [0, 1, 0, 2], [0, 0, 1, 2], [0, 0, 0, 1]])
    require(hom_dimensions == expected, "Product collection Hom matrix differs")
    first = cox_basis(0, (1, 0))
    second = cox_basis(0, (0, 1))
    target = cox_basis(0, (1, 1))
    through_one = multiplication(second, first, target)
    through_two = multiplication(first, second, target)
    all_paths = sp.Matrix.hstack(through_one, through_two)
    require(all_paths.shape == (4, 8), "Product paths have wrong size")
    require(all_paths.rank() == 4, "Product paths do not span Hom(O,O(1,1))")
    relations = all_paths.cols - all_paths.rank()
    require(relations == 4, "Product collection does not have four relations")
    require(4 * 2 + relations == 12, "Product relation completion differs")
    print("PASS: product collection: 8 generating arrows, 4 relations, 12 completed arrows.")


def main() -> None:
    check_hirzebruch(0)
    check_hirzebruch(2)
    check_synthetic_ten()
    check_product_collection()
    print("PASS: finite examples only; no AS, relative-stack, or intrinsic-H2 certification.")


if __name__ == "__main__":
    main()

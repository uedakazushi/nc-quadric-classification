"""Exact samples for the relative AS/avatar and raw QP boundary comparisons."""
from sympy import Matrix, Symbol, diag, expand, eye, groebner, linsolve, linear_eq_to_matrix, rem


epsilon = Symbol("epsilon")


def dual_numbers(matrix):
    return matrix.applyfunc(lambda entry: rem(expand(entry), epsilon**2, epsilon))


def check_oriented_gram():
    """Distinguish the determinant coordinate and test uniqueness at rank three."""
    form = diag(1, 1, -1, -1)
    constant = diag(1, 1, 1, 0)
    moving = diag(1, 1, 1, epsilon)

    assert dual_numbers(constant.T * form * constant) == dual_numbers(moving.T * form * moving)
    assert constant.det() == 0 and moving.det() == epsilon

    skew = Matrix([
        [0, 2, 0, 1],
        [-2, 0, 3, 0],
        [0, -3, 0, 5],
        [-1, 0, -5, 0],
    ])
    isometry_derivative = form * skew
    isometry = eye(4) + epsilon * isometry_derivative
    other_lift = dual_numbers(isometry * moving)
    assert dual_numbers(other_lift.T * form * other_lift) == dual_numbers(moving.T * form * moving)
    assert rem(expand(other_lift.det()), epsilon**2, epsilon) == epsilon

    entries = [Symbol(f"x{row}{column}") for row in range(4) for column in range(4)]
    unknown = Matrix(4, 4, entries)
    equations = list(unknown.T * form + form * unknown)
    equations += list(
        dual_numbers((eye(4) + epsilon * unknown) * moving - other_lift)
        .applyfunc(lambda entry: expand(entry).coeff(epsilon))
    )
    matrix, rhs = linear_eq_to_matrix(equations, entries)
    assert linsolve((matrix, rhs), entries) == {tuple(isometry_derivative)}
    print("PASS: oriented Gram distinction and unique determinant-one lift over dual numbers")


def check_nonflat_point_incidence():
    """Read the affine intersection ideal in the chart where x11 is a unit."""
    x00, x01, x10 = (Symbol(name) for name in ("x00", "x01", "x10"))
    quadric = x00 - x01 * x10
    second_quadric = quadric + epsilon

    assert second_quadric.subs(x00, x01 * x10) == epsilon
    incidence = groebner([epsilon**2, quadric, second_quadric], x00, x01, x10, epsilon)
    # The nonzero class of 1 is killed by epsilon and cannot be an epsilon multiple.
    assert incidence.reduce(epsilon)[1] == 0
    assert incidence.reduce(x00 - x01 * x10)[1] == 0
    assert incidence.reduce(1 + 0 * epsilon)[1] == 1
    print("PASS: a flat AS first-order parameter can impose epsilon on the affine point incidence")


def linear_part_of_cyclic_derivative(cycles, arrow):
    """Return only the single-arrow terms of the cyclic derivative."""
    terms = {}
    for coefficient, word in cycles:
        if len(word) != 2:
            continue
        for index, letter in enumerate(word):
            if letter == arrow:
                other = word[1 - index]
                terms[other] = terms.get(other, 0) + coefficient
    return terms


def check_double_mass_generator_types():
    arrows = ("x", "y", "u", "v")
    left_mass, right_mass = Symbol("lambda"), Symbol("mu")
    cycles = [(left_mass, ("y", "x")), (right_mass, ("v", "u"))]
    derivatives = [linear_part_of_cyclic_derivative(cycles, arrow) for arrow in arrows]
    linear_relations = Matrix([
        [derivative.get(arrow, 0) for arrow in arrows]
        for derivative in derivatives
    ])
    for left, right in ((0, 0), (0, 1), (1, 0), (1, 1)):
        rank = linear_relations.subs({left_mass: left, right_mass: right}).rank()
        assert 4 - rank == 2 * int(left == 0) + 2 * int(right == 0)
    print("PASS: simultaneous vanishing of both masses leaves generators of both parities")


if __name__ == "__main__":
    check_oriented_gram()
    check_nonflat_point_incidence()
    check_double_mass_generator_types()
    print("Scope: three finite boundary checks, separate from the relative stack proofs.")

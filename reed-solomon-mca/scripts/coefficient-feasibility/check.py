"""Exact controls for the coefficient formulation; no search or global bound.

Supplied coefficients are in F_97. Field splitting is checked exactly for
F_(97^20). The mathematical system itself allows all coefficients in that
extension field; these controls do not enumerate its inputs.
"""

import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "resultant_control", ROOT / "scripts/resultant-pencil/check.py")
alg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(alg)
base = alg.base
P, H = base.P, base.H
ZERO, ONE, T = alg.ZERO, alg.ONE, alg.T


def coefficient(f, index):
    return f[index] if 0 <= index < len(f) else 0


def matrix_for_affine_moments(locator_coefficients):
    """24 recurrence coefficients, on (u_1,...,u_8,v_1,...,v_8)."""
    assert len(locator_coefficients) == 5
    rows = []
    for i in range(4):
        for h in range(6):
            row = [0] * 16
            for j, f in enumerate(locator_coefficients):
                row[i + j] = coefficient(f, h)
                row[8 + i + j] = coefficient(f, h - 1)
            rows.append(row)
    return rows


def kernel_basis(matrix):
    rows = [list(row) for row in matrix]
    pivots = []
    width = len(rows[0])
    for column in range(width):
        pivot = next((i for i in range(len(pivots), len(rows))
                      if rows[i][column] % P), None)
        if pivot is None:
            continue
        k = len(pivots)
        rows[k], rows[pivot] = rows[pivot], rows[k]
        inverse = pow(rows[k][column] % P, -1, P)
        rows[k] = [v * inverse % P for v in rows[k]]
        for i in range(len(rows)):
            if i != k:
                factor = rows[i][column]
                rows[i] = [(v - factor * w) % P
                           for v, w in zip(rows[i], rows[k])]
        pivots.append(column)
    basis = []
    for free in range(width):
        if free in pivots:
            continue
        vector = [0] * width
        vector[free] = 1
        for i, pivot in enumerate(pivots):
            vector[pivot] = -rows[i][free] % P
        basis.append(tuple(vector))
    for vector in basis:
        assert all(sum(a * b for a, b in zip(row, vector)) % P == 0
                   for row in matrix)
    return len(pivots), basis


def locators_by_coordinate(coefficients):
    return {x: base.trim([sum(coefficient(f, h) * pow(x, j, P)
                             for j, f in enumerate(coefficients)) % P
                          for h in range(5)]) for x in H}


def coefficient_power_audit(r):
    """Top-down fourth-root recursion, followed by all 48 residuals."""
    if alg.degree(r) != 64:
        return None, {"degree": alg.degree(r), "degree_gate": False}
    normalized = alg.monic(r)
    reverse_root = [1]
    inverse_four = pow(4, -1, P)
    for j in range(1, 17):
        previous = alg.power(base.trim(reverse_root), 4)
        value = (normalized[64 - j] - coefficient(previous, j)) * inverse_four % P
        reverse_root.append(value)
    candidate = base.trim(list(reversed(reverse_root)))
    expected = alg.power(candidate, 4)
    assert alg.degree(candidate) == 16 and candidate[-1] == 1
    assert all(coefficient(expected, 64 - j) == normalized[64 - j]
               for j in range(17))
    failures = [j for j in range(17, 65)
                if coefficient(expected, 64 - j) != normalized[64 - j]]
    # Check the separately written denominator-cleared recurrence and
    # residual equations; c != 0 must still be retained in that system.
    c = r[-1]
    cleared_root = [1]
    for j in range(1, 17):
        z_j = pow(c, j, P) * reverse_root[j] % P
        previous = alg.power(base.trim(cleared_root), 4)
        assert 4 * z_j % P == (pow(c, j - 1, P) * r[64 - j]
                               - coefficient(previous, j)) % P
        cleared_root.append(z_j)
    cleared_power = alg.power(base.trim(cleared_root), 4)
    cleared_failures = [j for j in range(17, 65)
                        if (pow(c, j - 1, P) * r[64 - j]
                            - coefficient(cleared_power, j)) % P]
    assert cleared_failures == failures
    return candidate, {"degree": 64, "degree_gate": True,
                       "triangular_coefficients": 16,
                       "residual_equations": 48,
                       "cleared_denominator_equations_checked": True,
                       "failed_residuals": failures,
                       "power_identity": not failures}


def primitive(coefficients):
    common = ZERO
    for f in coefficients:
        common = alg.gcd(common, f)
    return common == ONE


def minor_proportionality(coefficients, moment_vector):
    a = base.word_with_syndrome(moment_vector[:8])
    b = base.word_with_syndrome(moment_vector[8:])
    d, actual, _ = base.locator(a, b)
    if d == ZERO:
        return False
    pivot = next((j, h) for j, f in enumerate(coefficients)
                 for h, value in enumerate(f) if value)
    j, h = pivot
    scalar = coefficient(actual[j], h) * pow(coefficients[j][h], -1, P) % P
    return bool(scalar) and actual == tuple(base.scale(f, scalar) for f in coefficients)


def audit_actual(name, a, b, expected_persistent=False):
    d, coefficients, locators = base.locator(a, b)
    moment_vector = base.syndrome(a) + base.syndrome(b)
    matrix = matrix_for_affine_moments(coefficients)
    assert all(sum(c * v for c, v in zip(row, moment_vector)) % P == 0
               for row in matrix)
    assert locators == locators_by_coordinate(coefficients)
    rank, basis = kernel_basis(matrix)
    assert rank <= 15 and basis
    r = alg.resultant_product(locators)
    candidate, recursion = coefficient_power_audit(r)
    coordinate_squarefree = all(f != ZERO and alg.gcd(f, alg.derivative(f)) == ONE
                                for f in locators.values())
    persistent = any(f == ZERO for f in locators.values())
    assert persistent == expected_persistent
    record = {"name": name, "compatibility_rank": rank,
              "kernel_dimension": len(basis), "primitive_coefficients": primitive(coefficients),
              "nonzero_hankel_determinant": d != ZERO,
              "persistent_coordinate": persistent,
              "coordinate_squarefree": coordinate_squarefree,
              "coefficient_power_audit": recursion}
    if primitive(coefficients) and max(map(alg.degree, coefficients)) == 4:
        nonzero_minor_kernels = sum(minor_proportionality(coefficients, vector)
                                   for vector in basis)
        record["kernel_basis_vectors_with_proportional_nonzero_minors"] = nonzero_minor_kernels
        # These actual controls have a one-dimensional compatible space.
        assert len(basis) == 1 and nonzero_minor_kernels == 1
    if candidate is not None and recursion["power_identity"]:
        assert alg.target_power_root(r) == candidate or alg.gcd(candidate, alg.derivative(candidate)) != ONE
    return record


def balanced_bivariate_control():
    multipliers = tuple(pow(8, i, P) for i in range(4))
    # C(T,X)=product_(alpha in A)(T-alpha*X), with both degrees at most 4.
    coefficients = [ONE]
    for alpha in multipliers:
        updated = [ZERO] * (len(coefficients) + 1)
        for j, f in enumerate(coefficients):
            updated[j] = base.add(updated[j], base.multiply(T, f))
            updated[j + 1] = base.add(updated[j + 1], base.scale(f, -alpha))
        coefficients = updated
    coefficients = tuple(coefficients)
    locators = locators_by_coordinate(coefficients)
    r = alg.resultant_product(locators)
    candidate, recursion = coefficient_power_audit(r)
    assert candidate == base.root_polynomial(H) and recursion["power_identity"]
    assert alg.equality_check(coefficients[4], locators, r)
    supports = {t: tuple(x for x in H if base.evaluate(locators[x], t) == 0)
                for t in H}
    assert all(len(support) == 4 for support in supports.values())
    assert len(set(supports.values())) == 16
    assert all(sum(x in support for support in supports.values()) == 4 for x in H)
    assert primitive(coefficients)
    rank, basis = kernel_basis(matrix_for_affine_moments(coefficients))
    assert rank == 16 and not basis
    return {"multipliers": multipliers, "locator_coefficients": coefficients,
            "full_algebraic_equality_conditions": True,
            "distinct_four_coordinate_supports": 16,
            "compatibility_rank": rank, "kernel_dimension": 0,
            "coefficient_power_audit": recursion,
            "interpretation": "Fabricated locator only; no affine moment pencil exists."}


def main():
    first, second = H[:5], H[5:10]
    a, b = alg.two_block(first, second)
    dense_a = base.word_with_syndrome((2, 7, 11, 19, 23, 31, 41, 43))
    dense_b = base.word_with_syndrome((5, 13, 17, 29, 37, 47, 53, 59))
    e0 = tuple(i + 1 if i < 4 else 0 for i in range(16))
    e1 = tuple(i + 2 if 4 <= i < 8 else 0 for i in range(16))
    direction = tuple((v - u) % P for u, v in zip(e0, e1))
    fixed_direction = tuple((3 * i + 1) % P if i < 4 else 0 for i in range(16))
    records = [audit_actual("existing_two_block", a, b),
               audit_actual("specified_dense_moments", dense_a, dense_b),
               audit_actual("two_disjoint_four_error_points", e0, direction),
               audit_actual("persistent_four_support", e0, fixed_direction, True)]
    balanced = balanced_bivariate_control()

    # A fourth-power scalar is not required to be a fourth power itself.
    scalar = next(x for x in range(1, P) if pow(x, 24, P) != 1)
    split = base.root_polynomial(H)
    candidate, audit = coefficient_power_audit(base.scale(alg.power(split, 4), scalar))
    assert candidate == split and audit["power_identity"]
    assert alg.field_root_part(candidate, 20) == candidate
    # A squarefree fourth power need not split in the specified extension.
    # Compute the exact Frobenius remainder rather than extrapolating.
    nonsplit = (-5 % P,) + (0,) * 15 + (1,)
    assert alg.gcd(nonsplit, alg.derivative(nonsplit)) == ONE
    nonsplit_candidate, nonsplit_audit = coefficient_power_audit(alg.power(nonsplit, 4))
    assert nonsplit_candidate == nonsplit and nonsplit_audit["power_identity"]
    splitting_factor = alg.field_root_part(nonsplit, 20)
    assert splitting_factor != nonsplit

    report = {"scope": "Four actual controls and one fabricated bivariate locator; no feasibility search.",
              "coefficient_field": P, "target_extension_degree": 20,
              "actual_controls": records, "fabricated_balanced_control": balanced,
              "non_fourth_power_scalar_control": scalar,
              "nonsplit_fourth_power_root_count_in_target_field": alg.degree(splitting_factor)}
    output = Path(__file__).with_name("result.json")
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("PASS: triangular fourth-root coefficients and 48 residuals agree with exact polynomial identities.")
    print("PASS: all four actual controls satisfy the 24 affine-recurrence equations; valid primitive kernels recover their minors.")
    print("PASS: a split balanced locator with sixteen distinct supports has compatibility rank 16 and cannot arise from affine moments.")
    print("PASS: persistent-root, unrestricted scalar and exact extension-field splitting controls remain separate gates.")
    print("No witness, impossibility result or improved global count is claimed.")


if __name__ == "__main__":
    main()

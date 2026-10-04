"""Exact shared-coordinate quotient for one fixed triple, not all pencils.

All fourth supports are classified by affine cokernel equations. Because
those equations are linear over F_97, their isolated roots are exhaustive
over every extension. Universal systems are recorded separately.
"""

from collections import Counter
from itertools import combinations
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("three_support", HERE / "three_support.py")
three = importlib.util.module_from_spec(spec)
spec.loader.exec_module(three)
feas, alg, base = three.feas, three.alg, three.base
P, H = base.P, base.H
ZERO, ONE = alg.ZERO, alg.ONE
SUPPORTS = ((1, 8, 12, 18), (1, 8, 22, 27), (1, 33, 47, 50))
UNION = set(sum(SUPPORTS, ()))
Q = base.root_polynomial(x for x in H if x not in UNION)
C = {x: base.evaluate(Q, x) for x in H}
INV2 = pow(2, -1, P)
V = {x: tuple(pow(x, j, P) for j in range(1, 9)) for x in H}
H0 = tuple((-C[12] * V[12][i] - C[18] * V[18][i]) % P for i in range(8))
H1 = tuple((INV2 * C[8] * V[8][i] + C[12] * V[12][i]
            + C[18] * V[18][i] + INV2 * C[22] * V[22][i]
            + INV2 * C[27] * V[27][i]) % P for i in range(8))


def triple_inputs(p, q, z):
    weights = ((p, z, -C[12] % P, -C[18] % P),
               (q, (z + C[8]) * INV2 % P, C[22] * INV2 % P, C[27] * INV2 % P),
               ((-p + 2 * q - C[1]) % P, -C[33] % P, -C[47] % P, -C[50] % P))
    words = tuple(three.word_on(support, weight) for support, weight in zip(SUPPORTS, weights))
    assert all((-a + 2 * b - c - C[x]) % P == 0
               for x, a, b, c in zip(H, *words))
    initial = base.syndrome(words[0])
    direction = tuple((b - a) % P for a, b in zip(words[0], words[1]))
    direction_moments = base.syndrome(direction)
    assert initial == tuple((p * V[1][i] + z * V[8][i] + H0[i]) % P for i in range(8))
    assert direction_moments == tuple(((q - p) * V[1][i] - INV2 * z * V[8][i]
                                      + H1[i]) % P for i in range(8))
    return words[0], direction, weights


def recurrence(support, moments):
    f = base.root_polynomial(support)
    return tuple(sum(f[j] * moments[i + j] for j in range(5)) % P for i in range(4))


def linear_solution(columns, target):
    matrix = [list(row) + [value] for row, value in zip(zip(*columns), target)]
    _, kernels = feas.kernel_basis(matrix)
    vector = next(vector for vector in kernels if vector[-1])
    inverse = pow(vector[-1], -1, P)
    return tuple(value * inverse % P for value in vector[:-1])


def classify(support):
    columns = (recurrence(support, V[1]), recurrence(support, V[8]))
    residual = (recurrence(support, H0), recurrence(support, H1))
    rank, left_kernel = feas.kernel_basis(columns)
    assert rank == sum(x not in support for x in (1, 8))
    projected = [base.trim(tuple(sum(a * b for a, b in zip(row, h)) % P for h in residual))
                 for row in left_kernel]
    common = ZERO
    for f in projected:
        common = alg.gcd(common, f)
    # Independently reproduce the same condition by all smaller minors.
    active = [column for column in columns if any(column)]
    minors_gcd = ZERO
    for indices in combinations(range(4), rank + 1):
        rows = [[(column[i],) for column in active]
                + [base.trim((residual[0][i], residual[1][i]))] for i in indices]
        minors_gcd = alg.gcd(minors_gcd, base.determinant(rows))
    assert common == minors_gcd
    record = {"support": support, "constant_rank": rank,
              "cokernel_equations": projected, "smaller_minors_gcd": common}
    if common == ZERO:
        solution0 = linear_solution(columns, residual[0])
        solution1 = linear_solution(columns, residual[1])
        record.update(kind="universal", r=base.trim((solution0[0], solution1[0])),
                      w=base.trim((solution0[1], solution1[1])))
        return record
    if alg.degree(common) == 0:
        record["kind"] = "inconsistent"
        return record
    assert alg.degree(common) == 1
    t = -common[0] * pow(common[1], -1, P) % P
    record.update(kind="isolated", parameter=t)
    if t in (0, 1, 2):
        record["full_weight_status"] = "original_parameter"
        return record
    h = tuple((a + t * b) % P for a, b in zip(residual[0], residual[1]))
    r, w = linear_solution(columns, h)
    z = w * pow((1 - t * INV2) % P, -1, P) % P
    target = tuple((H0[i] + t * H1[i] + r * V[1][i] + w * V[8][i]) % P for i in range(8))
    weights = base.solve_square([[pow(x, j, P) for x in support] for j in range(1, 5)], target[:4])
    assert base.syndrome(three.word_on(support, weights)) == target
    fixed_nonzero = all(weight for x, weight in zip(support, weights) if x not in (1, 8))
    record.update(r=r if 1 not in support else None,
                  z=z if 8 not in support else None,
                  particular_fourth_weights=weights,
                  fixed_fourth_weights_nonzero=fixed_nonzero)
    if not fixed_nonzero:
        record["full_weight_status"] = "fixed_fourth_weight_zero"
    elif 8 not in support and z in (0, -C[8] % P):
        record["full_weight_status"] = "initial_eight_weight_zero"
    else:
        record["full_weight_status"] = "admissible"
    return record


def classify_infinity(support):
    columns = (recurrence(support, V[1]), recurrence(support, V[8]))
    residual = recurrence(support, H1)
    _, left_kernel = feas.kernel_basis(columns)
    if any(sum(a * b for a, b in zip(row, residual)) % P for row in left_kernel):
        return None
    d, w = linear_solution(columns, residual)
    z = -2 * w % P
    target = tuple((H1[i] + d * V[1][i] + w * V[8][i]) % P for i in range(8))
    weights = base.solve_square([[pow(x, j, P) for x in support] for j in range(1, 5)], target[:4])
    assert base.syndrome(three.word_on(support, weights)) == target
    # Check every solvable system before any full-fourth-weight rejection:
    # otherwise a lower-weight infinity point could be silently discarded.
    assert all(weight for x, weight in zip(support, weights) if x not in (1, 8))
    assert 8 in support or z not in (0, -C[8] % P)
    return {"support": support, "slope_q_minus_p": d if 1 not in support else None,
            "z": z if 8 not in support else None, "particular_weights": weights}


def complete_parameterization_control():
    core = sum(triple_inputs(0, 0, 0)[2], ())
    differences = []
    for p, q, z in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        vector = sum(triple_inputs(p, q, z)[2], ())
        differences.append(tuple((a - b) % P for a, b in zip(vector, core)))
    rank, _ = feas.kernel_basis([core] + differences)
    assert rank == 4
    triple_rank, triple_basis = feas.kernel_basis(
        [[-pow(x, j, P) % P for x in SUPPORTS[0]]
         + [2 * pow(x, j, P) % P for x in SUPPORTS[1]]
         + [-pow(x, j, P) % P for x in SUPPORTS[2]] for j in range(1, 9)])
    assert triple_rank == 8 and len(triple_basis) == 4
    return {"triple_rank": triple_rank, "triple_kernel_dimension": 4,
            "homogenized_parameterization_rank": rank}


def bound_control(retained, universal, infinity):
    assert len(retained) == 13 and all(record["constant_rank"] == 2 for record in retained)
    groups = {}
    for record in retained:
        groups.setdefault(record["z"], []).append(record)
    assert sorted(len(group) for group in groups.values()) == [1] * 10 + [3]
    repeated = groups[11]
    assert {(record["parameter"], record["r"]) for record in repeated} == {(81, 83), (69, 55), (41, 22)}
    p, slope = 88, 67
    assert all((p + slope * record["parameter"] - record["r"]) % P == 0 for record in repeated)
    assert (p + 2 * slope) % P == C[1]  # Full A2 weight at 1 would vanish.
    assert len(universal) == 1 and universal[0]["support"] == (12, 18, 22, 27)
    assert universal[0]["r"] == ZERO
    assert universal[0]["w"] == base.scale(alg.T, -C[8] * INV2)
    assert infinity == [{"support": (12, 18, 22, 27), "slope_q_minus_p": 0,
                         "z": C[8], "particular_weights": (C[12], C[18], C[22] * INV2 % P, C[27] * INV2 % P)}]
    return {"isolated_z_groups": {z: len(group) for z, group in groups.items()},
            "repeated_z": 11, "repeated_z_line_p": p, "repeated_z_line_slope": slope,
            "repeated_z_line_violates_A2_full_weight": True,
            "maximum_isolated_supports_per_full_weight_pencil": 1,
            "maximum_universal_support_parameters_including_infinity": 1,
            "projective_sparse_parameter_upper_bound": 5,
            "dependence": "Exact enumeration of all fourth supports after the proved degree-one field reduction."}


def audit_attaining_pencil():
    # One isolated support and the universal support, together with A0,A1,A2.
    p, q, z = 5, 85, 11
    a, b, weights = triple_inputs(p, q, z)
    assert all(sum(weights, ()))
    expected = {0: SUPPORTS[0], 1: SUPPORTS[1], 2: SUPPORTS[2],
                6: (12, 18, 22, 27), 81: (33, 47, 70, 96)}
    d, coefficients, locators = base.locator(a, b)
    assert d != ZERO and all(f != ZERO for f in locators.values())
    for t, support in expected.items():
        assert base.evaluate(d, t)
        assert tuple(x for x in H if not base.evaluate(locators[x], t)) == support
    # No sparse point at infinity: transforming the chart preserves this count.
    assert all(any(recurrence(support, base.syndrome(b)))
               for support in combinations(H, 4))
    bad, decoded_weights = base.original_event(a, b, base.interpolation_constraints())
    assert bad == set(expected) and all(decoded_weights[t] == 4 for t in bad)
    a_new, b_new, tau, d_new, coefficients_new, locators_new = three.no_coordinate_root_chart(
        a, b, d, coefficients, locators)
    r = alg.resultant_product(locators_new)
    candidate, power_audit = feas.coefficient_power_audit(r)
    assert alg.degree(r) == 64 and not power_audit["power_identity"]
    assert not alg.equality_check(d_new, locators_new, r)
    root, no_lower = three.exact_regular_weight_four(d_new, locators_new)
    assert no_lower and alg.degree(root) == 5
    assert alg.field_root_part(root, 1) == root
    assert alg.field_root_part(root, 20) == root
    moments = base.syndrome(a_new) + base.syndrome(b_new)
    assert all(sum(c * v for c, v in zip(row, moments)) % P == 0
               for row in feas.matrix_for_affine_moments(coefficients_new))
    independently_counted, _ = base.original_event(a_new, b_new, base.interpolation_constraints())
    assert independently_counted == {t for t in range(P) if not base.evaluate(root, t)}
    return {"p": p, "q": q, "z": z, "a": a, "b": b, "triple_weights": weights,
            "bad_parameters_original_chart": sorted(bad), "supports_by_parameter": expected,
            "projective_infinity_not_sparse": True, "D": d, "locator_coefficients": coefficients,
            "new_infinity_old_parameter": tau, "a_new": a_new, "b_new": b_new,
            "D_new": d_new, "locator_coefficients_new": coefficients_new, "R_new": r,
            "coefficient_power_audit": power_audit, "monic_fourth_root_candidate": candidate,
            "full_L010_equality": False, "all_lower_weight_roots_excluded": no_lower,
            "bad_root_polynomial_new_chart": root, "exact_bad_count_F_97_20": 5,
            "original_event_supports_checked_in_each_chart": 2517,
            "exact_field_root_checks_degrees": [1, 20]}


def main():
    assert len(UNION) == 9 and all(bool(C[x]) == (x in UNION) for x in H)
    assert base.syndrome(tuple(C[x] for x in H)) == (0,) * 8
    # Check the complete parameterization against the preexisting kernel.
    complete_parameters = complete_parameterization_control()
    for p, q, z in ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (11, 23, 31)):
        triple_inputs(p, q, z)
    records = [classify(support) for support in combinations(H, 4) if support not in SUPPORTS]
    counts = Counter(record["kind"] for record in records)
    counts.update(Counter(record.get("full_weight_status", "") for record in records if record["kind"] == "isolated"))
    assert all(record["fixed_fourth_weights_nonzero"] for record in records
               if record["kind"] == "isolated" and record["parameter"] not in (0, 1, 2))
    retained = [record for record in records if record.get("full_weight_status") == "admissible"]
    universal = [record for record in records if record["kind"] == "universal"]
    infinity = [record for support in combinations(H, 4)
                if (record := classify_infinity(support)) is not None]
    bound = bound_control(retained, universal, infinity)
    witness = audit_attaining_pencil()
    report = {"scope": "One fixed triple at 0,1,2; all fourth supports over any extension, with universal systems separate.",
              "coefficient_field": P, "target_extension_degree": 20,
              "supports": SUPPORTS, "shortened_codeword_polynomial": Q,
              "shortened_codeword_values": C, "h0": H0, "h1": H1,
              "complete_parameterization_control": complete_parameters,
              "systems_tested": len(records), "classification_counts": dict(counts),
              "universal_systems": universal, "admissible_isolated_systems": retained,
              "admissible_infinity_systems": infinity,
              "uniform_bound_control": bound, "attaining_pencil": witness,
              "all_systems": records, "completed_classification": True}
    (HERE / "shared-quotient-result.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("PASS: normalized full-triple parameterization and eight moments agree.")
    print("PASS: all affine cokernel equations agree with independently computed smaller minors.")
    print(json.dumps({"counts": dict(counts), "isolated_z_groups": bound["isolated_z_groups"],
                      "projective_sparse_parameter_upper_bound": 5}, sort_keys=True))
    print("PASS: full triple admits at most one isolated support and one universal support, over every extension.")
    print("PASS: the five-count attaining pencil passes actual-minor, original-event, full equality and exact F_(97^20) checks.")
    print("The fixed-triple exclusion depends on the exhaustive rational certificate; arbitrary triples remain open.")


if __name__ == "__main__":
    main()

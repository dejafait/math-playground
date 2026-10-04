"""Solve constrained three-/four-support pencils, then audit actual minors.

The six triple layouts and one-dimensional prime-field fourth kernels are
a bounded candidate generator. Unsearched extension roots, zero determinant
families and larger kernels are counted explicitly. Splitting of retained
prime-field pencils is tested exactly over F_(97^20).
"""

from collections import Counter
from itertools import combinations
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("feasibility", HERE / "check.py")
feas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(feas)
alg, base = feas.alg, feas.base
P, H = base.P, base.H
ZERO, ONE, T = alg.ZERO, alg.ONE, alg.T
SUPPORTS = tuple(combinations(H, 4))
LAYOUT_INDICES = (
    ((0, 1, 2, 3), (0, 1, 4, 5), (0, 6, 7, 8)),
    ((0, 1, 2, 3), (0, 1, 4, 5), (6, 7, 8, 9)),
    ((0, 1, 2, 3), (0, 4, 5, 6), (1, 4, 7, 8)),
    ((0, 1, 2, 3), (0, 4, 5, 6), (7, 8, 9, 10)),
    ((0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 8, 9)),
    ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11)),
)


def word_on(support, weights):
    return tuple(weights[support.index(x)] if x in support else 0 for x in H)


def triple_space(supports):
    a0, a1, a2 = supports
    matrix = [[(-pow(x, j, P)) % P for x in a0]
              + [(2 * pow(x, j, P)) % P for x in a1]
              + [(-pow(x, j, P)) % P for x in a2]
              for j in range(1, 9)]
    rank, basis = feas.kernel_basis(matrix)
    assert rank == 8 and len(basis) == 4
    initial, direction = [], []
    for weights in basis:
        u = base.syndrome(word_on(a0, weights[:4]))
        end = base.syndrome(word_on(a1, weights[4:8]))
        third = base.syndrome(word_on(a2, weights[8:]))
        v = tuple((b - a) % P for a, b in zip(u, end))
        assert tuple((a + 2 * b) % P for a, b in zip(u, v)) == third
        initial.append(u)
        direction.append(v)
    return basis, initial, direction


def shared_coordinate_control():
    supports = tuple(tuple(H[i] for i in entry) for entry in LAYOUT_INDICES[0])
    common = set(supports[0]) & set(supports[1]) & set(supports[2])
    assert common == {1}
    x = next(iter(common))
    weights = (T, (-1 % P, 1), (-2 % P, 1))
    for j in range(1, 9):
        u, v, w = (base.scale(f, pow(x, j, P)) for f in weights)
        assert base.add(base.add(base.scale(u, -1), base.scale(v, 2)), base.scale(w, -1)) == ZERO
        assert base.add(base.multiply((1, -1), u), base.multiply(T, v)) == ZERO
    return {"layout": 0, "common_coordinate": x,
            "shared_coordinate_weights_at_parameters_0_1_2": weights,
            "triple_kernel_polynomial_identity": True,
            "zero_syndrome_at_fourth_parameter_polynomial_identity": True,
            "all_twelve_weights_nonzero_gate_fails": True,
            "interpretation": "Nonzero polynomial kernel exists for every fourth-support matrix; it is inadmissible."}


def fourth_matrix(support, initial, direction):
    f = base.root_polynomial(support)
    return [[base.trim((sum(f[j] * u[i + j] for j in range(5)),
                        sum(f[j] * v[i + j] for j in range(5))))
             for u, v in zip(initial, direction)] for i in range(4)]


def scalar_determinant(rows):
    """Independent elimination determinant for polynomial evaluations."""
    rows = [list(row) for row in rows]
    answer = 1
    for j in range(len(rows)):
        pivot = next((i for i in range(j, len(rows)) if rows[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            rows[j], rows[pivot] = rows[pivot], rows[j]
            answer = -answer % P
        value = rows[j][j]
        answer = answer * value % P
        inverse = pow(value, -1, P)
        for i in range(j + 1, len(rows)):
            factor = rows[i][j] * inverse % P
            for k in range(j + 1, len(rows)):
                rows[i][k] = (rows[i][k] - factor * rows[j][k]) % P
    return answer


def line_key(u, v):
    minors = tuple((u[i] * v[j] - u[j] * v[i]) % P
                   for i, j in combinations(range(8), 2))
    assert any(minors)
    inverse = pow(next(value for value in minors if value), -1, P)
    return tuple(value * inverse % P for value in minors)


def affine_chart(f, tau):
    # Homogeneous degree-four substitution (U,V)=(1+T,tau*T).
    result = ZERO
    for h, value in enumerate(f):
        monomial = (0,) * h + (value * pow(tau, h, P) % P,)
        result = base.add(result, base.multiply(monomial, alg.power((1, 1), 4 - h)))
    return result


def no_coordinate_root_chart(a, b, d, coefficients, locators):
    tau = next(t for t in range(P) if base.evaluate(d, t)
               and all(base.evaluate(f, t) for f in locators.values()))
    direction = tuple((u + tau * v) % P for u, v in zip(a, b))
    new_coefficients = tuple(affine_chart(f, tau) for f in coefficients)
    new_d = new_coefficients[-1]
    new_locators = feas.locators_by_coordinate(new_coefficients)
    assert new_d == affine_chart(d, tau)
    assert all(new_locators[x] == affine_chart(f, tau)
               for x, f in locators.items())
    assert alg.degree(new_d) == 4
    assert all(alg.degree(f) == 4 for f in new_locators.values())
    return a, direction, tau, new_d, new_coefficients, new_locators


def exact_regular_weight_four(d, locators):
    """Count distinct-coordinate roots, permitting unrelated repeated roots.

    Each coordinate radical contributes one incidence. The multiplicity-four
    factor of their product, with D-roots removed, is exactly the regular
    four-error set over the algebraic closure. If all locators have gcd one,
    L010 excludes lower-weight parameters too.
    """
    distinct_product, common = ONE, ZERO
    for f in locators.values():
        common = alg.gcd(common, f)
        radical = alg.quotient(f, alg.gcd(f, alg.derivative(f)))
        distinct_product = base.multiply(distinct_product, alg.monic(radical))
    factors = alg.squarefree_factors(distinct_product)
    four = factors.get(4, ONE)
    four = alg.quotient(four, alg.gcd(four, d))
    in_field = alg.field_root_part(four, 20)
    return alg.monic(in_field), common == ONE


def audit_candidate(a, b, metadata, stats):
    d, coefficients, locators = base.locator(a, b)
    if d == ZERO:
        stats["zero_D"] += 1
        return None
    if any(f == ZERO for f in locators.values()):
        stats["persistent_locator"] += 1
        return None
    for t, support in zip((0, 1, 2, metadata["fourth_parameter"]),
                          metadata["supports"]):
        assert base.evaluate(d, t)
        assert tuple(x for x in H if not base.evaluate(locators[x], t)) == tuple(support)
    a, b, tau, d, coefficients, locators = no_coordinate_root_chart(
        a, b, d, coefficients, locators)
    r = alg.resultant_product(locators)
    _, recursion = feas.coefficient_power_audit(r)
    full_equality = alg.equality_check(d, locators, r)
    assert full_equality == (recursion["power_identity"]
                             and alg.target_power_root(r) is not None
                             and alg.field_root_part(alg.target_power_root(r), 20)
                             == alg.target_power_root(r)
                             and alg.gcd(alg.target_power_root(r), d) == ONE
                             and all(alg.gcd(f, alg.derivative(f)) == ONE
                                     for f in locators.values()))
    stats["actual_nonpersistent_pencils"] += 1
    stats["power_identity"] += int(recursion["power_identity"])
    stats["full_equality"] += int(full_equality)
    root, no_lower = exact_regular_weight_four(d, locators)
    count = alg.degree(root)
    stats["weight_four_counts_F_97_20"][count] += 1
    if no_lower:
        stats["exact_total_counts_F_97_20"][count] += 1
    else:
        stats["possible_lower_weight_unresolved"] += 1
    return {**metadata, "a": a, "b": b, "new_infinity_old_parameter": tau,
            "D": d, "locator_coefficients": coefficients, "R": r,
            "coefficient_power_audit": recursion, "full_L010_equality": full_equality,
            "bad_weight_four_root_polynomial": root,
            "all_lower_weight_parameters_excluded": no_lower,
            "exact_bad_count_F_97_20": count if no_lower else None,
            "weight_four_count_F_97_20": count}


def independent_best_audit(record):
    a, b = record["a"], record["b"]
    d, coefficients, locators = base.locator(a, b)
    assert d == record["D"] and coefficients == tuple(record["locator_coefficients"])
    bad, weights = base.original_event(a, b, base.interpolation_constraints())
    roots = record["bad_weight_four_root_polynomial"]
    expected = {t for t in range(P) if not base.evaluate(roots, t)}
    assert record["all_lower_weight_parameters_excluded"] and bad == expected
    assert all(weights[t] == 4 for t in bad)
    # The input moments satisfy the independently assembled recurrence matrix.
    moments = base.syndrome(a) + base.syndrome(b)
    matrix = feas.matrix_for_affine_moments(coefficients)
    assert all(sum(c * v for c, v in zip(row, moments)) % P == 0 for row in matrix)
    rank, basis = feas.kernel_basis(matrix)
    assert rank <= 15 and basis
    record["independent_original_event_parameters_F_97"] = sorted(bad)
    record["original_event_supports_checked"] = 2517
    record["independent_actual_minor_recomputation"] = True
    record["affine_recurrence_compatibility_rank"] = rank
    record["bad_parameters_outside_F_97"] = alg.degree(roots) - len(bad)


def main():
    alg.algebra_controls()
    shared_control = shared_coordinate_control()
    stats = Counter()
    stats["weight_four_counts_F_97_20"] = Counter()
    stats["exact_total_counts_F_97_20"] = Counter()
    seen, layouts, best = set(), [], None
    for index, entries in enumerate(LAYOUT_INDICES):
        supports = tuple(tuple(H[i] for i in entry) for entry in entries)
        basis, initial, direction = triple_space(supports)
        layout = {"index": index, "supports": supports,
                  "first_two_union": len(set(supports[0] + supports[1])),
                  "triple_union": len(set(sum(supports, ()))),
                  "triple_rank": 8, "triple_kernel_dimension": 4,
                  "determinant_degrees": Counter(), "zero_determinants": 0,
                  "fourth_supports_tested": 0, "prime_field_determinant_roots": 0,
                  "nonprime_roots_in_target_field_unsearched": 0,
                  "larger_kernel_roots_unsearched": 0, "zero_weight_kernels": 0,
                  "one_dimensional_full_weight_roots": 0, "new_projective_lines": 0}
        for k, fourth in enumerate(SUPPORTS):
            if fourth in supports:
                continue
            layout["fourth_supports_tested"] += 1
            matrix = fourth_matrix(fourth, initial, direction)
            determinant = base.determinant(matrix)
            # Five evaluations check all coefficients of this quartic.
            for t in range(5):
                numerical = [[base.evaluate(f, t) for f in row] for row in matrix]
                assert scalar_determinant(numerical) == base.evaluate(determinant, t)
            if determinant == ZERO:
                layout["zero_determinants"] += 1
                continue
            layout["determinant_degrees"][alg.degree(determinant)] += 1
            prime_roots = [t for t in range(P) if t not in (0, 1, 2)
                           and not base.evaluate(determinant, t)]
            radical = alg.monic(alg.quotient(determinant, alg.gcd(determinant, alg.derivative(determinant))))
            extension = alg.field_root_part(radical, 20)
            rational = alg.field_root_part(radical, 1)
            layout["nonprime_roots_in_target_field_unsearched"] += alg.degree(extension) - alg.degree(rational)
            layout["prime_field_determinant_roots"] += len(prime_roots)
            for t in prime_roots:
                numerical = [[base.evaluate(f, t) for f in row] for row in matrix]
                rank, kernels = feas.kernel_basis(numerical)
                assert kernels and rank < 4
                if len(kernels) != 1:
                    layout["larger_kernel_roots_unsearched"] += 1
                    continue
                weights = tuple(sum(z * b[j] for z, b in zip(kernels[0], basis)) % P
                                for j in range(12))
                if not all(weights):
                    layout["zero_weight_kernels"] += 1
                    continue
                e0 = word_on(supports[0], weights[:4])
                e1 = word_on(supports[1], weights[4:8])
                e2 = word_on(supports[2], weights[8:])
                a, b = e0, tuple((v - u) % P for u, v in zip(e0, e1))
                u, v = base.syndrome(a), base.syndrome(b)
                assert tuple((a + 2 * b) % P for a, b in zip(u, v)) == base.syndrome(e2)
                target = tuple((a + t * b) % P for a, b in zip(u, v))
                fourth_weights = base.solve_square([[pow(x, j, P) for x in fourth]
                                                     for j in range(1, 5)], target[:4])
                assert base.syndrome(word_on(fourth, fourth_weights)) == target
                if not all(fourth_weights):
                    layout["zero_weight_kernels"] += 1
                    continue
                layout["one_dimensional_full_weight_roots"] += 1
                key = line_key(u, v)
                if key in seen:
                    continue
                seen.add(key)
                layout["new_projective_lines"] += 1
                metadata = {"layout": index, "supports": supports + (fourth,),
                            "fourth_parameter": t, "triple_weights": weights,
                            "fourth_weights": fourth_weights}
                record = audit_candidate(a, b, metadata, stats)
                if record is not None and record["all_lower_weight_parameters_excluded"]:
                    if best is None or record["exact_bad_count_F_97_20"] > best["exact_bad_count_F_97_20"]:
                        best = record
            if (k + 1) % 256 == 0:
                print(f"layout {index}: fourth supports {k + 1}/1820; "
                      f"unique lines {len(seen)}; best exact count "
                      f"{None if best is None else best['exact_bad_count_F_97_20']}", flush=True)
        layouts.append(layout)
        report = {"scope": "Six triple layouts, all fourth supports, one-dimensional F_97 kernels only; no extension-input exhaustion.",
                  "coefficient_field": P, "target_extension_degree": 20,
                  "shared_coordinate_zero_syndrome_control": shared_control,
                  "layouts_completed": len(layouts), "layouts": layouts,
                  "unique_projective_lines": len(seen), "actual_pencil_audits": dict(stats),
                  "best_exact_pencil": best}
        (HERE / "three-support-result.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        print(f"completed layout {index}: {json.dumps(layout, sort_keys=True)}", flush=True)
    assert len(layouts) == 6 and sum(l["fourth_supports_tested"] for l in layouts) == 10902
    assert best is not None
    independent_best_audit(best)
    report["best_exact_pencil"] = best
    report["completed"] = True
    (HERE / "three-support-result.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(seen)} distinct projective pencils generated from 10902 fourth-support matrices.")
    print(f"PASS: full power/equality checks and exact F_(97^20) weight-four counts; best exact count {best['exact_bad_count_F_97_20']}.")
    print("PASS: independent actual-minor, affine-recurrence and original-event audit of the best pencil.")
    print("Unsearched branches are recorded; no class exclusion or global count improvement is inferred.")


if __name__ == "__main__":
    main()

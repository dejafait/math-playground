"""Constrained actual pencils and an exact five-set point configuration.

The C++ calculation enumerates projective point pairs, not input weights.
A separate Python implementation checks one full configuration and every
stored maximal line. No global MCA bound follows from these computations.
"""

from collections import Counter
from itertools import combinations
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("feasibility", HERE / "check.py")
feas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(feas)
alg, base = feas.alg, feas.base
PRIME, H = base.P, base.H
INVERSE = {x: pow(x, -1, PRIME) for x in range(1, PRIME)}
ZERO, ONE = alg.ZERO, alg.ONE


def point_configuration(a):
    complement = tuple(x for x in H if x not in a)
    result = []
    for support in combinations(complement, 4):
        polynomial = base.root_polynomial(x for x in complement if x not in support)
        point = tuple(base.evaluate(polynomial, x) for x in a)
        assert all(point)
        result.append((tuple(value * INVERSE[point[0]] % PRIME for value in point), support))
    assert len(result) == 330 and len({p for p, _ in result}) == 330
    return result


def line_key(p, q):
    minors = tuple((p[i] * q[j] - p[j] * q[i]) % PRIME
                   for i, j in combinations(range(5), 2))
    inverse = INVERSE[next(value for value in minors if value)]
    return tuple(value * inverse % PRIME for value in minors)


def on_line(point, first, second):
    pivot = next(i for i in range(1, 5) if first[i] != second[i])
    parameter = (point[pivot] - first[pivot]) * INVERSE[(second[pivot] - first[pivot]) % PRIME] % PRIME
    return all((p - u - parameter * (v - u)) % PRIME == 0
               for p, u, v in zip(point, first, second))


def verify_record(record):
    configuration = point_configuration(record["A"])
    by_support = {tuple(sorted(support)): point for point, support in configuration}
    supports = [tuple(sorted(support)) for support in record["maximum_line_supports"]]
    first, second = (by_support[support] for support in supports[:2])
    assert list(line_key(first, second)) == record["maximum_line_plucker"]
    actual_supports = {tuple(sorted(support)) for point, support in configuration
                       if on_line(point, first, second)}
    assert actual_supports == set(supports)
    assert len(supports) == record["maximum_external_points"]
    histogram = {int(m): count for m, count in record["line_size_histogram"].items()}
    assert sum(histogram.values()) == record["lines"]
    assert sum(m * (m - 1) // 2 * count for m, count in histogram.items()) == 54285
    assert max(histogram) == record["maximum_external_points"]
    return configuration, first, second


def independent_configuration_check(record):
    configuration, _, _ = verify_record(record)
    pair_counts = Counter(line_key(p, q) for (p, _), (q, _) in combinations(configuration, 2))
    inverse_triangular = {m * (m - 1) // 2: m for m in range(2, 331)}
    assert all(pairs in inverse_triangular for pairs in pair_counts.values())
    histogram = Counter(inverse_triangular[pairs] for pairs in pair_counts.values())
    assert dict(histogram) == {int(m): count for m, count in record["line_size_histogram"].items()}
    assert len(pair_counts) == record["lines"]
    return {"mask": record["mask"], "pairs_checked": sum(pair_counts.values()),
            "line_size_histogram": dict(sorted(histogram.items())),
            "independent_maximum": max(histogram)}


def pencil_from_record(record):
    configuration, p, q = verify_record(record)
    all_points = {point for point, _ in configuration}
    for scalar in range(PRIME):
        direction = tuple((v - scalar * u) % PRIME for u, v in zip(p, q))
        if not all(direction):
            continue
        normalized = tuple(value * INVERSE[direction[0]] % PRIME for value in direction)
        if normalized not in all_points:
            break
    else:
        raise AssertionError("No prime-field affine chart avoiding all sparse directions")
    a = tuple(p[record["A"].index(x)] if x in record["A"] else 0 for x in H)
    b = tuple(direction[record["A"].index(x)] if x in record["A"] else 0 for x in H)
    cancellations = sorted({-u * INVERSE[v] % PRIME for u, v in zip(p, direction)})
    return a, b, scalar, cancellations


def exact_weight_four_root_polynomial(d, locators):
    """Union of the regular four-coordinate roots, in the specified field."""
    result = ONE
    for support in combinations(H, 4):
        common = locators[support[0]]
        for x in support[1:]:
            common = alg.gcd(common, locators[x])
        if alg.degree(common) <= 0:
            continue
        common = alg.quotient(common, alg.gcd(common, alg.derivative(common)))
        common = alg.quotient(common, alg.gcd(common, d))
        common = alg.field_root_part(common, 20)
        result = alg.quotient(base.multiply(result, common), alg.gcd(result, common))
    return alg.monic(result)


def actual_pencil_audit(record):
    a, b, scalar, cancellations = pencil_from_record(record)
    d, coefficients, locators = base.locator(a, b)
    assert d != ZERO and all(f != ZERO for f in locators.values())
    r = alg.resultant_product(locators)
    full_equality = alg.equality_check(d, locators, r)
    candidate, recursion = feas.coefficient_power_audit(r)
    root_polynomial = exact_weight_four_root_polynomial(d, locators)
    # All five internal weights are nonzero polynomials. For this selected
    # chart the cancellations must be distinct, excluding lower-weight roots.
    assert len(cancellations) == 5
    assert alg.field_root_part(root_polynomial, 1) == root_polynomial
    constraints = base.interpolation_constraints()
    bad, weights = base.original_event(a, b, constraints)
    exact_bad = {t for t in range(PRIME) if base.evaluate(root_polynomial, t) == 0}
    assert bad == exact_bad and all(weights[t] == 4 for t in bad)
    assert len(bad) == record["maximum_external_points"] + 5
    inverse_audit = feas.audit_actual("selected_five_coordinate_line", a, b)
    # Short polynomial identity for the informal proof of this one pencil.
    # All eleven known roots have exactly four product incidences. A
    # coprime residual with multiplicities below four rules out any other
    # four-error root and every lower-weight root, in every extension field.
    residual = alg.quotient(alg.monic(r), alg.power(root_polynomial, 4))
    assert alg.degree(residual) == 20
    residual_factors = alg.squarefree_factors(residual)
    assert set(residual_factors) == {1, 3}
    assert all(alg.gcd(f, alg.derivative(f)) == ONE for f in residual_factors.values())
    assert alg.gcd(residual_factors[1], residual_factors[3]) == ONE
    assert alg.gcd(residual, root_polynomial) == ONE
    assert alg.gcd(root_polynomial, d) == ONE
    assert alg.monic(r) == base.multiply(alg.power(root_polynomial, 4), residual)
    external_witnesses = []
    for parameter in sorted(bad - set(cancellations)):
        support = tuple(x for x in H if base.evaluate(locators[x], parameter) == 0)
        assert len(support) == 4 and not (set(support) & set(record["A"]))
        polynomial = base.root_polynomial(x for x in H if x not in record["A"] and x not in support)
        anchor = record["A"][0]
        anchor_index = H.index(anchor)
        scalar = (a[anchor_index] + parameter * b[anchor_index]) * INVERSE[base.evaluate(polynomial, anchor)] % PRIME
        codeword = base.scale(polynomial, scalar)
        assert scalar and alg.degree(codeword) == 7
        assert all((u + parameter * v - base.evaluate(codeword, x)) % PRIME == 0
                   for x, u, v in zip(H, a, b) if x not in support)
        assert all(base.evaluate(codeword, x) for x in support)
        external_witnesses.append({"parameter": parameter, "support": support,
                                   "codeword_scalar": scalar,
                                   "monic_codeword_zero_set": tuple(x for x in H
                                        if x not in record["A"] and x not in support)})
    return {"orbit_mask": record["mask"], "A": record["A"], "a": a, "b": b,
            "chart_scalar": scalar, "cancellation_parameters": cancellations,
            "D": d, "locator_coefficients": coefficients, "R": r,
            "coefficient_power_audit": recursion, "full_L010_equality": full_equality,
            "monic_bad_parameter_polynomial": root_polynomial,
            "monic_resultant_residual": residual,
            "residual_squarefree_factors_by_multiplicity": residual_factors,
            "resultant_factorization_scalar": r[-1],
            "factorization_and_squarefree_gcds_checked": True,
            "external_codeword_witnesses": external_witnesses,
            "exact_bad_count_F_97_20": alg.degree(root_polynomial),
            "all_bad_parameters_already_in_F_97": True,
            "independent_original_event_bad_parameters_F_97": sorted(bad),
            "admissible_supports_checked": len(constraints), "inverse_compatibility": inverse_audit}


def two_block_specialization():
    """Applicability and independent checks for the C013a partition."""
    first = (1, 8, 22, 27, 89)
    second = (18, 33, 50, 85, 96)
    complement = tuple(x for x in H if x not in first + second)
    u, v = base.root_polynomial(first), base.root_polynomial(second)
    ratios = {x: base.evaluate(u, x) * INVERSE[base.evaluate(v, x)] % PRIME
              for x in complement}
    assert ratios == {12: 54, 47: 55, 64: 55, 70: 55, 75: 55, 79: 11}
    fiber = (47, 64, 70, 75)
    normalized = alg.monic(base.add(u, base.scale(v, -55)))
    quotient = alg.quotient(normalized, base.root_polynomial(fiber))
    assert quotient == (20, 1)
    expected = set(first + second + (77,))
    a, b = alg.two_block(first, second)
    d, coefficients, locators = base.locator(a, b)
    assert alg.audit_two_block(a, b, first + second, d, coefficients, locators) == (11, 4)
    bad_polynomial = exact_weight_four_root_polynomial(d, locators)
    assert bad_polynomial == base.root_polynomial(sorted(expected))
    assert alg.field_root_part(bad_polynomial, 1) == bad_polynomial
    bad, weights = base.original_event(a, b, base.interpolation_constraints())
    assert bad == expected and all(weights[t] == 4 for t in bad)
    r = alg.resultant_product(locators)
    _, recursion = feas.coefficient_power_audit(r)
    assert not alg.equality_check(d, locators, r)
    return {"A": first, "B": second, "J": complement,
            "U": u, "V": v, "ratios": ratios, "large_fiber": fiber,
            "large_fiber_ratio": 55, "normalized_fiber_polynomial": normalized,
            "residual_linear_factor": quotient, "extra_parameter": 77,
            "a": a, "b": b, "D": d, "locator_coefficients": coefficients,
            "exact_bad_parameters": sorted(expected), "exact_bad_count_F_97_20": 11,
            "exact_field_bad_root_polynomial": bad_polynomial,
            "coefficient_power_audit": recursion, "full_L010_equality": False,
            "independent_original_event_supports_checked": 2517}


def main():
    source = HERE / "five_coordinate_lines.cpp"
    with tempfile.TemporaryDirectory(prefix="five-coordinate-build-", dir=HERE) as build:
        executable = Path(build) / "enumerate"
        subprocess.run(["c++", "-O3", "-std=c++17", str(source), "-o", str(executable)], check=True)
        result = subprocess.run([str(executable)], check=True, text=True, capture_output=True)
    records = [json.loads(line) for line in result.stdout.splitlines()]
    assert len(records) == 273
    cyclic = tuple(pow(8, i, PRIME) for i in range(16))
    masks = {record["mask"] for record in records}
    all_five_sets = set()
    for record in records:
        mask = record["mask"]
        assert tuple(record["A"]) == tuple(cyclic[i] for i in range(16) if mask & (1 << i))
        orbit = {((mask << shift) | (mask >> (16 - shift))) & 65535 for shift in range(16)}
        assert len(orbit) == 16 and min(orbit) == mask
        assert not (all_five_sets & orbit)
        all_five_sets.update(orbit)
        verify_record(record)
    expected_masks = {sum(1 << i for i in support) for support in combinations(range(16), 5)}
    assert all_five_sets == expected_masks and len(expected_masks) == 4368
    assert len(masks) == 273
    (HERE / "five-coordinate-orbits.jsonl").write_text(result.stdout)
    maximum = max(record["maximum_external_points"] for record in records)
    # Prefer a maximal line with five distinct coordinate cancellations.
    eligible = []
    for record in records:
        if record["maximum_external_points"] != maximum:
            continue
        _, p, q = verify_record(record)
        ratios = {v * INVERSE[u] % PRIME for u, v in zip(p, q)}
        if len(ratios) == 5:
            eligible.append(record)
    assert eligible
    selected = min(eligible, key=lambda record: record["mask"])
    independent = independent_configuration_check(selected)
    print(f"PASS: 273 free orbits cover all 4368 five-sets; {273 * 54285} point pairs enumerated.", flush=True)
    print(f"Maximum external points on a projective line: {maximum}.", flush=True)
    actual = actual_pencil_audit(selected)
    specialization = two_block_specialization()
    assert actual["a"] == tuple((85 * u + 46 * v) % PRIME
                                 for u, v in zip(specialization["a"], specialization["b"]))
    assert actual["b"] == tuple((27 * u + 66 * v) % PRIME
                                 for u, v in zip(specialization["a"], specialization["b"]))
    assert (85 * 66 - 46 * 27) % PRIME == 3
    report = {"scope": "Exact point configurations for all five-coordinate error spaces; general pencils remain open.",
              "coefficient_field": PRIME, "target_extension_degree": 20,
              "five_sets": 4368, "five_set_orbits": 273, "points_per_configuration": 330,
              "point_pairs_enumerated": 273 * 54285,
              "maximum_external_points": maximum,
              "orbit_maximum_histogram": dict(sorted(Counter(record["maximum_external_points"] for record in records).items())),
              "stored_maximal_lines_independently_checked": 273,
              "independent_complete_configuration_check": independent,
              "selected_actual_pencil": actual,
              "L013_partition_specialization": specialization,
              "selected_chart_as_L013_input_matrix": [[85, 46], [27, 66]],
              "input_change_determinant": 3,
              "interpretation": "Finite configuration evidence plus actual-pencil audit; not a global fifteen bound."}
    (HERE / "five-coordinate-result.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: selected actual pencil has {actual['exact_bad_count_F_97_20']} bad parameters in F_(97^20).", flush=True)
    print("PASS: actual minors, coefficient residuals, inverse compatibility, exact splitting and original-event support audit.", flush=True)
    print("General extension-field moment pencils and the grand challenge remain unresolved.", flush=True)


if __name__ == "__main__":
    main()

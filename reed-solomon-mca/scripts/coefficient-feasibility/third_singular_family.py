"""Exact third singular fourth-support family; arbitrary extension weights.

Only K={8,47,64,75} for the saved disjoint triple is tested. Polynomial
tuples are in increasing degree, over F_97. S is the fourth parameter;
T is the original affine pencil parameter.
"""

from itertools import combinations
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("second_family_tools", HERE / "second_singular_family.py")
tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)
three, base, alg, ext = tools.three, tools.base, tools.alg, tools.ext
P, H, A = tools.P, tools.H, tools.A
K = (8, 47, 64, 75)


def family():
    basis, initial, direction = three.triple_space(A)
    matrix = three.fourth_matrix(K, initial, direction)
    assert base.determinant(matrix) == alg.ZERO
    minor_gcd, chosen = alg.ZERO, None
    for rows in combinations(range(4), 3):
        vector = tuple(base.scale(base.determinant(
            [[matrix[i][j] for j in range(4) if j != k] for i in rows]), (-1) ** k)
            for k in range(4))
        for f in vector:
            minor_gcd = alg.gcd(minor_gcd, f)
        if chosen is None and any(f != alg.ZERO for f in vector):
            chosen = (rows, vector)
    assert minor_gcd == (95, 1)
    rows, vector = chosen
    common = alg.ZERO
    for f in vector:
        common = alg.gcd(common, f)
    vector = tuple(alg.quotient(f, common) for f in vector)
    assert vector == ((18, 88), (40, 56), (94, 50), (43, 11))
    for row in matrix:
        residual = alg.ZERO
        for f, g in zip(row, vector):
            residual = base.add(residual, base.multiply(f, g))
        assert residual == alg.ZERO
    assert alg.gcd(vector[0], vector[1]) == alg.ONE
    weights = tuple(tools.dot_polynomial([b[j] for b in basis], vector) for j in range(12))
    u = tuple(tools.dot_polynomial([r[j] for r in initial], vector) for j in range(8))
    v = tuple(tools.dot_polynomial([r[j] for r in direction], vector) for j in range(8))
    assert all(f != alg.ZERO for f in weights)
    assert weights == ((0, 85), (27, 8), (0, 44), (0, 93),
                       (53, 44), (10, 87), (91, 6), (50, 11),
                       (18, 88), (40, 56), (94, 50), (43, 11))
    for t, support, offset in zip((0, 1, 2), A, (0, 4, 8)):
        moment = tuple(base.add(a, base.scale(b, t)) for a, b in zip(u, v))
        for j in range(8):
            assert moment[j] == tools.dot_polynomial(
                [pow(x, j + 1, P) for x in support], weights[offset:offset + 4])
    target = tuple(base.add(a, base.multiply(alg.T, b)) for a, b in zip(u, v))
    vandermonde = [[pow(x, j, P) for x in K] for j in range(1, 5)]
    by_degree = [base.solve_square(vandermonde,
                                  [f[k] if k < len(f) else 0 for f in target[:4]])
                 for k in range(3)]
    fourth_weights = tuple(base.trim([f[j] for f in by_degree]) for j in range(4))
    for j in range(8):
        assert tools.dot_polynomial([pow(x, j + 1, P) for x in K], fourth_weights) == target[j]
    assert all(f != alg.ZERO for f in fourth_weights)
    assert fourth_weights == ((27, 8, 62), (0, 25, 36), (0, 21, 76), (0, 16, 81))
    product = alg.ONE
    for f in weights + fourth_weights:
        product = base.multiply(product, f)
    forbidden = alg.monic(alg.quotient(product, alg.gcd(product, alg.derivative(product))))
    assert forbidden == base.root_polynomial((0, 1, 2, 27, 33, 49, 66))
    rank_at_two, _ = three.feas.kernel_basis([[base.evaluate(f, 2) for f in row] for row in matrix])
    assert rank_at_two == 2
    ring = ext.Polynomials(tools.ParameterRing())
    d, coefficients, locators = ext.actual_locator(ring, u, v)
    assert d != ring.zero and all(f != ring.zero for f in locators.values())
    return {"fourth_support": K, "triple_kernel_basis": basis, "fourth_matrix": matrix,
            "three_by_three_minor_gcd": minor_gcd, "kernel_rows": rows,
            "primitive_kernel": vector, "weights": weights, "fourth_weights": fourth_weights,
            "full_weight_forbidden_polynomial": forbidden, "rank_at_two": rank_at_two,
            "u": u, "v": v, "D": d, "coefficients": coefficients, "locators": locators}


def equality_elimination(data):
    forbidden = data["full_weight_forbidden_polynomial"]
    resultants = {}
    for y in H:
        if y == 79:
            continue
        res = tools.resultant(data["locators"][79], data["locators"][y])
        assert res != alg.ZERO and alg.degree(res) <= 32
        matrix = tools.sylvester(data["locators"][79], data["locators"][y])
        for s in range(33):
            expected = three.scalar_determinant([[base.evaluate(f, s) for f in row] for row in matrix])
            assert base.evaluate(res, s) == expected
        radical = alg.monic(alg.quotient(res, alg.gcd(res, alg.derivative(res))))
        saturated = alg.quotient(radical, alg.gcd(radical, forbidden))
        resultants[y] = {"resultant": res, "radical": radical, "saturated_radical": saturated}
    pairs, triples = [], []
    for x, y in combinations(resultants, 2):
        gcd = alg.gcd(resultants[x]["saturated_radical"], resultants[y]["saturated_radical"])
        assert gcd == ((54, 66, 1) if (x, y) == (22, 47) else (4, 1))
        pairs.append({"coordinates": (x, y), "gcd": gcd})
    for xs in combinations(resultants, 3):
        gcd = alg.gcd(alg.gcd(resultants[xs[0]]["saturated_radical"],
                             resultants[xs[1]]["saturated_radical"]),
                      resultants[xs[2]]["saturated_radical"])
        assert gcd == (4, 1)
        triples.append({"coordinates": xs, "gcd": gcd})
    assert len(resultants) == 15 and len(pairs) == 105 and len(triples) == 455
    union = alg.ONE
    for entry in triples:
        union = alg.quotient(base.multiply(union, entry["gcd"]), alg.gcd(union, entry["gcd"]))
    assert alg.monic(union) == (4, 1)
    data.update({"coordinate_79_resultants": resultants, "pairwise_gcd_certificate": pairs,
                 "triple_gcd_certificate": triples, "scalar_resultant_evaluation_checks": 495,
                 "necessary_equality_parameter_polynomial": alg.monic(union)})


def exceptional_pencil(data):
    s = 93
    weights = tuple(base.evaluate(f, s) for f in data["weights"])
    fourth_weights = tuple(base.evaluate(f, s) for f in data["fourth_weights"])
    assert all(weights) and all(fourth_weights)
    a = three.word_on(A[0], weights[:4])
    endpoint = three.word_on(A[1], weights[4:8])
    b = tuple((y - x) % P for x, y in zip(a, endpoint))
    u, v = base.syndrome(a), base.syndrome(b)
    assert u == tuple(base.evaluate(f, s) for f in data["u"])
    assert v == tuple(base.evaluate(f, s) for f in data["v"])
    d, coefficients, locators = base.locator(a, b)
    assert d == tools.evaluate_S(data["D"], s)
    assert coefficients == tuple(tools.evaluate_S(f, s) for f in data["coefficients"])
    assert locators == {x: tools.evaluate_S(f, s) for x, f in data["locators"].items()}
    assert u == (27, 35, 72, 88, 73, 77, 88, 19)
    assert v == (43, 50, 52, 71, 45, 61, 20, 75)
    assert d == (23, 38, 28, 50, 39)
    common = alg.ZERO
    for f in locators.values():
        common = alg.gcd(common, f)
    assert common == (15, 1) and base.evaluate(d, 82) == 0
    degrees = {x: alg.degree(f) for x, f in locators.items()}
    assert degrees[50] == 3 and all(n == 4 for x, n in degrees.items() if x != 50)
    product = alg.resultant_product(locators)
    candidate, power_audit = three.feas.coefficient_power_audit(product)
    decomposition = alg.squarefree_factors(product)
    fourth_power = set(decomposition) == {4} and alg.degree(decomposition[4]) == 16
    assert alg.degree(product) == 63 and candidate is None
    assert power_audit == {"degree": 63, "degree_gate": False} and not fourth_power
    equality = alg.equality_check(d, locators, product)
    assert not equality
    radicals = {x: alg.monic(alg.quotient(f, alg.gcd(f, alg.derivative(f))))
                for x, f in locators.items()}
    root_parts = {x: alg.field_root_part(f, 20) for x, f in radicals.items()}
    gates = {"all_coordinate_degrees_four": all(n == 4 for n in degrees.values()),
             "all_coordinates_squarefree": all(alg.gcd(f, alg.derivative(f)) == alg.ONE
                                                for f in locators.values()),
             "all_coordinates_split_in_F_97_20": all(root_parts[x] == f for x, f in radicals.items()),
             "resultant_c_times_degree_16_fourth_power": fourth_power,
             "all_coordinate_roots_regular": alg.gcd(product, d) == alg.ONE,
             "full_L010_equality": equality}
    assert gates == {"all_coordinate_degrees_four": False,
                     "all_coordinates_squarefree": True,
                     "all_coordinates_split_in_F_97_20": False,
                     "resultant_c_times_degree_16_fourth_power": False,
                     "all_coordinate_roots_regular": False,
                     "full_L010_equality": False}
    radical_product = alg.ONE
    for f in radicals.values():
        radical_product = base.multiply(radical_product, f)
    regular_four = alg.squarefree_factors(radical_product).get(4, alg.ONE)
    regular_four = alg.quotient(regular_four, alg.gcd(regular_four, d))
    expected = base.root_polynomial((0, 1, 2, 93))
    assert regular_four == expected and alg.field_root_part(regular_four, 20) == expected
    singular_moments = tuple((x + 82 * y) % P for x, y in zip(u, v))
    assert singular_moments == (61, 61, 68, 90, 77, 35, 79, 58)
    lower_weight_supports_checked = 0
    for support in combinations(H, 3):
        matrix = [[pow(x, j, P) for x in support] for j in range(1, 4)]
        proposed = base.solve_square(matrix, singular_moments[:3])
        matches = all(sum(w * pow(x, j, P) for x, w in zip(support, proposed)) % P
                      == singular_moments[j - 1] for j in range(1, 9))
        assert not matches
        lower_weight_supports_checked += 1
    assert lower_weight_supports_checked == 560
    bad, event_weights = base.original_event(a, b, base.interpolation_constraints())
    assert bad == {0, 1, 2, 93} and all(w == 4 for w in event_weights.values())
    infinity_roots = tuple(x for x, f in locators.items() if alg.degree(f) < 4)
    assert d[-1] and infinity_roots == (50,)
    # Full weight four at infinity would require four locator zeros,
    # and lower weight would force the leading Hankel determinant to vanish.
    data["exceptional_pencil_S_93"] = {
        "weights": weights, "fourth_weights": fourth_weights, "a": a, "b": b,
        "u": u, "v": v, "D": d, "locator_coefficients": coefficients,
        "locators": locators, "coordinate_degrees": degrees,
        "common_locator_gcd": common, "resultant": product,
        "resultant_squarefree_decomposition": decomposition,
        "coefficient_power_audit": power_audit,
        "degree_16_power_candidate": None,
        "power_candidate_gate_note": "Degree 63 rejects a degree-sixteen fourth root before coefficient recursion; no candidate splitting or D-coprimality is claimed.",
        "separate_equality_gates": gates,
        "coordinate_target_field_root_parts": root_parts,
        "target_field_weight_four_polynomial": regular_four,
        "exact_bad_parameters_algebraic_closure": (0, 1, 2, 93),
        "singular_moments_at_T_82": singular_moments,
        "lower_weight_supports_checked": lower_weight_supports_checked,
        "lower_weight_parameters_excluded": True,
        "independent_original_event_supports_checked": 2517,
        "independent_original_event_parameters": sorted(bad),
        "infinity_locator_roots": infinity_roots, "original_infinity_is_sparse": False}


def redundancy_check(data):
    # Bounded check only; not a full code-automorphism classification.
    triple_sets = {frozenset(a) for a in A}
    matches = []
    for previous in ((1, 12, 22, 64), (8, 27, 50, 75)):
        for c in H:
            for inverse in (False, True):
                def phi(x):
                    return c * (pow(x, -1, P) if inverse else x) % P
                if ({frozenset(phi(x) for x in a) for a in A} == triple_sets
                        and frozenset(phi(x) for x in previous) == frozenset(K)):
                    matches.append((previous, c, inverse))
    assert not matches
    data["bounded_scaling_inversion_redundancy_matches"] = matches


def main():
    data = family()
    output = HERE / "third-singular-family-result.json"
    output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: data[key] for key in ("primitive_kernel", "weights", "fourth_weights",
                                                "full_weight_forbidden_polynomial")}), flush=True)
    tools.independent_minors(data)
    equality_elimination(data)
    exceptional_pencil(data)
    redundancy_check(data)
    data["conclusion"] = "No sixteen-count pencil in this full-weight third singular fourth-support family."
    output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"necessary_equality_parameter_polynomial": data["necessary_equality_parameter_polynomial"],
                      "pair_gcds": sorted(set(tuple(r["gcd"]) for r in data["pairwise_gcd_certificate"])),
                      "triple_gcds": sorted(set(tuple(r["gcd"]) for r in data["triple_gcd_certificate"])),
                      "output": str(output.relative_to(HERE.parent.parent))}), flush=True)


if __name__ == "__main__":
    main()

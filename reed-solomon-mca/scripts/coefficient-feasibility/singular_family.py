"""Exact first zero-determinant family for the saved disjoint triple.

S is the fourth support's parameter; T is the actual affine pencil parameter.
Every polynomial uses exact F_97 arithmetic. Other singular families are
outside this calculation.
"""

from itertools import combinations
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("extension_roots", HERE / "extension_roots.py")
ext = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ext)
three, base, alg = ext.three, ext.base, ext.alg
P, H = base.P, base.H
A = ext.SUPPORTS
K = (1, 12, 22, 64)


class ParameterRing:
    """F_97[S], used as the coefficient ring for T-polynomials."""

    zero, one = alg.ZERO, alg.ONE

    @staticmethod
    def c(n):
        return (n % P,)

    add = staticmethod(base.add)
    mul = staticmethod(base.multiply)
    scale = staticmethod(base.scale)

    @staticmethod
    def neg(f):
        return base.scale(f, -1)

    @staticmethod
    def sub(f, g):
        return base.add(f, base.scale(g, -1))


def dot_polynomial(scalars, polys):
    answer = alg.ZERO
    for c, f in zip(scalars, polys):
        answer = base.add(answer, base.scale(f, c))
    return answer


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
    assert minor_gcd == alg.T
    rows, vector = chosen
    common = alg.ZERO
    for f in vector:
        common = alg.gcd(common, f)
    vector = tuple(alg.quotient(f, common) for f in vector)
    assert vector == ((83, 7), (33, 37), (76, 59), (58, 68))
    for row in matrix:
        residual = alg.ZERO
        for f, g in zip(row, vector):
            residual = base.add(residual, base.multiply(f, g))
        assert residual == alg.ZERO
    # Primitive coordinates do not all vanish at any specialization.
    assert alg.gcd(vector[0], vector[1]) == alg.ONE
    weights = tuple(dot_polynomial([b[j] for b in basis], vector) for j in range(12))
    u = tuple(dot_polynomial([r[j] for r in initial], vector) for j in range(8))
    v = tuple(dot_polynomial([r[j] for r in direction], vector) for j in range(8))
    assert all(f != alg.ZERO for f in weights)
    for t, support, offset in zip((0, 1, 2), A, (0, 4, 8)):
        moment = tuple(base.add(a, base.scale(b, t)) for a, b in zip(u, v))
        for j in range(8):
            expected = dot_polynomial([pow(x, j + 1, P) for x in support],
                                      weights[offset:offset + 4])
            assert moment[j] == expected
    target = tuple(base.add(a, base.multiply(alg.T, b)) for a, b in zip(u, v))
    vandermonde = [[pow(x, j, P) for x in K] for j in range(1, 5)]
    by_degree = [base.solve_square(vandermonde,
                                  [f[k] if k < len(f) else 0 for f in target[:4]])
                 for k in range(3)]
    fourth_weights = tuple(base.trim([f[j] for f in by_degree]) for j in range(4))
    for j in range(8):
        assert dot_polynomial([pow(x, j + 1, P) for x in K], fourth_weights) == target[j]
    assert fourth_weights == ((80, 74, 40), (76, 80, 38), (0, 17, 40), (0, 92, 5))
    forbidden_product = alg.ONE
    for f in weights + fourth_weights:
        forbidden_product = base.multiply(forbidden_product, f)
    forbidden = alg.monic(alg.quotient(forbidden_product,
                                     alg.gcd(forbidden_product, alg.derivative(forbidden_product))))
    assert forbidden == base.root_polynomial((0, 1, 2, 47, 49, 52, 83))
    rank_at_zero, _ = three.feas.kernel_basis([[f[0] for f in row] for row in matrix])
    assert rank_at_zero == 2
    ring = ext.Polynomials(ParameterRing())
    d, coefficients, locators = ext.actual_locator(ring, u, v)
    assert d != ring.zero and all(f != ring.zero for f in locators.values())
    return {"triple_kernel_basis": basis, "fourth_matrix": matrix,
            "three_by_three_minor_gcd": minor_gcd,
            "kernel_rows": rows, "primitive_kernel": vector,
            "weights": weights, "fourth_weights": fourth_weights,
            "full_weight_forbidden_polynomial": forbidden,
            "rank_at_zero": rank_at_zero, "u": u, "v": v,
            "D": d, "coefficients": coefficients, "locators": locators}, ring


def bareiss(matrix):
    """Polynomial determinant by fraction-free elimination over F_97[S]."""
    rows = [list(row) for row in matrix]
    n, previous, sign = len(rows), alg.ONE, 1
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if rows[i][k] != alg.ZERO), None)
        if pivot is None:
            return alg.ZERO
        if pivot != k:
            rows[k], rows[pivot] = rows[pivot], rows[k]
            sign = -sign
        value = rows[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = base.add(base.multiply(value, rows[i][j]),
                                     base.scale(base.multiply(rows[i][k], rows[k][j]), -1))
                rows[i][j] = alg.quotient(numerator, previous)
            rows[i][k] = alg.ZERO
        previous = value
    return base.scale(rows[-1][-1], sign)


def sylvester(f, g):
    n, m = len(f) - 1, len(g) - 1
    size = n + m
    rows = []
    for poly, count in ((f, m), (g, n)):
        for shift in range(count):
            row = [alg.ZERO] * size
            row[shift:shift + len(poly)] = reversed(poly)
            rows.append(row)
    return rows


def resultant(f, g):
    return bareiss(sylvester(f, g))


def evaluate_S(f, s):
    return base.trim([base.evaluate(c, s) for c in f])


def independent_minors(data):
    # Bidegrees at most (4,4): a five-by-five evaluation grid checks
    # every coefficient against independent scalar determinants.
    assert all(alg.degree(f) <= 4 for coefficient in data["coefficients"] for f in coefficient)
    for s in range(5):
        u = [base.evaluate(f, s) for f in data["u"]]
        v = [base.evaluate(f, s) for f in data["v"]]
        for t in range(5):
            moments = [(x + t * y) % P for x, y in zip(u, v)]
            rows = [[moments[i + j] for j in range(5)] for i in range(4)]
            for k, f in enumerate(data["coefficients"]):
                expected = (-1) ** k * three.scalar_determinant(
                    [[row[j] for j in range(5) if j != k] for row in rows]) % P
                assert base.evaluate(evaluate_S(f, s), t) == expected
    data["actual_minor_evaluation_grid_checks"] = 125


def equality_elimination(data):
    """Every equality root at coordinate 79 needs three other coordinates."""
    forbidden = data["full_weight_forbidden_polynomial"]
    resultants = {}
    for y in H:
        if y == 79:
            continue
        res = resultant(data["locators"][79], data["locators"][y])
        assert res != alg.ZERO and alg.degree(res) <= 32
        matrix = sylvester(data["locators"][79], data["locators"][y])
        # Degrees in S are at most 32. Thirty-three scalar determinant
        # comparisons certify the entire symbolic resultant.
        for s in range(33):
            expected = three.scalar_determinant([[base.evaluate(f, s) for f in row]
                                                  for row in matrix])
            assert base.evaluate(res, s) == expected
        radical = alg.monic(alg.quotient(res, alg.gcd(res, alg.derivative(res))))
        saturated = alg.quotient(radical, alg.gcd(radical, forbidden))
        assert base.evaluate(saturated, 16) == 0
        resultants[y] = {"resultant": res, "radical": radical,
                         "saturated_radical": saturated}
    pairs, triples = [], []
    for x, y in combinations(resultants, 2):
        gcd = alg.gcd(resultants[x]["saturated_radical"], resultants[y]["saturated_radical"])
        expected = (84, 3, 1) if (x, y) == (22, 89) else (81, 1)
        assert gcd == expected
        pairs.append({"coordinates": (x, y), "gcd": gcd})
    for xs in combinations(resultants, 3):
        gcd = alg.gcd(alg.gcd(resultants[xs[0]]["saturated_radical"],
                             resultants[xs[1]]["saturated_radical"]),
                      resultants[xs[2]]["saturated_radical"])
        assert gcd == (81, 1)
        triples.append({"coordinates": xs, "gcd": gcd})
    assert len(resultants) == 15 and len(pairs) == 105 and len(triples) == 455
    data["coordinate_79_resultants"] = resultants
    data["pairwise_gcd_certificate"] = pairs
    data["triple_gcd_certificate"] = triples
    data["scalar_resultant_evaluation_checks"] = 495
    data["necessary_equality_parameter_polynomial"] = (81, 1)


def exceptional_pencil(data):
    s = 16
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
    assert d == evaluate_S(data["D"], s)
    assert coefficients == tuple(evaluate_S(f, s) for f in data["coefficients"])
    assert locators == {x: evaluate_S(f, s) for x, f in data["locators"].items()}
    assert d == (48, 43, 42, 25, 13)
    common = alg.ZERO
    for f in locators.values():
        common = alg.gcd(common, f)
    assert common == (90, 1) and base.evaluate(d, 7) == 0
    assert all(alg.degree(f) == 4 for f in locators.values())
    product = alg.resultant_product(locators)
    candidate, power_audit = three.feas.coefficient_power_audit(product)
    decomposition = alg.squarefree_factors(product)
    fourth_power = set(decomposition) == {4} and alg.degree(decomposition[4]) == 16
    assert power_audit["power_identity"] == fourth_power
    assert not fourth_power and power_audit["failed_residuals"] == list(range(17, 65))
    equality = alg.equality_check(d, locators, product)
    assert not equality
    candidate_radical = alg.quotient(candidate, alg.gcd(candidate, alg.derivative(candidate)))
    # All gates are recorded separately, including exact target-field splitting.
    gates = {"all_coordinate_degrees_four": True,
             "all_coordinates_squarefree": all(alg.gcd(f, alg.derivative(f)) == alg.ONE
                                                for f in locators.values()),
             "all_coordinates_split_in_F_97_20": all(
                 alg.field_root_part(alg.quotient(f, alg.gcd(f, alg.derivative(f))), 20)
                 == alg.monic(alg.quotient(f, alg.gcd(f, alg.derivative(f))))
                 for f in locators.values()),
             "candidate_squarefree": alg.gcd(candidate, alg.derivative(candidate)) == alg.ONE,
             "candidate_D_coprime": alg.gcd(candidate, d) == alg.ONE,
             "candidate_split_in_F_97_20": alg.field_root_part(candidate_radical, 20)
                                           == alg.monic(candidate_radical),
             "all_coordinate_roots_regular": alg.gcd(product, d) == alg.ONE,
             "full_L010_equality": equality}
    radical_product = alg.ONE
    for f in locators.values():
        radical_product = base.multiply(radical_product,
                                       alg.monic(alg.quotient(f, alg.gcd(f, alg.derivative(f)))))
    regular_four = alg.squarefree_factors(radical_product).get(4, alg.ONE)
    regular_four = alg.quotient(regular_four, alg.gcd(regular_four, d))
    expected = base.root_polynomial((0, 1, 2, 16))
    assert regular_four == expected and alg.field_root_part(regular_four, 20) == expected
    # Any lower-weight parameter must be a root of the common locator gcd.
    # Its only root is 7; test all three-sets, using prime-field inversion.
    singular_moments = tuple((x + 7 * y) % P for x, y in zip(u, v))
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
    assert bad == {0, 1, 2, 16} and all(w == 4 for w in event_weights.values())
    infinity_roots = tuple(x for x, f in locators.items() if alg.degree(f) < 4)
    assert d[-1] and not infinity_roots
    data["exceptional_pencil_S_16"] = {
        "weights": weights, "fourth_weights": fourth_weights,
        "a": a, "b": b, "u": u, "v": v, "D": d,
        "locator_coefficients": coefficients, "locators": locators,
        "common_locator_gcd": common, "resultant": product,
        "coefficient_power_audit": power_audit, "separate_equality_gates": gates,
        "target_field_weight_four_polynomial": regular_four,
        "exact_bad_parameters_algebraic_closure": (0, 1, 2, 16),
        "singular_moments_at_T_7": singular_moments,
        "lower_weight_supports_checked": lower_weight_supports_checked,
        "lower_weight_parameters_excluded": True,
        "independent_original_event_supports_checked": 2517,
        "independent_original_event_parameters": sorted(bad),
        "original_infinity_is_sparse": False}


def main():
    data, _ = family()
    independent_minors(data)
    equality_elimination(data)
    exceptional_pencil(data)
    data["conclusion"] = "No sixteen-count pencil in this full-weight singular fourth-support family."
    output = HERE / "singular-family-result.json"
    output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"fourth_support": K,
                      "full_weight_forbidden_parameters": (0, 1, 2, 47, 49, 52, 83),
                      "necessary_equality_parameter": 16,
                      "exceptional_pencil_bad_count": 4,
                      "pair_gcd_checks": len(data["pairwise_gcd_certificate"]),
                      "triple_gcd_checks": len(data["triple_gcd_certificate"]),
                      "symbolic_resultants_independently_checked": 15,
                      "full_family_sixteen_count_excluded": True,
                      "output": str(output.relative_to(HERE.parent.parent))}), flush=True)


if __name__ == "__main__":
    main()

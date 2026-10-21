"""Last singular fourth-support family for the saved disjoint triple.

Exact F_97[S,T] identities; S is the fourth parameter, T the pencil
parameter. No prime-field restriction on specialized S or weights.
"""
from itertools import combinations
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('family_tools', HERE / 'second_singular_family.py')
tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)
three, base, alg, ext = tools.three, tools.base, tools.alg, tools.ext
P, H, A = tools.P, tools.H, tools.A
K = (12, 33, 47, 50)
OUTPUT = HERE / 'fourth-singular-family-result.json'


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
            chosen = rows, vector
    assert minor_gcd == (96, 1)
    rows, vector = chosen
    common = alg.ZERO
    for f in vector:
        common = alg.gcd(common, f)
    vector = tuple(alg.quotient(f, common) for f in vector)
    for row in matrix:
        assert tools.dot_polynomial((1, 1, 1, 1),
            [base.multiply(f, g) for f, g in zip(row, vector)]) == alg.ZERO
    assert vector == ((33, 80), (30, 82), (83, 7), (9, 44))
    vector_gcd = alg.ZERO
    for f in vector:
        vector_gcd = alg.gcd(vector_gcd, f)
    assert vector_gcd == alg.ONE
    weights = tuple(tools.dot_polynomial([b[j] for b in basis], vector) for j in range(12))
    u = tuple(tools.dot_polynomial([r[j] for r in initial], vector) for j in range(8))
    v = tuple(tools.dot_polynomial([r[j] for r in direction], vector) for j in range(8))
    assert all(f != alg.ZERO for f in weights)
    for t, support, offset in zip((0, 1, 2), A, (0, 4, 8)):
        moment = tuple(base.add(a, base.scale(b, t)) for a, b in zip(u, v))
        for j in range(8):
            assert moment[j] == tools.dot_polynomial(
                [pow(x, j + 1, P) for x in support], weights[offset:offset + 4])
    target = tuple(base.add(a, base.multiply(alg.T, b)) for a, b in zip(u, v))
    degree = max(alg.degree(f) for f in target)
    vandermonde = [[pow(x, j, P) for x in K] for j in range(1, 5)]
    by_degree = [base.solve_square(vandermonde,
        [f[k] if k < len(f) else 0 for f in target[:4]]) for k in range(degree + 1)]
    fourth_weights = tuple(base.trim([f[j] for f in by_degree]) for j in range(4))
    assert all(f != alg.ZERO for f in fourth_weights)
    for j in range(8):
        assert tools.dot_polynomial([pow(x, j + 1, P) for x in K], fourth_weights) == target[j]
    product = alg.ONE
    for f in weights + fourth_weights:
        product = base.multiply(product, f)
    forbidden = alg.monic(alg.quotient(product, alg.gcd(product, alg.derivative(product))))
    assert forbidden == base.root_polynomial((0, 1, 2, 14, 28, 57, 59))
    exceptional_ranks = {s: three.feas.kernel_basis(
        [[base.evaluate(f, s) for f in row] for row in matrix])[0]
        for s in range(P) if base.evaluate(minor_gcd, s) == 0}
    assert exceptional_ranks == {1: 2}
    ring = ext.Polynomials(tools.ParameterRing())
    d, coefficients, locators = ext.actual_locator(ring, u, v)
    assert d != ring.zero and all(f != ring.zero for f in locators.values())
    return {'fourth_support': K, 'triple_kernel_basis': basis, 'fourth_matrix': matrix,
        'three_by_three_minor_gcd': minor_gcd, 'kernel_rows': rows,
        'primitive_kernel': vector, 'weights': weights, 'fourth_weights': fourth_weights,
        'full_weight_forbidden_polynomial': forbidden, 'exceptional_ranks_prime_field': exceptional_ranks,
        'u': u, 'v': v, 'D': d, 'coefficients': coefficients, 'locators': locators}


def equality_elimination(data):
    forbidden = data['full_weight_forbidden_polynomial']
    resultants = {}
    for y in H:
        if y == 79:
            continue
        res = tools.resultant(data['locators'][79], data['locators'][y])
        assert res != alg.ZERO and alg.degree(res) <= 32
        matrix = tools.sylvester(data['locators'][79], data['locators'][y])
        for s in range(33):
            expected = three.scalar_determinant([[base.evaluate(f, s) for f in row] for row in matrix])
            assert base.evaluate(res, s) == expected
        radical = alg.monic(alg.quotient(res, alg.gcd(res, alg.derivative(res))))
        saturated = alg.quotient(radical, alg.gcd(radical, forbidden))
        resultants[y] = {'resultant': res, 'radical': radical, 'saturated_radical': saturated}
    pairs, triples = [], []
    for x, y in combinations(resultants, 2):
        gcd = alg.gcd(resultants[x]['saturated_radical'], resultants[y]['saturated_radical'])
        assert gcd == alg.ONE
        pairs.append({'coordinates': (x, y), 'gcd': gcd})
    for xs in combinations(resultants, 3):
        gcd = resultants[xs[0]]['saturated_radical']
        for x in xs[1:]:
            gcd = alg.gcd(gcd, resultants[x]['saturated_radical'])
        assert gcd == alg.ONE
        triples.append({'coordinates': xs, 'gcd': gcd})
    assert len(resultants) == 15 and len(pairs) == 105 and len(triples) == 455
    union = alg.ONE
    for entry in triples:
        union = alg.quotient(base.multiply(union, entry['gcd']), alg.gcd(union, entry['gcd']))
    assert union == alg.ONE
    data.update({'coordinate_79_resultants': resultants, 'pairwise_gcd_certificate': pairs,
        'triple_gcd_certificate': triples, 'scalar_resultant_evaluation_checks': 495,
        'necessary_equality_parameter_polynomial': alg.monic(union)})



def representative_audit(data):
    # A concrete full-weight pencil audits the remaining gates; this sample
    # is not used to exclude the whole family, which the gcd certificate does.
    s = 3
    weights = tuple(base.evaluate(f, s) for f in data['weights'])
    fourth_weights = tuple(base.evaluate(f, s) for f in data['fourth_weights'])
    assert all(weights) and all(fourth_weights)
    a = three.word_on(A[0], weights[:4])
    endpoint = three.word_on(A[1], weights[4:8])
    b = tuple((y - x) % P for x, y in zip(a, endpoint))
    u, v = base.syndrome(a), base.syndrome(b)
    assert u == tuple(base.evaluate(f, s) for f in data['u'])
    assert v == tuple(base.evaluate(f, s) for f in data['v'])
    d, coefficients, locators = base.locator(a, b)
    assert d == tools.evaluate_S(data['D'], s)
    assert coefficients == tuple(tools.evaluate_S(f, s) for f in data['coefficients'])
    assert locators == {x: tools.evaluate_S(f, s) for x, f in data['locators'].items()}
    common = alg.ZERO
    for f in locators.values():
        common = alg.gcd(common, f)
    assert common == alg.ONE
    product = alg.resultant_product(locators)
    candidate, power_audit = three.feas.coefficient_power_audit(product)
    decomposition = alg.squarefree_factors(product)
    fourth_power = set(decomposition) == {4} and alg.degree(decomposition[4]) == 16
    assert alg.degree(product) == 64 and not fourth_power
    assert power_audit['power_identity'] == fourth_power
    assert power_audit['failed_residuals'] == list(range(17, 65))
    radicals = {x: alg.monic(alg.quotient(f, alg.gcd(f, alg.derivative(f))))
                for x, f in locators.items()}
    root_parts = {x: alg.field_root_part(f, 20) for x, f in radicals.items()}
    gates = {
        'all_coordinate_degrees_four': all(alg.degree(f) == 4 for f in locators.values()),
        'all_coordinates_squarefree': all(alg.gcd(f, alg.derivative(f)) == alg.ONE
                                         for f in locators.values()),
        'all_coordinates_split_in_F_97_20': all(root_parts[x] == f for x, f in radicals.items()),
        'resultant_c_times_degree_16_fourth_power': fourth_power,
        'all_coordinate_roots_regular': alg.gcd(product, d) == alg.ONE,
        'full_L010_equality': alg.equality_check(d, locators, product)}
    assert gates == {'all_coordinate_degrees_four': True,
        'all_coordinates_squarefree': False, 'all_coordinates_split_in_F_97_20': False,
        'resultant_c_times_degree_16_fourth_power': False,
        'all_coordinate_roots_regular': True, 'full_L010_equality': False}
    radical_product = alg.ONE
    for f in radicals.values():
        radical_product = base.multiply(radical_product, f)
    regular_four = alg.squarefree_factors(radical_product).get(4, alg.ONE)
    regular_four = alg.quotient(regular_four, alg.gcd(regular_four, d))
    expected = base.root_polynomial((0, 1, 2, 3))
    assert regular_four == expected and alg.field_root_part(regular_four, 20) == expected
    bad, event_weights = base.original_event(a, b, base.interpolation_constraints())
    assert bad == {0, 1, 2, 3} and all(w == 4 for w in event_weights.values())
    assert d[-1] and all(alg.degree(f) == 4 for f in locators.values())
    candidate_radical = alg.monic(alg.quotient(candidate, alg.gcd(candidate, alg.derivative(candidate))))
    data['representative_pencil_S_3'] = {
        'weights': weights, 'fourth_weights': fourth_weights, 'a': a, 'b': b,
        'u': u, 'v': v, 'D': d, 'locator_coefficients': coefficients, 'locators': locators,
        'common_locator_gcd': common, 'resultant': product,
        'resultant_squarefree_decomposition': decomposition,
        'coefficient_power_audit': power_audit, 'degree_16_power_candidate': candidate,
        'candidate_squarefree': alg.gcd(candidate, alg.derivative(candidate)) == alg.ONE,
        'candidate_D_coprime': alg.gcd(candidate, d) == alg.ONE,
        'candidate_split_in_F_97_20': alg.field_root_part(candidate_radical, 20) == candidate_radical,
        'separate_equality_gates': gates, 'coordinate_target_field_root_parts': root_parts,
        'target_field_weight_four_polynomial': regular_four,
        'exact_bad_parameters_algebraic_closure': (0, 1, 2, 3),
        'lower_weight_parameters_excluded': True, 'original_infinity_is_sparse': False,
        'independent_original_event_supports_checked': 2517,
        'independent_original_event_parameters': sorted(bad)}


def redundancy_check(data):
    # Bounded code-domain check, not an automorphism classification.
    triple_sets = {frozenset(a) for a in A}
    matches = []
    for previous in ((1, 12, 22, 64), (8, 27, 50, 75), (8, 47, 64, 75)):
        for c in H:
            for inverse in (False, True):
                def phi(x):
                    return c * (pow(x, -1, P) if inverse else x) % P
                if ({frozenset(phi(x) for x in a) for a in A} == triple_sets
                        and frozenset(phi(x) for x in previous) == frozenset(K)):
                    matches.append((previous, c, inverse))
    data['bounded_scaling_inversion_redundancy_matches'] = matches


def main():
    data = family()
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    print(json.dumps({key: data[key] for key in ('primitive_kernel', 'weights', 'fourth_weights',
        'full_weight_forbidden_polynomial', 'three_by_three_minor_gcd', 'exceptional_ranks_prime_field')}), flush=True)
    tools.independent_minors(data)
    equality_elimination(data)
    representative_audit(data)
    redundancy_check(data)
    data['conclusion'] = 'No sixteen-count pencil in the full-weight fourth singular fourth-support family, even over the algebraic closure.'
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'necessary_equality_parameter_polynomial': data['necessary_equality_parameter_polynomial'],
        'pair_gcds': sorted(set(tuple(r['gcd']) for r in data['pairwise_gcd_certificate'])),
        'triple_gcds': sorted(set(tuple(r['gcd']) for r in data['triple_gcd_certificate']))}), flush=True)


if __name__ == '__main__':
    main()

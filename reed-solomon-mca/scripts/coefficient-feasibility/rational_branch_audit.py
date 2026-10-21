"""Complete rational-root certificate for the saved disjoint triple.

Audit extension-scalar descent inputs and every projective identification;
this is certificate assembly, not fresh sampling or arbitrary-triple search.
"""
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('three', HERE / 'three_support.py')
three = importlib.util.module_from_spec(spec)
spec.loader.exec_module(three)
base, alg, feas = three.base, three.alg, three.feas
P, H = base.P, base.H
SUPPORTS = ((1, 8, 12, 18), (22, 27, 33, 47), (50, 64, 70, 75))


def basis_change(u, v, U, V):
    i, j = next((i, j) for i in range(8) for j in range(i + 1, 8)
                if (U[i] * V[j] - U[j] * V[i]) % P)
    inverse = pow((U[i] * V[j] - U[j] * V[i]) % P, -1, P)
    def coordinates(w):
        a = (w[i] * V[j] - w[j] * V[i]) * inverse % P
        b = (U[i] * w[j] - U[j] * w[i]) * inverse % P
        assert tuple((a * x + b * y) % P for x, y in zip(U, V)) == w
        return (a, b)
    a, b = coordinates(u)
    c, d = coordinates(v)
    assert (a * d - b * c) % P
    return ((a, b), (c, d))


def audit(a, b, metadata, stats):
    old_d, old_c, old_l = base.locator(a, b)
    record = three.audit_candidate(a, b, metadata, stats)
    assert record is not None and not record['full_L010_equality']
    assert record['coefficient_power_audit']['degree_gate']
    assert record['coefficient_power_audit']['failed_residuals']
    # Check all homogeneous signed-minor coefficients in the safe chart
    # directly from its actual words, rather than trust the substitution.
    d, c, locators = base.locator(record['a'], record['b'])
    assert d == record['D'] and c == record['locator_coefficients']
    assert locators == feas.locators_by_coordinate(c)
    moments = base.syndrome(record['a']) + base.syndrome(record['b'])
    assert all(sum(x * y for x, y in zip(row, moments)) % P == 0
               for row in feas.matrix_for_affine_moments(c))
    assert len(d) == 5 and all(len(f) == 5 for f in locators.values())
    # An independent factor-multiplicity recognition check must agree
    # with the triangular fourth-root residual, even over extensions.
    decomposition = alg.squarefree_factors(record['R'])
    assert set(decomposition) != {4}
    record['resultant_squarefree_decomposition'] = decomposition
    # Record the exact specified-field locator-root gates, separately
    # from the already decisive power failure.
    record['coordinate_simple'] = all(alg.gcd(f, alg.derivative(f)) == alg.ONE
                                      for f in locators.values())
    field_parts, all_split = {}, True
    for x, f in locators.items():
        radical = alg.monic(alg.quotient(f, alg.gcd(f, alg.derivative(f))))
        part = alg.field_root_part(radical, 20)
        field_parts[x] = part
        all_split = all_split and part == radical
    record['coordinate_radical_parts_in_F_97_20'] = field_parts
    record['all_coordinate_roots_in_F_97_20'] = all_split
    record['resultant_D_coprime'] = alg.gcd(record['R'], d) == alg.ONE
    record['infinity_nonsparse'] = True
    record['original_a'], record['original_b'] = a, b
    record['original_D'], record['original_locator_coefficients'] = old_d, old_c
    return record


def main():
    basis, initial, direction = three.triple_space(SUPPORTS)
    stats = {'zero_D': 0, 'persistent_locator': 0, 'actual_nonpersistent_pencils': 0,
             'power_identity': 0, 'full_equality': 0,
             'weight_four_counts_F_97_20': Counter(),
             'exact_total_counts_F_97_20': Counter(), 'possible_lower_weight_unresolved': 0}
    counts, systems, records, seen = Counter(), [], [], {}
    for k, fourth in enumerate(three.SUPPORTS):
        if fourth in SUPPORTS:
            continue
        counts['fourth_supports'] += 1
        matrix = three.fourth_matrix(fourth, initial, direction)
        determinant = base.determinant(matrix)
        for t in range(5):
            numerical = [[base.evaluate(f, t) for f in row] for row in matrix]
            assert three.scalar_determinant(numerical) == base.evaluate(determinant, t)
        system = {'support': fourth, 'matrix': matrix, 'determinant': determinant,
                  'rational_roots': []}
        systems.append(system)
        if determinant == alg.ZERO:
            counts['zero_determinants'] += 1
            continue
        radical = alg.monic(alg.quotient(determinant,
                                         alg.gcd(determinant, alg.derivative(determinant))))
        rational = alg.field_root_part(radical, 1)
        roots = [t for t in range(P) if not base.evaluate(rational, t)]
        assert len(roots) == alg.degree(rational)
        assert base.root_polynomial(roots) == rational
        system['rational_root_factor'] = rational
        system['excluded_triple_roots'] = [t for t in roots if t in (0, 1, 2)]
        for t in roots:
            if t in (0, 1, 2):
                continue
            counts['rational_root_occurrences'] += 1
            numerical = [[base.evaluate(f, t) for f in row] for row in matrix]
            rank, kernels = feas.kernel_basis(numerical)
            assert rank == 3 and len(kernels) == 1
            occurrence = {'parameter': t, 'rank': rank, 'kernel': kernels[0]}
            system['rational_roots'].append(occurrence)
            weights = tuple(sum(z * w[j] for z, w in zip(kernels[0], basis)) % P
                            for j in range(12))
            occurrence['triple_weights'] = weights
            if not all(weights):
                counts['zero_weight_roots'] += 1
                occurrence['gate'] = 'zero_triple_weight'
                continue
            e0 = three.word_on(SUPPORTS[0], weights[:4])
            e1 = three.word_on(SUPPORTS[1], weights[4:8])
            e2 = three.word_on(SUPPORTS[2], weights[8:])
            a, b = e0, tuple((y - x) % P for x, y in zip(e0, e1))
            u, v = base.syndrome(a), base.syndrome(b)
            assert tuple((x + 2 * y) % P for x, y in zip(u, v)) == base.syndrome(e2)
            target = tuple((x + t * y) % P for x, y in zip(u, v))
            fourth_weights = base.solve_square([[pow(x, j, P) for x in fourth]
                                                for j in range(1, 5)], target[:4])
            assert base.syndrome(three.word_on(fourth, fourth_weights)) == target
            occurrence['fourth_weights'] = fourth_weights
            if not all(fourth_weights):
                counts['zero_weight_roots'] += 1
                occurrence['gate'] = 'zero_fourth_weight'
                continue
            counts['full_weight_root_occurrences'] += 1
            occurrence['gate'] = 'full_weight_actual_pencil'
            key = three.line_key(u, v)
            if key not in seen:
                seen[key] = len(records)
                metadata = {'layout': 5, 'supports': SUPPORTS + (fourth,),
                            'fourth_parameter': t, 'triple_weights': weights,
                            'fourth_weights': fourth_weights, 'projective_line_key': key}
                records.append(audit(a, b, metadata, stats))
            index = seen[key]
            representative = records[index]
            U = base.syndrome(representative['original_a'])
            V = base.syndrome(representative['original_b'])
            occurrence['audited_line_index'] = index
            occurrence['basis_change_to_representative'] = basis_change(u, v, U, V)
        if (k + 1) % 256 == 0:
            print(f"supports {k+1}/1820; rational roots {counts['rational_root_occurrences']}; "
                  f"audited lines {len(records)}", flush=True)
            write(counts, stats, systems, records, False)
    old = json.loads((HERE / 'three-support-result.json').read_text())['layouts'][5]
    assert counts['fourth_supports'] == old['fourth_supports_tested'] == 1817
    assert counts['zero_determinants'] == old['zero_determinants'] == 4
    assert counts['rational_root_occurrences'] == old['prime_field_determinant_roots'] == 1329
    assert counts['full_weight_root_occurrences'] == old['one_dimensional_full_weight_roots'] == 1132
    assert counts['zero_weight_roots'] == old['zero_weight_kernels'] == 197
    assert not stats['power_identity'] and not stats['full_equality']
    assert not stats['zero_D'] and not stats['persistent_locator']
    counts['audited_projective_lines'] = len(records)
    write(counts, stats, systems, records, True)
    print('PASS: complete rank-three rational-root certificate; explicit basis changes for every retained occurrence.')
    print('PASS: actual minors, all failed fourth-power residuals, independent multiplicity and exact target-field gates.')
    print(json.dumps({'counts': counts, 'audit_counts': stats, 'required_upper_count': 15,
                      'restricted_triple_upper_count': 15}, sort_keys=True))
    print('Artifacts: scripts/coefficient-feasibility/rational-branch-audit-result.json')
    print('No arbitrary-triple or global fifteen-count bound is claimed.')


def write(counts, stats, systems, records, completed):
    report = {'scope': 'Saved disjoint triple; all rational roots of nonzero fourth determinants, arbitrary extension scalars via rank-three descent.',
              'completed': completed, 'supports': SUPPORTS, 'target_extension_degree': 20,
              'counts': counts, 'actual_pencil_audit_counts': stats,
              'fourth_system_certificate': systems, 'audited_projective_lines': records}
    (HERE / 'rational-branch-audit-result.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()

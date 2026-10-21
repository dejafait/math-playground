#!/usr/bin/env python3
"""L057 critical audit: reconstruct full sets, all saved minors and zero pivots.

No notebook imports. Uses removed/added five-sets rather than membership
atoms and rational Gaussian elimination rather than permutation determinants
or the existing verifier's closed formulas. Writes complete audit evidence.
"""
import hashlib
import itertools as it
import json
import re
from fractions import Fraction as Q
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'released-zero-reanchored-critical-audit-results.json'


def enc(value):
    value = Q(value)
    return [value.numerator, value.denominator]


def determinant(matrix):
    a = [row[:] for row in matrix]
    value = Q(1)
    for k in range(len(a)):
        pivot = next((j for j in range(k, len(a)) if a[j][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            value = -value
        value *= a[k][k]
        for j in range(k+1, len(a)):
            ratio = a[j][k] / a[k][k]
            for h in range(k+1, len(a)):
                a[j][h] -= ratio*a[k][h]
            a[j][k] = Q(0)
    return value


def psd_pivots(matrix):
    a = [row[:] for row in matrix]
    steps = []
    for k in range(len(a)):
        p = a[k][k]
        zero_row = all(a[k][j] == 0 for j in range(k+1, len(a)))
        steps.append({'pivot': enc(p), 'zero_pivot_remaining_row_zero': zero_row if p == 0 else None})
        if p < 0 or (p == 0 and not zero_row):
            return False, steps
        if p:
            for i in range(k+1, len(a)):
                for j in range(k+1, len(a)):
                    a[i][j] -= a[i][k]*a[k][j]/p
    return True, steps


def main():
    source = ROOT / 'released-zero-reanchored-results.json'
    verification = ROOT / 'released-zero-reanchored-verification.json'
    manuscript = NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md'
    lp_path = ROOT / 'delsarte-lp-results.json'
    saved = json.loads(source.read_text())
    verified = json.loads(verification.read_text())
    primal = json.loads(lp_path.read_text())['exact']['primal']
    parsed = [(int(r), int(q), Q(z)) for r, q, z in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', manuscript.read_text(), re.M)]
    z = {(r, q): value for r, q, value in parsed}
    p = [Q(1)] + [Q(0)]*4 + [Q(a['numerator'], a['denominator']) /
        (2*comb(68, i)*comb(956, i)) for i, a in enumerate(primal, 5)]
    rho = (Q(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    failures, checks, all_records, boolean_records = [], 0, [], []
    minor_count, zero_minors, singular_count = 0, 0, 0

    def check(name, condition, where=None):
        nonlocal checks
        checks += 1
        if not condition:
            failures.append({'check': name, 'where': where})

    def audit_matrix(record, supports, tag, y=None):
        nonlocal minor_count, zero_minors, singular_count
        anchor, second, third = supports
        indices = list(dict.fromkeys((frozenset([anchor]), frozenset([anchor, second]),
                                      frozenset([anchor, third]))))

        def value(family):
            if len(family) == 1:
                return Q(1)
            if len(family) == 2:
                u, v = tuple(family)
                return p[len(u ^ v)//2]
            assert y is not None
            return y

        matrix = [[value(i | j) for j in indices] for i in indices]
        check('matrix_from_support_family_unions', record['matrix_over_rho'] ==
              [[enc(v) for v in row] for row in matrix], tag)
        check('symmetric', matrix == list(map(list, zip(*matrix))), tag)
        saved_minors = record['principal_minors_over_rho']
        subsets = [list(s) for n in range(1, len(matrix)+1)
                   for s in it.combinations(range(len(matrix)), n)]
        check('complete_minor_order', [m['indices'] for m in saved_minors] == subsets, tag)
        minors = []
        for s, stored in zip(subsets, saved_minors):
            v = determinant([[matrix[i][j] for j in s] for i in s])
            check('exact_minor', stored['value'] == enc(v), [tag, s])
            check('nonnegative_minor', v >= 0, [tag, s])
            if 'sign' in stored:
                check('minor_sign', stored['sign'] == (v > 0)-(v < 0), [tag, s])
            minors.append({'indices': s, 'value': enc(v)})
            minor_count += 1
            zero_minors += (v == 0)
        schur = [[matrix[i][j]-matrix[i][0]*matrix[0][j]
                  for j in range(1, len(matrix))] for i in range(1, len(matrix))]
        if 'Schur_over_rho' in record:
            check('saved_Schur', record['Schur_over_rho'] ==
                  [[enc(v) for v in row] for row in schur], tag)
        passed, pivots = psd_pivots(matrix)
        check('PSD_including_zero_pivots', passed, tag)
        check('singular_cases_exactly_zero_pair_diagonal',
              any(s['pivot'][0] == 0 for s in pivots) ==
              any(matrix[i][i] == 0 for i in range(1, len(matrix))), tag)
        if 'PSD' in record:
            check('saved_PSD', record['PSD'] == passed, tag)
        singular_count += any(s['pivot'][0] == 0 for s in pivots)
        return {'tag': tag, 'matrix': [[enc(v) for v in row] for row in matrix],
                'Schur': [[enc(v) for v in row] for row in schur],
                'minors': minors, 'pivots': pivots}, indices

    check('full_primal', len(primal) == 64 and len(p) == 69)
    check('canonical_21_coefficients', [(r, q) for r, q, v in parsed] ==
          [(r, q) for r in range(6) for q in range(6) if r+q >= 5])
    check('nonnegative_coefficients', all(v >= 0 for v in z.values()))
    check('normalization', saved['normalization']['p'] == list(map(enc, p)) and
          saved['normalization']['rho'] == enc(rho) and rho > 0)
    check('pair_range_and_p5', all(0 <= a <= 1 for a in p) and p[5] == Q(1, 68881143660))
    for path, sha in saved['source_sha256'].items():
        check('source_hash', hashlib.sha256((NB/path).read_bytes()).hexdigest() == sha, path)
    check('complete_relations', [s['relation'] for s in saved['records']] ==
          [[r, q] for r in range(6) for q in range(6)])
    universe = set(range(1024))
    A, X, Y = frozenset(range(68)), set(range(5)), set(range(68, 73))
    B = frozenset((A-X) | Y)
    orbit_keys = {}
    for record in saved['records']:
        r, q = record['relation']
        X2 = set(range(5-r)) | set(range(5, 5+r))
        Y2 = set(range(68, 73-q)) | set(range(73, 73+q))
        C = frozenset((A-X2) | Y2)
        supports = [A, B, C]
        check('complete_supports', all(len(s) == 68 and s <= universe for s in supports), [r, q])
        check('distinct_supports', record['distinct_supports'] == len(set(supports)) ==
              (2 if r == q == 0 else 3), [r, q])
        y = p[5] if r == q == 0 else p[5]*z.get((r, q), Q(0)) / (
            comb(5, r)*comb(63, r)*comb(5, q)*comb(951, q))
        check('triple_value', record['triple_over_rho'] == enc(y), [r, q])
        orders = list(it.permutations(range(3)))
        check('six_orders', [m['order'] for m in record['matrices']] == list(map(list, orders)), [r, q])
        keys = []
        for order, m in zip(orders, record['matrices']):
            D, E, F = [supports[i] for i in order]
            # Independently count point membership in all eight regions.
            counts = [0]*8
            for point in universe:
                counts[4*(point in D)+2*(point in E)+(point in F)] += 1
            regions = [counts[i] for i in (4, 5, 6, 7, 3, 2, 1, 0)]
            keys.append(tuple(regions))
            distances = [len(u ^ v)//2 for u, v in ((D, E), (D, F), (E, F))]
            tag = [r, q, list(order)]
            check('all_saved_regions', m['full_regions'] == regions, tag)
            check('all_saved_distances', m['distances'] == distances, tag)
            if distances[:2] == [5, 5]:
                check('eligible_anchor_relation', [5-regions[0], 5-regions[4]] == [r, q], tag)
            evidence, indices = audit_matrix(m, (D, E, F), tag, y)
            stored_indices = [frozenset(supports[i] for i in family) for family in m['indices']]
            check('all_saved_family_indices', stored_indices == indices and
                  all(len(family) == len(set(family)) for family in m['indices']), tag)
            evidence.update(regions=regions, distances=distances,
                            family_indices=[sorted(supports.index(s) for s in family) for family in indices])
            all_records.append(evidence)
        key = min(keys)
        check('no_unordered_orbit_collision', key not in orbit_keys, [r, q])
        orbit_keys[key] = [r, q]
    represented_zero = zero_minors
    represented_singular = singular_count
    expected_boolean = [(0, [0, 0, 0])] + [(d, list(pat)) for d in range(1, 11)
                         for pat in ((0, 0, 1), (0, 1, 0), (1, 0, 0))]
    check('complete_Boolean_patterns', [(m['distance'], m['equality_pattern']) for m in
          saved['Boolean_closure']] == expected_boolean)
    for m in saved['Boolean_closure']:
        d, pattern = m['distance'], m['equality_pattern']
        other = frozenset((A-set(range(d))) | set(range(68, 68+d)))
        supports = [(A, other)[i] for i in pattern]
        evidence, indices = audit_matrix(m, supports, ['Boolean', d, pattern])
        boolean_records.append(evidence)
    check('matrix_counts', len(all_records) == 216 and len(boolean_records) == 31)
    check('minor_counts', minor_count == 1579 and represented_zero == 224)
    check('complete_singular_case_counts', represented_singular == 56 and singular_count-represented_singular == 12)
    check('constructor_counts', saved['counts'] == {
        'relations': 36, 'matrices': 216, 'distinct_matrices': 210, 'Boolean_matrices': 6,
        'minors': 1488, 'negative_minors': 0, 'nonPSD_matrices': 0, 'zero_minors': represented_zero})
    check('constructor_summary', saved['reconstruction_checks'] == 1170 and
          saved['input_errors'] == [] and saved['negative_minors'] == [] and saved['verdict'] == 'PASS')
    check('entire_verifier_report', verified == {
        'certificate_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'checks': 5435, 'minors_verified': 1579, 'failures': [], 'verified': True})
    result = {'source_sha256': {str(path.relative_to(NB)): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in (source, verification, manuscript, lp_path)},
              'checks': checks, 'failures': failures, 'verified': not failures,
              'counts': {'represented_matrices': len(all_records), 'Boolean_matrices': len(boolean_records),
                         'minors': minor_count, 'represented_zero_minors': represented_zero,
                         'represented_singular_matrices': represented_singular,
                         'Boolean_singular_matrices': singular_count-represented_singular,
                         'total_zero_minors': zero_minors, 'singular_matrices': singular_count},
              'represented_evidence': all_records, 'Boolean_evidence': boolean_records}
    OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print('Actual/required: 216/216 represented matrices; 31/31 Boolean matrices;', minor_count, '/1579 minors')
    print('Checks:', checks, '; failures:', len(failures), '; singular matrices:', singular_count,
          '; total zero minors:', zero_minors, '; retained:', not failures)
    print('Full evidence:', OUT)
    if failures:
        print('Failures:', failures)
    assert not failures


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact fixed L056 reanchored small-principal test; no optimization.

Parse every z from the canonical manuscript, check saved fixed inputs,
construct full point sets and Boolean union indices, and save ALL minors.
No notebook module is imported. Negative minors are test results, whereas
input/identity failures invalidate the reconstruction.
"""
import hashlib
import itertools
import json
import re
from fractions import Fraction as Q
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT.parent.parent
OUT = ROOT / 'released-zero-reanchored-results.json'


def enc(z):
    z = Q(z)
    return [z.numerator, z.denominator]


def determinant(matrix):
    total = Q(0)
    for perm in itertools.permutations(range(len(matrix))):
        sign = (-1)**sum(perm[i] > perm[j]
                        for i in range(len(perm)) for j in range(i+1, len(perm)))
        term = Q(sign)
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total += term
    return total


def main():
    paths = [NOTEBOOK / 'lemmas/L056-released-zero-five-shell-nonexclusion.md',
             ROOT / 'released-zero-five-shell-results.json',
             ROOT / 'selected-triple-sdp-results.json',
             ROOT / 'delsarte-lp-results.json']
    text = paths[0].read_text()
    released, selected, lp = [json.loads(path.read_text()) for path in paths[1:]]
    p = [Q(1)] + [Q(0)]*4 + [
        Q(z['numerator'], z['denominator'])/(2*comb(68, i)*comb(956, i))
        for i, z in zip(range(5, 69), lp['exact']['primal'])]
    relations = [(r, q) for r in range(6) for q in range(6) if r+q >= 5]
    parsed = [(int(r), int(q), Q(z)) for r, q, z in
              re.findall(r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', text, re.M)]
    errors, checks = [], []

    def check(name, valid, detail=None):
        checks.append(name)
        if not valid:
            errors.append({'check': name, 'detail': detail})

    check('complete_manuscript_vector', [(r, q) for r, q, z in parsed] == relations)
    check('fixed_pairs', len(p) == 69 and list(map(enc, p)) == selected['p']
          == released['parameters']['p'])
    check('pair_interval', all(0 <= z <= 1 for z in p))
    check('p5', p[5] == Q(1, 68881143660))
    check('saved_relations', released['parameters']['relations'] == [list(t) for t in relations])
    check('saved_coefficients', [enc(z) for r, q, z in parsed] == released['exact']['primal'])
    zvalues = {(r, q): z for r, q, z in parsed}
    dvalues = {(r, q): z/(comb(5, r)*comb(63, r)*comb(5, q)*comb(951, q))
               for (r, q), z in zvalues.items()}
    check('fixed_valencies', released['parameters']['valencies'] == [
        comb(5, r)*comb(63, r)*comb(5, q)*comb(951, q) for r, q in relations])
    U = Q(comb(1024, 64), comb(68, 64))
    rho = (U+1)/(2*comb(1024, 68))
    check('positive_singleton', rho > 0)
    records, negative, counts = [], [], {'relations': 0, 'matrices': 0,
        'distinct_matrices': 0, 'Boolean_matrices': 0, 'minors': 0,
        'negative_minors': 0, 'nonPSD_matrices': 0, 'zero_minors': 0}
    orbit_keys = {}
    for r in range(6):
        for q in range(6):
            counts['relations'] += 1
            sizes = {4: 5-r, 5: r, 6: r, 7: 63-r,
                     3: 5-q, 2: q, 1: q, 0: 951-q}
            atoms, cursor = {}, 0
            for mask in range(8):
                atoms[mask] = set(range(cursor, cursor+sizes[mask]))
                cursor += sizes[mask]
            supports = [frozenset().union(*(atoms[mask] for mask in range(8)
                                          if mask & bit)) for bit in (4, 2, 1)]
            check('point_partition', cursor == 1024 and all(len(s) == 68 for s in supports), [r, q])
            unique = len(set(supports))
            check('Boolean_relation', (unique == 2) == (r == q == 0), [r, q])
            y = p[5] if unique == 2 else p[5]*dvalues.get((r, q), Q(0))
            check('moment_nonnegative', y >= 0, [r, q])
            full_keys, matrices = [], []
            for order in itertools.permutations(range(3)):
                A, B, C = [supports[i] for i in order]
                i, j, h = len(A-B), len(A-C), len(B-C)
                t, s = len((A-B) & (A-C)), len((B-A) & (C-A))
                regions = [t, i-t, j-t, 68-i-j+t, s, i-s, j-s, 956-i-j+s]
                direct = [len(A-(B|C)), len((A&C)-B), len((A&B)-C), len(A&B&C),
                          len((B&C)-A), len(B-(A|C)), len(C-(A|B)), 1024-len(A|B|C)]
                check('permuted_full_regions', regions == direct and h == i+j-t-s, [r, q, order])
                full_keys.append(tuple(direct))
                if i == j == 5:
                    check('eligible_relation', (5-t, 5-s) == (r, q), [r, q, order])
                # Families of supports, not unions of their ground-set points.
                indices = list(dict.fromkeys((frozenset([A]), frozenset([A, B]), frozenset([A, C]))))

                def moment(family):
                    if len(family) == 1:
                        return Q(1)
                    if len(family) == 2:
                        first, second = tuple(family)
                        return p[len(first-second)]
                    assert len(family) == 3
                    return y

                matrix = [[moment(I | J) for J in indices] for I in indices]
                expected = [[Q(1), p[i], p[j]], [p[i], p[i], y], [p[j], y, p[j]]]
                check('union_matrix', unique != 3 or matrix == expected, [r, q, order])
                check('Boolean_matrix', unique != 2 or matrix == [[Q(1), p[5]], [p[5], p[5]]], [r, q, order])
                minors = []
                for size in range(1, len(matrix)+1):
                    for subset in itertools.combinations(range(len(matrix)), size):
                        value = determinant([[matrix[a][b] for b in subset] for a in subset])
                        minors.append({'indices': list(subset), 'value': enc(value),
                                       'sign': (value > 0)-(value < 0)})
                        counts['minors'] += 1
                        counts['zero_minors'] += value == 0
                        if value < 0:
                            counts['negative_minors'] += 1
                            negative.append({'relation': [r, q], 'order': list(order),
                                             'distances': [i, j, h], 'indices': list(subset),
                                             'value': enc(value)})
                if unique == 3:
                    schur = [[p[i]-p[i]**2, y-p[i]*p[j]],
                             [y-p[i]*p[j], p[j]-p[j]**2]]
                    check('Schur_determinant', determinant(schur) == determinant(matrix), [r, q, order])
                else:
                    schur = [[p[5]-p[5]**2]]
                passed = all(item['sign'] >= 0 for item in minors)
                counts['matrices'] += 1
                counts['distinct_matrices' if unique == 3 else 'Boolean_matrices'] += 1
                counts['nonPSD_matrices'] += not passed
                matrices.append({'order': list(order), 'distances': [i, j, h],
                    'full_regions': direct, 'indices': [[supports.index(S) for S in sorted(I)] for I in indices],
                    'matrix_over_rho': [[enc(v) for v in row] for row in matrix],
                    'Schur_over_rho': [[enc(v) for v in row] for row in schur],
                    'principal_minors_over_rho': minors, 'PSD': passed})
            key = min(full_keys)
            check('unordered_orbit_distinctness', key not in orbit_keys, [r, q])
            orbit_keys[key] = [r, q]
            records.append({'relation': [r, q], 'triple_over_rho': enc(y),
                            'distinct_supports': unique, 'matrices': matrices})
    check('coverage_counts', counts['relations'] == 36 and counts['matrices'] == 216
          and counts['Boolean_matrices'] == 6 and counts['minors'] == 1488)
    # Boolean lower-order closure: every represented pair distance is 0..10.
    # These are support identities, not additional distinct triple values.
    boolean_records = []
    for distance in range(11):
        patterns = [(0, 0, 0)] if distance == 0 else [(0, 0, 1), (0, 1, 0), (1, 0, 0)]
        for pattern in patterns:
            anchor, second, third = pattern
            indices = list(dict.fromkeys((frozenset([anchor]), frozenset([anchor, second]),
                                         frozenset([anchor, third]))))
            matrix = [[Q(1) if len(I | J) == 1 else p[distance] for J in indices] for I in indices]
            minors = []
            for size in range(1, len(matrix)+1):
                for subset in itertools.combinations(range(len(matrix)), size):
                    value = determinant([[matrix[a][b] for b in subset] for a in subset])
                    minors.append({'indices': list(subset), 'value': enc(value)})
            expected = [[Q(1)]] if distance == 0 else [[Q(1), p[distance]], [p[distance], p[distance]]]
            check('Boolean_closure_matrix', matrix == expected, [distance, pattern])
            check('Boolean_closure_PSD', all(Q(*item['value']) >= 0 for item in minors), [distance, pattern])
            boolean_records.append({'distance': distance, 'equality_pattern': list(pattern),
                                    'matrix_over_rho': [[enc(v) for v in row] for row in matrix],
                                    'principal_minors_over_rho': minors})
    check('Boolean_closure_coverage', len(boolean_records) == 31
          and sum(len(item['principal_minors_over_rho']) for item in boolean_records) == 91)
    result = {'source_sha256': {str(path.relative_to(NOTEBOOK)): hashlib.sha256(path.read_bytes()).hexdigest()
                                for path in paths},
              'normalization': {'rho': enc(rho), 'p': list(map(enc, p)),
                                'matrices_are_actual_moments_divided_by': 'rho>0'},
              'counts': counts, 'reconstruction_checks': len(checks), 'input_errors': errors,
              'records': records, 'Boolean_closure': boolean_records, 'negative_minors': negative,
              'verdict': 'INVALID' if errors else 'FAIL' if negative else 'PASS',
              'scope': 'Unchanged L056 represented triples, all anchors and Boolean repetitions only.'}
    OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print('Verdict:', result['verdict'], '; input/identity errors:', len(errors))
    print('Coverage actual/required:', counts['relations'], '/36 relations;', counts['matrices'],
          '/216 ordered matrices;', counts['minors'], '/1488 principal minors')
    print('NonPSD matrices:', counts['nonPSD_matrices'], '; negative minors:', counts['negative_minors'],
          '; zero minors:', counts['zero_minors'])
    print('Boolean closure actual/required: 31/31 matrices; 91/91 minors')
    if negative:
        print('First negative minor:', negative[0])
    print('Full certificate:', OUT)
    assert not errors, errors


if __name__ == '__main__':
    main()

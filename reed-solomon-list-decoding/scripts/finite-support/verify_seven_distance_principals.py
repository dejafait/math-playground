#!/usr/bin/env python3
"""Independent intersection enumeration, Gaussian minors and complete congruences.

No constructor or other notebook code is imported. All saved cases are consumed.
"""
import hashlib
import itertools as it
import json
import re
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'seven-distance-principals-verification.json'


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def determinant(matrix):
    a = [row[:] for row in matrix]
    value = F(1)
    for k in range(len(a)):
        row = next((j for j in range(k, len(a)) if a[j][k]), None)
        if row is None:
            return F(0)
        if row != k:
            a[k], a[row] = a[row], a[k]
            value = -value
        value *= a[k][k]
        for j in range(k+1, len(a)):
            ratio = a[j][k]/a[k][k]
            for h in range(k+1, len(a)):
                a[j][h] -= ratio*a[k][h]
    return value


def main():
    paths = [ROOT/'seven-distance-principals-results.json',
             NB/'lemmas/L056-released-zero-five-shell-nonexclusion.md',
             ROOT/'delsarte-lp-results.json',
             ROOT/'simultaneous-shell-ordinary-scalars-results.json']
    saved, lp, scalar = [json.loads(paths[i].read_text()) for i in (0, 2, 3)]
    z = {(int(a), int(b)): F(v) for a, b, v in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', paths[1].read_text(), re.M)}
    pairs = [F(1)]+[F(0)]*4+[F(v['numerator'], v['denominator'])/(2*comb(68, i)*comb(956, i))
                            for i, v in enumerate(lp['exact']['primal'], 5)]
    rho = (F(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    checks, failures = 0, []
    def check(name, condition, where=None):
        nonlocal checks
        checks += 1
        if not condition:
            failures.append({'check': name, 'where': where})
    check('input_hashes', all(hashlib.sha256((NB/path).read_bytes()).hexdigest() == value
                            for path, value in saved['source_sha256'].items()))
    check('constructor_valid', not saved['errors'] and saved['verdict'] in ('PASS', 'FAIL'))
    check('normalization', saved['normalization'] == {'rho': enc(rho), 'pairs': list(map(enc, pairs))}
          and rho > 0 and pairs[7] == F(3539, 248922676958508))
    check('canonical_L056_domain', set(z) == {(r, q) for r in range(6) for q in range(6) if r+q >= 5})
    check('same_L062_pairs', list(map(enc, pairs[:13])) == scalar['pairs_through_12'] and enc(rho) == scalar['rho'])
    # Distinct supports have pair intersection sizes 68-distance.
    fixed = {0: 1024, 1: 68, 2: 68, 4: 68, 8: 68,
             3: 63, 5: 63, 9: 61, 6: 62, 10: 63, 12: 63}
    triples = [7, 11, 13, 14]
    boxes = []
    for mask in triples:
        vertices = [1 << j for j in range(4) if mask & (1 << j)]
        lower = max(fixed[a|b]+fixed[a|c]-68
                    for a, b, c in it.permutations(vertices))
        upper = min(fixed[a|b] for a, b in it.combinations(vertices, 2))
        boxes.append(range(lower, upper+1))
    # Removing 5+5+7 points from D gives |DEFG|>=51.
    # Containment in DG gives |DEFG|<=61. Loose lower bounds are allowed.
    boxes.append(range(51, 62))
    check('proven_complete_boxes', [(r.start, r.stop-1) for r in boxes]
          == [(58, 62), (58, 61), (58, 61), (58, 62), (51, 61)])
    atom_vectors = []
    for values in it.product(*boxes):
        intersections = {**fixed, **dict(zip(triples+[15], values))}
        atoms = tuple(sum((-1)**((t^s).bit_count())*intersections[t]
                          for t in range(16) if t&s == s) for s in range(16))
        if min(atoms) < 0:
            continue
        check('mobius_inverse_all_intersections',
              all(sum(atoms[t] for t in range(16) if t&s == s) == intersections[s]
                  for s in range(16)), values)
        atom_vectors.append(atoms)
    lookup = {tuple(row['atoms_by_D_E_F_G_bitmask']): (index, row)
              for index, row in enumerate(saved['records'])}
    check('independent_unique_enumeration', len(atom_vectors) == len(set(atom_vectors)))
    check('full_enumeration_equality', len(lookup) == len(saved['records']) == len(atom_vectors)
          and set(lookup) == set(atom_vectors))
    check('nonempty_scope', len(atom_vectors) > 0)
    dictionary = {}
    for row in scalar['types']:
        key = min(tuple(p['atoms']) for p in row['presentations'])
        value = F(*row['y'])
        check('L062_dictionary_consistent', key not in dictionary or dictionary[key] == value, row['type'])
        dictionary[key] = value
    all_subsets = [list(s) for size in range(1, 5) for s in it.combinations(range(4), size)]
    reconstructed = []
    count_minors = count_matrices = zero_minors = singular = 0
    negative = []
    minimum_pivot_ratio = None
    for atoms in atom_vectors:
        record_index, row = lookup[atoms]
        tag = row['parameters']
        # Counts of arbitrary membership predicates, without constructing
        # consecutive point representatives or using removed/added recipes.
        def count(predicate):
            return sum(n for mask, n in enumerate(atoms) if predicate(mask))
        check('full_partition_and_weights', sum(atoms) == 1024
              and all(count(lambda m: bool(m & (1 << j))) == 68 for j in range(4)), tag)
        distances = [count(lambda m: bool(m & (1 << i)) and not (m & (1 << j)))
                     for i, j in it.combinations(range(4), 2)]
        check('all_distances', distances == row['distances'] == [5, 5, 7, 6, 5, 5], tag)
        def removed_mask(i, j):
            return count(lambda m: bool(m & 1) and not (m & (1 << i)) and not (m & (1 << j)))
        parameters = [removed_mask(i, j) for i, j in [(1, 2), (1, 3), (2, 3)]]
        parameters += [atoms[1], atoms[14]]
        check('independent_parameter_recovery', parameters == tag, tag)
        triple_values, triple_evidence = {}, {}
        check('exact_four_triples', set(row['triples']) == {'0,1,2', '0,1,3', '0,2,3', '1,2,3'}, tag)
        for ids in it.combinations(range(4), 3):
            key_string = ','.join(map(str, ids))
            stored = row['triples'][key_string]
            permutations, values = [], []
            for order in it.permutations(ids):
                A, B, C = [1 << i for i in order]
                regions = [0]*8
                for mask, n in enumerate(atoms):
                    regions[4*bool(mask&A)+2*bool(mask&B)+bool(mask&C)] += n
                a = regions[4]+regions[5]
                b = regions[4]+regions[6]
                h = regions[2]+regions[6]
                eligible = a == b == 5
                item = {'order': list(order), 'atoms_4_2_1': regions, 'eligible': eligible}
                if eligible:
                    r = 5-regions[4]
                    q = 5-regions[3]
                    check('complete_region_recipe',
                          regions == [951-q, q, q, 5-q, 5-r, r, r, 63-r]
                          and r+q == h and (r, q) in z, [tag, order])
                    item['relation'] = [r, q]
                    values.append(pairs[5]*z[r, q]/(comb(5, r)*comb(63, r)*comb(5, q)*comb(951, q)))
                permutations.append(item)
            key = min(tuple(p['atoms_4_2_1']) for p in permutations)
            check('all_six_presentations', permutations == stored['presentations'], [tag, ids])
            check('canonical_key', list(key) == stored['unordered_key'], [tag, ids])
            check('exact_covered_triple', len(values) == 2 and len(set(values)) == 1
                  and enc(values[0]) == stored['moment_over_rho']
                  and key in dictionary and dictionary[key] == values[0], [tag, ids])
            triple_values[frozenset(ids)] = values[0]
            triple_evidence[key_string] = {'presentations': permutations, 'y': enc(values[0])}
        matrices = []
        check('exact_four_anchor_order', [v['anchor'] for v in row['matrices']] == list(range(4)), tag)
        for anchor, stored in enumerate(row['matrices']):
            families = [frozenset([anchor])]+[frozenset([anchor, j]) for j in range(4) if j != anchor]
            def moment(ids):
                if len(ids) == 1:
                    return F(1)
                if len(ids) == 2:
                    i, j = sorted(ids)
                    return pairs[count(lambda m: bool(m & (1 << i)) and not (m & (1 << j)))]
                return triple_values[ids]
            matrix = [[moment(I|J) for J in families] for I in families]
            check('all_family_union_entries', stored['indices'] == [sorted(I) for I in families]
                  and stored['matrix_over_rho'] == [list(map(enc, r)) for r in matrix], [tag, anchor])
            check('all_nonempty_principal_subsets',
                  [v['indices'] for v in stored['principal_minors_over_rho']] == all_subsets, [tag, anchor])
            minors = []
            for subset, old in zip(all_subsets, stored['principal_minors_over_rho']):
                value = determinant([[matrix[i][j] for j in subset] for i in subset])
                check('independent_rational_minor', enc(value) == old['value'], [tag, anchor, subset])
                count_minors += 1
                zero_minors += value == 0
                minors.append({'indices': subset, 'value': enc(value)})
            PSD = all(F(*m['value']) >= 0 for m in minors)
            check('PSD_all_minors_verdict', PSD == stored['PSD'], [tag, anchor])
            evidence = {'anchor': anchor, 'matrix_over_rho': [list(map(enc, r)) for r in matrix], 'minors': minors}
            if PSD:
                columns = [[F(*x) for x in col] for col in stored['congruence_columns']]
                check('invertible_congruence', len(columns) == 4 and all(len(v) == 4 for v in columns)
                      and determinant(columns) != 0, [tag, anchor])
                diagonal = [[sum(v[i]*matrix[i][j]*w[j] for i in range(4) for j in range(4))
                             for w in columns] for v in columns]
                check('complete_congruence_identity', stored['congruence_diagonal_matrix']
                      == [list(map(enc, r)) for r in diagonal], [tag, anchor])
                for i, j in it.product(range(4), repeat=2):
                    check('every_diagonal_and_offdiagonal_entry',
                          diagonal[i][j] == (F(*stored['pivots'][i]) if i == j else 0), [tag, anchor, i, j])
                check('all_nonnegative_pivots', all(diagonal[i][i] >= 0 for i in range(4)), [tag, anchor])
                check('determinant_congruence_identity', determinant(matrix)*determinant(columns)**2
                      == diagonal[0][0]*diagonal[1][1]*diagonal[2][2]*diagonal[3][3], [tag, anchor])
                singular += any(diagonal[i][i] == 0 for i in range(4))
                evidence.update({'congruence_columns': stored['congruence_columns'],
                                 'diagonal': [list(map(enc, r)) for r in diagonal]})
                for i in range(4):
                    ratio = diagonal[i][i]/matrix[i][i]
                    if minimum_pivot_ratio is None or ratio < minimum_pivot_ratio['value']:
                        minimum_pivot_ratio = {'value': ratio, 'parameters': tag, 'anchor': anchor, 'pivot': i}
            else:
                negative.append([record_index, anchor])
                v = [F(*x) for x in stored['negative_vector']]
                value = sum(v[i]*matrix[i][j]*v[j] for i in range(4) for j in range(4))
                check('independent_negative_quadratic_form', value < 0 and enc(value) == stored['negative_value'], [tag, anchor])
                evidence.update({'negative_vector': list(map(enc, v)), 'negative_value': enc(value)})
            count_matrices += 1
            matrices.append(evidence)
        reconstructed.append({'atoms': list(atoms), 'triples': triple_evidence, 'matrices': matrices})
    counts = {'feasible_atoms': len(atom_vectors), 'matrices': count_matrices, 'principal_minors': count_minors,
              'zero_minors': zero_minors, 'singular_PSD': singular, 'nonPSD': len(negative)}
    check('all_aggregate_counts', counts == saved['counts'] and count_matrices == 4*len(atom_vectors)
          and count_minors == 60*len(atom_vectors) and negative == sorted(saved['negative_record_anchors']))
    check('verdict_matches_evidence', saved['verdict'] == ('FAIL' if negative else 'PASS'))
    if minimum_pivot_ratio is not None:
        minimum_pivot_ratio['value'] = enc(minimum_pivot_ratio['value'])
    result = {'source_sha256': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checks': checks, 'failures': failures, 'coverage': counts,
              'intersection_boxes': [[r.start, r.stop-1] for r in boxes],
              'minimum_pivot_to_original_diagonal_ratio': minimum_pivot_ratio,
              'records': reconstructed, 'verdict': 'INVALID' if failures else 'VERIFIED_FAIL' if negative else 'VERIFIED_PASS'}
    OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print('Verdict:', result['verdict'], '; checks:', checks, '; failures:', len(failures))
    print('Independent counts:', counts)
    print('Actual/required: matrices', count_matrices, '/', 4*len(atom_vectors),
          '; minors', count_minors, '/', 60*len(atom_vectors))
    if minimum_pivot_ratio is not None:
        print('Smallest pivot/original-diagonal ratio:', F(*minimum_pivot_ratio['value']),
              '; required PSD bound: >=0; zero pivots:', singular)
    print('Certificate:', OUT.relative_to(NB))
    assert not failures, failures


if __name__ == '__main__':
    main()

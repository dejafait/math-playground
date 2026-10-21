#!/usr/bin/env python3
"""Approved fixed moments: full atoms, four anchors, exact minor/congruence evidence."""
import hashlib
import itertools as it
import json
import re
from fractions import Fraction as Q
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'seven-distance-principals-results.json'
DISTANCES = [5, 5, 7, 6, 5, 5]


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def determinant(matrix):
    n = len(matrix)
    answer = Q(0)
    for perm in it.permutations(range(n)):
        term = Q((-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n)))
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        answer += term
    return answer


def part(weights, pairs, triple, capacity):
    u, v, w = weights
    a, b, c = pairs
    h = triple
    return [capacity-u-v-w+a+b+c-h, u-a-b+h, v-a-c+h,
            a-h, w-b-c+h, b-h, c-h, h]


def diagonalize(matrix):
    columns = [[Q(i == j) for i in range(4)] for j in range(4)]
    def bil(v, w):
        return sum(v[i]*matrix[i][j]*w[j] for i in range(4) for j in range(4))
    pivots = []
    for k in range(4):
        pivot = bil(columns[k], columns[k])
        pivots.append(enc(pivot))
        if pivot < 0:
            return {'PSD': False, 'pivots': pivots,
                    'negative_vector': list(map(enc, columns[k])), 'negative_value': enc(pivot)}
        if pivot == 0:
            for j in range(k+1, 4):
                b = bil(columns[k], columns[j])
                if b:
                    t = -b/(abs(bil(columns[j], columns[j]))+1)
                    v = [x+t*y for x, y in zip(columns[k], columns[j])]
                    return {'PSD': False, 'pivots': pivots,
                            'negative_vector': list(map(enc, v)), 'negative_value': enc(bil(v, v))}
        else:
            for j in range(k+1, 4):
                t = bil(columns[k], columns[j])/pivot
                columns[j] = [x-t*y for x, y in zip(columns[j], columns[k])]
    return {'PSD': True, 'pivots': pivots,
            'congruence_columns': [list(map(enc, v)) for v in columns],
            'congruence_diagonal_matrix': [[enc(bil(v, w)) for w in columns] for v in columns]}


def main():
    paths = [NB/'lemmas/L056-released-zero-five-shell-nonexclusion.md',
             ROOT/'delsarte-lp-results.json', ROOT/'released-zero-five-shell-results.json',
             ROOT/'simultaneous-shell-ordinary-scalars-results.json']
    z = {(int(r), int(q)): Q(value) for r, q, value in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', paths[0].read_text(), re.M)}
    lp, released, scalar = [json.loads(path.read_text()) for path in paths[1:]]
    p = [Q(1)]+[Q(0)]*4+[Q(v['numerator'], v['denominator'])/(2*comb(68, i)*comb(956, i))
                         for i, v in enumerate(lp['exact']['primal'], 5)]
    rho = (Q(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    d = {(r, q): value/(comb(5, r)*comb(63, r)*comb(5, q)*comb(951, q))
         for (r, q), value in z.items()}
    checks = 0
    errors = []
    def check(name, condition, where=None):
        nonlocal checks
        checks += 1
        if not condition:
            errors.append({'check': name, 'where': where})
    check('canonical_21_coefficients', list(z) == [(r, q) for r in range(6) for q in range(6) if r+q >= 5]
          and list(map(enc, z.values())) == released['exact']['primal'])
    check('all_original_pairs', len(p) == 69 and list(map(enc, p)) == released['parameters']['p']
          and list(map(enc, p[:13])) == scalar['pairs_through_12'])
    check('positive_unchanged_rho', rho > 0 and enc(rho) == scalar['rho'])
    check('canonical_inputs_valid', not lp['failures'] and not scalar['failures'])
    # L062 keys use A,B,C as bits 4,2,1 and take the lexicographic
    # minimum over all six support orders.
    dictionary = {}
    for row in scalar['types']:
        key = min(tuple(item['atoms']) for item in row['presentations'])
        value = Q(*row['y'])
        check('L062_unordered_consistency', key not in dictionary or dictionary[key] == value, row['type'])
        dictionary[key] = value
    records, negative, seen = [], [], set()
    minor_count = zero_minors = singular = 0
    for a, b, c in it.product(range(5), range(2, 6), range(2, 6)):
        A, B, C = 4-a, 7-b, 7-c
        for h in range(max(0, a+b-5, a+c-5, b+c-7), min(a, b, c)+1):
            for H in range(max(0, A+B-5, A+C-5, B+C-7), min(A, B, C)+1):
                tag = [a, b, c, h, H]
                inside = part((5, 5, 7), (a, b, c), h, 68)
                outside = part((5, 5, 7), (A, B, C), H, 956)
                check('nonnegative_partitions', min(inside+outside) >= 0, tag)
                atoms = [0]*16
                for mask in range(8):
                    atoms[1|((7^mask)<<1)] = inside[mask]
                    atoms[mask<<1] = outside[mask]
                check('distinct_atom_vector', tuple(atoms) not in seen, tag)
                seen.add(tuple(atoms))
                supports = [set() for _ in range(4)]
                cursor = 0
                for mask, count in enumerate(atoms):
                    for j in range(4):
                        if mask & (1 << j):
                            supports[j].update(range(cursor, cursor+count))
                    cursor += count
                check('ground_and_weights', cursor == 1024 and all(len(S) == 68 for S in supports), tag)
                distances = [len(supports[i]-supports[j]) for i, j in it.combinations(range(4), 2)]
                check('six_fixed_distances', distances == DISTANCES, tag)
                triples = {}
                for ids in it.combinations(range(4), 3):
                    presentations, values = [], []
                    for order in it.permutations(ids):
                        S, T, W = [supports[i] for i in order]
                        region = [sum(4*(x in S)+2*(x in T)+(x in W) == mask
                                      for x in range(1024)) for mask in range(8)]
                        eligible = len(S-T) == len(S-W) == 5
                        item = {'order': list(order), 'atoms_4_2_1': region, 'eligible': eligible}
                        if eligible:
                            r = 63-len(S&T&W)
                            q = len(T-W)-r
                            check('represented_relation', (r, q) in d, [tag, order])
                            direct = [len(S-(T|W)), len((S&W)-T), len((S&T)-W), len(S&T&W),
                                      len((T&W)-S), len(T-(S|W)), len(W-(S|T)), 1024-len(S|T|W)]
                            check('full_L056_regions', direct == [5-r, r, r, 63-r, 5-q, q, q, 951-q], [tag, order])
                            item['relation'] = [r, q]
                            values.append(p[5]*d[r, q])
                        presentations.append(item)
                    key = min(tuple(item['atoms_4_2_1']) for item in presentations)
                    check('represented_eligible_orders', len(values) == 2 and len(set(values)) == 1, [tag, ids])
                    if not values:
                        raise ValueError('Unrepresented triple; no extension permitted')
                    check('exact_L062_unordered_moment', key in dictionary and dictionary[key] == values[0], [tag, ids])
                    triples[','.join(map(str, ids))] = {'presentations': presentations,
                         'unordered_key': list(key), 'moment_over_rho': enc(values[0])}
                def moment(ids):
                    if len(ids) == 1:
                        return Q(1)
                    if len(ids) == 2:
                        i, j = sorted(ids)
                        return p[len(supports[i]-supports[j])]
                    return Q(*triples[','.join(map(str, sorted(ids)))]['moment_over_rho'])
                matrices = []
                for anchor in range(4):
                    families = [frozenset([anchor])]+[frozenset([anchor, j]) for j in range(4) if j != anchor]
                    K = [[moment(I|J) for J in families] for I in families]
                    minors = []
                    for size in range(1, 5):
                        for subset in it.combinations(range(4), size):
                            value = determinant([[K[i][j] for j in subset] for i in subset])
                            minors.append({'indices': list(subset), 'value': enc(value)})
                            minor_count += 1
                            zero_minors += value == 0
                    evidence = diagonalize(K)
                    check('all_minors_congruence_agree', evidence['PSD'] == all(Q(*m['value']) >= 0 for m in minors), [tag, anchor])
                    if not evidence['PSD']:
                        check('strict_negative_witness', Q(*evidence['negative_value']) < 0, [tag, anchor])
                        negative.append([len(records), anchor])
                    else:
                        singular += any(Q(*v) == 0 for v in evidence['pivots'])
                    matrices.append({'anchor': anchor, 'indices': [sorted(I) for I in families],
                        'matrix_over_rho': [list(map(enc, row)) for row in K],
                        'principal_minors_over_rho': minors, **evidence})
                records.append({'parameters': tag, 'atoms_by_D_E_F_G_bitmask': atoms,
                                'distances': distances, 'triples': triples, 'matrices': matrices})
    check('coverage_totals', len(records) == len(seen) and minor_count == 60*len(records))
    result = {'scope': 'Exactly (5,5,7,6,5,5); unchanged L062; all sixteen atoms and four anchors.',
        'source_sha256': {str(path.relative_to(NB)): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
        'normalization': {'rho': enc(rho), 'pairs': list(map(enc, p))},
        'counts': {'feasible_atoms': len(records), 'matrices': 4*len(records), 'principal_minors': minor_count,
                   'zero_minors': zero_minors, 'singular_PSD': singular, 'nonPSD': len(negative)},
        'checks': checks, 'errors': errors, 'negative_record_anchors': negative, 'records': records,
        'verdict': 'INVALID' if errors else 'FAIL' if negative else 'PASS'}
    OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print('Verdict:', result['verdict'], '; checks:', checks, '; errors:', len(errors))
    print('Actual/required: matrices', 4*len(records), '/', 4*len(seen),
          '; minors', minor_count, '/', 60*len(seen))
    print('Counts:', result['counts'], '; p7:', p[7])
    if negative:
        print('First negative record/anchor:', negative[0])
    print('Certificate:', OUT.relative_to(NB))
    assert not errors, errors


if __name__ == '__main__':
    main()

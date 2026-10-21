#!/usr/bin/env python3
"""Step 192: complete L058 manuscript/certificate audit; no notebook imports."""
import hashlib
import itertools as it
import json
import re
from fractions import Fraction as Q
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'released-zero-four-index-critical-audit-results.json'


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def determinant(a):
    # Laplace recursion, independent of both saved determinant algorithms.
    if not a:
        return Q(1)
    return sum((-1)**j * a[0][j] * determinant(
        [row[:j] + row[j+1:] for row in a[1:]]) for j in range(len(a)))


def main():
    paths = [ROOT/'released-zero-four-index-results.json',
             ROOT/'released-zero-four-index-verification.json',
             NB/'lemmas/L056-released-zero-five-shell-nonexclusion.md',
             ROOT/'released-zero-five-shell-results.json']
    original, verification = [json.loads(p.read_text()) for p in paths[:2]]
    z = {(int(r), int(q)): Q(v) for r, q, v in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', paths[2].read_text(), re.M)}
    released = json.loads(paths[3].read_text())
    p5, p6 = Q(1, 68881143660), Q(133, 9357995374380)
    rho = (Q(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    failures, records = [], []
    checks = 0

    def check(name, condition, location=None):
        nonlocal checks
        checks += 1
        if not condition:
            failures.append({'name': name, 'location': location})

    for certificate in (original, verification):
        check('complete_source_hashes', all(
            hashlib.sha256((NB/p).read_bytes()).hexdigest() == h
            for p, h in certificate['source_sha256'].items()))
    check('all_21_manuscript_coefficients',
          set(z) == {(r, q) for r in range(6) for q in range(6) if r+q >= 5}
          and [enc(z[key]) for key in sorted(z)] == released['exact']['primal'])
    check('positive_actual_normalization', rho > 0 and original['normalization'] ==
          {'rho': enc(rho), 'p5': enc(p5), 'p6': enc(p6)})

    # Loose ranges, with all eight atom inequalities tested on each part.
    # This tests the manuscript's tightened inclusive bounds independently.
    enumeration = {}
    for a, b, c, h, tail in it.product(range(6), range(6), range(6), range(6), range(6)):
        def cells(ab, ac, bc, t, capacity):
            # Intersections of X_E,X_F,X_G or Y_E,Y_F,Y_G.
            f = [capacity, 5, 5, ab, 6, ac, bc, t]
            return [sum((-1)**(u.bit_count()-s.bit_count())*f[u]
                        for u in range(8) if u & s == s) for s in range(8)]
        inside = cells(a, b, c, h, 68)
        outside = cells(5-a, 6-b, 6-c, tail, 956)
        if min(inside+outside) < 0:
            continue
        atoms = [0]*16
        for s in range(8):
            atoms[1+2*(7-s)] = inside[s]
            atoms[2*s] = outside[s]
        params = (a, b, c, h, tail)
        check('tight_ranges_match', 1 <= b <= 5 and 1 <= c <= 5 and
              max(0, a+b-5, a+c-5, b+c-6) <= h <= min(a,b,c) and
              max(0, 6-a-b, 6-a-c, 6-b-c) <= tail <= min(5-a,6-b,6-c), params)
        enumeration[params] = tuple(atoms)
    originals = {tuple(r['parameters']): r for r in original['records']}
    verified = {tuple(r['atoms']): r for r in verification['records']}
    check('all_parameters_and_all_atoms', len(enumeration) == len(originals) ==
          len(original['records']) == len(verified) == len(verification['records']) == 150
          and set(enumeration) == set(originals) and set(enumeration.values()) == set(verified))
    all_minors, all_pivots, det_transforms = [], [], []
    for params, atoms in sorted(enumeration.items()):
        old = originals[params]
        prior = verified[atoms]
        check('all_16_atoms', tuple(old['atoms_by_D_E_F_G_bitmask']) == atoms, params)
        # Marginalize the 16 atoms, without building point-set representatives.
        def intersection(mask):
            return sum(atoms[t] for t in range(16) if t & mask == mask)
        check('all_intersections', intersection(0) == 1024 and
              all(intersection(1 << i) == 68 for i in range(4)) and
              [68-intersection((1 << i)|(1 << j)) for i,j in it.combinations(range(4),2)]
              == [5,5,6,5,5,5], params)
        triple_values, triple_evidence = {}, []
        for ids in [(0,1,2), (0,1,3), (0,2,3)]:
            values, eligible = [], set()
            for order in it.permutations(ids):
                anchor, b, c = order
                regions = [0]*8
                for mask, count in enumerate(atoms):
                    bits = tuple((mask >> i) & 1 for i in order)
                    index = [(1,0,0),(1,0,1),(1,1,0),(1,1,1),
                             (0,1,1),(0,1,0),(0,0,1),(0,0,0)].index(bits)
                    regions[index] += count
                if 68-intersection((1<<anchor)|(1<<b)) != 5 or \
                   68-intersection((1<<anchor)|(1<<c)) != 5:
                    continue
                eligible.add(anchor)
                r, q = 63-regions[3], 5-regions[4]
                check('full_permuted_triple_regions',
                      regions == [5-r,r,r,63-r,5-q,q,q,951-q] and (r,q) in z,
                      [params, order])
                value = p5*z[r,q]/(comb(5,r)*comb(63,r)*comb(5,q)*comb(951,q))
                values.append(value)
                triple_evidence.append({'order': order, 'regions': regions,
                                        'relation': [r,q], 'value': enc(value)})
            expected = {0,1,2} if ids == (0,1,2) else {1} if ids == (0,1,3) else {2}
            check('all_eligible_anchor_values', eligible == expected and len(set(values)) == 1 and
                  old['triples'][','.join(map(str,ids))]['moment_over_rho'] == enc(values[0]),
                  [params, ids])
            triple_values[ids] = values[0]
        x,y,z3 = [triple_values[ids] for ids in [(0,1,2),(0,1,3),(0,2,3)]]
        matrix = [[Q(1),p5,p5,p6],[p5,p5,x,y],[p5,x,p5,z3],[p6,y,z3,p6]]
        encoded = [[enc(v) for v in row] for row in matrix]
        check('both_complete_saved_matrices', old['matrix_over_rho'] == prior['matrix_over_rho'] == encoded, params)
        minors = []
        for size in range(1,5):
            for ids in it.combinations(range(4),size):
                value = determinant([[matrix[i][j] for j in ids] for i in ids])
                check('strict_principal_minor', value > 0, [params,ids])
                all_minors.append(value)
                minors.append({'indices': list(ids), 'value': enc(value)})
        check('both_complete_minor_certificates',
              minors == old['principal_minors_over_rho'] == prior['minors'], params)
        columns = [[Q(*x) for x in col] for col in old['congruence_columns']]
        check('congruence_shape', len(columns) == 4 and all(len(c) == 4 for c in columns), params)
        det_t = determinant(columns)
        check('invertible_congruence', det_t != 0, params)
        det_transforms.append(det_t)
        diagonal = []
        complete = []
        for i in range(4):
            row = []
            for j in range(4):
                value = sum(columns[i][a]*matrix[a][b]*columns[j][b]
                            for a in range(4) for b in range(4))
                check('every_congruence_entry', enc(value) == old['congruence_diagonal_matrix'][i][j]
                      and (value > 0 if i == j else value == 0), [params,i,j])
                row.append(enc(value))
                if i == j:
                    diagonal.append(value)
            complete.append(row)
        check('every_pivot_both_certificates',
              list(map(enc,diagonal)) == old['pivots'] == prior['congruence_pivots'], params)
        product = Q(1)
        for v in diagonal:
            product *= v
        check('determinant_congruence_identity', determinant(matrix)*det_t**2 == product, params)
        all_pivots.extend(diagonal)
        records.append({'parameters': params, 'atoms': atoms, 'triples': triple_evidence,
                        'matrix': encoded, 'minors': minors, 'det_T': enc(det_t),
                        'congruence': complete})
    check('all_required_evidence', len(records) == 150 and len(all_minors) == 2250 and len(all_pivots) == 600)
    result = {'source_sha256': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checks': checks, 'failures': failures,
              'coverage': {'atoms': len(records), 'minors': len(all_minors),
                           'congruence_entries': 16*len(records), 'positive_pivots': len(all_pivots)},
              'minimum_minor': enc(min(all_minors)), 'minimum_pivot': enc(min(all_pivots)),
              'transform_determinants': sorted(set(map(str,det_transforms))),
              'records': records, 'verdict': 'RETAIN' if not failures else 'INVALID'}
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Verdict:',result['verdict'],'checks:',checks,'failures:',len(failures))
    print('Actual/required: atoms',len(records),'/150; minors',len(all_minors),
          '/2250; congruence entries',16*len(records),'/2400; positive pivots',len(all_pivots),'/600')
    print('All minors and pivots strictly > required 0:',min(all_minors)>0 and min(all_pivots)>0)
    print('Full certificate:',OUT)
    assert not failures, failures


if __name__ == '__main__':
    main()

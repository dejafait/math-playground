#!/usr/bin/env python3
"""L064 audit: broader boxes, manuscript matrices, fraction-free minors.

Consumes both complete certificates; imports no notebook routines.
"""
import hashlib
import itertools as it
import json
import re
from fractions import Fraction as Q
from math import comb, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
NB = HERE.parent.parent
OUT = HERE / 'seven-distance-principals-critical-audit.json'


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def det(a):
    """Clear row denominators; integer Bareiss, exact divisions checked."""
    scale = [lcm(*(Q(x).denominator for x in row)) for row in a]
    b = [[int(Q(x)*s) for x in row] for s, row in zip(scale, a)]
    divisor, sign = 1, 1
    for k in range(len(b)-1):
        pivot = next((i for i in range(k, len(b)) if b[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            b[k], b[pivot] = b[pivot], b[k]
            sign = -sign
        for i in range(k+1, len(b)):
            for j in range(k+1, len(b)):
                numerator = b[k][k]*b[i][j]-b[i][k]*b[k][j]
                assert numerator % divisor == 0
                b[i][j] = numerator//divisor
        divisor = b[k][k]
        for i in range(k+1, len(b)):
            b[i][k] = 0
    answer = Q(sign*b[-1][-1])
    for s in scale:
        answer /= s
    return answer


def main():
    names = ['scripts/finite-support/seven-distance-principals-results.json',
             'scripts/finite-support/seven-distance-principals-verification.json',
             'scripts/finite-support/simultaneous-shell-ordinary-scalars-results.json',
             'scripts/finite-support/delsarte-lp-results.json',
             'lemmas/L056-released-zero-five-shell-nonexclusion.md']
    paths = [NB/name for name in names]
    old, verified, scalar, lp = [json.loads(p.read_text()) for p in paths[:4]]
    z = {(int(r), int(q)): Q(v) for r, q, v in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', paths[4].read_text(), re.M)}
    checks, failures, records = 0, [], []

    def check(name, condition, at=None):
        nonlocal checks
        checks += 1
        if not condition:
            failures.append({'check': name, 'at': at})

    for data in (old, verified):
        check('source_hashes', all(hashlib.sha256((NB/p).read_bytes()).hexdigest() == h
                                  for p, h in data['source_sha256'].items()))
    check('saved_failure_lists', not old['errors'] and not verified['failures'])
    a = [Q(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    pairs = [Q(1)]+[Q(0)]*4+[v/(2*comb(68, i)*comb(956, i)) for i, v in enumerate(a, 5)]
    rho = (Q(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    check('positive_original_normalization', rho > 0 and old['normalization'] ==
          {'rho': enc(rho), 'pairs': list(map(enc, pairs))})
    check('manuscript_pairs', pairs[5:8] == [Q(1, 68881143660), Q(133, 9357995374380),
                                           Q(3539, 248922676958508)])
    check('L062_normalization', scalar['rho'] == enc(rho)
          and scalar['pairs_through_12'] == list(map(enc, pairs[:13])))
    # Import L021's unique-system specification; verify the complete defining equations.
    def choose(n, k):
        return comb(n, k) if 0 <= k <= n else 0
    for j in range(1, 65):
        row = [Q(sum((-1)**h*choose(j, h)*choose(68-j, i-h)*choose(956-j, i-h)
                     for h in range(i+1)), comb(68, i)*comb(956, i)) for i in range(5, 69)]
        check('L021_defining_equation', sum(x*y for x, y in zip(row, a)) == -1, j)
    check('canonical_z_domain', set(z) == {(r, q) for r in range(6) for q in range(6) if r+q >= 5})
    dictionary = {}
    for row in scalar['types']:
        key = min(tuple(p['atoms']) for p in row['presentations'])
        value = Q(*row['y'])
        check('existing_dictionary_consistency', key not in dictionary or dictionary[key] == value)
        dictionary[key] = value

    # Deliberately broader pair/triple ranges than the manuscript: all
    # intersections involving a five-set are between zero and five.
    def invert(f, bits):
        return tuple(sum((-1)**((t ^ s).bit_count())*f[t]
                         for t in range(1 << bits) if (t & s) == s)
                     for s in range(1 << bits))
    removed, restricted = {}, {}
    for a0, b, c, h, H in it.product(range(6), repeat=5):
        inside = invert([68, 5, 5, a0, 7, b, c, h], 3)
        outside = invert([956, 5, 5, 4-a0, 7, 7-b, 7-c, H], 3)
        A, B, C = 4-a0, 7-b, 7-c
        allowed = (0 <= a0 <= 4 and 2 <= b <= 5 and 2 <= c <= 5
                   and max(0, a0+b-5, a0+c-5, b+c-7) <= h <= min(a0, b, c)
                   and max(0, A+B-5, A+C-5, B+C-7) <= H <= min(A, B, C))
        feasible = min(inside+outside) >= 0
        check('restricted_box_iff_all_atoms_nonnegative', allowed == feasible, [a0,b,c,h,H])
        if not feasible:
            continue
        atoms = [0]*16
        for s in range(8):
            atoms[1+2*(7-s)] = inside[s]
            atoms[2*s] = outside[s]
        key = tuple(atoms)
        check('removed_added_injective', key not in removed)
        removed[key] = [a0,b,c,h,H]
        restricted[key] = allowed
    fixed = {0:1024, 1:68, 2:68, 4:68, 8:68, 3:63, 5:63, 9:61, 6:62, 10:63, 12:63}
    triple_masks = [7,11,13,14]
    bounds = []
    for mask in triple_masks:
        bits = [1 << i for i in range(4) if mask & (1 << i)]
        bounds.append((max(fixed[i|j]+fixed[i|k]-68 for i,j,k in it.permutations(bits)),
                       min(fixed[i|j] for i,j in it.combinations(bits,2))))
    bounds.append((68-5-5-7, 68-7))
    check('manuscript_intersection_bounds', bounds == [(58,62),(58,61),(58,61),(58,62),(51,61)])
    intersections = {}
    for values in it.product(*(range(lo,hi+1) for lo,hi in bounds)):
        f = dict(fixed)
        f.update(zip(triple_masks+[15], values))
        atoms = invert(f, 4)
        if min(atoms) < 0:
            continue
        check('all_sixteen_inverse_intersections', all(sum(atoms[t] for t in range(16)
              if (t&s) == s) == f[s] for s in range(16)), values)
        check('intersection_enumeration_injective', atoms not in intersections)
        intersections[atoms] = values
    old_rows = {tuple(r['atoms_by_D_E_F_G_bitmask']): r for r in old['records']}
    ver_rows = {tuple(r['atoms']): r for r in verified['records']}
    check('both_certificates_complete_no_duplicates', len(old_rows) == len(old['records']) ==
          len(ver_rows) == len(verified['records']) == 110 and
          set(old_rows) == set(ver_rows) == set(removed) == set(intersections))
    subsets = [list(s) for size in range(1,5) for s in it.combinations(range(4),size)]
    total_minors, total_entries = 0, 0
    min_ratio = Q(1)
    for atoms in sorted(removed):
        o, v = old_rows[atoms], ver_rows[atoms]
        check('saved_parameters', removed[atoms] == o['parameters'])
        # Literal finite set representatives independently realize all atoms.
        supports = [set() for _ in range(4)]
        cursor = 0
        for mask, size in enumerate(atoms):
            for j in range(4):
                if mask & (1 << j):
                    supports[j].update(range(cursor,cursor+size))
            cursor += size
        distances = [len(supports[i]-supports[j]) for i,j in it.combinations(range(4),2)]
        check('converse_ground_sizes_distances', cursor == 1024 and all(len(s)==68 for s in supports)
              and distances == o['distances'] == [5,5,7,6,5,5])
        ys, triples = [], {}
        for ids in it.combinations(range(4),3):
            name = ','.join(map(str,ids))
            presentations, vals = [], []
            for order in it.permutations(ids):
                S,T,W = [supports[j] for j in order]
                region = [sum(4*(x in S)+2*(x in T)+(x in W) == m for x in range(1024)) for m in range(8)]
                eligible = len(S-T) == len(S-W) == 5
                item = {'order':list(order), 'atoms_4_2_1':region, 'eligible':eligible}
                if eligible:
                    r, q = 63-len(S&T&W), len(T-W)-(63-len(S&T&W))
                    check('manuscript_full_regions', region == [951-q,q,q,5-q,5-r,r,r,63-r])
                    item['relation'] = [r,q]
                    vals.append(pairs[5]*z[r,q]/(comb(5,r)*comb(63,r)*comb(5,q)*comb(951,q)))
                presentations.append(item)
            key = min(tuple(p['atoms_4_2_1']) for p in presentations)
            check('all_six_presentations_both_certificates', presentations == o['triples'][name]['presentations']
                  == v['triples'][name]['presentations'])
            check('unchanged_unordered_value', len(vals) == 2 and vals[0] == vals[1] == dictionary[key]
                  and list(key) == o['triples'][name]['unordered_key']
                  and enc(vals[0]) == o['triples'][name]['moment_over_rho'] == v['triples'][name]['y'])
            ys.append(vals[0])
            triples[frozenset(ids)] = vals[0]
        y1,y2,y3,y4 = ys
        p5,p6,p7 = pairs[5:8]
        matrices = [
            [[1,p5,p5,p7],[p5,p5,y1,y2],[p5,y1,p5,y3],[p7,y2,y3,p7]],
            [[1,p5,p6,p5],[p5,p5,y1,y2],[p6,y1,p6,y4],[p5,y2,y4,p5]],
            [[1,p5,p6,p5],[p5,p5,y1,y3],[p6,y1,p6,y4],[p5,y3,y4,p5]],
            [[1,p7,p5,p5],[p7,p7,y2,y3],[p5,y2,p5,y4],[p5,y3,y4,p5]]]
        check('both_four_anchors', [m['anchor'] for m in o['matrices']] ==
              [m['anchor'] for m in v['matrices']] == [0,1,2,3])
        audit_matrices = []
        for anchor,K in enumerate(matrices):
            so,sv = o['matrices'][anchor],v['matrices'][anchor]
            families = [frozenset([anchor])]+[frozenset([anchor,j]) for j in range(4) if j != anchor]
            def moment(family):
                if len(family) == 1:
                    return Q(1)
                if len(family) == 2:
                    i,j = sorted(family)
                    return pairs[len(supports[i]-supports[j])]
                assert len(family) == 3
                return triples[family]
            check('manuscript_all_boolean_union_entries', K == [[moment(I|J) for J in families] for I in families]
                  and so['indices'] == [sorted(I) for I in families])
            encoded = [list(map(enc,row)) for row in K]
            check('both_saved_matrices', so['matrix_over_rho'] == sv['matrix_over_rho'] == encoded)
            check('both_complete_minor_indices', [m['indices'] for m in so['principal_minors_over_rho']] ==
                  [m['indices'] for m in sv['minors']] == subsets)
            minors = []
            for subset,mo,mv in zip(subsets,so['principal_minors_over_rho'],sv['minors']):
                d = det([[K[i][j] for j in subset] for i in subset])
                check('both_exact_Bareiss_minors_strictly_positive', d > 0 and enc(d) == mo['value'] == mv['value'], [removed[atoms],anchor,subset])
                minors.append({'indices':subset,'value':enc(d)})
                total_minors += 1
            columns = [[Q(*x) for x in col] for col in so['congruence_columns']]
            check('both_congruence_columns', so['congruence_columns'] == sv['congruence_columns'])
            determinant = det(columns)
            check('invertible_unit_triangular_congruence', determinant == 1 and all(columns[j][j] == 1
                  and all(columns[j][i] == 0 for i in range(j+1,4)) for j in range(4)))
            diagonal = [[sum(columns[i][r]*K[r][s]*columns[j][s] for r,s in it.product(range(4),repeat=2))
                         for j in range(4)] for i in range(4)]
            check('both_full_congruence_results', [list(map(enc,row)) for row in diagonal] ==
                  so['congruence_diagonal_matrix'] == sv['diagonal'])
            for i,j in it.product(range(4),repeat=2):
                check('each_exact_congruence_entry', diagonal[i][j] == (Q(*so['pivots'][i]) if i == j else 0), [removed[atoms],anchor,i,j])
                total_entries += 1
            check('strictly_positive_pivots', all(diagonal[i][i] > 0 for i in range(4)))
            check('determinant_congruence_identity', det(K)*determinant**2 ==
                  diagonal[0][0]*diagonal[1][1]*diagonal[2][2]*diagonal[3][3])
            min_ratio = min(min_ratio, *(diagonal[i][i]/K[i][i] for i in range(4)))
            audit_matrices.append({'anchor':anchor,'matrix':encoded,'minors':minors,
                                   'congruence_determinant':enc(determinant),
                                   'congruence': [list(map(enc,row)) for row in diagonal]})
        records.append({'atoms':list(atoms),'removed_parameters':removed[atoms],
                        'intersection_parameters':list(intersections[atoms]),
                        'triple_values':list(map(enc,ys)), 'matrices':audit_matrices})
    counts = {'feasible_atoms':110,'matrices':440,'principal_minors':6600,
              'zero_minors':0,'singular_PSD':0,'nonPSD':0}
    check('all_aggregate_claims', counts == old['counts'] == verified['coverage'] and
          total_minors == 6600 and total_entries == 7040 and old['verdict'] == 'PASS'
          and verified['verdict'] == 'VERIFIED_PASS')
    check('saved_minimum_pivot_ratio', enc(min_ratio) == verified['minimum_pivot_to_original_diagonal_ratio']['value'])
    report = {'source_sha256':{name:hashlib.sha256(path.read_bytes()).hexdigest() for name,path in zip(names,paths)},
              'checks':checks,'failures':failures,'counts':counts,
              'broad_box_candidates':6**5,'intersection_box_candidates':4400,
              'exact_congruence_entries':total_entries,'minimum_pivot_ratio':enc(min_ratio),
              'records':records,'verdict':'INVALID' if failures else 'RETAIN_L064'}
    OUT.write_text(json.dumps(report,separators=(',',':'))+'\n')
    print('Verdict:',report['verdict'],'; checks:',checks,'; failures:',len(failures))
    print('Actual/required: cases',len(records),'/110; matrices',4*len(records),'/440; minors',total_minors,'/6600; congruence entries',total_entries,'/7040')
    print('Positive pivots; minimum pivot/diagonal:',min_ratio,'; required >0')
    print('Certificate:',OUT.relative_to(NB))
    assert not failures, failures


if __name__ == '__main__':
    main()

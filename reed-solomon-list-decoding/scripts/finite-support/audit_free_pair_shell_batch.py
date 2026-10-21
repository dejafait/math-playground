"""Separate L097 audit: actual-set reanchoring, row coverage, all minors.

No generator/verifier mathematics is imported. The separately replayed
source verifier supplies the full literal-beta/congruence reconstruction;
this challenges its orbit and PSD interpretations by different operations.
"""
import hashlib
import json
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb, lcm
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / 'free-pair-shell-batch-critical-audit.json'


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def segment(start, size):
    return ((1 << size) - 1) << start


def representative(i, j, t, s):
    # X has weight 68. Removed sets have sizes i,j and intersection t;
    # added sets have sizes i,j and intersection s on its complement.
    x = segment(0, 68)
    r1 = segment(0, i)
    r2 = segment(0, t) | segment(i, j-t)
    a1 = segment(68, i)
    a2 = segment(68, s) | segment(68+i, j-s)
    return x, (x ^ r1) | a1, (x ^ r2) | a2


def orbit(x, y, z):
    return ((x & ~y).bit_count(), (x & ~z).bit_count(),
            (x & ~y & ~z).bit_count(), (~x & y & z).bit_count())


def det_integer(a):
    # Leibniz formula, independent of either stored elimination.
    total = 0
    n = len(a)
    for perm in permutations(range(n)):
        term = (-1) ** sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        for i in range(n):
            term *= a[i][perm[i]]
        total += term
    return total


def main():
    names = ['free-pair-shell-batch-results.json',
             'free-pair-shell-batch-critical-source-verification.json',
             'selected-triple-sdp-results.json']
    data, replay, old = [json.loads((BASE / name).read_text()) for name in names]
    failures = []
    counts = {}

    def check(test, label):
        counts[label.split(':')[0]] = counts.get(label.split(':')[0], 0) + 1
        if not test:
            failures.append(label)

    check(replay['verified'] and replay['failures'] == [], 'complete source replay')
    p = [F(*x) for x in data['p']]
    check(p == [F(*x) for x in old['p']], 'all old pairs')
    records = {tuple(r['key']): r for r in data['orbits']}
    for r in old['orbits']:
        check(records[tuple(r['key'])] == r, 'old orbit overlap:' + str(r['key']))
    row_map = {}
    for row in data['scalar_rows']:
        key = (tuple(row['key']), row['kind'], row.get('i'), row.get('j'))
        check(key not in row_map, 'distinct stored row:' + str(key))
        row_map[key] = F(*row['slack'])
    reanchor_records = []
    used_rows = set()
    repeated = forbidden = 0
    distinct_u = {}
    for key, record in records.items():
        value = F(*record['value'])
        closure = {tuple(o) for o in record['closure']}
        distinct_u.setdefault(key[:3], set()).add(key[3])
        for o in sorted(closure):
            i, j, t, s = o
            x, y, z = representative(*o)
            check(all(a.bit_count() == 68 and a.bit_length() <= 1024 for a in (x,y,z)),
                  'representative weights:' + str(o))
            check(orbit(x,y,z) == o, 'original actual orbit:' + str(o))
            presentations = [orbit(*abc) for abc in permutations((x,y,z))]
            check(set(presentations) == closure, 'actual reanchor closure:' + str(o))
            check(all(a+b-c-d in key[:3] and c-d == key[3]
                      and tuple(sorted((a,b,a+b-c-d))) == key[:3]
                      for a,b,c,d in presentations), 'actual source invariant:' + str(o))
            # Every original ordered scalar row must map to a retained row.
            for kind, a, b, slack in [('nonnegative',None,None,value),
                                      ('upper',i,j,p[i]-value),
                                      ('lower',i,j,1+value-p[i]-p[j])]:
                rk = (key,kind,a,b)
                used_rows.add(rk)
                check(rk in row_map and row_map[rk] == slack and slack >= 0,
                      'original scalar row:' + str((o,kind)))
            h = i+j-t-s
            if min(i,j,h) == 0:
                repeated += 1
                check(value == p[max(i,j,h)] and t == s, 'Boolean identity:' + str(o))
            if any(1 <= a <= 4 for a in (i,j,h)):
                forbidden += 1
                check(value == 0, 'forbidden identity:' + str(o))
            reanchor_records.append({'orbit':o,'six_actual_presentations':presentations})
    check(used_rows == set(row_map), 'scalar coverage both directions')
    multi_u = [dist for dist, us in distinct_u.items() if len(us)>1]
    check(len(multi_u)>0, 'distinct equal-valued source variables retained')
    expected_support = [(k,l,[i for i in range(69) if i in (5,6,7,8)
                             and k<=i<=68-k and l<=i<=956-l])
                        for k in range(9) for l in range(9)]
    expected_support[0] = (0,0,[0,5,6,7,8,68])
    expected_support += [(33,33,[33,34,35]),(34,34,[34])]
    check([(b['k'],b['l'],b['indices']) for b in data['blocks']] == expected_support,
          'entire ordered batch')
    minor_records = []
    positives = zeros = pivots_positive = pivots_zero = 0
    for b in data['blocks']:
        for family, entry in enumerate(b['families']):
            a = [[F(*v) for v in row] for row in entry['matrix']]
            n = len(a)
            check(all(a[i][j] == a[j][i] for i in range(n) for j in range(n)), 'matrix symmetry')
            denominator = lcm(*(v.denominator for row in a for v in row))
            ai = [[int(v*denominator) for v in row] for row in a]
            minors = []
            for size in range(1,n+1):
                for subset in combinations(range(n),size):
                    d = det_integer([[ai[i][j] for j in subset] for i in subset])
                    singular = (b['k'],b['l'],family)==(0,0,1) and 0 in subset
                    check(d == 0 if singular else d > 0,
                          'principal minor:' + str((b['k'],b['l'],family,subset)))
                    positives += d > 0
                    zeros += d == 0
                    minors.append({'indices':subset,'determinant':enc(F(d,denominator**size))})
            if (b['k'],b['l'],family)==(0,0,1):
                check(all(v==0 for v in a[0]), 'whole original zero row')
            diagonal = [F(*v) for v in entry['certificate']['diagonal']]
            pivots_positive += sum(v>0 for v in diagonal)
            pivots_zero += sum(v==0 for v in diagonal)
            minor_records.append({'k':b['k'],'l':b['l'],'family':family,'minors':minors})
    objective = sum(comb(68,i)*comb(956,i)*p[i] for i in range(69))
    threshold = F(65537**28,2**128)
    K = threshold.numerator//threshold.denominator
    U = F(comb(1024,64),comb(68,64))
    floor_m = objective.numerator//objective.denominator
    floor_excess = 2**128*floor_m-65537**28
    check(objective == (U+1)/2 and objective >= K+1 and floor_m > threshold,
          'exact integer obstruction')
    check(F(1383,1000)<objective/threshold<F(1384,1000), 'exact ratio endpoints')
    check(floor_excess == 278623344535004185563774417633448491259524856948687283912464936072396859308983357073255491132778317876968018526278791647748932648566783,
          'full manuscript integer')
    expected_counts = {'orbit_classes':7386,'permutation_closure':32151,
                       'retained_variables':7208,'scalar_rows':71688,'pair_rows':68,
                       'affine_coefficient_entries':42915,'PSD_families':166}
    check(all(replay['checks'][k]==v for k,v in expected_counts.items()), 'manuscript source counts')
    check(pivots_positive==471 and pivots_zero==1, 'manuscript pivot counts')
    check(data['construction']['distinct_triple_variables']==7144 and
          7144+64==7208<=20000 and 71688+68==71756<=200000, 'resource caps')
    result = {'verified':not failures,'failures':failures,'checks':counts,
              'input_sha256':{name:hashlib.sha256((BASE/name).read_bytes()).hexdigest() for name in names},
              'actual_reanchor_records':reanchor_records,'complete_principal_minors':minor_records,
              'summary':{'check_count':sum(counts.values()),'original_ordered_orbits':len(reanchor_records),
                         'actual_presentations':6*len(reanchor_records),'original_scalar_rows':3*len(reanchor_records),
                         'retained_scalar_rows':len(used_rows),'old_orbit_overlaps':len(old['orbits']),
                         'repeated_orbits':repeated,'forbidden_orbits':forbidden,
                         'distance_multisets_with_multiple_u':len(multi_u),
                         'positive_principal_minors':positives,'zero_principal_minors':zeros,
                         'objective':enc(objective),'threshold':enc(threshold),'K':K,
                         'objective_minus_K_plus_one':enc(objective-K-1),
                         'floor_scaled_excess':floor_excess,
                         'variables_actual_required':[7208,20000],
                         'rows_actual_required':[71756,200000]},
              'scope':'L097 exact selected free-pair support only; no solve, retuning, enlargement or full SDP claim'}
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Verified:',not failures,'; checks:',sum(counts.values()))
    print('All principal minors:',positives,'positive,',zeros,'zero; required nonnegative.')
    print('Variables 7208 <= 20000; rows 71756 <= 200000.')
    print('M/(threshold) in (1.383,1.384); M >= K+1:',objective>=K+1)
    print('Failures:',failures,'; complete certificate:',OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

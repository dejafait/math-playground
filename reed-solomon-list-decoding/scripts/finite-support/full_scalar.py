"""All actual ordered scalar orbits of the unchanged L022 extension.

Numerical caching does not identify orbit variables. Source ranges retain
every original (i,j,t,s); h_ids map only their rational evaluations.
"""
import json
import sys
from fractions import Fraction as F
from itertools import permutations
from math import comb, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).parent
OUT = BASE / 'full-scalar-results.json'
W, V = 68, 956


def enc(x):
    return [x.numerator, x.denominator]


def main():
    lp = json.loads((BASE / 'delsarte-lp-results.json').read_text())
    old = json.loads((BASE / 'selected-triple-sdp-results.json').read_text())
    p = [F(1)] + [F(0)] * 4 + [
        F(x['numerator'], x['denominator']) / (2 * comb(W, i) * comb(V, i))
        for i, x in zip(range(5, 69), lp['exact']['primal'])]
    assert len(p) == 69 and p[68] > 0
    D = lcm(*(x.denominator for x in p))
    A = [int(x * D) for x in p]
    H = D * D * A[68]
    P = [x * D * A[68] for x in A]  # P_i/H = p_i
    assert H > 0
    records, cache, entries, failures, violations = [], {}, [], [], []

    def record(i, j, h):
        a, b, c = key = tuple(sorted((i, j, h)))
        if key in cache:
            return cache[key]
        if any(1 <= x <= 4 for x in key):
            y = 0
        elif a == 0:
            assert b == c
            y = P[b]
        else:
            y = A[a] * A[b] * A[c]
        upper = [P[x] - y for x in key]
        lower = [H + y - P[x] - P[z] for x, z in ((a, b), (a, c), (b, c))]
        index = len(records)
        cache[key] = index
        # Slacks, all over H: y; upper indexed by distance position;
        # lower indexed by pairs (a,b),(a,c),(b,c).
        records.append({'distances': list(key), 'y': y, 'upper': upper, 'lower': lower})
        return index

    orbit_count = 0
    equality_count = 0
    forbidden_count = 0
    repeated_count = 0
    old_orbits = {tuple(o) for row in old['orbits'] for o in row['closure']}
    old_overlap = 0
    for i in range(69):
        for j in range(69):
            tl, th = max(0, i+j-W), min(i, j)
            sl, sh = max(0, i+j-V), min(i, j)
            hl, hh = i+j-th-sh, i+j-tl-sl
            ids = [record(i, j, h) for h in range(hl, hh+1)]
            entries.append({'i': i, 'j': j, 't_range': [tl, th],
                            's_range': [sl, sh], 'h_min': hl, 'h_ids': ids})
            for t in range(tl, th+1):
                for s in range(sl, sh+1):
                    h, u = i+j-t-s, t-s
                    row = records[ids[h-hl]]
                    y = row['y']
                    slacks = [y, P[i]-y, H+y-P[i]-P[j]]
                    for kind, slack in zip(('nonnegative', 'upper', 'lower'), slacks):
                        if slack < 0:
                            violations.append({'orbit': [i,j,t,s], 'kind': kind,
                                               'slack': enc(F(slack,H)), 'value': enc(F(y,H))})
                    if any(1 <= x <= 4 for x in (i,j,h)):
                        forbidden_count += 1
                        if y != 0:
                            failures.append(['forbidden', i,j,t,s])
                    if min(i,j,h) == 0:
                        repeated_count += 1
                        if u != 0:
                            failures.append(['repeated invariant', i,j,t,s])
                    for a,b,c in permutations((i,j,h)):
                        numer = a+b-c+u
                        tt, ss = numer//2, (a+b-c-u)//2
                        if numer % 2 or not (max(0,a+b-W) <= tt <= min(a,b)
                                            and max(0,a+b-V) <= ss <= min(a,b)):
                            failures.append(['permutation scope', i,j,t,s,a,b,c])
                        elif records[record(a,b,c)]['y'] != y:
                            failures.append(['permutation value', i,j,t,s,a,b,c])
                        equality_count += 1
                    orbit_count += 1
                    old_overlap += (i,j,t,s) in old_orbits
        if i % 16 == 0 or i == 68:
            print('Full ordered scalar construction through i =', i, flush=True)

    objective = sum(comb(W,i)*comb(V,i)*p[i] for i in range(69))
    threshold = F(65537**28, 2**128)
    result = {'stage': 'completed', 'parameters': {'n':1024,'w':W,'v':V,'d':10},
              'scope': 'all actual ordered scalar orbits; unchanged assignment; no PSD claim',
              'mapping': 'for original i,j,t,s take h=i+j-t-s and record h_ids[h-h_min]; t-s remains original',
              'p': list(map(enc,p)), 'pair_denominator':D, 'pair_numerators':A,
              'scalar_denominator':H, 'entries':entries, 'evaluation_records':records,
              'counts': {'ordered_entries':len(entries), 'actual_ordered_orbits':orbit_count,
                         'expanded_scalar_rows':3*orbit_count, 'permutation_checks':equality_count,
                         'forbidden_orbits':forbidden_count, 'repeated_orbits':repeated_count,
                         'numerical_cache_records':len(records), 'old_closure_orbits':old_overlap,
                         'new_ordered_orbits':orbit_count-old_overlap},
              'objective':enc(objective), 'required_threshold':enc(threshold),
              'ratio_milli_interval':[1383,1384],
              'violations':violations, 'failures':failures,
              'scalar_feasible':not violations and not failures and p[0]==1}
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Scalar feasible:',result['scalar_feasible'],'; counts:',result['counts'])
    print('Actual objective:',objective,'; required <=',threshold)
    print('Violations:',len(violations),'; implementation failures:',failures,'; certificate:',OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

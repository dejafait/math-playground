"""Independent occupancy enumeration and integer capacity comparisons.

Imports no construction routines and performs no nonlinear iteration.
The earlier root enclosure itself is an input, not critically re-audited here.
"""
import gzip
import hashlib
import json
import time
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
SOURCE = B/'enclosed-root-all-capacities.json.gz'
OUT = B/'enclosed-root-all-capacities-verification.json'


def main():
    started = time.monotonic()
    checks = Counter(); failures = []
    report = dict(stage='in_progress', failures=failures,
                  source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

    def save():
        report.update(checks=sum(checks.values()), checks_by_kind=dict(checks),
                      seconds=time.monotonic()-started)
        OUT.write_text(json.dumps(report, indent=2)+'\n')

    def ck(kind, ok, detail=None):
        checks[kind] += 1
        if not ok:
            failures.append(dict(kind=kind, detail=detail))
            report['stage'] = 'failed'; save(); raise AssertionError((kind, detail))

    save()
    with gzip.open(SOURCE, 'rt') as f: saved = json.load(f)
    ck('completed_input', saved['stage'] == 'complete' and saved['failures'] == [])
    for path, digest in saved['input_sha256'].items():
        ck('unchanged_input_hash', hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path)
    ck('unchanged_constructor', saved['code_sha256'] ==
       hashlib.sha256((B/'enclosed_root_all_capacities.py').read_bytes()).hexdigest())
    with gzip.open(B/'positive-factor-enclosure.json.gz', 'rt') as f: z = json.load(f)
    pv = json.loads((B/'positive-factor-enclosure-verification.json').read_text())
    ck('bound_prior_root_certificate', pv['stage'] == 'verified' and pv['failures'] == []
       and pv['input_sha256'] == hashlib.sha256((B/'positive-factor-enclosure.json.gz').read_bytes()).hexdigest()
       and z['stage'] == 'exact_complete' and z['inclusion']
       and pv['inclusion_margins'] == z['inclusion_margins'] and min(z['inclusion_margins']) > 0)
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    a = [Fraction(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    N = 1 + 65537**28 // (1 << 128)
    H = comb(1024,68)
    U = Fraction(comb(1024,64),comb(68,64))
    alpha = Fraction(2*(N-1),1)/(U-1)
    gs = [comb(956,i)*comb(68,i) for i in range(69)]
    cs = [Fraction(1),*([Fraction(0)]*4)]
    cs.extend(alpha*a[k]/(2*gs[k+5]) for k in range(64))
    ck('canonical_pairs', len(a) == 64 and min(a) > 0 and sum(a) == U-1
       and cs == [Fraction(*p) for p in saved['c']] == [Fraction(*p) for p in z['c']])
    ck('parameters_and_coincident_row', N == saved['N'] == z['N'] and H == saved['H'] == z['H']
       and sum(g*c for g,c in zip(gs,cs)) == N
       and (N-1)*(1 << 128) <= 65537**28 < N*(1 << 128))
    ck('fixed_box', z['Q'] == 10**70 and z['radius'] == 10**25 and len(z['point']) == 64
       and z['box'] == [[p-10**25,p+10**25] for p in z['point']])
    endpoints = {}
    ck('endpoint_record_count', len(saved['endpoints']) == len(z['scale_powers']) == 64)
    for k, row in enumerate(saved['endpoints']):
        i = k+5
        power = z['scale_powers'][k]
        scale = Fraction(10**power,1) if power >= 0 else Fraction(1,10**(-power))
        ck('original_coordinate_scaling', z['K'] > 0 and
           z['K']**3*(N-1) <= H < (z['K']+1)**3*(N-1)
           and scale <= z['K']*cs[i] < 10*scale)
        lo = Fraction(z['box'][k][0]*scale.numerator,z['Q']*scale.denominator)
        hi = Fraction(z['box'][k][1]*scale.numerator,z['Q']*scale.denominator)
        ck('every_original_endpoint', row['i'] == i and 0 < lo < hi
           and [lo.numerator,lo.denominator] == row['lower']
           and [hi.numerator,hi.denominator] == row['upper'], i)
        endpoints[i] = lo,hi
    # Independent four-region occupancies, all possible Z, and all six orders.
    choose = [[comb(n,k) if 0 <= k <= n else 0 for k in range(69)] for n in range(1025)]
    left = {}; right = {}
    for i in range(69):
        for j in range(69):
            left[i,j] = [choose[i][t]*choose[68-i][j-t] if t <= j else 0 for t in range(69)]
            right[i,j] = [choose[i][s]*choose[956-i][j-s] if s <= j else 0 for s in range(69)]
    counts = Counter(); classes = {}; shell_sums = []
    coeff = [defaultdict(int) for _ in range(64)]
    rep_rows = []
    for i in range(69):
        if time.monotonic()-started > 300:
            report['stage'] = 'incomplete_budget'; save(); raise TimeoutError(OUT)
        sums = [0]*69; reps = []
        for common in range(69-i):
            for aonly in range(i+1):
                for bonly in range(i+1):
                    outside = 68-common-aonly-bonly
                    if not 0 <= outside <= 956-i: continue
                    j = 68-common-aonly; h = 68-common-bonly
                    t = i-aonly; s = bonly
                    atoms = (956-i-outside,i-aonly,i-bonly,68-i-common,
                             outside,aonly,bonly,common)
                    D = choose[68-i][common]*choose[i][aonly]*choose[i][bonly]*choose[956-i][outside]
                    ck('full_original_orbit_and_D', min(atoms) >= 0 and sum(atoms) == 1024
                       and atoms == (956-i-j+s,t,i-s,j-t,j-s,i-t,s,68-i-j+t)
                       and max(0,i+j-68) <= t <= min(i,j)
                       and max(0,i+j-956) <= s <= min(i,j)
                       and h == i+j-t-s and D == left[i,j][t]*right[i,j][s] > 0)
                    orders = ((i,j,t,s),(j,i,t,s),
                              (i,h,atoms[2],atoms[5]),(h,i,atoms[2],atoms[5]),
                              (j,h,atoms[4],atoms[3]),(h,j,atoms[4],atoms[3]))
                    G = gs[i]*D
                    ck('all_six_presentations', all(
                        tt-ss == t-s and G == gs[ii]*left[ii,jj][tt]*right[ii,jj][ss]
                        for ii,jj,tt,ss in orders))
                    counts['original'] += 1; sums[j] += D
                    if i == 0 or j == 0 or h == 0:
                        counts['repeated'] += 1
                        ck('repetition_D', D == (gs[j] if i == 0 else 1))
                        if i: reps.append([j,t,s,D])
                    elif i < 5 or j < 5 or h < 5:
                        counts['null'] += 1
                        ck('null_edges_have_zero_capacity', min(cs[i],cs[j],cs[h]) == 0)
                    else:
                        counts['permitted'] += 1
                        key = tuple(sorted((i,j,h)))
                        orbit = [i,j,t,s]
                        if key not in classes:
                            classes[key] = [0,0,0,orbit]
                        r = classes[key]
                        r[0] += 1; r[1] += D; r[2] += G; r[3] = min(r[3],orbit)
                        coeff[i-5][tuple(sorted((j-5,h-5)))] += D
        ck('complete_shell_sums', sums == gs and sums == saved['shell_sums'][i], i)
        ck('both_repetitions', sorted(reps) == saved['endpoint_repetitions'][i]
           == ([] if i == 0 else [[0,0,0,1],[i,i,i,1]]), i)
        rep_rows.append(sorted(reps)); shell_sums.append(sums)
    ck('full_original_partition', dict(counts) == saved['counts'] == z['counts'] ==
       dict(original=1500625,repeated=205,null=10220,permitted=1490200))
    reconstructed = [[[j,h,v] for (j,h),v in sorted(row.items())] for row in coeff]
    ck('same_full_polynomial_system', reconstructed == z['coefficients']
       and sum(map(len,reconstructed)) == 81355)
    # Reconstruct side feasibility independently as possible common intersections.
    feasible = set()
    for i in range(5,69):
        for j in range(i,69):
            for h in range(j,69):
                # r=68-i-j+t, outside=j-s, with s=i+j-h-t.
                t0 = max(0,i+j-68,i+j-h-min(i,j))
                t1 = min(i,j,i+j-h-max(0,i+j-956))
                if t0 <= t1: feasible.add((i,j,h))
    old = json.loads((B/'equilateral-capacity-allowance.json').read_text())
    prior_classes = {tuple(r['distances']):r['source_entries'] for r in old['permitted_side_classes']}
    ck('all_actual_class_coverage', set(classes) == feasible == set(prior_classes)
       and len(classes) == saved['side_class_count'] == len(saved['classes']) == 28215)
    ck('saved_class_order_and_uniqueness', [tuple(r['distances']) for r in saved['classes']] == sorted(classes))
    verdicts = Counter(); rejected = []; straddles = []; maxlo = None; maxhi = None
    verified_rows = []
    for row in saved['classes']:
        key = tuple(row['distances']); actual = classes[key]
        ck('every_class_full_source_data', actual ==
           [row['source_entries'],row['sum_D'],row['sum_gD'],row['representative']]
           and actual[0] == prior_classes[key], list(key))
        capacity = min(cs[k] for k in key)
        ck('every_minimum_capacity', [capacity.numerator,capacity.denominator] == row['capacity'])
        bounds = []
        for endpoint in (0,1):
            numerator = capacity.denominator
            denominator = capacity.numerator
            for distance in key:
                x = endpoints[distance][endpoint]
                numerator *= x.numerator
                denominator *= x.denominator
            bound = Fraction(numerator,denominator)
            field = 'lower_ratio' if endpoint == 0 else 'upper_ratio'
            ck('every_full_endpoint_fraction', numerator > 0 and denominator > 0
               and [bound.numerator,bound.denominator] == row[field], [list(key),field])
            # Sign comparison is performed on original integers, before reduction.
            bounds.append((bound, (numerator > denominator)-(numerator < denominator)))
        lo,lsign = bounds[0]; hi,hsign = bounds[1]
        verdict = 'pass' if hsign <= 0 else 'reject_enclosed_root' if lsign > 0 else 'straddles'
        ck('every_exact_capacity_verdict', lo < hi and verdict == row['verdict'], list(key))
        verdicts[verdict] += 1
        if verdict == 'reject_enclosed_root': rejected.append(list(key))
        if verdict == 'straddles': straddles.append(list(key))
        if maxlo is None or lo > maxlo[0]: maxlo = lo,key
        if maxhi is None or hi > maxhi[0]: maxhi = hi,key
        verified_rows.append(dict(distances=list(key), verdict=verdict,
                                  exact_record_sha256=hashlib.sha256(json.dumps(row,sort_keys=True).encode()).hexdigest()))
    ck('all_verdict_counts', dict(verdicts) == saved['verdict_counts']
       and rejected == saved['rejected_classes'] and straddles == saved['straddling_classes'])
    for name,value in (('maximum_lower',maxlo),('maximum_upper',maxhi)):
        expected = dict(distances=list(value[1]), ratio=[value[0].numerator,value[0].denominator])
        ck('global_endpoint_maximum', expected == saved[name], name)
        report[name] = expected
    report.update(stage='verified', counts=dict(counts), side_class_count=len(classes),
                  verdict_counts=dict(verdicts), rejected_classes=rejected, straddling_classes=straddles,
                  required_ratio_at_most=1, verified_class_records=verified_rows,
                  scope='All fixed-box upper capacities and original-orbit coverage; prior root proof is an input.')
    save()
    print(json.dumps(dict(stage=report['stage'], checks=report['checks'], failures=len(failures),
          classes=len(classes), verdicts=dict(verdicts), required='upper ratio <=1', path=str(OUT))))


if __name__ == '__main__':
    main()

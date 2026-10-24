"""Independent L110 audit. Reads originals, writes a separate full certificate.

No constructor imports, factor solve, or scaling existence claim. Enumerate
third supports by their four fixed-edge region occupancies, not source t,s.
"""
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from math import lcm
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'l110-critical-audit.json'
SOURCE = B / 'equilateral-capacity-allowance.json'
SAVED = B / 'equilateral-capacity-saved-verification.json'


def main():
    report = dict(stage='in_progress', checks_by_kind={}, failures=[])
    OUT.write_text(json.dumps(report) + '\n')

    def ck(kind, value, detail=None):
        report['checks_by_kind'][kind] = report['checks_by_kind'].get(kind, 0) + 1
        if not value:
            report['failures'].append(dict(kind=kind, detail=detail))
            OUT.write_text(json.dumps(report, indent=2) + '\n')
            raise AssertionError((kind, detail))

    src = json.loads(SOURCE.read_text())
    saved = json.loads(SAVED.read_text())
    lp = json.loads((B / 'delsarte-lp-results.json').read_text())
    # Pascal recurrence, independent of the constructors' math.comb calls.
    C = [[1]]
    for n in range(1, 1025):
        prev = C[-1]
        C.append([1] + [(prev[k-1] if k-1 < len(prev) else 0)
                        + (prev[k] if k < len(prev) else 0)
                        for k in range(1, min(n, 68)+1)])

    def choose(n, k):
        return C[n][k] if 0 <= k <= min(n, 68) else 0

    N = 65537**28 // 2**128 + 1
    U = F(choose(1024, 64), choose(68, 64))
    alpha = 2*(N-1)/(U-1)
    a = [F(z['numerator'], z['denominator']) for z in lp['exact']['primal']]
    g = [choose(68, i)*choose(956, i) for i in range(69)]
    c = [F(1)] + [F(0)]*4 + [alpha*a[i-5]/(2*g[i]) for i in range(5, 69)]
    q = lcm(*(x.denominator for x in c))
    P = [int(q*x) for x in c]
    H = choose(1024, 68)
    ck('pair_input', len(a) == 64 and min(a) > 0 and sum(a) == U-1)
    ck('pair_normalization', N > 2 and 0 < alpha < 1 and sum(g[i]*c[i] for i in range(69)) == N)
    ck('saved_parameters', src['N'] == N and src['H'] == H and F(*src['U']) == U
       and F(*src['alpha']) == alpha and src['denominator'] == q
       and src['pair_numerators'] == P and src['shell_sizes'] == g)
    ck('integer_endpoint', (N-1)*2**128 <= 65537**28 < N*2**128)

    # Independently reconstruct both complete equilateral records.
    E = {}
    equilateral = []
    for i in range(1, 69):
        direct, terms = [], []
        for r in range(69-i):
            p = 68-i-r
            o = 68-r-2*p
            if 0 <= p <= i and 0 <= o <= 956-i:
                D = choose(68-i, r)*choose(i, p)**2*choose(956-i, o)
                direct.append(dict(common=r, each_pair_only=p, outside=o, count=D))
                t, s = i-p, p
                ns = [956-i-o, i-p, i-p, 68-i-r, o, p, p, r]
                terms.append(dict(t=t, s=s, t_minus_s=t-s, D=D, atoms=ns))
                ck('equilateral_term', D == choose(i,t)**2*choose(68-i,i-t)*choose(956-i,t)
                   and min(ns) >= 0 and sum(ns) == 1024, [i,r])
        E[i] = sum(z['count'] for z in direct)
        row = dict(i=i, E=E[i], source_terms=terms, direct_four_region_terms=direct)
        ck('complete_equilateral_record', row == src['equilateral_counts'][i-1], i)
        ck('positive_equilateral_count', E[i] > 0 and terms[-1]['D'] == choose(956-i,i), i)
        equilateral.append(row)
    ck('equilateral_record_length', len(src['equilateral_counts']) == 68)

    # Complete four-region enumeration: Z uses r common points, p points
    # of A\B, v points of B\A, and o outside A union B.
    counts = Counter()
    classes = Counter()
    reps = {}
    cells = []
    repetitions = []
    # Independent source formula lookup for every possible (i,j,t/s).
    left, right = {}, {}
    for i in range(69):
        for j in range(69):
            left[i,j] = [choose(i,t)*choose(68-i,j-t) for t in range(min(i,j)+1)]
            right[i,j] = [choose(i,s)*choose(956-i,j-s) for s in range(min(i,j)+1)]
    for i in range(69):
        shell_sums = [0]*69
        shell_entries = [0]*69
        rep = []
        eq_sum = 0
        for r in range(69-i):
            for p in range(i+1):
                for v in range(i+1):
                    o = 68-r-p-v
                    if not 0 <= o <= 956-i:
                        continue
                    j, h, t, s = 68-r-p, 68-r-v, i-p, v
                    ns = (956-i-o, i-p, i-v, 68-i-r, o, p, v, r)
                    orbit = (i,j,t,s)
                    D = choose(68-i,r)*choose(i,p)*choose(i,v)*choose(956-i,o)
                    ck('source_geometry', 0 <= j <= 68 and 0 <= h <= 68
                       and max(0,i+j-68) <= t <= min(i,j)
                       and max(0,i+j-956) <= s <= min(i,j)
                       and h == i+j-t-s and min(ns) >= 0 and sum(ns) == 1024, orbit)
                    ck('fixed_edge_multiplicity', D == left[i,j][t]*right[i,j][s] > 0, orbit)
                    # Three anchors suffice: swapping the two other supports
                    # leaves G unchanged by the symmetric source formula.
                    tB, sB = ns[2], ns[5]
                    tZ, sZ = ns[4], ns[3]
                    G = g[i]*D
                    ck('all_anchor_multiplicities', tB-sB == tZ-sZ == t-s
                       and G == g[i]*left[i,h][tB]*right[i,h][sB]
                       and G == g[j]*left[j,h][tZ]*right[j,h][sZ], orbit)
                    counts['original'] += 1
                    shell_entries[j] += 1
                    shell_sums[j] += D
                    if i == j == h:
                        eq_sum += D
                    if min(i,j,h) == 0:
                        counts['repeated'] += 1
                        ck('repetition_coefficient', D == (g[j] if i == 0 else 1), orbit)
                        if i:
                            rep.append([j,t,s,D])
                    elif min(i,j,h) < 5:
                        counts['null_capacity_distinct'] += 1
                        ck('null_edge', min(c[i],c[j],c[h]) == 0, orbit)
                    else:
                        counts['permitted_distinct'] += 1
                        key = tuple(sorted((i,j,h)))
                        classes[key] += 1
                        reps[key] = min(reps.get(key, orbit), orbit)
        rep.sort()
        ck('complete_endpoint_removal', rep == ([] if i == 0 else [[0,0,0,1],[i,i,i,1]]), i)
        repetitions.append(dict(i=i, distinct_edge_repetitions=rep))
        ck('all_third_supports', shell_sums == g and sum(shell_sums) == H, i)
        ck('source_equilateral_exhaustion', eq_sum == (E[i] if i else 1), i)
        cells.append(dict(i=i, entries_by_j=shell_entries, coefficient_sums_by_j=shell_sums))
    ck('saved_source_partition', dict(counts) == src['original_counts'] == dict(
        original=1500625, repeated=205, null_capacity_distinct=10220, permitted_distinct=1490200))
    ck('saved_repetitions', repetitions == src['repetitions'])

    # Independent Venn-common-core interval for every sorted side triple.
    # All other seven atoms are forced once k=|A intersection B intersection Z| is fixed.
    actual = {}
    for i,j,h in itertools.combinations_with_replacement(range(5,69), 3):
        lo = max(0,68-i-j,68-i-h,68-j-h)
        hi = min(68-i,68-j,68-h,1024-i-j-h)
        if lo <= hi:
            actual[i,j,h] = (lo, hi)
            ck('class_presentation_count', classes[i,j,h] == (hi-lo+1)*len(set(itertools.permutations((i,j,h)))), [i,j,h])
    ck('complete_side_classes', set(actual) == set(classes) and len(classes) == 28215)
    ck('saved_side_keys', [tuple(z['distances']) for z in src['permitted_side_classes']] == sorted(classes))

    M = F(N-2, E[5])
    maximum_cube = M**3
    tally = Counter(below_one=0, above_one=0, equal_one=0)
    rows = []
    old_checks = []

    def old(name, passed):
        old_checks.append(dict(name=name, passed=bool(passed)))
        ck('saved_verifier_assertion', passed, name)

    old('exact_equilateral_maximum', maximum_cube == F(*src['maximum']['ratio_cube']))
    old('distance_five_count', E[5] == 89469195005112)
    old('exact_maximum_bracket', F(*src['maximum']['ratio_lower']) <= M < F(*src['maximum']['ratio_strict_upper']))
    maxima = []
    for z in src['permitted_side_classes']:
        i,j,h = key = tuple(z['distances'])
        kmin = min(key, key=lambda k: c[k])
        # Rational pairs are independently rebuilt above, not read from P.
        cube = (N-2)**3*c[i]*c[j]*c[h]/(E[i]*E[j]*E[h]*c[kmin]**3)
        label = 'below_one' if cube < 1 else 'above_one' if cube > 1 else 'equal_one'
        old(f'unique_{i}_{j}_{h}', key not in {tuple(row['distances']) for row in rows[-1:]})
        old(f'positive_denominator_{i}_{j}_{h}', E[i]*E[j]*E[h]*min(P[i],P[j],P[h])**3 > 0)
        old(f'bounded_by_maximum_{i}_{j}_{h}', cube <= maximum_cube)
        old(f'capacity_comparison_{i}_{j}_{h}', label == z['comparison_with_one'])
        ck('saved_class_record', z['source_entries'] == classes[key] and z['representative'] == list(reps[key]) and z['min_pair_index'] == kmin, key)
        if cube == maximum_cube:
            maxima.append(list(key))
        tally[label] += 1
        rows.append(dict(distances=list(key), common_core_interval=list(actual[key]),
                         source_entries=classes[key], representative=list(reps[key]),
                         min_pair_index=kmin, comparison_with_one=label,
                         bounded_by_maximum=True))
    old('comparison_counts', all(src[k] == v for k,v in tally.items()))
    old('side_class_count', len(classes) == src['side_class_count'] == 28215)
    old('source_entry_count', sum(classes.values()) == 1490200)
    old('construction_failures', src['failures'] == [])
    ck('full_saved_verification', old_checks == saved['checks'] and len(old_checks) == saved['check_count'] == 112867
       and saved['failures'] == [] and saved['comparisons'] == dict(tally)
       and F(*saved['exact_maximum_allowance']) == M and saved['required_maximum_at_most'] == 1)
    ck('maximum_and_threshold', maxima == [[5,5,5]] and 238*10**80 <= M < 239*10**80 and M > 1)
    ck('comparison_totals', dict(tally) == dict(below_one=2902, above_one=25313, equal_one=0))
    worst = src['maximum']
    supports = list(map(set, worst['supports']))
    ck('actual_maximum_sets', all(len(x) == 68 for x in supports)
       and len(set.union(*supports)) == 73 and all(x <= set(range(1024)) for x in supports)
       and all(len(x-y) == 5 for x,y in itertools.permutations(supports,2)))
    atom_sizes = [sum(sum((point in supports[k]) << k for k in range(3)) == bits
                      for point in range(1024)) for bits in range(8)]
    ck('maximum_atoms', atom_sizes == worst['atoms'] == [951,0,0,5,0,5,5,58])
    presentations = []
    for order in itertools.permutations(range(3)):
        A,B0,Z = (supports[k] for k in order)
        i,j = len(A-B0), len(A-Z)
        t,s = len((A-B0)&(A-Z)), len((B0-A)&(Z-A))
        presentations.append(dict(order=list(order), orbit=[i,j,t,s], h=len(B0-Z),
                                  t_minus_s=t-s, D=left[i,j][t]*right[i,j][s]))
    ck('maximum_all_presentations', presentations == worst['presentations']
       and worst['representative'] == [5,5,0,5] and worst['distances'] == [5,5,5] and worst['min_pair_index'] == 5)
    ck('original_integrity', saved['source_sha256'] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
       and saved['code_sha256'] == hashlib.sha256((B/'equilateral_capacity_verify_saved.py').read_bytes()).hexdigest()
       and src['code_sha256'] == hashlib.sha256((B/'equilateral_capacity_allowance.py').read_bytes()).hexdigest())
    # Construction input hashes concern its own invocation; review uses current
    # files and records hashes separately, without rewriting that evidence.
    paths = [SOURCE, SAVED, B/'delsarte-lp-results.json', Path(__file__)]
    paths += [ROOT/p for p in src['input_sha256'] if p.endswith('.md')]
    report.update(stage='complete', verdict='RETAIN_CONDITIONAL_CERTIFICATE_STOP',
                  input_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
                  N=N, denominator=q, pair_numerators=P, equilateral_counts=equilateral,
                  original_counts=dict(counts), fixed_edge_cells=cells, repetitions=repetitions,
                  classes=rows, comparisons=dict(tally), maximizers=maxima,
                  maximum_allowance=[M.numerator,M.denominator], required_allowance_at_most=1,
                  maximum_presentations=presentations, saved_verification_assertions=len(old_checks),
                  qualification='Conditional allowance only; no factor existence, actual capacity violation, full lift, PSD or RS result.')
    report['check_count'] = sum(report['checks_by_kind'].values())
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(f'L110 critical audit: {report["verdict"]}; {report["check_count"]} exact checks; failures={report["failures"]}')
    print(f'{counts["original"]} source entries; {len(classes)} side classes; all {len(old_checks)} saved assertions reconstructed.')
    print('Actual maximum (N-2)/89469195005112 in [2.38e82,2.39e82), required <=1; allowance failure only.')
    print(f'Full certificate: {OUT}')


if __name__ == '__main__':
    main()

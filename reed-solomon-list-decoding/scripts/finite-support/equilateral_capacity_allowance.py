"""One exact conditional capacity evaluation; no scaling solve or iteration.

The complete certificate factors every ratio cube through P_i and E_i.
All original source entries are retained in the exhaustive counting pass.
"""
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from math import comb, lcm
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'equilateral-capacity-allowance.json'


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def atoms(i, j, t, s):
    return (956-i-j+s, t, i-s, j-t, j-s, i-t, s, 68-i-j+t)


def indices(A, B0, Z):
    return [len(A-B0), len(A-Z), len((A-B0) & (A-Z)),
            len((B0-A) & (Z-A))]


def actual_sets(ns):
    sets = [set(), set(), set()]
    offset = 0
    for bits, size in enumerate(ns):
        part = set(range(offset, offset+size))
        for k in range(3):
            if bits & (1 << k):
                sets[k].update(part)
        offset += size
    assert offset == 1024
    return sets


def main():
    paths = [
        'scripts/finite-support/delsarte-lp-results.json',
        'lemmas/L021-basic-delsarte-support-lp-optimum.md',
        'lemmas/L098-exact-cardinality-normalized-control-obstruction.md',
        'lemmas/L105-fixed-pair-independent-row-capacity-nonexclusion.md',
        'lemmas/L108-equilateral-triangles-stop-uncapacitated-distance-dual.md',
        'lemmas/L109-capacitated-two-distance-dual-nonseparation.md',
        'foundations/04-constant-weight-triple-sdp-source.md',
        'foundations/12-global-degree-three-moment-source.md',
        'foundations/13-fixed-cardinality-marginal-source.md',
        'drafts/literature/2026-10-23-equilateral-scaling-capacity-test.md',
    ]
    report = dict(stage='in_progress', failures=[], checks_by_kind={})
    OUT.write_text(json.dumps(report)+'\n')

    def ck(kind, test, detail=None):
        report['checks_by_kind'][kind] = report['checks_by_kind'].get(kind, 0)+1
        if not test:
            report['failures'].append(dict(kind=kind, detail=detail))
            OUT.write_text(json.dumps(report, indent=2)+'\n')
            raise AssertionError((kind, detail))

    report['input_sha256'] = {
        p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    a = [F(x['numerator'], x['denominator']) for x in lp['exact']['primal']]
    N = 65537**28 // 2**128+1
    H = comb(1024, 68)
    U = F(comb(1024, 64), comb(68, 64))
    alpha = 2*(N-1)/(U-1)
    g = [comb(68, i)*comb(956, i) for i in range(69)]
    c = [F(1)]+[F(0)]*4+[alpha*a[i-5]/(2*g[i]) for i in range(5, 69)]
    q = lcm(*(z.denominator for z in c))
    P = [int(z*q) for z in c]
    ck('canonical_pairs', len(a) == 64 and min(a) > 0 and sum(a) == U-1)
    ck('parameters', H > N > 2 and 0 < alpha < 1)
    ck('objective', sum(g[i]*c[i] for i in range(69)) == N)
    ck('pair_signs', c[0] == 1 and c[1:5] == [0]*4 and min(c[5:]) > 0)
    ck('integer_endpoint', (N-1)*2**128 <= 65537**28 < N*2**128)
    report.update(N=N, H=H, U=enc(U), alpha=enc(alpha),
                  denominator=q, pair_numerators=P, shell_sizes=g)

    # Every equilateral orbit at a fixed edge, not just (i,i,i,0).
    eq = []
    E = [0]*69
    for i in range(1, 69):
        terms = []
        for t in range(max(0, 2*i-68), i+1):
            s = i-t
            ns = atoms(i, i, t, s)
            D = comb(i, t)*comb(68-i, i-t)*comb(i, s)*comb(956-i, i-s)
            ck('equilateral_atoms', min(ns) >= 0 and sum(ns) == 1024, [i,t])
            ck('equilateral_product', D == comb(i,t)**2*comb(68-i,i-t)*comb(956-i,t), [i,t])
            terms.append(dict(t=t, s=s, t_minus_s=t-s, D=D, atoms=list(ns)))
        E[i] = sum(z['D'] for z in terms)
        # Independently choose Z in the four fixed-edge regions.
        # r=|Z intersection (A intersection B)|, b points from each pair-only part,
        # and o points outside their union. Distances impose b=68-i-r.
        direct = []
        for r in range(69-i):
            b = 68-i-r
            o = 68-r-2*b
            if 0 <= b <= i and 0 <= o <= 956-i:
                count = comb(68-i,r)*comb(i,b)**2*comb(956-i,o)
                direct.append(dict(common=r, each_pair_only=b, outside=o, count=count))
        ck('complete_equilateral_count', E[i] == sum(z['count'] for z in direct) > 0, i)
        ck('equilateral_single_orbit_included', terms[-1]['D'] == comb(956-i,i), i)
        eq.append(dict(i=i, E=E[i], source_terms=terms, direct_four_region_terms=direct))
    report['equilateral_counts'] = eq

    # Exhaust actual source orbits; keep their original t-s and count each once.
    # Ratio cubes depend only on the distances under this explicit ansatz, but
    # no source variables are identified or used to assert feasibility.
    counts = Counter()
    class_counts = Counter()
    representatives = {}
    repetitions = []
    for i in range(69):
        rep = []
        for j in range(69):
            ts = range(max(0,i+j-68), min(i,j)+1)
            ss = range(max(0,i+j-956), min(i,j)+1)
            da = {t: comb(i,t)*comb(68-i,j-t) for t in ts}
            db = {s: comb(i,s)*comb(956-i,j-s) for s in ss}
            for t in ts:
                for s in ss:
                    h = i+j-t-s
                    counts['original'] += 1
                    if min(i,j,h) == 0:
                        counts['repeated'] += 1
                        D = da[t]*db[s]
                        ck('repetition_multiplicity', D == (g[j] if i == 0 else 1), [i,j,t,s])
                        if i:
                            rep.append([j,t,s,D])
                    elif min(i,j,h) < 5:
                        counts['null_capacity_distinct'] += 1
                        ck('zero_incident_weight', min(P[i],P[j],P[h]) == 0, [i,j,t,s])
                    else:
                        counts['permitted_distinct'] += 1
                        key = tuple(sorted((i,j,h)))
                        class_counts[key] += 1
                        representatives.setdefault(key, [i,j,t,s])
        ck('endpoint_repetitions', rep == ([[0,0,0,1],[i,i,i,1]] if i else []), i)
        repetitions.append(dict(i=i, distinct_edge_repetitions=rep))
    ck('source_exhaustion', counts['original'] == 1500625 and counts['repeated'] == 205)
    ck('permitted_partition', sum(class_counts.values()) == counts['permitted_distinct'])

    # Independent feasible-side test: admissible t must fit both t and s ranges.
    feasible_keys = set()
    for i in range(5,69):
        for j in range(i,69):
            for h in range(j,69):
                u = i+j-h
                lower = max(0,i+j-68,u-min(i,j))
                upper = min(i,j,u-max(0,i+j-956))
                if lower <= upper:
                    feasible_keys.add((i,j,h))
    ck('actual_side_exhaustion', set(class_counts) == feasible_keys)

    ratios = []
    maximum = None
    passing = failing = equal = 0
    for key in sorted(class_counts):
        i,j,h = key
        kmin = min(key, key=lambda k: P[k])
        ratio = F((N-2)**3*P[i]*P[j]*P[h], E[i]*E[j]*E[h]*P[kmin]**3)
        # Independent rational expression retains the actual c_i normalization.
        alternate = ((N-2)*c[i]/E[i])*((N-2)*c[j]/E[j])*((N-2)*c[h]/E[h])/c[kmin]**3
        ck('ratio_cube_identity', ratio == alternate, list(key))
        status = 'above_one' if ratio > 1 else 'below_one' if ratio < 1 else 'equal_one'
        failing += ratio > 1
        passing += ratio < 1
        equal += ratio == 1
        ratios.append(dict(distances=list(key), source_entries=class_counts[key],
                           representative=representatives[key], min_pair_index=kmin,
                           comparison_with_one=status))
        if maximum is None or ratio > maximum[0]:
            maximum = (ratio, key, kmin)
    worst,key,kmin = maximum
    orbit = representatives[key]
    ns = atoms(*orbit)
    supports = actual_sets(ns)
    presentations = []
    for order in itertools.permutations(range(3)):
        A,B0,Z = [supports[k] for k in order]
        ii,jj,t,s = indices(A,B0,Z)
        hh = len(B0-Z)
        D = comb(ii,t)*comb(68-ii,jj-t)*comb(ii,s)*comb(956-ii,jj-s)
        ck('maximum_actual_sets', len({frozenset(X) for X in supports}) == 3 and
           all(len(X) == 68 for X in supports))
        ck('maximum_presentation', sorted((ii,jj,hh)) == list(key) and hh == ii+jj-t-s and
           t-s == orbit[2]-orbit[3] and D > 0, list(order))
        presentations.append(dict(order=list(order), orbit=[ii,jj,t,s], h=hh,
                                  t_minus_s=t-s, D=D))
    # A transparent exact integer lower bound and decimal-scale bracket for cube root.
    # 10^k <= worst^(1/3) < 10^(k+1), found by integer digit lengths then exact checks.
    power = (len(str(worst.numerator))-len(str(worst.denominator)))//3
    while worst < F(10)**(3*power):
        power -= 1
    while worst >= F(10)**(3*(power+1)):
        power += 1
    scale = 10**max(power,0)
    lower = 10**power if power >= 0 else F(1,10**(-power))
    # First three significant decimal digits, with exact cubing comparisons.
    unit = F(10)**(power-2)
    digit = next(z for z in range(100,1000) if (unit*(z+1))**3 > worst)
    ck('maximum_ratio_bracket', (unit*digit)**3 <= worst < (unit*(digit+1))**3)
    report.update(stage='complete', original_counts=dict(counts), repetitions=repetitions,
                  permitted_side_classes=ratios, side_class_count=len(ratios),
                  below_one=passing, above_one=failing, equal_one=equal,
                  ratio_cube_formula='(N-2)^3*P_i*P_j*P_h/(E_i*E_j*E_h*min(P_i,P_j,P_h)^3)',
                  maximum=dict(distances=list(key), min_pair_index=kmin, ratio_cube=enc(worst),
                               representative=orbit, atoms=list(ns),
                               supports=[sorted(X) for X in supports], presentations=presentations,
                               ratio_lower=enc(unit*digit), ratio_strict_upper=enc(unit*(digit+1))),
                  required_ratio_at_most=1,
                  verdict='PASS' if failing == 0 else 'PARK_SUFFICIENT_CERTIFICATE',
                  mathematical_qualification='Conditional allowance only; no existence or actual capacity violation is proved.')
    report['check_count'] = sum(report['checks_by_kind'].values())
    report['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(f'Conditional equilateral allowance: {report["verdict"]}; failures: {report["failures"]}')
    print(f'{report["check_count"]} exact checks; {counts["original"]} original entries; {len(ratios)} permitted side classes.')
    print(f'Allowance comparisons: {passing} below one, {equal} equal, {failing} above one; required all <= 1.')
    print(f'Maximum at {key}, source orbit {orbit}; ratio in [{digit}/100*10^{power}, {digit+1}/100*10^{power}).')
    print(f'Full exact and losslessly factored certificate: {OUT}')


if __name__ == '__main__':
    main()

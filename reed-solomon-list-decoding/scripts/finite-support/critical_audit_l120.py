"""L120 manuscript audit; preserve original box, scripts and certificates.

Replay the complete independent comparison checker, then reconstruct actual
unions and the contraction polynomials. No solve or changed enclosure.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
import gzip
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B/'l120-critical-audit.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(name):
    return json.loads((B/name).read_text())


def enc(q):
    return [q.numerator, q.denominator]


@lru_cache(None)
def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def mask(start, size):
    return ((1 << size)-1) << start


def pair_tag(i):
    return ('one',) if i == 0 else ('zero',) if i < 5 else ('pair', i)


def main():
    counts = Counter()
    report = dict(stage='in_progress', failures=[], code_sha256=sha(Path(__file__)))

    def save():
        report.update(checks=sum(counts.values()), checks_by_kind=dict(counts))
        OUT.write_text(json.dumps(report, indent=2)+'\n')

    def ck(kind, ok, detail=None):
        counts[kind] += 1
        if not ok:
            report['stage'] = 'failed'
            report['failures'].append(dict(kind=kind, detail=detail))
            save()
            raise AssertionError((kind, detail))

    source = read('full-product-global-comparison.json')
    paths = set(source['input_sha256'])
    paths.update('scripts/finite-support/'+n for n in [
        'full-product-global-comparison.json',
        'full-product-global-comparison-verification.json',
        'full_product_global_comparison.py', 'verify_full_product_global_comparison.py'])
    report['input_sha256'] = {p:sha(ROOT/p) for p in sorted(paths)}
    save()
    spec = importlib.util.spec_from_file_location('l120_replay', B/'verify_full_product_global_comparison.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.OUT = B/'l120-critical-reverification.json'
    module.main()
    replay = read(module.OUT.name)
    ck('complete_replay_equality', replay == read('full-product-global-comparison-verification.json'))
    ck('complete_replay_status', replay['stage'] == 'verified' and not replay['failures']
       and replay['checks'] == 5206)
    report['replay_sha256'] = sha(module.OUT)

    with gzip.open(B/'positive-factor-enclosure.json.gz', 'rt') as f:
        root = json.load(f)
    c = list(map(lambda q:F(*q), source['c']))
    N, H = source['N'], source['H']
    g = [choose(68,i)*choose(956,i) for i in range(69)]
    ck('root_normalization', N > 2 and F(*source['rho']) == F(N,H) > 0
       and sum(g[i]*c[i] for i in range(5,69)) == N-1)
    ck('root_demands', [enc((N-2)*c[i]) for i in range(5,69)] == root['demands'])

    # One explicit actual-set representative per four-region occupancy.
    # The proof in L112 gives its bijection with all original (i,j,t,s).
    A = mask(0,68)
    classes = Counter()
    polys = [defaultdict(int) for _ in range(64)]
    repeated = []
    for i in range(69):
        V = mask(0,68-i) | mask(68,i)
        totals = [0]*69
        rep = []
        for r in range(69-i):
            for a in range(i+1):
                for b in range(i+1):
                    o = 68-r-a-b
                    if not 0 <= o <= 956-i:
                        continue
                    Z = mask(0,r) | mask(68-i,a) | mask(68,b) | mask(68+i,o)
                    j, h = (A & ~Z).bit_count(), (V & ~Z).bit_count()
                    D = choose(68-i,r)*choose(i,a)*choose(i,b)*choose(956-i,o)
                    ck('actual_support_geometry', Z.bit_count() == V.bit_count() == 68
                       and j == 68-r-a and h == 68-r-b and D > 0)
                    totals[j] += D
                    words = sorted({A,V,Z})
                    if len(words) == 1:
                        entry = ('one',)
                    elif len(words) == 2:
                        entry = pair_tag((words[0] & ~words[1]).bit_count())
                    else:
                        sides = sorted((words[p] & ~words[q]).bit_count()
                                       for p,q in ((0,1),(0,2),(1,2)))
                        entry = ('zero',) if min(sides) < 5 else ('product', *sides)
                    if 1 <= i <= 4 or 1 <= j <= 4:
                        reduced, case = ('zero',), 'forbidden_anchor_row'
                    elif i == 0 or j == 0:
                        reduced, case = pair_tag(max(i,j)), 'singleton_anchor'
                    elif V == Z:
                        reduced, case = pair_tag(i), 'Boolean_diagonal'
                    elif h < 5:
                        reduced, case = ('zero',), 'forbidden_opposite_pair'
                    else:
                        reduced, case = ('product', *sorted((i,j,h))), 'product_off_diagonal'
                    ck('every_union_congruence_case', entry == reduced, [i,j,h])
                    classes[case] += 1
                    if len(words) < 3:
                        rep.append([j,h,D])
                        ck('every_repetition_weight', D == (g[j] if i == 0 else 1))
                    elif i >= 5 and j >= 5 and h >= 5:
                        polys[i-5][tuple(sorted((j-5,h-5)))] += D
        ck('complete_row_counts', totals == g and sum(totals) == H, i)
        ck('complete_endpoint_repetitions', len(rep) == (69 if i == 0 else 2)
           and (i == 0 or sorted(rep) == [[0,i,1],[i,0,1]]), i)
        repeated.append(dict(i=i, entries=rep))
    rows = [[[j,h,v] for (j,h),v in sorted(p.items())] for p in polys]
    ck('entire_root_polynomial', rows == root['coefficients']
       and sum(map(len,rows)) == 81355)
    ck('source_exhaustion', sum(classes.values()) == 1500625)
    report.update(union_cases=dict(classes), repetitions=repeated,
                  contraction_coefficients=rows)
    # With these same polynomials, root equations give (N-2)c_i.
    # C retains Z=B and excludes Z=A: its row sum is (N-1)c_i.
    root_rows = []
    for i in range(5,69):
        row_sum = (N-2)*c[i]+c[i]
        ck('root_only_range_row', row_sum/(N-1) == c[i])
        root_rows.append(enc(row_sum))
    ck('root_only_scalar_and_null_top', sum(g[i]*c[i]/(N-1) for i in range(5,69)) == 1
       and -(N-1)+sum(g[i]*c[i] for i in range(5,69)) == 0)
    report['root_only_row_sums'] = root_rows

    # A different algebraic reconstruction of the SAME signed endpoints,
    # not an alternative enclosure or a midpoint sign test.
    endpoints = [tuple(F(*q) for q in e['interval']) for e in source['endpoints']]
    endpoint_rows = []
    for j in range(69):
        weights = source['eigenmatrix'][j][5:]
        center = sum(w*(lo+hi)/2 for w,(lo,hi) in zip(weights,endpoints))
        radius = sum(abs(w)*(hi-lo)/2 for w,(lo,hi) in zip(weights,endpoints))
        row = [enc(center-radius),enc(center+radius)]
        ck('same_signed_endpoints', row == source['modes'][j]['interval'])
        endpoint_rows.append(row)
    t = source['comparison']
    low, high = [F(*q) for q in t['interval']]
    ref = F(*t['reference'])
    grid = t['normalized_grid']
    floor, ceil = t['normalized_bracket']
    ck('complete_signed_grid_endpoints', ref > 0 and low < 0 < high
       and floor*ref <= grid*low < (floor+1)*ref
       and (ceil-1)*ref < grid*high <= ceil*ref)
    ck('manuscript_minimizers', t['lower_mode'] == [1] and t['upper_mode'] == [64]
       and t['lower_correction'] == t['upper_correction'] == [5])
    ck('manuscript_grid', floor == -11660741035356041112426863955343247787961878293817116679
       and ceil == 630870 and grid == 10**6)
    report.update(stage='verified', signed_endpoints=endpoint_rows, comparison=t,
                  verdict='RETAIN_REDUCTION_AND_INCONCLUSIVE_COMPARISON')
    save()
    print('Actual/required: 1500625/1500625 union cases; 81355/81355 root coefficients; full 5206-check replay agrees')
    print('Comparison/reference in [%s,%s]/%s; required lower >= 0; inconclusive, no PSD verdict' % (floor,ceil,grid))
    print('Additional checks:',sum(counts.values()),'; failures:',len(report['failures']),'; certificate:',OUT)


if __name__ == '__main__':
    main()

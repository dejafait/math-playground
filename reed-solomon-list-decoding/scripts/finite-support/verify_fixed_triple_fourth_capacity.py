"""Independent reconstruction of all fixed-triple atoms and support counts."""
import gzip
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SRC = HERE / 'fixed-triple-fourth-capacity.json.gz'
OUT = HERE / 'fixed-triple-fourth-capacity-verification.json'


def pair(x):
    return [x.numerator, x.denominator]


def main():
    result = dict(stage='in_progress', failures=[], checks=0,
                  constructor_sha256=hashlib.sha256(SRC.read_bytes()).hexdigest(),
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

    def save():
        OUT.write_text(json.dumps(result, indent=2)+'\n')

    def check(label, value):
        result['checks'] += 1
        if not value:
            result['failures'].append(label)
            result['stage'] = 'failed'
            save()
            raise AssertionError(label)

    save()
    with gzip.open(SRC, 'rt') as f:
        saved = json.load(f)
    check('constructor_complete', saved['stage'] == 'complete' and saved['failures'] == [])
    for name, digest in saved['input_sha256'].items():
        check('unchanged_'+name, hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest)
    result['input_sha256'] = saved['input_sha256']
    with gzip.open(HERE/'positive-factor-enclosure.json.gz', 'rt') as f:
        root = json.load(f)
    lp = json.loads((HERE/'delsarte-lp-results.json').read_text())
    N = 1+65537**28//(1 << 128)
    H = factorial(1024)//(factorial(68)*factorial(956))
    density = Fraction(N, H)
    bound = Fraction(factorial(1024)*factorial(4), factorial(960)*factorial(68))
    c = [Fraction(1)]+[Fraction(0)]*4
    for i, record in enumerate(lp['exact']['primal'], 5):
        ai = Fraction(record['numerator'], record['denominator'])
        c.append((N-1)*ai/((bound-1)*comb(68, i)*comb(956, i)))
    check('entire_pair_vector', c == [Fraction(*v) for v in saved['c']] ==
          [Fraction(*v) for v in root['c']])
    check('N_H_rho', N == saved['N'] == root['N'] and H == saved['H'] == root['H'] and
          density == Fraction(*saved['rho']))
    check('unchanged_original_box', root['Q'] == 10**70 and root['radius'] == 10**25 and
          root['box'] == [[p-10**25, p+10**25] for p in root['point']])
    x = {i: [Fraction(10)**root['scale_powers'][i-5]*Fraction(root['point'][i-5]+s*10**25, 10**70)
             for s in [-1, 1]] for i in range(5, 69)}
    check('all_endpoints', saved['endpoints'] == [[i, pair(x[i][0]), pair(x[i][1])]
                                                for i in range(5, 69)])

    # Direct formulas for k<=3 atoms; independent of the constructor's inversion loop.
    def smaller_min(vertices, distances):
        lows = []
        for v in vertices:
            lows.extend([Fraction(1), 1/density-1])
        for a, b in itertools.combinations(vertices, 2):
            p = c[distances[tuple(sorted((a, b)))]]
            lows.extend([p, 1-p, 1-p, 1/density-2+p])
        for tri in itertools.combinations(vertices, 3):
            edges = list(itertools.combinations(tri, 2))
            ps = {e: c[distances[e]] for e in edges}
            lo, hi = triple(tri, distances)
            lows.append(lo)
            lows.extend(ps[e]-hi for e in edges)
            for a in tri:
                lows.append(1-sum(ps[e] for e in edges if a in e)+lo)
            lows.append(1/density-3+sum(ps.values())-hi)
        check('complete_smaller_atoms', min(lows) >= 0)
        return min(lows)

    def triple(vertices, distances):
        sides = [distances[e] for e in itertools.combinations(vertices, 2)]
        if min(sides) < 5:
            return Fraction(0), Fraction(0)
        return tuple(x[sides[0]][k]*x[sides[1]][k]*x[sides[2]][k] for k in (0, 1))

    upper_by_type = {}
    cases = {}
    minimum = None
    for key, data in saved['types'].items():
        ds = tuple(map(int, key.split(',')))
        distances = {(0, 1): 5, (0, 2): 5, (1, 2): 5,
                     (0, 3): ds[0], (1, 3): ds[1], (2, 3): ds[2]}
        repeated = 0 in ds
        vertices = range(3) if repeated else range(4)
        low = smaller_min(vertices, distances)
        check('saved_smaller_min', pair(low) == data['prerequisite_min'])
        minimum = low if minimum is None else min(minimum, low)
        if repeated:
            lo, hi = triple((0, 1, 2), distances)
            check('repeated_boolean_top', data['case'] == 'repeated' and
                  data['normalized_top'] == [pair(lo), pair(hi)])
            cases[key] = 'repeated'
            continue
        triples = {t: triple(t, distances) for t in itertools.combinations(range(4), 3)}
        upper_low = min(t[0] for t in triples.values())
        upper_high = min(t[1] for t in triples.values())
        pair_sum = sum(c[d] for d in distances.values())
        lower = {0: 4-pair_sum+sum(t[1] for t in triples.values())-1/density,
                 15: Fraction(0)}
        for edge in distances:
            mask = sum(1 << j for j in edge)
            lower[mask] = sum(b[1] for tri, b in triples.items() if set(edge) <= set(tri))-c[distances[edge]]
        singles = {}
        for a in range(4):
            singles[1 << a] = (1-sum(c[d] for e, d in distances.items() if a in e)+
                               sum(b[0] for t, b in triples.items() if a in t))
        check('all_eight_lower_candidates', max(lower.values()) == 0)
        check('all_four_singleton_upper_candidates', min(singles.values()) >= upper_high)
        check('every_lower_endpoint', data['lower_candidate_upper'] ==
              [[m, pair(v)] for m, v in sorted(lower.items())])
        check('every_singleton_upper_endpoint', data['singleton_upper_lower'] ==
              [[m, pair(v)] for m, v in sorted(singles.items())])
        check('all_four_triple_intervals', data['triple_bounds'] ==
              [[pair(l), pair(u)] for l, u in triples.values()])
        check('exact_interval_structure', data['normalized_upper'] == [pair(upper_low), pair(upper_high)])
        case = 'null' if min(ds) < 5 else 'permitted'
        check('null_or_permitted', data['case'] == case and
              ((upper_low == upper_high == 0) if case == 'null' else upper_low > 0))
        upper_by_type[key] = upper_low, upper_high
        cases[key] = case

    # Independent occupancy generation: fix outside and core, solve the third private count.
    universe = set(range(1024))
    A = set(range(68))
    B = set(range(63)) | set(range(68, 73))
    C = set(range(63)) | set(range(73, 78))
    real_regions = []
    for mask in range(8):
        points = universe.copy()
        for bit, support in enumerate([A, B, C]):
            points &= support if mask >> bit & 1 else universe-support
        real_regions.append(sorted(points))
    sizes = [len(r) for r in real_regions]
    check('actual_eight_regions', sizes == saved['regions'] == [946, 5, 5, 0, 5, 0, 0, 63])
    expected = {}
    for outside in range(69):
        for common in range(64):
            for ka in range(6):
                for kb in range(6):
                    kc = 68-outside-common-ka-kb
                    if not 0 <= kc <= 5:
                        continue
                    occ = (outside, ka, kb, 0, kc, 0, 0, common)
                    mult = 1
                    D = set()
                    for points, count in zip(real_regions, occ):
                        mult *= factorial(len(points))//(factorial(count)*factorial(len(points)-count))
                        D.update(points[:count])
                    check('actual_D_size', len(D) == 68)
                    ds = tuple(len(s-D) for s in [A, B, C])
                    key = ','.join(map(str, ds))
                    check('type_exists', key in cases)
                    if cases[key] == 'repeated':
                        check('actual_repetition', D in [A, B, C] and mult == 1)
                    else:
                        check('actual_distinct', D not in [A, B, C])
                    expected[occ] = mult, ds, key
    total, counters, masses = 0, Counter(), Counter()
    sum_lo = sum_hi = Fraction(0)
    used = set()
    for row in saved['rows']:
        occ = tuple(row['occupancy'])
        check('unique_occupancy', occ in expected and occ not in used)
        used.add(occ)
        weight, ds, key = expected[occ]
        check('entire_row', weight == row['multiplicity'] and list(ds) == row['distances'] and key == row['type'])
        case = cases[key]
        counters[case] += 1
        masses[case] += weight
        total += weight
        if case != 'repeated':
            lo, hi = upper_by_type[key]
            sum_lo += weight*lo
            sum_hi += weight*hi
    check('all_occupancies_and_types', len(used) == len(expected) == len(saved['rows']) and
          {v[2] for v in expected.values()} == set(saved['types']))
    # Independent Vandermonde convolution gives the mass of all 68-subsets.
    polynomial = [1]+[0]*68
    for size in sizes:
        polynomial = [sum(polynomial[j]*comb(size, k-j) for j in range(k+1)
                          if 0 <= k-j <= size) for k in range(69)]
    check('mass_vandermonde', polynomial[68] == total == H)
    required = [(N-3)*x[5][j]**3 for j in (0, 1)]
    ratios = [sum_lo/required[1], sum_hi/required[0]]
    summary = saved['summary']
    check('complete_saved_summary', summary['occupancies'] == len(expected) and
          summary['types'] == len(cases) and summary['counts'] == dict(counters) and
          summary['masses'] == dict(masses) and summary['required_mass'] == H and
          summary['prerequisite_min'] == pair(minimum) and summary['distinct_lower'] == [0, 1] and
          summary['total_upper_bounds'] == [pair(sum_lo), pair(sum_hi)] and
          summary['required_distinct_bounds'] == [pair(v) for v in required] and
          summary['capacity_over_required'] == [pair(v) for v in ratios])
    check('exact_pass', required[0] > 0 and sum_lo > required[1] and
          summary['verdict'] == 'ONE_ROW_CAPACITY_PASSES')
    check('simple_rational_ratio_bracket', 93301984669 < ratios[0] <= ratios[1] < 93301984670)
    result.update(stage='verified', summary=summary,
                  ratio_integer_bracket=[93301984669, 93301984670],
                  root_triple_bounds=[pair(x[5][j]**3) for j in (0, 1)],
                  verification_scope='All occupancy rows, all local types, all smaller atoms, all sixteen fourth atoms and one cardinality row; no other triple row or PSD.')
    save()
    print('Actual/required support mass:', total, '/', H)
    print('Independent occupancies/types:', len(expected), len(cases), '; ratio in (93301984669,93301984670)')
    print('Checks:', result['checks'], '; failures:', len(result['failures']), '; verdict:', summary['verdict'])
    print('Certificate:', OUT)


if __name__ == '__main__':
    main()

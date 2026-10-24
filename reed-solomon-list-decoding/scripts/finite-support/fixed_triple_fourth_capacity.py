"""One complete fixed-triple Boolean/cardinality test at the original box."""
import gzip
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'fixed-triple-fourth-capacity.json.gz'


def enc(x):
    return [x.numerator, x.denominator]


def main():
    report = dict(stage='in_progress', checks=0, failures=[],
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

    def save():
        with gzip.open(OUT, 'wt') as f:
            json.dump(report, f)

    def ck(label, ok):
        report['checks'] += 1
        if not ok:
            report['failures'].append(label)
            report['stage'] = 'failed'
            save()
            raise AssertionError(label)

    paths = ['scripts/finite-support/'+s for s in [
        'positive-factor-enclosure.json.gz', 'positive-factor-enclosure-verification.json',
        'delsarte-lp-results.json', 'l112-l113-critical-audit.json', 'l114-critical-audit.json']]
    paths += ['lemmas/'+s for s in [
        'L021-basic-delsarte-support-lp-optimum.md',
        'L098-exact-cardinality-normalized-control-obstruction.md',
        'L112-enclosed-product-root-passes-distance-five-capacity.md',
        'L113-enclosed-product-root-passes-all-upper-capacities.md',
        'L114-fixed-product-box-passes-Boolean-lower-rows.md']]
    paths += ['foundations/15-four-variable-boolean-marginal-source.md']
    report['input_sha256'] = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    save()
    with gzip.open(B/'positive-factor-enclosure.json.gz', 'rt') as f:
        z = json.load(f)
    rv = json.loads((B/'positive-factor-enclosure-verification.json').read_text())
    ck('root_binding', rv['stage'] == 'verified' and not rv['failures'] and
       rv['input_sha256'] == report['input_sha256'][paths[0]])
    ck('strict_inclusion', z['inclusion'] and len(z['inclusion_margins']) == 64 and
       min(z['inclusion_margins']) > 0 and rv['inclusion_margins'] == z['inclusion_margins'])
    for name in ['l112-l113-critical-audit.json', 'l114-critical-audit.json']:
        audit = json.loads((B/name).read_text())
        ck('retained_audit_'+name, audit['stage'] == 'verified' and not audit['failures'])
        for p, digest in audit['input_sha256'].items():
            ck('audit_input_'+p, hashlib.sha256((ROOT/p).read_bytes()).hexdigest() == digest)
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    a = [F(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    N, H = 65537**28//2**128+1, comb(1024, 68)
    U = F(comb(1024, 64), comb(68, 64))
    g = [comb(68, i)*comb(956, i) for i in range(69)]
    c = [F(1)]+[F(0)]*4+[(N-1)*a[i-5]/((U-1)*g[i]) for i in range(5, 69)]
    rho = F(N, H)
    ck('canonical_pairs', len(a) == 64 and min(a) > 0 and sum(a) == U-1 and
       c == [F(*v) for v in z['c']] and N == z['N'] and H == z['H'])
    ck('normalization', sum(g[i]*c[i] for i in range(69)) == N and 0 < N < H)
    ck('box_contract', z['Q'] == 10**70 and z['radius'] == 10**25 and
       z['box'] == [[p-z['radius'], p+z['radius']] for p in z['point']])
    endpoints = {i: tuple(F(10)**z['scale_powers'][i-5]*F(v, z['Q'])
                          for v in z['box'][i-5]) for i in range(5, 69)}
    ck('positive_box', all(0 < l < u for l, u in endpoints.values()))
    report.update(N=N, H=H, rho=enc(rho), c=[enc(v) for v in c],
                  endpoints=[[i, enc(l), enc(u)] for i, (l, u) in endpoints.items()])

    # The constructor derives region sizes from actual sets, not a supplied table.
    sets = [set(range(68)), set(range(63)) | set(range(68, 73)),
            set(range(63)) | set(range(73, 78))]
    regions = [sum(sum((1 << j) for j, s in enumerate(sets) if p in s) == m
                   for p in range(1024)) for m in range(8)]
    ck('regions', regions == [946, 5, 5, 0, 5, 0, 0, 63])
    ck('fixed_pair_distances', all(len(sets[i]-sets[j]) == 5
                                  for i in range(3) for j in range(i)))
    types, rows = {}, []
    counts, mass = Counter(), Counter()
    sum_lo = sum_hi = F(0)
    prerequisite_min = None

    def type_data(ds):
        nonlocal prerequisite_min
        key = ','.join(map(str, ds))
        if key in types:
            return key, types[key]
        distances = {(0, 1): 5, (0, 2): 5, (1, 2): 5,
                     (0, 3): ds[0], (1, 3): ds[1], (2, 3): ds[2]}
        alias = {j: j for j in range(4)}
        for j, d in enumerate(ds):
            if d == 0:
                alias[3] = j
        ids = tuple(sorted(set(alias.values())))

        def moment(indices):
            ids0 = tuple(sorted({alias[j] for j in indices}))
            if not ids0:
                return (1/rho, 1/rho)
            if len(ids0) == 1:
                return (F(1), F(1))
            sides = [distances[e] for e in itertools.combinations(ids0, 2)]
            if len(ids0) == 2:
                v = c[sides[0]]
                return v, v
            if min(sides) < 5:
                return F(0), F(0)
            return tuple(endpoints[sides[0]][k]*endpoints[sides[1]][k]*
                         endpoints[sides[2]][k] for k in (0, 1))

        # Check all atoms on every smaller subset, after collapsing repetitions.
        local_min = None
        for size in range(1, min(3, len(ids))+1):
            for sub in itertools.combinations(ids, size):
                for smask in range(1 << size):
                    lo = F(0)
                    for jmask in range(1 << size):
                        if smask & jmask != smask:
                            continue
                        J = [sub[j] for j in range(size) if jmask >> j & 1]
                        l, u = moment(J)
                        sign = (-1)**((jmask ^ smask).bit_count())
                        lo += l if sign > 0 else -u
                    ck('smaller_atom', lo >= 0)
                    local_min = lo if local_min is None else min(local_min, lo)
        prerequisite_min = local_min if prerequisite_min is None else min(prerequisite_min, local_min)
        if len(ids) < 4:
            repeated = moment(range(4))
            data = dict(case='repeated', normalized_top=[enc(v) for v in repeated],
                        prerequisite_min=enc(local_min))
        else:
            lower, upper = [], []
            for smask in range(16):
                lo = hi = F(0)
                for jmask in range(15):
                    if smask & jmask != smask:
                        continue
                    l, u = moment([j for j in range(4) if jmask >> j & 1])
                    sign = (-1)**((jmask ^ smask).bit_count())
                    lo += l if sign > 0 else -u
                    hi += u if sign > 0 else -l
                if (4-smask.bit_count()) % 2 == 0:
                    lower.append((smask, -hi, -lo))
                else:
                    upper.append((smask, lo, hi))
            triples = [moment(t) for t in itertools.combinations(range(4), 3)]
            ulo, uhi = min(v[0] for v in triples), min(v[1] for v in triples)
            ck('all_lower_candidates_nonpositive', all(hi <= 0 for _, _, hi in lower))
            ck('zero_lower_candidate', (15, F(0), F(0)) in lower)
            ck('all_singleton_upper_candidates_redundant',
               all(lo >= uhi for mask, lo, _ in upper if mask.bit_count() == 1))
            data = dict(case='null' if min(ds) < 5 else 'permitted',
                        lower_candidate_upper=[[mask, enc(hi)] for mask, _, hi in lower],
                        singleton_upper_lower=[[mask, enc(lo)] for mask, lo, _ in upper
                                               if mask.bit_count() == 1],
                        triple_bounds=[[enc(l), enc(u)] for l, u in triples],
                        normalized_upper=[enc(ulo), enc(uhi)], prerequisite_min=enc(local_min))
        types[key] = data
        return key, data

    # Eight-region occupancies: the three pair-only coordinates are forced zero.
    for private in itertools.product(range(6), repeat=3):
        for core in range(64):
            outside = 68-core-sum(private)
            if not 0 <= outside <= regions[0]:
                continue
            occ = [outside, private[0], private[1], 0, private[2], 0, 0, core]
            weight = 1
            for size, k in zip(regions, occ):
                weight *= comb(size, k)
            ck('positive_weight', weight > 0 and sum(occ) == 68)
            ds = tuple(68-sum(occ[m] for m in range(8) if m >> j & 1) for j in range(3))
            key, data = type_data(ds)
            case = data['case']
            counts[case] += 1
            mass[case] += weight
            if case == 'repeated':
                ck('repetition_weight_one', weight == 1)
            else:
                lo, hi = (F(*v) for v in data['normalized_upper'])
                sum_lo += weight*lo
                sum_hi += weight*hi
            rows.append(dict(occupancy=occ, multiplicity=weight, distances=ds, type=key))
    ck('total_mass', sum(mass.values()) == H)
    ck('three_repetitions', counts['repeated'] == mass['repeated'] == 3)
    zlo, zhi = endpoints[5][0]**3, endpoints[5][1]**3
    required_lo, required_hi = (N-3)*zlo, (N-3)*zhi
    ck('positive_residual', N > 3 and required_lo > 0)
    # This is an attainable inner interval, not a claim that an outer bound passes.
    verdict = 'ONE_ROW_CAPACITY_PASSES' if required_hi < sum_lo else 'STRADDLE_PARK'
    report.update(stage='complete', regions=regions, rows=rows, types=types,
                  summary=dict(occupancies=len(rows), types=len(types), counts=dict(counts),
                               masses=dict(mass), required_mass=H,
                               prerequisite_min=enc(prerequisite_min),
                               distinct_lower=enc(F(0)),
                               total_upper_bounds=[enc(sum_lo), enc(sum_hi)],
                               required_distinct_bounds=[enc(required_lo), enc(required_hi)],
                               capacity_over_required=[enc(sum_lo/required_hi), enc(sum_hi/required_lo)],
                               verdict=verdict))
    save()
    print('Actual/required support mass:', sum(mass.values()), '/', H)
    print('Occupancies/types:', len(rows), len(types), '; cases:', dict(counts))
    print('Capacity/required lower:', float(sum_lo/required_hi), '; required >=1; verdict:', verdict)
    print('Checks:', report['checks'], '; failures:', len(report['failures']), '; certificate:', OUT)


if __name__ == '__main__':
    main()

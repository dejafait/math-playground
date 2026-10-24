"""Complete fixed-box capacity comparison; never solves or refines a root."""
import gzip
import hashlib
import json
import time
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import comb
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'enclosed-root-all-capacities.json.gz'


def enc(x):
    return [x.numerator, x.denominator]


def main():
    started = time.monotonic()
    checks = Counter()
    report = dict(stage='in_progress', failures=[])

    def save():
        report.update(checks_by_kind=dict(checks), checks=sum(checks.values()),
                      seconds=time.monotonic()-started)
        with gzip.open(OUT, 'wt') as f:
            json.dump(report, f)

    def ck(kind, ok, detail=None):
        checks[kind] += 1
        if not ok:
            report['failures'].append(dict(kind=kind, detail=detail))
            report['stage'] = 'failed'
            save()
            raise AssertionError((kind, detail))

    paths = [
        'scripts/finite-support/positive-factor-enclosure.json.gz',
        'scripts/finite-support/positive-factor-enclosure-verification.json',
        'scripts/finite-support/delsarte-lp-results.json',
        'scripts/finite-support/equilateral-capacity-allowance.json',
        'lemmas/L021-basic-delsarte-support-lp-optimum.md',
        'lemmas/L098-exact-cardinality-normalized-control-obstruction.md',
        'lemmas/L109-capacitated-two-distance-dual-nonseparation.md',
        'lemmas/L110-equilateral-scaling-capacity-allowance-failure.md',
        'lemmas/L111-positive-distance-product-triangle-factors.md',
        'lemmas/L112-enclosed-product-root-passes-distance-five-capacity.md',
        'foundations/04-constant-weight-triple-sdp-source.md',
        'foundations/13-fixed-cardinality-marginal-source.md',
        'foundations/14-validated-nonlinear-enclosure-source.md',
        'drafts/literature/2026-10-23-enclosed-root-all-upper-capacities.md',
    ]
    report['input_sha256'] = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    report['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    save()
    with gzip.open(B/'positive-factor-enclosure.json.gz', 'rt') as f:
        z = json.load(f)
    verified = json.loads((B/'positive-factor-enclosure-verification.json').read_text())
    prior = json.loads((B/'equilateral-capacity-allowance.json').read_text())
    ck('prior_enclosure_binding', verified['stage'] == 'verified' and not verified['failures']
       and verified['input_sha256'] == report['input_sha256'][paths[0]])
    ck('prior_strict_inclusion', z['stage'] == 'exact_complete' and z['inclusion']
       and min(z['inclusion_margins']) > 0 and verified['inclusion_margins'] == z['inclusion_margins'])
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    a = [F(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    N = 65537**28 // 2**128 + 1
    H = comb(1024, 68)
    U = F(comb(1024, 64), comb(68, 64))
    g = [comb(68, i)*comb(956, i) for i in range(69)]
    c = [F(1)]+[F(0)]*4+[(N-1)*a[i-5]/((U-1)*g[i]) for i in range(5, 69)]
    ck('canonical_pairs', len(a) == 64 and min(a) > 0 and sum(a) == U-1
       and c == [F(*v) for v in z['c']] and N == z['N'] and H == z['H'])
    ck('objective_and_endpoint', sum(g[i]*c[i] for i in range(69)) == N
       and (N-1)*2**128 <= 65537**28 < N*2**128)
    Q, radius = z['Q'], z['radius']
    ck('unchanged_box_contract', Q == 10**70 and radius == 10**25 and len(z['point']) == 64
       and z['box'] == [[p-radius, p+radius] for p in z['point']])
    scales = [F(10)**p for p in z['scale_powers']]
    lower = [scales[k]*F(z['point'][k]-radius, Q) for k in range(64)]
    upper = [scales[k]*F(z['point'][k]+radius, Q) for k in range(64)]
    ck('positive_original_endpoints', len(scales) == 64 and all(0 < l < u for l,u in zip(lower, upper)))
    report.update(N=N, H=H, c=[enc(v) for v in c],
                  endpoints=[dict(i=i+5, lower=enc(lower[i]), upper=enc(upper[i])) for i in range(64)])
    counts = Counter()
    classes = {}
    repetitions = []
    shell_sums = []
    for i in range(69):
        if time.monotonic()-started > 300:
            report['stage'] = 'incomplete_budget'; save(); raise TimeoutError(OUT)
        totals = [0]*69
        rep = []
        for j in range(69):
            ts = range(max(0,i+j-68), min(i,j)+1)
            ss = range(max(0,i+j-956), min(i,j)+1)
            left = {t: comb(i,t)*comb(68-i,j-t) for t in ts}
            right = {s: comb(i,s)*comb(956-i,j-s) for s in ss}
            for t in ts:
                for s in ss:
                    h = i+j-t-s
                    D = left[t]*right[s]
                    ck('positive_original_D', D > 0)
                    counts['original'] += 1
                    totals[j] += D
                    if min(i,j,h) == 0:
                        counts['repeated'] += 1
                        ck('repeated_D', D == (g[j] if i == 0 else 1))
                        if i: rep.append([j,t,s,D])
                    elif min(i,j,h) < 5:
                        counts['null'] += 1
                        ck('null_capacity', min(c[i],c[j],c[h]) == 0)
                    else:
                        counts['permitted'] += 1
                        key = tuple(sorted((i,j,h)))
                        if key not in classes:
                            classes[key] = dict(distances=list(key), source_entries=0, sum_D=0,
                                                sum_gD=0, representative=[i,j,t,s])
                        r = classes[key]
                        r['source_entries'] += 1; r['sum_D'] += D; r['sum_gD'] += g[i]*D
        ck('both_endpoint_repetitions', rep == ([] if i == 0 else [[0,0,0,1],[i,i,i,1]]), i)
        ck('complete_shell_sums', totals == g and sum(totals) == H, i)
        repetitions.append(rep); shell_sums.append(totals)
    ck('source_partition', dict(counts) == z['counts'] ==
       dict(original=1500625, repeated=205, null=10220, permitted=1490200))
    actual = set()
    for i in range(5,69):
        for j in range(i,69):
            for h in range(j,69):
                u = i+j-h
                if max(0,i+j-68,u-min(i,j)) <= min(i,j,u-max(0,i+j-956)):
                    actual.add((i,j,h))
    ck('actual_side_criterion', set(classes) == actual and len(actual) == 28215)
    old = {tuple(r['distances']): r for r in prior['permitted_side_classes']}
    ck('prior_class_coverage', set(classes) == set(old) and not prior['failures'])
    verdicts = Counter(); worst_upper = None; worst_lower = None
    rows = []; rejected = []; straddling = []
    for key, r in sorted(classes.items()):
        ck('prior_class_multiplicity', r['source_entries'] == old[key]['source_entries'], list(key))
        capacity = min(c[k] for k in key)
        low = lower[key[0]-5]*lower[key[1]-5]*lower[key[2]-5]/capacity
        high = upper[key[0]-5]*upper[key[1]-5]*upper[key[2]-5]/capacity
        verdict = 'pass' if high <= 1 else 'reject_enclosed_root' if low > 1 else 'straddles'
        ck('positive_ordered_ratios', 0 < low < high)
        r.update(capacity=enc(capacity), lower_ratio=enc(low), upper_ratio=enc(high), verdict=verdict)
        verdicts[verdict] += 1
        if verdict == 'reject_enclosed_root': rejected.append(list(key))
        if verdict == 'straddles': straddling.append(list(key))
        if worst_upper is None or high > worst_upper[0]: worst_upper = high, key
        if worst_lower is None or low > worst_lower[0]: worst_lower = low, key
        rows.append(r)
    report.update(stage='complete', counts=dict(counts), side_class_count=len(rows),
                  shell_sums=shell_sums, endpoint_repetitions=repetitions, classes=rows,
                  verdict_counts=dict(verdicts), rejected_classes=rejected, straddling_classes=straddling,
                  maximum_upper=dict(distances=list(worst_upper[1]), ratio=enc(worst_upper[0])),
                  maximum_lower=dict(distances=list(worst_lower[1]), ratio=enc(worst_lower[0])),
                  required_ratio_at_most=1)
    save()
    with localcontext() as ctx:
        ctx.prec = 18
        maximum = str(Decimal(worst_upper[0].numerator)/Decimal(worst_upper[0].denominator))
    print(json.dumps(dict(stage=report['stage'], checks=report['checks'], failures=len(report['failures']),
          classes=len(rows), verdicts=dict(verdicts), maximum_upper_approx=maximum,
          maximum_class=list(worst_upper[1]), required='<=1', path=str(OUT))))


if __name__ == '__main__':
    main()

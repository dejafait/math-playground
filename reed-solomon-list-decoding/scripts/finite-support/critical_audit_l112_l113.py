"""Fixed-box proof audit. No candidate solve, box change, or new constraint test.

Replays the two full independent verifiers to new output paths, then checks
exact rational polynomial values and collected-power derivatives against the
saved rounded enclosures. All original artifacts remain unchanged.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path
import time

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B/'l112-l113-critical-audit.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    if p.suffix == '.gz':
        with gzip.open(p, 'rt') as f:
            return json.load(f)
    return json.loads(p.read_text())


def enc(x):
    return [x.numerator, x.denominator]


def main(reuse=False):
    start = time.monotonic()
    counts = Counter()
    report = dict(stage='in_progress', failures=[], code_sha256=sha(Path(__file__)))

    def save():
        report.update(checks=sum(counts.values()), checks_by_kind=dict(counts),
                      seconds=time.monotonic()-start)
        OUT.write_text(json.dumps(report, indent=2)+'\n')

    def ck(kind, condition, detail=None):
        counts[kind] += 1
        if not condition:
            report['failures'].append(dict(kind=kind, detail=detail))
            report['stage'] = 'failed'
            save()
            raise AssertionError((kind, detail))

    save()
    replays = [
        ('verify_positive_factor_enclosure.py', 'l112-critical-reverification.json',
         'positive-factor-enclosure-verification.json'),
        ('verify_enclosed_root_all_capacities.py', 'l113-critical-reverification.json',
         'enclosed-root-all-capacities-verification.json')]
    for code, output, original in replays:
        if not reuse:
            spec = importlib.util.spec_from_file_location('replay_'+output[:4], B/code)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            mod.OUT = B/output
            mod.main()
        a, b = read(B/output), read(B/original)
        ck('complete_replayed_evidence', a['stage'] == b['stage'] == 'verified'
           and a['failures'] == b['failures'] == [])
        ck('all_replayed_fields', {k:v for k,v in a.items() if k != 'seconds'} ==
           {k:v for k,v in b.items() if k != 'seconds'}, output)

    z = read(B/'positive-factor-enclosure.json.gz')
    cap = read(B/'enclosed-root-all-capacities.json.gz')
    rv = read(B/'positive-factor-enclosure-verification.json')
    cv = read(B/'enclosed-root-all-capacities-verification.json')
    files = ['positive-factor-enclosure.json.gz',
             'positive-factor-enclosure-verification.json',
             'enclosed-root-all-capacities.json.gz',
             'enclosed-root-all-capacities-verification.json',
             'positive_factor_enclosure.py', 'enclosed_root_all_capacities.py',
             'verify_positive_factor_enclosure.py', 'verify_enclosed_root_all_capacities.py',
             'delsarte-lp-results.json', *[v[1] for v in replays]]
    report['input_sha256'] = {str((B/p).relative_to(ROOT)): sha(B/p) for p in files}
    for p, h in cap['input_sha256'].items():
        ck('all_constructor_input_hashes', sha(ROOT/p) == h, p)
    ck('root_binding', rv['input_sha256'] == sha(B/'positive-factor-enclosure.json.gz'))
    ck('capacity_bindings', cv['source_sha256'] == sha(B/'enclosed-root-all-capacities.json.gz')
       and cv['code_sha256'] == sha(B/'verify_enclosed_root_all_capacities.py')
       and cap['code_sha256'] == sha(B/'enclosed_root_all_capacities.py'))

    Q, radius = z['Q'], z['radius']
    a = [F(p,Q) for p in z['point']]
    lo = [F(p-radius,Q) for p in z['point']]
    hi = [F(p+radius,Q) for p in z['point']]
    scales = [F(10)**p for p in z['scale_powers']]
    demands = [F(*v) for v in z['demands']]
    ck('positive_square_domain', Q == 10**70 and radius == 10**25
       and len(a) == len(lo) == len(hi) == len(scales) == len(demands) == 64
       and all(0 < l < p < u for l,p,u in zip(lo,a,hi))
       and min(scales) > 0 and min(demands) > 0)
    exact_residuals = []
    exact_derivatives = []
    shape_counts = Counter()
    # Positive coefficients and positive box: each collected derivative
    # monomial is increasing in every variable. Thus its exact minimum and
    # maximum are at the common lower and upper corners, including repeats.
    for i, row in enumerate(z['coefficients']):
        val = F(-1)
        low_der = [F(0) for _ in range(64)]
        high_der = [F(0) for _ in range(64)]
        for j,h,D in row:
            ck('positive_monomial_coefficient', D > 0 and 0 <= j <= h < 64)
            exponents = Counter((i,j,h))
            shape_counts[str(tuple(sorted(exponents.values())))] += 1
            b = F(D)*scales[i]*scales[j]*scales[h]/demands[i]
            val += b*prod(a[k]**e for k,e in exponents.items())
            for k,e in exponents.items():
                low_der[k] += b*e*prod(lo[m]**(v-(m == k)) for m,v in exponents.items())
                high_der[k] += b*e*prod(hi[m]**(v-(m == k)) for m,v in exponents.items())
        ck('exact_unrounded_residual_enclosed', F(z['residual'][i][0],Q) <= val <=
           F(z['residual'][i][1],Q), i)
        exact_residuals.append(enc(val))
        row_bounds = []
        for k in range(64):
            jl,jh = z['jacobian'][i][k]
            ck('exact_collected_derivative_enclosed',
               F(jl,Q) <= low_der[k] <= high_der[k] <= F(jh,Q), [i,k])
            row_bounds.append([enc(low_der[k]), enc(high_der[k])])
        exact_derivatives.append(row_bounds)
    ck('complete_polynomial_size', sum(shape_counts.values()) == 81355
       and set(shape_counts) == {'(1, 1, 1)', '(1, 2)', '(3,)'})
    report.update(exact_residuals=exact_residuals,
                  exact_derivative_corner_bounds=exact_derivatives,
                  monomial_multiplicity_shapes=dict(shape_counts))
    margins = [min(l+radius, radius-u) for l,u in z['krawczyk_image']]
    row_norms = [sum(max(abs(l),abs(u)) for l,u in row) for row in z['defect']]
    ck('all_manuscript_inclusion_margins', margins == z['inclusion_margins'] == rv['inclusion_margins']
       and min(margins) == 9999999999999999999196016 > 0)
    ck('manuscript_defect_norm', max(row_norms) == 21421458450760567325986134
       and max(row_norms) < Q and rv['max_defect_row_l1'] == [max(row_norms),Q])
    report.update(minimum_margin_units=min(margins), required_margin_units='>0',
                  max_defect_row_l1=[max(row_norms),Q], required_defect_norm='<1')

    # Every full class record was reconstructed above by the six-presentation
    # verifier. Independently verify all capacity ratios directly in x units.
    c = [F(*v) for v in z['c']]
    xl = [l*s for l,s in zip(lo,scales)]
    xu = [u*s for u,s in zip(hi,scales)]
    ck('repetition_upper_caps', c[0] == 1 and c[1:5] == [0]*4
       and all(0 < v <= 1 for v in c[5:]))
    maxima = [None,None]
    for row in cap['classes']:
        key = row['distances']
        capacity = min(c[k] for k in key)
        ratios = [prod(xs[k-5] for k in key)/capacity for xs in (xl,xu)]
        ck('full_class_ratios_and_strict_upper', 0 < ratios[0] < ratios[1] < 1
           and enc(ratios[0]) == row['lower_ratio'] and enc(ratios[1]) == row['upper_ratio']
           and row['verdict'] == 'pass', key)
        for endpoint, ratio in enumerate(ratios):
            if maxima[endpoint] is None or ratio > maxima[endpoint][0]:
                maxima[endpoint] = ratio,key
    for endpoint,name in enumerate(('maximum_lower','maximum_upper')):
        value,key = maxima[endpoint]
        record = dict(distances=key, ratio=enc(value))
        ck('complete_extrema', record == cap[name] == cv[name], name)
        report[name] = record
    ck('manuscript_maximum_classes', maxima[0][1] == [5,5,5] and maxima[1][1] == [5,5,6])
    ck('manuscript_strict_ratio_bracket', F(107,10**13) < maxima[1][0] < F(108,10**13) < 1)
    ck('distance_five_capacity_consistency',
       enc(xl[0]**3/c[5]) == z['capacity']['lower_cube_ratio'] == rv['capacity']['lower_cube_ratio']
       and enc(xu[0]**3/c[5]) == z['capacity']['upper_cube_ratio'] == rv['capacity']['upper_cube_ratio'])
    ck('source_partition_manuscript', cap['counts'] == z['counts'] ==
       dict(original=1500625,repeated=205,null=10220,permitted=1490200)
       and cap['side_class_count'] == len(cap['classes']) == 28215
       and cap['verdict_counts'] == {'pass':28215}
       and cap['rejected_classes'] == cap['straddling_classes'] == [])
    report.update(stage='verified', root_replay_checks=read(B/replays[0][1])['checks'],
                  capacity_replay_checks=read(B/replays[1][1])['checks'],
                  side_classes=28215, required_upper_ratio=1,
                  scope='Fixed-box root, full source coverage and upper capacities only.')
    save()
    print(json.dumps({k:report[k] for k in ('stage','checks','root_replay_checks','capacity_replay_checks',
          'minimum_margin_units','required_margin_units','side_classes','required_upper_ratio')}))
    print('Maximum upper ratio: 107/10^13 < B < 108/10^13; failures: 0; certificate:', OUT)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--reuse-replays', action='store_true', help='Use complete existing audit replay files.')
    main(parser.parse_args().reuse_replays)

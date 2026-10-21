#!/usr/bin/env python3
"""L043 audit: full replay, distinct exact-endpoint sum, targeted corruptions.

External homology, coefficient, optimality and period premises remain in
L043. This script neither proves them nor imports the certificate producer.
"""
import copy
import importlib.util
import json
import sys
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE / 'critical-audit'
sys.set_int_max_str_digits(0)


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + '\n')


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def need(condition, message):
    if not condition:
        raise ValueError(message)


def fresh_replay(data, directory):
    directory.mkdir(parents=True, exist_ok=True)
    spec = importlib.util.spec_from_file_location('absolute_checker', HERE / 'verify_certificate.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Change only the report directory; mathematical inputs retain their paths.
    module.HERE = directory
    checks, failures, summary = [], [], None
    try:
        summary = module.replay(data, checks)
    except Exception as error:
        failures.append(type(error).__name__ + ': ' + str(error))
    path = directory / 'input.json'
    save(path, data)
    report = {'input_sha256': digest(path), 'checker_sha256': digest(HERE / 'verify_certificate.py'),
              'summary': summary, 'checks': checks, 'checks_passed': len(checks), 'failures': failures}
    save(directory / 'verification.json', report)
    return report


def independent_enclosure(data):
    """New 64-bit elementary bounds; direct powers; no intermediate rounding.

    Complete replay has already established each input Fourier coefficient.
    Every rational endpoint of every new term is retained below.
    """
    workscale = 1 << 64

    def outward(x, scale=workscale):
        return [(x[0] * scale).__floor__(), -((-x[1] * scale).__floor__())]

    def grid(x):
        return [F(v, workscale) for v in outward(x)]

    def multiply(x, y):
        values = [a * b for a in x for b in y]
        return [min(values), max(values)]

    def atan_bounds(d):
        lower = sum((F((-1)**j, (2*j+1)*d**(2*j+1)) for j in range(40)), F(0))
        return [lower, lower + F(1, 81*d**81)]

    a, b = atan_bounds(5), atan_bounds(239)
    pi_raw = [16*a[0]-4*b[1], 16*a[1]-4*b[0]]
    pi = grid(pi_raw)
    h = [2*x/11 for x in pi]
    need(0 < h[0] <= h[1] < 1, 'exponential alternating domain')

    def exp_bounds(x):
        upper = sum(((-x)**j/factorial(j) for j in range(51)), F(0))
        return [upper + (-x)**51/factorial(51), upper]

    ends = [exp_bounds(x) for x in h]
    r_raw = [ends[1][0], ends[0][1]]
    r = grid(r_raw)
    need(0 < r[0] <= r[1] < 1, 'geometric tail domain')
    cosines, cosine_evidence = [], []
    for j in range(6):
        angles = [2*j*x/11 for x in pi]
        mid, radius = sum(angles)/2, (angles[1]-angles[0])/2
        polynomial = sum((F((-1)**k)*mid**(2*k)/factorial(2*k) for k in range(31)), F(0))
        error = abs(mid)**62/factorial(62)+radius
        interval = grid([polynomial-error, polynomial+error])
        cosines.append(interval)
        cosine_evidence.append({'j': j, 'angles': list(map(str, angles)), 'midpoint': str(mid),
                                'radius': str(radius), 'polynomial': str(polynomial),
                                'error': str(error), 'interval': list(map(str, interval))})

    def cosine(k):
        k %= 11
        return cosines[min(k, 11-k)]

    coefficients = data['fourier']['coefficients']
    partial, terms = [F(0), F(0)], []
    for n in range(1, 65):
        # Direct exact powers replace the original repeated dyadic rounding.
        power = [x**n for x in r]
        end, start = cosine(-5*n), cosine(-2*n)
        difference = [end[0]-start[1], end[1]-start[0]]
        term = sorted(x*F(coefficients[n], n) for x in multiply(power, difference))
        partial = [partial[k]+term[k] for k in range(2)]
        terms.append({'n': n, 'a_n': coefficients[n], 'power': list(map(str, power)),
                      'difference': list(map(str, difference)), 'term': list(map(str, term)),
                      'partial': list(map(str, partial))})
    tail = 2*r[1]**65/(1-r[1])
    exact_period = [partial[0]-tail, partial[1]+tail]
    scale = data['fourier']['scale']
    rounded = outward(exact_period, scale)
    old = data['fourier']['period_interval']
    need(old[0] <= rounded[0] <= rounded[1] <= old[1] < 0,
         'distinct exact enclosure must be negative and contained in original')
    evidence = {'workscale': workscale, 'atan_terms': 40, 'exponential_degree': 50,
                'cosine_degree': 60, 'atan_bounds': [list(map(str, a)), list(map(str, b))],
                'pi_exact': list(map(str, pi_raw)), 'pi_dyadic': list(map(str, pi)),
                'h': list(map(str, h)), 'exp_endpoint_bounds': [list(map(str, x)) for x in ends],
                'r_exact': list(map(str, r_raw)), 'r_dyadic': list(map(str, r)),
                'cosines': cosine_evidence, 'terms': terms, 'finite_sum': list(map(str, partial)),
                'tail': str(tail), 'exact_period': list(map(str, exact_period)),
                'outward_period': rounded, 'scale': scale, 'failures': []}
    save(OUT / 'independent-fourier.json', evidence)
    return {'terms_actual': len(terms), 'terms_required': 64, 'outward_period': rounded,
            'scale': scale, 'required_upper': 0, 'tail_upper_units': outward([tail, tail], scale)[1]}


def main():
    OUT.mkdir(exist_ok=True)
    summary, failures = {}, []
    manifest = {}
    try:
        files = [HERE / name for name in ('certificate.json', 'verification.json', 'comparison.json',
                 'development-failure-01.json', 'build_certificate.py', 'verify_certificate.py', 'audit_certificate.py')]
        files += [HERE.parent / name for name in ('structural-certificate.json', 'dual-certificate.json',
                  'arithmetic-input.json', 'arithmetic-certificate.json')]
        files += [ROOT / 'scripts' / name / 'verify_certificate.py' for name in ('general-relative', 'dual-kernel')]
        files += [HERE / 'upstream-replay/dual-verification.json',
                  HERE / 'upstream-replay/dual-verification-structure/general-verification.json']
        for path in files:
            key = str(path.relative_to(ROOT))
            manifest[key] = digest(path)
            target = OUT / 'originals' / key
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(path.read_bytes())
        save(OUT / 'pre-replay-manifest.json', manifest)
        data = json.loads((HERE / 'certificate.json').read_text())
        original = json.loads((HERE / 'verification.json').read_text())
        need(original['certificate_sha256'] == digest(HERE / 'certificate.json'), 'original certificate binding')
        need(original['checker_sha256'] == digest(HERE / 'verify_certificate.py'), 'original checker binding')
        fresh = fresh_replay(data, OUT / 'full-replay')
        need(not fresh['failures'], 'full replay: ' + str(fresh['failures']))
        need(fresh['summary'] == original['summary'] and fresh['checks'] == original['checks'],
             'entire replay summary/check list differs')
        structural = json.loads((OUT / 'full-replay/upstream-replay/dual-verification-structure/general-verification.json').read_text())
        old_structural = json.loads((HERE / 'upstream-replay/dual-verification-structure/general-verification.json').read_text())
        need(structural == old_structural and not structural['failures'], 'complete structural replay differs')
        summary['full_replay'] = fresh['summary']
        summary['checks_passed'] = fresh['checks_passed']
        summary['upstream_actual'] = structural['actual']
        summary['upstream_required'] = structural['required']
        summary['independent_enclosure'] = independent_enclosure(data)

        mutations = [
            ('boundary-sign', ('boundary', 'quotient_reduced', 2), 1, 'integral quotient boundary'),
            ('kernel-index', ('kernel', 'unimodular_transform', 0, 1), 2, 'both unimodular inverse products'),
            ('primitive-image', ('kernel', 'bezout', 0), 0, 'full image gcd and complete Bezout'),
            ('cycle-orientation', ('cycle', 'path'), [[-1, 2], [0, 1]], 'oriented cycle is reversed generator 3'),
            ('last-fourier-term', ('fourier', 'terms', 63, 'term', 0), 1, 'complete oriented term 64'),
            ('omitted-tail', ('fourier', 'tail_upper'), 0, 'Wuthrich full two-series geometric tail'),
            ('period-factor-two', ('normalization', 'beta_over_total_period'), '2/5', 'signed total-period scale, not least real projection'),
        ]
        rejected = []
        for name, path, value, expected in mutations:
            altered = copy.deepcopy(data)
            cursor = altered
            for key in path[:-1]:
                cursor = cursor[key]
            cursor[path[-1]] = value
            report = fresh_replay(altered, OUT / 'altered' / name)
            need(report['failures'] == ['ValueError: '+expected], name+' rejection differs: '+str(report['failures']))
            rejected.append({'case': name, 'expected': expected, 'failures': report['failures']})
        summary['expected_rejections'] = rejected

        # Final comparison only after recovery/replay and independent sign test.
        calibration_path = HERE.parent / 'calibrated-symbols/certificate.json'
        calibration = json.loads(calibration_path.read_text())
        comparison = json.loads((HERE / 'comparison.json').read_text())
        need(comparison['absolute_certificate_sha256'] == digest(HERE / 'certificate.json')
             and comparison['twist_normalized_certificate_sha256'] == digest(calibration_path), 'comparison byte bindings')
        need(F(calibration['scale']) == F(data['normalization']['beta_over_total_period']) == F(1, 5), 'final scalar comparison')
        need(list(map(F, calibration['integral_generator_values'])) == list(map(F, data['normalization']['generator_values'])), 'all twelve final comparison values')
        summary['comparison'] = {'scalar': '1/5', 'all_generator_values_actual': 12,
                                  'all_generator_values_required': 12, 'calibration_sha256': digest(calibration_path)}
        for path, expected in manifest.items():
            need(digest(ROOT / path) == expected, 'original changed: '+path)
        summary['original_files_unchanged'] = len(manifest)
    except Exception as error:
        failures.append(type(error).__name__+': '+str(error))
    save(OUT / 'audit.json', {'audit_program_sha256': digest(Path(__file__)),
                            'summary': summary, 'failures': failures})
    print('L043 audit:', 'PASS' if not failures else 'FAIL', '; failures:', failures)
    if 'independent_enclosure' in summary:
        print('Independent Fourier actual/required bounds:', summary['independent_enclosure'])
    print('Complete report:', OUT / 'audit.json')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

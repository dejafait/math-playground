#!/usr/bin/env python3
"""L044: isolated actual-main replay, distinct exact sum, persisted rejections.

Named mathematical inputs and retained source qualifications are in L044.
No producer or calibrated/twist value is used in the independent recovery.
"""
import copy
import json
import subprocess
import sys
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
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


def fresh_main(data, directory, expected=None):
    """Execute the unchanged main, including its own failure report writer."""
    scripts = directory / 'scripts'
    scripts.mkdir(parents=True, exist_ok=True)
    for name in ('relative-t2', 'dual-kernel'):
        link = scripts / name
        if not link.exists():
            link.symlink_to(ROOT / 'scripts' / name, target_is_directory=True)
    local = scripts / HERE.name
    local.mkdir(exist_ok=True)
    checker = local / 'verify_certificate.py'
    checker.write_bytes((HERE / checker.name).read_bytes())
    path, report_path = local / 'certificate.json', local / 'verification.json'
    save(path, data)
    sentinel = {'stale_sentinel': True, 'certificate_sha256': 'not-current', 'failures': []}
    save(report_path, sentinel)
    result = subprocess.run([sys.executable, str(checker)], capture_output=True, text=True)
    (directory / 'main-output.txt').write_text(result.stdout + result.stderr)
    report = json.loads(report_path.read_text())
    need(report != sentinel and report_path.stat().st_size > 0, 'fresh report not persisted')
    need(report['certificate_sha256'] == digest(path), 'report does not bind actual input')
    need(report['checker_sha256'] == digest(checker) == digest(HERE / checker.name), 'checker byte mismatch')
    if expected is None:
        need(result.returncode == 0 and report['failures'] == [], 'full replay failed: '+str(report['failures']))
    else:
        need(result.returncode != 0 and report['failures'] == ['ValueError: '+expected]
             and report['summary'] is None, 'wrong rejection: '+str(report['failures']))
    return report, {'input': str(path.relative_to(ROOT)), 'report': str(report_path.relative_to(ROOT)),
                    'input_sha256': digest(path), 'report_sha256': digest(report_path),
                    'exit_code': result.returncode, 'failures': report['failures'],
                    'stale_report_replaced': True}


def independent_enclosure(data):
    """Separate elementary degrees and exact powers/sums; no rounded recurrence."""
    D = 1 << 64

    def outward(x):
        return [(x[0]*D).__floor__(), -((-x[1]*D).__floor__())]

    def grid(x):
        return [F(v, D) for v in outward(x)]

    def multiply(x, y):
        v = [a*b for a in x for b in y]
        return [min(v), max(v)]

    def atan(d):
        lo = sum((F((-1)**j, (2*j+1)*d**(2*j+1)) for j in range(40)), F(0))
        return [lo, lo+F(1, 81*d**81)]

    ab = [atan(5), atan(239)]
    pi_raw = [16*ab[0][0]-4*ab[1][1], 16*ab[0][1]-4*ab[1][0]]
    pi = grid(pi_raw)
    h = [2*x/389 for x in pi]
    need(0 < h[0] <= h[1] < 1, 'independent exponential domain')

    def exponential(x):
        hi = sum(((-x)**j/factorial(j) for j in range(51)), F(0))
        return [hi+(-x)**51/factorial(51), hi]

    ex = [exponential(x) for x in h]
    r_raw = [ex[1][0], ex[0][1]]
    r = grid(r_raw)
    need(0 < r[0] <= r[1] < 1, 'independent full-tail domain')
    cs, evidence = {}, []
    for j in range(195):
        theta = [2*j*x/389 for x in pi]
        mid, radius = sum(theta)/2, (theta[1]-theta[0])/2
        polynomial = sum((F((-1)**k)*mid**(2*k)/factorial(2*k) for k in range(31)), F(0))
        error = abs(mid)**62/factorial(62)+radius
        interval = grid([polynomial-error, polynomial+error])
        cs[j] = interval
        evidence.append({'j': j, 'theta': list(map(str, theta)), 'midpoint': str(mid),
                         'radius': str(radius), 'polynomial': str(polynomial), 'error': str(error),
                         'interval': list(map(str, interval))})

    def cosine(k):
        k %= 389
        return cs[min(k, 389-k)]

    # Complete model-derived coefficients were independently replayed above.
    coeffs = data['attempts'][0]['fourier']['coefficients']
    need(data['candidates'][0]['matrix'] == [-78, 1, 389, -5]
         and data['selected_attempt'] == 0, 'independent exact geometry/schedule')
    partial, terms = [F(0), F(0)], []
    for n in range(1, 257):
        powers = [x**n for x in r]
        end, start = cosine(-78*n), cosine(5*n)
        difference = [end[0]-start[1], end[1]-start[0]]
        term = sorted(x*F(coeffs[n], n) for x in multiply(powers, difference))
        partial = [partial[k]+term[k] for k in range(2)]
        terms.append({'n': n, 'a_n': coeffs[n], 'powers': list(map(str, powers)),
                      'difference': list(map(str, difference)), 'term': list(map(str, term)),
                      'partial': list(map(str, partial))})
    tail = 2*r[1]**257/(1-r[1])
    period = [partial[0]-tail, partial[1]+tail]
    rounded = outward(period)
    need(rounded[0] > 0, 'independent sign failed')
    artifact = {'atan_terms': 40, 'atan_brackets': [list(map(str, x)) for x in ab],
                'pi_exact': list(map(str, pi_raw)), 'pi': list(map(str, pi)),
                'h': list(map(str, h)), 'exponential_degree': 50,
                'exponential_brackets': [list(map(str, x)) for x in ex],
                'r_exact': list(map(str, r_raw)), 'r': list(map(str, r)),
                'cosine_degree': 60, 'cosines': evidence, 'terms': terms,
                'finite_sum': list(map(str, partial)), 'tail': str(tail),
                'period': list(map(str, period)), 'outward_period': rounded,
                'scale': D, 'failures': []}
    save(OUT / 'independent-fourier.json', artifact)
    return {'terms_actual': len(terms), 'terms_required': 256, 'outward_period': rounded,
            'scale': D, 'required_lower_bound': 0, 'tail_upper_units': outward([tail, tail])[1],
            'finite_sum_outward': outward(partial), 'complete_evidence_sha256': digest(OUT / 'independent-fourier.json')}


def main():
    OUT.mkdir(exist_ok=True)
    summary, failures, manifest = {}, [], {}
    try:
        files = [p for p in HERE.rglob('*') if p.is_file() and OUT not in p.parents
                 and '__pycache__' not in p.parts]
        files += [ROOT/'scripts/relative-t2'/name for name in
                  ('certificate.json', 'verify_certificate.py', 'audit_certificate.py')]
        files += [ROOT/'scripts/dual-kernel'/name for name in
                  ('conductor389-certificate.json', 'conductor389-arithmetic.json', 'verify_certificate.py')]
        for path in files:
            key = str(path.relative_to(ROOT))
            manifest[key] = digest(path)
        save(OUT / 'pre-replay-manifest.json', manifest)
        data = json.loads((HERE/'certificate.json').read_text())
        original = json.loads((HERE/'verification.json').read_text())
        need(original['certificate_sha256'] == digest(HERE/'certificate.json')
             and original['checker_sha256'] == digest(HERE/'verify_certificate.py'), 'original byte bindings')
        fresh, record = fresh_main(data, OUT/'full-replay')
        need(fresh['checks'] == original['checks'] and fresh['summary'] == original['summary'], 'complete replay differs')
        summary['full_replay'] = record
        summary['checks_passed'] = fresh['checks_passed']
        summary['actual_required'] = fresh['summary']
        upstream = OUT/'full-replay/scripts'/HERE.name/'upstream-replay'
        for name in ('fixed-audit.json', 'fixed-verification.json'):
            report = json.loads((upstream/'dual-verification-structure'/name).read_text())
            old = json.loads((HERE/'upstream-replay/dual-verification-structure'/name).read_text())
            need(report == old and not report['failures'], 'entire structural report differs: '+name)
        print('Fresh full structural/dual/absolute replay passed:', fresh['checks_passed'], 'checks', flush=True)
        summary['independent_enclosure'] = independent_enclosure(data)
        print('Independent sign actual/required:', summary['independent_enclosure'], flush=True)
        save(OUT/'audit-checkpoint.json', {'summary': summary, 'failures': [], 'state': 'mutation tests pending'})
        mutations = [
            ('input-binding', ('inputs', 'scripts/relative-t2/certificate.json'), '0'*64, 'complete input bindings'),
            ('component-scope', ('source_scope', 'components'), 1, 'exact source scope'),
            ('cusp-orientation', ('candidates', 0, 'path'), [[-1,5],[0,1]], 'complete oriented raw cycle'),
            ('kernel-inverse', ('kernel', 'inverse', 0, 0), 1, 'both unimodular inverse products'),
            ('image-primitivity', ('kernel', 'bezout', 57), 0, 'complete gcd Bezout primitivity'),
            ('fourier-coefficient', ('attempts', 0, 'fourier', 'coefficients', 256), 0, 'every model-derived Fourier coefficient'),
            ('full-tail', ('attempts', 0, 'fourier', 'tail_upper'), 0, 'full two-series geometric remainder'),
            ('last-normalized-value', ('normalization', 'generator_values', 389), '999', 'all 390 normalized generators'),
        ]
        rejected = []
        summary['rejections'] = rejected
        for name, keys, value, expected in mutations:
            altered = copy.deepcopy(data)
            cursor = altered
            for key in keys[:-1]:
                cursor = cursor[key]
            need(cursor[keys[-1]] != value, 'mutation unchanged: '+name)
            cursor[keys[-1]] = value
            report, record = fresh_main(altered, OUT/'altered'/name, expected)
            need(record['input_sha256'] != digest(HERE/'certificate.json'), 'mutation bytes unchanged')
            rejected.append({'case': name, 'expected': expected, **record})
            save(OUT/'audit-checkpoint.json', {'summary': summary, 'failures': [], 'state': 'mutation tests in progress'})
            print('Rejected with fresh byte-bound report:', name, flush=True)
        # First read of L032 evidence: final comparison after independent recovery.
        path = ROOT/'scripts/calibrated-symbols/certificate.json'
        old = json.loads(path.read_text())
        need(data['inputs']['scripts/relative-t2/certificate.json'] == old['input_sha256']['scripts/relative-t2/certificate.json'], 'comparison structural bytes')
        need(F(old['scale']) == F(data['normalization']['beta_over_total_period']) == -1, 'final scale comparison')
        need(len(old['integral_generator_values']) == 390 and list(map(F, old['integral_generator_values']))
             == list(map(F, data['normalization']['generator_values'])), 'all final comparison values')
        need(old['denominator']['lcm'] == data['normalization']['common_denominator'] == 2, 'final denominator comparison')
        summary['post_recovery_comparison'] = {'L032_sha256': digest(path), 'values_actual': 390,
                                              'values_required': 390, 'scalar': '-1', 'denominator': 2}
    except Exception as error:
        failures.append(type(error).__name__+': '+str(error))
    changed = [key for key, value in manifest.items() if digest(ROOT/key) != value]
    if changed:
        failures.append('Original bytes changed: '+str(changed))
    summary['original_files_unchanged'] = len(manifest)-len(changed)
    save(OUT/'audit.json', {'audit_program_sha256': digest(Path(__file__)), 'summary': summary, 'failures': failures})
    print('L044 audit:', 'FAIL' if failures else 'PASS', '; failures:', failures,
          '; complete report:', OUT/'audit.json', flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

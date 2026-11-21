"""Exact low-mode inequality used for the smooth flat-exterior phase lift.

Retains L778's full coefficient intervals and analytic error. The analytic
implication and all omitted positive terms are justified in L851.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'scripts/actual-fredholm/fixed-pair-certificate-431.json'


def interval_add(a, b):
    return a[0]+b[0], a[1]+b[1]


def scalar_mul(a, x):
    ends = (a[0]*x, a[1]*x)
    return min(ends), max(ends)


def pair(a):
    return [str(a[0]), str(a[1])]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='exterior-phase-certificate.json')
    args = parser.parse_args()
    output = Path(__file__).with_name(args.output)
    if output.exists():
        raise SystemExit('Preserve existing evidence; choose a fresh output name.')
    raw = SOURCE.read_bytes()
    data = json.loads(raw)['evaluation']
    coefficients = [tuple(Q(x) for x in c) for c in data['coefficients']]
    error = Q(data['uniform_G_error'][1])
    disk = Q(1600)
    checks, failures = [], []

    def check(name, passed, actual, required):
        checks.append(dict(name=name, passed=bool(passed), actual=actual, required=required))
        if not passed:
            failures.append(name)

    check('inherited disk and degree', data['uniform_disk_radius'] == 1600 and len(coefficients) == 97,
          [data['uniform_disk_radius'], len(coefficients)], '[1600, 97]')
    check('ordered coefficient intervals', all(lo <= hi for lo, hi in coefficients),
          all(lo <= hi for lo, hi in coefficients), True)
    check('full analytic error', 0 <= error < Q('3.141e-48'), str(error), '0 <= E < 3.141e-48')
    if failures:
        raise RuntimeError('Inherited input contract failed: '+str(failures))

    radius = (Q('184.82837518'), Q('184.82837520'))

    def saddle_enclosure(x):
        # P is the exact polynomial with coefficients in the inherited boxes.
        # Cauchy centered at x gives |(G-P)'(x)| <= E/(1600-x).
        value = (Q(0), Q(0))
        for n in range(len(coefficients)-1, -1, -1):
            value = interval_add(scalar_mul(value, x), scalar_mul(coefficients[n], n-1))
        tail = error*disk/(disk-x)
        return value[0]-tail, value[1]+tail

    saddle_low, saddle_high = [saddle_enclosure(x) for x in radius]
    check('lower saddle sign', saddle_low[1] < 0, pair(saddle_low), 'upper endpoint < 0')
    check('upper saddle sign', saddle_high[0] > 0, pair(saddle_high), 'lower endpoint > 0')

    retained = 12
    actual_coefficients, scaled = [], []
    for n in range(retained):
        uncertainty = error/disk**n
        bound = (coefficients[n][0]-uncertainty, coefficients[n][1]+uncertainty)
        actual_coefficients.append(bound)
        scaled.append((bound[0]*radius[0]**n, bound[1]*radius[1]**n))
    check('positive retained coefficient lower bounds', all(c[0] > 0 for c in actual_coefficients),
          all(c[0] > 0 for c in actual_coefficients), True)

    modes, terms = {}, {}
    for k in (1, 2, 3):
        entries = []
        for n in range(retained-k):
            weight = 2*n+k-2
            endpoint = 1 if weight < 0 else 0
            value = weight*scaled[n][endpoint]*scaled[n+k][endpoint]
            entries.append(dict(n=n, weight=weight, bound=str(value)))
        terms[str(k)] = entries
        modes[k] = sum(Q(t['bound']) for t in entries)
    check('positive second and third mode lower bounds', modes[2] > 0 and modes[3] > 0,
          [str(modes[2]), str(modes[3])], 'both > 0')
    if modes[3] <= 0:
        raise RuntimeError('Quadratic completion needs positive third mode.')
    margin = modes[1]+modes[2]-modes[2]**2/(4*modes[3])
    check('uniform quadratic phase margin', margin > Q(1, 4000), str(margin), '> 1/4000 > 0')
    result = dict(status='PASS_PENDING_INDEPENDENT_AUDIT' if not failures else 'FAIL',
                  input_path=str(SOURCE.relative_to(ROOT)), input_sha256=hashlib.sha256(raw).hexdigest(),
                  arithmetic='Python Fraction exact rational operations',
                  inherited_qualification='L778(2)-(5), step433 analytic/software input; not rebuilt',
                  inherited_coefficients=data['coefficients'], inherited_uniform_G_error=data['uniform_G_error'],
                  inherited_disk_radius=data['uniform_disk_radius'], radius=pair(radius),
                  saddle_enclosures=[pair(saddle_low), pair(saddle_high)], retained_count=retained,
                  actual_coefficient_bounds=[pair(c) for c in actual_coefficients],
                  scaled_coefficient_bounds=[pair(c) for c in scaled], lower_mode_terms=terms,
                  lower_modes={str(k): str(v) for k, v in modes.items()},
                  phase_margin=str(margin), checks=checks, failures=failures,
                  limitation='Certifies the analytic phase inequality used for an exterior lift only; no transition or full-torus solution.')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(result['status'])
    print('R bracket:', *map(str, radius))
    print('Saddle upper at lower R:', format(float(saddle_low[1]), '.12g'), '; required < 0')
    print('Saddle lower at upper R:', format(float(saddle_high[0]), '.12g'), '; required > 0')
    print('Phase margin:', format(float(margin), '.12g'), '; required > 1/4000 = 0.00025')
    print('Checks:', len(checks), '; failures:', failures)
    print('Full certificate:', output.relative_to(ROOT))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

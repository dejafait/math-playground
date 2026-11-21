"""Exact rational checks for the flat-exterior test in L850.

Reuses L778's audited coefficient intervals and full analytic error.
Writes every input and cell enclosure; does not overwrite evidence.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / 'scripts/actual-fredholm/fixed-pair-certificate-431.json'


def mul(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def pair(x):
    return [str(x[0]), str(x[1])]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='linear-phase-exterior-bounds.json')
    args = parser.parse_args()
    output = Path(__file__).with_name(args.output)
    if output.exists():
        raise SystemExit('Preserve existing evidence; use a fresh --output name.')
    raw = INPUT.read_bytes()
    data = json.loads(raw)['evaluation']
    coefficients = [tuple(Q(x) for x in c) for c in data['coefficients']]
    error = Q(data['uniform_G_error'][1])
    checks, failures = [], []

    def check(name, passed, actual, required):
        checks.append(dict(name=name, passed=bool(passed), actual=actual,
                           required=required))
        if not passed:
            failures.append(name)

    check('inherited disk', data['uniform_disk_radius'] == 1600,
          data['uniform_disk_radius'], 1600)
    check('all polynomial coefficients', len(coefficients) == 97,
          len(coefficients), 97)
    check('ordered input intervals', all(c[0] <= c[1] for c in coefficients),
          all(c[0] <= c[1] for c in coefficients), True)
    check('full analytic error', 0 <= error < Q('3.141e-48'),
          str(error), '0 <= error < 3.141e-48')
    if failures:
        raise RuntimeError('Input contract failed: '+str(failures))

    # Cauchy's coefficient estimate for the entire difference G-P_0.
    a0_upper = coefficients[0][1]+error
    a2_lower = coefficients[2][0]-error/Q(1600)**2
    saddle_margin = Q(256)**2*a2_lower-a0_upper
    check('R_1 < 256 from positive coefficients', saddle_margin > Q('0.001'),
          str(saddle_margin), '> 0.001 > 0')

    cells = []
    for j in range(256):
        interval = (Q(-j-1), Q(-j))
        value = coefficients[-1]
        for c in reversed(coefficients[:-1]):
            value = add(mul(value, interval), c)
        enclosure = (value[0]-error, value[1]+error)
        cells.append(dict(x=[j, j+1], G_minus_x=pair(enclosure)))
    minimum = min(Q(c['G_minus_x'][0]) for c in cells)
    check('all cells retained and contiguous',
          [c['x'] for c in cells] == [[j, j+1] for j in range(256)],
          len(cells), '256 exact consecutive unit cells covering [0,256]')
    check('G(-x) positive on the complete interval', minimum > Q('0.01'),
          str(minimum), '> 0.01 > 0 for every x in [0,256]')

    result = dict(
        status='PASS_PENDING_INDEPENDENT_AUDIT' if not failures else 'FAIL',
        input_path=str(INPUT.relative_to(ROOT)),
        input_sha256=hashlib.sha256(raw).hexdigest(),
        arithmetic='Python Fraction exact rational operations',
        inherited_qualification='L778(2)-(5) and step433 analytic/software input; not rebuilt',
        inherited_coefficients=data['coefficients'],
        inherited_uniform_disk_radius=data['uniform_disk_radius'],
        inherited_uniform_G_error=data['uniform_G_error'],
        coefficient_bounds=dict(a0_upper=str(a0_upper), a2_lower=str(a2_lower)),
        cells=cells, checks=checks, failures=failures,
        summary=dict(saddle_margin_lower=str(saddle_margin),
                     G_negative_interval_lower=str(minimum),
                     required_saddle_margin='>0', required_G_lower='>0'),
        limitation='Bounds support only the matrix-inversion test, not linear solvability or a full range obstruction.')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(result['status'])
    print('Saddle margin lower (display):', format(float(saddle_margin), '.12g'), '; required > 0')
    print('G(-x) interval lower (display):', format(float(minimum), '.12g'), '; required > 0')
    print('Exact checks and all 256 enclosures:', output.relative_to(ROOT))
    print('Failures:', failures)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

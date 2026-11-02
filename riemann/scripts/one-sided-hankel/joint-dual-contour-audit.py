#!/usr/bin/env python3
"""Replay C645x arithmetic; the conceptual proof audit is in its lemma."""

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import subprocess
import sys


def rat(obj):
    return F(int(obj['numerator']), int(obj['denominator']))


def encode(q):
    return {'numerator': str(q.numerator), 'denominator': str(q.denominator)}


def main():
    base = Path(__file__).resolve().parent
    certificate = base / 'joint-dual-contour-certificate.json'
    before = certificate.read_bytes()
    run = subprocess.run(
        [sys.executable, str(base / 'joint-dual-contour-certificate.py')],
        capture_output=True, text=True, check=True,
    )
    after = certificate.read_bytes()
    data = json.loads(after)
    logs, checks = {}, {}

    # Independently accumulate the proved log series with 96 terms.
    for name, item in data['log_bounds'].items():
        q = rat(item['argument'])
        v = (q - 1) / (q + 1)
        power, partial = v, F(0)
        for k in range(96):
            partial += 2 * power / (2 * k + 1)
            power *= v * v
        remainder = 2 * power / (193 * (1 - v * v))
        logs[name] = (partial, partial + remainder)
        checks['log_containment_' + name] = (
            rat(item['lower']) <= partial <= partial + remainder <= rat(item['upper'])
        )

    # Form coefficients from the antiderivatives, not saved expressions.
    R, d, U = F(11, 8), F(5, 4), F(121, 64)
    expressions = {'lambda': [(F(1), R / d), (1 + U / d, 1 + d / U), (-(1 + d), 1 + 1 / d)]}
    for label, r in [('kappa_31_25', F(31, 25)), ('kappa_9_8', F(9, 8))]:
        expressions[label] = [(F(1), R / r), ((U - r) / r, U / (U - r)), (-(r - 1), r / (r - 1))]
    rounded, values = {}, {}
    for name, expression in expressions.items():
        lo = hi = F(0)
        actual = []
        for coefficient, argument in expression:
            key = str(argument)
            low, high = logs[key]
            lo += coefficient * (low if coefficient > 0 else high)
            hi += coefficient * (high if coefficient > 0 else low)
            actual.append((coefficient, key))
        expected = [(rat(item['coefficient']), item['log']) for item in data['expressions'][name]]
        checks['analytic_expression_' + name] = actual == expected
        stored = data['rounded_value_bounds'][name]
        checks['rounded_containment_' + name] = rat(stored['lower']) <= lo <= hi <= rat(stored['upper'])
        scale = 10 ** 12
        lower, upper = F((lo * scale).__floor__(), scale), F((hi * scale).__ceil__(), scale)
        rounded[name] = {'lower': encode(lower), 'upper': encode(upper)}
        values[name] = {'lower': encode(lo), 'upper': encode(hi)}

    checks['replay_byte_identical'] = before == after
    checks['all_original_checks_pass'] = (
        all(item['pass'] for item in data['checks'].values())
        and not data['failures'] and data['status'] == 'PASS'
    )
    checks['gamma_gap'] = rat(data['proved_conservative_rate']) - rat(data['required_rate']) == F(1, 8000)
    # Exact floor classes: N(n+50)=N(n)+27; not an asymptotic sample.
    floor_cases = []
    for residue in range(50):
        n = 400 + residue
        N = (F(27 * n, 50) - F(1, 2)).__floor__()
        offset = F(27 * n, 50) - (N + F(1, 2))
        passed = F(0) <= offset < 1 and 2 * N + 1 > F(n, 3)
        floor_cases.append({'n_mod_50': residue, 'offset': encode(offset), 'N_at_400_plus_residue': N, 'pass': passed})
    checks['all_floor_classes'] = all(item['pass'] for item in floor_cases)
    checks['cardinality_increment'] = 54 > F(50, 3)
    failures = [key for key, passed in checks.items() if not passed]
    output = {
        'status': 'PASS' if not failures else 'FAIL',
        'scope': 'Exact arithmetic replay and independent log/antiderivative/floor checks; analytic conceptual audit is canonical in C645x.',
        'original_sha256_before': hashlib.sha256(before).hexdigest(),
        'original_sha256_after': hashlib.sha256(after).hexdigest(),
        'original_replay_stdout': run.stdout,
        'independent_log_terms': 96,
        'independent_log_bounds': {key: {'lower': encode(lo), 'upper': encode(hi)} for key, (lo, hi) in logs.items()},
        'independent_value_bounds': values,
        'independent_rounded_bounds': rounded,
        'floor_cases': floor_cases,
        'checks': checks,
        'failures': failures,
        'proved_rate': data['proved_conservative_rate'],
        'required_rate': data['required_rate'],
        'rate_gap': encode(F(1, 8000)),
        'limits': ['fractional mixture only', 'spatial projection through 2n only', 'no admissible countersequence', 'no full angular Hankel upper bound', 'no Xi realization or signs'],
    }
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(output, indent=2) + '\n')
    print(run.stdout, end='')
    print(f"Audit: {output['status']}; {sum(checks.values())}/{len(checks)} checks; {sum(item['pass'] for item in floor_cases)}/50 exact floor classes")
    print(f"Replay byte identical: {before == after}; failures: {failures}")
    print(f"Full audit certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

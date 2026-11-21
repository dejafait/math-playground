#!/usr/bin/env python3
"""Exact coefficient envelopes for C998a; not a residual or sign certificate.

All coefficient arithmetic is rational. Transcendental factors and the
complete operator estimates are bounded analytically in the canonical proof.
Full dyadic inputs and all calculated bounds are saved, not printed.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import numpy as np

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'jump-log-h1-bounds-654.json'
checks, failures, pins = [], [], {}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(condition, name):
    checks.append({'check': name, 'passed': bool(condition)})
    if not condition:
        failures.append(name)
        raise ValueError(name)


def encode(value):
    return {'numerator': str(value.numerator), 'denominator': str(value.denominator)}


def ceiling(value):
    return -(-value.numerator // value.denominator)


def envelope(values):
    s0 = sum((abs(x) for x in values), Q(0))
    s1 = sum(((n + 1) * abs(x) for n, x in enumerate(values, start=2)), Q(0))
    return 6 * s0, 24 * s1


report = {'result': 'UNFINISHED', 'checks': checks, 'failures': failures,
          'input_sha256': pins, 'columns': [],
          'scope': 'C998a exact symbolic representation and conservative H1 envelopes only',
          'not_certified': ['actual residual norms', 'scalar jump/log/projection evaluations',
                            'inverse pairings', 'Hermitian comparison', 'S3 or RH']}
try:
    names = ['frozen-reference-proposal-652.json', 'frozen-reference-proposal-652.npz',
             'neutral-reference-rank-obstruction-640.json', 'neutral-reference-rank-audit-642.json']
    for name in names:
        pins[name] = sha(B / name)
    proposal = json.loads((B / names[0]).read_text())
    rank = json.loads((B / names[2]).read_text())
    audit = json.loads((B / names[3]).read_text())
    check(pins[names[1]] == proposal['archive']['sha256'] ==
          '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6',
          'entire pinned652 archive')
    check(pins[names[2]] == audit['input_sha256'][names[2]], 'frozen640 witness source pin642')
    witness = proposal['witness']
    check(witness == rank['witness'] == audit['witness'], 'entire96-integer witness equality')
    check(witness['support_indices_zero_based'] == list(range(16)) + list(range(1022, 1038))
          and witness['denominator'] == 2**24 and witness['ambient_dimension'] == 2044
          and witness['omitted_coordinates'] == 'exactly zero', 'exact endpoint supports')
    xi = witness['integer_columns_by_row']
    check(len(xi) == 32 and all(len(row) == 3 and all(type(x) is int for x in row) for row in xi),
          'all integer coordinates have expected shape')
    with np.load(B / names[1], allow_pickle=False) as archive:
        yy = archive['free_middle_dyadics'].copy()
        check(yy.dtype == np.dtype('float64') and yy.shape == (254, 3)
              and np.isfinite(yy).all(), 'all762 finite binary64 free coefficients')
    report['exact_X_witness'] = witness
    report['exact_free_middle_columns'] = []
    for col in range(3):
        free_f = [Q(row[col], 2**24) for row in xi[:16]]
        free_h = [Q(row[col], 2**24) for row in xi[16:]]
        free_q = [Q.from_float(float(x)) for x in yy[:, col]]
        report['exact_free_middle_columns'].append([encode(x) for x in free_q])
        F, LF = envelope(free_f)
        H, LH = envelope(free_h)
        V, LV = envelope(free_q)
        G = 5 * (F + H) + 45 * V
        jump_sum = 16 * (F + H) + 40 * V
        remainder_l2 = G + 16 * (F + H) + 41 * V
        remainder_derivative = 16 * (LF + LH) + F + H + 23 * LV + 83 * V + 384 * G
        h1 = remainder_l2 + remainder_derivative
        simplified = 1942 * (F + H) + 17449 * V + 16 * (LF + LH) + 23 * LV
        check(h1 == simplified, f'column{col} full H1 ledger identity')
        values = dict(F=F, LF=LF, H=H, LH=LH, V=V, LV=LV, unprojected_l2=G,
                      total_absolute_jumps=jump_sum, remainder_l2=remainder_l2,
                      remainder_derivative=remainder_derivative, remainder_h1=h1)
        report['columns'].append({'column_zero_based': col,
                                  'bounds': {k: encode(v) for k, v in values.items()},
                                  'h1_integer_upper': ceiling(h1)})
    upper = max(c['h1_integer_upper'] for c in report['columns'])
    report['uniform_H1_integer_upper'] = upper
    # The canonical proof supplies exact no-coincidence arguments; this is
    # their finite inventory, not a floating-point ordering test.
    powers = [29, 31, 32, 37, 41, 43, 47, 49, 53, 59, 61, 64, 67, 71, 73, 79]
    report['event_inventory'] = {
        'prime_powers': powers, 'positive_delta': [n for n in powers if n*n < 3**7],
        'negative_delta': [n for n in powers if n*n > 3**7],
        'translations': 2*len(powers), 'grid': 2*(286-1), 'midpoint': 1,
        'total_distinct_candidate_interfaces': 2*len(powers) + 2*(286-1) + 1,
        'zero_coefficients_may_remove_actual_jumps': True,
        'coincidence_proof': 'C998a Section2, prime factorization; no numerical location test'}
    check(all(n % 3 for n in powers), 'all shift powers exclude prime3')
    check(all(n*n != 3**7 for n in powers), 'no zero nearest delay')
    check(all(sha(B / name) == digest for name, digest in pins.items()), 'all inputs preserved')
    report['result'] = 'EXACT_COEFFICIENT_BOUNDS_PASS_UNDER_C998a_ANALYTIC_ESTIMATES'
except Exception as exc:
    if not failures:
        failures.append(type(exc).__name__ + ': ' + str(exc))
    report['result'] = 'FAILED'
report['script_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(report, indent=2) + '\n')
print(report['result'])
for record in report['columns']:
    print('Column', record['column_zero_based'], 'H1 remainder upper <=', record['h1_integer_upper'])
print('Required regularity: finite ordinary-interval H1 bound; uniform upper:',
      report.get('uniform_H1_integer_upper', 'unavailable'))
print('Actual residual error and .000999 matrix comparison: unverified')
print('Failures:', failures)
print('Complete certificate:', OUT.relative_to(ROOT))
if failures:
    raise SystemExit(1)

#!/usr/bin/env python3
"""Independent exact replay of C998a's finite data and complete bound ledger.

No previous calculation module is imported and no old output is overwritten.
Analytic trace/derivative arguments are audited in C998a, not by this script.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import numpy as np

B = Path(__file__).resolve().parent
checks = []
snapshots = {}
columns = []


def check(name, condition):
    checks.append({'name': name, 'pass': bool(condition)})


def read(name):
    raw = (B / name).read_bytes()
    snapshots[name] = raw
    return json.loads(raw)


def decode(value):
    return Q(int(value['numerator']), int(value['denominator']))


def encode(value):
    return {'numerator': str(value.numerator), 'denominator': str(value.denominator)}


def envelopes(coefficients):
    # Distinct accumulation of the unweighted and frequency-weighted sums.
    mass = sum(map(abs, coefficients), Q())
    frequency = sum((n * abs(c) for n, c in enumerate(coefficients, 2)), Q())
    return 6 * mass, 24 * (frequency + mass)


report = {'result': 'UNFINISHED', 'checks': checks, 'columns': columns,
          'scope': 'all finite inputs/ledger entries; analytic proof separately audited in C998a',
          'not_verified': ['scalar jump/log/projection evaluations', 'actual residual norms',
                           'inverse pairings', 'signed comparison', 'source/core/c_* contracts']}
try:
    old = read('jump-log-h1-bounds-654.json')
    proposal = read('frozen-reference-proposal-652.json')
    rank = read('neutral-reference-rank-obstruction-640.json')
    rank_audit = read('neutral-reference-rank-audit-642.json')
    archive_name = 'frozen-reference-proposal-652.npz'
    snapshots[archive_name] = (B / archive_name).read_bytes()
    archive_sha = sha256(snapshots[archive_name]).hexdigest()
    check('entire frozen652 archive pin', archive_sha == proposal['archive']['sha256'] ==
          '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6')
    for name, digest in old['input_sha256'].items():
        check('654 input hash: ' + name, sha256(snapshots[name]).hexdigest() == digest)
    generator = B / 'jump-log-h1-bounds-654.py'
    snapshots[generator.name] = generator.read_bytes()
    check('654 executed generator hash', sha256(snapshots[generator.name]).hexdigest() == old['script_sha256'])
    check('642 source pin for640', sha256(snapshots['neutral-reference-rank-obstruction-640.json']).hexdigest()
          == rank_audit['input_sha256']['neutral-reference-rank-obstruction-640.json'])
    witness = rank['witness']
    check('all four complete witness records agree',
          witness == rank_audit['witness'] == proposal['witness'] == old['exact_X_witness'])
    check('witness support and omitted coordinates', witness['support_indices_zero_based'] ==
          list(range(16)) + list(range(1022, 1038)) and witness['denominator'] == 2**24 and
          witness['ambient_dimension'] == 2044 and witness['omitted_coordinates'] == 'exactly zero')
    rows = witness['integer_columns_by_row']
    check('all96 witness values are integers', len(rows) == 32 and
          all(len(row) == 3 and all(type(x) is int for x in row) for row in rows))
    with np.load(B / archive_name, allow_pickle=False) as data:
        trials = data['free_middle_dyadics'].copy()
    check('all762 free trials finite binary64', trials.shape == (254, 3) and
          trials.dtype == np.dtype('float64') and bool(np.isfinite(trials).all()))
    check('exact ledger shape', len(old['columns']) == 3 and len(old['exact_free_middle_columns']) == 3)
    for j in range(3):
        q = [Q(*float(x).as_integer_ratio()) for x in trials[:, j]]
        check(f'column{j}: every exact trial dyadic',
              q == [decode(x) for x in old['exact_free_middle_columns'][j]])
        f = [Q(row[j], 2**24) for row in rows[:16]]
        h = [Q(row[j], 2**24) for row in rows[16:]]
        F, LF = envelopes(f)
        H, LH = envelopes(h)
        V, LV = envelopes(q)
        forcing = F + H
        raw = 5 * forcing + 45 * V
        jumps = 16 * forcing + 40 * V
        function = raw + V + jumps
        derivative = 16 * (LF + LH) + forcing + 21 * LV + 2 * (V + LV) + 81 * V + 384 * raw
        total = function + derivative
        values = {'F': F, 'LF': LF, 'H': H, 'LH': LH, 'V': V, 'LV': LV,
                  'unprojected_l2': raw, 'total_absolute_jumps': jumps,
                  'remainder_l2': function, 'remainder_derivative': derivative, 'remainder_h1': total}
        saved = old['columns'][j]
        check(f'column{j}: every rational ledger entry', saved['column_zero_based'] == j and
              values == {key: decode(value) for key, value in saved['bounds'].items()})
        check(f'column{j}: independent ledger expansion', total ==
              1942 * forcing + 17449 * V + 16 * (LF + LH) + 23 * LV)
        upper = saved['h1_integer_upper']
        check(f'column{j}: exact ceiling', Q(upper - 1) < total <= Q(upper) and
              upper == [253066, 184234, 324793][j])
        columns.append({'column': j, 'all_bounds': {k: encode(v) for k, v in values.items()},
                        'ceil_h1': upper, 'ceiling_slack': encode(Q(upper) - total)})
    check('uniform H1 ceiling', old['uniform_H1_integer_upper'] ==
          max(c['ceil_h1'] for c in columns) == 324793)
    check('printed final exact bound', decode(old['columns'][2]['bounds']['remainder_h1']) ==
          Q(6282395223318363954214193951853, 19342813113834066795298816))

    # Enumerate the relevant prime powers independently of the saved list.
    powers = set()
    for p in range(2, 81):
        if any(p % d == 0 for d in range(2, p)):
            continue
        n = p
        while n < 81:
            if n > 27:
                powers.add(n)
            n *= p
    powers = sorted(powers)
    events = old['event_inventory']
    check('complete prime-power set and delay signs', powers == events['prime_powers'] and
          events['positive_delta'] == [n for n in powers if n*n < 3**7] and
          events['negative_delta'] == [n for n in powers if n*n > 3**7])
    check('no powers divisible by3 or zero delays', all(n % 3 and n*n != 3**7 for n in powers))
    check('all603 candidate interfaces', events['translations'] == 2*len(powers) == 32 and
          events['grid'] == 2*(286-1) == 570 and events['midpoint'] == 1 and
          events['total_distinct_candidate_interfaces'] == 603)
    report['event_inventory'] = events

    # Rational boundary tests for the analytic majorants used in C998a.
    terms = 32
    log3_lower = sum((Q(1, (2*k+1)*4**k) for k in range(terms)), Q())
    log3_upper = log3_lower + Q(4, 3*(2*terms+1)*4**terms)
    check('1/4<a<3/10 from positive log series', Q(1, 4) < log3_lower/4 < log3_upper/4 < Q(3, 10))
    check('d>1/5 and exp(-2a)<2/3 by integer powers', Q(5, 4)**4 < 3 and Q(3, 2)**2 < 3)
    exp_lower = sum((Q(1, k) for k in [1, 1, 2, 6]), Q())
    check('e>5/2, e^5>79, e^8>1021', exp_lower > Q(5, 2) and Q(5, 2)**5 > 79 and Q(5, 2)**8 > 1021)
    check('exp(.6) Taylor upper<2', 1 + Q(3, 5) + Q(3, 5)**2/(2*(1-Q(3, 5)/3)) < 2)
    constants = {
        'K_derivative_majorant': Q(192, 3969),
        'h_m_operator_majorant': Q(3, 10)*(Q(1, 4)+Q(3, 5)*Q(303, 16)),
        'E_operator_majorant': 4*Q(3, 10)/(Q(1, 5)*Q(1, 3)),
        'E_derivative_majorant': 4*Q(3, 10)/Q(1, 5)*(2*Q(2, 3)/Q(1, 3)**2+Q(1, 2)/Q(1, 3)),
        'grid_jump_majorant': 4*19*Q(3, 10)**2,
        'midpoint_jump_majorant': Q(3, 2)*(Q(1, 2)+Q(7, 2)+18),
        'projection_derivative_majorant': Q(1, 2)*2*384,
        'digamma_real_majorant': 8 + Q(2, 5) + 4 + Q(4, 25) + 2,
    }
    check('forcing bound<1', constants['K_derivative_majorant'] < 1)
    check('h_m operator<3.5', constants['h_m_operator_majorant'] < Q(7, 2))
    check('E operator<=18 and derivative<=81', constants['E_operator_majorant'] == 18 and
          constants['E_derivative_majorant'] == 81)
    check('grid<7V and midpoint<=33V', constants['grid_jump_majorant'] < 7 and constants['midpoint_jump_majorant'] == 33)
    check('projection derivative<=384G', constants['projection_derivative_majorant'] == 384)
    check('digamma bound<20', constants['digamma_real_majorant'] < 20 and
          Q(3, 2)/(6*Q(5, 4)**2) == Q(4, 25))
    report['elementary_constants'] = {k: encode(v) for k, v in constants.items()}
    check('all original twelve checks passed', len(old['checks']) == 12 and
          all(c['passed'] for c in old['checks']) and old['failures'] == [])
    check('every input preserved', all((B / name).read_bytes() == raw for name, raw in snapshots.items()))
except Exception as exc:
    check('exception: ' + type(exc).__name__ + ': ' + str(exc), False)

failures = [c['name'] for c in checks if not c['pass']]
report['failures'] = failures
report['input_sha256'] = {name: sha256(raw).hexdigest() for name, raw in snapshots.items()}
report['script_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
report['result'] = 'PASS_FINITE_REPLAY_ANALYTIC_AUDIT_SEPARATE' if not failures else 'FAIL'
report['summary'] = {'checks_passed': len(checks)-len(failures), 'checks_total': len(checks),
                     'H1_upper_bounds': [c['ceil_h1'] for c in columns],
                     'required': 'finite ordinary-interval H1 bound; no small residual threshold',
                     'failures': failures}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(report, indent=2) + '\n')
print(report['result'])
print(json.dumps(report['summary'], sort_keys=True))
print('Full certificate:', output.relative_to(B.parent.parent))
if failures:
    raise SystemExit(1)

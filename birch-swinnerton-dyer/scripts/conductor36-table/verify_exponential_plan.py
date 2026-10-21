#!/usr/bin/env python3
"""Complete independent Fraction replay; imports no tail producer.

Reuses the saved coupled-plan and positive-period verifier. These are
read-only calls, so historical certificate/report bytes are preserved.
"""
import json
import traceback
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path

from verify_coupled_plan import replay as replay_coupled

HERE = Path(__file__).resolve().parent


def replay(data):
    assert data['schema'] == 'conductor36-full-exponential-tail-plan-v1'
    assert data['bits'] == 96 and data['scale'] == 2**96
    D = data['scale']
    source = HERE/'coupled_plan.json'
    analytic = HERE.parent/'nonunitary-cusp/reduced_phase_certificate.json'
    assert data['coupled_plan_sha256'] == sha256(source.read_bytes()).hexdigest()
    assert data['audited_analytic_sha256'] == sha256(analytic.read_bytes()).hexdigest()
    saved = json.loads(source.read_text())
    old = json.loads(analytic.read_text())
    upstream = replay_coupled(saved)
    assert upstream['replay_passed'] and not upstream['failures']
    omega = Q(upstream['period']['lower'])
    assert Q(data['omega_lower']) == omega > 0
    assert data['infinity_primitive'] == '0' and upstream['infinity']['actual_solution_rhs_zero']
    assert data['H'] == 4860 and data['minimality_claimed'] is False
    H = data['H']
    pi = old['pi']['interval']
    assert data['pi'] == pi

    def endpoints(v):
        assert len(v) == 2 and all(type(x) is int for x in v) and v[0] <= v[1]
        return [Q(x, D) for x in v]
    def enclose(values):
        return [(min(values)*D).__floor__(), -((-max(values)*D).__floor__())]
    def times(a, b):
        return enclose([x*y for x in endpoints(a) for y in endpoints(b)])
    def scalar(a, c):
        return enclose([x*c for x in endpoints(a)])

    heights = sorted({Q(p['y']) for p in saved['primitives']})
    assert [Q(row['y']) for row in data['attenuation']] == heights
    remainder = Q(3**8*8**161, factorial(161))
    radius = -((-D*remainder).__floor__())
    tail_bounds = []
    taylor_operations = power_operations = 0
    for row, y in zip(data['attenuation'], heights):
        assert 0 < y <= 1
        w = scalar(pi, -2*y)
        assert row['w'] == w and -8*D <= w[0] <= w[1] < 0
        assert row['degree'] == 160 and Q(row['remainder']) == remainder and row['radius'] == radius
        t = s = [D, D]
        assert len(row['taylor_trace']) == 160
        for k, record in enumerate(row['taylor_trace'], 1):
            t = scalar(times(t, w), Q(1, k))
            s = enclose([x+z for x in endpoints(s) for z in endpoints(t)])
            assert record == {'k': k, 'term': t, 'partial': s}
            taylor_operations += 1
        assert row['polynomial'] == s
        q = [s[0]-radius, s[1]+radius]
        assert row['q'] == q and 0 < q[0] <= q[1] < D
        assert row['power_exponent'] == H+1
        remaining, base, accum = H+1, q[:], [D, D]
        records = row['power_trace']
        assert len(records) == (H+1).bit_length()
        for record in records:
            assert record['remaining'] == remaining and record['base'] == base and record['before'] == accum
            if remaining & 1:
                accum = times(accum, base)
                power_operations += 1
            assert record['after'] == accum
            remaining >>= 1
            if remaining:
                base = times(base, base)
                power_operations += 1
            assert record['next_base'] == base
        assert remaining == 0 and row['power_interval'] == accum
        assert 0 <= accum[0] <= accum[1]
        # Quotients reconstructed from Fraction endpoints with both strictly
        # positive denominator endpoints, rather than the producer formula.
        quotients = [a/(1-b) for a in endpoints(accum) for b in endpoints(q)]
        bound = [min(quotients), max(quotients)]
        assert list(map(Q, row['tail_bounds'])) == bound
        tail_bounds.append(bound)

    ids = {y: i for i, y in enumerate(heights)}
    assert len(data['primitives']) == len(saved['primitives']) == 98
    tails = []
    for p, before in zip(data['primitives'], saved['primitives']):
        i = ids[Q(before['y'])]
        assert p == {'x_reduced': before['x_reduced'], 'y': before['y'], 'H': H,
                     'attenuation_id': i, 'tail_bounds': list(map(str, tail_bounds[i]))}
        tails.append(tail_bounds[i])
    assert len(data['generators']) == len(saved['generators']) == 72
    widths = []
    occurrence_count = 0
    for i, (row, g) in enumerate(zip(data['generators'], saved['generators'])):
        assert row['generator_id'] == i and row['endpoints'] == g['endpoints']
        assert row['occurrences'] == g['occurrences']
        assert row['absolute_occurrence_weight'] == g['absolute_occurrence_weight']
        W = sum((abs(Q(w)) for j, w in g['occurrences']), Q(0))
        assert Q(row['absolute_occurrence_weight']) == W
        bounds = [sum((2*abs(Q(w))*tails[j][side]/omega for j, w in g['occurrences']), Q(0))
                  for side in (0, 1)]
        assert list(map(Q, row['normalized_tail_width_bounds'])) == bounds
        widths.append(bounds)
        occurrence_count += len(g['occurrences'])
    budget = Q(1, 2**38)
    worst = max(range(72), key=lambda i: widths[i][1])
    failures = [i for i, (lo, hi) in enumerate(widths) if hi > budget]
    obstructions = [i for i, (lo, hi) in enumerate(widths) if lo > budget]
    inconclusive = [i for i in failures if i not in obstructions]
    assert data['threshold_failures'] == failures and data['obstruction_rows'] == obstructions
    assert data['inconclusive_rows'] == inconclusive
    rho = budget*omega/(2*max(Q(g['absolute_occurrence_weight']) for g in saved['generators']))
    assert Q(data['uniform_rho']) == rho
    k = max(k for k in range(101) if widths[worst][1] <= Q(1, 2**k))
    actual = {'generators': 72, 'points': 98, 'heights': len(heights), 'endpoint_occurrences': 144,
              'max_H': max(p['H'] for p in data['primitives']),
              'distinct_terms': sum(p['H'] for p in data['primitives']),
              'worst_generator_id': worst, 'max_width_le_dyadic_power': k,
              'passing_width_rows': 72-len(failures),
              'uniform_rho_all_pass': all(t[1] <= rho for t in tails)}
    required = {'generators': 72, 'points': 98, 'max_H': 4860, 'distinct_terms': 1000000,
                'normalized_two_sided_tail_width': str(budget)}
    assert data['actual'] == actual and data['required'] == required
    passed = not failures and actual['max_H'] <= 4860 and actual['distinct_terms'] <= 1000000
    assert data['workload_passed'] == passed and data['table_complete'] is False
    return {'replay_passed': True, 'workload_passed': passed, 'table_complete': False,
            'actual': actual, 'required': required, 'failures': [], 'threshold_failures': failures,
            'obstruction_rows': obstructions, 'inconclusive_rows': inconclusive,
            'checks': {'all_q_brackets': len(heights), 'Taylor_steps': taylor_operations,
                       'power_multiplications': power_operations, 'primitive_tail_rows': 98,
                       'uncombined_occurrences': occurrence_count, 'generator_width_rows': 72},
            'worst_width_bounds': list(map(str, widths[worst])),
            'period': upstream['period'], 'source_plan_checks': upstream['checks'],
            'source_structural_actual': upstream['structural_actual'],
            'source_structural_required': upstream['structural_required'],
            'preserved_upstream_threshold_failures': upstream['threshold_failures'],
            'unperformed': ['new finite Fourier sums and arithmetic errors', 'signed period division',
                            'integer isolation and full table', 'separate critical audit']}


if __name__ == '__main__':
    source = HERE/'exponential_plan.json'
    destination = HERE/'exponential_plan_verification.json'
    try:
        report = replay(json.loads(source.read_text()))
    except Exception as exc:
        report = {'replay_passed': False, 'workload_passed': False, 'table_complete': False,
                  'failures': [repr(exc)], 'traceback': traceback.format_exc()}
    report['certificate_sha256'] = sha256(source.read_bytes()).hexdigest()
    destination.write_text(json.dumps(report, indent=2)+'\n')
    print('full-exponential replay=', report['replay_passed'], 'workload=', report['workload_passed'],
          'actual=', report.get('actual'), 'required=', report.get('required'),
          'failures=', report['failures'], 'threshold failures=', report.get('threshold_failures'),
          'report=', destination)
    raise SystemExit(0 if report['replay_passed'] else 1)

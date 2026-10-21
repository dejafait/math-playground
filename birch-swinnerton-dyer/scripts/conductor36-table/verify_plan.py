#!/usr/bin/env python3
"""Independent full presentation/endpoint plan replay; no analytic success claim.

Imports the existing independent structural verifier, never either producer.
Every matrix, cusp, interior image, point index and tail cutoff is checked.
"""
import importlib.util
import json
import traceback
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent


def replay(data):
    assert type(data) is dict and set(data) == {
        'schema', 'presentation_sha256', 'ell', 'endpoints', 'cusps',
        'primitives', 'T', 'summary'}
    verifier = HERE.parent/'general-relative/verify_certificate.py'
    spec = importlib.util.spec_from_file_location('structural_replay', verifier)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    source = HERE/'presentation.json'
    structural = json.loads(source.read_text())
    checker = module.Checker()
    structure = module.replay(checker, structural, 36, [])
    assert data['schema'] == 'conductor36-endpoint-plan-v1'
    assert data['presentation_sha256'] == sha256(source.read_bytes()).hexdigest()
    assert data['endpoints'] == structural['endpoints']
    assert data['ell'] == 37 and all(37%d for d in range(2, isqrt(37)+1)) and 37 % 36 == 1
    expected_cusps = sorted({Q(p, q) for pair in structural['endpoints'] for p, q in pair if q})
    assert len(data['cusps']) == len(expected_cusps)
    assert [row['r'] for row in data['cusps']] == list(map(str, expected_cusps))
    expected_keys, uses = set(), set()
    transport_count, maximum_C, worst = 0, 0, None
    primitives = data['primitives']
    keys = []
    term_count = 0
    for row in primitives:
        assert set(row) == {'x_reduced', 'y', 'H'}
        x, y = Q(row['x_reduced']), Q(row['y'])
        H = row['H']
        assert type(H) is int and H >= 0 and -Q(1, 2) <= x < Q(1, 2) and 0 < y <= 1
        def bound(n):
            exponent = (6*n*y).__floor__()
            assert exponent >= 0
            return Q(1, (1 << exponent))*Q(1, 6*y)
        assert bound(H) <= Q(1, 1 << 38)
        assert H == 0 or bound(H-1) > Q(1, 1 << 38)
        keys.append((x, y)); term_count += H
    assert keys == sorted(set(keys))

    def multiply(a, b):
        return [[sum(a[i][k]*b[k][j] for k in (0, 1)) for j in (0, 1)] for i in (0, 1)]

    for cusp in data['cusps']:
        assert set(cusp) == {'r', 'transports'}
        r = Q(cusp['r']); a, m = r.numerator, r.denominator
        assert gcd(m, 37) == 1
        vs = [37*r]+[(r+j)/37 for j in range(37)]
        assert len(cusp['transports']) == 38
        for row, v in zip(cusp['transports'], vs):
            assert set(row) == {'v', 'bezout_r', 'bezout_v', 't', 'matrix', 'tau', 'image', 'primitive_ids'}
            assert Q(row['v']) == v
            p, q = v.numerator, v.denominator
            sr, tr = row['bezout_r']; sv, tv = row['bezout_v']; t = row['t']
            assert all(type(n) is int for n in (sr, tr, sv, tv, t))
            assert a*sr-m*tr == 1 and p*sv-q*tv == 1
            matrix = multiply(multiply([[p, tv], [q, sv]], [[1, t], [0, 1]]), [[sr, -tr], [-m, a]])
            A, B = matrix[0]; C, D = matrix[1]
            assert row['matrix'] == [A, B, C, D]
            assert all(type(n) is int for n in row['matrix'])
            assert A*D-B*C == 1 and C % 36 == 0
            assert C*a+D*m != 0 and q*(A*a+B*m) == p*(C*a+D*m)
            # Congruence solutions change C by the entire arithmetic step.
            step = m*q*(36//gcd(m*q, 36))
            assert abs(C) <= abs(C-step) and abs(C) <= abs(C+step)
            assert len(row['tau']) == len(row['image']) == 2
            x, y = map(Q, row['tau']); u, w = map(Q, row['image'])
            assert y > 0 and w > 0
            divisor = (C*x+D)**2+(C*y)**2
            assert divisor > 0
            assert u == ((A*x+B)*(C*x+D)+A*C*y*y)/divisor and w == y/divisor
            if C:
                assert x == -Q(D, C) and y == Q(1, abs(C))
            else:
                assert (x, y) == (0, 1)
            ids = row['primitive_ids']; assert type(ids) is list and len(ids) == 2
            for i, point in zip(ids, ((x, y), (u, w))):
                assert type(i) is int and 0 <= i < len(keys)
                xx, yy = point; xx -= (xx+Q(1, 2)).__floor__()
                key = (xx, yy)
                assert keys[i] == key
                expected_keys.add(key); uses.add(i)
            transport_count += 1
            if abs(C) > maximum_C:
                maximum_C = abs(C)
                worst = {'r': str(r), 'v': str(v), 'matrix': [A, B, C, D],
                         'primitive_ids': ids,
                         'primitives': [primitives[i] for i in ids]}
    assert expected_keys == set(keys) and uses == set(range(len(keys)))
    T = max(37, max(row['H'] for row in primitives))
    assert type(data['T']) is int and data['T'] == T
    summary = {'generators': structure['s'], 'finite_cusps': len(expected_cusps),
               'transports': transport_count, 'points': len(keys),
               'Fourier_terms': term_count, 'max_abs_C': maximum_C}
    assert data['summary'] == summary
    # Exact workload for the unchanged prime-by-prime coefficient method,
    # without executing the astronomical point-count workload itself.
    prime_mask = bytearray(b'\1')*(T+1)
    prime_mask[:2] = b'\0\0'
    for p in range(2, isqrt(T)+1):
        if prime_mask[p]:
            prime_mask[p*p:T+1:p] = b'\0'*len(range(p*p, T+1, p))
    good_primes = [p for p in range(5, T+1) if prime_mask[p]]
    return {'plan_passed': True, 'table_complete': False,
            'structure': structure, 'actual': summary,
            'required': {'generators': 72, 'finite_cusps': len(expected_cusps),
                         'transports': 38*len(expected_cusps), 'points': len(expected_keys)},
            'T': T, 'tail_budget': '1/274877906944',
            'worst_transport': worst,
            'coefficient_schedule': {'good_primes': len(good_primes),
                                     'required_x_counts': sum(good_primes)},
            'failures': [], 'structural_actual': checker.counts,
            'structural_required': checker.required,
            'unperformed': ['point counts/coefficients beyond existing evidence',
                            'new finite phases/attenuation/Fourier sums and tails',
                            'all-generator analytic containment and scaled-integer isolation',
                            'normalized table/source and saturated relation replay']}


if __name__ == '__main__':
    destination = HERE/'plan_verification.json'
    source = HERE/'plan.json'
    try:
        report = replay(json.loads(source.read_text()))
    except Exception as exc:
        report = {'plan_passed': False, 'table_complete': False,
                  'failures': [repr(exc)], 'traceback': traceback.format_exc()}
    report['plan_sha256'] = sha256(source.read_bytes()).hexdigest()
    destination.write_text(json.dumps(report, indent=2)+'\n')
    print('plan replay', 'PASS' if report['plan_passed'] else 'FAIL',
          'table complete=', report['table_complete'], 'actual=', report.get('actual'),
          'required=', report.get('required'), 'T=', report.get('T'),
          'coefficient workload=', report.get('coefficient_schedule'),
          'failures=', len(report['failures']), 'path=', destination)
    raise SystemExit(0 if report['plan_passed'] else 1)

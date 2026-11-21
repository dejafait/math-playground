#!/usr/bin/env python3
"""Exact-rational origin coefficients for the approved L821 endpoint test.

Full integer-lattice intervals and every polynomial/tail are saved to disk.
The infinity proof is analytic in L826, not a floating-point experiment.
"""
import json
import math
from fractions import Fraction as F
from pathlib import Path
from confluent_compact_audit_614 import Box, S, BITS, TERMS, exp_box, pi_box

OUT = Path(__file__).with_suffix('.json')


def add(p, k, a):
    p[k] = p.get(k, F(0)) + a
    if not p[k]:
        del p[k]


def step(p):
    q = {}
    for k, a in p.items():
        add(q, k, (F(1, 2) + 2*k)*a)
        add(q, k+1, -2*a)
    return q


def evaluate(p, x):
    value = Box.of(0)
    for k in range(max(p), -1, -1):
        value = value*x + p.get(k, 0)
    return value


# Multivariate exact polynomial algebra in (c2,c4,c6,c8).
ZERO = (0, 0, 0, 0)
ONE = {ZERO: F(1)}


def plus(p, q):
    r = dict(p)
    for k, a in q.items():
        add(r, k, a)
    return r


def scale(p, a):
    return {k: v*a for k, v in p.items() if v*a}


def times(p, q):
    r = {}
    for k, a in p.items():
        for l, b in q.items():
            add(r, tuple(x+y for x, y in zip(k, l)), a*b)
    return r


def series_times(p, q):
    r = [{} for _ in range(5)]
    for i in range(5):
        for j in range(5-i):
            r[i+j] = plus(r[i+j], times(p[i], q[j]))
    return r


def serial(p):
    return [{'powers': list(k), 'coefficient': str(v)} for k, v in sorted(p.items())]


def main():
    failures = []
    pi = pi_box()
    assert 3*S < pi.lo <= pi.hi < 4*S
    # With n>=9, r<=8, the largest power is n^20.
    ratio = Box.of(F(10, 9)**20)*exp_box(Box.of(-57))
    if not ratio.hi*2 < S:
        failures.append('origin tail geometric ratio not below 1/2')
    p = {1: F(-12), 2: F(8)}
    derivatives, rows = [], []
    for r in range(9):
        degree = r+2
        assert max(p) == degree
        norm = sum(abs(a) for a in p.values())
        terms = [evaluate(p, pi*(n*n))*exp_box(-pi*(n*n)) for n in range(1, 9)]
        finite = sum(terms, Box.of(0))
        tail = Box.of(2*norm*4**degree*9**(2*degree))*exp_box(Box.of(-243))
        full = finite + Box(-tail.hi, tail.hi)
        derivatives.append(full)
        rows.append({'r': r, 'polynomial': {str(k): str(a) for k, a in sorted(p.items())},
                     'coefficient_norm': str(norm), 'finite_terms': [x.data() for x in terms],
                     'finite_sum': finite.data(), 'tail_upper': str(tail.hi), 'full': full.data()})
        p = step(p)
    k0 = derivatives[0]
    if k0.lo <= 0:
        failures.append('K(0) denominator not strictly positive')
    coeffs = [derivatives[2*j]/math.factorial(2*j)/k0 for j in range(1, 5)]
    c2, c4, c6, c8 = coeffs
    leading = -256*c2*c4
    next_term = 768*c2*(c2*c4-3*c6)
    # Intentionally coarse rational bounds are the human-facing proof contract.
    bounds = [('K0', k0, F(1), F(2)),
              ('c2', c2, F(-10), F(-9)), ('c4', c4, F(37), F(39)),
              ('origin_leading', leading, F(90000), F(91000))]
    bound_checks = []
    for name, value, lower, upper in bounds:
        ok = value.lo > lower*S and value.hi < upper*S
        bound_checks.append({'name': name, 'required_strict_lower': str(lower),
                             'required_strict_upper': str(upper), 'passed': ok})
        if not ok:
            failures.append(name+' coarse bound failed')
    # Formal logarithm mod t^5, t=u^2, with no fitted coefficients.
    z = [{}]+[{tuple(int(k == j) for k in range(4)): F(1)} for j in range(4)]
    power = [{} for _ in range(5)]
    power[0] = ONE
    log = [{} for _ in range(5)]
    for k in range(1, 5):
        power = series_times(power, z)
        for j in range(5):
            log[j] = plus(log[j], scale(power[j], F((-1)**(k+1), k)))
    jets = {r: [scale(log[j], (2*j)**r) for j in range(5)] for r in (2, 3, 4)}
    q = series_times(jets[3], jets[3])
    other = series_times(jets[2], jets[4])
    cube = series_times(series_times(jets[2], jets[2]), jets[2])
    q = [plus(plus(q[j], scale(other[j], -1)), scale(cube[j], -2)) for j in range(5)]
    expected = [{}, {}, {}, {(1,1,0,0): F(-256)},
                {(2,1,0,0): F(768), (1,0,1,0): F(-2304)}]
    if q != expected:
        failures.append('formal Q3 cancellations failed')
    report = {'purpose': 'L821 approved two-endpoint test: origin arithmetic and exact cancellations',
              'arithmetic': {'scale': str(S), 'bits': BITS, 'exp_taylor_terms': TERMS,
                             'rounding': 'exact integer lattice, inherited audited Box operations'},
              'pi': pi.data(), 'tail_ratio': ratio.data(), 'derivatives': rows,
              'normalized_even_coefficients': {str(2*j+2): x.data() for j,x in enumerate(coeffs)},
              'log_series': [serial(x) for x in log], 'Q3_series': [serial(x) for x in q],
              'origin_leading': leading.data(), 'origin_u8': next_term.data(),
              'coarse_bound_checks': bound_checks,
              'infinity_required_relative_error': 'tends to 0; see L826 analytic proof, not a numerical certificate',
              'failures': failures, 'result': 'PASS' if not failures else 'FAIL'}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('Origin exact cancellations through u^8:', 'PASS' if q == expected else 'FAIL')
    for name, value, lower, upper in bounds:
        print(name+': actual in ('+str(F(value.lo, S).__float__())+', '+str(F(value.hi, S).__float__())+
              '); required strict bounds ('+str(lower)+', '+str(upper)+')')
    print('Displayed decimals are previews; full exact interval endpoints:', OUT)
    print('Failures:', len(failures), '; result:', report['result'])
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

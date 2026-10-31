#!/usr/bin/env python3
"""Exact rational interval certificate for the N=2 Hermite-Gram boundary.

Run from the active notebook:
    python3 scripts/hermite-gram/leading-block-boundary-certificate.py

Only integer/Fraction arithmetic is used. The accompanying lemma proves
the interval rules, exponential remainder and both omitted-tail bounds.
The complete panel certificate is saved; the console prints summaries.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
from pathlib import Path
import json

S = 1 << 160
ORDER = 40
PANELS_PER_UNIT = 512
LIMIT = 6
THETA_TERMS = 4
OUT = Path(__file__).with_name('leading-block-boundary-certificate.json')


def ceildiv(a, b):
    assert b > 0
    return -((-a) // b)


def point(x):
    x = F(x)
    return (x.numerator * S // x.denominator,
            ceildiv(x.numerator * S, x.denominator))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[1], a[1] - b[0]


def mul(a, b):
    products = [x * y for x in a for y in b]
    return min(products) // S, ceildiv(max(products), S)


def scale(a, n):
    assert n >= 0
    return a[0] * n, a[1] * n


def divide(a, n):
    assert n > 0
    return a[0] // n, ceildiv(a[1], n)


@lru_cache(maxsize=None)
def exp_point(x):
    x = F(x)
    if x == 0:
        return S, S
    if x <= -128:
        # e>2; hence exp(x)<=2^-128. No floating underflow.
        return 0, S >> 128
    if x < 0:
        a, b = exp_point(-x)
        assert a > 0
        return S * S // b, ceildiv(S * S, a)
    squarings = 0
    while x > 1:
        x /= 2
        squarings += 1
    z = point(x)
    term = (S, S)
    total = term
    for j in range(1, ORDER + 1):
        term = (term[0] * z[0] // (S * j),
                ceildiv(term[1] * z[1], S * j))
        total = add(total, term)
    # For 0<=x<=1, Taylor remainder <=e*x^41/41!<3/41!.
    total = total[0], total[1] + ceildiv(3 * S, factorial(ORDER + 1))
    for _ in range(squarings):
        total = mul(total, total)
    return total


def exp_interval(a):
    return exp_point(F(a[0], S))[0], exp_point(F(a[1], S))[1]


def atan_bounds(x, terms):
    partial = sum(((-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
                   for j in range(terms)), F(0))
    following = partial + (-1) ** terms * x ** (2 * terms + 1) / (2 * terms + 1)
    return min(partial, following), max(partial, following)


def rational_interval(a):
    return [str(F(a[0], S)), str(F(a[1], S))]


def decimal_coarse(a, places=16):
    d = 10 ** places
    lo = a[0] * d // S
    hi = ceildiv(a[1] * d, S)
    def fmt(n):
        sign = '-' if n < 0 else ''
        n = abs(n)
        return f'{sign}{n // d}.{n % d:0{places}d}'
    return [fmt(lo), fmt(hi)]


def main():
    a5 = atan_bounds(F(1, 5), 16)
    a239 = atan_bounds(F(1, 239), 6)
    pi_exact = (16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0])
    assert F(3) < pi_exact[0] < pi_exact[1] < F(4)
    pi = point(pi_exact[0])[0], point(pi_exact[1])[1]
    pi2 = mul(pi, pi)
    integral = [(0, 0) for _ in range(3)]
    panels = []
    for j in range(LIMIT * PANELS_PER_UNIT):
        u = point(F(j, PANELS_PER_UNIT))[0], point(F(j + 1, PANELS_PER_UNIT))[1]
        u2 = mul(u, u)
        gauss = exp_interval((-ceildiv(u2[1], 4), -(u2[0] // 4)))
        e2u = exp_interval(scale(u, 2))
        e9u2 = exp_interval(divide(scale(u, 9), 2))
        e5u2 = exp_interval(divide(scale(u, 5), 2))
        kernel = (0, 0)
        for k in range(1, THETA_TERMS + 1):
            bracket = sub(scale(mul(pi2, e9u2), 2 * k ** 4),
                          scale(mul(pi, e5u2), 3 * k ** 2))
            # Every original theta bracket is positive for u>=0, pi>3.
            bracket = max(0, bracket[0]), bracket[1]
            assert bracket[1] >= 0
            decay_arg = scale(mul(pi, e2u), k * k)
            decay = exp_interval((-decay_arg[1], -decay_arg[0]))
            kernel = add(kernel, scale(mul(bracket, decay), 2))
        base = mul(gauss, kernel)
        weights = [(S, S), u2, mul(u2, u2)]
        contributions = [divide(mul(base, w), PANELS_PER_UNIT) for w in weights]
        integral = [add(v, w) for v, w in zip(integral, contributions)]
        panels.append({'index': j, 'integral_fixedpoint_intervals': contributions})

    # On [0,L], Phi's omitted k>=5 contribution is <=80000*2^-75.
    theta_tail = F(80000, 1 << 75)
    # Beyond L=6, use L564: exp(-u^2/4)Phi(u)<=10000 exp(-5u^2/4).
    gaussian_a = F(5, 4)
    r0 = 1 / (2 * gaussian_a * LIMIT)
    r2 = F(LIMIT) / (2 * gaussian_a) + r0 / (2 * gaussian_a)
    r4 = F(LIMIT ** 3) / (2 * gaussian_a) + 3 * r2 / (2 * gaussian_a)
    decay_tail_upper = F(exp_point(-gaussian_a * LIMIT ** 2)[1], S)
    mu = []
    tails = []
    for n, (v, r) in enumerate(zip(integral, [r0, r2, r4])):
        theta_error = 2 * theta_tail * F(LIMIT ** (2 * n + 1), 2 * n + 1)
        spatial_error = 20000 * r * decay_tail_upper
        error = point(theta_error + spatial_error)[1]
        mu.append((2 * v[0], 2 * v[1] + error))
        tails.append({'theta_rational_upper': str(theta_error),
                      'spatial_rational_upper': str(spatial_error)})
    b = [divide(v, 2 ** (2 * n) * factorial(2 * n)) for n, v in enumerate(mu)]
    coarse = [decimal_coarse(v) for v in b]
    coarse_f = [(F(lo), F(hi)) for lo, hi in coarse]
    b0, b2, b4 = coarse_f
    # Use only the displayed rational coefficient bounds for the decisive sign.
    q_upper = b2[1] ** 2 + 16 * b2[1] * b4[1] + 96 * b4[1] ** 2 - 4 * b0[0] * b4[0]
    q_lower = b2[0] ** 2 + 16 * b2[0] * b4[0] + 96 * b4[0] ** 2 - 4 * b0[1] * b4[1]
    failures = []
    if not all(v[0] > 0 for v in coarse_f):
        failures.append('coarse coefficient lower bound is not positive')
    if q_upper >= 0:
        failures.append('N=2 negative-sign threshold not certified')
    certificate = {
        'status': 'PASS' if not failures else 'FAIL',
        'parameters': {'fixedpoint_scale': str(S), 'exp_taylor_order': ORDER,
                       'panels_per_unit': PANELS_PER_UNIT, 'limit': LIMIT,
                       'theta_terms': THETA_TERMS},
        'pi_bounds': [str(x) for x in pi_exact],
        'panel_integral_totals_fixedpoint': integral,
        'omitted_tails': tails,
        'moment_bounds': [rational_interval(v) for v in mu],
        'coefficient_bounds': [rational_interval(v) for v in b],
        'coarse_b_bounds': dict(zip(['b0', 'b2', 'b4'], coarse)),
        'decisive_test': {
            'quantity': 'Q=b2^2+16*b2*b4+96*b4^2-4*b0*b4',
            'necessary_for_psd': 'Q>=0',
            'certified_lower': str(q_lower), 'certified_upper': str(q_upper),
            'upper_decimal_outward': decimal_coarse(point(q_upper), 20)[1],
            'negative_certified': q_upper < 0},
        'failures': failures,
        'scope': 'Actual N=2 only. No large-cutoff or Xi sign assertion.',
        'panels': panels,
    }
    OUT.write_text(json.dumps(certificate, indent=2) + '\n')
    print('status:', certificate['status'])
    print('b0,b2,b4 rational decimal bounds:', coarse)
    print('required for PSD: Q >= 0')
    print('actual certified upper bound:', certificate['decisive_test']['upper_decimal_outward'])
    print('failures:', failures)
    print('full certificate:', OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""One fixed rational interval sufficient test; no subdivisions or search.

Run from riemann: python3 scripts/heat/actual-box-origin-217.py
The input is exactly panel0 of L917, not a new quadrature calculation.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from pathlib import Path
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
import hashlib
import json


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_i(other))

    def __mul__(self, other):
        other = as_i(other)
        ends = [x * y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return I(min(ends), max(ends))

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        if n == 0:
            return I(1)
        if n % 2:
            return I(self.lo ** n, self.hi ** n)
        return I(0 if self.lo <= 0 <= self.hi else min(self.lo ** n, self.hi ** n),
                 max(self.lo ** n, self.hi ** n))


def as_i(value):
    return value if isinstance(value, I) else I(value)


ZERO = (0,) * 6


def const(value):
    return {} if value == 0 else {ZERO: F(value)}


def add(*polys):
    out = {}
    for poly in polys:
        for powers, coefficient in poly.items():
            out[powers] = out.get(powers, F(0)) + coefficient
    return {p: c for p, c in out.items() if c}


def scale(poly, value):
    return {p: c * value for p, c in poly.items() if c * value}


def mul(left, right):
    out = {}
    for lp, lc in left.items():
        for rp, rc in right.items():
            powers = tuple(x + y for x, y in zip(lp, rp))
            out[powers] = out.get(powers, F(0)) + lc * rc
    return {p: c for p, c in out.items() if c}


def evaluate(poly, box):
    out = I(0)
    for powers, coefficient in sorted(poly.items()):
        term = I(coefficient)
        for value, power in zip(box, powers):
            term = term * value ** power
        out = out + term
    return out


def series_product(left, right):
    return [add(*(mul(left[k], right[n-k]) for k in range(n+1))) for n in range(7)]


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, I):
        return {"lower": str(value.lo), "upper": str(value.hi)}
    if isinstance(value, dict):
        if value and all(isinstance(k, tuple) for k in value):
            return [{"e_powers": list(k), "coefficient": str(v)} for k, v in sorted(value.items())]
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def display(value):
    def endpoint(x, rounding):
        with localcontext() as context:
            context.prec = 9
            context.rounding = rounding
            return str(Decimal(x.numerator) / Decimal(x.denominator))
    return '[' + endpoint(value.lo, ROUND_FLOOR) + ', ' + endpoint(value.hi, ROUND_CEILING) + ']'


def main():
    source = Path('scripts/heat/low-time-h2-uniform-195.json')
    source_bytes = source.read_bytes()
    panel = json.loads(source_bytes)['panels'][0]
    assert panel['lambda'] == {'lower': '0', 'upper': '0.0001953125'}
    moments = panel['moments']
    assert set(moments) == {str(2*k) for k in range(7)}
    raw = [I(moments[str(2*k)]['lower'], moments[str(2*k)]['upper']) for k in range(7)]
    assert all(value.lo > 0 for value in raw)
    # Independent normalized boxes only: no shared-mass or parameter constraint.
    y = [I(1)] + [I(value.lo / raw[0].hi, value.hi / raw[0].lo) for value in raw[1:]]
    e = [y[k] * F(1, factorial(2*k)) for k in range(1, 7)]
    g = [const(1)]
    for k in range(1, 7):
        powers = tuple(int(j == k-1) for j in range(6))
        g.append({powers: F((-1)**k)})
    S, a = [{}], [const(1)]
    for n in range(1, 7):
        S.append(add(scale(g[n], -n), *(scale(mul(S[k], g[n-k]), -1) for k in range(1, n))))
        a.append(add(*(scale(mul(g[k], a[n-k]), -1) for k in range(1, n+1))))
    # Independent formal-log and inverse checks fix all signs and factorials.
    w = [{}] + g[1:]
    power = [const(1)] + [{} for _ in range(6)]
    log = [{} for _ in range(7)]
    for r in range(1, 7):
        power = series_product(power, w)
        log = [add(log[n], scale(power[n], F((-1)**(r+1), r))) for n in range(7)]
    log_residual = [add(S[n], scale(log[n], n)) for n in range(1, 7)]
    conv = series_product(g, a)
    inverse_residual = [add(conv[n], const(-int(n == 0))) for n in range(7)]
    assert not any(log_residual) and not any(inverse_residual)
    sb = [I(0)] + [evaluate(poly, e) for poly in S[1:]]
    ab = [evaluate(poly, e) for poly in a]
    delta = sb[2] * sb[4] - sb[3] ** 2
    checks = {
        'exact_panel_band': True, 'complete_seven_moments': True,
        'all_raw_lower_endpoints_positive': True,
        'all_ratio_boxes_positive': all(z.lo > 0 for z in y),
        'finite_log_symbolic_residuals_zero': not any(log_residual),
        'finite_inverse_symbolic_residuals_zero': not any(inverse_residual),
        'S2_strict_lower_positive': sb[2].lo > 0,
        'leading_delta_strict_lower_positive': delta.lo > 0,
    }
    minors = {name: [list(indices) for size in range(1, dim+1)
                    for indices in combinations(range(dim), size)]
              for name, dim in [('M3', 4), ('N2', 3), ('H2', 3)]}
    cert = {
        'schema': 'actual-box-origin-fixed-sufficient-test-217-v1',
        'target': "Test L921's joint-null-row relaxation with L917's fixed panel-zero normalized moment boxes for exact infeasibility, J>=0, or a box-compatible J<0 witness.",
        'source': {'path': str(source), 'sha256': hashlib.sha256(source_bytes).hexdigest(),
                   'pointer': '/panels/0/moments', 'lambda': panel['lambda'],
                   'moment_endpoint_strings': moments, 'exact_moments': raw},
        'y_boxes': y, 'factorial_normalized_e_boxes': e,
        'polynomials_in_e1_through_e6': {'g': g, 'S': S, 'a': a},
        'finite_log_symbolic_residuals': log_residual,
        'finite_inverse_symbolic_residuals': inverse_residual,
        'constraints': {'y0': '1', 'y1': '>0',
            'box': 'All six y_boxes, both closed faces, no added correlation',
            'PSD': {'M3': 'y[i+j], 0<=i,j<=3', 'N2': 'y[i+j+1], 0<=i,j<=2',
                    'H2': 'S[i+j+2], 0<=i,j<=2'},
            'nonempty_principal_minor_indices': minors,
            'c': ['c0^2+c1^2+c2^2=1', 'c2!=0'],
            'null_rows': ['S2*c0+S3*c1+S4*c2=0', 'S3*c0+S4*c1+S5*c2=0',
                          'S4*c0+S5*c1+S6*c2=0'],
            'J': 'sum c_i*c_j*((i+j+2)*a[i+j+2]+a[i+j+1]), 0<=i,j<=2'},
        'bounds': {'S': sb, 'a': ab, 'leading_delta': delta},
        'sufficient_test': 'First two null rows fix direction v if Delta>0; sign J=sign(v^T K v). All remaining premises retained, but not needed for a sufficient positive bound.',
        'checks': checks,
    }
    failed_stage = None
    if sb[2].lo <= 0 or delta.lo <= 0:
        failed_stage = 'leading_block_inversion_not_certified'
    else:
        v = [sb[3]*sb[5] - sb[4]**2, sb[3]*sb[4] - sb[2]*sb[5], delta]
        K = [[(i+j+2)*ab[i+j+2] + ab[i+j+1] for j in range(3)] for i in range(3)]
        terms = [{'indices': [i, j], 'bound': (1 if i == j else 2)*K[i][j]*(v[i]**2 if i == j else v[i]*v[j])}
                 for i in range(3) for j in range(i, 3)]
        numerator = sum((term['bound'] for term in terms), I(0))
        norm_squared = sum((value**2 for value in v), I(0))
        assert norm_squared.lo > 0
        cert['bounds'].update({'v': v, 'K': K, 'numerator_terms': terms,
                              'numerator': numerator, 'norm_squared': norm_squared})
        checks['norm_squared_strict_lower_positive'] = True
        checks['numerator_lower_nonnegative'] = numerator.lo >= 0
        if numerator.lo < 0:
            failed_stage = 'origin_numerator_not_certified_nonnegative'
    cert['outcome'] = 'INCONCLUSIVE' if failed_stage else 'J_NONNEGATIVE_SUFFICIENT_CERTIFICATE'
    cert['failed_stage'] = failed_stage
    cert['failures'] = [key for key, passed in checks.items() if not passed]
    # Exact short brackets compare complete rational endpoints, not previews.
    brackets = {'S2': (sb[2], I('3.7143e-5', '3.7205e-5')),
                'leading_delta': (delta, I('9.71e-16', '6.75e-15'))}
    if 'numerator' in cert['bounds']:
        brackets.update({'numerator': (numerator, I('-8.897e-38', '1.328e-37')),
                         'norm_squared': (norm_squared, I('9.44e-31', '4.557e-29'))})
    cert['verified_short_brackets'] = {
        key: {'outer': short, 'complete_endpoint_comparison': short.lo < value.lo <= value.hi < short.hi}
        for key, (value, short) in brackets.items()}
    assert all(item['complete_endpoint_comparison'] for item in cert['verified_short_brackets'].values())
    cert['signs_from_complete_endpoints'] = {
        key: {'lower_sign': (value.lo > 0) - (value.lo < 0),
              'upper_sign': (value.hi > 0) - (value.hi < 0)}
        for key, (value, _) in brackets.items()}
    cert['qualification'] = 'No witness, infeasibility or actual contact claimed. A failed sufficient bound is inconclusive; no refinement or further search is performed.'
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(encode(cert), indent=2) + '\n')
    print('Outcome:', cert['outcome'])
    print('S2:', display(sb[2]), '; required lower > 0')
    print('Delta:', display(delta), '; required lower > 0')
    if 'numerator' in cert['bounds']:
        print('Origin numerator:', display(cert['bounds']['numerator']), '; required lower >= 0')
        print('Norm squared:', display(cert['bounds']['norm_squared']), '; required lower > 0')
    print('Failures:', cert['failures'])
    print('Full exact certificate:', output)


if __name__ == '__main__':
    main()

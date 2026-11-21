#!/usr/bin/env python3
"""Outward n=2 theta-moment certificate; standard library only.

All elementary values use interval rational Taylor arithmetic, not floats.
See L970 for derivative, series-tail and improper-tail justifications.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
import math

OUT = Path(__file__).with_suffix('.json')
DOWN = Context(prec=60, rounding=ROUND_FLOOR, Emin=-999999, Emax=999999)
UP = Context(prec=60, rounding=ROUND_CEILING, Emin=-999999, Emax=999999)


class IV:
    def __init__(self, a, b=None):
        if isinstance(a, IV):
            self.lo, self.hi = a.lo, a.hi
        elif isinstance(a, F):
            self.lo = DOWN.divide(D(a.numerator), D(a.denominator))
            self.hi = UP.divide(D(a.numerator), D(a.denominator))
        else:
            self.lo, self.hi = D(a), D(a if b is None else b)
        assert self.lo <= self.hi

    def __add__(self, other):
        y = IV(other)
        return IV(DOWN.add(self.lo, y.lo), UP.add(self.hi, y.hi))

    __radd__ = __add__

    def __neg__(self):
        return IV(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + -IV(other)

    def __rsub__(self, other):
        return IV(other) + -self

    def __mul__(self, other):
        y = IV(other)
        pairs = [(a, b) for a in (self.lo, self.hi) for b in (y.lo, y.hi)]
        return IV(min(DOWN.multiply(a, b) for a, b in pairs),
                  max(UP.multiply(a, b) for a, b in pairs))

    __rmul__ = __mul__

    def __truediv__(self, other):
        y = IV(other)
        assert y.lo > 0 or y.hi < 0
        return self * IV(DOWN.divide(D(1), y.hi), UP.divide(D(1), y.lo))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = IV(1)
        for _ in range(n):
            result = result * self
        return result

    def record(self):
        return [str(self.lo), str(self.hi)]


@lru_cache(maxsize=100000)
def exp_point(x):
    """exp(x): Taylor at |z|<=1/8, positive terms then reciprocal/squaring."""
    assert x.is_finite()
    negative = x < 0
    magnitude = x.copy_abs()
    k = 0
    while magnitude > D('0.125'):
        # Comparison only; the actual z is divided outward below.
        magnitude = UP.divide(magnitude, D(2))
        k += 1
    z = IV(x.copy_abs()) / (2**k)
    term, total = IV(1), IV(1)
    for j in range(1, 31):
        term = term*z/j
        total = total+term
    # For 0<=z<=1/8, the entire tail from degree 31 is <=2 z^31/31!.
    remainder = 2*(z**31)/math.factorial(31)
    total = IV(total.lo, UP.add(total.hi, remainder.hi))
    for _ in range(k):
        total = total*total
    return IV(1)/total if negative else total


def exp(x):
    x = IV(x)
    return IV(exp_point(x.lo).lo, exp_point(x.hi).hi)


def atan_bounds(inverse):
    total = F(0)
    for j in range(200):
        total += (-1)**j*F(1, (2*j+1)*inverse**(2*j+1))
        next_term = F(1, (2*j+3)*inverse**(2*j+3))
        if next_term < F(1, 10**70):
            other = total+(-1)**(j+1)*next_term
            return min(total, other), max(total, other), j+1
    raise AssertionError('atan truncation insufficient')


a5, b5, j5 = atan_bounds(5)
a239, b239, j239 = atan_bounds(239)
pi_lo, pi_hi = 16*a5-4*b239, 16*b5-4*a239
PI = IV(IV(pi_lo).lo, IV(pi_hi).hi)
assert PI.lo > 3 and PI.hi < 4


def poly(v, coefficients):
    value = IV(0)
    for c in coefficients:
        value = value*v+c
    return value


def evaluate(u):
    """Return four f, f'' and omitted-n bounds, using one u interval."""
    ehalf, e2 = exp(u/2), exp(2*u)
    kval, kp, kpp = IV(0), IV(0), IV(0)
    for n in range(1, 5):
        v = PI*(n*n)*e2
        weight = ehalf*exp(-v)
        kval += weight*poly(v, [8, -12, 0])
        kp += weight*poly(v, [-16, 60, -30, 0])
        kpp += weight*poly(v, [32, -224, 330, -75, 0])
    # For n>=5, the ratio of n^4 exp(-pi*n^2*e^(2u)) terms is <1/2.
    omitted_k = 10000*(PI**2)*exp(F(9, 2)*u-25*PI*e2)
    result = {}
    for name, alpha in [('b', IV(F(1, 2))), ('h', IV(72))]:
        plus, minus = exp(alpha*u), exp(-alpha*u)
        cosh, sinh = (plus+minus)/2, (plus-minus)/2
        hs = [(cosh, alpha*sinh, (alpha**2)*cosh),
              (u*sinh/(2*alpha), sinh/(2*alpha)+u*cosh/2,
               cosh+alpha*u*sinh/2)]
        for r, (hr, hrp, hrpp) in enumerate(hs):
            result[f'{name}{r}'] = (kval*hr,
                kpp*hr+2*kp*hrp+kval*hrpp, omitted_k*hr)
    return result


def abs_upper(x):
    return max(x.lo.copy_abs(), x.hi.copy_abs())


N = 3072
delta = IV(F(3, N))
keys = ['b0', 'b1', 'h0', 'h1']
sums = {key: IV(0) for key in keys}
derivative_errors = {key: IV(0) for key in keys}
series_errors = {key: IV(0) for key in keys}
cells = []
for j in range(N+1):
    values = evaluate(IV(F(3*j, N)))
    for key in keys:
        weight = F(1, 2) if j in (0, N) else F(1)
        sums[key] += weight*values[key][0]
    if j % 1024 == 0:
        print(f'nodes {j}/{N}', flush=True)
for j in range(N):
    left, right = IV(F(3*j, N)), IV(F(3*(j+1), N))
    values = evaluate(IV(left.lo, right.hi))
    row = {'j': j, 'u': [str(left.lo), str(right.hi)], 'integrands': {}}
    for key in keys:
        second = abs_upper(values[key][1])
        omitted = max(D(0), values[key][2].hi)
        derivative_errors[key] += IV(second)*(delta**3)/12
        series_errors[key] += IV(omitted)*delta
        row['integrands'][key] = {'f_second': values[key][1].record(),
                                 'omitted_theta_upper': str(omitted)}
    cells.append(row)
    if j % 1024 == 0:
        print(f'cells {j}/{N}', flush=True)

# All four integrands on u>=3 are <=16*pi^2*u*exp(77*u-pi*exp(2u)).
# phi'(u)<=77-2*pi*exp(6)<-2000, hence integral <=
# 16*pi^2*exp(phi(3))*(3/2000+1/2000^2).
slope = 77-2*PI*exp(6)
assert slope.hi < -2000
tail = 16*(PI**2)*exp(231-PI*exp(6))*(IV(F(3, 2000))+IV(F(1, 2000**2)))
moments = {}
detail = {}
for key in keys:
    trap = delta*sums[key]
    err = derivative_errors[key]
    # All omitted integrands are positive. Only quadrature widens downward.
    integral = IV(DOWN.subtract(trap.lo, err.hi),
                  UP.add(UP.add(UP.add(trap.hi, err.hi), series_errors[key].hi), tail.hi))
    assert integral.lo > 0
    moments[key] = integral
    detail[key] = {'trapezoid': trap.record(), 'quadrature_error': err.record(),
                   'theta_tail': series_errors[key].record(), 'u_tail': tail.record(),
                   'integral': integral.record()}
r = moments['b1']/moments['b0']
t = moments['h1']/moments['h0']
h, gap = F(5184), F(20735, 4)
d1, d2 = 4*h*h/gap**2, h/gap
required_lower = d1*(F(1, 50)-F(1, 100))-d2*F(1, 40)**2
box_r = r.lo >= IV(F(1, 50)).hi and r.hi <= IV(F(1, 40)).lo
box_t = t.lo > 0 and t.hi <= IV(F(1, 100)).lo
direct_lower = IV(d1)*IV(r.lo)-IV(d2)*IV(r.hi)**2-IV(d1)*IV(t.hi)
passed = box_r and box_t and required_lower > 0 and direct_lower.lo > 0
certificate = {
    'step': 184, 'status': 'PASS' if passed else 'FAIL',
    'parameters': {'N': N, 'u_interval': [0, 3], 'theta_N': 4, 'precision': 60,
                   'exp_degree': 30, 'exp_reduced_argument_max': '1/8'},
    'pi': {'interval': PI.record(), 'Machin_atan_terms': [j5, j239],
           'exact_lower': str(pi_lo), 'exact_upper': str(pi_hi)},
    'improper_tail': {'phi_prime_at_3': slope.record(), 'bound': tail.record()},
    'moments': detail, 'ratios': {'b': r.record(), 'h': t.record()},
    'required_boxes': {'b': ['1/50', '1/40'], 'h': ['0', '1/100']},
    'checks': {'b_box': box_r, 'h_box': box_t,
               'positive_signed_lower': direct_lower.lo > 0},
    'signed_propagation': {
        'formula': 'd1*r+d2*s-d2*r^2-d1*t; s>0 by L966',
        'd1': str(d1), 'd2': str(d2), 's_lower_used': '0',
        'box_lower_exact': str(required_lower), 'direct_lower': direct_lower.record()},
    'failures': [] if passed else [k for k, v in
        {'b_box': box_r, 'h_box': box_t, 'positive_signed_lower': direct_lower.lo > 0}.items() if not v],
    'cells': cells,
}
OUT.write_text(json.dumps(certificate, indent=2)+'\n')
print('status:', certificate['status'])
print('b ratio:', r.record(), 'required [1/50,1/40]')
print('h ratio:', t.record(), 'required (0,1/100]')
print('signed lower:', direct_lower.record(), 'required >0; box lower', required_lower)
print('failures:', certificate['failures'])
print('certificate:', OUT)
assert passed

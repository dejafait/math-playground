#!/usr/bin/env python3
"""Exact integer interval enclosure for L527's fixed bump coefficient.

No floating-point arithmetic is used in the calculation or comparison.
Every interval endpoint is an integer divided by SCALE. Elementary
functions use alternating Taylor series, range reduction and isqrt.
The mathematical quadrature/tail bounds are proved in L527.
"""

import json
from math import isqrt
from pathlib import Path

SCALE = 10**40


def ceildiv(a, b):
    return -((-a) // b)


class I:
    def __init__(self, lo, hi=None):
        self.lo = lo
        self.hi = lo if hi is None else hi
        assert self.lo <= self.hi

    @classmethod
    def q(cls, a, b=1):
        assert b > 0
        return cls((a * SCALE) // b, ceildiv(a * SCALE, b))

    def __add__(self, other):
        return I(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        products = [a * b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return I(min(products) // SCALE, ceildiv(max(products), SCALE))

    def __truediv__(self, other):
        assert other.lo > 0, 'Only positive denominators are used.'
        pairs = [(a * SCALE, b) for a in (self.lo, self.hi)
                 for b in (other.lo, other.hi)]
        return I(min(a // b for a, b in pairs),
                 max(ceildiv(a, b) for a, b in pairs))

    def square(self):
        lowsq = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return I(lowsq // SCALE,
                 ceildiv(max(self.lo**2, self.hi**2), SCALE))

    def sqrt(self):
        assert self.lo >= 0
        low = isqrt(self.lo * SCALE)
        high = isqrt(self.hi * SCALE)
        if high * high < self.hi * SCALE:
            high += 1
        return I(low, high)

    def widen(self, radius):
        assert radius.lo >= 0
        return I(self.lo - radius.hi, self.hi + radius.hi)

    def clip(self, lo, hi):
        return I(max(lo, self.lo), min(hi, self.hi))

    def record(self):
        return {'lower_numerator': str(self.lo),
                'upper_numerator': str(self.hi),
                'denominator': str(SCALE),
                'decimal_enclosure': [render(self.lo), render(self.hi)]}


ZERO, ONE, TWO, FOUR = (I.q(n) for n in (0, 1, 2, 4))


def render(n):
    sign = '-' if n < 0 else ''
    a = abs(n)
    return f'{sign}{a // SCALE}.{a % SCALE:040d}'


def exp_negative(y):
    assert y.lo >= 0
    k = 0
    while y.hi > SCALE // 8:
        y = y / TWO
        k += 1
    term, total = ONE, ONE
    for n in range(1, 33):
        term = term * y / I.q(n)
        total = total - term if n % 2 else total + term
    remainder = term * y / I.q(33)
    total = total.widen(remainder).clip(0, SCALE)
    for _ in range(k):
        total = total.square().clip(0, SCALE)
    return total


def sincos_small(x):
    assert 0 <= x.lo <= x.hi <= SCALE // 8
    x2 = x.square()
    st, ct, ss, cs = x, ONE, x, ONE
    for n in range(1, 17):
        st = st * x2 / I.q((2*n) * (2*n+1))
        ct = ct * x2 / I.q((2*n-1) * (2*n))
        ss = ss - st if n % 2 else ss + st
        cs = cs - ct if n % 2 else cs + ct
    sr = st * x2 / I.q(34 * 35)
    cr = ct * x2 / I.q(33 * 34)
    return ss.widen(sr).clip(-SCALE, SCALE), cs.widen(cr).clip(-SCALE, SCALE)


def sincos(x):
    assert x.lo >= 0
    k = 0
    while x.hi > SCALE // 8:
        x = x / TWO
        k += 1
    s, c = sincos_small(x)
    for _ in range(k):
        s, c = (TWO*s*c).clip(-SCALE, SCALE), (c.square()-s.square()).clip(-SCALE, SCALE)
    return s, c


def arctan_reciprocal(n):
    x = I.q(1, n)
    x2, power, total = x.square(), x, x
    for j in range(1, 41):
        power = power*x2
        term = power/I.q(2*j+1)
        total = total-term if j % 2 else total+term
    return total.widen(power*x2/I.q(83))


def main():
    nx, nt, limit = 512, 2048, 32
    e = ONE/exp_negative(ONE)
    pi = I.q(16)*arctan_reciprocal(5)-FOUR*arctan_reciprocal(239)
    assert e.lo > I.q(8, 3).hi
    dx = I.q(2, nx)
    bump = []
    norm_sum = ZERO
    for i in range(nx//2):
        x = I.q(2*i+1, nx)
        b = exp_negative(ONE/(ONE-x.square()))
        bump.append(b)
        norm_sum = norm_sum+b.square()
    norm_error = I.q(873, 96*nx*nx)
    norm = (TWO*dx*norm_sum).widen(norm_error)
    assert norm.lo > 0
    fourier_error = I.q(489, 3*nx*nx)
    outer_error = I.q(26*limit**3, 24*nt*nt)
    integral_sum = ZERO
    nodes = []
    for j in range(nt):
        t = I.q((2*j+1)*limit, 2*nt)
        s, c = sincos(t/I.q(nx))
        ds, dc = TWO*s*c, c.square()-s.square()
        value = ZERO
        for b in bump:
            value = value+b*c
            s, c = s*dc+c*ds, c*dc-s*ds
        transform = (TWO*dx*value).widen(fourier_error)
        sin2t, cos2t = sincos(TWO*t)
        numerator = e*cos2t-ONE+TWO*t*e*sin2t
        denominator = ((ONE+FOUR*t.square()) *
                       (e.square()+ONE-TWO*e*cos2t)).sqrt()
        phase_cos = (numerator/denominator).clip(-SCALE, SCALE)
        summand = transform.square()*phase_cos
        integral_sum = integral_sum+summand
        nodes.append({'j': j, 't': t.record(),
                      'unnormalized_fourier': transform.record(),
                      'phase_cosine': phase_cos.record(),
                      'integrand': summand.record()})
    integral = (I.q(limit, nt)*integral_sum).widen(outer_error)
    tail = I.q(81, 32*limit*limit)/norm
    coefficient = (integral/(pi*norm)).widen(tail)
    threshold = pi/FOUR
    gamma_limit = -ONE-FOUR*coefficient/pi
    passes = coefficient.hi < threshold.lo and gamma_limit.lo > -2*SCALE
    certificate = {
        'statement': 'c_h < pi/4; therefore -1-4*c_h/pi > -2',
        'arithmetic': 'Outward exact integer intervals, common denominator 10^40; no floating point.',
        'grid': {'nx_on_minus_one_one': nx, 'nt_on_zero_T': nt, 'T': limit},
        'bounds': {'b_sup': '3/8', 'b_prime_sup': '9/8',
                   'b_second_sup': '33', 'b_squared_second_sup': '873/32',
                   'inner_integrand_second_sup': '489',
                   'phase_first_sup': '26/5', 'phase_second_sup': '171/25',
                   'phase_cosine_second_sup': '847/25',
                   'outer_integrand_second_sup': '26',
                   'b_prime_L2_squared_upper': '81/32'},
        'elementary_enclosures': {'e': e.record(), 'pi': pi.record()},
        'bump_L2_squared': norm.record(),
        'errors': {'normalization_midpoint': norm_error.record(),
                   'inner_midpoint': fourier_error.record(),
                   'outer_midpoint': outer_error.record(),
                   'normalized_tail': tail.record()},
        'unnormalized_truncated_integral': integral.record(),
        'coefficient_interval': coefficient.record(),
        'required_threshold': threshold.record(),
        'gamma_limit_interval': gamma_limit.record(),
        'comparison': {'passed': passes,
                       'c_upper_below_threshold_lower': coefficient.hi < threshold.lo,
                       'gamma_lower_above_minus_two': gamma_limit.lo > -2*SCALE},
        'failures': [] if passes else ['The strict comparison was not certified.'],
        'positive_half_bump_nodes': [b.record() for b in bump],
        'outer_nodes': nodes,
    }
    path = Path(__file__).with_name('coefficient-certificate.json')
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print('PASS' if passes else 'FAIL')
    print('c_h enclosure:', render(coefficient.lo), render(coefficient.hi))
    print('Required upper threshold:', render(threshold.lo))
    print('Gamma/(rL) limit enclosure:', render(gamma_limit.lo), render(gamma_limit.hi))
    print('Failures:', certificate['failures'])
    print('Certificate:', path)
    if not passes:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

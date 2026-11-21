#!/usr/bin/env python3
"""Directed Decimal / rational Taylor certificate for the fixed H_K test.

No binary floating point, numerical integration library, Decimal.exp, or
RH assumption is used. See L876 for the integral/operator inequalities.
Run from the active notebook: python3 scripts/primitive-hankel/coefficient-test-24.py
"""

from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
import json
from pathlib import Path

PREC = 50
DENOM = 2000
END = 2
B = F(3, 10)
TERMS = 36


def directed(op, rounding):
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = rounding
        return op()


class I:
    def __init__(self, lo, hi=None):
        self.lo = D(lo)
        self.hi = self.lo if hi is None else D(hi)
        assert self.lo <= self.hi

    @staticmethod
    def fraction(x):
        x = F(x)
        return I(directed(lambda: D(x.numerator) / D(x.denominator), ROUND_FLOOR),
                 directed(lambda: D(x.numerator) / D(x.denominator), ROUND_CEILING))

    def __add__(self, other):
        other = as_i(other)
        return I(directed(lambda: self.lo + other.lo, ROUND_FLOOR),
                 directed(lambda: self.hi + other.hi, ROUND_CEILING))

    __radd__ = __add__

    def __neg__(self):
        # copy_negate is exact and unaffected by the ambient precision.
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + (-as_i(other))

    def __rsub__(self, other):
        return as_i(other) + (-self)

    def __mul__(self, other):
        other = as_i(other)
        pairs = [(a, b) for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(directed(lambda: a * b, ROUND_FLOOR) for a, b in pairs),
                 max(directed(lambda: a * b, ROUND_CEILING) for a, b in pairs))

    __rmul__ = __mul__

    def reciprocal(self):
        assert self.lo > 0
        return I(directed(lambda: D(1) / self.hi, ROUND_FLOOR),
                 directed(lambda: D(1) / self.lo, ROUND_CEILING))

    def __truediv__(self, other):
        return self * as_i(other).reciprocal()

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        answer = I(1)
        for _ in range(n):
            answer = answer * self
        return answer

    def out(self):
        return [str(self.lo), str(self.hi)]


def as_i(x):
    if isinstance(x, I):
        return x
    if isinstance(x, F):
        return I.fraction(x)
    return I(x)


def exp_point(x):
    """Enclose exp(x) by a positive Taylor sum, geometric tail, squaring."""
    x = D(x)
    if x < 0:
        return exp_point(x.copy_negate()).reciprocal()
    y = I(x)
    squarings = 0
    while y.hi > D('0.125'):
        y = y / 2
        squarings += 1
    term = I(1)
    total = I(1)
    for k in range(1, TERMS + 1):
        term = term * y / k
        total = total + term
    next_term = term * y / (TERMS + 1)
    tail = next_term / (1 - y / (TERMS + 2))
    total = I(total.lo, (total + tail).hi)
    for _ in range(squarings):
        total = total * total
    return total


def exp_i(x):
    x = as_i(x)
    return I(exp_point(x.lo).lo, exp_point(x.hi).hi)


def atan_bounds(q, terms):
    s = sum((F((-1)**k, (2*k + 1) * q**(2*k + 1))
             for k in range(terms)), F(0))
    nxt = F((-1)**terms, (2*terms + 1) * q**(2*terms + 1))
    return min(s, s + nxt), max(s, s + nxt)


def pi_interval():
    a, aa = atan_bounds(5, 55)
    b, bb = atan_bounds(239, 18)
    return I(I.fraction(16*a - 4*bb).lo, I.fraction(16*aa - 4*b).hi)


def q(v):
    assert v.lo > 3
    return 4 * v * (2*v - 3) * exp_i(-v)


def int_power(a, b, j):
    return I.fraction((b**(j+1) - a**(j+1)) / (j+1))


def main():
    pi = pi_interval()
    assert 3 < pi.lo < pi.hi < 4
    # Sum n>=3: n=3+j, n^4<=81*16^j, n^2>=9+7*j.
    eps = (8*pi**2*81*exp_i(-9*pi) /
           (1 - 16*exp_i(-7*pi)))
    assert eps.hi < D('1e-8')

    # Verify the elementary constants used in the analytic half-line bound.
    e4 = exp_i(4)
    e13 = exp_i(13)
    assert e4.lo > 54 and e13.lo > 256
    assert (16*exp_i(-3*pi)).hi < D('0.5')

    # K(u)<=exp(-70u) on u>=2. Exact integrals of that envelope.
    def exp_tail(j, rate):
        # Integral_2^infinity u^j exp(-rate*u) du, by j integrations by parts.
        coeff = F(0)
        falling = 1
        for k in range(j+1):
            if k:
                falling *= j-k+1
            coeff += F(falling * END**(j-k), rate**(k+1))
        return exp_i(-rate*END) * coeff

    mtails = {j: exp_tail(j, 70) for j in (0, 2, 4)}
    ttail = exp_tail(1, 140)

    sums = {j: I(0) for j in (0, 2, 4)}
    trace = I(0)
    trial_integral = I(0)
    k_min = None
    k_max = D(0)

    def edge(i):
        u = F(i, DENOM)
        ehalf = exp_i(I.fraction(u/2))
        e2 = exp_i(I.fraction(2*u))
        return ehalf, q(pi*e2) + q(4*pi*e2)

    left_e, left_q = edge(0)
    for i in range(END*DENOM):
        right_e, right_q = edge(i+1)
        lower = (left_e * I(right_q.lo)).lo
        upper = (right_e * I(left_q.hi) + I(eps.hi)).hi
        kval = I(lower, upper)
        assert 0 < lower <= upper
        k_min = lower if k_min is None else min(k_min, lower)
        k_max = max(k_max, upper)
        a, b = F(i, DENOM), F(i+1, DENOM)
        for j in sums:
            sums[j] = sums[j] + kval * int_power(a, b, j)
        trace = trace + kval**2 * int_power(a, b, 1)
        if b <= B:
            weight = (b*b-a*a)/2
        elif a >= B and b <= 2*B:
            weight = 2*B*(b-a) - (b*b-a*a)/2
        elif a >= 2*B:
            weight = F(0)
        else:
            raise AssertionError('Trial corners must coincide with mesh edges')
        trial_integral = trial_integral + kval * weight
        left_e, left_q = right_e, right_q

    moments = {j: I(sums[j].lo, (sums[j] + mtails[j]).hi) for j in sums}
    trace = I(trace.lo, (trace + ttail).hi)
    trial = trial_integral / B
    m0, m2, m4 = (moments[j] for j in (0, 2, 4))
    s1 = m2/(2*m0)
    s2 = (3*m2**2-m0*m4)/(12*m0**2)
    c = s1/trace
    purity_lower = (I(trial.lo)**4 / I(trace.hi)**2).lo
    # Positive spectral eigenvalues yield J^4<=Tr(A^2)<=(Tr A)^2.
    residual_lower = (I(s1.lo)**2 * I(purity_lower) - I(s2.hi)).lo
    residual_upper = (I(s1.hi)**2 - I(s2.lo)).hi
    tr_a2 = I((I(trial.lo)**4).lo, (I(trace.hi)**2).hi)
    residual = I(residual_lower, residual_upper)
    failures = []
    if residual.lo <= 0:
        failures.append('Residual lower bound did not exceed required threshold zero')
    result = {
        'target': 'Fixed unshifted H_K; A=H_K^*H_K; c=S_1/Tr(A); residual c^2 Tr(A^2)-S_2',
        'rigorous': True,
        'arithmetic': {
            'precision': PREC, 'rounding': 'ROUND_FLOOR / ROUND_CEILING for every arithmetic operation',
            'exp': 'positive Taylor sum k=0..36 after reduction to [0,1/8], next-term geometric tail, interval squaring; negative inputs by reciprocal',
            'pi': 'Machin formula with alternating rational atan sums: 55 terms for 1/5 and 18 for 1/239',
            'binary_float_or_Decimal_exp_used': False,
        },
        'parameters': {'mesh_denominator': DENOM, 'cells': END*DENOM, 'endpoint': END, 'trial_b': str(B), 'retained_n': [1, 2]},
        'constants': {'pi': pi.out(), 'e4': e4.out(), 'e13': e13.out(), 'n_ge_3_uniform_kernel_tail': eps.out()},
        'integration': {
            'K_cell_lower': 'exp(a/2) [q(pi exp(2b))+q(4pi exp(2b))] lower endpoint',
            'K_cell_upper': 'exp(b/2) [q(pi exp(2a))+q(4pi exp(2a))] upper endpoint plus uniform n>=3 tail',
            'tail_envelope': 'K(u)<=exp(-70u), u>=2',
            'moment_tail_bounds': {str(j): mtails[j].out() for j in mtails},
            'TrA_tail_bound': ttail.out(),
            'smallest_K_cell_lower': str(k_min), 'largest_K_cell_upper': str(k_max),
            'compact_moment_integrals': {str(j): sums[j].out() for j in sums},
        },
        'enclosures': {
            'M0': m0.out(), 'M2': m2.out(), 'M4': m4.out(),
            'TrA': trace.out(), 'J': trial.out(), 'S1': s1.out(), 'S2': s2.out(), 'c': c.out(),
            'TrA2': tr_a2.out(), 'purity_lower': str(purity_lower), 'residual': residual.out(),
        },
        'required_threshold': '0', 'decision': 'REJECT_FIXED_ANSATZ' if not failures else 'INCONCLUSIVE',
        'failures': failures,
        'qualifications': ['No identity, RH or real-zero assumption used', 'TrA2 enclosure uses a spectral lower/upper bound, not equality to quadrature', 'Only the fixed ansatz is tested; no higher coefficients or fitted corrections'],
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'decision': result['decision'], 'residual': residual.out(),
                      'required_threshold': '0', 'failures': failures, 'certificate': str(output)}))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())

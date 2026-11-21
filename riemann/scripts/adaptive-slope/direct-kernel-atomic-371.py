#!/usr/bin/env python3
"""Finite atomic LOWER certificates, never an asymptotic or mesh certificate.

Only the Python standard library is used. Every kernel value is enclosed
by directed Decimal interval arithmetic and a proved exponential series
tail. Linear elimination merely proposes rational weights; verification
uses those rational weights and the original complete kernel afresh.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, getcontext
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, isqrt
from pathlib import Path
import argparse
import json

PREC = 240
getcontext().prec = PREC
LO = Context(prec=PREC, rounding=ROUND_FLOOR)
HI = Context(prec=PREC, rounding=ROUND_CEILING)


class R:
    def __init__(self, lo=0, hi=None):
        if isinstance(lo, R):
            self.lo, self.hi = lo.lo, lo.hi
        elif isinstance(lo, F):
            self.lo = LO.divide(D(lo.numerator), D(lo.denominator))
            self.hi = HI.divide(D(lo.numerator), D(lo.denominator))
        else:
            self.lo, self.hi = D(lo), D(lo if hi is None else hi)

    def __add__(self, b):
        b = R(b)
        return R(LO.add(self.lo, b.lo), HI.add(self.hi, b.hi))

    def __neg__(self):
        return R(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, b):
        return self + (-R(b))

    def __mul__(self, b):
        b = R(b)
        pairs = [(a, c) for a in (self.lo, self.hi) for c in (b.lo, b.hi)]
        return R(min(LO.multiply(a, c) for a, c in pairs),
                 max(HI.multiply(a, c) for a, c in pairs))

    def __truediv__(self, b):
        b = R(b)
        if b.lo <= 0 <= b.hi:
            raise ArithmeticError('interval division contains zero')
        return self * R(LO.divide(D(1), b.hi), HI.divide(D(1), b.lo))

    def upper_abs(self):
        return max(self.lo.copy_abs(), self.hi.copy_abs())

    def lower_abs(self):
        if self.lo <= 0 <= self.hi:
            return D(0)
        return min(self.lo.copy_abs(), self.hi.copy_abs())

    def midpoint(self):
        return (self.lo + self.hi) / 2

    def json(self):
        return [str(self.lo), str(self.hi)]


class C:
    def __init__(self, re=0, im=0):
        if isinstance(re, C):
            self.re, self.im = re.re, re.im
        else:
            self.re, self.im = R(re), R(im)

    def __add__(self, b):
        b = C(b)
        return C(self.re + b.re, self.im + b.im)

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, b):
        return self + (-C(b))

    def __mul__(self, b):
        b = C(b)
        return C(self.re*b.re-self.im*b.im, self.re*b.im+self.im*b.re)

    def __truediv__(self, b):
        b = C(b)
        norm = b.re*b.re + b.im*b.im
        return C((self.re*b.re+self.im*b.im)/norm,
                 (self.im*b.re-self.re*b.im)/norm)

    def upper_abs(self):
        # Deliberate l1 upper bound on the COMPLEX MODULUS.
        return HI.add(self.re.upper_abs(), self.im.upper_abs())

    def lower_abs(self):
        return max(self.re.lower_abs(), self.im.lower_abs())

    def midpoint(self):
        return C(self.re.midpoint(), self.im.midpoint())

    def json(self):
        return {'re': self.re.json(), 'im': self.im.json()}


def exp_ball(z):
    """Enclose exp(z); reduce |z|_1 <=1/8, sum through degree 128.

    The remaining complex modulus is <=2/(8^129*129!), because the
    ratio of consecutive absolute tail terms is at most 1/8.
    Expanding each coordinate by that amount encloses the tail.
    Repeated interval squaring then encloses the original exponential.
    """
    z = C(z)
    scale = 0
    while z.upper_abs() > D(1)/8:
        z = z / 2
        scale += 1
    term = total = C(1)
    for k in range(1, 129):
        term = term*z/k
        total = total+term
    error = R(F(2, 8**129*factorial(129))).hi
    total = total + C(R(-error, error), R(-error, error))
    for _ in range(scale):
        total = total*total
    return total


@lru_cache(None)
def exact_exp(re, im=F(0)):
    return exp_ball(C(re, im))


def primitive_coefficients(n, a):
    # K=(L_{n+1}^{(2)}-1)/(n+1), including its constant subtraction.
    p = [F((-1)**j*comb(n+3, n+1-j), factorial(j)*(n+1))
         for j in range(n+2)]
    p[0] -= F(1, n+1)
    q = [C(0) for _ in p]
    for j in range(n+1, -1, -1):
        q[j] = (C(p[j])-(q[j+1]*(j+1) if j < n+1 else C(0)))/a
    return q


def evaluate_polynomial(q, t):
    value = C(0)
    for a in reversed(q):
        value = value*t+a
    return value


def kernel_column(n, slopes, z_re, z_im):
    """Exact polynomial antiderivatives; no quadrature or asymptotics."""
    values = [C(0) for _ in slopes]
    for base in (F(-1, 8), F(-7, 8)):
        ar, ai = base-z_im, z_re
        q = primitive_coefficients(n, C(ar, ai))

        def at(t):
            return exact_exp(ar*t, ai*t)*evaluate_polynomial(q, t)

        lower = at(F(n+2))-at(F(n))
        for l, c in enumerate(slopes):
            upper = at(c*(n+2))-at(c*n)
            values[l] = values[l]-(upper-lower)*exact_exp(-c*n/4)
    return values


def propose_weights(columns):
    """Square elimination is a heuristic proposal, NOT a rank assertion."""
    size = len(columns)
    a = [[columns[j][l].midpoint() for l in range(size)]
         + [(-columns[j][-1]).midpoint()] for j in range(size)]
    for k in range(size):
        p = max(range(k, size), key=lambda r: a[r][k].upper_abs())
        a[k], a[p] = a[p], a[k]
        for r in range(k+1, size):
            mult = (a[r][k]/a[k][k]).midpoint()
            for j in range(k+1, size+1):
                a[r][j] = (a[r][j]-mult*a[k][j]).midpoint()
            a[r][k] = C(0)
    weights = [C(0) for _ in range(size)]
    for r in range(size-1, -1, -1):
        rhs = a[r][size]
        for j in range(r+1, size):
            rhs = (rhs-a[r][j]*weights[j]).midpoint()
        weights[r] = (rhs/a[r][r]).midpoint()
    weights.append(C(1))
    scale = max(w.upper_abs() for w in weights)
    integers = [(int(w.re.midpoint()/scale*D(10)**120),
                 int(w.im.midpoint()/scale*D(10)**120)) for w in weights]
    denominator = sum(abs(x)+abs(y) for x, y in integers)
    if denominator == 0:
        raise ArithmeticError('zero candidate')
    # Exact rational weights; sum(|Re w|+|Im w|)=1, hence complex TV<=1.
    return [(F(x, denominator), F(y, denominator)) for x, y in integers]


def pairing(weights, values):
    total = C(0)
    for (wr, wi), v in zip(weights, values):
        total = total+C(wr, wi)*v
    return total


def run(n):
    slopes = [F(7, 4)+F(l, 2*(n+1)) for l in range(n+2)]
    gammas = [F(15, 8)+F(j, 4*n) for j in range(n+1)]
    columns = [kernel_column(n, slopes, gamma, F(0)) for gamma in gammas]
    target = kernel_column(n, slopes, F(1), F(1, 8))
    weights = propose_weights(columns)
    target_pair = pairing(weights, target)
    band_pairs = [pairing(weights, col) for col in columns]
    leakage = max(p.upper_abs() for p in band_pairs)
    den = 10**80
    rt = isqrt(n*den*den)
    sqrt_n = R(R(F(rt, den)).lo, R(F(rt+1, den)).hi)
    budget = exp_ball(C(sqrt_n)).re
    lower = LO.subtract(target_pair.lower_abs(), HI.multiply(budget.hi, leakage))
    lower = max(D(0), lower)
    scaled_lower = LO.multiply(lower, exact_exp(F(n, 64)).re.lo)
    raw_width = max(HI.subtract(v.re.hi, v.re.lo) for col in columns+[target] for v in col)
    imag_width = max(HI.subtract(v.im.hi, v.im.lo) for col in columns+[target] for v in col)
    return {
        'n': n, 'slopes': [str(c) for c in slopes],
        'gammas': [str(g) for g in gammas],
        'rational_weights': [[str(r), str(i)] for r, i in weights],
        'rectangular_variation_exact': str(sum(abs(r)+abs(i) for r, i in weights)),
        'kernel_columns': [[v.json() for v in col] for col in columns],
        'target_column': [v.json() for v in target],
        'target_pairing': target_pair.json(),
        'band_pairings': [p.json() for p in band_pairs],
        'target_modulus_lower': str(target_pair.lower_abs()),
        'band_modulus_upper': str(leakage), 'budget': budget.json(),
        'E_n_lower': str(lower), 'scaled_lower': str(scaled_lower),
        'largest_kernel_coordinate_width': str(max(raw_width, imag_width)),
        'finite_lower_positive': lower > 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--degrees', nargs='+', type=int, default=[4, 8, 12, 16])
    args = parser.parse_args()
    out = Path(__file__).with_suffix('.json')
    report = {
        'status': 'FINITE_ATOMIC_LOWER_CERTIFICATES_ONLY',
        'arithmetic': '240-digit outward Decimal rectangles; degree-128 exponential with exact tail bound and scaling/squaring',
        'threshold': 'Asymptotic obstruction requires E_n*exp(n/64) unbounded on an unbounded integer subsequence; finite lower values cannot decide it.',
        'method': 'n+2 equispaced slope atoms; near-null vector of n+1 complete band columns; exact rational weights with complex TV<=1; weak support-function lower bound',
        'failures': ['No all-n lower estimate', 'No primal upper certificate', 'No optimality claim for the chosen witness'],
        'runs': [],
    }
    for n in args.degrees:
        if n < 2:
            raise ValueError('n must be >=2')
        row = run(n)
        report['runs'].append(row)
        out.write_text(json.dumps(report, indent=2)+'\n')
        print(f"n={n} lower={D(row['E_n_lower']):.8E} scaled={D(row['scaled_lower']):.8E} leakage<={D(row['band_modulus_upper']):.3E} coordinate_width<={D(row['largest_kernel_coordinate_width']):.3E}", flush=True)
        exact_exp.cache_clear()
    print('Required: an unbounded-subsequence lower rate; NOT established.')
    print('Full certificate:', out)


if __name__ == '__main__':
    main()

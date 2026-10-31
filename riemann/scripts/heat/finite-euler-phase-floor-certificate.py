#!/usr/bin/env python3
"""Standalone exact-rational reproduction of the L496 scalar envelope."""
from fractions import Fraction as F
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
import json
import math

GRID = 10**70
LOG_TERMS = 100
EXP_DEGREE = 180
evaluations = []
checks = []


def down(q):
    return F(q.numerator * GRID // q.denominator, GRID)


def up(q):
    return -down(-q)


def rat(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = interval(other)
        return I(down(self.lo + other.lo), up(self.hi + other.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -interval(other)

    def __rsub__(self, other):
        return interval(other) + -self

    def __mul__(self, other):
        other = interval(other)
        ends = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(down(min(ends)), up(max(ends)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = interval(other)
        assert other.lo * other.hi > 0, "denominator interval contains zero"
        return self * I(down(1/other.hi), up(1/other.lo))

    def data(self):
        return {"lower": rat(self.lo), "upper": rat(self.hi)}


def interval(x):
    return x if isinstance(x, I) else I(x)


def atan_reciprocal(n):
    # The first omitted term has positive sign after an even number of terms.
    count = 100
    total = sum((F((-1)**j, (2*j+1)*n**(2*j+1)) for j in range(count)), F(0))
    remainder = F(1, (2*count+1)*n**(2*count+1))
    ans = I(down(total), up(total + remainder))
    evaluations.append({"kind": "atan_reciprocal", "n": n, "count": count,
                        "partial_sum": rat(total), "remainder_upper": rat(remainder),
                        "enclosure": ans.data()})
    return ans


def log_unit(v):
    assert 1 <= v <= 2
    z = (v-1)/(v+1)
    z2 = z*z
    power = I(down(z), up(z))
    total = I(0)
    for j in range(LOG_TERMS):
        total = total + power / (2*j+1)
        power = power * z2
    tail = 2*power.hi / ((2*LOG_TERMS+1)*(1-z2))
    ans = I(down(2*total.lo), up(2*total.hi + tail))
    evaluations.append({"kind": "log_unit", "v": rat(v), "z": rat(z),
                        "count": LOG_TERMS, "sum": total.data(),
                        "first_omitted_power": power.data(), "tail_upper": rat(tail),
                        "enclosure": ans.data()})
    return ans


LOG2 = log_unit(F(2))


def log_exact(q):
    assert q > 0
    v, k = q, 0
    while v >= 2:
        v /= 2
        k += 1
    while v < 1:
        v *= 2
        k -= 1
    ans = k*LOG2 + log_unit(v)
    evaluations.append({"kind": "log_range_reduction", "q": rat(q),
                        "k": k, "v": rat(v), "enclosure": ans.data()})
    return ans


def logarithm(q):
    q = interval(q)
    lo, hi = log_exact(q.lo), log_exact(q.hi)
    return I(lo.lo, hi.hi)


def exp_exact(q):
    a = abs(q)
    assert a < EXP_DEGREE+2
    term = I(1)
    total = I(1)
    for k in range(1, EXP_DEGREE+1):
        term = term * a / k
        total = total + term
    tail = term.hi*a/(EXP_DEGREE+1)/(1-a/(EXP_DEGREE+2))
    ans = I(total.lo, up(total.hi+tail))
    if q < 0:
        ans = I(down(1/ans.hi), up(1/ans.lo))
    evaluations.append({"kind": "exp", "q": rat(q), "degree": EXP_DEGREE,
                        "sum": total.data(), "last_term": term.data(),
                        "tail_upper": rat(tail), "enclosure": ans.data()})
    return ans


def exponential(q):
    return I(exp_exact(q.lo).lo, exp_exact(q.hi).hi)


def less(name, actual_upper, required):
    checks.append({"name": name, "actual_upper": rat(actual_upper),
                   "required_strict_upper": rat(required), "passed": actual_upper < required})


def show(q, lower=False):
    with localcontext() as ctx:
        ctx.prec = 22
        ctx.rounding = ROUND_FLOOR if lower else ROUND_CEILING
        return str(Decimal(q.numerator)/Decimal(q.denominator))


X, t0, t1 = F('6000284561421.5'), F('.16836'), F('.1718')
cap = F('.500000000001')
pi = 16*atan_reciprocal(5) - 4*atan_reciprocal(239)
log4pi = logarithm(4*pi)
L = logarithm(X) - log4pi
Lstar = logarithm(X*X+1)/2 - log4pi
sigma = F('.5') + t0*Lstar/4 - F(t0, 2*(1+X*X))
nu_cap = F(1, 2) + t1/(4*(X-6))
less('nu derivative cap', nu_cap, cap)
primes = [p for p in range(2, 308)
          if all(p % d for d in range(2, math.isqrt(p)+1))]
assert len(primes) == 63 and primes[-1] == 307
logs = {p: logarithm(p) for p in primes}
less('time monotonicity for every prime',
     logs[307].hi + 2/(1+X*X), Lstar.lo)
less('base phase source lower height', F('6000284561419.5'), X)
less('base phase source upper time', t1, F('.2'))
rows = []
loss_sum = I(0)
for p in primes:
    h = logs[p]
    exponent = t0*h*h/4 - sigma*h
    r = exponential(exponent)
    less(f'r_{p} < 1', r.hi, F(1))
    contribution = h*r/(1-r)
    loss_sum = loss_sum + contribution
    rows.append({"p": p, "log_p": h.data(), "exponent": exponent.data(),
                 "r": r.data(), "denominator": (1-r).data(),
                 "loss_contribution": contribution.data()})
floor = L - 4*cap*loss_sum
less('uniform phase floor exceeds 24.18', F('24.18'), floor.lo)
max_radius = max(F(int(row['r']['upper']['numerator']),
                   int(row['r']['upper']['denominator'])) for row in rows)
less('maximum prime radius below .32926', max_radius, F('.32926'))
less('displayed phase interval lower', F('24.18022820120389189144'), floor.lo)
less('displayed phase interval upper', floor.hi, F('24.18022820120389189145'))
failures = [c['name'] for c in checks if not c['passed']]
output = Path(__file__).with_suffix('.json')
certificate = {
    "result": "FAIL" if failures else "PASS",
    "method": "Exact Fraction intervals on a 10^-70 grid; Machin pi, alternating arctan, range-reduced atanh logarithms, Taylor/geometric exponential tails.",
    "scope": "Scalar envelope at the worst corner; analytic monotonicity, phase identity and imported base phase are justified in L496. No coefficient reserve or collision exclusion.",
    "parameters": {"X": rat(X), "t0": rat(t0), "t1": rat(t1), "cap": rat(cap),
                   "grid_denominator": str(GRID)},
    "corner": {"pi": pi.data(), "L": L.data(), "Lstar": Lstar.data(),
               "sigma": sigma.data(), "nu_derivative_cap": rat(nu_cap)},
    "primes": primes, "prime_rows": rows, "loss_sum": loss_sum.data(),
    "phase_floor": floor.data(), "max_radius_upper": rat(max_radius),
    "checks": checks, "failures": failures,
    "evaluations": evaluations,
}
output.write_text(json.dumps(certificate, indent=2)+'\n')
print(f"{certificate['result']}: {len(checks)} checks, {len(primes)} primes; failures={failures}")
print(f"phase floor lower={show(floor.lo, True)}; required >24.18")
print(f"phase floor upper={show(floor.hi)}")
print(f"max r_p upper={show(max_radius)}; required <.32926<1")
print(f"nu' cap upper={show(nu_cap)}; required <{cap}")
print(f"certificate={output}")
raise SystemExit(bool(failures))

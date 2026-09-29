"""Finite Bessel-order gap certificate for L355; not a statement about zeta.

Uses L037's outward Decimal arithmetic. Logarithms and arctangents
are enclosed by power series with explicit tails, rather than a new
transcendental-library contract. Floating-point values only propose
rational brackets; every accepted assertion is checked with intervals.
See L355 for the analytic gap estimate above order parameter 100.
"""

import cmath
from fractions import Fraction as Q
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "hankel"))
from certify_hankel import I, PRECISION, pi_bounds  # noqa: E402

TERMS = 96
PI = pi_bounds()


def widen(value, radius):
    r = I.lift(radius).hi
    return value + I(r.copy_negate(), r)


def log_series(x):
    # x lies in [1, 3], so |(x-1)/(x+1)| <= 1/2.
    if not (1 <= x.lo <= x.hi <= 3):
        raise ArithmeticError("Log-series range")
    t = (x-1)/(x+1)
    t2 = t*t
    power = t
    total = I(0)
    for j in range(TERMS):
        total += power/(2*j+1)
        power *= t2
    r = I(t.magnitude())
    tail = 2*r**(2*TERMS+1)/((2*TERMS+1)*(1-r*r))
    return widen(2*total, tail)


LOG_TWO = log_series(I(2))


def log_interval(x):
    if x.lo < 1:
        raise ArithmeticError("This certificate only needs log x for x >= 1")
    count = 0
    while x.lo >= 2:
        x /= 2
        count += 1
    return count*LOG_TWO + log_series(x)


def atan_interval(x):
    if x.hi < 0:
        return -atan_interval(-x)
    if x.lo > 1:
        return PI/2 - atan_interval(I(1)/x)
    if x.lo > Q(1, 2):
        return PI/4 + atan_interval((x-1)/(x+1))
    r = I(x.magnitude())
    if r.hi > Q(1, 2):
        raise ArithmeticError("Arctangent reduction range")
    total, power, x2 = I(0), x, x*x
    for j in range(TERMS):
        total += ((-1)**j)*power/(2*j+1)
        power *= x2
    # Absolute geometric remainder works also for interval arguments.
    tail = r**(2*TERMS+1)/((2*TERMS+1)*(1-r*r))
    return widen(total, tail)


def bessel_series(v):
    if v.lo < 9:
        raise ArithmeticError("Bessel-series tail range")
    chi = PI*PI
    real, imag = I(1), I(0)
    sr, si = real, imag
    for j in range(1, 65):
        denominator = j*(j*j+v*v)
        real, imag = (chi*(j*real+v*imag)/denominator,
                      chi*(j*imag-v*real)/denominator)
        sr, si = sr+real, si+imag
    tail = I.rational(Q(50, 49)*Q(10, 9)**65/math.factorial(65))
    return widen(sr, tail), widen(si, tail)


def phase_interval(v):
    # Gamma recurrence to w=33+i*v, then Stirling with 1/(12w).
    denominator = 33**2+v*v
    phase = (I.rational(Q(65, 2))*atan_interval(v/33)
             + v*log_interval(denominator)/2-v
             - v/(12*denominator))
    for j in range(1, 33):
        phase -= atan_interval(v/j)
    # DLMF 5.11(ii): sec(arg(w)/2)^4 < 4 and |w| >= 33.
    phase = widen(phase, I.rational(Q(1, 90*33**3)))
    real, imag = bessel_series(v)
    if real.lo <= 0:
        raise ArithmeticError("Bessel argument requires positive real part")
    return phase-v*log_interval(PI)-atan_interval(imag/real)


def approximate_phase(v):
    # Discovery only. No acceptance test uses this returned float.
    w = complex(33, v)
    g = (w-.5)*cmath.log(w)-w+1/(12*w)
    g -= sum((cmath.log(complex(j, v)) for j in range(1, 33)), 0j)
    term = total = 1+0j
    for j in range(1, 65):
        term *= math.pi**2/(j*complex(j, v))
        total += term
    return g.imag-v*math.log(math.pi)-cmath.phase(total)


def certify():
    rows = []
    brackets = []
    sign_margins = []
    for n in range(1, 81):
        lo, hi = 9., 102.
        for _ in range(45):
            mid = (lo+hi)/2
            if approximate_phase(mid) < n*math.pi:
                lo = mid
            else:
                hi = mid
        center = round(100000*(lo+hi)/2)
        left, right = Q(center-2, 100000), Q(center+2, 100000)
        lp = phase_interval(I.rational(left))-n*PI
        rp = phase_interval(I.rational(right))-n*PI
        if not (-PI.lo < lp.lo <= lp.hi < 0 < rp.lo <= rp.hi < PI.lo):
            raise ArithmeticError(f"Sign bracket failed: {n}")
        sign_margins.extend((lp.hi.copy_negate(), rp.lo))
        brackets.append((left, right))
        rows.append({"phase_index": n, "left": str(left), "right": str(right),
                     "left_phase_minus_n_pi": lp.data(),
                     "right_phase_minus_n_pi": rp.data()})

    gap_margins = []
    for (left, _), (_, right) in zip(brackets, brackets[1:]):
        l = I.rational(left)
        margin = PI/log_interval(l/PI)-I.rational(right-left)
        if margin.lo <= Q(8, 10000):
            raise ArithmeticError("Consecutive witness gap failed")
        gap_margins.append(margin.lo)

    # The same bracket can contain more than one zero. Its width is
    # also safely below the gap threshold throughout the finite range.
    assert all(r-l == Q(1, 25000) for l, r in brackets)
    assert all(9 < l < r < 102 for l, r in brackets)
    assert all(r < l for (_, r), (l, _) in zip(brackets, brackets[1:]))
    assert min(sign_margins) > Q(19, 1000000)
    assert brackets[0][1] < 10 and brackets[0][0] > 9
    assert 100 < brackets[-1][0] < brackets[-1][1] < 102
    assert PI.lo > 3 and PI.hi < Q(22, 7)
    small_margin = PI/log_interval(I(7)/PI)-(10-2*PI)
    # On [2*pi, 7] use this constant bound. On [7, 10],
    # g(v)=v+pi/log(v/pi) is increasing and g(7)>10.
    at_seven = 7+PI/log_interval(I(7)/PI)-10
    increasing = 1-PI/(7*log_interval(I(7)/PI)**2)
    if not (small_margin.lo > Q(1, 5) and at_seven.lo > 0
            and increasing.lo > Q(3, 10)):
        raise ArithmeticError("Initial range coverage failed")
    internal_width = PI/log_interval(I(102)/PI)-I.rational(Q(1, 25000))
    if internal_width.lo <= 0:
        raise ArithmeticError("Within-bracket coverage failed")
    return {
        "scope": "Bessel-order witness brackets and exact finite gap bound; not RH",
        "arithmetic_contract": "L037", "precision": PRECISION,
        "phase_tail_bound": str(Q(1, 90*33**3)),
        "series_terms": TERMS, "bessel_last_term": 64,
        "brackets": rows,
        "minimum_phase_sign_margin": str(min(sign_margins)),
        "minimum_witness_gap_margin": str(min(gap_margins)),
        "initial_range_margin": small_margin.data(),
        "at_seven_margin": at_seven.data(),
        "increasing_g_margin": increasing.data(),
        "within_bracket_gap_margin": internal_width.data(),
        "finite_gap_certified": True,
    }


if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))

#!/usr/bin/env python3
"""Rigorous dyadic scalar inputs and rational power-log error certificate.

This does NOT construct or certify either finite Schur matrix. The interval
operations below use integer floor/ceiling only. All endpoints are saved as
integers with the common denominator 2**BITS; no float decides a check.
"""
from decimal import Context, Decimal, ROUND_CEILING
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import json

BITS = 2048
SCALE = 1 << BITS
LOG_TERMS = 700
MOMENT_LAST = 256


def ceildiv(n, d):
    assert d > 0
    return -((-n)//d)


class Ball:
    """Closed interval [lo/SCALE,hi/SCALE], with exact integer endpoints."""
    def __init__(self, lo, hi=None):
        self.lo = int(lo)
        self.hi = int(lo if hi is None else hi)
        assert self.lo <= self.hi

    @classmethod
    def rational(cls, n, d=1):
        assert d > 0
        return cls(n*SCALE//d, ceildiv(n*SCALE, d))

    def __add__(self, other):
        return Ball(self.lo+other.lo, self.hi+other.hi)

    def __neg__(self):
        return Ball(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        products = [self.lo*other.lo, self.lo*other.hi,
                    self.hi*other.lo, self.hi*other.hi]
        return Ball(min(products)//SCALE, ceildiv(max(products), SCALE))

    def __truediv__(self, other):
        assert other.lo > 0
        # Extrema of x/y on a rectangle with y>0 occur at corners.
        corners = [(self.lo, other.lo), (self.lo, other.hi),
                   (self.hi, other.lo), (self.hi, other.hi)]
        return Ball(min(x*SCALE//y for x,y in corners),
                    max(ceildiv(x*SCALE,y) for x,y in corners))

    def integer_div(self, n):
        assert n > 0
        return Ball(self.lo//n, ceildiv(self.hi,n))

    def sqrt(self):
        assert self.lo >= 0
        lo = isqrt(self.lo*SCALE)
        hi = isqrt(self.hi*SCALE)
        return Ball(lo, hi if hi*hi == self.hi*SCALE else hi+1)

    def nonnegative(self):
        # Used only for quantities proved nonnegative in C744j's series.
        assert self.hi >= 0
        return Ball(max(0,self.lo),self.hi)

    def json(self):
        return {"lower_numerator":str(self.lo), "upper_numerator":str(self.hi)}

    def width(self):
        return F(self.hi-self.lo,SCALE)


ONE = Ball.rational(1)
ZERO = Ball.rational(0)


def log_small(x):
    """Enclose log(x) for an interval contained in [1,2]."""
    assert x.lo >= SCALE and x.hi <= 2*SCALE
    z = (x-ONE)/(x+ONE)
    z2 = z*z
    power = z
    total = ZERO
    for k in range(LOG_TERMS):
        total = total + power.integer_div(2*k+1)
        power = power*z2
    # log(x)=2 sum z^(2k+1)/(2k+1); 0<=z<=1/3.
    tail = F(2, (2*LOG_TERMS+1)*3**(2*LOG_TERMS+1)) / F(8,9)
    return total*Ball.rational(2) + Ball(0,ceildiv(tail.numerator*SCALE,tail.denominator))


def frac_json(x):
    return {"numerator":str(x.numerator), "denominator":str(x.denominator)}


def up(x):
    return str(Context(prec=13,rounding=ROUND_CEILING).divide(
        Decimal(x.numerator),Decimal(x.denominator)))


def scalar_inputs():
    d = log_small(Ball.rational(2))
    log_three_halves = log_small(Ball.rational(3,2))
    log3 = d+log_three_halves
    ell = log3.integer_div(2)
    b = d/ell-ONE
    log_b = log_small(b*Ball.rational(4))-d*Ball.rational(2)
    root2 = Ball.rational(2).sqrt()
    a = d/root2
    t = ell.integer_div(4)
    t2 = t*t
    leading = ONE
    integrals = []
    # Every positive-series ratio is <1/294. The remainder after k=K
    # is at most (1/294)^(K+1)/(1-1/294), before the leading factor.
    tail = F(1,294**(MOMENT_LAST+1))/F(293,294)
    tail_ball = Ball(0,ceildiv(tail.numerator*SCALE,tail.denominator))
    for n in range(257):
        if n:
            leading = (leading*t).integer_div(2*n+1).nonnegative()
        term = total = ONE
        for k in range(MOMENT_LAST):
            term = (term*t2).integer_div(2*(k+1)*(2*n+2*k+3)).nonnegative()
            total = total+term
        integrals.append((leading*(total+tail_ball)).nonnegative())
    ratios = []
    for n in range(2,257):
        e = n%2
        r = Ball.rational(2*n+1,2*e+1).sqrt()*integrals[n]/integrals[e]
        ratios.append(r.nonnegative())
    constants = {"log2":d, "log3":log3, "log_three_halves":log_three_halves,
                 "ell":ell,"split_b":b,"log_b":log_b,"sqrt2":root2,
                 "a":a,"moment_t":t}
    return constants,integrals,ratios,tail


def main():
    constants,integrals,ratios,moment_tail = scalar_inputs()
    m = 768
    log_error = F(1,2**m*(m+1))
    graph_norm = F(51,50)
    reflected_evaluation_norm = graph_norm*257*6**256
    action_error = log_error*(graph_norm+2*reflected_evaluation_norm)
    schur_error = (2+F(250,171)*1023)*action_error
    total_schur_error = F(1,10**19)+schur_error
    exp_lower = sum((F(311,250)**j/factorial(j) for j in range(21)),F(0))
    constant_width = max(x.width() for x in constants.values())
    ratio_width = max(x.width() for x in ratios)
    b = constants["split_b"]
    # Explicit exact rational functional; index k ranges through twice
    # the maximum polynomial degree 1024. Save every moment, not a preview.
    moments = [[F(1,k+1),-F(1,(k+1)**2),F(2,(k+1)**3)] for k in range(2049)]
    checks = {
        "split_lower_via_256_gt_243":256>243,
        "split_upper_via_8_lt_9":8<9,
        "scalar_split_in_one_quarter_one_third":4*b.lo>SCALE and 3*b.hi<SCALE,
        "scalar_moment_t_below_one_seventh":7*constants["moment_t"].hi<SCALE,
        "rational_c0_lower_bound_exp_test":exp_lower>F(121,35),
        "all_scalar_interval_widths_below_1e_minus_600":constant_width<F(1,10**600),
        "all_255_moment_ratio_widths_below_1e_minus_600":ratio_width<F(1,10**600),
        "both_low_moment_integrals_strictly_positive":integrals[0].lo>0 and integrals[1].lo>0,
        "all_moment_ratios_nonnegative":all(x.lo>=0 for x in ratios),
        "log_action_error_below_1e_minus_30":action_error<F(1,10**30),
        "action_comparison_norm_below_510":501+5*graph_norm<510,
        "log_approximated_action_norm_below_511":510+action_error<511,
        "log_schur_error_below_1e_minus_19":schur_error<F(1,10**19),
        "total_schur_error_below_2e_minus_19":total_schur_error<F(2,10**19),
        "conditional_head_reserve_exceeds_9_over_250":F(1,25)-total_schur_error>F(9,250),
        "conditional_full_margin_exceeds_one_thirtieth":F(9,250)/F(26,25)>F(1,30),
        "all_power_log_gram_2_by_2_blocks_positive":all(v[0]*v[2]-v[1]*v[1]>0 for v in moments),
    }
    output = Path(__file__).with_suffix(".json")
    evidence = {
        "scope":"C744l analytic action reduction and scalar inputs; finite Schur matrices NOT evaluated",
        "analytic_and_scalar_checks_pass":all(checks.values()),
        "full_two_sign_margin_certified":False,
        "precision_bits":BITS,"interval_denominator":str(SCALE),
        "log_series_terms":LOG_TERMS,"moment_series_last_index":MOMENT_LAST,
        "log_polynomial_degree":m,"action_polynomial_degree_bound":1024,
        "checks":checks,
        "bounds":{k:frac_json(v) for k,v in {
            "uniform_log_error":log_error,"outside_legendre_evaluation_norm":reflected_evaluation_norm,
            "joint_action_error":action_error,"additional_schur_error":schur_error,
            "total_schur_error":total_schur_error,"exp_311_over_250_lower":exp_lower,
            "maximum_scalar_width":constant_width,"maximum_moment_ratio_width":ratio_width,
            "moment_series_remainder":moment_tail}.items()},
        "constants":{k:v.json() for k,v in constants.items()},
        "moment_integrals_i_n":[v.json() for v in integrals],
        "neutral_moment_ratios_r_n":[{"n":n,"interval":v.json()} for n,v in enumerate(ratios,2)],
        "power_log_moments":[{"k":k,"r0_r1_r2":[frac_json(v) for v in row]}
                             for k,row in enumerate(moments)],
        "failures":[k for k,v in checks.items() if not v],
        "unresolved":["Finite action polynomial coefficients have not been constructed.",
            "No finite head, complete covariance or Schur matrix is enclosed by this script.",
            "Input scalar widths must be propagated through later cancellation-sensitive arithmetic.",
            "C744i/j/k/l remain independently unaudited; remote/non-neutral/odd/global signs remain open."]}
    output.write_text(json.dumps(evidence,indent=2)+"\n")
    print(f"Exact/dyadic checks: {sum(checks.values())}/{len(checks)}")
    print(f"Joint log action error <= {up(action_error)}; required < 1e-30")
    print(f"Additional Schur error <= {up(schur_error)}; required < 1e-19")
    print(f"Max scalar width <= {up(constant_width)}; required < 1e-600")
    print(f"Max moment-ratio width <= {up(ratio_width)}; required < 1e-600")
    print(f"Failures: {evidence['failures']}")
    print("Finite Schur signs: NOT ESTABLISHED; required both >= 1/25")
    print(f"Full certificate: {output}")
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

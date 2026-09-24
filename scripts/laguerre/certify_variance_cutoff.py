"""Certify V_64 < 1/200 under L037's arithmetic contracts.

The moment tails through degree 130 and the resulting compact-height
reduction are proved in L310. This does not certify the lower levels or RH.
"""

import argparse
import json
from fractions import Fraction
from math import comb
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "hankel"))
from certify_hankel import (  # noqa: E402
    I, ORDER, PRECISION, moment_jet, pi_bounds, self_check, theta_kernel_jet,
)

LEVEL = 64
MAX_DEGREE = 2 * LEVEL + 2


def tail_bounds():
    # Common upper bounds for every even half-line moment through degree 130.
    spatial = I.rational(Fraction(512 * 2**130, 461)) * I(-141).exp()
    theta = 1280 * I(-75).exp() + 180 * I(-520).exp()
    return spatial, theta


def certify(panels):
    if panels < 1 or panels & (panels - 1):
        raise ValueError("Panel count must be a positive power of two")
    pi = pi_bounds()
    h = I.rational(Fraction(1, panels))
    totals = {degree: I(0) for degree in range(0, MAX_DEGREE + 1, 2)}
    errors = {degree: I(0) for degree in totals}
    integral_weights = {j: 2 * h**(j + 1) / (j + 1) for j in (0, 2, 4, 6)}
    remainder_weight = 2 * h**9 / 9
    for panel in range(panels):
        center = I.rational(Fraction(2 * panel + 1, panels))
        domain = I(I.rational(Fraction(2 * panel, panels)).lo,
                   I.rational(Fraction(2 * panel + 2, panels)).hi)
        midpoint_kernel = theta_kernel_jet(center, pi)
        domain_kernel = theta_kernel_jet(domain, pi)
        for degree in totals:
            coefficients = moment_jet(center, degree, midpoint_kernel)
            bound = moment_jet(domain, degree, domain_kernel)[8].magnitude()
            integral = sum((coefficients[j] * weight
                            for j, weight in integral_weights.items()), I(0))
            error = I(bound) * remainder_weight
            totals[degree] = totals[degree] + integral + I(error.hi.copy_negate(), error.hi)
            errors[degree] = errors[degree] + error

    spatial_tail, theta_tail = tail_bounds()
    common_tail = spatial_tail + theta_tail
    moments = {degree: total + I(0, common_tail.hi)
               for degree, total in totals.items()}
    if any(value.lo <= 0 for value in moments.values()):
        raise ArithmeticError("A moment enclosure is not strictly positive")

    # These are half-line moments: their common factor two cancels in V_64.
    z = sum((comb(2 * LEVEL, j) * moments[j] * moments[2 * LEVEL - j]
             for j in range(0, 2 * LEVEL + 1, 2)), I(0))
    p = sum((comb(2 * LEVEL, j) * moments[j + 2] * moments[2 * LEVEL - j]
             for j in range(0, 2 * LEVEL + 1, 2)), I(0))
    q = sum((comb(2 * LEVEL, j) * moments[j + 1] * moments[2 * LEVEL - j + 1]
             for j in range(1, 2 * LEVEL, 2)), I(0))
    variance = (p - q) / (2 * z)
    # Exact rational endpoint comparisons; no rounded decimal is a premise.
    if not (Fraction(411, 100000) < Fraction(variance.lo)
            <= Fraction(variance.hi) < Fraction(413, 100000)
            < Fraction(1, 200)):
        raise ArithmeticError("Variance enclosure missed the stated threshold")
    margin = 1 - 200 * variance
    return {
        "scope": "V_64 cutoff for n >= 64 and |a| <= 10; lower levels unresolved; not RH",
        "arithmetic_contract": "L037",
        "precision": PRECISION,
        "panels": panels,
        "taylor_order": ORDER,
        "theta_terms": 4,
        "u_cutoff": 2,
        "maximum_moment_degree": MAX_DEGREE,
        "pi": pi.data(),
        "spatial_tail_bound": spatial_tail.data(),
        "omitted_theta_tail_bound": theta_tail.data(),
        "common_tail_bound": common_tail.data(),
        "quadrature_error_bounds": {str(k): value.data() for k, value in errors.items()},
        "half_line_moments": {str(k): value.data() for k, value in moments.items()},
        "half_line_Z_64": z.data(),
        "half_line_P_64": p.data(),
        "half_line_Q_64": q.data(),
        "V_64": variance.data(),
        "variance_rational_bounds": ["411/100000", "413/100000"],
        "required_variance_upper_bound": "1/200",
        "quadratic_margin_at_height_10": margin.data(),
        "variance_threshold_certified": True,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panels", type=int, default=256)
    args = parser.parse_args()
    self_check()
    print(json.dumps(certify(args.panels), indent=2))

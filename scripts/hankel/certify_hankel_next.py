"""Validated H_2 certificate; extends, and does not alter, the H_1 procedure."""

import argparse
import json
from fractions import Fraction
from math import factorial

from certify_hankel import (
    I, PRECISION, ORDER, pi_bounds, theta_kernel_jet, moment_jet, self_check,
)


def higher_tail(max_k):
    p = max_k // 2 + 2
    coefficient = sum((Fraction(factorial(p), factorial(p-j)) *
                       Fraction(50**(p-j), 3**(j+1)) for j in range(p+1)), Fraction(0))
    return 128 * I(-150).exp() * I.rational(coefficient) + 80000 * factorial(p) * I(-74).exp()


def moment_enclosures(panels, max_k=12):
    if panels < 1 or panels & (panels-1):
        raise ValueError("Panel count must be a positive power of two")
    pi = pi_bounds()
    h = I.rational(Fraction(1, panels))
    totals = {k: I(0) for k in range(0, max_k+1, 2)}
    errors = {k: I(0) for k in totals}
    for panel in range(panels):
        center = I.rational(Fraction(2*panel+1, panels))
        domain = I(I.rational(Fraction(2*panel, panels)).lo,
                   I.rational(Fraction(2*panel+2, panels)).hi)
        midpoint_kernel = theta_kernel_jet(center, pi)
        domain_kernel = theta_kernel_jet(domain, pi)
        for k in totals:
            coefficients = moment_jet(center, k, midpoint_kernel)
            bound = moment_jet(domain, k, domain_kernel)[8].magnitude()
            integral = sum((2 * coefficients[j] * h**(j+1) / (j+1)
                            for j in (0, 2, 4, 6)), I(0))
            error = 2 * I(bound) * h**9 / 9
            totals[k] = totals[k] + integral + I(error.hi.copy_negate(), error.hi)
            errors[k] = errors[k] + error
    tail = higher_tail(max_k)
    moments = {k: total + I(0, tail.hi) for k, total in totals.items()}
    if any(value.lo <= 0 for value in moments.values()):
        raise ArithmeticError("A moment enclosure is not strictly positive")
    return moments, errors, tail


def newton_sums(moments, max_power):
    e = {j: moments[2*j] / (factorial(2*j)*moments[0])
         for j in range(1, max_power+1)}
    sums = {}
    for k in range(1, max_power+1):
        sums[k] = sum(((-1)**(j-1) * e[j] * sums[k-j] for j in range(1, k)), I(0))
        sums[k] = sums[k] + (-1)**(k-1) * k * e[k]
    return sums


def certify(panels):
    moments, errors, tail = moment_enclosures(panels)
    sums = newton_sums(moments, 6)
    s2, s3, s4, s5, s6 = (sums[k] for k in range(2, 7))
    d1 = s2*s4 - s3**2
    d2 = s2*s4*s6 + 2*s3*s4*s5 - s2*s5**2 - s6*s3**2 - s4**3
    return {
        "scope": "finite H_2 positive definiteness only; not RH",
        "precision": PRECISION, "panels": panels, "taylor_order": ORDER,
        "theta_terms": 4, "u_cutoff": 2, "common_tail_bound": tail.data(),
        "quadrature_error_bounds": {str(k): value.data() for k, value in errors.items()},
        "moments": {str(k): value.data() for k, value in moments.items()},
        "power_sums": {str(k): value.data() for k, value in sums.items()},
        "leading_principal_minors": [value.data() for value in (s2, d1, d2)],
        "finite_sign_certified": all(value.lo > 0 for value in (s2, d1, d2)),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panels", type=int, default=128)
    args = parser.parse_args()
    self_check()
    print(json.dumps(certify(args.panels), indent=2))

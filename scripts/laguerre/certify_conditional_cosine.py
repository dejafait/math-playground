"""Enclose a negative conditional cosine derivative under L037's contracts.

The analytical tails and differentiation argument are recorded in L312.
This tests conditional ordering at s=1/5, a=16, not any Laguerre sign or RH.
"""

import argparse
import json
from fractions import Fraction
from math import factorial
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "hankel"))
from certify_hankel import (  # noqa: E402
    I, ORDER, PRECISION, add, constant, exponential, multiply, pi_bounds,
    scale, self_check,
)

S = Fraction(1, 5)
A = 16
TRIG_DEGREE = 49


def sin_cos(x, pi):
    # Any integer reduction is exact; the radius assertion checks its utility.
    turns = (Fraction(x.lo) / (2 * Fraction(pi.lo)) + Fraction(1, 2)) // 1
    reduced = x - 2 * turns * pi
    radius = I(reduced.magnitude())
    if radius.hi > 4:
        raise ArithmeticError("Trigonometric reduction radius exceeds four")
    square = reduced * reduced
    sine, cosine = I(0), I(0)
    for j in range(24, -1, -1):
        sine = sine * square + I.rational(Fraction((-1)**j, factorial(2*j + 1)))
        cosine = cosine * square + I.rational(Fraction((-1)**j, factorial(2*j)))
    sine = sine * reduced
    # Degree-49 Taylor polynomials (cosine's odd coefficient is zero).
    remainder = radius**50 / factorial(50)
    enlargement = I(remainder.hi.copy_negate(), remainder.hi)
    return sine + enlargement, cosine + enlargement


def cosine_jet(t, pi):
    sine, cosine = sin_cos(2 * A * t, pi)
    cycle = (cosine, -sine, -cosine, sine)
    return [cycle[j % 4] * I.rational(Fraction((2*A)**j, factorial(j)))
            for j in range(ORDER + 1)]


def kernel_jets(u, slope, pi):
    # Taylor coefficients in t; u is an affine function with slope +/-1.
    ujet = constant(u)
    ujet[1] = I(slope)
    e2u = exponential(scale(ujet, 2))
    ehalf = exponential(scale(ujet, I.rational(Fraction(1, 2))))
    kernel, derivative = constant(0), constant(0)
    for m in range(1, 5):
        v = scale(e2u, pi * m*m)
        v2 = multiply(v, v)
        v3 = multiply(v2, v)
        damping = exponential(scale(v, -1))
        p = add(scale(v2, 8), scale(v, -12))
        dp = add(add(scale(v3, -16), scale(v2, 60)), scale(v, -30))
        kernel = add(kernel, multiply(p, damping))
        derivative = add(derivative, multiply(dp, damping))
    return multiply(ehalf, kernel), multiply(ehalf, derivative)


def integrand_jets(t, side, pi):
    s = I.rational(S)
    plus, dplus = kernel_jets(s + t, 1, pi)
    if side == "left":
        minus, dminus = kernel_jets(s - t, -1, pi)
        sign = 1
    else:
        minus, dminus = kernel_jets(t - s, 1, pi)
        sign = -1
    q = multiply(plus, minus)
    dsq = add(multiply(dplus, minus), scale(multiply(plus, dminus), sign))
    cos = cosine_jet(t, pi)
    return {"Z": q, "N": multiply(q, cos),
            "Z_s": dsq, "N_s": multiply(dsq, cos)}


def tail_bounds():
    kernel_error = 160000 * I(-75).exp()
    derivative_error = 80000000 * I(-75).exp()
    # Integrals over [0,2]; K and its finite head are <16, derivatives <5120.
    theta_mass = 64 * kernel_error
    theta_derivative = 64 * derivative_error + 20480 * kernel_error
    spatial_mass = 65536 * I(-282).exp() / 591
    spatial_derivative = 2621440 * I(-277).exp() / 589
    return {
        "kernel_pointwise_error": kernel_error,
        "derivative_pointwise_error": derivative_error,
        "theta_mass_error": theta_mass,
        "theta_derivative_error": theta_derivative,
        "spatial_mass_error": spatial_mass,
        "spatial_derivative_error": spatial_derivative,
    }


def certify(panels):
    if panels < 1:
        raise ValueError("Positive panel count required")
    pi = pi_bounds()
    totals = {name: I(0) for name in ("Z", "N", "Z_s", "N_s")}
    errors = {name: I(0) for name in totals}
    # Two smooth pieces; no finite reflected kernel is differentiated at its cusp.
    for left, right, side in ((Fraction(0), S, "left"), (S, Fraction(2), "right")):
        width = (right - left) / panels
        h = I.rational(width / 2)
        weights = {j: 2 * h**(j + 1) / (j + 1) for j in (0, 2, 4, 6)}
        remainder_weight = 2 * h**9 / 9
        for panel in range(panels):
            low, high = left + panel * width, left + (panel + 1) * width
            center = I.rational((low + high) / 2)
            domain = I(I.rational(low).lo, I.rational(high).hi)
            midpoint_jets = integrand_jets(center, side, pi)
            domain_jets = integrand_jets(domain, side, pi)
            for name in totals:
                value = sum((midpoint_jets[name][j] * w for j, w in weights.items()), I(0))
                error = I(domain_jets[name][8].magnitude()) * remainder_weight
                totals[name] = totals[name] + value + I(error.hi.copy_negate(), error.hi)
                errors[name] = errors[name] + error
    tails = tail_bounds()
    full = {}
    for name, value in totals.items():
        suffix = "derivative" if name.endswith("_s") else "mass"
        radius = tails[f"theta_{suffix}_error"] + tails[f"spatial_{suffix}_error"]
        full[name] = value + I(radius.hi.copy_negate(), radius.hi)
    z, n, zs, ns = (full[name] for name in ("Z", "N", "Z_s", "N_s"))
    if z.lo <= 0:
        raise ArithmeticError("Mass denominator not positive")
    numerator = ns*z - n*zs
    derivative = numerator / (z*z)
    bounds = [Fraction(-23, 10**6), Fraction(-21, 10**6)]
    if not bounds[0] < Fraction(derivative.lo) <= Fraction(derivative.hi) < bounds[1]:
        raise ArithmeticError(f"Derivative enclosure missed target: {derivative.data()}")
    return {
        "scope": "negative conditional cosine derivative only; no Laguerre sign or RH claim",
        "arithmetic_contract": "L037",
        "precision": PRECISION,
        "s": str(S), "a": A,
        "t_cutoff": 2, "theta_terms": 4,
        "panels_per_piece": panels, "pieces": ["[0,1/5]", "[1/5,2]"],
        "taylor_order": ORDER, "trigonometric_taylor_degree": TRIG_DEGREE,
        "pi": pi.data(),
        "tail_bounds": {name: value.data() for name, value in tails.items()},
        "quadrature_error_bounds": {name: value.data() for name, value in errors.items()},
        "half_line_integrals": {name: value.data() for name, value in full.items()},
        "conditional_cosine": (n/z).data(),
        "derivative_numerator": numerator.data(),
        "conditional_cosine_derivative": derivative.data(),
        "derivative_rational_bounds": [str(value) for value in bounds],
        "negative_derivative_certified": True,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panels", type=int, default=128)
    args = parser.parse_args()
    self_check()
    print(json.dumps(certify(args.panels), indent=2))

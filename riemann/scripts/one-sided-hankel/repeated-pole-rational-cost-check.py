#!/usr/bin/env python3
"""Exact constants for the step-56 full-product complementary-ray bound.

This is an arithmetic certificate. The analytic product estimate, rational
change of variable, continuum signs, and asymptotic conclusion require the
separate proof; this script does not audit them.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def record(value):
    value = F(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def ceil_fraction(value):
    return -((-value.numerator) // value.denominator)


def main():
    U, d, y0 = F(121, 64), F(5, 4), F(9, 20)
    delta = U - d*d
    kup, alo, aup = F(29, 20), F(53, 40), F(133, 100)
    bins, scale = 200, 10**8
    rows, checks = [], []

    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})

    check("Delta equals 21/64", delta == F(21, 64))
    check("K upper square margin positive", kup*kup > d*d + delta*delta/(y0*y0))
    check("radius lower square margin positive", alo*alo < d*d + y0*y0)
    check("radius upper square margin positive", aup*aup > d*d + y0*y0)
    check("g decreasing on [0,1]", kup > 1)
    check("all denominator lower bounds positive", U > d and alo > 1)
    lower_total, upper_total = 0, 0
    for i in range(1, bins+1):
        lo, hi = F(i-1, bins), F(i, bins)
        g = U + hi*hi - 2*kup*hi
        row = {"i": i, "lo": record(lo), "hi": record(hi), "g_hi": record(g)}
        if g >= 0:
            exact = y0*y0*(U-hi*hi)*g / ((U+d*hi)**2*(aup+hi)**2)
            units = (scale*exact).numerator // (scale*exact).denominator
            bound = F(units, scale)
            valid = F(0) <= bound <= exact < 1
            lower_total += units
            row.update(kind="contraction", exact=record(exact), units=units,
                       bound=record(bound), rounding_valid=valid)
        else:
            exact = delta*(U-lo*lo)*(-g) / ((U-d*hi)**2*(alo-hi)**2)
            units = ceil_fraction(scale*exact)
            bound = F(units, scale)
            valid = 0 < exact <= bound
            upper_total += units
            row.update(kind="excess", exact=record(exact), units=units,
                       bound=record(bound), rounding_valid=valid)
        rows.append(row)
    check("all interval constants and roundings valid", all(r["rounding_valid"] for r in rows))
    gamma = F(lower_total-upper_total, 2*bins*scale)
    constant = F(lower_total+upper_total, 2*scale)
    required = F(1, 100)
    check("full-product exponent exceeds required 1/100", gamma > required)
    failures = [c["name"] for c in checks if not c["passed"]]
    result = {
        "scope": "Exact arithmetic only; full analytic proof and separate critical audit remain necessary.",
        "parameters": {"bins": bins, "scale": scale, "U": record(U), "d": record(d),
                       "y0": record(y0), "Delta": record(delta), "K_upper": record(kup),
                       "radius_lower": record(alo), "radius_upper": record(aup)},
        "square_margins": {"K_upper": record(kup*kup-d*d-delta*delta/(y0*y0)),
                           "radius_lower": record(d*d+y0*y0-alo*alo),
                           "radius_upper": record(aup*aup-d*d-y0*y0)},
        "rows": rows,
        "aggregate": {"contraction_units": lower_total, "excess_units": upper_total,
                      "gamma": record(gamma), "required_gamma": record(required),
                      "margin": record(gamma-required), "B": record(constant),
                      "pointwise_bound": "|W_(-d+iy)(u)| <= exp(B-gamma*n), |y|>=y0, |u|=1"},
        "checks": checks, "failures": failures,
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Exact checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}")
    print(f"Actual gamma: {gamma} ({float(gamma):.12f}); required: {required}")
    print(f"Margin: {gamma-required}; constant B: {constant}")
    print(f"Certificate: {output.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

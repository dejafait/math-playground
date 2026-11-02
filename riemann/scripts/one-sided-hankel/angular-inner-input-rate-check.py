#!/usr/bin/env python3
"""Exact rational checks for C645n; no numerical norm claim."""

from fractions import Fraction as F
from pathlib import Path
import json


def encoded(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def log_interval(value, terms=16):
    """For rational value > 1, bound log(value) by its artanh series."""
    assert value > 1
    u = (value - 1) / (value + 1)
    lower = 2 * sum((u ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), F(0))
    tail = 2 * u ** (2 * terms + 1) / ((2 * terms + 1) * (1 - u * u))
    return lower, lower + tail, {
        "argument": encoded(value), "u": encoded(u), "terms": terms,
        "lower": encoded(lower), "upper": encoded(lower + tail),
        "tail_upper": encoded(tail),
    }


def main():
    d, R, eta = F(5, 4), F(11, 8), F(1, 100)
    U = R * R
    lo0, hi0, log0 = log_interval(F(11, 10))
    lo1, hi1, log1 = log_interval(F(201, 121))
    lo2, hi2, log2 = log_interval(F(9, 5))
    scale = 10 ** 12
    readable_bounds = []
    for lo, hi, record in [(lo0, hi0, log0), (lo1, hi1, log1), (lo2, hi2, log2)]:
        lower_numerator = (lo.numerator * scale) // lo.denominator
        upper_numerator = -((-hi.numerator * scale) // hi.denominator)
        assert F(lower_numerator, scale) <= lo <= hi <= F(upper_numerator, scale)
        readable_bounds.append({
            "argument": record["argument"],
            "lower_numerator": lower_numerator,
            "upper_numerator": upper_numerator,
            "denominator": scale,
        })
    lower = lo0 + F(201, 80) * lo1 - F(9, 4) * hi2
    upper = hi0 + F(201, 80) * hi1 - F(9, 4) * lo2
    threshold = F(1, 32)
    rho = (R - eta) / R
    checks = {
        "lambda_exceeds_47_over_1000": lower > F(47, 1000),
        "lambda_below_49_over_1000": upper < F(49, 1000),
        "lambda_strictly_above_required_1_over_32": lower > threshold,
        "finite_grid_endpoint_factor": d * (U + d) / (U * (d + 1)) == F(335, 363),
        "clearance_rho": rho == F(273, 275),
        "clearance_squared_gap": 1 - rho * rho == F(1096, 75625),
        "strict_radial_order": 1 < d < R and U > d * d,
    }
    result = {
        "kind": "exact_rational_rate_certificate",
        "claim": "Rate of the full inner-function test, not an upper bound on the Hankel operator norm",
        "parameters": {"d": encoded(d), "R": encoded(R), "eta": encoded(eta)},
        "log_series_inputs": [log0, log1, log2],
        "readable_log_bounds": readable_bounds,
        "lambda": {
            "formula": "log(11/10)+(201/80)*log(201/121)-(9/4)*log(9/5)",
            "lower": encoded(lower), "upper": encoded(upper),
            "decimal_preview": [float(lower), float(upper)],
        },
        "required_rate": encoded(threshold),
        "positive_margin_lower": encoded(lower - threshold),
        "finite_grid_factor": encoded(F(335, 363)),
        "clearance_rho": encoded(rho),
        "clearance_squared_gap": encoded(1 - rho * rho),
        "checks": checks,
        "failures": [key for key, value in checks.items() if not value],
        "limits": [
            "No finite angular sampling is used.",
            "The analytic proof, not this arithmetic certificate alone, establishes the uniform angular bounds.",
            "An upper bound on this particular input response does not upper-bound the largest Hankel norm.",
            "The target at exponent 1/32 and all Xi realization/sign claims remain unresolved.",
        ],
    }
    path = Path(__file__).with_name("angular-inner-input-rate-check.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print("All exact checks passed:" if not result["failures"] else "FAILED:", not result["failures"])
    print(f"Actual rate in [47/1000, 49/1000]: {float(lower):.12f} (decimal preview)")
    print("Required rate: 1/32 = 0.03125; actual-minus-required > 63/4000 = 0.01575")
    print("Failures:", result["failures"])
    print("Full certificate:", path)
    if result["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

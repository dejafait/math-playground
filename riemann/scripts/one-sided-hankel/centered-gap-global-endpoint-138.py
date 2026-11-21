#!/usr/bin/env python3
"""Exact constants for L702; not a finite-profile or asymptotic screen."""

import json
from fractions import Fraction as F
from pathlib import Path


def rational(value):
    return str(value.numerator) + "/" + str(value.denominator)


def log_bounds(value, terms=12):
    # log(value) = 2 sum_{k>=0} z^(2k+1)/(2k+1), 0<z<1.
    z = (value - 1) / (value + 1)
    assert 0 < z < 1
    lower = 2 * sum((z ** (2 * k + 1) / (2 * k + 1)
                     for k in range(terms)), F(0))
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + tail, {
        "argument": rational(value), "z": rational(z), "terms": terms,
        "lower": rational(lower), "upper": rational(lower + tail),
        "tail_upper": rational(tail), "strict": True,
    }


def main():
    d, U, A, Y = F(5, 4), F(121, 64), F(27, 10), F(9, 20)
    l5, u5, cert5 = log_bounds(F(5))
    lr, ur, certr = log_bounds(F(121, 41))
    omega_lo = A * (l5 - F(4, 5) + F(121, 100) * lr)
    omega_hi = A * (u5 - F(4, 5) + F(121, 100) * ur)
    beta_minus_alpha = (U - 2 * d + 1) / (d * U)
    square_gap = beta_minus_alpha * F(4, 5)
    square_denom = 1 + 16 * Y * Y
    factor_loss = square_gap * F(2, 5) ** 2 / square_denom
    rate = factor_loss / 2
    derivative = A * (4 + F(64, 41))
    endpoint_lower = Y - F(9, 8) * A / 63
    checks = []

    def check(name, actual, relation, required):
        passed = {">": actual > required, "<": actual < required,
                  ">=": actual >= required, "==": actual == required}[relation]
        checks.append({"name": name, "actual": rational(actual),
                       "relation": relation, "required": rational(required),
                       "passed": passed})

    check("frequency_lower", omega_lo, ">", F(11, 2))
    check("frequency_upper", omega_hi, "<", F(6))
    check("seven_pi_over_four_upper_uses_pi_lt_22_over_7",
          F(7, 4) * F(22, 7), "==", F(11, 2))
    check("two_pi_lower_uses_pi_gt_3", 2 * F(3), "==", F(6))
    check("positive_factor_numerator", U - 2 * d + 1, "==", F(25, 64))
    check("beta_minus_alpha_lower", beta_minus_alpha, "==", F(20, 121))
    check("beta_square_minus_alpha_square_lower", square_gap, "==", F(16, 121))
    check("factor_square_denominator_upper", square_denom, "==", F(106, 25))
    check("factor_square_loss", factor_loss, "==", F(32, 6413))
    check("product_decay_rate", rate, "==", F(16, 6413))
    check("uniform_real_kernel_derivative_upper", derivative, "<", F(16))
    check("actual_outer_endpoint_at_n_63", endpoint_lower, ">", F(2, 5))
    failures = [c["name"] for c in checks if not c["passed"]]
    result = {
        "step": 138,
        "scope": "Exact constants only; analytic limits and profile selection are proved in L702.",
        "log_bounds": {"log_5": cert5, "log_121_over_41": certr},
        "omega_bounds": {"lower": rational(omega_lo), "upper": rational(omega_hi),
                         "required_lower": "11/2", "required_upper": "6/1"},
        "checks": checks, "failures": failures, "passed": not failures,
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Exact checks: {len(checks) - len(failures)}/{len(checks)} passed; failures={failures}")
    print(f"Omega: ({float(omega_lo):.12f}, {float(omega_hi):.12f}); required (5.5, 6)")
    print(f"Outer-band decay rate: {rate} > 0; derivative bound {derivative} < 16")
    print(f"Endpoint at n=63: {endpoint_lower} > 2/5")
    print(f"Certificate: {output.as_posix()}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

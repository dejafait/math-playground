"""Exact constants for L704; this does not verify its analytic proof."""

from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


def exp_lower(x, degree):
    return sum((x**k / factorial(k) for k in range(degree + 1)), Q(0))


def exact(value):
    return f"{value.numerator}/{value.denominator}"


def main():
    r, s = Q(1, 2), Q(1, 10000)
    d, R, U, A, Y = Q(5, 4), Q(11, 8), Q(121, 64), Q(27, 10), Q(9, 20)
    tau = r * U / d
    kappa = (r - s) / (r + s)
    boundary_coefficient = Q(1, 2) + Q(3, 5) + Q(18, 25) * Q(9, 10)
    D_lower = (U / d) * s * Q(17, 2)
    gamma = (D_lower - (1 - kappa) * (tau + Q(7, 4))) / kappa
    required_charge = Q(1, 4000)
    checks = []

    def check(name, actual, relation, required):
        passed = {"<": actual < required, ">": actual > required,
                  "=": actual == required}[relation]
        checks.append({"name": name, "actual": exact(actual),
                       "relation": relation, "required": exact(required),
                       "passed": passed})

    check("contour_spatial_radius_squared", (d + Q(1, 100))**2 + Y**2, "<", U)
    check("low_frequency_log_argument", 1 + d / (U * s), "<", Q(10000))
    check("exp10_lower_from_exp1_gt_8_over_3", Q(8, 3)**10, ">", Q(10000))
    check("omega_upper_after_log_argument_lt_10", A * U * s * 10 / d**2, "<", Q(1, 2))
    check("exp_half_lower", exp_lower(Q(1, 2), 3), ">", Q(8, 5))
    check("exp_three_fifths_lower", exp_lower(Q(3, 5), 2), ">", Q(43, 25))
    check("exp_nine_tenths_lower", exp_lower(Q(9, 10), 3), ">", Q(43, 18))
    check("boundary_coefficient", boundary_coefficient, "<", Q(7, 4))
    check("exp1_geometric_tail_upper", Q(8, 3) + Q(5, 96), "<", Q(11, 4))
    check("exp8_upper_implies_log5000_gt_8", Q(11, 4)**8, "<", Q(5000))
    check("D_lower", D_lower, "=", Q(2057, 1600000))
    check("kappa", kappa, "=", Q(4999, 5001))
    check("pole_charge_coefficient", tau, "=", Q(121, 160))
    check("partial_charge_margin", gamma, ">", required_charge)
    check("permitted_deficit_coefficient", tau - required_charge, "=", Q(189, 250))
    check("paid_fraction_of_pole_coefficient", required_charge / tau, "=", Q(1, 3025))

    failures = [row["name"] for row in checks if not row["passed"]]
    certificate = {
        "scope": "Exact rational inequalities only; analytic proof and profile remain unaudited.",
        "constants": {
            "radius": exact(r), "positive_point": exact(s),
            "kappa": exact(kappa), "boundary_coefficient_upper": exact(Q(7, 4)),
            "D_lower": exact(D_lower), "gamma": exact(gamma),
            "required_partial_charge": exact(required_charge),
            "gamma_margin": exact(gamma - required_charge),
            "full_target_pole_coefficient": exact(tau),
        },
        "checks": checks,
        "failures": failures,
        "limitations": [
            "No effective n onset or numerical Picard profile is certified.",
            "No contour, Fourier, integrability or Poisson-Jensen proof is verified by this script.",
            "The positive partial charge does not establish the required o(n) deficit.",
        ],
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(f"Exact checks: {len(checks) - len(failures)}/{len(checks)}; failures: {failures}")
    print(f"Charge coefficient: {exact(gamma)} (~{float(gamma):.10f}); required partial: {exact(required_charge)}")
    print(f"Full target pole coefficient: {exact(tau)}; o(n) deficit remains unproved.")
    print(f"Certificate: {output.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

"""Exact scalar checks supporting C997d; no range or analytic audit."""
from fractions import Fraction as Q
from pathlib import Path
import json

theta_upper = Q(1, 96)  # Strict bound proved analytically in C997d.
values = {
    "upper_conversion_rate_floor": (2 / theta_upper - 9) / 32,
    "full_conversion_rate_floor": (5 / theta_upper - 9) / 32,
    "propagated_noise_exponent_floor": (2 - 11 * theta_upper) / 32,
}
expected = {
    "upper_conversion_rate_floor": Q(183, 32),
    "full_conversion_rate_floor": Q(471, 32),
    "propagated_noise_exponent_floor": Q(181, 3072),
}
checks = {
    name: {
        "exact_value": str(value),
        "expected_value": str(expected[name]),
        "positive": value > 0,
        "pass": value == expected[name] and value > 0,
    }
    for name, value in values.items()
}
failures = [name for name, result in checks.items() if not result["pass"]]
certificate = {
    "step_id": "2026-11-10-one-sided-paid-hardy-point-test-325",
    "scope": "Rational endpoint arithmetic only; theta bound and analytic hypotheses are proved in C997d, not by this script.",
    "assumptions": ["0 < theta < 1/96", "kappa > 0"],
    "required_amplification_rate": "0 (subexponential for every epsilon > 0)",
    "actual_bounds": {name: "> " + str(value) for name, value in values.items()},
    "checks": checks,
    "failures": failures,
    "limitations": "No admissible extremizer, actual-range lower bound, asymptotic calculation or independent analytic audit.",
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Checks: {len(checks) - len(failures)}/{len(checks)} passed; failures: {failures}")
print("Required amplification rate: 0; actual scalar certificate bounds:")
for name, bound in certificate["actual_bounds"].items():
    print(f"  {name}: {bound}")
print(f"Certificate: {destination.relative_to(Path.cwd())}")
if failures:
    raise SystemExit(1)

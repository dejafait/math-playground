"""Exact scalar checks only; does not evaluate the growing coherent square."""

from fractions import Fraction
from pathlib import Path
import json


def rational(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


a, b = Fraction(19, 100), Fraction(221, 100)
q_upper = Fraction(11, 20)
error_upper = Fraction(5, 2) * q_upper**16
relative_upper = b * error_upper
relative_required = Fraction(1, 2500)
surrogate_deficit = Fraction(1, 1000)
square_deficit = 1 - (1 - surrogate_deficit) / (1 - relative_required)
checks = {
    "q_upper_via_squared_endpoint_ratio": b / a < ((1 + q_upper) / (1 - q_upper))**2,
    "error_prefactor": (b - a) / (2 * a * b) < Fraction(5, 2),
    "relative_error_below_required": relative_upper < relative_required,
    "conditional_square_deficit": square_deficit == Fraction(1, 1666),
    "conditional_deficit_exceeds_three_over_5000": square_deficit > Fraction(3, 5000),
}
certificate = {
    "scope": "Exact rational bounds used in L932; no matrix or coherent-defect verification.",
    "spectral_enclosure": {"a": rational(a), "b": rational(b), "status": "Analytic eventual enclosure in L932, not checked by this program."},
    "degree": 16,
    "q_upper": rational(q_upper),
    "scalar_error_upper": rational(error_upper),
    "relative_error": {"actual_upper": rational(relative_upper), "required_upper": rational(relative_required)},
    "conditional_thresholds": {"required_surrogate_deficit": rational(surrogate_deficit), "resulting_square_deficit": rational(square_deficit)},
    "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
    "coherent_deficit": {"established": False, "reason": "The full four-term endpoint quadratic form has not been bounded below the required metric."},
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Scalar error upper: {float(error_upper):.12g}")
print(f"Relative square error upper: {float(relative_upper):.12g}; required < {float(relative_required):.12g}")
print(f"Required surrogate deficit: {float(surrogate_deficit):.12g}; established: False")
print(f"Exact checks: {sum(checks.values())}/{len(checks)}; failures: {certificate['failures']}")
print(f"Certificate: {output.relative_to(Path.cwd())}")
if certificate["failures"]:
    raise SystemExit(1)

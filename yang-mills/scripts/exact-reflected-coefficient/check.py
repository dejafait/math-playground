"""Reuse L011's exact moment-division check of L279's connected algebra.

This does not evaluate any four-dimensional Wilson-box coefficient.
"""

from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "combined-ward-response" / "check.py"
captured = StringIO()
with redirect_stdout(captured):
    data = runpy.run_path(str(SOURCE))


def polynomial(poly):
    return [{"powers": list(powers), "coefficient": str(coefficient)}
            for powers, coefficient in sorted(poly.items())]


direct = data["direct"]
combined = data["combined"]
without_cubic = data["coefficient"](
    data["left"], data["right"], data["ZERO"], data["quartic"], data["haar"])
without_haar = data["coefficient"](
    data["left"], data["right"], data["cubic"], data["quartic"], data["ZERO"])
checks = {
    "leading_covariance": direct[0] == data["cumulant"](data["left"][0], data["right"][0]),
    "odd_coefficient_zero": direct[1] == 0,
    "second_coefficient_agrees": direct[2] == combined,
    "cubic_terms_detected": combined != without_cubic,
    "haar_term_detected": combined != without_haar,
}
certificate = {
    "scope": "Exact rational generic Gaussian algebra only; no box evaluation or mesh bound.",
    "source": str(SOURCE.relative_to(HERE.parent.parent)),
    "source_sha256": sha256(SOURCE.read_bytes()).hexdigest(),
    "gaussian": "Three independent centered real normal variables of variance one.",
    "inputs": {
        "minus_jets": [polynomial(p) for p in data["left"]],
        "plus_jets": [polynomial(p) for p in data["right"]],
        "S3": polynomial(data["cubic"]),
        "S4": polynomial(data["quartic"]),
        "M2": polynomial(data["haar"]),
    },
    "comparison": {
        "normalized_covariance_series": list(map(str, direct)),
        "connected_second_coefficient": str(combined),
        "actual_difference": str(direct[2] - combined),
        "required_difference": "0",
        "without_cubic": str(without_cubic),
        "without_haar": str(without_haar),
    },
    "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
    "source_check_output": captured.getvalue(),
}
destination = HERE / "cumulant-certificate.json"
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Coefficient: normalized={direct[2]}, connected={combined}.")
print(f"Difference: actual={direct[2] - combined}, required=0; failures={certificate['failures']}.")
print(f"Certificate: {destination.relative_to(HERE.parent.parent)}")
if not all(checks.values()):
    raise SystemExit(1)

"""Exact finite arithmetic only; the analytic argument is in L951."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


checks = []
for a, threshold in [(F(13, 8), F(25, 128)), (F(2), F(1, 8))]:
    terms = [(-a) ** k / F(factorial(k)) for k in range(8)]
    lower = sum(terms, F(0))
    checks.append({
        "a": str(a), "taylor_degree": 7,
        "terms": [str(term) for term in terms],
        "polynomial_lower": str(lower), "required_lower": str(threshold),
        "gap": str(lower - threshold), "positive_gap": lower > threshold,
    })
checks += [
    {"name": "lower_r_square", "actual": str(F(13, 16) ** 2),
     "required_upper": str(F(2, 3)), "passes": F(13, 16) ** 2 < F(2, 3)},
    {"name": "upper_r_negative_case_constant", "actual": str(F(1, 8) / 16),
     "required_lower": str(F(1, 512)), "passes": F(1, 8) / 16 >= F(1, 512)},
    {"name": "nonnegative_case_constant", "actual": str(F(3, 100)),
     "required_lower": str(F(1, 512)), "passes": F(3, 100) > F(1, 512)},
]
failures = [c for c in checks if not c.get("positive_gap", c.get("passes", False))]
certificate = {
    "purpose": "Exact rational arithmetic supporting the analytic L951 proof; no sampled phase or transcendental evaluation.",
    "analytic_obligation": "DLMF1.4.35-37 gives exp(-a)>P7(-a) for a>0 because the eighth-order remainder is positive; uniform phase proof is in L951.",
    "checks": checks, "failures": failures,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
for c in checks:
    actual = c.get("polynomial_lower", c.get("actual"))
    required = c.get("required_lower", c.get("required_upper"))
    relation = ">" if "polynomial_lower" in c else ("<" if "required_upper" in c else ">=")
    print(f"actual={actual} required={relation}{required} pass={c.get('positive_gap', c.get('passes'))}")
print(f"failures={len(failures)} certificate={path}")
raise SystemExit(bool(failures))

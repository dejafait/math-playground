"""Exact arithmetic supporting L097; no numerical factorization oracle."""
import json
from functools import reduce
from math import gcd
from pathlib import Path

coefficients = [55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215]
prime = 11
checks = {
    "degree_eight": len(coefficients) == 9 and coefficients[-1] != 0,
    "all_lower_coefficients_divisible_by_11": all(c % prime == 0 for c in coefficients[:-1]),
    "leading_coefficient_not_divisible_by_11": coefficients[-1] % prime != 0,
    "constant_not_divisible_by_121": coefficients[0] % (prime * prime) != 0,
    "primitive_content": reduce(gcd, coefficients) == 1,
    "no_n_coordinate_factor": coefficients[-1] != 0,
    "no_m_coordinate_factor": coefficients[0] != 0,
}
certificate = {
    "coefficients_ascending_m_degree": coefficients,
    "prime": prime,
    "lower_coefficient_quotients": [c // prime for c in coefficients[:-1]],
    "leading_remainder_mod_11": coefficients[-1] % prime,
    "constant_remainder_mod_121": coefficients[0] % (prime * prime),
    "content": reduce(gcd, coefficients),
    "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
    "actual_factor_degrees_over_Q": [8],
    "continuation_requires_nontrivial_factor_degrees": True,
    "conclusion_basis": "Eisenstein at 11 plus the homogeneous argument in L097",
}
path = Path(__file__).with_name("octic-irreducibility-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {certificate['failures']}")
print("Actual rational factor degrees: [8]; continuation requires nontrivial factors: unmet")
print(f"Certificate: {path}")
if certificate["failures"]:
    raise SystemExit(1)

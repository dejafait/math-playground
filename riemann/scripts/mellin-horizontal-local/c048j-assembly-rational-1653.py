"""Exact arithmetic replay for C048j; analytic monotonicity is in the proof."""

from fractions import Fraction
import json
from pathlib import Path


def rational(value):
    value = Fraction(value)
    return f"{value.numerator}/{value.denominator}"


components = {
    "local": Fraction(1318214, 1000000),
    "gaussian_pair": Fraction(99276, 1000000),
    "right": Fraction(96514, 1000000),
    "near_left": Fraction(91191, 1000000),
    "lower_power": Fraction(1, 864),
    "higher_modes": Fraction(1, 10000),
    "distant_left": Fraction(1, 10000),
    "combined_origin": Fraction(1, 10000),
}
total = sum(components.values(), Fraction())
required = Fraction(17, 10)
scalar_cap = Fraction(196, 9 * 2**20)
checks = {
    "radial_endpoint": 2**12 > 28 * 12**2,
    "higher_mode_prefactor": Fraction(112 * 28, 12**2) == Fraction(196, 9),
    "higher_mode_allocation": scalar_cap < Fraction(1, 10000),
    "lower_power_scale": Fraction(2, 12**3) == Fraction(1, 864),
    "total_identity": total == Fraction(8675923, 5400000),
    "total_below_required": total < required,
    "margin_identity": required - total == Fraction(504077, 5400000),
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "scope": "Exact rational arithmetic only; no numerical sampling or analytic verification.",
    "proof": "lemmas/C048j-mellin-full-relative-remainder-assembly.md, equations (10)-(13)",
    "budget": {
        "components": {name: rational(value) for name, value in components.items()},
        "total": rational(total),
        "required": rational(required),
        "margin": rational(required - total),
    },
    "scalar": {
        "endpoint_actual_lower_numerator": 2**12,
        "endpoint_required_numerator": 28 * 12**2,
        "higher_mode_rational_cap": rational(scalar_cap),
        "higher_mode_required": "1/10000",
        "allocation_cross_product_actual": 196 * 10000,
        "allocation_cross_product_required": 9 * 2**20,
    },
    "checks": checks,
    "failures": failures,
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"checks: {sum(checks.values())}/{len(checks)}; failures: {failures}")
print(f"total: {rational(total)} < required {rational(required)}; margin {rational(required-total)}")
print(f"higher-mode cap: {rational(scalar_cap)} < required 1/10000")
print(f"certificate: {output}")
if failures:
    raise SystemExit(1)

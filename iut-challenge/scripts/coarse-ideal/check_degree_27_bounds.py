"""Exact rational checks for L015; no exact-logarithm/orbit computation."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def ceiling(value):
    return -((-value.numerator) // value.denominator)


exp_partial = sum((F(1, factorial(j)) for j in range(8)), F(0))
exp_tail_upper = F(1, factorial(8)) / (1 - F(1, 9))
ln_partial = 2 * sum((F(1, (2*j+1) * 2**(2*j+1)) for j in range(6)), F(0))
ln_tail_upper = 2 * F(1, 13 * 2**13) / (1 - F(1, 4))
checks = {
    "exp_lower": exp_partial > F(27, 10),
    "exp_upper": exp_partial + exp_tail_upper < F(2719, 1000),
    "ln_lower": ln_partial > F(109, 100),
    "ln_upper": ln_partial + ln_tail_upper < F(1099, 1000),
    "C_lower": F(27, 10) * F(109, 100) > F(29, 10),
    "C_upper": F(2719, 1000) * F(1099, 1000) < 3,
    "discrete_rounding": 29**27 > 3**26 * 10**27,
    "native_t": 3**3 <= F(81, 2) < 3**4,
}
rows = []
for k in range(27):
    q = ceiling(F(14, 27) - 1 - F(k, 27) + 2)
    q_native = ceiling(F(14, 27) - 1 - F(k, 27) + F(80, 27))
    radius = 3**(q + 3)
    row = {
        "k": k, "s": str(F(k, 27)), "q": q,
        "certified_radius_after_removing_3_pow_minus_n": radius,
        "required_radius_after_removing_3_pow_minus_n": 81,
        "ratio": str(F(radius, 81)), "certifies": radius <= 81,
        "native_q": q_native,
        "native_radius_exponent": str(F(q_native + 1) + F(80, 27)),
        "lower_valuation_at_q_1": str(F(k, 27)),
        "inner_threshold": "14/27",
    }
    checks[f"class_{k}"] = (
        q == (2 if k <= 13 else 1)
        and q_native == (3 if k <= 12 else 2)
        and (radius <= 81) == (k >= 14)
        and 1 + q + F(k, 27) - 2 >= F(14, 27)
        and 1 + (q-1) + F(k, 27) - 2 < F(14, 27)
    )
    rows.append(row)
failures = [name for name, passed in checks.items() if not passed]
out = Path(__file__).with_name("degree-27-bounds.json")
out.write_text(json.dumps({"scope": "sufficient ideal sandwich, not actual orbit radii",
                           "checks": checks, "failed_checks": failures, "rows": rows}, indent=2) + "\n")
print("Degree 27: k=0..13 certifies radius 243 versus required 81; k=14..26 certifies 81 versus 81 (remove common 3^(-n)).")
print("Failed checks:", failures)
print("Certificate:", out.relative_to(Path.cwd()))
if failures:
    raise SystemExit(1)

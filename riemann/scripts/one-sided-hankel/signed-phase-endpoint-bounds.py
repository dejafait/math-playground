"""Exact rational checks for L662; no numerical contour or H claim."""
from fractions import Fraction as F
from pathlib import Path
import json


rows = []


def check(name, actual, required, relation=">"):
    actual, required = F(actual), F(required)
    passed = actual > required if relation == ">" else actual < required
    rows.append({"name": name, "actual": str(actual),
                 "required": str(required), "relation": relation,
                 "passed": passed})


d, U, h, ymax = F(5, 4), F(121, 64), F(1, 8), F(27, 100)
cmax = 1 / d
num_lower = (1-cmax*h)**2-(cmax*ymax)**2
den_upper = ((1+cmax*h)**2+(cmax*ymax)**2)**2
check("f_prime_numerator", num_lower, F(3, 4))
check("f_prime_denominator", den_upper, F(15, 8), "<")
check("f_prime_ratio", num_lower/den_upper, F(2, 5))
bin_bounds = [F(11, 20), F(37, 100), F(23, 100), F(1, 8)]
for j, lower in enumerate(bin_bounds, 1):
    t = F(j, 4)
    check(f"right_bin_{j}_A_minus_b", 1/(d+t)-t/(U+d*t), lower)
check("four_bin_mean", sum(bin_bounds)/4, F(3, 10))
check("vertical_log_derivative_upper", cmax/(1-cmax*h), 1, "<")
for A in [F(4, 5), F(4)]:
    check(f"phase_factor_endpoint_{A}",
          A/((1+A*h)**2+(A*ymax)**2), F(3, 5))
rho, kappa = F(81, 6250), F(91, 5000)
horizontal_rate = F(3, 25)*h
bottom_rate = (F(6, 5)-1)*h
check("horizontal_vs_endpoint_rate", horizontal_rate, rho)
check("bottom_vs_endpoint_rate", bottom_rate, rho)
paid_margin = F(1, 16)-2*kappa-2*rho
check("paid_exponential_margin", paid_margin, 0)
check("limiting_beta_real_parameter_upper", 1, F(6, 5), "<")
failures = [row["name"] for row in rows if not row["passed"]]
output = {
    "status": "EXACT_RATIONAL_CHECKS_ONLY",
    "checks": rows,
    "comparisons": {
        "endpoint_rate": str(rho), "diagonal_half_rate": str(kappa),
        "horizontal_rate": str(horizontal_rate),
        "bottom_rate": str(bottom_rate),
        "horizontal_surplus": str(horizontal_rate-rho),
        "paid_margin": str(paid_margin),
        "paid_margin_required": "0",
        "paid_logarithmic_loss": "5 log n + an absolute constant",
    },
    "failures": failures,
    "limitations": [
        "Checks rational inequalities, not the analytic contour proof.",
        "No finite numerical H, D, endpoint integral or effective onset computed.",
        "L661's prior exact certificates and analytic hypotheses are inherited.",
    ],
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(output, indent=2)+"\n")
print(f"Exact rational checks: {len(rows)}; failures: {failures}")
print(f"Horizontal rate {horizontal_rate} > endpoint rate {rho}")
print(f"Paid exponential margin {paid_margin} > required 0; loss 5 log n + C")
print(path)
if failures:
    raise SystemExit(1)

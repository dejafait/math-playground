"""Exact arithmetic witnesses for L654; not a proof of its analytic steps."""
from fractions import Fraction as F
import json
from pathlib import Path

R, eta, d = F(11, 8), F(1, 100), F(5, 4)
sigma2, n0 = F(137, 5000), 8192
records = []


def check(name, actual, relation, required, purpose):
    valid = {"<": actual < required, "<=": actual <= required,
             "==": actual == required, ">": actual > required}[relation]
    records.append({"name": name, "actual": str(actual),
                    "relation": relation, "required": str(required),
                    "passed": valid, "purpose": purpose})


check("radial_margin", R*R-(R-eta)**2, "==", sigma2,
      "Original squared diagonal margin.")
check("ordinate_square", (R-eta)**2-d*d, "==", F(12029, 40000),
      "Common-line geometry for the polynomial kernel.")
check("ordinate_less_than_one", F(12029, 40000), "<", F(1),
      "Every node ordinate has modulus less than one.")
check("contour_holomorphic", R-eta+F(1, 16), "<", F(3, 2),
      "The entire union of disks avoids all possible poles of f_u.")
check("kernel_factor", 2+F(1, 16), "<", 2*R,
      "Every boundary-to-node factor is smaller than 2R.")
check("adaptive_radius", F(1, 3)/8, "<", F(1, 16),
      "r_0=N/(8n) has room for regular-radius approximation.")
check("log_ratio_coefficient", 2+4/(1-4*F(1, 16)), "<", F(8),
      "Scalar logarithm bound in the reflected-weight ratio.")
check("R_over_sigma_squared", R*R, "<", 81*sigma2,
      "R/sigma<9.")
check("density_log_argument", F(22*384), "<", F(2**14),
      "log(8448)<14 log(2).")
v = F(7, 10)
exp_lower = 1+v+v*v/2+v*v*v/6
check("log_two_witness", exp_lower, ">", F(2),
      "The positive exponential series proves log(2)<7/10.")
check("density_rate", (1+14*v)/384, "==", F(9, 320),
      "Upper envelope for phi(1/384).")
check("log_nine_witness", F(1+3)+F(9, 2)+F(27, 6), ">", F(9),
      "The positive exponential series proves log(9)<3.")
check("onset_polynomial_cost", 3+2*13*v, "<", F(n0, 320),
      "3+2 log(n)<=n/320 starts at n=8192.")
check("onset_monotonicity", F(1, 320)-F(2, n0), ">", F(0),
      "Derivative stays positive for every n>=8192.")
check("total_amplitude_rate", F(9, 320)+F(1, 320), "==", F(1, 32),
      "Contour and polynomial costs meet the required amplitude rate.")
check("anchor_diagonal", 1/(R*R-d*d), "==", F(64, 21),
      "r_x>=1 and W_x=1.")
check("correction_coefficient_squared", F(21), "<", 2304*sigma2,
      "sqrt(21)/(24 sigma)<2.")
check("correction_series_constant", F(12*32**3), "==", F(393216),
      "2n exp(-n/32)<=12*32^3/n^2.")
check("correction_at_onset", F(393216, n0*n0), "==", F(3, 512),
      "Uniform correction-to-guaranteed-response bound at the onset.")
check("correction_budget", F(3, 512), "<", F(1, 2),
      "At least one half of the guaranteed response remains.")
check("squared_rate", 2*F(1, 32), "==", F(1, 16),
      "Required squared exponent.")

failures = [r["name"] for r in records if not r["passed"]]
certificate = {
    "lemma": "L654", "arithmetic": "exact fractions",
    "scope": "Arithmetic witnesses only; the contour and uniform proof are in the lemma.",
    "checks": records, "failures": failures,
    "summary": {"passed": len(records)-len(failures), "total": len(records)},
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Exact checks: {len(records)-len(failures)}/{len(records)}; failures={failures}")
print("Amplitude rate: actual upper 1/32; required <=1/32.")
print("Correction ratio: actual upper 3/512; required <1/2.")
print(f"Certificate: {output}")
if failures:
    raise SystemExit(1)

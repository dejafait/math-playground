"""Exact rational checks for C033d; no kernel or residual evaluation."""
from decimal import Decimal, localcontext
from fractions import Fraction as Q
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "scripts/smoothed-law/bounded_variation_dual_1571.json"
OUTPUT = ROOT / "scripts/smoothed-law/fixed_coefficient_budget_1620.json"
KEY = "Im_kappa_imaginary_1/4"
EXPECTED = Q(
    "-1313856261460852651698517424056740423120000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000/35468128185841057810934033462631278307784452433174229572507840657635824754834175109863281250004123020165856090648277558652033231447112095364941"
)
source = json.loads(SOURCE.read_text())
coefficients = {k: Q(v) for k, v in source["candidate"]["coefficients"].items()}
c = coefficients[KEY]
C = abs(c)
A = 3 * (40 * Q(3, 8) ** 18 + Q(1, 10**100))
o0 = 2 * A
weighted_factor = C * o0
checks = []


def record(name, actual, relation, required):
    passed = {"==": actual == required, "<": actual < required,
              ">": actual > required}[relation]
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=passed))


record("literal_coefficient_matches_full_saved_fraction", c, "==", EXPECTED)
record("saved_dictionary_size", len(coefficients), "==", 20)
record("all_other_coefficients_zero",
       sum(v != 0 for k, v in coefficients.items() if k != KEY), "==", 0)
record("coefficient_nonzero", C, ">", Q(0))
record("C033c_disk_allowance", 16 * A, "<", Q(1, 8192))
record("O_error_at_fixed_point_positive", o0, ">", Q(0))
record("O_error_at_fixed_point_cap", o0, "<", Q(1, 65536))
record("weighted_rational_factor_lower", weighted_factor, ">", Q(19119813271, 10**20))
record("weighted_rational_factor_upper", weighted_factor, "<", Q(19119813273, 10**20))

failures = [x["name"] for x in checks if not x["passed"]]
certificate = dict(
    result="CONDITIONAL_BUDGET_ONLY",
    canonical_proof="lemmas/C033d-fixed-saved-coefficient-kappa-error-budget.md",
    source=str(SOURCE.relative_to(ROOT)), coefficient_key=KEY,
    full_coefficient=str(c), coefficient_magnitude=str(C),
    C033c_A=str(A), zero_O_error=str(o0), O_error_cap="1/65536",
    weighted_rational_factor=str(weighted_factor),
    weighted_error_formula="C*exp(-a)*((exp(e)-1)*sinh(B)+exp(e)*o*cosh(B+o))+h",
    tolerance_condition="D=m-h-C*exp(-a)*(exp(e)-1)*sinh(B)>0; o<=t; o<D*exp(a-e)/(C*cosh(B+t))",
    zero_approximant=dict(qhat="0", exact_arithmetic_residual="1",
                         required_residual="<1/2", positive_margin_available=False),
    unresolved=["certified uniform lower bound on Re(Ehat)",
                "certified E error", "final nonlinear arithmetic error",
                "certified candidate residual margin below 1/2",
                "external divisor/finite-zero/heat/fixed-v1 inputs not independently verified"],
    no_E_or_actual_residual_evaluation=True, checks=checks, failures=failures,
)
OUTPUT.write_text(json.dumps(certificate, indent=2) + "\n")
with localcontext() as ctx:
    ctx.prec = 14
    print("C*o0 =", Decimal(weighted_factor.numerator) / Decimal(weighted_factor.denominator),
          "; exp(-a+e) and cosh(o0) remain unpaid")
print("O error cap: actual 2*A; required <1/65536:", o0 < Q(1, 65536))
print("Zero O approximant residual: actual 1; required <1/2; no positive margin")
print("Rational-check failures:", failures)
print("Full certificate:", OUTPUT.relative_to(ROOT))
if failures:
    raise SystemExit(1)

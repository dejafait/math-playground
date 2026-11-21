"""Independent exact arithmetic audit of C032x; analytic proof stays canonical.

Read, but never rewrite, certificate1576. No large powers of ten, kernel
evaluations, zero coordinates or optimization are used.
"""
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
original = HERE / "bounded_variation_effective_cost_1576.json"
saved = json.loads(original.read_text())
checks = []


def record(name, actual, required, relation):
    predicates = {"=": lambda: actual == required,
                  ">": lambda: actual > required,
                  "<": lambda: actual < required}
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation=relation, passed=predicates[relation]()))


# Direct powers/factorials, independently of producer1576's recurrence.
def lower(x):
    return sum((x**n / factorial(n) for n in range(33)), F(0))


p2_lower = lower(F(25, 16)) + 6*lower(F(2)) + F(7, 2) + lower(F(81, 16))
record("P2_degree32_lower", p2_lower, F(210), ">")
record("P2_degree32_lower_upper_bracket", p2_lower, F(211), "<")
record("saved_P2_lower", p2_lower, F(saved["exact_values"]["P2_lower"]), "=")
record("e_cubed_lower", F(8, 3)**3, F(10), ">")
tail_constant = F(8)*F(4, 3)*F(210)
record("tail_allowance_constant", tail_constant, F(2240), "=")

expected = [(F(1), 2240, 12588154880000, 3345066),
            (F(1, 8), 17920, 51561082388480000, 214084266)]
costs = []
record("saved_cost_rows", len(saved["cost_bounds"]), len(expected), "=")
for index, (epsilon, t_required, k_required, j_required) in enumerate(expected):
    t0 = tail_constant / epsilon
    k0 = t0**4 / 2
    exponent = (2*t0*t0) // 3
    prefix = f"epsilon={epsilon}"
    record(prefix+":T_threshold", t0, F(t_required), "=")
    record(prefix+":K_threshold", k0, F(k_required), "=")
    record(prefix+":J_decimal_exponent", exponent, j_required, "=")
    record(prefix+":J_prefactor", t0**3/(8*epsilon), F(1), ">")
    remainder = 2*t0*t0 - 3*exponent
    record(prefix+":exponent_remainder_lower", remainder+1, F(0), ">")
    record(prefix+":exponent_remainder_upper", remainder, F(3), "<")
    row = saved["cost_bounds"][index]
    record(prefix+":saved_tolerance", F(row["requested_primitive_error_strict_upper"]), epsilon, "=")
    record(prefix+":saved_T", F(row["necessary_spatial_cutoff_strict_lower"]), t0, "=")
    record(prefix+":saved_K", F(row["necessary_Taylor_degree_strict_lower"]), k0, "=")
    record(prefix+":saved_J", row["necessary_midpoint_cell_count_strict_lower"], f"10^{exponent}", "=")
    record(prefix+":saved_exponent", row["decimal_power_exponent"], exponent, "=")
    record(prefix+":conditional_integer_T", row["integer_spatial_cutoff_at_least"], int(t0)+1, "=")
    costs.append(dict(epsilon=str(epsilon), strict_T_lower=str(t0),
                      strict_K_lower=str(k0), strict_J_lower=f"10^{exponent}",
                      exponent_remainder=str(remainder)))

# Check both coefficients of the affine identity, not samples in x.
# A=u+x/2, B=u+2*x, 4*A-B=3*u.
record("box_identity_u_coefficient", F(4)-1, F(3), "=")
record("box_identity_x_coefficient", F(4)*F(1, 2)-2, F(0), "=")
record("box_triangle_weight", F(4)+1, F(5), "=")
record("box_sharp_A_at_u1_x_minus4over5", 1-F(4, 5)/2, F(3, 5), "=")
record("box_sharp_B_at_u1_x_minus4over5", 1-2*F(4, 5), -F(3, 5), "=")
record("box_floor_exceeds_required_residual", F(3, 5), F(1, 2), ">")
record("saved_box_floor", F(saved["exact_values"]["independent_error_box_residual_lower"]), F(3, 5), "=")

failures = [entry for entry in checks if not entry["passed"]]
certificate = dict(
    scope="Exact arithmetic accompanying canonical C032x audit1604; no true-error or actual-cone bound",
    original_certificate="scripts/smoothed-law/"+original.name,
    complete_analytic_record="lemmas/C032x-common-disk-effective-evaluator-cost-stop.md",
    exact_P2_lower=str(p2_lower), cost_bounds=costs,
    box_floor="3/5", required_residual_strict_upper="1/2",
    checks=checks, failures=failures,
    limitations=["Analytic inequalities and box admissibility require canonical proof",
                 "No actual kernel residual certified; q=0 still has residual 1",
                 "External inputs inherited, not independently verified",
                 "No large powers of ten allocated"])
output = HERE / "common_disk_cost_audit_1604.json"
output.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Exact checks={len(checks)}; failures={len(failures)}; 210<P2_lower<211")
for row in costs:
    print(f"Delta_E<{row['epsilon']}: T>{row['strict_T_lower']}, "
          f"K>{row['strict_K_lower']}, J>{row['strict_J_lower']}")
print("Independent-box floor=3/5; target <1/2; actual-cone lower bound not asserted")
print(f"Full certificate: {output}")
raise SystemExit(bool(failures))

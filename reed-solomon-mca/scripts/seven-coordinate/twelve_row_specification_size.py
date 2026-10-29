"""Size and elementary encoding checks only; no compatibility solving."""
import json
from pathlib import Path

Q = 97**20
variables = {"kernel": 9, "chart_matrix": 4, "chart_inverse": 1,
             "support_bits": 100, "row_witnesses": 12*14}
equations = {"boolean": 100, "valid_support": 10, "pivot": 1,
             "plucker": 35, "chart_invertible": 1,
             "pair_incidence": 66, "label_degree": 16,
             "row_gates": 12*16}
V = sum(variables.values())
E = sum(equations.values())
codes = []
failures = []
for code in range(1024):
    bits = [(code >> i) & 1 for i in range(10)]
    selected = []
    for a in range(756):
        value = 1
        for i in range(10):
            value *= bits[i] if (a >> i) & 1 else 1-bits[i]
        if value:
            selected.append(a)
    expected = [code] if code < 756 else []
    if selected != expected:
        failures.append({"code": code, "actual": selected, "expected": expected})
    codes.append({"code": code, "selected": selected})
incidence_checks = []
for n in range(17):
    linear = (n*(n-1)) % 97 == 0
    degree_product = 1
    for j in range(5):
        degree_product = degree_product*(n-j) % 97
    low_degree = degree_product == 0
    if linear != (n <= 1) or low_degree != (n <= 4):
        failures.append({"count": n, "linear": linear, "degree": low_degree})
    incidence_checks.append({"integer_count": n, "linear_gate": linear,
                             "degree_gate": low_degree})
# Straight-line arithmetic gate upper bound from the draft's recipe.
# Scalar multiplications count as gates; signed p aliases have 14 spare gates.
gates = {"bit_complements": 100, "indicators": 10*756*9,
         "lookup_tables": 10*51*(756+755), "validity": 10*(755+1),
         "kernel_coordinates": 21*(9+8), "signed_frame": 14,
         "chart_vectors": 14*3, "boolean": 100*2, "pivot": 1,
         "plucker": 35*5, "chart_inverse": 5,
         "pair_incidence": 66*33, "label_degree": 16*19,
         "shortening": 12*7*6, "overlap_weights": 12*7*3,
         "lambda_inverse": 12*2, "projection": 12*60}
power_gates = Q.bit_length()-1 + Q.bit_count()-1
gates["field_equations"] = V*(power_gates+1)  # subtract the input
branches = 79380*21
result = {
    "scope": "Specification-size and encoding checks; no solver or row census",
    "variables": variables, "variables_per_branch": V,
    "equations_before_field": equations, "equations_before_field_total": E,
    "field_equations": V, "equations_per_branch": E+V,
    "field_order": str(Q), "field_order_bits": Q.bit_length(),
    "field_order_popcount": Q.bit_count(), "power_gates_per_variable": power_gates,
    "nonfield_degree_upper_bound": 50,
    "arithmetic_gate_upper_bounds": gates, "gates_per_branch_upper_bound": sum(gates.values()),
    "pair_branches": 79380, "plucker_charts": 21, "pair_chart_branches": branches,
    "factored_projection_pivot_combinations": 4**12,
    "ordered_extra_support_assignments_before_gates": str(756**10),
    "explicit_all_branch_variables": branches*V,
    "explicit_all_branch_equations": branches*(E+V),
    "explicit_all_branch_gate_upper_bound": branches*sum(gates.values()),
    "lookup_domain_checks": codes, "integer_gate_checks": incidence_checks,
    "failures": failures,
    "qualifications": ["No satisfiability or emptiness computation",
                       "No polynomial-multiplier certificate or certificate-size bound",
                       "Generator circuits are not expanded monomial lists",
                       "Counts do not establish computational tractability"],
}
path = Path(__file__).with_name("twelve-row-specification-size.json")
path.write_text(json.dumps(result, indent=2)+"\n")
print(f"variables={V}; equations={E+V} ({E} before field); branches={branches}")
print(f"nonfield degree <=50; field degree={Q}; gate upper bound={sum(gates.values())}")
print(f"lookup checks=1024/1024; integer count checks=17/17; failures={len(failures)}")
print(f"certificate={path}")
if failures:
    raise SystemExit(1)

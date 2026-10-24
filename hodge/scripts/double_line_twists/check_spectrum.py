#!/usr/bin/env python3
"""Exact arithmetic checks for L157; numerical feasibility is not existence."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
failures = []


def require(condition, label):
    if not condition:
        failures.append(label)


def chi(a, b):
    r, t, d = a
    s, u, e = b
    return 2 * r * s + r * e + s * d + 14 * t * u


def type_data(a):
    r, t, d = a
    return {
        "character_r_t_d": a,
        "euler": 2 * r + d,
        "simple_lhs": r * r + r * d + 7 * t * t,
        "mukai_square": -chi(a, a),
    }


def formal_model(a, b, opposite=False):
    # At z=0. Remainder is assigned to one formal stable type.
    whole = [31, 4, -132] if opposite else [24, -4, -167]
    line_t = [1, -1] if opposite else [-1, 1]
    q = a + b
    remainder = [whole[0] - q, whole[1] - line_t[0] * a - line_t[1] * b,
                 whole[2] + 7 * q]
    types = [[1, line_t[0], -7], [1, line_t[1], -7], remainder]
    multiplicities = [a, b, 1]
    indices = [[chi(x, y) for y in types] for x in types]
    ext1 = [[(2 if i == j else 0) - indices[i][j]
             for j in range(3)] for i in range(3)]
    rank_first_second = [sum(m * x[j] for m, x in zip(multiplicities, types))
                         for j in range(3)]
    endpoint = sum(m * m for m in multiplicities)
    middle = sum(multiplicities[i] * multiplicities[j] * ext1[i][j]
                 for i in range(3) for j in range(3))
    constraints = {
        "positive_residual_rank": remainder[0] > 0,
        "residual_nonpositive_euler": 2 * remainder[0] + remainder[2] <= 0,
        "residual_simple_bound": type_data(remainder)["simple_lhs"] <= 1,
        "distinct_pair_indices_nonpositive": all(indices[i][j] <= 0
                                                for i in range(3) for j in range(3)
                                                if i != j),
        "nonnegative_ext1": all(x >= 0 for row in ext1 for x in row),
        "character_sum": rank_first_second == whole,
        "whole_end_euler": 2 * endpoint - middle == chi(whole, whole),
        "middle_cohomology_sum": 5 * q - (2 * remainder[0] + remainder[2])
                                  == (70 if opposite else 119),
    }
    return {
        "multiplicities": multiplicities,
        "types": [type_data(x) for x in types],
        "whole_character_r_t_d": whole,
        "all_ordered_pair_euler_indices": indices,
        "all_ordered_pair_ext1_dimensions": ext1,
        "whole_end_ext_dimensions": [endpoint, middle, endpoint],
        "checks": constraints,
    }


transforms = []
finite_cases = []
for r in [-4, -3, -2, -1, 1, 2, 3, 4]:
    rank, t, d = 17 + 14 * r * r, 4 * r, -34 - 98 * r * r
    require(2 * rank + d == -70 * r * r, f"H_{r} Euler")
    transforms.append({"r": r, "character_r_t_d": [rank, t, d],
                       "cohomology": [0, 70 * r * r, 0],
                       "line_middle_cost_in_M": 7 * r * r - 2,
                       "individual_M_budget_bound_at_z0": 119 // (7 * r * r - 2)})

for r in [2, 3, 4]:
    qmax = 119 // (7 * r * r - 2)
    rows = []
    for a in range(qmax + 1):
        for b in range(qmax + 1 - a):
            q, t = a + b, 4 * r - a + b
            rank, d = 17 + 14 * r * r - q, -34 - 98 * r * r + 7 * q
            checks = {
                "cohomology": q <= 14 * r * r,
                "uniform_type_bound": 7 * q + 5 * abs(t) <= 34 + 98 * r * r,
                "both_distinct_line_indices": 12 * q + 14 * abs(t) <= 119 + 168 * r * r,
                "single_residual_simple_bound": rank * rank + rank * d + 7 * t * t <= 1,
                "single_residual_euler": 2 * rank + d <= 0,
            }
            for name, ok in checks.items():
                require(ok, f"r={r},a={a},b={b}: {name}")
            rows.append({"a": a, "b": b, "residual": type_data([rank, t, d]),
                         "checks": checks})
    finite_cases.append({"r": r, "required_q_bound": qmax,
                         "number_of_all_pairs": len(rows), "all_pairs": rows})

surviving = []
for a, b in [(12, 2), (6, 8)]:
    models = {"M": formal_model(a, b), "H1": formal_model(a, b, True)}
    for side, model in models.items():
        for name, ok in model["checks"].items():
            require(ok, f"surviving {a},{b} {side}: {name}")
    surviving.append({"a": a, "b": b, **models})

strict_comparisons = []
for a, b, violated in [(13, 0, "a<=12"), (2, 9, "b<=8"), (12, 3, "a+b<=14")]:
    baseline = formal_model(a, b)
    for name, ok in baseline["checks"].items():
        require(ok, f"baseline {a},{b}: {name}")
    strict_comparisons.append({"a": a, "b": b, "new_bound_violated": violated,
                               "M_only_formal_model": baseline})

remaining_lines = []
for t in [-4, -3, -2, 2, 3, 4]:
    residual = [23, -4 - t, -167 + 7 * t * t]
    index = chi([1, t, -7 * t * t], residual)
    require(index == -121 - 168 * t * t - 56 * t, f"line {t} index formula")
    require(type_data(residual)["simple_lhs"] <= 1, f"line {t} residual simple")
    require(2 * residual[0] + residual[2] < 0 and index < 0, f"line {t} endpoints/index")
    remaining_lines.append({"t": t, "M_residual": type_data(residual),
                            "line_residual_euler": index})

certificate = {
    "scope": "L157 exact arithmetic only; no existence, source verification or proof audit",
    "actual_bounds": {"absolute_nonzero_exponent": 4, "m_minus_1": 12,
                      "m_plus_1": 8, "sum_m_minus_plus_1": 14},
    "required_for_kernel_exclusion": "No compatible complete actual kernel; not established",
    "transforms": transforms,
    "all_higher_power_candidate_checks": finite_cases,
    "surviving_formal_models": surviving,
    "strict_comparisons_with_old_M_constraints": strict_comparisons,
    "remaining_line_exponents": remaining_lines,
    "b9_endpoint": {"forced_a": 2, "residual_character": [20, 11, -55],
                    "required_rank_from_uniform_equality": 22, "actual_rank": 20},
    "failures": failures,
    "passed": not failures,
}
output = HERE / "spectrum_certificate.json"
output.write_text(json.dumps(certificate, indent=2) + "\n")
print("Exact spectrum checks:", "PASS" if not failures else "FAIL")
print("Actual bounds: |t|<=4; m_-1<=12; m_1<=8; m_-1+m_1<=14.")
print("Required for exclusion: incompatible full kernel; not established.")
print("Higher-power cases:", sum(x["number_of_all_pairs"] for x in finite_cases),
      "; formal surviving branches:", len(surviving))
print("Failures:", failures)
print("Certificate:", output)
raise SystemExit(bool(failures))

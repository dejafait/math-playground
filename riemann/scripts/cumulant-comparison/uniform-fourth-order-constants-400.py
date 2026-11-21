"""Exact finite checks for L770; the analytic proof is in the lemma."""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json


checks = []


def check(name, actual, required, relation="<"):
    actual, required = Q(actual), Q(required)
    passed = {"<": actual < required, "<=": actual <= required,
              "=": actual == required}[relation]
    checks.append({"name": name, "actual": str(actual),
                   "relation": relation, "required": str(required),
                   "passed": passed})


q = [[Q(-3, 2), Q(1)]]
for _ in range(3):
    out = [Q(0)] * (len(q[-1]) + 1)
    for d, c in enumerate(q[-1]):
        out[d] += d*c
        out[d+1] -= c
    q.append(out)
expected = [[Q(-3, 2), Q(1)], [Q(0), Q(5, 2), Q(-1)],
            [Q(0), Q(5, 2), Q(-9, 2), Q(1)],
            [Q(0), Q(5, 2), Q(-23, 2), Q(15, 2), Q(-1)]]
for j in range(4):
    for d, c in enumerate(q[j]):
        check(f"q_{j}_coefficient_{d}", c, expected[j][d], "=")
    check(f"q_{j}_absolute_coefficient_sum", sum(map(abs, q[j])), 23, "<=")
    for k in range(4):
        bound = sum(abs(c)*comb(4-d, k) for d, c in enumerate(q[j])
                    if 4-d >= k)
        check(f"h_{j}_normalized_derivative_{k}", bound, 2**8)

# A term C a^l y^d exp(-a/y) differentiates to
# C d a^l y^(d-1) + C a^(l+1) y^(d-2), times the exponential.
derivative_tables = []
for b in range(5):
    terms = {(0, b): 1}
    for k in range(4):
        expected_coeffs = ([1], [b, 1], [b*(b-1), 2*b-2, 1],
                           [b*(b-1)*(b-2), 3*b*b-9*b+6, 3*b-6, 1])[k]
        expected_terms = {(l, b-k-l): c for l, c in enumerate(expected_coeffs) if c}
        terms = {key: c for key, c in terms.items() if c}
        check(f"monomial_derivative_recurrence_b{b}_k{k}",
              int(terms == expected_terms), 1, "=")
        # Dividing by n^6, the maximum of every n^(2l-6) for n>=2
        # occurs at n=2. This checks the whole n range, not a sample.
        coefficient_ratio = sum(Q(abs(c), 2**(6-2*l))
                                for (l, d), c in terms.items())
        check(f"derivative_coefficient_bound_b{b}_k{k}", coefficient_ratio, 4, "<=")
        check(f"derivative_minimum_power_b{b}_k{k}",
              -min(d for l, d in terms), 6, "<=")
        derivative_tables.append({"b": b, "k": k,
                                  "terms": [{"a_power": l, "y_power": d, "coefficient": c}
                                            for (l, d), c in sorted(terms.items())]})
        new = {}
        for (l, d), c in terms.items():
            new[l, d-1] = new.get((l, d-1), 0) + c*d
            new[l+1, d-2] = new.get((l+1, d-2), 0) + c
        terms = new

check("exponential_series_lower_through_degree_5", Q(27, 10),
      sum(Q(1, factorial(k)) for k in range(6)))
check("e_power_7_lower", 1000, Q(27, 10)**7)
check("e_power_6_lower", 384, Q(27, 10)**6)
check("e_power_4_lower", Q(128, 3), Q(27, 10)**4)
check("consecutive_tail_ratio_numerator", Q(3, 2)**16, 657)
check("consecutive_tail_ratio", Q(657, 1000), Q(2, 3))
check("complete_tail_constant", 92*2**12*3*2**16, 2**37)
check("global_matrix_entry_sum", 2**8+2**37, 2**38)
check("global_alternant_bound", 24*2**152, 2**160)
check("high_alternant_bound", 24*15*2**24*Q(1, 2**155), Q(1, 2**120))
check("conditional_pair_cost", 37*223, 2**14)
check("log_weight_ratio", Q(4)/(Q(4)+Q(1, 2)), Q(8, 9), "=")
check("six_smoothing_powers", Q(8, 9)**6, Q(1, 2))
check("onset_smoothing_exponent", 16000-4, 6*2666, "=")
check("conditional_union_exponent", 3*14+2*9*128+2, 2348, "=")
check("low_coordinate_probability_exponent", 2348-2666, -318, "=")
final_bound = Q(72, 19)*(Q(1, 2**120)+Q(1, 2**158))
check("final_relative_bound", final_bound, Q(1, 2**117))
check("required_relative_threshold", Q(1, 2**117), Q(1, 2))

failures = [c["name"] for c in checks if not c["passed"]]
result = {
    "status": "PASS" if not failures else "FAIL",
    "scope": "Exact finite constants/recurrences only; analytic proof and infinite quantifiers are in L770.",
    "parameters": {"r": 4, "M4": 16000, "A": 128, "p_at_onset": 15996},
    "q_coefficients": [[str(c) for c in row] for row in q],
    "derivative_tables": derivative_tables,
    "checks": checks,
    "final_bound": {"exact_upper_expression": str(final_bound),
                    "simplified_strict_bound": "2^-117", "required_strict_bound": "1/2"},
    "failures": failures,
    "limitations": ["Not an independent audit of L769 or L770.",
                    "No general-order or exceptional-coefficient theorem is checked."]
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result, indent=2)+"\n")
print(result["status"], f"{len(checks)} exact finite checks; failures={failures}")
print("M4=16000, all m>=M4, u>=0: analytic claim is in L770.")
print("Relative bound: (72/19)(2^-120+2^-158) < 2^-117; required < 1/2.")
print("Certificate:", path)
if failures:
    raise SystemExit(1)

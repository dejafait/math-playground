"""Independent complete replay of L106's saved certificate; no producer import."""
from collections import Counter
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
raw = (HERE / "certificate.json").read_bytes()
c = json.loads(raw)
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def qpower(n):
    # Multinomial expansion, independent of the producer's convolution.
    out = [0] * (2*n+1)
    for twos in range(n+1):
        for ones in range(n-twos+1):
            zeros = n-twos-ones
            out[2*twos+ones] += (
                factorial(n)//(factorial(twos)*factorial(ones)*factorial(zeros))
            ) * 3**twos
    return out


q5 = qpower(5)
poly = [(q5[i] if i < 11 else 0) - (5*q5[i-1] if i else 0)
        for i in range(12)]
deriv = [i*poly[i] for i in range(1, 12)]
check("polynomial", c["phi_coefficients_ascending"] == poly)
check("derivative", c["derivative_coefficients_ascending"] == deriv)
check("derivative_factorization", deriv == [0, 0]+[-165*a for a in qpower(4)])
check("one_branch_quotient", c["phi_minus_one_div_t_cubed_coefficients"] == poly[3:])
check("finite_branch_orders", poly[:4] == [1, 0, 0, -55])
check("infinity_degree", poly[-1] == -1215)
check("model_F0", c["marked_equations"]["F0"] ==
      "sum_i c_i sum_{j even<=i} binom(i,j) u^(i-j) v^j (-3)^(j/2) - phi(r)")
check("model_F1", c["marked_equations"]["F1"] ==
      "sum_i c_i sum_{j odd<=i} binom(i,j) u^(i-j) v^j (-3)^((j-1)/2)")

labels = [[a, b, d] for a in range(11) for b in range(11) for d in range(11)
          if a != b and a != d and b != d]
check("entire_label_list", c["labels"] == labels)
check("degree", c["degree"] == len(labels) == 990)
check("cap", c["required_label_cap"] == 1000 and len(labels) <= 1000)
expected_types = {"zero": {1: 1, 5: 2}, "one": {1: 8, 3: 1}, "infinity": {11: 1}}
expected_hist = {"zero": {5: 198}, "one": {1: 336, 3: 218}, "infinity": {11: 90}}
summary = {}
producer_checks = {
    "derivative_identity": deriv == [0, 0]+[-165*a for a in qpower(4)],
    "degree_11": len(poly) == 12 and poly[-1] == -1215,
    "phi_zero_equals_one": poly[0] == 1,
    "order_three_at_zero_over_one": poly[1:3] == [0, 0] and poly[3] == -55,
    "q_discriminant": 1-12 == -11,
    "q_at_one_fifth_nonzero": 3+5+25 == 33,
    "labels_exhausted": len(labels) == 990 == len({tuple(t) for t in labels}),
    "label_cap": len(labels) <= 1000,
}
check("branch_names", set(c["branches"]) == set(expected_types))
for name, branch in c["branches"].items():
    p = branch["root_permutation"]
    check(name+"_root_permutation", sorted(p) == list(range(11)))
    lengths = []
    unseen = set(range(11))
    while unseen:
        start = min(unseen)
        word = [start]
        while p[word[-1]] != start:
            word.append(p[word[-1]])
            assert len(word) <= 11
        unseen.difference_update(word)
        lengths.append(len(word))
    check(name+"_root_type", dict(Counter(lengths)) == expected_types[name])
    action = branch["induced_permutation"]
    check(name+"_action_permutation", sorted(action) == list(range(990)))
    for i, t in enumerate(labels):
        check(f"{name}_action_{i}", labels[action[i]] == [p[t[0]], p[t[1]], p[t[2]]])
    cycles = branch["cycles"]
    flat = [j for cycle in cycles for j in cycle]
    check(name+"_full_partition", sorted(flat) == list(range(990)))
    check(name+"_canonical_starts", [min(word) for word in cycles] ==
          sorted(word[0] for word in cycles))
    for number, word in enumerate(cycles):
        check(f"{name}_cycle_{number}_nonempty", len(word) > 0)
        for pos, j in enumerate(word):
            check(f"{name}_cycle_{number}_edge_{pos}",
                  action[j] == word[(pos+1) % len(word)])
        producer_checks[f"{name}_cycle_{word[0]}_closes"] = action[word[-1]] == word[0]
    hist = dict(Counter(map(len, cycles)))
    stored_hist = {int(k): v for k, v in branch["cycle_histogram"].items()}
    check(name+"_histogram", hist == stored_hist == expected_hist[name])
    ram = sum(len(word)-1 for word in cycles)
    check(name+"_stored_counts", branch["cycle_count"] == len(cycles)
          and branch["ramification_sum"] == ram == 990-len(cycles))
    producer_checks[name+"_full_partition"] = sorted(flat) == list(range(990))
    producer_checks[name+"_histogram"] = hist == expected_hist[name]
    summary[name] = {"histogram": hist, "cycles": len(cycles), "ramification": ram}

ramification = sum(b["ramification"] for b in summary.values())
rhs = -2*990 + ramification
producer_checks["genus_integral_nonnegative"] = rhs % 2 == 0 and rhs >= -2
check("all_original_check_names_and_values", c["checks"] == producer_checks)
check("original_check_count", len(producer_checks) == 857)
check("original_failures", c["failures"] == [k for k, v in producer_checks.items() if not v] == [])
check("ramification_total", c["ramification_sum"] == ramification == 2128)
check("rh_rhs", c["two_g_minus_two"] == rhs == 148)
check("genus", c["genus"] == (rhs+2)//2 == 75)
check("complete_top_level_schema", set(c) == {
    "phi_coefficients_ascending", "derivative_coefficients_ascending",
    "phi_minus_one_div_t_cubed_coefficients", "marked_equations", "labels",
    "branches", "degree", "required_label_cap", "ramification_sum",
    "two_g_minus_two", "genus", "checks", "failures",
})
result = {
    "input_sha256": sha256(raw).hexdigest(),
    "method": "Full stored-data replay, independent multinomial coefficients and direct action-edge checks",
    "degree": 990, "required_label_cap": 1000, "branches": summary,
    "ramification_sum": ramification, "two_g_minus_two": rhs, "genus": (rhs+2)//2,
    "checks": checks, "check_count": len(checks),
    "original_check_count": len(producer_checks),
    "failures": [k for k, v in checks.items() if not v],
    "limits": "The geometric model, monodromy, descent and normalization premises are audited in L106, not proved by this script.",
}
out = HERE / "audit-certificate.json"
out.write_text(json.dumps(result, indent=2)+"\n")
print("Full replay:", len(checks), "checks; original checks:", len(producer_checks))
print("Degree:", 990, "required cap:", 1000, "ramification:", ramification,
      "2g-2:", rhs, "genus:", result["genus"])
print("Failures:", result["failures"], "certificate:", out)
assert not result["failures"]

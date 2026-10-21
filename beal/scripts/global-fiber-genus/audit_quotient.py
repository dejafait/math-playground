"""Independent full replay of L107; no producer imports or external packages."""
from collections import Counter
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
paths = ["quotient-certificate.json", "certificate.json", "audit-certificate.json"]
raw = {name: (HERE / name).read_bytes() for name in paths}
c, marked, prior = (json.loads(raw[name]) for name in paths)
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


# Multinomial coefficients, rather than the producer's convolutions.
q5 = [0] * 11
for a in range(6):
    for b in range(6-a):
        q5[2*a+b] += factorial(5)//(factorial(a)*factorial(b)*factorial(5-a-b))*3**a
phi = [(q5[i] if i < 11 else 0) - (5*q5[i-1] if i else 0) for i in range(12)]
check("entire_phi", c["phi_coefficients_ascending"] == phi == marked["phi_coefficients_ascending"])
check("marked_audit_input_hash", prior["input_sha256"] == sha256(raw["certificate.json"]).hexdigest())
check("marked_audit_all_records", prior["check_count"] == len(prior["checks"]) == 6822
      and all(v is True for v in prior["checks"].values()) and prior["failures"] == [])
check("marked_audit_totals", (prior["degree"], prior["required_label_cap"],
      prior["ramification_sum"], prior["two_g_minus_two"], prior["genus"]) ==
      (990, 1000, 2128, 148, 75))

# Sparse four-variable polynomials in (r,u,z,T). Actual monic polynomial
# long division, not the producer's binomial expansion or power recurrence.
def add(*args):
    result = {}
    for p in args:
        for m, a in p.items():
            result[m] = result.get(m, 0) + a
    return {m: a for m, a in result.items() if a}


def multiply(p, q):
    result = {}
    for m, a in p.items():
        for n, b in q.items():
            t = tuple(x+y for x, y in zip(m, n))
            result[t] = result.get(t, 0) + a*b
    return {m: a for m, a in result.items() if a}


Q = {(0, 0, 0, 2): 1, (0, 1, 0, 1): -2,
     (0, 2, 0, 0): 1, (0, 0, 1, 0): 3}
original = add({(0, 0, 0, i): a for i, a in enumerate(phi) if a},
               {(i, 0, 0, 0): -a for i, a in enumerate(phi) if a})
remainder = dict(original)
quotient = {}
while any(m[3] >= 2 for m in remainder):
    m = max((m for m in remainder if m[3] >= 2), key=lambda m: (m[3], m))
    t = m[:3] + (m[3]-2,)
    a = remainder[m]
    quotient = add(quotient, {t: a})
    remainder = add(remainder, multiply({t: -a}, Q))
check("full_long_division_identity", original == add(multiply(quotient, Q), remainder))
g1 = {m[:3]: a for m, a in remainder.items() if m[3] == 1}
g0 = add({m[:3]: a for m, a in remainder.items() if m[3] == 0},
         {(m[0], m[1]+1, m[2]): a for m, a in g1.items()})
expected_invariants = {
    name: [{"exponents_r_u_z": list(m), "coefficient": a} for m, a in sorted(p.items())]
    for name, p in [("G0", g0), ("G1", g1)]
}
check("full_invariant_records", c["invariant_polynomials"] == expected_invariants)

# Independently substitute z=v^2 in the result and compare with phi(u+vw)
# by repeated multiplication in the algebra w^2=-3 (variables r,u,v).
one, uu, vv = {(0, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1}
even, odd = one, {}
f0, f1 = {}, {}
for a in phi:
    f0 = add(f0, {m: a*b for m, b in even.items()})
    f1 = add(f1, {m: a*b for m, b in odd.items()})
    even, odd = add(multiply(even, uu), multiply(odd, {(0, 0, 1): -3})), add(
        multiply(even, vv), multiply(odd, uu))
f0 = add(f0, {(i, 0, 0): -a for i, a in enumerate(phi) if a})
check("F0_is_G0_v_squared", f0 == {(i, j, 2*k): a for (i, j, k), a in g0.items()})
check("F1_is_v_G1_v_squared", f1 == {(i, j, 2*k+1): a for (i, j, k), a in g1.items()})

labels = [[r, a, b] for r in range(11) for a in range(11) for b in range(a+1, 11)
          if r not in (a, b)]
index = {tuple(t): i for i, t in enumerate(labels)}
ordered = [[r, a, b] for r in range(11) for a in range(11) for b in range(11)
           if len({r, a, b}) == 3]
ordered_index = {tuple(t): i for i, t in enumerate(ordered)}
check("full_quotient_labels", c["quotient_labels"] == labels and len(labels) == 495)
check("full_ordered_input_labels", marked["labels"] == ordered and len(ordered) == 990)
check("degrees_and_cap", (c["degree"], c["ordered_degree"], c["required_label_cap"]) ==
      (495, 990, 1000))
expected_types = {"zero": {1: 1, 5: 2}, "one": {1: 8, 3: 1}, "infinity": {11: 1}}
expected_hist = {"zero": {5: 99}, "one": {1: 168, 3: 109}, "infinity": {11: 45}}
check("branch_names", set(c["branches"]) == set(expected_hist))
producer = {
    "invariant_G0_equals_quadratic_remainder": checks["full_invariant_records"]
        and checks["F0_is_G0_v_squared"],
    "invariant_G1_equals_quadratic_remainder": checks["full_invariant_records"]
        and checks["F1_is_v_G1_v_squared"],
    "quadratic_discriminant": 4-4 == 0 and -4*3 == -12,
    "square_class_constant": -12 == -3*2**2,
    "complete_quotient_labels": len(labels) == len(index) == 495,
    "maximum_label_universe_within_cap": len(ordered) == 990 <= 1000,
}
summary = {}
all_lifts = {}
for name in expected_hist:
    b = c["branches"][name]
    p = b["root_permutation"]
    check(name+"_schema", set(b) == {"root_permutation", "quotient_action", "cycles",
          "ordered_returns", "cycle_histogram", "ramification_sum", "ordered_cycle_histogram"})
    producer[name+"_root_permutation"] = sorted(p) == list(range(11))
    check(name+"_same_marked_root_action", p == marked["branches"][name]["root_permutation"])
    unseen = set(range(11))
    root_lengths = []
    while unseen:
        start = min(unseen)
        orbit = [start]
        while p[orbit[-1]] != start:
            orbit.append(p[orbit[-1]])
            assert len(orbit) <= 11
        unseen.difference_update(orbit)
        root_lengths.append(len(orbit))
    check(name+"_root_type", dict(Counter(root_lengths)) == expected_types[name])
    action = [index[(p[r], min(p[a], p[b]), max(p[a], p[b]))] for r, a, b in labels]
    check(name+"_entire_action", b["quotient_action"] == action)
    producer[name+"_quotient_action_bijective"] = sorted(action) == list(range(495))
    flat = [i for word in b["cycles"] for i in word]
    producer[name+"_full_disjoint_partition"] = sorted(flat) == list(range(495))
    check(name+"_canonical_cycle_order", [w[0] for w in b["cycles"]] ==
          sorted(min(w) for w in b["cycles"]))
    returns, lifts = [], []
    for n, word in enumerate(b["cycles"]):
        start = labels[word[0]]
        producer[f"{name}_cycle_{word[0]}_closes"] = action[word[-1]] == word[0]
        for j, i in enumerate(word):
            check(f"{name}_cycle_{n}_edge_{j}", action[i] == word[(j+1) % len(word)])
        pair = []
        for orientation, seed in enumerate([start, [start[0], start[2], start[1]]]):
            current = list(seed)
            lift = []
            for j in word:
                lift.append(ordered_index[tuple(current)])
                check(f"{name}_cycle_{n}_lift_{orientation}_over_{j}",
                      index[(current[0], min(current[1:]), max(current[1:]))] == j)
                current = [p[t] for t in current]
            check(f"{name}_cycle_{n}_lift_{orientation}_returns", current == seed)
            check(f"{name}_cycle_{n}_lift_{orientation}_distinct", len(set(lift)) == len(word))
            pair.append(lift)
        check(f"{name}_cycle_{n}_two_disjoint_lifts", not set(pair[0]).intersection(pair[1]))
        producer[f"{name}_cycle_{word[0]}_ordered_return_has_no_swap"] = current == seed
        returns.append({"start": start, "after_one_quotient_cycle": list(start),
                        "local_degree_ratio": 1})
        lifts.extend(pair)
    check(name+"_entire_ordered_returns", b["ordered_returns"] == returns)
    check(name+"_all_990_ordered_lifts", sorted(i for w in lifts for i in w) == list(range(990)))
    check(name+"_all_marked_cycles_matched",
          {frozenset(w) for w in lifts} ==
          {frozenset(w) for w in marked["branches"][name]["cycles"]})
    # Also check every marked action edge, rather than only orbit sets.
    for lift in lifts:
        for j, i in enumerate(lift):
            check(f"{name}_marked_edge_{i}",
                  marked["branches"][name]["induced_permutation"][i] == lift[(j+1) % len(lift)])
    hist = dict(Counter(map(len, b["cycles"])))
    producer[name+"_expected_histogram"] = hist == expected_hist[name]
    check(name+"_stored_histograms", b["cycle_histogram"] == {str(e): n for e, n in hist.items()}
          and b["ordered_cycle_histogram"] == {str(e): 2*n for e, n in hist.items()})
    ram = sum(len(w)-1 for w in b["cycles"])
    check(name+"_ramification", b["ramification_sum"] == ram)
    check(name+"_marked_summary", prior["branches"][name] == {
        "histogram": {str(e): 2*n for e, n in hist.items()}, "cycles": 2*len(b["cycles"]),
        "ramification": 2*ram})
    summary[name] = {"histogram": hist, "ramification": ram,
                     "ordered_lift_count": len(lifts), "relative_indices": [1]}
    all_lifts[name] = lifts

ram = sum(b["ramification"] for b in summary.values())
rhs = -2*len(labels) + ram
producer["quotient_ramification_sum"] = ram == 1064
producer["quotient_rh_and_genus"] = rhs == 74 and (rhs+2)//2 == 38
producer["unramified_double_cover_genus_consistency"] = 2*prior["genus"]-2 == 2*rhs
check("all_original_check_names_and_values", c["checks"] == producer)
check("original_count_and_failures", c["check_count"] == len(producer) == 863
      and c["failures"] == [k for k, v in producer.items() if not v] == [])
check("all_original_checks_true", all(producer.values()))
check("all_stored_totals", (c["ramification_sum"], c["two_g_minus_two"], c["genus"]) ==
      (ram, rhs, (rhs+2)//2) == (1064, 74, 38))
check("top_level_schema", set(c) == {"degree", "ordered_degree", "required_label_cap",
      "phi_coefficients_ascending", "invariant_polynomials", "quotient_labels",
      "branches", "ramification_sum", "two_g_minus_two", "genus", "checks",
      "check_count", "failures", "limits"})
check("scope_qualification", c["limits"] ==
      "Actual monodromy and the marked-cover comparison come from audited L106; "
      "invariant rings, normalization, and rational lifting are proved in L107. "
      "Individual branch representatives are not a branch-generator tuple.")
result = {
    "input_sha256": {name: sha256(data).hexdigest() for name, data in raw.items()},
    "method": "Full record comparison; multinomial phi; monic long division; quadratic-algebra "
              "expansion; every quotient edge and both complete ordered lifts checked.",
    "degree": 495, "ordered_degree": 990, "required_label_cap": 1000,
    "invariant_polynomials": expected_invariants, "branches": summary,
    "all_ordered_lift_cycles": all_lifts,
    "ramification_sum": ram, "two_g_minus_two": rhs, "genus": (rhs+2)//2,
    "original_check_count": len(producer), "checks": checks, "check_count": len(checks),
    "failures": [k for k, v in checks.items() if not v],
    "limits": "The full scheme, constants, proper-model and residue-algebra arguments are "
              "audited in L107; these finite checks do not prove those general statements.",
}
out = HERE / "quotient-audit-certificate.json"
out.write_text(json.dumps(result, indent=2)+"\n")
print("Full quotient replay:", len(checks), "checks; original checks:", len(producer))
print("Degree:", 495, "ordered:", 990, "required cap:", 1000,
      "ramification:", ram, "2g-2:", rhs, "genus:", result["genus"])
for name, data in summary.items():
    print(name, data)
print("Failures:", result["failures"], "certificate:", out)
assert not result["failures"]

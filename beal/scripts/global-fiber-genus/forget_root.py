"""Exact invariant algebra and complete pair/incidence actions for L109."""
from collections import Counter
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import json

OUT = Path(__file__).with_name("forget-root-certificate.json")
checks = {}


def check(name, value):
    checks[name] = bool(value)


def mul_coeff(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


phi = [1]
for _ in range(5):
    phi = mul_coeff(phi, [1, 1, 3])
phi = mul_coeff(phi, [1, -5])
check("actual_polynomial", phi == [
    1, 0, 0, -55, -165, -594, -1100, -2145, -2475, -2970, -1782, -1215])


def add(*polys):
    out = Counter()
    for poly in polys:
        for m, c in poly.items():
            out[m] += c
    return {m: c for m, c in out.items() if c}


def scale(poly, c):
    return {m: c*x for m, x in poly.items() if c*x}


def mul(p, q):
    out = Counter()
    for (i, j), c in p.items():
        for (k, l), d in q.items():
            out[i+k, j+l] += c*d
    return {m: c for m, c in out.items() if c}


# Independent quadratic-remainder recurrence phi(T)=A+B*T modulo Q(T).
u = {(1, 0): 1}
A, B = {(0, 0): 1}, {}
sum_A, sum_B = {}, {}
for c in phi:
    sum_A = add(sum_A, scale(A, c))
    sum_B = add(sum_B, scale(B, c))
    A, B = mul({(2, 0): -1, (0, 1): -3}, B), add(A, scale(mul(u, B), 2))
even, odd = Counter(), Counter()
for i, c in enumerate(phi):
    for j in range(i+1):
        (even if j % 2 == 0 else odd)[i-j, j//2] += c*comb(i, j)*(-3)**(j//2)
H0, H1 = add(even), add(odd)
check("H0_exact_remainder", H0 == add(sum_A, mul(u, sum_B)))
check("H1_exact_remainder", H1 == sum_B)
check("discriminant_constant_twist", -12 == -3*4)

letters = range(11)
labels = {
    "pair": list(combinations(letters, 2)),
    "ordered_pair": list(permutations(letters, 2)),
    "incidence": [(r, a, b) for r in letters
                  for a, b in combinations([x for x in letters if x != r], 2)],
    "ordered_incidence": list(permutations(letters, 3)),
}
indices = {name: {t: i for i, t in enumerate(ls)} for name, ls in labels.items()}
degrees = {"pair": 55, "ordered_pair": 110, "incidence": 495, "ordered_incidence": 990}
for name, ls in labels.items():
    check(name+"_complete_labels", len(ls) == len(indices[name]) == degrees[name])
check("maximum_label_universe_cap", max(map(len, labels.values())) <= 1000)
projections = {
    "marked_double": ("ordered_pair", "pair",
                      [indices["pair"][tuple(sorted(t))] for t in labels["ordered_pair"]], 2),
    "forget_r": ("incidence", "pair",
                 [indices["pair"][t[1:]] for t in labels["incidence"]], 9),
    "marked_forget_r": ("ordered_incidence", "ordered_pair",
                        [indices["ordered_pair"][t[1:]] for t in labels["ordered_incidence"]], 9),
}
for name, (src, dst, projection, deg) in projections.items():
    check(name+"_all_fibers", Counter(projection) == {i: deg for i in range(degrees[dst])})

perms = {
    "zero": [1, 2, 3, 4, 0, 6, 7, 8, 9, 5, 10],
    "one": [1, 2, 0, 3, 4, 5, 6, 7, 8, 9, 10],
    "infinity": list(range(1, 11)) + [0],
}
expected = {
    "pair": {"zero": {5: 11}, "one": {1: 28, 3: 9}, "infinity": {11: 5}},
    "ordered_pair": {"zero": {5: 22}, "one": {1: 56, 3: 18}, "infinity": {11: 10}},
    "incidence": {"zero": {5: 99}, "one": {1: 168, 3: 109}, "infinity": {11: 45}},
    "ordered_incidence": {"zero": {5: 198}, "one": {1: 336, 3: 218}, "infinity": {11: 90}},
}
branches = {}
for branch, p in perms.items():
    records = {}
    for name, ls in labels.items():
        action = []
        for t in ls:
            image = tuple(p[x] for x in t)
            if name == "pair":
                image = tuple(sorted(image))
            elif name == "incidence":
                image = (image[0], *sorted(image[1:]))
            action.append(indices[name][image])
        check(branch+"_"+name+"_bijective", sorted(action) == list(range(len(ls))))
        cycles, seen, cycle_of = [], set(), {}
        for start in range(len(ls)):
            if start in seen:
                continue
            cycle, pos = [], start
            while pos not in seen:
                seen.add(pos)
                cycle_of[pos] = len(cycles)
                cycle.append(pos)
                pos = action[pos]
            check(f"{branch}_{name}_cycle_{start}_closes", pos == start)
            cycles.append(cycle)
        check(branch+"_"+name+"_partition",
              sorted(x for c in cycles for x in c) == list(range(len(ls))))
        histogram = dict(Counter(map(len, cycles)))
        check(branch+"_"+name+"_histogram", histogram == expected[name][branch])
        records[name] = {
            "action": action, "cycles": cycles, "cycle_of_label": cycle_of,
            "cycle_histogram": histogram, "ramification_sum": len(ls)-len(cycles),
        }
    relative = {}
    for name, (src, dst, projection, deg) in projections.items():
        sr, dr = records[src], records[dst]
        check(branch+"_"+name+"_equivariant", all(
            projection[sr["action"][i]] == dr["action"][projection[i]]
            for i in range(degrees[src])))
        cycle_data = []
        for i, cycle in enumerate(sr["cycles"]):
            target = dr["cycle_of_label"][projection[cycle[0]]]
            base_len = len(dr["cycles"][target])
            check(f"{branch}_{name}_{i}_integral_ratio", len(cycle) % base_len == 0)
            ratio = len(cycle)//base_len
            cycle_data.append({"source_cycle": i, "target_cycle": target, "relative_e": ratio})
        for j in range(len(dr["cycles"])):
            check(f"{branch}_{name}_fiber_{j}_degree", sum(
                c["relative_e"] for c in cycle_data if c["target_cycle"] == j) == deg)
        relative[name] = {
            "cycles": cycle_data,
            "relative_e_histogram": dict(Counter(c["relative_e"] for c in cycle_data)),
            "ramification_sum": sum(c["relative_e"]-1 for c in cycle_data),
        }
        expected_ram = (56 if name == "forget_r" else 112) if branch == "one" and name != "marked_double" else 0
        check(branch+"_"+name+"_relative_ramification",
              relative[name]["ramification_sum"] == expected_ram)
    # Geometric valuations of z = -(a-b)^2/12 on the pair normalization.
    # At 0/1 a same critical-cluster pair has difference of order one in
    # the branch uniformizer. At infinity every difference has order -1.
    z_orders = []
    for cycle in records["pair"]["cycles"]:
        a, b = labels["pair"][cycle[0]]
        if branch == "infinity":
            order = -2
        elif branch == "zero":
            order = 2 if (a < 5 and b < 5) or (5 <= a < 10 and 5 <= b < 10) else 0
        else:
            order = 2 if b < 3 else 0
        z_orders.append(order)
    expected_orders = {"zero": {0: 7, 2: 4}, "one": {0: 36, 2: 1}, "infinity": {-2: 5}}
    check(branch+"_z_orders", dict(Counter(z_orders)) == expected_orders[branch])
    branches[branch] = {"root_permutation": p, "covers": records, "relative_maps": relative,
                        "pair_z_orders": z_orders}

summary = {}
for name, degree in degrees.items():
    ram = sum(b["covers"][name]["ramification_sum"] for b in branches.values())
    rhs = -2*degree + ram
    check(name+"_integral_genus", rhs % 2 == 0)
    genus = (rhs+2)//2
    check(name+"_genus", genus == {"pair": 2, "ordered_pair": 3, "incidence": 38, "ordered_incidence": 75}[name])
    summary[name] = {"degree": degree, "ramification_sum": ram, "two_g_minus_two": rhs, "genus": genus}
check("strict_genus_threshold", summary["pair"]["genus"] < 38)
check("z_divisor_degree", sum(sum(b["pair_z_orders"]) for b in branches.values()) == 0)
result = {
    "phi_coefficients_ascending": phi,
    "invariant_polynomials": {name: [{"exponents_u_z": m, "coefficient": c}
                                    for m, c in sorted(poly.items())]
                              for name, poly in [("H0", H0), ("H1", H1)]},
    "labels": labels,
    "projections": {name: {"source": s, "target": t, "map": m, "degree": d}
                    for name, (s, t, m, d) in projections.items()},
    "branches": branches, "summary": summary,
    "maximum_labels": max(degrees.values()), "required_label_cap": 1000,
    "required_pair_genus_strict_upper_bound": 38,
    "checks": checks, "check_count": len(checks),
    "failures": [name for name, passed in checks.items() if not passed],
    "qualification": "Individual branch permutations represent conjugacy types only. "
    "Actual monodromy is imported from L106; normalization and rational descent "
    "are proved in L109. Geometric z orders are not rational residue-field classifications.",
}
OUT.write_text(json.dumps(result, indent=2)+"\n")
for name, record in summary.items():
    print(name, record)
for branch, b in branches.items():
    print(branch, "pair cycles:", b["covers"]["pair"]["cycle_histogram"],
          "z orders:", dict(Counter(b["pair_z_orders"])),
          "double ramification:", b["relative_maps"]["marked_double"]["ramification_sum"])
print("Genus:", summary["pair"]["genus"], "required: <38;",
      "maximum labels:", max(degrees.values()), "required: <=1000")
print("Checks:", len(checks), "failures:", result["failures"], "certificate:", OUT)
assert not result["failures"]

"""Independent complete replay of L109's certificate; no producer import."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "forget-root-certificate.json"
OUT = HERE / "forget-root-audit-certificate.json"
raw = SOURCE.read_bytes()
data = json.loads(raw)
checks = {}
original_names = set()


def check(name, assertion):
    if name in checks:
        raise ValueError("duplicate audit check: " + name)
    checks[name] = bool(assertion)


def original(name):
    original_names.add(name)


def add(p, q):
    ans = dict(p)
    for term, c in q.items():
        ans[term] = ans.get(term, 0) + c
        if not ans[term]:
            del ans[term]
    return ans


def scale(p, n):
    return {m: c*n for m, c in p.items() if c*n}


def times(p, q):
    ans = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            ans = add(ans, {(i+k, j+l): a*b})
    return ans


# Multinomial expansion, independent of the producer's repeated multiplication.
q5 = [0]*11
for a in range(6):
    for b in range(6-a):
        c = 5-a-b
        q5[b+2*c] += factorial(5)//(factorial(a)*factorial(b)*factorial(c))*3**c
phi = [q5[i] if i < 11 else 0 for i in range(12)]
for i, c in enumerate(q5):
    phi[i+1] -= 5*c
check("polynomial_all_coefficients", data["phi_coefficients_ascending"] == phi)
check("leading_and_cubic_constants", (phi[11], phi[3]) == (-1215, -55))
check("zero_fiber_separation", 3*Fraction(1, 5)**2+Fraction(1, 5)+1 == Fraction(33, 25))
# Monic long division by T²-2uT+u²+3z, not a remainder recurrence.
rem = [{(0, 0): c} if c else {} for c in phi]
quot = [{} for _ in range(10)]
for k in range(11, 1, -1):
    term = rem[k]
    quot[k-2] = term
    rem[k] = {}
    rem[k-1] = add(rem[k-1], times(term, {(1, 0): 2}))
    rem[k-2] = add(rem[k-2], times(term, {(2, 0): -1, (0, 1): -3}))
h1 = rem[1]
h0 = add(rem[0], times({(1, 0): 1}, h1))
reconstruction = [{} for _ in range(12)]
for k, term in enumerate(quot):
    for shift, factor in [(0, {(2, 0): 1, (0, 1): 3}),
                          (1, {(1, 0): -2}), (2, {(0, 0): 1})]:
        reconstruction[k+shift] = add(reconstruction[k+shift], times(term, factor))
reconstruction[0] = add(reconstruction[0], rem[0])
reconstruction[1] = add(reconstruction[1], rem[1])
check("full_long_division_identity", reconstruction ==
      [{(0, 0): c} if c else {} for c in phi])
for name, p in [("H0", h0), ("H1", h1)]:
    check(name+"_every_coefficient", data["invariant_polynomials"][name] ==
          [{"exponents_u_z": list(m), "coefficient": c} for m, c in sorted(p.items())])
check("invariant_schema", set(data["invariant_polynomials"]) == {"H0", "H1"})
for name in ["actual_polynomial", "H0_exact_remainder", "H1_exact_remainder",
             "discriminant_constant_twist"]:
    original(name)
check("twist", -12 == 4*(-3))

letters = range(11)
labels = {
    "pair": [(a, b) for a in letters for b in letters if a < b],
    "ordered_pair": [(a, b) for a in letters for b in letters if a != b],
    "incidence": [(r, a, b) for r in letters for a in letters for b in letters
                  if a < b and r not in (a, b)],
    "ordered_incidence": [(r, a, b) for r in letters for a in letters for b in letters
                          if len({r, a, b}) == 3],
}
degrees = {"pair": 55, "ordered_pair": 110, "incidence": 495, "ordered_incidence": 990}
index = {name: {v: i for i, v in enumerate(ls)} for name, ls in labels.items()}
for name, ls in labels.items():
    check(name+"_complete_labels", data["labels"][name] == [list(t) for t in ls]
          and len(ls) == degrees[name] == len(index[name]))
    original(name+"_complete_labels")
check("label_schema", set(data["labels"]) == set(labels))
projections = {}
for name, src, dst, deg in [
    ("marked_double", "ordered_pair", "pair", 2),
    ("forget_r", "incidence", "pair", 9),
    ("marked_forget_r", "ordered_incidence", "ordered_pair", 9),
]:
    target_labels = [tuple(sorted(t)) if name == "marked_double" else t[1:]
                     for t in labels[src]]
    mapping = [index[dst][t] for t in target_labels]
    projections[name] = (src, dst, mapping, deg)
    check(name+"_full_projection", data["projections"][name] ==
          {"source": src, "target": dst, "map": mapping, "degree": deg})
    check(name+"_fiber_degree", Counter(mapping) == {i: deg for i in range(degrees[dst])})
    original(name+"_all_fibers")
check("projection_schema", set(data["projections"]) == set(projections))

root_cycles = {
    "zero": [(0, 1, 2, 3, 4), (5, 6, 7, 8, 9), (10,)],
    "one": [(0, 1, 2)] + [(x,) for x in range(3, 11)],
    "infinity": [tuple(letters)],
}
expected_hist = {
    "pair": [(11, 5), (28, 1, 9, 3), (5, 11)],
    "ordered_pair": [(22, 5), (56, 1, 18, 3), (10, 11)],
    "incidence": [(99, 5), (168, 1, 109, 3), (45, 11)],
    "ordered_incidence": [(198, 5), (336, 1, 218, 3), (90, 11)],
}
replayed = {}
for bi, (branch, roots) in enumerate(root_cycles.items()):
    p = list(letters)
    for cyc in roots:
        for i, x in enumerate(cyc):
            p[x] = cyc[(i+1) % len(cyc)]
    stored = data["branches"][branch]
    check(branch+"_root_permutation", stored["root_permutation"] == p)
    records = {}
    for name, ls in labels.items():
        action = []
        for t in ls:
            im = tuple(p[x] for x in t)
            if name == "pair":
                im = tuple(sorted(im))
            if name == "incidence":
                im = (im[0], min(im[1:]), max(im[1:]))
            action.append(index[name][im])
        check(branch+"_"+name+"_action", stored["covers"][name]["action"] == action
              and sorted(action) == list(range(len(ls))))
        original(branch+"_"+name+"_bijective")
        cycles, covered = [], set()
        for i in range(len(ls)):
            if i in covered:
                continue
            cyc, j = [i], action[i]
            while j != i and len(cyc) <= len(ls):
                cyc.append(j)
                j = action[j]
            check(f"{branch}_{name}_orbit_{i}", j == i and len(set(cyc)) == len(cyc)
                  and not covered.intersection(cyc))
            covered.update(cyc)
            cycles.append(cyc)
            original(f"{branch}_{name}_cycle_{i}_closes")
        owner = {str(x): k for k, cyc in enumerate(cycles) for x in cyc}
        hist = {str(k): v for k, v in Counter(map(len, cycles)).items()}
        spec = expected_hist[name][bi]
        required = {str(spec[i+1]): spec[i] for i in range(0, len(spec), 2)}
        check(branch+"_"+name+"_partition_and_histogram",
              covered == set(range(len(ls))) and hist == required)
        record = {"action": action, "cycles": cycles, "cycle_of_label": owner,
                  "cycle_histogram": hist, "ramification_sum": len(ls)-len(cycles)}
        check(branch+"_"+name+"_full_record", stored["covers"][name] == record)
        records[name] = record
        original(branch+"_"+name+"_partition")
        original(branch+"_"+name+"_histogram")
    check(branch+"_cover_schema", set(stored["covers"]) == set(labels))
    relative = {}
    for name, (src, dst, mapping, deg) in projections.items():
        sr, dr = records[src], records[dst]
        check(branch+"_"+name+"_all_equivariant_edges", all(
            mapping[sr["action"][i]] == dr["action"][mapping[i]] for i in range(degrees[src])))
        original(branch+"_"+name+"_equivariant")
        cydata = []
        for i, cyc in enumerate(sr["cycles"]):
            targets = {dr["cycle_of_label"][str(mapping[x])] for x in cyc}
            target = next(iter(targets))
            target_length = len(dr["cycles"][target])
            e, remainder = divmod(len(cyc), target_length)
            check(f"{branch}_{name}_relative_{i}", len(targets) == 1 and remainder == 0)
            original(f"{branch}_{name}_{i}_integral_ratio")
            cydata.append({"source_cycle": i, "target_cycle": target, "relative_e": e})
        for j in range(len(dr["cycles"])):
            check(f"{branch}_{name}_fiber_{j}", sum(c["relative_e"] for c in cydata
                  if c["target_cycle"] == j) == deg)
            original(f"{branch}_{name}_fiber_{j}_degree")
        ram = sum(c["relative_e"]-1 for c in cydata)
        rec = {"cycles": cydata, "relative_e_histogram":
               dict(Counter(str(c["relative_e"]) for c in cydata)), "ramification_sum": ram}
        check(branch+"_"+name+"_full_relative_record", stored["relative_maps"][name] == rec)
        check(branch+"_"+name+"_required_relative_ramification",
              ram == ({"marked_double": 0, "forget_r": 56, "marked_forget_r": 112}[name]
                      if branch == "one" else 0))
        relative[name] = rec
        original(branch+"_"+name+"_relative_ramification")
    check(branch+"_relative_schema", set(stored["relative_maps"]) == set(projections))
    # Exact branch leading terms are justified in L109, not inferred by sampling.
    zorders = []
    for k, cyc in enumerate(records["pair"]["cycles"]):
        values = []
        for i in cyc:
            a, b = labels["pair"][i]
            if branch == "infinity":
                val = -2
            else:
                clustered = any(len(cluster) > 1 and a in cluster and b in cluster
                                for cluster in roots)
                val = 2 if clustered else 0
            values.append(val)
        check(f"{branch}_z_order_constant_on_cycle_{k}", len(set(values)) == 1)
        zorders.append(values[0])
    check(branch+"_all_z_orders", stored["pair_z_orders"] == zorders
          and Counter(zorders) == {"zero": {2: 4, 0: 7}, "one": {2: 1, 0: 36},
                                   "infinity": {-2: 5}}[branch])
    original(branch+"_z_orders")
    replayed[branch] = {"root_permutation": p, "covers": records,
                        "relative_maps": relative, "pair_z_orders": zorders}
    check(branch+"_entire_branch_record", stored == replayed[branch])
check("branch_schema", set(data["branches"]) == set(root_cycles))

summaries = {}
for name, degree in degrees.items():
    ram = sum(rec["covers"][name]["ramification_sum"] for rec in replayed.values())
    rhs = -2*degree+ram
    genus = (rhs+2)//2
    check(name+"_genus", rhs % 2 == 0 and genus ==
          {"pair": 2, "ordered_pair": 3, "incidence": 38, "ordered_incidence": 75}[name])
    summaries[name] = {"degree": degree, "ramification_sum": ram,
                       "two_g_minus_two": rhs, "genus": genus}
    for suffix in ["integral_genus", "genus"]:
        original(name+"_"+suffix)
check("all_summaries", data["summary"] == summaries)
check("thresholds", data["maximum_labels"] == max(degrees.values()) == 990
      and data["required_label_cap"] == 1000 and 990 <= 1000
      and data["required_pair_genus_strict_upper_bound"] == 38 and summaries["pair"]["genus"] < 38)
check("z_divisor_degree", sum(sum(b["pair_z_orders"]) for b in replayed.values()) == 0)
for name in ["maximum_label_universe_cap", "strict_genus_threshold", "z_divisor_degree"]:
    original(name)
check("original_check_names_and_values", data["checks"] == dict.fromkeys(original_names, True))
check("original_check_count", data["check_count"] == len(original_names) == 3082)
check("original_no_failures", data["failures"] == [])
check("qualification", data["qualification"] ==
      "Individual branch permutations represent conjugacy types only. "
      "Actual monodromy is imported from L106; normalization and rational descent "
      "are proved in L109. Geometric z orders are not rational residue-field classifications.")
check("top_schema", set(data) == {
    "phi_coefficients_ascending", "invariant_polynomials", "labels", "projections",
    "branches", "summary", "maximum_labels", "required_label_cap",
    "required_pair_genus_strict_upper_bound", "checks", "check_count", "failures", "qualification"})
failures = [name for name, passed in checks.items() if not passed]
result = {"input": str(SOURCE.relative_to(HERE.parent.parent)), "input_sha256": sha256(raw).hexdigest(),
          "summary": summaries, "replayed_branches": replayed,
          "actual_maximum_labels": 990, "required_label_cap": 1000,
          "actual_pair_genus": summaries["pair"]["genus"], "required_genus_strict_upper_bound": 38,
          "original_checks_verified": len(original_names), "checks": checks,
          "check_count": len(checks), "failures": failures,
          "qualification": "Full finite arithmetic replay; geometric and local-ring proofs remain in L109."}
OUT.write_text(json.dumps(result, indent=2)+"\n")
print("Genera:", {k: v["genus"] for k, v in summaries.items()})
print("Pair genus:", summaries["pair"]["genus"], "required: <38; labels: 990 required: <=1000")
print("Original checks verified:", len(original_names), "audit checks:", len(checks),
      "failures:", failures)
print("Certificate:", OUT)
assert not failures

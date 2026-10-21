"""Independent full-record audit of L108's finite evidence.

No producer imports. Formal normalization and descent remain in L108.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
source = HERE / "rational-boundary-certificate.json"
raw = source.read_bytes()
c = json.loads(raw)
checks, producer = {}, {}


def check(name, value):
    checks[name] = bool(value)


def old(name, value):
    producer[name] = bool(value)


# Multinomial coefficient formula, independent of producer convolution.
q5 = [0] * 11
for i in range(6):
    for j in range(6-i):
        q5[2*i+j] += factorial(5)//(
            factorial(i)*factorial(j)*factorial(5-i-j))*3**i
phi = [(q5[k] if k < 11 else 0) -
       (5*q5[k-1] if k else 0) for k in range(12)]
h = [-x for x in phi[3:]]
check("all_phi_coefficients", c["phi_ascending"] == phi)
check("all_h_coefficients", c["h_ascending"] == h)
old("phi_minus_one_is_minus_T_cubed_h",
    c["phi_ascending"] == [1, 0, 0]+[-x for x in c["h_ascending"]])
old("octic_Eisenstein_eleven",
    all(x % 11 == 0 for x in h[:-1]) and h[-1] % 11 != 0
    and h[0] % 121 != 0)
check("simple_scaled_one_roots", phi[:4] == [1, 0, 0, -55])
check("simple_scaled_infinity_roots", phi[-1] == -1215)

# Q(d), d^2=-11 arithmetic and exact valuation, not decimal roots.
norm = 11**2 + 11*5**2
v3, unit = 0, norm
while unit % 3 == 0:
    v3 += 1
    unit //= 3
old("zero_slope_numerator_norm", norm == 396)
old("zero_slope_norm_v3_exactly_two", v3 == 2)
old("zero_split_prime_simple", (1+11) % 3 == 0 and 2 % 3 != 0)
old("zero_numerator_zero_denominator_unit_at_d_one",
    (11-5) % 3 == 0 and (11+5) % 3 != 0)
check("all_zero_slope_record", c["zero_slope"] == {
    "E": "Q(d), d^2=-11", "C": "-(11-5d)/(11+5d)",
    "v_at_split_three_d_one": v3,
    "required_for_fifth_power": "multiple of 5"})
check("zero_valuation_fails_required_divisibility", v3 % 5 != 0)
# zeta^2+zeta+1=0: (zeta-zeta^2)^2=(1+2*zeta)^2=-3.
diff_square = (1-4, 4-4)
eta = -Fraction(diff_square[0], 12)
old("one_normalized_unit", eta == Fraction(1, 4) and diff_square[1] == 0)
check("full_normalized_unit", c["one_normalized_eta"] == str(eta))
check("normalized_unit_nonzero_square", eta == Fraction(1, 2)**2)

labels = {(r, a, b) for r in range(11) for a in range(11)
          for b in range(a+1, 11) if r != a and r != b}
old("label_cap", len(labels) == 495 <= 1000)


def move(label, k, fiber):
    def root(t):
        if fiber == "zero":
            return t if t == 10 else 5*(t//5)+(t+k) % 5
        return (t+k) % 3 if t < 3 else t
    r, a, b = map(root, label)
    return (r, min(a, b), max(a, b))


def category(label, fiber):
    r, a, b = label
    if fiber == "one":
        return ("r_zero_" if r < 3 else "r_simple_") + \
            str(sum(t < 3 for t in (a, b))) + "_pair_zero"
    if r == 10:
        return "r_gamma_pair_" + (
            "same_cluster" if a//5 == b//5 else "mixed_clusters")
    # The pair is sorted, so gamma, when present, is b.
    if b == 10:
        return "r_cluster_pair_gamma_" + ("same" if a//5 == r//5 else "other")
    n_same = sum(t//5 == r//5 for t in (a, b))
    return {2: "all_same_cluster", 0: "r_cluster_pair_other_cluster",
            1: "r_cluster_pair_same_and_other"}[n_same]


expected_counts = {
    "zero": {
        "r_gamma_pair_same_cluster": 4, "r_gamma_pair_mixed_clusters": 5,
        "r_cluster_pair_gamma_same": 8, "r_cluster_pair_gamma_other": 10,
        "all_same_cluster": 12, "r_cluster_pair_other_cluster": 20,
        "r_cluster_pair_same_and_other": 40},
    "one": {
        "r_simple_0_pair_zero": 168, "r_simple_1_pair_zero": 56,
        "r_simple_2_pair_zero": 8, "r_zero_0_pair_zero": 28,
        "r_zero_1_pair_zero": 16, "r_zero_2_pair_zero": 1}}
recomputed = {}
for fiber, order in (("zero", 5), ("one", 3)):
    records, seen, rebuilt = c[fiber+"_branches"], [], []
    counts, indices, starts = Counter(), Counter(), []
    for n, row in enumerate(records):
        prefix = f"{fiber}_{n}"
        check(prefix+"_schema", set(row) == {"labels", "e", "category"})
        stored = [tuple(t) for t in row["labels"]]
        start = stored[0]
        # Order divides prime 3 or 5, so only orbit lengths 1 and order occur.
        e = 1 if move(start, 1, fiber) == start else order
        orbit = [move(start, k, fiber) for k in range(e)]
        cat = category(start, fiber)
        check(prefix+"_entire_cycle", stored == orbit)
        check(prefix+"_valid_labels", all(t in labels for t in stored))
        check(prefix+"_canonical_start", start == min(orbit))
        check(prefix+"_length", row["e"] == e)
        check(prefix+"_category", row["category"] == cat)
        old("cycle_closes_"+str(start)+"_category_"+fiber,
            move(start, e, fiber) == start)
        old("category_constant_"+str(start)+"_category_"+fiber,
            {category(t, fiber) for t in orbit} == {cat})
        seen.extend(stored)
        starts.append(start)
        counts[cat] += 1
        indices[e] += 1
        rebuilt.append({"labels": [list(t) for t in orbit],
                        "e": e, "category": cat})
    check(fiber+"_all_495_labels_once", Counter(seen) == Counter({t: 1 for t in labels}))
    check(fiber+"_canonical_record_order", starts == sorted(starts))
    check(fiber+"_complete_count_record", c[fiber+"_counts"] == dict(counts))
    old(fiber+"_category_counts", dict(counts) == expected_counts[fiber])
    old("weighted_degree_"+fiber, sum(e*n for e, n in indices.items()) == 495)
    if fiber == "zero":
        old("zero_99_index_five", indices == {5: 99})
    else:
        old("one_indices", indices == {1: 168, 3: 109})
    recomputed[fiber] = rebuilt

# Exhaustively derive inertia orbits at infinity from ALL 495 labels,
# and identify their normalized difference pairs. This checks the scale
# removal combinatorially, in addition to testing the 45-pair action.
relative_pairs = Counter()
for r, a, b in labels:
    pair = tuple(sorted(((a-r) % 11, (b-r) % 11)))
    relative_pairs[pair] += 1
all_pairs = {(i, j) for i in range(1, 11) for j in range(i+1, 11)}
check("infinity_all_translation_orbits", relative_pairs == Counter({p: 11 for p in all_pairs}))
arithmetic_orbits = {
    tuple(sorted({tuple(sorted((m*i % 11, m*j % 11)))
                  for m in range(1, 11)})) for i, j in all_pairs}
infinity = []
seen = set()
for orbit in sorted(arithmetic_orbits):
    i, j = orbit[0]
    # Stabilizer via the sum AND product of roots represented in Q[zeta_11].
    # Reduce zeta^10=-(1+zeta+...+zeta^9) exactly.
    def zeta_power(k):
        k %= 11
        return tuple(-1 if k == 10 else int(t == k) for t in range(10))

    def symmetric(m):
        x, y = zeta_power(m*i), zeta_power(m*j)
        return tuple(a+b for a, b in zip(x, y)), zeta_power(m*(i+j))

    stab = [m for m in range(1, 11) if symmetric(m) == symmetric(1)]
    check(f"infinity_{i}_{j}_leading_pair_stabilizer",
          stab == [m for m in range(1, 11)
                   if sorted((m*i % 11, m*j % 11)) == [i, j]])
    check(f"infinity_{i}_{j}_orbit_stabilizer", len(stab)*len(orbit) == 10)
    old("infinity_orbit_disjoint_"+str((i, j)), not seen.intersection(orbit))
    seen.update(orbit)
    infinity.append({"representative": [i, j],
                     "orbit": [list(p) for p in orbit],
                     "stabilizer": stab, "residue_degree": len(orbit), "e": 11})
check("all_infinity_records", c["infinity_arithmetic_orbits"] == infinity)
check("infinity_full_pair_coverage", seen == all_pairs)
degrees = sorted(row["residue_degree"] for row in infinity)
old("infinity_residue_degrees", degrees == [5, 10, 10, 10, 10])
old("infinity_weighted_degree", sum(11*d for d in degrees) == 495)
old("infinity_stabilizers",
    all(row["stabilizer"] == ([1, 10] if sum(row["representative"]) == 11 else [1])
        for row in infinity))
old("infinity_no_rational_residue_point", all(d > 1 for d in degrees))

check("entire_original_check_map", c["checks"] == producer)
check("original_all_checks_true", len(producer) == 775 and all(producer.values()))
check("original_failure_list", c["failures"] == [n for n, v in producer.items() if not v])
check("honest_incomplete_field_flag", c["nonrational_field_decomposition_complete"] is False)
check("scope", c["scope"] == "L108 rational boundary selection; nonrational field splitting incomplete")
check("complete_schema", set(c) == {
    "scope", "phi_ascending", "h_ascending", "zero_slope", "one_normalized_eta",
    "zero_branches", "one_branches", "zero_counts", "one_counts",
    "infinity_arithmetic_orbits", "nonrational_field_decomposition_complete",
    "checks", "failures"})
failures = [n for n, v in checks.items() if not v]
out = HERE / "rational-boundary-audit-certificate.json"
report = {
    "scope": "Complete finite replay; formal proof audited in canonical L108",
    "input_sha256": sha256(raw).hexdigest(),
    "producer_sha256": sha256((HERE / "rational_boundary.py").read_bytes()).hexdigest(),
    "original_checks_recomputed": producer,
    "recomputed_phi": phi, "recomputed_h": h,
    "recomputed_branches": recomputed, "recomputed_infinity": infinity,
    "actual_label_count": len(labels), "required_label_cap": 1000,
    "actual_weighted_degrees": [
        sum(row["e"] for row in recomputed["zero"]),
        sum(row["e"] for row in recomputed["one"]), sum(11*d for d in degrees)],
    "required_weighted_degree": 495,
    "zero_valuation": v3, "required_fifth_power_valuation_modulus": 5,
    "normalized_unit": str(eta), "infinity_residue_degrees": degrees,
    "nonrational_field_decomposition_complete": False,
    "check_count": len(checks), "checks": checks, "failures": failures}
out.write_text(json.dumps(report, indent=2)+"\n")
print(f"{sum(checks.values())}/{len(checks)} audit checks; original {len(producer)} checks fully recomputed.")
print("Labels 495 <= cap 1000; actual/required weighted degrees 495/495 at each of three fibers.")
print(f"Zero valuation {v3}, required divisible by 5; normalized unit {eta}; infinity degrees {degrees}.")
print(f"Failures: {failures}")
print("Full certificate:", out.relative_to(Path.cwd()))
if failures:
    raise SystemExit(1)

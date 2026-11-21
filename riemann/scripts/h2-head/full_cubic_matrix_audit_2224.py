"""Audit frozen C919l by exact interval polynomial arithmetic.

Reads but never imports, executes or overwrites generator/certificate2222.
The analytic all-box/all-shift justification is canonical in C919l.
"""

from decimal import Decimal, localcontext
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import platform

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "full_cubic_matrix_2222.json"
GENERATOR = BASE / "full_cubic_matrix_2222.py"
saved = json.loads(SOURCE.read_text())
source_hash = sha256(SOURCE.read_bytes()).hexdigest()
generator_hash = sha256(GENERATOR.read_bytes()).hexdigest()
checks, comparisons = {}, {}


def check(name, predicate):
    checks[name] = bool(predicate)


def pack(value):
    value = Q(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def at(pointer):
    node = saved
    for key in pointer.strip("/").split("/"):
        node = node[int(key)] if isinstance(node, list) else node[key]
    return node


def compare(pointer, expected):
    raw = at(pointer)
    observed = Q(int(raw["numerator"]), int(raw["denominator"]))
    passed = int(raw["denominator"]) > 0 and observed == expected
    comparisons[pointer] = {
        "saved": pack(observed), "independent": pack(expected),
        "positive_denominator": int(raw["denominator"]) > 0, "matches": passed}
    check("exact:" + pointer, passed)


# Closed rational interval operations. Repeated variables are allowed:
# ignoring their correlations enlarges an enclosure and remains safe.
def add(left, right):
    return left[0] + right[0], left[1] + right[1]


def multiply(left, right):
    values = [x*y for x in left for y in right]
    return min(values), max(values)


def reciprocal(interval):
    low, high = interval
    assert low <= high and low*high > 0
    return 1/high, 1/low


def subtract(left, right):
    return left[0] - right[1], left[1] - right[0]


def encode_interval(interval):
    return [pack(v) for v in interval]


# Derive transformed endpoints directly from integer spatial fractions.
spatial = [((14, 1), (29, 2)), ((41, 2), (43, 2)),
           ((49, 2), (51, 2)), ((100, 1), (200, 1))]
y = []
for j, (lower, upper) in enumerate(spatial):
    for side, point in enumerate((lower, upper)):
        compare(f"/box_evidence/x/{j}/{side}", Q(*point))
    lo = Q(200 * upper[1]**2, upper[0]**2)
    hi = Q(200 * lower[1]**2, lower[0]**2)
    y.append((lo, hi))
    compare(f"/box_evidence/y/{j}/0", lo)
    compare(f"/box_evidence/y/{j}/1", hi)
    check(f"positive_interval_{j+1}", 0 < lo <= hi)

gaps = {}
for j in range(4):
    for k in range(j+1, 4):
        difference = subtract(y[j], y[k])
        gaps[j, k] = difference[0]
        compare(f"/box_evidence/gaps/{j+1}-{k+1}", difference[0])
        check(f"strict_order_{j+1}_{k+1}", difference[0] > 0)

rows, B = [], Q(0)
for j in range(4):
    other = [k for k in range(4) if k != j]
    prefix = f"/inverse_rows/{j}"
    check(prefix + ":node", at(prefix + "/node") == j+1)
    check(prefix + ":other_nodes", at(prefix + "/other_nodes") == [k+1 for k in other])
    # Construct prod_(k!=j)(t-y_k) with interval coefficients, in
    # increasing degree order, rather than enumerating symmetric sums.
    polynomial = [(Q(1), Q(1))]
    denominator = (y[j][0]**5, y[j][1]**5)
    compare(prefix + "/y_lower_fifth", denominator[0])
    for index, k in enumerate(other):
        new = [(Q(0), Q(0)) for _ in range(len(polynomial)+1)]
        minus_node = (-y[k][1], -y[k][0])
        for m, coefficient in enumerate(polynomial):
            new[m] = add(new[m], multiply(coefficient, minus_node))
            new[m+1] = add(new[m+1], coefficient)
        polynomial = new
        factor = subtract(y[j], y[k])
        check(prefix + f":separated_from_{k+1}", factor[0]*factor[1] > 0)
        gap = min(abs(factor[0]), abs(factor[1]))
        compare(prefix + f"/gap_lower_factors/{index}", gap)
        denominator = multiply(denominator, factor)
    denominator_min = min(abs(v) for v in denominator)
    compare(prefix + "/denominator_lower", denominator_min)
    # U=V diag((y/200)^5), hence the signed product denominator /200^5.
    weighted_denominator = tuple(v/Q(200**5) for v in denominator)
    intervals = [multiply(coefficient, reciprocal(weighted_denominator))
                 for coefficient in polynomial]
    magnitudes = []
    for m, (coefficient, interval) in enumerate(zip(polynomial, intervals)):
        numerator_upper = Q(200**5) * max(abs(v) for v in coefficient)
        upper = max(abs(v) for v in interval)
        magnitudes.append(upper)
        compare(prefix + f"/numerator_absolute_uppers/{m}", numerator_upper)
        compare(prefix + f"/inverse_entry_absolute_uppers/{m}", upper)
        check(prefix + f":strict_entry_sign_{m}", interval[0]*interval[1] > 0)
        enclosing = (Q(0), upper) if interval[0] > 0 else (-upper, Q(0))
        for side in (0, 1):
            compare(prefix + f"/inverse_entry_signed_enclosures/{m}/{side}", enclosing[side])
        check(prefix + f":inclusion_{m}", enclosing[0] <= interval[0] <= interval[1] <= enclosing[1])
    row_square = sum((v*v for v in magnitudes), Q(0))
    compare(prefix + "/row_square_upper", row_square)
    B += row_square
    rows.append({"node": j+1, "polynomial_coefficients": [encode_interval(v) for v in polynomial],
                 "signed_denominator": encode_interval(denominator),
                 "weighted_signed_denominator": encode_interval(weighted_denominator),
                 "inverse_inclusions": [encode_interval(v) for v in intervals],
                 "absolute_uppers": [pack(v) for v in magnitudes],
                 "row_square": pack(row_square)})

# Reconstruct the tail as a geometric vector factor times 1018/1000^19.
ratio_component = Q(1, 25000000)
components = [Q(1)]
for _ in range(3):
    components.append(components[-1] * ratio_component)
for i, component in enumerate(components):
    compare(f"/comparison/tail_components/{i}", component)
C = sum(components, Q(0))
head, tail = 1/B, C * Q(1018, 1000**19)
cross = head.numerator * tail.denominator - tail.numerator * head.denominator
fields = {
    "/comparison/B": B, "/comparison/head_lower_r4": head,
    "/comparison/tail_vector_factor": C,
    "/comparison/first_shell": Q(1, 1000**19),
    "/comparison/integral": Q(1, 18 * 1000**18),
    "/comparison/tail_upper_r4": tail,
    "/comparison/required_head_minus_tail": Q(0),
    "/comparison/actual_head_minus_tail": head-tail,
    "/comparison/head_over_tail": head/tail,
    "/all_r/head_step": Q(1, 200**4),
    "/all_r/tail_step": Q(1, 1000**4),
    "/all_r/relative_step": Q(200**4, 1000**4)}
for pointer, expected in fields.items():
    compare(pointer, expected)
check("strict_cross_product", at("/comparison/strict_cross_product") == str(cross) and cross > 0)
check("strict_head_exceeds_tail", head > tail > 0)
check("every_shift_relative_factor", fields["/all_r/relative_step"] == Q(1, 625) < 1)
check("frozen_parameters", saved["parameters"] == {
    "scale": 200, "onset": 4, "cutoff": 1000,
    "D": [1, 200, 40000, 8000000], "subdivisions": 0})
check("target", saved["target"] == "H_(3,r)>0 for every integer r>=4")
check("assessment", saved["assessment"] == "drafts/literature/2026-11-21-full-cubic-matrix-test-2221.md")
check("array_dimensions", len(saved["inverse_rows"]) == 4
      and len(saved["box_evidence"]["x"]) == len(saved["box_evidence"]["y"]) == 4
      and len(saved["box_evidence"]["gaps"]) == 6
      and len(saved["comparison"]["tail_components"]) == 4
      and all(len(row[key]) == 4 for row in saved["inverse_rows"] for key in
              ["numerator_absolute_uppers", "inverse_entry_absolute_uppers",
               "inverse_entry_signed_enclosures"]))
original_checks = {
    "frozen_parameters": True,
    "all_four_intervals_positive": all(0 < lo <= hi for lo, hi in y),
    "all_six_gaps_positive": len(gaps) == 6 and min(gaps.values()) > 0,
    "all_sixteen_inverse_bounds_positive": all(
        int(value["numerator"]) > 0 for row in rows for value in row["absolute_uppers"]),
    "head_and_tail_positive": head > 0 and tail > 0,
    "strict_onset_margin": head > tail,
    "all_r_relative_step": Q(200**4, 1000**4) == Q(1, 625) < 1}
check("all_original_booleans_reconstructed", saved["checks"] == original_checks)
check("original_failures_empty", saved["failures"] == [])

# Ensure no saved rational operand has silently escaped comparison.
def rational_pointers(node, path=""):
    if isinstance(node, dict):
        if set(node) == {"numerator", "denominator"}:
            return {path}
        answer = set()
        for key, value in node.items():
            answer |= rational_pointers(value, path + "/" + key)
        return answer
    if isinstance(node, list):
        answer = set()
        for i, value in enumerate(node):
            answer |= rational_pointers(value, path + "/" + str(i))
        return answer
    return set()


check("every_rational_operand_compared", rational_pointers(saved) == set(comparisons))
check("original_certificate_unchanged", sha256(SOURCE.read_bytes()).hexdigest() == source_hash)
check("original_generator_unchanged", sha256(GENERATOR.read_bytes()).hexdigest() == generator_hash)
failures = [name for name, passed in checks.items() if not passed]
report = {
    "assessment": "drafts/literature/2026-11-21-full-cubic-matrix-audit-2222.md",
    "method": "Exact signed interval polynomial multiplication; no original-generator execution",
    "arithmetic": {"implementation": platform.python_implementation(), "version": platform.python_version(),
                   "trust": "correct integer/Fraction arithmetic; Decimal displays only"},
    "original_hashes": {"certificate_sha256": source_hash, "generator_sha256": generator_hash},
    "inverse_rows": rows, "comparisons": comparisons,
    "bounds": {"h4": pack(head), "t4": pack(tail), "actual_margin": pack(head-tail),
               "required_margin": pack(0), "ratio": pack(head/tail), "cross_product": str(cross),
               "head_step": pack(Q(1, 200**4)), "tail_step": pack(Q(1, 1000**4)),
               "relative_step": pack(Q(1, 625))},
    "checks": checks, "failures": failures,
    "summary": {"rational_operands": len(comparisons), "inverse_inclusions": 16,
                "checks": len(checks), "passed": sum(checks.values()), "failures": failures},
    "limits": "Finite certificate audit only; analytic proof is in C919l, source computations and backend correctness are imported."}
destination = BASE / "full_cubic_matrix_audit_2224.json"
destination.write_text(json.dumps(report, indent=2) + "\n")
with localcontext() as context:
    context.prec = 18
    dec = lambda value: str(Decimal(value.numerator)/Decimal(value.denominator))
    print(f"result={'PASS' if not failures else 'FAIL'}; checks={len(checks)}; rational_operands={len(comparisons)}; inverse_inclusions=16")
    print(f"h4={dec(head)}; t4={dec(tail)}; actual_margin={dec(head-tail)}; required>0; h4/t4={dec(head/tail)}")
print(f"all-r relative factor=1/625; failures={failures}")
print(f"certificate={destination.relative_to(Path.cwd())}")
if failures:
    raise SystemExit(1)

"""Independent integer/rational reconstruction of the frozen C919k bounds.

Reads, but never imports, runs or overwrites, the original 2217 evidence.
The analytic occurrence, source and all-r arguments remain in C919k.
"""

from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


BASE = Path(__file__).resolve().parent
ORIGINAL = BASE / "counted_survivor_cubic_2217.json"
GENERATOR = BASE / "counted_survivor_cubic_2217.py"
saved = json.loads(ORIGINAL.read_text())
original_hash = sha256(ORIGINAL.read_bytes()).hexdigest()
generator_hash = sha256(GENERATOR.read_bytes()).hexdigest()
checks = {}
comparisons = {}


def check(name, assertion):
    checks[name] = bool(assertion)


def encode(x):
    x = Fraction(x)
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def at(pointer):
    node = saved
    for key in pointer.strip("/").split("/"):
        node = node[int(key)] if isinstance(node, list) else node[key]
    return node


def compare(pointer, expected):
    field = at(pointer)
    numerator = int(field["numerator"])
    denominator = int(field["denominator"])
    actual = Fraction(numerator, denominator)
    expected = Fraction(expected)
    passed = denominator > 0 and actual == expected
    comparisons[pointer] = {"saved": encode(actual), "independent": encode(expected),
                            "saved_denominator_positive": denominator > 0,
                            "matches": passed}
    check("exact:" + pointer, passed)


# Direct common-denominator formulas from endpoints, independent of the
# original negative-power/product implementation. Endpoints are p/q.
lower_pairs = [(14, 1), (41, 2), (49, 2)]
upper_pairs = [(29, 2), (43, 2), (51, 2)]
gaps = [Fraction(10000*q*q - p*p, 10000*p*p) for p, q in upper_pairs]
outside = [Fraction(1000000*q*q + p*p, 1000000*p*p) for p, q in lower_pairs]
g = gaps[0] * gaps[1] * gaps[2]
a = outside[0] * outside[1] * outside[2]

# 18*(1000^-19 + 1000^-18/18) = 1018/1000^19.
shell = Fraction(1018, 18 * 1000**19)
head = Fraction(g.numerator**2, 200**20 * g.denominator**2)
tail = Fraction(1018 * a.numerator**2, 1000**19 * a.denominator**2)
margin = head - tail
ratio = Fraction(head.numerator * tail.denominator,
                 head.denominator * tail.numerator)
cross = head.numerator * tail.denominator - tail.numerator * head.denominator
ratio_threshold_cross = (head.numerator * tail.denominator
                         - 10000000 * tail.numerator * head.denominator)
endpoint_error = Fraction(10076*6 + 24460*2 + 808344, 100000)
count_main = Fraction(350, 11)
count_strict = count_main - 2 * endpoint_error
integer_count = count_strict.numerator // count_strict.denominator + 1
head_step = Fraction(1, 200**4)
tail_step = Fraction(1, 1000**4)
relative_step = Fraction(200**4, 1000**4)

fields = {
    "/count/strict_main_lower": count_main,
    "/count/strict_error_upper_per_endpoint": endpoint_error,
    "/count/strict_count_lower": count_strict,
    "/bounds/gap_product": g,
    "/bounds/exterior_product": a,
    "/bounds/complete_shell_series_upper": shell,
    "/bounds/head_lower_at_4": head,
    "/bounds/tail_upper_at_4": tail,
    "/bounds/strict_margin_at_4": margin,
    "/bounds/head_tail_ratio": ratio,
    "/all_r/head_extra_shift_lower": head_step,
    "/all_r/tail_extra_shift_upper": tail_step,
    "/all_r/relative_extra_shift_upper": relative_step,
}
for i in range(3):
    fields[f"/bounds/survivor_gaps/{i}"] = gaps[i]
    fields[f"/bounds/exterior_factors/{i}"] = outside[i]
    for j, pairs in enumerate([lower_pairs, upper_pairs]):
        fields[f"/frozen_parameters/boxes/{i}/{j}"] = Fraction(*pairs[i])
for pointer, expected in fields.items():
    compare(pointer, expected)

check("frozen_onset_four", at("/frozen_parameters/onset") == 4)
check("frozen_band", at("/frozen_parameters/surviving_band") == "(100,200]")
check("frozen_cutoff", at("/frozen_parameters/complete_real_head_cutoff") == 1000)
check("box_count_three", len(at("/frozen_parameters/boxes")) == 3)
check("gap_factor_count_three", len(at("/bounds/survivor_gaps")) == 3)
check("exterior_factor_count_three", len(at("/bounds/exterior_factors")) == 3)
check("count_integer_matches", at("/count/integer_count_lower") == integer_count)
check("count_requirement_one", at("/count/required_count") == 1)
check("saved_cross_matches", int(at("/bounds/comparison_cross_product")) == cross)
check("count_strict_fraction", count_strict == Fraction(185127, 13750))
check("count_integer_is_fourteen", integer_count == 14)
check("head_exponent_is_twenty", 2 * (2 * 4 + 2) == 20)
check("tail_shell_integral_identity", shell == Fraction(1, 1000**19) + Fraction(1, 18*1000**18))
check("tail_assembled_identity", tail == 18 * a*a * shell)
check("strict_margin_positive", margin > 0 and cross > 0)
check("ratio_exceeds_ten_million_by_integer_comparison", ratio_threshold_cross > 0)
check("extra_shift_base_one_over_625", relative_step == Fraction(1, 625))
check("extra_shift_base_less_than_one", 0 < relative_step < 1)
check("finite_reality_covers_head", 1000 < 30610046000)

# Re-evaluate each original Boolean from the independent quantities.
lower = [Fraction(*x) for x in lower_pairs]
upper = [Fraction(*x) for x in upper_pairs]
original_checks = {
    "exp6_lower_exceeds_200": 8**6 > 200 * 3**6,
    "exp2_lower_exceeds_6": 8**2 > 6 * 3**2,
    "exp2_upper_below_log_argument_lower": 9 * 44 < 700,
    "error_per_endpoint_is_9_17720": endpoint_error == Fraction(22943, 2500),
    "strict_count_exceeds_13": count_strict > 13,
    "integer_count_lower_is_14": integer_count == 14,
    "cancelled_boxes_disjoint_below_surviving_band":
        0 < lower[0] < upper[0] < lower[1] < upper[1] < lower[2] < upper[2] < 100,
    "all_survivor_gaps_positive": min(gaps) > 0,
    "head_positive": head > 0,
    "tail_positive": tail > 0,
    "strict_head_tail_margin": margin > 0 and cross > 0,
    "head_tail_ratio_exceeds_ten_million": ratio_threshold_cross > 0,
    "relative_shift_is_1_over_625": relative_step == Fraction(1, 625),
    "relative_shift_strictly_between_zero_and_one": 0 < relative_step < 1,
}
check("original_check_names_complete", set(saved["checks"]) == set(original_checks))
for name, result in original_checks.items():
    check("original_check_recomputed:" + name, result and saved["checks"][name] is True)
check("original_failures_empty", saved["failures"] == [])
check("original_certificate_unchanged", sha256(ORIGINAL.read_bytes()).hexdigest() == original_hash)
check("original_generator_unchanged", sha256(GENERATOR.read_bytes()).hexdigest() == generator_hash)

failures = [name for name, passed in checks.items() if not passed]
report = {
    "step": "2219", "task": "proof_audit", "classification": "REPRODUCTION",
    "original_certificate_sha256": original_hash,
    "original_generator_sha256": generator_hash,
    "comparison_count": len(comparisons), "comparisons": comparisons,
    "integer_count_lower": integer_count, "required_count": 1,
    "comparison_cross_product": str(cross),
    "ratio_minus_ten_million_cross_product": str(ratio_threshold_cross),
    "original_checks_recomputed": original_checks,
    "checks": checks, "failures": failures,
    "analytic_scope": "C919k audit2219 proves complete occurrence/tail accounting and every integer r>=4; no finite sampling substitutes for that proof.",
    "qualifications": ["Correct integer/Fraction arithmetic assumed.",
                       "Platt/Bellotti-Wong source computations remain imported.",
                       "C919f's separate Decimal/libmpdec contract remains.",
                       "No arbitrary-degree, unshifted or RH conclusion."]
}
output = BASE / "counted_survivor_cubic_audit_2219.json"
output.write_text(json.dumps(report, indent=2) + "\n")
with localcontext() as context:
    context.prec = 20
    def display(x):
        return Decimal(x.numerator) / Decimal(x.denominator)
    print(f"count >= {integer_count}; required >= 1")
    print(f"head lower {display(head)}; full exterior upper {display(tail)}")
    print(f"margin {display(margin)}; required > 0")
    print(f"head/tail {display(ratio)}; required > 1; stronger bound > 10000000")
print(f"relative extra-shift factor {relative_step}; required < 1")
print(f"exact rational fields {len(comparisons)}; checks {sum(checks.values())}/{len(checks)}; failures {failures}")
print(f"certificate: {output}")
raise SystemExit(bool(failures))

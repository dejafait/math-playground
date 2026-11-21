#!/usr/bin/env python3
"""Independently check all exact fields of the C048h scalar certificate.

No producer import: exponential sums use powers/factorials, and square
roots are verified by squared rational grid inequalities, not isqrt.
Analytic hypotheses and uniformity are checked in C048h, not sampled here.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "near_left_constants_1645.json"
raw = SOURCE.read_bytes()
saved = json.loads(raw)
checks = []


def encode(x):
    x = Q(x)
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def decode(value):
    if set(value) != {"numerator", "denominator"}:
        raise ValueError("Unexpected rational schema")
    if int(value["denominator"]) <= 0:
        raise ValueError("Nonpositive denominator")
    return Q(int(value["numerator"]), int(value["denominator"]))


def check(name, actual, relation, required):
    actual, required = Q(actual), Q(required)
    passed = {"<": actual < required, "<=": actual <= required,
              ">": actual > required, "=": actual == required}[relation]
    checks.append({"name": name, "actual": encode(actual),
                   "relation": relation, "required": encode(required),
                   "passed": passed})


def exponential(x, degree, label):
    x = Q(x)
    check(label + "_positive_argument", x, ">", 0)
    check(label + "_remainder_ratio", x / (degree + 2), "<", 1)
    lower = sum((x**k / factorial(k) for k in range(degree + 1)), Q(0))
    first = x**(degree + 1) / factorial(degree + 1)
    ratio = x / (degree + 2)
    upper = lower + first / (1 - ratio)
    return {"argument": encode(x), "degree": degree,
            "lower": encode(lower), "first_omitted": encode(first),
            "tail_ratio_upper": encode(ratio), "upper": encode(upper)}


def arctangent(x, terms):
    # Pair positive and negative terms of the even partial sum.
    lower = sum((x**(4*j+1)/(4*j+1) - x**(4*j+3)/(4*j+3)
                 for j in range(terms // 2)), Q(0))
    return {"argument": encode(x), "terms": terms, "lower": encode(lower),
            "upper": encode(lower + x**(2*terms+1)/(2*terms+1))}


evidence_exp12 = exponential(Q(12), 120, "exp12")
atan5, atan239 = arctangent(Q(1, 5), 24), arctangent(Q(1, 239), 8)
tan2a = 2*Q(1, 5)/(1-Q(1, 5)**2)
tan4a = 2*tan2a/(1-tan2a**2)
check("Machin_tan_4a", tan4a, "=", Q(120, 119))
check("Machin_tan_difference", (tan4a-Q(1, 239))/(1+tan4a*Q(1, 239)), "=", 1)
check("Machin_angle_upper_below_pi_over_2", Q(4, 5), "<", Q(3, 2))

e_lo, e_hi = Q(1627547914190039, 10**10), Q(1627547914190040, 10**10)
pi_lo, pi_hi = Q(3141592653589793, 10**15), Q(3141592653589794, 10**15)
y_lo, y_hi = e_lo/12**4, e_hi/12**4
c, prefactor = Q(1007, 2430), Q(81, 133)
rad_lo, rad_hi = 6*y_lo/pi_hi, 6*y_hi/pi_lo
root_lo, root_hi = decode(saved["root"]["lower"]), decode(saved["root"]["upper"])
unit = Q(1, 10**18)
check("root_lower_positive", root_lo, ">", 0)
check("root_upper_positive", root_hi, ">", 0)
check("radicands_ordered", rad_lo, "<", rad_hi)
check("lower_root_square", root_lo**2, "<=", rad_lo)
check("lower_root_next_grid_square", rad_lo, "<", (root_lo+unit)**2)
check("upper_root_previous_grid_square", (root_hi-unit)**2, "<=", rad_hi)
check("upper_root_square", rad_hi, "<", root_hi**2)
for label, root in [("lower", root_lo), ("upper", root_hi)]:
    scaled = root / unit
    check(label + "_root_on_integer_grid", scaled.denominator, "=", 1)

exp_lo = exponential(c*y_lo, 80, "denominator_lower")
exp_hi = exponential(c*y_hi, 80, "denominator_upper")
den_lo, den_hi = decode(exp_lo["lower"]), decode(exp_hi["upper"])
check("denominator_lower_positive", den_lo, ">", 0)
check("denominators_ordered", den_lo, "<", den_hi)
lower, upper = prefactor*root_lo/den_hi, prefactor*root_hi/den_lo
rounded_lo, rounded_hi = Q(91190139998283, 10**15), Q(91190139998284, 10**15)
threshold, slack = Q(91191, 10**6), Q(1, 10**8)

expected_checks = []


def original_check(name, actual, relation, required):
    check(name, actual, relation, required)
    expected_checks.append(checks[-1])


original_check("theta_parameter_floor", Q(7**5, 144), ">", 1)
original_check("complete_amplitude_with_denominator", Q(6975, 4802), "<", Q(3, 2))
original_check("consecutive_mode_ratio", Q(81, 1568), "<", Q(1, 10))
original_check("left_tangent_rate", Q(38, 15)*Q(35, 36), "=", Q(133, 54))
original_check("left_phase_coefficient", Q(19, 45)*Q(53, 54), "=", c)
original_check("radial_floor", Q(7**6, 12**4), ">", 5)
original_check("decreasing_scalar_threshold", 5, ">", 1/(2*c))
original_check("exp12_lower", decode(evidence_exp12["lower"]), ">", e_lo)
original_check("exp12_upper", decode(evidence_exp12["upper"]), "<", e_hi)
original_check("pi_lower", 16*decode(atan5["lower"])-4*decode(atan239["upper"]), ">", pi_lo)
original_check("pi_upper", 16*decode(atan5["upper"])-4*decode(atan239["lower"]), "<", pi_hi)
original_check("A_minus_upper", upper, "<", threshold)
original_check("A_minus_rounded_lower", lower, ">", rounded_lo)
original_check("A_minus_rounded_upper", upper, "<", rounded_hi)
original_check("A_minus_slack", threshold-upper, ">", slack)

expected = {
    "scope": "C048h fixed scalar comparisons; analytic uniformity is proved in the lemma.",
    "exp12": evidence_exp12,
    "pi_machin": {"identity": "pi=16 atan(1/5)-4 atan(1/239)",
                  "atan5": atan5, "atan239": atan239},
    "scalar_intervals": {"exp12": [encode(e_lo), encode(e_hi)],
                         "pi": [encode(pi_lo), encode(pi_hi)],
                         "y0": [encode(y_lo), encode(y_hi)]},
    "root": {"lower_radicand": encode(rad_lo), "upper_radicand": encode(rad_hi),
             "lower": encode(root_lo), "upper": encode(root_hi),
             "lower_square_le_lower_radicand": root_lo**2 <= rad_lo,
             "upper_square_gt_upper_radicand": root_hi**2 > rad_hi},
    "denominator_lower": exp_lo, "denominator_upper": exp_hi,
    "A_minus": {"lower": encode(lower), "upper": encode(upper),
                "required_strict_upper": encode(threshold), "upper_slack": encode(threshold-upper)},
    "A_minus_rounded": {"lower": encode(rounded_lo), "upper": encode(rounded_hi),
                        "required_strict_upper": encode(threshold), "certified_slack_lower": encode(slack)},
    "checks": expected_checks,
    "failures": [item["name"] for item in expected_checks if not item["passed"]],
}
field_checks = []


def compare(actual, required, pointer=""):
    if isinstance(required, dict):
        same_keys = isinstance(actual, dict) and set(actual) == set(required)
        field_checks.append({"pointer": pointer or "/", "kind": "keys", "passed": same_keys})
        if same_keys:
            for key, value in required.items():
                compare(actual[key], value, pointer + "/" + key)
    elif isinstance(required, list):
        same_length = isinstance(actual, list) and len(actual) == len(required)
        field_checks.append({"pointer": pointer, "kind": "length", "passed": same_length})
        if same_length:
            for i, value in enumerate(required):
                compare(actual[i], value, pointer + "/" + str(i))
    else:
        field_checks.append({"pointer": pointer, "kind": "exact_value",
                             "passed": type(actual) is type(required) and actual == required})


compare(saved, expected)
failures = ([item["name"] for item in checks if not item["passed"]]
            + [item["pointer"] for item in field_checks if not item["passed"]])
certificate = {
    "scope": "Complete exact scalar audit only; analytic all-sector proof is in C048h audit1647.",
    "input": str(SOURCE.relative_to(Path.cwd())), "input_sha256": sha256(raw).hexdigest(),
    "method": "Power/factorial exponential sums, paired arctangent sums, squared root-grid inequalities, full-field comparison; no producer import.",
    "exact_checks": checks, "field_checks": field_checks,
    "recomputed_certificate": expected, "failures": failures,
    "summary": {"original_comparisons": len(expected_checks), "audit_comparisons": len(checks),
                "field_checks": len(field_checks), "rounded_interval": expected["A_minus_rounded"],
                "failures": failures},
}
destination = HERE / "near_left_audit_1647.json"
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact comparisons: {len(checks)}; original comparisons: {len(expected_checks)}; complete field checks: {len(field_checks)}")
print("Certified A_- interval: (0.091190139998283, 0.091190139998284)")
print("Required A_- < 0.091191; exact certified slack > 1/100000000")
print(f"Failures: {failures}")
print(f"Certificate: {destination.relative_to(Path.cwd())}")
if failures:
    raise SystemExit(1)

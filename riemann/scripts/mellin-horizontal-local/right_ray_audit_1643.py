#!/usr/bin/env python3
"""Validate every scalar record in C048g's certificate; independently bound A_+."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import subprocess
import sys

here = Path(__file__).parent
source = here / "right_ray_constants_1641.json"
before = source.read_bytes()
replay = subprocess.run([sys.executable, str(source.with_suffix(".py"))],
                        capture_output=True, text=True, check=True)
data = json.loads(source.read_text())
checks = []


def frac(v):
    return F(int(v["numerator"]), int(v["denominator"]))


def rat(v):
    v = F(v)
    return {"numerator": str(v.numerator), "denominator": str(v.denominator)}


def verify(name, passed):
    checks.append({"name": name, "passed": bool(passed)})


def positive_exp(x, n):
    # Direct factorial sums, independent of the producer's recurrence.
    assert 0 < x < n + 2
    low = sum((x**k / factorial(k) for k in range(n + 1)), F(0))
    first = x**(n+1) / factorial(n+1)
    ratio = x / (n+2)
    return low, low + first/(1-ratio), first, ratio


def exp_record(name, x, n):
    rec = data[name]
    low, high, first, ratio = positive_exp(x, n)
    expected = {"argument": rat(x), "degree": n, "lower": rat(low),
                "first_omitted": rat(first), "tail_ratio_upper": rat(ratio),
                "upper": rat(high)}
    verify(name + "_complete_record", rec == expected)
    return low, high


verify("replay_byte_identical", source.read_bytes() == before)
e3, _ = exp_record("exp3", F(3), 8)
e12lo, e12hi = exp_record("exp12", F(12), 120)
eighthlo, eighthhi = exp_record("exp_eighth", F(1, 8), 30)
el, eu = F(1627547914190039, 10**10), F(1627547914190040, 10**10)
pl, pu = F(3141592653589793, 10**15), F(3141592653589794, 10**15)
yl, yu = el/12**4, eu/12**4
c, prefactor = F(19, 45), F(75, 124)
dl, _ = exp_record("denominator_lower", c*yl, 80)
_, du = exp_record("denominator_upper", c*yu, 80)

atan_endpoints = []
for name, x, n in [("atan5", F(1, 5), 24), ("atan239", F(1, 239), 8)]:
    low = sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)), F(0))
    high = low + x**(2*n+1)/F(2*n+1)
    verify(name + "_complete_record", data["pi_machin"][name] == {
        "argument": rat(x), "terms": n, "lower": rat(low), "upper": rat(high)})
    atan_endpoints.append((low, high))
verify("machin_label", data["pi_machin"]["identity"] == "pi=16 atan(1/5)-4 atan(1/239)")
al, au = atan_endpoints[0]
bl, bu = atan_endpoints[1]
pil, piu = 16*al-4*bu, 16*au-4*bl
verify("scalar_intervals_complete", data["scalar_intervals"] == {
    "exp12": [rat(el), rat(eu)], "pi": [rat(pl), rat(pu)],
    "y0": [rat(yl), rat(yu)]})

radlo, radhi = 6*yl/pu, 6*yu/pl
rl, ru = frac(data["root"]["lower"]), frac(data["root"]["upper"])
verify("root_record_complete", data["root"] == {
    "lower_radicand": rat(radlo), "upper_radicand": rat(radhi),
    "lower": rat(rl), "upper": rat(ru),
    "lower_square_le_lower_radicand": rl**2 <= radlo,
    "upper_square_gt_upper_radicand": ru**2 > radhi})
verify("positive_root_bracket", 0 < rl and rl**2 <= radlo < radhi < ru**2)

lower, upper = prefactor*eighthlo*rl/du, prefactor*eighthhi*ru/dl
threshold = F(48257, 500000)
verify("A_plus_complete", data["A_plus"] == {
    "lower": rat(lower), "upper": rat(upper),
    "required_strict_upper": rat(threshold), "upper_slack": rat(threshold-upper)})
rlo, rhi = F(96513538928204, 10**15), F(96513538928205, 10**15)
verify("A_plus_rounded_complete", data["A_plus_rounded"] == {
    "lower": rat(rlo), "upper": rat(rhi),
    "required_strict_upper": rat(threshold), "certified_slack_lower": rat(F(1, 10**9))})

expected_checks = [
    ("exp3_partial_sum_above_20", e3, ">", F(20)),
    ("exp12_floor_pays_rate", F(20**4, 12**3), ">", F(675, 8)),
    ("theta_amplitude", 1+F(1,14)+F(20,343), "<", F(3,2)),
    ("mode_ratio", F(81,16*98), "<", F(1,10)),
    ("exp12_lower", e12lo, ">", el), ("exp12_upper", e12hi, "<", eu),
    ("pi_lower", pil, ">", pl), ("pi_upper", piu, "<", pu),
    ("y0_monotonicity_threshold", yl, ">", F(45,38)),
    ("A_plus_upper", upper, "<", threshold),
    ("A_plus_rounded_lower", lower, ">", rlo),
    ("A_plus_rounded_upper", upper, "<", rhi),
    ("A_plus_slack", threshold-upper, ">", F(1,10**9)),
]
verify("producer_check_count", len(data["checks"]) == len(expected_checks))
for entry, (name, actual, relation, required) in zip(data["checks"], expected_checks):
    passed = actual < required if relation == "<" else actual > required
    verify(name + "_record_and_truth", passed and entry == {
        "name": name, "actual": rat(actual), "relation": relation,
        "required": rat(required), "passed": True})
verify("producer_failure_list", data["failures"] == [])

# Independent enclosure: signed Taylor polynomials for exp(-x), avoiding
# the producer's reciprocal-of-positive-exponential construction.
# Taylor's integral remainder has sign (-1)^(n+1), for every x>0.
def alternating_exp(x, n):
    return sum(((-x)**k/F(factorial(k)) for k in range(n+1)), F(0))


negative_lo = alternating_exp(c*yu, 81)
negative_hi = alternating_exp(c*yl, 82)
independent_lo = prefactor*eighthlo*rl*negative_lo
independent_hi = prefactor*eighthhi*ru*negative_hi
verify("independent_positive_exp_bracket", 0 < negative_lo < negative_hi)
verify("independent_A_plus_bracket", rlo < independent_lo < independent_hi < rhi)
verify("independent_threshold_and_slack", threshold-independent_hi > F(1,10**9))

# Exact analytic constants whose signs control convergence and radial reduction.
verify("rate_difference", F(38,15)-F(62,25) == F(4,75))
verify("rate_absorption", F(4,75)*F(675,8) == F(9,2))
verify("phase_endpoint", F(19,10)*2/F(9) == F(19,45))
verify("width_endpoint", F(9,2)/F(3*12) == F(1,8))
verify("radial_threshold", F(160000,12**4) > F(45,38))

result = {
    "scope": "C048g scalar audit; analytic proof is recorded in the canonical lemma.",
    "producer_sha256": hashlib.sha256(before).hexdigest(),
    "producer_replay_stdout": replay.stdout,
    "checks": checks,
    "independent_method": "exp(-x) odd degree81 lower/even degree82 upper by Taylor integral remainder",
    "negative_exponential": {"lower_argument": rat(c*yu), "upper_argument": rat(c*yl),
                             "lower": rat(negative_lo), "upper": rat(negative_hi)},
    "A_plus_independent": {"lower": rat(independent_lo), "upper": rat(independent_hi),
                           "upper_slack": rat(threshold-independent_hi)},
    "A_plus_rounded": {"lower": rat(rlo), "upper": rat(rhi),
                       "required_strict_upper": rat(threshold),
                       "certified_slack_lower": rat(F(1,10**9))},
    "failures": [v["name"] for v in checks if not v["passed"]],
}
destination = here / "right_ray_audit_1643.json"
destination.write_text(json.dumps(result, indent=2) + "\n")
print(f"Complete scalar audit: {len(checks)} checks; failures: {result['failures']}")
print("Actual rational enclosure: 96513538928204/10^15 < A_+ < 96513538928205/10^15")
print("Required: A_+ < 48257/500000; certified slack > 1/10^9")
print(f"Certificate: {destination}")
if result["failures"]:
    raise SystemExit(1)

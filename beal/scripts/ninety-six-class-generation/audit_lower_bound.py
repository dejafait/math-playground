"""Independent exact arithmetic audit of L052's saved certificate.

No import of the original calculation. Local-field implications remain
the cited mathematical arguments in L052, not program assertions.
"""
import json
from fractions import Fraction
from pathlib import Path

folder = Path(__file__).resolve().parent
source = json.loads((folder / "discriminant-lower-bound-certificate.json").read_text())
m = [-8007, -6240, -660, -1320, -2112, -132, 66, -264, 0, 0, 0, -4, 1]
failures = []


def check(label, actual, expected):
    if actual != expected:
        failures.append({"check": label, "actual": actual, "expected": expected})


def horner_translate(a, shift):
    b = [a[-1]]
    for c in reversed(a[:-1]):
        b = [shift * b[0] + c] + [b[i - 1] + shift * b[i]
                                    for i in range(1, len(b))] + [b[-1]]
    return b


def vp(c, p):
    if c == 0:
        return None
    k, power = 0, p
    while c % power == 0:
        k, power = k + 1, power * p
    return k


check("model", source["models"]["m96_ascending"], m)
check("local factorization count", len(source["local"]), 2)
local = []
for index, (p, shift, different) in enumerate([(3, 0, 10), (11, 3, 11)]):
    c = horner_translate(m, shift)
    check(f"inverse translation at {p}", horner_translate(c, -shift), m)
    v = [vp(x, p) for x in c]
    points = [[i, x] for i, x in enumerate(v) if x is not None]
    gaps = [[i, 11 * x - (11 - i)] for i, x in points if i <= 11]
    check(f"segment supports at {p}", [v[0], v[11], v[12]], [1, 0, 0])
    check(f"all points above supporting lines at {p}", all(g >= 0 for _, g in gaps), True)
    # Exact supporting lines with slopes -1/11 < 0 certify the lower hull;
    # no implementation of the original convex-hull algorithm is reused.
    row = {
        "prime": p, "translation_U_equals_V_plus": shift,
        "coefficients_ascending": c,
        "coefficient_valuations_zero_is_null": v,
        "reduction_ascending": [x % p for x in c], "newton_points": points,
        "lower_hull": [[0, 1], [11, 0], [12, 0]],
        "first_segment_scaled_vertical_gaps": gaps,
        "segments": [
            {"length": 11, "slope": [-1, 11], "root_valuation": [1, 11]},
            {"length": 1, "slope": [0, 1], "root_valuation": [0, 1]}],
        # These fields are checked for faithful transcription of the proof,
        # rather than established by arithmetic alone.
        "proof_in_L052": {
            "complete_local_degrees": [11, 1],
            "ramification_residue_pairs": [[11, 1], [1, 1]],
            "different_exponent_lower_bounds": [different, 0],
            "K96_discriminant_exponent_lower_bound": different,
            "L96_discriminant_exponent_lower_bound": 3 * different}}
    check(f"complete local record at {p}", source["local"][index], row)
    local.append(row)

q = Fraction(1)
for i in range(1, 37):
    q *= Fraction(i, 36)
d0 = 3**30 * 11**33
a, b = q.numerator, q.denominator
n, d = d0 * a * a, b * b
# Integer bisection, independent of the original isqrt calculation.
low, high = 0, 1
while high * high * d <= n:
    high *= 2
while high - low > 1:
    mid = (low + high) // 2
    if mid * mid * d <= n:
        low = mid
    else:
        high = mid
cutoff = {
    "required_threshold": 10**6,
    "uniform_signature_factor_lower_bound": 1,
    "justification": "0<=s<=18 and pi<4 imply (4/pi)^s>=1",
    "rational_factor_numerator": a, "rational_factor_denominator": b,
    "floor_of_uniform_lower_comparison": low,
    "squared_threshold_difference": n - 10**12 * d,
    "rounding_lower_difference": n - low * low * d,
    "rounding_upper_difference": high * high * d - n}
check("complete cutoff record", source["cutoff"], cutoff)
check("strict comparisons", all(cutoff[k] > 0 for k in (
    "squared_threshold_difference", "rounding_lower_difference", "rounding_upper_difference")), True)
check("claimed floor", low, 7646157636)
check("maximal lower bound", source["maximal_field_lower_bound"],
      {"divisor": d0, "prime_exponents": {"3": 30, "11": 33}})
out = {
    "method": "Horner translation and inverse, exact supporting lines, product rational and integer bisection",
    "local": local, "cutoff": cutoff,
    "discriminant_divisor": d0,
    "failures": failures,
    "routing_threshold_met": False,
    "limitations": "Arithmetic audit only; field degrees are cited L051 inputs and local implications are audited in L052. No class-group complexity bound."}
path = folder / "lower-bound-audit-certificate.json"
path.write_text(json.dumps(out, indent=2) + "\n")
print("Independent arithmetic audit:", "FAIL" if failures else "PASS")
print("Actual lower-comparison floor:", low, "; required maximum:", 10**6)
print("Audit failures:", len(failures), "; enumeration threshold: FAIL (expected)")
print("Certificate:", path.relative_to(Path.cwd()))
if failures:
    raise SystemExit(1)

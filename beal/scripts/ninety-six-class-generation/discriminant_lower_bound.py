"""Exact arithmetic for L052; local-field conclusions are proved in L052.

Run: python3 scripts/ninety-six-class-generation/discriminant_lower_bound.py
The complete certificate is saved beside this script. No external backend.
"""
import json
from fractions import Fraction
from math import comb, factorial, isqrt
from pathlib import Path


def valuation(value, prime):
    if value == 0:
        return None  # infinity, omitted from the finite Newton points
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def translate(coefficients, shift):
    return [sum(coefficients[j] * comb(j, i) * shift**(j-i)
                for j in range(i, len(coefficients)))
            for i in range(len(coefficients))]


def lower_hull(points):
    hull = []
    for point in points:
        while len(hull) >= 2:
            a, b = hull[-2:]
            cross = ((b[0]-a[0])*(point[1]-b[1])
                     - (b[1]-a[1])*(point[0]-b[0]))
            if cross > 0:
                break
            hull.pop()
        hull.append(point)
    return hull


m = [-8007, -6240, -660, -1320, -2112, -132, 66, -264,
     0, 0, 0, -4, 1]  # ascending, L051's exact m96
local = []
for prime, shift, different_lower in [(3, 0, 10), (11, 3, 11)]:
    coefficients = translate(m, shift)
    valuations = [valuation(c, prime) for c in coefficients]
    points = [[i, v] for i, v in enumerate(valuations) if v is not None]
    hull = lower_hull(points)
    assert hull == [[0, 1], [11, 0], [12, 0]]
    # Full evidence that no coefficient falls below either segment.
    gaps = [[i, 11*v-(11-i)] for i, v in points if i <= 11]
    assert all(gap >= 0 for _, gap in gaps)
    assert coefficients[11] % prime and coefficients[12] == 1
    # Independent reduction identity V^11(V+c_11) modulo p.
    reduction = [c % prime for c in coefficients]
    expected = [0]*11 + [coefficients[11] % prime, 1]
    assert reduction == expected
    local.append({
        "prime": prime, "translation_U_equals_V_plus": shift,
        "coefficients_ascending": coefficients,
        "coefficient_valuations_zero_is_null": valuations,
        "reduction_ascending": reduction, "newton_points": points,
        "lower_hull": hull, "first_segment_scaled_vertical_gaps": gaps,
        "segments": [
            {"length": 11, "slope": [-1, 11], "root_valuation": [1, 11]},
            {"length": 1, "slope": [0, 1], "root_valuation": [0, 1]}],
        "proof_in_L052": {
            "complete_local_degrees": [11, 1],
            "ramification_residue_pairs": [[11, 1], [1, 1]],
            "different_exponent_lower_bounds": [different_lower, 0],
            "K96_discriminant_exponent_lower_bound": different_lower,
            "L96_discriminant_exponent_lower_bound": 3*different_lower}})

discriminant_lower = 3**30 * 11**33
q = Fraction(factorial(36), 36**36)
a, b = q.numerator, q.denominator
radicand = discriminant_lower*a*a
floor = isqrt(radicand // (b*b))
assert floor**2*b*b < radicand < (floor+1)**2*b*b
threshold = 10**6
difference = radicand-threshold**2*b*b
assert difference > 0
certificate = {
    "models": {"m96_ascending": m, "degree_K96": 12, "degree_L96": 36,
               "relative_degree": 3, "degree_source": "L051 cited FNS input"},
    "local": local,
    "maximal_field_lower_bound": {"divisor": discriminant_lower,
                                  "prime_exponents": {"3": 30, "11": 33}},
    "cutoff": {"required_threshold": threshold,
               "uniform_signature_factor_lower_bound": 1,
               "justification": "0<=s<=18 and pi<4 imply (4/pi)^s>=1",
               "rational_factor_numerator": a, "rational_factor_denominator": b,
               "floor_of_uniform_lower_comparison": floor,
               "squared_threshold_difference": difference,
               "rounding_lower_difference": radicand-floor**2*b*b,
               "rounding_upper_difference": (floor+1)**2*b*b-radicand},
    "checks": {"complete_coefficient_valuation_arrays": True,
               "both_full_newton_polygons_verified": True,
               "independent_modular_reductions_verified": True,
               "strict_squared_threshold_and_rounding_verified": True},
    "failures": ["True Minkowski cutoff exceeds the 10^6 enumeration entry threshold"],
    "limitations": ["Field conclusions use the canonical L052 proof and cited theorems",
                    "No exact field discriminant, signature or maximal order computed",
                    "No lower bound on necessary class-group computation complexity",
                    "No class/unit/Selmer computation or Beal branch exclusion"]}
path = Path(__file__).with_name("discriminant-lower-bound-certificate.json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print("Exact coefficient/Newton-polygon/threshold checks: PASS")
print("Complete local degrees at 3 and 11: [11,1] (proof: L052)")
print("Maximal-field discriminant lower bound:", discriminant_lower, "= 3^30*11^33")
print("Actual certified lower-comparison floor:", floor, "; required maximum:", threshold)
print("Decision: PARK true-Minkowski-cutoff enumeration; no branch exclusion")
print("Failures:", certificate["failures"])
print("Certificate:", path)

"""Exact arithmetic for L069; full rational Sturm chains are saved to disk."""
from fractions import Fraction as Q
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import json


def trim(p):
    p = list(map(Q, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def primitive(p):
    p = trim(p)
    denominator = lcm(*(c.denominator for c in p))
    integers = [int(c * denominator) for c in p]
    content = reduce(gcd, (abs(c) for c in integers)) or 1
    # The scaling is positive: signs in a Sturm chain are preserved.
    return trim([c // content for c in integers])


def divrem(p, d):
    r = trim(p)
    quotient = [Q(0)] * max(1, len(r) - len(d) + 1)
    while r != [0] and len(r) >= len(d):
        shift = len(r) - len(d)
        coefficient = r[-1] / d[-1]
        quotient[shift] += coefficient
        for i, c in enumerate(d):
            r[i + shift] -= coefficient * c
        r = trim(r)
    return trim(quotient), r


def sign(c):
    return (c > 0) - (c < 0)


def variations(signs):
    signs = [s for s in signs if s]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def sturm(p):
    p = trim(p)
    chain = [p, primitive([i * p[i] for i in range(1, len(p))])]
    division_records = []
    while len(chain[-1]) > 1:
        quotient, remainder = divrem(chain[-2], chain[-1])
        assert remainder != [0], "Nonconstant gcd: repeated-root input"
        next_polynomial = primitive([-c for c in remainder])
        multiplier = next_polynomial[-1] / (-remainder[-1])
        assert multiplier > 0
        assert next_polynomial == trim([-multiplier * c for c in remainder])
        division_records.append({
            "quotient": list(map(str, quotient)),
            "remainder": list(map(str, remainder)),
            "positive_normalization": str(multiplier),
        })
        chain.append(next_polynomial)
    plus = [sign(p[-1]) for p in chain]
    minus = [s * (-1) ** (len(p) - 1) for s, p in zip(plus, chain)]
    return {
        "ascending_polynomials": [list(map(str, p)) for p in chain],
        "divisions": division_records,
        "minus_infinity_signs": minus,
        "plus_infinity_signs": plus,
        "minus_variations": variations(minus),
        "plus_variations": variations(plus),
        "real_roots": variations(minus) - variations(plus),
        "last_polynomial_is_nonzero_constant": len(chain[-1]) == 1 and chain[-1][0] != 0,
    }


m = [-380, -774, -1062, -456, 258, 468, 104, -126, -6, 6, -6, 0, 1]
g = [-1264, -160, -4, 1]
m_sturm, g_sturm = sturm(m), sturm(g)
d, c, b, a = g
discriminant = b*b*c*c - 4*a*c*c*c - 4*b*b*b*d - 27*a*a*d*d + 18*a*b*c*d
residue_values = [sum(coefficient * x**i for i, coefficient in enumerate(g)) % 5
                  for x in range(5)]
r1 = m_sturm["real_roots"]
r2 = (12 - r1) // 2
rd1, rd2 = r1, r1 + 3*r2
base_unit_dimension = r1 + r2
cubic_unit_dimension = rd1 + rd2
kernel_dimension = cubic_unit_dimension - base_unit_dimension
torsion_dimension = 0
corrected_ambient_lower_bound = kernel_dimension - torsion_dimension
# After reducing y^2+y=x^3-x^2-10x-20, (8y+4)^2
# has the following coefficients in x. Compare with g(4x).
lhs_model = [16 - 64*20, -64*10, -64, 64]
rhs_model = [coefficient * 4**i for i, coefficient in enumerate(g)]
checks = {
    "integral_model_identity": lhs_model == rhs_model,
    "base_sturm_squarefree": m_sturm["last_polynomial_is_nonzero_constant"],
    "base_degree_and_signature": r1 == 2 and r2 == 5 and r1 + 2*r2 == 12,
    "cubic_discriminant": discriminant == -256 * 11**5,
    "cubic_one_real_root": g_sturm["real_roots"] == 1 and discriminant < 0,
    "cubic_no_root_modulo_five": all(residue_values),
    "simple_base_root_modulo_five": m[0] % 5 == 0 and m[1] % 5 != 0,
    "entire_cubic_signature": rd1 == 2 and rd2 == 17 and rd1 + 2*rd2 == 36,
    "unit_kernel_dimension": base_unit_dimension == 7 and cubic_unit_dimension == 19
        and kernel_dimension == 12,
    "strict_threshold_fails": corrected_ambient_lower_bound > 11,
}
certificate = {
    "inputs": {"m": m, "g": g},
    "model": {"lhs_reduced": lhs_model, "rhs": rhs_model},
    "base_sturm": m_sturm,
    "cubic_sturm": g_sturm,
    "cubic_discriminant": discriminant,
    "cubic_residue_values_modulo_five": residue_values,
    "base_simple_root_modulo_five": {"root": 0, "m_value": m[0] % 5,
                                         "derivative_value": m[1] % 5},
    "signatures": {"K": [r1, r2], "D": [rd1, rd2]},
    "dimensions": {"base_unit_squares": base_unit_dimension,
                   "cubic_unit_squares": cubic_unit_dimension,
                   "norm_square_unit_kernel": kernel_dimension,
                   "rational_two_torsion": torsion_dimension,
                   "corrected_ambient_lower_bound": corrected_ambient_lower_bound,
                   "required_upper_bound": 11},
    "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
    "qualification": "The torsion and unit assertions also require L069's proof; this is not a rank lower bound.",
}
destination = Path(__file__).with_name("diagnostic-certificate.json")
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {certificate['failures']}")
print(f"Signatures K={r1,r2}, D={rd1,rd2}; unit dimensions={base_unit_dimension},{cubic_unit_dimension}")
print(f"Actual ambient lower bound after torsion: {corrected_ambient_lower_bound}; required upper bound: 11")
print(f"Certificate: {destination}")
if certificate["failures"]:
    raise SystemExit(1)

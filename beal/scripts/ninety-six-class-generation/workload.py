"""Exact trace-order discriminant and conservative Minkowski workload.

Run from the notebook: python3 scripts/ninety-six-class-generation/workload.py
No external mathematical backend. Full evidence is written beside this script.
"""
import json
from math import factorial, isqrt
from fractions import Fraction
from pathlib import Path


def traces(coeffs):
    # Monic polynomial coefficients in descending order; Newton sums.
    n = len(coeffs) - 1
    out = [n]
    for k in range(1, 2*n-1):
        if k <= n:
            value = sum(coeffs[j]*out[k-j] for j in range(1, k)) + k*coeffs[k]
        else:
            value = sum(coeffs[j]*out[k-j] for j in range(1, n+1))
        out.append(-value)
    return out


def det(matrix):
    # Fraction-free Bareiss elimination, with exact divisibility checked.
    a = [row[:] for row in matrix]
    sign, previous = 1, 1
    for k in range(len(a)-1):
        if a[k][k] == 0:
            row = next(i for i in range(k+1, len(a)) if a[i][k])
            a[k], a[row] = a[row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def resultant_discriminant(coeffs):
    n = len(coeffs)-1
    derivative = [coeffs[i]*(n-i) for i in range(n)]
    size = 2*n-1
    sylvester = []
    for i in range(n-1):
        sylvester.append([0]*i+coeffs+[0]*(size-i-len(coeffs)))
    for i in range(n):
        sylvester.append([0]*i+derivative+[0]*(size-i-len(derivative)))
    return (-1)**(n*(n-1)//2)*det(sylvester)


m = [1, -4, 0, 0, 0, -264, 66, -132, -2112, -1320, -660, -6240, -8007]
h = [1, -4, -160, -1264]
tm, th = traces(m), traces(h)
gm = [[tm[i+j] for j in range(12)] for i in range(12)]
gh = [[th[i+j] for j in range(3)] for i in range(3)]
basis = [(i, j) for i in range(12) for j in range(3)]
g = [[tm[i+k]*th[j+l] for k, l in basis] for i, j in basis]
dm, dh, d = det(gm), det(gh), det(g)
assert d == dm**3 * dh**12 and d != 0
assert dm == resultant_discriminant(m)
assert dh == resultant_discriminant(h)
# Since 0<=s<=18 and 1<4/pi<4/3, M <= a/b sqrt(|d|).
q = Fraction(factorial(36)*4**18, 36**36*3**18)
a, b = q.numerator, q.denominator
radicand = abs(d)*a*a
floor_bound = isqrt(radicand // (b*b))
assert floor_bound**2*b*b <= radicand < (floor_bound+1)**2*b*b
ceil_bound = floor_bound if floor_bound**2*b*b == radicand else floor_bound+1
threshold = 10**6
assert floor_bound**2*b*b < radicand
assert radicand > threshold**2*b*b
certificate = {
    "models": {"m96_descending": m, "h_descending": h,
               "degree_36": "FNS Section 7.2, cited input, not inferred from determinant"},
    "traces": {"m96": tm, "h": th},
    "basis_exponents": basis,
    "trace_matrices": {"m96": gm, "h": gh, "order36": g},
    "discriminants": {"m96_order": dm, "cubic_order": dh, "tensor_order": d},
    "bound": {"signature": "conservative s<=18, not actual signature",
              "pi_lower": 3, "rational_factor_numerator": a,
              "rational_factor_denominator": b,
              "floor_of_conservative_bound": floor_bound,
              "certified_integer_cutoff": ceil_bound,
              "required_cutoff": threshold,
              "squared_comparison_difference": radicand-threshold**2*b*b},
    "checks": {"direct_36_determinant_equals_tensor_formula": True,
               "newton_discriminants_equal_derivative_resultants": True,
               "bareiss_divisions_exact": True, "rounding_verified": True},
    "failures": ["Order-based cutoff exceeds the proposed enumeration threshold"],
    "limitations": ["No maximal order, field discriminant, actual signature or ideal backend certified",
                    "No class/unit computation or Selmer completeness certificate"]
}
path = Path(__file__).with_name("workload-certificate.json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print("Exact order trace/discriminant checks: PASS")
print("degree: 36; conservative complex pairs: at most 18")
print("cubic order discriminant:", dh)
print("degree-12 order discriminant:", dm)
print("degree-36 order discriminant:", d)
print("actual certified cutoff:", ceil_bound, "; required cutoff:", threshold)
print("decision: PARK enumeration at this order cutoff; field refinement unresolved")
print("certificate:", path)

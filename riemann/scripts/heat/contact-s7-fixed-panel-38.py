#!/usr/bin/env python3
"""One exact rational candidate for the approved panel0 S7 class.

No quadrature, parameter sweep, floating optimizer, or new moment data.
Run from the active notebook: python3 scripts/heat/contact-s7-fixed-panel-38.py
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, permutations
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "scripts/heat/low-time-h2-uniform-195.json"
OUTPUT = ROOT / "scripts/heat/contact-s7-fixed-panel-38.json"
checks = {}


def check(name, assertion):
    checks[name] = bool(assertion)


def determinant(a):
    n = len(a)
    result = F(0)
    for p in permutations(range(n)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = F(sign)
        for i in range(n):
            term *= a[i][p[i]]
        result += term
    return result


def principal_minors(a):
    return {
        ",".join(map(str, ids)): determinant([[a[i][j] for j in ids] for i in ids])
        for k in range(1, len(a) + 1)
        for ids in combinations(range(len(a)), k)
    }


def matvec(a, v):
    return [sum((aij * vj for aij, vj in zip(row, v)), F(0)) for row in a]


def dot(u, v):
    return sum((x * y for x, y in zip(u, v)), F(0))


def solve(a, b):
    # Cramer's rule is used only after an exactly nonzero determinant check.
    d = determinant(a)
    if not d:
        raise ValueError("candidate's proposed inverse is singular")
    result = []
    for j in range(len(a)):
        aj = [list(row) for row in a]
        for i in range(len(a)):
            aj[i][j] = b[i]
        result.append(determinant(aj) / d)
    return result


def log_coefficients(y):
    q = [(-1) ** j * yj / factorial(2 * j) for j, yj in enumerate(y)]
    s = [F(0)]
    for n in range(1, len(y)):
        s.append(-n * q[n] - sum((s[k] * q[n - k] for k in range(1, n)), F(0)))
    return q, s


def multiply(a, b, degree):
    out = [F(0)] * (degree + 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= degree:
                out[i + j] += ai * bj
    return out


def independent_log(q):
    h = list(q)
    h[0] = F(0)
    power = [F(1)] + [F(0)] * 7
    result = [F(0)] * 8
    for r in range(1, 8):
        power = multiply(power, h, 7)
        for n in range(8):
            result[n] += F((-1) ** (r + 1), r) * power[n]
    return [-n * result[n] for n in range(8)]


def rounded_midpoint(lo, hi):
    z = (lo + hi) * 10**12 / 2 + F(1, 2)
    return F(z.numerator // z.denominator, 10**12)


def display_bounds(x):
    bounds = []
    for mode in (ROUND_FLOOR, ROUND_CEILING):
        with localcontext() as ctx:
            ctx.prec = 9
            ctx.rounding = mode
            bounds.append(str(Decimal(x.numerator) / Decimal(x.denominator)))
    # These compact strings are also verified as enclosing rationals.
    assert F(bounds[0]) <= x <= F(bounds[1])
    return {"lower": bounds[0], "upper": bounds[1]}


def encode(obj):
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, dict):
        return {str(k): encode(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [encode(v) for v in obj]
    return obj


source_bytes = SOURCE.read_bytes()
panel = json.loads(source_bytes)["panels"][0]
intervals = [(F(panel["moments"][str(2*j)]["lower"]),
              F(panel["moments"][str(2*j)]["upper"])) for j in range(7)]
check("source_panel_endpoints", F(panel["lambda"]["lower"]) == 0
      and F(panel["lambda"]["upper"]) == F(1, 5120))
m = [rounded_midpoint(*intervals[j]) for j in range(6)]
check("mass_positive", m[0] > 0)
y = [mj / m[0] for mj in m]
q, s = log_coefficients(y)
delta = s[2] * s[4] - s[3]**2
check("logarithmic_inverse_legitimate", s[2] > 0 and delta > 0)

certificate = {
    "schema": "single rational candidate with algebraically normalized contact vector",
    "source": {"path": str(SOURCE.relative_to(ROOT)), "sha256": sha256(source_bytes).hexdigest(),
               "panel": 0, "lambda": panel["lambda"], "complete_moment_intervals": panel["moments"]},
    "construction": {"rounding_denominator": 10**12,
                     "rule": "nearest 10^-12 to exact interval midpoint, half ties upward, for m0..m5; no search"},
}

if not checks["logarithmic_inverse_legitimate"]:
    certificate.update({"checks": checks, "failures": [k for k, v in checks.items() if not v],
                        "first_unpaid_comparison": "leading logarithmic block positive definite"})
    OUTPUT.write_text(json.dumps(encode(certificate), indent=2) + "\n")
    print("INCONCLUSIVE: candidate inverse not justified; certificate:", OUTPUT.relative_to(ROOT))
    raise SystemExit(1)

p = (s[3] * s[5] - s[4]**2) / delta
r = (s[3] * s[4] - s[2] * s[5]) / delta
vector = [p, r, F(1)]
s6 = -p * s[4] - r * s[5]
q6 = -(s6 + sum((s[k] * q[6-k] for k in range(1, 6)), F(0))) / 6
y.append(factorial(12) * q6)
m.append(m[0] * y[6])

membership = {}
for j, ((lo, hi), mj) in enumerate(zip(intervals, m)):
    membership[str(j)] = {"m": mj, "lower_slack": mj - lo, "upper_slack": hi - mj,
                          "relative_box_position": (mj - lo) / (hi - lo)}
    check(f"m{j}_in_complete_interval", lo <= mj <= hi)
    check(f"common_mass_y{j}", mj == m[0] * y[j])
check("y0_equals_one", y[0] == 1)

w = [[y[i+j+1] for j in range(3)] for i in range(3)]
wminors = principal_minors(w)
for key, value in wminors.items():
    check("W_minor_positive_" + key, value > 0)
certificate["raw_W_principal_minors"] = wminors
if not all(value > 0 for value in wminors.values()):
    certificate.update({"membership": membership, "checks": checks,
                        "failures": [k for k, v in checks.items() if not v],
                        "first_unpaid_comparison": "candidate raw W positive definite"})
    OUTPUT.write_text(json.dumps(encode(certificate), indent=2) + "\n")
    print("INCONCLUSIVE: candidate raw inverse not justified; certificate:", OUTPUT.relative_to(ROOT))
    raise SystemExit(1)

v = y[4:7]
a = solve(w, v)
y.append(dot(v, a))
q, s = log_coefficients(y)
check("forced_S6_matches_finite_log", s[6] == s6)
check("independent_finite_log_all_coefficients", independent_log(q) == s)
check("raw_W_solve_exact", matvec(w, a) == v)

M3 = [[y[i+j] for j in range(4)] for i in range(4)]
N3 = [[y[i+j+1] for j in range(4)] for i in range(4)]
H2 = [[s[i+j+2] for j in range(3)] for i in range(3)]
minors = {}
for name, matrix in (("M3", M3), ("N3", N3), ("H2", H2)):
    minors[name] = principal_minors(matrix)
    for key, value in minors[name].items():
        check(name + "_principal_minor_nonnegative_" + key, value >= 0)
for key, value in minors["M3"].items():
    check("M3_principal_minor_strict_" + key, value > 0)
check("N3_determinant_zero", determinant(N3) == 0)
check("H2_determinant_zero", determinant(H2) == 0)
null_rows = matvec(H2, vector)
for i, value in enumerate(null_rows):
    check(f"H2_null_row_{i}", value == 0)
norm_squared = dot(vector, vector)
normalized_products = [[vi*vj/norm_squared for vj in vector] for vi in vector]
check("algebraic_normalization_exists", norm_squared > 0)
check("unit_c", sum(normalized_products[i][i] for i in range(3)) == 1)
check("c2_nonzero", normalized_products[2][2] > 0)

b = {n: sum((vector[i] * vector[j] for i in range(3) for j in range(3)
             if i+j == n-2), F(0)) / norm_squared for n in range(2, 7)}
B = (-2 * sum((n*(2*n+1)*b[n]*s[n+1] for n in range(2, 6)), F(0))
     +4 * sum((n*b[n]*sum((s[k]*s[n+1-k] for k in range(2, n)), F(0))
               for n in range(2, 7)), F(0)))
phi = -156 * normalized_products[2][2] * s[7] + B
full_heat_flux = sum((b[n]*(-2*n*(2*n+1)*s[n+1]
    +4*n*sum((s[k]*s[n+1-k] for k in range(1, n+1)), F(0)))
    for n in range(2, 7)), F(0))
check("L874_flux_equals_full_heat_recurrence", phi == full_heat_flux)
threshold_y7 = F(factorial(14), 7) * (B / (156 * normalized_products[2][2])
                 + sum((s[k]*q[7-k] for k in range(1, 7)), F(0)))
deficit = threshold_y7 - y[7]
check("raw_threshold_flux_identity", phi == F(6, factorial(12))*normalized_products[2][2]*deficit)
strict_bounds = {"S2_lower": F("3.714e-5"), "delta_lower": F("9.7e-16"),
                 "delta_upper": F("7.026e-15")}
check("strict_S2_bound", s[2] > strict_bounds["S2_lower"])
check("strict_delta_lower", delta > strict_bounds["delta_lower"])
check("strict_delta_upper", delta < strict_bounds["delta_upper"])
check("strict_flux_positive", phi > 0)
quantities = {"S2": s[2], "delta": delta, "m6": m[6], "c2_squared": normalized_products[2][2],
              "y7": y[7], "threshold_y7": threshold_y7, "threshold_minus_y7": deficit, "Phi": phi}
compact_bounds = {key: display_bounds(value) for key, value in quantities.items()}
compact_bounds["m6_box_position"] = display_bounds(membership["6"]["relative_box_position"])
failures = [k for k, passed in checks.items() if not passed]
certificate.update({
    "construction": {**certificate["construction"], "m0_through_m6": m,
                     "y0_through_y7": y, "q0_through_q7": q, "S1_through_S7": s[1:],
                     "contact_vector_unnormalized": vector, "norm_squared": norm_squared,
                     "c_definition": "(p,r,1)/sqrt(norm_squared), positive real square root",
                     "normalized_pair_products": normalized_products,
                     "raw_v": v, "raw_W_inverse_v": a},
    "membership": membership, "matrices": {"M3": M3, "N3": N3, "H2": H2, "W": w},
    "principal_minors": minors, "null_rows_unnormalized": null_rows,
    "finite_log_independent_residuals": [a-bb for a, bb in zip(s, independent_log(q))],
    "strict_bounds_required": strict_bounds,
    "flux": {"b2_through_b6": b, "B": B, **quantities, "full_heat_flux": full_heat_flux},
    "compact_rational_enclosures": compact_bounds,
    "checks": checks, "failures": failures,
    "result": "CERTIFIED_VIOLATING_FINITE_TUPLE" if not failures else "INCONCLUSIVE_SINGLE_CANDIDATE",
    "qualifications": ["Finite relaxed tuple; no actual theta law or parameter is claimed.",
                       "All source endpoints are exact rationals; analytic actual-law inclusion retains L917 contracts.",
                       "W invertibility is proved for this tuple only; singular members of the target class are retained.",
                       "This certificate is not an independent later proof audit or an RH counterexample."]
})
OUTPUT.write_text(json.dumps(encode(certificate), indent=2) + "\n")
print(certificate["result"])
for key, enclosure in compact_bounds.items():
    print(f"{key}: [{enclosure['lower']}, {enclosure['upper']}]")
print("Required: S2>3.714e-5; 9.7e-16<delta<7.026e-15; 0<=m6_box_position<=1; Phi>0")
print(f"Exact checks: {len(checks)}; failures: {failures}")
print("Certificate:", OUTPUT.relative_to(ROOT))
raise SystemExit(bool(failures))

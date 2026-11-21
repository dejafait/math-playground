#!/usr/bin/env python3
"""Single approved model; exact rational evidence, no numerical truncation."""
from fractions import Fraction as F
import json
from pathlib import Path


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_add(a, b):
    return [(a[i] if i < len(a) else F(0))
            + (b[i] if i < len(b) else F(0))
            for i in range(max(len(a), len(b)))]


def evaluate(a, x):
    value = F(0)
    for v in reversed(a):
        value = value * x + v
    return value


def serialize(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: serialize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(item) for item in value]
    return value


checks = {}


def check(name, condition):
    checks[name] = bool(condition)


alpha = [F(-4, 5), F(-9, 10)]
P = [F(18, 25), F(17, 10), F(1)]
factor = [F(1), F(0), F(4, 5)]
G = poly_mul(P, factor)
sigma = F(21, 20)
check("distinct_simple_nonzero_negative_interior_nodes",
      -1 < alpha[1] < alpha[0] < 0)
check("G_zero_and_one_positive", G[0] > 0 and sum(G) > 0)
check("all_polynomial_coefficients_positive", all(x > 0 for x in G))
check("exterior_root_radius_exceeds_sigma", sigma**2 < F(5, 4))
check("sigma_exceeds_one", sigma > 1)
check("F_positive_reciprocal_margin", 1 - F(4, 5) * sigma**2 > 0)
check("P_has_exact_nodes", all(evaluate(P, x) == 0 for x in alpha))

d = [x**2 * evaluate(factor, x) / (2*x + F(17, 10)) for x in alpha]
check("ordered_residue_signs", d[0] > 0 > d[1])

# b = A/z^2 + B/z + (D+L*z)/(1+t*z^2), checked after
# multiplication by z^2(1+t*z^2), not by a finite series preview.
A, B, D, L, t = F(18, 25), F(17, 10), F(53, 125), F(-34, 25), F(4, 5)
b_numerator = poly_add(poly_mul([A, B], factor), [0, 0, D, L])
check("complete_b_partial_fraction_identity", b_numerator == P + [F(0)])

# c = polynomial + sum_i d_i/(z-alpha_i), with complete analytic part.
c_analytic = [F(342, 125), F(-34, 25), F(4, 5)]
c_remainder = [-d[0]*alpha[1] - d[1]*alpha[0], sum(d)]
c_numerator = poly_add(poly_mul(c_analytic, P), c_remainder)
check("complete_c_partial_fraction_identity", c_numerator == [0, 0, 1, 0, t])

q = -t
a, b = D*q**2, L*q**2


def h(x):
    return (a*x + b*x*x) / (1 + t*x*x)


def hp(x):
    return (a + 2*b*x - a*t*x*x) / (1 + t*x*x)**2


K12 = (h(alpha[0]) - h(alpha[1])) / (alpha[0] - alpha[1])
K = [[hp(alpha[0]), K12], [K12, hp(alpha[1])]]
weights = [abs(d[i])*abs(alpha[i])**3 for i in range(2)]
J = [F(1), F(-1)]
S = [[alpha[i]**3 * K[i][j] for j in range(2)] for i in range(2)]
# T = E^-1 (J-Q) E^-1 = J E^-2 + K. It has the same inertia.
T = [[K[i][j] + (J[i]/weights[i] if i == j else 0)
      for j in range(2)] for i in range(2)]
detT = T[0][0]*T[1][1] - T[0][1]*T[1][0]
pivots = [T[0][0], detT/T[0][0]]
check("all_similarity_weights_positive", all(w > 0 for w in weights))
check("complete_series_bidisk_ratio_below_one", F(9, 10)/sigma < 1)
check("symmetric_K", K[0][1] == K[1][0])
check("exact_signed_row_weight", all(d[i]*alpha[i]**3 == -J[i]*weights[i]
                                     for i in range(2)))
check("positive_LDL_pivots", all(p > 0 for p in pivots))
IminusCS = [[F(i == j) - d[i]*S[i][j] for j in range(2)] for i in range(2)]
detIminusCS = IminusCS[0][0]*IminusCS[1][1] - IminusCS[0][1]*IminusCS[1][0]
check("determinant_orientation", detIminusCS == -weights[0]*weights[1]*detT)
actual_inertia = {"positive": 2, "zero": 0, "negative": 0}
required = {"zero": 0, "negative": 1}
check("nullity_requirement_holds", actual_inertia["zero"] == required["zero"])
# Failure of the proposed negative-index equality is the tested outcome,
# not a script/check failure.
adverse = actual_inertia["negative"] != required["negative"]
check("adverse_index_certified", adverse and detT > 0 and T[0][0] > 0)

certificate = {
    "model": "(z+4/5)(z+9/10)(1+4*z^2/5); r=3; R=1",
    "arithmetic": "Python standard-library fractions.Fraction, exact rational",
    "alpha": alpha, "exterior_roots": "+/- i*sqrt(5)/2",
    "G_coefficients_ascending": G, "G_at_one": sum(G),
    "sigma": sigma, "F_disk_lower_bound": 1-t*sigma**2,
    "d": d, "b_decomposition_A_B_D_L_t": [A, B, D, L, t],
    "beta_all_positive": {"even_2m_m_ge_1": "(53/125)*(-4/5)^m",
                          "odd_2m_plus_1_m_ge_0": "(-34/25)*(-4/5)^m"},
    "c_analytic_coefficients_ascending": c_analytic,
    "c_remainder_coefficients_ascending": c_remainder,
    "c_negative_all_n_ge_1": "sum_i d_i*alpha_i^(n-1)",
    "h_numerator_coefficients_ascending": [0, a, b],
    "h_denominator_coefficients_ascending": factor,
    "h_at_nodes": [h(x) for x in alpha], "K": K, "S": S,
    "E_squared_diagonal": weights, "J_diagonal": J,
    "congruent_T": T, "T_determinant": detT, "T_LDL_pivots": pivots,
    "IminusCS": IminusCS, "det_IminusCS": detIminusCS,
    "actual_inertia_JminusQ": actual_inertia,
    "required_index_and_nullity": required, "adverse_index": adverse,
    "checks": checks, "failures": [key for key, value in checks.items() if not value],
    "qualification": "Finite local-premise countermodel only; no actual-Xi conclusion; proof in L783."
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(serialize(certificate), indent=2) + "\n")
print("Actual inertia (positive,zero,negative): (2,0,0); required negative index: 1; required nullity: 0")
print(f"Exact congruent pivots: {pivots[0]}, {pivots[1]}")
print(f"Checks: {len(checks)}; failures: {certificate['failures']}; adverse index: {adverse}")
print(f"Certificate: {path.relative_to(Path.cwd())}")
if certificate["failures"]:
    raise SystemExit(1)

#!/usr/bin/env python3
"""Independent L784 replay using exact Laurent polynomials in t=pi^2/128.

No import of the original interval implementation. Intermediate rational
endpoints are exact; only certificate serialization rounds outwards.
"""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import hashlib
import json


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    products = [x*y for x in a for y in b]
    return min(products), max(products)


def power(a, n):
    if n < 0:
        assert a[0] > 0 or a[1] < 0
        return power((1/a[1], 1/a[0]), -n)
    values = [a[0]**n, a[1]**n]
    if n > 0 and n % 2 == 0 and a[0] <= 0 <= a[1]:
        values.append(F(0))
    return min(values), max(values)


def scale(a, c):
    return mul(a, (F(c), F(c)))


def sub(a, b):
    return add(a, scale(b, -1))


def divide(a, b):
    return mul(a, power(b, -1))


def atan(q, n):
    s = sum(F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(n))
    a = s+F((-1)**n, (2*n+1)*q**(2*n+1))
    return min(s, a), max(s, a)


def polynomial(terms):
    result = {}
    for degree, coefficient in terms:
        result[degree] = result.get(degree, F(0))+coefficient
    return {n: c for n, c in result.items() if c}


def evaluate(poly, x):
    result = (F(0), F(0))
    for n, c in sorted(poly.items()):
        result = add(result, scale(power(x, n), c))
    return result


def interval_json(a):
    scale_224 = 2**224
    lo = F(a[0].numerator*scale_224//a[0].denominator, scale_224)
    hi = F(-((-a[1].numerator*scale_224)//a[1].denominator), scale_224)
    assert lo <= a[0] <= a[1] <= hi
    return {"lo": str(lo), "hi": str(hi)}


def inside(a, old):
    return F(old["lo"]) <= a[0] <= a[1] <= F(old["hi"])


def strict(a, lo, hi):
    return F(lo) < a[0] <= a[1] < F(hi)


original_path = Path(__file__).with_name("exact-inertia-453.json")
original_bytes = original_path.read_bytes()
old = json.loads(original_bytes)
pi = sub(scale(atan(5, 36), 16), scale(atan(239, 10), 4))
t = scale(power(pi, 2), F(1, 128))
root_scale = 10**60
root_floor = isqrt(2*root_scale**2)
sqrt2 = F(root_floor, root_scale), F(root_floor+1, root_scale)
g = [F(8**n, factorial(2*n))*sum(mass*atom**(2*n)
     for atom, mass in [(1, F(1, 2)), (2, F(2)), (3, F(1, 2))])
     for n in range(6)]
inv = [1/g[0]]
for n in range(1, 6):
    inv.append(-sum(g[j]*inv[n-j] for j in range(1, n+1))/g[0])

# P^2 has coefficient a_j*t^(4-j) at z^j. Expand exactly before
# evaluation, unlike the original T/Tprime interval implementation.
a = [F(81), F(180), F(118), F(20), F(1)]
terms = [(m, j, a[j]*inv[m+2-j])
         for m in range(-2, 4) for j in range(min(4, m+2)+1)]
beta_polys = {m: polynomial((4-j, c) for mm, j, c in terms if mm == m)
              for m in range(-2, 4)}
h_polys = [polynomial((m+1-j, -c*F(-q)**(m-3)) for m, j, c in terms)
           for q in [1, 9]]
diagonal_polys = [polynomial((m-j, (3-m)*c*F(-q)**(m-4))
                            for m, j, c in terms) for q in [1, 9]]
offdiag_poly = polynomial((m-j, c*(-F(-1)**(m-3)+F(-9)**(m-3))/8)
                         for m, j, c in terms)
M11, M22 = [evaluate(poly, t) for poly in diagonal_polys]
M12 = evaluate(offdiag_poly, t)
det_M = sub(mul(M11, M22), power(M12, 2))
pivot2 = divide(det_M, M11)
d = [divide(add((F(2), F(2)), scale(sqrt2, F(1, 2))), scale(pi, 2)),
     scale(divide(sub((F(2), F(2)), scale(sqrt2, F(1, 2))), scale(pi, 2)), -27)]
weights = [mul(d[0], power(t, 3)), scale(mul(d[1], power(t, 3)), -729)]
alpha = [scale(t, -1), scale(t, -9)]
Kdiag = [add(Mii, power(mul(d[i], power(alpha[i], 3)), -1))
         for i, Mii in enumerate([M11, M22])]
det_I_CS = scale(mul(mul(weights[0], weights[1]), det_M), -1)
field_values = {"pi": pi, "sqrt2": sqrt2, "t": t, "det_M": det_M,
                "det_I_CS": det_I_CS}
checks = {"original_22_checks_true": len(old["checks"]) == 22
          and all(value is True for value in old["checks"].values())
          and old["failures"] == [],
          "g_coefficients_exact_match": [str(v) for v in g] == old["G8_coefficients_0_to_5"],
          "inverse_coefficients_exact_match": [str(v) for v in inv] == old["inverse_local_coefficients_0_to_5"],
          "sqrt2_exact_integer_bracket": root_floor**2 < 2*root_scale**2 < (root_floor+1)**2,
          "M11_required_5063_5064": strict(M11, 5063, 5064),
          "M12_required_062_063": strict(M12, F(62, 1000), F(63, 1000)),
          "M22_required_minus454_minus453": strict(M22, F(-454, 1000), F(-453, 1000)),
          "det_required_minus2294_minus2293": strict(det_M, -2294, -2293),
          "strict_LDL_plus_minus": M11[0] > 0 and pivot2[1] < 0,
          "positive_congruence_weights": all(w[0] > 0 for w in weights),
          "det_I_CS_positive": det_I_CS[0] > 0}
for name, value in field_values.items():
    checks["independent_enclosure_inside_original_"+name] = inside(value, old[name])
for name, values in [("alpha", alpha), ("residues", d), ("E_squared_weights", weights),
                     ("h3_at_nodes_complete", [evaluate(p, t) for p in h_polys]),
                     ("LDL_pivots_M", [M11, pivot2])]:
    checks["independent_enclosures_inside_original_"+name] = all(
        inside(value, old[name][i]) for i, value in enumerate(values))
    for i, value in enumerate(values):
        field_values[name+"_"+str(i)] = value
for m, poly in beta_polys.items():
    value = evaluate(poly, t)
    checks["independent_beta_"+str(m)+"_inside_original"] = inside(value, old["beta_minus2_to3"][str(m)])
    field_values["beta_"+str(m)] = value
for name, values in [("K_complete", [[Kdiag[0], M12], [M12, Kdiag[1]]]),
                     ("residual_positive_diagonal_congruence_M", [[M11, M12], [M12, M22]])]:
    checks["independent_enclosures_inside_original_"+name] = all(
        inside(values[i][j], old[name][i][j]) for i in range(2) for j in range(2))
    for i in range(2):
        for j in range(2):
            field_values[name+"_"+str(i)+str(j)] = values[i][j]

failures = [name for name, result in checks.items() if not result]
certificate = {
    "scope": "L784 fixed-law independent arithmetic audit only; analytic proof remains canonical in L784",
    "original_sha256": hashlib.sha256(original_bytes).hexdigest(),
    "method": "Exact Laurent polynomials in positive t; exact rational endpoints without intermediate rounding; final 224-bit outward serialization",
    "pi_method": "Machin alternating sums with 36 and 10 terms; different from original 32 and 8",
    "M_laurent_polynomials_in_t": [{str(n): str(c) for n, c in sorted(p.items())}
                                   for p in [diagonal_polys[0], offdiag_poly, diagonal_polys[1]]],
    "intervals": {name: interval_json(value) for name, value in field_values.items()},
    "actual_inertia_J_minus_Q": [1, 0, 1] if checks["strict_LDL_plus_minus"] else None,
    "required_inertia_J": [1, 0, 1], "checks": checks, "failures": failures,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Independent checks: {sum(checks.values())}/{len(checks)}; failures: {failures}")
print("Actual certified M11 in (5063,5064), M12 in (.062,.063), M22 in (-.454,-.453)")
print("Actual certified det(M) in (-2294,-2293); required LDL signs (+,-): satisfied")
print(f"Actual inertia: {certificate['actual_inertia_J_minus_Q']}; required: [1, 0, 1]")
print(f"Full audit certificate: {path}")
assert not failures, failures

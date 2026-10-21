"""Exact HRR bookkeeping for L136; no existence or sheaf-sign test."""
from fractions import Fraction
from pathlib import Path
import json

# y,b,c are factor point classes; t,u are the two full mixed tensors.
# Their multidegrees are real cohomological degrees on (Y,B_1,B_2).
degrees = ((4, 0, 0), (0, 4, 0), (0, 0, 4), (2, 2, 0), (2, 0, 2))
zero = (0,) * 5


def add(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, Fraction(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(poly, value):
    return {key: coefficient * value for key, coefficient in poly.items()}


def monomial(*exponents):
    return {tuple(exponents): Fraction(1)}


def mul(left, right):
    out = {}
    for key1, value1 in left.items():
        for key2, value2 in right.items():
            key = [a + b for a, b in zip(key1, key2)]
            coefficient = value1 * value2
            # Full mixed-square integral, not just its divisor part.
            for mixed, base in ((3, 1), (4, 2)):
                while key[mixed] >= 2:
                    key[mixed] -= 2
                    key[0] += 1
                    key[base] += 1
                    coefficient *= 156
            degree = tuple(sum(key[j] * degrees[j][i] for j in range(5))
                           for i in range(3))
            if any(d > 4 for d in degree):
                continue
            key = tuple(key)
            out[key] = out.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in out.items() if value}


def serialize(poly):
    return [{"exponents_y_b_c_t_u": list(key), "coefficient": str(value)}
            for key, value in sorted(poly.items())]


one = {zero: Fraction(1)}
y = monomial(1, 0, 0, 0, 0)
b = monomial(0, 1, 0, 0, 0)
c = monomial(0, 0, 1, 0, 0)
t = monomial(0, 0, 0, 1, 0)
u = monomial(0, 0, 0, 0, 1)
beta1 = add(scale(y, -21), scale(b, -14), scale(t, -1))
beta2 = add(scale(y, -21), scale(c, -14), scale(u, -1))
ch1 = add(scale(one, 2), beta1, scale(mul(beta1, beta1), Fraction(1, 12)))
ch2 = add(scale(one, 2), beta2, scale(mul(beta2, beta2), Fraction(1, 12)))
coefficient = mul(ch1, ch2)  # Odd characters vanish; dualization changes none.
td_y = add(one, scale(y, 2))
td_b = add(one, scale(b, 2))
td_c = add(one, scale(c, 2))
integrand = mul(mul(mul(coefficient, td_y), td_b), td_c)
top = (1, 1, 1, 0, 0)
index = integrand.get(top, Fraction(0))

# Independent iterated integration, first over each parameter surface.
# Neither lone mixed tensor can pair to top degree on its parameter.
parameter_integrand = mul(ch1, td_b)
parameter_push = {
    y_power: parameter_integrand.get((y_power, 1, 0, 0, 0), Fraction(0))
    for y_power in (0, 1)
}
iterated_index = 2 * parameter_push[0] ** 2 + 2 * parameter_push[0] * parameter_push[1]
checks = {
    "full_beta_square": mul(beta1, beta1) == scale(mul(y, b), 744),
    "forced_fourth_character": scale(mul(beta1, beta1), Fraction(1, 12)) == scale(mul(y, b), 62),
    "absolute_index": index == -200,
    "iterated_index": iterated_index == index,
    "relative_pure_rank": mul(coefficient, td_y).get((1, 0, 0, 0, 0), 0) == -76,
    "relative_pure_second_each": all(mul(coefficient, td_y).get(key, 0) == 362 for key in ((1, 1, 0, 0, 0), (1, 0, 1, 0, 0))),
    "relative_pure_top": mul(coefficient, td_y).get(top, 0) == -1344,
}
certificate = {
    "scope": "L071 equality invariants; conditional F; cohomological HRR only",
    "degree_order": ["Y", "B_1", "B_2"],
    "generator_order": ["y", "b", "c", "t", "u"],
    "mixed_square_coefficient": 156,
    "beta1_squared": serialize(mul(beta1, beta1)),
    "character1": serialize(ch1),
    "character2": serialize(ch2),
    "coefficient_character": serialize(coefficient),
    "absolute_integrand": serialize(integrand),
    "parameter_push_character": {str(k): str(v) for k, v in parameter_push.items()},
    "index_actual": str(index),
    "index_required_for_identity": "-200",
    "iterated_index": str(iterated_index),
    "euler_identity": "N = chi(M) - 202",
    "count_upper_bound": None,
    "uncontrolled_term": "chi(M), ordinary M=H^1(K)",
    "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
    "limitations": ["No F existence", "No coincidence existence", "No middle-sheaf sign or upper bound", "No proof of the diagonal sheaf identification; see L136"],
}
path = Path(__file__).with_name("global_euler_certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Absolute Euler actual={index}; required=-200; independent={iterated_index}")
print("Count identity: N=chi(M)-202; required for N<=C: chi(M)<=C+202; upper control unavailable")
print(f"Checks={len(checks)}; failures={certificate['failures']}; certificate={path}")
raise SystemExit(bool(certificate["failures"]))

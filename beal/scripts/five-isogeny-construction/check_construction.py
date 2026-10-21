"""Exact rational/polynomial certificate for the bounded L033 construction."""
from fractions import Fraction as Q
from pathlib import Path
import json


def trim(a):
    a = list(map(Q, a))
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def scale(a, c):
    return trim([c * v for v in a])


def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    return trim(c)


def power(a, n):
    r = [Q(1)]
    for _ in range(n):
        r = mul(r, a)
    return r


def sub(a, b):
    return add(a, scale(b, -1))


def derivative(a):
    return trim([i * a[i] for i in range(1, len(a))] or [0])


def pair_mul(a, b):
    # (A+B*y)(C+D*y), reduced using y^2=g-y.
    A, B = a
    C, D = b
    return (add(mul(A, C), mul(mul(B, D), g)),
            sub(add(mul(A, D), mul(B, C)), mul(B, D)))


def group_add(P, R):
    if P is None:
        return R
    if R is None:
        return P
    x, y = P
    u, v = R
    if x == u and y + v == -1:
        return None
    s = (3*x*x - 2*x - 10)/(2*y + 1) if P == R else (v-y)/(u-x)
    b = y - s*x
    X = s*s + 1 - x - u
    return X, -s*X - b - 1


def invariants(a4, a6):
    b2, b4, b6 = -4, 2*a4, 1+4*a6
    b8 = -4*a6-1-a4*a4
    return {"discriminant": -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6,
            "c4": b2*b2-24*b4, "c6": -b2**3+36*b2*b4-216*b6}


def serial_poly(a):
    return [str(v) for v in a]


g = [-20, -10, -1, 1]
vT, v2T = [-5, 1], [-16, 1]
lT = ([20, -5], [1])
l2T = ([-35, 6], [1])
f = ([-55, 30, -4], [-4, 1])
miller = pair_mul(pair_mul(lT, lT), l2T)
miller_residuals = [sub(miller[i], mul(power(v2T, 2), f[i])) for i in range(2)]
A, B = f
norm = sub(sub(power(A, 2), mul(A, B)), mul(g, power(B, 2)))
norm_residual = add(norm, power(vT, 5))
line_residuals = []
for line_y, factor in [([ -20, 5], mul(power(vT, 2), v2T)),
                       ([35, -6], mul(power(v2T, 2), vT))]:
    line_residuals.append(add(sub(add(power(line_y, 2), line_y), g), factor))

D = mul(power(vT, 2), power(v2T, 2))
N = mul([0, 1], D)
for c, term in [(110, mul(vT, power(v2T, 2))),
                (121, power(v2T, 2)),
                (1452, mul(v2T, power(vT, 2))),
                (14641, power(vT, 2))]:
    N = add(N, scale(term, c))
H = sub(mul(derivative(N), D), mul(N, derivative(D)))
W = add(scale(g, 4), [1])
quotient_rhs = add(sub(scale(mul(power(N, 3), D), 4),
                       scale(mul(power(N, 2), power(D, 2)), 4)),
                   add(scale(mul(N, power(D, 3)), -31280),
                       scale(power(D, 4), -1054319)))
quotient_residual = sub(mul(W, power(H, 2)), quotient_rhs)

T = (Q(5), Q(5))
points, P = [], None
for n in range(1, 6):
    P = group_add(P, T)
    points.append(P)
expected = [(Q(5), Q(5)), (Q(16), Q(-61)), (Q(16), Q(60)),
            (Q(5), Q(-6)), None]

def f_value(P):
    x, y = P
    return (x-4)*y-4*x*x+30*x-55

torsion_values = [str(f_value(P)) for P in points[:4]]
# Each divisor (nT+R)-(R) is good: neither endpoint is T or O.
shifts = [2, 2, 4, 3]
exceptional_ratios = []
for n, r in enumerate(shifts, 1):
    endpoint = group_add(points[n-1], points[r-1])
    assert endpoint not in [T, None] and points[r-1] not in [T, None]
    exceptional_ratios.append(str(f_value(endpoint)/f_value(points[r-1])))

checks = {
    "exact_order_five": points == expected,
    "all_nonzero_torsion_points_on_curve": all(y*y+y == x**3-x*x-10*x-20 for x,y in points[:4]),
    "miller_identity": all(a == [0] for a in miller_residuals),
    "norm_identity": norm_residual == [0],
    "line_intersections": all(a == [0] for a in line_residuals),
    "quotient_curve_identity": quotient_residual == [0],
    "quotient_map_degree_five": len(N)-1 == 5 and len(D)-1 == 4 and
        sum(N[i]*Q(5)**i for i in range(len(N))) != 0 and
        sum(N[i]*Q(16)**i for i in range(len(N))) != 0,
    "discriminants": invariants(-10,-20)["discriminant"] == -11**5 and
        invariants(-7820,-263580)["discriminant"] == -11,
    "exceptional_ratios": exceptional_ratios == ["-1/11", "1/121", "121", "-11"],
}
certificate = {
    "arithmetic": "Exact fractions and polynomial identities; coefficients in ascending degree",
    "checks": checks,
    "failures": [k for k,v in checks.items() if not v],
    "order": {"actual": 5 if points == expected else None, "required": 5},
    "multiples": [None if P is None else [str(c) for c in P] for P in points],
    "f": {"constant_coefficient_in_y": serial_poly(A), "linear_coefficient_in_y": serial_poly(B),
          "miller_residuals": [serial_poly(a) for a in miller_residuals],
          "norm_residual": serial_poly(norm_residual),
          "line_residuals": [serial_poly(a) for a in line_residuals],
          "torsion_values": torsion_values, "good_divisor_shifts": shifts,
          "exceptional_ratios": exceptional_ratios},
    "quotient": {"x_numerator": serial_poly(N), "x_denominator": serial_poly(D),
                 "derivative_numerator": serial_poly(H), "curve_residual": serial_poly(quotient_residual),
                 "source_invariants": invariants(-10,-20),
                 "target_invariants": invariants(-7820,-263580),
                 "actual_degree": 5, "required_degree": 5},
    "not_certified": ["class group", "S-unit basis", "local images", "Selmer dimension",
                      "rank", "fourth-power incompatibility", "branch emptiness"],
}
output = Path(__file__).with_name("construction-certificate.json")
output.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"checks {sum(checks.values())}/{len(checks)}; failures {certificate['failures']}")
print(f"order actual={certificate['order']['actual']} required=5; map degree actual=5 required=5")
print("finite necessary class condition constructed; computed classes=not computed; emptiness=not established")
print(output)
if certificate["failures"]:
    raise SystemExit(1)

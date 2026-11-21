"""Exact finite algebra for C795a; no degree sweep or analytic certification."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import math

# Multivariate polynomials in (d,t,u,v), with rational coefficients.
ZERO = (0, 0, 0, 0)

def const(x):
    return {ZERO: F(x)} if x else {}

def add(*ps):
    out = {}
    for p in ps:
        for k, a in p.items():
            out[k] = out.get(k, F(0)) + a
    return {k: a for k, a in out.items() if a}

def scale(p, a):
    return {k: a*b for k, b in p.items() if a*b}

def mul(p, q):
    out = {}
    for k, a in p.items():
        for l, b in q.items():
            m = tuple(x+y for x, y in zip(k, l))
            out[m] = out.get(m, F(0)) + a*b
    return {k: a for k, a in out.items() if a}

def product(*ps):
    out = const(1)
    for p in ps:
        out = mul(out, p)
    return out

def trunc(p):
    return {k: a for k, a in p.items() if k[1]+2*k[2]+3*k[3] <= 3}

def serial(p):
    return [{"powers_d_t_u_v": list(k), "coefficient": str(a)}
            for k, a in sorted(p.items())]

d, t, u, v = [{tuple(int(i == j) for i in range(4)): F(1)} for j in range(4)]
checks = {}
q = {}
for j in range(5):
    z = add(scale(t, F(j*j-j, 2)), scale(u, -F(j**3-j, 6)),
            scale(v, F(j**4-j, 24)))
    q[j] = trunc(add(const(1), z, scale(mul(z, z), F(1, 2)),
                     scale(product(z, z, z), F(1, 6))))
delta = {k: add(*(scale(q[j], (-1)**(k-j)*math.comb(k, j))
                   for j in range(k+1))) for k in (2, 3, 4)}
t2, t3, tu = mul(t, t), product(t, t, t), mul(t, u)
expected = {
    2: add(t, scale(u, -1), scale(t2, F(1, 2)), scale(v, F(7, 12)),
           scale(tu, -1), scale(t3, F(1, 6))),
    3: add(scale(u, -1), scale(t2, 3), scale(v, F(3, 2)),
           scale(tu, -9), scale(t3, 4)),
    4: add(scale(t2, 3), v, scale(tu, -18), scale(t3, 19)),
}
for k in (2, 3, 4):
    checks[f"centered_delta_{k}"] = delta[k] == expected[k]
a2sq = trunc(mul(delta[2], delta[2]))
checks["delta2_square"] = a2sq == add(t2, scale(tu, -2), t3)
d1, d2, d3 = [add(d, const(-j)) for j in (1, 2, 3)]
A = scale(product(d, d1, add(mul(d, d), scale(d, -3), const(3))), F(1, 4))
B = scale(product(d, d1, d2, d3), F(1, 12))
fourth = add(mul(A, a2sq), scale(mul(B, delta[4]), -1))
expected_fourth = add(
    scale(product(d, d1, add(scale(d, 2), const(-3)), t2), F(1, 4)),
    scale(product(d, d1, add(scale(mul(d, d), 2), scale(d, -12), const(15)), tu), F(1, 2)),
    scale(product(d, d1, add(scale(mul(d, d), -16), scale(d, 86), const(-105)), t3), F(1, 12)),
    scale(product(d, d1, d2, d3, v), -F(1, 12)))
checks["fourth_cancellation_identity"] = fourth == expected_fourth

# Contract using d*t -> -1, d^2*u -> 1, d^3*v -> -2.
# Fourth has no surviving d^2 term after exact symbolic cancellation.
contracted = {}
for (a, b, c, e), coefficient in fourth.items():
    power = a-b-2*c-3*e-1  # divide by d
    contracted[power] = contracted.get(power, F(0)) + coefficient*(-1)**b*(-2)**e
contracted = {k: a for k, a in contracted.items() if a}
checks["fourth_no_positive_power"] = all(k <= 0 for k in contracted)
checks["fourth_limit_one"] = contracted.get(0) == 1

H = [[F(1), F(0), F(1, 2)], [F(0), F(1, 2), F(1, 2)],
     [F(1, 2), F(1, 2), F(1)]]

def det(m):
    if len(m) == 1:
        return m[0][0]
    return sum((-1)**j*m[0][j]*det([r[:j]+r[j+1:] for r in m[1:]])
               for j in range(len(m)))

minors = {}
for size in (1, 2, 3):
    for indices in combinations(range(3), size):
        val = det([[H[i][j] for j in indices] for i in indices])
        key = ",".join(map(str, indices))
        minors[key] = str(val)
        checks[f"positive_minor_{key}"] = val > 0
checks["determinant_one_eighth"] = det(H) == F(1, 8)
failures = [k for k, ok in checks.items() if not ok]
out = {
    "scope": "Exact algebra only. C795a supplies analytic errors and eventual sign reasoning.",
    "asymptotic_order_K": 4,
    "q_expansions": {str(k): serial(p) for k, p in q.items()},
    "centered_deltas": {str(k): serial(p) for k, p in delta.items()},
    "fourth_cancellation": serial(fourth),
    "contracted_fourth_over_d": {str(k): str(a) for k, a in sorted(contracted.items())},
    "limiting_moments": {"m0": "1", "m1": "0", "m2": "1/2", "m3": "1/2", "m4": "1"},
    "principal_minors": minors,
    "required_bound": "Every principal minor > 0 eventually; no effective onset claimed.",
    "checks": checks, "failures": failures,
    "status": "PASS" if not failures else "FAIL",
}
path = Path(__file__).with_name("half-factor-block-765.json")
path.write_text(json.dumps(out, indent=2)+"\n")
print(f"{out['status']}: {len(checks)} exact checks; failures={failures}")
print("Limiting principal minors:", minors, "; required: each > 0")
print("Analytic remainder required: O(log^4(d)/d) -> 0; proved in C795a, not by this script.")
print("Certificate:", path)
raise SystemExit(bool(failures))

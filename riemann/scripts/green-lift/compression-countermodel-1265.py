"""Exact replay of C032d; no numerical search or floating arithmetic."""
from fractions import Fraction as F
from pathlib import Path
import json


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    return [[sum((x * y for x, y in zip(row, col)), F(0))
             for col in transpose(b)] for row in a]


def add(a, b, sign=1):
    return [[x + sign * y for x, y in zip(ra, rb)]
            for ra, rb in zip(a, b)]


def gram(a):
    return mul(transpose(a), a)


def serial(a):
    if isinstance(a, F):
        return str(a)
    if isinstance(a, list):
        return [serial(x) for x in a]
    if isinstance(a, dict):
        return {k: serial(v) for k, v in a.items()}
    return a


L = [[F(2), F(2)], [F(1), F(0)], [F(-2), F(0)]]
C, R = [[F(1), F(1), F(1)]], [[F(1), F(0)]]
r = [F(1, 3), F(1), F(3)]
k = [(1 - x) / (1 + x) for x in r]
K = [[k[i] if i == j else F(0) for j in range(3)] for i in range(3)]
gp, gm = mul(C, L), mul(mul(C, K), L)
Q = add(gram(gp), gram(gm), -1)
f, h = [[F(1)], [F(0)]], [[F(0)], [F(1)]]
plus_f = mul(gp, f)[0][0]
E = [[x[0] / plus_f] for x in mul(L, f)]
CE, CKE = mul(C, E), mul(mul(C, K), E)
stationarity = mul(mul(transpose(f), Q), h)[0][0]
kernel_energy = mul(mul(transpose(h), Q), h)[0][0]
minimum = mul(mul(transpose(f), Q), f)[0][0]
graph = add(add(gram(gp), gram(gm)), gram(R))
graph_det = graph[0][0] * graph[1][1] - graph[0][1] * graph[1][0]

checks = {
    "positive_integration_weights": all(x > 0 for x in C[0]),
    "nonnegative_multiplier_parameters": all(x >= 0 for x in r),
    "multiplier_norm_at_most_one": max(abs(x) for x in k) <= 1,
    "trace_onto_and_kernel_nonzero": mul(R, f) == [[1]] and mul(R, h) == [[0]] and h != [[0], [0]],
    "feature_rows": gp == [[1, 2]] and gm == [[2, 1]],
    "quadratic_form": Q == [[-3, 0], [0, 3]],
    "strict_kernel_energy": kernel_energy == 3 and kernel_energy > 0,
    "fiber_stationarity": stationarity == 0,
    "unique_fiber_minimum": Q[1][1] > 0 and Q[0][1] == 0,
    "nonzero_minimizing_plus_profile": plus_f == 1,
    "right_inverse": CE == [[1]],
    "minimizing_lift_identity": mul(E, mul(gp, f)) == mul(L, f),
    "compressed_feature_identity": mul(CKE, mul(gp, f)) == mul(gm, f),
    "negative_minimum": minimum == -3 and minimum < 0,
    "strict_compression_failure": CKE == [[2]] and abs(CKE[0][0]) > 1,
    "graph_norm_positive_definite": graph[0][0] > 0 and graph_det == 14,
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "result": "PASS" if not failures else "FAIL",
    "scope": "C032d finite abstract inference only; no actual-theta or RH conclusion",
    "data": {"L": L, "C": C, "R": R, "r": r, "K": K},
    "computed": {"G_plus": gp, "G_minus": gm, "Q": Q,
                 "f_1": f, "kernel_basis": h, "kernel_energy": kernel_energy,
                 "stationarity": stationarity, "fiber_minimum": minimum,
                 "E": E, "CE": CE, "CKE": CKE,
                 "multiplier_norm": max(abs(x) for x in k),
                 "compressed_norm": abs(CKE[0][0]),
                 "graph_gram": graph, "graph_determinant": graph_det},
    "required": {"multiplier_norm_upper": 1, "compressed_norm_upper": 1,
                 "fiber_minimum_lower": 0},
    "universal_verification": "Q=diag(-3,3) gives f_x=(x,0), Q(f_x,(0,t))=0 and fiber difference 3t^2 for all real x,t; all maps are finite dimensional.",
    "checks": checks,
    "failures": failures,
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(serial(certificate), indent=2) + '\n')
print(f"{certificate['result']}: {len(checks)} exact checks; failures={failures}")
print(f"||K||={max(abs(x) for x in k)} <= 1; kernel energy={kernel_energy} > 0")
print(f"Q(f_1)={minimum}, required >= 0; ||CKE||={abs(CKE[0][0])}, required <= 1")
print(f"Full certificate: {path.relative_to(Path.cwd())}")
if failures:
    raise SystemExit(1)

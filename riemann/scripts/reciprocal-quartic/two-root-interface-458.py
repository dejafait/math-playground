"""Exact formal Laurent-polynomial certificate; no CAS or numerical roots."""
import json
from pathlib import Path

N = 8  # a,b,u_0,...,u_5; a and b may have negative powers
ZERO = (0,) * N


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(*ps):
    q = {}
    for p in ps:
        for k, v in p.items():
            q[k] = q.get(k, 0) + v
    return clean(q)


def scale(p, c):
    return clean({k: c * v for k, v in p.items()})


def mul(p, q):
    out = {}
    for k, v in p.items():
        for l, w in q.items():
            m = tuple(x + y for x, y in zip(k, l))
            out[m] = out.get(m, 0) + v * w
    return clean(out)


def mon(i, power=1):
    k = list(ZERO)
    k[i] = power
    return {tuple(k): 1}


one = {ZERO: 1}
a, b = mon(0), mon(1)
u = [mon(j + 2) for j in range(6)]
s, t = add(a, b), mul(a, b)
P = [t, scale(s, -1), one]
p = [{} for _ in range(5)]
for i in range(3):
    for j in range(3):
        p[i+j] = add(p[i+j], mul(P[i], P[j]))
c = [add(*(mul(p[l], u[j-l]) for l in range(min(4, j)+1)))
     for j in range(6)]


def f(node, derivative=False):
    return add(*(scale(mul(c[j], mon(node, j-5-int(derivative))),
                       -(j-5) if derivative else -1)
                 for j in range(6)))


m11 = add(u[2], scale(mul(b, u[3]), -2), mul(mul(b, b), u[4]))
m12 = add(u[2], scale(mul(s, u[3]), -1), mul(t, u[4]))
m22 = add(u[2], scale(mul(a, u[3]), -2), mul(mul(a, a), u[4]))
residuals = {
    "diagonal_a": add(f(0, True), scale(m11, -1)),
    "diagonal_b": add(f(1, True), scale(m22, -1)),
    "off_diagonal_times_a_minus_b": add(
        f(0), scale(f(1), -1), scale(mul(add(a, scale(b, -1)), m12), -1)),
    "determinant": add(mul(m11, m22), scale(mul(m12, m12), -1),
        scale(mul(mul(add(a, scale(b, -1)), add(a, scale(b, -1))),
                      add(mul(u[2], u[4]), scale(mul(u[3], u[3]), -1))), -1)),
}
checks = {name: value == {} for name, value in residuals.items()}
artifact = {
    "arithmetic": "exact Python integers, formal Laurent monomials in a,b,u0,...,u5",
    "hypotheses_not_checked_by_script": ["a,b nonzero and distinct",
        "analytic cancellation and convergence: see L785", "E real positive invertible"],
    "coefficients": {"P": "[ab,-(a+b),1]", "B5_j": "sum_l [z^l]P^2 u_(j-l), j=0..5"},
    "form": {"W": "[[1,-b],[1,-a]]", "H": "[[u2,u3],[u3,u4]]",
        "M11": "u2-2*b*u3+b^2*u4", "M12": "u2-(a+b)*u3+a*b*u4",
        "M22": "u2-2*a*u3+a^2*u4", "det_W": "b-a",
        "det_M": "(a-b)^2*(u2*u4-u3^2)"},
    "residuals": {name: [{"exponents": list(k), "coefficient": v}
                          for k, v in sorted(value.items())]
                  for name, value in residuals.items()},
    "checks": checks, "failures": [k for k, v in checks.items() if not v],
    "actual_nonzero_residuals": sum(not v for v in checks.values()),
    "required_nonzero_residuals": 0,
}
dest = Path(__file__).with_suffix(".json")
dest.write_text(json.dumps(artifact, indent=2) + "\n")
print(f"Exact symbolic identities: {sum(checks.values())}/{len(checks)} passed")
print(f"Nonzero residuals actual={artifact['actual_nonzero_residuals']}, required=0")
print(f"Failures: {artifact['failures']}; certificate: {dest}")
if artifact["failures"]:
    raise SystemExit(1)

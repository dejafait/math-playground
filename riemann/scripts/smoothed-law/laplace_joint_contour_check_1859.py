"""Exact rational checks for C034g; no numerical divisor or sign claim."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[k] if k < len(p) else 0) +
                 (q[k] if k < len(q) else 0)
                 for k in range(max(len(p), len(q)))])


def mul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, u in enumerate(p):
        for j, v in enumerate(q):
            r[i+j] += u*v
    return trim(r)


def deriv(p):
    return trim([k*p[k] for k in range(1, len(p))] or [0])


def rat(p, q=(1,)):
    return trim(p), trim(q)


def radd(f, g):
    return rat(add(mul(f[0], g[1]), mul(g[0], f[1])), mul(f[1], g[1]))


def scale(c, f):
    return rat([c*u for u in f[0]], f[1])


def rsub(f, g):
    return radd(f, scale(-1, g))


def rmul(f, g):
    return rat(mul(f[0], g[0]), mul(f[1], g[1]))


def rd(f):
    return rat(add(mul(deriv(f[0]), f[1]),
                   [-u for u in mul(f[0], deriv(f[1]))]),
               mul(f[1], f[1]))


def laurent(f, low, high):
    n, d = f
    if all(u == 0 for u in n):
        return {k: F(0) for k in range(low, high+1)}
    vn = next(k for k, u in enumerate(n) if u)
    vd = next(k for k, u in enumerate(d) if u)
    n, d = n[vn:], d[vd:]
    shift = vn-vd
    coeff = []
    for k in range(max(0, high-shift+1)):
        value = n[k] if k < len(n) else F(0)
        value -= sum(d[i]*coeff[k-i]
                     for i in range(1, min(len(d)-1, k)+1))
        coeff.append(value/d[0])
    return {k: coeff[k-shift] if 0 <= k-shift < len(coeff) else F(0)
            for k in range(low, high+1)}


checks = []
evidence = {}


def check(name, actual, required):
    checks.append({"name": name, "actual": actual, "required": required,
                   "pass": actual == required})


x = rat([0, 1])
x2 = rmul(x, x)
for j in (1, 2):
    base = [j, 0, 1]
    q = rat([4*j*j, 0, 12*j], mul([0, 0, 1], mul(base, base)))
    primitive = rat([-4*j], mul([0, 1], base))
    qp, qpp = rd(q), rd(rd(q))
    moment_primitive = radd(rsub(rmul(x2, qp), scale(2, rmul(x, q))),
                            scale(2, primitive))
    qpp_explicit = rat([24*j**4, 0, 96*j**3, 0, 120*j*j, 0, 240*j],
                       mul([0, 0, 0, 0, 1], mul(mul(base, base), mul(base, base))))
    for name, residual in (
        ("primitive", rsub(rd(primitive), q)),
        ("second_derivative", rsub(qpp, qpp_explicit)),
        ("quadratic_primitive", rsub(rd(moment_primitive), rmul(x2, qpp))),
    ):
        check(f"j{j}:{name}", all(v == 0 for v in residual[0]), True)

    expected = {
        "Q": {-2: F(4), 0: F(4, j)},
        "Qprime": {-3: F(-8)},
        "Qsecond": {-4: F(24), 0: F(-24, j*j)},
        "L": {-1: F(-4)},
        "M": {-1: F(-24)},
    }
    functions = {"Q": q, "Qprime": qp, "Qsecond": qpp,
                 "L": primitive, "M": moment_primitive}
    evidence[str(j)] = {}
    for name, f in functions.items():
        actual = laurent(f, -4, 0)
        required = {k: expected[name].get(k, F(0)) for k in range(-4, 1)}
        check(f"j{j}:laurent_{name}", actual, required)
        evidence[str(j)][name] = actual

    # p=1 and p=x^2/2 isolate the p(0) and p''(0) trace coefficients.
    for label, p, expected_trace in (
        ("p0", rat([1]), {-3: F(8)}),
        ("p2", rat([0, 0, F(1, 2)]), {-1: F(8)}),
    ):
        trace = rsub(rmul(rd(p), q), rmul(p, qp))
        check(f"j{j}:boundary_{label}", laurent(trace, -4, 0),
              {k: expected_trace.get(k, F(0)) for k in range(-4, 1)})

    for kernel_name, kernel, residue_order in (("Q", q, 1), ("Qsecond", qpp, 3)):
        for k in range(4):
            monomial = rat([0]*k + [F(1, factorial(k))])
            coeff = laurent(rmul(monomial, kernel), -4, -1)
            check(f"j{j}:{kernel_name}:residue_g{k}", coeff[-1],
                  F(4) if k == residue_order else F(0))
            # Symmetric divergent coefficient for epsilon^(1-m).
            divergent = {1-m: F(2, m-1)*coeff[-m] for m in (2, 4)}
            required = {-1: F(0), -3: F(0)}
            if kernel_name == "Q" and k == 0:
                required[-1] = F(8)
            if kernel_name == "Qsecond" and k == 0:
                required[-3] = F(16)
            if kernel_name == "Qsecond" and k == 2:
                required[-1] = F(24)
            check(f"j{j}:{kernel_name}:counterterm_g{k}", divergent, required)

failures = [c["name"] for c in checks if not c["pass"]]
certificate = {
    "scope": "Exact rational primitives, Laurent coefficients, finite-part counterterms and finite endpoint traces in C034g; not a contour/divisor/sign verification.",
    "method": "Python standard-library Fraction polynomial arithmetic; no external algebra package.",
    "checks": checks,
    "laurent_evidence": evidence,
    "summary": {"passed": len(checks)-len(failures), "required": len(checks),
                "failures": failures, "all_pass": not failures},
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, default=str, indent=2) + "\n")
print(f"Exact algebra: {len(checks)-len(failures)}/{len(checks)} required checks passed.")
print(f"Failures: {failures}")
print(f"Certificate: {path}")
raise SystemExit(bool(failures))

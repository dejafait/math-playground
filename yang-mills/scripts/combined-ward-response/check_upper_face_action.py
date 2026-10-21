"""Exact upper-face BCH/Wick identities; no signed-response asymptotics."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from pathlib import Path
import json

DIM = 9


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(c, p):
    return {k: c * v for k, v in p.items() if c * v}


def mul(p, q):
    out = {}
    for k, v in p.items():
        for l, w in q.items():
            e = tuple(a + b for a, b in zip(k, l))
            out[e] = out.get(e, F(0)) + v * w
    return {k: v for k, v in out.items() if v}


def deriv(p, j):
    out = {}
    for k, v in p.items():
        if k[j]:
            e = list(k)
            e[j] -= 1
            out[tuple(e)] = v * k[j]
    return out


def var(j):
    return {tuple(int(i == j) for i in range(DIM)): F(1)}


def va(*vs):
    return tuple(add(*(v[i] for v in vs)) for i in range(3))


def vs(c, v):
    return tuple(scale(c, p) for p in v)


def dot(v, w):
    return add(*(mul(v[i], w[i]) for i in range(3)))


def bracket(v, w):
    return tuple(add(scale(-1, mul(v[(i+1) % 3], w[(i+2) % 3])),
                     mul(v[(i+2) % 3], w[(i+1) % 3])) for i in range(3))


def encode(p):
    return [{"exponents": k, "coefficient": str(v)} for k, v in sorted(p.items())]


H, L, d = (tuple(var(3*j+i) for i in range(3)) for j in range(3))
zero = ({}, {}, {})
w1 = w2 = w3 = zero
for Y in (va(H, vs(F(1, 2), L)), zero,
          va(vs(-1, H), vs(F(1, 2), L)), va(vs(-1, L), d)):
    w1, w2, w3 = (va(w1, Y), va(w2, vs(F(1, 2), bracket(w1, Y))),
                  va(w3, vs(F(1, 2), bracket(w2, Y)),
                     vs(F(1, 12), bracket(w1, bracket(w1, Y))),
                     vs(F(1, 12), bracket(Y, bracket(Y, w1)))))
q_bch = add(scale(F(1, 2), dot(w2, w2)), dot(w1, w3))
hl, ld, hd = bracket(H, L), bracket(L, d), bracket(H, d)
q_claim = add(scale(F(1, 8), dot(hl, hl)),
              scale(F(-1, 24), dot(ld, ld)),
              scale(F(-1, 6), dot(hd, hl)))
checks = {"bch_quartic_difference": encode(add(q_bch, scale(-1, q_claim)))}

# Six independent per-colour covariance coefficients h,l,e,b,c,f.
expected = {
    "h": add(scale(F(1, 4), dot(L, L)), scale(F(-1, 3), dot(L, d))),
    "l": add(scale(F(1, 4), dot(H, H)), scale(F(-1, 12), dot(d, d))),
    "e": scale(F(-1, 12), dot(L, L)),
    "b": add(scale(F(-1, 2), dot(H, L)), scale(F(1, 3), dot(H, d))),
    "c": scale(F(1, 3), dot(H, L)),
    "f": add(scale(F(-1, 3), dot(H, H)), scale(F(1, 6), dot(L, d))),
}
wick = {}
for (r, s), name in zip(combinations_with_replacement(range(3), 2),
                         ("h", "b", "c", "l", "f", "e")):
    factor = F(1, 2) if r == s else F(1)
    wick[name] = scale(factor, add(*(deriv(deriv(q_bch, 3*r+i), 3*s+i)
                                    for i in range(3))))
    checks["wick_difference_" + name] = encode(add(wick[name], scale(-1, expected[name])))

failures = [name for name, residual in checks.items() if residual]
certificate = {
    "scope": "Exact 9-variable SU(2) upper-face polynomial and six covariance coefficients only",
    "variables": [v + str(i) for v in ("H", "L", "d") for i in range(3)],
    "q_bch": encode(q_bch), "q_claim": encode(q_claim),
    "wick_coefficients": {name: encode(p) for name, p in wick.items()},
    "checks": checks, "failures": failures,
    "bounds": {
        "proved_response_upper_bound": "O(a^-2), analytic L029; this script does not certify asymptotics",
        "required_response_bound": "O(1)",
        "common_path_coefficient": "l*(1/4-1/(3*N)); l >= N/6 for two interior transverse endpoints",
        "actual_probe_growth_or_log": "unresolved",
    },
}
path = Path(__file__).with_name("upper-face-action-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print("Exact BCH/Wick identities:", "PASS" if not failures else "FAIL")
print("Failures:", failures)
print("Analytic actual/required upper bounds: O(a^-2) / O(1); actual signed growth unresolved")
print("Certificate:", path)
if failures:
    raise SystemExit(1)

"""Exact L179 frozen-row contraction and qualified interval recombination.

No mesh extrapolation, new heat computation, or upstream arithmetic audit.
Full Laurent rows, comparisons, and rational intervals are saved to disk.
Directions 0..3 correspond to physical directions 1..4.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ZERO = (0,) * 4


def shift(z, mu, n=1):
    return tuple(v + n * (j == mu) for j, v in enumerate(z))


def clean(row):
    return {k: v for k, v in row.items() if v}


def add(out, row, factor=F(1)):
    for k, v in row.items():
        out[k] += factor * v


def curl(z, rho, nu):
    if rho == nu:
        return {}
    return {(z, nu): F(-1), (shift(z, rho), nu): F(1),
            (z, rho): F(1), (shift(z, nu), rho): F(-1)}


def clover(z, rho, nu):
    out = defaultdict(F)
    for a, b in product((0, -1), repeat=2):
        add(out, curl(shift(shift(z, rho, a), nu, b), rho, nu), F(1, 4))
    return clean(out)


def laplace(mu):
    edge = (ZERO, mu)
    out = defaultdict(F)
    for rho in range(4):
        if rho != mu:
            for z in (ZERO, shift(ZERO, rho, -1)):
                row = curl(z, rho, mu)
                add(out, row, row[edge])
    return clean(out)


def generator(mu, rho):
    out = defaultdict(F)
    for v in (ZERO, shift(ZERO, mu)):
        add(out, clover(v, rho, mu), F(1, 2))
    return clean(out)


def compose(a, b):
    rows = []
    for row in a:
        out = defaultdict(F)
        for (z, mu), v in row.items():
            for (w, nu), c in b[mu].items():
                add(out, {(tuple(x+y for x, y in zip(z, w)), nu): v*c})
        rows.append(clean(out))
    return rows


def transpose(a):
    rows = [defaultdict(F) for _ in range(4)]
    for mu, row in enumerate(a):
        for (z, nu), v in row.items():
            rows[nu][(tuple(-x for x in z), mu)] += v
    return [clean(r) for r in rows]


def padd(*polys):
    out = defaultdict(F)
    for p in polys:
        add(out, p)
    return clean(out)


def scale(p, f):
    return clean({k: v*f for k, v in p.items()})


def pmul(p, q):
    out = defaultdict(F)
    for z, v in p.items():
        for w, c in q.items():
            out[tuple(x+y for x, y in zip(z, w))] += v*c
    return clean(out)


def unit(mu, sign=1):
    return {tuple(sign * (j == mu) for j in range(3)): F(1)}


one = {(0, 0, 0): F(1)}
x = [padd(scale(one, 2), scale(unit(j), -1), scale(unit(j, -1), -1))
     for j in range(3)]
lam = padd(*x)
sum_sq = padd(*(pmul(t, t) for t in x))
L = [laplace(mu) for mu in range(4)]
records, failures = [], []


def encode_poly(p):
    return [{"offset": list(z), "coefficient": str(v)} for z, v in sorted(p.items())]


for rho in range(4):
    K = [generator(mu, rho) for mu in range(4)]
    LK, KTL = compose(L, K), compose(transpose(K), L)
    row = defaultdict(F)
    add(row, LK[0], F(1, 2))
    add(row, KTL[0], F(1, 2))
    for mu in range(4):
        # Sum all axial offsets and close with the exact endpoint SUM S.
        actual = defaultdict(F)
        for (z, nu), v in row.items():
            if nu == mu:
                actual[z[1:]] += v
                actual[shift(z, mu)[1:]] += v
        actual = clean(actual)
        expected = {}
        if rho == 0 and mu > 0:
            j = mu - 1
            odd = padd(unit(j), scale(unit(j, -1), -1))
            bracket = padd(sum_sq, scale(pmul(lam, x[j]), -1))
            expected = scale(pmul(odd, bracket), F(1, 8))
        error = padd(actual, scale(expected, -1))
        name = f"Gamma_S_b{rho+1}_component{mu+1}"
        records.append(dict(name=name, actual=encode_poly(actual),
                            required=encode_poly(expected), error=encode_poly(error)))
        if error:
            failures.append(name)

# Sum of all diagonal numerators: full permutation pairing, denominator
# (lambda+epsilon)^2 unchanged. Exact Laurent-polynomial equality.
diag_sum = {}
for j in range(3):
    tj_sq = pmul(x[j], padd(one, scale(x[j], F(-1, 4))))
    bracket = padd(sum_sq, scale(pmul(lam, x[j]), -1))
    diag_sum = padd(diag_sum, scale(pmul(tj_sq, bracket), -1))
paired = {}
for j in range(3):
    for k in range(j+1, 3):
        diff = padd(x[j], scale(x[k], -1))
        paired = padd(paired, scale(pmul(pmul(x[j], x[k]), pmul(diff, diff)), F(-1, 4)))
error = padd(diag_sum, scale(paired, -1))
records.append(dict(name="complete_diagonal_pairing", actual=encode_poly(diag_sum),
                    required=encode_poly(paired), error=encode_poly(error)))
if error:
    failures.append("complete_diagonal_pairing")


def interval(a, b):
    return (F(a), F(b))


def isum(*xs):
    return tuple(sum(x[j] for x in xs) for j in range(2))


def imul(a, b):
    p = [x*y for x in a for y in b]
    return (min(p), max(p))


def iscale(a, n):
    return imul(a, (F(n), F(n)))


g = interval("-0.061", "-0.043")
inputs = {
    "3": dict(G=interval("2408.3740053", "2408.3740056"),
              D=interval("-237.289643", "-237.289642"),
              R=interval("1228.1260684", "1228.1260686"),
              P=interval("2359.1", "2359.2"),
              KR=interval("-74.916", "-52.809"),
              KT=interval("84000", "100000")),
    "6": dict(G=interval("5174.7326818", "5174.7326826"),
              D=interval("-98.877430", "-98.877429"),
              R=interval("451.5469823", "451.5469825"),
              P=interval("703.6", "703.7"),
              KR=interval("-27.545", "-19.416"),
              KT=interval("-47000", "-38000")),
}
enclosures = {}
for i, t in inputs.items():
    bv = isum(t["G"], iscale(t["D"], -1), iscale(t["R"], F(-1, 2)),
              iscale(t["P"], F(1, 2)))
    kv = imul(iscale(g, -3), bv)
    complete = isum(t["KT"], kv, iscale(t["KR"], -6))
    required_v = (F(414), F(588)) if i == "3" else (F(696), F(989))
    required_complete = (F(84730), F(101038)) if i == "3" else (F(-46188), F(-36845))
    for name, actual, required in [("Vmix", kv, required_v),
                                   ("complete_response", complete, required_complete)]:
        if not required[0] < actual[0] <= actual[1] < required[1]:
            failures.append(f"probe_{i}_{name}_inclusion")
    enclosures[i] = dict(BV=bv, Vmix=kv, complete_response=complete,
                         required_Vmix=required_v, required_complete=required_complete)

out = dict(scope="Exact frozen stencil and rational recombination only; upstream IEEE heat premises imported",
           source_inputs={"g": "L141(1)", "G": "L144 conclusion", "D": "L082(1)",
                          "R_KR": "L146 conclusion", "P": "L133 conclusion", "KT": "L174(3)"},
           identities=records, intervals=dict(g=g, inputs=inputs, results=enclosures),
           failures=failures, passed=not failures)
path = Path(__file__).with_name("smooth-action-coefficient-certificate.json")
path.write_text(json.dumps(out, default=str, indent=2) + "\n")
print(f"Exact polynomial identities: {len(records)}; failures: {len(failures)}")
for i, t in enclosures.items():
    print(f"probe {i}: Vmix actual {tuple(str(x) for x in t['Vmix'])}, required {t['required_Vmix']}")
    print(f"probe {i}: complete actual {tuple(str(x) for x in t['complete_response'])}, required {t['required_complete']}")
print(f"Failures: {failures}; full certificate: {path}")
if failures:
    raise SystemExit(1)

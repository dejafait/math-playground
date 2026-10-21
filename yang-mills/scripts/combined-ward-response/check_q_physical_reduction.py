"""Exact full-component path/parity and endpoint checks for L138.

No floating-point operation enters the certificate's algebra or bounds.
Polynomial variables are d2,d3,d4,eta2,eta3,eta4. A numerator is checked
before division by lambda; separate-angle parity acts on d exponents.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def add(*polys):
    result = {}
    for poly in polys:
        for power, value in poly.items():
            result[power] = result.get(power, F(0)) + value
    return {p: c for p, c in result.items() if c}


def scale(poly, value):
    return {p: c * value for p, c in poly.items() if c * value}


def mul(*polys):
    result = {(0,) * 6: F(1)}
    for poly in polys:
        updated = {}
        for pa, ca in result.items():
            for pb, cb in poly.items():
                p = tuple(a + b for a, b in zip(pa, pb))
                updated[p] = updated.get(p, F(0)) + ca * cb
        result = {p: c for p, c in updated.items() if c}
    return result


def var(index):
    p = [0] * 6
    p[index] = 1
    return {tuple(p): F(1)}


def even(poly):
    return {p: c for p, c in poly.items() if all(n % 2 == 0 for n in p[:3])}


def rational(value):
    value = F(value)
    return dict(numerator=value.numerator, denominator=value.denominator)


def encode(poly):
    return {",".join(map(str, p)): rational(c) for p, c in sorted(poly.items())}


d = [var(j) for j in range(3)]
eta = [var(j + 3) for j in range(3)]
planes = [(0, 1), (0, 2), (1, 2)]
records = []


def check(label, actual, required, raw=None):
    difference = add(actual, scale(required, -1))
    row = dict(identity=label, actual=encode(actual), required=encode(required),
               difference=encode(difference), passed=not difference)
    if raw is not None:
        row["before_parity"] = encode(raw)
    records.append(row)


# Independently construct each exact path dot d from L097's b,q symbols.
# Real and imaginary coefficients are retained separately.
frows = {}
for a, b in planes:
    breal = add(mul(eta[b], d[a]), mul(eta[a], d[b]))
    bimag = add(scale(mul(d[b], d[a]), F(-1, 2)),
                scale(mul(d[a], d[b]), F(1, 2)))
    qreal = add(scale(mul(eta[b], d[a]), -1), mul(eta[a], d[b]))
    qimag = add(scale(mul(d[b], d[a]), F(-1, 2)),
                scale(mul(d[a], d[b]), F(1, 2)))
    row = [add(qreal, breal) if r == a else
           add(qreal, scale(breal, -1)) if r == b else {} for r in range(3)]
    imag = [add(qimag, bimag) if r == a else
            add(qimag, scale(bimag, -1)) if r == b else {} for r in range(3)]
    for r in range(3):
        required = scale(mul(d[b], eta[a]), 2) if r == a else \
            scale(mul(d[a], eta[b]), -2) if r == b else {}
        check(f"path-{a+2}{b+2}-physical-{r+2}-real", row[r], required)
        check(f"path-{a+2}{b+2}-physical-{r+2}-imaginary", imag[r], {})
    frows[(a, b)] = row


# All three strain coefficients and all nine physical matrix entries.
for t in range(3):
    for r in range(3):
        for s in range(3):
            raw = add(*(mul(frows[(a, b)][r], frows[(a, b)][s])
                        for a, b in planes if t in (a, b)))
            required = {}
            if r == s:
                required = scale(mul(eta[r], eta[r], add(*(
                    mul(d[b], d[b]) for b in range(3)
                    if b != r and t in (r, b)))), 4)
            check(f"triplet-w{t+2}-entry-{r+2}{s+2}", even(raw), required, raw)


def oriented_clover_row(a, b):
    sign = 1 if a < b else -1
    row = frows[tuple(sorted((a, b)))]
    return [scale(mul(eta[a], eta[b], x), sign) for x in row]


# Symmetric polarization is applied before parity, including all orientations.
for a, b in planes:
    c = next(j for j in range(3) if j not in (a, b))
    left = oriented_clover_row(a, c)
    right = oriented_clover_row(b, c)
    for r in range(3):
        for s in range(3):
            raw = scale(add(mul(left[r], right[s]), mul(right[r], left[s])), F(1, 2))
            required = scale(mul(eta[a], eta[a], eta[b], eta[b], eta[c], eta[c],
                                 d[c], d[c]), 2) if (r, s) in ((a, b), (b, a)) else {}
            check(f"shear-s{a+2}{b+2}-entry-{r+2}{s+2}", even(raw), required, raw)


# Sum X_c/lambda=1 and equal coordinate averages give the exact integral.
product_eta_mean = F(1, 2)**3
shear_quadratic = 4 * product_eta_mean / 3
shear_matrix = shear_quadratic / 2
shear_passed = shear_quadratic == F(1, 6) and shear_matrix == F(1, 12)

# L132's complete two-label tail with the derived coefficient upper bounds.
C_Q = F(20582100) + F(5, 6) * 20582100 + F(1395445968, 12)
tail = C_Q * 1640736 * 2717908992 / 20**27
tail_required = F(6, 10**12)

# L133's full intervals; preserve the dependence on the common scalar a_Q.
inputs = {
    3: [tuple(map(F, x)) for x in
        [("2359.1", "2359.2"), ("29198.8", "29198.9"), ("19170.0", "19170.1")]],
    6: [tuple(map(F, x)) for x in
        [("703.6", "703.7"), ("69177.0", "69177.1"), ("-4195.9", "-4195.8")]],
}
endpoints = []
for probe, (pd, px, pa) in inputs.items():
    combined = (pd[0] + pa[0], pd[1] + pa[1])
    products = [a * b for a in (F(2, 3), F(1)) for b in combined]
    actual = (min(products) - pa[1]/6 + px[0]/12,
              max(products) - pa[0]/6 + px[1]/12)
    required = (F(13590), F(20768)) if probe == 3 else (F(2971), F(4137))
    endpoints.append(dict(probe=probe, inputs={"D": list(map(rational, pd)),
                          "X": list(map(rational, px)), "A": list(map(rational, pa))},
                          combined_D_A=list(map(rational, combined)),
                          product_candidates=list(map(rational, products)),
                          actual=list(map(rational, actual)),
                          required=list(map(rational, required)),
                          passed=required[0] < actual[0] < actual[1] < required[1]))

failures = [r["identity"] for r in records if not r["passed"]]
if not shear_passed:
    failures.append("shear-average-and-polarization")
if not tail < tail_required:
    failures.append("complete-spectral-tail")
failures.extend(f"endpoint-probe-{r['probe']}" for r in endpoints if not r["passed"])
certificate = dict(method="exact rational polynomial algebra, parity and endpoint arithmetic",
                   variables=["d2", "d3", "d4", "eta2", "eta3", "eta4"],
                   qualification="Analytic symmetry/integration is proved in L138; imported L133 intervals retain its IEEE qualification. No new retained numerical integration.",
                   algebra=records,
                   shear=dict(product_eta_mean=rational(product_eta_mean),
                              quadratic=rational(shear_quadratic),
                              polarized_matrix=rational(shear_matrix), passed=shear_passed),
                   tail=dict(C_Q=rational(C_Q), actual=rational(tail),
                             required=rational(tail_required), passed=tail < tail_required),
                   endpoints=endpoints, failures=failures, passed=not failures)
path = Path(__file__).with_name("q-physical-reduction-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Full-component exact polynomial checks: {sum(r['passed'] for r in records)}/{len(records)}")
print(f"Shear quadratic/matrix constants: {shear_quadratic}, {shear_matrix}; passed={shear_passed}")
print(f"Cutoff-96 full spectral tail: {float(tail):.9g}; required <{float(tail_required):.9g}")
for row in endpoints:
    vals = [F(r['numerator'], r['denominator']) for r in row['actual']]
    print(f"Probe {row['probe']} Q bounds: ({vals[0]}, {vals[1]}); reported strict interval passed={row['passed']}")
print(f"Failures: {failures}")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))

"""Exact denominator-cleared algebra and bounds for L139.

The full certificate is rational. Angle integration and the analytic
strict scalar bounds are proved in L139, not inferred from sampling.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def add(*polys):
    out = {}
    for poly in polys:
        for p, c in poly.items():
            out[p] = out.get(p, F(0)) + c
    return {p: c for p, c in out.items() if c}


def scale(poly, c):
    return {p: c * v for p, v in poly.items() if c * v}


def mul(*polys):
    out = {(0,) * 6: F(1)}
    for poly in polys:
        new = {}
        for p, c in out.items():
            for q, v in poly.items():
                pq = tuple(a + b for a, b in zip(p, q))
                new[pq] = new.get(pq, F(0)) + c * v
        out = {p: c for p, c in new.items() if c}
    return out


def var(j):
    p = [0] * 6
    p[j] = 1
    return {tuple(p): F(1)}


def even(poly):
    return {p: c for p, c in poly.items() if all(n % 2 == 0 for n in p[:3])}


def rat(value):
    value = F(value)
    return dict(numerator=value.numerator, denominator=value.denominator)


def encode(poly):
    return {",".join(map(str, p)): rat(c) for p, c in sorted(poly.items())}


records = []


def check(name, actual, required, raw=None, variables=None):
    difference = add(actual, scale(required, -1))
    record = dict(identity=name, actual=encode(actual), required=encode(required),
                  difference=encode(difference), passed=not difference)
    if raw is not None:
        record["before_parity"] = encode(raw)
    if variables is not None:
        record["variables"] = variables
    records.append(record)


d = [var(j) for j in range(3)]
eta = [var(j + 3) for j in range(3)]
lam = add(*(mul(x, x) for x in d))
planes = [(0, 1), (0, 2), (1, 2)]
one = {(0,) * 6: F(1)}
z_rows, f_rows = [], []

# Construct the exact b dot d and q dot d directly from both complex paths.
for a, b in planes:
    bre = add(mul(eta[b], d[a]), mul(eta[a], d[b]))
    bim = add(scale(mul(d[b], d[a]), F(-1, 2)),
              scale(mul(d[a], d[b]), F(1, 2)))
    qre = add(scale(mul(eta[b], d[a]), -1), mul(eta[a], d[b]))
    qim = add(scale(mul(d[b], d[a]), F(-1, 2)),
              scale(mul(d[a], d[b]), F(1, 2)))
    z_rows.append([scale(d[b], -1) if j == a else d[a] if j == b else {}
                   for j in range(3)])
    f = []
    for r in range(3):
        real = add(qre, bre) if r == a else add(qre, scale(bre, -1)) if r == b else {}
        imag = add(qim, bim) if r == a else add(qim, scale(bim, -1)) if r == b else {}
        required = scale(mul(d[b], eta[a]), 2) if r == a else \
            scale(mul(d[a], eta[b]), -2) if r == b else {}
        check(f"path-{a+2}{b+2}-physical-{r+2}-real", real, required)
        check(f"path-{a+2}{b+2}-physical-{r+2}-imaginary", imag, {})
        f.append(real)
    f_rows.append(f)

# Entries of lambda Q, avoiding any numerical/singular inverse.
lq = [[add(lam if r == s else {}, scale(mul(d[r], d[s]), -1))
       for s in range(3)] for r in range(3)]

# All three physical basis inputs and all nine entries of alpha/i * lambda.
for r in range(3):
    for i in range(3):
        for j in range(3):
            actual = mul(d[i], add(*(mul(f[r], z[j])
                                     for f, z in zip(f_rows, z_rows))))
            required = scale(mul(d[i], eta[r], lq[r][j]), -2)
            check(f"alpha-physical-{r+2}-entry-{i+2}{j+2}", actual, required)

# The complete filtered bilinear matrix numerator is 4 E (lambda Q) E^2
# (lambda Q) E. Check all entries, retaining their raw polynomials.
diagonal = []
for r in range(3):
    for s in range(3):
        raw = scale(mul(eta[r], eta[s], add(*(
            mul(eta[b], eta[b], lq[r][b], lq[b][s]) for b in range(3)))), 4)
        required = {}
        if r == s:
            required = scale(mul(eta[r], eta[r], add(
                mul(eta[r], eta[r], lq[r][r], lq[r][r]),
                *(mul(eta[b], eta[b], d[r], d[r], d[b], d[b])
                  for b in range(3) if b != r))), 4)
            diagonal.append(raw)
        check(f"filtered-parity-entry-{r+2}{s+2}", even(raw), required, raw)

# Simultaneously swap each d coordinate and its eta coordinate.
for target in range(3):
    permutation = list(range(6))
    permutation[0], permutation[target] = permutation[target], permutation[0]
    permutation[3], permutation[target+3] = permutation[target+3], permutation[3]
    mapped = {}
    for power, coefficient in diagonal[0].items():
        pp = [0] * 6
        for j, exponent in enumerate(power):
            pp[permutation[j]] = exponent
        mapped[tuple(pp)] = coefficient
    check(f"diagonal-coordinate-permutation-{target+2}", mapped, diagonal[target])

# Verify the sign bookkeeping of the axial product derivative independently.
u, up, ell, ss, sp = [var(j) for j in range(5)]
original = add(scale(mul(u, ss), F(-1, 2)), scale(mul(ell, up, ss), -1),
               scale(mul(ell, u, sp), F(-1, 2)))
total_derivative = scale(add(mul(u, ss), mul(ell, up, ss), mul(ell, u, sp)), F(1, 2))
check("axial-IBP-kink-and-both-derivatives", add(original, total_derivative),
      scale(mul(ell, up, ss), F(-1, 2)),
      variables=["u1", "partial1_u1", "ell", "S", "partial1_S", "unused"])

tail = F(3, 4) * 20582100 * 1640736 * 2717908992 / 20**27
tail_required = F(1, 10**12)
endpoints = []
for probe, pd, required in [
    (3, (F("2359.1"), F("2359.2")), (F(786), F(1770))),
    (6, (F("703.6"), F("703.7")), (F(234), F(528))),
]:
    actual = (pd[0]/3, pd[1]*3/4)
    endpoints.append(dict(probe=probe, input_P_D=list(map(rat, pd)),
                          actual=list(map(rat, actual)), required=list(map(rat, required)),
                          passed=required[0] < actual[0] < actual[1] < required[1]))

failures = [row["identity"] for row in records if not row["passed"]]
failures.extend(f"endpoint-probe-{row['probe']}" for row in endpoints if not row["passed"])
if not tail < tail_required:
    failures.append("complete-spectral-tail")
certificate = dict(
    method="exact rational denominator-cleared polynomial checks and endpoint arithmetic",
    variables=["d2", "d3", "d4", "eta2", "eta3", "eta4"],
    qualifications="L139 proves angle integration, strict analytic scalar bounds, and IBP applicability. Imported full L133 heat intervals retain its IEEE model. No new quadrature.",
    algebra=records,
    scalar_bounds=dict(actual="proved analytically: 2/3<t_ax<3/2",
                       prefactor_bounds=list(map(rat, (F(1, 3), F(3, 4))))),
    endpoints=endpoints,
    full_cutoff96_tail=dict(actual_upper=rat(tail), required_upper=rat(tail_required),
                           passed=tail < tail_required),
    failures=failures,
    all_passed=not failures,
)
path = Path(__file__).with_name("ax-physical-reduction-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"exact algebra checks: {len(records)}; failures: {failures}")
print("analytic scalar bounds: 2/3 < t_ax < 3/2 (proof in L139)")
for row in endpoints:
    def value(r):
        return str(F(r["numerator"], r["denominator"]))
    print(f"probe {row['probe']}: actual endpoints {[value(x) for x in row['actual']]}; "
          f"required {[value(x) for x in row['required']]}; passed {row['passed']}")
print(f"full cutoff-96 tail upper: {float(tail):.12g}; required: {float(tail_required):.12g}")
print(f"certificate: {path}")
raise SystemExit(bool(failures))

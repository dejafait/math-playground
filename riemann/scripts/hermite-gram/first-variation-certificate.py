#!/usr/bin/env python3
"""Exact bounded falsification of the actual Hermite first variation.

Reuse C567a's audited full coefficient enclosures. L564 (4) encloses
the infinite Hermite tail and its first two derivatives. No floating
arithmetic or independent evaluation of Xi enters the certificate.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / "global-dual-pairing-certificate.json"
AUDIT = HERE / "c567a-audit-replay-comparison.json"
OUT = HERE / "first-variation-certificate.json"
N, M = 64, 256
PROBES = [F(1), F(5, 4), F(3, 2), F(7, 4), F(2)]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(a, c):
    return (a[0] * c, a[1] * c) if c >= 0 else (a[1] * c, a[0] * c)


def mul(a, b):
    products = [x * y for x in a for y in b]
    return min(products), max(products)


def enc(a):
    return [str(x) for x in a]


def coarse(a):
    """Six significant decimal digits, exact outward rounding."""
    maximum = max(map(abs, a))
    if not maximum:
        return ["0", "0"]
    exponent = len(str(maximum.numerator)) - len(str(maximum.denominator))
    while maximum < F(10) ** exponent:
        exponent -= 1
    while maximum >= F(10) ** (exponent + 1):
        exponent += 1
    unit = F(10) ** (exponent - 5)
    lo, hi = a[0] / unit, a[1] / unit
    lower = lo.numerator // lo.denominator
    upper = -((-hi.numerator) // hi.denominator)
    result = [f"{lower}e{exponent-5}", f"{upper}e{exponent-5}"]
    assert F(result[0]) <= a[0] <= a[1] <= F(result[1])
    return result


def load_coefficients():
    raw = SOURCE.read_bytes()
    certificate = json.loads(raw)
    audit = json.loads(AUDIT.read_text())
    digest = sha256(raw).hexdigest()
    assert digest == audit["retained_sha256"]
    assert audit["status"] == "PASS" and not audit["failures"]
    assert all(audit["all_mathematical_fields_equal"].values())
    assert audit["fresh_node_values_reused"] is False
    assert certificate["status"] == "PASS" and not certificate["failures"]
    assert certificate["parameters"] == dict(
        bits=2048, exp_order=320, degree=256, panels=128,
        length="1/32", limit=4, theta_terms=24)
    assert len(certificate["coefficients_b_even"]) == M + 1
    weight_norm = sum(abs(F(w)) for w in certificate["weights"])
    assert weight_norm == F(certificate["absolute_weight_norm"])
    coefficients = []
    checks = []
    for n in range(M + 1):
        raw_lo, raw_hi = map(int, certificate["integral_totals_fixedpoint"][n])
        interpolation = 8 * F(2)**60 * F(9, 2)**(2*n) * F(16)**(-257)
        theta = 512 * weight_norm * 3**18 * F(2)**(-1849) * 4**(2*n)
        spatial = 19200 * 3**18 * 4**(2*n) * F(2)**(-3072)
        assert certificate["remainders"][n] == dict(
            interpolation=str(interpolation), theta=str(theta), spatial=str(spatial))
        moment = (2*F(raw_lo, 2**2048) - interpolation - theta,
                  2*F(raw_hi, 2**2048) + interpolation + theta + spatial)
        assert enc(moment) == certificate["moments"][n]
        coefficient = scale(moment, F(1, 2**(2*n)*factorial(2*n)))
        assert enc(coefficient) == certificate["coefficients_b_even"][n]
        assert coefficient[0] <= coefficient[1]
        coefficients.append(coefficient)
        checks.append(dict(n=n, complete_moment_and_coefficient_match=True))
    return coefficients, digest, checks


def evaluate(coefficients, t):
    assert 1 <= t <= 2
    h = [F(1), 2*t]
    for j in range(1, 2*M):
        h.append(2*t*h[-1] - 2*j*h[-2])
    # Independent finite formula, every degree used in all three jets.
    formula_matches = []
    for j in range(2*M + 1):
        explicit = sum((F((-1)**r * factorial(j), factorial(r)*factorial(j-2*r))
                        * (2*t)**(j-2*r) for r in range(j//2 + 1)), F(0))
        assert explicit == h[j]
        formula_matches.append(True)
    p = [(F(0), F(0)) for _ in range(3)]
    tail_finite = [(F(0), F(0)) for _ in range(3)]
    for n, coefficient in enumerate(coefficients):
        j = 2*n
        values = [h[j], 2*j*h[j-1] if j else F(0),
                  4*j*(j-1)*h[j-2] if j else F(0)]
        destination = p if n <= N else tail_finite
        for derivative in range(3):
            destination[derivative] = add(destination[derivative], scale(
                coefficient, (-1)**n*values[derivative]))
    # L564 (4); exp(t^2/2) <= exp(2) < 9 on [1,2].
    error = 45000 * F(4*M + 5, 5**M)
    assert error < F("5.36176e-172")
    r = [add(v, (-error, error)) for v in tail_finite]
    terms = [scale(mul(p[1], r[1]), F(2)),
             scale(mul(p[0], r[2]), F(-1)),
             scale(mul(r[0], p[2]), F(-1))]
    b = add(add(terms[0], terms[1]), terms[2])
    rounded = coarse(b)
    assert F(rounded[0]) <= b[0] <= b[1] <= F(rounded[1])
    return dict(
        t=str(t), hermite_values=[str(v) for v in h],
        finite_formula_matches=formula_matches,
        P_jets=[enc(v) for v in p], finite_R_jets=[enc(v) for v in tail_finite],
        infinite_tail_error_each_derivative=str(error),
        infinite_tail_error_below_stated_bound=error < F("5.36176e-172"),
        R_jets=[enc(v) for v in r], B_terms=[enc(v) for v in terms],
        B=enc(b), coarse_B=rounded,
        negative_certified=b[1] < 0,
        coefficient_uncertainty_widths_R=[str(v[1]-v[0]) for v in tail_finite],
        coarse_P_jets=[coarse(v) for v in p], coarse_R_jets=[coarse(v) for v in r],
        coarse_B_terms=[coarse(v) for v in terms],
        coarse_infinite_tail_error=coarse((error, error)))


def main():
    coefficients, digest, checks = load_coefficients()
    rows = []
    for t in PROBES:
        row = evaluate(coefficients, t)
        rows.append(row)
        print("probe", t, "certified B interval", row["coarse_B"], flush=True)
        if row["negative_certified"]:
            break
    negative = any(row["negative_certified"] for row in rows)
    # The exact claim recorded in L568, independently of decimal display.
    first_b = tuple(map(F, rows[0]["B"]))
    assert F("-2.75514e-128") <= first_b[0] <= first_b[1] <= F("-2.75513e-128")
    result = dict(
        status="NEGATIVE_WITNESS" if negative else "NO_NEGATIVE_PROBE",
        target="B_64(t)>=0 for every t in [1,2]",
        required="An upper bound strictly below 0 at one approved probe stops the proposed sign.",
        parameters=dict(T=1, N=N, M=M, derivative_orders=[0, 1, 2]),
        source=str(SOURCE.relative_to(ROOT)), source_sha256=digest,
        source_audit=str(AUDIT.relative_to(ROOT)),
        source_audit_sha256=sha256(AUDIT.read_bytes()).hexdigest(),
        coefficient_postprocessing_checks=checks,
        coefficients_b_even=[enc(v) for v in coefficients],
        approved_probes=[str(t) for t in PROBES],
        stop_at_first_negative=True, evaluated_probes=len(rows), probes=rows,
        failures=[],
        limitations=["Reuses audited coefficient data; no fresh theta-node replay.",
                     "A negative first variation is not a negative Xi discriminant.",
                     "No all-height, interval-margin, higher-form, or RH conclusion."],
        arithmetic="Python standard-library integers and exact Fractions only.")
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("status", result["status"], "required upper bound < 0")
    print("failures", result["failures"], "certificate", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()

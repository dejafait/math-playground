#!/usr/bin/env python3
"""Approved degree24 diagnostic; an absent runtime yields no mathematical claim.

Protocol/citations: drafts/literature/2026-11-20-tilted-pollaczek-inertia-source-review-2001.md
Run: python3 scripts/pollaczek/tilted_degree24_inertia_2002.py
"""

import hashlib
import json
import platform
import sys
from fractions import Fraction
from math import factorial
from pathlib import Path


DEGREE = 24
PRECISIONS = (256, 512, 1024, 2048)
OUTPUT = Path(__file__).with_name("tilted-degree24-inertia-2002.json")


def save(certificate):
    temporary = OUTPUT.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(certificate, indent=2) + "\n")
    temporary.replace(OUTPUT)


def main():
    certificate = {
        "target": "Certify the Hermite-matrix inertia of Kuznetsov's Jensen-weighted tilted-Xi Pollaczek truncation at degree 24, testing whether its negative index is at most one.",
        "assessment": "drafts/literature/2026-11-20-tilted-pollaczek-degree24-inertia-2000.md",
        "method": "Kuznetsov2008 (2)/(4)/(13); Newton sums; Arb leading determinants; Coste p19 Jacobi",
        "implementation_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version,
        "executable": sys.executable,
        "platform": platform.platform(),
        "precision_ladder_bits": list(PRECISIONS),
        "required": {"degree": 24, "coefficients": 25, "newton_sums": 47,
                     "nonzero_leading_determinants": 24, "maximum_negative_index": 1},
        "runs": [],
        "failures": [],
        "actual": {"evaluated_coefficients": 0, "evaluated_determinants": 0},
        "conclusion": {"degree": None, "inertia_positive_negative_null": None,
                       "one_pair_test": "UNRESOLVED"},
        "status": "STARTED",
    }
    save(certificate)
    try:
        import flint
        from flint import arb, arb_mat, ctx
    except ImportError as error:
        certificate["status"] = "RUNTIME_BLOCKED"
        certificate["failures"].append({"stage": "import", "error": str(error)})
        save(certificate)
        print("RUNTIME_BLOCKED: actual coefficients=0/25, determinants=0/24; negative index unresolved (required <=1).")
        print(f"Failure: {error}. Certificate: {OUTPUT}")
        return 2

    certificate["versions"] = {
        "python_flint": str(getattr(flint, "__version__", "UNREPORTED")),
        "flint": str(getattr(flint, "__FLINT_VERSION__", "UNREPORTED")),
    }
    # Basis in ascending monomial order, computed with exact rational arithmetic.
    basis = [[Fraction(1)]]
    for n in range(DEGREE):
        following = [Fraction(0)] * (n + 2)
        for j, value in enumerate(basis[n]):
            following[j + 1] += value / (n + 1)
        if n:
            for j, value in enumerate(basis[n - 1]):
                following[j] -= Fraction(2 * n + 1, 2 * (n + 1)) * value
        basis.append(following)
    weights = [Fraction(factorial(DEGREE), factorial(DEGREE - k) * DEGREE**k)
               for k in range(DEGREE + 1)]
    certificate["basis_exact_ascending"] = [[str(x) for x in row] for row in basis]
    certificate["weights_exact"] = [str(x) for x in weights]

    def ball_rational(value):
        return arb(value.numerator) / value.denominator

    def sign(value):
        if value > 0:
            return 1
        if value < 0:
            return -1
        return None  # Includes exact zero, nonfinite and undecided enclosures.

    def encode(value):
        return {"ball": value.str(ctx.dps + 20, radius=True, more=True),
                "raw_repr": value.repr(), "sign": sign(value)}

    for precision in PRECISIONS:
        ctx.prec = precision
        run = {"precision_bits": precision, "status": "STARTED",
               "leading_determinants": [], "failures": []}
        certificate["runs"].append(run)
        save(certificate)
        try:
            pi = arb.pi()
            bernoulli = {j: arb.bernoulli(j) for j in range(2, 55, 2)}
            u = []
            for n in range(DEGREE + 3):
                total = arb(0)
                for k in range(n + 1):
                    angle = pi * ball_rational(Fraction(n - k, 2) + Fraction(1, 8))
                    total += (4**k * (4**(k + 1) - 1) * bernoulli[2 * k + 2]
                              * (2 * pi)**(k + 1) * angle.sin()
                              / (factorial(n - k) * factorial(2 * k + 2)))
                u.append(-factorial(n) * total / arb(2).sqrt())
            beta = []
            for n in range(DEGREE + 1):
                value = ((8 * n*n + 12 * n + 7) * u[n]
                         + (2*n + 3) * (2*n + 5) * u[n + 2])
                if n >= 2:
                    value += 4 * n * (n - 1) * u[n - 2]
                beta.append(value)
            coefficients = [arb(0) for _ in range(DEGREE + 1)]
            for k in range(DEGREE + 1):
                for j, value in enumerate(basis[k]):
                    coefficients[j] += beta[k] * ball_rational(weights[k] * value)
            run["bernoulli"] = {str(j): encode(v) for j, v in bernoulli.items()}
            run["u"] = [encode(v) for v in u]
            run["beta"] = [encode(v) for v in beta]
            run["coefficients_ascending"] = [encode(v) for v in coefficients]
            certificate["actual"]["evaluated_coefficients"] += len(coefficients)
            if sign(coefficients[DEGREE]) is None:
                run["status"] = "UNRESOLVED_DEGREE"
                run["failures"].append("Leading coefficient enclosure does not exclude zero.")
                save(certificate)
                continue
            run["certified_degree"] = DEGREE
            a = [coefficients[DEGREE - j] / coefficients[DEGREE]
                 for j in range(1, DEGREE + 1)]
            sums = [arb(DEGREE)]
            for k in range(1, 2 * DEGREE - 1):
                if k <= DEGREE:
                    value = k * a[k - 1]
                    for j in range(1, k):
                        value += a[j - 1] * sums[k - j]
                else:
                    value = arb(0)
                    for j in range(1, DEGREE + 1):
                        value += a[j - 1] * sums[k - j]
                sums.append(-value)
            run["monic_coefficients_descending_after_lead"] = [encode(v) for v in a]
            run["newton_sums"] = [encode(v) for v in sums]
            save(certificate)
            for j in range(1, DEGREE + 1):
                determinant = arb_mat([[sums[r + c] for c in range(j)]
                                       for r in range(j)]).det()
                run["leading_determinants"].append({"order": j, **encode(determinant)})
                certificate["actual"]["evaluated_determinants"] += 1
                save(certificate)
            signs = [1] + [v["sign"] for v in run["leading_determinants"]]
            unresolved = [j for j in range(1, DEGREE + 1) if signs[j] is None]
            if unresolved:
                run["status"] = "UNRESOLVED_MINORS"
                run["failures"].append({"zero_containing_orders": unresolved})
                save(certificate)
                print(f"bits={precision}: unresolved determinant orders={unresolved}; no index claimed.")
                continue
            negative = sum(left != right for left, right in zip(signs, signs[1:]))
            inertia = [DEGREE - negative, negative, 0]
            run["status"] = "CERTIFIED"
            run["inertia_positive_negative_null"] = inertia
            certificate["status"] = "CERTIFIED"
            certificate["conclusion"] = {
                "degree": DEGREE, "inertia_positive_negative_null": inertia,
                "distinct_real_roots": DEGREE - 2 * negative,
                "distinct_nonreal_conjugate_pairs": negative,
                "simple_roots": True,
                "one_pair_test": "PASS_FINITE_ONLY" if negative <= 1 else "STOP_UNIFORM_ONE_PAIR_BOUND",
            }
            save(certificate)
            print(f"CERTIFIED bits={precision}, degree={DEGREE}, inertia={inertia}; actual negative index={negative}, required <=1.")
            print(f"Certificate: {OUTPUT}")
            return 0
        except Exception as error:
            run["status"] = "IMPLEMENTATION_ERROR"
            run["failures"].append({"type": type(error).__name__, "error": str(error)})
            certificate["status"] = "IMPLEMENTATION_ERROR"
            save(certificate)
            print(f"Implementation failure: {error}. No inertia claimed. Certificate: {OUTPUT}")
            return 2
    certificate["status"] = "UNRESOLVED_AT_PRECISION_CEILING"
    save(certificate)
    print(f"UNRESOLVED through {PRECISIONS[-1]} bits; negative index unknown, required <=1. Certificate: {OUTPUT}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

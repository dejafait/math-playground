"""Exact diagnostic for review297; finite values do not establish a rate."""
from fractions import Fraction
from math import factorial, log, comb
from pathlib import Path
import json


def partitions(weight, length_cap, minimum=1):
    if weight == 0:
        yield ()
    elif length_cap:
        for j in range(minimum, weight + 1):
            for tail in partitions(weight - j, length_cap - 1, j):
                yield (j,) + tail


def cw(parts):
    r = len(parts)
    denominator = 1
    for j in set(parts):
        denominator *= factorial(parts.count(j)) * factorial(j) ** parts.count(j)
    return Fraction((-1) ** (r - 1) * factorial(r - 1), denominator)


def exact(n):
    coefficients = {p: 2 * n * cw(p) for p in partitions(2 * n, n)}
    half = [(p, cw(p)) for p in partitions(n, n)]
    ordered_pairs = 0
    for p, cp in half:
        for q, cq in half:
            if len(p) + len(q) <= n:
                ell = tuple(sorted(p + q))
                coefficients[ell] += n * n * cp * cq
                ordered_pairs += 1
    mass = sum(map(abs, coefficients.values()), Fraction(0))
    return {
        "n": n, "C_n": str(mass), "float_C_n": float(mass),
        "log_max_mass_over_n": log(max(1, mass)) / n,
        "full_vectors": len(coefficients), "ordered_pairs": ordered_pairs,
        "nonzero_vectors": sum(bool(c) for c in coefficients.values()),
        "coefficients": [{"parts": list(p), "value": str(c)}
                         for p, c in coefficients.items()],
    }


def balanced(m):
    n = r = 3 * m
    # Ratio of the entire second-family magnitude to the first one.
    ratio = Fraction(0)
    for a in range(m + 1):
        for b in range(m + 1):
            remainder = n - a - 2 * b
            if remainder < 0 or remainder % 3:
                continue
            c = remainder // 3
            if c > m:
                continue
            q = a + b + c
            if not 0 < q < r:
                continue
            ratio += Fraction(n * r * comb(m, a) * comb(m, b) * comb(m, c),
                              2 * q * (r - q) * comb(r, q))
    first = Fraction((-1) ** (r - 1) * 6 * m * factorial(r - 1),
                     factorial(m) ** 3 * 12 ** m)
    actual = first * (1 - ratio)
    formula = Fraction((-1) ** m * 3 * comb(2 * m, m), 12 ** m)
    bound = Fraction(3, 3 ** m)
    assert actual == formula and abs(actual) <= bound
    return {"m": m, "direct_coefficient": str(actual),
            "formula": str(formula), "required_upper_bound": str(bound),
            "ratio_second_to_first_magnitude": str(ratio),
            "identity_verified": True, "bound_verified": True}


if __name__ == "__main__":
    rows = [exact(n) for n in range(1, 13)]
    balanced_rows = [balanced(m) for m in range(1, 31)]
    path = Path(__file__).with_name("collected_mass_299_certificate.json")
    path.write_text(json.dumps({
        "scope": "Exact formal collection; no arithmetic interpretation or asymptotic proof",
        "required_rate": 0, "rows": rows, "balanced": balanced_rows,
        "failures": [],
    }, indent=2) + "\n")
    for row in rows:
        print(f"n={row['n']} C_n={row['C_n']} rate_preview={row['log_max_mass_over_n']:.8g}")
    print("Required asymptotic rate: 0; finite diagnostics do not decide it.")
    print("Balanced coefficients: direct ordered-split checks m=1..30 pass;")
    print("actual equals (-1)^m*3*binom(2m,m)/12^m; required |b|<=3^(1-m) passes.")
    print("Failures: 0. General identity requires the L999 proof.")
    print(f"Certificate: {path}")

#!/usr/bin/env python3
"""Exact finite certificate for L772; infinite assertions are proved in prose.

Run from the notebook: python3 scripts/coefficient-countermodel/strong-log-order-five-408.py
Only the standard library is used. No finite iterate test is an all-order proof.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json


def rational(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


def determinant(matrix):
    terms = []
    for p in permutations(range(len(matrix))):
        inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
        term = F((-1) ** inversions)
        for i, j in enumerate(p):
            term *= matrix[i][j]
        terms.append({"permutation": list(p), "term": rational(term)})
    total = sum((F(t["term"]["numerator"], t["term"]["denominator"]) for t in terms), F(0))
    return total, terms


b = [F(1, 10**12), F(1, 10**6), F(1, 100), F(3, 5), F(1),
     F(3, 5), F(1, 100), F(1, 10**6), F(1, 10**12)]
required = F(11, 4)
matrix = [[b[4 + j - i] for j in range(5)] for i in range(5)]
det, terms = determinant(matrix)
ratios = [b[n]**2 / (b[n - 1] * b[n + 1]) for n in range(1, 8)]
b9 = b[8] * F(1, 10**6) / 4
junction = b[8]**2 / (b[7] * b9)
# The reference determinant is motivation, not a replacement for the exact one.
reference = [[F(1) if i == j else F(3, 5) if abs(i - j) == 1 else F(0)
              for j in range(5)] for i in range(5)]
reference_det, _ = determinant(reference)
a, d, e, f = F(3, 5), F(1, 100), F(1, 10**6), F(1, 10**12)
odd_block = [[1 - f, a - e], [a - e, 1 - d]]
even_block = [[1 + f, a + e, d], [a + e, 1 + d, a], [2*d, 2*a, F(1)]]
odd_det, _ = determinant(odd_block)
even_det, _ = determinant(even_block)
checks = {
    "prefix_positive": all(x > 0 for x in b),
    "prefix_ratios_meet_bound": all(x >= required for x in ratios),
    "junction_meets_bound": junction >= required,
    "determinant_negative": det < 0,
    "reference_determinant": reference_det == F(-32, 625),
    "reversal_block_factorization": det == odd_det * even_det,
    "odd_block_positive": odd_det > 0,
    "even_block_negative": even_det < 0,
    "r0_below_required_via_sqrt5_lt_5_over_2": F(5) < F(25, 4),
}
certificate = {
    "lemma": "L772",
    "arithmetic": "exact fractions; determinant expanded over all 120 permutations",
    "prefix": [rational(x) for x in b],
    "matrix": [[rational(x) for x in row] for row in matrix],
    "required_ratio": rational(required),
    "prefix_ratios_n1_through_n7": [rational(x) for x in ratios],
    "b9": rational(b9),
    "junction_ratio_n8": rational(junction),
    "determinant": rational(det),
    "scaled_integer_matrix_determinant": int(det * 10**60),
    "determinant_terms": terms,
    "reference_determinant": rational(reference_det),
    "reversal_blocks": {
        "odd": [[rational(x) for x in row] for row in odd_block],
        "even": [[rational(x) for x in row] for row in even_block],
        "odd_determinant": rational(odd_det),
        "even_determinant": rational(even_det),
    },
    "checks": checks,
    "failures": [key for key, value in checks.items() if not value],
    "infinite_obligations": {
        "tail": "b_(8+k)=10^-12*(10^-6)^k*4^(-k(k+1)/2), k>=0",
        "ratio": "b_n^2/(b_(n-1)b_(n+1))=4 for every n>=8, including junction",
        "entire": "b_(n+1)/b_n=10^-6*4^(-(n-7)) for n>=8 tends to zero",
        "iterates": "McNamara-Sagan 0808.1065v2 Lemma2.1 plus positive-boundary induction; see L772",
        "scope": "These universal statements require the canonical proof; finite arithmetic alone does not verify them."
    },
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"D_(5,4) = {det} < 0 required: {det < 0}")
print(f"Prefix ratios n=1,...,7: {', '.join(map(str, ratios))}; required >= {required}")
print(f"Junction ratio n=8: {junction}; required >= {required}")
print(f"Reversal block determinants: {odd_det}, {even_det}")
print(f"Failures: {certificate['failures']}; certificate: {path}")
raise SystemExit(bool(certificate["failures"]))

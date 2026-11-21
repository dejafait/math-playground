"""Exact certificate for the approved q=1/2 cubic second-ray test.

Run from the active notebook: python3 scripts/dyadic-cubic/second_ray_exact.py
The analytic and Jacobi--Trudi justifications are in L842; this script
certifies only the finite rational arithmetic, by two different routes.
"""

from fractions import Fraction as Q
from itertools import permutations
import json
from pathlib import Path


def determinant(matrix):
    """Leibniz sum, including every permutation; no pivot divisions."""
    total = Q(0)
    terms = []
    for perm in permutations(range(len(matrix))):
        inversions = sum(
            perm[i] > perm[j]
            for i in range(len(perm))
            for j in range(i + 1, len(perm))
        )
        term = Q((-1) ** inversions)
        for row, col in enumerate(perm):
            term *= matrix[row][col]
        total += term
        terms.append({"permutation": list(perm), "signed_term": str(term)})
    return total, terms


def coeff(sequence, index):
    return sequence[index] if index >= 0 else Q(0)


# F(z)=P(z)F(z/2) and P(-t)H(t)=H(t/2), H(t)=1/F(-t).
a = [Q(1)]
h = [Q(1)]
p = [1, 2, 2, 1]
for n in range(1, 7):
    denominator = 1 - Q(1, 2**n)
    a.append(sum(
        (p[k] * a[n-k] * Q(1, 2**(n-k))
         for k in range(1, min(3, n) + 1)), Q(0)
    ) / denominator)
    h.append((2 * coeff(h, n-1) - 2 * coeff(h, n-2)
              + coeff(h, n-3)) / denominator)

reciprocal_checks = [
    sum(((-1)**k * a[k] * h[n-k] for k in range(n+1)), Q(0))
    == (1 if n == 0 else 0)
    for n in range(7)
]
rays = []
for rank in range(1, 6):
    matrix = [[coeff(a, 2+j-i) for j in range(rank)]
              for i in range(rank)]
    direct, terms = determinant(matrix)
    rectangular = h[rank]**2 - h[rank-1] * h[rank+1]
    rays.append({
        "rank": rank,
        "matrix": [[str(x) for x in row] for row in matrix],
        "direct_determinant": str(direct),
        "rectangular_expression": str(rectangular),
        "methods_agree": direct == rectangular,
        "negative": direct < 0,
        "leibniz_terms": terms,
    })

checks = {
    "reciprocity_degrees_0_through_6": all(reciprocal_checks),
    "all_five_direct_and_rectangular_values_agree": all(
        item["methods_agree"] for item in rays),
    "ranks_1_through_4_strictly_positive": all(
        Q(item["direct_determinant"]) > 0 for item in rays[:4]),
    "rank_5_exact_value": rays[4]["direct_determinant"]
        == "-1409024/2966607",
    "rank_5_below_required_zero_bound": rays[4]["negative"],
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "scope": "Exact finite arithmetic only; see L842 for analytic justification.",
    "polynomial_coefficients": p,
    "dyadic_ratio": "1/2",
    "a_0_through_6": [str(x) for x in a],
    "h_0_through_6": [str(x) for x in h],
    "rays": rays,
    "rank5": {key: value for key, value in rays[4].items()
              if key != "leibniz_terms"},
    "required_lower_bound": "0",
    "checks": checks,
    "failures": failures,
}
destination = Path(__file__).with_name("second-ray-exact-certificate.json")
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print("rank=5; actual determinant=-1409024/2966607; required lower bound=0")
print(f"checks={len(checks)}; passed={len(checks)-len(failures)}; failures={failures}")
print(f"certificate={destination.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))

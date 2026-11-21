"""Exact approved two-atom screen; no finite screen proves all orders."""

import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path


def encode(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def determinant(matrix):
    a = [row[:] for row in matrix]
    value = F(1)
    pivots = []
    for k in range(len(a)):
        row = next((i for i in range(k, len(a)) if a[i][k]), None)
        if row is None:
            return F(0), pivots
        if row != k:
            a[k], a[row] = a[row], a[k]
            value = -value
        pivot = a[k][k]
        pivots.append({"column": k, "selected_row": row, "value": encode(pivot)})
        value *= pivot
        for i in range(k + 1, len(a)):
            factor = a[i][k] / pivot
            for j in range(k + 1, len(a)):
                a[i][j] -= factor * a[k][j]
            a[i][k] = F(0)
    return value, pivots


def permutation_determinant(matrix):
    total = F(0)
    for p in itertools.permutations(range(5)):
        parity = sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) % 2
        total += (-1 if parity else 1) * math.prod(matrix[i][p[i]] for i in range(5))
    return total


def main():
    cases = []
    survivors = []
    failures = []
    counts = {"points": 0, "negative_determinants": 0, "zero_determinants": 0,
              "positive_determinants": 0, "screen_rejected": 0, "survivors": 0}
    for p in range(1, 16):
        for j in range(-8, 9):
            r, w = F(p, 16), F(2) ** j
            b = [(1 + w * r ** n) / math.factorial(2 * n) for n in range(13)]
            matrix = [[b[4 + col - row] for col in range(5)] for row in range(5)]
            det, pivots = determinant(matrix)
            independent = permutation_determinant(matrix)
            if det != independent:
                failures.append({"p": p, "j": j, "reason": "determinant methods disagree"})
            case = {"p": p, "j": j, "r": encode(r), "w": encode(w),
                    "initial_entries_0_through_12": [encode(x) for x in b],
                    "determinant": encode(det), "elimination_pivots": pivots,
                    "permutation_determinant": encode(independent), "screen": None}
            counts["points"] += 1
            counts[("negative" if det < 0 else "positive" if det > 0 else "zero") + "_determinants"] += 1
            if det < 0:
                layers, nonpositive = [], []
                a = b
                for depth in range(1, 5):
                    a = [a[n] ** 2 - (a[n - 1] * a[n + 1] if n else F(0))
                         for n in range(len(a) - 1)]
                    layers.append({"depth": depth, "last_index": len(a) - 1,
                                   "entries": [encode(x) for x in a]})
                    for n in range(9):
                        if a[n] <= 0:
                            nonpositive.append({"depth": depth, "index": n, "value": encode(a[n])})
                case["screen"] = {"layers": layers, "nonpositive_target_entries": nonpositive,
                                  "passes": not nonpositive}
                if nonpositive:
                    counts["screen_rejected"] += 1
                else:
                    survivors.append({"p": p, "j": j, "determinant": encode(det)})
                    counts["survivors"] += 1
            cases.append(case)
    assert counts["points"] == 255
    report = {
        "scope": "r=p/16, 1<=p<=15; w=2^j, -8<=j<=8; D_(5,4); depths 1..4, n=0..8",
        "arithmetic": "Python fractions; exact rational elimination and independent 120-term determinant",
        "boundary": "zero at negative indices only; layer d stored through 12-d; no right zero extension",
        "counts": counts, "failures": failures, "survivors": survivors,
        "selected": survivors[0] if survivors else None, "cases": cases,
        "qualification": "Finite necessary screen only; all-order and all-position closure unproved."
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"counts": counts, "failures": failures, "selected": report["selected"],
                      "certificate": str(output)}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

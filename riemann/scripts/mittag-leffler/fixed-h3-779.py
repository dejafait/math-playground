#!/usr/bin/env python3
"""One fixed E_(3/2)(-w) logarithmic H_3, with rational certificates.

No external numerical packages. Machin's identity and alternating arctan
bounds enclose pi, then integer square roots enclose sqrt(pi). All later
arithmetic, including the final quadratic form, uses Fraction intervals.
Run from the active notebook: python3 scripts/mittag-leffler/fixed-h3-779.py
"""
from fractions import Fraction as Q
from math import factorial, isqrt
from pathlib import Path
import json


class I:
    def __init__(self, lo, hi=None):
        lo, hi = Q(lo), Q(lo if hi is None else hi)
        assert lo <= hi
        # Fixed outward rational rounding limits denominator growth. Every
        # rounded interval contains the exact unrounded interval.
        grid = 10 ** 60
        a, b = lo * grid, hi * grid
        self.lo = Q(a.numerator // a.denominator, grid)
        self.hi = Q(-((-b.numerator) // b.denominator), grid)

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        values = [a * b for a in (self.lo, self.hi)
                  for b in (other.lo, other.hi)]
        return I(min(values), max(values))

    __rmul__ = __mul__

    def inverse(self):
        assert self.lo * self.hi > 0
        return I(1 / self.hi, 1 / self.lo)

    def record(self):
        def rat(x):
            return {"numerator": str(x.numerator), "denominator": str(x.denominator)}
        return {"lower": rat(self.lo), "upper": rat(self.hi)}


def atan_reciprocal(d, terms):
    partial = sum((Q((-1) ** k, (2 * k + 1) * d ** (2 * k + 1))
                   for k in range(terms)), Q(0))
    next_term = Q((-1) ** terms, (2 * terms + 1) * d ** (2 * terms + 1))
    return I(min(partial, partial + next_term), max(partial, partial + next_term))


def solve(matrix, rhs):
    """Exact Gaussian elimination; only the prescribed leading block."""
    a = [list(row) + [value] for row, value in zip(matrix, rhs)]
    n = len(rhs)
    for j in range(n):
        assert a[j][j] != 0
        for k in range(j + 1, n):
            ratio = a[k][j] / a[j][j]
            for l in range(j, n + 1):
                a[k][l] -= ratio * a[j][l]
    out = [Q(0)] * n
    for j in reversed(range(n)):
        out[j] = (a[j][n] - sum(a[j][k] * out[k]
                               for k in range(j + 1, n))) / a[j][j]
    return out


def main():
    pi = 16 * atan_reciprocal(5, 60) - 4 * atan_reciprocal(239, 20)
    scale = 10 ** 60
    low_square = pi.lo * scale ** 2
    high_square = pi.hi * scale ** 2
    root_low = isqrt(low_square.numerator // low_square.denominator)
    root_high = isqrt(high_square.numerator // high_square.denominator) + 1
    sqrt_pi = I(Q(root_low, scale), Q(root_high, scale))
    assert sqrt_pi.lo ** 2 <= pi.lo <= pi.hi <= sqrt_pi.hi ** 2
    e = [I(1)]
    for n in range(1, 9):
        if n % 2 == 0:
            e.append(I(Q(1, factorial(3 * n // 2))))
        else:
            k = (3 * n + 1) // 2
            e.append(Q(4 ** k * factorial(k), factorial(2 * k)) * sqrt_pi.inverse())
    s = [I(0)]
    for k in range(1, 9):
        s.append(sum(((-1) ** (j - 1) * e[j] * s[k - j]
                      for j in range(1, k)), I(0))
                 + (-1) ** (k - 1) * k * e[k])
    h = [[s[i + j + 2] for j in range(4)] for i in range(4)]
    mid = [[(x.lo + x.hi) / 2 for x in row] for row in h]
    trial = solve([row[:3] for row in mid[:3]], [-row[3] for row in mid[:3]])
    # One fixed rounding, no parameter/dimension/adjacent-minor sweep.
    denominator = 10 ** 9
    v = [Q(round(x * denominator), denominator) for x in trial] + [Q(1)]
    q = sum((v[i] * v[j] * h[i][j] for i in range(4) for j in range(4)), I(0))
    coarse_upper = Q(-1, 10 ** 12)
    success = q.hi < 0
    # Certify the same single matrix by interval LDL^T. These pivots are
    # a definiteness test, not a search over other Hankel matrices.
    lower = [[I(int(i == j)) for j in range(4)] for i in range(4)]
    pivots = []
    pivot_floors = [Q(1, 10), Q(1, 10000), Q(1, 10 ** 7), Q(1, 10 ** 10)]
    for j in range(4):
        pivot = h[j][j] - sum((lower[j][k] * lower[j][k] * pivots[k]
                              for k in range(j)), I(0))
        pivots.append(pivot)
        assert pivot.lo > 0, "Cannot certify a positive pivot in this fixed test."
        for i in range(j + 1, 4):
            residual = h[i][j] - sum((lower[i][k] * lower[j][k] * pivots[k]
                                     for k in range(j)), I(0))
            lower[i][j] = residual * pivot.inverse()
    positive_definite = all(p.lo > 0 for p in pivots)
    record = {
        "model": "E_(3/2)(-t^2)",
        "definition": "S_k=-k[w^k]log(E_(3/2)(-w)); H_3[i,j]=S_(i+j+2)",
        "arctan_terms": {"5": 60, "239": 20},
        "pi": pi.record(), "sqrt_pi": sqrt_pi.record(),
        "e": [x.record() for x in e], "S": [x.record() for x in s],
        "H_3": [[x.record() for x in row] for row in h],
        "vector": [str(x) for x in v], "quadratic_form": q.record(),
        "required_upper": "0", "negative_direction_certified": success,
        "coarse_upper": str(coarse_upper), "coarse_upper_certified": q.hi < coarse_upper,
        "LDL_lower": [[x.record() for x in row] for row in lower],
        "LDL_pivots": [x.record() for x in pivots],
        "pivot_floors": [str(x) for x in pivot_floors],
        "pivot_floors_certified": [p.lo > bound for p, bound in zip(pivots, pivot_floors)],
        "positive_definite_certified": positive_definite,
        "failures": [] if success else ["Fixed rational vector did not certify negativity."],
        "scope": "One prescribed model/matrix/vector rounding; no sweep.",
        "interval_arithmetic": "Every operation rounded outward to the fixed rational grid 10^-60.",
        "implementation_note": "Unrounded LDL serialization exceeded Python's 4300-digit limit; fixed outward rational rounding repaired this without changing the model or matrix."
    }
    output = Path(__file__).with_name("fixed-h3-779.json")
    output.write_text(json.dumps(record, indent=2) + "\n")
    print("negative_direction_certified:", success)
    print("vector:", [str(x) for x in v])
    print("quadratic interval (display only):", float(q.lo), float(q.hi))
    print("required upper: 0; coarse upper:", coarse_upper,
          "; certified:", q.hi < coarse_upper)
    print("failures:", record["failures"])
    print("same-matrix LDL pivots (display only):", [float(x.lo) for x in pivots])
    print("strict rational pivot floors:", [str(x) for x in pivot_floors])
    print("floors certified:", record["pivot_floors_certified"])
    print("positive_definite_certified:", positive_definite)
    print("full rational certificate:", output)


if __name__ == "__main__":
    main()

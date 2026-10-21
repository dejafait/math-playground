"""Exact six-field check for L021, including both pairing classes.

Finite rational covariance data test the formula for arbitrary symmetric
residual matrices. This is not a numerical box/coefficient asymptotic.
Run: python3 scripts/combined-ward-response/check_radial_remaining_pairings.py
"""
from fractions import Fraction as F


def pairings(indices):
    if not indices:
        yield ()
        return
    first, *rest = indices
    for j, partner in enumerate(rest):
        for tail in pairings(rest[:j] + rest[j + 1:]):
            yield ((first, partner),) + tail


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def bilinear(x, matrix, y):
    return sum(x[j] * matrix[j][k] * y[k]
               for j in range(3) for k in range(3))


unit = tuple(tuple(F(j == k) for j in range(3)) for k in range(3))
rows = (
    ((F(1), F(2), F(-1)), (F(2), F(-1), F(3))),
    ((F(1, 2), F(-2, 3), F(3, 4)), (F(-1), F(3, 2), F(2))),
    ((F(0), F(1), F(0)), (F(1), F(0), F(1))),
)
residuals = (
    ((F(2), F(-1), F(3)), (F(-1), F(-2), F(1)), (F(3), F(1), F(0))),
    ((F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))),
)
connected_pairings = [p for p in pairings(list(range(6))) if (4, 5) not in p]
cases = 0
for colors in (1, 2, 3, 4):
    for h, z in rows:
        for residual in residuals:
            internal = external = F(0)
            for c in range(colors):
                for b in range(colors):
                    for color_r in range(colors):
                        for j in range(3):
                            for k in range(3):
                                fields = ((z, c), (h, b), (h, b), (h, c),
                                          (unit[j], color_r), (unit[k], color_r))
                                for pairs in connected_pairings:
                                    value = residual[j][k]
                                    for left, right in pairs:
                                        vl, cl = fields[left]
                                        vr, cr = fields[right]
                                        value *= dot(vl, vr) if cl == cr else 0
                                    is_internal = any(left in (1, 2, 3) and right in (1, 2, 3)
                                                      for left, right in pairs)
                                    if is_internal:
                                        internal += value
                                    else:
                                        external += value
            factor = 2 * colors * (colors + 2)
            predicted_internal = factor * dot(h, h) * bilinear(z, residual, h)
            predicted_external = factor * dot(z, h) * bilinear(h, residual, h)
            assert internal == predicted_internal
            assert external == predicted_external
            assert (internal + external) / 12 == F(colors * (colors + 2), 6) * (
                dot(h, h) * bilinear(z, residual, h)
                + dot(z, h) * bilinear(h, residual, h))
            cases += 1
assert F(3 * (3 + 2), 6) == F(5, 2)
print(f"PASS: {cases} exact rational cases; internal and external pairings separately agree.")
print("Three-color radial-response prefactor: 5/2. No box asymptotic is tested here.")

"""Exact connected eight-field check for L023's radial action insertion.

Run: python3 scripts/combined-ward-response/check_radial_action_pairings.py
This tests the cumulant and color factors, not the box cutoff asymptotic.
The full finite certificate is saved next to this script.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def pairings(indices):
    if not indices:
        yield ()
        return
    first, *rest = indices
    for j, partner in enumerate(rest):
        for tail in pairings(rest[:j] + rest[j + 1:]):
            yield ((first, partner),) + tail


groups = (0, 0, 1, 1, 2, 2, 2, 2)


def connected(pairs):
    reached = {0}
    while True:
        expanded = reached | {groups[j] for i, j in pairs if groups[i] in reached}
        expanded |= {groups[i] for i, j in pairs if groups[j] in reached}
        if expanded == reached:
            return len(reached) == 3
        reached = expanded


classes = {0: [], 1: []}
for pairs in pairings(list(range(8))):
    if connected(pairs):
        internal = sum(i >= 4 and j >= 4 for i, j in pairs)
        assert internal in classes
        classes[internal].append(pairs)


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def bilinear(x, matrix, y):
    return sum(x[j] * matrix[j][k] * y[k]
               for j in range(2) for k in range(2))


def multiply(left, right):
    return tuple(tuple(sum(left[j][l] * right[l][k] for l in range(2))
                       for k in range(2)) for j in range(2))


unit = ((F(1), F(0)), (F(0), F(1)))
matrices = (
    (((F(2), F(-1)), (F(-1), F(3))),
     ((F(-2), F(1)), (F(1), F(1)))),
    (((F(0), F(1)), (F(1), F(0))),
     ((F(3), F(-2)), (F(-2), F(-1)))),
)
rows = ((F(1), F(2)), (F(1, 2), F(-2, 3)))
certificate = []
for colors, (probe, residual), h in product((1, 2, 3, 4), matrices, rows):
    totals = {0: F(0), 1: F(0)}
    for c, d, b, e in product(range(colors), repeat=4):
        for j, k, l, m in product(range(2), repeat=4):
            coefficient = probe[j][k] * residual[l][m]
            if not coefficient:
                continue
            fields = ((unit[j], c), (unit[k], c),
                      (unit[l], d), (unit[m], d),
                      (h, b), (h, b), (h, e), (h, e))
            for internal, possibilities in classes.items():
                for pairs in possibilities:
                    value = coefficient
                    for left, right in pairs:
                        vl, cl = fields[left]
                        vr, cr = fields[right]
                        value *= dot(vl, vr) if cl == cr else 0
                        if not value:
                            break
                    totals[internal] += value
    v = dot(h, h)
    alpha = bilinear(h, probe, h)
    beta = bilinear(h, residual, h)
    chi = bilinear(h, multiply(probe, residual), h)
    expected = {0: 8 * colors * (colors + 2) * alpha * beta,
                1: 16 * colors * (colors + 2) * v * chi}
    assert totals == expected, (colors, probe, residual, h, totals, expected)
    assert sum(totals.values()) / 96 == F(colors * (colors + 2), 12) * (
        alpha * beta + 2 * v * chi)
    certificate.append({"colors": colors, "probe": str(probe),
                        "residual": str(residual), "row": str(h),
                        "fourth_chaos": str(totals[0]),
                        "quadratic_chaos": str(totals[1]),
                        "negative_radial_action_cumulant": str(sum(totals.values()) / 96)})
assert F(3 * 5, 12) == F(5, 4)
output = Path(__file__).with_name("radial-action-pairings-certificate.json")
output.write_text(json.dumps({"connected_pairing_counts": {
    str(k): len(v) for k, v in classes.items()}, "cases": certificate}, indent=2) + "\n")
print(f"PASS: {len(certificate)} exact rational cases; both connected pairing classes agree.")
print("Three-color action prefactor: 5/4; positive sign after -S4,rad.")
print("Actual/required cutoff bounds: not tested numerically; no full logarithm conclusion.")
print(f"Certificate: {output.relative_to(Path.cwd())}")

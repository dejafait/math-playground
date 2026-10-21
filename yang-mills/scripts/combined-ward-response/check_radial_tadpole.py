"""Exact pairing check for L020's selected internal contraction.

This checks its color and connected-covariance factors, not a numerical
evaluation of the original box or of the complete one-loop coefficient.
"""

from fractions import Fraction as F
from math import factorial


def pairings(indices):
    if not indices:
        yield ()
        return
    first, *rest = indices
    for j, partner in enumerate(rest):
        for tail in pairings(rest[:j] + rest[j + 1:]):
            yield ((first, partner),) + tail


# One color: X=U+V, Y=U+2W, Z=2U-V+W, for independent unit normals.
# Hence the covariance is positive definite, and both cross terms are nonzero.
coefficients = ((1, 1, 0), (1, 0, 2), (2, -1, 1))
cov = tuple(tuple(sum(a*b for a, b in zip(left, right))
                  for right in coefficients) for left in coefficients)

selected_connected = F(0)
for c in range(3):
    for b in range(3):
        for d in range(3):
            fields = ((0, c), (1, b), (1, b), (1, c), (2, d), (2, d))
            for pairs in pairings(list(range(6))):
                # The subtraction E[f] E[r] is exactly the pair (4,5).
                if (4, 5) in pairs:
                    continue
                # Retain only internal pairs in the three-input cubic vertex.
                if not any(i in (1, 2, 3) and j in (1, 2, 3) for i, j in pairs):
                    continue
                value = F(2)  # polarization of the outer quadratic probe
                for i, j in pairs:
                    kind_i, color_i = fields[i]
                    kind_j, color_j = fields[j]
                    value *= cov[kind_i][kind_j] if color_i == color_j else 0
                selected_connected += value

v = cov[1][1]
from_contracted_vertex = 12 * 5 * v * cov[0][2] * cov[1][2]
assert selected_connected == from_contracted_vertex == 1200

# Wilson numerator 4(1-cos(r/2)): its radial quartic coefficient and
# the negative gradient coefficient in the flow (before a^-2 D*).
radial_action4 = -F(4, 2**4 * factorial(4))
assert radial_action4 == -F(1, 96)
assert -4 * radial_action4 == F(1, 24)
print("Exact selected six-field pairings agree: 1200; color factor 5 and covariance factor 12.")
print("Wilson radial action coefficient -1/96 and cubic flow coefficient +1/24 agree.")

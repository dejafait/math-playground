"""Exact algebra checks for L004; no interacting or asymptotic computation."""

from fractions import Fraction as F


planes = ((1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4))
n = len(planes)
identity = [[F(i == j) for j in range(n)] for i in range(n)]
scalar = [[F(1, 6) for _ in planes] for _ in planes]
stress_rows = {
    mu: [F(1 if mu in plane else -1) for plane in planes]
    for mu in range(1, 5)
}
tensor = [
    [(stress_rows[mu][j] + stress_rows[nu][j]) / 4 for j in range(n)]
    for mu, nu in planes
]
remainder = [
    [identity[i][j] - scalar[i][j] - tensor[i][j] for j in range(n)]
    for i in range(n)
]


def multiply(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


zero = [[F(0) for _ in planes] for _ in planes]
projectors = (scalar, tensor, remainder)
for i, left in enumerate(projectors):
    assert left == [list(row) for row in zip(*left)]
    for j, right in enumerate(projectors):
        assert multiply(left, right) == (left if i == j else zero)

ranks = [sum(p[i][i] for i in range(n)) for p in projectors]
assert ranks == [1, 3, 2]

for i, plane in enumerate(planes):
    complement = tuple(sorted({1, 2, 3, 4} - set(plane)))
    ci = planes.index(complement)
    assert remainder[i] == [
        (identity[i][j] + identity[ci][j]) / 2 - F(1, 6)
        for j in range(n)
    ]

plane_difference = [identity[0][j] - identity[5][j] for j in range(n)]
stress_difference = [
    (stress_rows[1][j] + stress_rows[2][j]
     - stress_rows[3][j] - stress_rows[4][j]) / 4
    for j in range(n)
]
assert plane_difference == stress_difference
assert multiply([plane_difference] * n, tensor)[0] == plane_difference
assert multiply([plane_difference] * n, scalar)[0] == [F(0)] * n
assert multiply([plane_difference] * n, remainder)[0] == [F(0)] * n

# Pairs encode a + b*y modulo y^2, with y = b0*g^2/epsilon.
def series_product(left, right):
    return (left[0] * right[0], left[0] * right[1] + left[1] * right[0])


coupling_z = (1, -1)
inverse_z = (1, 1)
scalar_z = series_product((1, 1), coupling_z)
assert scalar_z == (1, 0)
assert series_product(scalar_z, inverse_z) == (1, 1)
assert series_product(coupling_z, inverse_z) == (1, 0)

print("Exact plane projectors: orthogonal, ranks 1 + 3 + 2 = 6.")
print("Complementary-plane difference lies entirely in the stress sector.")
print("One-loop normalized residues: scalar b0, stress 0.")
print("No Wilson diagrams, reflection lower bound, or remainder estimated.")

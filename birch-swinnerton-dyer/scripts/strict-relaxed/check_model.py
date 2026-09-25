"""Exact matrix checks for L011's formal model, not an arithmetic example.

Run from the notebook: python3 scripts/strict-relaxed/check_model.py
Coordinates over F[epsilon]/epsilon^2 are (v_1, v_2, epsilon*v_1,
epsilon*v_2). Integer matrices suffice; ranks use exact fractions.
"""

from fractions import Fraction
import json


def rank(matrix):
    rows = [list(map(Fraction, row)) for row in matrix]
    pivot = 0
    for column in range(len(rows[0])):
        found = next((i for i in range(pivot, len(rows)) if rows[i][column]), None)
        if found is None:
            continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        scale = rows[pivot][column]
        rows[pivot] = [x / scale for x in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot:
                scale = rows[i][column]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
    return pivot


def multiply(left, right):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*right)]
            for row in left]


def diagonal(entries):
    return [[x if i == j else 0 for j in range(len(entries))]
            for i, x in enumerate(entries)]


def localization(c):
    return [[1, 0, 0, 0], [0, 0, 0, 0],
            [0, 0, 1, 0], [0, c, 0, 0]]


fiber_loc = [[1, 0], [0, 0]]
boundary = [[0, 0], [0, 0], [0, 1]]
restriction_dual = [[1, 0, 0], [0, 1, 0]]
assert multiply(boundary, fiber_loc) == [[0, 0]] * 3
assert multiply(restriction_dual, boundary) == [[0, 0]] * 2
assert rank(fiber_loc) + rank(boundary) == 2
assert rank(boundary) + rank(restriction_dual) == 3
assert rank(restriction_dual) == 2
assert boundary[2][1] == 1  # Perfect pairing on the two minus lines.

epsilon = [[0, 0, 0, 0], [0, 0, 0, 0],
           [1, 0, 0, 0], [0, 1, 0, 0]]
tau_s = diagonal([1, 1, -1, -1])
tau_d = diagonal([1, -1, -1, 1])
results = []
for c in (0, 1):
    loc = localization(c)
    inverse_dual = localization(-c)  # A-transpose of diag(1, -epsilon*c).
    assert multiply(loc, epsilon) == multiply(epsilon, loc)
    assert multiply(tau_d, loc) == multiply(loc, tau_s)
    assert multiply(tau_s, inverse_dual) == multiply(inverse_dual, tau_d)
    strict_beta, relaxed_beta = c, -c
    assert strict_beta + relaxed_beta == 0
    beta_rank = rank([[c]])
    strict_h1_length = 4 - rank(loc)
    relaxed_h1_length = 8 - rank(inverse_dual)
    assert strict_h1_length == 1 + (1 - beta_rank)
    assert relaxed_h1_length == 3 + (3 - beta_rank)
    assert relaxed_h1_length == 8 - rank(loc)
    # P=e_1, Q=lambda*e_1+e_2: ell=(1,lambda), t=(0,c).
    # The determinant is lambda*0 - 1*c; no value of lambda is sampled.
    determinant = -c
    assert (determinant == 0) == (beta_rank == 0)
    results.append({"c": c, "strict_H1_A_dimension_over_F": strict_h1_length,
                    "relaxed_H1_A_dimension_over_F": relaxed_h1_length,
                    "kummer_test_determinant": determinant,
                    "strict_lift_exists": beta_rank == 0})

print(json.dumps({"formal_model_checks": "PASS", "cases": results}, indent=2))

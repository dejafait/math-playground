"""Exact polynomial checks for L013; no elliptic-curve realization.

Run from the notebook: python3 scripts/cyclotomic-determinant/check_model.py
Polynomial identities over Z[t] also hold over Lambda with
t = T/(1+T/2) and sigma(t) = -t. No numerical p-adic samples are used.
"""

from fractions import Fraction
import json


def poly(*coefficients):
    result = list(coefficients or (0,))
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


ZERO, ONE, T = poly(0), poly(1), poly(0, 1)


def add(left, right):
    return poly(*(sum(p[i] if i < len(p) else 0 for p in (left, right))
                  for i in range(max(len(left), len(right)))))


def neg(value):
    return poly(*(-x for x in value))


def mul(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return poly(*result)


def sigma(value):
    return poly(*(x * (-1) ** i for i, x in enumerate(value)))


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def signed_dual(matrix):
    return [[neg(sigma(x)) for x in row] for row in transpose(matrix)]


def multiply(left, right):
    result = []
    for row in left:
        output = []
        for column in zip(*right):
            value = ZERO
            for x, y in zip(row, column):
                value = add(value, mul(x, y))
            output.append(value)
        result.append(output)
    return result


def subtract(left, right):
    return [[add(x, neg(y)) for x, y in zip(a, b)]
            for a, b in zip(left, right)]


def rank_at_zero(matrix):
    rows = [[Fraction(x[0]) for x in row] for row in matrix]
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


def order(value):
    return next(i for i, x in enumerate(value) if x)


identity = [[ONE, ZERO], [ZERO, ONE]]
d_global = [[ZERO, T]]
localization = [[ONE, ZERO], [T, ZERO]]
local_pairing = [[ZERO, ONE], [ONE, ZERO]]
d_strict = d_global + localization  # Output coordinates f,a,b.
d_ordinary = [[T, ZERO], [ZERO, T]]  # Output coordinates b,f.
d_full_ordinary = [[ZERO, T, ZERO], [ONE, ZERO, neg(ONE)], [T, ZERO, ZERO]]

# Ordinary fiber cancellation, retaining the entire local-condition map.
cancel_1 = [[ONE, ZERO, ZERO], [ZERO, ONE, ZERO]]
cancel_2 = [[ZERO, ZERO, ONE], [ONE, ZERO, ZERO]]
assert multiply(cancel_2, d_full_ordinary) == multiply(d_ordinary, cancel_1)
assert multiply(d_full_ordinary, [[ZERO], [ZERO], [ONE]]) == [[ZERO], [neg(ONE)], [ZERO]]

# Reciprocity, finite-line annihilator, and the adjoint local boundary.
bar_localization = [[sigma(x) for x in row] for row in localization]
assert multiply(multiply(transpose(localization), local_pairing), bar_localization) == [[ZERO, ZERO], [ZERO, ZERO]]
finite_line = [[ONE], [ZERO]]
assert multiply(multiply(transpose(finite_line), local_pairing), finite_line) == [[ZERO]]
assert multiply(transpose(finite_line), local_pairing) == [[ZERO, ONE]]

# Strict/relaxed signed duality; its kernel is the acyclic unit pair.
d_dual = signed_dual(d_global)
assert signed_dual(d_ordinary) == d_ordinary
p_1 = [[ZERO, ONE]]
p_2 = [[ZERO, neg(T), ONE], [ONE, ZERO, ZERO]]
assert multiply(p_2, d_strict) == multiply(d_dual, p_1)
kernel_1 = [[ONE], [ZERO]]
kernel_2 = [[ZERO], [ONE], [T]]
assert multiply(p_1, kernel_1) == [[ZERO]]
assert multiply(p_2, kernel_2) == [[ZERO], [ZERO]]
assert multiply(d_strict, kernel_1) == kernel_2
assert rank_at_zero(p_1) == 1 and rank_at_zero(p_2) == 2
local_adjoint = multiply(transpose(bar_localization), local_pairing)
assert [row[1:] for row in p_2] == local_adjoint

# The ordinary/relaxed map and its dual; adjointness up to homotopy.
projection_2 = [[ZERO, ONE]]
adjoint_1 = [[ZERO], [ONE]]
assert multiply(projection_2, d_ordinary) == d_global
assert multiply(d_ordinary, adjoint_1) == d_dual
homotopy = [[ZERO, ONE, ZERO], [ZERO, ZERO, ZERO]]
assert subtract(identity, multiply(adjoint_1, p_1)) == multiply(homotopy, d_strict)
assert subtract(cancel_2, p_2) == multiply(d_ordinary, homotopy)

# Base cohomology and the exact ordinary/relaxed local-condition sequence.
assert rank_at_zero(d_global) == rank_at_zero(d_ordinary) == 0
assert rank_at_zero(d_strict) == 1
quotient_loc = [[T, ZERO]]
boundary = [[ONE], [ZERO]]
assert rank_at_zero(quotient_loc) == 0
assert multiply(projection_2, boundary) == [[ZERO]]
assert rank_at_zero(boundary) + rank_at_zero(projection_2) == 2
assert rank_at_zero(projection_2) == 1
finite_loc = [[ONE, ZERO]]
strict_line = [[ZERO], [ONE]]
assert multiply(finite_loc, strict_line) == [[ZERO]]
assert rank_at_zero(finite_loc) + rank_at_zero(strict_line) == 2

# First Bockstein, its dual factor, and both paths through descent.
beta = [[ZERO, ONE]]
assert d_global == [[mul(T, x) for x in beta[0]]]
assert rank_at_zero(beta) == 1  # First cokernel is zero.
z = [[d_global[0][1]], [neg(d_global[0][0])]]  # Kernel cofactors of d.
assert multiply(d_global, z) == [[ZERO]]
regulator_of_delta = [[mul(T, beta[0][1])], [neg(mul(T, beta[0][0]))]]
assert z == regulator_of_delta
normalized_leading_vector = [[ONE], [ZERO]]
assert multiply(beta, normalized_leading_vector) == [[ZERO]]
assert multiply(finite_loc, normalized_leading_vector) == [[ONE]]

# Characteristic determinant, scalar reciprocity, and marked W/Sha.
characteristic = add(mul(d_ordinary[0][0], d_ordinary[1][1]), neg(mul(d_ordinary[0][1], d_ordinary[1][0])))
scalar = multiply(quotient_loc, z)[0][0]
assert characteristic == scalar == poly(0, 0, 1)
assert order(characteristic) == order(scalar) == 2
sha_quotient = [[ZERO, ONE]]
kummer_line = [[ONE], [ZERO]]
assert multiply(sha_quotient, kummer_line) == [[ZERO]]
assert multiply(sha_quotient, strict_line) == [[ONE]]
assert multiply(beta, kummer_line) == [[ZERO]]
assert rank_at_zero(kummer_line) == rank_at_zero(sha_quotient) == 1

print(json.dumps({
    "formal_model_checks": "PASS",
    "global_base_H1_dimension": 2,
    "global_base_H2_dimension": 1,
    "ordinary_base_Selmer_dimension": 2,
    "first_Bockstein_rank": 1,
    "determinant_derivative_degree": 1,
    "characteristic_order": order(characteristic),
    "formal_reciprocity_scalar_order": order(scalar),
    "rational_Kummer_dimension": 1,
    "marked_V_p_Sha_dimension": 1,
    "leading_vector_is_rational": True,
    "rational_exterior_square_dimension": 0,
    "arithmetic_realization_asserted": False,
}, indent=2))

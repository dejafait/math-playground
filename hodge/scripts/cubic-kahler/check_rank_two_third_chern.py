#!/usr/bin/env python3
"""Exact checks for L044; no exact maps, bundles or stability are certified."""

from collections import Counter
from fractions import Fraction as Q

from check_eigenvector_certificate import (
    identity, linear_combination, matrix, multiply, transpose,
)


GRAM = matrix([[0, 1, 0, 1], [1, -2, 0, 0],
               [0, 0, -2, 1], [1, 0, 1, -2]])
ZERO = (Q(0),) * 4
FIBRE = (Q(1), Q(0), Q(0), Q(0))


def vector_sum(*terms):
    return tuple(sum(c * v[i] for c, v in terms) for i in range(4))


def apply(operator, vector):
    return tuple(sum(x * y for x, y in zip(row, vector)) for row in operator)


def pairing(left, right):
    return sum(x * y for x, y in zip(left, apply(GRAM, right)))


def outer(left, right):
    return [[x * y for y in right] for x in left]


def inverse(operator):
    rows = [list(row) + unit for row, unit in zip(operator, identity(4))]
    for column in range(4):
        pivot = next(i for i in range(column, 4) if rows[i][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        divisor = rows[column][column]
        rows[column] = [x / divisor for x in rows[column]]
        for i in range(4):
            if i != column:
                coefficient = rows[i][column]
                rows[i] = [x - coefficient * y
                           for x, y in zip(rows[i], rows[column])]
    return [row[4:] for row in rows]


def line_characters(lines):
    """Characters of sum(lines) - 2[I_C], through ch_3.

    Only the divisor part of mixed ch_2 is represented. The omitted
    2U tensor on T is killed by every divisor in the ch_3 products.
    The geometric support characters themselves are proved in L044.
    """
    a = vector_sum(*[(s, x) for (x, y), s in lines.items()])
    b = vector_sum(*[(s, y) for (x, y), s in lines.items()])
    s1 = sum(s * pairing(x, x) for (x, y), s in lines.items())
    s2 = sum(s * pairing(y, y) for (x, y), s in lines.items())
    tensor = [[sum(s * x[i] * y[j] for (x, y), s in lines.items())
               for j in range(4)] for i in range(4)]
    mixed = linear_combination((4, inverse(GRAM)), (1, tensor))
    h31 = vector_sum((-2, FIBRE),
                     *[(s * pairing(y, y) / 2, x)
                       for (x, y), s in lines.items()])
    h32 = vector_sum((-2, FIBRE),
                     *[(s * pairing(x, x) / 2, y)
                       for (x, y), s in lines.items()])
    return a, b, Q(4) + s1 / 2, Q(4) + s2 / 2, mixed, h31, h32


def normalized_third(characters):
    a, b, p1, p2, mixed, h31, h32 = characters
    # These are the N tensor eta and eta tensor N coefficients of
    # ch_3 - c_1 ch_2 / 2 + c_1^3 / 12, respectively.
    first = vector_sum((1, h31), (-p2 / 2, a),
                       (Q(-1, 2), apply(mixed, apply(GRAM, b))),
                       (pairing(b, b) / 4, a))
    second = vector_sum((1, h32), (-p1 / 2, b),
                        (Q(-1, 2), apply(transpose(mixed), apply(GRAM, a))),
                        (pairing(a, a) / 4, b))
    return first, second


def twist(characters, t1, t2):
    a, b, p1, p2, mixed, h31, h32 = characters
    next_mixed = linear_combination(
        (1, mixed), (1, outer(t1, b)), (1, outer(a, t2)),
        (2, outer(t1, t2)))
    next_h31 = vector_sum(
        (1, h31), (p2, t1), (1, apply(mixed, apply(GRAM, t2))),
        (pairing(t2, t2) / 2, a), (pairing(t2, b), t1),
        (pairing(t2, t2), t1))
    next_h32 = vector_sum(
        (1, h32), (p1, t2),
        (1, apply(transpose(mixed), apply(GRAM, t1))),
        (pairing(t1, t1) / 2, b), (pairing(t1, a), t2),
        (pairing(t1, t1), t2))
    return (vector_sum((1, a), (2, t1)),
            vector_sum((1, b), (2, t2)),
            p1 + pairing(t1, a) + pairing(t1, t1),
            p2 + pairing(t2, b) + pairing(t2, t2),
            next_mixed, next_h31, next_h32)


def add_delta(lines, x, y, coefficient):
    for pair, sign in [((x, y), 1), ((x, ZERO), -1),
                       ((ZERO, y), -1), ((ZERO, ZERO), 1)]:
        lines[pair] += coefficient * sign


def add_third_difference(lines, x, z, y, reverse=False):
    # ([L_1(x)]-1)([L_1(z)]-1)([L_2(y)]-1), or factor reversal.
    for left, sign_left in [(vector_sum((1, x), (1, z)), 1),
                            (x, -1), (z, -1), (ZERO, 1)]:
        for right, sign_right in [(y, 1), (ZERO, -1)]:
            pair = (right, left) if reverse else (left, right)
            lines[pair] += sign_left * sign_right


def main():
    a0 = matrix([[1, 2, -2, 5], [Q(1, 2), 0, -1, Q(3, 2)],
                 [Q(1, 2), 0, -2, 2], [0, 0, 0, 0]])
    b0 = matrix([[0, -2, 2, 0], [-2, 1, 1, 0],
                 [2, 1, 4, 0], [0, 0, 0, 0]])
    reflect_e = matrix([[1, 0, 0, 0], [0, 1, 0, 0],
                        [0, 0, -1, 1], [0, 0, 0, 1]])
    reflect_r = matrix([[1, 1, 2, 0], [0, 1, 0, 0],
                        [0, -1, -1, 0], [0, 0, 0, 1]])
    chamber = multiply(reflect_r, reflect_e)
    assert multiply(multiply(transpose(chamber), GRAM), chamber) == GRAM
    assert multiply(reflect_e, reflect_e) == identity(4)
    assert multiply(reflect_r, reflect_r) == identity(4)
    assert apply(chamber, FIBRE) == FIBRE
    k = tuple(map(Q, [-4, -2, 1, 2]))
    assert apply(chamber, k) == k
    final_a = multiply(multiply(chamber, a0), inverse(chamber))
    final_b = multiply(multiply(chamber, b0), transpose(chamber))
    pi_k = matrix([[0, 0, 0, -2], [0, 0, 0, -1],
                   [0, 0, 0, Q(1, 2)], [0, 0, 0, 1]])
    pi_w = linear_combination((1, identity(4)), (-1, pi_k))
    assert multiply(final_b, GRAM) == multiply(
        linear_combination((2, final_a), (-4, identity(4))), pi_w)
    assert all(entry.denominator == 1 for row in final_b for entry in row)

    basis = [tuple(Q(i == j) for i in range(4)) for j in range(3)]
    u = [apply(chamber, e) for e in basis]
    assert pairing(u[0], u[1]) == 1
    lines = Counter({(ZERO, ZERO): 4})
    for i in range(3):
        for j in range(3):
            add_delta(lines, u[i], u[j], b0[i][j])
    before = line_characters(lines)
    y = vector_sum((2, u[0]), (2, u[1]), (5, u[2]))
    assert y == tuple(map(Q, [-6, 2, 3, 0]))
    assert before[:2] == (ZERO, ZERO)
    assert before[2:4] == (Q(4), Q(4))
    assert before[5:] == (vector_sum((-1, y)), vector_sum((-1, y)))
    add_third_difference(lines, u[0], u[1], y)
    add_third_difference(lines, u[0], u[1], y, reverse=True)
    after = line_characters(lines)
    assert sum(lines.values()) - 2 == 2
    assert after[:5] == before[:5]
    assert after[5:] == (ZERO, ZERO)
    assert normalized_third(after) == (ZERO, ZERO)
    assert all(x[3] == y[3] == 0 for (x, y) in lines)
    assert all(s.denominator == 1 for s in lines.values())

    # Test twist cancellation with nonzero c_1 and twisting components
    # outside W, rather than silently normalizing by a rational line bundle.
    trials = [(k, vector_sum((-1, k))),
              (tuple(map(Q, [2, -1, 3, 1])), tuple(map(Q, [-1, 2, 0, 3])))]
    arbitrary_lines = Counter({(ZERO, ZERO): 1,
                               (u[0], u[1]): 2,
                               (u[2], u[0]): 1})
    for characters in (before, after, line_characters(arbitrary_lines)):
        for t1, t2 in trials:
            assert normalized_third(twist(characters, t1, t2)) == normalized_third(characters)
    nonzero_moments = lines.copy()
    nonzero_moments[(u[1], u[2])] += 2
    nonzero_moments[(ZERO, ZERO)] -= 2
    for data in (lines, nonzero_moments):
        characters = line_characters(data)
        a, b, p1, p2, mixed, h31, h32 = characters
        tensor = linear_combination((1, mixed), (-4, inverse(GRAM)))
        assert tensor == linear_combination((1, final_b), (Q(1, 2), outer(a, b)))
        s1, s2 = 2 * (p1 - 4), 2 * (p2 - 4)
        t1 = vector_sum(*[(s * pairing(x, x), y)
                         for (x, y), s in data.items()])
        t2 = vector_sum(*[(s * pairing(y, y), x)
                         for (x, y), s in data.items()])
        reduced_second = vector_sum((Q(1, 2), t1), (-s1 / 4 - 2, b),
                                    (-1, apply(final_a, a)), (-2, FIBRE))
        reduced_first = vector_sum((Q(1, 2), t2), (-s2 / 4 - 2, a),
                                   (-1, apply(final_a, b)), (-2, FIBRE))
        assert normalized_third(characters) == (reduced_first, reduced_second)

    print("PASS: integral chamber reflections preserve W_0, its complement and the fibre.")
    print("PASS: final doubled tensor is integral and has L029's forced operator.")
    print("PASS: signed rank-two class preserves c_1,ch_2 and cancels both ch_3 components.")
    print("PASS: rank-two normalized third character survives arbitrary integral line twists.")
    print("PASS: both forced third-moment formulas, including nonzero first moments.")
    print("Ample-cone membership and normalization Riemann--Roch are proved in L044.")
    print("No c_4 test, exact presentation, rank-two bundle or stability is certified.")


if __name__ == "__main__":
    main()

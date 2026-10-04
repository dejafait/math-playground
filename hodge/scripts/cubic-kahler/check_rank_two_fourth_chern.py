#!/usr/bin/env python3
"""Exact arithmetic for L045's fixed V'; no bundle or stability is certified.

The geometric finite-cover trace and three-point normalization sequence
are inputs proved in L008/L019. This script checks their HRR bookkeeping,
all signed product-line terms and the full cup square, including T.
"""

from collections import Counter
from fractions import Fraction as Q

from check_eigenvector_certificate import (
    identity, linear_combination, matrix, multiply, transpose,
)
from check_rank_two_third_chern import (
    GRAM, ZERO, FIBRE, add_delta, add_third_difference, apply, inverse,
    line_characters, pairing, vector_sum,
)


def trace(operator):
    return sum(operator[i][i] for i in range(len(operator)))


def line_fourth(lines):
    return sum(s * pairing(x, x) * pairing(y, y) / 4
               for (x, y), s in lines.items())


def line_euler(lines):
    return sum(s * (2 + pairing(x, x) / 2) * (2 + pairing(y, y) / 2)
               for (x, y), s in lines.items())


def main():
    # Surface HRR, finite trace, and all three normalization quotients.
    chi_s = Q(2)
    chi_y = chi_s + chi_s + pairing(FIBRE, FIBRE) / 2
    double_points = 3
    chi_c = chi_y - double_points
    projection_degrees = (Q(2), Q(2))
    ambient_todd_contribution = chi_s * sum(projection_degrees)
    ch4_normalization = chi_y - ambient_todd_contribution
    ch4_c = ch4_normalization - double_points
    assert (chi_y, chi_c, ambient_todd_contribution) == (4, 1, 8)
    assert (ch4_normalization, ch4_c) == (-4, -7)
    assert ch4_c + ambient_todd_contribution == chi_c

    a0 = matrix([[1, 2, -2, 5], [Q(1, 2), 0, -1, Q(3, 2)],
                 [Q(1, 2), 0, -2, 2], [0, 0, 0, 0]])
    b0 = matrix([[0, -2, 2, 0], [-2, 1, 1, 0],
                 [2, 1, 4, 0], [0, 0, 0, 0]])
    chamber = matrix([[1, 1, -2, 2], [0, 1, 0, 0],
                      [0, -1, 1, -1], [0, 0, 0, 1]])
    assert multiply(multiply(transpose(chamber), GRAM), chamber) == GRAM
    basis = [tuple(Q(i == j) for i in range(4)) for j in range(3)]
    u = [apply(chamber, e) for e in basis]
    y = vector_sum((2, u[0]), (2, u[1]), (5, u[2]))
    assert y == tuple(map(Q, [-6, 2, 3, 0]))
    assert pairing(u[0], u[1]) == 1
    assert pairing(y, y) == -50

    # Expand the exact K-class in L044 (12), then both terms in (15).
    lines = Counter({(ZERO, ZERO): 4})
    for i in range(3):
        for j in range(3):
            add_delta(lines, u[i], u[j], b0[i][j])
    before = line_characters(lines)
    delta_fourth = line_fourth(lines)
    assert delta_fourth == 7
    corrections = []
    for reverse in (False, True):
        correction = Counter()
        add_third_difference(correction, u[0], u[1], y, reverse=reverse)
        assert line_fourth(correction) == -25
        assert line_euler(correction) == -25
        corrections.append(line_fourth(correction))
        lines.update(correction)
    after = line_characters(lines)
    assert sum(lines.values()) - 2 == 2
    assert after[:5] == before[:5]
    assert after[:2] == (ZERO, ZERO)
    assert after[2:4] == (Q(4), Q(4))
    assert after[5:] == (ZERO, ZERO)
    assert line_fourth(lines) == delta_fourth + sum(corrections) == -43
    ch4_v = line_fourth(lines) + 2 * ch4_c
    assert ch4_v == -57

    # Mixed N action directly from the signed-line tensor plus 2[C].
    final_a = multiply(multiply(chamber, a0), inverse(chamber))
    final_b = multiply(multiply(chamber, b0), transpose(chamber))
    b_operator = multiply(final_b, GRAM)
    d_n = multiply(after[4], GRAM)
    pi_k = matrix([[0, 0, 0, -2], [0, 0, 0, -1],
                   [0, 0, 0, Q(1, 2)], [0, 0, 0, 1]])
    assert d_n == linear_combination((2, final_a), (4, pi_k))
    assert multiply(transpose(d_n), GRAM) == multiply(GRAM, d_n)
    n_square = trace(multiply(d_n, d_n))
    assert n_square == 36

    # f(z)=z^3+z^2-2z-1; Newton/Vieta gives sum(root^2)=5.
    f_second_coefficient, f_first_coefficient = Q(1), Q(-2)
    root_sum = -f_second_coefficient
    root_pair_sum = f_first_coefficient
    root_square_sum = root_sum**2 - 2 * root_pair_sum
    dim_t, field_degree = 18, 3
    assert dim_t % field_degree == 0
    trace_u_squared = (dim_t // field_degree) * root_square_sum
    t_square = 4 * trace_u_squared
    assert (root_square_sum, trace_u_squared, t_square) == (5, 30, 120)

    pure_square = 2 * after[2] * after[3]
    beta_square = pure_square + n_square + t_square
    assert (pure_square, beta_square) == (32, 188)

    # Separate expansion of (2[C]+B_c)^2 checks the tensor contraction.
    c_n = linear_combination((2, identity(4)))
    c_square = (2 * projection_degrees[0] * projection_degrees[1]
                + trace(multiply(c_n, c_n)) + trace_u_squared)
    c_b = trace(multiply(c_n, b_operator))
    b_square = trace(multiply(b_operator, b_operator))
    assert (c_square, c_b, b_square) == (54, -28, 84)
    assert 4 * c_square + 4 * c_b + b_square == beta_square

    # c_1=0: ch_4=(2 c_2^2-4 c_4)/24. Virtual rank does not truncate.
    c4_v = beta_square / 2 - 6 * ch4_v
    required_rank_two_ch4 = beta_square / 12
    assert (required_rank_two_ch4, c4_v) == (Q(47, 3), Q(436))
    assert c4_v != 0

    # HRR through all signed lines, independently of the character product.
    chi_x = chi_s**2
    chi_ic = chi_x - chi_c
    chi_v_direct = line_euler(lines) - 2 * chi_ic
    chi_v_character = (2 * chi_x + chi_s * (after[2] + after[3])
                       + ch4_v)
    assert (line_euler(lines), chi_v_direct, chi_v_character) == (-27, -33, -33)

    print("PASS: chi(Y)=4, chi(C)=1, ambient Todd term=8, ch_4(O_C)=-7.")
    print("PASS: Delta ch_4=7; both finite differences contribute -25; ch_4(V')=-57.")
    print("PASS: full ch_2 square=188 (pure 32, divisor 36, transcendental 120).")
    print("PASS: expanding (2[C]+B_c)^2 independently gives 4(54)+4(-28)+84=188.")
    print("PASS: direct signed-line HRR and ambient-character HRR both give chi(V')=-33.")
    print("EXCLUDED: rank-two c_4 must be zero; fixed V' has c_4=436 and required ch_4=47/3.")
    print("Geometric inputs and rank truncation are justified in L045; no stability claim.")


if __name__ == "__main__":
    main()

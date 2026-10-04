#!/usr/bin/env python3
"""Exact polynomial and residue arithmetic for L048; no bundle is certified.

The geometric mixed tensor and K3-product Todd class are inputs from
L045. Sparse polynomials below use the pure coefficients p,t; only
untwisted HRR is evaluated.
"""

from fractions import Fraction as Q


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, Q(0)) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def scale(polynomial, coefficient):
    return {exponent: coefficient * value
            for exponent, value in polynomial.items() if coefficient * value}


def evaluate(polynomial, p, t):
    return sum(coefficient * p**i * t**j
               for (i, j), coefficient in polynomial.items())


def main():
    # Exact trace bookkeeping already justified geometrically in L045.
    root_square_sum = Q(-1)**2 - 2 * Q(-2)
    divisor_square = 4 * root_square_sum + 4**2
    transcendental_square = 4 * (18 // 3) * root_square_sum
    mixed_square = divisor_square + transcendental_square
    assert (divisor_square, transcendental_square, mixed_square) == (36, 120, 156)

    beta_square = {(1, 1): Q(2), (0, 0): mixed_square}
    ch4 = scale(beta_square, Q(1, 12))
    assert ch4 == {(1, 1): Q(1, 6), (0, 0): Q(13)}
    # c_1=0, c_3=0 and c_4=0: beta^2/2 - 6 ch_4 is identically zero.
    assert add(scale(beta_square, Q(1, 2)), scale(ch4, -6)) == {}

    rank_todd = {(0, 0): Q(8)}
    second_todd = {(1, 0): Q(2), (0, 1): Q(2)}
    chi = add(rank_todd, second_todd, ch4)
    six_chi = scale(chi, 6)
    assert six_chi == {(1, 1): Q(1), (1, 0): Q(12),
                       (0, 1): Q(12), (0, 0): Q(126)}
    # Every other numerator coefficient is divisible by six.
    residual = add(six_chi, {(1, 1): Q(-1)})
    assert all(value.denominator == 1 and value.numerator % 6 == 0
               for value in residual.values())
    # Substitute p=a+4,t=b+4 symbolically through degree (1,1).
    chi_ab = {(1, 1): chi[(1, 1)],
              (1, 0): 4 * chi[(1, 1)] + chi[(1, 0)],
              (0, 1): 4 * chi[(1, 1)] + chi[(0, 1)],
              (0, 0): 16 * chi[(1, 1)] + 4 * chi[(1, 0)]
                      + 4 * chi[(0, 1)] + chi[(0, 0)]}
    assert chi_ab == {(1, 1): Q(1, 6), (1, 0): Q(8, 3),
                      (0, 1): Q(8, 3), (0, 0): Q(119, 3)}

    residues = set()
    for a in range(6):
        for b in range(6):
            p, t = a + 4, b + 4
            integral_index = evaluate(chi, p, t).denominator == 1
            assert integral_index == (p * t % 6 == 0)
            assert integral_index == ((p % 2 == 0 or t % 2 == 0)
                                      and (p % 3 == 0 or t % 3 == 0))
            if integral_index:
                residues.add((a, b))
    assert len(residues) == 15
    expected_rows = {0: [2, 5], 1: [2], 2: list(range(6)),
                     3: [2], 4: [2, 5], 5: [0, 2, 4]}
    for a, expected in expected_rows.items():
        assert sorted(b for row_a, b in residues if row_a == a) == expected
        assert ((a, a) in residues) == (a == 2)

    examples = [(-13, 0, Q(7), Q(5)),
                (-7, -7, Q(29, 2), Q(21, 2)),
                (-10, -10, Q(19), Q(3))]
    for a, b, fourth, euler in examples:
        assert a + b <= -13
        assert evaluate(ch4, a + 4, b + 4) == fourth
        assert evaluate(chi, a + 4, b + 4) == euler
        assert evaluate(chi_ab, a, b) == euler

    print("PASS: mixed square=156, retaining divisor 36 and transcendental 120.")
    print("PASS: ch_3=0; forced ch_4=(pt+78)/6 gives c_4=0 identically.")
    print("PASS: 6 chi=pt+12p+12t+126=ab+16a+16b+238.")
    print("PASS: all 36 residue pairs checked; 15 pass exactly when 6 divides pt.")
    print("Correction residues a: allowed b modulo 6:")
    for a, row in expected_rows.items():
        print(f"  {a}: {row}")
    print("PASS: (-13,0) has chi=5; (-7,-7) fails with 21/2; (-10,-10) has chi=3.")
    print("Formal character and untwisted index tests only; no K-class or bundle claim.")


if __name__ == "__main__":
    main()

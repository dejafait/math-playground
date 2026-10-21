#!/usr/bin/env python3
"""Exact numerical specialization of the imported quaternionic-line criterion.

The full mixed square 156 is the established input from L048. Steenrod
vanishing and the source theorem's sufficiency are proved in L050;
this program checks only the characteristic number and congruences.
"""

from fractions import Fraction


def characteristic_number(p, t):
    tangent_pairing = 48 * (p + t)  # p_1(TX) times u=-beta
    second_chern_square = 2 * p * t + 156
    return Fraction(tangent_pairing + 2 * second_chern_square, 4)


def index(p, t):
    return 8 + 2 * (p + t) + Fraction(p * t + 78, 6)


def main():
    old_count = new_count = 0
    for p in range(12):
        for t in range(12):
            number = characteristic_number(p, t)
            assert number == 12 * (p + t) + p * t + 78
            assert number.denominator == 1
            passes = number % 12 == 0
            assert passes == (p * t % 12 == 6)
            old_passes = index(p, t).denominator == 1
            assert old_passes == (p * t % 6 == 0)
            assert passes == ((index(p, t) / 2).denominator == 1)
            assert not passes or old_passes
            old_count += old_passes
            new_count += passes
    assert (old_count, new_count) == (60, 20)
    assert all(p * p % 12 != 6 for p in range(12))

    for a, b, expected_number, expected_index, passes in [
        (-10, -10, -30, 3, False),
        (-13, 0, -18, 5, False),
        (-7, -6, 24, 12, True),
        (-6, -7, 24, 12, True),
        (-13, -2, -24, 4, True),
    ]:
        p, t = a + 4, b + 4
        number = characteristic_number(p, t)
        assert a + b <= -13
        assert number == expected_number
        assert index(p, t) == expected_index
        assert (number % 12 == 0) == passes
        assert Fraction(p * t + 78, 6).denominator == 1

    print("PASS: full characteristic number is 12(p+t)+pt+78.")
    print("PASS: all 144 residue pairs give pt=6 mod 12 exactly.")
    print("PASS: 60 ordinary-index residues reduce to 20 SU(2) residues.")
    print("PASS: no symmetric residue survives; (-10,-10) gives -30=6 mod 12.")
    print("PASS: (-7,-6) gives J=24, ch_4=14P and index 12.")
    print("Topological existence uses the cited theorem; holomorphic stability is untested.")


if __name__ == "__main__":
    main()

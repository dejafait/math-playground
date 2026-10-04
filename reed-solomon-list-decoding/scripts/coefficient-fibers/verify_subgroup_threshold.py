#!/usr/bin/env python3
"""Exact arithmetic for Zhu-Wan's zero-sum estimate in one proper subgroup.

Imports the count inequality by citation. Checks its numerical applicability
using integer and rational arithmetic, without enumerating subsets or claiming
an exact subgroup count. Existing coefficient-fiber checks are left unchanged.
"""

from fractions import Fraction
from math import comb, factorial, isqrt
import json


def generalized_binomial(top, size):
    value = Fraction(1)
    for j in range(size):
        assert top - j > 0
        value *= Fraction(top - j, j + 1)
    return value


def ceiling(value):
    return -(-value.numerator // value.denominator)


def main():
    source_q = characteristic = 65537
    n = 1024
    index = (source_q - 1) // n
    ambient_degree = 28
    ambient_q = source_q**ambient_degree
    threshold = Fraction(ambient_q, 2**128)

    residues = []
    residue = 3
    for j in range(16):
        assert residue == pow(3, 2**j, source_q)
        residues.append(residue)
        residue = residue**2 % source_q
    assert residues == [
        3, 9, 81, 6561, 54449, 61869, 19139, 15028,
        282, 13987, 8224, 65529, 64, 4096, 65281, 65536,
    ]
    assert residues[-1] == source_q - 1 and residue == 1
    # An independent primality check, beyond the modular-order certificate.
    assert all(source_q % d for d in range(2, isqrt(source_q) + 1))
    generator = pow(3, 64, source_q)
    assert generator == 19139
    assert pow(generator, n, source_q) == 1
    assert pow(generator, n // 2, source_q) == source_q - 1
    subgroup = {pow(generator, j, source_q) for j in range(n)}
    assert len(subgroup) == n and 0 not in subgroup
    assert n < source_q - 1 and n * index == source_q - 1

    # Exact elementary comparisons used in the uniform proof.
    assert source_q < 257**2
    assert Fraction(source_q, index * characteristic) == Fraction(1, 64)
    assert Fraction(771, 1024) < Fraction(4, 5)
    assert 9 * 4**10 < 5**10
    assert 3**12 > 2 * source_q
    assert factorial(65) < 2**303
    assert 15**32 > 2**125
    assert 960**65 > 2**643
    assert comb(n, 65) > 2**340
    assert 2 * source_q < 2**18
    assert Fraction(28, 2**16) < Fraction(1, 2)
    assert 2**320 < threshold < 2**321

    sqrt_lower = Fraction(256)
    sqrt_upper = Fraction(256) + Fraction(1, 512)
    assert sqrt_lower**2 < source_q < sqrt_upper**2
    cases = []
    for k in (512, 256, 128, 64):
        s = k + 1
        total = comb(n, s)
        coarse_error = comb(s + 258, s)
        coarse_lower = Fraction(total, source_q) - coarse_error
        assert total >= comb(n, 65)
        assert Fraction(coarse_error, total) < Fraction(1, 2 * source_q)
        assert coarse_lower > Fraction(total, 2 * source_q) > 2**322
        assert coarse_lower > threshold

        # The theorem's real square root is bounded before this exact rational
        # product is evaluated. This need not match the coarse proof's error.
        top_upper = s + sqrt_upper + Fraction(1, 64)
        refined_error = generalized_binomial(top_upper, s)
        assert refined_error < coarse_error
        refined_lower = Fraction(total, source_q) - refined_error
        assert refined_lower > coarse_lower > threshold
        integer_lower = ceiling(coarse_lower)
        refined_integer_lower = ceiling(refined_lower)
        exponent = integer_lower.bit_length() - 1
        assert coarse_lower > 2**exponent
        support_upper = comb(n, k) // s
        assert refined_integer_lower <= support_upper
        cases.append({
            "k": k,
            "rate": str(Fraction(k, n)),
            "s": s,
            "center_parameter": 0,
            "total_subsets": total,
            "coarse_error_upper": coarse_error,
            "certified_integer_list_lower": integer_lower,
            "strict_power_of_two_lower_exponent": exponent,
            "refined_error_upper_ceil": ceiling(refined_error),
            "refined_integer_list_lower": refined_integer_lower,
            "support_count_upper": support_upper,
            "unsafe_error_index": n - k - 1,
            "largest_safe_index_upper": n - k - 2,
            "lower_exceeds_ambient_threshold": True,
        })

    print(json.dumps({
        "all_checks_passed": True,
        "source": "Zhu-Wan arXiv:1101.0289v1, Theorem 1.1, p. 2",
        "count_is_exact": False,
        "source_field_cardinality": source_q,
        "characteristic": characteristic,
        "subgroup_order": n,
        "subgroup_index": index,
        "subgroup_generator": generator,
        "primality_repeated_square_residues": residues,
        "sqrt_upper": str(sqrt_upper),
        "ambient_extension_degree": ambient_degree,
        "ambient_field_cardinality": ambient_q,
        "epsilon": str(Fraction(1, 2**128)),
        "ambient_threshold": str(threshold),
        "ambient_threshold_between_powers": [320, 321],
        "uniform_strict_list_lower_exponent": 322,
        "interleaving_widths": "all m >= 1, by L012",
        "cases": cases,
    }, indent=2))


if __name__ == "__main__":
    main()

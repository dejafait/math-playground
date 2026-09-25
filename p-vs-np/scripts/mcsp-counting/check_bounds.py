#!/usr/bin/env python3
"""Check rounding/constants in L006; not a complexity lower-bound test."""

from fractions import Fraction


def main():
    low_cases = 0
    high_cases = 0
    for r in range(1, 257):
        n = 1 << r
        ell = (r + 1).bit_length()  # ceil(log2(r+2)), without floats
        bound_on_s = r // (16 * ell)
        for s in range(bound_on_s + 1):
            count_bound = (s + 1) * (r + s) * (3 * (r + s) ** 2) ** s
            assert count_bound <= n**3, (r, s)
            low_cases += 1
        if r >= 8:
            s = n // (32 * r)
            exponent_bound = 2 * r + s * (2 + 2 * r)
            assert 4 * exponent_bound <= n, r
            assert r + s <= n and s + 1 <= n, r
            assert 2 * r <= Fraction(n, 16), r
            assert (
                2 * r + Fraction(n, 16) + Fraction(n, 16 * r)
                <= Fraction(n, 4)
            ), r
            high_cases += 1
    print(
        f"OK: {low_cases} low-threshold bounds (r=1..256); "
        f"{high_cases} high-threshold bounds (r=8..256)."
    )
    print("Finite checks cover constants and rounding, not asymptotic complexity.")


if __name__ == "__main__":
    main()

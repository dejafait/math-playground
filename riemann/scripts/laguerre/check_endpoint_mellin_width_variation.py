#!/usr/bin/env python3
"""Exact finite checks of L350's discrete energy identity and inequality."""

from itertools import product


def main():
    checked = 0
    zero_weights = 0
    for length in range(2, 9):
        for values in product((-1, 0, 1), repeat=length):
            differences = [b - a for a, b in zip(values, values[1:])]
            second = [b - a for a, b in zip(differences, differences[1:])]
            energy = sum(d * d for d in differences)
            telescoped = (
                values[-1] * differences[-1]
                - values[0] * differences[0]
                - sum(z * d for z, d in zip(values[1:-1], second))
            )
            assert energy == telescoped, values
            weight = max(abs(z) for z in values)
            bound = abs(differences[0]) + abs(differences[-1])
            bound += sum(abs(d) for d in second)
            assert energy <= weight * bound, values
            if weight == 0:
                assert energy == bound == 0
                zero_weights += 1
            checked += 1

    print(f"OK: {checked} exact discrete energy identities and inequalities; "
          f"{zero_weights} zero-weight cases.")
    print("Finite algebra only: this does not certify the analytic derivative "
          "bounds, the sampling norm, or any endpoint sign.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact local-lattice probe for the screened general literal-input target.

For K = Q_2(pi), pi^e = 2, a proved tail ideal makes the finite logarithm
sums generate the exact log lattice when that ideal is included. No sampled
automorphism or unbounded numerical truncation is used.
"""

from fractions import Fraction as Q
import json
from pathlib import Path

from check_packet import columns, inverse, matmul, matvec, printable, v2


def pi_power(e, power):
    quotient, remainder = divmod(power, e)
    result = [Q(0)] * e
    result[remainder] = Q(2) ** quotient
    return result


def multiply_pi(e, vector, power):
    result = [Q(0)] * e
    for index, value in enumerate(vector):
        quotient, remainder = divmod(index + power, e)
        result[remainder] += value * Q(2) ** quotient
    return result


def ideal_basis(e, power):
    return columns([pi_power(e, power + index) for index in range(e)])


def residue(value, precision):
    """Representative modulo 2^precision with only a power-of-2 denominator."""
    value = Q(value)
    if not value or v2(value) >= precision:
        return Q(0)
    denominator_power = v2(Q(value.denominator))
    odd_denominator = value.denominator // 2 ** denominator_power
    modulus = 2 ** (precision + denominator_power)
    numerator = (value.numerator * pow(odd_denominator, -1, modulus)) % modulus
    return Q(numerator, 2 ** denominator_power)


def logarithm_representatives(e, depth):
    # In the block [2^h,2^(h+1)), k-e*v2(k) >= 2^h-e*h.
    # Once this lower bound exceeds depth and 2^h >= e, it is increasing.
    h = 0
    while 2 ** h < e or 2 ** h - e * h < depth:
        h += 1
    cutoff = 2 ** h
    representatives = []
    for j in range(1, depth):
        vector = [Q(0)] * e
        for k in range(1, cutoff):
            quotient, remainder = divmod(j * k, e)
            term = Q((-1) ** (k + 1), k) * Q(2) ** quotient
            vector[remainder] += term
        # pi^depth O has coordinate r divisible by 2^ceil((depth-r)/e).
        vector = [residue(value, (depth - r + e - 1) // e)
                  for r, value in enumerate(vector)]
        representatives.append(vector)
    return representatives, cutoff


def lattice_basis(generators):
    """Column elimination over Z_2, with exact rational entries.

    At each ambient coordinate use a column of minimum valuation as pivot.
    All subtraction multipliers are then Z_2-integral. Swaps and these
    operations preserve the generated Z_2-lattice, yielding a square basis.
    """
    vectors = [list(vector) for vector in generators]
    dimension = len(vectors[0])
    for row in range(dimension):
        pivot = min(range(row, len(vectors)), key=lambda k: v2(vectors[k][row]))
        assert vectors[pivot][row]
        vectors[row], vectors[pivot] = vectors[pivot], vectors[row]
        for k in range(row + 1, len(vectors)):
            multiplier = vectors[k][row] / vectors[row][row]
            assert v2(multiplier) >= 0
            vectors[k] = [x - multiplier * y for x, y in zip(vectors[k], vectors[row])]
    assert all(not any(vector) for vector in vectors[dimension:])
    return columns(vectors[:dimension])


def inspect(e):
    depth = 2 * e + 1
    logs, cutoff = logarithm_representatives(e, depth)
    deep_basis = ideal_basis(e, depth)
    generators = logs + [list(col) for col in zip(*deep_basis)]
    log_basis = lattice_basis(generators)
    shell_basis = [[value / 4 for value in row] for row in log_basis]
    shell_inverse = inverse(shell_basis)
    # Includes actual O, all log representatives and the entire certified tail.
    assert all(v2(value) >= 0 for row in shell_inverse for value in row)
    assert all(v2(value) >= 0 for row in matmul(shell_inverse, columns(generators))
               for value in row)
    assert all(v2(value) >= 0 for row in matmul(shell_inverse, deep_basis)
               for value in row)
    result = {"e": e, "depth": depth, "log_cutoff": cutoff, "witness": None}
    for power in range(1, e):
        for j, vector in enumerate(logs, start=1):
            point = multiply_pi(e, vector, power)
            coordinates = matvec(shell_inverse, point)
            minimum = min(map(v2, coordinates))
            if minimum < 0:
                result.update({
                    "witness": f"pi^{power} log(1+pi^{j})",
                    "scalar_power": power, "log_generator_power": j,
                    "scalar_valuation": str(Q(power, e)), "beta": "1",
                    "required_rounded_exponent": 0,
                    "minimum_shell_coordinate_valuation": minimum,
                    "log_representatives": printable(columns(logs)),
                    "exact_log_lattice_basis": printable(log_basis),
                    "normalized_shell_basis": printable(shell_basis),
                    "witness_log_representative": [str(x) for x in vector],
                    "witness_shell_coordinates_mod_certified_tail": [str(x) for x in coordinates],
                })
                return result
    return result


def main():
    results = []
    for e in (1, 2, 4, 8, 16, 32):
        result = inspect(e)
        results.append(result)
        if result["witness"]:
            break
    report = {"arithmetic": "exact fractions with an analytic tail ideal",
              "packet": "single Q_2(pi) factor, pi^e=2", "results": results,
              "status": "probe; requires an informal proof and witness review"}
    Path(__file__).with_name("general-input-probe.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

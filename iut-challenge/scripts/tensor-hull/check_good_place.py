#!/usr/bin/env python3
"""Exact checks for a = 1 and canonical beta in the fixed tensor packet.

L008 proves the full orbit using the lattice and primitive-vector argument
from L007. These checks verify the multiplication, hull minima and witness;
they neither sample the automorphism group nor truncate a logarithm series.
"""

import json
from pathlib import Path

from check_packet import (
    Q, action, columns, field_valuation, integral, inverse, matmul, matvec,
    minimum_entry_valuation, printable, product_mul,
)


def component_minima(basis_matrix):
    return [min(field_valuation(vector[offset:offset + 2])
                for vector in zip(*basis_matrix)) for offset in (0, 2)]


def main():
    shell = columns([
        [Q(1), Q(0), Q(1), Q(0)],
        [Q(0), Q(1, 4), Q(0), Q(1, 4)],
        [Q(0), Q(1, 4), Q(0), Q(-1, 4)],
        [Q(1, 8), Q(0), Q(-1, 8), Q(0)],
    ])
    beta = [Q(0), Q(2), Q(0), Q(-2)]
    gamma = [Q(0), Q(1, 4), Q(0), Q(-1, 4)]
    one = [Q(1), Q(0), Q(1), Q(0)]
    assert product_mul(beta, gamma) == one
    beta_valuation = field_valuation(beta[:2])
    assert beta_valuation == field_valuation(beta[2:]) == Q(3, 2)

    enlarged_basis = matmul(action(gamma), shell)
    gamma_matrix = matmul(inverse(shell), enlarged_basis)
    assert gamma_matrix == [
        [Q(0), Q(0), Q(1, 8), Q(0)],
        [Q(0), Q(0), Q(0), Q(1, 8)],
        [Q(1), Q(0), Q(0), Q(0)],
        [Q(0), Q(1), Q(0), Q(0)],
    ]
    orbit_exponent = minimum_entry_valuation(gamma_matrix)
    rounded_exponent = (Q(0) - beta_valuation) // 1
    assert orbit_exponent == -3
    assert rounded_exponent == -2
    rounded_scalar = Q(2) ** rounded_exponent
    orbit_scalar = Q(2) ** orbit_exponent
    rounded_basis = [[rounded_scalar * value for value in row]
                     for row in shell]
    orbit_basis = [[orbit_scalar * value for value in row] for row in shell]
    assert component_minima(enlarged_basis) == [Q(-9, 2), Q(-9, 2)]
    assert component_minima(rounded_basis) == [-5, -5]
    assert component_minima(orbit_basis) == [-6, -6]
    assert integral([[value / orbit_scalar for value in row]
                     for row in gamma_matrix])
    assert not integral([[value / rounded_scalar for value in row]
                         for row in gamma_matrix])

    swap = columns([
        [Q(0), Q(0), Q(0), Q(1)],
        [Q(0), Q(1), Q(0), Q(0)],
        [Q(0), Q(0), Q(1), Q(0)],
        [Q(1), Q(0), Q(0), Q(0)],
    ])
    assert integral(swap) and integral(inverse(swap))
    source_coefficients = [Q(0), Q(0), Q(1), Q(0)]
    image_coefficients = matvec(swap, matvec(gamma_matrix,
                                           source_coefficients))
    witness = matvec(shell, image_coefficients)
    assert witness == [Q(1, 64), Q(0), Q(-1, 64), Q(0)]
    assert field_valuation(witness[:2]) == -6
    assert field_valuation(witness[2:]) == -6

    report = {
        "arithmetic": "exact fractions; no logarithm truncation",
        "scalar": "a = 1",
        "beta": "1 tensor 2sqrt(2)",
        "gamma_I_basis_matrix": printable(gamma_matrix),
        "rounded_exponent": rounded_exponent,
        "orbit_exponent_from_L008_proof": orbit_exponent,
        "unsaturated_component_minimum_valuations": ["-9/2", "-9/2"],
        "rounded_hull_radii": [32, 32],
        "full_orbit_hull_radii": [64, 64],
        "basis_swap_witness": [str(value) for value in witness],
        "full_orbit_hull_contained_in_rounded_hull": False,
        "infinite_assertions": "exact log-shell in L007; full orbit in L008",
        "scope": "auxiliary enlarged lattice; no final enclosure or IUT instance",
    }
    destination = Path(__file__).with_name("good-place-result.json")
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

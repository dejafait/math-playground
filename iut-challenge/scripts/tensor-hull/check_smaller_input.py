#!/usr/bin/env python3
"""Exact finite checks for the literal smaller input in L009.

The proof in L009 establishes the whole-group orbit. These checks use the
actual tensor-order basis and verify both branches and a sharp witness;
they do not sample the group or truncate a logarithm series.
"""

import json
from pathlib import Path

from check_packet import (
    Q, action, columns, field_valuation, integral, inverse, matmul, matvec,
    minimum_entry_valuation, printable, product_mul,
)
from check_good_place import component_minima


def scaled(matrix, scalar):
    return [[scalar * value for value in row] for row in matrix]


def main():
    shell = columns([
        [Q(1), Q(0), Q(1), Q(0)],
        [Q(0), Q(1, 4), Q(0), Q(1, 4)],
        [Q(0), Q(1, 4), Q(0), Q(-1, 4)],
        [Q(1, 8), Q(0), Q(-1, 8), Q(0)],
    ])
    tensor_order = columns([
        [Q(1), Q(0), Q(1), Q(0)],
        [Q(0), Q(1), Q(0), Q(1)],
        [Q(0), Q(1), Q(0), Q(-1)],
        [Q(2), Q(0), Q(-2), Q(0)],
    ])
    log_tensor = scaled(shell, Q(16))
    beta = [Q(0), Q(2), Q(0), Q(-2)]
    gamma = [Q(0), Q(1, 4), Q(0), Q(-1, 4)]
    one = [Q(1), Q(0), Q(1), Q(0)]
    assert product_mul(beta, gamma) == one
    beta_valuation = field_valuation(beta[:2])
    assert beta_valuation == field_valuation(beta[2:]) == Q(3, 2)

    shell_inverse = inverse(shell)
    order_coordinates = matmul(shell_inverse, tensor_order)
    assert order_coordinates == [
        [Q(1), Q(0), Q(0), Q(0)],
        [Q(0), Q(4), Q(0), Q(0)],
        [Q(0), Q(0), Q(4), Q(0)],
        [Q(0), Q(0), Q(0), Q(16)],
    ]
    smaller_basis = matmul(action(gamma), tensor_order)
    smaller_coordinates = matmul(shell_inverse, smaller_basis)
    assert smaller_coordinates == [
        [Q(0), Q(0), Q(1, 2), Q(0)],
        [Q(0), Q(0), Q(0), Q(2)],
        [Q(1), Q(0), Q(0), Q(0)],
        [Q(0), Q(4), Q(0), Q(0)],
    ]
    orbit_exponent = minimum_entry_valuation(smaller_coordinates)
    rounded_exponent = (Q(0) - beta_valuation) // 1
    assert orbit_exponent == -1
    assert rounded_exponent == -2
    orbit_basis = scaled(shell, Q(2) ** orbit_exponent)
    rounded_basis = scaled(shell, Q(2) ** rounded_exponent)

    smaller_in_orbit = matmul(inverse(orbit_basis), smaller_basis)
    log_in_orbit = matmul(inverse(orbit_basis), log_tensor)
    log_in_smaller = matmul(inverse(smaller_basis), log_tensor)
    assert integral(smaller_in_orbit)
    assert integral(log_in_orbit)
    assert integral(log_in_smaller)
    assert not integral(smaller_coordinates)  # e1/2 makes I/2 sharp.
    assert component_minima(smaller_basis) == [Q(-3, 2), Q(-3, 2)]
    assert component_minima(log_tensor) == [Q(1), Q(1)]
    assert component_minima(orbit_basis) == [-4, -4]
    assert component_minima(rounded_basis) == [-5, -5]
    assert integral(matmul(inverse(rounded_basis), orbit_basis))

    swap = columns([
        [Q(0), Q(0), Q(0), Q(1)],
        [Q(0), Q(1), Q(0), Q(0)],
        [Q(0), Q(0), Q(1), Q(0)],
        [Q(1), Q(0), Q(0), Q(0)],
    ])
    assert integral(swap) and integral(inverse(swap))
    source = [Q(0), Q(0), Q(1), Q(0)]  # 1 tensor pi in T's basis.
    image_coordinates = matvec(swap, matvec(smaller_coordinates, source))
    witness = matvec(shell, image_coordinates)
    assert witness == [Q(1, 16), Q(0), Q(-1, 16), Q(0)]
    assert field_valuation(witness[:2]) == -4
    assert field_valuation(witness[2:]) == -4

    report = {
        "arithmetic": "exact fractions; no logarithm truncation",
        "input": "beta^(-1) T union J, a = 1",
        "beta": "1 tensor 2sqrt(2)",
        "beta_inverse_T_in_I_basis": printable(smaller_coordinates),
        "beta_inverse_T_contained_in_I_over_2": True,
        "J_contained_in_I_over_2": True,
        "J_contained_in_beta_inverse_T": True,
        "rounded_exponent": rounded_exponent,
        "orbit_exponent_from_L009_proof": orbit_exponent,
        "unsaturated_branch_component_minima": {
            "beta_inverse_T": ["-3/2", "-3/2"],
            "J": ["1", "1"],
        },
        "sharp_full_orbit_hull_radii": [16, 16],
        "required_rounded_hull_radii": [32, 32],
        "sharp_witness_source": "1 tensor sqrt(2) in T",
        "sharp_basis_swap_witness": [str(value) for value in witness],
        "full_orbit_hull_contained_in_rounded_hull": True,
        "infinite_assertions": "log-shell in L007; whole-group orbit in L009",
        "scope": "fixed smaller input; no full IUT instance or normalized A/B",
    }
    destination = Path(__file__).with_name("smaller-input-result.json")
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

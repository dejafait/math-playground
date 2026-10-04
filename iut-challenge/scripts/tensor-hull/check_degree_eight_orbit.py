#!/usr/bin/env python3
"""Exact finite certificate for the literal-input full orbit in L011.

L010 supplies the analytic logarithm tails and exact unit-group generation.
L011 proves the whole-group orbit using primitive-vector transitivity. This
checks the hull extrema, both branch enclosures and an explicit involution;
it neither samples automorphisms nor approximates an infinite logarithm.
"""

from fractions import Fraction as Q
import json
from pathlib import Path

from check_degree_eight_input import FUNCTIONAL, evaluate
from check_packet import columns, matmul, matvec, printable, v2
from probe_general_input import ideal_basis, logarithm_representatives, multiply_pi


def field_valuation(vector):
    return min(v2(value) + Q(r, 8) for r, value in enumerate(vector))


def main():
    representatives, cutoff = logarithm_representatives(8, 9)
    assert cutoff == 64
    q1 = representatives[0]
    assert q1 == [0, 1, Q(1, 2), 1, Q(5, 4), 1, Q(3, 2), 1]
    tail_basis = [list(vector) for vector in zip(*ideal_basis(8, 9))]
    generators = representatives + tail_basis
    assert all(v2(evaluate(vector)) >= 2 for vector in generators)
    representative_valuations = list(map(field_valuation, representatives))
    assert representative_valuations == [
        Q(-3, 2), Q(-1, 2), Q(-1, 2), Q(1, 2), Q(1, 4),
        Q(1, 2), Q(3, 4), float("inf"),
    ]
    log_minimum = min(field_valuation(vector) for vector in generators)
    assert log_minimum == field_valuation(q1) == Q(-3, 2)

    # 8*pi*J lies in H: the generator minimum 13/8 exceeds 9/8.
    eight_pi_generators = [
        [8 * value for value in multiply_pi(8, vector, 1)]
        for vector in generators
    ]
    assert min(map(field_valuation, eight_pi_generators)) == Q(13, 8)
    assert all(field_valuation(vector) >= Q(9, 8)
               for vector in eight_pi_generators)
    # 4*pi*O lies in H as well, certifying pi*O subset I.
    order_basis = columns([[Q(r == j) for r in range(8)] for j in range(8)])
    four_pi_order = [
        [4 * value for value in multiply_pi(8, list(vector), 1)]
        for vector in zip(*order_basis)
    ]
    assert all(field_valuation(vector) >= Q(9, 8)
               for vector in four_pi_order)

    x0 = multiply_pi(8, q1, 1)
    w = [2 * value for value in x0]
    u = [value / 4 for value in q1]
    d = [left - right for left, right in zip(u, w)]
    assert evaluate(x0) == Q(1, 2)
    assert evaluate(w) == 1
    assert evaluate(u) == -1
    assert evaluate(d) == -2
    # u is in I since q1 is in J; w is in I since 4w is in H.
    assert field_valuation([4 * value for value in w]) >= Q(9, 8)
    shell_generators = [[value / 4 for value in vector] for vector in generators]
    assert all(v2(evaluate(vector)) >= 0 for vector in shell_generators)

    identity = [[Q(i == j) for j in range(8)] for i in range(8)]
    involution = [[identity[i][j] + d[i] * FUNCTIONAL[j]
                   for j in range(8)] for i in range(8)]
    assert matmul(involution, involution) == identity
    assert matvec(involution, w) == u
    witness = matvec(involution, x0)
    assert witness == [value / 8 for value in q1]

    required_minimum = min(map(field_valuation, shell_generators))
    orbit_minimum = min(field_valuation(vector) - 1
                        for vector in shell_generators)
    assert required_minimum == Q(-7, 2)
    assert orbit_minimum == field_valuation(witness) == Q(-9, 2)
    assert field_valuation(x0) == Q(-11, 8)
    assert Q(1, 8) // 1 == 0
    report = {
        "arithmetic": "exact fractions; analytic logarithm inputs proved in L010",
        "field": "K=Q_2(pi), pi^8=2",
        "literal_input": "pi (O_K union J), J=log(O_K^times)",
        "beta": "empty derivative product 1",
        "rounded_exponent": 0,
        "tail_ideal": "H=pi^9 O_K subset J",
        "log_generator_minimum_field_valuation": str(log_minimum),
        "log_representative_field_valuations": [
            str(value) for value in representative_valuations
        ],
        "eight_pi_J_generator_minimum_field_valuation": "13/8",
        "pi_O_contained_in_I": True,
        "pi_J_contained_in_I_over_2": True,
        "q1_is_exact_log_image_point": "proved from q1=log(1+pi)-h, h in H",
        "source_x0_pi_q1": [str(value) for value in x0],
        "functional_on_twice_source": "1; twice source is primitive in I",
        "involution_formula": "g(y)=y+lambda(y)(q1/4-2pi q1)",
        "involution_matrix_in_rational_coordinate_basis": printable(involution),
        "involution_squared_is_identity": True,
        "involution_preserves_I": "integral lambda and d in I; inverse equals itself",
        "sharp_witness_q1_over_8": [str(value) for value in witness],
        "full_orbit": "I/2; complete group argument proved in L011",
        "required_hull": "pi^(-28) O_K",
        "achieved_full_orbit_hull": "pi^(-36) O_K",
        "required_minimum_field_valuation": str(required_minimum),
        "achieved_minimum_field_valuation": str(orbit_minimum),
        "required_radius": "2^(7/2)",
        "achieved_radius": "2^(9/2)",
        "radius_ratio": 2,
        "rounded_full_orbit_hull_bound_holds": False,
        "scope": "local rounded comparison; final enclosure and original IUT data unresolved",
    }
    Path(__file__).with_name("degree-eight-orbit-result.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(json.dumps({
        key: report[key] for key in (
            "full_orbit", "required_hull", "achieved_full_orbit_hull",
            "radius_ratio", "involution_squared_is_identity",
            "rounded_full_orbit_hull_bound_holds",
        )
    }, indent=2))


if __name__ == "__main__":
    main()

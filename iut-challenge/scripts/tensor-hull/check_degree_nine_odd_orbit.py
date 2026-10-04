#!/usr/bin/env python3
"""Exact finite certificate for the screened odd-prime packet in L012.

L012 proves the logarithm tail, all-unit reduction and complete group orbit.
This checks every finite logarithm congruence, the functionals, both branch
enclosures and an explicit involution, with no sampled automorphisms.
"""

from fractions import Fraction as Q
import json
from pathlib import Path

from check_packet import matmul, matvec, printable


P, E, DEPTH, CUTOFF = 3, 9, 5, 81
REPRESENTATIVES = [
    [Q(7, 3), 1, 1, Q(7, 3), 2, 0, Q(1, 3), 0, 0],
    [1, 0, 1, 1, 1, 0, Q(1, 3), 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
]
ALPHA = [Q(18, 7)] + [Q(0)] * 8
ETA = [Q(-3, 49), Q(1, 7)] + [Q(0)] * 7


def v3(value):
    value = Q(value)
    if not value:
        return float("inf")
    numerator, denominator = abs(value.numerator), value.denominator
    valuation = 0
    while numerator % P == 0:
        numerator //= P
        valuation += 1
    while denominator % P == 0:
        denominator //= P
        valuation -= 1
    return valuation


def field_valuation(vector):
    return min(v3(value) + Q(r, E) for r, value in enumerate(vector))


def pi_power(power):
    quotient, remainder = divmod(power, E)
    vector = [Q(0)] * E
    vector[remainder] = Q(P) ** quotient
    return vector


def times_pi(vector):
    return [P * vector[-1]] + list(vector[:-1])


def scale(vector, scalar):
    return [Q(scalar) * value for value in vector]


def evaluate(functional, vector):
    return sum(x * y for x, y in zip(functional, vector))


def main():
    representatives = [[Q(value) for value in row] for row in REPRESENTATIVES]
    # Direct rational sums check the displayed residues without a modular
    # reduction algorithm or a computed lattice basis.
    for j, representative in enumerate(representatives, start=1):
        exact_sum = [Q(0)] * E
        for k in range(1, CUTOFF):
            quotient, remainder = divmod(j * k, E)
            exact_sum[remainder] += Q((-1) ** (k + 1), k) * P ** quotient
        for r, (actual, reduced) in enumerate(zip(exact_sum, representative)):
            assert v3(actual - reduced) >= (DEPTH - r + E - 1) // E
    # Only the base and increasing increment of the proved infinite block
    # bound are checked here. Infinite analytic assertions remain in L012.
    assert 3 ** 4 - E * 4 == 45 >= DEPTH
    assert 2 * 3 ** 4 - E > 0
    assert Q(DEPTH, E) > Q(1, 2)
    tail_basis = [pi_power(DEPTH + r) for r in range(E)]
    generators = representatives + tail_basis
    log_valuations = list(map(field_valuation, representatives))
    assert log_valuations == [Q(-1), Q(-1, 3), Q(0), Q(1, 3)]
    log_minimum = min(map(field_valuation, generators))
    assert log_minimum == -1
    shell_generators = [scale(vector, Q(1, 6)) for vector in generators]
    assert min(map(field_valuation, shell_generators)) == -2

    # 6*pi*O subset H subset J gives the order branch in I.
    six_pi_order = [scale(pi_power(r + 1), 6) for r in range(E)]
    assert min(map(field_valuation, six_pi_order)) == Q(10, 9)
    assert all(field_valuation(vector) >= Q(DEPTH, E)
               for vector in six_pi_order)
    # 18*pi*J subset H subset J gives the log branch in I/3.
    eighteen_pi_log = [scale(times_pi(vector), 18) for vector in generators]
    assert min(map(field_valuation, eighteen_pi_log)) == Q(10, 9)
    assert all(field_valuation(vector) >= Q(DEPTH, E)
               for vector in eighteen_pi_log)

    assert [evaluate(ALPHA, vector) for vector in representatives] == [
        Q(6), Q(18, 7), Q(18, 7), Q(0),
    ]
    assert [evaluate(ETA, vector) for vector in representatives] == [
        Q(0), Q(-3, 49), Q(-3, 49), Q(0),
    ]
    assert all(v3(evaluate(functional, vector)) >= 0
               for functional in (ALPHA, ETA) for vector in shell_generators)
    q1 = representatives[0]
    x0 = times_pi(q1)
    w, u = scale(x0, 3), scale(q1, Q(1, 6))
    assert field_valuation(scale(w, 6)) == Q(10, 9)
    assert evaluate(ALPHA, u) == evaluate(ETA, w) == 1
    assert evaluate(ALPHA, w) == evaluate(ETA, u) == 0
    assert evaluate(ETA, x0) == Q(1, 3)
    d = [left - right for left, right in zip(w, u)]
    functional = [left - right for left, right in zip(ALPHA, ETA)]
    assert evaluate(functional, d) == -2
    identity = [[Q(r == s) for s in range(E)] for r in range(E)]
    involution = [[identity[r][s] + d[r] * functional[s]
                   for s in range(E)] for r in range(E)]
    assert matmul(involution, involution) == identity
    assert matvec(involution, w) == u
    assert matvec(involution, u) == w
    sharp_witness = matvec(involution, x0)
    assert sharp_witness == scale(q1, Q(1, 18))
    assert field_valuation(sharp_witness) == -3
    assert Q(1, E) // 1 == 0
    assert min(field_valuation(times_pi(vector))
               for vector in tail_basis) == Q(2, 3) > -2

    report = {
        "arithmetic": "exact fractions; infinite analytic and group assertions proved in L012",
        "field": "K=Q_3(pi), pi^9=3",
        "literal_input": "pi (O_K union J), J=log(O_K^times)",
        "normalized_lattice": "I=J/6=J/3 as Z_3-lattices",
        "beta": "empty derivative product 1",
        "rounded_exponent": 0,
        "tail_ideal": "H=pi^5 O_K=log(1+pi^5 O_K)",
        "series_cutoff_exclusive": CUTOFF,
        "log_representatives_rows_j_1_to_4": printable(representatives),
        "log_representative_field_valuations": [str(v) for v in log_valuations],
        "log_lattice_minimum_field_valuation": str(log_minimum),
        "six_pi_O_minimum_field_valuation": "10/9",
        "eighteen_pi_J_minimum_field_valuation": "10/9",
        "pi_O_contained_in_I": True,
        "pi_J_contained_in_I_over_3": True,
        "alpha_coefficients": [str(x) for x in ALPHA],
        "eta_coefficients": [str(x) for x in ETA],
        "alpha_eta_integral_on_I": True,
        "primitive_point": "w=3pi q1 in I, eta(w)=1",
        "involution_formula": "g(y)=y+(alpha(y)-eta(y))(3pi q1-q1/6)",
        "involution_matrix": printable(involution),
        "involution_squared_is_identity": True,
        "involution_preserves_I": "integral functional and direction in I; inverse equals itself",
        "sharp_literal_log_image_point": "pi q1, with q1 in the exact log image J",
        "sharp_witness_q1_over_18": [str(x) for x in sharp_witness],
        "actual_log_witness": "g(pi log(1+pi)) in q1/18+I, also valuation -3",
        "full_orbit": "I/3; whole-group proof in L012",
        "required_hull": "pi^(-18) O_K",
        "achieved_full_orbit_hull": "pi^(-27) O_K",
        "required_minimum_field_valuation": "-2",
        "achieved_minimum_field_valuation": "-3",
        "required_radius": 9,
        "achieved_radius": 27,
        "radius_ratio": 3,
        "rounded_full_orbit_hull_bound_holds": False,
        "scope": "odd-prime local rounded comparison; original initial data, final container and B>=A unresolved",
    }
    Path(__file__).with_name("degree-nine-odd-orbit-result.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(json.dumps({key: report[key] for key in (
        "full_orbit", "required_hull", "achieved_full_orbit_hull",
        "required_radius", "achieved_radius", "radius_ratio",
        "involution_squared_is_identity", "rounded_full_orbit_hull_bound_holds",
    )}, indent=2))


if __name__ == "__main__":
    main()

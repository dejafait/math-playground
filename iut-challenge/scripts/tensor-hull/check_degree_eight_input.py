#!/usr/bin/env python3
"""Check the separating-functional certificate in L010 with exact fractions.

The logarithm tails and generation of the entire unit group are proved in
L010. This verifies every finite residue, the dual-lattice test and the
literal log-branch witness; no automorphism sampling is involved.
"""

from fractions import Fraction as Q
import json
from pathlib import Path

from probe_general_input import (
    ideal_basis, logarithm_representatives, multiply_pi,
)
from check_packet import printable, v2


FUNCTIONAL = [Q(2), Q(0), Q(-2), Q(0), Q(-4), Q(2), Q(0), Q(0)]


def evaluate(vector):
    return sum(x * y for x, y in zip(FUNCTIONAL, vector))


def main():
    e, depth = 8, 9
    representatives, cutoff = logarithm_representatives(e, depth)
    expected = [
        [0, 1, Q(1, 2), 1, Q(5, 4), 1, Q(3, 2), 1],
        [0, 0, 1, 0, Q(1, 2), 0, 1, 0],
        [3, 0, 0, 1, Q(3, 2), 0, Q(3, 2), 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0],
        [2, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert representatives == expected
    assert cutoff == 64
    # Independently check the displayed residues by unreduced rational sums.
    # The reduction routine is not used to check these differences.
    for j, representative in enumerate(expected, start=1):
        exact_sum = [Q(0)] * e
        for k in range(1, 64):
            quotient, remainder = divmod(j * k, e)
            exact_sum[remainder] += Q((-1) ** (k + 1), k) * 2 ** quotient
        for r, (actual, reduced) in enumerate(zip(exact_sum, representative)):
            assert v2(actual - reduced) >= (depth - r + e - 1) // e
    # Check the analytic block inequality at its base; monotonicity for all
    # subsequent blocks is established in the proof, not sampled here.
    assert 2 ** 6 - e * 6 == 16 >= depth
    assert 2 ** 6 - e > 0
    values = [evaluate(vector) for vector in representatives]
    assert values == [-4, -4, 0, -4, -4, 0, 0, 0]
    assert all(v2(value) >= 2 for value in values)

    tail = ideal_basis(e, depth)
    tail_values = [evaluate(vector) for vector in zip(*tail)]
    assert tail_values == [0, -4, 0, -8, 4, 0, 0, 8]
    assert all(v2(value) >= 2 for value in tail_values)
    multiplied_tail = [multiply_pi(e, list(vector), 1) for vector in zip(*tail)]
    multiplied_tail_values = [evaluate(vector) for vector in multiplied_tail]
    assert all(v2(value) >= 2 for value in multiplied_tail_values)

    witness_representative = multiply_pi(e, representatives[0], 1)
    witness_value = evaluate(witness_representative)
    assert witness_value == Q(1, 2)
    assert v2(witness_value) == -1
    rounded_exponent = Q(1, 8) // 1
    assert rounded_exponent == 0
    report = {
        "arithmetic": "exact fractions; logarithm tails certified in L010",
        "field": "K=Q_2(pi), pi^8=2",
        "packet_size": 1,
        "scalar": "a=pi", "scalar_valuation": "1/8",
        "beta": "empty derivative product 1", "beta_valuation": 0,
        "rounded_exponent": rounded_exponent,
        "log_tail_ideal": "pi^9 O_K",
        "series_cutoff_exclusive": cutoff,
        "log_representatives_rows_j_1_to_8": printable(representatives),
        "separating_functional_coefficients": [str(x) for x in FUNCTIONAL],
        "functional_on_log_representatives": [str(x) for x in values],
        "functional_on_tail_basis": [str(x) for x in tail_values],
        "functional_on_multiplied_tail_basis": [str(x) for x in multiplied_tail_values],
        "functional_on_entire_log_lattice_in_4_Z2": True,
        "functional_on_normalized_shell_in_Z2": True,
        "literal_witness": "pi log(1+pi) in a J",
        "witness_functional_coset": "1/2 + 4 Z_2",
        "literal_input_not_contained_in_required_shell": True,
        "scope": "genuine lattice inclusion only; full-orbit hull and original IUT applicability unresolved",
    }
    Path(__file__).with_name("degree-eight-input-result.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

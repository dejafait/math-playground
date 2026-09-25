"""Check L004's block and valuation identities, not Collatz convergence."""

import json


def valuation_two(value):
    assert value > 0
    return (value & -value).bit_length() - 1


def direct_block(start):
    assert start > 0 and start % 2 == 1
    current = start
    odd_steps = 0
    even_steps = 0
    states = []
    while current % 2:
        current = (3 * current + 1) // 2
        odd_steps += 1
        states.append(current)
    while current % 2 == 0:
        current //= 2
        even_steps += 1
        states.append(current)
    return odd_steps, even_steps, current, states


def check():
    transitions = 0
    domain_matches = 0
    residue_starts = 0
    for start in range(1, 32 * 512, 2):
        a, b, endpoint, states = direct_block(start)
        transitions += len(states)
        residue_starts += 1
        assert ((a, b) == (3, 1)) == (start % 32 == 7), start
        if (a, b) == (3, 1):
            t = (start - 7) // 32
            assert endpoint == 54 * t + 13
            assert endpoint - start == 22 * t + 6
            assert valuation_two(start + 5) == 2
            assert valuation_two(endpoint + 5) == 1 + valuation_two(3 * t + 1)
            domain_matches += 1

    parameters = sorted(set(range(256)) | {(4**k - 1) // 3 for k in range(33)})
    examples = []
    maximum_valuation_gain = 0
    for s in parameters:
        start = 128 * s + 103
        a, b, endpoint, states = direct_block(start)
        transitions += len(states)
        assert (a, b) == (3, 1)
        assert endpoint == 216 * s + 175
        assert valuation_two(start + 5) == valuation_two(endpoint + 5) == 2
        assert 3 * (endpoint + 5) - 5 * (start + 5) == 8 * s >= 0
        assert min(states) > start
        if s in (0, 1, 2):
            examples.append({
                "family": "valuation_preserving", "s": s,
                "start": start, "states": states,
                "initial_valuation": 2, "endpoint_valuation": 2,
            })

        start = 128 * s + 39
        a, b, endpoint, states = direct_block(start)
        transitions += len(states)
        assert (a, b) == (3, 1)
        assert endpoint == 216 * s + 67
        assert valuation_two(start + 5) == 2
        endpoint_valuation = valuation_two(endpoint + 5)
        assert endpoint_valuation == 3 + valuation_two(3 * s + 1)
        assert 11 * (endpoint + 5) - 18 * (start + 5) == 72 * s >= 0
        assert min(states) > start
        maximum_valuation_gain = max(maximum_valuation_gain, endpoint_valuation - 2)
        if s in (0, 1, 2):
            examples.append({
                "family": "valuation_increasing", "s": s,
                "start": start, "states": states,
                "initial_valuation": 2, "endpoint_valuation": endpoint_valuation,
            })

    return {
        "result": "PASS",
        "scope": "Finite arithmetic checks only; L004 contains the unrestricted proof.",
        "domain_check": {
            "odd_starts_checked": residue_starts,
            "full_periods_modulo_32": 512,
            "matching_3_1_blocks": domain_matches,
        },
        "witness_check": {
            "s_values": "0..255 and (4^k-1)/3 for k=0..32, without duplicates",
            "parameters_per_family": len(parameters),
            "witness_starts_checked": 2 * len(parameters),
            "largest_valuation_gain_checked": maximum_valuation_gain,
        },
        "shortcut_transitions_checked": transitions,
        "potential_sign_checks": "Exact integer ratio bounds; valuation terms cancel in the first family.",
        "examples": examples,
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

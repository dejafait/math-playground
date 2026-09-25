"""Check L003 by direct shortcut iteration; this is not a convergence test."""

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


def check_exact_prefix_length(start):
    expected = (valuation_two(start + 5) - 1) // 3
    current = start
    transitions = 0
    for index in range(expected + 1):
        a, b, endpoint, states = direct_block(current)
        transitions += len(states)
        if index < expected:
            assert (a, b) == (2, 1), (start, index, a, b)
            assert min(states) > current >= start
            assert (endpoint + 5) * 8 ** (index + 1) == (
                9 ** (index + 1) * (start + 5)
            )
            current = endpoint
        else:
            assert (a, b) != (2, 1), (start, index, a, b)
    return expected, transitions


def check():
    residue_starts = 0
    witness_starts = 0
    transitions = 0
    residue_periods = []

    for k in range(1, 6):
        modulus = 2 ** (3 * k + 1)
        matches = []
        for start in range(1, modulus, 2):
            prefix_length, steps = check_exact_prefix_length(start)
            transitions += steps
            residue_starts += 1
            assert (prefix_length >= k) == ((start + 5) % modulus == 0)
            if prefix_length >= k:
                matches.append(start)
        assert matches == [modulus - 5], (k, matches)
        residue_periods.append({
            "K": k, "modulus": modulus,
            "matching_start_in_period": matches[0],
        })

    for k in range(1, 33):
        for q in range(1, 17):
            for t in (1, 2, 3, 17):
                start = 2 ** (3 * k + 1) * q * t - 5
                current = start
                for j in range(1, k + 1):
                    a, b, endpoint, states = direct_block(current)
                    transitions += len(states)
                    assert (a, b) == (2, 1), (k, q, t, j, a, b)
                    assert min(states) > current >= start
                    assert endpoint == 9**j * 2 ** (3 * (k - j) + 1) * q * t - 5
                    assert endpoint % q == start % q == (-5) % q
                    assert endpoint * 8**j > start * 9**j
                    current = endpoint
                length, steps = check_exact_prefix_length(start)
                transitions += steps
                assert length == k + valuation_two(q * t) // 3
                witness_starts += 1

    examples = []
    for k in (1, 2, 3, 4, 8):
        start = 2 ** (3 * k + 1) - 5
        current = start
        endpoints = [start]
        for _ in range(k):
            a, b, current, states = direct_block(current)
            transitions += len(states)
            assert (a, b) == (2, 1)
            endpoints.append(current)
        examples.append({"K": k, "endpoints": endpoints})

    return {
        "result": "PASS",
        "scope": "Finite arithmetic checks only; L003 contains the unrestricted proof.",
        "residue_periods": residue_periods,
        "odd_starts_in_residue_periods_checked": residue_starts,
        "parameterized_witnesses": {
            "K_range": [1, 32], "q_range": [1, 16], "t_values": [1, 2, 3, 17],
            "starts_checked": witness_starts,
        },
        "shortcut_transitions_checked": transitions,
        "examples": examples,
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

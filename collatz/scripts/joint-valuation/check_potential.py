"""Check L006's two-block valuation return; this is not a convergence test."""

import json
from fractions import Fraction


def valuation_two(value):
    assert value > 0
    return (value & -value).bit_length() - 1


def joint_valuation(value):
    return valuation_two(value + 5), valuation_two(11 * value + 19)


def direct_block(start):
    assert start > 0 and start % 2 == 1
    current = start
    odd_steps = even_steps = 0
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
    transitions = domain_starts = allowed_blocks = 0
    # Check both domains and all four shifted identities independently of
    # the constructed family, using actual maximal shortcut runs.
    for start in range(1, 2048, 2):
        a, b, endpoint, states = direct_block(start)
        domain_starts += 1
        transitions += len(states)
        assert ((a, b) == (2, 1)) == (start % 16 == 11)
        assert ((a, b) == (3, 1)) == (start % 32 == 7)
        x, y = start + 5, 11 * start + 19
        next_x, next_y = endpoint + 5, 11 * endpoint + 19
        if (a, b) == (2, 1):
            allowed_blocks += 1
            assert 8 * next_x == 9 * x
            assert 8 * next_y == 9 * (y + 4)
            assert joint_valuation(start)[0] >= 4
            assert joint_valuation(start)[1] == 2
        if (a, b) == (3, 1):
            allowed_blocks += 1
            assert 16 * next_x == 27 * x - 36
            assert 16 * next_y == 27 * y
            assert joint_valuation(start)[0] == 2
            assert joint_valuation(start)[1] >= 5

    parameters = sorted(set(range(256)) | {2**k for k in (16, 32, 64, 128, 256)})
    examples = []
    for s in parameters:
        n0 = 8192 * s + 4699
        a0, b0, n1, states0 = direct_block(n0)
        a1, b1, n2, states1 = direct_block(n1)
        transitions += len(states0) + len(states1)
        assert (a0, b0) == (2, 1)
        assert (a1, b1) == (3, 1)
        assert n1 == 9216 * s + 5287
        assert n2 == 15552 * s + 8923
        assert joint_valuation(n0) == (5, 2)
        assert joint_valuation(n1) == (2, 6)
        assert joint_valuation(n2) == (5, 2)
        assert min(states0) > n0
        assert min(states1) > n1
        assert Fraction(n1 + 5, n0 + 5) == Fraction(9, 8)
        assert 49 * (n2 + 5) - 93 * (n0 + 5) == 192 * s >= 0
        assert Fraction(n2 + 5, n0 + 5) >= Fraction(93, 49) > 1
        if s in (0, 1, 2):
            examples.append({
                "s": s,
                "block_endpoints": [n0, n1, n2],
                "shortcut_states_after_start": states0 + states1,
                "valuation_pairs": [joint_valuation(n) for n in (n0, n1, n2)],
                "shifted_size_ratio": str(Fraction(n2 + 5, n0 + 5)),
            })

    return {
        "result": "PASS",
        "scope": "Finite arithmetic checks only; L006 proves the unrestricted obstruction.",
        "domain_check": {
            "odd_starts_checked": domain_starts,
            "matching_allowed_blocks": allowed_blocks,
            "range": "1 <= n < 2048",
        },
        "witness_check": {
            "s_values": "0..255 and 2^k for k=16,32,64,128,256",
            "parameters_checked": len(parameters),
            "block_paths_checked": len(parameters),
            "valuation_return": "(5,2), (2,6), (5,2)",
        },
        "shortcut_transitions_checked": transitions,
        "potential_sign_check": "Exact cancellation for every F; ratio >= 93/49 > 1.",
        "examples": examples,
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

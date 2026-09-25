"""Compare L002 with direct integer iteration; this is not a convergence test."""

import json


def valuation_two(value):
    assert value > 0
    return (value & -value).bit_length() - 1


def direct_block(start):
    current = start
    odd_steps = 0
    even_steps = 0
    minimum_after_start = None
    while current % 2:
        current = (3 * current + 1) // 2
        odd_steps += 1
        minimum_after_start = (
            current if minimum_after_start is None
            else min(minimum_after_start, current)
        )
    while current % 2 == 0:
        current //= 2
        even_steps += 1
        minimum_after_start = min(minimum_after_start, current)
    return odd_steps, even_steps, current, minimum_after_start


def check_start(a, u):
    start = 2**a * u - 1
    first_even = 3**a * u - 1
    b = valuation_two(first_even)
    endpoint = first_even // 2**b
    actual_a, actual_b, actual_endpoint, minimum = direct_block(start)
    assert (actual_a, actual_b, actual_endpoint) == (a, b, endpoint), (a, u)
    assert endpoint * 2 ** (a + b) == 3**a * start + 3**a - 2**a
    exact_descent = (2 ** (a + b) - 3**a) * u > 2**b - 1
    assert (endpoint < start) == exact_descent == (minimum < start), (a, u)
    assert endpoint * 2 ** (a + b) > 3**a * start
    if exact_descent:
        assert 2 ** (a + b) > 3**a
    return b, endpoint, a + b


def check():
    grid_starts = 0
    congruence_starts = 0
    growth_starts = 0
    transitions = 0
    endpoint_counts = {"below_start": 0, "equal_to_start": 0, "above_start": 0}
    for a in range(1, 65):
        for u in range(1, 512, 2):
            _, endpoint, steps = check_start(a, u)
            start = 2**a * u - 1
            comparison = (
                "below_start" if endpoint < start
                else "equal_to_start" if endpoint == start
                else "above_start"
            )
            endpoint_counts[comparison] += 1
            grid_starts += 1
            transitions += steps

    for a in range(1, 33):
        for b in range(1, 33):
            modulus = 2 ** (b + 1)
            residue = pow(3**a, -1, modulus) * (1 + 2**b) % modulus
            assert residue > 0 and residue % 2 == 1
            for t in (0, 1, 2, 17):
                u = residue + modulus * t
                actual_b, endpoint, steps = check_start(a, u)
                assert actual_b == b, (a, b, t)
                if a >= 2 and b == 1:
                    assert endpoint > 2**a * u - 1
                congruence_starts += 1
                transitions += steps

    for t in (*range(1000), 10**20, 2**128):
        b, endpoint, steps = check_start(2, 4 * t + 3)
        assert b == 1 and endpoint == 18 * t + 13
        assert endpoint - (16 * t + 11) == 2 * t + 2
        growth_starts += 1
        transitions += steps

    examples = []
    for start in (1, 3, 7, 11, 15, 27, 31):
        a, b, endpoint, minimum = direct_block(start)
        examples.append({
            "start": start, "a": a, "b": b, "endpoint": endpoint,
            "minimum_after_start_in_block": minimum,
        })

    return {
        "result": "PASS",
        "scope": "Finite sanity checks only; L002 contains the unrestricted proof.",
        "grid": {
            "a_range": [1, 64], "odd_u_range": [1, 511],
            "starts_checked": grid_starts, "endpoint_counts": endpoint_counts,
        },
        "prescribed_run_lengths": {
            "a_range": [1, 32], "b_range": [1, 32], "t_values": [0, 1, 2, 17],
            "starts_checked": congruence_starts,
        },
        "explicit_growth_family": {"starts_checked": growth_starts},
        "shortcut_transitions_checked": transitions,
        "examples": examples,
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

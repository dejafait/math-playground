"""Exact four-type inverse checks against independent forward block iteration."""

from collections import Counter
import json


ALPHABET = ((1, 1), (2, 1), (3, 1), (1, 2))
EXISTENCE = {
    (1, 1): (3, {1}),
    (2, 1): (9, {4}),
    (3, 1): (27, {13}),
    (1, 2): (3, {2}),
}
EXTENDIBILITY = {
    (1, 1): (9, {1, 4}),
    (2, 1): (27, {13, 22}),
    (3, 1): (81, {13, 40}),
    (1, 2): (9, {2, 5}),
}


def direct_block(start):
    assert start > 0 and start % 2 == 1
    current = start
    odd_run = even_run = 0
    while current % 2:
        current = (3 * current + 1) // 2
        odd_run += 1
    while current % 2 == 0:
        current //= 2
        even_run += 1
    return (odd_run, even_run), current


def inverse_branches(endpoint):
    result = []
    for a, b in ALPHABET:
        numerator = 2**a * (2**b * endpoint + 1)
        if numerator % 3**a == 0:
            result.append(((a, b), numerator // 3**a - 1))
    return sorted(result)


def check():
    # A two-block word has at most six odd steps, so every inverse
    # integrality condition has modulus dividing 3**6. The factor 2
    # retains odd endpoints. Exact runs and positivity follow from
    # L010; the forward search below checks all cases in this period.
    period = 2 * 3**6
    endpoint_limit = period - 1
    # Every allowed inverse is <= (8m-1)/3. Applying this twice ensures
    # that forward enumeration contains every required predecessor.
    predecessor_limit = (8 * endpoint_limit - 1) // 3
    earliest_limit = (8 * predecessor_limit - 1) // 3
    incoming = {m: [] for m in range(1, predecessor_limit + 1, 2)}
    forward_starts_checked = 0
    for start in range(1, earliest_limit + 1, 2):
        block_type, endpoint = direct_block(start)
        forward_starts_checked += 1
        if block_type in ALPHABET and endpoint in incoming:
            incoming[endpoint].append((block_type, start))
    for branches in incoming.values():
        branches.sort()

    immediate_counts = Counter()
    extendible_counts = Counter()
    depth_two_counts = Counter()
    max_depth_two = 0
    least_sharp_endpoint = None
    sharp_histories = None
    for m in range(1, period, 2):
        actual = incoming[m]
        predicted_types = sorted(
            block_type
            for block_type, (modulus, residues) in EXISTENCE.items()
            if m % modulus in residues
        )
        assert [block_type for block_type, _ in actual] == predicted_types
        assert actual == inverse_branches(m), m
        assert bool(actual) == (m % 3 != 0)
        assert len(actual) <= 3
        immediate_counts.update(str(block_type) for block_type, _ in actual)

        actual_extendible = [
            block_type for block_type, n in actual if incoming[n]
        ]
        predicted_extendible = sorted(
            block_type
            for block_type, (modulus, residues) in EXTENDIBILITY.items()
            if m % modulus in residues
        )
        assert actual_extendible == predicted_extendible, m
        assert len(actual_extendible) <= 3
        assert (len(actual_extendible) == 3) == (m % 81 in {13, 40})
        extendible_counts.update(str(block_type) for block_type in actual_extendible)

        histories = sorted(
            (earlier, middle, m)
            for _, middle in actual
            for _, earlier in incoming[middle]
        )
        predicted_histories = sorted(
            (earlier, middle, m)
            for _, middle in inverse_branches(m)
            for _, earlier in inverse_branches(middle)
        )
        assert histories == predicted_histories
        assert len(histories) == len(set(histories)) <= 5
        depth_two_counts[len(histories)] += 1
        if len(histories) > max_depth_two:
            max_depth_two = len(histories)
            least_sharp_endpoint = m
            sharp_histories = histories

    assert max_depth_two == 5 and least_sharp_endpoint == 661
    expected_sharp = sorted([
        (2349, 881, 661),
        (1565, 587, 661),
        (521, 391, 661),
        (347, 391, 661),
        (231, 391, 661),
    ])
    assert sharp_histories == expected_sharp
    assert incoming[1] == [((1, 1), 1)]

    lifts_checked = (0, 1, 2, 17, 10**6)
    for t in lifts_checked:
        m = 162 * t + 13
        families = (
            ((576 * t + 45, 216 * t + 17, m), ((1, 2), (1, 1))),
            ((384 * t + 29, 144 * t + 11, m), ((1, 2), (2, 1))),
            ((128 * t + 9, 96 * t + 7, m), ((1, 1), (3, 1))),
        )
        assert len({states[1] for states, _ in families}) == 3
        for states, block_types in families:
            for i, block_type in enumerate(block_types):
                assert direct_block(states[i]) == (block_type, states[i + 1])

    return {
        "result": "PASS",
        "scope": "Exact inverse and extendibility classes; sharp depth-two count. No infinite-orbit claim.",
        "complete_odd_residue_period_for_depth_two": period,
        "odd_endpoints_checked": period // 2,
        "independent_forward_starts_checked": forward_starts_checked,
        "forward_start_bound": earliest_limit,
        "immediate_branch_counts": dict(sorted(immediate_counts.items())),
        "extendible_branch_counts": dict(sorted(extendible_counts.items())),
        "depth_two_count_distribution": dict(sorted(depth_two_counts.items())),
        "max_depth_two_histories": max_depth_two,
        "least_endpoint_attaining_maximum": least_sharp_endpoint,
        "sharp_histories": sharp_histories,
        "positive_family_parameters_checked": lifts_checked,
        "fixed_point_predecessors": incoming[1],
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

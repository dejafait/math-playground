"""Exact tests for inverse branching in the (2,1)/(3,1) block alphabet."""

import itertools
import json


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
    return odd_run, even_run, current


def predecessors(endpoint):
    result = []
    for odd_run, numerator, denominator in (
        (2, 8 * endpoint - 5, 9),
        (3, 16 * endpoint - 19, 27),
    ):
        if numerator % denominator:
            continue
        start = numerator // denominator
        assert start > 0 and start % 2 == 1
        assert direct_block(start) == (odd_run, 1, endpoint)
        result.append((odd_run, start))
    return result


def least_word_start(word):
    odd_steps = all_steps = offset = 0
    for odd_run in word:
        offset = 3**odd_run * offset + (3**odd_run - 2**odd_run) * 2**all_steps
        odd_steps += odd_run
        all_steps += odd_run + 1
    modulus = 2 ** (all_steps + 1)
    start = (pow(3**odd_steps, -1, modulus) * (2**all_steps - offset)) % modulus
    return start, modulus


def check():
    # Forward enumeration is independent of the inverse congruence tests.
    period = 2 * 3**5
    incoming = {endpoint: [] for endpoint in range(1, period, 2)}
    for start in range(1, period, 2):
        a, b, endpoint = direct_block(start)
        if a in (2, 3) and b == 1 and endpoint < period:
            incoming[endpoint].append((a, start))

    immediate_counts = {"2": 0, "3": 0, "both": 0}
    extendible_counts = {"2": 0, "3": 0}
    for endpoint, actual in incoming.items():
        actual.sort()
        predicted = []
        if endpoint % 9 == 4:
            predicted.append((2, (8 * endpoint - 5) // 9))
            immediate_counts["2"] += 1
        if endpoint % 27 == 13:
            predicted.append((3, (16 * endpoint - 19) // 27))
            immediate_counts["3"] += 1
        assert predicted == actual == predecessors(endpoint), endpoint
        immediate_counts["both"] += len(actual) == 2

        actual_extendible = [a for a, start in actual if incoming[start]]
        predicted_extendible = []
        if endpoint % 81 == 76:
            predicted_extendible.append(2)
            extendible_counts["2"] += 1
        if endpoint % 243 == 175:
            predicted_extendible.append(3)
            extendible_counts["3"] += 1
        assert actual_extendible == predicted_extendible, endpoint
        assert len(actual_extendible) <= 1
        if len(actual) == 2:
            assert not incoming[dict(actual)[2]]

    words_checked = endpoints_checked = history_levels_checked = 0
    two_history_levels = 0
    largest_endpoint = 0
    for length in range(1, 9):
        for word in itertools.product((2, 3), repeat=length):
            residue, modulus = least_word_start(word)
            words_checked += 1
            for lift in (0, 1):
                start = residue + lift * modulus
                states = [start]
                for a in word:
                    actual_a, actual_b, endpoint = direct_block(states[-1])
                    assert (actual_a, actual_b) == (a, 1)
                    states.append(endpoint)
                endpoint = states[-1]
                largest_endpoint = max(largest_endpoint, endpoint)
                endpoints_checked += 1

                histories = [(endpoint,)]
                for depth in range(1, length + 1):
                    histories = [
                        (earlier,) + history
                        for history in histories
                        for _, earlier in predecessors(history[0])
                    ]
                    assert tuple(states[-depth - 1:]) in histories
                    assert 1 <= len(histories) <= 2
                    if len(histories) == 2:
                        assert histories[0][0] != histories[1][0]
                        assert histories[0][1:] == histories[1][1:]
                        two_history_levels += 1
                    for history in histories:
                        assert 9**depth * history[0] < 8**depth * endpoint
                        for i in range(2, len(history)):
                            later, earlier = history[i], history[i - 1]
                            if later % 81 == 76:
                                assert earlier == (8 * later - 5) // 9
                            else:
                                assert later % 243 == 175
                                assert earlier == (16 * later - 19) // 27
                    history_levels_checked += 1

    assert predecessors(13) == [(2, 11), (3, 7)]
    assert predecessors(175) == [(2, 155), (3, 103)]
    assert predecessors(155) == []
    assert predecessors(103) == [(2, 91)]
    assert predecessors(319) == [(2, 283)]
    assert predecessors(283) == [(2, 251), (3, 167)]
    return {
        "result": "PASS",
        "scope": "Inverse congruences and finite histories only; no forward escape claim.",
        "complete_odd_residue_period": period,
        "odd_endpoints_checked_in_period": period // 2,
        "immediate_branch_counts": immediate_counts,
        "extendible_branch_counts": extendible_counts,
        "mixed_words_checked": words_checked,
        "constructed_endpoints_checked": endpoints_checked,
        "backward_history_levels_checked": history_levels_checked,
        "levels_with_two_histories": two_history_levels,
        "largest_constructed_endpoint": largest_endpoint,
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

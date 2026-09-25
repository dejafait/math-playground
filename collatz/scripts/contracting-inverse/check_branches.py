"""Exact checks for the (1,1)/(2,1)/(3,1) inverse decoder."""

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
    for a in (1, 2, 3):
        numerator = 2**a * (2 * endpoint + 1)
        if numerator % 3**a:
            continue
        start = numerator // 3**a - 1
        assert direct_block(start) == (a, 1, endpoint)
        result.append((a, start))
    return result


def extendible_types(endpoint):
    return [
        a
        for a, modulus, residue in ((1, 9, 1), (2, 27, 22), (3, 81, 13))
        if endpoint % modulus == residue
    ]


def valuation_decoder(endpoint):
    unit = 2 * endpoint + 1
    exponent = 0
    while unit % 3 == 0:
        exponent += 1
        unit //= 3
    if exponent in (1, 2, 3) and 2**exponent * unit % 3 == 2:
        return [exponent]
    return []


def least_word_start(word):
    odd_steps = all_steps = offset = 0
    for a in word:
        offset = 3**a * offset + (3**a - 2**a) * 2**all_steps
        odd_steps += a
        all_steps += a + 1
    modulus = 2 ** (all_steps + 1)
    start = pow(3**odd_steps, -1, modulus) * (2**all_steps - offset) % modulus
    return start, modulus


def check():
    # Every possible inverse satisfies n <= (4m-1)/3. The two bounds
    # ensure forward enumeration includes all predecessors needed to
    # decide extendibility for endpoints in the complete period.
    period = 2 * 3**4
    endpoint_limit = period - 1
    predecessor_limit = (4 * endpoint_limit - 1) // 3
    earliest_limit = (4 * predecessor_limit - 1) // 3
    incoming = {m: [] for m in range(1, predecessor_limit + 1, 2)}
    forward_starts_checked = 0
    for start in range(1, earliest_limit + 1, 2):
        a, b, endpoint = direct_block(start)
        forward_starts_checked += 1
        if a in (1, 2, 3) and b == 1 and endpoint in incoming:
            incoming[endpoint].append((a, start))
    for actual in incoming.values():
        actual.sort()

    immediate_counts = {str(a): 0 for a in (1, 2, 3)}
    extendible_counts = {str(a): 0 for a in (1, 2, 3)}
    for m in range(1, period, 2):
        predicted = []
        for a, modulus, residue in ((1, 3, 1), (2, 9, 4), (3, 27, 13)):
            if m % modulus == residue:
                predicted.append((a, 2**a * (2 * m + 1) // 3**a - 1))
                immediate_counts[str(a)] += 1
        actual = incoming[m]
        assert predicted == actual == predecessors(m), m
        assert bool(actual) == (m % 3 == 1)
        actual_extendible = [a for a, start in actual if incoming[start]]
        assert actual_extendible == extendible_types(m) == valuation_decoder(m), m
        assert len(actual_extendible) <= 1
        for a in actual_extendible:
            extendible_counts[str(a)] += 1

    words_checked = endpoints_checked = history_levels_checked = 0
    three_history_levels = 0
    for length in range(1, 8):
        for word in itertools.product((1, 2, 3), repeat=length):
            residue, modulus = least_word_start(word)
            words_checked += 1
            for lift in (0, 1):
                states = [residue + lift * modulus]
                for a in word:
                    actual_a, actual_b, endpoint = direct_block(states[-1])
                    assert (actual_a, actual_b) == (a, 1)
                    states.append(endpoint)
                endpoints_checked += 1
                histories = [(states[-1],)]
                for depth in range(1, length + 1):
                    histories = [
                        (earlier,) + history
                        for history in histories
                        for _, earlier in predecessors(history[0])
                    ]
                    assert tuple(states[-depth - 1:]) in histories
                    assert 1 <= len(histories) <= 3
                    assert len({h[1:] for h in histories}) == 1
                    assert len({h[0] for h in histories}) == len(histories)
                    if len(histories) == 3:
                        three_history_levels += 1
                    for history in histories:
                        if history[-1] == 1:
                            assert all(n == 1 for n in history)
                        for i in range(2, len(history)):
                            m, earlier = history[i], history[i - 1]
                            branch = extendible_types(m)
                            assert branch == valuation_decoder(m) and len(branch) == 1
                            a = branch[0]
                            assert earlier == 2**a * (2 * m + 1) // 3**a - 1
                    history_levels_checked += 1

    assert direct_block(1) == (1, 1, 1)
    assert predecessors(1) == [(1, 1)]
    assert extendible_types(19) == [1]
    assert predecessors(19) == [(1, 25)]
    assert predecessors(91) == [(1, 121)]
    sharp_histories = [
        (earlier, middle, 91)
        for _, middle in predecessors(91)
        for _, earlier in predecessors(middle)
    ]
    assert sharp_histories == [(161, 121, 91), (107, 121, 91), (71, 121, 91)]
    return {
        "result": "PASS",
        "scope": "Exact inverse arithmetic and finite histories; no escape or convergence claim.",
        "complete_odd_residue_period": period,
        "odd_endpoints_checked_in_period": period // 2,
        "independent_forward_starts_checked": forward_starts_checked,
        "forward_start_bound": earliest_limit,
        "immediate_branch_counts": immediate_counts,
        "extendible_branch_counts": extendible_counts,
        "mixed_words_checked": words_checked,
        "constructed_endpoints_checked": endpoints_checked,
        "backward_history_levels_checked": history_levels_checked,
        "levels_with_three_histories": three_history_levels,
        "sharp_depth_two_histories": sharp_histories,
        "extendible_inverse_growth_example": {"endpoint": 19, "predecessor": 25},
        "fixed_point_predecessors": predecessors(1),
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

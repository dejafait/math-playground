"""Exact finite sanity check of the unrestricted proof in L001."""

import json


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def check():
    starts = 0
    transitions = 0
    for q in range(1, 33):
        for window in range(1, 25):
            for multiplier in (1, 2, 3, 17):
                start = 2 ** (window + 1) * q * multiplier - 1
                current = start
                for j in range(window + 1):
                    expected = 3**j * 2 ** (window + 1 - j) * q * multiplier - 1
                    assert current == expected, (q, window, multiplier, j)
                    assert current > 0 and current % 2 == 1
                    assert current % q == start % q == (q - 1)
                    if j:
                        assert current * 2**j > start * 3**j
                    if j < window:
                        current = shortcut(current)
                        transitions += 1
                starts += 1

    example = [2**6 * 6 - 1]
    for _ in range(5):
        example.append(shortcut(example[-1]))
    return {
        "result": "PASS",
        "scope": "Finite sanity check only; L001 contains the universal proof.",
        "q_range": [1, 32],
        "K_range": [1, 24],
        "t_values": [1, 2, 3, 17],
        "starting_values_checked": starts,
        "shortcut_transitions_checked": transitions,
        "example": {"q": 6, "K": 5, "t": 1, "orbit_prefix": example},
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

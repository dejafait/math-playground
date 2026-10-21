"""Exact bounded postspell screen; finite replays do not prove convergence."""

import json


def replay(root, word):
    states = [root]
    for letter in word:
        x = states[-1]
        assert x > 0 and x % 2 == (letter == "O")
        states.append((3 * x + 1) // 2 if letter == "O" else x // 2)
    return states


def parity_class(word):
    multiplier, offset, residue = 1, 0, 0
    for i, letter in enumerate(word):
        modulus = 1 << i
        assert (multiplier * residue + offset) % modulus == 0
        if ((multiplier * residue + offset) // modulus) % 2 != (letter == "O"):
            residue += modulus
        if letter == "O":
            multiplier, offset = 3 * multiplier, 3 * offset + modulus
    return multiplier, offset, residue


def valuation(value, prime):
    assert value > 0
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def check():
    improving = []
    rejected = 0
    replay_count = 0
    for j in range(2, 13):
        for h in range(3, 13):
            e = j + h + (2 - j - h) % 18
            for a in range(2, e, 18):
                word = "OOEO" * j + "O" * h + "E" * a
                multiplier, offset, residue = parity_class(word)
                modulus = 1 << len(word)
                assert multiplier == 3 ** (3 * j + h)
                closed_offset = (
                    23 * 3**h * ((27**j - 16**j) // 11)
                    + (3**h - 2**h) * 16**j
                )
                assert (27**j - 16**j) % 11 == 0
                assert offset == closed_offset > 0
                root = residue + modulus * ((20 - residue) * pow(modulus, -1, 27) % 27)
                period = 27 * modulus
                delta = modulus - multiplier
                for lift in (0, 1, 7):
                    n = root + lift * period
                    states = replay(n, word)
                    z, m = states[4 * j + h], states[-1]
                    assert n % 27 == m % 27 == 20
                    assert m * modulus == multiplier * n + offset
                    assert z == m * 2**a and valuation(z, 2) >= a
                    assert (m < n) == (delta * n > offset)
                    replay_count += 1
                if delta > 0:
                    assert a == 20 and j + h >= 21 and e == 38
                    assert offset < delta  # Every positive actual root descends.
                    improving.append({
                        "J": j, "H": h, "a": a, "old_e": e,
                        "D": len(word), "A": multiplier, "C": offset,
                        "delta": delta, "least_CRT_root": root,
                        "endpoint": replay(root, word)[-1],
                    })
                else:
                    assert a == 2 and delta < 0
                    rejected += 1

    assert len(improving) == 10 and rejected == 110 and replay_count == 360
    assert 34 * 3**48 < 11 * 2**80
    assert 3**9 > 2**13
    # A witness with exactly twenty available E steps, surviving L014--L018.
    j, h, a = 11, 10, 20
    root = 470239661327756758709339
    endpoint = 8171720986502293243553
    period = 59049 * 2**75
    word = "OOEO" * j + "O" * h + "E" * a
    for t in (0, 1, 2):
        n = root + period * t
        states = replay(n, word)
        m, z = states[-1], states[54]
        assert m == endpoint + 2 * 59049 * 3**43 * t
        assert m % 2 == 1 and valuation(z, 2) == 20
        assert 0 < m < n and n % 243 == 47 and m % 27 == 20
        assert valuation(n + 7, 3) == valuation(4 * n + 1, 3) == 3
        assert valuation(128 * n - 157, 3) == 3
        assert n % 19683 == 776 and n % 59049 == 40142
    return {
        "result": "PASS",
        "scope": "2<=J<=12, 3<=H<=12, all a=2 mod18 below e(J,H); exact finite checks only.",
        "triples_checked": 120, "noncontracting_triples": rejected,
        "CRT_replays": replay_count, "improving_triples": improving,
        "exact_tail_witness": {
            "J": j, "H": h, "a": a, "old_e": 38,
            "root": root, "endpoint": endpoint,
            "v2_prefix_endpoint": 20, "total_steps": 74,
            "family_root_increment": period,
            "family_endpoint_increment": 2 * 59049 * 3**43,
            "family_replays": 3,
        },
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

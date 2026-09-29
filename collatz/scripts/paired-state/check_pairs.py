"""Exact coupled backward test for L011, retaining its one-block offset.

Run from the notebook: python3 scripts/paired-state/check_pairs.py
Every node describes two compatible suffixes for all integer t >= 0.
The second suffix is one block shorter. An additional inverse on that
side gives equal depths, when both original-start inequalities are tested.
This is a bounded search, not an all-depth or convergence assertion.
"""

import argparse
from dataclasses import dataclass
from math import gcd
import json


ALPHABET = ((1, 1), (2, 1), (3, 1), (1, 2))


@dataclass(frozen=True)
class Pair:
    # Each (p, c) represents p*t+c, t a nonnegative integer.
    left: tuple
    right: tuple
    left_word: tuple
    right_word: tuple


def inverse_condition(affine, block):
    p, c = affine
    a, b = block
    factor, denominator, correction = 2**(a+b), 3**a, 3**a-2**a
    coefficient = factor*p
    rhs = correction-factor*c
    common = gcd(coefficient, denominator)
    if rhs % common:
        return None
    modulus = denominator // common
    residue = (rhs // common) * pow(coefficient // common, -1, modulus) % modulus
    return residue, modulus


def combine(left, right):
    if left is None or right is None:
        return None
    if left[1] > right[1]:
        left, right = right, left
    assert right[1] % left[1] == 0
    if right[0] % left[1] != left[0]:
        return None
    return right


def lift(affines, congruence):
    residue, modulus = congruence
    return tuple((p*modulus, p*residue+c) for p, c in affines)


def inverse(affine, block):
    p, c = affine
    a, b = block
    factor, denominator, correction = 2**(a+b), 3**a, 3**a-2**a
    assert factor*p % denominator == 0
    assert (factor*c-correction) % denominator == 0
    result = factor*p // denominator, (factor*c-correction) // denominator
    assert result[0] > 0 and result[0] % 2 == 0
    assert result[1] > 0 and result[1] % 2 == 1
    return result


def extend(pair):
    for left_block in ALPHABET:
        lc = inverse_condition(pair.left[0], left_block)
        for right_block in ALPHABET:
            rc = inverse_condition(pair.right[0], right_block)
            condition = combine(lc, rc)
            if condition is None:
                continue
            left, right = lift(pair.left, condition), lift(pair.right, condition)
            yield Pair((inverse(left[0], left_block),)+left,
                       (inverse(right[0], right_block),)+right,
                       (left_block,)+pair.left_word,
                       (right_block,)+pair.right_word)


def equal_depth_pairs(pair):
    for block in ALPHABET:
        condition = inverse_condition(pair.right[0], block)
        if condition is None:
            continue
        left, right = lift(pair.left, condition), lift(pair.right, condition)
        yield Pair(left, (inverse(right[0], block),)+right,
                   pair.left_word, (block,)+pair.right_word)


def feasible_parameter(pair):
    lower, upper = 0, None
    for states in (pair.left, pair.right):
        p0, c0 = states[0]
        inequalities = [(p0, c0-3)]
        inequalities += [(p-p0, c-c0) for p, c in states[1:]]
        for p, c in inequalities:
            # p*t+c >= 0, including t>=0 and each start>=3.
            if p > 0:
                lower = max(lower, -(c // p))
            elif p < 0:
                bound = c // (-p)
                upper = bound if upper is None else min(upper, bound)
            elif c < 0:
                return None
    if upper is not None and lower > upper:
        return None
    return lower, upper


def direct_history(start, depth):
    n = start
    states, word, minimum = [n], [], n
    for _ in range(depth):
        a = b = 0
        while n % 2:
            n = (3*n+1)//2
            minimum = min(minimum, n)
            a += 1
        while n % 2 == 0:
            n //= 2
            minimum = min(minimum, n)
            b += 1
        states.append(n)
        word.append((a, b))
    return tuple(states), tuple(word), minimum


def verify(pair, parameter, admitted):
    histories = []
    for affines, word in ((pair.left, pair.left_word), (pair.right, pair.right_word)):
        expected = tuple(p*parameter+c for p, c in affines)
        actual, actual_word, minimum = direct_history(expected[0], len(word))
        assert actual == expected and actual_word == word
        assert (minimum >= expected[0]) == (min(expected) >= expected[0])
        histories.append(expected)
    if admitted is not None:
        assert all(h[0] > 1 and min(h) >= h[0] for h in histories) == admitted
    assert histories[0][-1] == histories[1][-1]
    assert histories[0][-2] != histories[1][-2]
    return histories


def roots():
    # L011: s=2 gives y=48t+43; s=3 gives y=96t+7.
    # These retain oddness of m=(3^s*w-1)/2 and 3 not dividing w.
    for s, p, c in ((2, 48, 43), (3, 96, 7)):
        y = p, c
        z = 4*p, 4*c+1
        x = 3*p//2, (3*c+1)//2
        m = 3**s*p // 2**(s+1), (3**s*(c+1)-2**s) // 2**(s+1)
        yield Pair((z, x, m), (y, m), ((1, 2), (s-1, 1)), ((s, 1),))


def check_transition_table():
    checked = 0
    for t in (*range(81), 10**6):
        v = 6*t+1
        u = 8*v+5
        expected = {(1, 1)}
        if v % 9 == 1:
            expected.add((2, 1))
        if v % 27 == 1:
            expected.add((3, 1))
        if v % 9 == 4:
            expected.add((1, 2))
        if v % 27 == 13:
            expected.add((1, 3))
        actual = set()
        for a in (1, 2, 3):
            for b in (1, 2, 3):
                if (2*u+1) % 3**a or (2*v+1) % 3**b:
                    continue
                p = 2**a*(2*u+1)//3**a-1
                q = 2**b*(2*v+1)//3**b-1
                numerators = {(1, 1): (8*q+9, 1),
                              (2, 1): (16*q+17, 3),
                              (3, 1): (32*q+31, 9),
                              (1, 2): (12*q+13, 1),
                              (1, 3): (18*q+19, 1)}
                numerator, denominator = numerators[(a, b)]
                assert denominator*p == numerator
                assert direct_history(p, 1)[:2] == ((p, u), ((a, 1),))
                assert direct_history(q, 1)[:2] == ((q, v), ((b, 1),))
                actual.add((a, b))
                checked += 1
        assert actual == expected
    return checked


def search(max_depth, node_limit):
    frontier = list(roots())
    summaries, checks = [], 0
    for depth in range(2, max_depth+1):
        candidates = 0
        for pair in frontier:
            assert len(pair.left_word) == depth
            assert len(pair.right_word) == depth-1
            for candidate in equal_depth_pairs(pair):
                candidates += 1
                interval = feasible_parameter(candidate)
                if interval is not None:
                    parameter, upper = interval
                    histories = verify(candidate, parameter, True)
                    verify(candidate, parameter+17, upper is None or parameter+17 <= upper)
                    return {
                        "result": "WITNESS",
                        "depth": depth,
                        "parameter_interval": [parameter, upper],
                        "left_affines": candidate.left,
                        "right_affines": candidate.right,
                        "left_word": candidate.left_word,
                        "right_word": candidate.right_word,
                        "histories": histories,
                        "completed_depths": summaries,
                    }
                # Independent forward checks for every class through depth 8.
                if depth <= 8:
                    for parameter in (0, 17):
                        verify(candidate, parameter, False)
                        checks += 1
        summaries.append({"depth": depth, "paired_classes": len(frontier),
                          "equal_depth_classes": candidates, "witnesses": 0})
        if depth == max_depth:
            break
        following = []
        for pair in frontier:
            for child in extend(pair):
                following.append(child)
                if len(following) > node_limit:
                    return {"result": "BOUNDED_NO_WITNESS", "stop": "node_limit",
                            "completed_depths": summaries,
                            "forward_class_realizations_checked": checks}
        frontier = following
    return {"result": "BOUNDED_NO_WITNESS", "stop": "max_depth",
            "completed_depths": summaries,
            "forward_class_realizations_checked": checks}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=11)
    parser.add_argument("--node-limit", type=int, default=250000)
    args = parser.parse_args()
    table_checks = check_transition_table()
    result = search(args.max_depth, args.node_limit)
    result["transition_table_realizations_checked"] = table_checks
    result["requested_max_depth"] = args.max_depth
    result["node_limit"] = args.node_limit
    result["scope"] = "Exact finite-depth pair classes; no endpoint cutoff or all-depth inference."
    print(json.dumps(result, indent=2))

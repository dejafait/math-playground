"""Screen exact non-descent word classes; this is not an all-depth theorem.

Run from the Collatz notebook:
    python3 scripts/nondescending-suffix/check_histories.py

Every word of lengths 1 through 6 is considered. Endpoint classes and
non-descent inequalities are computed with integers, without a height
cutoff. Independent forward shortcut iteration checks sample realizations
and the points immediately outside each nonempty feasible interval.
"""

from collections import Counter
from dataclasses import dataclass
from itertools import combinations, product
import json


ALPHABET = ((1, 1), (2, 1), (3, 1), (1, 2))
MAX_DEPTH = 6


def ceil_div(numerator, denominator):
    assert denominator > 0
    return -((-numerator) // denominator)


def direct_history(start, depth):
    """Use only shortcut iteration, independently of the affine formulas."""
    assert start > 0 and start % 2 == 1
    current = start
    states = [start]
    word = []
    minimum = start
    for _ in range(depth):
        a = b = 0
        while current % 2:
            current = (3 * current + 1) // 2
            minimum = min(minimum, current)
            a += 1
        while current % 2 == 0:
            current //= 2
            minimum = min(minimum, current)
            b += 1
        states.append(current)
        word.append((a, b))
    return tuple(word), tuple(states), minimum


@dataclass(frozen=True)
class WordClass:
    word: tuple
    # Entry j represents n_j=(p_j*m-c_j)/q_j.
    triples: tuple
    residue: int
    modulus: int
    lower: int
    upper: object  # None means no upper bound.
    least: int

    def states(self, endpoint):
        assert endpoint % self.modulus == self.residue
        result = []
        for p, c, q in self.triples:
            numerator = p * endpoint - c
            assert numerator % q == 0
            n = numerator // q
            assert n > 0 and n % 2
            result.append(n)
        return tuple(result)


def inverse_triples(word):
    triples = [(1, 0, 1)]
    for a, b in reversed(word):
        p, c, q = triples[-1]
        triples.append((
            2 ** (a + b) * p,
            2 ** (a + b) * c + (3**a - 2**a) * q,
            3**a * q,
        ))
    return tuple(reversed(triples))


def classify(word):
    triples = inverse_triples(word)
    p0, c0, q0 = triples[0]
    # Integrality of the first inverse implies integrality of every
    # suffix: reduce its numerator modulo the suffix's power of 3,
    # then cancel the intervening power of 2. For an odd endpoint,
    # exact inverses have positive odd predecessors by L010.
    residue = c0 * pow(p0, -1, q0) % q0
    if residue % 2 == 0:
        residue += q0
    modulus = 2 * q0

    # n_0>1 means n_0>=3. All remaining inequalities have the form
    # coefficient*m >= rhs; retain upper bounds as well as lower ones.
    lower = max(1, ceil_div(c0 + 3 * q0, p0))
    upper = None
    for p, c, q in triples[1:]:
        coefficient = p * q0 - p0 * q
        rhs = c * q0 - c0 * q
        if coefficient > 0:
            lower = max(lower, ceil_div(rhs, coefficient))
        elif coefficient < 0:
            bound = rhs // coefficient
            upper = bound if upper is None else min(upper, bound)
        elif rhs > 0:
            return None, "inconsistent_constant_inequality"
    least = residue + modulus * ceil_div(lower - residue, modulus)
    if upper is not None and least > upper:
        return None, "empty_interval_on_endpoint_class"
    return WordClass(word, triples, residue, modulus, lower, upper, least), None


def overlap(left, right):
    # All moduli are 2*3^s, so one divides the other.
    if left.modulus > right.modulus:
        left, right = right, left
    assert right.modulus % left.modulus == 0
    if right.residue % left.modulus != left.residue:
        return None
    lower = max(left.lower, right.lower)
    uppers = [c.upper for c in (left, right) if c.upper is not None]
    upper = min(uppers) if uppers else None
    least = right.residue + right.modulus * ceil_div(
        lower - right.residue, right.modulus
    )
    if upper is not None and least > upper:
        return None
    return least, right.modulus, upper


def verify_realization(word_class, endpoint, admitted):
    states = word_class.states(endpoint)
    actual_word, actual_states, actual_minimum = direct_history(
        states[0], len(word_class.word)
    )
    assert actual_word == word_class.word
    assert actual_states == states
    actual_admitted = states[0] > 1 and actual_minimum >= states[0]
    assert actual_admitted == admitted
    assert (min(states) >= states[0]) == (actual_minimum >= states[0])


def check():
    # Necessary first-merge patterns from L011. These checks make no
    # claim that both paths can be non-descending at a larger depth.
    tail_family_checks = 0
    for s, w0 in ((2, 11), (3, 1)):
        for t in (0, 1, 2, 17, 10**6):
            w = 12 * t + w0
            m = (3**s * w - 1) // 2
            y = 2**s * w - 1
            assert y % 3 == 1
            tail = ((32 * y + 7) // 3, 4 * y + 1, (3 * y + 1) // 2, m)
            word, states, _ = direct_history(tail[0], 3)
            assert word == ((1, 2), (1, 2), (s - 1, 1))
            assert states == tail
            word, states, _ = direct_history(y, 1)
            assert word == ((s, 1),) and states == (y, m)
            tail_family_checks += 1
    witness_pairs = ((973, 365, 137, 103), (71, 121, 91, 103))
    for expected in witness_pairs:
        _, states, minimum = direct_history(expected[0], 3)
        assert states == expected
        assert (minimum >= states[0]) == (states[0] == 71)

    summaries = []
    violations = []
    realization_checks = boundary_checks = pair_checks = 0
    first_letter_counts = Counter()
    for depth in range(1, MAX_DEPTH + 1):
        records = []
        rejections = Counter()
        for word in product(ALPHABET, repeat=depth):
            word_class, reason = classify(word)
            if word_class is None:
                rejections[reason] += 1
                continue
            records.append(word_class)
            first_letter_counts[str(word[0])] += 1
            # Check the least member and both small and large lifts.
            for t in (0, 1, 17, 10**6):
                endpoint = word_class.least + t * word_class.modulus
                if word_class.upper is None or endpoint <= word_class.upper:
                    verify_realization(word_class, endpoint, True)
                    realization_checks += 1
            previous = word_class.least - word_class.modulus
            if previous > 0:
                verify_realization(word_class, previous, False)
                boundary_checks += 1
            if word_class.upper is not None:
                first_after = word_class.residue + word_class.modulus * (
                    (word_class.upper - word_class.residue)
                    // word_class.modulus + 1
                )
                verify_realization(word_class, first_after, False)
                boundary_checks += 1

        compatible_pairs = different_suffix_pairs = 0
        for left, right in combinations(records, 2):
            hit = overlap(left, right)
            if hit is None:
                continue
            compatible_pairs += 1
            least, period, upper = hit
            suffix_differs = left.word[1:] != right.word[1:]
            for t in (0, 17):
                endpoint = least + t * period
                if upper is not None and endpoint > upper:
                    continue
                verify_realization(left, endpoint, True)
                verify_realization(right, endpoint, True)
                left_states = left.states(endpoint)
                right_states = right.states(endpoint)
                assert (left_states[1:] != right_states[1:]) == suffix_differs
                pair_checks += 1
            if suffix_differs:
                different_suffix_pairs += 1
                violations.append({
                    "depth": depth,
                    "left_word": left.word,
                    "right_word": right.word,
                    "least_common_endpoint": least,
                    "endpoint_period": period,
                    "upper_endpoint_bound": upper,
                    "left_states": left.states(least),
                    "right_states": right.states(least),
                })
        summaries.append({
            "depth": depth,
            "words_considered": len(ALPHABET)**depth,
            "nonempty_nondescending_word_classes": len(records),
            "nonempty_classes_with_finite_upper_bound": sum(
                record.upper is not None for record in records
            ),
            "rejections": dict(sorted(rejections.items())),
            "compatible_pairs": compatible_pairs,
            "compatible_pairs_with_distinct_suffixes": different_suffix_pairs,
        })

    # A separate finite forward scan also checks rejected words and class
    # membership. This scan is a diagnostic, not the domain of the search.
    forward_scan_limit = 100_001
    forward_prefixes_checked = 0
    for start in range(1, forward_scan_limit + 1, 2):
        word, states, _ = direct_history(start, MAX_DEPTH)
        for depth in range(1, MAX_DEPTH + 1):
            prefix = word[:depth]
            if any(block not in ALPHABET for block in prefix):
                break
            record, _ = classify(prefix)
            actual_admitted = start > 1 and min(states[:depth + 1]) >= start
            endpoint = states[depth]
            predicted_admitted = (
                record is not None
                and endpoint % record.modulus == record.residue
                and endpoint >= record.lower
                and (record.upper is None or endpoint <= record.upper)
            )
            assert predicted_admitted == actual_admitted
            if actual_admitted:
                assert record.states(endpoint) == states[:depth + 1]
            forward_prefixes_checked += 1

    return {
        "result": "PASS",
        "scope": (
            "Exact-arithmetic screening of all word classes through depth six; "
            "no endpoint cutoff, no all-depth rigidity or convergence claim."
        ),
        "alphabet": ALPHABET,
        "depths": summaries,
        "words_considered_total": sum(s["words_considered"] for s in summaries),
        "first_merge_tail_family_realizations_checked": tail_family_checks,
        "depth_three_comparison_histories": witness_pairs,
        "class_realizations_checked_by_shortcut_iteration": realization_checks,
        "excluded_class_boundary_points_checked": boundary_checks,
        "compatible_pair_realizations_checked": pair_checks,
        "admitted_first_block_type_counts": dict(sorted(first_letter_counts.items())),
        "independent_forward_scan_max_start": forward_scan_limit,
        "independent_forward_scan_odd_starts": (forward_scan_limit + 1) // 2,
        "independent_forward_prefixes_checked": forward_prefixes_checked,
        "distinct_suffix_violations": violations,
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

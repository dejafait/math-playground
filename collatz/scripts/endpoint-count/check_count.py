"""Exact finite endpoint-count checks; no infinite-itinerary conclusion."""

from fractions import Fraction
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


def extend_classes(classes):
    result = []
    for exponent, residue, suffix in classes:
        for a in (2, 3):
            modulus = 3 ** (exponent + a)
            new_residue = (
                pow(2 ** (a + 1), -1, modulus)
                * (3**a * residue + 3**a - 2**a)
            ) % modulus
            result.append((exponent + a, new_residue, suffix + (a,)))
    return result


def first_odd(exponent, residue):
    return residue if residue % 2 else residue + 3**exponent


def count_below(classes, cutoff):
    return sum(
        1 + (cutoff - first_odd(s, r)) // (2 * 3**s)
        for s, r, _ in classes
    )


def backward_histories(endpoint, depth):
    histories = [(endpoint,)]
    for _ in range(depth):
        earlier = []
        for history in histories:
            m = history[0]
            for a in (2, 3):
                numerator = 2 ** (a + 1) * m - (3**a - 2**a)
                if numerator % 3**a == 0:
                    n = numerator // 3**a
                    assert n > 0 and n % 2 == 1
                    assert direct_block(n) == (a, 1, m)
                    earlier.append((n,) + history)
        histories = earlier
        assert len(histories) <= 2
    return histories


def check():
    classes = [(2, 4, ())]
    periods = []
    representatives_checked = 0
    residue_pairs_checked = 0
    direct_starts_checked = 0
    four_classes = None
    for depth in range(1, 11):
        if depth > 1:
            classes = extend_classes(classes)
        assert len(classes) == 2 ** (depth - 1)
        density = sum((Fraction(1, 2 * 3**s) for s, _, _ in classes), Fraction())
        assert density == Fraction(1, 18) * Fraction(4, 27) ** (depth - 1)
        for i, (s, r, suffix) in enumerate(classes):
            assert 2 * depth <= s <= 3 * depth - 1
            for other_s, other_r, _ in classes[:i]:
                assert (r - other_r) % 3 ** min(s, other_s) != 0
                residue_pairs_checked += 1
            for lift in (0, 1):
                endpoint = first_odd(s, r) + lift * 2 * 3**s
                histories = backward_histories(endpoint, depth)
                assert histories
                for history in histories:
                    word = tuple(direct_block(n)[0] for n in history[:-1])
                    assert word[1:] == suffix
                    assert history[0] < endpoint
                representatives_checked += 1

        if depth > 4:
            continue
        if depth == 4:
            four_classes = classes.copy()
        common_period = 2 * 3 ** (3 * depth - 1)
        predicted = set()
        for s, r, _ in classes:
            members = set(range(first_odd(s, r), common_period + 1, 2 * 3**s))
            assert not (predicted & members)
            predicted.update(members)
        actual = set()
        for start in range(1, common_period, 2):
            direct_starts_checked += 1
            current = start
            for _ in range(depth):
                a, b, current = direct_block(current)
                if a not in (2, 3) or b != 1 or current > common_period:
                    break
            else:
                actual.add(current)
        assert actual == predicted
        assert len(actual) == 4 ** (depth - 1)

        # Compare every integer cutoff in the full period, without floats.
        count = 0
        minimum_error = maximum_error = 0
        for cutoff in range(common_period + 1):
            count += cutoff in actual
            error = count * density.denominator - cutoff * density.numerator
            assert abs(error) < len(classes) * density.denominator
            minimum_error = min(minimum_error, error)
            maximum_error = max(maximum_error, error)
        for cutoff in (0, 1, common_period, Fraction(common_period, 2)):
            assert count_below(classes, cutoff) == sum(m <= cutoff for m in actual)
        periods.append({
            "K": depth,
            "common_period": common_period,
            "class_count": len(classes),
            "endpoint_residues": len(actual),
            "minimum_endpoint": min(actual),
            "density": str(density),
            "integer_cutoff_error_minimum": str(Fraction(minimum_error, density.denominator)),
            "integer_cutoff_error_maximum": str(Fraction(maximum_error, density.denominator)),
        })

    path = [603, 679, 1147, 1291, 1453]
    for start, endpoint, a in zip(path, path[1:], (2, 3, 2, 2)):
        assert direct_block(start) == (a, 1, endpoint)
    cutoff = Fraction(27, 16) ** 4 * (175 + 5)
    bulk = Fraction(1, 18) * Fraction(4, 27) ** 3 * cutoff
    actual_count = count_below(four_classes, cutoff)
    assert cutoff == Fraction(23914845, 16384)
    assert path[-1] < cutoff and bulk == Fraction(135, 512)
    assert actual_count == 1 and actual_count - bulk == Fraction(377, 512)
    return {
        "result": "PASS",
        "scope": "Finite exact classes and counts only; no eventual-vanishing claim.",
        "maximum_class_depth": 10,
        "class_representatives_checked": representatives_checked,
        "disjoint_class_pairs_checked": residue_pairs_checked,
        "direct_forward_starts_checked": direct_starts_checked,
        "complete_periods": periods,
        "boundary_witness": {
            "N": 175,
            "K": 4,
            "path": path,
            "cutoff": str(cutoff),
            "density_contribution": str(bulk),
            "actual_endpoint_count": actual_count,
            "boundary_error": str(actual_count - bulk),
        },
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

"""Auxiliary direct support-event checks for L005, not its general proof."""

from itertools import combinations, product
from math import comb


def field_tables(q):
    """F_4 uses bit coefficients modulo X^2+X+1; other cases are prime."""
    if q == 4:
        add = [[a ^ b for b in range(q)] for a in range(q)]

        def multiply(a, b):
            result = 0
            while b:
                if b & 1:
                    result ^= a
                b >>= 1
                a <<= 1
                if a & 4:
                    a ^= 7
            return result

        mul = [[multiply(a, b) for b in range(q)] for a in range(q)]
    else:
        assert all(q % d for d in range(2, q))
        add = [[(a + b) % q for b in range(q)] for a in range(q)]
        mul = [[a * b % q for b in range(q)] for a in range(q)]
    return add, mul


def check(q, n, k, expected):
    assert n <= q
    add, mul = field_tables(q)

    def evaluate(coefficients, x):
        value = 0
        for coefficient in reversed(coefficients):
            value = add[mul[value][x]][coefficient]
        return value

    codes = {
        tuple(evaluate(coefficients, x) for x in range(n))
        for coefficients in product(range(q), repeat=k)
    }
    assert len(codes) == q**k
    supports = (tuple(range(n)),) + tuple(combinations(range(n), n - 1))
    punctures = tuple({tuple(c[i] for i in s) for c in codes} for s in supports)

    def membership_mask(word):
        return sum(
            1 << index
            for index, (s, puncture) in enumerate(zip(supports, punctures))
            if tuple(word[i] for i in s) in puncture
        )

    # Independent translations of a and b by codewords preserve the event.
    # Interpolation on the first k coordinates gives exactly these classes.
    words = tuple((0,) * k + tail for tail in product(range(q), repeat=n - k))
    masks = {word: membership_mask(word) for word in words}
    all_supports = (1 << len(supports)) - 1
    largest = largest_full = 0
    witness = None
    for b in words:
        directions = tuple(tuple(mul[gamma][bi] for bi in b) for gamma in range(q))
        for a in words:
            # Original failure event: at least one input fails on this support.
            failing_inputs = all_supports ^ (masks[a] & masks[b])
            count = count_full = 0
            for direction in directions:
                word = tuple(add[ai][di] for ai, di in zip(a, direction))
                bad_supports = masks[word] & failing_inputs
                assert not (bad_supports & masks[b])
                count += bool(bad_supports)
                count_full += bool(bad_supports & 1)
            assert count <= expected, (q, n, k, a, b, count)
            assert count_full <= 1
            if count > largest:
                largest, witness = count, (a, b)
            largest_full = max(largest_full, count_full)
    assert largest == expected and largest_full == 1

    if k <= n - 3:
        # Check the proof's explicit pair directly, without normalization.
        negative_one = next(x for x in range(q) if add[x][1] == 0)
        a = (1,) + (0,) * (n - 1)
        b = (negative_one, 1) + (0,) * (n - 2)
        failing_inputs = all_supports ^ (membership_mask(a) & membership_mask(b))
        event = {
            gamma
            for gamma in range(q)
            if membership_mask(
                tuple(add[ai][mul[gamma][bi]] for ai, bi in zip(a, b))
            )
            & failing_inputs
        }
        assert event == {0, 1}, (q, n, k, event)
    else:
        assert largest > 2
        print(f"Boundary witness outside k<=n-3: a,b={witness}.")

    print(
        f"PASS F_{q}, n={n}, k={k}: {len(words)**2} pair classes; "
        f"max counts at cutoffs n,n-1: {largest_full},{largest}."
    )
    return len(words) ** 2


if __name__ == "__main__":
    cases = (
        (4, 4, 1, 2),
        (5, 5, 1, 2),
        (5, 5, 2, 2),
        (7, 6, 3, 2),
        (5, 4, 2, 4),  # The excluded codimension-two case.
    )
    total = sum(check(*case) for case in cases)
    comparison = [comb(16, k + 1) // comb(14, k) for k in (8, 4, 2, 1)]
    assert comparison == [3, 4, 6, 8]
    assert 2 * 2**128 == 2**129
    print(f"PASS length-16 comparison: old counts {comparison}; exact count 2.")
    print(f"TOTAL: {total} pair classes checked by direct polynomial membership.")

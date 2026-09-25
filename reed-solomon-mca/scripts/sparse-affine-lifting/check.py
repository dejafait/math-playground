"""Auxiliary direct support-event checks for L006, not its general proof."""

from functools import lru_cache
from itertools import combinations, product
from math import comb
from random import Random


def field_tables(q):
    if q == 8:
        # Bit coefficients modulo X^3+X+1, irreducible over F_2.
        add = [[a ^ b for b in range(q)] for a in range(q)]

        def multiply(a, b):
            result = 0
            while b:
                if b & 1:
                    result ^= a
                b >>= 1
                a <<= 1
                if a & 8:
                    a ^= 11
            return result

        mul = [[multiply(a, b) for b in range(q)] for a in range(q)]
    else:
        assert q >= 2 and all(q % d for d in range(2, q))
        add = [[(a + b) % q for b in range(q)] for a in range(q)]
        mul = [[a * b % q for b in range(q)] for a in range(q)]
    neg = [next(b for b in range(q) if add[a][b] == 0) for a in range(q)]
    assert all(any(mul[a][b] == 1 for b in range(q)) for a in range(1, q))
    return add, mul, neg


def check(q, n, k, r, exhaustive_constant_shapes=False):
    assert n <= q and 1 <= k and 1 <= r and 3 * r <= n - k
    add, mul, neg = field_tables(q)

    def evaluate(coefficients, x):
        value = 0
        for coefficient in reversed(coefficients):
            value = add[mul[value][x]][coefficient]
        return value

    codes = tuple(
        tuple(evaluate(coefficients, x) for x in range(n))
        for coefficients in product(range(q), repeat=k)
    )
    assert len(set(codes)) == q**k
    supports = tuple(
        tuple(i for i in range(n) if i not in omitted)
        for size in range(r + 1)
        for omitted in combinations(range(n), size)
    )
    punctures = tuple({tuple(c[i] for i in s) for c in codes} for s in supports)
    all_supports = (1 << len(supports)) - 1

    @lru_cache(maxsize=30000)
    def membership_mask(word):
        return sum(
            1 << index
            for index, (s, puncture) in enumerate(zip(supports, punctures))
            if tuple(word[i] for i in s) in puncture
        )

    def combine(a, b, gamma):
        return tuple(add[ai][mul[gamma][bi]] for ai, bi in zip(a, b))

    def subtract(a, b):
        return tuple(add[ai][neg[bi]] for ai, bi in zip(a, b))

    def event(a, b):
        # Original disjunction on the same support; no sparse-lift criterion.
        failing_inputs = all_supports ^ (membership_mask(a) & membership_mask(b))
        return {
            gamma
            for gamma in range(q)
            if membership_mask(combine(a, b, gamma)) & failing_inputs
        }

    cases = largest = 0

    def verify(a, b, expected=None):
        nonlocal cases, largest
        bad = event(a, b)
        assert len(bad) <= r + 1, (q, n, k, r, a, b, bad)
        if expected is not None:
            assert bad == expected, (q, n, k, r, a, b, bad, expected)
        cases += 1
        largest = max(largest, len(bad))

    zero = (0,) * n
    a = tuple(neg[i] if i <= r else 0 for i in range(n))
    b = (1,) * (r + 1) + (0,) * (n - r - 1)
    verify(a, b, set(range(r + 1)))
    verify(a, zero, set())
    verify(a, codes[-1], set())
    # A line through a codeword has only its zero quotient parameter bad.
    verify(zero, b, {0})
    verify(combine(zero, b, neg[2]), b, {2})
    # Every parameter is close, but only the r coordinate roots are bad.
    small_a = tuple(neg[i] if i < r else 0 for i in range(n))
    small_b = (1,) * r + (0,) * (n - r)
    verify(small_a, small_b, set(range(r)))
    # A constant active coordinate has no root and uses part of the budget.
    constant_a = (1,) + small_a[1:]
    constant_b = (0,) + small_b[1:]
    verify(constant_a, constant_b, set(range(1, r)))

    rng = Random(20260925 + 1000 * q + 100 * n + 10 * k + r)
    for _ in range(80):
        random_a = tuple(rng.randrange(q) for _ in range(n))
        random_b = tuple(rng.randrange(q) for _ in range(n))
        verify(random_a, random_b)
        # Two independently positioned sparse endpoints give more near-code
        # intersections than uniformly random words typically do.
        endpoints = []
        for _endpoint in range(2):
            word = [0] * n
            for i in rng.sample(range(n), rng.randrange(r + 1)):
                word[i] = rng.randrange(1, q)
            endpoints.append(tuple(word))
        first, second = endpoints
        verify(first, subtract(second, first))
        ca, cb = rng.choice(codes), rng.choice(codes)
        translated_a = combine(a, ca, 1)
        translated_b = combine(b, cb, 1)
        verify(translated_a, translated_b, set(range(r + 1)))

    shape_count = 0
    if exhaustive_constant_shapes:
        assert k == 1 and r == 2
        # Constant codes are invariant under all coordinate permutations.
        # These canonical support pairs cover all two-error endpoint pairs
        # up to that symmetry, including every assignment of nonzero values.
        for s0 in range(r + 1):
            for s1 in range(r + 1):
                for overlap in range(min(s0, s1) + 1):
                    support0 = tuple(range(s0))
                    support1 = tuple(range(overlap)) + tuple(
                        range(s0, s0 + s1 - overlap)
                    )
                    for values in product(range(1, q), repeat=s0 + s1):
                        first, second = [0] * n, [0] * n
                        for i, value in zip(support0, values[:s0]):
                            first[i] = value
                        for i, value in zip(support1, values[s0:]):
                            second[i] = value
                        first, second = tuple(first), tuple(second)
                        verify(first, subtract(second, first))
                        shape_count += 1

    assert largest == r + 1
    print(
        f"PASS F_{q}, n={n}, k={k}, r={r}: {cases} tested pairs, "
        f"{shape_count} exhaustive sparse endpoint shapes; max {largest}."
    )
    return cases


def check_excluded_example():
    # A constant code agrees on S exactly when the entries on S are equal.
    q, n, r = 7, 5, 2
    a, b = (0, 0, 1, 1, 1), (0, 0, 1, 2, 3)
    supports = tuple(
        s for size in range(n - r, n + 1) for s in combinations(range(n), size)
    )
    bad = {
        gamma
        for gamma in range(q)
        if any(
            len({(a[i] + gamma * b[i]) % q for i in s}) == 1
            and (len({a[i] for i in s}) > 1 or len({b[i] for i in s}) > 1)
            for s in supports
        )
    }
    assert bad == {0, 2, 3, 6}
    print(f"PASS excluded n=5,k=1,r=2 example: bad parameters {sorted(bad)}.")


if __name__ == "__main__":
    total = sum(
        check(*case)
        for case in (
            (7, 7, 1, 2, True),
            (8, 8, 2, 2, False),
            (11, 10, 1, 3, False),
            (11, 11, 2, 3, False),
        )
    )
    check_excluded_example()
    old_counts = [comb(16, k + 1) // comb(13, k) for k in (8, 4, 2, 1)]
    assert old_counts == [8, 6, 7, 9]
    assert (256 - 128) // 3 == 42
    assert 43 * 2**128 <= 257**32
    print(f"PASS length-16 comparison: old counts {old_counts}; exact count 3.")
    print(f"TOTAL: {total} pairs checked by direct polynomial membership.")

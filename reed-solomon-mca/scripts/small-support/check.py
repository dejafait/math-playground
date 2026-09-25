"""Exact auxiliary checks for L003; finite checks are not its general proof."""

from itertools import combinations, product
from math import comb


def codewords(q, xs, k):
    return {
        tuple(sum(c * pow(x, j, q) for j, c in enumerate(cs)) % q for x in xs)
        for cs in product(range(q), repeat=k)
    }


def project(word, support):
    return tuple(word[i] for i in support)


def coefficient_form(q, xs, support):
    coefficients = [0] * len(xs)
    for i in support:
        denominator = 1
        for j in support:
            if i != j:
                denominator = denominator * (xs[i] - xs[j]) % q
        coefficients[i] = pow(denominator, -1, q)
    return tuple(coefficients)


def dot(q, form, word):
    return sum(c * z for c, z in zip(form, word)) % q


def check_all_pairs_modulo_code(q, n, k):
    xs = tuple(range(n))
    supports = tuple(s for size in range(n + 1) for s in combinations(range(n), size))
    small = tuple(s for s in supports if len(s) == k + 1)
    forms = {s: coefficient_form(q, xs, s) for s in small}
    codes = codewords(q, xs, k)
    punctures = {s: {project(c, s) for c in codes} for s in supports}

    # Adding a codeword to either input preserves every membership/failure
    # condition. Subtracting its interpolant on the first k coordinates
    # gives the unique representative used here. This covers all input pairs
    # modulo these independent translations, including every degenerate case.
    words = tuple((0,) * k + tail for tail in product(range(q), repeat=n - k))
    memberships = {
        word: {s for s in supports if project(word, s) in punctures[s]}
        for word in words
    }
    values = {word: {s: dot(q, forms[s], word) for s in small} for word in words}
    contained = {s: tuple(t for t in small if set(t) <= set(s)) for s in supports}
    for word in words:
        for s in small:
            assert (values[word][s] == 0) == (s in memberships[word])

    max_counts = [0] * (n + 1)
    for a, b in product(words, repeat=2):
        roots = {
            -values[a][s] * pow(values[b][s], -1, q) % q
            for s in small if values[b][s] != 0
        }
        failing_inputs = set(supports) - (memberships[a] & memberships[b])
        events = [set() for _ in range(n + 1)]
        for gamma in range(q):
            word = tuple((ai + gamma * bi) % q for ai, bi in zip(a, b))
            bad_supports = memberships[word] & failing_inputs
            for s in bad_supports:
                assert s not in memberships[b]
                assert any(t in bad_supports for t in contained[s])
            if bad_supports:
                assert gamma in roots
                largest_support = max(map(len, bad_supports))
                for minimum_size in range(largest_support + 1):
                    events[minimum_size].add(gamma)
        for minimum_size, event in enumerate(events):
            assert event <= roots
            assert len(event) <= min(q, comb(n, k + 1))
            if minimum_size <= k + 1:
                assert event == roots
            max_counts[minimum_size] = max(max_counts[minimum_size], len(event))

    print(
        f"PASS: F_{q}, n={n}, k={k}: {len(words)**2} input-pair classes; "
        f"max bad counts at grid radii 0,1/{n},...,1: {max_counts[::-1]}"
    )


def check_distinct_root_witness():
    q, n, k = 101, 5, 2
    xs = tuple(range(n))
    a = (42, 16, 98, 65, 15)
    b = tuple(x**k % q for x in xs)
    supports = tuple(combinations(range(n), k + 1))
    codes = codewords(q, xs, k)
    roots = []
    for s in supports:
        form = coefficient_form(q, xs, s)
        assert dot(q, form, b) == 1
        gamma = -dot(q, form, a) % q
        roots.append(gamma)
        word = tuple((ai + gamma * bi) % q for ai, bi in zip(a, b))
        puncture = {project(c, s) for c in codes}
        assert project(word, s) in puncture
        assert project(b, s) not in puncture
    assert roots == [47, 0, 2, 54, 30, 6, 7, 58, 8, 59]
    assert len(set(roots)) == comb(n, k + 1) == 10
    assert q > comb(len(roots), 2)
    print("PASS: F_101, n=5, k=2: ten distinct certified challenges for one pair.")


def check_thresholds():
    counts = [comb(16, k + 1) for k in (8, 4, 2, 1)]
    assert counts == [11440, 4368, 560, 120]
    assert 5**7 > 2**16
    assert 5**64 > max(counts) * 2**128
    assert (5**64 - 1) % 16 == 0
    assert 5**64 > comb(max(counts), 2)
    assert 2**379 < comb(256, 129) * 2**128 < 2**380
    print("PASS: all four length-16 rates safe over F_(5^64) at error 2^-128.")
    print("PASS: n=256, k=128 sufficient field threshold lies between 2^379 and 2^380.")


if __name__ == "__main__":
    for parameters in ((2, 2, 1), (3, 3, 1), (3, 3, 2), (5, 4, 1), (5, 4, 2), (5, 4, 3)):
        check_all_pairs_modulo_code(*parameters)
    check_distinct_root_witness()
    check_thresholds()

"""Exact auxiliary checks for L004; enumeration is not its general proof."""

from itertools import combinations, product
from math import comb


def codewords(q, n, k):
    return {
        tuple(sum(c * pow(x, j, q) for j, c in enumerate(cs)) % q for x in range(n))
        for cs in product(range(q), repeat=k)
    }


def model(q, n, k):
    supports = tuple(s for size in range(n + 1) for s in combinations(range(n), size))
    codes = codewords(q, n, k)
    punctures = {s: {tuple(c[i] for i in s) for c in codes} for s in supports}
    # Independent codeword translations preserve all punctured-code membership
    # tests. Interpolation on the first k points gives these unique representatives.
    words = tuple((0,) * k + tail for tail in product(range(q), repeat=n - k))
    memberships = {
        w: {s for s in supports if tuple(w[i] for i in s) in punctures[s]}
        for w in words
    }
    small = {s for s in supports if len(s) == k + 1}
    contained = {s: {t for t in small if set(t) <= set(s)} for s in supports}
    return supports, words, memberships, small, contained


def check_multiplicity(q, n, k, data):
    supports, words, memberships, small, contained = data
    cases = 0
    equality_cases = 0
    for b in words:
        failing_small = small - memberships[b]
        for s in set(supports) - memberships[b]:
            m = len(s)
            assert m >= k + 1
            count = len(failing_small & contained[s])
            threshold = comb(m - 1, k)
            assert count >= threshold, (q, n, k, b, s, count, threshold)
            cases += 1
            equality_cases += count == threshold

    # One changed coordinate attains the multiplicity for every support size.
    b = (0,) * (n - 1) + (1,)
    for m in range(k + 1, n + 1):
        s = tuple(range(m - 1)) + (n - 1,)
        assert s not in memberships[b]
        count = len((small - memberships[b]) & contained[s])
        assert count == comb(m - 1, k)
    print(
        f"PASS multiplicity: F_{q}, n={n}, k={k}: {len(words)} word classes, "
        f"{cases} noncode supports, {equality_cases} equality cases."
    )
    return cases


def check_challenges(q, n, k, data):
    supports, words, memberships, small, contained = data
    maxima = [0] * (n + 1)
    for a, b in product(words, repeat=2):
        failing_inputs = set(supports) - (memberships[a] & memberships[b])
        assigned = set()
        events = [set() for _ in range(n + 1)]
        for gamma in range(q):
            w = tuple((ai + gamma * bi) % q for ai, bi in zip(a, b))
            # Direct enumeration of degree-<k polynomials supplies memberships;
            # the divided-difference formula is not used in this check.
            certificates = (small & memberships[w]) - memberships[b]
            assert not (certificates & assigned)
            assigned.update(certificates)
            bad_supports = memberships[w] & failing_inputs
            if not bad_supports:
                continue
            for s in bad_supports:
                assert s not in memberships[b]
                assert len(certificates & contained[s]) >= comb(len(s) - 1, k)
            largest = max(map(len, bad_supports))
            for cutoff in range(largest + 1):
                events[cutoff].add(gamma)
        for cutoff, event in enumerate(events):
            m = max(k + 1, cutoff)
            bound = min(q, comb(n, k + 1) // comb(m - 1, k))
            assert len(event) <= bound, (q, n, k, a, b, cutoff, len(event), bound)
            maxima[cutoff] = max(maxima[cutoff], len(event))
    print(
        f"PASS challenges: F_{q}, n={n}, k={k}: {len(words)**2} pair classes; "
        f"max counts at support cutoffs 0,...,{n}: {maxima}."
    )
    return len(words) ** 2


def check_threshold():
    n, k = 256, 128
    q = 257**32
    total = comb(n, k + 1)
    assert all(257 % d != 0 for d in range(2, 17))
    assert (q - 1) % n == 0
    assert 2**256 < q < 2**257
    bounds = {m: total // comb(m - 1, k) for m in range(k + 1, n + 1)}
    assert bounds[167] * 2**128 <= q < bounds[166] * 2**128
    assert bounds[167] < 2**127
    assert min(m for m, bound in bounds.items() if bound * 2**128 <= q) == 167
    assert total * 2**128 > 2**379 > q
    print(
        "PASS threshold: smooth length 256 over F_(257^32), k=128; "
        "all real radii delta < 90/256 meet error 2^-128 by L004."
    )
    print(
        f"At m=167, integer challenge bound K={bounds[167]}; "
        "the sufficient test fails at m=166, which is not an unsafe-radius claim."
    )


if __name__ == "__main__":
    noncode_supports = 0
    pair_classes = 0
    parameters = (
        (2, 2, 1, True),
        (3, 3, 1, True),
        (3, 3, 2, True),
        (5, 4, 1, True),
        (5, 5, 1, False),
        (5, 5, 2, True),
        (5, 5, 3, True),
        (5, 5, 4, True),
        (7, 6, 2, False),
    )
    for q, n, k, check_pairs in parameters:
        data = model(q, n, k)
        noncode_supports += check_multiplicity(q, n, k, data)
        if check_pairs:
            pair_classes += check_challenges(q, n, k, data)
    check_threshold()
    print(f"TOTAL: {noncode_supports} noncode supports, {pair_classes} input-pair classes.")

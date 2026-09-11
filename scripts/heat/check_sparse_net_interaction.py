"""Exact finite checks supplementing the analytic proof of Lemma 69."""
from fractions import Fraction as Q


def heights(n):
    return 1 - Q(1, 2**n), 1 - Q(1, 2**(n + 1))


def term(x, b, u, v):
    return 2 * (v - b) / ((x - u)**2 + (b - v)**2)


checks = 0
for n in range(1, 21):
    x = 2**n
    b, c = heights(n)
    assert term(x, b, x, c) == 2**(n + 2)
    assert term(x, b, x, -b) == -1 / b
    assert term(x, b, x, -c) == -2 / (b + c)
    checks += 3
    reflected = sum(abs(term(x, b, -x, v)) for v in (b, c, -b, -c))
    assert reflected <= Q(4, 4**n)
    total = reflected
    checks += 1
    for m in range(1, 41):
        if m == n:
            continue
        bm, cm = heights(m)
        cluster = sum(abs(term(x, b, u, v))
                      for u in (2**m, -2**m)
                      for v in (bm, cm, -bm, -cm))
        assert cluster <= Q(32, (x - 2**m)**2)
        total += cluster
        checks += 1
    bound = (4 + 128*(n - 1) + Q(128, 3)) / 4**n
    assert total <= bound
    assert sum(Q(1, (x - 2**m)**2) for m in range(1, n)) <= Q(4*(n-1), 4**n)
    assert sum(Q(1, (x - 2**m)**2) for m in range(n+1, 41)) <= Q(4, 3*4**n)
    checks += 3
print(f'Passed {checks} exact local-contribution and cluster-bound checks.')

"""Exact finite checks of L229's reindexing, not asymptotic evidence."""
from collections import Counter
from fractions import Fraction
from math import isqrt

checks = atoms = 0
for N in (4, 6, 8):
    R = N
    for a in range(N, 2 * N + 1):
        divisors = [e for e in range(1, a + 1) if a % e == 0]
        direct = Counter()
        products = Counter()
        for b in range(N, 2 * N + 1):
            for c in range(N, 2 * N + 1):
                for d in range(N, 2 * N + 1):
                    lower = a * b * c * d - R
                    upper = a * b * (c * d + 1) + R - 1
                    products[b * c * d] += 1
                    for e in divisors:
                        lo = isqrt(lower) // e
                        hi = isqrt(upper) // e
                        atom = (e * hi) ** 2 == upper
                        atoms += atom
                        exact = hi - lo - atom
                        selected = [m for m in range(isqrt(lower) + 1,
                                                      isqrt(upper) + 1)
                                    if m * m < upper and m % e == 0]
                        assert exact == len(selected)
                        for m in selected:
                            assert Fraction(m*m-R+1, a)-2*N < b*c*d
                            assert b*c*d < Fraction(m*m+R, a)
                            direct[e, m] += 1
                        checks += 1
        for (e, m), count in direct.items():
            enlarged = sum(multiplicity for t, multiplicity in products.items()
                           if Fraction(m*m-R+1, a)-2*N < t
                           < Fraction(m*m+R, a))
            assert count <= enlarged
        for cutoff in (1, N // 2, N, 2 * N):
            tail = sum(count for (e, m), count in direct.items() if e > cutoff)
            reversed_tail = sum(sum(count for (ee, m), count in direct.items()
                                    if ee == e) for e in divisors if e > cutoff)
            assert tail == reversed_tail
print(f'Passed {checks} strict-cell counts and product bounds; {atoms} endpoint atoms.')

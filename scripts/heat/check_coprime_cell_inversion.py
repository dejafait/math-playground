"""Exact finite checks for L228; no asymptotic distribution claim."""
from math import gcd, isqrt


def mu(n):
    result = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            result = -result
            if n % p == 0:
                return 0
        p += 1
    return -result if n > 1 else result


checks = atoms = 0
for a in range(1, 41):
    for lower in range(1, 81):
        for width in (1, 2, 7, 19):
            upper = lower + width
            direct = sum(gcd(a, m) == 1 for m in range(1, isqrt(upper) + 1)
                         if lower < m * m < upper)
            inverted = 0
            for e in range(1, a + 1):
                if a % e:
                    continue
                lo = isqrt(lower) // e
                hi = isqrt(upper) // e
                atom = (e * hi) ** 2 == upper
                count = hi - lo - atom
                brute = sum(m % e == 0 for m in range(1, isqrt(upper) + 1)
                            if lower < m * m < upper)
                assert count == brute
                inverted += mu(e) * count
                atoms += atom
            assert inverted == direct
            checks += 1
print(f'Passed {checks} coprime open-cell inversions; {atoms} upper endpoint atoms.')

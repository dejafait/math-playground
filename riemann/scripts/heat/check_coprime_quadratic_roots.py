"""Exact finite checks for L188; no asymptotic inference."""
from fractions import Fraction as F
from math import gcd


def omega(n):
    count = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            count += 1
            while n % p == 0:
                n //= p
        p += 1
    return count + (n > 1)


root_cases = 0
for u in range(1, 161):
    for r in range(u):
        if gcd(r, u) != 1:
            continue
        roots = [m for m in range(u) if gcd(m, u) == 1 and (m*m+r) % u == 0]
        assert len(roots) <= 2 ** (omega(u) + 1)
        root_cases += 1

interval_cases = 0
for n in range(2, 7):
    rho = F(1, 2)
    for amin, amax in [(F(n*n), F(n*n+2)),
                       (F(2*n*n), F(2*n*n+1, 1)),
                       (F(n*n)+F(1, 2), F(n*n)+F(3, 2))]:
        for u in range(n*n, 4*n*n+1):
            for r in range(-4*n*n, 4*n*n+1):
                if r == 0:
                    continue
                original = []
                regrouped = []
                for m in range(1, 4*n*n+3):
                    k = m*m+r
                    common = ((k % u == 0) and gcd(m, u) == 1)
                    if (common and amin-rho <= m <= amax+rho
                        and amin**2 <= k <= amax**2
                        and -2*m*rho+rho*rho <= r <= 2*m*rho+rho*rho
                        and n*n <= k//u <= 4*n*n):
                        original.append(m)
                    # Square the positive-root interval inequalities exactly.
                    if (common and gcd(r, u) == 1
                        and amin-rho <= m <= amax+rho
                        and amin**2-r <= m*m <= amax**2-r
                        and u*n*n-r <= m*m <= 4*u*n*n-r
                        and m >= abs(r-rho*rho)/(2*rho)):
                        regrouped.append(m)
                assert original == regrouped, (n, u, r)
                interval_cases += 1
print(f'Passed {root_cases} unit-root and {interval_cases} exact interval checks.')

"""Exact finite checks for L192; asymptotic estimates are analytic."""
from fractions import Fraction as F
from math import gcd


def squarefree(n):
    return all(n % (p*p) for p in range(2, n+1))


cases = 0
for u in range(2, 61):
    density = F(sum(gcd(r, u) == 1 for r in range(u)), u)
    D = sum(squarefree(d) for d in range(1, u+1) if u % d == 0)
    for b in range(-12, 13):
        for t in range(b-1, 14):
            for alpha, beta in [(F(2, 3), F(-3, 7)), (F(-1), F(0)),
                                (F(0), F(2, 5))]:
                if b > t:
                    continue
                roots = [r for r in range(b, t+1) if gcd(r, u) == 1]
                exact = sum((alpha+beta*r for r in roots), F(0))
                integral = density*(alpha*(t-b)+beta*F(t*t-b*b, 2))
                partial = (alpha+beta*t)*len(roots)-beta*sum(t-r for r in roots)
                assert exact == partial
                bound = 2*D*(abs(alpha+beta*t)+abs(beta)*(t-b))
                assert abs(exact-integral) <= bound, (u, b, t)
                cases += 1
cells = 0
for u in range(2, 90):
    R = (u-1)//2
    for m in range(1, 70):
        occupied = {(m*m+r)//u for r in range(-R, R+1)}
        assert len(occupied) <= 2
        cells += 1
print(f'Passed {cases} rational affine checks and {cells} short-window cell checks.')

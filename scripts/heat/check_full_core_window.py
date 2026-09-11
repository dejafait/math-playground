"""Finite exact endpoint/divisor checks; no asymptotic inference."""
from fractions import Fraction as F
from math import ceil, floor, gcd, isqrt
from decimal import Decimal, localcontext


def sqrt_floor(x):
    return isqrt(x.numerator // x.denominator)


def sqrt_ceil(x):
    k = sqrt_floor(x)
    return k if k*k == x else k+1


def mu(n):
    sign = 1
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        while n % p == 0:
            n //= p
        p += 1
    return -sign if n > 1 else sign


cases = empty = singleton = 0
with localcontext() as ctx:
    ctx.prec = 60
    dec = lambda x: Decimal(x.numerator)/Decimal(x.denominator)
    for N in (2, 3, 4):
        # Rational rho tests the general endpoint algebra, not its scale limit.
        rho = F(1, 2)
        for u in range(N*N, 4*N*N+1):
            for v in range(N*N, 4*N*N+1):
                for W in (1, 2):
                    am, ap, R = F(N*N, 1)+F(1, 2), F(3*N*N), F(3)
                    low = [am*am+W, F(u*N*N+W), F(u*v+W)]
                    high = [ap*ap-W, F(4*u*N*N-W), F(u*(v+1)-1-W)]
                    linear = (W+rho*rho)/(2*rho)
                    lo = max([sqrt_ceil(x) for x in low]+[ceil(linear)])
                    hi = min(sqrt_floor(x) for x in high)
                    predicted = list(range(lo, hi+1))
                    actual = []
                    for m in range(1, ceil(ap)+2):
                        b = max(ceil(-R), ceil(am*am-m*m),
                                ceil(-2*m*rho+rho*rho), u*N*N-m*m, u*v-m*m)
                        t = min(floor(R), floor(ap*ap-m*m),
                                floor(2*m*rho+rho*rho), 4*u*N*N-m*m,
                                u*(v+1)-m*m-1)
                        if b <= -W and t >= W:
                            actual.append(m)
                    assert actual == predicted, (N,u,v,W,actual,predicted)
                    A = max([dec(x).sqrt() for x in low]+[dec(linear)])
                    B = min(dec(x).sqrt() for x in high)
                    count = sum(gcd(m,u) == 1 for m in actual)
                    if A <= B:
                        divisors = [d for d in range(1,u+1) if u % d == 0]
                        exact = sum(mu(d)*(hi//d - (lo+d-1)//d + 1)
                                    for d in divisors)
                        assert exact == count
                        phi = sum(gcd(m,u) == 1 for m in range(1,u+1))
                        budget = sum(abs(mu(d)) for d in divisors)
                        assert abs(Decimal(count)-Decimal(phi)/u*(B-A)) <= budget+Decimal('1e-50')
                    empty += not actual
                    singleton += len(actual) == 1
                    cases += 1
assert empty and singleton
print(f'Passed {cases} cases ({empty} empty, {singleton} singleton integer windows).')

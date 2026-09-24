"""Exact rational checks for L193; no numerical asymptotic inference."""
from fractions import Fraction as F
from math import ceil, floor, isqrt

cases = regular = boundary = endpoint = empty = singleton = 0
for N in (9, 16, 25):
    rho = F(1, isqrt(N))
    h = N * isqrt(N)
    for shift in (F(0), F(1, 3)):
        amin = 2*N*N + shift
        amax = amin + F(h, 3)
        R = F(h)
        for m in range(ceil(amin-rho), floor(amax+rho)+1):
            exceptional = min(abs(m*m-amin*amin), abs(m*m-amax*amax)) <= R+2
            for u in range(N*N, 4*N*N+1, N):
                # Distance to the closest integer multiple of u.
                rem = m*m % u
                is_boundary = min(rem, u-rem) <= R+2
                nonempty = 0
                for v in range(floor((m*m-R)/u), floor((m*m+R)/u)+1):
                    if not N*N <= v <= 4*N*N:
                        continue
                    b = max(ceil(-R), ceil(amin*amin-m*m),
                            ceil(-2*m*rho+rho*rho), ceil(u*N*N-m*m),
                            u*v-m*m)
                    t = min(floor(R), floor(amax*amax-m*m),
                            floor(2*m*rho+rho*rho), floor(4*u*N*N-m*m),
                            u*(v+1)-m*m-1)
                    cases += 1
                    if b > t:
                        empty += 1
                        continue
                    nonempty += 1
                    singleton += b == t
                    J = F(t*t-b*b, 2)
                    assert abs(J) <= R*(t-b)
                    assert J == F(t-b, 2)*(t+b)
                    if exceptional:
                        endpoint += 1
                    elif is_boundary:
                        boundary += 1
                    else:
                        regular += 1
                        assert b == ceil(max(-R, -2*m*rho+rho*rho))
                        assert t == floor(min(R, 2*m*rho+rho*rho))
                        assert abs(b+t) <= 2+2*rho*rho
                        assert abs(J) <= (t-b)*(1+rho*rho)
                assert nonempty <= 2
assert regular and boundary and endpoint and empty
# Isolate singleton and asymmetric rounding, including a clipped radius.
rounding = 0
for R in (F(0), F(1, 3), F(3, 2), F(5), F(11, 3)):
    for L in (F(0), F(1, 4), F(2), F(7)):
        for delta in (F(0), F(1, 25), F(1, 9)):
            lo, hi = max(-R, -L+delta), min(R, L+delta)
            if lo > hi:
                continue
            b, t = ceil(lo), floor(hi)
            if b <= t:
                assert abs(b+t) <= 2+2*delta
                singleton += b == t
                rounding += 1
assert singleton
print(f'Passed {cases} interval checks: {regular} regular, {boundary} boundary, '
      f'{endpoint} endpoint, {empty} empty; {rounding} rounding checks '
      f'({singleton} singleton cases).')

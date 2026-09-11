"""Exact endpoint checks for L226; no asymptotic distribution claim."""
from math import gcd, isqrt
checks = deficient = zero = 0
for a in range(2, 10):
    for v in range(50, 70):
        for b in range(10, 25):
            for R in range(1, 5):
                lower, upper = a*v*b-R, a*(v+1)*b+R-1
                m = isqrt(lower)+1
                if m*m >= upper or gcd(a,m) != 1:
                    continue
                for A in range(-R, R):
                    for B in range(A+1, R+1):
                        L, U = a*v*b-m*m, a*(v+1)*b-m*m-1
                        overlap = max(0, min(B,U)-max(A,L))
                        loss = B-A-overlap
                        assert 0 <= loss <= 2*R
                        if loss:
                            assert L>A or U<B
                            assert abs(a*v*b-m*m)<=R+1 or abs(a*(v+1)*b-m*m)<=R+1
                            deficient += 1
                            zero += overlap == 0
                        checks += 1
assert deficient and zero
print(f'Passed {checks} exact overlaps; {deficient} deficient, {zero} zero-overlap transitions.')

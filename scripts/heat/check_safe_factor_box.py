"""Finite exact checks for L202; no asymptotic population inference."""
from fractions import Fraction as F
from math import isqrt
from random import Random

rng = Random(202)
checks = selected = 0
for j in (8, 16, 32, 64):
    n = j*j
    scale = j**3
    v0 = 2*n*n
    t = F(1, 16)
    lo, hi = v0-2*t*scale, v0-t*scale
    pairs = []
    for a in range((11*n+9)//10, 6*n//5+1):
        left, right = lo/a, hi/a
        for b in range(-(-left.numerator//left.denominator), right.numerator//right.denominator+1):
            assert n <= a <= 2*n and n <= b <= 2*n
            assert F(b, n) >= F(8, 5)
            pairs.append((a, b))
    # The analytic lower bound is conservative; these cases meet it.
    assert len(pairs) >= t*scale/48
    amin, amax = F(v0-scale)-F(1, 4), F(v0)-F(1, 4)
    rho = F(1, j)
    for _ in range(2000):
        a, b = rng.choice(pairs)
        c, d = rng.choice(pairs)
        u, v = a*b, c*d
        m = isqrt(u*v)+1
        w = scale
        assert abs(v-v0) <= scale and abs(u-v) <= t*scale
        assert amin**2+w <= m*m <= amax**2-w
        assert u*n*n+w <= m*m <= 4*u*n*n-w
        assert 2*m*rho-rho*rho >= w
        s, k = u+v, u-v
        q = F(s, 2)-F(k*k, 4*s)-F(k**4, 16*s**3)
        phase = q-q.numerator//q.denominator
        if F(5, 8) <= phase <= F(7, 8):
            assert u*v+w <= m*m <= u*(v+1)-1-w
            selected += 1
        checks += 1
    print(f'N={n}: {len(pairs)} ordered pairs; exact cutoff checks passed')
print(f'{checks} candidate checks; {selected} phase-selected floor-cell checks passed')

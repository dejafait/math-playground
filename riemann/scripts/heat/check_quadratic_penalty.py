"""Supplement Lemma 71 with exact rational checks; no asymptotic certificate."""
from fractions import Fraction as F

checks = 0
for j in range(2, 10):
    eps = F(1, 2**j)
    for k in range(1, 20):
        d = F(1, 2**k)
        b = F(1, 2)
        delta = eps*d*(2+d)/2
        c = b+delta
        assert c < 1
        assert c-eps*(1+d)**2 == b-eps-delta < b-eps
        exact = 2*delta/(d*d+delta*delta)
        assert exact == eps*(2+d)/(d*(1+eps**2*(2+d)**2/4))
        assert exact <= 2*eps*(2+d)/d
        assert exact >= eps/d  # explicit divergence lower bound on this range
        checks += 5
for a in [F(-3), F(0), F(2)]:
    for u in [F(-5), F(5)]:
        for eps in [F(1, 100), F(1, 8)]:
            delta = eps*(u*u-a*a)/3
            assert 2*delta/((u-a)**2+delta**2) <= 2*eps*abs(u+a)/abs(u-a)
            checks += 1
print(f'OK: {checks} exact quadratic-penalty checks')

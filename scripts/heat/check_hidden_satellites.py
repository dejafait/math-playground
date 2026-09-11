"""Supplementary exact checks for Lemma 75; not an infinite certificate."""
from fractions import Fraction as Q

checks = 0
for n in range(1, 101):
    x = Q(2**n)
    b = 1 - Q(1, 2**n)
    d = Q(1, 16**n)
    delta = d*d
    a = x*x
    gap = 2*x*d + d*d
    next_b = 1 - Q(1, 2**(n+1))
    slope = (next_b-b)/(3*a)
    lam = gap/(3*a)
    assert x < x+d < 2*x
    assert 0 < b < b+delta < next_b < 1
    assert slope == Q(1, 6*8**n)
    assert 0 < lam < 1
    assert delta/gap < d/(2*x) < slope
    assert 2*delta/(d*d+delta*delta) == 2/(1+d*d) > 1
    checks += 6
    for eps in (slope/2, slope, slope*2, Q(1), Q(1, 10**100)):
        left = b-eps*a
        right = next_b-eps*4*a
        satellite = b+delta-eps*(a+gap)
        chord = (1-lam)*left+lam*right
        assert satellite < chord <= max(left, right)
        assert chord-satellite == slope*gap-delta
        checks += 2
print(f"Passed {checks} exact rational checks for Lemma 75.")

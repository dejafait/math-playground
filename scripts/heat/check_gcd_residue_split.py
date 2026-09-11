"""Exact rational regression checks for L187, not asymptotic evidence."""
from fractions import Fraction as F
from math import gcd, ceil, floor

cases = 0
for m in range(1, 51):
    for u in range(1, 61):
        g = gcd(m, u)
        t, s = m // g, u // g
        for lo, hi in [(F(-9), F(11)), (F(-3, 2), F(7, 2)),
                       (F(0), F(0)), (F(2), F(1)), (F(-g), F(g))]:
            direct = [(v, u*v-m*m) for v in
                      range(ceil((m*m+lo)/u), floor((m*m+hi)/u)+1)
                      if u*v != m*m]
            split = []
            for ell in range(ceil(lo/g), floor(hi/g)+1):
                if ell and (g*t*t+ell) % s == 0:
                    assert gcd(ell, s) == gcd(g, s)
                    split.append(((g*t*t+ell)//s, g*ell))
            assert direct == split
            # Signed stand-in weights and a linear real amplitude.
            def weighted(rows):
                return sum(((u % 5)-2)*((v % 7)-3)*(F(2, 3)-F(r, 11))
                           for v, r in rows)
            assert weighted(direct) == weighted(split)
            if hi-lo < u:
                assert len(split) <= 1
            cases += 1
print(f'Passed {cases} exact gcd reindexing and signed-sum cases.')

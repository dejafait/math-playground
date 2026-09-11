"""Exact finite algebra regression; no analytic or RH certification."""
from fractions import Fraction
from itertools import product

for frequencies in [(0,), (0, 1), (0, 1, 2), (0, 1, 3, 4)]:
    pairs = [(a, b) for a in frequencies for b in frequencies if a != b]
    for amplitudes in [{a: 1 for a in frequencies},
                       {a: j + 1 for j, a in enumerate(frequencies)}]:
        raw = Fraction(0)
        mass = 0
        for (r, s), (m, n), (a, b) in product(pairs, repeat=3):
            x, y, z = r-s, m-n, a-b
            if x+y+z:
                continue
            assert x+y != 0
            weight = amplitudes[r]*amplitudes[s]*amplitudes[m]*amplitudes[n]*amplitudes[a]*amplitudes[b]
            raw += Fraction(z, x+y)*(Fraction(x, y)+Fraction(y, x))/2*weight
            mass += weight
        assert raw == Fraction(mass, 2), (frequencies, raw, mass)
print('Sextic resonance identity passed (8 exact finite cases).')

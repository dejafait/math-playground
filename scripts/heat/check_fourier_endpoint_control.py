"""Finite identity checks for L230; no asymptotic distribution claim."""
from fractions import Fraction
from math import ceil, floor, pi, sin


def psi(x):
    return Fraction(0) if x.denominator == 1 else x - floor(x) - Fraction(1, 2)


checks = atoms = 0
for lower in [Fraction(i, 6) for i in range(-12, 49)]:
    for width in [Fraction(i, 7) for i in range(1, 7)]:
        upper = lower + width
        for e in range(1, 8):
            x, y = lower / e, upper / e
            exact = ceil(y) - floor(x) - 1 - (y - x)
            atom = Fraction(int(x.denominator == 1) + int(y.denominator == 1), 2)
            assert exact == psi(x) - psi(y) - atom
            atoms += bool(atom)
            checks += 1

# Both product maps, including nonintegral R and exact square endpoints.
products = 0
for a in range(2, 9):
    for b in range(2, 9):
        for c in range(2, 9):
            for d in range(2, 9):
                for t in [5, 10]:
                    for offset in [Fraction(0), Fraction(1, 8), Fraction(-1, 8)]:
                        q = a * b * c * d
                        r = q - t*t + offset
                        assert abs(q - (t*t + r)) < Fraction(1, 4)
                        assert floor(t*t + r + Fraction(1, 2)) == q
                        assert (q // a) == b*c*d
                        q = a*b*(c*d+1)
                        r = t*t + 1 - q + offset
                        assert abs(q - (t*t - r + 1)) < Fraction(1, 4)
                        assert floor(t*t - r + 1 + Fraction(1, 2)) == q
                        assert q % (a*b) == 0 and q // (a*b) - 1 == c*d
                        products += 2

samples = 0
for denominator in [7, 19, 101]:
    for numerator in range(denominator):
        x = Fraction(numerator, denominator)
        distance = min(x, 1-x)
        for cutoff in [8, 31, 128, 1024]:
            approx = -sum(sin(2*pi*k*float(x))/k for k in range(1, cutoff+1))/pi
            assert abs(approx) <= 2
            if distance:
                assert abs(float(psi(x))-approx) <= 2/(cutoff*float(distance))
            else:
                assert approx == 0
            samples += 1
print(f'Passed {checks} strict endpoint identities ({atoms} atom cases), '
      f'{products} product identities, and {samples} Fourier samples.')

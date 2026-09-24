"""Exact rational checks of the slice Taylor bounds; no distribution inference."""
from fractions import Fraction as F

count = 0
for den in range(1, 201):
    for num in range(den // 2 + 1):
        z = F(num, den)
        p2 = 1 + z / 2 - z**2 / 8
        p4 = p2 + z**3 / 16 - 5 * z**4 / 128
        upper = p4 + 7 * z**5 / 256
        assert p4 > 0
        assert p4**2 <= 1 + z <= upper**2
        lower2 = p2 + z**3 / 32
        upper2 = p2 + z**3
        assert lower2**2 <= 1 + z <= upper2**2
        count += 1
print(f'Passed {count} exact rational Taylor and cubic-bound checks.')

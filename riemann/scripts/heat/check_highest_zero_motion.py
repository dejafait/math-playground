"""Exact rational checks; hypothetical configurations, not theta zero data."""
from fractions import Fraction as F


def im_reciprocal(x, y):
    return -F(y, x*x + y*y)


checks = 0
for a in (-5, -1, 1, 5):
    for b in (1, 2, 3):
        own = (2*im_reciprocal(2*a, 2*b)
               + 2*im_reciprocal(0, 2*b)
               + 2*im_reciprocal(2*a, 0))
        assert own == -F(1, b)-F(b, a*a+b*b)
        checks += 1
        for u in range(-6, 7):
            for v in range(-b, b+1):
                if (u, v) in ((a, b), (-a, -b), (a, -b), (-a, b)):
                    continue
                if (u, v) == (0, 0):
                    continue
                # 4w/(w²-alpha²), evaluated independently in rational parts.
                dr = a*a-b*b-u*u+v*v
                di = 2*a*b-2*u*v
                paired = F(4*(b*dr-a*di), dr*dr+di*di)
                individual = (2*im_reciprocal(a-u, b-v)
                              + 2*im_reciprocal(a+u, b+v))
                assert paired == individual < 0
                for multiplicity in (1, 2, 5):
                    assert own + multiplicity*paired < own < 0
                checks += 1
print(f'Passed {checks} exact quartet and paired-imaginary checks.')

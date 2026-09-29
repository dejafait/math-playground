"""Exact polynomial checks for the positive density in L355, not RH."""

from collections import defaultdict
from fractions import Fraction as Q
from math import comb


def differentiate_density_polynomial(p):
    # k'= -2*s*k, v'=2*s, s'=2*v, q'=0.
    out = defaultdict(int)
    for (v, s, q), c in p.items():
        if v:
            out[v-1, s+1, q] += 2*v*c
        if s:
            out[v+1, s-1, q] += 2*s*c
        out[v, s+1, q] -= 2*c
    return {key: c for key, c in out.items() if c}


def eliminate_s(p):
    out = defaultdict(int)
    for (v, s, q), c in p.items():
        assert s % 2 == 0
        # s^2 = v^2-q^2.
        for j in range(s//2+1):
            out[v+2*(s//2-j), q+2*j] += c*comb(s//2, j)*(-1)**j
    return {key: c for key, c in out.items() if c}


def shift_v(p):
    out = defaultdict(int)
    for (v, q), c in p.items():
        for y in range(v+1):
            out[y, q+v-y] += c*comb(v, y)
    return {key: c for key, c in out.items() if c}


def check():
    p = {(0, 0, 0): 1}
    derivatives = [p]
    for _ in range(4):
        p = differentiate_density_polynomial(p)
        derivatives.append(p)
    assert eliminate_s(derivatives[2]) == {(2, 0): 4, (1, 0): -4, (0, 2): -4}
    fourth = {key: Q(c, 16) for key, c in eliminate_s(derivatives[4]).items()}
    assert fourth == {(4, 0): 1, (3, 0): -6, (2, 0): 7, (2, 2): -2,
                      (1, 2): 6, (1, 0): -1, (0, 4): 1, (0, 2): -4}
    assert shift_v(fourth) == {
        (4, 0): 1, (3, 1): 4, (3, 0): -6,
        (2, 2): 4, (2, 1): -18, (2, 0): 7,
        (1, 2): -12, (1, 1): 14, (1, 0): -1,
        (0, 2): 3, (0, 1): -1,
    }
    assert 4*6**2-18*6+7 == 43 and 8*6-18 > 0
    assert -12*7**2-1 == -589
    assert Q(16*589**2, 4*43) < 33000
    assert 40**4-56*40**2-33000 == 2437400
    print("PASS: exact derivative identities, shifted coefficients and positive kernel bound")


if __name__ == "__main__":
    check()

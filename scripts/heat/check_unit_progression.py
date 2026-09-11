#!/usr/bin/env python3
"""Exact endpoint-formula tests, not distribution evidence."""
from fractions import Fraction as F
from math import floor, ceil


def primitive(x):
    z = x - floor(x)
    return (z*z-z+F(1, 6))/2


checks = crossings = 0
for a in range(1, 6):
    for v in range(2, 9):
        for m in range(4, 16):
            for A, B in [(-2, 3), (-3, 3), (0, 1)]:
                R = F(3)
                p, q = a*(v+1), a*v
                L = lambda t: F(m*m+t+1, p)
                U = lambda t: F(m*m+t, q)
                assert L(A) < U(A)
                def f(x):
                    return max(min(F(B), p*x-m*m-1)
                               - max(F(A), q*x-m*m), 0)/R
                # Every switch/zero of the four defining affine lines.
                lines = [(0, A), (0, B), (p, -m*m-1), (q, -m*m)]
                knots = {L(A), U(B)}
                for s, t in lines:
                    for u, w in lines:
                        if s != u:
                            x = F(w-t, s-u)
                            if L(A) < x < U(B):
                                knots.add(x)
                knots = sorted(knots)
                area = sum((y-x)*(f(x)+f(y))/2
                           for x, y in zip(knots, knots[1:]))
                sampled = sum(f(F(b)) for b in range(floor(L(A)), ceil(U(B))+1))
                formula = F(B-A, 1)/R*(F(m*m, 1)+F(A+B, 2)-v)/ (a*v*(v+1))
                delta = (p*(primitive(L(B))-primitive(L(A)))
                         -q*(primitive(U(B))-primitive(U(A))))/R
                assert area == formula
                assert sampled-area == delta
                assert -area <= delta and abs(delta) <= F(B-A, 1)/R
                checks += 1
                crossings += floor(L(A)) != floor(L(B)) or floor(U(A)) != floor(U(B))
print(f'Passed {checks} rational cell checks ({crossings} endpoint crossings).')

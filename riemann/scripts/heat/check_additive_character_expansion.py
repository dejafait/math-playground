"""Finite regression checks for L189; orthogonality is proved in the lemma."""
from cmath import exp
from fractions import Fraction as F
from math import gcd, pi


def character(k, u):
    return exp(2j*pi*(k % u)/u)


cases = terms = 0
for n in range(2, 6):
    p = {a: (-1)**a * F(a, n) for a in range(n, 2*n+1)}
    q = {a: F((a % 3)-1, 2) for a in p}
    P, Q = {}, {}
    for a in p:
        for b in p:
            P[a*b] = P.get(a*b, 0) + p[a]*p[b]
            Q[a*b] = Q.get(a*b, 0) + q[a]*q[b]
    rho = F(1, 2)
    for lo, hi in [(F(n*n), F(n*n+2)),
                   (F(2*n*n)+F(1, 2), F(2*n*n)+F(3, 2)),
                   (F(n*n+2), F(n*n))]:
        direct = F(0)
        zero = F(0)
        nonzero = 0j
        delta = F(0)
        changed_nonzero = 0j
        for u in range(n*n, 4*n*n+1):
            for r in range(-4*n*n, 4*n*n+1):
                if r == 0 or gcd(r, u) != 1:
                    continue
                rows = []
                for m in range(1, 4*n*n+3):
                    k = m*m+r
                    if not (gcd(m, u) == 1 and lo-rho <= m <= hi+rho
                            and lo*lo-r <= m*m <= hi*hi-r
                            and u*n*n-r <= m*m <= 4*u*n*n-r
                            and m >= abs(r-rho*rho)/(2*rho)):
                        continue
                    # A real signed test coefficient, independent of congruence.
                    H = F((-1)**m, 1) - F(r, m)
                    weight = P.get(u, 0)*Q.get(k//u, 0)*H
                    change = F((m % 5)-2, 3)*P.get(u, 0) if k % u else F(0)
                    rows.append((k, weight, change))
                    zero += weight/u
                    delta += change/u
                    if k % u == 0:
                        direct += weight
                    terms += 1
                modes = [sum(complex(w)*character(a*k, u)/u
                             for k, w, d in rows) for a in range(1, u)]
                for a in range(1, u):
                    assert abs(modes[a-1].conjugate()-modes[u-a-1]) < 1e-9
                nonzero += sum(modes)
                changed_nonzero += sum(complex(w+d)*character(a*k, u)/u
                                       for a in range(1, u) for k, w, d in rows)
        assert abs(complex(zero)+nonzero-complex(direct)) < 1e-8
        assert abs(nonzero.imag) < 1e-8
        assert abs(changed_nonzero-nonzero+complex(delta)) < 1e-8
        cases += 1
assert terms > 0
print(f'Passed {cases} signed cutoff cases, {terms} extended terms; tolerance 1e-8.')

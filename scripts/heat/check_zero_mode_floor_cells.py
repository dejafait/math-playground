"""Exact finite regression tests for L190, not asymptotic evidence."""
from fractions import Fraction as F
from math import gcd

cases = terms = upper_hits = global_hits = 0
for n in range(2, 6):
    I = range(n, 2*n+1)
    p = {a: F((-1)**a*a, n) for a in I}
    q = {a: F(a % 3-1, 2) for a in I}
    P, Q = {}, {}
    for a in I:
        for b in I:
            P[a*b] = P.get(a*b, 0) + p[a]*p[b]
            Q[a*b] = Q.get(a*b, 0) + q[a]*q[b]
    rho = F(1, 2)
    for lo, hi in [(F(n*n), F(4*n*n)),
                   (F(2*n*n)+F(1, 2), F(2*n*n)+F(3, 2)),
                   (F(n*n+2), F(n*n))]:
        direct = F(0)
        T = {v: F(0) for v in range(n*n, 4*n*n+1)}
        for u in range(n*n, 4*n*n+1):
            for r in range(-4*n*n, 4*n*n+1):
                if r == 0 or gcd(r, u) != 1:
                    continue
                rows = []
                for m in range(1, 4*n*n+3):
                    k = m*m+r
                    if (gcd(m, u) == 1 and lo-rho <= m <= hi+rho
                            and lo*lo <= k <= hi*hi
                            and u*n*n <= k <= 4*u*n*n
                            and m >= abs(r-rho*rho)/(2*rho)):
                        rows.append((m, k))
                        H = F((-1)**m)-F(r, m)
                        direct += P.get(u, 0)*Q.get(k//u, 0)*H/u
                # Independently use the two cell inequalities, not floor.
                partition = []
                for v in T:
                    for m, k in rows:
                        if k == u*(v+1):
                            upper_hits += 1
                        if k == 4*u*n*n:
                            global_hits += 1
                        if u*v <= k < u*(v+1):
                            partition.append(m)
                            T[v] += P.get(u, 0)*(F((-1)**m)-F(r, m))/u
                assert sorted(partition) == sorted(m for m, k in rows)
                terms += len(rows)
        grouped = sum(Q.get(v, 0)*value for v, value in T.items())
        pairs = sum(q[c]*q[d]*T[c*d] for c in I for d in I)
        assert direct == grouped == pairs
        cases += 1
assert terms and upper_hits and global_hits
print(f'Passed {cases} exact signed cases, {terms} terms; strict and global boundaries exercised.')

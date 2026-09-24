"""Exact finite checks for L186; no asymptotic conclusions."""
from collections import defaultdict
from fractions import Fraction as F
from math import ceil, floor

cases = 0
unique_cases = 0
for n in range(2, 10):
    indices = range(n, 2 * n + 1)
    p = {a: (a % 3) - 1 for a in indices}
    q = {a: (a % 5) - 2 for a in indices}
    P, Q, W = defaultdict(int), defaultdict(int), defaultdict(int)
    for a in indices:
        for b in indices:
            P[a*b] += p[a]*p[b]
            Q[a*b] += q[a]*q[b]
            for c in indices:
                for d in indices:
                    W[a*b*c*d] += p[a]*p[b]*q[c]*q[d]
    # Rational endpoints deliberately include both integer boundaries and
    # clipped or empty intersections; these identities hold for any bounds.
    for m in range(n*n, 3*n*n + 1):
        for lower, upper in [(F(-3, 2), F(7, 2)), (F(0), F(0)),
                             (F(2), F(1)), (F(-n), F(n)),
                             (F(-m, n+1), F(m, n+1))]:
            direct = [sum((r**j)*W.get(m*m+r, 0)
                          for r in range(ceil(lower), floor(upper)+1)
                          if r != 0) for j in (0, 1)]
            paired = [0, 0]
            for u, weight in P.items():
                vs = [v for v in range(ceil((m*m+lower)/u),
                                      floor((m*m+upper)/u)+1)
                      if u*v != m*m]
                for v in vs:
                    r = u*v-m*m
                    paired[0] += weight*Q.get(v, 0)
                    paired[1] += weight*Q.get(v, 0)*r
                if upper-lower < u:
                    b, e = divmod(m*m, u)
                    j0 = ceil((lower+e)/u)
                    r0 = u*j0-e
                    filtered = [b+j0] if lower <= r0 <= upper and r0 else []
                    assert vs == filtered, (n, m, u, lower, upper)
                    unique_cases += 1
            assert direct == paired, (n, m, lower, upper, direct, paired)
            cases += 1
print(f'Passed {cases} signed convolution checks and {unique_cases} residue-filter checks.')

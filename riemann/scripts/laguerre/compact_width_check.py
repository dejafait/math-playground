"""Exact Bernstein certificate at width 3/4 for L264."""
from fractions import Fraction as F
from math import factorial as fac, comb


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


b, epsilon = F(1,4), F(1,40)
c = [F(1)]
for r in [10-2*epsilon, 10-epsilon, F(10), 10+epsilon, 10+2*epsilon]:
    c = mul(c, [r*r, F(1)])
c = mul(c, [(100+b*b)**2, 200-2*b*b, F(1)])
for j in range(8):
    a = [F(0)] * 16
    for k in range(8):
        d = 15-2*k
        for h in range(j+1):
            for l in range(d+1):
                a[l] += (c[k]*F(4,3)**(2*k)*(-1)**h*comb(16,h)
                         * F(comb(d,l)*2**l*(2*(j-h))**(d-l), fac(d)))
    beta = [sum(a[l]*F(comb(i,l),comb(15,l)) for l in range(i+1))
            for i in range(16)]
    assert all(v >= 0 for v in beta)
    if j == 0:
        assert beta[0] == 0 and all(v > 0 for v in beta[1:])
    else:
        assert all(v > 0 for v in beta)
    print('PASS interval', j, ': Bernstein coefficients positive',
          '(except endpoint zero)' if j == 0 else '')

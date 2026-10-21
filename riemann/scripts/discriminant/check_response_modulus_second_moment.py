"""Exact rational bounds for step 165; no floating-point proof decisions."""
import json
from pathlib import Path
import math
from fractions import Fraction as F

DEN = 10**18


def round_iv(lo, hi):
    return (F(lo.numerator * DEN // lo.denominator, DEN),
            F(-((-hi.numerator * DEN) // hi.denominator), DEN))


def add(a, b):
    return round_iv(a[0]+b[0], a[1]+b[1])


def sub(a, b):
    return round_iv(a[0]-b[1], a[1]-b[0])


def mul(a, b):
    vals = [x*y for x in a for y in b]
    return round_iv(min(vals), max(vals))


def div(a, b):
    assert b[0] > 0
    return mul(a, (1/b[1], 1/b[0]))


def exact(x):
    return F(x), F(x)


def encode(a):
    return {'lower': str(a[0]), 'upper': str(a[1]),
            'decimal_preview': [float(x) for x in a]}


def primes_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for a in range(2, math.isqrt(n) + 1):
        if sieve[a]:
            sieve[a*a:n+1:a] = b'\x00' * ((n-a*a)//a+1)
    return [a for a in range(2, n+1) if sieve[a]]


def main():
    cutoff, order = 200, 40
    ps = primes_to(cutoff)
    c, local, tails = {}, {}, {}
    for j in [1, 2, 13, 14, 15, 16]:
        val = exact(1)
        local[j] = []
        for p in ps:
            term = total = F(1)
            for e in range(1, order+1):
                term *= F((j+e-1)**2, e**2*p**5)
                total += term
            ratio = F((j+order)**2, (order+1)**2*p**5)
            assert ratio < 1
            rem = term*ratio/(1-ratio)
            factor = round_iv(total, total+rem)
            val = mul(val, factor)
            local[j].append({'p': p, 'factor': encode(factor)})
        # binom(j+e-1,e)<=j**e; log local <=j^2*p^-5/(1-j^2*p^-5).
        r = F(j*j, 4*cutoff**4) / (1-F(j*j, (cutoff+1)**5))
        assert r < 1
        tails[f'C{j}'] = str(r)
        c[j] = mul(val, (F(1), 1/(1-r)))
    zs = {}
    for power in [3, 5, 6]:
        finite = exact(1)
        for p in ps:
            finite = mul(finite, exact(1/(1-F(1, p**power))))
        r = F(1, (power-1)*cutoff**(power-1))/(1-F(1, (cutoff+1)**power))
        tails[f'zeta{power}'] = str(r)
        zs[power] = mul(finite, (F(1), 1/(1-r)))
    s = div(mul(zs[5], mul(zs[3], zs[3])), zs[6])
    t = exact(1)
    for p in ps:
        u, v = F(1, p**3), F(1, p**5)
        factor = ((1+v)*(1-u*u)+2*u*(1-v))/((1-v)**3*(1-u)**2)
        t = mul(t, exact(factor))
    # Local T <= (1-p^-3)^-4(1-p^-5)^-4.
    r = (F(2, cutoff**2)/(1-F(1, (cutoff+1)**3))
         + F(1, cutoff**4)/(1-F(1, (cutoff+1)**5)))
    tails['T'] = str(r)
    t = mul(t, (F(1), 1/(1-r)))
    b = {}
    for k in [13, 14]:
        ratio = div(c[k+1], c[k])
        theta = div(sub(s, c[1]), sub(ratio, c[1]))
        bk = add(c[2], mul(theta, sub(div(c[k+2], c[k]), c[2])))
        b[k] = bk
    bounds = {'S': encode(s), 'T': encode(t),
              'B13': encode(b[13]), 'B14': encode(b[14]),
              'C': {j: encode(v) for j, v in c.items()}}
    checks = {
        'B13_below_2236_over_1000': b[13][1] < F(2236, 1000),
        'T_above_2237_over_1000': t[0] > F(2237, 1000),
        'T_below_4475_over_2000': t[1] < F(4475, 2000),
        'B14_above_4477_over_2000': b[14][0] > F(4477, 2000),
        'S_above_C1': s[0] > c[1][1],
        'C2_above_C1_squared': c[2][0] > c[1][1]**2,
    }
    out = dict(status='EXACT_RATIONAL_INTERVAL_CERTIFICATE',
               prime_cutoff=cutoff, local_order=order, primes=ps,
               denominator=DEN, bounds=bounds, checks=checks,
               log_tail_upper_bounds=tails, C_local_factors=local,
               failures=[key for key, ok in checks.items() if not ok])
    path = Path(__file__).with_name('response-modulus-second-moment-certificate.json')
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Actual intervals / required thresholds:')
    for key in ['S', 'T', 'B13', 'B14']:
        print(key, bounds[key]['decimal_preview'])
    print('Checks:', checks, 'Failures:', out['failures'])
    print('Certificate:', path)
    assert all(checks.values())


if __name__ == '__main__':
    main()

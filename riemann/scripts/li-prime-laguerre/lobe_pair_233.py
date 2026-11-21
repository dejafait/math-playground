#!/usr/bin/env python3
"""Approved finite diagnostic; all bounds use integer/rational arithmetic.

Run from riemann: python3 scripts/li-prime-laguerre/lobe_pair_233.py
Intervals [a,b] encode [a/S,b/S]. Certificate retains all actual terms.
"""
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import json

S = 10**50
N = 70
OUT = Path(__file__).with_name('lobe-pair-certificate-233.json')


def ceildiv(a, b):
    assert b > 0
    return -((-a)//b)


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def neg(a):
    return (-a[1], -a[0])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    v = [x*y for x in a for y in b]
    return (min(v)//S, ceildiv(max(v), S))


def div(a, b):
    assert b > 0
    return (a[0]//b, ceildiv(a[1], b))


def scale(a, k):
    return (k*a[0], k*a[1]) if k >= 0 else (k*a[1], k*a[0])


def rational(a, b=1):
    return (a*S//b, ceildiv(a*S, b))


def log_reduced(a, b):
    # z=a/b in [0,1/3].  log((1+z)/(1-z))=2*atanh(z).
    assert 0 <= 3*a <= b
    z = rational(a, b)
    z2 = mul(z, z)
    power, total = z, (0, 0)
    for j in range(N):
        total = add(total, div(power, 2*j+1))
        power = mul(power, z2)
    # Tail <= 9/[4*(2N+1)*3^(2N+1)] <= 1/S.
    assert 9*S <= 4*(2*N+1)*3**(2*N+1)
    total = scale(total, 2)
    return (total[0], total[1]+1)


LOG2 = log_reduced(1, 3)


def log_integer(m):
    assert m >= 1
    k = m.bit_length()-1
    t = 1 << k
    return add(scale(LOG2, k), log_reduced(m-t, m+t))


def coefficients(n):
    # A=(n-1)!*ell_n has integer coefficients, ascending order.
    f = factorial(n-1)
    return [(-1)**j*comb(n, j+1)*f//factorial(j) for j in range(n)]


def sign_at(coeff, a):
    # Exact numerator of S^degree*A(a/S).
    d = len(coeff)-1
    value = sum(c*a**j*S**(d-j) for j, c in enumerate(coeff))
    return (value > 0)-(value < 0)


def polynomial(coeff, x):
    y = (0, 0)
    for c in reversed(coeff):
        y = add(mul(y, x), rational(c))
    return y


def isolate(n):
    coeff = coefficients(n)
    brackets = []
    a, sa = 0, sign_at(coeff, 0)
    for k in range(1, 16*64+1):
        b = k*S//16
        sb = sign_at(coeff, b)
        assert sb != 0, 'Unexpected exact grid root: retain for separate handling'
        if sa*sb < 0:
            brackets.append([a, b, sa, sb])
        a, sa = b, sb
        if len(brackets) == n-1:
            break
    assert len(brackets) == n-1  # degree bound makes these all the roots
    result = [(0, 0)]
    for a, b, sa, sb in brackets:
        while b-a > 1:
            mid = (a+b)//2
            sm = sign_at(coeff, mid)
            assert sm != 0, 'Unexpected exact bisection root'
            if sm == sa:
                a, sa = mid, sm
            else:
                b, sb = mid, sm
        assert sa*sb < 0 and 0 < a < b
        result.append((a, b))
    assert all(result[k][1] < result[k+1][0] for k in range(n-1))
    return result


def exponential_floor(root):
    if root == (0, 0):
        return {'floor': 1, 'exponential_exact': 1}
    left, right = 1, 2
    while log_integer(right)[0] <= root[1]:
        right *= 2
    while right-left > 1:
        mid = (left+right)//2
        lm = log_integer(mid)
        if lm[1] < root[0]:
            left = mid
        elif lm[0] > root[1]:
            right = mid
        else:
            raise ArithmeticError('Endpoint overlap: refine, do not guess')
    llog, rlog = log_integer(left), log_integer(right)
    assert llog[1] < root[0] <= root[1] < rlog[0]
    return {'floor': left, 'exponential_open_interval': [left, right],
            'log_floor': llog, 'log_successor': rlog}


def sieve(limit):
    table = bytearray(b'\1')*(limit+1)
    table[:2] = b'\0\0'
    p = 2
    while p*p <= limit:
        if table[p]:
            table[p*p:limit+1:p] = b'\0'*((limit-p*p)//p+1)
        p += 1
    return [p for p in range(2, limit+1) if table[p]]


def antiderivative(coeff, f, x):
    # Exact coefficients A_j/[f*(j+1)] and zero constant.
    y = (0, 0)
    for j in reversed(range(len(coeff))):
        c = rational(coeff[j], f*(j+1))
        y = add(mul(y, x), c)
    return mul(y, x)


def decimal_bounds(x, places=12):
    unit = 10**places
    lo, hi = x[0]*unit//S, ceildiv(x[1]*unit, S)
    def fmt(v):
        sign = '-' if v < 0 else ''
        v = abs(v)
        return f'{sign}{v//unit}.{v%unit:0{places}d}'
    return [fmt(lo), fmt(hi)]


def main():
    certificate = {'scale': str(S), 'log_series_terms': N,
                   'tail_bound_numerator': 9,
                   'tail_bound_denominator': str(4*(2*N+1)*3**(2*N+1)),
                   'required_pair_upper_bound': 0, 'pairs': [], 'failures': []}
    stop = False
    try:
        for n in (3, 4, 5, 6):
            roots = isolate(n)
            coeff, f = coefficients(n), factorial(n-1)
            for j in range(0, n-2, 2):
                low = exponential_floor(roots[j])
                high = exponential_floor(roots[j+2])
                terms, total = [], (0, 0)
                for p in sieve(high['floor']):
                    lp = log_integer(p)
                    m, k = p, 1
                    while m <= high['floor']:
                        if m > low['floor']:
                            lm = scale(lp, k)
                            assert roots[j][1] < lm[0] <= lm[1] < roots[j+2][0]
                            ell = div(polynomial(coeff, lm), f)
                            term = div(mul(lp, ell), m)
                            terms.append({'m': m, 'p': p, 'k': k,
                                          'log_p': lp, 'log_m': lm,
                                          'ell': ell, 'term': term})
                            total = add(total, term)
                        m *= p
                        k += 1
                terms.sort(key=lambda t: t['m'])
                assert len({t['m'] for t in terms}) == len(terms)
                fa = antiderivative(coeff, f, roots[j])
                fb = antiderivative(coeff, f, roots[j+2])
                integral = sub(fb, fa)
                value = sub(total, integral)
                sign = 'POSITIVE' if value[0] > 0 else ('NEGATIVE' if value[1] < 0 else 'UNRESOLVED')
                pair = {'n': n, 'j': j, 'integer_coefficients': coeff,
                        'coefficient_divisor': f, 'all_root_brackets': roots,
                        'root_endpoint_signs': [[sign_at(coeff, a), sign_at(coeff, b)] for a, b in roots[1:]],
                        'lower_endpoint': low, 'upper_endpoint': high,
                        'prime_power_count': len(terms), 'terms': terms,
                        'prime_sum': total, 'antiderivative_lower': fa,
                        'antiderivative_upper': fb, 'integral': integral,
                        'B': value, 'B_decimal_outward': decimal_bounds(value), 'sign': sign}
                certificate['pairs'].append(pair)
                OUT.write_text(json.dumps(certificate, indent=2)+'\n')
                print(f'n={n}, j={j}: B in {decimal_bounds(value)}, required <=0; {sign}; powers={len(terms)}', flush=True)
                if sign in ('POSITIVE', 'UNRESOLVED'):
                    stop = True
                    break
            if stop:
                break
        certificate['termination'] = certificate['pairs'][-1]['sign'] if stop else 'ALL_SIX_NONPOSITIVE'
    except Exception as exc:
        certificate['failures'].append(f'{type(exc).__name__}: {exc}')
        certificate['termination'] = 'FAILURE'
        raise
    finally:
        OUT.write_text(json.dumps(certificate, indent=2)+'\n')
        print(f'Failures: {certificate["failures"]}; certificate: {OUT}')


if __name__ == '__main__':
    main()

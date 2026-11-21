#!/usr/bin/env python3
"""Independent rational-series/trial-division verification of B_(6,2).

No imports from the producer. Check every witness term, not a preview.
Round exact Fraction log series to 30-place rational intervals. Save
all recomputed terms and compare all 637 original witness records.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE/'lobe-pair-certificate-233.json'
OUT = HERE/'lobe-witness-independent-233.json'
Q = 10**30
R = 50


def rounded_bounds(lo, hi):
    a, b = lo*Q, hi*Q
    return [a.numerator//a.denominator, -((-b.numerator)//b.denominator)]


def as_fractions(iv, denominator=Q):
    return (F(iv[0], denominator), F(iv[1], denominator))


def interval_product(a, b):
    values = [x*y for x in a for y in b]
    return (min(values), max(values))


def interval_add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def evaluate(coeff, x):
    value = (F(0), F(0))
    for c in reversed(coeff):
        value = interval_add(interval_product(value, x), (c, c))
    return value


def exact_log_bounds(m):
    # Rational range reduction; sum and remainder kept as Fractions.
    k = m.bit_length()-1
    t = 2**k
    def atanh(z):
        assert 0 <= z <= F(1, 3)
        total = sum((2*z**(2*i+1)/F(2*i+1) for i in range(R)), F(0))
        tail = 2*z**(2*R+1)/(F(2*R+1)*(1-z*z))
        return (total, total+tail)
    a, b = atanh(F(1, 3)), atanh(F(m-t, m+t))
    return rounded_bounds(k*a[0]+b[0], k*a[1]+b[1])


def factor(m):
    # Independent exhaustive trial division, not the producer's sieve.
    result = []
    for p in range(2, isqrt(m)+1):
        if m % p == 0:
            k = 0
            while m % p == 0:
                m //= p
                k += 1
            result.append((p, k))
        if m == 1:
            break
    if m > 1:
        result.append((m, 1))
    return result


def decimal_outward(iv):
    unit = 10**12
    a = iv[0]*unit//Q
    b = -((-iv[1]*unit)//Q)
    return [f'{v//unit}.{v%unit:012d}' for v in (a, b)]


def main():
    source = json.loads(SOURCE.read_text())
    pair = source['pairs'][5]
    assert (pair['n'], pair['j']) == (6, 2)
    assert not source['failures'] and source['termination'] == 'POSITIVE'
    s = int(source['scale'])
    coeff = list(map(F, [720, -1800, 1200, -300, 30, -1]))
    assert pair['integer_coefficients'] == [int(c) for c in coeff]
    assert pair['coefficient_divisor'] == 120
    roots = [as_fractions(iv, s) for iv in pair['all_root_brackets']]
    assert roots[0] == (0, 0) and len(roots) == 6
    root_signs = []
    for a, b in roots[1:]:
        va = evaluate(coeff, (a, a))[0]
        vb = evaluate(coeff, (b, b))[0]
        assert va*vb < 0
        root_signs.append([1 if va > 0 else -1, 1 if vb > 0 else -1])
    assert root_signs == pair['root_endpoint_signs']
    assert all(roots[i][1] < roots[i+1][0] for i in range(5))
    # Five disjoint sign changes exhaust the degree-five polynomial.
    endpoints = []
    for index, m in ((2, 8), (4, 4442)):
        lower, upper = exact_log_bounds(m), exact_log_bounds(m+1)
        assert F(lower[1], Q) < roots[index][0]
        assert roots[index][1] < F(upper[0], Q)
        endpoints.append({'root_index': index, 'floor': m,
                          'log_floor': lower, 'log_successor': upper})
    expected = []
    for m in range(9, 4443):
        fs = factor(m)
        if len(fs) == 1:
            expected.append((m, *fs[0]))
    recorded = [(t['m'], t['p'], t['k']) for t in pair['terms']]
    assert recorded == expected and len(recorded) == 637
    recomputed = []
    sum_lo, sum_hi = 0, 0
    cache = {}
    for record, (m, p, k) in zip(pair['terms'], expected):
        if p not in cache:
            cache[p] = exact_log_bounds(p)
        lp = as_fractions(cache[p])
        lm = (k*lp[0], k*lp[1])
        assert roots[2][1] < lm[0] and lm[1] < roots[4][0]
        ell_raw = evaluate(coeff, lm)
        ell = (ell_raw[0]/120, ell_raw[1]/120)
        term_raw = interval_product(lp, ell)
        term = rounded_bounds(term_raw[0]/m, term_raw[1]/m)
        # Original bounds are finer; require every original log/weight/
        # contribution enclosure to be nested in our independent one.
        for key, wide in [('log_p', lp), ('log_m', lm), ('ell', ell),
                          ('term', as_fractions(term))]:
            narrow = as_fractions(record[key], s)
            assert wide[0] <= narrow[0] <= narrow[1] <= wide[1]
        sum_lo += term[0]
        sum_hi += term[1]
        recomputed.append({'m': m, 'p': p, 'k': k,
                           'log_p': cache[p], 'term': term})
    anti = [F(0)]+[c/F(120*(j+1)) for j, c in enumerate(coeff)]
    fa, fb = evaluate(anti, roots[2]), evaluate(anti, roots[4])
    integral = rounded_bounds(fb[0]-fa[1], fb[1]-fa[0])
    value = [sum_lo-integral[1], sum_hi-integral[0]]
    original_B = as_fractions(pair['B'], s)
    assert F(value[0], Q) <= original_B[0] <= original_B[1] <= F(value[1], Q)
    assert value[0] > 0
    result = {'denominator': str(Q), 'rational_series_terms': R,
              'all_five_root_signs_checked': root_signs,
              'endpoints': endpoints, 'complete_prime_power_count': len(expected),
              'every_original_witness_term_checked': True,
              'terms': recomputed, 'prime_sum': [sum_lo, sum_hi],
              'integral': integral, 'B': value,
              'B_decimal_outward': decimal_outward(value),
              'threshold': 0, 'failures': [], 'result': 'POSITIVE'}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Independent B_(6,2) in {decimal_outward(value)}; required <=0; POSITIVE')
    print(f'Checked all {len(expected)} terms, every root and endpoint; failures=[]; certificate: {OUT}')


if __name__ == '__main__':
    main()

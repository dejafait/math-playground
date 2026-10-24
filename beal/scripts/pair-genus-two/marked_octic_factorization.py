"""Exact entire-octic factor certificate; ascending coefficient arrays.

Imported criterion: Milne, Fields and Galois Theory v5.10, Exercise 4-8.
No external packages, field-order assumption, or maximal-order assumption.
"""
from pathlib import Path
from math import gcd, isqrt
from functools import reduce
import json

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / 'marked-octic-factorization-certificate.json'


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    return trim([((a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def scale(a, c, p):
    return trim([c*x % p for x in a])


def mul(a, b, p):
    if not a or not b:
        return []
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j]+x*y) % p
    return trim(c)


def divmod_poly(a, b, p):
    a, b = trim([x % p for x in a]), trim([x % p for x in b])
    assert b
    q = [0]*max(0, len(a)-len(b)+1)
    inverse = pow(b[-1], -1, p)
    while a and len(a) >= len(b):
        k, c = len(a)-len(b), a[-1]*inverse % p
        q[k] = c
        a = add(a, [0]*k+scale(b, -c, p), p)
    return trim(q), a


def bezout(a, b, p):
    r0, r1 = a, b
    s0, s1, t0, t1 = [1], [], [], [1]
    trace = []
    while r1:
        q, r = divmod_poly(r0, r1, p)
        trace.append(dict(dividend=r0, divisor=r1, quotient=q, remainder=r))
        r0, r1 = r1, r
        s0, s1 = s1, add(s0, scale(mul(q, s1, p), -1, p), p)
        t0, t1 = t1, add(t0, scale(mul(q, t1, p), -1, p), p)
    c = pow(r0[-1], -1, p)
    g, s, t = scale(r0, c, p), scale(s0, c, p), scale(t0, c, p)
    assert add(mul(s, a, p), mul(t, b, p), p) == g
    return dict(gcd=g, left_multiplier=s, right_multiplier=t, euclidean_trace=trace)


def modular_power(a, exponent, f, p):
    e, result, base, trace = exponent, [1], a, []
    while e:
        if e & 1:
            product = mul(result, base, p)
            q, r = divmod_poly(product, f, p)
            trace.append(dict(kind='multiply', left=result, right=base,
                              quotient=q, remainder=r))
            result = r
        e >>= 1
        if e:
            product = mul(base, base, p)
            q, r = divmod_poly(product, f, p)
            trace.append(dict(kind='square', left=base, right=base,
                              quotient=q, remainder=r))
            base = r
    return dict(base=a, exponent=exponent, remainder=result, trace=trace)


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def main():
    g = [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]
    content = reduce(gcd, g)
    primitive = [a//content for a in g]
    attempts = []
    success = None
    for p in range(2, 102):
        if not prime(p):
            continue
        if g[-1] % p == 0:
            attempts.append(dict(prime=p, skipped='leading coefficient vanishes'))
            continue
        # Even bad-discriminant primes may be tested: they cannot pass.
        inverse = pow(primitive[-1], -1, p)
        f = [a*inverse % p for a in primitive]
        x, powers = [0, 1], []
        a = x
        for k in range(1, 9):
            entry = modular_power(a, p, f, p)
            entry['frobenius_index'] = k
            powers.append(entry)
            a = entry['remainder']
        fourth_minus_x = add(powers[3]['remainder'], scale(x, -1, p), p)
        witness = bezout(f, fourth_minus_x, p)
        eighth_minus_x = add(powers[7]['remainder'], scale(x, -1, p), p)
        passed = eighth_minus_x == [] and witness['gcd'] == [1]
        row = dict(prime=p, normalized_reduction=f, frobenius_powers=powers,
                   fourth_minus_x=fourth_minus_x, fourth_gcd_certificate=witness,
                   eighth_minus_x=eighth_minus_x, irreducible=passed)
        attempts.append(row)
        if passed:
            success = row
            break
    checks = dict(input_degree_eight=len(g)-1 == 8,
                  exact_positive_content=content == 11 and reduce(gcd, primitive) == 1,
                  exact_product=[content*a for a in primitive] == g,
                  irreducible_reduction_found=success is not None)
    result = dict(input_coefficients=g, content=content,
                  primitive_coefficients=primitive, search_prime_cap=101,
                  attempts=attempts, selected_prime=success['prime'] if success else None,
                  rational_factors=[dict(coefficients=primitive, multiplicity=1)] if success else None,
                  checks=checks, failures=[k for k, v in checks.items() if not v])
    CERTIFICATE.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Largest prime visited: {attempts[-1]["prime"]}; required <=101')
    print('Selected irreducible-reduction prime:', result['selected_prime'])
    print('Content:', content, '; required=11; factor degrees:', [8] if success else 'unresolved')
    print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {result["failures"]}')
    print('Certificate:', CERTIFICATE.relative_to(HERE.parent.parent))
    assert not result['failures']


if __name__ == '__main__':
    main()

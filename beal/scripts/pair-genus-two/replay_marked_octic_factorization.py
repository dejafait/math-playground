"""Arithmetic replay for the selected certificate, without producer imports.

This is a second exact arithmetic implementation, not a separate critical
mathematical audit of the theorem application.
"""
from pathlib import Path
from math import gcd, isqrt
from functools import reduce
import json

HERE = Path(__file__).resolve().parent


def main():
    source = HERE / 'marked-octic-factorization-certificate.json'
    saved = json.loads(source.read_text())
    p = saved['selected_prime']
    row = next(a for a in saved['attempts'] if a['prime'] == p)
    f = row['normalized_reduction']
    n = len(f)-1
    checks = {}

    def check(name, actual, required):
        checks[name] = dict(actual=actual, required=required, pass_=actual == required)

    def plus(a, b):
        c = [((a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)) % p
             for i in range(max(len(a), len(b)))]
        while c and c[-1] == 0:
            c.pop()
        return c

    def times(a, b):
        c = [0]*(max(0, len(a)+len(b)-1))
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i+j] = (c[i+j]+x*y) % p
        return plus(c, [])

    def quotient_product(a, b):
        # Multiplication by x is a shift followed by one use of x^n=-sum f_i*x^i.
        a = a+[0]*(n-len(a))
        c = [0]*n
        for y in b:
            c = [(z+y*x) % p for z, x in zip(c, a)]
            high = a[-1]
            a = [0]+a[:-1]
            a = [(x-high*f[i]) % p for i, x in enumerate(a)]
        return plus(c, [])

    g = [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]
    primitive = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]
    check('input_coefficients', saved['input_coefficients'], g)
    check('content', saved['content'], reduce(gcd, g))
    check('primitive_coefficients', saved['primitive_coefficients'], primitive)
    check('primitive_content', reduce(gcd, primitive), 1)
    check('complete_product', [saved['content']*a for a in primitive], g)
    check('factor_list', saved['rational_factors'], [dict(coefficients=primitive, multiplicity=1)])
    check('selected_prime', p, 19)
    check('prime_trial_division', all(p % d for d in range(2, isqrt(p)+1)), True)
    check('leading_coefficient_nonzero', g[-1] % p, 4)
    check('monic_reduction', f, [(a*pow(275, -1, p)) % p for a in primitive])
    check('primitive_leading_residue', 275 % p, 9)
    check('normalizing_inverse', pow(275, -1, p), 17)
    a, powers, arithmetic_rows = [0, 1], [], []
    for k, entry in enumerate(row['frobenius_powers'], 1):
        check(f'power_{k}_base', entry['base'], a)
        check(f'power_{k}_exponent', entry['exponent'], p)
        check(f'power_{k}_index', entry['frobenius_index'], k)
        r = [1]
        for _ in range(p):
            r = quotient_product(r, a)
        check(f'power_{k}_remainder', entry['remainder'], r)
        for j, step in enumerate(entry['trace']):
            product = times(step['left'], step['right'])
            reconstructed = plus(times(step['quotient'], f), step['remainder'])
            check(f'power_{k}_trace_{j}', product, reconstructed)
            check(f'power_{k}_trace_{j}_degree', len(step['remainder']) < len(f), True)
            arithmetic_rows.append(dict(k=k, j=j, product=product, reconstructed=reconstructed))
        powers.append(r)
        a = r
    check('power_count', len(powers), 8)
    check('fourth_remainder', powers[3], [0, 18])
    check('eighth_remainder', powers[7], [0, 1])
    h = plus(powers[3], [0, -1])
    check('fourth_minus_x', row['fourth_minus_x'], h)
    check('eighth_minus_x', row['eighth_minus_x'], [])
    bez = row['fourth_gcd_certificate']
    bezout_value = plus(times(bez['left_multiplier'], f), times(bez['right_multiplier'], h))
    check('bezout_identity', bezout_value, [1])
    check('bezout_gcd', bez['gcd'], [1])
    for j, step in enumerate(bez['euclidean_trace']):
        check(f'euclid_{j}', step['dividend'],
              plus(times(step['quotient'], step['divisor']), step['remainder']))
        check(f'euclid_{j}_degree', len(step['remainder']) < len(step['divisor']), True)
    failures = [name for name, c in checks.items() if not c['pass_']]
    result = dict(prime=p, normalized_reduction=f, frobenius_remainders=powers,
                  bezout_left=bez['left_multiplier'], bezout_right=bez['right_multiplier'],
                  bezout_identity=bezout_value, arithmetic_rows=arithmetic_rows,
                  checks=checks, failures=failures)
    destination = HERE / 'marked-octic-factorization-replay.json'
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}')
    print('Actual/required: Q-factor degrees [8]/[8]; multiplicities [1]/[1]; content 11/11')
    print('Actual/required: R4=-x/-x; R8=x/x; Bezout value 1/1 in F19[x]')
    print('Replay:', destination.relative_to(HERE.parent.parent))
    assert not failures


if __name__ == '__main__':
    main()

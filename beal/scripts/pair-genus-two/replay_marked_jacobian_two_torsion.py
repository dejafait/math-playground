#!/usr/bin/env python3
"""Independent arithmetic replay for L126; no producer/helper imports."""
from pathlib import Path
from math import isqrt
from hashlib import sha256
import json

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'marked-jacobian-two-torsion-certificate.json'
OUT = BASE / 'marked-jacobian-two-torsion-replay.json'


def main():
    data = json.loads(SOURCE.read_text())
    checks, summaries = {}, []

    def ck(name, actual, required):
        checks[name] = dict(actual=actual, required=required, passes=actual == required)

    def trim(a):
        while a and a[-1] == 0:
            a.pop()
        return a

    def add(a, b, p):
        return trim([((a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)) % p
                     for i in range(max(len(a), len(b)))])

    def mul(a, b, p):
        out = [0]*max(0, len(a)+len(b)-1)
        for i, u in enumerate(a):
            for j, v in enumerate(b):
                out[i+j] = (out[i+j]+u*v) % p
        return trim(out)

    def rem(a, h, p):
        a = trim([v % p for v in a])
        while len(a) >= len(h):
            v = a[-1]*pow(h[-1], -1, p) % p
            shift = len(a)-len(h)
            for j, u in enumerate(h):
                a[shift+j] = (a[shift+j]-v*u) % p
            trim(a)
        return a

    def bezout(name, h, b, cert, p):
        value = add(mul(cert['left_multiplier'], h, p),
                    mul(cert['right_multiplier'], b, p), p)
        ck(name+'_value', value, [1])
        ck(name+'_saved_gcd', cert['gcd'], [1])
        # Every stored Euclidean identity is also replayed in full.
        for j, row in enumerate(cert['euclidean_trace']):
            ck(name+f'_euclid_{j}', row['dividend'],
               add(mul(row['quotient'], row['divisor'], p), row['remainder'], p))
            ck(name+f'_degree_{j}', len(row['remainder']) < len(row['divisor']), True)
        return value

    F = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]
    ck('F', data['F'], F)
    ck('scalar', data['marked_curve_scalar'], 11)
    ck('field_degree', data['root_field_degree'], 8)
    ck('discriminant', data['field_discriminant'], 2**8*3**7*5**4*11**7)
    ck('discriminant_factors', data['field_discriminant_factorization'],
       [[2, 8], [3, 7], [5, 4], [11, 7]])
    ck('helper_hash', data['source_helper_sha256'],
       sha256((BASE/'marked_octic_factorization.py').read_bytes()).hexdigest())
    ck('prime_list', [r['prime'] for r in data['modular_certificates']], [7, 13, 19, 29, 31, 43])
    for row in data['modular_certificates']:
        p = row['prime']
        prefix = str(p)
        ck(prefix+'_prime', p > 1 and all(p % v for v in range(2, isqrt(p)+1)), True)
        ck(prefix+'_leading_unit', F[-1] % p != 0, True)
        f = [v*pow(F[-1], -1, p) % p for v in F]
        ck(prefix+'_normalization', row['monic_reduction'], f)
        df = [i*f[i] % p for i in range(1, 9)]
        bezout(prefix+'_squarefree', f, df, row['squarefree_bezout'], p)
        total, factor_summaries = [1], []
        for j, factor in enumerate(row['factors']):
            h = factor['coefficients']
            n = len(h)-1
            label = prefix+f'_{j}'
            ck(label+'_monic', h[-1], 1)
            ck(label+'_coefficients', all(0 <= v < p for v in h), True)
            ck(label+'_degree', factor['degree'], n)
            ck(label+'_multiplicity', factor['multiplicity'], 1)
            x = rem([0, 1], h, p)
            ck(label+'_x', factor['x_remainder'], x)
            ck(label+'_power_count', len(factor['powers']), n)
            a, powers = x, []
            for k, w in enumerate(factor['powers'], 1):
                ck(label+f'_{k}_base', w['base'], a)
                ck(label+f'_{k}_exponent', w['exponent'], p)
                ck(label+f'_{k}_index', w['index'], k)
                # Different powering from producer: p successive products.
                r = [1]
                for _ in range(p):
                    r = rem(mul(r, a, p), h, p)
                ck(label+f'_{k}_residue', w['remainder'], r)
                for m, op in enumerate(w['trace']):
                    ck(label+f'_{k}_{m}_division', mul(op['left'], op['right'], p),
                       add(mul(op['quotient'], h, p), op['remainder'], p))
                    ck(label+f'_{k}_{m}_degree', len(op['remainder']) < len(h), True)
                a = r
                powers.append(r)
            ck(label+'_last_frobenius', a, x)
            divisors = [q for q in range(2, n+1) if n % q == 0 and
                        all(q % v for v in range(2, isqrt(q)+1))]
            ck(label+'_gcd_indices', [v['prime_divisor'] for v in factor['gcds']], divisors)
            gc = []
            for saved in factor['gcds']:
                q = saved['prime_divisor']
                b = add(powers[n//q-1], [-v for v in x], p)
                ck(label+f'_gcd_{q}_input', saved['polynomial'], b)
                value = bezout(label+f'_gcd_{q}', h, b, saved['bezout'], p)
                gc.append(dict(index=n//q, polynomial=b,
                               left=saved['bezout']['left_multiplier'],
                               right=saved['bezout']['right_multiplier'], value=value))
            total = mul(total, h, p)
            factor_summaries.append(dict(coefficients=h, degree=n,
                                         all_frobenius_residues=powers, bezout_tests=gc))
        ck(prefix+'_product', total, f)
        ck(prefix+'_saved_product', row['reconstructed_product'], f)
        deg = [v['degree'] for v in row['factors']]
        subsets = [dict(mask=m, degree=sum(v for j, v in enumerate(deg) if m >> j & 1))
                   for m in range(1 << len(deg))]
        ck(prefix+'_all_subsets', row['all_factor_subsets'], subsets)
        ck(prefix+'_no_degree_four', all(v['degree'] != 4 for v in subsets), True)
        summaries.append(dict(prime=p, monic_reduction=f, factors=factor_summaries,
                              subset_degrees=[v['degree'] for v in subsets]))
    # Independent enumeration by squarefreeness/divisibility, not bit products.
    candidates = [s*d for d in range(1, 331) if 330 % d == 0 and
                  all(d % (q*q) != 0 for q in range(2, isqrt(d)+1))
                  for s in [-1, 1] if s*d != 1]
    candidates.sort()
    ck('all_fields', [r['d'] for r in data['quadratic_fields']], candidates)
    ck('field_count', len(candidates), 31)
    valid_primes = {r['prime'] for r in summaries}
    for row in data['quadratic_fields']:
        d, p, r = row['d'], row['prime'], row['square_root_mod_p']
        label = 'field_'+str(d)
        ck(label+'_prime_certified', p in valid_primes, True)
        ck(label+'_root_range', 0 < r < p, True)
        ck(label+'_root_equation', r*r % p, d % p)
        ck(label+'_simple_root', 2*r % p != 0, True)
        ck(label+'_saved_derivative', row['derivative_mod_p'], 2*r % p)
        ck(label+'_quartics', row['number_of_quartic_divisors'], 0)
        ck(label+'_degrees', row['complete_quadratic_factor_degrees'], [8])
    ck('Q_even_divisors', data['rational_even_divisor_degrees'], [0, 8])
    ck('partitions', data['rational_unordered_even_partitions'], ['empty/full'])
    ck('generators', data['nonzero_generators'], [])
    ck('order', data['rational_two_torsion_order'], 1)
    ck('dimension', data['rational_two_torsion_dimension'], 0)
    ck('producer_failures', data['failures'], [])
    ck('producer_checks', all(data['checks'].values()), True)
    failures = [k for k, v in checks.items() if not v['passes']]
    output = dict(source_sha256=sha256(SOURCE.read_bytes()).hexdigest(),
                  complete_modular_evidence=summaries,
                  complete_quadratic_cover=data['quadratic_fields'],
                  checks=checks, failures=failures,
                  summary=dict(checks=len(checks), passed=len(checks)-len(failures),
                               fields=len(candidates), primes=len(summaries),
                               torsion_order=1, torsion_dimension=0))
    OUT.write_text(json.dumps(output, indent=2)+'\n')
    print(f'Independent arithmetic replay: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}')
    print('Actual/required: fields 31/31; quartic divisors 0/0 in each; partition count 1/1')
    print('Replay:', OUT.relative_to(BASE.parent.parent))
    assert not failures


if __name__ == '__main__':
    main()

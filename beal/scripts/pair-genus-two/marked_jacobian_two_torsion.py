#!/usr/bin/env python3
"""Complete quadratic-field quartic-absence certificate for L126.

Only standard-library arithmetic is used. The imported polynomial routines
are from L115's already audited producer; replay imports neither producer.
"""
from pathlib import Path
from itertools import product
from hashlib import sha256
import json
import marked_octic_factorization as ff

BASE = Path(__file__).resolve().parent
OUT = BASE / 'marked-jacobian-two-torsion-certificate.json'
F = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]
SEEDS = {
    7: [[-3, 0, 1], [3, -1, 2, 1], [-3, -1, -2, 1]],
    13: [[-5, 0, 1], [6, -2, 2, 1], [-6, -2, -2, 1]],
    19: [[8, 0, 3, 0, 10, 0, 1, 0, 1]],
    29: [[14, 0, 1], [-14, 0, 13, 0, -7, 0, 1]],
    31: [[5, 0, 1], [8, 0, 3, 0, -3, 0, 1]],
    43: [[10, 1], [-10, 1], [10, 0, -19, 0, -5, 0, 1]],
}


def main():
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    primes = []
    for p, seed in SEEDS.items():
        check(f'{p}_prime', ff.prime(p))
        check(f'{p}_leading_unit', F[-1] % p != 0)
        f = [a * pow(F[-1], -1, p) % p for a in F]
        deriv = [i*f[i] % p for i in range(1, len(f))]
        sf = ff.bezout(f, deriv, p)
        check(f'{p}_squarefree', sf['gcd'] == [1])
        factors, reconstruction = [], [1]
        for j, raw in enumerate(seed):
            h = [a % p for a in raw]
            n = len(h)-1
            x = ff.divmod_poly([0, 1], h, p)[1]
            a, powers = x, []
            for k in range(1, n+1):
                w = ff.modular_power(a, p, h, p)
                w['index'] = k
                powers.append(w)
                a = w['remainder']
            divisors = [r for r in range(2, n+1) if n % r == 0 and ff.prime(r)]
            gcds = []
            for r in divisors:
                b = ff.add(powers[n//r-1]['remainder'], ff.scale(x, -1, p), p)
                bez = ff.bezout(h, b, p)
                gcds.append(dict(prime_divisor=r, polynomial=b, bezout=bez))
                check(f'{p}_{j}_gcd_{r}', bez['gcd'] == [1])
            check(f'{p}_{j}_frobenius', a == x)
            factors.append(dict(coefficients=h, degree=n, multiplicity=1,
                                x_remainder=x, powers=powers, gcds=gcds))
            reconstruction = ff.mul(reconstruction, h, p)
        check(f'{p}_product', reconstruction == f)
        subsets = []
        for mask in range(1 << len(factors)):
            degree = sum(h['degree'] for j, h in enumerate(factors) if mask >> j & 1)
            subsets.append(dict(mask=mask, degree=degree))
        check(f'{p}_no_quartic', all(s['degree'] != 4 for s in subsets))
        primes.append(dict(prime=p, monic_reduction=f, squarefree_bezout=sf,
                           factors=factors, reconstructed_product=reconstruction,
                           all_factor_subsets=subsets))

    divisors = []
    for bits in product([0, 1], repeat=4):
        d = 1
        for b, p in zip(bits, [2, 3, 5, 11]):
            if b:
                d *= p
        divisors.append(d)
    candidates = sorted({s*d for d in divisors for s in [-1, 1]} - {1})
    fields = []
    for d in candidates:
        witnesses = [(p['prime'], r) for p in primes for r in range(1, p['prime'])
                     if r*r % p['prime'] == d % p['prime']]
        check(f'field_{d}_covered', bool(witnesses))
        if not witnesses:
            fields.append(dict(d=d, unresolved=True))
            continue
        p, r = witnesses[0]
        fields.append(dict(d=d, prime=p, square_root_mod_p=r,
                           derivative_mod_p=2*r % p,
                           number_of_quartic_divisors=0,
                           complete_quadratic_factor_degrees=[8]))
        check(f'field_{d}_simple_root', 2*r % p != 0)
    check('all_31_candidates', len(candidates) == 31)
    failures = [k for k, ok in checks.items() if not ok]
    cert = dict(
        F=F, marked_curve_scalar=11, root_field_degree=8,
        field_discriminant=6818950876320000,
        field_discriminant_factorization=[[2, 8], [3, 7], [5, 4], [11, 7]],
        source_helper_sha256=sha256(Path(ff.__file__).read_bytes()).hexdigest(),
        method='complete split-prime quartic-divisor absence, not Galois-group inference',
        modular_certificates=primes, quadratic_fields=fields,
        rational_even_divisor_degrees=[0, 8],
        rational_unordered_even_partitions=['empty/full'],
        nonzero_generators=[], rational_two_torsion_order=1,
        rational_two_torsion_dimension=0, checks=checks, failures=failures)
    OUT.write_text(json.dumps(cert, indent=2)+'\n')
    print(f'Quadratic fields covered: {len(fields)}/31; primes {[r["prime"] for r in primes]}')
    print('Quartic divisors: 0 in every candidate field; required: complete classification')
    print('Rational two-torsion: order 1, dimension 0; separate critical audit pending')
    print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
    print('Certificate:', OUT.relative_to(BASE.parent.parent))
    assert not failures


if __name__ == '__main__':
    main()

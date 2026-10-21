"""Exact arithmetic for L100's single approved uniform upper certificate."""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, gcd, prod
from pathlib import Path
import json


def main():
    passed, failures = [], []

    def check(name, condition):
        (passed if condition else failures).append(name)

    Q, n, s, B = 65537, 1024, 67, 513
    D = n * Q**2
    C, error = comb(n, s), comb(B+s-1, s)
    mean = Fraction(C, D)
    cap = mean + Fraction(Q**2-1, Q**2)*error
    T = Fraction(Q**28, 2**128)
    check('strict character bound rounding', 4*Q < B**2)
    check('all powers retain nonzero unipotent characters', s < Q)
    check('constant-character orders coprime to subset size', gcd(n, s) == 1)
    check('full and restricted group index', (Q-1)*Q**2 == 64*D)
    check('nonconstant character count', D-n == n*(Q**2-1))
    check('Fourier numerator', cap == Fraction(C+n*(Q**2-1)*error, D))

    # The all-B absolute cycle sum, normalized by s!, from its coefficient
    # recurrence. Independently compare every coefficient with a binomial.
    positive = [Fraction(1)]
    principal = [Fraction(1)]
    for k in range(1, s+1):
        positive.append(sum(B*positive[k-j] for j in range(1, k+1))/k)
        principal.append(sum((-1)**(j-1)*n*principal[k-j]
                             for j in range(1, k+1))/k)
        check(f'absolute cycle coefficient {k}', positive[k] == comb(B+k-1, k))
        check(f'principal signed coefficient {k}', principal[k] == comb(n, k))
    check('complete factorial normalization', error*factorial(s) == prod(range(B, B+s)))
    row = [1] + [0]*s
    for k in range(1, n+1):
        for j in range(min(k, s), 0, -1):
            row[j] += row[j-1]
    check('independent Pascal subset count', row[s] == C)
    check('independent factorial subset count', C*factorial(s)*factorial(n-s) == factorial(n))

    # All possible nonprincipal constant-character orders, with their exact
    # cycle sums. Save full coefficient lists, including nonzero lower degrees.
    exceptional = {}
    for exponent in range(1, 11):
        d = 2**exponent
        values = [Fraction(1)]
        for k in range(1, s+1):
            values.append(sum((-1)**(j-1)*n*values[k-j]
                              for j in range(d, k+1, d))/k)
        check(f'exceptional order {d} vanishes at 67', values[s] == 0)
        check(f'exceptional order {d} complete support', all(
            value == 0 for k, value in enumerate(values) if k % d))
        exceptional[str(d)] = [str(v) for v in values]

    scale = 10**9
    ratio = cap/T
    r = ratio.numerator*scale // ratio.denominator
    check('strict threshold comparison', cap < T)
    check('strict ratio lower', Fraction(r, scale) < ratio)
    check('strict ratio upper', ratio < Fraction(r+1, scale))
    check('integer list cap', cap.numerator//cap.denominator < T)

    # Small proper subgroup: verify the actual root residues/log coordinates,
    # every constant-product fiber, and all extension exponent restrictions.
    p, z, small_n, size = 17, 3, 8, 5
    h = pow(z, 2, p)
    H = [pow(h, e, p) for e in range(small_n)]
    index = {x: e for e, x in enumerate(H)}
    check('small primitive generator', len({pow(z, e, p) for e in range(p-1)}) == p-1)
    check('small proper subgroup and minus one', len(index) == small_n and p-1 in index)
    constants = {x: 0 for x in H}
    small_records = []
    inv2 = pow(2, -1, p)
    for S in combinations(H, size):
        coeff = [1]
        for x in S:
            nxt = [0]*(len(coeff)+1)
            for j, v in enumerate(coeff):
                nxt[j] = (nxt[j]-x*v) % p
                nxt[j+1] = (nxt[j+1]+v) % p
            coeff = nxt
        c, b, a = coeff[:3]
        u = b*pow(c, -1, p) % p
        v = (a*pow(c, -1, p)-inv2*u*u) % p
        inverses = [pow(x, -1, p) for x in S]
        check('small complete logarithm identity', (
            c == -prod(S) % p and u == -sum(inverses) % p
            and v == -inv2*sum(t*t for t in inverses) % p))
        constants[c] += 1
        small_records.append({'roots': S, 'residue': [c,b,a], 'coordinates': [index[c],u,v]})
    check('small constant fibers uniform', set(constants.values()) == {comb(small_n,size)//small_n})
    # An H character indexed r extends to E* with the same r. The other
    # extensions have indices r+l*n. Check every exponent, not floating phases.
    for r_small in range(small_n):
        check(f'small extension restriction {r_small}', all(
            (2*(r_small+ell*small_n)*e) % (p-1) == (2*r_small*e) % (p-1)
            for ell in range(2) for e in range(small_n)))

    def rational(value):
        return {'numerator': value.numerator, 'denominator': value.denominator}

    result = {
        'target': 'L100 uniform upper certificate for L099 fibers',
        'fixed': {'Q': Q, 'n': n, 'subset_size': s, 'cycle_bound': B,
                  'restricted_group_size': D, 'nonconstant_character_count': D-n,
                  'subset_count': C, 'sieve_error': error,
                  'mean': rational(mean), 'uniform_cap': rational(cap),
                  'integer_cap': cap.numerator//cap.denominator,
                  'threshold': rational(T), 'cap_to_threshold': rational(ratio),
                  'ratio_interval': [r, r+1, scale],
                  'positive_threshold_margin_cross_product':
                      T.numerator*cap.denominator-cap.numerator*T.denominator},
        'absolute_cycle_coefficients': [str(v) for v in positive],
        'exceptional_cycle_coefficients': exceptional,
        'small': {'p': p, 'H': H, 'subset_size': size,
                  'constant_fiber_counts': constants, 'all_root_residues': small_records},
        'checks': len(passed)+len(failures), 'passed': passed, 'failures': failures,
        'limitations': ['Symbolic character and sieve argument is in L100; arithmetic alone is not its proof.',
                        'No arbitrary-center safety, large-domain enumeration, or boundary improvement.']}
    out = Path(__file__).with_name('order-three-pole-uniform-upper-results.json')
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(f'checks={result["checks"]}; failures={failures}')
    print(f'cap/T in ({r},{r+1})/{scale}; required <=1; passing={cap <= T}')
    print(f'integer cap={cap.numerator//cap.denominator}')
    print(f'full certificate: {out.relative_to(Path.cwd())}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

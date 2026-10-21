"""Independent exact reconstruction of L100's arithmetic certificate."""
from fractions import Fraction
from math import factorial, prod
from pathlib import Path
import json


def main():
    source = Path(__file__).with_name('order-three-pole-uniform-upper-results.json')
    saved = json.loads(source.read_text())
    passed, failures = [], []

    def check(name, condition):
        (passed if condition else failures).append(name)

    def ratio(value):
        return Fraction(value['numerator'], value['denominator'])

    q, n, s = 65537, 1024, 67
    C = prod(range(n-s+1,n+1))//factorial(s)
    error = prod(range(513,580))//factorial(s)
    cap = Fraction(C+n*(q*q-1)*error, n*q*q)
    threshold = Fraction(q**28,2**128)
    fixed = saved['fixed']
    values = {'Q':q, 'n':n, 'subset_size':s, 'cycle_bound':513,
              'restricted_group_size':n*q*q, 'nonconstant_character_count':n*(q*q-1),
              'subset_count':C, 'sieve_error':error,
              'integer_cap':cap.numerator//cap.denominator}
    for key, expected in values.items():
        check(key, fixed[key] == expected)
    for key, value in [('mean',Fraction(C,n*q*q)), ('uniform_cap',cap),
                       ('threshold',threshold), ('cap_to_threshold',cap/threshold)]:
        check(key, ratio(fixed[key]) == value)
    margin = q**28*cap.denominator-2**128*cap.numerator
    check('full margin', fixed['positive_threshold_margin_cross_product'] == margin > 0)
    lo, hi, scale = fixed['ratio_interval']
    check('reported interval', [lo,hi,scale] == [1571790,1571791,10**9])
    check('strict interval', lo*q**28*cap.denominator < scale*2**128*cap.numerator
          < hi*q**28*cap.denominator)
    check('required safety threshold', cap < threshold)
    check('sieve rounding', 4*q < 513**2)

    # Reconstruct every exceptional coefficient from the closed signed
    # generating polynomial (1-t^d)^(n/d), without the constructor's recurrence.
    for d_text, coefficients in saved['exceptional_cycle_coefficients'].items():
        d = int(d_text)
        expected = []
        for k in range(s+1):
            if k % d:
                expected.append(0)
            else:
                j = k//d
                expected.append((-1)**j*factorial(n//d)//(factorial(j)*factorial(n//d-j)))
        check(f'full exceptional polynomial {d}', [Fraction(v) for v in coefficients] == expected)
    check('all ten exceptional orders', set(saved['exceptional_cycle_coefficients']) ==
          {str(2**a) for a in range(1,11)})

    # Reconstruct every positive cycle coefficient using its product formula.
    for k, coefficient in enumerate(saved['absolute_cycle_coefficients']):
        expected = Fraction(prod(range(513,513+k)),factorial(k))
        check(f'absolute normalized coefficient {k}', Fraction(coefficient) == expected)
    check('all coefficients through 67', len(saved['absolute_cycle_coefficients']) == 68)

    # Independent elementary-symmetric reconstruction for every small residue.
    small = saved['small']
    H = set(small['H'])
    actual_sets = set()
    constant_counts = {c:0 for c in H}
    for record in small['all_root_residues']:
        roots = record['roots']
        elementary = [1]+[0]*len(roots)
        for t in roots:
            for j in range(len(roots),0,-1):
                elementary[j] = (elementary[j]+t*elementary[j-1]) % 17
        c,b,a = (-elementary[5])%17, elementary[4], (-elementary[3])%17
        check('all small ending coefficients', record['residue'] == [c,b,a])
        check('all small root subsets', len(set(roots)) == 5 and set(roots) <= H)
        actual_sets.add(tuple(sorted(roots)))
        constant_counts[c] += 1
    check('complete small subset coverage', len(actual_sets) == 56)
    check('small constant distribution', constant_counts ==
          {int(c):v for c,v in small['constant_fiber_counts'].items()})
    check('all small constant fibers', set(constant_counts.values()) == {7})
    check('constructor reports pass', saved['failures'] == [] and saved['checks'] == len(saved['passed']))
    out = source.with_name('order-three-pole-uniform-upper-verification.json')
    out.write_text(json.dumps({'checks':len(passed)+len(failures), 'passed':passed,
                              'failures':failures, 'cap':fixed['uniform_cap'],
                              'required_threshold':fixed['threshold'],
                              'ratio_interval':[lo,hi,scale], 'passing':cap < threshold},indent=2)+'\n')
    print(f'independent checks={len(passed)+len(failures)}; failures={failures}')
    print(f'cap/T in ({lo},{hi})/{scale}; required <=1; passing={cap < threshold}')
    print(f'full reconstruction: {out.relative_to(Path.cwd())}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

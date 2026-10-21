#!/usr/bin/env python3
"""Independent exact replay for L102; exact roots use the cited Hensel theorem."""
import hashlib
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'five-lifts-certificate.json'
OUT = HERE / 'five-lifts-audit-certificate.json'
raw = SOURCE.read_bytes()
stored = json.loads(raw)
checks = []


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})


def valuation(n):
    if n == 0:
        return 'infinity'
    k = 0
    while n % (5 ** (k + 1)) == 0:
        k += 1
    return k


# Expand (t^2+t+3)^5 by multinomials, independently of the generator.
qp = [0] * 11
for i in range(6):
    for j in range(6-i):
        k = 5-i-j
        qp[2*i+j] += comb(5, i)*comb(5-i, j)*3**k
complement = [0] * 12
complement[11] = 1
for degree, coefficient in enumerate(qp):
    complement[degree] += 5*coefficient
    complement[degree+1] -= coefficient
canonical_h = [1215, 1782, 2970, 2475, 2145, 1100, 594, 165, 55]
check('full complementary polynomial coefficients',
      complement == canonical_h + [0, 0, 0])

replayed = []
records = []
for name, d, c, seed, error_v in [('I', 1, 6, 1, 1),
                                  ('II', 5, 9765626, 2, 2)]:
    n = d*c
    q = (n+1)*n+3
    h = 0
    for coefficient in reversed(canonical_h):
        h = h*n+coefficient
    scale = d**11
    cube, remainder = divmod(h, scale)
    check(name+' normalization remainder zero', remainder == 0)
    error = seed**3-cube
    derivative = 3*seed**2
    ve, vd = valuation(error), valuation(derivative)
    # These implications use Clark 1.79, not a finite root approximation.
    hensel = isinstance(ve, int) and ve > 2*vd
    root_is_unit = hensel and vd == 0 and seed % 5 != 0
    predicates = [
        ('defining C', c == (5+1 if name == 'I' else 1+5**10)),
        ('full complementary identity', h == n**11-q**5*(n-5)),
        ('exact linear scale', n-5 == scale),
        ('exact integral normalization', remainder == 0 and cube == c**11-q**5),
        ('seed is cube root modulo five', error % 5 == 0),
        ('unit derivative', vd == 0),
        ('strict Hensel inequality', hensel),
        ('m,C units', valuation(c) == 0),
        ('cube root remains unit', root_is_unit and cube % 5 != 0),
        ('all fixed coordinates nonzero', c != 0 and q != 0),
        ('original equation after cube substitution', cube+q**5 == c**11),
        ('local primitive reconstruction', valuation(c) == 0),
    ]
    replayed.extend({'name': name+' '+label, 'passed': bool(value)}
                    for label, value in predicates)
    expected = {
        'system': name, 'm': 1, 'u': 1, 'C': c, 'n': n, 'Q': q, 'B': q,
        'H': h, 'scale': scale, 'integral_cube_value': cube, 'seed': seed,
        'error': error, 'error_valuation': ve, 'derivative': derivative,
        'derivative_valuation': vd,
        'required_error_valuation_strictly_above': 2*vd,
        'valuations': {'m': 0, 'u': 0, 'A': 0 if root_is_unit else None,
                       'B': valuation(q), 'C': valuation(c)},
        'cube_value_mod5': cube % 5,
        'interpretation': 'A=a is an exact Hensel root, not the integer seed; finite arithmetic supports the cited theorem application.',
    }
    check(name+' exact asserted error valuation', ve == error_v)
    check(name+' error valuation divisibility and nondivisibility',
          error % 5**error_v == 0 and error % 5**(error_v+1) != 0)
    check(name+' unit exact root implication', root_is_unit)
    records.append(expected)
    if name == 'II':
        check('II complete modulo-125 claims',
              (c % 125, q % 125, q**5 % 125, cube % 125, error % 125)
              == (1, 33, 18, 108, 25))
    else:
        check('I exact cube and mod25 claim', cube == 178268931 and cube % 25 == 6)

check('complete source records and schema match', stored['systems'] == records)
check('all source assertions exactly replayed', stored['checks'] == replayed)
check('all replayed assertions true', all(row['passed'] for row in replayed))
check('source counts and failures', stored['passed'] == stored['required'] == len(replayed) == 24
      and stored['failures'] == [])
check('complete source top-level schema',
      set(stored) == {'checks', 'passed', 'required', 'failures', 'systems'})
failures = [row['name'] for row in checks+replayed if not row['passed']]
result = {
    'source_sha256': hashlib.sha256(raw).hexdigest(),
    'method': 'Independent multinomial expansion, Horner evaluation, exact quotient/remainder and valuation divisibility; no generator import.',
    'hensel_qualification': 'A valuations follow from Clark Theorem 1.79 with unit derivative and nonzero seed residue; exact p-adic coordinates are not stored integers.',
    'complement_coefficients_ascending': complement,
    'checks': checks, 'replayed_checks': replayed, 'systems': records,
    'passed': sum(row['passed'] for row in checks+replayed),
    'required': len(checks)+len(replayed), 'failures': failures,
}
OUT.write_text(json.dumps(result, indent=2)+'\n')
print(f"Checks: {result['passed']}/{result['required']}; original assertions: {len(replayed)}; failures: {failures}")
for row in records:
    print(f"{row['system']}: actual error valuation {row['error_valuation']} > required {row['required_error_valuation_strictly_above']}; derivative valuation {row['derivative_valuation']}; normalization remainder 0")
print(f'Certificate: {OUT}')
raise SystemExit(bool(failures))

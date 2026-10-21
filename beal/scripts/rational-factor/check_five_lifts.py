#!/usr/bin/env python3
"""Exact finite evidence for the two Hensel applications in L102."""
import json
from pathlib import Path

OUT = Path(__file__).with_name('five-lifts-certificate.json')
COEFF = [55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215]

def q(m, n):
    return 3*m*m + m*n + n*n

def h(m, n):
    return sum(c*m**i*n**(8-i) for i, c in enumerate(COEFF))

def v5(n):
    if n == 0:
        return 'infinity'
    v = 0
    while n % 5 == 0:
        n //= 5
        v += 1
    return v

checks = []
records = []
def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})

for name, d, c, seed in [('I', 1, 6, 1), ('II', 5, 1+5**10, 2)]:
    m = u = 1
    n = d*c
    b = q(m, n)*u
    scale = d**11
    hv = h(m, n)
    # Integral normalization is proved by the identity, never assumed.
    cube = c**11-b**5
    error = seed**3-cube
    derivative = 3*seed**2
    check(name+' defining C', c == (5*m+u**5 if d == 1 else m+5**10*u**5))
    check(name+' full complementary identity', n**11-q(m,n)**5*(n-5*m) == m**3*hv)
    check(name+' exact linear scale', n-5*m == scale*u**5)
    check(name+' exact integral normalization', hv == scale*cube)
    check(name+' seed is cube root modulo five', error % 5 == 0)
    check(name+' unit derivative', derivative % 5 != 0)
    check(name+' strict Hensel inequality', isinstance(v5(error), int) and v5(error) > 2*v5(derivative))
    check(name+' m,C units', m % 5 != 0 and c % 5 != 0)
    check(name+' cube root remains unit', seed % 5 != 0 and cube % 5 != 0)
    check(name+' all fixed coordinates nonzero', all(x != 0 for x in (m,u,b,c)))
    check(name+' original equation after cube substitution', m**3*cube+b**5 == c**11)
    check(name+' local primitive reconstruction', c % 5 != 0)
    records.append({'system': name, 'm': m, 'u': u, 'C': c, 'n': n,
                    'Q': q(m,n), 'B': b, 'H': hv, 'scale': scale,
                    'integral_cube_value': cube, 'seed': seed,
                    'error': error, 'error_valuation': v5(error),
                    'derivative': derivative, 'derivative_valuation': v5(derivative),
                    'required_error_valuation_strictly_above': 2*v5(derivative),
                    'valuations': {'m': v5(m), 'u': v5(u), 'A': 0,
                                   'B': v5(b), 'C': v5(c)},
                    'cube_value_mod5': cube % 5,
                    'interpretation': 'A=a is an exact Hensel root, not the integer seed; finite arithmetic supports the cited theorem application.'})
failures = [c['name'] for c in checks if not c['passed']]
OUT.write_text(json.dumps({'checks': checks, 'passed': len(checks)-len(failures),
                           'required': len(checks), 'failures': failures,
                           'systems': records}, indent=2)+'\n')
print(f'Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}')
for r in records:
    print(f"{r['system']}: v5(error)={r['error_valuation']} > required {r['required_error_valuation_strictly_above']}; v5(derivative)={r['derivative_valuation']}; cube mod5={r['cube_value_mod5']}; valuations={r['valuations']}")
print(f'Certificate: {OUT}')
raise SystemExit(bool(failures))

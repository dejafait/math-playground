#!/usr/bin/env python3
"""Independent rational-budget audit plus preserved full replay of2068."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
from unittest.mock import patch
import hashlib
import json
import runpy

ROOT = Path(__file__).resolve().parent
ORIGINAL = ROOT / 'direct-theta-coefficients-2068.json'
GENERATOR = ROOT / 'direct_theta_coefficients_2068.py'
REPLAY = ROOT / 'direct-theta-coefficients-replay-2070.json'
OUTPUT = ROOT / 'direct-theta-audit-2070.json'
saved_bytes = ORIGINAL.read_bytes()
old = json.loads(saved_bytes)
checks, failures = [], []


def check(name, condition):
    checks.append(dict(name=name, passed=bool(condition)))
    if not condition:
        failures.append(name)


def bounds(obj):
    return F(obj['lower']), F(obj['upper'])


def rising(a, r):
    ans = F(1)
    for i in range(r):
        ans *= a+i
    return ans


# Reconstruct g derivatives from polynomial monomials and falling
# factorials, instead of the generator's three-term expression.
G = []
for r in range(5):
    total = F(0)
    for n in range(1, 5):
        A = F(22*n*n, 7)
        for power, coefficient in [(2, 2*A*A), (1, 3*A)]:
            for s in range(min(power, r)+1):
                total += (F(comb(r, s))*coefficient
                          * F(factorial(power), factorial(power-s))
                          * A**(r-s) / 20**(n*n))
    G.append(total)
V = [rising(F(3, 2), r)/2**(r+1) for r in range(5)]
BN = F(160*25, 20**25)
BX = F(240, 20**16)*(F(16**2, 3)+F(32, 9)+F(2, 27))
check('saved common derivative/tail vectors', old['analytic_common'] == dict(
    G=list(map(str, G)), V=list(map(str, V)),
    theta_index_error=str(BN), spatial_error=str(BX)))
check('index geometric ratio < 1/2', F(36, 25*20**11) < F(1, 2))
check('spatial geometric ratio < 1/2', F(16, 20**48) < F(1, 2))
check('index integrated polynomial constant < 80',
      120*(F(1, 3)+F(2, 9)+F(2, 27)) < 80)
check('exponential series lower bound > 20',
      sum((F(3)**r/factorial(r) for r in range(9)), F(0)) > 20)
check('normalization squared < 36', 32 < 36)
check('12 pi upper squared < 120', 12*F(22, 7)**2 < 120)

# Independently sum multinomial Leibniz partitions over k copies of u
# and one v, instead of iterated convolution. All degrees here <=4.
audited_rows = []
for j, row in enumerate(old['coefficients']):
    k = 2*j
    W = []
    for r in range(5):
        total = F(0)
        for degrees in product(range(r+1), repeat=k):
            used = sum(degrees)
            if used <= r:
                rv = r-used
                term = F(factorial(r), factorial(rv))*V[rv]
                for s in degrees:
                    term *= F(1, 2**s)
                total += term
        W.append(total)
    M = sum((6*comb(4, r)*G[r]*W[4-r] for r in range(5)), F(0))
    E = F(15**5, 180*2**72)*M
    ql, qu = bounds(row['quadrature'])
    lower, upper = bounds(row['enclosure'])
    check(f'c{k} independent multinomial W', list(map(str, W)) == row['weight_derivative_bounds'])
    check(f'c{k} independent M and E', F(row['fourth_derivative_bound']) == M and F(row['simpson_error']) == E)
    check(f'c{k} two tail errors', F(row['theta_index_error']) == BN and F(row['spatial_error']) == BX)
    check(f'c{k} arithmetic width', qu-ql == F(row['arithmetic_and_constants_width']))
    check(f'c{k} final outward error application', lower <= ql-E and upper >= qu+E+BN+BX)
    check(f'c{k} width and positive endpoints', 0 < lower < upper and upper-lower == F(row['width']) and upper-lower <= F(1, 2**40))
    check(f'c{k} saved pass booleans', row['coefficient'] == f'c{k}' and row['positive_finite'] is True and row['passed'] is True)
    audited_rows.append(dict(coefficient=f'c{k}', M=str(M), E=str(E),
                             actual_width=str(upper-lower), required_width=str(F(1, 2**40))))

# Recompute Machin endpoints by grouping adjacent positive/negative
# series terms; the odd 239 sum is the upper alternating bound.
def grouped_atan(q, pairs):
    return sum((F(1, (4*i+1)*q**(4*i+1))
                - F(1, (4*i+3)*q**(4*i+3)) for i in range(pairs)), F(0))


a5lo = grouped_atan(5, 40)
a5hi = a5lo+F(1, 161*5**161)
a239hi = grouped_atan(239, 12)+F(1, 49*239**49)
a239lo = a239hi-F(1, 51*239**51)
pl, pu = 16*a5lo-4*a239hi, 16*a5hi-4*a239lo
check('exact Machin rational endpoints', list(map(str, (pl, pu))) == old['constants']['pi_exact_machin_bounds'])
dl, du = bounds(old['constants']['pi'])
check('pi directed conversion and comparisons', 3 < dl <= pl < pu <= du < F(22, 7))
sl, su = bounds(old['constants']['sqrt2'])
check('sqrt2 exact square enclosure', 0 < sl and sl*sl <= 2 <= su*su)
check('parameters and required width', old['parameters'] == dict(X=16, N=4, panels=2**18, digits=60) and F(old['required_width']) == F(1, 2**40))
check('saved script hash', old['script_sha256'] == hashlib.sha256(GENERATOR.read_bytes()).hexdigest())
check('saved status and failures', old['status'] == 'PASS' and old['failures'] == [])

# Execute the unchanged generator; intercept just its certificate write
# so that the original evidence remains byte-for-byte preserved.
write_text = Path.write_text


def redirected_write(path, data, *args, **kwargs):
    if path.resolve() == ORIGINAL:
        return write_text(REPLAY, data, *args, **kwargs)
    return write_text(path, data, *args, **kwargs)


print('Independent rational-budget checks complete; starting full replay.', flush=True)
try:
    with patch.object(Path, 'write_text', redirected_write):
        runpy.run_path(str(GENERATOR), run_name='__main__')
except BaseException as exc:
    failures.append('Replay exception: '+repr(exc))
else:
    replay = json.loads(REPLAY.read_text())
    check('all certificate fields except runtime replay identically',
          {k: v for k, v in old.items() if k != 'runtime'} ==
          {k: v for k, v in replay.items() if k != 'runtime'})
    for label, cert in [('original', old), ('replay', replay)]:
        runtime = cert['runtime']
        check(label+' complete node/sqrt/operation counts', runtime['counts'] == dict(
            basic=23855249, exp=2097168, sqrt=262146,
            sqrt_square_checks=524292, nodes=262145))
        check(label+' no unexpected Decimal signals', runtime['unexpected_signals'] == [] and
              all({name for name, flag in flags.items() if flag} == {'Inexact', 'Rounded'}
                  for flags in runtime['flags'].values()))
        check(label+' all contexts and traps', all(
            'prec=60' in runtime['contexts'][name] and rounding in runtime['contexts'][name]
            and 'Emin=-999999, Emax=999999' in runtime['contexts'][name]
            and 'traps=[Clamped, InvalidOperation, DivisionByZero, FloatOperation, Overflow, Subnormal, Underflow]'
            in runtime['contexts'][name]
            for name, rounding in [('lo', 'ROUND_FLOOR'), ('hi', 'ROUND_CEILING'), ('near', 'ROUND_HALF_EVEN')]))
check('original certificate preserved byte-for-byte', ORIGINAL.read_bytes() == saved_bytes)
result = dict(status='FAIL' if failures else 'PASS', checks=checks,
              failures=failures, coefficients=audited_rows,
              original=str(ORIGINAL.name), replay=str(REPLAY.name),
              original_sha256=hashlib.sha256(saved_bytes).hexdigest(),
              audit_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              trust='Correct CPython integers/Fraction and libmpdec directed basics/correctly rounded exp; replay is not a backend proof.')
OUTPUT.write_text(json.dumps(result, indent=2)+'\n')
print(f'Audit: {result["status"]}; {len(checks)} checks; failures={failures}', flush=True)
for row in audited_rows:
    print(row['coefficient'], 'actual width', float(F(row['actual_width'])),
          'required <=', float(F(row['required_width'])), flush=True)
print('Audit evidence:', OUTPUT, flush=True)
print('Preserved replay:', REPLAY, flush=True)
if failures:
    raise SystemExit(1)

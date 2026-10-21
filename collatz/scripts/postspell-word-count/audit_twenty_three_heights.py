#!/usr/bin/env python3
"""Audit all L052 certificate data and independently enclose its logarithms.

No imports from the generator. Independent bounds sum 144 exact unrounded
terms and use the argument-specific integrated-geometric remainder.
"""
from fractions import Fraction as Q
from pathlib import Path
from tempfile import TemporaryDirectory
from math import factorial
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'twenty-three-height-certificate.json'
raw = SOURCE.read_bytes()
saved = json.loads(raw)
checks = []
rounding_evidence = {}


def verify(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=actual,
                       required=required))


def equal(name, actual, required):
    verify(name, actual == required, actual, required)


def less(name, actual, required):
    verify(name, actual < required, actual, required)


def audit_base(label, t, detail):
    x = (t-1)/(t+1)
    equal(label + ' detail schema', sorted(detail),
          sorted(['x', 'rounded_summands', 'rounding_budget', 'remainder_upper']))
    equal(label + ' x', Q(detail['x']), x)
    verify(label + ' domain', 0 <= x <= Q(1, 3), x, '[0,1/3]')
    equal(label + ' term count', len(detail['rounded_summands']), 96)
    term = 2*x
    rows = []
    for j, rounded in enumerate(detail['rounded_summands']):
        scaled = term*2**192
        passed = type(rounded) is int and rounded <= scaled < rounded+1
        verify(f'{label} floor {j}', passed, scaled, [rounded, rounded+1])
        rows.append(dict(index=j, exact_term=term, rounded=rounded))
        term *= x*x*Q(2*j+1, 2*j+3)
    remainder = Q(9, 4*193*3**193)
    equal(label + ' rounding budget', Q(detail['rounding_budget']), Q(96, 2**192))
    equal(label + ' remainder', Q(detail['remainder_upper']), remainder)
    lo = Q(sum(detail['rounded_summands']), 2**192)
    rounding_evidence[label] = rows
    return lo, lo+Q(96, 2**192)+remainder


equal('precision', [saved['precision']['bits'], saved['precision']['terms']], [192, 96])
ell0, ell1 = audit_base('base log2', Q(2), saved['precision']['log2_detail'])
equal('all log arguments', sorted(saved['logs']), sorted(['2', '3', '11/4', '3600000000']))
original_logs = {}
for key, row in saved['logs'].items():
    t = Q(key)
    k = 0
    while 2**(k+1) <= t:
        k += 1
    v = t / 2**k
    equal(key + ' argument', Q(row['argument']), t)
    equal(key + ' exponent', row['binary_exponent'], k)
    equal(key + ' reduction', Q(row['reduced_argument']), v)
    lo, hi = audit_base(key, v, row['detail'])
    lo, hi = lo+k*ell0, hi+k*ell1
    equal(key + ' lower', Q(row['lower']), lo)
    equal(key + ' upper', Q(row['upper']), hi)
    original_logs[key] = (lo, hi)


def exact_series(v):
    x = (v-1)/(v+1)
    assert 0 <= x <= Q(1, 3)
    term = 2*x
    total = Q(0)
    terms = []
    for j in range(144):
        total += term
        terms.append(term)
        term *= x*x*Q(2*j+1, 2*j+3)
    error = 2*x**289/(289*(1-x*x))
    return total, total+error, dict(x=x, exact_terms=terms, error=error)


e0, e1, ed = exact_series(Q(2))
independent = {}
independent_logs = {}
for key in saved['logs']:
    t, k = Q(key), 0
    while t >= 2:
        t /= 2
        k += 1
    lo, hi, detail = exact_series(t)
    lo, hi = lo+k*e0, hi+k*e1
    independent_logs[key] = (lo, hi)
    independent[key] = dict(exponent=k, reduced=t, lower=lo, upper=hi, detail=detail)
    a, b = original_logs[key]
    verify(key + ' independent containment', a <= lo <= hi < b,
           [lo, hi], [a, b])


rho, beta, count = Q(189, 100), Q(31, 100), Q(14, 5)
R = (rho**23-1)/(rho-1)
equal('geometric identity', R, sum((rho**j for j in range(23)), Q(0)))
A = Q(8, 5)*count*2600000*Q(133, 10)
B = Q(8, 5)*count*2600000*13+2
M, p, q = 3600000000, 9809721694, 6189245291
D = Q(1587*q+23, 11)
K_upper = count*2600000*29
l2, u2 = original_logs['2']
l3, u3 = original_logs['3']
expected_operands = dict(rho=str(rho), beta=str(beta), count=str(count), R=str(R),
                        R_upper='2600000', A=str(A), B=str(B), M=M, p=p, q=q,
                        epsilon_lower=str(q*l3-p*u2), epsilon_upper=str(q*u3-p*l2),
                        D=str(D), K_upper=str(K_upper), K_required='225640000')
equal('all saved operands', saved['operands'], expected_operands)


def numerical_claims(bounds):
    lo2, hi2 = bounds['2']
    lo3, hi3 = bounds['3']
    du, el, cu = Q(793, 500), Q(6931, 10000), Q(41, 40)
    eps0, eps1 = q*lo3-p*hi2, q*hi3-p*lo2
    return [
        ('log2 lower', el, lo2),
        ('log3 upper', hi3, Q(10987, 10000)),
        ('c upper', bounds['11/4'][1], cu),
        ('delta upper', Q(10987, 6931), du),
        ('transfer coefficient', 3*du**2/4, rho),
        ('transfer additive', du*(3*du-4)*cu/4, beta),
        ('shifted transfer', beta+1, rho),
        ('odd-count coefficient', 3*(du+1)/(4*el), count),
        ('odd-count additive', (3*du-1)*cu/(4*el), Q(7, 5)),
        ('geometric sum', R, Q(2600000)),
        ('log23 via exponential lower bound', Q(23), Q(27, 10)**4),
        ('length additive constant', Q(1587, 1034), Q(2)),
        ('logM upper', bounds[str(M)][1], Q(111, 5)),
        ('whole-ray derivative guard', A, Q(M)),
        ('whole-ray value guard', A*Q(111, 5)+B, Q(M)),
        ('epsilon positive', Q(0), eps0),
        ('epsilon compact upper', eps1, Q(958, 10**13)),
        ('compact half-log comparison', 2*M*Q(958, 10**13), el),
        ('same-pair half-log guard', 2*M*eps1, lo2),
        ('log2 exceeds 2/3', Q(2, 3), lo2),
        ('minimum-height exponential comparison', D, Q(27, 10)**28),
        ('odd-count contradiction', K_upper, Q(225640000)),
    ]


expected_checks = []
for name, actual, required in numerical_claims(original_logs):
    expected_checks.append(dict(name=name, actual=str(actual), relation='<',
                                required=str(required), margin=str(required-actual),
                                passed=actual < required))
    less('recomputed ' + name, actual, required)
equal('complete saved check rows', saved['checks'], expected_checks)
equal('complete saved failure list', saved['failures'],
      [c['name'] for c in expected_checks if not c['passed']])
for name, actual, required in numerical_claims(independent_logs):
    less('independent ' + name, actual, required)

equal('stated count slope', Q(19395, 6931), 3*(Q(793, 500)+1)/(4*Q(6931, 10000)))
equal('stated count intercept', Q(77039, 55448), (3*Q(793, 500)-1)*Q(41, 40)/(4*Q(6931, 10000)))
equal('stated transfer slope', Q(1886547, 1000000), 3*Q(793, 500)**2/4)
equal('stated transfer intercept', Q(12322427, 40000000), Q(793, 500)*(3*Q(793, 500)-4)*Q(41, 40)/4)
equal('stated A', A, Q(154918400))
equal('stated B', B, Q(151424002))
equal('stated whole-ray margin', M-A*Q(111, 5)-B, Q(9387518))
equal('stated compact half-log operand', 2*M*Q(958, 10**13), Q(4311, 6250))
equal('stated D', D, Q(9822332276840, 11))
equal('stated K ceiling', K_upper, Q(211120000))
equal('exponential partial sum', sum((Q(1, factorial(j)) for j in range(6)), Q(0)), Q(163, 60))
less('e partial sum exceeds 27/10', Q(27, 10), Q(163, 60))
less('delta lower via integer powers', 2**3, 3**2)
less('positive alpha via integer powers', 16, 27)
less('shift domination', Q(23, 11), Q(3, 4)*Q(540, 11))

with TemporaryDirectory(prefix='collatz-l052-audit-') as tmp:
    generator = Path(tmp)/'certify_twenty_three_heights.py'
    shutil.copyfile(ROOT/generator.name, generator)
    replay = subprocess.run([sys.executable, str(generator)], capture_output=True, text=True)
    equal('generator exit', replay.returncode, 0)
    regenerated = (Path(tmp)/SOURCE.name).read_bytes()
    equal('byte-for-byte regeneration', hashlib.sha256(regenerated).hexdigest(),
          hashlib.sha256(raw).hexdigest())

failures = [c['name'] for c in checks if not c['passed']]
result = dict(target='Critical audit of L052 at r=23 only',
              source_sha256=hashlib.sha256(raw).hexdigest(),
              rounding_evidence=rounding_evidence,
              independent_log2=dict(lower=e0, upper=e1, detail=ed),
              independent_logs=independent, operands=expected_operands,
              checks=checks, failures=failures)
output = ROOT/'twenty-three-height-audit-certificate.json'
output.write_text(json.dumps(result, default=str, indent=2)+'\n')
print(f'Audit checks: {len(checks)}; failures: {failures}')
print(f'Rounded summands checked: {sum(len(v) for v in rounding_evidence.values())}; logarithm arguments: {len(independent)}')
print(f'N ceiling: {M}; whole-ray margin: {M-A*Q(111, 5)-B}')
print(f'K upper: {K_upper}; required lower: >225640000; gap: {225640000-K_upper}')
print(f'Original SHA-256: {result["source_sha256"]}')
print(f'Certificate: {output}')
if failures:
    raise SystemExit(1)

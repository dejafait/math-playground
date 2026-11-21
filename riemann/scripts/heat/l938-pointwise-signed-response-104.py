#!/usr/bin/env python3
"""One fixed E=8 endpoint test; preserves every prior producer/artifact.

Reuses audited C948a maxima/majorants, not its integrated allowances.
Original theta, signed-prefix and full-polynomial execution contracts persist.
"""
import hashlib
import json
import sys
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import factorial, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l938-pointwise-signed-response-104.json'
report = dict(status='IN_PROGRESS', checks=[], failures=[], inputs_sha256={},
              qualification='Inherited theta inclusion, signed derivative-prefix, '
              'full polynomial and Python arithmetic contracts; no original producer rerun.')


def save():
    OUT.write_text(json.dumps(report, indent=2) + '\n')


def check(name, ok):
    report['checks'].append(dict(name=name, passed=bool(ok)))
    if not ok:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw = (BASE / name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def shown(value):
    with localcontext() as ctx:
        ctx.prec = 16
        ctx.rounding = ROUND_FLOOR
        lo = str(Decimal(value.numerator) / Decimal(value.denominator))
        ctx.rounding = ROUND_CEILING
        hi = str(Decimal(value.numerator) / Decimal(value.denominator))
    check('directed display ' + str(len(report['checks'])), F(lo) <= value <= F(hi))
    return dict(lower=lo, upper=hi)


save()
claim = read('l938-signed-response-complete-90.json')
audit = read('c948a-complete-budget-audit-92.json')
kernel = read('actual-h2-energy-cell-48.json')
poly = read('actual-h2-energy-cell-polynomial-48.json')
poly_audit = read('actual-h2-energy-cell-audit-50.json')
compact = read('l938-compact-bernstein-enclosures-94.json')
compact_report = read('l938-compact-negative-mass-94.json')
compact_check = read('l938-compact-negative-mass-check-94.json')
for name, obj in [('audit92', audit), ('audit50', poly_audit),
                  ('compact producer94', compact_report), ('compact verifier94', compact_check)]:
    check(name + ' inherited complete flags', not obj['failures']
          and len(obj['checks']) > 0 and all(c['passed'] is True for c in obj['checks']))
for name, obj in [('l938-signed-response-complete-90.json', audit),
                  ('actual-h2-energy-cell-48.json', audit),
                  ('actual-h2-energy-cell-48.json', poly_audit),
                  ('actual-h2-energy-cell-polynomial-48.json', poly_audit)]:
    check('input identity ' + name + str(len(report['checks'])),
          report['inputs_sha256'][name] == obj['inputs_sha256'][name])
check('complete compact identity', compact_report['coefficient_sha256']
      == report['inputs_sha256']['l938-compact-bernstein-enclosures-94.json'])
ap = kernel['approximation']
G, D, J, L, E, N = 10**120, 2816, 1411, 1412, 8, 3089
check('fixed kernel and response scope', (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision'])
      == (256, 257, 8, 200) and int(ap['chebyshev_denominator']) == G
      and L == J+1 <= D and compact['degree'] == N and int(compact['grid']) == G)
epsilon = 8*10**9*F(2, 3)**256 + sum((F(c['absolute_error'])
              for c in ap['chebyshev_coefficients']), F(0))
check('full epsilon', epsilon == F(ap['epsilon']) and 0 < epsilon < F('6.664e-36'))
C = 2*factorial(12)*int(ap['power_denominator'])*4**262
R = list(map(int, poly['numerators']))
den = int(poly['denominator'])
check('complete density normalization', len(R) == 3073 and R[-1] != 0
      and den == C**12 and N == 17+len(R)-1)

# Existing exact audited prefix maxima, in their original complete basis.
M = list(map(F, claim['prefix']['maxima']))
check('all seven maxima', len(M) == 7 and all(v > 0 for v in M)
      and [F(row['maximum']) for row in audit['replay_rows']] == M)
beta = []
for k in range(7):
    b = F(factorial(34-2*k)*factorial(2*k),
          4**17*factorial(17-k)*factorial(k)*factorial(17))
    odd = F(prod(range(1, 2*(17-k), 2))*prod(range(1, 2*k, 2)),
            2**17*factorial(17))
    check('positive beta factorial/odd normalization '+str(k), b == odd
          == F(claim['prefix']['beta_masses_over_pi'][k]) and b > 0)
    beta.append(b)
prefix_norm = E**17*sum((m*b for m, b in zip(M, beta)), F(0))

# Every remaining degree is bounded before any energy integration.
rho = F(1, 32)
V = list(map(F, claim['tail']['derivative_majorants']))
check('unchanged complete majorants', len(V) == 7 and all(v > 0 for v in V)
      and rho == F(claim['tail']['r']) and claim['tail']['first_degree'] == L)
q = F(E, 1)/rho/(L+18)
check('pointwise ratio differs from integrated ratio', q == F(256, 1430)
      and 0 < q < 1 and q != F(claim['tail']['geometric_ratio']))
weights = sum((v/F(2*4**k*factorial(k)) for k, v in enumerate(V)), F(0))
tail_norm = F(E**17*256**L, factorial(L+17))/(1-q)*weights
# Independent first-term ratio check; monotonic denominator proves all later cases.
first_term = F(256**L, factorial(L+17))
next_term = F(256**(L+1), factorial(L+18))
check('exact factorial ratio', next_term/first_term == q
      and F(256, D+18) <= q and first_term > 0)
check('pointwise complement positive', tail_norm > 0)

pi_lo, pi_hi = F(ap['pi']['lower']), F(ap['pi']['upper'])
check('positive inherited pi enclosure', 3 < pi_lo <= pi_hi < 4)
Z = F(293, 540*2**36*factorial(17))
linear = epsilon*pi_hi**6*(prefix_norm+tail_norm)
second = 66*epsilon**2*8**10*pi_hi**6*Z*E**17
error = linear + second
check('complete pointwise Taylor payment', 0 < second < linear < error)

# All3073 signed terms, one exact factorial denominator, no truncation.
facN = factorial(N)
numerator = 0
for l, value in enumerate(R):
    s = l+17
    quotient, remainder = divmod(facN, factorial(s))
    check('full endpoint factorial division '+str(l), remainder == 0)
    numerator += value*E**s*quotient
center = F(numerator, den*facN)  # v_p(8)/pi^6
lo, hi = map(int, compact['global_bernstein'][-1])
check('full Bernstein closed endpoint consistency', F(lo, G) <= center <= F(hi, G)
      and compact['normalized'] == 'v_p(8x)/pi^6')
check('positive polynomial endpoint only', center > 0)
vp_lo, vp_hi = pi_lo**6*center, pi_hi**6*center
actual_lo, actual_hi = vp_lo-error, vp_hi+error
required = vp_lo  # strict sufficient threshold for this symmetric sign test
outcome = ('POSITIVE' if actual_lo > 0 else
           'NEGATIVE' if actual_hi < 0 else 'INCONCLUSIVE')
check('complete ordered enclosure', actual_lo <= actual_hi and 0 < required)
report['exact'] = {k: str(v) for k, v in dict(
    epsilon=epsilon, rho=rho, geometric_ratio=q, prefix_norm=prefix_norm,
    complement_norm=tail_norm, first_order_upper=linear,
    second_order_upper=second, total_error_upper=error,
    normalized_polynomial_endpoint=center, polynomial_endpoint_lower=vp_lo,
    polynomial_endpoint_upper=vp_hi, actual_endpoint_lower=actual_lo,
    actual_endpoint_upper=actual_hi, required_strict_error_upper=required,
    error_to_required_ratio=error/required).items()}
report['summary'] = {k: shown(v) for k, v in dict(
    prefix_norm=prefix_norm, complement_norm=tail_norm, first_order_upper=linear,
    second_order_upper=second, total_error_upper=error,
    polynomial_endpoint_lower=vp_lo, polynomial_endpoint_upper=vp_hi,
    actual_endpoint_lower=actual_lo, actual_endpoint_upper=actual_hi,
    required_strict_error_upper=required, error_to_required_ratio=error/required).items()}
report['test'] = dict(energy=E, prefix_degree=J, response_degree=D,
    density_degree=N, sign=outcome, sufficient_positive_test=error < required,
    mathematical_failures=[] if outcome != 'INCONCLUSIVE' else
    ['Complete symmetric endpoint enclosure contains zero; fixed test ends.'])
report['status'] = 'COMPLETED_CONDITIONAL_' + outcome
save()
print(json.dumps(dict(status=report['status'], checks=len(report['checks']),
    failures=report['failures'], bounds=report['summary'], test=report['test'],
    certificate=str(OUT)), indent=2))

#!/usr/bin/env python3
"""Fixed b=1/10, E=1/4,4, exponential degree32; see canonical L947.

Exact integer factorial-basis multiplication and rational integration.
Inherited theta/polynomial audit is reused, never regenerated or refined.
"""
import hashlib
import json
import re
import sys
from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING, localcontext
from fractions import Fraction as F
from math import comb, factorial, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l938-tilted-endpoints-81.json'
report = {'status': 'IN_PROGRESS', 'checks': [], 'failures': [],
          'inputs_sha256': {}, 'scope': 'b=1/10; E=1/4,4; exp degree32; unchanged L938',
          'python': sys.version}


def save():
    OUT.write_text(json.dumps(report, indent=2) + '\n')


def check(name, passed):
    report['checks'].append({'name': name, 'passed': bool(passed)})
    if not passed:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw = (BASE / name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def outward(value, rounding):
    with localcontext() as context:
        context.prec = 16
        context.rounding = rounding
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def bounds(lo, hi):
    dl, dh = outward(lo, ROUND_FLOOR), outward(hi, ROUND_CEILING)
    check('outward conversion ' + str(len(report['checks'])), F(dl) <= lo <= hi <= F(dh))
    return {'lower': dl, 'upper': dh}


save()
data = read('actual-h2-energy-cell-48.json')
poly = read('actual-h2-energy-cell-polynomial-48.json')
audit = read('actual-h2-energy-cell-audit-50.json')
audit75 = read('l944-c944a-audit-75.json')
for name, expected in audit['inputs_sha256'].items():
    digest = hashlib.sha256((BASE/name).read_bytes()).hexdigest()
    report['inputs_sha256'][name] = digest
    check('step50 audited hash ' + name, digest == expected)
for name, source, count in [('step50', audit, 5101), ('step75', audit75, 15620)]:
    check(name + ' state/count/no failures', source['status'] == 'PASSED'
          and len(source['checks']) == count and source['failures'] == [])
    # Inspect every saved check, not a preview or a summary.
    for i, entry in enumerate(source['checks']):
        check(name + ' check ' + str(i), entry['passed'] is True)
for name in ['actual-h2-energy-cell-48.json', 'actual-h2-energy-cell-polynomial-48.json']:
    check('step75 inherited hash ' + name,
          audit75['inputs_sha256'][name] == report['inputs_sha256'][name])
identity = audit['integer_identity']
check('inherited exact polynomial identity', identity['residual'] == '0'
      and identity['difference_bound_lt_half_base'] is True and identity['degree'] == 3072)

ap = data['approximation']
check('unchanged budget', (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision'])
      == (256, 257, 8, 200))
check('unchanged rational grid', int(ap['chebyshev_denominator']) == 10**120
      and int(ap['power_denominator']) == 10**120 * 4**256)
check('all257 coefficient records', len(ap['chebyshev_coefficients']) == 257)
etas = []
for ell, row in enumerate(ap['chebyshev_coefficients']):
    chosen = F(int(row['chosen_numerator']), 10**120)
    lo, hi = F(row['enclosure']['lower']), F(row['enclosure']['upper'])
    eta = max(abs(chosen-lo), abs(chosen-hi))
    check('complete coefficient radius ' + str(ell), row['k'] == ell and lo <= hi
          and eta == F(row['absolute_error']))
    etas.append(eta)
epsilon = 8*10**9*F(2, 3)**256 + sum(etas, F(0))
check('complete kernel error', sum(etas, F(0)) == F(ap['coefficient_error_sum'])
      and epsilon == F(ap['epsilon']) and 0 < epsilon < F(1, 10**34))

rows = data['algebra']['terms']
lemma = (BASE.parent.parent / 'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md').read_text()
table = [(int(c), tuple(map(int, exponents.split(','))))
         for c, exponents in re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([0-9,]+)\)\s*\|$', lemma, re.M)]
check('all34 canonical rows', len(table) == len(rows) == 34)
weights = []
for i, row in enumerate(rows):
    alpha = row['exponents_A0_to_A6']
    coefficient = row['coefficient']
    check('complete row ' + str(i), table[i] == (coefficient, tuple(alpha))
          and len(alpha) == 7 and all(isinstance(a, int) and a >= 0 for a in alpha)
          and sum(alpha) == 12 and sum(k*a for k, a in enumerate(alpha)) == 12)
    weight = F(abs(coefficient), prod(factorial(k)**a for k, a in enumerate(alpha)))
    direct_beta = F(abs(coefficient), 2**12 * factorial(17))
    for k, a in enumerate(alpha):
        direct_beta *= F(1, 4**k * factorial(k))**a
    check('complete beta weight ' + str(i), direct_beta == weight / (2**36 * factorial(17)))
    weights.append(weight)
W = sum(weights, F(0))
check('absolute row weight', W == F(293, 540))
Z = W / (2**36 * factorial(17))

rr = list(map(int, poly['numerators']))
den = int(poly['denominator'])
check('all3073 convolution coefficients and denominator', len(rr) == 3073
      and den == (2*factorial(12)*int(ap['power_denominator'])*4**262)**12)
max_saved = max(map(abs, rr))
check('complete inherited coefficient bound', max_saved == int(identity['saved_max_abs_coefficient'])
      and int(identity['actual_polynomial_coefficient_bound']) + max_saved
      < 2**(identity['base_power_of_two']-1))

# exp(2/5) is bounded by its positive degree32 sum and a geometric tail.
x = F(2, 5)
exp_sum = sum((x**j/factorial(j) for j in range(33)), F(0))
exp_tail = x**33 / factorial(33) / (1-x/34)
exp_upper = F(3, 2)
check('full exponential upper bound', exp_sum + exp_tail < exp_upper)
report['constants'] = {k: str(v) for k, v in
    {'epsilon': epsilon, 'W': W, 'Z': Z, 'factor_bound': F(8),
     'exp_upper': exp_upper, 'exp_series_sum': exp_sum, 'exp_tail_bound': exp_tail}.items()}
report['inherited_identity_scope'] = ('Reused step50 zero residual and proof; all saved coefficients '
    'loaded, hashes/full audit flags/coefficient bound checked; no theta or large-product replay.')
save()
print('Inputs and full audit records checked; exact degree3104 Taylor product begins.', flush=True)

# T32(t)*v_p(t)/pi^6 = sum S_m t^(17+m)/(17+m)! /(den*10^32).
degree = len(rr)-1+32
ss = []
for m in range(degree+1):
    ss.append(sum(rr[m-j] * comb(17+m, j) * 10**(32-j)
                  for j in range(max(0, m-(len(rr)-1)), min(32, m)+1)))
check('exact product edge coefficients', ss[0] == rr[0]*10**32
      and ss[-1] == rr[-1]*comb(17+degree, 32))
report['product'] = {'degree': degree, 'factorial_offset': 17,
                     'denominator': str(den*10**32), 'numerators': list(map(str, ss))}
save()


def exact_integral(E):
    # Descending homogeneous Horner; no rounding or quadrature.
    qpower, quotient, acc = 1, 1, 0
    for m in range(degree, -1, -1):
        acc = E.numerator*acc + ss[m]*quotient*qpower
        quotient *= 18+m
        qpower *= E.denominator
    return F(acc * E.numerator**18,
             den * 10**32 * factorial(18+degree) * E.denominator**(18+degree))


def direct_integral(E):
    # Independent forward monomial accumulation checks the homogeneous Horner.
    top = factorial(18+degree)
    running_factorial = factorial(18)
    ppower, qpower, total = E.numerator**18, E.denominator**degree, 0
    for m, coefficient in enumerate(ss):
        quotient, remainder = divmod(top, running_factorial)
        check('direct factorial division ' + str(E) + ',' + str(m), remainder == 0)
        total += coefficient * quotient * ppower * qpower
        running_factorial *= 19+m
        ppower *= E.numerator
        qpower //= E.denominator
    return F(total, den * 10**32 * top * E.denominator**(18+degree))


pi_lo, pi_hi = F(ap['pi']['lower']), F(ap['pi']['upper'])
check('ordered inherited positive pi enclosure', 3 < pi_lo <= pi_hi < 4)
report['pi_enclosure'] = {'lower': str(pi_lo), 'upper': str(pi_hi)}
report['endpoints'] = {}
summary = {}
for E in [F(1, 4), F(4)]:
    center = exact_integral(E)
    check('independent exact center ' + str(E), direct_integral(E) == center)
    beta_mass = Z * E**18 / 18
    kernel_error = exp_upper * 12 * epsilon * 8**11 * beta_mass
    taylor_sup_error = exp_upper * (E/10)**33 / factorial(33)
    absolute_vp_mass = 8**12 * beta_mass
    taylor_error = taylor_sup_error * absolute_vp_mass
    radius = kernel_error + taylor_error
    lower, upper = center-radius, center+radius
    # Multiply the whole interval by positive pi^6, accounting for both signs.
    corners = [bound*pi_endpoint**6 for bound in [lower, upper]
               for pi_endpoint in [pi_lo, pi_hi]]
    actual_lo, actual_hi = min(corners), max(corners)
    sign = 'NEGATIVE' if upper < 0 else 'POSITIVE' if lower > 0 else 'UNRESOLVED'
    key = str(E)
    exact = {'center_over_pi6': center, 'kernel_error_over_pi6': kernel_error,
             'taylor_sup_error': taylor_sup_error, 'absolute_vp_mass_over_pi6': absolute_vp_mass,
             'taylor_error_over_pi6': taylor_error, 'radius_over_pi6': radius,
             'lower_over_pi6': lower, 'upper_over_pi6': upper,
             'actual_lower': actual_lo, 'actual_upper': actual_hi,
             'signed_center_over_radius': center/radius}
    report['endpoints'][key] = {field: str(value) for field, value in exact.items()}
    summary[key] = {'sign': sign, 'U_interval': bounds(actual_lo, actual_hi),
                    'center_over_pi6': bounds(center, center),
                    'kernel_error_over_pi6': bounds(kernel_error, kernel_error),
                    'taylor_error_over_pi6': bounds(taylor_error, taylor_error),
                    'signed_center_over_radius': bounds(center/radius, center/radius),
                    'required_absolute_ratio_for_strict_sign': '>1'}
    print('E='+key+': '+sign+'; U enclosure='+str(summary[key]['U_interval'])
          +'; center/error='+str(summary[key]['signed_center_over_radius'])+'; required |ratio|>1.', flush=True)
    save()

contrast = summary['1/4']['sign'] == 'NEGATIVE' and summary['4']['sign'] == 'POSITIVE'
report['summary'] = summary
report['status'] = 'SCOPED_ENDPOINT_CONTRAST_PASS' if contrast else 'SCOPED_ENDPOINT_CONTRAST_STOP'
report['decision'] = ('Fixed contrast certified; global primitive variation and tail join remain open.'
                      if contrast else 'Stop stipulated contrast without refinement; no global conclusion.')
report['producer_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()
print('Result: '+report['status']+'; failures='+str(report['failures'])+'; certificate: '+str(OUT))

#!/usr/bin/env python3
"""Independent fixed E=4 audit; preserve every original artifact.

Use inherited L938/step50 polynomial validation, not a new theta-library
audit. Recompute endpoint sums by direct even/odd integer accumulation,
independently of the two producers' descending Horner recurrence.
"""
import contextlib
import hashlib
import io
import json
import re
import sys
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import factorial, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l944-c944a-audit-75.json'
report = {'status': 'IN_PROGRESS', 'checks': [], 'failures': [],
          'scope': 'E=4; original degree256,257 nodes,theta8,precision200,grid10^-120',
          'python': sys.version, 'inputs_sha256': {}}


def save():
    OUT.write_text(json.dumps(report, indent=2) + '\n')


def check(name, result):
    report['checks'].append({'name': name, 'passed': bool(result)})
    if not result:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw = (BASE / name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def display(value):
    with localcontext() as context:
        context.prec = 12
        return str(Decimal(value.numerator) / Decimal(value.denominator))


save()
data = read('actual-h2-energy-cell-48.json')
poly = read('actual-h2-energy-cell-polynomial-48.json')
prior_audit = read('actual-h2-energy-cell-audit-50.json')
coarse = read('l938-direct-endpoint-enclosure-69.json')
sharp = read('l938-two-bound-endpoint-73.json')
failed = read('l938-two-bound-endpoint-73-bracket-failure.json')
producer_names = ['actual-h2-energy-cell-48.py',
                  'l938-direct-endpoint-enclosure-69.py',
                  'l938-two-bound-endpoint-73.py',
                  'l938-two-bound-endpoint-73-first-pass.py']
for name in producer_names:
    report['inputs_sha256'][name] = digest(BASE / name)
expected_inputs = {'actual-h2-energy-cell-48.json',
                   'actual-h2-energy-cell-polynomial-48.json',
                   'actual-h2-energy-cell-48.py'}
check('all three inherited input hash keys', set(prior_audit['inputs_sha256']) == expected_inputs)
for name, expected in prior_audit['inputs_sha256'].items():
    check('inherited input hash ' + name, report['inputs_sha256'][name] == expected)
for title, source, count, state in [('step50', prior_audit, 5101, 'PASSED'),
                                    ('coarse', coarse, 529, 'SCOPED_ENCLOSURE_STOP'),
                                    ('sharp', sharp, 540, 'SCOPED_ENDPOINT_PASS')]:
    # Check every entry, rather than trusting a summary or preview.
    check(title + ' state and no failures', source['status'] == state and source['failures'] == [])
    check(title + ' check count', len(source['checks']) == count)
    for i, entry in enumerate(source['checks']):
        check(title + ' check ' + str(i) + ': ' + entry['name'], entry['passed'] is True)
check('sharp producer hash', sharp['producer_sha256'] == report['inputs_sha256'][producer_names[2]])
check('coarse certificate hash', sharp['prior_endpoint_sha256'] == report['inputs_sha256']['l938-direct-endpoint-enclosure-69.json'])
for title, source in [('coarse', coarse), ('sharp', sharp), ('failed', failed)]:
    check(title + ' full inherited hash map', source['input_hashes'] == prior_audit['inputs_sha256'])

ap = data['approximation']
check('all fixed budgets', (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision']) == (256, 257, 8, 200))
check('coefficient grid', int(ap['chebyshev_denominator']) == 10**120)
check('power denominator', int(ap['power_denominator']) == 10**120 * 4**256)
check('all257 coefficient rows', len(ap['chebyshev_coefficients']) == 257)
etas, weighted_etas, weighted_coeffs = [], [], []
coefficient_records = []
for ell, row in enumerate(ap['chebyshev_coefficients']):
    chosen = F(int(row['chosen_numerator']), 10**120)
    lo, hi = F(row['enclosure']['lower']), F(row['enclosure']['upper'])
    eta = max(chosen - lo, hi - chosen)
    check('ordered coefficient interval ' + str(ell), lo <= hi)
    check('coefficient index ' + str(ell), row['k'] == ell)
    check('coefficient full radius ' + str(ell), eta == F(row['absolute_error']) and eta >= 0)
    etas.append(eta)
    weighted_etas.append(eta * F(ell * ell, 4))
    weighted_coeffs.append(abs(chosen) * F(ell * ell, 4))
    coefficient_records.append({'index': ell, 'eta': str(eta), 'derivative_eta': str(weighted_etas[-1])})
report['coefficient_allowances'] = coefficient_records
r, n, N = F(2, 3), 257, 256
tail0 = r**n / (1-r)
tail2 = r**n * (n*n*(1-r)**2 + 2*n*r*(1-r) + r*(1+r)) / (1-r)**3
epsilon = 8*10**9*r**N + sum(etas, F(0))
delta = F(10**9, 2)*(tail2 + N*N*tail0) + sum(weighted_etas, F(0))
B = sum(weighted_coeffs, F(0)) + delta
check('full coefficient sum', sum(etas, F(0)) == F(ap['coefficient_error_sum']))
check('complete epsilon', epsilon == F(ap['epsilon']) and 0 < epsilon < F(1, 10**34))

rows = data['algebra']['terms']
lemma = (BASE.parent.parent / 'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md').read_text()
table = [(int(c), tuple(map(int, exponents.split(','))))
         for c, exponents in re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([0-9,]+)\)\s*\|$', lemma, re.M)]
check('exact complete34 table rows', len(table) == len(rows) == 34)
beta_rows = []
for i, row in enumerate(rows):
    alpha = row['exponents_A0_to_A6']
    coefficient = row['coefficient']
    check('table row ' + str(i), (coefficient, tuple(alpha)) == table[i])
    check('twelve factors and weighted degree12 row ' + str(i),
          len(alpha) == 7 and all(isinstance(a, int) and a >= 0 for a in alpha)
          and sum(alpha) == 12 and sum(k*a for k, a in enumerate(alpha)) == 12)
    row_weight = F(abs(coefficient), prod(factorial(k)**a for k, a in enumerate(alpha)))
    # Direct positive half-integer Gamma weight, with pi^6 removed.
    direct = F(abs(coefficient), 2**12 * factorial(17))
    for k, a in enumerate(alpha):
        direct *= (F(factorial(2*k), 4**k*factorial(k)) / factorial(2*k))**a
    check('beta factors row ' + str(i), direct == row_weight / (2**36*factorial(17)))
    beta_rows.append({'row': i, 'absolute_weight': str(row_weight), 'scaled_beta': str(direct)})
weight = sum((F(row['absolute_weight']) for row in beta_rows), F(0))
Z = weight / (2**36 * factorial(17))
check('complete beta weight', weight == F(293, 540))
report['beta_rows'] = beta_rows

rr = list(map(int, poly['numerators']))
check('all3073 polynomial coefficients', len(rr) == 3073)
den = int(poly['denominator'])
check('exact polynomial denominator', den == (2*factorial(12)*int(ap['power_denominator'])*4**262)**12)
identity = prior_audit['integer_identity']
check('full residual', identity['residual'] == '0')
check('identity degree', identity['degree'] == len(rr)-1)
max_saved = max(map(abs, rr))
check('full saved coefficient maximum', max_saved == int(identity['saved_max_abs_coefficient']))
# Rebuild every Q coefficient only to check the inherited coefficient bound;
# reuse the already-audited zero residual, without redoing the 100M-bit product.
power = list(map(int, ap['power_numerators']))
check('all257 power coefficients', len(power) == 257)
qnorms = []
for k in range(7):
    qnorm = 0
    for ell, a in enumerate(power):
        value = F(a * factorial(2*k+2*ell)*4**(262-k-ell)*factorial(12),
                  factorial(k+ell)*factorial(2*k))
        check('Q coefficient integer '+str(k)+','+str(ell), value.denominator == 1)
        qnorm += abs(value.numerator)
    qnorms.append(qnorm)
bound = sum(abs(row['coefficient'])*prod(qnorms[k]**a for k, a in enumerate(row['exponents_A0_to_A6'])) for row in rows)
check('full inherited actual coefficient bound', bound == int(identity['actual_polynomial_coefficient_bound']))
bits = identity['base_power_of_two']
check('full inherited uniqueness bound', bits == (bound+max_saved).bit_length()+1 == 32471
      and bound+max_saved < 2**(bits-1) and identity['difference_bound_lt_half_base'] is True)
report['inherited_integer_identity'] = identity
report['identity_scope'] = 'All input hashes and full bound recomputed; zero residual reused from audited step50, not rerun.'
save()

def independent_endpoint(offset):
    top = factorial(offset+len(rr)-1)
    running_factorial = factorial(offset)
    power4 = 4**offset
    even, odd = 0, 0
    for ell, coefficient in enumerate(rr):
        quotient, remainder = divmod(top, running_factorial)
        check('direct factorial quotient '+str(offset)+','+str(ell), remainder == 0)
        term = coefficient * quotient * power4
        if ell % 2:
            odd += term
        else:
            even += term
        power4 *= 4
        running_factorial *= offset+ell+1
    return F(even+odd, den*top)

centers = {'v_over_pi6': independent_endpoint(17),
           'vprime_over_pi6': independent_endpoint(16)}
report['independent_enclosures'] = {}
summary = {}
for name, source, H in [('coarse', coarse, F(8)), ('sharp', sharp, 2+epsilon)]:
    A, D = 12*epsilon*H**11, delta*H**11 + 11*B*epsilon*H**10
    constants = {'epsilon': epsilon, 'delta': delta, 'B': B,
                 'product_error': A, 'product_derivative_error': D, 'beta_constant': Z}
    if name == 'sharp':
        constants['common_factor_bound'] = H
    for key, value in constants.items():
        check(name+' exact constant '+key, value == F(source['bounds'][key]))
    radii = {'v_over_pi6': Z*4**17*A,
             'vprime_over_pi6': Z*4**16*(17*A+4*D)}
    enclosures = {}
    for key, center in centers.items():
        error = radii[key]
        values = {'center': center, 'radius': error, 'lower': center-error,
                  'upper': center+error, 'center_over_radius': center/error}
        check(name+' positive radius '+key, error > 0)
        for field, value in values.items():
            check(name+' full exact '+key+' '+field, value == F(source['endpoint_enclosures'][key][field]))
        enclosures[key] = {field: str(value) for field, value in values.items()}
    vratio, dratio = centers['v_over_pi6']/radii['v_over_pi6'], -centers['vprime_over_pi6']/radii['vprime_over_pi6']
    if name == 'coarse':
        check('coarse exact value ratio', F(338,10000) < vratio < F(339,10000))
        check('coarse exact derivative ratio', F(220,10**6) < dratio < F(221,10**6))
        check('coarse both zero containments', abs(vratio) < 1 and abs(dratio) < 1)
    else:
        check('sharp exact value ratio', 141790 < vratio < 141791)
        check('sharp exact derivative ratio', 921 < dratio < 922)
        check('sharp actual value positive', centers['v_over_pi6']-radii['v_over_pi6'] > 0)
        check('sharp actual derivative negative', centers['vprime_over_pi6']+radii['vprime_over_pi6'] < 0)
        check('failed reporting bracket remains false', not (200 < dratio < 300))
    report['independent_enclosures'][name] = enclosures
    summary[name] = {'value_ratio_display': display(vratio), 'negative_derivative_ratio_display': display(dratio),
                     'required_ratio_for_sign': '>1', 'constants': {key: str(value) for key, value in constants.items()}}
check('preserved old failure state', failed['status'] == 'FAILED'
      and failed['failures'] == ['negative derivative ratio bracket'] and len(failed['checks']) == 540)
for i, entry in enumerate(failed['checks']):
    check('preserved first-pass entry '+str(i), entry['passed'] is (entry['name'] != 'negative derivative ratio bracket'))
check('preserved first-pass two sign successes', all(any(c['name'] == name and c['passed'] is True for c in failed['checks'])
      for name in ['density lower bound positive', 'derivative upper bound negative']))
report['summary'] = summary
save()

# Re-execute only the two reviewed endpoint producers; redirect just their
# output path, retaining original __file__ so their producer hashes agree.
report['replays'] = []
for script_name, json_name in [('l938-direct-endpoint-enclosure-69.py', 'l938-direct-endpoint-enclosure-69.json'),
                               ('l938-two-bound-endpoint-73.py', 'l938-two-bound-endpoint-73.json')]:
    path = BASE / script_name
    source = path.read_text()
    replay_name = json_name.replace('.json', '-replay-75.json')
    old_line = "out = base / '"+json_name+"'"
    check('unique output redirection '+script_name, source.count(old_line) == 1)
    replay_source = source.replace(old_line, "out = base / '"+replay_name+"'")
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(replay_source, str(path), 'exec'), {'__file__': str(path), '__name__': '__main__'})
    check('complete replay equality '+script_name,
          json.loads((BASE/replay_name).read_text()) == json.loads((BASE/json_name).read_text()))
    report['replays'].append({'producer': script_name, 'certificate': 'scripts/heat/'+replay_name, 'full_equality': True})
for name, expected in report['inputs_sha256'].items():
    check('original unchanged '+name, digest(BASE/name) == expected)
report['status'] = 'PASSED'
report['producer_sha256'] = digest(Path(__file__))
report['summary']['check_count'] = len(report['checks'])
report['summary']['failures'] = report['failures']
report['summary']['conclusion'] = 'L944 coarse stop and C944a E=4 signs validated under inherited contracts; no compact cover.'
save()
print('PASSED: '+str(len(report['checks']))+' exact checks; failures='+str(report['failures']))
for name in ('coarse', 'sharp'):
    print(name+': value/error='+summary[name]['value_ratio_display']+', -derivative/error='+summary[name]['negative_derivative_ratio_display']+'; sign exclusion requires >1.')
print('Full report: '+str(OUT))

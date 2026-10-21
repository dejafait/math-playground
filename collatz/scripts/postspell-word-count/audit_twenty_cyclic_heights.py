#!/usr/bin/env python3
"""Independent exact arithmetic audit of L050; analytic audit is in the lemma."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

base = Path(__file__).resolve().parent
source = base / 'twenty-cyclic-height-certificate.json'
before = source.read_bytes()
subprocess.run([sys.executable, str(base / 'certify_twenty_cyclic_heights.py')], check=True)
after = source.read_bytes()
saved = json.loads(after)
checks = []


def check(name, actual, relation, required):
    ok = {'=': lambda: actual == required,
          '<': lambda: actual < required,
          '>': lambda: actual > required}[relation]()
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=ok))


def enclosure(x, terms):
    # Horner evaluation of the integrated finite geometric polynomial.
    poly = Q(0)
    for j in reversed(range(terms)):
        poly = Q(1, 2*j+1) + x*x*poly
    low = 2*x*poly
    remainder = 2*x**(2*terms+1)/((2*terms+1)*(1-x*x))
    return low, low+remainder, remainder


check('generator byte reproduction', sha256(after).hexdigest(), '=', sha256(before).hexdigest())
logs = {}
for label, argument, x in [('log2', 2, Q(1, 3)), ('log3', 3, Q(1, 2))]:
    lo, hi, rem = enclosure(x, 48)
    expected = dict(argument=str(argument), x=str(x), terms=48,
                    lower=str(lo), remainder_upper=str(rem), upper=str(hi))
    check(label+' full saved enclosure', saved['log_enclosures'][label], '=', expected)
    logs[label] = (lo, hi)

l2, u2 = logs['log2']
l3, u3 = logs['log3']
p, q, M = 9809721694, 6189245291, 10**9
R = Q(48**20-25**20, 23*25**19)
res_lo, res_hi = q*l3-p*u2, q*u3-p*l2
expected_checks = [
    ('geometric identity', R, '=', R),
    ('twenty occurrence geometric upper bound', R, '<', Q(503775)),
    ('length constant', Q(690, 517), '<', Q(2)),
    ('e lower comparison', Q(163, 60), '>', Q(27, 10)),
    ('log20 below 3', Q(163**3, 60**3), '>', Q(20)),
    ('log ceiling below 21', Q(27**21, 10**21), '>', Q(M)),
    ('monotonicity derivative guard', Q(40201245), '<', Q(M)),
    ('ceiling contradiction upper bound', Q(21*40201245+36271802), '<', Q(M)),
    ('rational approximant is strictly below log ratio', res_lo, '>', Q(0)),
    ('rational approximant residual upper bound', res_hi, '<', l2/(2*M)),
    ('log2 exceeds 2/3', l2, '>', Q(2, 3)),
    ('minimum log height below 28', Q(27**28, 10**28), '>', Q(1380*q+23, 11)),
    ('represented odd count contradiction', Q(15*503775*29, 4), '<', Q(225640000)),
]
check('original check count', len(saved['checks']), '=', len(expected_checks))
for record, (name, actual, relation, required) in zip(saved['checks'], expected_checks):
    check(name, actual, relation, required)
    check(name+' saved record', record, '=', dict(name=name, actual=str(actual),
          relation=relation, required=str(required), passed=checks[-1]['passed']))

summary = dict(R=str(R), R_upper=503775, A=str(Q(399, 5)*503775),
               B=72*503775+2, length_ceiling=M, p=p, q=q,
               residual_lower=str(res_lo), residual_upper=str(res_hi),
               minimum_shifted_height_upper=str(Q(1380*q+23, 11)),
               minimum_log_height_upper=28,
               represented_odd_count_upper=str(Q(15*503775*29, 4)),
               primitive_odd_count_required=225640000, failures=[])
check('all mathematical summary fields', {key: saved[key] for key in summary}, '=', summary)

# Different logarithm arguments and precision: log3 = log2 + log(3/2).
# Because q-p<0, its lower residual uses the UPPER log2 endpoint.
v2, w2, _ = enclosure(Q(1, 3), 64)
v15, w15, _ = enclosure(Q(1, 5), 64)
alt_lo, alt_hi = (q-p)*w2+q*v15, (q-p)*v2+q*w15
check('independent residual lower bound', alt_lo, '>', Q(9, 10**11))
check('independent residual upper bound', alt_hi, '<', Q(1, 10**10))
check('independent required residual bound', alt_hi, '<', v2/(2*M))
check('independent interval above original lower', alt_lo, '>', res_lo)
check('independent interval below original upper', alt_hi, '<', res_hi)

initial = json.loads((base / 'twenty-cyclic-height-initial-certificate.json').read_text())
check('preserved initial failed guard', initial['failures'], '=', [dict(
    name='log20 below 3', actual='19683/1000', relation='>', required='20', passed=False)])
failures = [item for item in checks if not item['passed']]
result = dict(lemma='L050', scope='Exact constants only; full analytic audit in L050.',
              original_sha256=sha256(after).hexdigest(),
              independent_log_enclosures=dict(log2=[str(v2), str(w2)],
                                               log_three_halves=[str(v15), str(w15)]),
              independent_residual=dict(lower=str(alt_lo), upper=str(alt_hi)),
              checks=checks, failures=failures)
path = base / 'twenty-cyclic-height-audit-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'Audit: checks={len(checks)}, failures={len(failures)}')
print('Independent residual: 9/10^11 < r < 1/10^10 < log2/(2*10^9)')
print('Ceiling: 880497947 < 10^9; odd-count bound: 219142125/4 < 225640000')
print(f'Certificate: {path.relative_to(Path.cwd())}')
if failures:
    print('Failed checks: '+', '.join(item['name'] for item in failures))
    raise SystemExit(1)

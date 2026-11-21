#!/usr/bin/env python3
"""Exact replay of every recorded Simpson node and the final sign budget.

Does not independently evaluate special functions or prove C466m.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

directory = Path(__file__).parent
source = directory / 'density-937.json'
data = json.loads(source.read_text())
checks = []


def endpoint(value):
    return F(int(value['mantissa'])) * F(2)**value['exponent_2']


def interval(value):
    lo, hi = endpoint(value['lower']), endpoint(value['upper'])
    assert lo <= hi
    return lo, hi


def check(name, actual, relation, required):
    passed = {'<': lambda: actual < required, '>': lambda: actual > required,
              '==': lambda: actual == required, '<=': lambda: actual <= required,
              '>=': lambda: actual >= required}[relation]()
    checks.append({'name':name, 'actual':str(actual), 'relation':relation,
                   'required':str(required), 'passed':passed})


c = data['constants']
n, T = c['n'], c['T']
check('no_reported_failures', len(data['failures'])+len(data['failed_checks']), '==', 0)
check('script_hash_matches', hashlib.sha256((directory/'density_937.py').read_bytes()).hexdigest(),
      '==', data['script_sha256'])
check('complete_node_count', len(data['nodes']), '==', n+1)
lo = hi = F(0)
for j, node in enumerate(data['nodes']):
    assert node['j'] == j
    a, b = interval(node['value'])
    weight = 1 if j in (0,n) else (4 if j % 2 else 2)
    lo += weight*a
    hi += weight*b
lo *= F(T, 3*n)
hi *= F(T, 3*n)
saved_lo, saved_hi = interval(data['result']['finite_simpson_sum'])
check('simpson_lower_encloses_exact_sum', saved_lo, '<=', lo)
check('simpson_upper_encloses_exact_sum', saved_hi, '>=', hi)
check('S_lower', interval(c['S'])[0], '>', F(1,100))
check('S_upper', interval(c['S'])[1], '<', 1)
check('fourth_derivative_upper', interval(c['fourth_derivative_upper'])[1], '<', F(183,10**6))
check('simpson_error_upper', interval(c['simpson_error_upper'])[1], '<', F(260,10**6))
check('tail_error_upper', interval(c['one_sided_tail_upper'])[1], '<', F(59,10**6))
budget = F(319,10**6)
check('unscaled_integral_positive_margin', saved_lo-budget, '>', F(1,250))
# e^S/pi>1/4 since S>0 and pi<4. The positive integral lower bound
# therefore proves p(S)>1/1000 without using a transcendental prefactor.
check('conservative_density_lower_bound', (saved_lo-budget)/4, '>', F(1,1000))
check('reported_density_lower', interval(data['result']['density_enclosure'])[0], '>', F(9946,10**6))
check('reported_density_upper', interval(data['result']['density_enclosure'])[1], '<', F(10164,10**6))

out = {'scope':'Exact aggregate replay of all stored node enclosures; special-function enclosures and analytic bounds require the canonical proof and independent audit.',
       'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
       'checks':checks, 'failures':[c['name'] for c in checks if not c['passed']],
       'all_nodes_replayed':len(data['nodes']),
       'conservative_density_lower_bound':str((saved_lo-budget)/4)}
dest = directory/'density-937-check.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(f"Nodes replayed: {len(data['nodes'])}; checks: {len(checks)}; failures: {out['failures']}")
print('Exact replay proves p(S)>1/1000 under the recorded node and analytic enclosures.'
      if not out['failures'] else 'REPLAY FAILED')
print(f'Certificate: {dest}')
raise SystemExit(bool(out['failures']))

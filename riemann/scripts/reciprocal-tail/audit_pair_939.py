#!/usr/bin/env python
"""Replay the audited generator, preserving 937, then check full exact evidence.

Run with the same installed Python 2.7/SymPy interval environment as 937.
The elementary interval library and external density inputs remain trusted.
"""
from __future__ import print_function, division
from fractions import Fraction as F
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, 'density_937.py')
original = open(SOURCE, 'rb').read()
replacement = original.replace("'density-937.json'", "'density-939-recomputed.json'")
assert replacement != original and original.count("'density-937.json'") == 1
namespace = {'__name__': '__main__', '__file__': SOURCE}
exit_code = None
try:
    eval(compile(replacement, SOURCE, 'exec'), namespace)
except SystemExit as exc:
    exit_code = exc.code

saved_path = os.path.join(HERE, 'density-937.json')
replay_path = os.path.join(HERE, 'density-939-recomputed.json')
saved = json.load(open(saved_path))
replay = json.load(open(replay_path))
checks = []


def endpoint(v):
    return F(int(v['mantissa'])) * F(2)**v['exponent_2']


def interval(v):
    a, b = endpoint(v['lower']), endpoint(v['upper'])
    assert a <= b
    return a, b


def check(name, actual, relation, required):
    passed = {'==': lambda: actual == required,
              '<': lambda: actual < required, '>': lambda: actual > required,
              '<=': lambda: actual <= required, '>=': lambda: actual >= required}[relation]()
    checks.append({'name': name, 'actual': str(actual), 'relation': relation,
                   'required': str(required), 'passed': passed})


def enclosure(name, stored, calculated):
    a, b = interval(stored)
    check(name + '_lower', a, '<=', calculated[0])
    check(name + '_upper', b, '>=', calculated[1])


check('generator_exit', exit_code, '==', 0)
check('generator_failures', len(replay['failures']) + len(replay['failed_checks']), '==', 0)
check('saved_source_hash', saved['script_sha256'], '==', hashlib.sha256(original).hexdigest())
check('replay_source_hash', replay['script_sha256'], '==', saved['script_sha256'])
check('all_saved_prerequisites', sum(not v['passed'] for v in saved['checks']), '==', 0)

# Compare all endpoint-bearing records, not a node sample or a display string.
endpoint_records = [0]
endpoint_mismatches = []


def compare(a, b, path):
    if isinstance(a, dict) and 'lower' in a and 'upper' in a:
        endpoint_records[0] += 1
        if interval(a) != interval(b):
            endpoint_mismatches.append(path)
    elif isinstance(a, dict):
        for key in a:
            if key not in ('elapsed_seconds', 'display'):
                compare(a[key], b[key], path + '/' + str(key))
    elif isinstance(a, list):
        assert len(a) == len(b)
        for j, (left, right) in enumerate(zip(a, b)):
            compare(left, right, path + '/' + str(j))
    elif a != b:
        endpoint_mismatches.append(path)


compare(saved, replay, '')
check('all_endpoint_record_mismatches', len(endpoint_mismatches), '==', 0)

# Independently compute Bernoulli numbers by their defining recurrence.
bern = [F(1)]
binomial = lambda n, k: namespace['fact'](n) // (namespace['fact'](k)*namespace['fact'](n-k))
for m in range(1, 33):
    bern.append(-sum(F(binomial(m+1, k))*bern[k] for k in range(m))/F(m+1))
for m in range(2, 33, 2):
    check('Bernoulli_' + str(m), namespace['B'][m], '==', bern[m])

c, r = saved['constants'], saved['result']
check('n_even', c['n'] % 2, '==', 0)
check('n_exact', c['n'], '==', 8192)
check('T_exact', c['T'], '==', 4096)
enclosure('step', c['step'], (F(1, 2), F(1, 2)))
check('complete_node_count', len(saved['nodes']), '==', c['n'] + 1)
sum_lo = sum_hi = F(0)
max_width = F(0)
for j, node in enumerate(saved['nodes']):
    assert node['j'] == j and replay['nodes'][j]['j'] == j
    lo, hi = interval(node['value'])
    max_width = max(max_width, hi-lo)
    weight = 1 if j in (0, c['n']) else (4 if j % 2 else 2)
    sum_lo += weight*lo
    sum_hi += weight*hi
enclosure('Simpson_sum', r['finite_simpson_sum'], (sum_lo/6, sum_hi/6))

for j, v in enumerate(saved['checks']):
    a, b = interval(v['actual'])
    lower, upper = interval(v['required'])
    if v['relation'] == '<':
        check('saved_inequality_' + v['name'], b, '<', lower)
    else:
        check('saved_inequality_' + v['name'], a, '>', upper)

x = interval(c['x'])
enclosure('S_from_x', c['S'], (3*x[0], 3*x[1]))
S = interval(c['S'])
check('S_positive_lower_for_R', S[0], '>', F(1, 100))
check('S_upper_for_R', S[1], '<', 1)
lap = [interval(v) for v in c['laplace_values']]
dlo = dhi = F(0)
for weight, (lo, hi) in zip([1, -4, 6, -4, 1], lap):
    dlo += weight*(lo if weight > 0 else hi)
    dhi += weight*(hi if weight > 0 else lo)
enclosure('five_Laplace_difference', c['fourth_difference'], (dlo, dhi))
d = interval(c['fourth_difference'])
check('five_Laplace_difference_positive', d[0], '>', 0)
enclosure('mu4', c['mu4_upper'], (256*d[0], 256*d[1]))
mu = interval(c['mu4_upper'])
enclosure('Q4', c['fourth_derivative_upper'],
          (8*(S[0]**4*lap[2][0]+mu[0]), 8*(S[1]**4*lap[2][1]+mu[1])))
Q4 = interval(c['fourth_derivative_upper'])
enclosure('Simpson_error', c['simpson_error_upper'], (F(64,45)*Q4[0], F(64,45)*Q4[1]))
eq, et = interval(c['simpson_error_upper']), interval(c['one_sided_tail_upper'])
error = interval(r['total_integral_error_upper'])
check('combined_error_covers_both', error[0], '>=', eq[1]+et[1])
check('Q4_printed', Q4[1], '<', F(182705, 10**9))
check('Simpson_error_printed', eq[1], '<', F(260, 10**6))
check('tail_error_printed', et[1], '<', F(59, 10**6))
check('combined_error_printed', error[1], '<', F(319, 10**6))

def rounded(name, value, lo, hi):
    a, b = interval(value)
    check(name+'_rounded_lower', a, '>', F(lo))
    check(name+'_rounded_upper', b, '<', F(hi))


rounded('c0', c['c0_complex']['real'], '0.49712077818831', '0.49712077818832')
rounded('S', c['S'], '0.06920389209069', '0.06920389209070')
rounded('A', r['finite_simpson_sum'], '0.02947556997059', '0.02947556997060')
rounded('density', r['density_enclosure'], '0.00994617', '0.01016314')
integral = interval(r['finite_simpson_sum'])
lower_density = (integral[0]-F(319,10**6))/4
check('positive_unscaled_integral', integral[0]-F(319,10**6), '>', F(1,250))
check('conservative_density', lower_density, '>', F(1,1000))

out = {'scope': 'All nodes regenerated with audited remainder code; exact endpoint and propagation checks. Analytic audit is canonical in C466m/C466n. Elementary intervals and external inputs remain trusted.',
       'original_generator_sha256': hashlib.sha256(original).hexdigest(),
       'executed_generator_sha256': hashlib.sha256(replacement).hexdigest(),
       'only_generator_edit': 'Output filename changed to density-939-recomputed.json; __file__ retains original source for its provenance hash.',
       'original_certificate_sha256': hashlib.sha256(open(saved_path,'rb').read()).hexdigest(),
       'recomputed_certificate': 'scripts/reciprocal-tail/density-939-recomputed.json',
       'nodes_regenerated': len(replay['nodes']), 'endpoint_records_compared': endpoint_records[0],
       'endpoint_mismatches': endpoint_mismatches, 'maximum_node_width': str(max_width),
       'conservative_density_lower_bound': str(lower_density),
       'checks': checks, 'failures': [v['name'] for v in checks if not v['passed']]}
dest = os.path.join(HERE, 'pair-audit-939.json')
with open(dest, 'w') as handle:
    json.dump(out, handle, indent=2, sort_keys=True)
    handle.write('\n')
print('Full replay: nodes=%d; endpoint records=%d; checks=%d; failures=%s' %
      (len(replay['nodes']), endpoint_records[0], len(checks), out['failures']))
print('Conservative density lower bound=%s; required >1/1000' % lower_density)
print('Audit certificate: %s' % dest)
sys.exit(bool(out['failures']))

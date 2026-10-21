#!/usr/bin/env python3
"""Independent finite audit for L081 only; exact arithmetic, no t=1 test."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import operator
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'redistributed-h-t0-real-feasibility-certificate.json'
data = json.loads(SOURCE.read_text())
table_path = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
table = [list(map(int, t)) for t in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', table_path.read_text(), re.M)]
checks = []


def verify(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})


verify('complete indexed source table', [r[0] for r in table] == list(range(25)))
verify('source hash', data['source']['sha256'] == hashlib.sha256(table_path.read_bytes()).hexdigest())
rows = []
for i, j, h in table:
    h += -1 if i == 0 else 1 if i == 24 else 0
    rows.append({'i': i, 'J': j, 'H': h, 'a': 166504412 if i == 24 else 2})
verify('all changed rows and tails', rows == data['parameters'])
J, H, tails = (sum(r[k] for r in rows) for k in ('J', 'H', 'a'))
K, N = 3*J+H, 4*J+H+tails
L = N-K
verify('all aggregate counts', data['counts'] == dict(K=K, L=L, N=N, d=1, K0=K, L0=L))
prefix = [(sum(3*r['J']+r['H'] for r in rows[:i]),
           sum(4*r['J']+r['H']+r['a'] for r in rows[:i])) for i in range(26)]
verify('closing product including actual last tail', prefix[25] == (397573379, 630138897))
verify('all incoming prefixes', len(data['prefixes']) == 25 and all(
    p['i'] == i and (p['three_exponent'], p['two_exponent']) == prefix[i]
    and F(p['product_lower']) == (1 if i == 0 else 10**8*2**(i-1))
    for i, p in enumerate(data['prefixes'])))


def independent_series(x, terms):
    z = F(x-1, x+1)
    power = z
    values = []
    for odd in range(1, 2*terms, 2):
        values.append(2*power/odd)
        power *= z*z
    tail = 2*power/((2*terms+1)*(1-z*z))
    return values, tail


intervals = {}
for x in (2, 3):
    terms100, error100 = independent_series(x, 100)
    saved = data['logs'][str(x)]
    low100 = sum(terms100, F(0))
    verify(f'all saved log{x} terms and bounds',
           F(saved['argument']) == x and F(saved['z']) == F(x-1, x+1)
           and list(map(F, saved['terms'])) == terms100
           and F(saved['remainder_upper']) == error100
           and F(saved['lower']) == low100 and F(saved['upper']) == low100+error100)
    values, error = independent_series(x, 120)
    low = sum(values, F(0))
    intervals[x] = (low, low+error)
    verify(f'independent log{x} interval nests strictly', low100 < low < low+error < low100+error100)
l2, u2 = intervals[2]
l3, u3 = intervals[3]
lm, lp = F(10584, 10**14), F(10585, 10**14)
lambda120 = (N*l2-K*u3, N*u2-K*l3)
lambda100 = (N*F(data['logs']['2']['lower'])-K*F(data['logs']['3']['upper']),
             N*F(data['logs']['2']['upper'])-K*F(data['logs']['3']['lower']))
verify('complete saved amplified Lambda interval', tuple(map(F, data['lambda_interval'])) == lambda100)
verify('strict independent Lambda bounds', 0 < lm < lambda120[0] < lambda120[1] < lp < 1)
verify('strict saved Lambda bounds', lm < lambda100[0] < lambda100[1] < lp)
kap = F(23, 11)
Rplus = kap*(1+F(2, 10**8))
cap = Rplus/lm+Rplus+kap
root = data['root']
verify('complete numeric root certificate', F(root['lambda_lower']) == lm
       and F(root['lambda_upper']) == lp and F(root['R_upper']) == Rplus
       and F(root['normalized_shifted_upper']) == cap)
verify('normalized cap exact value and strict threshold',
       cap == F(435606069410390910013, 22050000000) and cap < 20000000000)
expterms = [F(1)]
for k in range(1, 41):
    expterms.append(expterms[-1]*24/k)
verify('all exponential partial-sum terms', list(map(F, data['exp24_terms'])) == expterms)
verify('strict exp24 threshold', sum(expterms) > 20000000000)
q3, q2 = prefix[18][0]+3*rows[18]['J'], prefix[18][1]+4*rows[18]['J']+rows[18]['H']
grid2, grid3 = F(693147180559, 10**12), F(1098612288669, 10**12)
grid_margin = 24+q3*grid3-q2*grid2
tight_margin = (24+q3*l3-q2*u2, 24+q3*u3-q2*l2)
expected_guard = dict(i=18, J=693015, H=3295208, own_input=18,
                      prefix_three=6078923, prefix_two=6862840,
                      log3_coefficient=8157968, log2_negative_coefficient=12930108,
                      actual_margin='h_18+J_18*log(27/16)-H_18*log2',
                      margin_strict_upper=str(grid_margin), required_relation='actual margin > 0')
verify('complete saved own-input guard', data['failed_necessary_guard'] == expected_guard)
verify('independent coefficient and sign check', (q3, q2) == (8157968, 12930108)
       and grid2 < l2 and u3 < grid3
       and tight_margin[1] < grid_margin == -F(457745289, 50000000000) < 0)

# Independently reconstruct every saved check operand, not just its pass flag.
expected = {}


def expect(name, actual, relation, required):
    expected[name] = (F(actual), relation, F(required))


for name, actual, required in [('sum J', J, 66061058), ('sum H', H, 199390205),
    ('sum tails', tails, 166504460), ('K', K, 397573379), ('L', L, 232565518), ('N', N, 630138897)]:
    expect(name, actual, '=', required)
for r in rows:
    i = r['i']
    for label, key, floor in [('J', 'J', 2), ('H', 'H', 3), ('tail', 'a', 2)]:
        expect(f'row {i} {label} domain', r[key], '>=', floor)
    expect(f'row {i} tail congruence', r['a'] % 18, '=', 2)
    if i < 24:
        expect(f'incoming row {i} tail exactly 2', r['a'], '=', 2)
for args in [
    ('explicit d=1 odd count threshold', K, '>', 225640000),
    ('explicit d=1 even count positive', L, '>', 0),
    ('aggregate length inequality', N, '<', F(8,5)*K+F(1725,1034)),
    ('fresh Lambda lower', lm, '<', lambda100[0]),
    ('fresh Lambda upper', lambda100[1], '<', lp),
    ('positive Lambda lower', lm, '>', 0), ('Lambda upper below one', lp, '<', 1),
    ('every eta positive from parameter floors', F(16,27)**2*(F(12,11)+F(2,3)**3), '<', kap),
    ('fresh changed row0 c0', F(3**(3*rows[0]['J']+rows[0]['H']), 2**(4*rows[0]['J']+rows[0]['H']+rows[0]['a'])), '>', 10**8),
    ('other incoming c_i floor', F(3**9,2**13), '>', 2),
    ('closing product odd exponent', prefix[25][0], '=', K),
    ('closing product denominator exponent', prefix[25][1], '=', N),
    ('full inverse prefix bound', kap*(1+sum(F(1,10**8*2**j) for j in range(24))), '<', Rplus),
    ('fresh all-input normalized shifted root cap', cap, '<', 20*10**9),
    ('exp24 strict partial-sum bound', 20*10**9, '<', sum(expterms)),
    ('log2 grid lower', grid2, '<', F(data['logs']['2']['lower'])),
    ('log2 grid upper', F(data['logs']['2']['upper']), '<', F(693147180560,10**12)),
    ('log3 grid lower', F(1098612288668,10**12), '<', F(data['logs']['3']['lower'])),
    ('log3 grid upper', F(data['logs']['3']['upper']), '<', grid3),
    ('own-input row18 H margin upper strictly negative', grid_margin, '<', 0)]:
    expect(*args)
ops = {'<': operator.lt, '>': operator.gt, '=': operator.eq, '<=': operator.le, '>=': operator.ge}
verify('exact set of 150 check names', len(data['checks']) == len(expected) == 150
       and {c['name'] for c in data['checks']} == set(expected))
for c in data['checks']:
    actual, relation, required = expected[c['name']]
    verify('reconstructed check: '+c['name'], F(c['actual']) == actual
           and c['relation'] == relation and F(c['required']) == required
           and F(c['difference']) == actual-required
           and c['passed'] is True and ops[relation](actual, required))
verify('saved verdict and absence of certification failures',
       data['failures'] == [] and data['verdict'] == 'INFEASIBLE_H_GUARD_18')
failures = [c['name'] for c in checks if not c['passed']]
result = dict(target='L081 independent t=0 critical audit',
    source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    checks=checks, failures=failures,
    evidence=dict(counts=dict(K=K,L=L,N=N), all_26_prefixes=prefix,
                  independent_log_intervals=intervals, lambda_interval=lambda120,
                  amplified_lambda_error=N*(u2-l2)+K*(u3-l3),
                  normalized_cap=cap, cap_required=20000000000,
                  exp24_partial_sum=sum(expterms),
                  margin_grid_upper=grid_margin, margin_required_lower=0,
                  tighter_affine_upper_expression_interval=tight_margin,
                  amplified_margin_error=q3*(u3-l3)+q2*(u2-l2)),
    summary=dict(verdict='NO_DEFECT_FOUND' if not failures else 'AUDIT_FAILED',
                 checks=len(checks), original_checks_reconstructed=len(expected),
                 failures=failures, margin_upper=grid_margin, required_margin='>0'),
    scope='L081 t=0 only; algebraic proof audit is canonical in L081; no full Collatz result.')
output = HERE / 'redistributed-h-t0-real-feasibility-audit-certificate.json'
output.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f"{result['summary']['verdict']}: {len(checks)} audit checks; 150 original checks reconstructed")
print(f'Actual H margin < {grid_margin}; required > 0')
print(f'Normalized input cap {cap} < 20000000000 < exp(24)')
print(f'Failures: {failures}; certificate: {output.relative_to(ROOT)}')
assert not failures

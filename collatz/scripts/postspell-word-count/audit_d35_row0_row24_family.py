#!/usr/bin/env python3
"""Audit C104a in delta=m-1 coordinates; universal proof stays in C104a.

Independently resums each prefix, checks all saved family operands, and
reuses audited L104's log enclosure only after checking identical totals.
No construction imports, orbit samples, or expanded huge powers.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
table = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
construction = HERE / 'd35-row0-row24-family-certificate.json'
saved = json.loads(construction.read_text())
raw = table.read_bytes()
base = [tuple(map(int, line.strip('|').split('|')))
        for line in raw.decode().splitlines()
        if re.fullmatch(r'\|\d+\|\d+\|\d+\|', line)]
assert [i for i, _, _ in base] == list(range(25))
B, kap = 9250245, F(23, 11)
checks = []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b,
              '>=': a >= b, '<=': a <= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation,
                       required=b, difference=a-b, passed=passed))


rows = []
for i, j, h in base:
    h += -35 if i == 0 else 35 if i == 24 else 0
    b = [1, 1] if i == 0 else [B-1, -1] if i == 24 else [0, 0]
    a = [2+18*b[0], 18*b[1]]
    q = [4*j+h+a[0], a[1]]
    row = dict(i=i, J=j, H=h, b_delta=b, a_delta=a, p=3*j+h, q_delta=q)
    rows.append(row)
    old = saved['rows'][i]
    for key, value in [('i', i), ('J', j), ('H', h), ('p', 3*j+h)]:
        check(f'row{i} saved {key}', old[key], '=', value)
    for key, pair in [('b', b), ('a', a), ('q', q)]:
        check(f'row{i} saved {key} at m1', sum(old[key]), '=', pair[0])
        check(f'row{i} saved {key} slope', old[key][1], '=', pair[1])
    check(f'row{i} eta J premise', j, '>=', 2)
    check(f'row{i} eta H premise', h, '>=', 3)
    for delta in (0, B-1):
        check(f'row{i} budget at delta{delta}', b[0]+b[1]*delta, '>=', 0)
        check(f'row{i} tail at delta{delta}', a[0]+a[1]*delta, '>=', 2)
    if 1 <= i <= 23:
        check(f'row{i} ordinary H floor', h, '>=', 6)
        check(f'row{i} ordinary tail', a[0], '=', 2)
        check(f'row{i} ordinary tail slope', a[1], '=', 0)

K = sum(r['p'] for r in rows)
N = [sum(r['q_delta'][d] for r in rows) for d in range(2)]
check('K matches audited L104', K, '=', 397573379)
check('N matches audited L104', N[0], '=', 630138897)
check('N independent of delta', N[1], '=', 0)
check('budget total', sum(r['b_delta'][0] for r in rows), '=', B)
check('budget total slope', sum(r['b_delta'][1] for r in rows), '=', 0)
check('row0 exponent numerator', rows[0]['p'], '=', 29)
check('row0 exponent denominator at m1', rows[0]['q_delta'][0], '=', 57)
check('row0 exponent slope', rows[0]['q_delta'][1], '=', 18)

order = list(range(1,25))+[0]
prefixes = []
for k, i in enumerate(order):
    included = order[:k]
    p = sum(rows[t]['p'] for t in included)
    q = [sum(rows[t]['q_delta'][d] for t in included) for d in range(2)]
    old = saved['cut1_prefixes'][k]
    for key, value in [('input_row', i), ('p', p)]:
        check(f'prefix{k} saved {key}', old[key], '=', value)
    check(f'prefix{k} saved q at m1', sum(old['q']), '=', q[0])
    check(f'prefix{k} saved q slope', old['q'][1], '=', q[1])
    if k < 24:
        assert included == list(range(1,k+1))
        check(f'prefix{k} constant', q[1], '=', 0)
    prefixes.append(dict(input_row=i, outgoing_row=(i+1)%25,
                         included_rows=included, p=p, q_delta=q))
assert [p['outgoing_row'] for p in prefixes] == order[1:]+order[:1]
check('last prefix p', prefixes[-1]['p'], '=', K-29)
check('last prefix q at m1', prefixes[-1]['q_delta'][0], '=', N[0]-57)
check('last prefix q slope', prefixes[-1]['q_delta'][1], '=', -18)
check('m=B final decay exponent', -18*(B-1), '=', -166504392)
check('m=B closing tail', rows[24]['a_delta'][0]+rows[24]['a_delta'][1]*(B-1), '=', 2)

endpoints = []
for m in (1,B):
    delta = m-1
    ep = dict(m=m, budgets=[r['b_delta'][0]+delta*r['b_delta'][1] for r in rows],
              tails=[r['a_delta'][0]+delta*r['a_delta'][1] for r in rows])
    endpoints.append(ep)
assert endpoints == saved['domain_endpoints']

# Imported enclosure has identical K,N; no new logarithm calculation.
lm, lp = F(10584,10**14), F(10585,10**14)
check('imported lower matches', saved['imported_L104_enclosure']['Lambda_lower'], '=', lm)
check('imported upper matches', saved['imported_L104_enclosure']['Lambda_upper'], '=', lp)
check('positive denominator lower', lm, '>', 0)
check('exponential upper bound domain', lp, '<', F(1,2))
c0 = F(3**29,2**57)
geometric = 2-F(1,2**23)
last = c0/(1-lp)
bsum = kap*(2+F(1,500))
cap = bsum/lm+kap
guard = F(4*2**(4*rows[1]['J']),11)
bounds = dict(c0_at1=c0, geometric_sum=geometric, last_reciprocal_upper=last,
              B1_coarse_upper=bsum, s1_uniform_upper=cap, coarse_cap=60000000000,
              row1_J_required=guard, guard_gap_above_coarse=guard-60000000000)
for key, value in bounds.items():
    check('saved bound '+key, saved['bounds'][key], '=', value)
check('ordinary growth floor', F(729,256), '>', 2)
check('geometric strict cap', geometric, '<', 2)
check('last reciprocal strict cap', last, '<', F(1,500))
check('B1 rational cap', bsum, '=', F(2093,500))
check('s1 rational cap', cap, '=', F(82225000004347,2079))
check('s1 coarse cap', cap, '<', 60000000000)
check('row1 guard operand', guard, '=', F(4611686018427387904,11))
check('row1 necessary contradiction', guard, '>', 60000000000)

for c in saved['checks']:
    check('construction comparison '+c['name'], c['actual'], c['relation'], c['required'])
    check('construction difference '+c['name'], c['difference'], '=', F(c['actual'])-F(c['required']))
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='Full integer edge 1<=m<=9250245; delta=m-1; exact endpoints and closure',
    source_hashes={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in (table, construction)},
    rows=rows, K=K, N_delta=N, prefixes=prefixes, endpoints=endpoints,
    imported_enclosure=dict(lower=lm, upper=lp, input='audited L104, identical K,N'),
    bounds=bounds, checks=checks,
    summary=dict(verdict='PASS' if not failures else 'FAIL', checks=len(checks),
                 failures=failures, saved_checks_recomputed=len(saved['checks']),
                 prefixes_verified=len(prefixes), parameter_samples=0),
    limitations='Uniform monotonicity and exact closure are proved symbolically in C104a; '
                'no logarithm recertification, other supports or actual-word transfer.')
out = HERE / 'd35-row0-row24-family-audit-certificate.json'
out.write_text(json.dumps(result,default=str,indent=2)+'\n')
print(f"Audit {result['summary']['verdict']}; checks={len(checks)}; failures={failures}")
print(f'K={K}, N(delta)={N}; required unchanged (397573379,630138897)')
print(f's1 < {cap} < 60000000000; required s1 >= {guard}')
print(f'm=B closing tail={endpoints[-1]["tails"][24]}; required 2')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)

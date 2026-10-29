#!/usr/bin/env python3
"""Independent finite audit of C106a; no generator import or huge orbit.

L104's audited logarithm enclosure is an input, not recomputed here.
The canonical proof supplies the analytic and same-tuple arguments.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / 'l106-row3-guard-failure-certificate.json'
saved = json.loads(SOURCE.read_text())
literal = [
    (8,40), (15,72), (28,134), (52,249), (98,467), (184,877),
    (347,1650), (653,3106), (1230,5849), (2317,11018),
    (4365,20756), (8224,39104), (15494,73672), (29191,138802),
    (54998,261511), (103621,492705), (195229,928293),
    (367827,1748976), (693015,3295208), (1305695,6208431),
    (2460032,11697176), (4634896,22038409), (8732512,41522114),
    (16452748,78230965), (30998279,32670621),
]
checks = []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b, '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation, required=b,
                       difference=a-b, passed=passed))


table = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
parsed = [tuple(map(int, v)) for v in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', table.read_text(), re.M)]
check('literal table count', len(parsed), '=', 25)
for i, (j, h) in enumerate(literal):
    for field, a, b in zip(('i', 'J', 'H'), parsed[i], (i, j, h)):
        check(f'literal row{i} {field}', a, '=', b)

rows = []
for i, (j, old_h) in enumerate(literal):
    h = old_h + (-35 if i == 0 else 35 if i == 24 else 0)
    b = {0: 1, 1: 1, 2: 12, 24: 9250231}.get(i, 0)
    a = 2+18*b
    row = dict(i=i, J=j, H=h, b=b, a=a, p=3*j+h, q=4*j+h+a)
    rows.append(row)
    for field, value in row.items():
        check(f'construction row{i} {field}', saved['rows'][i][field], '=', value)
    check(f'eta positivity row{i} J premise', j, '>=', 8)
    check(f'eta positivity row{i} H premise', h, '>', 0)
check('construction rows count', len(saved['rows']), '=', 25)
check('eta lower factor', 2*16**8, '<', 27**8)
K, N = sum(r['p'] for r in rows), sum(r['q'] for r in rows)
totals = dict(K=K, N=N, J=sum(r['J'] for r in rows),
              H=sum(r['H'] for r in rows), a=sum(r['a'] for r in rows),
              b=sum(r['b'] for r in rows))
for field, expected in dict(K=397573379, N=630138897, J=66061058,
                           H=199390205, a=166504460, b=9250245).items():
    check(f'total {field}', totals[field], '=', expected)
for field in ('K', 'N'):
    check(f'construction total {field}', saved['totals'][field], '=', totals[field])
check('row24 closing tail', rows[24]['a'], '=', 166504160)

# Each prefix is summed independently from its row subset, not incremented
# from the preceding prefix or copied from the construction certificate.
order = list(range(3,25))+list(range(3))
prefixes = []
for k, input_row in enumerate(order):
    factors = order[:k]
    record = dict(k=k, input_row=input_row,
                  p=sum(rows[i]['p'] for i in factors),
                  q=sum(rows[i]['q'] for i in factors))
    for field, value in record.items():
        check(f'construction prefix{k} {field}',
              saved['cut3_prefixes'][k][field], '=', value)
    prefixes.append(dict(**record, factor_rows=factors))
check('construction prefix count', len(saved['cut3_prefixes']), '=', 25)
check('first group count', len(order[:22]), '=', 22)
for i in range(3,24):
    check(f'growth row{i} tail', rows[i]['a'], '=', 2)
    check(f'growth row{i} H', rows[i]['H'], '>=', 6)
    check(f'growth row{i} J', rows[i]['J'], '>', 0)
check('growth rational lower bound', F(3,2)**6/4, '>', 2)
geometric = F(2**22-1, 2**21)
check('geometric identity', sum((F(1,2)**k for k in range(22)), F(0)), '=', geometric)
check('geometric cap', geometric, '<', 2)

complements = []
for k, factors in ((22, [0,1,2]), (23, [1,2]), (24, [2])):
    p = sum(rows[i]['p'] for i in factors)
    q = sum(rows[i]['q'] for i in factors)
    check(f'complement{k} p', prefixes[k]['p']+p, '=', K)
    check(f'complement{k} q', prefixes[k]['q']+q, '=', N)
    check(f'complement{k} input', order[k], '=', k-22)
    quotient, remainder = divmod(p, 5)
    bound = 8*quotient+2*remainder
    check(f'power decomposition{k}', 5*quotient+remainder, '=', p)
    check(f'power majorant{k}', 3**p, '<', 2**bound)
    check(f'power gap{k}', bound, '<', q)
    check(f'complement{k} direct product', 3**p, '<', 2**q)
    complements.append(dict(k=k, factors=factors, p=p, q=q,
                            quotient=quotient, remainder=remainder, bound=bound))
    original = saved['suffix_products'][24-k]
    check(f'construction complement{k} count', len(original['indices']), '=', len(factors))
    for n, i in enumerate(factors):
        check(f'construction complement{k} factor{n}', original['indices'][n], '=', i)
    for field, value in dict(p=p,q=q,quotient=quotient,remainder=remainder,
                             upper_power_of_two=bound).items():
        check(f'construction complement{k} {field}', original[field], '=', value)
check('small base inequality', 3**5, '<', 2**8)

kap = F(23,11)
lm, lp = F(10584,10**14), F(10585,10**14)
check('imported lower', saved['imported_enclosure']['lower'], '=', lm)
check('imported upper', saved['imported_enclosure']['upper'], '=', lp)
check('enclosure lower positive', lm, '>', 0)
check('enclosure ordered', lm, '<', lp)
check('exponential majorant domain', lp, '<', F(1,2))
check('exponential majorant cap', 1/(1-lp), '<', 2)
cap = kap*(1+8/lm)
threshold = F(2**210,11)
bounds = dict(first22_reciprocal_sum_upper=geometric,
              each_final_reciprocal_prefix_strict_upper=2,
              numerator_strict_upper=8*kap, D_strict_lower=lm,
              s3_strict_upper=cap, coarse_s3_strict_upper=10**12,
              row3_J_required_lower=threshold, strict_separation=threshold-cap)
for field, value in bounds.items():
    check(f'construction bound {field}', saved['bounds'][field], '=', value)
check('printed exact cap', cap, '=', F(2300000000030429,14553))
check('cap below coarse', cap, '<', 10**12)
check('own input J3', rows[3]['J'], '=', 52)
check('guard threshold formula', threshold, '=', F(4,11)*2**(4*rows[3]['J']))
check('coarse below own J3 threshold', 10**12, '<', threshold)

# Replay all recorded comparisons/differences, never trusting success flags.
for record in saved['checks']:
    check('replay: '+record['name'], record['actual'], record['relation'], record['required'])
    check('difference: '+record['name'], record['difference'], '=',
          F(record['actual'])-F(record['required']))

failures = [c['name'] for c in checks if not c['passed']]
data = dict(scope='Independent C106a finite audit only; L104 enclosure imported',
            construction=dict(path=str(SOURCE.relative_to(ROOT)),
                              sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest()),
            rows=rows, totals=totals, cut3_prefixes=prefixes,
            complementary_products=complements,
            imported_enclosure=dict(K=K,N=N,lower=lm,upper=lp), bounds=bounds,
            replayed_construction_checks=len(saved['checks']), checks=checks,
            summary=dict(verdict='ROW3_J_GUARD_FAILURE_CONFIRMED' if not failures else 'AUDIT_FAILED',
                         checks=len(checks),failures=failures),
            limitations='Other49 guards untested; no realization, other-allocation or universal conclusion.')
out = HERE / 'l106-row3-guard-failure-audit-certificate.json'
out.write_text(json.dumps(data, default=str, indent=2)+'\n')
print(f"Verdict={data['summary']['verdict']}; checks={len(checks)}; failures={failures}")
print(f's3 < {cap} < {10**12}; own J3 requires s3 >= {threshold}')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)

#!/usr/bin/env python3
"""Finite rational/affine operands for C104a; universal proof is in C104a.

An exponent pair [constant, slope] represents constant+slope*m.
Imports audited L104's Lambda enclosure, rather than recomputing logs.
No expanded huge powers, parameter sampling or orbit realization.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TABLE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
BOUND = ROOT / 'lemmas/L104-d35-fixed-row0-unit-exclusion.md'
raw = TABLE.read_bytes()
base = [tuple(map(int, r)) for r in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert [i for i, _, _ in base] == list(range(25))
B, kap = 9250245, F(23, 11)
rows = []
for i, j, old_h in base:
    h = 5 if i == 0 else 32670656 if i == 24 else old_h
    budget = [0, 1] if i == 0 else [B, -1] if i == 24 else [0, 0]
    tail = [2+18*budget[0], 18*budget[1]]
    rows.append(dict(i=i, J=j, H=h, b=budget, a=tail,
                     p=3*j+h, q=[4*j+h+tail[0], tail[1]]))
checks = []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b,
              '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation,
                       required=b, difference=a-b, passed=passed))


def evaluate(pair, m):
    return pair[0]+pair[1]*m


check('budget constant', sum(r['b'][0] for r in rows), '=', B)
check('budget slope', sum(r['b'][1] for r in rows), '=', 0)
K = sum(r['p'] for r in rows)
N = [sum(r['q'][d] for r in rows) for d in range(2)]
check('total K', K, '=', 397573379)
check('total N constant', N[0], '=', 630138897)
check('total N slope', N[1], '=', 0)
endpoints = []
for m in (1, B):
    record = dict(m=m, budgets=[], tails=[])
    for r in rows:
        b, a = evaluate(r['b'], m), evaluate(r['a'], m)
        record['budgets'].append(b)
        record['tails'].append(a)
        check(f"endpoint m={m} row{r['i']} budget", b, '>=', 0)
        check(f"endpoint m={m} row{r['i']} tail", a, '>=', 2)
        check(f"endpoint m={m} row{r['i']} congruence", a % 18, '=', 2)
    endpoints.append(record)
check('m=B closing tail2', endpoints[-1]['tails'][24], '=', 2)
check('row0 p', rows[0]['p'], '=', 29)
check('row0 q constant', rows[0]['q'][0], '=', 39)
check('row0 q slope', rows[0]['q'][1], '=', 18)
check('m=1 row0 q', evaluate(rows[0]['q'], 1), '=', 57)

prefixes = []
pk, nq = 0, [0, 0]
for r in rows[1:]+rows[:1]:
    prefixes.append(dict(input_row=r['i'], p=pk, q=nq[:]))
    pk += r['p']
    nq = [nq[d]+r['q'][d] for d in range(2)]
check('full rotated p', pk, '=', K)
for d in range(2):
    check(f'full rotated q coefficient {d}', nq[d], '=', N[d])
for k, prefix in enumerate(prefixes[:24]):
    check(f'prefix{k} parameter slope', prefix['q'][1], '=', 0)
for d in range(2):
    check(f'last prefix q complement {d}', prefixes[24]['q'][d],
          '=', N[d]-rows[0]['q'][d])
check('last prefix p complement', prefixes[24]['p'], '=', K-29)
check('last reciprocal prefix slope', prefixes[24]['q'][1], '=', -18)
check('integer delta lower', 1-1, '=', 0)
check('integer delta upper', B-1, '=', 9250244)
check('decay exponent at m=B', -18*(B-1), '=', -166504392)

# Reproduce the small rational cap from L104's audited imported enclosure.
lm, lp = F(10584, 10**14), F(10585, 10**14)
c01 = F(3**29, 2**57)
check('imported Lambda lower positive', lm, '>', 0)
check('imported Lambda upper below 1/2', lp, '<', F(1, 2))
check('c0(1) bound', c01, '<', F(1, 1000))
check('last reciprocal prefix uniform bound', c01/(1-lp), '<', F(1, 500))
for r in rows[1:24]:
    check(f"row{r['i']} unchanged tail", r['a'][0], '=', 2)
    check(f"row{r['i']} tail slope", r['a'][1], '=', 0)
    check(f"row{r['i']} H floor", r['H'], '>=', 6)
check('ordinary growth floor', F(3, 2)**6/4, '>', 2)
geometric = sum((F(1, 2**k) for k in range(24)), F(0))
check('first24 reciprocal-prefix bound', geometric, '<', 2)
bsum_cap = kap*(2+F(1, 500))
s1_cap = bsum_cap/lm+kap
check('same exact rational root cap', s1_cap, '=', F(82225000004347, 2079))
check('uniform coarse cap', s1_cap, '<', 60000000000)
check('row1 J', rows[1]['J'], '=', 15)
required = F(4, 11)*2**60
check('necessary guard exceeds uniform cap', required, '>', 60000000000)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='All integers 1<=m<=9250245; literal d35; b0=m,b24=B-m,others0',
    sources=[dict(path=str(p.relative_to(ROOT)),
                  sha256=hashlib.sha256(p.read_bytes()).hexdigest())
             for p in (TABLE, BOUND)],
    rows=rows, K=K, N_affine=N, cut1_prefixes=prefixes,
    domain_endpoints=endpoints,
    imported_L104_enclosure=dict(Lambda_lower=lm, Lambda_upper=lp,
                                status='audited mathematical input; not recertified here'),
    symbolic=dict(
        first24_prefixes='constant in m',
        last_prefix_inverse='c0(1)*exp(Lambda)*2^(-18*(m-1))',
        B1='A+eta0*c0(1)*exp(Lambda)*2^(-18*(m-1)), A constant positive',
        root='n1(m)=B1(m)/(exp(Lambda)-1)',
        conclusion='s1(m)<=s1(1)<82225000004347/2079'),
    bounds=dict(c0_at1=c01, geometric_sum=geometric,
                last_reciprocal_upper=c01/(1-lp), B1_coarse_upper=bsum_cap,
                s1_uniform_upper=s1_cap, coarse_cap=60000000000,
                row1_J_required=required, guard_gap_above_coarse=required-60000000000),
    checks=checks,
    summary=dict(verdict='INFEASIBLE' if not failures else 'UNCERTIFIED',
                 checks=len(checks), failures=failures, parameter_samples=0,
                 domain_endpoint_checks='affine-domain bookkeeping, not family sampling',
                 independent_critical_audit=False),
    limitations='C104a supplies universal algebra; no other support, order, '
                'realization, actual-word or universal-descent conclusion.')
out = HERE / 'd35-row0-row24-family-certificate.json'
out.write_text(json.dumps(result, default=str, indent=2)+'\n')
print(f"Verdict: {result['summary']['verdict']}; checks={len(checks)}; failures={failures}")
print(f'K={K}; N(m)={N}; last reciprocal-prefix exponent slope=-18')
print(f'Uniform s1 < {s1_cap} < 60000000000; required >= {required}')
print(f'Gap above coarse cap: {required-60000000000}')
print(f'Closing tail at m={B}: {endpoints[-1]["tails"][24]} (required 2)')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)

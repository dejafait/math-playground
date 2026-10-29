#!/usr/bin/env python3
"""L105 finite operands; uniform symbolic proof is in the canonical lemma.
Affine triples encode constant + coefficient*m + coefficient*u.
Imports L104's audited Lambda interval only after matching exact totals.
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
base = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', TABLE.read_text(), re.M)]
assert [row[0] for row in base] == list(range(25))
B, kap = 9250245, F(23, 11)
rows, checks = [], []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b, '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation, required=b,
                       difference=a-b, passed=passed))


def ev(v, m, u):
    return v[0]+v[1]*m+v[2]*u


for i, j, old_h in base:
    h = 5 if i == 0 else 32670656 if i == 24 else old_h
    b = [0, 1, 0] if i == 0 else [0, 0, 1] if i == 1 else [B, -1, -1] if i == 24 else [0, 0, 0]
    a = [2+18*b[0], 18*b[1], 18*b[2]]
    rows.append(dict(i=i, J=j, H=h, b=b, a=a, p=3*j+h,
                     q=[4*j+h+a[0], a[1], a[2]]))
    check(f'row{i} J positive', j, '>', 0)
    check(f'row{i} H positive', h, '>', 0)
K = sum(r['p'] for r in rows)
N = [sum(r['q'][d] for r in rows) for d in range(3)]
check('K', K, '=', 397573379)
for d in range(3):
    check(f'N coefficient{d}', N[d], '=', [630138897, 0, 0][d])
    check(f'budget coefficient{d}', sum(r['b'][d] for r in rows), '=', [B, 0, 0][d])
vertices = []
for m, u in [(1, 1), (1, B-1), (B-1, 1)]:
    v = dict(m=m, u=u, budgets=[], tails=[])
    for r in rows:
        b, a = ev(r['b'], m, u), ev(r['a'], m, u)
        v['budgets'].append(b)
        v['tails'].append(a)
        check(f'vertex({m},{u}) row{r["i"]} budget', b, '>=', 0)
        check(f'vertex({m},{u}) row{r["i"]} tail', a, '>=', 2)
        check(f'vertex({m},{u}) row{r["i"]} tail residue', a % 18, '=', 2)
    vertices.append(v)
for v in vertices[1:]:
    check(f'closing tail at ({v["m"]},{v["u"]})', v['tails'][24], '=', 2)
order = rows[2:]+rows[:2]
p, q, prefixes = 0, [0, 0, 0], []
for r in order:
    prefixes.append(dict(input_row=r['i'], p=p, q=q[:]))
    p += r['p']
    q = [q[d]+r['q'][d] for d in range(3)]
check('rotated full p', p, '=', K)
for d in range(3):
    check(f'rotated full q{d}', q[d], '=', N[d])
for k, pref in enumerate(prefixes[:23]):
    for d in (1, 2):
        check(f'prefix{k} parameter coefficient{d}', pref['q'][d], '=', 0)
for k, remaining in [(23, rows[:2]), (24, rows[1:2])]:
    check(f'prefix{k} p complement', prefixes[k]['p'], '=', K-sum(r['p'] for r in remaining))
    for d in range(3):
        check(f'prefix{k} q complement{d}', prefixes[k]['q'][d], '=', N[d]-sum(r['q'][d] for r in remaining))
for r in rows[2:24]:
    check(f'row{r["i"]} H floor', r['H'], '>=', 6)
    for d in range(3):
        check(f'row{r["i"]} tail coefficient{d}', r['a'][d], '=', [2, 0, 0][d])
check('ordinary growth floor', F(3, 2)**6/4, '>', 2)
lm, lp = F(10584, 10**14), F(10585, 10**14)
c0, c1 = F(3**29, 2**57), F(3**117, 2**152)
for i, expected_p, expected_q in [(0, 29, 57), (1, 117, 152)]:
    check(f'row{i} numerator exponent', rows[i]['p'], '=', expected_p)
    check(f'row{i} denominator exponent at(1,1)', ev(rows[i]['q'], 1, 1), '=', expected_q)
check('Lambda lower positive', lm, '>', 0)
check('Lambda upper below half', lp, '<', F(1, 2))
check('exp upper below2', 1/(1-lp), '<', 2)
check('c0 maximum', c0, '<', F(1, 1000))
check('c1 maximum', c1, '<', 2**34)
geometric = sum((F(1, 2**k) for k in range(23)), F(0))
check('first23 reciprocal sum', geometric, '<', 2)
bcap = kap*(2+F(1001, 1000)*2**35)
scap = bcap/lm+kap
required = F(4, 11)*2**112
check('uniform s2 cap', scap, '<', 10**21)
check('row2 J', rows[2]['J'], '=', 28)
check('own-input guard exceeds cap', required, '>', 10**21)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(scope='literal d35; integer m,u>=1,m+u<=9250245; b0=m,b1=u,b24=B-m-u,others0',
    sources=[dict(path=str(p.relative_to(ROOT)), sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in (TABLE, BOUND)],
    rows=rows, K=K, N_affine=N, cut2_prefixes=prefixes, domain_vertices=vertices,
    imported_L104_enclosure=dict(lower=lm, upper=lp, status='audited input; logs not recertified'),
    symbolic=dict(first23='independent of m,u; reciprocals <=2^-k',
                  prefix23_inverse='c0(m)*c1(u)*exp(Lambda)',
                  prefix24_inverse='c1(u)*exp(Lambda)',
                  root='s2=kappa+B2/(exp(Lambda)-1)',
                  c0='(3^29/2^57)*2^(-18*(m-1))',
                  c1='(3^117/2^152)*2^(-18*(u-1))'),
    bounds=dict(c0_maximum=c0, c1_maximum=c1, geometric_sum=geometric,
                prefix23_upper=F(2**35, 1000), prefix24_upper=2**35,
                B2_upper=bcap, s2_upper=scap, coarse_cap=10**21,
                row2_J_required=required, guard_gap=required-10**21),
    checks=checks, summary=dict(verdict='INFEASIBLE' if not failures else 'UNCERTIFIED',
        checks=len(checks), failures=failures, parameter_samples=0, independent_audit=False),
    limitations='Uniformity and closure require L105 symbolic proof; no actual-word transfer or universal descent.')
out = HERE / 'd35-row0-row1-row24-certificate.json'
out.write_text(json.dumps(result, default=str, indent=2)+'\n')
print(f'Verdict: {result["summary"]["verdict"]}; checks={len(checks)}; failures={failures}')
print(f'K={K}; N affine={N}; full triangle includes closing tail2')
print(f'Uniform s2 < {scap} < {10**21}; required >= {required}')
print(f'Guard gap above coarse cap: {required-10**21}')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)

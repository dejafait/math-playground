#!/usr/bin/env python3
"""Independent finite audit of L104; symbolic identities are in the lemma.

No imports from the construction, no huge integer-power expansion, and
no parameter samples. Check saved operands rather than trusting flags.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
source = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
certificate = HERE / 'd35-row0-unit-certificate.json'
saved = json.loads(certificate.read_text())
checks = []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b,
              '>=': a >= b, '<=': a <= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation,
                       required=b, difference=a-b, passed=passed))


# Independent transcription of the canonical table, before the H changes.
pairs = [
    (8,40), (15,72), (28,134), (52,249), (98,467),
    (184,877), (347,1650), (653,3106), (1230,5849),
    (2317,11018), (4365,20756), (8224,39104), (15494,73672),
    (29191,138802), (54998,261511), (103621,492705),
    (195229,928293), (367827,1748976), (693015,3295208),
    (1305695,6208431), (2460032,11697176), (4634896,22038409),
    (8732512,41522114), (16452748,78230965), (30998279,32670621),
]
raw = source.read_bytes()
parsed = [tuple(map(int, line.strip('|').split('|')))
          for line in raw.decode().splitlines()
          if re.fullmatch(r'\|\d+\|\d+\|\d+\|', line)]
assert parsed == [(i, j, h) for i, (j, h) in enumerate(pairs)]
assert saved['table_source']['sha256'] == hashlib.sha256(raw).hexdigest()
rows = []
for i, (j, h) in enumerate(pairs):
    h += -35 if i == 0 else 35 if i == 24 else 0
    b = {0: 1, 24: 9250244}.get(i, 0)
    a = 2 + 18*b
    r = dict(i=i, J=j, H=h, b=b, a=a, p=3*j+h, q=4*j+h+a)
    assert r == saved['rows'][i]
    rows.append(r)
    check(f'row{i} J positive', j, '>', 0)
    check(f'row{i} H positive', h, '>', 0)
check('sum budgets', sum(r['b'] for r in rows), '=', 9250245)
K = 3*sum(r['J'] for r in rows)+sum(r['H'] for r in rows)
N = 4*sum(r['J'] for r in rows)+sum(r['H']+r['a'] for r in rows)
check('K', K, '=', 397573379)
check('N', N, '=', 630138897)
check('saved K', saved['K'], '=', K)
check('saved N', saved['N'], '=', N)
kap = F(23, 11)
check('saved kappa', saved['kappa'], '=', kap)
order = list(range(1,25))+[0]
prefixes = []
for k, i in enumerate(order):
    # Direct resummation, independent of the construction's running totals.
    p = sum(rows[t]['p'] for t in order[:k])
    q = sum(rows[t]['q'] for t in order[:k])
    prefix = dict(input_row=i, p=p, q=q)
    assert prefix == saved['cut1_prefixes'][k]
    prefixes.append(prefix)
    if k < 24:
        assert order[:k] == list(range(1,k+1))
check('last prefix p', prefixes[-1]['p'], '=', K-rows[0]['p'])
check('last prefix q', prefixes[-1]['q'], '=', N-rows[0]['q'])
assert sorted(order) == list(range(25))
assert [(i+1) % 25 for i in order] == order[1:]+order[:1]
check('row0 p', rows[0]['p'], '=', 29)
check('row0 q', rows[0]['q'], '=', 57)
for r in rows[1:24]:
    check(f"row{r['i']} ordinary tail", r['a'], '=', 2)
    check(f"row{r['i']} H growth premise", r['H'], '>=', 6)


def direct_log(t):
    x = (t-1)/(t+1)
    terms = [2*x**(2*k+1)/(2*k+1) for k in range(128)]
    lo = sum(terms, F(0))
    rem = 2*x**257/(257*(1-x*x))
    return dict(argument=t, x=x, terms=terms, lower=lo,
                remainder_upper=rem, upper=lo+rem)


# Evaluate log3 directly at x=1/2, without binary reduction or rounding.
logs = {name: direct_log(F(t)) for name, t in [('log2',2), ('log3',3)]}
l2, u2 = logs['log2']['lower'], logs['log2']['upper']
l3, u3 = logs['log3']['lower'], logs['log3']['upper']
lo, hi = N*l2-K*u3, N*u2-K*l3
lm, lp = F(10584,10**14), F(10585,10**14)
check('independent Lambda lower', lo, '>', lm)
check('independent Lambda upper', hi, '<', lp)
independent_error = N*(u2-l2)+K*(u3-l3)
check('independent complete width', hi-lo, '=', independent_error)
check('independent amplified error', independent_error, '<', F(1,10**68))

# Check every original summand and both original outward enclosures.
rebuilt = {}
for name, t in [('log2', F(2)), ('log_three_halves', F(3,2))]:
    record = saved['logarithms'][name]
    x = (t-1)/(t+1)
    check(name+' argument', record['argument'], '=', t)
    check(name+' x', record['x'], '=', x)
    assert len(record['rounded_terms']) == 96
    for m, floor in enumerate(record['rounded_terms']):
        term = 2*x**(2*m+1)/(2*m+1)
        check(f'{name} floor{m} lower', F(floor,2**192), '<=', term)
        check(f'{name} floor{m} upper', term, '<', F(floor+1,2**192))
    rounding = F(96,2**192)
    remainder = F(9,4*193*3**193)
    actual_remainder_bound = 2*x**193/(193*(1-x*x))
    check(name+' remainder majorant', actual_remainder_bound, '<=', remainder)
    lower = F(sum(record['rounded_terms']),2**192)
    upper = lower+rounding+remainder
    for key, value in [('rounding_upper',rounding), ('remainder_upper',remainder),
                       ('lower',lower), ('upper',upper)]:
        check(name+' saved '+key, record[key], '=', value)
    rebuilt[name] = (lower,upper)
ol2, ou2 = rebuilt['log2']
olv, ouv = rebuilt['log_three_halves']
ol3, ou3 = ol2+olv, ou2+ouv
olo, ohi = N*ol2-K*ou3, N*ou2-K*ol3
for key, value in [('log3_lower',ol3), ('log3_upper',ou3),
                   ('Lambda_lower',olo), ('Lambda_upper',ohi),
                   ('coarse_Lambda_lower',lm), ('coarse_Lambda_upper',lp)]:
    check('saved '+key, saved['logarithms'][key], '=', value)
check('original Lambda lower', olo, '>', lm)
check('original Lambda upper', ohi, '<', lp)
original_error = (N+2*K)*(F(96,2**192)+F(9,4*193*3**193))
check('original full amplified width', ohi-olo, '=', original_error)
check('original amplified error', original_error, '<', F(1,10**46))
check('independent enclosure inside original lower', lo, '>', olo)
check('independent enclosure inside original upper', hi, '<', ohi)

c0 = F(3**29,2**57)
geom = 2-F(1,2**23)
last = c0/(1-lp)
coarse = kap*(2+F(1,500))
ncap = coarse/lm
scap = ncap+kap
guard = F(4*2**(4*rows[1]['J']),11)
bounds = dict(c0=c0, ordinary_multiplier_floor=F(729,256),
              geometric_sum=geom, last_reciprocal_upper=last,
              B1_upper=kap*(geom+last), B1_coarse_upper=coarse,
              n1_upper=ncap, s1_upper=scap,
              required_s1_from_row1_J=guard, coarse_s1_upper=60000000000,
              gap_above_coarse_cap=guard-60000000000)
for key, value in bounds.items():
    check('saved bound '+key, saved['bounds'][key], '=', value)
check('ordinary growth', F(729,256), '>', 2)
check('small row0 multiplier', c0, '<', F(1,1000))
check('positive denominator lower', lm, '>', F(1,10**10))
check('exponential majorant domain', lp, '<', F(1,2))
check('exponential majorant cap', 1/(1-lp), '<', 2)
check('geometric cap', geom, '<', 2)
check('last reciprocal cap', last, '<', F(1,500))
check('B1 cap', coarse, '=', F(2093,500))
check('n1 cap identity', ncap, '=', F(7475000000000,189))
check('s1 cap identity', scap, '=', F(82225000004347,2079))
check('s1 coarse cap', scap, '<', 60000000000)
check('own input row1 J', rows[1]['J'], '=', 15)
check('guard identity', guard, '=', F(4611686018427387904,11))
check('guard contradiction', guard, '>', 60000000000)

# Re-evaluate every saved check as well; never accept its success flag.
for item in saved['checks']:
    check('original operand comparison: '+item['name'],
          item['actual'],item['relation'],item['required'])
    check('original difference: '+item['name'],item['difference'], '=',
          F(item['actual'])-F(item['required']))

# A compact outward decimal enclosure, still using integer division only.
grid = 10**30
gridlo = F((lo*grid).__floor__(),grid)
gridhi = F(-(-hi*grid).__floor__(),grid)
check('displayed lower outward', gridlo, '<=', lo)
check('displayed upper outward', gridhi, '>=', hi)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope=saved['scope'], rows=rows, K=K, N=N, cut1_prefixes=prefixes,
    source_sha256=hashlib.sha256(raw).hexdigest(),
    construction_sha256=hashlib.sha256(certificate.read_bytes()).hexdigest(),
    independent_logs=logs,
    cancellation=dict(lower=lo,upper=hi,original_lower=olo,original_upper=ohi,
                      original_amplified_error=original_error,
                      independent_amplified_error=independent_error,
                      grid_lower=gridlo,grid_upper=gridhi,
                      required_lower=lm,required_upper=lp),
    bounds=bounds, checks=checks,
    summary=dict(verdict='PASS' if not failures else 'FAIL', checks=len(checks),
                 failures=failures, original_checks_recomputed=len(saved['checks']),
                 rounded_terms_verified=192, prefix_records_verified=25,
                 parameter_samples=0,
                 symbolic_review='L104 independent critical audit section',
                 limitations='Fixed real allocation only; no actual-word or universal conclusion'))
path = HERE / 'd35-row0-unit-audit-certificate.json'
path.write_text(json.dumps(result,default=str,indent=2)+'\n')
print(f"Audit: {result['summary']['verdict']}; checks={len(checks)}; failures={failures}")
print(f'Independent Lambda: {gridlo} < Lambda < {gridhi}; required ({lm}, {lp})')
print('Amplified enclosure errors: original <1e-46; independent <1e-68')
print(f's1 < {scap} < 60000000000; required s1 >= {guard}')
print(f'Gap above coarse cap: {guard-60000000000}')
print(f'Certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)

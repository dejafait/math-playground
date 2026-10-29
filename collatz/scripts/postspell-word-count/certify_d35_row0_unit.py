#!/usr/bin/env python3
"""Exact finite evidence for the approved fixed positive-row0 allocation.

L104 gives the symbolic cyclic-root argument. No expanded huge root,
parameter sampling, minimum, seed or integer realization is used.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
source = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
raw = source.read_bytes()
base = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert [i for i, _, _ in base] == list(range(25))
B, kap = 9250245, F(23, 11)
rows = []
for i, j, old_h in base:
    h = 5 if i == 0 else 32670656 if i == 24 else old_h
    b = 1 if i == 0 else B-1 if i == 24 else 0
    a = 2+18*b
    rows.append(dict(i=i, J=j, H=h, b=b, a=a,
                     p=3*j+h, q=4*j+h+a))
checks = []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b,
              '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation,
                       required=b, difference=a-b, passed=passed))


check('budget sum', sum(r['b'] for r in rows), '=', B)
for r in rows:
    check(f"row{r['i']} J domain", r['J'], '>=', 2)
    check(f"row{r['i']} H domain", r['H'], '>=', 3)
    check(f"row{r['i']} tail congruence", r['a'] % 18, '=', 2)
    check(f"row{r['i']} nonnegative budget", r['b'], '>=', 0)
K, N = sum(r['p'] for r in rows), sum(r['q'] for r in rows)
check('total K', K, '=', 397573379)
check('total N', N, '=', 630138897)
check('row0 p', rows[0]['p'], '=', 29)
check('row0 q', rows[0]['q'], '=', 57)
c0 = F(3**29, 2**57)
check('row0 multiplier', c0, '<', F(1, 1000))

# L055's 96-term, 192-bit outward logarithm method. For t=2,3,
# only 3 needs binary reduction (3=2*(3/2)). Store every rounded term.
BITS, TERMS = 192, 96


def base_log(t):
    x = (t-1)/(t+1)
    assert 0 <= x <= F(1, 3)
    scale = 2**BITS
    terms = [2*x**(2*m+1)/(2*m+1) for m in range(TERMS)]
    rounded = [(v*scale).__floor__() for v in terms]
    lo = F(sum(rounded), scale)
    rounding = F(TERMS, scale)
    remainder = F(9, 4*(2*TERMS+1)*3**(2*TERMS+1))
    hi = lo+rounding+remainder
    return lo, hi, dict(argument=t, x=x, rounded_terms=rounded,
                        rounding_upper=rounding, remainder_upper=remainder,
                        lower=lo, upper=hi)


l2, u2, log2_record = base_log(F(2))
lv, uv, logv_record = base_log(F(3, 2))
l3, u3 = l2+lv, u2+uv
lam_lower, lam_upper = N*l2-K*u3, N*u2-K*l3
lm, lp = F(10584, 10**14), F(10585, 10**14)
check('Lambda certified lower', lam_lower, '>', lm)
check('Lambda certified upper', lam_upper, '<', lp)
check('Lambda lower above 1e-10', lm, '>', F(1, 10**10))
check('Lambda upper below 1/2', lp, '<', F(1, 2))
check('exp(Lambda) rational upper', 1/(1-lp), '<', 2)

# For rows1,...,23, a=2 and H>=6 imply c>(3/2)^6/4>2.
small_growth = F(3, 2)**6/4
check('uniform ordinary multiplier floor', small_growth, '>', 2)
for r in rows[1:24]:
    check(f"row{r['i']} ordinary tail", r['a'], '=', 2)
    check(f"row{r['i']} H floor for growth", r['H'], '>=', 6)

# Every prefix at the original cut and at cut1 is kept factored.
# A pair (p,q) denotes 3^p/2^q; no huge powers are expanded.
prefixes = []
pk = pn = 0
for r in rows[1:]+rows[:1]:
    prefixes.append(dict(input_row=r['i'], p=pk, q=pn))
    pk, pn = pk+r['p'], pn+r['q']
check('cut1 full p', pk, '=', K)
check('cut1 full q', pn, '=', N)
check('prefix before row0 p', prefixes[-1]['p'], '=', K-29)
check('prefix before row0 q', prefixes[-1]['q'], '=', N-57)
geometric = sum((F(1, 2**k) for k in range(24)), F(0))
check('first24 reciprocal-prefix majorant', geometric, '<', 2)
last_reciprocal_upper = c0/(1-lp)
check('last reciprocal-prefix upper', last_reciprocal_upper, '<', F(1, 500))
bsum_upper = kap*(geometric+last_reciprocal_upper)
coarse_bsum_upper = kap*(2+F(1, 500))
check('B1 explicit upper', bsum_upper, '<', coarse_bsum_upper)
check('B1 coarse upper', coarse_bsum_upper, '<', 5)
n1_upper = coarse_bsum_upper/lm
s1_upper = n1_upper+kap
check('n1 root cap', n1_upper, '<', 50000000000)
check('s1 cap', s1_upper, '<', 60000000000)
check('own input row1 J', rows[1]['J'], '=', 15)
required_s1 = F(4, 11)*2**(4*rows[1]['J'])
check('row1 necessary J lower bound exceeds root cap',
      60000000000, '<', required_s1)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='Only b0=1,b24=9250244,b1=...=b23=0 in literal d35 real system',
    table_source=dict(path=str(source.relative_to(ROOT)),
                      sha256=hashlib.sha256(raw).hexdigest()),
    rows=rows, K=K, N=N, kappa=kap, cut1_prefixes=prefixes,
    exact_root=dict(c='3^(3J+H)/2^(4J+H+a)',
                    eta='23/11-(12/11)*(16/27)^J-(16/27)^J*(2/3)^H',
                    D='2^N/3^K-1',
                    B1='sum eta_i/P_i in order1,...,24,0',
                    n1='B1/D', closure='product c_i=3^K/2^N'),
    logarithms=dict(log2=log2_record, log_three_halves=logv_record,
                    log3_lower=l3, log3_upper=u3,
                    Lambda_lower=lam_lower, Lambda_upper=lam_upper,
                    coarse_Lambda_lower=lm, coarse_Lambda_upper=lp),
    bounds=dict(c0=c0, ordinary_multiplier_floor=small_growth,
                geometric_sum=geometric,
                last_reciprocal_upper=last_reciprocal_upper,
                B1_upper=bsum_upper, B1_coarse_upper=coarse_bsum_upper,
                n1_upper=n1_upper, s1_upper=s1_upper,
                required_s1_from_row1_J=required_s1,
                coarse_s1_upper=60000000000,
                gap_above_coarse_cap=required_s1-60000000000),
    checks=checks,
    summary=dict(verdict='INFEASIBLE' if not failures else 'UNCERTIFIED',
                 decisive_constraint='own-input non-strict J at row1',
                 checks=len(checks), failures=failures,
                 all_endpoints_and_closure='retained by symbolic cyclic root',
                 domain_and_other_guards='not needed after one necessary violation',
                 parameter_samples=0, independent_critical_audit=False),
    limitations='Only this fixed real allocation is excluded; no row0 support '
                'exhaustion, arbitrary word transfer or universal descent.')
path = HERE / 'd35-row0-unit-certificate.json'
path.write_text(json.dumps(result, default=str, indent=2)+'\n')
print(f"Verdict: {result['summary']['verdict']}; checks={len(checks)}; failures={failures}")
print(f'Lambda: {lm} < Lambda < {lp}; required >0')
print(f'B1 < {coarse_bsum_upper} < 5; D > {lm} > 1e-10')
print(f's1 < {s1_upper} < 60000000000; row1 J requires s1 >= {required_s1}')
print(f'Necessary-bound gap above coarse cap: {required_s1-60000000000}')
print(f'Certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)

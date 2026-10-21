#!/usr/bin/env python3
"""One approved changed-table C077a certificate, using exact rationals only.

No table search, survivor arithmetic, giant expanded powers, or feasibility
test is performed. All inequalities and analytic remainders go to disk.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
raw = SOURCE.read_bytes()
original = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert len(original) == 25 and [i for i, _, _ in original] == list(range(25))
table = [(i, j, 39 if i == 0 else 32670622 if i == 24 else h)
         for i, j, h in original]
r, p, q, B, tau = 25, 23, 24, 9250245, 2
kappa = Q(23, 11)
checks = []


def check(name, actual, relation, required):
    a, b = Q(actual), Q(required)
    ok = {'<': a < b, '<=': a <= b, '=': a == b,
          '>': a > b, '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=str(a), relation=relation,
                       required=str(b), difference=str(a-b), passed=ok))


def log_interval(argument, count=100):
    z = (argument-1)/(argument+1)
    assert 0 < z <= Q(1, 2)
    terms = [2*z**(2*k+1)/(2*k+1) for k in range(count)]
    lower = sum(terms, Q(0))
    remainder = 2*z**(2*count+1)/((2*count+1)*(1-z*z))
    return dict(argument=argument, z=z, count=count, terms=terms,
                lower=lower, remainder_upper=remainder, upper=lower+remainder)


logs = {name: log_interval(x) for name, x in
        [('2', Q(2)), ('3', Q(3)), ('11/4', Q(11, 4))]}
K = sum(3*j+h for _, j, h in table)
N = sum(4*j+h for _, j, h in table)+2*r+18*B
check('sum J', sum(j for _, j, _ in table), '=', 66061058)
check('sum H', sum(h for _, _, h in table), '=', 199390205)
check('K', K, '=', 397573379)
check('N', N, '=', 630138897)
check('full allocated tail sum', 2*r+18*B, '=', 166504460)
lm, lp = Q(10584, 10**14), Q(10585, 10**14)
lambda_interval = [N*logs['2']['lower']-K*logs['3']['upper'],
                   N*logs['2']['upper']-K*logs['3']['lower']]
check('fresh Lambda lower', lm, '<', lambda_interval[0])
check('fresh Lambda upper', lambda_interval[1], '<', lp)
check('positive lambda lower', lm, '>', 0)
check('lambda upper below one', lp, '<', 1)
S = 10**12
ell, u, v = Q(693147180559, S), Q(1098612288669, S), Q(1011600911679, S)
check('positive ell', ell, '>', 0)
check('ell below log2', ell, '<', logs['2']['lower'])
check('u above log3', u, '>', logs['3']['upper'])
check('v above log11over4', v, '>', logs['11/4']['upper'])
check('order v=2 above log11over4', Q(2), '>', logs['11/4']['upper'])
exp_terms = {T: [Q(T)**k/factorial(k) for k in range(41)] for T in (24, 27)}
exp_lower = {T: sum(terms, Q(0)) for T, terms in exp_terms.items()}
prefixes = []
A = D = 0
for i, j, h in table:
    prefixes.append(dict(i=i, A=A, D=D))
    A += 3*j+h
    D += 4*j+h+2
check('closing base odd exponent', A, '=', K)
check('closing base denominator plus budget', D+18*B, '=', N)

# O: all offsets use a proved common H floor, all margins are recomputed.
O_cap = 23*r/(11*lm)+kappa
check('O cap below exp27 partial sum', O_cap, '<', exp_lower[27])
d_upper = Q(81, 44)-Q(3, 11)*Q(3, 2)**39
order_offsets, order_margins = [], []
for i, j, h in table:
    check(f'O row {i} H floor', h, '>=', 39)
    check(f'O row {i} tail2 offset upper', d_upper, '<', 0)
    order_offsets.append(dict(i=i, H=h, H_floor=39, d_upper=d_upper))
for k in range(r-1):
    a, d = prefixes[k]['A'], prefixes[k]['D']
    margin = 4*table[k+1][1]*ell-27-2-a*u+d*ell
    check(f'O displacement {k}', margin, '>', 0)
    order_margins.append(dict(k=k, row=k+1, A=a, D=d, margin=margin))

# S: guard-conditioned root cap, every early offset, every recipient.
E = Q(23*(r-1), 4*2**(4*table[1][1])-23)
check('S residual positive', lm-E, '>', 0)
S_root = kappa/(lm-E)+kappa
S_cap = Q(20*10**9)
check('S root below U', S_root, '<', S_cap)
check('S U below exp24 partial sum', S_cap, '<', exp_lower[24])
Q_early_lower = Q(12, 11)*Q(3, 2)**39+1
support_offsets, support_margins = [], []
for i, j, h in table[:p]:
    check(f'S row {i} H floor', h, '>=', 39)
    check(f'S row {i} tail20 Q lower', Q_early_lower, '>', kappa*2**20)
    support_offsets.append(dict(i=i, H=h, H_floor=39, Q_lower=Q_early_lower))
    a, d = prefixes[i+1]['A'], prefixes[i+1]['D']
    margin = (d+18+4*table[i+1][1])*ell-24-v-a*u
    check(f'S recipient {i}', margin, '>', 0)
    support_margins.append(dict(j=i, input=i+1, A=a, D=d, margin=margin))

# C: eta_q >= eta_0 follows from both exponents and bases in (0,1).
eta0 = kappa-Q(12, 11)*Q(16, 27)**8-Q(16, 27)**8*Q(2, 3)**39
e = Q(2)
check('C eta0 above e', eta0, '>', e)
check('C eta_q J comparison', table[q][1], '>=', table[0][1])
check('C eta_q H comparison', table[q][2], '>=', table[0][2])
domain_lower = e*(1-lp)/lp
check('C uniform unshifted domain', domain_lower, '>=', 47)
tails = [2+18*tau if i == p else 2+18*(B-tau) if i == q else 2
         for i in range(r)]
check('C boundary tail sum', sum(tails), '=', 2*r+18*B)
check('C boundary p tail', tails[p], '=', 38)
check('C boundary q tail', tails[q], '=', 166504376)
# Row 0's multiplier is computed with changed H=39; all later incoming
# factors (rows 1..23) dominate the explicitly verified (15,72,38) factor.
c0 = Q(3**63, 2**73)
c_baseline = Q(3**117, 2**170)
check('C row0 multiplier lower', c0, '>', 10**8)
check('C other incoming multiplier baseline', c_baseline, '>', 2)
factor_certificates = [dict(i=0, J=8, H=39, a=2, exact_multiplier=c0,
                            lower=Q(10**8))]
for i, j, h in table[1:q]:
    check(f'C factor {i} J floor', j, '>=', 15)
    check(f'C factor {i} H floor', h, '>=', 72)
    check(f'C factor {i} tail ceiling', tails[i], '<=', 38)
    factor_certificates.append(dict(i=i, J=j, H=h, a=tails[i],
                                    baseline=c_baseline, lower=Q(2)))
L = [Q(1)]+[Q(10**8*2**(i-1)) for i in range(1, r)]
incoming = [dict(i=i, A=prefixes[i]['A'],
                 denominator_exponent=prefixes[i]['D']+(36 if i == q else 0),
                 lower=L[i], reciprocal=1/L[i]) for i in range(r)]
# Multiplication of the certified factor lower bounds gives all L_i;
# this avoids expanding the huge exact prefixes 3^A/2^denominator.
for i in range(1, r):
    check(f'C prefix lower induction {i}',
          L[i-1]*factor_certificates[i-1]['lower'], '=', L[i])
C_Q = kappa*(1+Q(2, 10**8))
check('C Q bounds all 25 inverse prefixes', kappa*sum(1/x for x in L), '<=', C_Q)
C_required = C_Q/lm+C_Q+kappa/L[q]
C_U = C_Q/lm+C_Q+kappa
check('C normalized cap below U', C_required, '<=', C_U)
check('C U below 20 billion', C_U, '<', 20*10**9)
check('C U below exp24 partial sum', C_U, '<', exp_lower[24])
aq, dq = incoming[q]['A'], incoming[q]['denominator_exponent']
check('C incoming odd exponent', aq, '=', 271907920)
check('C incoming denominator exponent', dq, '=', 306970783)
F = 24+aq*u-(dq+4*table[q][1])*ell+v
check('C final strict boundary margin', F, '<', 0)

integer_checks = dict(
    r_at_least_three=r >= 3, budget_nonnegative=B >= 0,
    cutoff_admitted=0 <= tau <= B,
    indexed_rows=[i for i, _, _ in table] == list(range(r)),
    pair_domain=all(j >= 2 and h >= 3 for _, j, h in table),
    increasing_J=all(table[i][1] < table[i+1][1] for i in range(q)),
    changed_rows_only=[(i, h-old_h) for (i, j, h), (_, old_j, old_h)
                       in zip(table, original) if (j, h) != (old_j, old_h)] == [(0, -1), (24, 1)],
    order_indices=[x['k'] for x in order_margins] == list(range(24)),
    support_indices=[x['j'] for x in support_margins] == list(range(23)),
    all_25_incoming=[x['i'] for x in incoming] == list(range(25)),
    all_boundary_tails=all(a >= 2 and a % 18 == 2 for a in tails),
    final_tail_at_B=2+18*(B-B) == 2,
    c0_exponents=(3*table[0][1]+table[0][2],
                  4*table[0][1]+table[0][2]+tails[0]) == (63, 73))
failures = [x['name'] for x in checks if not x['passed']]
failures += [name for name, ok in integer_checks.items() if not ok]
summary = dict(rational_checks=len(checks), integer_checks=len(integer_checks),
               min_order_margin=min(x['margin'] for x in order_margins),
               min_support_margin=min(x['margin'] for x in support_margins),
               cutoff_margin=F, failures=failures,
               verdict='ALL C077a DATA TESTS CERTIFIED' if not failures else 'FAILED TESTS')
result = dict(
    target='One changed-H table: all C077a data tests, no survivor arithmetic',
    source=dict(path=str(SOURCE.relative_to(ROOT)), sha256=hashlib.sha256(raw).hexdigest()),
    table=table, totals=dict(r=r, B=B, tau=tau, K=K, N=N),
    analytic_proof='For 0<z<=1/2, sum k=0..m-1 of 2*z^(2k+1)/(2k+1) '
                   'is below log((1+z)/(1-z)); the positive remainder is at most '
                   '2*z^(2m+1)/((2m+1)*(1-z^2)). Positive exponential partial '
                   'sums are strict lower bounds. All arithmetic is exact.',
    logs=logs, lambda_interval=lambda_interval, exp_terms=exp_terms,
    O=dict(lambda_lower=lm, T=27, ell=ell, u=u, v=Q(2), cap=O_cap,
           offsets=order_offsets, margins=order_margins),
    S=dict(lambda_lower=lm, E=E, residual=lm-E, root_cap=S_root,
           U=S_cap, T=24, ell=ell, u=u, v=v,
           offsets=support_offsets, margins=support_margins),
    C=dict(lambda_lower=lm, lambda_upper=lp, e=e, eta0=eta0,
           eta_q_lower_justification='J_q>=J_0, H_q>=H_0; both subtracted bases lie in (0,1)',
           domain_lower=domain_lower, boundary_tails=tails,
           factor_certificates=factor_certificates, incoming=incoming,
           prefix_proof='C_0=L_0=1; C_(i+1)=C_i*c_i>=L_i*factor_lower_i=L_(i+1)',
           Q=C_Q, normalized_cap=C_required, U=C_U, T=24,
           ell=ell, u=u, v=v, margin=F),
    checks=checks, integer_checks=integer_checks, summary=summary,
    limitations='Only sufficient data tests and their conditional C077a reduction; '
                'no survivor existence/nondivisibility, integer exclusion or universal descent')


def encode(obj):
    if isinstance(obj, Q):
        return str(obj)
    raise TypeError(type(obj).__name__)


path = HERE / 'redistributed-h-table-certificate.json'
path.write_text(json.dumps(result, indent=2, default=encode)+'\n')
print(f'Checks: {len(checks)} rational, {len(integer_checks)} integer; failures: {failures}')
print(f'Lambda: {lm} < actual < {lp}; required >0 and <1')
print(f'O minimum: {summary["min_order_margin"]}; required >0')
print(f'S minimum: {summary["min_support_margin"]}; required >0')
print(f'C boundary: {F}; required <0; domain lower {domain_lower}, required >=47')
print(f'Certificate: {path.relative_to(ROOT)}')
assert not failures

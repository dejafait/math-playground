#!/usr/bin/env python3
"""Exactly d=34,t=0,1: replacement normalized cap and row18 H test.

Use L077's independent endpoint formulas and L083's cap/margin proof
cases, not either full sufficient-test conjunction. All finite evidence
and analytic errors are rational and are saved in the certificate.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
OUTPUT = HERE / 'd34-two-root-h-certificate.json'
raw = SOURCE.read_bytes()
base = [tuple(map(int, x)) for x in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert len(base) == 25 and [x[0] for x in base] == list(range(25))
rows = [(i, j, 6 if i == 0 else 32670655 if i == 24 else h)
        for i, j, h in base]
B, T, U = 9250245, F(24), F(21000000000)
kappa = F(23, 11)
lm, lp = F(10584, 10**14), F(10585, 10**14)
ell, u = F(693147180559, 10**12), F(1098612288669, 10**12)
checks, failures = [], []


def check(name, a, relation, b):
    a, b = F(a), F(b)
    passed = {'=': a == b, '<': a < b, '>': a > b,
              '<=': a <= b, '>=': a >= b}[relation]
    item = dict(name=name, actual=a, relation=relation, required=b,
                difference=a-b, passed=passed)
    checks.append(item)
    if not passed:
        failures.append(item)


def logarithm(x):
    x = F(x)
    z = (x-1)/(x+1)
    check(f'log{x} series domain lower', z, '>', 0)
    check(f'log{x} series domain upper', z, '<', 1)
    terms = [2*z**(2*k+1)/(2*k+1) for k in range(100)]
    lower = sum(terms, F(0))
    remainder = 2*z**201/(201*(1-z*z))
    return dict(argument=x, z=z, terms=terms, lower=lower,
                remainder_upper=remainder, upper=lower+remainder)


logs = {str(x): logarithm(x) for x in (2, 3)}
l2, h2 = logs['2']['lower'], logs['2']['upper']
l3, h3 = logs['3']['lower'], logs['3']['upper']
K = sum(3*j+h for _, j, h in rows)
N = sum(4*j+h for _, j, h in rows)+50+18*B
lam = [N*l2-K*h3, N*h2-K*l3]
check('K', K, '=', 397573379)
check('N', N, '=', 630138897)
check('positive lambda lower', lm, '>', 0)
check('Lambda lower', lam[0], '>', lm)
check('Lambda upper', lam[1], '<', lp)
check('lambda upper below one', lp, '<', 1)
check('ell positive', ell, '>', 0)
check('ell lower bound', ell, '<', l2)
check('u upper bound', u, '>', h3)
eta0 = kappa-F(16, 27)**8*(F(12, 11)+F(2, 3)**6)
domain = 2*(1-lp)/lp
check('eta0 exceeds e=2', eta0, '>', 2)
check('eta0 below kappa', eta0, '<', kappa)
check('eta24 monotone J premise', rows[24][1], '>=', rows[0][1])
check('eta24 monotone H premise', rows[24][2], '>=', rows[0][2])
check('uniform unshifted domain bound', domain, '>', 47)
for i, j, h in rows:
    check(f'row{i} J', j, '>=', 2)
    check(f'row{i} H', h, '>=', 3)
    if i:
        check(f'row{i} increasing J', j, '>', rows[i-1][1])

w = F(10**8)*F(2, 3)**33
L = [F(1)]+[w*2**i for i in range(24)]
reciprocals = [1/x for x in L]
reciprocal_sum = sum(reciprocals, F(0))
Q = kappa*reciprocal_sum
Lstar = min(L)
R_H = Q/lm+Q+kappa/Lstar
c0 = F(3**30, 2**40)
check('row0 c0 exceeds w', c0, '>', w)
check('w exceeds one', w, '>', 1)
check('actual L minimum', Lstar, '=', 1)
check('complete reciprocal sum', reciprocal_sum, '=', 1+2/w*(1-F(1, 2**24)))
check('cap lower integer enclosure', R_H, '>', 20011074612)
check('cap upper integer enclosure', R_H, '<', 20011074613)
check('replacement U', R_H, '<=', U)
exp_terms = [T**k/factorial(k) for k in range(41)]
exp_lower = sum(exp_terms, F(0))
check('positive T', T, '>', 0)
check('replacement U below exp lower sum', U, '<', exp_lower)
for i in range(25):
    check(f'incoming{i} L positive', L[i], '>', 0)
    if i:
        check(f'incoming{i} induction', L[i-1]*(w if i == 1 else 2), '=', L[i])

allocations = []
for t in (0, 1):
    tails = [2]*23+[2+18*t, 2+18*(B-t)]
    A, D = [0], [0]
    factors = []
    for (i, j, h), tail in zip(rows, tails):
        A.append(A[-1]+3*j+h)
        D.append(D[-1]+4*j+h+tail)
        check(f't{t} row{i} tail lower', tail, '>=', 2)
        check(f't{t} row{i} tail congruence', tail % 18, '=', 2)
        if 1 <= i <= 23:
            a, b = 3*j+h, 4*j+h+tail+1
            interval = [a*l3-b*h2, a*h3-b*l2]
            check(f't{t} row{i} log(c/2) lower', interval[0], '>', 0)
            factors.append(dict(i=i, numerator_exponent=a,
                denominator_exponent_plus_one=b, log_c_over_2=interval,
                amplified_log_errors=[a*logs['3']['remainder_upper'],
                                      b*logs['2']['remainder_upper']]))
    check(f't{t} closing K', A[25], '=', K)
    check(f't{t} closing N including last tail', D[25], '=', N)
    check(f't{t} total tail sum', sum(tails), '=', 166504460)
    check(f't{t} row18 A', A[18], '=', 6078890)
    check(f't{t} row18 D', D[18], '=', 6862807)
    incoming = []
    for i in range(25):
        # Relative to t=0, only incoming row24 includes row23's extra tail.
        baseline_D = sum(4*j+h+2 for _, j, h in rows[:i])
        check(f't{t} incoming{i} exponent', D[i], '=', baseline_D+(18*t if i == 24 else 0))
        incoming.append(dict(i=i, A=A[i], D=D[i], L=L[i], reciprocal=reciprocals[i]))
    P = A[18]+3*rows[18][1]
    R = D[18]+4*rows[18][1]+rows[18][2]
    upper = T+P*u-R*ell
    analytic_interval = [T+P*l3-R*h2, T+P*h3-R*l2]
    error = [P*(u-h3)+R*(l2-ell), P*(u-l3)+R*(h2-ell)]
    check(f't{t} positive row18 P', P, '>', 0)
    check(f't{t} positive row18 R', R, '>', 0)
    check(f't{t} outward error positive', error[0], '>', 0)
    check(f't{t} outward error ordered', error[1], '>', error[0])
    check(f't{t} full propagated error', error[1], '<', F(1, 50000))
    check(f't{t} upper rejects strict H guard', upper, '<', 0)
    allocations.append(dict(t=t, tails=tails, incoming=incoming,
        closing=dict(A=A[25], D=D[25]), factors=factors,
        row18=dict(J=rows[18][1], H=rows[18][2], A=A[18], D=D[18],
            P=P, R=R, upper_margin=upper, analytic_interval=analytic_interval,
            outward_error_interval=error,
            verdict='REJECTED: certified negative upper H margin')))

report = dict(scope=dict(d=34, t=[0, 1], literal_order=True, B=B,
    inputs=['L055', 'L077', 'L083', 'L084'],
    no_allocation_or_order_reduction=True),
    source=dict(path=str(SOURCE.relative_to(ROOT)), sha256=hashlib.sha256(raw).hexdigest()),
    table=rows, constants=dict(kappa=kappa, lambda_minus=lm, lambda_plus=lp,
        ell=ell, u=u, U=U, T=T),
    analytic=dict(logs=logs, lambda_interval=lam,
        lambda_amplified_errors=[N*logs['2']['remainder_upper'], K*logs['3']['remainder_upper']],
        exp24_terms=exp_terms, exp24_lower=exp_lower),
    endpoint=dict(K=K, N=N, eta0=eta0, eta24_lower=eta0, e=2, domain_lower=domain),
    cap=dict(w=w, c0=c0, L=L, L_star=Lstar, reciprocals=reciprocals,
        complete_reciprocal_sum=reciprocal_sum, Q=Q, R_H=R_H, U=U, T=T),
    allocations=allocations, checks=checks, failures=failures,
    summary=dict(roots=2, checks=len(checks), failures=len(failures),
        R_H=R_H, U=U, T=T, exp24_lower_floor=exp_lower.numerator//exp_lower.denominator,
        row18_upper=[x['row18']['upper_margin'] for x in allocations], required_upper=0,
        verdicts=[x['row18']['verdict'] for x in allocations]))
OUTPUT.write_text(json.dumps(report, indent=2, default=str)+'\n')
print(json.dumps(report['summary'], default=str))
print('Complete rational certificate:', OUTPUT.relative_to(ROOT))
if failures:
    print('First failed comparison:', failures[0]['name'])
    raise SystemExit(1)

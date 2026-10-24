#!/usr/bin/env python3
"""One approved d34 C-cap test: U=21000000000,T=24,tau=2.

L077 supplies the quantified implication. This program verifies its finite
data only; no search, tuning, guard feasibility or allocation reduction.
Full rational operands, series evidence and failures are saved to disk.
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
OUTPUT = HERE / 'd34-independent-cutoff-certificate.json'
raw = SOURCE.read_bytes()
base = [tuple(map(int, x)) for x in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert len(base) == 25 and [x[0] for x in base] == list(range(25))
rows = [(i, j, 6 if i == 0 else 32670655 if i == 24 else h)
        for i, j, h in base]
B, tau, U, T = 9250245, 2, F(21000000000), F(24)
kap = F(23, 11)
lm, lp = F(10584, 10**14), F(10585, 10**14)
ell, u, v = (F(x, 10**12) for x in
             (693147180559, 1098612288669, 1011600911679))
checks, failures = [], []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b,
              '<=': a <= b, '>=': a >= b}[relation]
    item = dict(name=name, actual=a, relation=relation, required=b,
                difference=a-b, passed=passed)
    checks.append(item)
    if not passed:
        failures.append(item)


def grid_interval(lower, upper, scale=10**12):
    """Full certified outward enclosure, not a truncated value preview."""
    assert lower <= upper
    return [F((lower*scale).__floor__(), scale),
            F((upper*scale).__ceil__(), scale)]


def logarithm(x):
    x = F(x)
    z = (x-1)/(x+1)
    check(f'log{x} positive series argument', z, '>', 0)
    check(f'log{x} series domain', z, '<', 1)
    terms = [2*z**(2*k+1)/(2*k+1) for k in range(100)]
    lower = sum(terms, F(0))
    remainder = 2*z**201/(201*(1-z*z))
    return dict(argument=x, z=z, terms=terms, lower=lower,
                remainder_upper=remainder, upper=lower+remainder)


logs = {str(x): logarithm(x) for x in (F(2), F(3), F(11, 4))}
l2, h2 = logs['2']['lower'], logs['2']['upper']
l3, h3 = logs['3']['lower'], logs['3']['upper']
lv, hv = logs['11/4']['lower'], logs['11/4']['upper']
K = sum(3*j+h for _, j, h in rows)
N = sum(4*j+h for _, j, h in rows)+50+18*B
lam = [N*l2-K*h3, N*h2-K*l3]
check('K', K, '=', 397573379)
check('N', N, '=', 630138897)
check('r domain', len(rows), '>=', 3)
check('budget domain', B, '>=', 0)
check('cutoff domain', tau, '>=', 0)
check('cutoff within budget', tau, '<=', B)
check('lambda minus positive', lm, '>', 0)
check('Lambda lower', lam[0], '>', lm)
check('Lambda upper', lam[1], '<', lp)
check('lambda plus below one', lp, '<', 1)
check('ell positive', ell, '>', 0)
check('ell lower', ell, '<', l2)
check('u upper', u, '>', h3)
check('v upper', v, '>', hv)
eta0 = kap-F(16, 27)**8*(F(12, 11)+F(2, 3)**6)
domain = 2*(1-lp)/lp
check('positive e', 2, '>', 0)
check('eta0 exceeds e', eta0, '>', 2)
check('eta24 J monotonicity premise', rows[24][1], '>=', rows[0][1])
check('eta24 H monotonicity premise', rows[24][2], '>=', rows[0][2])
check('unshifted domain', domain, '>', 47)
for i, j, h in rows:
    check(f'row{i} J', j, '>=', 2)
    check(f'row{i} H', h, '>=', 3)
    if i:
        check(f'row{i} increasing J', j, '>', rows[i-1][1])

tails = [2]*23+[2+18*tau, 2+18*(B-tau)]
check('row23 tail', tails[23], '=', 38)
check('closing row24 tail', tails[24], '=', 166504376)
check('total tails', sum(tails), '=', 166504460)
w = F(10**8)*F(2, 3)**33
L = [F(1)]+[w*2**(i-1) for i in range(1, 25)]
c0 = F(3**30, 2**40)
check('row0 exact multiplier exceeds w', c0, '>', w)
check('w positive', w, '>', 0)
A, D = [0], [0]
factors = []
for (i, j, h), a in zip(rows, tails):
    check(f'row{i} tail domain', a, '>=', 2)
    check(f'row{i} tail congruence', a % 18, '=', 2)
    A.append(A[-1]+3*j+h)
    D.append(D[-1]+4*j+h+a)
    if 1 <= i <= 23:
        aa, dd = 3*j+h, 4*j+h+a+1
        interval = [aa*l3-dd*h2, aa*h3-dd*l2]
        check(f'row{i} log(c/2) lower', interval[0], '>', 0)
        factors.append(dict(i=i, numerator_exponent=aa,
            denominator_exponent_plus_one=dd, interval=interval,
            certified_grid_interval=grid_interval(*interval),
            amplified_series_errors=[aa*logs['3']['remainder_upper'],
                                     dd*logs['2']['remainder_upper']]))
check('closing exponent K', A[25], '=', K)
check('closing exponent N', D[25], '=', N)
incoming = []
for i in range(25):
    check(f'incoming{i} L positive', L[i], '>', 0)
    if i:
        check(f'incoming{i} induction', L[i-1]*(w if i == 1 else 2), '=', L[i])
    incoming.append(dict(i=i, A=A[i], D=D[i], L=L[i], reciprocal=1/L[i]))
reciprocal_sum = sum((1/x for x in L), F(0))
check('complete reciprocal identity', reciprocal_sum, '=',
      1+2/w*(1-F(1, 2**24)))
Q = kap*reciprocal_sum
RC = Q/lm+Q+kap/L[24]
check('Q positive', Q, '>', 0)
check('C cap lower integer enclosure', RC, '>', 20011074610)
check('C cap upper integer enclosure', RC, '<', 20011074611)
check('one replacement U bounds C cap', RC, '<=', U)
exp_terms = [T**k/factorial(k) for k in range(41)]
exp_lower = sum(exp_terms, F(0))
check('T positive', T, '>', 0)
check('one replacement U below exp lower', U, '<', exp_lower)
P, R = A[24], D[24]+4*rows[24][1]
check('incoming row24 k', P, '=', 271907887)
check('incoming row24 d', D[24], '=', 306970750)
check('complete negative log2 coefficient', R, '=', 430963866)
upper_margin = T+P*u-R*ell+v
analytic_interval = [T+P*l3-R*h2+lv, T+P*h3-R*l2+hv]
error = [P*(u-h3)+R*(l2-ell)+(v-hv),
         P*(u-l3)+R*(h2-ell)+(v-lv)]
check('positive log3 coefficient', P, '>', 0)
check('positive negative-log2 coefficient', R, '>', 0)
check('full error positive', error[0], '>', 0)
check('full error ordered', error[1], '>', error[0])
check('full amplified error below 1/1000', error[1], '<', F(1, 1000))
check('row24 upper margin strictly negative', upper_margin, '<', 0)
summary = dict(checks=len(checks), failures=len(failures),
    RC=RC, required_U=U, U_minus_RC=U-RC,
    exp_lower_floor=exp_lower.__floor__(), exp_lower_minus_U_floor=(exp_lower-U).__floor__(),
    row24_upper_margin=upper_margin, required_margin='strictly below 0',
    row24_analytic_grid_interval=grid_interval(*analytic_interval),
    complete_amplified_error_grid_interval=grid_interval(*error),
    lambda_grid_interval=grid_interval(*lam, scale=10**20),
    rejected_interval=[tau, B] if not failures else None)
report = dict(scope=dict(d=34, literal=True, B=B, tau=tau,
    candidate_count=1,
    no_early_support_or_order_reduction=True),
    source=dict(path=str(SOURCE.relative_to(ROOT)), sha256=hashlib.sha256(raw).hexdigest()),
    table=rows, tails=tails, constants=dict(kappa=kap, lm=lm, lp=lp,
        e=2, U=U, T=T, ell=ell, u=u, v=v, eta0=eta0, domain=domain),
    analytic=dict(logs=logs, lambda_interval=lam,
        lambda_amplified_errors=[N*logs['2']['remainder_upper'], K*logs['3']['remainder_upper']],
        exp24_terms=exp_terms, exp24_lower=exp_lower),
    incoming=incoming, factors=factors,
    complete_factor_enclosures=[dict(i=f['i'],
        A=f['numerator_exponent'], D_plus_one=f['denominator_exponent_plus_one'],
        log_c_over_2=f['certified_grid_interval']) for f in factors],
    cap=dict(w=w, c0=c0, reciprocal_sum=reciprocal_sum, Q=Q,
             last_shift_term=kap/L[24], RC=RC),
    row24=dict(J=rows[24][1], H=rows[24][2], k=P, d=D[24], R=R,
        upper_margin=upper_margin, analytic_interval=analytic_interval,
        complete_amplified_error_interval=error),
    summary=summary, checks=checks, failures=failures)


def serial(x):
    if isinstance(x, F):
        return str(x)
    raise TypeError(type(x).__name__)


OUTPUT.write_text(json.dumps(report, default=serial, indent=2)+'\n')
print(f'Checks: {len(checks)}; failures: {len(failures)}')
print(f'C cap: {RC}; required <= {U}; exp24 lower sum > {exp_lower.__floor__()}')
print(f'Row24 upper J margin: {upper_margin}; required < 0')
print(f'Full amplified analytic error < {error[1].__ceil__() if error[1] >= 1 else "1/1000 (checked)"}')
print(f'Failures: {[x["name"] for x in failures]}')
print(f'Certificate: {OUTPUT}')
assert not failures

#!/usr/bin/env python3
"""Independent L095 audit; never imports or executes the constructor.

Regenerate all stored mathematical records and replay all stored comparisons.
A second analytic basis uses log(3)=log(2)+log(3/2), with 120 terms.
Full exact evidence is written locally; stdout contains only a short verdict.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import operator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
CONSTRUCTION = HERE / 'd34-two-root-h-certificate.json'
OUTPUT = HERE / 'd34-two-root-h-audit-certificate.json'
original = json.loads(CONSTRUCTION.read_text())
checks = []
ops = {'=': operator.eq, '<': operator.lt, '>': operator.gt,
       '<=': operator.le, '>=': operator.ge}


def certify(label, actual, relation, required):
    actual, required = F(actual), F(required)
    checks.append(dict(label=label, actual=actual, relation=relation,
                       required=required, difference=actual-required,
                       passed=ops[relation](actual, required)))


def same(label, actual, expected):
    # Exact recursive comparison, including complete arrays and key sets.
    if isinstance(expected, dict):
        assert isinstance(actual, dict) and set(actual) == set(expected), label
        for key in expected:
            same(label+'/'+key, actual[key], expected[key])
    elif isinstance(expected, (tuple, list)):
        assert isinstance(actual, list) and len(actual) == len(expected), label
        for index, value in enumerate(expected):
            same(label+'/'+str(index), actual[index], value)
    elif isinstance(expected, (int, F)) and not isinstance(expected, bool):
        certify(label, actual, '=', expected)
    else:
        assert actual == expected, (label, actual, expected)


def series(x, count):
    """Successive-power evaluation of the previously assessed log series."""
    x = F(x)
    z = (x-1)/(x+1)
    assert 0 < z < 1
    power, terms = z, []
    for index in range(count):
        terms.append(2*power/(2*index+1))
        power *= z*z
    lo = sum(terms, F())
    rem = 2*power/((2*count+1)*(1-z*z))
    return dict(argument=x, z=z, terms=terms, lower=lo,
                remainder_upper=rem, upper=lo+rem)


# Parse the literal canonical table independently of the constructor's regex.
base = []
for line in SOURCE.read_text().splitlines():
    fields = line.strip().strip('|').split('|')
    if len(fields) == 3 and all(field.isdecimal() for field in fields):
        base.append(list(map(int, fields)))
assert len(base) == 25 and [r[0] for r in base] == list(range(25))
rows = [row[:] for row in base]
rows[0][2] -= 34
rows[24][2] += 34
assert rows[0] == [0, 8, 6] and rows[24] == [24, 30998279, 32670655]
B, U, T = 9250245, F(21000000000), F(24)
kap = F(23, 11)
lm, lp = F(10584, 10**14), F(10585, 10**14)
ell, u = F(693147180559, 10**12), F(1098612288669, 10**12)
logs = {str(x): series(x, 100) for x in (2, 3)}
l2, h2 = logs['2']['lower'], logs['2']['upper']
l3, h3 = logs['3']['lower'], logs['3']['upper']
K = 3*sum(r[1] for r in rows)+sum(r[2] for r in rows)
N = K+sum(r[1] for r in rows)+2*len(rows)+18*B
lam = [N*l2-K*h3, N*h2-K*l3]
certify('positive Lambda lower', lam[0], '>', lm)
certify('Lambda upper', lam[1], '<', lp)
certify('lower logarithm', l2, '>', ell)
certify('upper logarithm', h3, '<', u)
eta0 = kap - F(16**8, 27**8)*(F(12, 11)+F(2**6, 3**6))
certify('endpoint e', eta0, '>', 2)
domain = 2*(1/lp-1)
certify('endpoint lower domain', domain, '>', 47)
for i, j, h in rows:
    certify(f'eta monotonicity J {i}', j, '>=', 8)
    certify(f'eta monotonicity H {i}', h, '>=', 6)
    if i:
        certify(f'increasing J {i}', j, '>', rows[i-1][1])

w = F(10**8*2**33, 3**33)
c0 = F(3**30, 2**40)
certify('first factor', c0, '>', w)
certify('w', w, '>', 1)
certify('weaker common tail38 factor', F(3**117, 2**170), '>', 2)
bounds = [F(1), w]
while len(bounds) < 25:
    bounds.append(2*bounds[-1])
recips = [F(1)/v for v in bounds]
qsum = sum(recips, F())
certify('complete finite reciprocal identity', qsum, '=', 1+2/w*(1-F(1, 2**24)))
Q, Lstar = kap*qsum, min(bounds)
certify('actual minimum incoming bound', Lstar, '=', 1)
RH = Q*(1/lm+1)+kap/Lstar
certify('RH displayed rational', RH, '=', F(419693935179938468251189621018264434581, 20973083320679305052160000000))
certify('RH lower integer', RH, '>', 20011074612)
certify('RH upper integer', RH, '<', 20011074613)
certify('old U still fails', RH, '>', 20000000000)
certify('new U works', RH, '<', U)
eterms = [F(1)]
for index in range(1, 41):
    eterms.append(eterms[-1]*T/index)
exp_lower = sum(eterms, F())
certify('new U below complete exp lower sum', U, '<', exp_lower)
certify('exp lower floor', exp_lower.numerator//exp_lower.denominator, '=', 26462988572)

allocations = []
for t in (0, 1):
    budget = [0]*25
    budget[23], budget[24] = t, B-t
    tails = [2+18*b for b in budget]
    aa = [0]
    dd = [0]
    incoming, factors = [], []
    for i, j, h in rows:
        incoming.append(dict(i=i, A=aa[-1], D=dd[-1], L=bounds[i], reciprocal=recips[i]))
        aa.append(aa[-1]+3*j+h)
        dd.append(dd[-1]+4*j+h+tails[i])
        certify(f't{t} tail {i} lower', tails[i], '>=', 2)
        certify(f't{t} tail {i} residue', tails[i] % 18, '=', 2)
        if 1 <= i <= 23:
            a, b = aa[-1]-aa[-2], dd[-1]-dd[-2]+1
            interval = [a*l3-b*h2, a*h3-b*l2]
            certify(f't{t} factor {i} >2', interval[0], '>', 0)
            factors.append(dict(i=i, numerator_exponent=a,
                denominator_exponent_plus_one=b, log_c_over_2=interval,
                amplified_log_errors=[a*logs['3']['remainder_upper'], b*logs['2']['remainder_upper']]))
    certify(f't{t} entire closing numerator', aa[-1], '=', K)
    certify(f't{t} entire closing denominator', dd[-1], '=', N)
    certify(f't{t} total tails', sum(tails), '=', 166504460)
    P = aa[18]+3*rows[18][1]
    R = dd[18]+4*rows[18][1]+rows[18][2]
    upper = T+P*u-R*ell
    err = [P*(u-h3)+R*(l2-ell), P*(u-l3)+R*(h2-ell)]
    certify(f't{t} P', P, '=', 8157935)
    certify(f't{t} R', R, '=', 12930075)
    certify(f't{t} upper exact', upper, '=', F(-1338950347341, 100000000000))
    certify(f't{t} upper sign', upper, '<', 0)
    certify(f't{t} error lower', err[0], '>', 0)
    certify(f't{t} error upper', err[1], '<', F(1, 50000))
    allocations.append(dict(t=t, tails=tails, incoming=incoming,
        closing=dict(A=aa[25], D=dd[25]), factors=factors,
        row18=dict(J=rows[18][1], H=rows[18][2], A=aa[18], D=dd[18],
            P=P, R=R, upper_margin=upper,
            analytic_interval=[T+P*l3-R*h2, T+P*h3-R*l2],
            outward_error_interval=err,
            verdict='REJECTED: certified negative upper H margin')))

# Compare every original non-check record, not merely displayed summary flags.
expected = dict(scope=dict(d=34, t=[0, 1], literal_order=True, B=B,
    inputs=['L055', 'L077', 'L083', 'L084'], no_allocation_or_order_reduction=True),
    source=dict(path=str(SOURCE.relative_to(ROOT)), sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest()),
    table=rows, constants=dict(kappa=kap, lambda_minus=lm, lambda_plus=lp, ell=ell, u=u, U=U, T=T),
    analytic=dict(logs=logs, lambda_interval=lam,
        lambda_amplified_errors=[N*logs['2']['remainder_upper'], K*logs['3']['remainder_upper']],
        exp24_terms=eterms, exp24_lower=exp_lower),
    endpoint=dict(K=K, N=N, eta0=eta0, eta24_lower=eta0, e=2, domain_lower=domain),
    cap=dict(w=w, c0=c0, L=bounds, L_star=Lstar, reciprocals=recips,
        complete_reciprocal_sum=qsum, Q=Q, R_H=RH, U=U, T=T),
    allocations=allocations, failures=[],
    summary=dict(roots=2, checks=368, failures=0, R_H=RH, U=U, T=T,
        exp24_lower_floor=26462988572,
        row18_upper=[x['row18']['upper_margin'] for x in allocations],
        required_upper=0, verdicts=[x['row18']['verdict'] for x in allocations]))
same('construction', {k: v for k, v in original.items() if k != 'checks'}, expected)
assert len(original['checks']) == 368
assert len({c['name'] for c in original['checks']}) == 368
for item in original['checks']:
    assert set(item) == {'name', 'actual', 'relation', 'required', 'difference', 'passed'}
    certify('replayed/'+item['name'], item['actual'], item['relation'], item['required'])
    certify('difference/'+item['name'], item['difference'], '=', F(item['actual'])-F(item['required']))
    assert item['passed'] is True

# Changed analytic basis: substantially tighter intervals, no constructor use.
crosslogs = {'2': series(2, 120), '3/2': series(F(3, 2), 120)}
a, b = crosslogs['2']['lower'], crosslogs['2']['upper']
c, d = crosslogs['3/2']['lower'], crosslogs['3/2']['upper']
crosslam = [(N-K)*a-K*d, (N-K)*b-K*c]
certify('second Lambda lies above old lower', crosslam[0], '>', lam[0])
certify('second Lambda lies below old upper', crosslam[1], '<', lam[1])
crossrows = []
for alloc in allocations:
    row = alloc['row18']
    P, R = row['P'], row['R']
    # P-R<0, so the second log2 interval is used with reversed endpoints.
    certify('second row18 negative log2 coefficient', P-R, '<', 0)
    interval = [T+P*c+(P-R)*b, T+P*d+(P-R)*a]
    error = [row['upper_margin']-interval[1], row['upper_margin']-interval[0]]
    certify('second row18 upper inside first', interval[1], '<', row['analytic_interval'][1])
    certify('second row18 lower inside first', interval[0], '>', row['analytic_interval'][0])
    certify('second row18 error positive', error[0], '>', 0)
    certify('second row18 error ceiling', error[1], '<', F(1, 50000))
    crossrows.append(dict(t=alloc['t'], expression_interval=interval, error_interval=error))

failures = [c for c in checks if not c['passed']]
summary = dict(checks=len(checks), failures=len(failures), original_comparisons_replayed=368,
    incoming_indices_per_root=25, actual_nonzero_row_factors=46,
    R_H_integer_interval=[20011074612, 20011074613], U=U,
    exp24_lower_floor=26462988572, T=T,
    row18_upper=[a['row18']['upper_margin'] for a in allocations],
    required_H_upper=0, complete_error_upper_bound=F(1, 50000),
    verdict='NO DEFECT FOUND IN L095 FIXED TWO-ROOT SCOPE' if not failures else 'AUDIT FAILED')
report = dict(construction_sha256=hashlib.sha256(CONSTRUCTION.read_bytes()).hexdigest(),
    reconstructed=expected, independent_analytic=dict(logs=crosslogs,
    lambda_interval=crosslam, row18=crossrows), checks=checks,
    failures=failures, summary=summary)
OUTPUT.write_text(json.dumps(report, indent=2, default=str)+'\n')
print(json.dumps(summary, default=str))
print('Full audit certificate:', OUTPUT.relative_to(ROOT))
if failures:
    print('Failed checks:', ', '.join(c['label'] for c in failures))
    raise SystemExit(1)

#!/usr/bin/env python3
"""One fixed-rule pass over the 37 preassessed tables; no certificate tuning.

All arithmetic is rational. Existing L079/L083 series bounds and existing
C077a/L083 implications are used, not reproved. Full operands, interval
endpoints, terms, failures and incoming exponents are written to disk.
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
original = [tuple(map(int, x)) for x in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert len(original) == 25 and [x[0] for x in original] == list(range(25))
r, p, q, B, tau, m = 25, 23, 24, 9250245, 2, 1
kap = Q(23, 11)
lm, lp = Q(10584, 10**14), Q(10585, 10**14)
ell = Q(693147180559, 10**12)
u = Q(1098612288669, 10**12)
v = Q(1011600911679, 10**12)
U = Q(20_000_000_000)


def log_bounds(x):
    z = (x-1)/(x+1)
    assert 0 < z <= Q(1, 2)
    terms = [2*z**(2*k+1)/(2*k+1) for k in range(100)]
    lower = sum(terms, Q(0))
    remainder = 2*z**201/(201*(1-z*z))
    return dict(argument=x, z=z, terms=terms, lower=lower,
                remainder_upper=remainder, upper=lower+remainder)


logs = {str(x): log_bounds(x) for x in (Q(2), Q(3), Q(11, 4))}
exp_terms = {T: [Q(T)**k/factorial(k) for k in range(41)] for T in (24, 27)}
exp_lower = {T: sum(terms, Q(0)) for T, terms in exp_terms.items()}
tables = []
for d in range(1, 38):
    rows = [(i, j, 40-d if i == 0 else 32670621+d if i == q else h)
            for i, j, h in original]
    checks = []

    def check(package, name, actual, relation, required):
        a, b = Q(actual), Q(required)
        ok = {'<': a < b, '<=': a <= b, '=': a == b,
              '>': a > b, '>=': a >= b}[relation]
        checks.append(dict(package=package, name=name, actual=a,
                           relation=relation, required=b, difference=a-b,
                           verdict='PASS' if ok else 'FAIL'))

    def positive_interval(package, name, lower, upper):
        assert lower <= upper
        verdict = 'PASS' if lower > 0 else 'FAIL' if upper <= 0 else 'INCONCLUSIVE'
        checks.append(dict(package=package, name=name, lower=lower, upper=upper,
                           relation='>', required=Q(0), verdict=verdict))

    K = sum(3*j+h for _, j, h in rows)
    N = sum(4*j+h for _, j, h in rows)+2*r+18*B
    lambda_interval = [N*logs['2']['lower']-K*logs['3']['upper'],
                       N*logs['2']['upper']-K*logs['3']['lower']]
    check('table', 'K', K, '=', 397573379)
    check('table', 'N', N, '=', 630138897)
    check('table', 'sum H', sum(h for _, _, h in rows), '=', 199390205)
    check('table', 'sum J', sum(j for _, j, _ in rows), '=', 66061058)
    check('table', 'r lower', r, '>=', 3)
    check('table', 'budget lower', B, '>=', 0)
    check('table', 'cutoff within budget', tau, '<=', B)
    check('table', 'survivor maximum', m, '=', min(B, tau-1))
    for i, j, h in rows:
        check('table', f'row{i} J domain', j, '>=', 2)
        check('table', f'row{i} H domain', h, '>=', 3)
        if i:
            check('table', f'row{i} increasing J', j, '>', rows[i-1][1])
    A = D = 0
    prefixes = []
    for i, j, h in rows:
        prefixes.append(dict(i=i, A=A, D_tail2=D))
        A += 3*j+h
        D += 4*j+h+2
    check('table', 'complete odd exponent', A, '=', K)
    check('table', 'complete denominator with budget', D+18*B, '=', N)

    # Each independent package explicitly checks its own analytic constants.
    for pkg in ('O', 'S', 'C', 'H'):
        check(pkg, 'positive lambda lower', lm, '>', 0)
        check(pkg, 'Lambda lower enclosure', lm, '<=', lambda_interval[0])
        check(pkg, 'positive ell', ell, '>', 0)
        check(pkg, 'ell below log2', ell, '<=', logs['2']['lower'])
        check(pkg, 'u above log3', u, '>=', logs['3']['upper'])
        if pkg != 'H':
            check(pkg, 'v above log11over4', 2 if pkg == 'O' else v,
                  '>=', logs['11/4']['upper'])

    O_cap = 23*r/(11*lm)+kap
    check('O', 'minimum cap below exp27 lower', O_cap, '<=', exp_lower[27])
    offsets_O = []
    for i, j, h in rows:
        floor = min(h, 72)
        upper = Q(81, 44)-Q(3, 11)*Q(3, 2)**floor
        check('O', f'row{i} offset H floor', h, '>=', floor)
        check('O', f'row{i} tail2 offset upper', upper, '<', 0)
        offsets_O.append(dict(i=i, H_floor=floor, offset_upper=upper,
                              exact_offset=(floor == h)))
    margins_O = []
    for k in range(q):
        a, dd = prefixes[k]['A'], prefixes[k]['D_tail2']
        margin = 4*rows[k+1][1]*ell-27-2-a*u+dd*ell
        check('O', f'displacement{k}', margin, '>', 0)
        margins_O.append(dict(k=k, row=k+1, A=a, D=dd, margin=margin))

    E = Q(23*(r-1), 4*2**(4*rows[1][1])-23)
    check('S', 'residual positive', lm-E, '>', 0)
    S_cap = kap/(lm-E)+kap
    check('S', 'residual root cap', S_cap, '<=', U)
    check('S', 'U below exp24 lower', U, '<=', exp_lower[24])
    offsets_S, margins_S = [], []
    for i, j, h in rows[:p]:
        floor = min(h, 72)
        lower = Q(12, 11)*Q(3, 2)**floor+1
        check('S', f'row{i} offset H floor', h, '>=', floor)
        check('S', f'row{i} tail20 Q lower', lower, '>', kap*2**20)
        offsets_S.append(dict(i=i, H_floor=floor, Q_lower=lower,
                              exact_Q=(floor == h), required=kap*2**20))
        a, dd = prefixes[i+1]['A'], prefixes[i+1]['D_tail2']
        margin = (dd+18+4*rows[i+1][1])*ell-24-v-a*u
        check('S', f'recipient{i}', margin, '>', 0)
        margins_S.append(dict(j=i, input=i+1, A=a, D=dd, margin=margin))

    h0, j0 = rows[0][2], rows[0][1]
    eta0 = kap-Q(12, 11)*Q(16, 27)**j0-Q(16, 27)**j0*Q(2, 3)**h0
    check('C', 'Lambda upper enclosure', lambda_interval[1], '<=', lp)
    check('C', 'lambda upper below one', lp, '<', 1)
    check('C', 'positive e', 2, '>', 0)
    check('C', 'eta0 bound', eta0, '>=', 2)
    check('C', 'eta_q J comparison', rows[q][1], '>=', j0)
    check('C', 'eta_q H comparison', rows[q][2], '>=', h0)
    domain = 2*(1-lp)/lp
    check('C', 'uniform domain', domain, '>=', 47)

    w = Q(10**8)*Q(2, 3)**(d-1)
    L = [Q(1)]+[w*2**(i-1) for i in range(1, r)]
    reciprocal_sum = sum((1/x for x in L), Q(0))
    cap_Q = kap*reciprocal_sum  # fixed rule: full sum, not its infinite bound
    packages = {}
    for pkg, t in (('C', tau), ('H', m)):
        tails = [2 if i < p else 2+18*t if i == p else 2+18*(B-t)
                 for i in range(r)]
        check(pkg, 'full allocated tail sum', sum(tails), '=', 2*r+18*B)
        check(pkg, 'row23 actual tail', tails[p], '=', 38 if pkg == 'C' else 20)
        check(pkg, 'row24 actual tail', tails[q], '=',
              166504376 if pkg == 'C' else 166504394)
        for i, tail in enumerate(tails):
            check(pkg, f'row{i} tail lower', tail, '>=', 2)
            check(pkg, f'row{i} tail congruence', tail % 18, '=', 2)
        c0 = Q(3**(3*j0+h0), 2**(4*j0+h0+tails[0]))
        check(pkg, 'row0 c0 >= w', c0, '>=', w)
        factors = [dict(i=0, exact=c0, lower=w)]
        for i, j, h in rows[1:q]:
            a, dd = 3*j+h, 4*j+h+tails[i]
            # log(c_i/2) retains every exponent and analytic error.
            lower = a*logs['3']['lower']-(dd+1)*logs['2']['upper']
            upper = a*logs['3']['upper']-(dd+1)*logs['2']['lower']
            positive_interval(pkg, f'row{i} log(c/2)', lower, upper)
            factors.append(dict(i=i, A=a, D=dd, lower=Q(2),
                                log_ratio_interval=[lower, upper]))
        incoming = []
        for i in range(r):
            check(pkg, f'incoming{i} positive L', L[i], '>', 0)
            check(pkg, f'incoming{i} definition', L[i], '=',
                  1 if i == 0 else w*2**(i-1))
            if i:
                check(pkg, f'incoming{i} induction', L[i-1]*factors[i-1]['lower'],
                      '=', L[i])
            incoming.append(dict(i=i, A=prefixes[i]['A'],
                D=prefixes[i]['D_tail2']+(18*t if i == q else 0),
                L=L[i], reciprocal=1/L[i]))
        check(pkg, 'complete reciprocal cap', cap_Q, '>=',
              kap*sum((x['reciprocal'] for x in incoming), Q(0)))
        lden = L[q] if pkg == 'C' else min(L)
        required_cap = cap_Q/lm+cap_Q+kap/lden
        check(pkg, 'normalized cap <= U', required_cap, '<=', U)
        check(pkg, 'U below exp24 lower', U, '<=', exp_lower[24])
        check(pkg, 'complete closing odd exponent', K, '=', 397573379)
        check(pkg, 'complete closing denominator',
              sum(4*j+h+a for (_, j, h), a in zip(rows, tails)), '=', N)
        packages[pkg] = dict(t=t, tails=tails, factors=factors, incoming=incoming,
            L=L, L_min=min(L), reciprocal_sum=reciprocal_sum, Q=cap_Q,
            cap_denominator=lden, required_cap=required_cap, U=U, T=24,
            lambda_lower=lm, ell=ell, u=u)

    aq = prefixes[q]['A']
    dq = packages['C']['incoming'][q]['D']
    cutoff_margin = 24+aq*u-(dq+4*rows[q][1])*ell+v
    check('C', 'strict cutoff margin', cutoff_margin, '<', 0)
    packages['C'].update(lambda_upper=lp, e=2, eta0=eta0,
        eta_q_lower=eta0, eta_q_bound='Monotone in J,H; both bases are in (0,1)',
        domain_lower=domain, v=v, cutoff_margin=cutoff_margin)

    F = []
    for i, j, h in rows:
        a, dd = prefixes[i]['A'], prefixes[i]['D_tail2']
        positive, negative = a+3*j, dd+4*j+h
        margin = 24+positive*u-negative*ell
        F.append(dict(i=i, A=a, D_at_0=dd, log3_coefficient=positive,
                      negative_log2_coefficient=negative, F=margin,
                      rejecting=margin <= 0))
    rejected = [x['i'] for x in F if x['rejecting']]
    packages['H'].update(F=F, rejected_rows=rejected,
        rejection_test='Some F_i <= 0; evaluated independently of prerequisites')
    verdicts = {pkg: ('FAIL' if any(x['verdict'] == 'FAIL' for x in checks
                                  if x['package'] == pkg) else
                     'INCONCLUSIVE' if any(x['verdict'] == 'INCONCLUSIVE' for x in checks
                                          if x['package'] == pkg) else 'PASS')
                for pkg in ('table', 'O', 'S', 'C', 'H')}
    failure_names = [f"{x['package']}: {x['name']}" for x in checks if x['verdict'] == 'FAIL']
    inconclusive = [f"{x['package']}: {x['name']}" for x in checks if x['verdict'] == 'INCONCLUSIVE']
    all_data = all(x == 'PASS' for x in verdicts.values())
    verdict = ('EXCLUDED' if all_data and rejected else 'DATA_TEST_FAILURE' if failure_names
               else 'INCONCLUSIVE' if inconclusive else 'NO_REJECTING_F')
    summary = dict(d=d, verdict=verdict, package_verdicts=verdicts,
        failures=failure_names, inconclusive=inconclusive, rejected_rows=rejected,
        min_O=min(x['margin'] for x in margins_O),
        min_S=min(x['margin'] for x in margins_S), cutoff_margin=cutoff_margin,
        F18=F[18]['F'], O_row0=offsets_O[0]['offset_upper'],
        S_row0_Q=offsets_S[0]['Q_lower'], S_required_Q=kap*2**20,
        C_required_cap=packages['C']['required_cap'],
        H_required_cap=packages['H']['required_cap'], L_min=min(L), checks=len(checks))
    tables.append(dict(d=d, rows=rows, counts=dict(K=K, N=N),
        Lambda_interval=lambda_interval, w=w, prefixes=prefixes,
        O=dict(lambda_lower=lm, T=27, ell=ell, u=u, v=2, cap=O_cap,
               offsets=offsets_O, margins=margins_O),
        S=dict(lambda_lower=lm, U=U, T=24, ell=ell, u=u, v=v,
               E=E, residual=lm-E, cap=S_cap, offsets=offsets_S, margins=margins_S),
        C=packages['C'], H=packages['H'], checks=checks, summary=summary))

certified = [x for x in tables if x['summary']['verdict'] == 'EXCLUDED']
report_bounds = dict(
    certified_min_O=min(x['summary']['min_O'] for x in certified),
    certified_min_S=min(x['summary']['min_S'] for x in certified),
    certified_max_C_margin=max(x['summary']['cutoff_margin'] for x in certified),
    certified_max_H_F18=max(x['summary']['F18'] for x in certified),
    certified_max_C_cap=max(x['C']['required_cap'] for x in certified),
    certified_max_H_cap=max(x['H']['required_cap'] for x in certified),
    all_min_L=min(x['H']['L_min'] for x in tables),
    all_min_factor_log_ratio=min(f['log_ratio_interval'][0]
        for x in tables for pkg in ('C', 'H') for f in x[pkg]['factors'][1:]),
    all_c0_over_w={str(x['d']): x['C']['factors'][0]['exact']/x['w'] for x in tables})
assert report_bounds['certified_min_O'] > Q(1258, 100)
assert report_bounds['certified_min_S'] > Q(972, 100)
assert report_bounds['certified_max_C_margin'] < -Q(420, 100)
assert report_bounds['certified_max_C_cap'] < Q(198, 10)*10**9
assert report_bounds['certified_max_H_cap'] < Q(198, 10)*10**9
assert report_bounds['all_min_L'] == 1
assert report_bounds['all_min_factor_log_ratio'] > 0
assert all(x > 1 for x in report_bounds['all_c0_over_w'].values())

result = dict(target='Test C077a and L083 on the 37 preassessed H-transfer tables',
    source=dict(path=str(SOURCE.relative_to(ROOT)), sha256=hashlib.sha256(raw).hexdigest()),
    assessment='drafts/literature/2026-10-19-h-transfer-family-sufficient-tests.md',
    parameters=dict(r=r, B=B, tau=tau, m=m, d_min=1, d_max=37),
    analytic_inputs='L079 (2), L083 and the prior assessment; exact 100-term '
        'logarithm bounds with positive geometric remainders; degree-40 exp lower sums',
    logs=logs, exp_terms=exp_terms, exp_lower=exp_lower, tables=tables,
    report_bounds=report_bounds,
    summary=dict(excluded=[x['d'] for x in tables if x['summary']['verdict'] == 'EXCLUDED'],
        data_test_failure=[x['d'] for x in tables if x['summary']['verdict'] == 'DATA_TEST_FAILURE'],
        inconclusive=[x['d'] for x in tables if x['summary']['verdict'] == 'INCONCLUSIVE'],
        no_rejecting_F=[x['d'] for x in tables if x['summary']['verdict'] == 'NO_REJECTING_F'],
        checks=sum(len(x['checks']) for x in tables)),
    limitations='A failed fixed sufficient certificate gives no feasibility verdict. '
        'No tuning, arithmetic search, root construction or d=0 recertification. '
        'Only C077a/L083 conditional real-subsystem consequences; no universal descent.')
path = HERE / 'h-transfer-family-certificate.json'
path.write_text(json.dumps(result, indent=2, default=str)+'\n')
print('Lambda: 10584/10^14 < actual < 10585/10^14; required positive and <1.')
for t in tables:
    s = t['summary']
    print(f"d={t['d']:2}: {s['verdict']}; O/S/C/H="+
          '/'.join(s['package_verdicts'][p] for p in ('O', 'S', 'C', 'H'))+
          f"; F18={s['F18']} (reject if <=0); failures={s['failures']}")
    if s['failures']:
        a = s['S_row0_Q']
        print(f'  S row0 Q in [{a.numerator//a.denominator},'
              f'{a.numerator//a.denominator+1}), required >24117248/11.')
    if t['d'] >= 34:
        for pkg in ('C', 'H'):
            a = s[pkg+'_required_cap']
            print(f'  {pkg} required cap in [{a.numerator//a.denominator},'
                  f'{a.numerator//a.denominator+1}), required <=20000000000.')
    if t['d'] >= 36:
        print(f"  O row0 offset={s['O_row0']}, required <0.")
print(f"Summary: {result['summary']}")
print(f'Full operands, actual/required bounds and failures: {path.relative_to(ROOT)}')

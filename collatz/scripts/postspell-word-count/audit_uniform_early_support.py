#!/usr/bin/env python3
"""Independent L091 proof-data audit. Does not import/run any constructor.

Direct prefix sums and integer-scaled margins reconstruct every mathematical
construction field. Source certificates are comparison targets, never inputs
to the reconstructed quantities. Full rational evidence is saved to disk.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PAIRS = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
         (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
         (8224,39104),(15494,73672),(29191,138802),(54998,261511),
         (103621,492705),(195229,928293),(367827,1748976),
         (693015,3295208),(1305695,6208431),(2460032,11697176),
         (4634896,22038409),(8732512,41522114),(16452748,78230965),
         (30998279,32670621)]
scale = 10**12
el, up, vv = 693147180559, 1098612288669, 1011600911679
ell, u, v = (F(x, scale) for x in (el, up, vv))
kappa, U, T = F(23,11), F(20000000000), F(24)
lam, lam_hi = F(10584,10**14), F(10585,10**14)
E = F(23*24, 2**62-23)
R = kappa/(lam-E)+kappa
failures, verification, construction_checks = [], [], []
leaf_count = 0


def relation(a, op, b):
    return {'<': a < b, '>': a > b, '=': a == b}[op]


def verify(name, a, op, b):
    a, b = F(a), F(b)
    ok = relation(a, op, b)
    verification.append(dict(name=name, actual=a, relation=op,
                             required=b, difference=a-b, passed=ok))
    if not ok:
        failures.append('proof/'+name)


def expect_check(name, a, op, b):
    a, b = F(a), F(b)
    construction_checks.append(dict(name=name, actual=a, relation=op,
                                    required=b, difference=a-b,
                                    passed=relation(a, op, b)))
    if not relation(a, op, b):
        failures.append('reconstruction/'+name)


def compare(path, actual, expected):
    global leaf_count
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or set(actual) != set(expected):
            failures.append(path+'/keys')
            return
        for key, value in expected.items():
            compare(path+'/'+str(key), actual[key], value)
    elif isinstance(expected, (tuple, list)):
        if not isinstance(actual, (tuple, list)) or len(actual) != len(expected):
            failures.append(path+'/length')
            return
        for index, value in enumerate(expected):
            compare(path+'/'+str(index), actual[index], value)
    else:
        leaf_count += 1
        if isinstance(expected, F):
            actual = F(actual)
        if actual != expected:
            failures.append(path)


def log_interval(x, count=100):
    z = (x-1)/(x+1)
    # Direct powers, separate from the construction's analytic imports.
    terms = [F(2,2*k+1)*z**(2*k+1) for k in range(count)]
    lower = sum(terms, F(0))
    remainder = 2*z**(2*count+1)/((2*count+1)*(1-z*z))
    return dict(argument=x, z=z, terms=terms, lower=lower,
                remainder_upper=remainder, upper=lower+remainder)


logs = {str(x): log_interval(x) for x in (F(2),F(3),F(11,4))}
l2, h2 = logs['2']['lower'], logs['2']['upper']
l3, h3 = logs['3']['lower'], logs['3']['upper']
lv, hv = logs['11/4']['lower'], logs['11/4']['upper']
verify('ell below log2 lower', ell, '<', l2)
verify('log3 upper below u', h3, '<', u)
verify('log11/4 upper below v', hv, '<', v)
lambda_interval = [630138897*l2-397573379*h3,
                   630138897*h2-397573379*l3]
verify('Lambda lower above lambda', lambda_interval[0], '>', lam)
verify('Lambda upper below lambda upper', lambda_interval[1], '<', lam_hi)

exp_terms = [F(1)]
for k in range(1,41):
    exp_terms.append(exp_terms[-1]*24/k)
prefix_offset = kappa-(F(12,11)*F(3,2)**7+1)/4
recipient_Q = F(12,11)*F(3,2)**72+1
required_Q = kappa*2**20
expect_check('uniform prefix tail2 offset', prefix_offset, '<', 0)
expect_check('uniform recipient tail20 Q', recipient_Q, '>', required_Q)
expect_check('positive margin increment u-ell', u-ell, '>', 0)
expect_check('U below exp24 positive lower sum', U, '<', sum(exp_terms))
expect_check('L090 positive residual', lam-E, '>', 0)
expect_check('L090 root cap below U', R, '<', U)

source_path = ROOT/'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
source_bytes = source_path.read_bytes()
source_rows = [tuple(map(int,x)) for x in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', source_bytes.decode(), re.M)]
compare('canonical_pairs', source_rows, [(i,j,h) for i,(j,h) in enumerate(PAIRS)])
prior_bytes = (HERE/'h-transfer-family-certificate.json').read_bytes()
prior = json.loads(prior_bytes)['tables']
d5_bytes = (HERE/'d5-remaining-early-recipients-certificate.json').read_bytes()
d5 = json.loads(d5_bytes)
stored_path = HERE/'uniform-remaining-early-recipients-certificate.json'
stored_bytes = stored_path.read_bytes()
stored = json.loads(stored_bytes)


def prefix(rows, stop):
    return (sum(3*j+h for _,j,h in rows[:stop]),
            sum(4*j+h+2 for _,j,h in rows[:stop]))


def margin(A,D,next_J):
    # Integer numerator avoids reusing the constructor's Fraction expression.
    return F((D+18+4*next_J)*el-24*scale-vv-A*up, scale)


original_rows = [(i,j,h) for i,(j,h) in enumerate(PAIRS)]
d5_margins = {}
for j in range(1,23):
    oa, od = prefix(original_rows,j+1)
    d5_margins[j] = margin(oa-5,od-5,PAIRS[j+1][0])
    compare('d5/margin/'+str(j), d5['margins'][j-1]['margin'], d5_margins[j])

tables, errors = [], []
for d in range(6,34):
    rows = [(i,j,h+d*((i==24)-(i==0))) for i,(j,h) in enumerate(PAIRS)]
    verify(f'd{d} J minimum', min(j for _,j,h in rows), '>', 1)
    verify(f'd{d} H minimum', min(h for _,j,h in rows), '>', 2)
    verify(f'd{d} cap J minimum', min(j for _,j,h in rows[1:]), '=', 15)
    compare(f'L084/d{d}/rows', prior[d-1]['rows'], rows)
    expect_check(f'd{d} prior index', d, '=', d)
    expect_check(f'd{d} minimum prefix H', min(h for _,j,h in rows[:22]), '=', 40-d)
    expect_check(f'd{d} prefix H floor', 40-d, '>', 6)
    expect_check(f'd{d} minimum recipient H', min(h for _,j,h in rows[1:23]), '=', 72)
    Q0 = F(12,11)*F(3,2)**(40-d)+1
    expect_check(f'd{d} failed full row0 tail20 datum retained', Q0, '<', required_Q)
    prefixes, margins = [], []
    compare(f'L084/d{d}/index', prior[d-1]['d'], d)
    for i in range(25):
        A,D = prefix(rows,i)
        prefixes.append(dict(i=i,A=A,D=D))
        compare(f'L084/d{d}/prefix{i}/A', prior[d-1]['prefixes'][i]['A'], A)
        compare(f'L084/d{d}/prefix{i}/D', prior[d-1]['prefixes'][i]['D_tail2'], D)
        expect_check(f'd{d} incoming{i} A matches L084', A, '=', A)
        expect_check(f'd{d} incoming{i} D matches L084', D, '=', D)
        if not 1 <= i <= 22:
            continue
        A,D = prefix(rows,i+1)
        oa,od = prefix(original_rows,i+1)
        next_J = rows[i+1][1]
        C = D+18+4*next_J
        M = margin(A,D,next_J)
        q = prior[d-1]['S']['margins'][i]
        for field,value in [('A',A),('D',D),('margin',M)]:
            compare(f'L084/d{d}/margin{i}/{field}',q[field],value)
        expect_check(f'd{d} recipient{i} positive A', A, '>', 0)
        expect_check(f'd{d} recipient{i} positive log2 coefficient', C, '>', 0)
        expect_check(f'd{d} recipient{i} A matches L084', A, '=', A)
        expect_check(f'd{d} recipient{i} D matches L084', D, '=', D)
        expect_check(f'd{d} recipient{i} M matches L084', M, '=', M)
        expect_check(f'd{d} recipient{i} A shift', A-oa, '=', -d)
        expect_check(f'd{d} recipient{i} D shift', D-od, '=', -d)
        expect_check(f'd{d} recipient{i} d5 margin shift', M, '=', d5_margins[i]+(d-5)*(u-ell))
        expect_check(f'd{d} recipient{i} rejection', M, '>', F(47,4))
        margins.append(dict(j=i,next_input=i+1,A=A,D=D,next_J=next_J,
                            log2_coefficient=C,margin=M))
        err_low = C*(l2-ell)+A*(u-h3)+(v-hv)
        err_high = C*(h2-ell)+A*(u-l3)+(v-lv)
        x_low, x_high = C*l2-24-hv-A*h3, C*h2-24-lv-A*l3
        verify(f'd{d} j{i} outward error positive',err_low,'>',0)
        verify(f'd{d} j{i} lower error identity',x_low-M,'=',err_low)
        verify(f'd{d} j{i} upper error identity',x_high-M,'=',err_high)
        verify(f'd{d} j{i} error coarse upper',err_high,'<',F(1,1000))
        errors.append(dict(d=d,j=i,A=A,C=C,lower=err_low,upper=err_high,
                           exact_expression_interval=[x_low,x_high]))
    A,D = prefix(rows,25)
    expect_check(f'd{d} total K',A,'=',397573379)
    expect_check(f'd{d} total N',D+18*9250245,'=',630138897)
    tables.append(dict(d=d,rows=rows,prefixes=prefixes,margins=margins,failed_row0_Q=Q0))

minimum, md, mj = min((m['margin'],t['d'],m['j']) for t in tables for m in t['margins'])
expected = dict(
    scope='Literal d=6..33 endpoint/domain/J subsystem, full allocation simplex',
    imports='L090: b0=0 and s0<U; L084 (2): analytic ell,u,v; DLMF 4.2.19',
    source_sha256=hashlib.sha256(source_bytes).hexdigest(),
    prior_certificate_sha256=hashlib.sha256(prior_bytes).hexdigest(),
    d5_certificate_sha256=hashlib.sha256(d5_bytes).hexdigest(),
    constants=dict(kappa=kappa,U=U,T=T,ell=ell,u=u,v=v,E=E,lambda_lower=lam,R=R),
    offsets=dict(prefix_H_floor=7,prefix_tail2_upper=prefix_offset,
                 recipient_H_floor=72,recipient_Q_lower=recipient_Q,required_Q=required_Q),
    exponential_terms=exp_terms,tables=tables,checks=construction_checks,
    summary=dict(checks=len(construction_checks),tables=28,recipients=616,
                 minimum_margin=minimum,minimum_d=md,minimum_j=mj,
                 required_margin=F(47,4),failures=[],passed=True),
    limitations='No cyclic-order, last-pair/survivor, H/seed, integrality, realization or actual-word conclusion.')
compare('complete_construction',stored,expected)
# Check the printed d6 table independently, not only its certificate.
lemma = (ROOT/'lemmas/L091-uniform-literal-early-support-exclusion.md').read_text()
printed = [tuple(map(int,x)) for x in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|$',lemma,re.M)]
compare('L091_printed_d6',printed,[(m['j'],m['A'],m['D'],int(m['margin']*scale)) for m in tables[0]['margins']])
verify('printed uniform minimum',minimum,'=',F(5877662392133,500000000000))
verify('printed prefix offset',prefix_offset,'=',F(-3969,1408))
verify('printed recipient Q',recipient_Q,'=',F(67585198634830509743348335148655587,12986507827891524337664))
verify('all 7146 comparisons present',len(construction_checks),'=',7146)
verify('all 616 errors present',len(errors),'=',616)
verify('unique construction names',len({c['name'] for c in construction_checks}),'=',7146)
max_error = max(e['upper'] for e in errors)
output = HERE/'uniform-early-support-audit-certificate.json'
result = dict(reconstructed=expected,logarithms=logs,lambda_interval=lambda_interval,
              amplified_errors=errors,proof_checks=verification,
              construction_sha256=hashlib.sha256(stored_bytes).hexdigest(),
              summary=dict(comparison_leaves=leaf_count,construction_checks=len(construction_checks),
                           proof_checks=len(verification),tables=28,margins=616,
                           minimum_margin=minimum,minimum_d=md,minimum_j=mj,
                           required_margin=F(47,4),max_error_upper=max_error,
                           error_required_upper=F(1,1000),failures=failures,passed=not failures))
output.write_text(json.dumps(result,indent=2,default=str)+'\n')
print(f'Independent reconstruction: {len(tables)}/28 tables; {len(errors)}/616 margins.')
print(f'Complete comparisons: {leaf_count} leaves, {len(construction_checks)} construction checks; {len(verification)} proof checks.')
print(f'Minimum M({md},{mj})={minimum}; required >47/4>0. All outward errors required in (0,1/1000).')
print(f'Prefix offset={prefix_offset}<0; recipient Q={recipient_Q}>{required_Q}.')
print(f'Failures: {len(failures)}; {failures[:10]}')
print(f'Certificate: {output.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)

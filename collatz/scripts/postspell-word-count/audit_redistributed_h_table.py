#!/usr/bin/env python3
"""Independent, read-only audit of L079's existing certificate.

Does not import or execute its constructor. Reconstructs every mathematical
field and comparison; independently checks Lambda using log3=log2+log(3/2).
The proof of each analytic remainder and factored bound is in L079's audit.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import operator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INPUT = HERE / 'redistributed-h-table-certificate.json'
raw = INPUT.read_bytes()
c = json.loads(raw)
records, failures = [], []


def serial(x):
    if isinstance(x, F):
        return str(x)
    raise TypeError(type(x).__name__)


def test(name, actual, relation, required):
    operations = {'=': operator.eq, '<': operator.lt, '<=': operator.le,
                  '>': operator.gt, '>=': operator.ge}
    ok = operations[relation](actual, required)
    records.append(dict(name=name, actual=actual, relation=relation,
                        required=required, passed=ok))
    if not ok:
        failures.append(name)


def match(path, actual, expected):
    """Traverse complete evidence, including every array entry and rational."""
    if isinstance(expected, dict):
        test(path + ':keys', sorted(actual), '=', sorted(expected))
        for key, value in expected.items():
            match(path + '/' + str(key), actual[key], value)
    elif isinstance(expected, list):
        test(path + ':length', len(actual), '=', len(expected))
        for i, value in enumerate(expected):
            match(path + '/' + str(i), actual[i], value)
    else:
        test(path, F(actual) if isinstance(expected, F) else actual, '=', expected)


# Separately transcribed from L055, then compared with its complete table.
J = [8,15,28,52,98,184,347,653,1230,2317,4365,8224,15494,29191,
     54998,103621,195229,367827,693015,1305695,2460032,4634896,
     8732512,16452748,30998279]
oldH = [40,72,134,249,467,877,1650,3106,5849,11018,20756,39104,
        73672,138802,261511,492705,928293,1748976,3295208,6208431,
        11697176,22038409,41522114,78230965,32670621]
source = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
source_raw = source.read_bytes()
source_table = []
for line in source_raw.decode().splitlines():
    cells = line.split('|')
    if len(cells) == 5 and all(v.isdecimal() for v in cells[1:4]):
        source_table.append([int(v) for v in cells[1:4]])
match('L055/table', source_table, [[i,J[i],oldH[i]] for i in range(25)])
match('source', c['source'], dict(path=str(source.relative_to(ROOT)),
                               sha256=hashlib.sha256(source_raw).hexdigest()))
H = oldH.copy()
H[0] -= 1
H[24] += 1
match('table', c['table'], [[i,J[i],H[i]] for i in range(25)])
r, B, tau, p, q = 25, 9250245, 2, 23, 24
kappa = F(23,11)
K = 3*sum(J)+sum(H)
N = 4*sum(J)+sum(H)+2*r+18*B
match('totals', c['totals'], dict(r=r,B=B,tau=tau,K=K,N=N))


def logarithm(x, count):
    z = (x-1)/(x+1)
    # Recurrence for numerator powers, independent of stored term generation.
    power, terms = 2*z, []
    for denominator in range(1, 2*count, 2):
        terms.append(power/denominator)
        power *= z*z
    lower = sum(terms, F(0))
    rem = power/((2*count+1)*(1-z*z))
    test(f'log{x},m={count}:positive z', z, '>', 0)
    test(f'log{x},m={count}:z<1', z, '<', 1)
    return dict(argument=x,z=z,count=count,terms=terms,lower=lower,
                remainder_upper=rem,upper=lower+rem)


logs = {s: logarithm(F(s),100) for s in ['2','3','11/4']}
match('logs', c['logs'], logs)
lam = [N*logs['2']['lower']-K*logs['3']['upper'],
       N*logs['2']['upper']-K*logs['3']['lower']]
match('lambda_interval', c['lambda_interval'], lam)
lm, lp = F(10584,10**14), F(10585,10**14)
ell, u, v = [F(x,10**12) for x in [693147180559,1098612288669,1011600911679]]

# A different, tighter rational enclosure, with no reuse of stored log3.
l2, l32 = logarithm(F(2),120), logarithm(F(3,2),120)
ind_lam = [(N-K)*l2['lower']-K*l32['upper'],
           (N-K)*l2['upper']-K*l32['lower']]
test('independent Lambda lower', ind_lam[0], '>', lm)
test('independent Lambda upper', ind_lam[1], '<', lp)
test('independent enclosure inside stored lower', ind_lam[0], '>', lam[0])
test('independent enclosure inside stored upper', ind_lam[1], '<', lam[1])
exp_terms = {}
for t in [24,27]:
    terms = [F(1)]
    for k in range(1,41):
        terms.append(terms[-1]*t/k)
    exp_terms[str(t)] = terms
match('exp_terms', c['exp_terms'], exp_terms)
exp = {int(t): sum(terms,F(0)) for t,terms in exp_terms.items()}

# Complete recomputation of every named comparison stored by construction.
expected_checks = {}


def obligation(name, actual, relation, required):
    a,b = F(actual),F(required)
    test(name,a,relation,b)
    ok = records[-1]['passed']
    expected_checks[name] = dict(name=name,actual=a,relation=relation,
                                required=b,difference=a-b,passed=ok)


for name,a,b in [('sum J',sum(J),66061058),('sum H',sum(H),199390205),
                 ('K',K,397573379),('N',N,630138897),
                 ('full allocated tail sum',2*r+18*B,166504460)]:
    obligation(name,a,'=',b)
for name,a,rel,b in [
    ('fresh Lambda lower',lm,'<',lam[0]),('fresh Lambda upper',lam[1],'<',lp),
    ('positive lambda lower',lm,'>',0),('lambda upper below one',lp,'<',1),
    ('positive ell',ell,'>',0),('ell below log2',ell,'<',logs['2']['lower']),
    ('u above log3',u,'>',logs['3']['upper']),
    ('v above log11over4',v,'>',logs['11/4']['upper']),
    ('order v=2 above log11over4',2,'>',logs['11/4']['upper'])]:
    obligation(name,a,rel,b)
A = [sum(3*J[j]+H[j] for j in range(i)) for i in range(26)]
D = [sum(4*J[j]+H[j]+2 for j in range(i)) for i in range(26)]
obligation('closing base odd exponent',A[25],'=',K)
obligation('closing base denominator plus budget',D[25]+18*B,'=',N)
cap = r*kappa/lm+kappa
obligation('O cap below exp27 partial sum',cap,'<',exp[27])
offset = F(81,44)-F(3,11)*F(3,2)**39
om = [4*J[k+1]*ell-29-A[k]*u+D[k]*ell for k in range(24)]
for i in range(25):
    obligation(f'O row {i} H floor',H[i],'>=',39)
    obligation(f'O row {i} tail2 offset upper',offset,'<',0)
for k in range(24):
    obligation(f'O displacement {k}',om[k],'>',0)
match('O',c['O'],dict(lambda_lower=lm,T=27,ell=ell,u=u,v=F(2),cap=cap,
    offsets=[dict(i=i,H=H[i],H_floor=39,d_upper=offset) for i in range(25)],
    margins=[dict(k=k,row=k+1,A=A[k],D=D[k],margin=om[k]) for k in range(24)]))
E = F(552,4*2**(4*J[1])-23)
root = kappa/(lm-E)+kappa
earlyQ = F(12,11)*F(3,2)**39+1
sm = [(D[j+1]+18+4*J[j+1])*ell-24-v-A[j+1]*u for j in range(23)]
obligation('S residual positive',lm-E,'>',0)
obligation('S root below U',root,'<',20*10**9)
obligation('S U below exp24 partial sum',20*10**9,'<',exp[24])
for j in range(23):
    obligation(f'S row {j} H floor',H[j],'>=',39)
    obligation(f'S row {j} tail20 Q lower',earlyQ,'>',kappa*2**20)
    obligation(f'S recipient {j}',sm[j],'>',0)
match('S',c['S'],dict(lambda_lower=lm,E=E,residual=lm-E,root_cap=root,
    U=F(20*10**9),T=24,ell=ell,u=u,v=v,
    offsets=[dict(i=i,H=H[i],H_floor=39,Q_lower=earlyQ) for i in range(23)],
    margins=[dict(j=j,input=j+1,A=A[j+1],D=D[j+1],margin=sm[j]) for j in range(23)]))

eta = kappa-F(16,27)**J[0]*(F(12,11)+F(2,3)**H[0])
domain = 2*(1-lp)/lp
tails = [2]*23+[2+18*tau,2+18*(B-tau)]
obligation('C eta0 above e',eta,'>',2)
obligation('C eta_q J comparison',J[q],'>=',J[0])
obligation('C eta_q H comparison',H[q],'>=',H[0])
obligation('C uniform unshifted domain',domain,'>=',47)
obligation('C boundary tail sum',sum(tails),'=',2*r+18*B)
obligation('C boundary p tail',tails[p],'=',38)
obligation('C boundary q tail',tails[q],'=',166504376)
first = F(27,16)**J[0]*F(3,2)**H[0]/2**tails[0]
baseline = F(27,16)**15*F(3,2)**72/2**38
obligation('C row0 multiplier lower',first,'>',10**8)
obligation('C other incoming multiplier baseline',baseline,'>',2)
factors = [dict(i=0,J=J[0],H=H[0],a=tails[0],exact_multiplier=first,lower=F(10**8))]
for i in range(1,24):
    obligation(f'C factor {i} J floor',J[i],'>=',15)
    obligation(f'C factor {i} H floor',H[i],'>=',72)
    obligation(f'C factor {i} tail ceiling',tails[i],'<=',38)
    factors.append(dict(i=i,J=J[i],H=H[i],a=tails[i],baseline=baseline,lower=F(2)))
L = [F(1)]
for f in factors:
    L.append(L[-1]*f['lower'])
for i in range(1,25):
    obligation(f'C prefix lower induction {i}',L[i-1]*factors[i-1]['lower'],'=',L[i])
incomingD = [sum(4*J[j]+H[j]+tails[j] for j in range(i)) for i in range(26)]
test('closing boundary denominator',incomingD[25],'=',N)
test('all lower prefixes positive',all(x>0 for x in L),'=',True)
CQ = kappa*(1+F(2,10**8))
need = CQ/lm+CQ+kappa/L[q]
CU = CQ/lm+CQ+kappa
cm = 24+A[q]*u-(incomingD[q]+4*J[q])*ell+v
obligation('C Q bounds all 25 inverse prefixes',kappa*sum(1/x for x in L),'<=',CQ)
obligation('C normalized cap below U',need,'<=',CU)
obligation('C U below 20 billion',CU,'<',20*10**9)
obligation('C U below exp24 partial sum',CU,'<',exp[24])
obligation('C incoming odd exponent',A[q],'=',271907920)
obligation('C incoming denominator exponent',incomingD[q],'=',306970783)
obligation('C final strict boundary margin',cm,'<',0)
match('C',c['C'],dict(lambda_lower=lm,lambda_upper=lp,e=F(2),eta0=eta,
    eta_q_lower_justification='J_q>=J_0, H_q>=H_0; both subtracted bases lie in (0,1)',
    domain_lower=domain,boundary_tails=tails,factor_certificates=factors,
    incoming=[dict(i=i,A=A[i],denominator_exponent=incomingD[i],lower=L[i],reciprocal=1/L[i]) for i in range(25)],
    prefix_proof='C_0=L_0=1; C_(i+1)=C_i*c_i>=L_i*factor_lower_i=L_(i+1)',
    Q=CQ,normalized_cap=need,U=CU,T=24,ell=ell,u=u,v=v,margin=cm))

stored = {row['name']:row for row in c['checks']}
test('no duplicate stored comparisons',len(stored),'=',len(c['checks']))
match('checks',stored,expected_checks)
integer = dict(r_at_least_three=r>=3,budget_nonnegative=B>=0,cutoff_admitted=0<=tau<=B,
    indexed_rows=c['table']==[[i,J[i],H[i]] for i in range(25)],
    pair_domain=all(j>=2 and h>=3 for j,h in zip(J,H)),
    increasing_J=all(J[i]<J[i+1] for i in range(24)),
    changed_rows_only=[(i,H[i]-oldH[i]) for i in range(25) if H[i]!=oldH[i]]==[(0,-1),(24,1)],
    order_indices=[d['k'] for d in c['O']['margins']]==list(range(24)),
    support_indices=[d['j'] for d in c['S']['margins']]==list(range(23)),
    all_25_incoming=[d['i'] for d in c['C']['incoming']]==list(range(25)),
    all_boundary_tails=all(a>=2 and a%18==2 for a in tails),
    final_tail_at_B=2+18*(B-B)==2,
    c0_exponents=(3*J[0]+H[0],4*J[0]+H[0]+tails[0])==(63,73))
match('integer_checks',c['integer_checks'],integer)
test('all integer/domain obligations',all(integer.values()),'=',True)
match('summary',c['summary'],dict(rational_checks=len(expected_checks),integer_checks=len(integer),
    min_order_margin=min(om),min_support_margin=min(sm),cutoff_margin=cm,
    failures=[],verdict='ALL C077a DATA TESTS CERTIFIED'))

# Verify every printed margin in the canonical lemma, including its indices.
lemma = (ROOT/'lemmas/L079-redistributed-h-table-data-certificate.md').read_text()
printed = []
for line in lemma.splitlines():
    cells = line.split('|')
    if len(cells)==5 and cells[1].isdecimal():
        printed.append([int(cells[1]),int(cells[2]),None if cells[3]=='—' else int(cells[3])])
match('L079/printed_margins',printed,[[i,int(om[i]*10**12),int(sm[i]*10**12) if i<23 else None] for i in range(24)])
for i,m in enumerate(om+sm):
    test(f'printed scaled margin {i} is integer',(m*10**12).denominator,'=',1)
for name,a,rel,b in [
    ('printed O cap',cap,'=',F(7187500000030429,14553)),
    ('printed S root cap',root,'=',F(1325859730438202850942226985830949,67113790726173775832193)),
    ('printed eta0',eta,'=',F(2374185650978801216525801124919,1144561273430837494885949696427)),
    ('printed domain',domain,'=',F(39999999995766,2117)),
    ('printed C U',CU,'=',F(435606069410390910013,22050000000)),
    ('printed O minimum',min(om),'=',F(629441541677,50000000000)),
    ('printed S minimum',min(sm),'=',F(2431999810929,250000000000)),
    ('printed C margin',cm,'=',-F(2102267684691,500000000000)),
    ('O claimed threshold',min(om),'>',F('12.58')),
    ('S claimed threshold',min(sm),'>',F('9.72')),
    ('C claimed threshold',cm,'<',-F('4.20')),
    ('O cap intermediate',cap,'<',500000000000),
    ('exp27 intermediate',exp[27],'>',500000000000),
    ('support minimum index',sm.index(min(sm)),'=',4),
    ('v below 2',v,'<',2)]:
    test(name,a,rel,b)

result = dict(input=str(INPUT.relative_to(ROOT)),sha256=hashlib.sha256(raw).hexdigest(),
    independent_logs={'2':l2,'3/2':l32},independent_lambda=ind_lam,
    exact_inverse_prefix_sum=sum(1/x for x in L),records=records,
    summary=dict(checks=len(records),construction_comparisons=len(expected_checks),
        stored_log_terms=300,stored_exp_terms=82,incoming_prefixes=25,
        order_margins=24,support_margins=23,O_min=min(om),S_min=min(sm),C_margin=cm,
        failures=failures,verdict='NO DEFECT FOUND' if not failures else 'DEFECT FOUND'))
out = HERE/'redistributed-h-table-audit-certificate.json'
out.write_text(json.dumps(result,indent=2,default=serial)+'\n')
print(f'Audit: {len(records)} checks; {len(expected_checks)} construction comparisons; failures {failures}')
print(f'O minimum {min(om)} > 12.58 > 0; S minimum {min(sm)} > 9.72 > 0')
print(f'C boundary {cm} < -4.20 < 0; domain {domain} >= 47')
print(f'Independent Lambda: {lm} < actual < {lp}; required 0 < Lambda < 1')
print(f'Full audit certificate: {out.relative_to(ROOT)}')
assert not failures

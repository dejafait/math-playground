#!/usr/bin/env python3
"""L093 only: independent table, analytic and applicability reconstruction.

No constructor or earlier audit module is imported or executed. The analytic
remainder is the previously assessed positive-real logarithm series bound.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'uniform-literal-survivor-h-applicability-certificate.json'
OUTPUT = HERE / 'uniform-literal-survivor-h-audit-certificate.json'
raw = SOURCE.read_bytes()
stored = json.loads(raw)
base = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
        (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
        (8224,39104),(15494,73672),(29191,138802),(54998,261511),
        (103621,492705),(195229,928293),(367827,1748976),
        (693015,3295208),(1305695,6208431),(2460032,11697176),
        (4634896,22038409),(8732512,41522114),(16452748,78230965),
        (30998279,32670621)]
B = 9250245
kappa, lo, hi = F(23,11), F(10584,10**14), F(10585,10**14)
ell, u = F(693147180559,10**12), F(1098612288669,10**12)
checks, failures, reconstructed, evidence = [], [], [], []
leaves = 0

def check(name, a, relation, b):
    a, b = F(a), F(b)
    ok = {'=':a==b, '<':a<b, '>':a>b, '<=':a<=b, '>=':a>=b}[relation]
    item = dict(name=name, actual=a, relation=relation, required=b,
                difference=a-b, passed=ok)
    checks.append(item)
    if not ok:
        failures.append(item)

def compare(path, actual, expected):
    global leaves
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or set(actual) != set(expected):
            failures.append(dict(path=path, actual=actual, expected=expected))
            return
        for key, value in expected.items():
            compare(path+'/'+str(key), actual[key], value)
    elif isinstance(expected, (list, tuple)):
        if not isinstance(actual, (list, tuple)) or len(actual) != len(expected):
            failures.append(dict(path=path, actual=actual, expected=expected))
            return
        for i, value in enumerate(expected):
            compare(path+'/'+str(i), actual[i], value)
    else:
        leaves += 1
        try:
            matched = F(actual) == expected if isinstance(expected,F) else actual == expected
        except (ValueError, TypeError):
            matched = False
        if not matched:
            failures.append(dict(path=path, actual=actual, expected=expected))

canonical = (ROOT/'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [list(map(int,row)) for row in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$',canonical,re.M)]
compare('canonical_table',table,[[i,j,h] for i,(j,h) in enumerate(base)])

def logarithm(x):
    z = (F(x)-1)/(F(x)+1)
    power = z
    terms = []
    for k in range(100):
        terms.append(2*power/(2*k+1))
        power *= z*z
    rem = 2*power/(201*(1-z*z))
    lower = sum(terms,F(0))
    return dict(z=z,terms=terms,remainder=rem,lower=lower,upper=lower+rem)

logs = {str(x):logarithm(x) for x in (2,3)}
l2,h2 = logs['2']['lower'],logs['2']['upper']
l3,h3 = logs['3']['lower'],logs['3']['upper']
K,N = 397573379,630138897
lam = [N*l2-K*h3,N*h2-K*l3]
exp_terms = [F(1)]
for k in range(1,41):
    exp_terms.append(exp_terms[-1]*F(24,k))
exp_lower = sum(exp_terms,F(0))
check('positive lambda lower',lo,'>',0)
check('Lambda lower',lam[0],'>',lo)
check('Lambda upper',lam[1],'<',hi)
check('lambda upper below one',hi,'<',1)
check('ell positive',ell,'>',0)
check('ell below log2',ell,'<',l2)
check('u above log3',u,'>',h3)
check('exp24 lower sum',exp_lower,'>',20000000000)
check('domain',2*(1-hi)/hi,'>',47)
check('weak tail38 common factor',F(3**117,2**170),'>',2)
check('universal eta endpoint lower',kappa-F(16,27)**8*(F(12,11)+F(2,3)**3),'>',2)

for d in range(6,34):
    pairs = list(base)
    pairs[0] = (8,40-d)
    pairs[24] = (30998279,32670621+d)
    w = 10**8*F(2,3)**(d-1)
    L = [F(1)]+[w*2**i for i in range(24)]
    recips = [1/x for x in L]
    total = sum(recips,F(0))
    Q = kappa*total
    cap = Q/lo+Q+kappa/min(L)
    A,D0 = [0],[0]
    for j,h in pairs:
        A.append(A[-1]+3*j+h)
        D0.append(D0[-1]+4*j+h+2)
    p = A[18]+3*pairs[18][0]
    r = D0[18]+4*pairs[18][0]+pairs[18][1]
    margin = 24+p*u-r*ell
    small = []
    for name,left,relation,right in [('w_d>1',w,'>',F(1)),
            ('H normalized cap',cap,'<',F(20000000000)),
            ('own-input row18 upper margin',margin,'<',F(0))]:
        check(f'd{d} {name}',left,relation,right)
        small.append(dict(name=name,left=left,relation=relation,right=right,
            left_minus_right=left-right,passes=checks[-1]['passed']))
    reconstructed.append(dict(d=d,H_0=40-d,H_24=32670621+d,w_d=w,L_i=L,
        L_star=min(L),complete_reciprocal_sum=total,Q_d=Q,R_H=cap,
        A_18=A[18],D_18_at_t0=D0[18],P=p,R=r,F_18=margin,checks=small))
    check(f'd{d} geometric sum',total,'=',1+2/w*(1-F(1,2**24)))
    check(f'd{d} actual L minimum',min(L),'=',1)
    check(f'd{d} prefix A18',A[18],'=',6078923-(d-1))
    check(f'd{d} prefix D18',D0[18],'=',6862840-(d-1))
    check(f'd{d} margin identity',margin,'=',-F(457745289,50000000000)-(d-1)*(u-ell))
    check(f'd{d} uniform margin',margin,'<=',-F(203648044633,100000000000))
    c0 = F(3**(64-d),2**(74-d))
    eta0 = kappa-F(16,27)**8*(F(12,11)+F(2,3)**(40-d))
    check(f'd{d} c0>w',c0,'>',w)
    check(f'd{d} eta0',eta0,'>',2)
    check(f'd{d} eta0<kappa',eta0,'<',kappa)
    check(f'd{d} eta24 J comparison',pairs[24][0],'>=',pairs[0][0])
    check(f'd{d} eta24 H comparison',pairs[24][1],'>=',pairs[0][1])
    for i,(j,h) in enumerate(pairs):
        check(f'd{d} row{i} J',j,'>=',2)
        check(f'd{d} row{i} H',h,'>=',7)
        if i:
            check(f'd{d} row{i} increasing J',j,'>',pairs[i-1][0])
            check(f'd{d} incoming{i} L induction',L[i-1]*(w if i==1 else 2),'=',L[i])
    allocations = []
    for t in (0,1):
        tails = [2]*23+[2+18*t,2+18*(B-t)]
        den = [0]
        factors = []
        for i,((j,h),tail) in enumerate(zip(pairs,tails)):
            den.append(den[-1]+4*j+h+tail)
            check(f'd{d} t{t} row{i} tail',tail,'>=',2)
            check(f'd{d} t{t} row{i} congruence',tail%18,'=',2)
            if 1<=i<=23:
                a,b = 3*j+h,4*j+h+tail+1
                interval = [a*l3-b*h2,a*h3-b*l2]
                factors.append(dict(i=i,A=a,D_plus_one=b,log_c_over_2=interval))
                check(f'd{d} t{t} row{i} actual factor>2',interval[0],'>',0)
                check(f'd{d} t{t} row{i} common J',j,'>=',15)
                check(f'd{d} t{t} row{i} common H',h,'>=',72)
                check(f'd{d} t{t} row{i} common tail',tail,'<=',38)
        for i in range(25):
            check(f'd{d} t{t} incoming{i} exponent',den[i],'=',D0[i]+(18*t if i==24 else 0))
        check(f'd{d} t{t} K',A[-1],'=',K)
        check(f'd{d} t{t} N including closure',den[-1],'=',N)
        check(f'd{d} t{t} complete tail sum',sum(tails),'=',166504460)
        allocations.append(dict(t=t,tails=tails,A=A,D=den,factors=factors))
    error = [p*(u-h3)+r*(l2-ell),p*(u-l3)+r*(h2-ell)]
    check(f'd{d} positive H coefficient P',p,'>',0)
    check(f'd{d} positive H coefficient R',r,'>',0)
    check(f'd{d} outward H error positive',error[0],'>',0)
    check(f'd{d} outward H error ordered',error[1],'>',error[0])
    evidence.append(dict(d=d,pairs=pairs,c0=c0,eta0=eta0,reciprocals=recips,
        allocations=allocations,row18_outward_error=error))

expected = dict(scope=dict(d=[6,33],t=[0,1],r=25,B=B,
    tail_pairs=[[2,166504412],[20,166504394]],incoming_indices=[0,24],
    closing_product_lower_bound_assumed=False),
    inputs=['L055','L077','L083','L084'],
    constants=dict(kappa=kappa,lambda_minus=lo,ell=ell,u=u,
        required_cap=20000000000,required_margin_upper_bound=0),
    tables=reconstructed,summary=dict(tables=28,checks=84,failures=0,
        max_R_H_d=33,max_F_18_d=6,all_L_star_equal_one=True))
# Only the free-text kind label is excluded, not mathematical fields.
compare('applicability',{k:v for k,v in stored.items() if k!='kind'},expected)
maxcap = max(x['R_H'] for x in reconstructed)
maxmargin = max(x['F_18'] for x in reconstructed)
check('quoted maximum cap',maxcap,'=',F(208953172694278031610263934769714811527,10486541660339652526080000000))
check('quoted minimum w',reconstructed[-1]['w_d'],'=',F(429496729600000000,1853020188851841))
report = dict(source=str(SOURCE.relative_to(ROOT)),sha256=hashlib.sha256(raw).hexdigest(),
    scope='Only L093 audit, d=6..33,t=0,1; no wider assembly or exclusions.',
    reconstruction=expected,logs=logs,lambda_interval=lam,
    lambda_errors=[N*logs['2']['remainder'],K*logs['3']['remainder']],
    exp24_terms=exp_terms,exp24_lower=exp_lower,tables=evidence,
    checks=checks,failures=failures,
    summary=dict(tables=28,roots=56,leaf_comparisons=leaves,proof_checks=len(checks),
        failures=len(failures),maximum_cap=maxcap,required_cap=20000000000,
        maximum_H_upper=maxmargin,required_H_upper=0))
OUTPUT.write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps(report['summary'],default=str))
print('Complete rational evidence, operands, thresholds and failures:',OUTPUT.relative_to(ROOT))
if failures:
    print('First failure location:',failures[0].get('path',failures[0].get('name')))
    raise SystemExit(1)

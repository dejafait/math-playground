#!/usr/bin/env python3
"""Independent, fixed-scope arithmetic audit of L088 (only t=0,1).

Reconstruct the complete applicability certificate and the required analytic
and incoming-factor bounds. No constructor or family-audit module is run.
Analytic remainder formulas are the previously assessed L084 inputs.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INPUT = HERE / 'd5-literal-survivor-h-applicability-certificate.json'
OUTPUT = HERE / 'd5-literal-survivor-h-audit-certificate.json'
raw = INPUT.read_bytes()
stored = json.loads(raw)
original = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
            (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
            (8224,39104),(15494,73672),(29191,138802),(54998,261511),
            (103621,492705),(195229,928293),(367827,1748976),
            (693015,3295208),(1305695,6208431),(2460032,11697176),
            (4634896,22038409),(8732512,41522114),(16452748,78230965),
            (30998279,32670621)]
pairs = list(original)
pairs[0], pairs[24] = (8,35), (30998279,32670626)
kappa, low, high = F(23,11), F(10584,10**14), F(10585,10**14)
ell, u = F(693147180559,10**12), F(1098612288669,10**12)
budget = 9250245
rows = [[i,j,h] for i,(j,h) in enumerate(pairs)]
w = F(1600000000,81)
L = [F(1)] + [w*2**i for i in range(24)]
reciprocals = [1/x for x in L]
mass = kappa*sum(reciprocals,F(0))
cap = mass/low+mass+kappa/min(L)
odd = [3*j+h for j,h in pairs]
den0 = [4*j+h+2 for j,h in pairs]
A, D0 = [0], [0]
for a,d in zip(odd,den0):
    A.append(A[-1]+a)
    D0.append(D0[-1]+d)
K, N = A[-1], D0[-1]+18*budget
J18,H18 = pairs[18]
P,R = A[18]+3*J18,D0[18]+4*J18+H18
margin = 24+P*u-R*ell
eta0 = kappa-F(16,27)**8*(F(12,11)+F(2,3)**35)
c0 = F(3**59,2**69)
domain = 2*(1-high)/high
allocations = []
for t in (0,1):
    tails = [2]*23+[2+18*t,2+18*(budget-t)]
    allocations.append(dict(t=t,tails=tails,K=K,
        N=sum(4*j+h+a for (j,h),a in zip(pairs,tails))))

checks, mismatches = [], []
def check(name,a,op,b,where=checks):
    a,b = F(a),F(b)
    ok = {'=':a==b,'>':a>b,'<':a<b,'>=':a>=b,'<=':a<=b}[op]
    item = dict(name=name,actual=a,relation=op,required=b,difference=a-b,passed=ok)
    where.append(item)
    if not ok:
        mismatches.append(dict(path='check/'+name,actual=a,relation=op,required=b))

check('complete reciprocal sum',sum(reciprocals,F(0)),'=',F(2684354831790883,2684354560000000))
check('actual minimum L',min(L),'=',1)
check('H Q',mass,'=',F(61740161131190309,29527900160000000))
check('H cap matches audited d5',cap,'=',F(771752014303243320582804778807,39065411911680000000))
check('H cap below U',cap,'<',20000000000)
check('row0 multiplier above w',c0,'>',w)
check('common unchanged and tail20 factor above 2',F(3**117,2**170),'>',2)
check('endpoint eta lower',eta0,'>',2)
check('endpoint domain lower',domain,'>',47)
check('incoming A18',A[18],'=',6078919)
check('incoming D18',D0[18],'=',6862836)
check('row18 upper margin',margin,'=',F(-81550766911,50000000000))
check('row18 margin sign',margin,'<',0)
for a in allocations:
    check(f"t={a['t']} total K",a['K'],'=',397573379)
    check(f"t={a['t']} closing N",a['N'],'=',630138897)
    check(f"t={a['t']} tail sum",sum(a['tails']),'=',166504460)
expected = dict(inputs=['L055','L077','L083','L084'],rows=rows,
    allocations=allocations,L=L,reciprocal_sum=sum(reciprocals,F(0)),Q=mass,
    lambda_H=low,ell=ell,u=u,cap=cap,
    row18=dict(A=A[18],D_at_0=D0[18],J=J18,H=H18,P=P,R=R,F=margin),
    checks=checks,failures=[])
compared = 0
def compare(path,a,b):
    global compared
    if isinstance(b,dict):
        if not isinstance(a,dict) or set(a)!=set(b):
            mismatches.append(dict(path=path,actual=a,expected=b))
            return
        for k in b:
            compare(path+'/'+str(k),a[k],b[k])
    elif isinstance(b,(list,tuple)):
        if not isinstance(a,(list,tuple)) or len(a)!=len(b):
            mismatches.append(dict(path=path,actual=a,expected=b))
            return
        for i,v in enumerate(b):
            compare(path+'/'+str(i),a[i],v)
    else:
        compared += 1
        if isinstance(b,F):
            a=F(a)
        if a!=b:
            mismatches.append(dict(path=path,actual=a,expected=b))

# The sole excluded field is the prose scope, not mathematical evidence.
compare('applicability',{k:v for k,v in stored.items() if k!='scope'},expected)
canonical = (ROOT/'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
canonical_rows = [list(map(int,m)) for m in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$',canonical,re.M)]
compare('canonical-original-table',canonical_rows,[[i,j,h] for i,(j,h) in enumerate(original)])

def log_interval(x):
    z=(x-1)/(x+1)
    terms=[2*z**(2*k+1)/F(2*k+1) for k in range(100)]
    remainder=2*z**201/(201*(1-z*z))
    lower=sum(terms,F(0))
    return dict(argument=x,z=z,terms=terms,remainder=remainder,
                lower=lower,upper=lower+remainder)
logs={str(x):log_interval(F(x)) for x in (2,3)}
l2,h2=logs['2']['lower'],logs['2']['upper']
l3,h3=logs['3']['lower'],logs['3']['upper']
lam=[N*l2-K*h3,N*h2-K*l3]
exp_terms=[F(1)]
for k in range(1,41):
    exp_terms.append(exp_terms[-1]*24/k)
exp_lower=sum(exp_terms,F(0))
extra=[]
def prove(name,a,op,b):
    check(name,a,op,b,extra)
prove('lambda lower positive',low,'>',0)
prove('Lambda lower',lam[0],'>',low)
prove('Lambda upper',lam[1],'<',high)
prove('lambda upper below one',high,'<',1)
prove('ell positive',ell,'>',0)
prove('ell below log2 lower',ell,'<',l2)
prove('u above log3 upper',u,'>',h3)
prove('U below exp24 lower',20000000000,'<',exp_lower)
prove('eta0 below kappa',eta0,'<',kappa)
prove('eta_q J monotonicity',pairs[24][0],'>=',pairs[0][0])
prove('eta_q H monotonicity',pairs[24][1],'>=',pairs[0][1])
prove('w above one',w,'>',1)
for i,(j,h) in enumerate(pairs):
    prove(f'row{i} J domain',j,'>=',2)
    prove(f'row{i} H domain',h,'>=',3)
    if i:
        prove(f'row{i} increasing J',j,'>',pairs[i-1][0])
    prove(f'incoming{i} L positive',L[i],'>',0)
    prove(f'incoming{i} L >= actual minimum',L[i],'>=',min(L))

full_allocations=[]
for a in allocations:
    t,tails=a['t'],a['tails']
    D=[0]
    factors=[]
    for i,((j,h),tail) in enumerate(zip(pairs,tails)):
        exponent=4*j+h+tail
        D.append(D[-1]+exponent)
        prove(f't{t} row{i} tail domain',tail,'>=',2)
        prove(f't{t} row{i} tail congruence',tail%18,'=',2)
        if 1<=i<=23:
            interval=[odd[i]*l3-(exponent+1)*h2,odd[i]*h3-(exponent+1)*l2]
            factors.append(dict(i=i,A=odd[i],D=exponent,log_c_over_2=interval))
            prove(f't{t} row{i} factor >2',interval[0],'>',0)
            prove(f't{t} row{i} J common bound',j,'>=',15)
            prove(f't{t} row{i} H common bound',h,'>=',72)
            prove(f't{t} row{i} tail common bound',tail,'<=',38)
    incoming=[]
    for i in range(25):
        prove(f't{t} incoming{i} exact exponent',D[i],'=',D0[i]+(18*t if i==24 else 0))
        if i:
            prove(f't{t} incoming{i} L induction',L[i-1]*(w if i==1 else 2),'=',L[i])
        incoming.append(dict(i=i,A=A[i],D=D[i],L=L[i],reciprocal=reciprocals[i]))
    prove(f't{t} full closing exponent',D[-1],'=',N)
    full_allocations.append(dict(t=t,tails=tails,denominator_prefixes=D,
                                 factors=factors,incoming=incoming))
error=[P*(u-h3)+R*(l2-ell),P*(u-l3)+R*(h2-ell)]
prove('row18 outward error positive',error[0],'>',0)
prove('row18 outward error ordered',error[1],'>=',error[0])
report=dict(input=str(INPUT.relative_to(ROOT)),input_sha256=hashlib.sha256(raw).hexdigest(),
    scope='Only L088 fixed d=5 t=0,1; no assembly, order reduction or actual-word transfer.',
    reconstruction=expected,logs=logs,lambda_interval=lam,
    lambda_amplified_errors=[N*logs['2']['remainder'],K*logs['3']['remainder']],
    exp24_terms=exp_terms,exp24_lower=exp_lower,full_allocations=full_allocations,
    eta0=eta0,c0=c0,domain_lower=domain,reciprocals=reciprocals,
    row18_outward_error=error,proof_checks=extra,mismatches=mismatches,
    summary=dict(applicability_checks=len(checks),leaf_comparisons=compared,
        additional_checks=len(extra),failures=len(mismatches),
        H_cap=cap,H_cap_required=20000000000,row18_upper=margin,row18_required=0,
        closing_tails=[[x['tails'][23],x['tails'][24]] for x in allocations]))
OUTPUT.write_text(json.dumps(report,indent=2,default=str)+'\n')
print(f'Applicability checks reconstructed: {len(checks)}; leaf comparisons: {compared}; additional checks: {len(extra)}; failures: {len(mismatches)}.')
print(f'H cap {cap} < 20000000000 < certified exp(24) lower sum.')
print(f'Both own-input row18 margins < {margin} < 0; full closing exponents N={N}.')
print('Both final tail pairs:',report['summary']['closing_tails'])
print('Complete operands, analytic errors, actual/required bounds and failures:',OUTPUT.relative_to(ROOT))
if mismatches:
    print('First failure:',mismatches[0]['path'])
    raise SystemExit(1)

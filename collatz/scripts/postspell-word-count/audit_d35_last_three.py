#!/usr/bin/env python3
"""L102 audit: independent data/interval reconstruction, no constructor import.

The symbolic domain and endpoint proof is audited in L102. No sampling
or stored verdict is used to certify the quantified exclusion.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INPUT = HERE / 'd35-last-three-certificate.json'
OUTPUT = HERE / 'd35-last-three-audit-certificate.json'
PAIRS = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
         (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
         (8224,39104),(15494,73672),(29191,138802),(54998,261511),
         (103621,492705),(195229,928293),(367827,1748976),
         (693015,3295208),(1305695,6208431),(2460032,11697176),
         (4634896,22038409),(8732512,41522114),(16452748,78230965),
         (30998279,32670621)]
raw = INPUT.read_bytes()
stored = json.loads(raw)
failures, proofs, leaf_count = [], [], 0


def compare(path, actual, expected):
    global leaf_count
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or set(actual) != set(expected):
            failures.append(dict(path=path, actual=actual, expected=expected))
            return
        for k, v in expected.items():
            compare(path+'/'+str(k), actual[k], v)
    elif isinstance(expected, (list, tuple)):
        if not isinstance(actual, (list, tuple)) or len(actual) != len(expected):
            failures.append(dict(path=path, actual=actual, expected=expected))
            return
        for i, v in enumerate(expected):
            compare(path+'/'+str(i), actual[i], v)
    else:
        leaf_count += 1
        a = F(actual) if isinstance(expected, F) else actual
        if a != expected:
            failures.append(dict(path=path, actual=actual, expected=expected))


def record(name, a, op, b):
    a, b = F(a), F(b)
    verdict = {'=': a == b, '<': a < b, '>': a > b, '>=': a >= b}[op]
    return dict(name=name, actual=a, relation=op, required=b,
                difference=a-b, passed=verdict)


def prove(name, a, op, b):
    entry = record(name, a, op, b)
    proofs.append(entry)
    if not entry['passed']:
        failures.append(dict(path='proof/'+name, **entry))


source = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
source_raw = source.read_bytes()
base = [[i, j, h] for i, (j, h) in enumerate(PAIRS)]
compare('/canonical_table', [list(map(int, m)) for m in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', source_raw.decode(), re.M)], base)
rows = [row.copy() for row in base]
rows[0][2] -= 35
rows[-1][2] += 35
kap, budget, U, T = F(23,11), 9250245, F(20000000000), F(24)
ell, q, w = [F(n,10**12) for n in (693147180559,1098612288669,1011600911679)]
lam = F(10584,10**14)
E = F(24*23, 4*2**(4*rows[1][1])-23)
R = kap + kap/(lam-E)
K = sum(3*j+h for _,j,h in rows)
N = sum(4*j+h for _,j,h in rows) + 2*len(rows) + 18*budget
A = sum(3*j+h for _,j,h in rows[:23])
D = sum(4*j+h for _,j,h in rows[:23]) + 2*23
J = rows[23][1]
C = D + 18 + 4*J
M = C*ell - A*q - w - T
exp_terms = [F(1)]
for k in range(1,41):
    exp_terms.append(exp_terms[-1]*24/k)
exp_lower = sum(exp_terms, F(0))
offsets = []
for i, _, h in rows[:23]:
    hf = min(h,72)
    qlo = (12*F(3,2)**hf+11)/11
    offsets.append(dict(i=i,H_floor=hf,Q_lower=qlo,tail2_upper=kap-qlo/4))
rq = offsets[22]['Q_lower']
recipient = dict(i=22,H_floor=72,Q_lower=rq,required_Q=kap*2**20,
                 tail20_upper=kap-rq/2**20)
prefix = offsets[0]['tail2_upper']
prior_path = HERE / 'h-transfer-family-certificate.json'
prior_raw = prior_path.read_bytes()
prior = json.loads(prior_raw)['tables'][34]
compare('/L084/d',prior['d'],35)
compare('/L084/rows',prior['rows'],rows)
for key, val in dict(U=U,T=T,ell=ell,u=q,v=w,cap=R).items():
    compare('/L084/S/'+key,prior['S'][key],val)
for entry in offsets:
    i = entry['i']
    for key, val in dict(i=i,H_floor=entry['H_floor'],
                         offset_upper=entry['tail2_upper']).items():
        compare(f'/L084/O/{i}/{key}',prior['O']['offsets'][i][key],val)
compare('/L084/S/recipient/i',prior['S']['offsets'][22]['i'],22)
compare('/L084/S/recipient/Q',prior['S']['offsets'][22]['Q_lower'],rq)
for key, val in dict(j=22,A=A,D=D,margin=M).items():
    compare('/L084/S/margin/'+key,prior['S']['margins'][22][key],val)

# Rebuild every named construction comparison with independently computed
# operands, then check its complete six-field record, not just its flag.
checks = {}


def expect(name, a, op, b):
    assert name not in checks
    checks[name] = record(name,a,op,b)


for key, val in dict(U=U,T=T,ell=ell,u=q,v=w).items():
    expect('L084 S constant '+key,val,'=',val)
expect('budget positive',budget,'>',0)
for i,j,h in rows:
    expect(f'row{i} J domain',j,'>=',2)
    expect(f'row{i} H domain',h,'>=',3)
    if i:
        expect(f'row{i} increasing J',j,'>',rows[i-1][1])
expect('total K',K,'=',397573379)
expect('total N',N,'=',630138897)
expect('J1 for residual',rows[1][1],'=',15)
expect('positive residual',lam-E,'>',0)
expect('cap',R,'<',U)
expect('cap equals independent L084 datum',R,'=',R)
expect('U below exp24 lower sum',U,'<',exp_lower)
expect('prefix minimum H',min(h for _,j,h in rows[:22]),'=',5)
expect('prefix uniform tail2 offset',prefix,'<',0)
for entry in offsets:
    i,hf,o = entry['i'],entry['H_floor'],entry['tail2_upper']
    expect(f'row{i} L084 O index',i,'=',i)
    expect(f'row{i} L084 O floor',hf,'=',hf)
    expect(f'row{i} L084 O offset',o,'=',o)
    if i<22:
        expect(f'prefix row{i} tail2 offset',o,'<',0)
expect('recipient H floor',rows[22][2],'>=',72)
expect('recipient Q lower',rq,'>',kap*2**20)
expect('recipient S index',22,'=',22)
expect('recipient Q matches L084',rq,'=',rq)
expect('recipient offset',recipient['tail20_upper'],'<',0)
expect('failed full-package row0 tail20 test retained',offsets[0]['Q_lower'],'<',kap*2**20)
for key,val in dict(j=22,A=A,D=D,margin=M).items():
    expect('row22 matches L084 S '+key,val,'=',val)
expect('prefix A shift',A-sum(3*j+h for _,j,h in base[:23]),'=',-35)
expect('prefix D shift',D-sum(4*j+h+2 for _,j,h in base[:23]),'=',-35)
expect('A positive',A,'>',0)
expect('log2 coefficient positive',C,'>',0)
expect('row23 rejection margin',M,'>',25)
expect('scaled row23 margin',10**12*M,'=',25450077965484)
names = [c['name'] for c in stored['checks']]
compare('/unique_check_names',len(set(names)),len(names))
compare('/complete_check_names',sorted(names),sorted(checks))
for entry in stored['checks']:
    if entry['name'] in checks:
        compare('/checks/'+entry['name'],entry,checks[entry['name']])

fresh = dict(
    scope='Literal d35 u>=1,v>=0,u+v<=B three-tail endpoint/domain/J subsystem',
    imports='L055 table; L076 cap proof(6)-(7); audited L084 analytic enclosures',
    sources=[dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(b).hexdigest())
             for p,b in [(source,source_raw),(prior_path,prior_raw)]],
    rows=rows,B=budget,
    constants=dict(kappa=kap,U=U,T=T,ell=ell,log3_upper=q,logv_upper=w,
                   lambda_lower=lam,E=E,R=R),
    exponential_terms=exp_terms,exp24_lower=exp_lower,offsets=offsets,
    recipient=recipient,
    row23=dict(A=A,D=D,J=J,log2_coefficient=C,margin=M,scaled_margin=10**12*M),
    summary=dict(checks=len(checks),failures=[n for n,c in checks.items() if not c['passed']],
                 passed=all(c['passed'] for c in checks.values()),prefix_tail2_upper=prefix,
                 required_offset='strictly below 0',rejection_margin=M,
                 required_margin='strictly above 25 > 0',
                 uniform_domain='integers u>=1,v>=0,u+v<=9250245',parameter_samples=0),
    limitations='Construction evidence, not independent audit; no other support/order '
                'exhaustion, realization, actual-word transfer or universal descent.')
compare('/keys',sorted(stored),sorted([*fresh,'checks']))
for key,val in fresh.items():
    compare('/'+key,stored[key],val)


def log_interval(x):
    # The previously assessed positive-real series/remainder, now 120 terms.
    z = (x-1)/(x+1)
    terms = [2*z**(2*k+1)/(2*k+1) for k in range(120)]
    lo = sum(terms,F(0))
    rem = 2*z**241/(241*(1-z*z))
    return dict(argument=x,z=z,terms=terms,remainder_upper=rem,lower=lo,upper=lo+rem)


logs = {str(x):log_interval(x) for x in (F(2),F(3),F(11,4),F(3,2))}
l2,l3,lv,lr = [logs[k] for k in ('2','3','11/4','3/2')]
lambda_interval = [N*l2['lower']-K*l3['upper'],N*l2['upper']-K*l3['lower']]
lambda_alternative = [(N-K)*l2['lower']-K*lr['upper'],
                      (N-K)*l2['upper']-K*lr['lower']]
prove('lambda independently lower',lambda_interval[0],'>',lam)
prove('lambda independently upper',lambda_interval[1],'<',F(10585,10**14))
prove('alternative lambda lower',lambda_alternative[0],'>',lam)
prove('alternative lambda upper',lambda_alternative[1],'<',F(10585,10**14))
prove('ell strictly lower',ell,'<',l2['lower'])
prove('q strictly upper',q,'>',l3['upper'])
prove('w strictly upper',w,'>',lv['upper'])
error_lower = C*(l2['lower']-ell)+A*(q-l3['upper'])+(w-lv['upper'])
error_upper = C*(l2['upper']-ell)+A*(q-l3['lower'])+(w-lv['lower'])
true_margin_lower = C*l2['lower']-A*l3['upper']-lv['upper']-24
prove('outward error positive',error_lower,'>',0)
prove('exact amplified identity',true_margin_lower,'=',M+error_lower)
prove('margin threshold as printed',M,'=',F(6362519491371,250000000000))
prove('printed cap',R,'=',F(1325859730438202850942226985830949,67113790726173775832193))
prove('printed exponential sum',exp_lower,'=',F(202750314819830504045671593478515759301,7661655986496068058455078125))
prove('printed prefix sign',prefix,'=',F(-81,352))
prove('printed recipient Q',rq,'=',F(67585198634830509743348335148655587,12986507827891524337664))
for name,value,required in [('sum J',sum(j for _,j,h in rows),66061058),
                           ('sum H',sum(h for _,j,h in rows),199390205),
                           ('tail sum',50+18*budget,166504460),
                           ('printed A',A,144318677),('printed D',D,162928754),
                           ('printed next J',J,16452748),('printed C',C,228739764)]:
    prove(name,value,'=',required)
prove('all construction comparisons independently true',sum(not c['passed'] for c in checks.values()),'=',0)
prove('construction certificate unchanged',hashlib.sha256(INPUT.read_bytes()).hexdigest()==hashlib.sha256(raw).hexdigest(),'=',1)
fresh['checks'] = list(checks.values())
result = dict(scope='Independent critical audit of L102 only; no parameter sampling',
              construction_sha256=hashlib.sha256(raw).hexdigest(),reconstructed=fresh,
              logs=logs,lambda_interval=lambda_interval,lambda_alternative=lambda_alternative,
              amplified_error_interval=[error_lower,error_upper],true_margin_lower=true_margin_lower,
              proof_checks=proofs,
              summary=dict(construction_checks=len(checks),compared_leaves=leaf_count,
                           additional_checks=len(proofs),failures=failures,passed=not failures,
                           cap=R,required_cap=U,margin=M,required_margin=25,parameter_samples=0))
OUTPUT.write_text(json.dumps(result,default=str,indent=2)+'\n')
print(f'Construction comparisons: {len(checks)}; compared leaves: {leaf_count}; additional checks: {len(proofs)}')
print(f'Failures: {len(failures)}; parameter samples: 0')
print(f'Cap {R}; required <{U}')
print(f'Row23 margin {M}; required >25>0')
print(f'Certificate: {OUTPUT.relative_to(ROOT)}')
if failures:
    print('Failure paths:',[f['path'] for f in failures])
    raise SystemExit(1)

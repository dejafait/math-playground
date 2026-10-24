"""L094 applicability check; imports L084's audited analytic enclosures.

Reconstruct only the table and independent O operands. This does not rerun
the analytic series proof, S/C/H packages, or prove the symbolic criterion.
Run from the collatz notebook directory with python3 and this relative path.
"""
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'uniform-independent-order-audit-certificate.json'
paths = [HERE / 'h-transfer-family-certificate.json',
         HERE / 'h-transfer-family-audit-certificate.json']
raw = [p.read_bytes() for p in paths]
construction, audited = [json.loads(x) for x in raw]
# Independently transcribe the complete canonical L055 pair table.
PAIRS = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
         (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
         (8224,39104),(15494,73672),(29191,138802),(54998,261511),
         (103621,492705),(195229,928293),(367827,1748976),
         (693015,3295208),(1305695,6208431),(2460032,11697176),
         (4634896,22038409),(8732512,41522114),(16452748,78230965),
         (30998279,32670621)]
ell, u = F(693147180559,10**12), F(1098612288669,10**12)
lam, B = F(10584,10**14), 9250245
cap = F(575,11)/lam + F(23,11)
checks = []


def check(name, actual, relation, required):
    passed = {'=': lambda: actual == required,
              '>': lambda: actual > required,
              '<': lambda: actual < required,
              '>=': lambda: actual >= required}[relation]()
    checks.append(dict(name=name, actual=actual, relation=relation,
                       required=required, passed=passed))


def encode(value):
    return json.loads(json.dumps(value, default=str))


logs = audited['logs']
# These endpoints are imported from the completed L084 analytic audit.
lo = 630138897*F(logs['2']['lower'])-397573379*F(logs['3']['upper'])
hi = 630138897*F(logs['2']['upper'])-397573379*F(logs['3']['lower'])
P27 = sum((F(27**j, factorial(j)) for j in range(41)), F(0))
check('positive lambda',lam,'>',0)
check('lambda below imported lower endpoint',lam,'<',lo)
check('positive ell',ell,'>',0)
check('ell below imported log2 lower',ell,'<',F(logs['2']['lower']))
check('u above imported log3 upper',u,'>',F(logs['3']['upper']))
check('v above imported log11over4 upper',F(2),'>',F(logs['11/4']['upper']))
check('u exceeds ell',u,'>',ell)
check('complete cap fraction',cap,'=',F(7187500000030429,14553))
check('cap threshold',cap,'<',500000000000)
check('degree40 exp27 lower threshold',P27,'>',500000000000)
check('imported exp27 sum match',P27,'=',F(audited['exp_lower']['27']))

records = []
for d in range(6,34):
    pairs = list(PAIRS)
    pairs[0], pairs[24] = (8,40-d),(30998279,32670621+d)
    rows = [[i,j,h] for i,(j,h) in enumerate(pairs)]
    A, D = [0], [0]
    for j,h in pairs:
        A.append(A[-1]+3*j+h)
        D.append(D[-1]+4*j+h+2)
    check(f'd{d} increasing J',all(pairs[i][0]<pairs[i+1][0] for i in range(24)),'=',True)
    check(f'd{d} J domain',min(j for j,h in pairs),'>=',2)
    check(f'd{d} H domain',min(h for j,h in pairs),'>=',3)
    check(f'd{d} sum J',sum(j for j,h in pairs),'=',66061058)
    check(f'd{d} sum H',sum(h for j,h in pairs),'=',199390205)
    check(f'd{d} K',A[-1],'=',397573379)
    check(f'd{d} N',D[-1]+18*B,'=',630138897)
    offsets, margins = [], []
    for i,(j,h) in enumerate(pairs):
        hf = min(h,72)
        off = F(81,44)-F(3,11)*F(3,2)**hf
        offsets.append(dict(i=i,H_floor=hf,offset_upper=off,exact_offset=h==hf))
        check(f'd{d} row{i} H floor',h,'>=',hf)
        check(f'd{d} row{i} negative offset upper',off,'<',0)
    for k in range(24):
        margin = (4*pairs[k+1][0]+D[k])*ell-A[k]*u-29
        margins.append(dict(k=k,row=k+1,A=A[k],D=D[k],margin=margin))
        check(f'd{d} k{k} positive margin',margin,'>',0)
        # Reconstruct the d=1 baseline directly from the canonical table.
        shift = int(k>0)
        a1 = sum(3*j+h for j,h in PAIRS[:k])-shift
        d1 = sum(4*j+h+2 for j,h in PAIRS[:k])-shift
        m1 = (4*pairs[k+1][0]+d1)*ell-a1*u-29
        check(f'd{d} k{k} A shift',A[k],'=',a1-(d-1)*shift)
        check(f'd{d} k{k} D shift',D[k],'=',d1-(d-1)*shift)
        check(f'd{d} k{k} margin shift',margin,'=',m1+(d-1)*shift*(u-ell))
    check(f'd{d} final A',A[23],'=',144318712-d)
    check(f'd{d} final D',D[23],'=',162928789-d)
    order = dict(lambda_lower=lam,T=27,ell=ell,u=u,v=2,cap=cap,
                 offsets=offsets,margins=margins)
    expected = dict(d=d,rows=rows,counts=dict(K=A[-1],N=D[-1]+18*B),
                    Lambda_interval=[lo,hi],O=order)
    for label,table in [('construction',construction['tables'][d-1]),
                        ('audited',audited['reconstructed_tables'][d-1])]:
        for key,value in expected.items():
            check(f'd{d} complete {label} {key}',table[key],'=',encode(value))
    check(f'd{d} exact minimum',min(x['margin'] for x in margins),
          '=',60*ell-29)
    records.append(expected)

minimum = min(x['margin'] for t in records for x in t['O']['margins'])
check('uniform exact minimum',minimum,'=',F(629441541677,50000000000))
check('uniform threshold',minimum,'>',F(1258,100))
failures = [c for c in checks if not c['passed']]
evidence = dict(scope='L094 independent O applicability; analytic endpoints imported',
    inputs=[dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(b).hexdigest())
            for p,b in zip(paths,raw)],
    imported_log_intervals={k:{s:logs[k][s] for s in ('lower','upper')}
                            for k in ('2','3','11/4')},
    exp27_degree40_sum=P27,tables=records,checks=checks,failures=failures,
    summary=dict(tables=28,offsets=700,margins=672,checks=len(checks),
                 failures=len(failures),minimum=minimum,required=F(1258,100)))
OUT.write_text(json.dumps(evidence,indent=2,default=str)+'\n')
print(f'28 tables; 700 offsets; 672 margins; {len(checks)} checks; {len(failures)} failures.')
print(f'Actual minimum {minimum}; required >1258/100. Cap {cap} <500000000000 <P27.')
print(f'Full certificate: {OUT.relative_to(ROOT)}')
if failures:
    print('Failed checks: '+', '.join(c['name'] for c in failures))
raise SystemExit(bool(failures))

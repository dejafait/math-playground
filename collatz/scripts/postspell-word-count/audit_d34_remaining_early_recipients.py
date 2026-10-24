#!/usr/bin/env python3
"""Independent L099 finite audit; never imports or executes its constructor.

Analytic intervals are audited imports. The quantified proof is reviewed in
L099; this program verifies its complete finite operands, not infinite tuples.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'scripts/postspell-word-count/d34-remaining-early-recipients-audit-certificate.json'
CONSTRUCTION = ROOT / 'scripts/postspell-word-count/d34-remaining-early-recipients-certificate.json'
SOURCE = ROOT / 'scripts/postspell-word-count/h-transfer-family-certificate.json'
TABLE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
LEMMA = ROOT / 'lemmas/L099-d34-literal-early-support-exclusion.md'

# Separate transcription from the canonical L055 table.
J = [8,15,28,52,98,184,347,653,1230,2317,4365,8224,15494,29191,
     54998,103621,195229,367827,693015,1305695,2460032,4634896,
     8732512,16452748,30998279]
H0 = [40,72,134,249,467,877,1650,3106,5849,11018,20756,39104,
      73672,138802,261511,492705,928293,1748976,3295208,6208431,
      11697176,22038409,41522114,78230965,32670621]
H = H0.copy()
H[0], H[24] = 6, 32670655
B = 9250245
kappa, U, T = F(23,11), F(20000000000), F(24)
ell, u, v = (F(x,10**12) for x in (693147180559,1098612288669,1011600911679))
lam = F(10584,10**14)
E = F(24*23,4*2**(4*J[1])-23)
residual = lam-E
R = kappa/residual+kappa
K = sum(3*j+h for j,h in zip(J,H))
N = sum(4*j+h for j,h in zip(J,H))+50+18*B
source = json.loads(SOURCE.read_text())
saved = json.loads(CONSTRUCTION.read_text())
d34 = source['tables'][33]
records = []

def plain(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,list): return [plain(y) for y in x]
    if isinstance(x,dict): return {k:plain(y) for k,y in x.items()}
    return x

def compare(name, actual, required, relation='='):
    ok = {'=': lambda: plain(actual)==plain(required),
          '>': lambda: actual>required, '<': lambda: actual<required}[relation]()
    rec = {'name':name,'actual':plain(actual),'relation':relation,
           'required':plain(required),'passed':ok}
    if isinstance(actual,(int,F)) and isinstance(required,(int,F)):
        rec['difference'] = str(actual-required)
    records.append(rec)

rows = [[i,J[i],H[i]] for i in range(25)]
original = [[i,J[i],H0[i]] for i in range(25)]
transcribed = [[int(x) for x in m] for m in
               re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', TABLE.read_text(), re.M)]
compare('canonical original table',original,transcribed)
compare('saved changed table',rows,saved['rows'])
compare('L084 changed table',rows,d34['rows'])
compare('d34 index',d34['d'],34)
compare('B',B,saved['B'])
compare('K',K,397573379)
compare('N with complete tail budget',N,630138897)
compare('all J increasing',all(J[i]<J[i+1] for i in range(24)),True)
compare('minimum H',min(H),6)
compare('positive residual',residual,F(0),'>')
compare('strict cap',R,U,'<')
constants = dict(kappa=kappa,U=U,T=T,ell=ell,u=u,v=v,R=R)
compare('construction constants',plain(constants),saved['constants'])
for name,value in dict(U=U,T=T,ell=ell,u=u,v=v,E=E,residual=residual,cap=R,lambda_lower=lam).items():
    compare('L084 S '+name,value,F(d34['S'][name]))
# Inspect full exact imported interval endpoints; do not recertify the series.
for key,value,side in [('2',ell,'lower'),('3',u,'upper'),('11/4',v,'upper')]:
    endpoint = F(source['logs'][key][side])
    compare('outward imported log '+key,value,endpoint,'<' if side=='lower' else '>')
compare('Lambda lower import',F(d34['Lambda_interval'][0]),lam,'>')
compare('Lambda upper import',F(d34['Lambda_interval'][1]),F(10585,10**14),'<')

# Prefixes are direct slice sums, rather than reading construction totals.
prefixes = [dict(i=i,A=sum(3*J[k]+H[k] for k in range(i)),
                 D=sum(4*J[k]+H[k]+2 for k in range(i))) for i in range(25)]
compare('all construction prefixes',prefixes,saved['prefixes'])
compare('all L084 prefixes',[dict(i=p['i'],A=p['A'],D_tail2=p['D']) for p in prefixes],d34['prefixes'])
for i in range(1,25):
    compare('A shift '+str(i),prefixes[i]['A']-sum(3*J[k]+H0[k] for k in range(i)),-34)
    compare('D shift '+str(i),prefixes[i]['D']-sum(4*J[k]+H0[k]+2 for k in range(i)),-34)

q = lambda h: F(12,11)*F(3,2)**h+1
uniform = dict(prefix_H_floor=6,prefix_tail2_upper=kappa-q(6)/4,
               recipient_H_floor=72,recipient_Q_lower=q(72),
               required_Q=kappa*2**20,failed_row0_Q=q(6))
compare('uniform operands',plain(uniform),saved['uniform_offsets'])
compare('H6 tail2 sign',uniform['prefix_tail2_upper'],F(0),'<')
compare('H72 tail20 sign',q(72),kappa*2**20,'>')
compare('preserved failed row0 support test',q(6),kappa*2**20,'<')
offsets = []
for i in range(23):
    h = min(H[i],72)
    o = dict(i=i,H_floor=h,Q_lower=q(h),tail2_upper=kappa-q(h)/4,
             tail20_upper=kappa-q(h)/2**20)
    offsets.append(o)
    compare('L084 O operand '+str(i),o['tail2_upper'],F(d34['O']['offsets'][i]['offset_upper']))
    compare('L084 S operand '+str(i),o['Q_lower'],F(d34['S']['offsets'][i]['Q_lower']))
    compare('L084 O row '+str(i),d34['O']['offsets'][i]['i'],i)
    compare('L084 S row '+str(i),d34['S']['offsets'][i]['i'],i)
    if i<=21: compare('prefix tail2 negative '+str(i),o['tail2_upper'],F(0),'<')
    if i>=1: compare('recipient tail20 negative '+str(i),o['tail20_upper'],F(0),'<')
compare('all construction offset operands',plain(offsets),saved['offsets'])

margins = []
for j in range(1,23):
    A,D = prefixes[j+1]['A'],prefixes[j+1]['D']
    coefficient = D+18+4*J[j+1]
    # Integer common denominator retains all amplified enclosure errors.
    scaled = coefficient*693147180559-24*10**12-1011600911679-A*1098612288669
    margin = F(scaled,10**12)
    m = dict(j=j,next_input=j+1,A=A,D=D,next_J=J[j+1],
             log2_coefficient=coefficient,margin=str(margin),scaled_margin=str(scaled))
    margins.append(m)
    compare('positive log3 coefficient '+str(j),A,0,'>')
    compare('positive log2 coefficient '+str(j),coefficient,0,'>')
    compare('strict margin '+str(j),margin,F(231,10),'>')
    compare('L084 complete S margin '+str(j),
            dict(j=j,input=j+1,A=A,D=D,margin=str(margin)),d34['S']['margins'][j])
compare('all construction margins',margins,saved['margins'])
display = [[int(x) for x in m] for m in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|$',LEMMA.read_text(),re.M)]
compare('all 22 written table rows',[[m['j'],m['A'],m['D'],int(m['scaled_margin'])] for m in margins],display)
minimum = min(margins,key=lambda m:F(m['margin']))
compare('minimum index',minimum['j'],4)
compare('minimum exact margin',F(minimum['margin']),F(11554173905673,500000000000))

# Independent factorial formula, not the construction term recurrence.
terms = [F(24**k,factorial(k)) for k in range(41)]
exp_sum = sum(terms,F(0))
compare('all exponential terms',plain(terms),saved['exponential_terms'])
compare('exponential sum',exp_sum,F(saved['exp24_lower']))
compare('written exponential sum',exp_sum,F(202750314819830504045671593478515759301,7661655986496068058455078125))
compare('U below finite exponential sum',U,exp_sum,'<')

# Stored check reports get an internal arithmetic consistency check only;
# the mathematical operands above were reconstructed independently.
stored_failures=[]
for c in saved['checks']:
    a,b=F(c['actual']),F(c['required'])
    verdict={'=':a==b,'>':a>b,'<':a<b,'>=':a>=b,'<=':a<=b}[c['relation']]
    if F(c['difference'])!=a-b or c['passed']!=verdict or not verdict:
        stored_failures.append(c['name'])
compare('stored check count',len(saved['checks']),443)
compare('stored check unique names',len({c['name'] for c in saved['checks']}),443)
compare('stored check arithmetic failures',stored_failures,[])
compare('saved summary',saved['summary'],dict(checks=443,recipients=22,minimum_j=4,
        minimum_margin=str(minimum['margin']),required_margin='231/10',failures=[],passed=True))
for item in saved['sources']:
    compare('source hash '+item['path'],hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest(),item['sha256'])
failures=[r['name'] for r in records if not r['passed']]
result=dict(scope='Independent finite audit of L099 only',
    provenance=dict(construction_sha256=hashlib.sha256(CONSTRUCTION.read_bytes()).hexdigest(),
                    constructor_imported_or_executed=False,analytic_intervals='audited L084 imports'),
    rows=rows,counts=dict(K=K,N=N,B=B),cap=dict(E=E,residual=residual,R=R,U=U),
    constants=constants,uniform_offsets=uniform,offsets=offsets,prefixes=prefixes,
    margins=margins,exp24_lower=exp_sum,exponential_terms=terms,checks=records,
    summary=dict(recipients=22,minimum_j=minimum['j'],minimum_margin=minimum['margin'],
                 required_margin='231/10',comparisons=len(records),failures=failures,passed=not failures),
    limitations='Finite comparisons do not prove quantified coverage; see L099 audit. No assembly or actual-word transfer. Stored-check operand provenance is not separately reconstructed by name.')
OUT.write_text(json.dumps(plain(result),indent=2)+'\n')
print('L099 audit:', 'PASS' if not failures else 'FAIL')
print('22 margins; minimum =',minimum['margin'],'at j =',minimum['j'],'; required > 231/10')
print('cap R =',R,'; required <',U)
print('tail2 upper =',uniform['prefix_tail2_upper'],'; required < 0')
print('recipient Q lower =',q(72),'; required >',kappa*2**20)
print('comparisons =',len(records),'; failures =',failures)
print('certificate:',OUT.relative_to(ROOT))
raise SystemExit(bool(failures))

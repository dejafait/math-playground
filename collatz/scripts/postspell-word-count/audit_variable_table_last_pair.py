#!/usr/bin/env python3
"""Independent L077 benchmark audit; general sufficiency is checked in L077.

No construction program is imported or run. Preserve every original artifact.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TABLE = [
    (8,40), (15,72), (28,134), (52,249), (98,467), (184,877),
    (347,1650), (653,3106), (1230,5849), (2317,11018), (4365,20756),
    (8224,39104), (15494,73672), (29191,138802), (54998,261511),
    (103621,492705), (195229,928293), (367827,1748976), (693015,3295208),
    (1305695,6208431), (2460032,11697176), (4634896,22038409),
    (8732512,41522114), (16452748,78230965), (30998279,32670621)]
PATH = HERE / 'variable-table-last-pair-certificate.json'
OLD_PATH = HERE / 'uniform-last-pair-certificate.json'
AUDITED_PATH = HERE / 'uniform-last-pair-audit-certificate.json'
original = json.loads(PATH.read_text())
old = json.loads(OLD_PATH.read_text())
audited = json.loads(AUDITED_PATH.read_text())
checks = []

def equal(name, actual, expected):
    checks.append(dict(name=name, actual=actual, expected=expected,
                       passed=actual == expected))

def compare(name, actual, relation, required):
    actual, required = F(actual), F(required)
    ok = {'<': actual < required, '<=': actual <= required,
          '=': actual == required, '>': actual > required,
          '>=': actual >= required}[relation]
    result = dict(name=name, actual=str(actual), relation=relation,
                  required=str(required), actual_minus_required=str(actual-required),
                  passed=ok)
    checks.append(result)
    return result

canonical = [tuple(map(int, match)) for match in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$',
    (ROOT/'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text(), re.M)]
equal('complete independently transcribed table', canonical,
      [(i,j,h) for i,(j,h) in enumerate(TABLE)])
budget, tau, q = 9250245, 2, 24
kappa = F(23,11)
lo, hi = F(10584,10**14), F(10585,10**14)
eta = kappa - F(16,27)**8 * (F(12,11)+F(2,3)**40)
domain = 2/hi-2
L = [1] + [10**8 * 2**i for i in range(24)]
recip = sum((F(1,v) for v in L), F(0))
Q = kappa * (1+F(1,50000000))
required = Q/lo+Q+kappa/L[-1]
U = Q/lo+Q+kappa
terms = [F(24**i, factorial(i)) for i in range(41)]
rows = [dict(i=i,J=j,H=h,a=(38 if i==23 else 166504376 if i==24 else 2))
        for i,(j,h) in enumerate(TABLE)]
K = sum(3*j+h for j,h in TABLE)
N = sum(4*j+h for j,h in TABLE) + 50 + 18*budget
prefixes = [(sum(3*j+h for j,h in TABLE[:i]),
             sum(4*row['J']+row['H']+row['a'] for row in rows[:i]))
            for i in range(26)]
k,d = prefixes[q]
S = 10**12
ell, u, v = F(693147180559,S), F(1098612288669,S), F(1011600911679,S)
margin = 24+k*u-(d+4*TABLE[-1][0])*ell+v

# Independently recompute every construction comparison and full operand record.
specs = [
    (lo,'>',0), (lo,'<',hi), (hi,'<',1), (eta,'>',2),
    (F(19683,8192),'>',2), (F(3**64,2**74),'>',10**8),
    (F(3**117,2**170),'>',2), (domain,'>=',47),
    (domain,'>',18000000000), (kappa*recip,'<=',Q),
    (required,'<=',U), (U,'=',F(435606069410390910013,22050000000)),
    (U,'<',20000000000), (sum(terms),'>',20000000000),
    (margin,'<',0), (margin,'=',F(-474883782659,125000000000)),
    (margin,'<',F(-379,100))]
equal('original rational comparison count', len(original['checks']), len(specs))
for saved,(a,relation,b) in zip(original['checks'],specs):
    rebuilt = compare(saved['name'],a,relation,b)
    equal('complete original record: '+saved['name'], rebuilt, saved)
integers = dict(
    literal_increasing_J=all(TABLE[i][0]<TABLE[i+1][0] for i in range(24)),
    eta_monotonicity_hypotheses=all(j>=8 and h>=40 for j,h in TABLE),
    boundary_row0_exact_pair=TABLE[0]==(8,40),
    boundary_other_prefix_baseline=all(j>=15 and h>=72 for j,h in TABLE[1:24])
        and all(row['a']<=38 for row in rows[1:24]),
    all_early_tails_two=all(row['a']==2 for row in rows[:23]),
    boundary_changed_tails=(rows[23]['a'],rows[24]['a'])==(38,166504376),
    full_exponents=(K,N)==(397573379,630138897),
    incoming_exponents=(k,d)==(271907921,306970784),
    full_tail_sum=sum(row['a'] for row in rows)==50+18*budget,
    last_parameter_final_tail_two=166504412-18*budget==2,
    cutoff_admitted=0<=tau<=budget)
equal('all 11 original integer comparisons', integers, original['integer_checks'])
equal('all independently recomputed integer comparisons pass', all(integers.values()), True)
equal('complete boundary', original['boundary'], dict(rows=rows,incoming_k=k,
      incoming_d=d,J_last=TABLE[-1][0],negative_log2_coefficient=d+4*TABLE[-1][0],
      margin_upper=str(margin)))
for i,value in enumerate(L):
    equal(f'incoming prefix bound {i}',original['prefixes'][i],
          dict(i=i,incoming_lower=str(value),reciprocal=str(F(1,value))))
equal('prefix bound count',len(original['prefixes']),25)
for name,value in [('eta0',eta),('domain_lower',domain),('reciprocal_sum',recip),
                   ('normalized_required',required),('exp24_partial_sum',sum(terms))]:
    equal(name,original[name],str(value))
equal('all 41 exponential terms',original['exp24_terms'],list(map(str,terms)))
equal('old benchmark exponential terms',audited['exponential_terms'],list(map(str,terms)))
equal('audited boundary rows',rows,audited['t2']['rows'])
equal('audited closure counts',dict(three=K,two=N),audited['t2']['closing_exponents'])
equal('audited complete margin',str(margin),audited['t2']['margin_upper'])
equal('original failed probe preserved',original['preserved_optional_probes'],old['diagnostic_probes'])
equal('failed probe actual',original['preserved_optional_probes'][0]['actual'],str(margin))
equal('failed probe threshold',original['preserved_optional_probes'][0]['requested'],'-4')
equal('failed probe verdict',original['preserved_optional_probes'][0]['passed'],margin < -4)
equal('unchanged old certificate hash',hashlib.sha256(OLD_PATH.read_bytes()).hexdigest(),
      original['preserved_original_certificate_sha256'])

# Existing integrated-geometric-remainder method, with 128 unrounded terms.
# Positive arguments below are <=3, hence 0<x<=1/2. No floating point.
logs = {}
def log_interval(name,z):
    z = F(z)
    x = (z-1)/(z+1)
    assert 0 < x <= F(1,2)
    ts = [2*x**(2*i+1)/(2*i+1) for i in range(128)]
    lower = sum(ts)
    error = 2*x**257/(257*(1-x*x))
    logs[name] = dict(argument=str(z),x=str(x),terms=list(map(str,ts)),
                      lower=str(lower),remainder=str(error),upper=str(lower+error))
    return lower,lower+error
a,b = log_interval('log2',2)
c,e = log_interval('log3',3)
f,g = log_interval('log11over4',F(11,4))
z,w = log_interval('reduced_log18billion',F(18000000000,2**34))
for name,actual,relation,required_value in [
    ('lower log2 grid',a,'>',ell),('upper log2 grid',b,'<',F(693147180560,S)),
    ('lower log3 grid',c,'>',F(1098612288668,S)),('upper log3 grid',e,'<',u),
    ('lower guard log grid',f,'>',F(1011600911678,S)),('upper guard log grid',g,'<',v),
    ('Lambda lower with cancellation',N*a-K*e,'>',lo),
    ('Lambda upper with cancellation',N*b-K*c,'<',hi),
    ('log18billion lower',z+34*a,'>',F(2361,100)),
    ('independent boundary bound improves F',24+k*e-(d+4*TABLE[-1][0])*a+g,'<',margin)]:
    compare(name,actual,relation,required_value)

# Recover all imported survivor operands with their actual outgoing tails.
survivors = []
for t in (0,1):
    tails = [2]*23+[2+18*t,2+18*(budget-t)]
    for i,(j,h) in enumerate(TABLE):
        pk = sum(3*x+y for x,y in TABLE[:i])
        pd = sum(4*x+y+tails[m] for m,(x,y) in enumerate(TABLE[:i]))
        lower = F(2361,100)+pk*F(1098612288668,S)-(pd+4*j)*F(693147180560,S)+F(1011600911678,S)
        independent = F(2361,100)+pk*c-(pd+4*j)*b+f
        saved = audited['survivor_checks'][25*t+i]
        equal(f'survivor {t}/{i} exact imported operands',
              (saved['t'],saved['i'],saved['three'],saved['two'],saved['lower']),
              (t,i,pk,pd,str(lower)))
        compare(f'survivor {t}/{i} strictly passes',lower,'>',0)
        compare(f'survivor {t}/{i} independent bound',independent,'>',lower)
        survivors.append(dict(t=t,i=i,three=pk,two=pd,lower=str(lower),
                              independent_lower=str(independent)))
equal('all imported survivor records',len(audited['survivor_checks']),50)
equal('last-pair rejection coverage',
      (original['symbolic_coverage']['first_rejected'],original['symbolic_coverage']['last_rejected'],
       original['symbolic_coverage']['number_rejected']),(2,budget,budget-1))
equal('small budgets',[(v['B'],v['cutoff'],v['rejected_interval_empty'],v['boundary_tests_required'])
      for v in original['small_budgets']],[(0,2,True,False),(1,2,True,False)])

failures = [v['name'] for v in checks if not v['passed']]
summary = dict(verdict='NO_DEFECT' if not failures else 'FAILURE',checks=len(checks),
               failures=failures,original_rational_checks=17,original_integer_checks=11,
               prefix_bounds=25,boundary_rows=25,exp_terms=41,survivor_margins=50,
               domain_lower=str(domain),required_domain=47,normalized_upper=str(U),
               required_normalized_upper=20000000000,boundary_margin_upper=str(margin),
               required_margin_upper='-379/100',optional_margin_below_minus4=margin < -4,
               survivor_minima={str(t):str(min(F(v['lower']) for v in survivors if v['t']==t)) for t in (0,1)},
               coverage='Integers 2..9250245 rejected by symbolic monotonicity, including final tail 2')
result = dict(summary=summary,checks=checks,independent_logs=logs,survivors=survivors,
              incoming_exponents=[dict(i=i,three=k,two=d) for i,(k,d) in enumerate(prefixes)],
              exponential_terms=list(map(str,terms)),
              original_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in (PATH,OLD_PATH,AUDITED_PATH)},
              qualification='Finite benchmark verification supplements the quantified proof audit in L077; no new table or integrality claim')
out = HERE/'variable-table-last-pair-audit-certificate.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(f'Checks: {len(checks)}; failures: {failures}')
print(f'Uniform n > {domain}; required >=47')
print(f'Normalized upper {U} < 20000000000')
print(f'Boundary margin < {margin}; required <-3.79; optional <-4 remains false')
print(f'Certificate: {out}')
assert not failures

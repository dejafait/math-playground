#!/usr/bin/env python3
"""Independent finite-data audit of L101; imports no construction program.

Reuses the inspected d34 independent-audit framework with freshly matched
d35 operands; neither imports nor executes either constructor.
Reconstructs every certificate field and comparison from a separate table
transcription. A second logarithm evaluation uses multiplicative argument
decomposition and 128 terms. L077 supplies the quantified implication.
"""
from fractions import Fraction as R
from pathlib import Path
import hashlib
import json
import operator
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ORIGINAL = HERE / 'd35-independent-cutoff-certificate.json'
OUTPUT = HERE / 'd35-independent-cutoff-audit-certificate.json'
TABLE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
raw = TABLE.read_bytes()
original_raw = ORIGINAL.read_bytes()
original = json.loads(original_raw)
pairs = [
    (8,40), (15,72), (28,134), (52,249), (98,467), (184,877),
    (347,1650), (653,3106), (1230,5849), (2317,11018),
    (4365,20756), (8224,39104), (15494,73672), (29191,138802),
    (54998,261511), (103621,492705), (195229,928293),
    (367827,1748976), (693015,3295208), (1305695,6208431),
    (2460032,11697176), (4634896,22038409), (8732512,41522114),
    (16452748,78230965), (30998279,32670621),
]
base = [[i,j,h] for i,(j,h) in enumerate(pairs)]
canonical = [list(map(int, m)) for m in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
rows = [[i,j,h + (-35 if i == 0 else 35 if i == 24 else 0)]
        for i,j,h in base]
B, tau = 9250245, 2
kap, lm, lp = R(23,11), R(10584,10**14), R(10585,10**14)
ell, u, v = map(lambda n: R(n,10**12),
                [693147180559,1098612288669,1011600911679])
U, T = R(21000000000), R(24)
relations = {'=': operator.eq, '<': operator.lt, '>': operator.gt,
             '<=': operator.le, '>=': operator.ge}
expected_checks, audit_checks, mismatches = {}, [], []


def comparison(name, a, relation, b):
    a, b = R(a), R(b)
    return dict(name=name, actual=a, relation=relation, required=b,
                difference=a-b, passed=relations[relation](a,b))


def saved(name, a, relation, b):
    assert name not in expected_checks
    expected_checks[name] = comparison(name,a,relation,b)


def audit(name, a, relation, b):
    audit_checks.append(comparison(name,a,relation,b))


def grid(interval, scale=10**12):
    a,b = interval
    return [R((a*scale).__floor__(),scale), R((b*scale).__ceil__(),scale)]


def series(x, count):
    """Successive powers, rather than the constructor's direct powers."""
    x = R(x)
    z = (x-1)/(x+1)
    assert 0 < z < 1
    power, terms = z, []
    for odd in range(1,2*count,2):
        terms.append(2*power/odd)
        power *= z*z
    lower = sum(terms,R(0))
    remainder = 2*power/((2*count+1)*(1-z*z))
    return dict(argument=x,z=z,terms=terms,lower=lower,
                remainder_upper=remainder,upper=lower+remainder)


logs = {str(x): series(x,100) for x in [R(2),R(3),R(11,4)]}
for key,data in logs.items():
    saved(f'log{key} positive series argument',data['z'],'>',0)
    saved(f'log{key} series domain',data['z'],'<',1)
l2,h2 = logs['2']['lower'],logs['2']['upper']
l3,h3 = logs['3']['lower'],logs['3']['upper']
lv,hv = logs['11/4']['lower'],logs['11/4']['upper']
tails = [2+18*(tau if i==23 else B-tau if i==24 else 0)
         for i in range(25)]
word_counts = [(3*j+h, 4*j+h+a) for (_,j,h),a in zip(rows,tails)]
prefixes = [(sum(a for a,b in word_counts[:i]),
             sum(b for a,b in word_counts[:i])) for i in range(26)]
K,N = prefixes[-1]
lam = [N*l2-K*h3,N*h2-K*l3]
eta0 = kap-R(12*16**8,11*27**8)-R(16**8*2**5,27**8*3**5)
domain = R(2)*(1/lp-1)
for name,a,rel,b in [
    ('K',K,'=',397573379), ('N',N,'=',630138897),
    ('r domain',len(rows),'>=',3), ('budget domain',B,'>=',0),
    ('cutoff domain',tau,'>=',0), ('cutoff within budget',tau,'<=',B),
    ('lambda minus positive',lm,'>',0), ('Lambda lower',lam[0],'>',lm),
    ('Lambda upper',lam[1],'<',lp), ('lambda plus below one',lp,'<',1),
    ('ell positive',ell,'>',0), ('ell lower',ell,'<',l2),
    ('u upper',u,'>',h3), ('v upper',v,'>',hv),
    ('positive e',2,'>',0), ('eta0 exceeds e',eta0,'>',2),
    ('eta24 J monotonicity premise',rows[24][1],'>=',rows[0][1]),
    ('eta24 H monotonicity premise',rows[24][2],'>=',rows[0][2]),
    ('unshifted domain',domain,'>',47),
]:
    saved(name,a,rel,b)
for i,j,h in rows:
    saved(f'row{i} J',j,'>=',2)
    saved(f'row{i} H',h,'>=',3)
    if i:
        saved(f'row{i} increasing J',j,'>',rows[i-1][1])
saved('row23 tail',tails[23],'=',38)
saved('closing row24 tail',tails[24],'=',166504376)
saved('total tails',sum(tails),'=',166504460)
w = R(10**8*2**34,3**34)
c0 = R(3**word_counts[0][0],2**word_counts[0][1])
lower_bounds = [R(1),w]
while len(lower_bounds)<25:
    lower_bounds.append(2*lower_bounds[-1])
saved('row0 exact multiplier exceeds w',c0,'>',w)
saved('w positive',w,'>',0)
factors = []
for i,a in enumerate(tails):
    saved(f'row{i} tail domain',a,'>=',2)
    saved(f'row{i} tail congruence',a%18,'=',2)
    if 1<=i<=23:
        aa,den = word_counts[i]
        dd = den+1
        interval = [aa*l3-dd*h2, aa*h3-dd*l2]
        saved(f'row{i} log(c/2) lower',interval[0],'>',0)
        factors.append(dict(i=i,numerator_exponent=aa,
            denominator_exponent_plus_one=dd,interval=interval,
            certified_grid_interval=grid(interval),
            amplified_series_errors=[aa*(h3-l3),dd*(h2-l2)]))
saved('closing exponent K',prefixes[25][0],'=',K)
saved('closing exponent N',prefixes[25][1],'=',N)
incoming = []
for i,L in enumerate(lower_bounds):
    saved(f'incoming{i} L positive',L,'>',0)
    if i:
        saved(f'incoming{i} induction',lower_bounds[i-1]*(w if i==1 else 2),'=',L)
    incoming.append(dict(i=i,A=prefixes[i][0],D=prefixes[i][1],L=L,reciprocal=1/L))
reciprocal_sum = sum([R(1)]+[R(3**34,10**8*2**(34+i)) for i in range(24)])
saved('complete reciprocal identity',reciprocal_sum,'=',1+(2-R(1,2**23))/w)
Q = kap*reciprocal_sum
shift = kap/lower_bounds[-1]
RC = Q*(1/lm+1)+shift
saved('Q positive',Q,'>',0)
saved('C cap lower integer enclosure',RC,'>',20138923465)
saved('C cap upper integer enclosure',RC,'<',20138923466)
saved('one replacement U bounds C cap',RC,'<=',U)
exp_terms = [R(1)]
for n in range(1,41):
    exp_terms.append(exp_terms[-1]*T/n)
exp_lower = sum(exp_terms)
saved('T positive',T,'>',0)
saved('one replacement U below exp lower',U,'<',exp_lower)
P,d = prefixes[24]
negative = d+4*rows[24][1]
margin = T+P*u-negative*ell+v
exact_interval = [T+P*l3-negative*h2+lv,T+P*h3-negative*l2+hv]
error = [margin-exact_interval[1],margin-exact_interval[0]]
for name,a,rel,b in [
    ('incoming row24 k',P,'=',271907886),
    ('incoming row24 d',d,'=',306970749),
    ('complete negative log2 coefficient',negative,'=',430963865),
    ('positive log3 coefficient',P,'>',0),
    ('positive negative-log2 coefficient',negative,'>',0),
    ('full error positive',error[0],'>',0),
    ('full error ordered',error[1],'>',error[0]),
    ('full amplified error below 1/1000',error[1],'<',R(1,1000)),
    ('row24 upper margin strictly negative',margin,'<',0),
]:
    saved(name,a,rel,b)
summary = dict(checks=len(expected_checks),failures=0,RC=RC,required_U=U,
    U_minus_RC=U-RC,exp_lower_floor=exp_lower.__floor__(),
    exp_lower_minus_U_floor=(exp_lower-U).__floor__(),
    row24_upper_margin=margin,required_margin='strictly below 0',
    row24_analytic_grid_interval=grid(exact_interval),
    complete_amplified_error_grid_interval=grid(error),
    lambda_grid_interval=grid(lam,10**20),rejected_interval=[tau,B])
rebuilt = dict(scope=dict(d=35,literal=True,B=B,tau=tau,candidate_count=1,
    no_early_support_or_order_reduction=True),
    source=dict(path=str(TABLE.relative_to(ROOT)),sha256=hashlib.sha256(raw).hexdigest()),
    table=rows,tails=tails,constants=dict(kappa=kap,lm=lm,lp=lp,e=2,U=U,T=T,
        ell=ell,u=u,v=v,eta0=eta0,domain=domain),
    analytic=dict(logs=logs,lambda_interval=lam,
        lambda_amplified_errors=[N*(h2-l2),K*(h3-l3)],
        exp24_terms=exp_terms,exp24_lower=exp_lower),
    incoming=incoming,factors=factors,
    complete_factor_enclosures=[dict(i=f['i'],A=f['numerator_exponent'],
        D_plus_one=f['denominator_exponent_plus_one'],
        log_c_over_2=f['certified_grid_interval']) for f in factors],
    cap=dict(w=w,c0=c0,reciprocal_sum=reciprocal_sum,Q=Q,last_shift_term=shift,RC=RC),
    row24=dict(J=rows[24][1],H=rows[24][2],k=P,d=d,R=negative,
        upper_margin=margin,analytic_interval=exact_interval,
        complete_amplified_error_interval=error),summary=summary,
    failures=[c for c in expected_checks.values() if not c['passed']])

# Match the complete name set before using saved order for presentation only.
names = [c['name'] for c in original['checks']]
if len(names)!=len(set(names)) or set(names)!=set(expected_checks):
    mismatches.append(dict(path='/checks/names',actual=names,expected=sorted(expected_checks)))
rebuilt['checks'] = [expected_checks[n] for n in names if n in expected_checks]
leaf_count = 0


def compare(actual, expected, path=''):
    global leaf_count
    if isinstance(expected,dict):
        if not isinstance(actual,dict) or set(actual)!=set(expected):
            mismatches.append(dict(path=path+'/keys',actual=list(actual),expected=list(expected)))
        if isinstance(actual,dict):
            for k in set(actual)&set(expected):
                compare(actual[k],expected[k],path+'/'+k)
    elif isinstance(expected,list):
        if not isinstance(actual,list) or len(actual)!=len(expected):
            mismatches.append(dict(path=path+'/length',actual=len(actual),expected=len(expected)))
        if isinstance(actual,list):
            for i,(a,b) in enumerate(zip(actual,expected)):
                compare(a,b,path+'/'+str(i))
    else:
        leaf_count += 1
        good = (actual==str(expected)) if isinstance(expected,R) else (
            type(actual) is type(expected) and actual==expected)
        if not good:
            mismatches.append(dict(path=path,actual=actual,expected=expected))


compare(original,rebuilt)
if canonical!=base:
    mismatches.append(dict(path='/separate_table_transcription',actual=canonical,expected=base))

# Second evaluation: log3=log2+log(3/2), log(11/4)=log2+log(11/8).
alternate = {str(x):series(x,128) for x in [R(2),R(3,2),R(11,8)]}


def linear_interval(constant, coeffs):
    low=high=R(constant)
    for key,coefficient in coeffs.items():
        a,b = alternate[key]['lower'],alternate[key]['upper']
        low += coefficient*(a if coefficient>=0 else b)
        high += coefficient*(b if coefficient>=0 else a)
    return [low,high]


lam_alt=linear_interval(0,{'2':N-K,'3/2':-K})
margin_alt=linear_interval(T,{'2':P-negative+1,'3/2':P,'11/8':1})
factor_alt=[]
for f in factors:
    aa,dd=f['numerator_exponent'],f['denominator_exponent_plus_one']
    bounds=linear_interval(0,{'2':aa-dd,'3/2':aa})
    audit(f'alternate factor {f["i"]} positive',bounds[0],'>',0)
    audit(f'alternate factor {f["i"]} inside original lower',bounds[0],'>',f['interval'][0])
    audit(f'alternate factor {f["i"]} inside original upper',bounds[1],'<',f['interval'][1])
    factor_alt.append(dict(i=f['i'],interval=bounds))
audit('alternate Lambda above lambda minus',lam_alt[0],'>',lm)
audit('alternate Lambda below lambda plus',lam_alt[1],'<',lp)
audit('alternate Lambda inside original lower',lam_alt[0],'>',lam[0])
audit('alternate Lambda inside original upper',lam_alt[1],'<',lam[1])
audit('alternate E inside original lower',margin_alt[0],'>',exact_interval[0])
audit('alternate E inside original upper',margin_alt[1],'<',exact_interval[1])
audit('alternate E below rational F',margin_alt[1],'<',margin)
audit('alternate full error lower',margin-margin_alt[1],'>',R(649476131,10**12))
audit('alternate full error upper',margin-margin_alt[0],'<',R(649476132,10**12))
for name,a,rel,b in [
    ('written eta0',eta0,'=',R(142223884206271,68630377364883)),
    ('written w',w,'=',R(1717986918400000000,16677181699666569)),
    ('written Q',Q,'=',R(67580051164552809819556541,31705341376688291840000000)),
    ('written C cap',RC,'=',R(187489044665819986358454838929133547,9309784854704947200000000)),
    ('written margin',margin,'=',R(-8995174522561,500000000000)),
    ('written margin below -17.99',margin,'<',R(-1799,100)),
    ('written domain',domain,'=',R(39999999995766,2117)),
    ('old cap still fails',RC,'>',20000000000),
    ('common factor bound',R(3**117,2**170),'>',2),
    ('empty prefix',lower_bounds[0],'=',1),
    ('complete incoming array length',len(incoming),'=',25),
    ('complete factor array length',len(factors),'=',23),
    ('exponential positive sum lower integer',exp_lower,'>',26462988572),
    ('full error written lower',error[0],'>',R(649476131,10**12)),
    ('full error written upper',error[1],'<',R(649476132,10**12)),
    ('last rejection endpoint tail',2+18*(B-B),'=',2),
    ('first rejection endpoint row23 tail',2+18*tau,'=',38),
    ('total H conserved',sum(h for _,j,h in rows),'=',sum(h for j,h in pairs)),
]:
    audit(name,a,rel,b)
for i in range(1,24):
    audit(f'common factor row{i} J',rows[i][1],'>=',15)
    audit(f'common factor row{i} H',rows[i][2],'>=',72)
    audit(f'common factor row{i} tail',tails[i],'<=',38)
for i,term in enumerate(exp_terms):
    audit(f'exp term {i} positive',term,'>',0)
failed = [c for c in list(expected_checks.values())+audit_checks if not c['passed']]
report = dict(scope='Independent L101 finite certificate and applicability audit; no wider target',
    source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in [TABLE,ORIGINAL,HERE/'certify_d35_independent_cutoff.py']},
    separate_base_table=base,rebuilt_certificate=rebuilt,
    alternate=dict(logs=alternate,lambda_interval=lam_alt,
        row24_E_interval=margin_alt,full_error_interval=[margin-margin_alt[1],margin-margin_alt[0]],
        factors=factor_alt),audit_checks=audit_checks,mismatches=mismatches,failures=failed,
    summary=dict(recursive_leaf_comparisons=leaf_count,
        original_comparisons=len(expected_checks),additional_checks=len(audit_checks),
        mismatches=len(mismatches),failures=len(failed),
        RC_integer_interval=[20138923465,20138923466],required_U=U,
        exponential_lower_floor=exp_lower.__floor__(),row24_upper_margin=margin,
        required_margin='strictly below zero',complete_error_interval=grid(error),
        rejected_interval=[tau,B],closing_tail_at_B=2,
        no_feasibility_or_wider_exclusion=True))
OUTPUT.write_text(json.dumps(report,default=str,indent=2)+'\n')
print(f'Original comparisons: {len(expected_checks)}; recursive leaves: {leaf_count}; additional checks: {len(audit_checks)}')
print(f'Mismatches: {len(mismatches)}; failures: {len(failed)}')
print(f'20138923465 < C cap < 20138923466 < required U={U}; exp24 lower sum > {exp_lower.__floor__()}')
print(f'Row24 upper J margin: {margin}; required < 0; full error: {grid(error)}')
print(f'Closed rejection interval: [{tau}, {B}], last closing tail=2 (L077 implication)')
print(f'Failure names: {[c["name"] for c in failed]}')
print(f'Mismatch paths: {[c["path"] for c in mismatches]}')
print(f'Certificate: {OUTPUT.relative_to(ROOT)}')
assert not mismatches and not failed

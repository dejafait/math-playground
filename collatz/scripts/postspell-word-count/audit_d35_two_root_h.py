#!/usr/bin/env python3
"""Independent fixed-scope L100 audit; never imports/runs its constructor."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INPUT = HERE / 'd35-two-root-h-certificate.json'
OUTPUT = HERE / 'd35-two-root-h-audit-certificate.json'
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
raw = SOURCE.read_bytes()
original = json.loads(INPUT.read_text())
checks, failures = [], []


def serial(x):
    return json.loads(json.dumps(x, default=str))


def test(name, actual, relation, required):
    ok = {'=': lambda: actual == required, '<': lambda: actual < required,
          '>': lambda: actual > required, '<=': lambda: actual <= required}[relation]()
    record = dict(name=name, actual=serial(actual), relation=relation,
                  required=serial(required), passed=ok)
    if isinstance(actual, (int, Q)) and isinstance(required, (int, Q)):
        record['difference'] = str(actual-required)
    checks.append(record)
    if not ok:
        failures.append(record)


def match(path, actual, expected):
    """Compare complete trees, not previews or floating point renderings."""
    if isinstance(expected, dict):
        test(path+' keys', sorted(actual), '=', sorted(expected))
        for k, v in expected.items():
            match(path+'/'+k, actual[k], v)
    elif isinstance(expected, list):
        test(path+' length', len(actual), '=', len(expected))
        for i, v in enumerate(expected):
            match(path+'/'+str(i), actual[i], v)
    else:
        test(path, actual, '=', expected)


def log_series(x, count):
    z = (x-1)/(x+1)
    test(f'log {x} positive z ({count})', z, '>', 0)
    test(f'log {x} z below one ({count})', z, '<', 1)
    power, terms = z, []
    for k in range(count):
        terms.append(2*power/(2*k+1))
        power *= z*z
    lo = sum(terms, Q())
    remainder = 2*power/((2*count+1)*(1-z*z))
    return dict(argument=x, z=z, terms=terms, lower=lo,
                remainder_upper=remainder, upper=lo+remainder)


# Separate transcription of the canonical table, then literal d35 change.
J = [8,15,28,52,98,184,347,653,1230,2317,4365,8224,15494,29191,
     54998,103621,195229,367827,693015,1305695,2460032,4634896,
     8732512,16452748,30998279]
H0 = [40,72,134,249,467,877,1650,3106,5849,11018,20756,39104,
      73672,138802,261511,492705,928293,1748976,3295208,6208431,
      11697176,22038409,41522114,78230965,32670621]
base = [[i, J[i], H0[i]] for i in range(25)]
read_rows = [list(map(int, m)) for m in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
test('independent transcription versus complete L055 table', read_rows, '=', base)
H = H0.copy()
H[0], H[24] = 5, 32670656
table = [[i, J[i], H[i]] for i in range(25)]
B = 9250245
kappa, lm, lp = Q(23,11), Q(10584,10**14), Q(10585,10**14)
ell, u = Q(693147180559,10**12), Q(1098612288669,10**12)
U, T = Q(21000000000), Q(24)
# Full allocations independently specified, with both closing tails.
tail_lists = [[2]*24+[166504412], [2]*23+[20,166504394]]
K = 3*sum(J)+sum(H)
N = K+sum(J)+sum(tail_lists[0])
logs = {str(x): log_series(Q(x),100) for x in (2,3)}
l2,h2 = logs['2']['lower'],logs['2']['upper']
l3,h3 = logs['3']['lower'],logs['3']['upper']
lambda_interval = [N*l2-K*h3, N*h2-K*l3]
test('K exact', K, '=', 397573379)
test('N exact', N, '=', 630138897)
test('positive Lambda lower bound', lm, '>', 0)
test('full Lambda lower enclosure', lambda_interval[0], '>', lm)
test('full Lambda upper enclosure', lambda_interval[1], '<', lp)
test('lambda upper below one', lp, '<', 1)
test('ell positive', ell, '>', 0)
test('ell below log2', ell, '<', l2)
test('u above log3', u, '>', h3)
eta0 = kappa-Q(16,27)**8*(Q(12,11)+Q(2,3)**5)
domain = 2*(1-lp)/lp
test('eta0 exact printed value', eta0, '=', Q(142223884206271,68630377364883))
test('eta0 exceeds e', eta0, '>', 2)
test('eta0 below kappa', eta0, '<', kappa)
test('domain exceeds 47', domain, '>', 47)
for i in range(25):
    test(f'row{i} J eta monotonicity', J[i], '>', 7)
    test(f'row{i} H eta monotonicity', H[i], '>', 4)
    if i:
        test(f'row{i} strictly increasing J', J[i], '>', J[i-1])
test('unchanged tail2 domain growth comparison', Q(19683,8192), '>', 2)

w = Q(100000000)*Q(2,3)**34
c0 = Q(3**29,2**39)
test('row0 actual factor exceeds w', c0, '>', w)
test('w exceeds one', w, '>', 1)
test('independent common tail38 factor exceeds two', Q(3**117,2**170), '>', 2)
L = [Q(1), w]
while len(L) < 25:
    L.append(2*L[-1])
reciprocals = [Q(1)/x for x in L]
total = sum(reciprocals,Q())
test('finite reciprocal sum versus closed form', total, '=', 1+2/w*(1-Q(1,2**24)))
q = kappa*total
smallest = min(L)
test('actual minimum incoming lower factor', smallest, '=', Q(1))
cap = q/lm+q+kappa/smallest
test('cap exact printed value', cap, '=', Q(844750639734024151594364496473033303743,
                                            41946166641358610104320000000))
test('cap integer lower', cap, '>', 20138923467)
test('cap integer upper', cap, '<', 20138923468)
test('replacement cap passes', cap, '<', U)
test('old cap still fails', cap, '>', 20000000000)
exp_terms = [Q(1)]
for k in range(1,41):
    exp_terms.append(exp_terms[-1]*24/k)
exp_lower = sum(exp_terms,Q())
test('exponential argument positive', T, '>', 0)
test('replacement U below positive exponential lower sum', U, '<', exp_lower)
test('exponential sum exact printed value', exp_lower, '=',
     Q(202750314819830504045671593478515759301,7661655986496068058455078125))
for i, term in enumerate(exp_terms):
    test(f'exponential term{i} positive', term, '>', 0)

# Second analytic calculation: log3=log2+log(3/2), independently
# using 120 terms, to check all highly cancelled linear forms.
alt2, alt32 = log_series(Q(2),120),log_series(Q(3,2),120)
a,b,c,d = alt2['lower'],alt2['upper'],alt32['lower'],alt32['upper']
alt_lambda = [(N-K)*a-K*d,(N-K)*b-K*c]
test('alternate Lambda lower', alt_lambda[0], '>', lm)
test('alternate Lambda upper', alt_lambda[1], '<', lp)
test('alternate Lambda inside first lower', alt_lambda[0], '>', lambda_interval[0])
test('alternate Lambda inside first upper', alt_lambda[1], '<', lambda_interval[1])
allocations, alternative_margins = [], []
for t, tails in enumerate(tail_lists):
    test(f't{t} full tail formula', tails, '=', [2]*23+[2+18*t,2+18*(B-t)])
    test(f't{t} tail total', sum(tails), '=', 166504460)
    prefix_A, prefix_D = [0], [0]
    factors = []
    for i in range(25):
        odd, length = 3*J[i]+H[i],4*J[i]+H[i]+tails[i]
        prefix_A.append(prefix_A[-1]+odd)
        prefix_D.append(prefix_D[-1]+length)
        test(f't{t} row{i} tail positive', tails[i], '>', 1)
        test(f't{t} row{i} tail congruence', tails[i]%18, '=', 2)
        if 0 < i < 24:
            interval = [odd*l3-(length+1)*h2,odd*h3-(length+1)*l2]
            test(f't{t} row{i} actual factor above two', interval[0], '>', 0)
            factors.append(dict(i=i,numerator_exponent=odd,
                denominator_exponent_plus_one=length+1,log_c_over_2=interval,
                amplified_log_errors=[odd*(h3-l3),(length+1)*(h2-l2)]))
    test(f't{t} full product numerator exponent', prefix_A[-1], '=', K)
    test(f't{t} full product denominator exponent', prefix_D[-1], '=', N)
    incoming = []
    for i in range(25):
        expected_D = 4*sum(J[:i])+sum(H[:i])+2*i+(18*t if i==24 else 0)
        test(f't{t} incoming{i} full exponent', prefix_D[i], '=', expected_D)
        test(f't{t} incoming{i} bound positive', L[i], '>', 0)
        if i:
            test(f't{t} incoming{i} bound induction', L[i], '=',
                 L[i-1]*(w if i==1 else 2))
        incoming.append(dict(i=i,A=prefix_A[i],D=prefix_D[i],L=L[i],reciprocal=reciprocals[i]))
    A,D = prefix_A[18],prefix_D[18]
    P,R = A+3*J[18],D+4*J[18]+H[18]
    test(f't{t} row18 full coefficients', [A,D,P,R,J[18],H[18]], '=',
         [6078889,6862806,8157934,12930074,693015,3295208])
    test(f't{t} P positive', P, '>', 0)
    test(f't{t} R positive', R, '>', 0)
    f = T+P*u-R*ell
    interval = [T+P*l3-R*h2,T+P*h3-R*l2]
    error = [f-interval[1],f-interval[0]]
    test(f't{t} complete error positive', error[0], '>', 0)
    test(f't{t} complete error ordered', error[0], '<', error[1])
    test(f't{t} complete error bound', error[1], '<', Q(1,50000))
    test(f't{t} printed H upper bound', f, '=', Q(-172437107269,12500000000))
    test(f't{t} H guard rejected', f, '<', 0)
    test(f't{t} alternate negative coefficient', P-R, '<', 0)
    alt_margin = [T+(P-R)*b+P*c,T+(P-R)*a+P*d]
    test(f't{t} alternate margin lower nested', alt_margin[0], '>', interval[0])
    test(f't{t} alternate margin upper nested', alt_margin[1], '<', interval[1])
    alternative_margins.append(dict(t=t,interval=alt_margin,
        outward_error_interval=[f-alt_margin[1],f-alt_margin[0]]))
    allocations.append(dict(t=t,tails=tails,incoming=incoming,
        closing=dict(A=prefix_A[25],D=prefix_D[25]),factors=factors,
        row18=dict(J=J[18],H=H[18],A=A,D=D,P=P,R=R,upper_margin=f,
                   analytic_interval=interval,outward_error_interval=error,
                   verdict='REJECTED: certified negative upper H margin')))

expected = dict(scope=dict(d=35,t=[0,1],literal_order=True,B=B,
    inputs=['L055','L077','L083','L084'],no_allocation_or_order_reduction=True),
    source=dict(path=str(SOURCE.relative_to(ROOT)),sha256=hashlib.sha256(raw).hexdigest()),
    table=table,constants=dict(kappa=kappa,lambda_minus=lm,lambda_plus=lp,
        ell=ell,u=u,U=U,T=T),
    analytic=dict(logs=logs,lambda_interval=lambda_interval,
        lambda_amplified_errors=[N*(h2-l2),K*(h3-l3)],
        exp24_terms=exp_terms,exp24_lower=exp_lower),
    endpoint=dict(K=K,N=N,eta0=eta0,eta24_lower=eta0,e=2,domain_lower=domain),
    cap=dict(w=w,c0=c0,L=L,L_star=smallest,reciprocals=reciprocals,
        complete_reciprocal_sum=total,Q=q,R_H=cap,U=U,T=T),
    allocations=allocations,failures=[],
    summary=dict(roots=2,checks=424,failures=0,R_H=cap,U=U,T=T,
        exp24_lower_floor=exp_lower.numerator//exp_lower.denominator,
        row18_upper=[x['row18']['upper_margin'] for x in allocations],
        required_upper=0,verdicts=[x['row18']['verdict'] for x in allocations]))
match('construction', {k:v for k,v in original.items() if k!='checks'}, serial(expected))
test('construction comparison count', len(original['checks']), '=', 424)
test('construction comparison names unique', len({c['name'] for c in original['checks']}), '=', 424)
replays = []
for item in original['checks']:
    x,y = Q(item['actual']),Q(item['required'])
    rel = item['relation']
    passed = {'=': x==y,'<': x<y,'>': x>y,'<=': x<=y,'>=': x>=y}[rel]
    rebuilt = dict(name=item['name'],actual=str(x),relation=rel,required=str(y),
                   difference=str(x-y),passed=passed)
    match('replay/'+item['name'],item,rebuilt)
    test('replay truth/'+item['name'],passed,'=',True)
    replays.append(rebuilt)

summary = dict(checks=len(checks),failures=len(failures),
    constructor_comparisons_replayed=len(replays),incoming_terms=25,
    actual_nonzero_row_factor_intervals=46,R_H=cap,U=U,
    exp24_lower_floor=exp_lower.numerator//exp_lower.denominator,
    row18_upper=[x['row18']['upper_margin'] for x in allocations],required_upper=0,
    verdict='NO DEFECT FOUND' if not failures else 'AUDIT FAILED')
report = dict(scope='L100 only: d35 literal t=0,1; no larger-family verdict',
    construction_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    reconstruction=expected,construction_comparison_replays=replays,
    alternative_analytic=dict(log2=alt2,log_three_halves=alt32,
        lambda_interval=alt_lambda,row18=alternative_margins),
    checks=checks,failures=failures,summary=summary)
OUTPUT.write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps(summary,default=str))
print('Full audit certificate:',OUTPUT.relative_to(ROOT))
if failures:
    print('First failure:',failures[0]['name'])
    raise SystemExit(1)

#!/usr/bin/env python3
"""Fixed Taylor/beta response test. Exact selected full-degree coefficient.

The selected coefficient can stop a positive Bernstein norm allowance;
it cannot certify the response norm or lower-bound the actual error.
All higher degrees contribute identically zero to this selected coefficient.
"""
import hashlib
import importlib.util
import json
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction as Q
from math import comb, factorial, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l938-signed-response-89.json'
COEFF = BASE / 'l938-signed-response-coefficients-89.json'
DEG_E, DEG_Y, SELECTED = 2816, 2822, 1411
report = dict(status='IN_PROGRESS', checks=[], failures=[], inputs_sha256={},
              scope='Fixed [4,8], unchanged L938 p and full epsilon; second order then signed response',
              python=sys.version)


def save():
    OUT.write_text(json.dumps(report, indent=2) + '\n')


def check(name, ok):
    report['checks'].append(dict(name=name, passed=bool(ok)))
    if not ok:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw = (BASE / name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def enclosure(lo, hi):
    with localcontext() as ctx:
        ctx.prec = 16
        ctx.rounding = ROUND_FLOOR
        a = str(Decimal(lo.numerator) / Decimal(lo.denominator))
        ctx.rounding = ROUND_CEILING
        b = str(Decimal(hi.numerator) / Decimal(hi.denominator))
    check('outward display ' + str(len(report['checks'])), Q(a) <= lo <= hi <= Q(b))
    return dict(lower=a, upper=b)


save()
old = read('l938-negative-tail-allowance-87.json')
data = read('actual-h2-energy-cell-48.json')
check('unchanged approximation hash', old['inputs_sha256']['actual-h2-energy-cell-48.json']
      == report['inputs_sha256']['actual-h2-energy-cell-48.json'])
check('full inherited allowance checks', len(old['checks']) == 5682 and old['failures'] == []
      and all(row['passed'] is True for row in old['checks']))
ap = data['approximation']
check('unchanged fixed settings', (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision'])
      == (256, 257, 8, 200) and int(ap['chebyshev_denominator']) == 10**120)
epsilon = 8*10**9*Q(2,3)**256
for i, row in enumerate(ap['chebyshev_coefficients']):
    d = Q(int(row['chosen_numerator']), 10**120)
    eta = max(abs(d-Q(row['enclosure']['lower'])), abs(d-Q(row['enclosure']['upper'])))
    check('complete coefficient radius '+str(i), eta == Q(row['absolute_error']) and row['k']==i)
    epsilon += eta
check('complete unchanged epsilon', epsilon == Q(ap['epsilon']) == Q(old['exact']['epsilon'])
      and 0 < epsilon < Q(1, 10**34))
pi_lo, pi_hi = (Q(old['exact']['pi_'+s]) for s in ('lower','upper'))
exp_lo, exp_hi = (Q(old['exact']['exp_'+s]) for s in ('lower','upper'))
threshold = Q('8.935649629627030e-35')
W = sum((Q(abs(row['coefficient']), prod(factorial(k)**a for k,a in
        enumerate(row['exponents_A0_to_A6']))) for row in data['algebra']['terms']), Q(0))
check('row beta sum', len(data['algebra']['terms'])==34 and W==Q(293,540))
beta_mass = W*Q(8**18-4**18, 2**36*factorial(18))
second_factor = comb(12,2)*epsilon**2*8**10
second_lo = exp_lo*pi_lo**6*second_factor*beta_mass
second_hi = exp_hi*pi_hi**6*second_factor*beta_mass
check('complete Taylor combinatorics', 12*11*Q(1,2)==66)
check('second order below strict margin', 0 < second_lo <= second_hi < threshold)
report['second_order'] = dict(factor=str(second_factor), lower=str(second_lo), upper=str(second_hi),
    enclosure=enclosure(second_lo,second_hi), margin=str(threshold),
    margin_ratio=enclosure(second_lo/threshold, second_hi/threshold))
report['inherited_qualifications'] = ('L938 analytic kernel inclusion, source data and step50 audit '
    'remain inherited. Hashes/flags are consistency checks, not independent validation. '
    'Python integer, Fraction, Decimal display execution contracts retained; displays are checked exactly.')
save()
print('Second-order allowance:', report['second_order']['enclosure'], '; required <', threshold, flush=True)

# Rebuild the exact power basis, not a sampled evaluation of p.
def add(a,b):
    c=a[:]+[0]*max(0,len(b)-len(a))
    for i,v in enumerate(b): c[i]+=v
    return c


T0, T1 = [1], [-4,1]  # T_n(x/4-1)=Tn_int(x)/4^n.
chosen = [int(row['chosen_numerator']) for row in ap['chebyshev_coefficients']]
power = [chosen[0]*4**256]
power = add(power, [chosen[1]*4**255*v for v in T1])
for n in range(2,257):
    # 4^n T_n = 2(x-4)4^(n-1)T_(n-1) -16*4^(n-2)T_(n-2).
    nxt = add([0]+[2*v for v in T1], [-8*v for v in T1])
    nxt = add(nxt, [-16*v for v in T0])
    power = add(power, [chosen[n]*4**(256-n)*v for v in nxt])
    T0,T1=T1,nxt
check('complete exact Chebyshev to power basis', power==list(map(int,ap['power_numerators'])))
den=int(ap['power_denominator'])
check('unchanged power denominator', den==10**120*4**256)

# Use the already documented exact integer multiplication implementation,
# importing definitions only (the producer's main block is not invoked).
spec=importlib.util.spec_from_file_location('l938_integer_polys',BASE/'actual-h2-energy-cell-48.py')
lib=importlib.util.module_from_spec(spec)
spec.loader.exec_module(lib)
report['multiplication_source_sha256']=hashlib.sha256((BASE/'actual-h2-energy-cell-48.py').read_bytes()).hexdigest()
cut=SELECTED


def multiply(a,b):
    # Quotient ring Z[z]/(z^(cut+1)); nonnegative powers imply exact prefixes.
    return lib.intpoly_mul(a,b)[:cut+1]


C=2*factorial(12)*den*4**262
q=[]
for k in range(7):
    q.append([a*(factorial(2*(k+l))//factorial(k+l))*4**(262-k-l)
              *(factorial(12)//factorial(2*k)) for l,a in enumerate(power)])
powers={(k,0):[1] for k in range(7)}
powers.update({(k,1):q[k] for k in range(7)})


def getpower(k,n):
    if (k,n) not in powers:
        powers[k,n]=multiply(getpower(k,n//2),getpower(k,n-n//2))
    return powers[k,n]


grad=[]
for k in range(7):
    common0=5 if k==0 else 6
    inner=[0]
    for row in data['algebra']['terms']:
        alpha=row['exponents_A0_to_A6'][:]
        mult=alpha[k]
        if mult==0: continue
        alpha[k]-=1
        alpha[0]-=common0
        check('derivative factor exponents '+str(k)+','+str(len(report['checks'])),
              min(alpha)>=0 and sum(alpha)+common0==11)
        factors=[getpower(j,n) for j,n in enumerate(alpha) if n]
        factors.sort(key=len)
        while len(factors)>1:
            a,b=factors.pop(0),factors.pop(0)
            factors.append(multiply(a,b))
            factors.sort(key=len)
        inner=lib.intpoly_add(inner,factors[0],row['coefficient']*mult)
    grad.append(multiply(inner,getpower(0,common0)))
    check('full selected derivative prefix length '+str(k), len(grad[-1])==cut+1)
    print('Signed derivative prefix',k,'complete; all contributing rows combined',flush=True)

# E=8 is the right endpoint of the final energy cell. Therefore its
# Bernstein coefficient i=DEG_E equals that of Q(8,1-y) in y.
# y^(l+6-k)(1-y)^k contributes only if l+6-k <= SELECTED <= DEG_Y-k.
# The uncomputed coefficients l>cut cannot contribute for any 0<=k<=6.
check('all uncomputed powers vanish in selected Bernstein coefficient',
      all(cut+1+6-k>SELECTED for k in range(7)))
fact_common=factorial(2*(17+cut))
Fden=2*C**11*factorial(12)*fact_common
N=DEG_Y
numerator=0
pieces=[]
for k in range(7):
    subtotal=0
    for l,val in enumerate(grad[k]):
        a=l+6-k
        if not (a<=SELECTED<=N-k): continue
        h=17-k+l
        fac=factorial(2*h)
        check('half gamma denominator divides common '+str(k)+','+str(l),fact_common%fac==0)
        term=(val*4**h*factorial(h)*(factorial(12)//factorial(2*k))
              *(fact_common//fac)*8**l*comb(N-l-6,SELECTED-a))
        subtotal+=term
    pieces.append(subtotal)
    numerator+=subtotal
b=Q(numerator,Fden*comb(N,SELECTED))

# Strong coefficient-wise positive allowance, not just the maximum norm.
# w(y)=y^(21/2)(1-y)^(-1/2); integral w B_j^N = pi*beta_j.
j=SELECTED
beta_j=Q(comb(N,j)*factorial(2*j+22)*factorial(2*N-2*j),
         4**(N+11)*factorial(j+11)*factorial(N-j)*factorial(N+11))
a,h=Q(31,4),Q(1,4)
energy_mass=sum((Q(comb(17,z))*a**(17-z)*h**(z+1)/(DEG_E+z+1) for z in range(18)),Q(0))
contribution_lo=exp_lo*epsilon*pi_lo**6*abs(b)*beta_j*energy_mass
contribution_hi=exp_hi*epsilon*pi_hi**6*abs(b)*beta_j*energy_mass
report['selected'] = dict(energy_degree=DEG_E,residual_degree=DEG_Y,
    cell=['31/4','8'],i=DEG_E,j=SELECTED,coefficient=str(b),
    coefficient_enclosure=enclosure(b,b),beta_mass_over_pi=str(beta_j),
    energy_mass=str(energy_mass),coefficient_piece_numerators=list(map(str,pieces)),
    contribution_lower=str(contribution_lo),contribution_upper=str(contribution_hi),
    contribution_enclosure=enclosure(contribution_lo,contribution_hi),
    margin_ratio=enclosure(contribution_lo/threshold,contribution_hi/threshold))
COEFF.write_text(json.dumps(dict(C=str(C),cut=cut,full_degree=DEG_E,
    gradients=[list(map(str,row)) for row in grad],common_factorial=str(fact_common),
    selected_numerator=str(numerator),selected_denominator=str(Fden*comb(N,SELECTED)),
    multiplications=lib.MULTIPLICATIONS),indent=2)+'\n')
report['coefficient_certificate']=COEFF.name
report['coefficient_sha256']=hashlib.sha256(COEFF.read_bytes()).hexdigest()
if contribution_lo>threshold:
    report['status']='FIXED_SIGNED_BERNSTEIN_ALLOWANCE_STOP'
    report['decision']='One complete signed coefficient already exceeds the full margin in the positive coefficient-wise allowance; no actual error lower bound.'
else:
    report['status']='SELECTED_COEFFICIENT_INCONCLUSIVE'
    report['decision']='Second order paid; selected coefficient supplies no obstruction. Full positive coefficient sum remains unpaid.'
report['producer_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()
print('Result:',report['status'])
print('Selected coefficient:',report['selected']['coefficient_enclosure'])
print('Its positive allowance contribution:',report['selected']['contribution_enclosure'])
print('Required full allowance <',threshold,'; ratio:',report['selected']['margin_ratio'])
print('Checks:',len(report['checks']),'; failures:',report['failures'],'; certificate:',OUT)

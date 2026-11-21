#!/usr/bin/env python3
"""One fixed positive-row Chernoff test; full finite boxes and two omitted tails."""
import hashlib
import importlib.util
import json
import re
import sys
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE/'l938-fixed-outer-tail-96.json'
BOX = BASE/'l938-fixed-outer-tail-boxes-96.json'
report = dict(status='IN_PROGRESS', checks=[], failures=[], inputs_sha256={},
              settings=dict(precision=200, theta_terms=8, panels=4096, cutoff=4,
                            tilt='1/10', increment=1, energy_split=8), python=sys.version)


def save():
    OUT.write_text(json.dumps(report, indent=2)+'\n')


def check(name, ok):
    report['checks'].append(dict(name=name, passed=bool(ok)))
    if not ok:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw = (BASE/name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def display(lo, hi):
    with localcontext() as c:
        c.prec = 16
        c.rounding = ROUND_FLOOR
        a = str(Decimal(lo.numerator)/Decimal(lo.denominator))
        c.rounding = ROUND_CEILING
        b = str(Decimal(hi.numerator)/Decimal(hi.denominator))
    check('outward display '+str(len(report['checks'])), Q(a)<=lo<=hi<=Q(b))
    return dict(lower=a, upper=b)


save()
module_path = BASE.parent/'hankel/certify_hankel.py'
spec = importlib.util.spec_from_file_location('fixed_interval96', module_path)
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
report['interval_module_sha256'] = hashlib.sha256(module_path.read_bytes()).hexdigest()
for ctx in (iv.DOWN, iv.UP, iv.NEAR):
    ctx.prec = 200
check('all interval contexts precision200', all(c.prec == 200 for c in (iv.DOWN,iv.UP,iv.NEAR)))
I = iv.I
kernel = read('actual-h2-energy-cell-48.json')
compact = read('l938-compact-negative-mass-94.json')
audit92 = read('c948a-complete-budget-audit-92.json')
claim90 = read('l938-signed-response-complete-90.json')
ap = kernel['approximation']
check('fixed original settings', (ap['degree'],ap['nodes'],ap['theta_terms'],ap['precision'])
      == (256,257,8,200) and int(ap['chebyshev_denominator']) == 10**120)
check('compact same kernel', compact['inputs_sha256']['actual-h2-energy-cell-48.json']
      == report['inputs_sha256']['actual-h2-energy-cell-48.json'])
check('replacement same kernel and producer', audit92['inputs_sha256']['actual-h2-energy-cell-48.json']
      == report['inputs_sha256']['actual-h2-energy-cell-48.json']
      and audit92['inputs_sha256']['l938-signed-response-complete-90.json']
      == report['inputs_sha256']['l938-signed-response-complete-90.json'])
m = Q('8.935649629627030e-35')
B = Q(audit92['exact']['total_upper'])
margin = Q(compact['exact']['unused_margin'])
check('full exact margin identity', 0<B<m and B == Q(claim90['result']['total_upper'])
      and B == Q(compact['exact']['replacement_B'])
      and Q(compact['exact']['compact_polynomial_upper']) == 0
      and Q(compact['exact']['combined_upper']) == B
      and Q(compact['exact']['required_strict_upper']) == m and margin == m-B)

# Full rational Machin enclosure, including both alternating remainders.
def atan(q):
    s = sum((Q((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(128)), Q(0))
    return s, s+Q(1,257*q**257)


a,b = atan(5),atan(239)
plo,phi = Q(ap['pi']['lower']),Q(ap['pi']['upper'])
check('pi independent rational inclusion', 3<plo<=16*a[0]-4*b[1]<=16*a[1]-4*b[0]<=phi<4)
pi = I.rational(plo)+I(0, I.rational(phi-plo).hi)
check('pi interval enclosure', Q(pi.lo)<=plo<=phi<=Q(pi.hi))

lemma_path = BASE.parent.parent/'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md'
canonical = lemma_path.read_text()
table = [(int(c),list(map(int,s.split(',')))) for c,s in
         re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([0-9,]+)\)\s*\|$',canonical,re.M)]
rows = kernel['algebra']['terms']
check('complete exact34 row table', len(table)==len(rows)==34)
for j,((c,alpha),row) in enumerate(zip(table,rows)):
    check('row identity '+str(j), c==row['coefficient'] and alpha==row['exponents_A0_to_A6']
          and len(alpha)==7 and all(type(t)is int and t>=0 for t in alpha)
          and sum(alpha)==12 and sum(k*t for k,t in enumerate(alpha))==12)

q = (-pi).exp()
C = 8*pi**2*(1+11*q+11*q**2+q**3)/(1-q)**5
check('L058 cutoff meets every p case', Q(4)>=max(Q(1),3*Q(33,5)/(2*plo)))
e8 = I(8).exp()
u_tail = C*(-pi*e8/2).exp()/(pi*e8)
r = 2*(-19*pi).exp()
check('omitted theta geometric ratio', 0<r.lo<=r.hi<1 and Q(10,9)**4<2)
theta_kernel = 8*pi**2*I(18).exp()*9**4*(-81*pi).exp()/(1-r)
theta_tails = [theta_kernel*4*4**(2*k)*I.rational(Q(88,5)).exp()/factorial(2*k)
               for k in range(7)]
report['tail_enclosures'] = dict(C=C.data(), u_tail_each=u_tail.data(),
    theta_kernel_on_0_4=theta_kernel.data(), theta_moment_tails=[v.data() for v in theta_tails],
    theta_ratio=r.data())
report['stage'] = 'finite direct boxes; plan saved in drafts/2026-11-09-fixed-outer-tail-work-96.md'
save()
totals = [I(0) for _ in range(7)]
box_records = []
h = I.rational(Q(1,1024))
for j in range(4096):
    u = I(I.rational(Q(j,1024)).lo,I.rational(Q(j+1,1024)).hi)
    x = (2*u).exp()
    prefactor = (u/2).exp()
    K = I(0)
    for n in range(1,9):
        v = pi*n*n*x
        # Positive factorization from L019; no cancellation of large exponentials.
        term = 4*v*(2*v-3)*prefactor*(-v).exp()
        check('positive theta term '+str(j)+','+str(n), term.lo>0)
        K += term
    heated = (I.rational(Q(11,10))*u**2).exp()*K
    contributions = [h*heated*u**(2*k)/factorial(2*k) for k in range(7)]
    for k,value in enumerate(contributions):
        check('nonnegative finite contribution '+str(j)+','+str(k), 0<=value.lo<=value.hi)
        totals[k] += value
    box_records.append(dict(index=j, K=K.data(), contributions=[v.data() for v in contributions]))
    if (j+1)%1024==0:
        report['completed_panels']=j+1
        save()
BOX.write_text(json.dumps(dict(panels=4096,cutoff=4,width='1/1024',records=box_records),indent=2)+'\n')
report['box_artifact']=BOX.name
report['box_sha256']=hashlib.sha256(BOX.read_bytes()).hexdigest()

# Sum every stored contribution again with exact rational arithmetic, independently
# of the directed Decimal accumulation. No selected-panel preview is a check.
moments=[]
for k,total in enumerate(totals):
    exact_lo=sum((Q(row['contributions'][k]['lower']) for row in box_records),Q(0))
    exact_hi=sum((Q(row['contributions'][k]['upper']) for row in box_records),Q(0))
    check('complete rational panel-sum inclusion '+str(k), Q(total.lo)<=exact_lo<=exact_hi<=Q(total.hi))
    upper = total+I(0,theta_tails[k].hi)+I(0,u_tail.hi)
    check('complete positive moment '+str(k), 0<upper.lo<=upper.hi)
    moments.append(upper)
report['moments']=[dict(k=k,finite=totals[k].data(),actual=val.data(),
    display=display(Q(val.lo),Q(val.hi))) for k,val in enumerate(moments)]

row_results=[]
negative_sum=I(0)
for j,(c,alpha) in enumerate(table):
    if c>=0:
        continue
    product=I(abs(c))
    exact_lower=Q(abs(c))
    exact_upper=Q(abs(c))
    for k,power in enumerate(alpha):
        product *= moments[k]**power
        exact_lower *= Q(moments[k].lo)**power
        exact_upper *= Q(moments[k].hi)**power
    check('independent exact row endpoints '+str(j), Q(product.lo)<=exact_lower<=exact_upper<=Q(product.hi))
    negative_sum += product
    row_results.append(dict(row=j,coefficient=c,alpha=alpha,product=product.data(),
                            exact_lower=str(exact_lower),exact_upper=str(exact_upper)))
factor=I(-8).exp()
allowance=factor*negative_sum
elo=sum((Q(v['exact_lower']) for v in row_results),Q(0))*Q(factor.lo)
ehi=sum((Q(v['exact_upper']) for v in row_results),Q(0))*Q(factor.hi)
check('full independent exact allowance inclusion', Q(allowance.lo)<=elo<=ehi<=Q(allowance.hi))
check('all negative rows used',len(row_results)==sum(c<0 for c,_ in table))
upper=Q(allowance.hi)
lower=Q(allowance.lo)
report['row_results']=row_results
report['exact']=dict(m=str(m),B=str(B),unused_margin=str(margin),
    allowance_lower=str(lower),allowance_upper=str(upper),ratio_lower=str(lower/margin),
    ratio_upper=str(upper/margin),combined_upper=str(B+upper))
report['summary']=dict(allowance=display(lower,upper),margin=display(margin,margin),
    ratio=display(lower/margin,upper/margin),combined_upper=display(B+upper,B+upper),
    moments=7,negative_rows=len(row_results),passes=upper<margin,
    certified_allowance_exceeds_margin=lower>=margin)
report['status']='FIXED_CHERNOFF_PASSED' if upper<margin else 'FIXED_CHERNOFF_STOP'
report['stage']='complete'
report['qualification']='Original compact contracts inherited; new moment boxes conditional on L037 Decimal and exact Python arithmetic; no independent conceptual audit claimed.'
report['producer_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()
print('Result:',report['status'],'; allowance:',report['summary']['allowance'])
print('Required allowance <',report['summary']['margin'],'; ratio:',report['summary']['ratio'])
print('Moments7; panels4096; negative rows',len(row_results),'; checks',len(report['checks']),'; failures',report['failures'])
print('Certificate:',OUT,'; full boxes:',BOX)

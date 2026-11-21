"""Independent complete finite audit of C759n; originals are read-only.

Unpacked integer convolutions, recurrence Legendre polynomials, exact rational
kernel/exponential coefficients, and 1050-digit outward interval recomputation.
The certificate stores every comparison, not just samples or boolean summaries.
Analytic justifications and software trust qualifications are canonical in C759n.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import contextlib
import hashlib
import json
import runpy
import shutil
import sys
import numpy as np

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
SAVED = ROOT/'frozen-full-quotient-852.json'
SOURCE = ROOT/'frozen-full-quotient-852.py'
INPUT = ROOT/'even-time-one-pair-849.npz'
OUT = ROOT/'frozen-full-quotient-audit-854.json'
P = 1050
DOWN = Context(prec=P, rounding=ROUND_FLOOR)
UP = Context(prec=P, rounding=ROUND_CEILING)
old = json.loads(SAVED.read_text())
checks, failures = [], []
result = {'status': 'IN_PROGRESS', 'source_hashes': {}, 'checks': checks,
          'failures': failures, 'precision': P,
          'scope': 'One exact stored column0 only; no spectral or RH conclusion'}
for path in (SOURCE, SAVED, INPUT):
    result['source_hashes'][path.name] = hashlib.sha256(path.read_bytes()).hexdigest()

def save():
    OUT.write_text(json.dumps(result, indent=2)+'\n')

def check(name, condition, **evidence):
    checks.append({'name': name, 'passed': bool(condition), **evidence})
    if not condition:
        failures.append(name)
        save()
        raise ArithmeticError(name)

class J:
    def __init__(self, x=0, y=None):
        if isinstance(x, J):
            self.l, self.u = x.l, x.u
        elif isinstance(x, F):
            self.l = DOWN.divide(D(x.numerator), D(x.denominator))
            self.u = UP.divide(D(x.numerator), D(x.denominator))
        else:
            self.l, self.u = D(x), D(x if y is None else y)
        assert self.l.is_finite() and self.u.is_finite() and self.l <= self.u
    def __add__(a,b):
        b=J(b)
        return J(DOWN.add(a.l,b.l), UP.add(a.u,b.u))
    __radd__=__add__
    def __neg__(a):
        return J(a.u.copy_negate(),a.l.copy_negate())
    def __sub__(a,b): return a+-J(b)
    def __rsub__(a,b): return J(b)+-a
    def __mul__(a,b):
        b=J(b)
        ends=[(x,y) for x in (a.l,a.u) for y in (b.l,b.u)]
        return J(min(DOWN.multiply(x,y) for x,y in ends),
                 max(UP.multiply(x,y) for x,y in ends))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=J(b)
        assert b.l*b.u > 0  # only sign is tested; no rounded value is used
        ends=[(x,y) for x in (a.l,a.u) for y in (b.l,b.u)]
        return J(min(DOWN.divide(x,y) for x,y in ends),
                 max(UP.divide(x,y) for x,y in ends))
    def __rtruediv__(a,b): return J(b)/a
    def trans(a, name):
        if name in ('ln','sqrt'): assert a.l > 0
        return J(DOWN.next_minus(getattr(DOWN,name)(a.l)),
                 UP.next_plus(getattr(UP,name)(a.u)))
    def widen(a,r):
        r=J(r)
        assert r.l >= 0
        return J(DOWN.subtract(a.l,r.u),UP.add(a.u,r.u))
    def pair(a): return [str(a.l),str(a.u)]

def contains(name, outer, inner):
    inner=J(inner)
    check(name, D(outer[0]) <= inner.l <= inner.u <= D(outer[1]),
          independent_interval=inner.pair())

def exact(name, a, b):
    check(name, a == b)

save()
# Identity of every input, not just the zip hash.
check('input hash', result['source_hashes'][INPUT.name] ==
      'f74832d1420ec849848f3392e740a87b1bf9ddd53cb39a7ec9d7662c265548fa')
exact('generator hash', result['source_hashes'][SOURCE.name],old['script_sha256'])
raw=np.load(INPUT)['modal_coefficients']
check('input shape and finite', raw.shape == (256,256) and np.isfinite(raw[:,0]).all())
coeff=[F(*float(x).as_integer_ratio()) for x in raw[:,0]]
exact('all 256 coefficient fractions', [str(q) for q in coeff], old['input']['coefficients'])
exact('basis order',old['input']['basis'],'v,(1-x^2)P_0,(1-x^2)P_2,...,(1-x^2)P_508')
d=old['input']['denominator_exponent']
exact('denominator exponent',d,max(q.denominator.bit_length()-1 for q in coeff)+508)
scale=1<<d
facts=[factorial(k) for k in range(1300)]
# A_n=2^n P_n. (n+1)A_(n+1)=2(2n+1)x A_n-4n A_(n-1).
previous,current=[1],[0,2]
leg=[[1],[0,2]]
for n in range(1,508):
    v=[0]*(n+2)
    for k,c in enumerate(current): v[k+1]+=2*(2*n+1)*c
    for k,c in enumerate(previous): v[k]-=4*n*c
    assert all(c%(n+1)==0 for c in v)
    v=[c//(n+1) for c in v]
    previous,current=current,v
    leg.append(v)
p=[0]*511
for j,c in enumerate(coeff[1:]):
    q=c*scale/(1<<(2*j))
    assert q.denominator==1
    for k,z in enumerate(leg[2*j]):
        p[k]+=q.numerator*z
        p[k+2]-=q.numerator*z
check('exact polynomial parity and endpoints',not any(p[1::2]) and sum(p)==0)
# Successive differentiation, then Horner evaluation at -1 (no binomial formula).
left=[]
poly=p[:]
while poly:
    value=0
    for c in reversed(poly): value=c-value
    left.append(value)
    poly=[k*poly[k] for k in range(1,len(poly))]
right=[-((-1)**k)*v for k,v in enumerate(left)]
c=coeff[0]*scale
assert c.denominator==1
# Independently multiply the left-edge quadratic 80t-1600t^2 by itself.
q=[0,80,-1600]
bump=[sum(q[i]*q[k-i] for i in range(3) if 0<=k-i<3)
      for k in range(5)]
bl=[c.numerator*v*facts[k] for k,v in enumerate(bump)]
br=[-((-1)**k)*v for k,v in enumerate(bl)]
positions=list(map(F,('-1','-33/40','-31/40','31/40','33/40','1')))
jumps=[left,bl,br,bl,br,right]
exact('all jump positions',[str(x) for x in positions],old['exact_geometry']['jump_positions'])
exact('every derivative jump',[[str(x) for x in row] for row in jumps],
      old['exact_geometry']['jump_derivatives_integer_numerators'])
# Ordered pairs and ordinary distributive convolution, with no packing.
rows={}
for a,wa in zip(positions,jumps):
    for b,wb in zip(positions,jumps):
        edge=-a-b
        if edge<=0: continue
        row=rows.setdefault(edge,[0]*1022)
        for i,x in enumerate(wa):
            if not x: continue
            for j,y in enumerate(wb):
                if y: row[i+j+1]+=x*y
oldrows=old['exact_geometry']['autocorrelation_integer_numerators']
exact('all correlation breakpoints',set(map(str,rows)),set(oldrows))
for b,row in sorted(rows.items()):
    exact('every integer coefficient at '+str(b),list(map(str,row)),oldrows[str(b)])
print('All input, endpoint jumps and unpacked convolution coefficients verified.',flush=True)
# Exact rational weights; independent second derivative and norm evaluations.
weights={b:[(k,F(v,scale*scale*facts[k])*b**k)
             for k,v in enumerate(row) if v] for b,row in rows.items()}
N=sum((a for row in weights.values() for _,a in row),F(0))
D1=-sum((a*k*(k-1)/(b*b) for b,row in weights.items() for k,a in row if k>=2),F(0))
exact('exact norm fraction',str(N),old['exact_geometry']['norm_squared_exact'])
exact('exact derivative fraction',str(D1),old['exact_geometry']['derivative_norm_squared_exact'])
check('norm and derivative positive',N>0 and D1>0)
norm,derivative=J(N),J(D1)
contains('norm interval',old['bounds']['norm_squared'],norm)
contains('derivative interval',old['bounds']['derivative_norm_squared'],derivative)
result['exact_norms']={'norm_squared':str(N),'derivative_squared':str(D1)}
save()
# Exact harmonic numbers; moment accumulation in reverse boundary/k order.
harm=[F(0)]
for k in range(1,1022): harm.append(harm[-1]+F(1,k))
mom=[J(0) for _ in range(257)]
t0=J(0)
for b,row in sorted(weights.items(),reverse=True):
    sub=J(0)
    lg=J(2/b).trans('ln')
    for k,a in reversed(row):
        sub+=J(a)*(J(harm[k])+lg)
        term=J(a*b/F(k+1))
        for n in range(1,257):
            mom[n]+=term
            term*=J(b*n/F(k+n+1))
    t0+=sub
    original=next(x['T0'] for x in old['integration']['T0_components'] if x['boundary']==str(b))
    contains('origin component '+str(b),original,sub)
for n in range(1,257):
    contains('moment '+str(n),old['integration']['moments'][n-1],mom[n])
print('All origin components and 256 complete moments verified.',flush=True)
save()
# All kernel coefficients and exponential integrals first calculated rationally.
kernel=[]
integral=J(0)
exp_error=J(0)
for n in range(257):
    kn=F(1,(1<<n)*facts[n])-sum((kernel[n-j]/facts[j+1] for j in range(2,n+1,2)),F(0))
    kernel.append(kn)
    en=sum((F((-1)**j*(1<<n),facts[j]*(n+j)) for j in range(1,129)),F(0))
    er=F(1<<n,facts[129]*(n+129))
    e=J(en).widen(J(er))
    t=t0 if n==0 else J(N*F(1<<n,n))-mom[n]
    term=J(kn)*(t+norm*e)
    integral+=term
    exp_error+=J(abs(kn)*N*er)
    rec=old['integration']['terms'][n]
    exact('term index '+str(n),rec['n'],n)
    for label,val in [('kernel',J(kn)),('En',e),('Tn',t),('term',term)]:
        contains(label+' '+str(n),rec[label],val)
err=J(100*F(4,5)**257*(D1+N))
contains('entire kernel error',old['integration']['kernel_error'],err)
contains('exponential error',old['integration']['exponential_error_included'],exp_error)
integral=integral.widen(err)
# Machin and Euler--Maclaurin imports, exact rational partial sums/radii.
def atan(k):
    a=sum((F((-1)**j,(2*j+1)*k**(2*j+1)) for j in range(60)),F(0))
    return J(a).widen(J(F(1,121*k**121)))
pi=16*atan(5)-4*atan(239)
sin_lower=sum((F((-1)**j)*F(5,2)**(2*j+1)/facts[2*j+1] for j in range(6)),F(0))
check('Cauchy circle constant',pi.l>D('2.5') and sin_lower>F(1,2) and J(F(5,4)).trans('exp').u<4,
      sin_lower_exact=str(sin_lower))
gk=1024
gerr=J(F(1,60*gk**4))
gamma=J(sum((F(1,j) for j in range(1,gk+1)),F(0))-F(1,2*gk)+F(1,12*gk*gk))-J(gk).trans('ln')
gamma=gamma.widen(gerr)
contains('gamma radius',old['integration']['gamma_error'],gerr)
e2=J(2).trans('exp')
tanh=(e2-1)/(e2+1)
arch=-(gamma+(4*pi*tanh).trans('ln'))*norm+integral
pole=sum((mom[2*j+1]*J(F(4,(1<<(2*j))*facts[2*j])) for j in reversed(range(65))),J(0))
perr=J(F(16)*N/facts[130])
contains('pole error',old['integration']['pole_error'],perr)
pole=pole.widen(perr)
# Direct powers with factorial recurrence, different from generator Horner.
primes=J(0)
for rec,(n,base) in zip(old['primes'],[(2,2),(3,3),(4,2),(5,5),(7,7)]):
    exact('prime identifiers '+str(n),(rec['n'],rec['base']),(n,base))
    y=J(n).trans('ln')
    w=J(base).trans('ln')/J(n).trans('sqrt')
    cy=J(0)
    for b,row in sorted(rows.items(),reverse=True):
        edge=J(b)
        if edge.u<y.l: continue
        check('shift piece '+str(n)+' '+str(b),edge.l>y.u)
        r=edge-y
        power=J(1)
        for k,v in enumerate(row):
            if v: cy+=power*J(F(v,scale*scale))
            power=power*r/(k+1)
    contribution=-2*w*cy
    for label,val in [('delay',y),('weight',w),('correlation',cy),('contribution',contribution)]:
        contains('prime '+str(n)+' '+label,rec[label],val)
    primes+=contribution
form=arch+pole+primes
quotient=form/norm
result['independent_bounds']={k:v.pair() for k,v in
    [('norm_squared',norm),('derivative_norm_squared',derivative),('archimedean',arch),
     ('both_poles',pole),('prime_sum',primes),('full_form',form),('quotient',quotient)]}
for key in ('archimedean','both_poles','prime_sum','full_form','quotient'):
    contains('complete '+key,old['bounds'][key],J(*result['independent_bounds'][key]))
# Check published brackets against ALL original endpoints as well.
for key,lo,hi in [('norm_squared','0.00012977475671912','0.00012977475671913'),
                  ('derivative_norm_squared','10.92731417769','10.92731417771'),
                  ('full_form','0.00000175452250713','0.00000175452250715'),
                  ('quotient','0.01351975184924','0.01351975184928'),
                  ('archimedean','0.00005742105688320','0.00005742105688322'),
                  ('both_poles','0.00000364173996494','0.00000364173996496'),
                  ('prime_sum','-0.00005930827434103','-0.00005930827434100')]:
    a,b=map(D,old['bounds'][key])
    check('published '+key,D(lo)<a<=b<D(hi),required_open_bracket=[lo,hi])
check('published kernel upper bound',D(old['integration']['kernel_error'][1])<D('1.358e-22'))
check('original checks and failures',old['failures']==[] and
      all(v == (k!='quotient_negative') for k,v in old['checks'].items()))
result['mathematical_result']='POSITIVE_FIXED_VECTOR'
print('Every saved term, error, shift and complete interval checked; positive quotient.',flush=True)
save()
# Exact-byte replay, under deliberately small ambient precision, in a new directory.
replay=ROOT/'audit-854-replay'
replay.mkdir(exist_ok=True)
shutil.copyfile(SOURCE,replay/SOURCE.name)
shutil.copyfile(INPUT,replay/INPUT.name)
with localcontext() as ctx, (replay/'replay.log').open('w') as log, contextlib.redirect_stdout(log):
    ctx.prec=7
    runpy.run_path(str(replay/SOURCE.name),run_name='__main__')
replayed=json.loads((replay/SAVED.name).read_text())
exact('entire parsed replay certificate',replayed,old)
for path in (SOURCE,SAVED,INPUT):
    exact('original preserved '+path.name,hashlib.sha256(path.read_bytes()).hexdigest(),result['source_hashes'][path.name])
result['status']='AUDIT_PASSED'
result['replay']={'path':str((replay/SAVED.name).relative_to(ROOT)),
                  'ambient_decimal_precision':7,'entire_certificate_equal':True}
result['software']={'python':sys.version,'numpy':np.__version__,
                    'trust':'Python integers/Fraction/Decimal and NumPy binary64 loading; not formal verification'}
result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
result['check_count']=len(checks)
save()
print('Audit:',len(checks),'checks;',len(failures),'failures; required quotient lower>0.')
print('Original quotient bracket: (0.01351975184924, 0.01351975184928)')
print('Certificate:',OUT)
print('Replay:',replay/SAVED.name)

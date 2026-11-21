#!/usr/bin/env python3
"""Independent fixed-parameter reconstruction for C919n. No evaluator imports."""
import decimal as dec
from decimal import Decimal as D
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import json, hashlib, sys, time

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
CP = ROOT/'origin_margin_2231.json'
PP = ROOT/'origin_margin_preflight_2231.json'
original = json.loads(CP.read_text())
pre = json.loads(PP.read_text())
contexts = [dec.Context(prec=100, rounding=r, Emin=-999999, Emax=999999)
            for r in [dec.ROUND_FLOOR, dec.ROUND_CEILING, dec.ROUND_HALF_EVEN]]
L,H,C = contexts
for ctx in contexts:
    for sig in ctx.traps:
        ctx.traps[sig] = sig not in (dec.Inexact, dec.Rounded)
    ctx.clear_flags()
checks, failures, bounds, node_rows = [], [], [], []

def check(name, ok):
    checks.append({'name':name,'passed':bool(ok)})
    if not ok:
        failures.append(name)

def scalar(x):
    if isinstance(x, Q):
        return L.divide(D(x.numerator),D(x.denominator)), H.divide(D(x.numerator),D(x.denominator))
    return D(x),D(x)

def plus(a,b):
    return L.add(a[0],b[0]), H.add(a[1],b[1])

def minus(a):
    return a[1].copy_negate(), a[0].copy_negate()

def times(a,b):
    return min(L.multiply(x,y) for x in a for y in b), max(H.multiply(x,y) for x in a for y in b)

def subtract(a,b):
    return plus(a,minus(b))

def ipow(a,n):
    v=scalar(1)
    for _ in range(n): v=times(v,a)
    return v

def exponential(a):
    return L.next_minus(C.exp(a[0])), H.next_plus(C.exp(a[1]))

def upper(x): return x[1]

def isum(xs):
    v=scalar(0)
    for x in xs: v=plus(v,x)
    return v

def record(a): return {'lower':str(a[0]),'upper':str(a[1])}

def saved(a): return Q(a['lower']),Q(a['upper'])

def contains(outer,inner):
    return Q(outer[0]) <= Q(inner[0]) <= Q(inner[1]) <= Q(outer[1])

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

check('original script hash',sha(ROOT/'origin_margin_2231.py')==original['script_sha256'])
check('original preflight hash',sha(PP)==original['preflight_sha256'])
params=dict(U=4,N=4,panels=65536,spatial_cells=1024,parameter_cells=32,
            degree=8,digits=80,center='57/4',radius='1/4',bracket=['14','29/2'])
check('fixed claimed parameters',original['parameters']==pre['parameters']==params)
# Exact finite Machin enclosures, independent summation order.
def atan(q,m):
    terms=[Q((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(m+1)]
    s=sum(reversed(terms[:-1]),Q(0))
    return min(s,s+terms[-1]),max(s,s+terms[-1])
a,b=atan(5,80),atan(239,25)
piq=(16*a[0]-4*b[1],16*a[1]-4*b[0])
pi=(scalar(piq[0])[0],scalar(piq[1])[1])
check('exact Machin bounds',list(map(str,piq))==pre['constants']['exact_pi_bounds'])
check('pi inequalities',3<piq[0]<piq[1]<Q(22,7) and piq[1]**2<10)
check('pi serialized enclosure',contains(saved(original['constants']['pi']),pi))
check('geometric fourth moment', (1+11*Q(1,2)+11*Q(1,2)**2+Q(1,2)**3)/(1-Q(1,2))**5==300)
check('spatial constant',sum((Q(3)**j/factorial(j) for j in range(9)),Q(0))>20 and
      80*(1+11*Q(1,20)+11*Q(1,20)**2+Q(1,20)**3)/(1-Q(1,20))**5<200)
index0=times(scalar(15000000),exponential(scalar(-75)))
space=times(scalar(Q(200,768)),exponential(scalar(-384)))
indices=[times(index0,scalar(Q(factorial(j),145**(j+1)))) for j in range(10)]
check('pointwise tail',Q(pre['k0_index_tail'])>=Q(index0[1]))
check('ninth index and spatial tails',Q(pre['complete_ninth']['index'])>=Q(indices[9][1]) and Q(pre['complete_ninth']['spatial'])>=Q(space[1]))
rates=[times(pi,scalar(n*n)) for n in range(1,5)]
max4=[D(0)]*9
moment9=scalar(0)
# Independent generic interval Bell recurrences, not original's upper-only helpers.
for k in range(1024):
    left,right=Q(k,256),Q(k+1,256)
    el=exponential(scalar(2*left)); er=exponential(scalar(2*right))
    E=[scalar(0) for _ in range(5)]
    for alpha in rates:
        vlo=times(alpha,el)[0]; vhi=times(alpha,er)[1]
        for b,pref in [(Q(9,2),times(scalar(8),ipow(alpha,2))),
                       (Q(5,2),times(scalar(12),alpha))]:
            z=H.subtract(scalar(b*right)[1],vlo)
            E0=times(pref,exponential(scalar(z)))
            hh=[None,plus(scalar(b),times(scalar(2),scalar(vhi))),
                times(scalar(4),scalar(vhi)),times(scalar(8),scalar(vhi)),times(scalar(16),scalar(vhi))]
            bell=[scalar(1)]
            for order in range(1,5):
                bell.append(isum(times(scalar(comb(order-1,s)),times(bell[order-1-s],hh[s+1])) for s in range(order)))
            for order in range(5): E[order]=plus(E[order],times(E0,bell[order]))
    row=pre['spatial_cells'][k]
    check('spatial cell '+str(k),row['index']==k and saved(row['interval'])==(left,right))
    check('exponential derivative reconstruction '+str(k),all(Q(v)>=Q(e[1]) for v,e in zip(row['kernel_derivative_bounds'],E)))
    part=times(scalar((right-left)*right**9),E[0])
    check('ninth cell '+str(k),Q(row['ninth_moment_part'])>=Q(part[1]))
    moment9=plus(moment9,part)
    for j in range(9):
        value=isum(times(scalar(Q(comb(4,t)*comb(t,s),factorial(j-s))*right**(j-s)*Q(57,4)**(4-t)),E[t-s])
                   for t in range(5) for s in range(t+1) if s<=j)
        max4[j]=max(max4[j],value[1])
    bounds.append({'index':k,'derivatives':[str(e[1]) for e in E], 'ninth':str(part[1])})
complete9=isum([moment9,indices[9],space])
rem=times(complete9,scalar(Q(1,4)**9/factorial(9)))
check('complete ninth reconstructed',Q(pre['complete_ninth']['bound'])>=Q(complete9[1]))
check('remainder reconstructed',Q(pre['complete_ninth']['remainder'])>=Q(rem[1]))
errors=[]
for j in range(9):
    e=pre['errors'][j]
    check('fourth maximum '+str(j),Q(e['fourth_derivative'])>=Q(max4[j]))
    simpson=times(scalar(Q(4**5,180*65536**4)),scalar(max4[j]))
    ix=times(indices[j],scalar(Q(1,factorial(j))))
    sp=times(space,scalar(Q(1,factorial(j))))
    check('coefficient errors '+str(j),Q(e['simpson'])>=Q(simpson[1]) and Q(e['index'])>=Q(ix[1]) and Q(e['spatial'])>=Q(sp[1]))
    errors.append(isum([simpson,ix,sp])[1])
print('Independent preflight:',len(checks),'checks; failures:',len(failures),flush=True)
# Rational step polynomials then conversion, instead of repeated interval powers.
d=Q(57,65536)
tr=d**32/factorial(32)
cs=sum(((-1)**k*d**(2*k)/factorial(2*k) for k in range(16)),Q(0))
sn=sum(((-1)**k*d**(2*k+1)/factorial(2*k+1) for k in range(16)),Q(0))
stepc=(scalar(cs-tr)[0],scalar(cs+tr)[1]); steps=(scalar(sn-tr)[0],scalar(sn+tr)[1])
check('trig cosine step',contains(saved(original['trig']['step_cosine']),stepc))
check('trig sine step',contains(saved(original['trig']['step_sine']),steps))
c,s=scalar(1),scalar(0)
sums=[scalar(0) for _ in range(9)]
k0=None
for i in range(65537):
    t=Q(i,16384)
    tval=scalar(t)
    ex=exponential(scalar(2*t))
    # Difference of the two exponential kernel terms, independently normalized.
    kernel=scalar(0)
    for alpha in rates:
        v=times(alpha,ex)
        term1=times(times(scalar(8),ipow(alpha,2)),exponential(subtract(scalar(Q(9,2)*t),v)))
        term2=times(times(scalar(12),alpha),exponential(subtract(scalar(Q(5,2)*t),v)))
        kernel=plus(kernel,subtract(term1,term2))
    if i==0: k0=kernel
    phase=[s,c,minus(s),minus(c)]
    wt=1 if i in (0,65536) else (4 if i%2 else 2)
    power=scalar(1)
    for j in range(9):
        term=times(times(kernel,power),times(scalar(Q(wt,factorial(j))),phase[j%4]))
        sums[j]=plus(sums[j],term)
        power=times(power,tval)
    if i%4096==0:
        node_rows.append({'i':i,'kernel':record(kernel),'cos':record(c),'sin':record(s)})
    if i<65536:
        c,s=subtract(times(c,stepc),times(s,steps)),plus(times(s,stepc),times(c,steps))
check('final trig cosine',contains(saved(original['trig']['final_cosine']),(c)))
check('final trig sine',contains(saved(original['trig']['final_sine']),(s)))
check('finite K0',contains(saved(original['k0']['finite']),k0))
fullk=(k0[0],H.add(k0[1],index0[1]))
check('full K0',contains(saved(original['k0']['enclosure']),fullk))
coeff=[]; coeffrows=[]
for j in range(9):
    quad=times(scalar(Q(1,49152)),sums[j])
    check('independent quadrature '+str(j),contains(saved(original['coefficients'][j]['quadrature']),quad))
    a=(L.subtract(quad[0],errors[j]),H.add(quad[1],errors[j]))
    coeff.append(a)
    check('independent coefficient '+str(j),contains(saved(original['coefficients'][j]['enclosure']),a))
    coeffrows.append({'j':j,'quadrature':record(quad),'error':str(errors[j]),'coefficient':record(a)})
cellrows=[]
for k in range(32):
    x=(scalar(Q(14)+Q(k,64))[0],scalar(Q(14)+Q(k+1,64))[1])
    delta=subtract(x,scalar(Q(57,4)))
    v=coeff[-1]
    for a in reversed(coeff[:-1]): v=plus(times(v,delta),a)
    sine=(L.subtract(v[0],rem[1]),H.add(v[1],rem[1]))
    margin=subtract(times(x,sine),fullk)
    check('closed parameter cell '+str(k),original['parameter_cells'][k]['x']==[str(Q(x[0])),str(Q(x[1]))])
    check('independent margin contained '+str(k),contains(saved(original['parameter_cells'][k]['margin']),margin))
    check('independent margin >1/5 '+str(k),Q(margin[0])>Q(1,5))
    cellrows.append({'index':k,'x':record(x),'margin':record(margin)})
hull=(min(D(r['margin']['lower']) for r in cellrows),max(D(r['margin']['upper']) for r in cellrows))
check('original displayed rational hull',Q('0.2420677')<=Q(hull[0]) and Q(hull[1])<=Q('0.2779602'))
for label,artifact in [('original',original),('preflight',pre)]:
    check(label+' runtime contracts',artifact['failures']==[] and artifact['runtime']['unexpected_signals']==[] and
          all(not flag or signal in ('Inexact','Rounded') for flags in artifact['runtime']['flags'].values() for signal,flag in flags.items()))
for n,ctx in enumerate(contexts):
    check('audit exceptional signals '+str(n),all(not v or sig in (dec.Inexact,dec.Rounded) for sig,v in ctx.flags.items()))
result={'status':'PASS' if not failures else 'FAIL','checks':checks,'failures':failures,
 'fixed_parameters':params,'independent_digits':100,'spatial_reconstruction':bounds,
 'complete_ninth':record(complete9),'remainder':record(rem),'nodes_evaluated':65537,
 'node_checkpoints':node_rows,'trig':{'cos':record(c),'sin':record(s)},
 'k0':record(fullk),'coefficients':coeffrows,'parameter_cells':cellrows,
 'uniform_margin':record(hull),'required_bound':'1/5',
 'original_metadata_note':'rational_claim says 1/10; independently checked stronger canonical 1/5',
 'runtime':{'python':sys.version,'libmpdec':dec.__libmpdec_version__,'contexts':list(map(str,contexts)),
            'elapsed_seconds':time.monotonic()-START},
 'hashes':{'original':sha(CP),'preflight':sha(PP),'audit_source':sha(Path(__file__))},
 'qualification':'Same stated backend contracts; independent implementation, not backend recertification.'}
out=ROOT/'origin_margin_audit_2233.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(result['status'],len(checks),'checks; failures:',failures,flush=True)
print('Actual:',hull,'required >1/5; certificate:',out,flush=True)
if failures: raise SystemExit(1)

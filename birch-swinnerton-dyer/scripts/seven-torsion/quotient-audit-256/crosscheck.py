"""Exact interpolation over the full direction field; no notebook imports."""
from fractions import Fraction as Q
from pathlib import Path
import json,signal,time
R=Path(__file__).resolve().parent; U=R.parent
start=time.monotonic()
signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('180-second bound')))
signal.alarm(180)
c=json.loads((U/'quotient-254/quotient.json').read_text())
h=list(map(Q,c['h'])); assert len(h)==9 and h[8]==1
zero=(Q(0),)*8
one=(Q(1),)+(Q(0),)*7

def field(a):
    a=list(map(Q,a))
    while len(a)>8:
        v=a.pop(); offset=len(a)-8
        for j in range(8):a[offset+j]-=v*h[j]
    return tuple(a+[Q(0)]*(8-len(a)))
def add(*args):return tuple(sum(v[i] for v in args) for i in range(8))
def scale(a,k):return tuple(k*x for x in a)
def mul(a,b):
    p=[Q(0)]*15
    for i in range(8):
        for j in range(8):p[i+j]+=a[i]*b[j]
    return field(p)
def power(a,n):
    r=one
    for _ in range(n):r=mul(r,a)
    return r
def read(k):return [field(v) for v in c[k]]
def ev(p,t):
    r=zero
    for a in reversed(p):r=add(scale(r,t),a)
    return r
def deriv(p):return [scale(p[i],i) for i in range(1,len(p))]
def enc(v):
    if isinstance(v,Q):return str(v)
    if isinstance(v,(list,tuple)):return [enc(x) for x in v]
    if isinstance(v,dict):return {k:enc(x) for k,x in v.items()}
    return v
checks=[]
def need(v,label):
    if not v:raise ValueError(label)
    checks.append(label)
q=read('q');N=read('x_numerator');M=read('y_multiplier_numerator')
need(len(q)==4 and q[-1]==one and len(N)==8 and N[-1]==one and len(M)==10 and M[-1]==one,'monic_degrees_3_7_9')
need(all(len(v)<=8 for k in ['q','x_numerator','y_multiplier_numerator'] for v in c[k]),'full_field_coefficient_bounds')
qp=deriv(q);qpp=deriv(qp);np=deriv(N)
ap=field(c['target_a']);bp=field(c['target_b']);a=Q(-3024);b=Q(46224)
s1=scale(q[2],-1)
for i,w in enumerate(c['constant_inverses']):need(mul(field(w['value']),field(w['inverse']))==one,'constant_unit_'+str(i))
disc=scale(add(scale(power(ap,3),4),scale(power(bp,2),27)),-16)
need(disc==field(c['target_discriminant']) and mul(disc,field(c['target_discriminant_inverse']))==one,'target_nonsingular')
rows=[]
for t in range(-10,12):
    qt=ev(q,t);dt=ev(qp,t);ddt=ev(qpp,t);nt=ev(N,t);mt=ev(M,t);ndt=ev(np,t)
    ct=t**3+a*t+b
    q2=power(qt,2);q4=power(qt,4);q6=power(qt,6)
    # A distinct evaluation of the displayed kernel-polynomial formula.
    predicted=add(mul(add(scale(one,7*t),scale(s1,-2)),q2),
        scale(mul(dt,qt),-(6*t*t+2*a)),
        scale(add(power(dt,2),scale(mul(qt,ddt),-1)),4*ct))
    diffN=add(nt,scale(predicted,-1))
    diffM=add(mt,scale(mul(ndt,qt),-1),scale(mul(nt,dt),2))
    # Cleared equation has degree at most 21 in t, before evaluation.
    lhs=scale(power(mt,2),ct)
    rhs=add(power(nt,3),mul(ap,mul(nt,q4)),mul(bp,q6))
    curve=add(lhs,scale(rhs,-1))
    differential=add(mul(mt,qt),scale(mul(ndt,q2),-1),scale(mul(nt,mul(qt,dt)),2))
    denx=add(ev(read('x_denominator'),t),scale(q2,-1))
    deny=add(ev(read('y_multiplier_denominator'),t),scale(power(qt,3),-1))
    residuals={'N_formula':diffN,'M_formula':diffM,'curve':curve,'differential':differential,'x_denominator':denx,'y_denominator':deny}
    for k,v in residuals.items():need(v==zero,k+'_'+str(t))
    rows.append({'t':t,'q':qt,'N':nt,'M':mt,'curve_left':lhs,'curve_right':rhs,'residuals':residuals})
need(len(c['x_denominator'])==7 and len(c['y_multiplier_denominator'])==10,'denominator_degree_bounds')
report={'passed':True,'checks':checks,'failures':[],
    'identity_degree_bounds':{'N_formula':7,'M_formula':9,'curve':21,'differential':12,'x_denominator':6,'y_denominator':9},
    'actual_distinct_evaluations':len(rows),'required_for_all_identities':22,'field_coordinates_each':8,'evaluations':rows,
    'seconds':time.monotonic()-start,'required_seconds':180}
with (R/'crosscheck.json').open('x') as f:json.dump(enc(report),f,indent=2)
signal.alarm(0)
print(json.dumps({k:v for k,v in report.items() if k not in ['checks','evaluations']}))

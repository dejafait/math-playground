"""Integer interval Simpson certificate for exp(-u^6-4u^2), x=10.
Only Python's exact integer/Fraction arithmetic is used for the proof.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
S=2**256
N=8192

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[1],-a[0])
def mul(a,b):
    vs=[x*y for x in a for y in b]
    return (min(vs)//S, -((-max(vs))//S))
def div(a,k): return (a[0]//k,-((-a[1])//k))
def exact(q):
    q=Q(q)*S
    assert q.denominator==1
    return (q.numerator,q.numerator)
def widen(a): return (a[0]-1,a[1]+1)
def exp_minus(q):
    r=div(neg(q),128)
    t=exact(1); z=t
    for k in range(1,81):
        t=div(mul(t,r),k); z=add(z,t)
    z=widen(z)
    for _ in range(7): z=mul(z,z)
    return z
def trig(y):
    y=div(y,32); yy=neg(mul(y,y))
    ct=exact(1); st=y; c=ct; s=st
    for k in range(1,41):
        ct=div(mul(ct,yy),(2*k-1)*(2*k)); c=add(c,ct)
        st=div(mul(st,yy),(2*k)*(2*k+1)); s=add(s,st)
    c=widen(c); s=widen(s)
    for _ in range(5):
        c,s=add(mul(c,c),neg(mul(s,s))),mul(exact(2),mul(s,c))
    return c,s
assert Q(5,8)**81/Q(factorial(81)) < Q(1,S)
assert Q(5,8)**82/Q(factorial(82)) < Q(1,S)
assert Q(5,8)**83/Q(factorial(83)) < Q(1,S)
sums=[(0,0)]*3
for i in range(N+1):
    u=Q(2*i,N)
    e=exp_minus(exact(u**6+4*u*u))
    c,s=trig(exact(10*u))
    vals=[mul(e,c),neg(mul(exact(u),mul(e,s))),neg(mul(exact(u*u),mul(e,c)))]
    w=1 if i in (0,N) else 4 if i%2 else 2
    sums=[add(a,(w*v[0],w*v[1])) for a,v in zip(sums,vals)]
A,B,C,D=218,488,960,1440
H2=A*A+B
H3=A**3+3*A*B+C
H4=A**4+6*A*A*B+3*B*B+4*A*C+D
Ms=[H4,2*H4+4*H3,4*H4+16*H3+12*H2]
# Q(u)>=80+208(u-2) for u>=2. exp(-80)<2^-80.
# Moments of (2+v)^j exp(-208v), v>=0, j=0,1,2.
tails=[2*Q(1,2**80)*Q(1,208),2*Q(1,2**80)*(Q(2,208)+Q(1,208**2)),2*Q(1,2**80)*(Q(4,208)+Q(4,208**2)+Q(2,208**3))]
errors=[Q(16*m,45*N**4) for m in Ms]
intervals=[]
for a,err,tail in zip(sums,errors,tails):
    intervals.append((Q(4*a[0],3*N*S)-err-tail,Q(4*a[1],3*N*S)+err+tail))
coarse=[(Q(2041,10**6),Q(2043,10**6)),(Q(-552,10**6),Q(-550,10**6)),(Q(777,10**6),Q(779,10**6))]
checks=[lo<=a<=b<=hi for (a,b),(lo,hi) in zip(intervals,coarse)]
assert all(checks), 'coarse enclosure failed'
d_upper=coarse[1][0]**2-coarse[0][0]*coarse[2][0]
assert d_upper<0
out=dict(kind='EXACT_INTEGER_INTERVAL_CERTIFICATE',parameter_b=4,frequency_x=10,N=N,scale_bits=256,exploratory_evaluations_added=0,
    derivative_constants=dict(A=A,B=B,C=C,D=D,H2=H2,H3=H3,H4=H4,Ms=Ms),
    taylor_remainder_checks=True,simpson_error_bounds=list(map(str,errors)),tail_bounds=list(map(str,tails)),
    integral_enclosures=[[str(a),str(b)] for a,b in intervals],coarse_enclosures=[[str(a),str(b)] for a,b in coarse],
    enclosure_checks=checks,determinant_upper_bound=str(d_upper),required_upper_bound='0',failures=[])
p=Path('scripts/sextic/first-sign-certificate.json'); p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(result='STRICT_NEGATIVE',coarse_enclosures=out['coarse_enclosures'],simpson_error_bounds=out['simpson_error_bounds'],determinant_upper_bound=str(d_upper),required='negative',failures=[],path=str(p)),indent=2))

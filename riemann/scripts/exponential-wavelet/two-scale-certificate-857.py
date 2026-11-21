"""Directed Decimal certificate for one fixed rational rejecting pair.
Numerical full blocks select the pair only. This file encloses full Q
on that pair, including all delays, analytic quadrature error and tail.
See canonical C998 for definitions and bounds. No parameter sweep.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
import hashlib
import json

LO = Context(prec=60, rounding=ROUND_FLOOR)
HI = Context(prec=60, rounding=ROUND_CEILING)


class I:
    def __init__(self, lo=0, hi=None):
        if isinstance(lo, I):
            self.lo, self.hi = lo.lo, lo.hi
        else:
            self.lo = D(lo)
            self.hi = self.lo if hi is None else D(hi)

    def __add__(a, b):
        b = I(b)
        return I(LO.add(a.lo, b.lo), HI.add(a.hi, b.hi))

    __radd__ = __add__

    def __neg__(a):
        return I(a.hi.copy_negate(), a.lo.copy_negate())

    def __sub__(a, b):
        return a + (-I(b))

    def __rsub__(a, b):
        return I(b) - a

    def __mul__(a, b):
        b = I(b)
        ends = [(x, y) for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return I(min(LO.multiply(x, y) for x, y in ends),
                 max(HI.multiply(x, y) for x, y in ends))

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = I(b)
        if b.lo <= 0 <= b.hi:
            raise ArithmeticError('division interval contains zero')
        return a * I(LO.divide(D(1), b.hi), HI.divide(D(1), b.lo))

    def __rtruediv__(a, b):
        return I(b) / a

    def __pow__(a, n):
        if n < 0:
            return I(1) / a**(-n)
        result = I(1)
        while n:
            if n & 1:
                result *= a
            a *= a
            n //= 2
        return result

    def ln(a):
        return I(LO.next_minus(LO.ln(a.lo)), HI.next_plus(HI.ln(a.hi)))

    def exp(a):
        return I(LO.next_minus(LO.exp(a.lo)), HI.next_plus(HI.exp(a.hi)))

    def sqrt(a):
        return I(LO.next_minus(LO.sqrt(a.lo)), HI.next_plus(HI.sqrt(a.hi)))

    def absupper(a):
        return max(a.lo.copy_abs(), a.hi.copy_abs())

    def save(a):
        return [str(a.lo), str(a.hi)]


def pm(a, e):
    r = I(e).absupper()
    return I(LO.subtract(a.lo, r), HI.add(a.hi, r))


def atan_recip(k):
    z = I(1) / k
    val, power = I(0), z
    for j in range(60):
        val += (-1)**j * power / (2*j+1)
        power *= z*z
    return pm(val, power/121)


PI = 16*atan_recip(5)-4*atan_recip(239)


def sincos_turns(turns):
    center = LO.divide(LO.add(turns.lo, turns.hi), D(2))
    shift = int(center.to_integral_value(rounding=ROUND_HALF_EVEN))
    x = 2*PI*(turns-shift)
    if x.absupper() >= 4:
        raise ArithmeticError('argument reduction bound failed')
    x2 = x*x
    st, ct = x, I(1)
    ss, cc = st, ct
    for k in range(1,60):
        st = -st*x2/((2*k)*(2*k+1))
        ct = -ct*x2/((2*k-1)*(2*k))
        ss += st
        cc += ct
    se, ce = st*x2/(120*121), ct*x2/(119*120)
    return pm(ss,2*se), pm(cc,2*ce), x, shift


from math import factorial, isqrt
from numpy.polynomial.legendre import leggauss
from decimal import localcontext, ROUND_HALF_EVEN

BASE=Path(__file__).resolve().parent
OUT=BASE/'two-scale-certificate-857.json'
WITNESS=BASE/'witness-857.json'
wit=json.loads(WITNESS.read_text())
ORDER=24
CUTOFF=512
checks=[]
failures=[]
def check(name,ok):
    checks.append({'name':name,'passed':bool(ok)})
    if not ok:failures.append(name)

def trig(x):
    # Integer reduction is only a choice: the interval includes exact x-2*pi*k.
    with localcontext(HI):
        k=int(((x.lo+x.hi)/(2*(PI.lo+PI.hi))).to_integral_value(rounding=ROUND_HALF_EVEN))
    y=x-2*PI*k
    assert y.absupper()<4
    y2=y*y
    ss=st=y;cc=ct=I(1)
    for j in range(1,44):
        st=-st*y2/((2*j)*(2*j+1));ct=-ct*y2/((2*j-1)*(2*j))
        ss+=st;cc+=ct
    # Absolute omitted-series tails; subsequent term ratios <1/2.
    return pm(ss,2*st*y2/(88*89)),pm(cc,2*ct*y2/(87*88))

def legendre(x):
    p0,p1=I(1),x
    for k in range(2,ORDER+1):p0,p1=p1,((2*k-1)*x*p1-(k-1)*p0)/k
    return p1,ORDER*(x*p1-p0)/(x*x-1)

nodes=[];weights=[];rootrows=[]
for seed in leggauss(ORDER)[0]:
    center=D(str(float(seed)));lo=LO.subtract(center,D('1e-12'));hi=HI.add(center,D('1e-12'))
    pl=legendre(I(lo))[0];ph=legendre(I(hi))[0]
    sl=1 if pl.lo>0 else -1 if pl.hi<0 else 0
    sh=1 if ph.lo>0 else -1 if ph.hi<0 else 0
    assert sl*sh==-1
    for _ in range(100):
        mid=LO.divide(LO.add(lo,hi),D(2));p=legendre(I(mid))[0]
        sm=1 if p.lo>0 else -1 if p.hi<0 else 0
        assert sm
        if sm==sl:lo=mid
        else:hi=mid
    x=I(lo,hi);dp=legendre(x)[1]
    w=2/((1-x*x)*dp*dp)
    nodes.append(x);weights.append(w)
    rootrows.append({'root':x.save(),'P_lower':legendre(I(lo))[0].save(),'P_upper':legendre(I(hi))[0].save(),'weight':w.save()})
check('24 disjoint sign-changing Legendre brackets',all(nodes[j].hi<nodes[j+1].lo for j in range(23)))
check('all quadrature weights positive',all(w.lo>0 for w in weights))

T0=I(3).ln()/16
L=4*I(3).ln()

def convolution_fundamental(t,a):
    # inverse Laplace (s^2-a^2)^-4, truncated after m=15, positive tail
    if t==0:return I(0)
    term=I(t)**7/factorial(7);total=term
    for m in range(1,16):
        term=term*(m+3)/m*a*a*t*t/((2*m+6)*(2*m+7))
        total+=term
    nxt=term*19/16*a*a*t*t/(38*39)
    # On t<=7,a<=.04, all subsequent ratios are <1/2.
    return total+I(0,(2*nxt).hi)

def polyconv(a,b):
    out=[I(0) for _ in range(len(a)+len(b)-1)]
    for j,x in enumerate(a):
        for k,y in enumerate(b):out[j+k]+=x*y
    return out

def construction(T,coeff):
    a=T/2;ch=(a.exp()+(-a).exp())/2
    check('positive a below0.04 '+str(len(coeff)),0<a.lo and a.hi<D('0.04'))
    numerator=[I(1)]
    for _ in range(4):numerator=polyconv(numerator,[I(1),-2*ch,I(1)])
    R=[]
    for k in range(4):
        y=k+4
        R.append(sum((numerator[j]*convolution_fundamental(y-j,a) for j in range(y+1)),I(0)))
    auto=[x/R[0] for x in R]
    check('positive spline autocorrelation norm '+str(len(coeff)),R[0].lo>0)
    check('positive extreme autocorrelation '+str(len(coeff)),auto[3].lo>0)
    coeff=[I(int(x))/int(wit['denominator']) for x in coeff]
    assert all(coeff[j].save()==coeff[-1-j].save() for j in range(len(coeff)))
    l1=sum((I(x.absupper()) for x in coeff),I(0))
    amax=auto[0]+2*sum(auto[1:],I(0))
    hsum=(2+2*ch)**2
    norm1=T*T.exp()*hsum*amax*l1
    check('pair L1 majorant below100 '+str(len(coeff)),norm1.hi<100)
    tailC=16*(ch+1)**4*amax*l1/T**3
    return {'T':T,'a':a,'ch':ch,'auto':auto,'R':R,'coeff':coeff,'l1':l1,'amax':amax,'norm1':norm1,'tailC':tailC}

cs=[construction(T0,wit['coarse_integer_coefficients']),construction(T0/2,wit['fine_integer_coefficients'])]
pp=[]
for p in range(2,81):
    if any(p%d==0 for d in range(2,isqrt(p)+1)):continue
    n=p
    while n<81:
        pp.append((n,p,I(p).ln()/I(n).sqrt(),I(n).ln()));n*=p
pp.sort()
Cprime=2*sum((row[2] for row in pp),I(0))
check('all active delays below L',all(row[3].hi<L.lo for row in pp))
check('81 is endpoint', (I(81).ln()-L).absupper()<D('1e-55'))
check('prime norm bound below100',Cprime.hi<100)
check('e^L below82',L.exp().hi<82)


def symbol(t):
    # Re digamma at .25+it/2 via recurrence to20.25 and DLMF5.11.
    x=I(81)/4;y=t/2;den=x*x+y*y
    val=den.ln()/2-x/(2*den)
    for k in range(20):
        xx=I(k)+I(1)/4
        val-=xx/(xx*xx+y*y)
    return pm(val-PI.ln(),I(2).sqrt()/(6*den))

# Exactly L744's imported first-order remainder, no higher expansion.
digerr=I(2).sqrt()/(6*(I(81)/4)**2)
check('DLMF first-order digamma remainder below0.001',digerr.hi<D('0.001'))


def wavevalue(c,t):
    z=c['T']*t;sn,cz=trig(z)
    c2=2*cz*cz-1;c3=2*c2*cz-cz
    aa=c['auto'];alt=aa[0]-2*aa[1]*cz+2*aa[2]*c2-2*aa[3]*c3
    # Palindromic coefficients: the two physical centers are both L/2.
    half=c['coeff'][:len(c['coeff'])//2]
    odd=[cz]
    if len(half)>1:odd.append(c3)
    for _ in range(2,len(half)):odd.append(2*c2*odd[-1]-odd[-2])
    train=2*sum((q*r for q,r in zip(half,reversed(odd))),I(0))
    amplitude=-16*c['T']*(c['ch']-cz)**4/(c['a']**2+z*z)**2*alt
    return amplitude*train

# Exact rational panel endpoints; real disk radii1/4 on[0,2],1 on[2,512].
panels=[(I(j)/8,I(j+1)/8) for j in range(16)]
panels += [(I(j),I(j+1)) for j in range(2,CUTOFF)]
sums=[I(0),I(0),I(0)]
rows=[]
# Per-node arithmetic rotations, restarted every16 integer panels.
rot={};steps=[trig(row[3]) for row in pp]
for panel,(left,right) in enumerate(panels):
    mid=(left+right)/2;half=(right-left)/2
    vals=[I(0),I(0),I(0)]
    low=panel<16
    restart=low or (panel-16)%16==0
    for node,(x,w) in enumerate(zip(nodes,weights)):
        t=mid+half*x
        m=symbol(t)
        for k,(n,p,weight,delay) in enumerate(pp):
            key=(node,k)
            if restart:
                ss,cc=trig(t*delay)
            else:
                os,oc=rot[key];ds,dc=steps[k]
                ss,cc=os*dc+oc*ds,oc*dc-os*ds
            rot[key]=(ss,cc)
            m-=2*weight*cc
        u,v=wavevalue(cs[0],t),wavevalue(cs[1],t)
        for j,value in enumerate([u*u,v*v,u*v]):vals[j]+=w*m*value*half
    sums=[x+y for x,y in zip(sums,vals)]
    rows.append({'left':left.save(),'right':right.save(),'quadrature': [v.save() for v in vals]})
    if panel%32==0:print('panels',panel,'of',len(panels),flush=True)

# Uniform holomorphic integrand bound on the disks: pair L1<100,
# exp(2rL)<82^2, |m_hol|<100+log(2R+10), arithmetic<100*82.
M=I(10000)*82**2*(100+I(2*CUTOFF+10).ln()+100*82)
check('holomorphic integrand bound below1e14',M.hi<D('1e14'))
Cgauss=I(factorial(ORDER)**4)/((2*ORDER+1)*factorial(2*ORDER)**2)
quaderr=I(CUTOFF)*M*Cgauss
A=2+8*I(2).sqrt()/3+(4*PI).ln()
tailbase=(A+Cprime+I(3*CUTOFF).ln())/(7*I(CUTOFF)**7)+I(1)/(49*I(CUTOFF)**7)
tails=[cs[0]['tailC']**2*tailbase,cs[1]['tailC']**2*tailbase,cs[0]['tailC']*cs[1]['tailC']*tailbase]
results=[pm(s,quaderr+tail)/PI for s,tail in zip(sums,tails)]
qu,qv,h=results
delta=4*h*h-qu*qv
check('Q(u)>0',qu.lo>0);check('Q(v)>0',qv.lo>0)
check('reject strict half:4H^2-Q(u)Q(v)>0',delta.lo>0)
ratio=I(h.lo if h.lo>0 else -h.hi,h.hi if h.lo>0 else -h.lo)/(qu*qv).sqrt()
report={'status':'CERTIFIED REJECTING PAIR' if not failures else 'FAILED CERTIFICATE','parameters':{'order':ORDER,'cutoff_t':CUTOFF,'panels':len(panels),'pair_denominator':wit['denominator'],'source_origin':0,'coarse_indices':[5,28],'fine_indices':[5,60]},'quadrature_roots':rootrows,'construction':[{'T':c['T'].save(),'a':c['a'].save(),'cosh':c['ch'].save(),'autocorrelations':[a.save() for a in c['auto']],'raw_correlations':[a.save() for a in c['R']],'pair_l1':c['l1'].save(),'function_L1_upper':c['norm1'].save(),'Fourier_tail_C':c['tailC'].save()} for c in cs],'prime_powers':[{'n':n,'p':p,'weight':w.save(),'delay':d.save()} for n,p,w,d in pp],'Cprime':Cprime.save(),'digamma_error_bound':digerr.save(),'holomorphic_integrand_bound':M.save(),'gauss_error':quaderr.save(),'panels':rows,'quadrature_sums':[s.save() for s in sums],'tails_before_pi':[e.save() for e in tails],'Q_u':qu.save(),'Q_v':qv.save(),'H_uv':h.save(),'four_H_squared_minus_Q_product':delta.save(),'ratio':ratio.save(),'required':'positive pair Q values and ratio>=1/2','checks':checks,'failures':failures,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'witness_sha256':hashlib.sha256(WITNESS.read_bytes()).hexdigest()}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'Q_u':report['Q_u'],'Q_v':report['Q_v'],'H_uv':report['H_uv'],'ratio':report['ratio'],'required':report['required'],'gauss_error':report['gauss_error'],'tails_before_pi':report['tails_before_pi'],'failures':failures,'path':str(OUT)},indent=2),flush=True)

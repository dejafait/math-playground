"""Two-sine normalized primitive full-Q certificate; see C759f.
Interval primitives reused from audited C759d/e; all new tails paid here.
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
    shift = int(center.to_integral_value())
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


class Z:
    def __init__(self, r=0, i=0):
        if isinstance(r, Z):
            self.r, self.i = r.r, r.i
        else:
            self.r, self.i = I(r), I(i)
    def __add__(a,b):
        b=Z(b); return Z(a.r+b.r,a.i+b.i)
    __radd__=__add__
    def __neg__(a): return Z(-a.r,-a.i)
    def __sub__(a,b): return a+-Z(b)
    def __mul__(a,b):
        b=Z(b);return Z(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)
    __rmul__=__mul__
    def __truediv__(a,b):
        b=Z(b);d=b.r*b.r+b.i*b.i
        return Z((a.r*b.r+a.i*b.i)/d,(a.i*b.r-a.r*b.i)/d)
    def save(a):return {'real':a.r.save(),'imag':a.i.save()}


def correlation(c):
    out={k:[Z(),Z()] for k in range(-2,3)}
    def add(k,u=0,v=0):
        out[k][0]+=u;out[k][1]+=v
    for a,ca in c.items():
        for b,cb in c.items():
            z=ca*cb
            if a+b==0:
                add(a,2*z,-z)
            else:
                z=z*((-1)**(a+b))/Z(0,(a+b)*PI)
                add(-b,z);add(a,-z)
    return out


def cross(ci,cj):
    s={k:ci.get(k,Z())+cj.get(k,Z()) for k in set(ci)|set(cj)}
    r,a,b=correlation(s),correlation(ci),correlation(cj)
    return {k:[(r[k][j]-a[k][j]-b[k][j])/2 for j in (0,1)] for k in r}


def minus_reference(r,h):
    return {k:[r[k][j]-refcorr[k][j]*h for j in (0,1)] for k in r}


def laplace_basis(b):
    E=(-2*b).exp();out=[]
    out.append((Z((1-E)/b), Z((1-E)/(b*b)-2*E/b)))
    for k in (1,2):
        w=k*PI; den=b*b+w*w
        out.append((Z((1-E)*b/den,(1-E)*w/den),
                    Z((1-E)*(b*b-w*w)/(den*den)-2*E*b/den,
                      (1-E)*2*b*w/(den*den)-2*E*w/den)))
    return E,out


def laplace(r,basis):
    val=(r[0][0]*basis[0][0]+r[0][1]*basis[0][1]).r
    for k in (1,2):
        val+=2*(r[k][0]*basis[k][0]+r[k][1]*basis[k][1]).r
    return val


def correlation_at(r,y):
    total=(r[0][0]+r[0][1]*Z(y)).r; rows=[]
    for k in (1,2):
        sn,cs,arg,shift=sincos_turns(k*y/2)
        total+=2*((r[k][0]+r[k][1]*Z(y))*Z(cs,sn)).r
        rows.append({'k':k,'sin':sn.save(),'cos':cs.save(),
                     'argument':arg.save(),'shift':shift})
    return total,rows


def fourier_poles(c):
    out=[]
    for sign in (1,-1):
        z=I(sign)/2;sh=(z.exp()-(-z).exp())/2
        v=Z()
        for k,ck in c.items():
            v+=ck*Z(2*((-1)**k)*sh)/Z(z,k*PI)
        assert v.i.lo<=0<=v.i.hi and v.i.absupper()<D('1e-50')
        out.append(v.r)
    return out

s1={1:Z(0,'-0.5'),-1:Z(0,'0.5')}
s2={2:Z(0,'-0.5'),-2:Z(0,'0.5')}
g1={0:Z(-1),1:Z('-0.5'),-1:Z('-0.5')}
g2={0:Z('0.5'),2:Z('-0.25'),-2:Z('-0.25')}
refcorr=correlation(s1)
# h is exact L2 metric entry, d is ||u'||*||v'|| divided by pi^2.
pairs=[('A12',s1,s2,I(0),I(2)),('A22',s2,s2,I(1),I(4)),
       ('B11',g1,g1,I(3),I(1)),('B12',g1,g2,I(-1),I(1)),
       ('B22',g2,g2,I('0.75'),I(1))]
rel={name:minus_reference(cross(ci,cj),h) for name,ci,cj,h,d in pairs}
K=8192
partials={name:I(0) for name,*_ in pairs}
terms=[]
for j in range(K):
    b=I(2*j)+I('0.5');E,basis=laplace_basis(b)
    row={'j':j,'b':b.save(),'exp_minus_2b':E.save(),'relative_laplace':{}}
    for name,*_ in pairs:
        v=laplace(rel[name],basis);partials[name]+=v
        row['relative_laplace'][name]=v.save()
    terms.append(row)
B=I(2*K)+I('0.5');R3=B**(-3)+B**(-2)/4
fp=fourier_poles(s1);pole_ref=2*fp[0]*fp[1]
entries={};details={}
for name,ci,cj,h,d in pairs:
    radius=2*(d+I(h.absupper()))*PI*PI*R3
    arch=pm(-2*partials[name],radius)
    fi,fj=fourier_poles(ci),fourier_poles(cj)
    pole=fi[0]*fj[1]+fj[0]*fi[1]-h*pole_ref
    prime=I(0);prime_rows=[]
    for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
        delay=I(n).ln();cv,trig=correlation_at(rel[name],delay)
        weight=I(p).ln()/I(n).sqrt();v=-2*weight*cv;prime+=v
        prime_rows.append({'n':n,'p':p,'delay':delay.save(),'relative_correlation':cv.save(),
                           'trigonometry':trig,'weight':weight.save(),'term':v.save()})
    entry=arch+pole+prime;entries[name]=entry
    details[name]={'metric':h.save(),'derivative_product_over_pi2':d.save(),
                   'relative_correlation_coefficients':{str(k):[z.save() for z in v] for k,v in rel[name].items()},
                   'partial_laplace_sum':partials[name].save(),'arch_tail_radius':radius.save(),
                   'archimedean':arch.save(),'poles_i':[z.save() for z in fi],
                   'poles_j':[z.save() for z in fj],'relative_pole':pole.save(),
                   'primes':prime_rows,'relative_prime':prime.save(),'entry':entry.save()}
A12,A22,B11,B12,B22=(entries[k] for k in ['A12','A22','B11','B12','B22'])
# q(t) = B(t)*(1+t^2)-A(t)*(3-2t+3t^2/4).
q=[B11,2*B12-6*A12,B11+B22+4*A12-3*A22,
   2*B12-I('1.5')*A12+2*A22,B22-I('0.75')*A22]
from math import comb
center=I('0.43')
a=[sum((-q[k])*comb(k,j)*center**(k-j) for k in range(j,5)) for j in range(5)]
# a4*u^4+a3*u^3+a2*u^2 >= (a2-a3^2/(4*a4))*u^2.
curvature=a[2]-a[3]*a[3]/(4*a[4])
floor=a[0]-a[1]*a[1]/(4*curvature)
checks={
 'complete_prime_powers':I(7).ln().hi<2<I(8).ln().lo,
 'metric_positive_definite':(I(3)*I('0.75')-1).lo>0,
 'quartic_leading_positive':a[4].lo>0,
 'square_completion_curvature_positive':curvature.lo>0,
 'whole_real_line_floor_positive':floor.lo>D('0.000009'),
 'first_sine_eligible':D('0.00364123566126519')<(I(1)/250).lo,
 'relative_tail_radii_paid':all(D(v['arch_tail_radius'][1])<D('0.0000001') for v in details.values()),
}
failures=[k for k,v in checks.items() if not v]
cert={'kind':'complete two-sine normalized primitive certificate, REPRODUCTION; not independently audited',
 'parameters':{'K':K,'precision':60,'half_width':1,'energy_cap':'1/250','center':'43/100'},
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'constants':{'pi':PI.save(),'pole_reference':pole_ref.save()},
 'analytic_tail':{'B':B.save(),'R3':R3.save(),'bound':'2*(derivative_product+abs(metric)*pi^2)*R3'},
 'series_terms':terms,'entries':details,
 'result':{'defect_numerator_coefficients':[x.save() for x in q],
           'negative_numerator_centered_coefficients':[x.save() for x in a],
           'square_completion_curvature':curvature.save(),'square_completion_floor':floor.save(),
           'required_floor':0,'sign':'strictly negative normalized defect for every nonzero real two-sine vector' if not failures else 'unresolved'},
 'checks':checks,'failures':failures}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(cert,indent=2)+'\n')
for name in entries:print(name,entries[name].save())
print('Square completion curvature:',curvature.save())
print('Floor:',floor.save(),'; required >0; certificate target >0.000009')
print('Checks:',len(checks),'Failures:',failures,'Full certificate:',out)
if failures:raise SystemExit(1)

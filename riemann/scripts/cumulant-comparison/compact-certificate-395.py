#!/usr/bin/env python3
"""Bounded certificate attempt for the fixed r=3,m=5 comparison.

Analytic justifications and limitations must accompany the output.
This file does not import or execute the earlier certificate scripts.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN

PREC = 55
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
NEAR = Context(prec=PREC, rounding=ROUND_HALF_EVEN)


class Ball:
    """Decimal intervals; directed arithmetic, outward transcendental bounds."""
    def __init__(self, lo, hi=None):
        self.lo, self.hi = D(lo), D(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, b):
        if not isinstance(b, Ball): b = Ball(b)
        return Ball(DOWN.add(self.lo,b.lo),UP.add(self.hi,b.hi))
    __radd__ = __add__
    def __neg__(self): return Ball(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self, b): return self + -asball(b)
    def __rsub__(self, b): return asball(b) + -self
    def __mul__(self, b):
        if not isinstance(b, Ball): b = Ball(b)
        if self.lo >= 0 and b.lo >= 0:
            return Ball(DOWN.multiply(self.lo,b.lo),UP.multiply(self.hi,b.hi))
        if self.hi <= 0 and b.hi <= 0:
            return Ball(DOWN.multiply(self.hi,b.hi),UP.multiply(self.lo,b.lo))
        if self.lo >= 0 and b.hi <= 0:
            return Ball(DOWN.multiply(self.hi,b.lo),UP.multiply(self.lo,b.hi))
        if self.hi <= 0 and b.lo >= 0:
            return Ball(DOWN.multiply(self.lo,b.hi),UP.multiply(self.hi,b.lo))
        pairs=[(self.lo,b.lo),(self.lo,b.hi),(self.hi,b.lo),(self.hi,b.hi)]
        return Ball(min(DOWN.multiply(a,c) for a,c in pairs),
                    max(UP.multiply(a,c) for a,c in pairs))
    __rmul__ = __mul__
    def __truediv__(self, b):
        b=asball(b)
        assert b.lo*b.hi > 0
        return self*Ball(DOWN.divide(D(1),b.hi),UP.divide(D(1),b.lo))
    def __rtruediv__(self, b): return asball(b)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        out=Ball(1)
        for _ in range(n): out=out*self
        return out
    def exp(self):
        return Ball(DOWN.next_minus(NEAR.exp(self.lo)),UP.next_plus(NEAR.exp(self.hi)))
    def log(self):
        assert self.lo>0
        return Ball(DOWN.next_minus(NEAR.ln(self.lo)),UP.next_plus(NEAR.ln(self.hi)))
    def absmax(self): return max(self.lo.copy_abs(),self.hi.copy_abs())
    def encode(self): return dict(lower=str(self.lo),upper=str(self.hi))


def asball(x): return x if isinstance(x,Ball) else Ball(x)


def bconv(a,b,degree):
    out=[Ball(0) for _ in range(min(degree+1,len(a)+len(b)-1))]
    for i,ai in enumerate(a):
        if i>degree: break
        for j,bj in enumerate(b[:degree+1-i]):
            out[i+j]=out[i+j]+ai*bj
    return out


def bhorn(coeffs,t):
    out=Ball(0)
    for v in reversed(coeffs): out=out*t+v
    return out


def badd(a,b,scale=1):
    return [(a[i] if i<len(a) else Ball(0))+
            (scale*b[i] if i<len(b) else Ball(0)) for i in range(max(len(a),len(b)))]


def gradients(d):
    a,b,c,e,f=d
    return [e*e-c*f,2*f*b-2*c*e,3*c*c-a*f-2*b*e,
            2*a*e-2*b*c,b*b-a*c]


def moment_quadrature(x,degree=36,Q=96):
    """Unit panels, Taylor radius 2 and half-width 1/2; q>=Q bounded."""
    x=Ball(x)
    sums=[Ball(0) for _ in range(5)]
    errors=[Ball(0) for _ in range(5)]
    panels=[]
    weights=[Ball(1)/(2**k*(k+1)) if k%2==0 else Ball(0)
             for k in range(degree+1)]
    exp_coeff=[Ball((-1)**k)/factorial(k) for k in range(degree+1)]
    for j in range(Q):
        c=Ball(D(j)+D('0.5'))
        z=x+c
        inv=1/z
        log_coeff=[x*(1+c/x).log()]
        u_coeff=[((1+c/x).log()/4).exp()]
        ip=Ball(1)
        for k in range(1,degree+1):
            ip=ip*inv
            log_coeff.append(x*((-1)**(k+1))*ip/k)
            u_coeff.append(u_coeff[-1]*(Ball('0.25')-k+1)*inv/k)
        v=[1+c/(x-Ball('1.5')),1/(x-Ball('1.5'))]
        common=bconv(bconv(u_coeff,v,degree),exp_coeff,degree)
        common=[(-c).exp()*w for w in common]
        power=[Ball(1)]
        vals=[]
        errs=[]
        for p in range(5):
            poly=bconv(common,power,degree)
            val=sum((poly[k]*weights[k] for k in range(0,degree+1,2)),Ball(0))/factorial(p)
            # Supremum on |q-c|=2, valid uniformly for real x>=3.
            M=(Ball(2)-c).exp()*(c+6)**p/factorial(p)*(c+5)*(2*c+7)/9
            err=M/(4**(degree+1))*Ball(4)/3
            sums[p]=sums[p]+val
            errors[p]=errors[p]+err
            vals.append(val.encode())
            errs.append(err.encode())
            if p<4: power=bconv(power,log_coeff,degree)
        panels.append(dict(q_center=str(c.lo),integrals=vals,remainder_bounds=errs))
    tails=[]
    for p in range(5):
        # H <= (1+q/12)(1+2q/3); L<=q, x>=3.
        def gamma_tail(k):
            return Ball(-Q).exp()*factorial(k)*sum(
                (Ball(Q)**j/factorial(j) for j in range(k+1)),Ball(0))
        tail=(gamma_tail(p)+Ball(3)/4*gamma_tail(p+1)+gamma_tail(p+2)/18)/factorial(p)
        tails.append(tail.encode())
        sums[p]=sums[p]+Ball(errors[p].hi.copy_negate(),errors[p].hi)+Ball(0,tail.hi)
    return sums,dict(degree=degree,Q=Q,panels=panels,tail_bounds=tails,
                     moments=[v.encode() for v in sums])


def cell_certificate(a,degree=64):
    c=D(a)+D('0.5')
    d,quad=moment_quadrature(c)
    assert all(0<v.lo<=v.hi<3 for v in d)
    coeffs=[]
    for p in range(5):
        alpha=[]
        for k in range(degree):
            alpha.append((Ball(1) if k==0 else Ball(0))+((-1)**k)*(
                (Ball(p)-Ball('0.25'))/Ball(c)**(k+1)-1/Ball(c-D('1.5'))**(k+1)))
        b=[d[p]]
        prev=coeffs[-1] if p else [Ball(1)]+[Ball(0)]*degree
        for k in range(degree):
            b.append((sum((alpha[j]*b[k-j] for j in range(k+1)),Ball(0))-prev[k])/(k+1))
        coeffs.append(b)
    # Complex disk radius 1: row-sum <=6, initial sup-norm <3.
    assert (Ball(6).exp()*3).hi<1500
    delta=Ball(3000)/(2**(degree+1))
    t=Ball('-0.5','0.5')
    enclosure=[bhorn(b,t)+Ball(delta.hi.copy_negate(),delta.hi) for b in coeffs]
    assert all(v.lo>0 for v in enclosure)
    # Form the entire signed polynomial before interval evaluation in t.
    A,B,C,E,Ff=coeffs
    def prod3(f,g,h): return bconv(bconv(f,g,2*degree),h,3*degree)
    signed=prod3(A,E,E)
    signed=badd(signed,prod3(C,C,C))
    signed=badd(signed,prod3(Ff,B,B))
    signed=badd(signed,prod3(A,C,Ff),-1)
    signed=badd(signed,prod3(B,C,E),-2)
    sp=bhorn(signed,t)
    err=sum((Ball(g.absmax())*delta for g in gradients(enclosure)),Ball(0))
    sb=sp+Ball(err.hi.copy_negate(),err.hi)
    # All n>=2, first term separated; monotone upper bound at x=a.
    x=Ball(a)
    eta=[]
    for p in range(5):
        rn=(8*x-3)/(2*x-3)
        qcoef=2/(2*x-3)
        factor=rn*(1+Ball(p+1)/(16*x))+qcoef*(p+1)*(1+Ball(p+2)/(16*x))
        eta.append(((-3*x).exp()*factor/(4**p)+80*(-8*x).exp()))
    box=[v+Ball(0,e.hi) for v,e in zip(enclosure,eta)]
    error=sum((Ball(g.absmax())*e for g,e in zip(gradients(box),eta)),Ball(0))
    passed=sb.lo>0 and error.hi<DOWN.divide(sb.lo,D(2))
    ratio=UP.divide(error.hi,sb.lo) if sb.lo>0 else None
    return dict(a=a,b=a+1,center=str(c),quadrature=quad,
        local_taylor_coefficients=[[v.encode() for v in b] for b in coeffs],
        analytic_entry_remainder=delta.encode(),
        moment_enclosures=[v.encode() for v in enclosure],
        signed_polynomial_coefficients=[v.encode() for v in signed],
        signed_polynomial_enclosure=sp.encode(),
        determinant_remainder=err.encode(),signed_base=sb.encode(),
        all_theta_tail_entries=[v.encode() for v in eta],
        determinant_tail_error=error.encode(),relative_upper=str(ratio),passed=passed)


def conv(a, b, degree):
    c = [F(0)] * (degree + 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b[:degree + 1 - i]):
            c[i+j] += ai * bj
    return c


class RatInterval:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, b):
        if not isinstance(b, RatInterval): b = RatInterval(b)
        return RatInterval(self.lo+b.lo, self.hi+b.hi)
    __radd__ = __add__
    def __neg__(self): return RatInterval(-self.hi, -self.lo)
    def __sub__(self, b): return self + -b
    def __mul__(self, b):
        if not isinstance(b, RatInterval): b = RatInterval(b)
        v = [self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi]
        return RatInterval(min(v), max(v))
    __rmul__ = __mul__
    def __pow__(self, n):
        out = RatInterval(1)
        for _ in range(n): out = out*self
        return out
    def encode(self): return dict(lower=str(self.lo), upper=str(self.hi))


def horner(coeffs, e):
    out = RatInterval(0)
    for v in reversed(coeffs): out = out*e+v
    return out


def tail_attempt(X, degree):
    # Terms of L^p: q^(p+k) times the kth coefficient below.
    l = [F((-1)**k, k+1) for k in range(degree+2)]
    lp = [F(1)] + [F(0)]*(degree+1)
    u = [F(1)]
    for k in range(1, degree+2): u.append(u[-1]*(F(1,4)-k+1)/k)
    emax = F(1, X)
    v0 = [F(1), emax/(1-F(3,2)*emax)]
    u0 = [F(1), emax/4]
    coeffs, errors = [], []
    for p in range(5):
        dc = []
        for k in range(degree+1):
            val = F(0)
            for i in range(k+1):
                for j in range(k-i+1):
                    t = k-i-j
                    vc = F(1) if j == 0 else F(3,2)**(j-1)
                    power = p+t+i+(j > 0)
                    val += u[i]*vc*lp[t]*factorial(power)/factorial(p)
            dc.append(val)
        # Uniform normalized derivative of order degree+1.
        k = degree+1
        err = F(0)
        for i in range(k+1):
            up = u0 if i == 0 else [F(0)]*i+[abs(u[i])]
            for j in range(k-i+1):
                t = k-i-j
                vp = v0 if j == 0 else [F(0), F(3,2)**(j-1)/(1-F(3,2)*emax)**(j+1)]
                for a, ua in enumerate(up):
                    for b, vb in enumerate(vp):
                        err += ua*vb*abs(lp[t])*factorial(p+t+a+b)/factorial(p)
        coeffs.append(dc)
        errors.append(err)
        lp = conv(lp, l, degree+1)
    differences = [[sum((-1)**(k-j)*comb(k,j)*coeffs[j][i]
                         for j in range(k+1)) for i in range(degree+1)]
                   for k in range(5)]
    rd = [sum(comb(k,j)*errors[j] for j in range(k+1)) for k in range(5)]
    orders = [0,1,1,2,2]
    e = RatInterval(0, emax)
    vs=[]
    for c, r, order in zip(differences, rd, orders):
        assert all(v == 0 for v in c[:order])
        vs.append(horner(c[order:], e)+RatInterval(-r,r)*e**(degree+1-order))
    v0,v1,v2,v3,v4=vs
    signed=-v0*v2*v4+v2**3+e*(v0*v3**2+v1**2*v4-2*v1*v2*v3)
    relative=F(26664660*factorial(30),3**30*X**27)/signed.lo if signed.lo>0 else None
    result=dict(X=X, degree=degree, signed_times_x_cubed=signed.encode(),
                scaled_entries=[v.encode() for v in vs],
                coefficients=[[str(v) for v in c] for c in coeffs],
                remainders=[str(v) for v in errors],
                relative_upper=str(relative) if relative is not None else None,
                passed=signed.lo>0 and relative is not None and relative<F(1,2))
    if X==32 and degree==20:
        coarse=[RatInterval(F(999,1000),F(1041,1000)),
                RatInterval(F(249,1000),F(263,1000)),
                RatInterval(F(-101,100),F(-999,1000)),
                RatInterval(F(37,10),F(43,10)),
                RatInterval(F(154,100),F(301,100))]
        assert all(b.lo<=v.lo<=v.hi<=b.hi for b,v in zip(coarse,vs))
        lower=F(999,1000)**2*F(154,100)-F(101,100)**3
        upper=F(2*26664660*factorial(30),3**30*32**27)
        assert lower>F(1,2) and upper<F(1,10**14)
        result.update(coarse_scaled_entries=[v.encode() for v in coarse],
                      coarse_signed_lower=str(lower),coarse_relative_upper=str(upper))
    return result


if __name__ == '__main__':
    trials=[]
    for X in [32,64,128]:
        row=tail_attempt(X,20)
        trials.append(row)
        s=F(row['signed_times_x_cubed']['lower'])
        print('Tail:',X,'lower:',float(s),'required >0; relative upper:',
              float(F(row['relative_upper'])) if row['relative_upper'] else 'unavailable',
              'required <0.5; passed:',row['passed'],flush=True)
        if row['passed']: break
    out=Path(__file__).with_suffix('.json')
    result=dict(status='PARTIAL_ATTEMPT',tail_trials=trials,cells=[],
        failures=['Compact domain not yet certified.'])
    out.write_text(json.dumps(result,indent=2)+'\n')
    assert trials[-1]['passed']
    X=trials[-1]['X']
    for a in range(3,X):
        row=cell_certificate(a)
        result['cells'].append(row)
        if a==3 or a%5==0 or not row['passed']:
            print('Compact cell:',a,a+1,'signed lower:',row['signed_base']['lower'],
                  'relative upper:',row['relative_upper'],'passed:',row['passed'],flush=True)
            out.write_text(json.dumps(result,indent=2)+'\n')
        if not row['passed']: break
    complete=len(result['cells'])==X-3 and all(r['passed'] for r in result['cells'])
    assert all(r['a']==3+i and r['b']==4+i for i,r in enumerate(result['cells']))
    if complete:
        minimum=min(DOWN.multiply(D(r['signed_base']['lower']),D(r['a']**3)) for r in result['cells'])
        maximum=max(D(r['relative_upper']) for r in result['cells'])
        assert minimum>D('0.1005239') and maximum<D('0.364211')
        assert D(result['cells'][0]['signed_base']['lower'])>D('0.0037231095')
        assert F(trials[-1]['signed_times_x_cubed']['lower'])>F(1,2)
        assert F(trials[-1]['relative_upper'])<F(1,10**14)
        result['status']='FULL_DOMAIN_INTERVAL_AND_RATIONAL_CERTIFICATE'
        result['failures']=[]
        result['summary']=dict(compact_domain=[3,X],compact_cells=len(result['cells']),
            minimum_compact_lower_times_x_cubed=str(minimum),
            maximum_compact_relative_upper=str(maximum),
            tail_domain=[X,'infinity'],base_required='>0',relative_required='<1/2',
            uniform_base_lower='1/(10*x^3)',uniform_relative_upper='37/100',
            precision_decimal=PREC,all_checks_passed=True,
            limitations=['Analytic derivations require the accompanying proof.',
                        'Independent later-turn audit pending; no all-order or RH conclusion.'])
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('Status:',result['status'])
    if complete: print('Compact rescaled lower:',minimum,'required >0; relative upper:',maximum,'required <0.5.')
    print('Failures:',result['failures'])
    print('Full evidence:',out)

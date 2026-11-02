"""Outward decimal interval enclosure for one continuum saddle contour.

No binary floating-point value enters an accepted bound.  Every basic
Decimal operation is expanded by next_minus/next_plus at precision 42.
Transcendentals use finite series and explicit tails.  This certificate
does not itself prove the finite-product saddle asymptotic.
"""
from decimal import Decimal as D, getcontext
import json
from pathlib import Path

getcontext().prec = 42

class I:
    def __init__(self, lo, hi=None):
        self.lo=D(lo); self.hi=self.lo if hi is None else D(hi)
        assert self.lo<=self.hi
    def __add__(self, other):
        if isinstance(other,C): return NotImplemented
        o=ii(other)
        return I((self.lo+o.lo).next_minus(),(self.hi+o.hi).next_plus())
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other):
        if isinstance(other,C): return NotImplemented
        return self+-ii(other)
    def __rsub__(self,other): return ii(other)+-self
    def __mul__(self,other):
        if isinstance(other,C): return NotImplemented
        o=ii(other); vs=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(min(vs).next_minus(),max(vs).next_plus())
    __rmul__=__mul__
    def inv(self):
        assert self.lo*self.hi>0
        return I((1/self.hi).next_minus(),(1/self.lo).next_plus())
    def __truediv__(self,other):
        if isinstance(other,C): return NotImplemented
        return self*ii(other).inv()
    def __rtruediv__(self,other): return ii(other)*self.inv()
    def __pow__(self,n):
        assert n>=0 and int(n)==n
        out=I(1)
        for _ in range(n): out=out*self
        return out
    def sq(self):
        lo=D(0) if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi).next_minus()
        hi=max(self.lo*self.lo,self.hi*self.hi).next_plus()
        return I(lo,hi)
    def sqrt(self):
        assert self.lo>=0
        return I(self.lo.sqrt().next_minus(),self.hi.sqrt().next_plus())
    def absup(self): return max(abs(self.lo),abs(self.hi))
    def midpoint(self): return (self.lo+self.hi)/2
    def dump(self): return [str(self.lo),str(self.hi)]

def ii(v): return v if isinstance(v,I) else I(v)
def widen(v,e): return v+I(-e,e)

class C:
    def __init__(self,re=0,im=0): self.re=ii(re); self.im=ii(im)
    def __add__(self,other):
        o=cc(other); return C(self.re+o.re,self.im+o.im)
    __radd__=__add__
    def __neg__(self): return C(-self.re,-self.im)
    def __sub__(self,other): return self+-cc(other)
    def __rsub__(self,other): return cc(other)+-self
    def __mul__(self,other):
        o=cc(other)
        return C(self.re*o.re-self.im*o.im,self.re*o.im+self.im*o.re)
    __rmul__=__mul__
    def inv(self):
        norm=self.re.sq()+self.im.sq()
        assert norm.lo>0
        return C(self.re/norm,-self.im/norm)
    def __truediv__(self,other): return self*cc(other).inv()
    def __rtruediv__(self,other): return cc(other)*self.inv()
    def __pow__(self,n):
        out=C(1)
        for _ in range(n): out=out*self
        return out
    def absup(self): return (self.re.sq()+self.im.sq()).hi.sqrt().next_plus()
    def dump(self): return {'re':self.re.dump(),'im':self.im.dump()}

def cc(v): return v if isinstance(v,C) else C(v)

# Machin's formula, with the alternating-series remainder included.
def atan_inv(q,N):
    total=I(0)
    for k in range(N): total+=I((-1)**k)/((2*k+1)*q**(2*k+1))
    return widen(total,(I(1)/((2*N+1)*q**(2*N+1))).hi)
pi=16*atan_inv(5,48)-4*atan_inv(239,16)

def real_trig(t):
    # Exact periodic shift by a multiple of pi/2; the interval pi is retained.
    k=int((t.midpoint()/(pi.midpoint()/2)).to_integral_value())
    y=t-k*pi/2
    assert y.absup()<1
    sin=I(0); cos=I(0); sy=y; cy=I(1)
    for j in range(20):
        sin+=sy; cos+=cy
        sy=-sy*y*y/((2*j+2)*(2*j+3))
        cy=-cy*y*y/((2*j+1)*(2*j+2))
    # Since |y|<1, both omitted factorial tails are < 2/40!.
    fac=1
    for j in range(1,41): fac*=j
    err=(I(2)/fac).hi
    sin=widen(sin,err); cos=widen(cos,err)
    return [(sin,cos),(cos,-sin),(-sin,-cos),(-cos,sin)][k%4]

def hyper(h):
    assert h.absup()<1
    sh=I(0); ch=I(0); sy=h; cy=I(1)
    for j in range(20):
        sh+=sy; ch+=cy
        sy=sy*h*h/((2*j+2)*(2*j+3))
        cy=cy*h*h/((2*j+1)*(2*j+2))
    fac=1
    for j in range(1,41): fac*=j
    err=(I(2)/fac).hi
    return widen(sh,err),widen(ch,err)

def trig(z):
    sn,cs=real_trig(z.re); sh,ch=hyper(z.im)
    return C(sn*ch,cs*sh),C(cs*ch,-sn*sh)

SERIES=120
def log_series(w,j=False):
    # Enclose log(1-w), or J(w), by point series plus a disk Lipschitz bound.
    q=w.absup(); assert q<D('.9')
    center=C(w.re.midpoint(),w.im.midpoint())
    radius=(w-center).absup()
    power=C(1); result=C(0)
    for k in range(1,SERIES+1):
        power=power*center
        result-=power/(k*(k+1) if j else k)
    tail=(I(q)**(SERIES+1)/((SERIES+1)*(1-I(q)))).hi
    if j: tail=(I(tail)/(SERIES+2)).hi
    variation=(I(radius)/((2 if j else 1)*(1-I(q)))).hi
    error=(I(tail)+variation).hi
    return C(widen(result.re,error),widen(result.im,error))

x=I('-1.25'); r=I('.54'); U=I(121)/64
u=C(I('-.831471','-.831468'),I('.555569','.555572'))
z0=C('4.876972288459421','.11410424409610605')
root_radius=D('.0002')
zbox=C(widen(z0.re,root_radius),widen(z0.im,root_radius))
iiunit=C(0,1)

def phase(z,need_value=True):
    sn,cs=trig(z)
    v=C(x)+iiunit*r*cs
    vp=-iiunit*r*sn; vpp=-iiunit*r*cs
    a=U*u
    l1=log_series(v/a); l2=log_series(u/v)
    pv=1/v+a/(v*v)*l1+1/u*l2
    pvv=-1/(v*v)-2*a/(v*v*v)*l1-1/(v*v*(1-v/a))+1/(v*v*(1-u/v))
    hp=pv*vp-C(0,I(2)/3)
    hpp=pvv*vp*vp+pv*vpp
    h=None; p=None
    if need_value:
        p=-log_series(-(v-C(x))/x)+log_series(u/x,True)-log_series(u/v,True)+log_series(v/a,True)-log_series(x/a,True)
        h=p-C(0,I(2)/3)*z
    return h,hp,hpp,p

checks=[]; failures=[]
def check(name,actual,required,rel='<'):
    ok=actual<required if rel=='<' else actual>required
    checks.append(dict(name=name,actual=str(actual),required=str(required),relation=rel,passed=ok))
    if not ok: failures.append(name)

h0,hp0,hpp0,p0=phase(z0)
hb,hpb,hppb,pb=phase(zbox,False)
der_center=C('-.20186986852836578','.17099621992252434')
contraction=(1-hppb/der_center).absup()
displacement=(hp0/der_center).absup()
image_radius=(I(displacement)+I(contraction)*root_radius).hi
check('saddle contraction',contraction,D('.5'))
check('saddle disk maps strictly inside itself',image_radius,root_radius)
saddle_re_lower=(h0.re-I(hpb.absup())*root_radius).lo
check('saddle real phase lower',saddle_re_lower,D('.005'),'>')
snbox,csbox=real_trig(zbox.re)
kappa=-zbox.im/snbox
check('contour height upper',kappa.absup(),D('.117'))
gaussian_a=-hppb*C(1,-kappa*csbox)**2
check('Gaussian real part lower',gaussian_a.re.lo,D('.18'),'>')
check('Gaussian imaginary absolute upper',gaussian_a.im.absup(),D('.20'))
check('Gaussian real part upper',gaussian_a.re.hi,D('.22'))

def curve(t,need_value=True):
    sn,cs=real_trig(t)
    z=C(t,-kappa*sn)
    zp=C(1,-kappa*cs); zpp=C(0,kappa*sn)
    h,hp,hpp,p=phase(z,need_value)
    return h,hp*zp,hpp*zp*zp+hp*zpp,p

# Certify curvature on a full interval containing the excluded global cells.
local_rows=[]
NLOCAL=32
for j in range(NLOCAL):
    t=z0.re+I('-.21')+I('.42')*I(j,j+1)/NLOCAL
    _,_,dd,_=curve(t,False)
    local_rows.append(dict(t=t.dump(),real_second_upper=str(dd.re.hi)))
curvature=max(D(row['real_second_upper']) for row in local_rows)
check('local real curvature upper',curvature,D('-.05'))

# Point phase plus an interval derivative covers every t cell continuously.
rows=[]; N=1024
for j in range(N):
    t=2*pi*I(j,j+1)/N
    mid=I(t.midpoint()); half=(t-mid).absup()
    h,_,_,p=curve(mid)
    _,der,_,_=curve(t,False)
    hu=(h.re+I(der.re.absup())*half).hi
    # P'=H'+2i*z'/3; Re P'=Re H'+(2/3)kappa*cos(t).
    _,cs=real_trig(t)
    pder=der.re+I(2)/3*kappa*cs
    pu=(p.re+I(pder.absup())*half).hi
    outside=(t.hi<=z0.re.lo-D('.2') or t.lo>=z0.re.hi+D('.2'))
    rows.append(dict(j=j,t=t.dump(),alias_real_upper=str(hu),b0_real_upper=str(pu),outside=outside))
    if j%128==0: print('enclosed contour cells',j,'/',N,flush=True)
global_upper=max(D(row['alias_real_upper']) for row in rows if row['outside'])
b0_upper=max(D(row['b0_real_upper']) for row in rows)
check('complementary contour real phase upper',global_upper,D('.004'))
check('b0 real phase upper',b0_upper,D('-.06'))

# Every non-outside cell lies in the region with certified curvature.
inside=[row for row in rows if not row['outside']]
check('left overlap',D(inside[0]['t'][0]),z0.re.lo-D('.21'),'>')
check('right overlap',D(inside[-1]['t'][1]),z0.re.hi+D('.21'))

out=Path(__file__).with_suffix('.json')
summary=dict(passed=not failures,root_radius=str(root_radius),contraction_upper=str(contraction),
             displacement_upper=str(displacement),image_radius_upper=str(image_radius),
             saddle_real_lower=str(saddle_re_lower),kappa=kappa.dump(),
             gaussian_a=gaussian_a.dump(),
             curvature_upper=str(curvature),complementary_phase_upper=str(global_upper),
             b0_phase_upper=str(b0_upper),cells=N,local_cells=NLOCAL)
out.write_text(json.dumps(dict(status='OUTWARD_DECIMAL_SERIES_CERTIFICATE',precision=42,
                              summary=summary,checks=checks,failures=failures,
                              pi=pi.dump(),saddle_h0=h0.dump(),saddle_hp0=hp0.dump(),
                              saddle_hpp_box=hppb.dump(),local_cells=local_rows,cells=rows),indent=2)+'\n')
print('Saddle/contour certificate:', 'PASS' if not failures else 'FAIL')
for ch in checks: print(ch)
print('Failures:',failures)
print('Full certificate:',out)

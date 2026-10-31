"""Exact arithmetic for the single approved degree-eight model."""
from fractions import Fraction as F
from pathlib import Path
import json

class QI:
    def __init__(self, r=0, i=0): self.r,self.i=F(r),F(i)
    def __add__(self,o):
        o=qi(o); return QI(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return QI(-self.r,-self.i)
    def __sub__(self,o): return self+-qi(o)
    def __rsub__(self,o): return qi(o)+-self
    def __mul__(self,o):
        o=qi(o); return QI(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=qi(o); n=o.r**2+o.i**2
        return self*QI(o.r/n,-o.i/n)
    def __rtruediv__(self,o): return qi(o)/self
    def __repr__(self): return f'({self.r})+i({self.i})'
    def approx(self): return complex(float(self.r),float(self.i))
def qi(o): return o if isinstance(o,QI) else QI(o)
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for j,a in enumerate(p):
        for k,b in enumerate(q): r[j+k]+=a*b
    return r
def der(p): return [j*p[j] for j in range(1,len(p))]
def ev(p,z):
    v=0
    for a in reversed(p): v=v*z+a
    return v
P=mul(mul([F(1),0,F(-1)],[F(1),0,F(-1,4)]),[F(1),0,F(-51168,2563201),0,F(256,2563201)])
dP=der(P); ddP=der(dP)
A=-1/ev(dP,F(1)); B=-1/ev(dP,F(2))
a=QI(10,F(1,4)); c=-1/ev(dP,a)
# p(x)=A exp(-x)+B exp(-2x)+exp(-10x)(C cos(x/4)+D sin(x/4)) for x>=0.
C=2*c.r; D=2*c.i
jet=ev(dP,F(10))**2-ev(P,F(10))*ev(ddP,F(10))
if __name__=='__main__':
    print('A,B,C,D:',A,B,C,D)
    print('approx:',*[float(v) for v in (A,B,C,D)])
    print('jet:',jet,float(jet))
    for k in range(4):
        v=A*(-1)**k+B*(-2)**k+2*(c*ev([0]*k+[1],-a)).r
        print('right derivative at zero',k,':',v,float(v))

# Complete certificate: exact algebra and rational bounds, without grids.
def add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for j,v in enumerate(p): r[j]+=v
    for j,v in enumerate(q): r[j]+=v
    return r
def scale(p,c): return [c*v for v in p]
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def certify():
    a2=a*a; mod_a2=a2.r*a2.r+a2.i*a2.i
    d1=[F(1),0,F(-1)]; d2=[F(4),0,F(-1)]
    dc=[mod_a2,0,-2*a2.r,0,F(1)]
    ac=a*c
    nc=[4*(ac*QI(a2.r,-a2.i)).r,0,-4*ac.r]
    numerator=add(add(scale(mul(d2,dc),2*A),scale(mul(d1,dc),4*B)),mul(nc,mul(d1,d2)))
    assert trim(numerator)==[4*mod_a2]
    assert mul(mul(d1,d2),dc)==scale(P,4*mod_a2)
    u=-2*A*c*(a-1)*(a-1); v=-2*B*c*(a-2)*(a-2)
    b=-A*B; k=(c.r*c.r+c.i*c.i)/4
    # Imaginary conjugate residues produce C cos+D sin with these signs.
    derivatives=[A*(-1)**j+B*(-2)**j+2*(c*ev([0]*j+[1],-a)).r for j in range(4)]
    positivity=A+B-C-D
    near=b+u.r
    monotonic_margin=8*(-u.r)-(-u.i)/4
    far=b-(-u.r-u.i)/256-(v.r+v.i)/512
    assert A>0 and B<0 and C>0 and D>0
    assert b>0 and k>0 and u.r<0 and u.i<0 and v.r>0 and v.i>0
    assert positivity>0 and near>0 and far>0 and monotonic_margin>=0
    assert derivatives[1]==derivatives[3]==0
    assert jet<0
    data={
      'target':'exactly the approved degree-eight polynomial; no parameter search',
      'polynomial_coefficients_ascending':[str(v) for v in P],
      'density_coefficients':{n:str(v) for n,v in zip(['A','B','C','D'],[A,B,C,D])},
      'transform_identity':{'common_denominator_coefficients':list(map(str,mul(mul(d1,d2),dc))),
                            'summed_numerator_coefficients':list(map(str,numerator)),
                            'required_constant':str(4*mod_a2),'pass':True},
      'right_derivatives_at_zero':list(map(str,derivatives)),
      'curvature_coefficients':{n:str(w) for n,w in zip(['b','u_r','u_i','v_r','v_i','k'],[b,u.r,u.i,v.r,v.i,k])},
      'global_bounds':{
        'density_scaled_lower':str(positivity),
        'curvature_scaled_near_lower':str(near),
        'near_envelope_derivative_margin':str(monotonic_margin),
        'curvature_scaled_far_lower':str(far),
        'required_lower_bound':'0',
        'near_interval':'0<=x<=1',
        'far_interval':'x>=1',
        'tail_inequalities':'e>2 implies exp(-8x)<1/256 and exp(-9x)<1/512 for x>=1',
        'all_pass':True},
      'polynomial_jet':{'P_10':str(ev(P,F(10))),'Pprime_10':str(ev(dP,F(10))),
                        'Psecond_10':str(ev(ddP,F(10))),'first_laguerre_10':str(jet),
                        'required':'strictly negative','pass':True},
      'failures':[],
      'qualifications':['No actual-Xi claim','No PF256 certification','No novelty certification','Informal proof; not formally verified']}
    out=Path(__file__).with_name('fixed-model-certificate.json')
    out.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS: rational transform identity, zero matching, positivity and curvature bounds; failures: 0')
    for name,val in [('density lower',positivity),('curvature near lower',near),('curvature far lower',far)]:
        print(f'{name}: {float(val):.12g} > required 0 (exact values in certificate)')
    print(f'jet: {float(jet):.12g} < required 0 (exact value in certificate)')
    print('certificate:',out)

if __name__=='__main__': certify()

"""Fixed-cap real interval census. Proof of tails: L815. Python stdlib only."""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from math import factorial
import json, platform, time, decimal, hashlib
from pathlib import Path
lo=Context(prec=50,rounding=ROUND_FLOOR); hi=Context(prec=50,rounding=ROUND_CEILING)
near=Context(prec=50,rounding=ROUND_HALF_EVEN)
class I:
 def __init__(self,a,b=None):
  self.a=D(a); self.b=D(a if b is None else b)
 def __add__(self,o):
  o=cv(o); return I(lo.add(self.a,o.a),hi.add(self.b,o.b))
 __radd__=__add__
 def __neg__(self): return I(self.b.copy_negate(),self.a.copy_negate())
 def __sub__(self,o): return self+-cv(o)
 def __rsub__(self,o): return cv(o)+-self
 def __mul__(self,o):
  o=cv(o); return I(min(lo.multiply(a,b) for a in [self.a,self.b] for b in [o.a,o.b]),max(hi.multiply(a,b) for a in [self.a,self.b] for b in [o.a,o.b]))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=cv(o)
  if o.a<=0<=o.b: raise ValueError('zero denominator')
  return self*I(lo.divide(D(1),o.b),hi.divide(D(1),o.a))
 def __pow__(self,n):
  if n==0:return I(1)
  if n%2==0:
   return I(0 if self.a<=0<=self.b else min(lo.power(self.a,n),lo.power(self.b,n)),max(hi.power(self.a,n),hi.power(self.b,n)))
  return I(lo.power(self.a,n),hi.power(self.b,n))
 def exp(self):return I(near.exp(self.a).next_minus(near),near.exp(self.b).next_plus(near))
 def data(self):return [str(self.a),str(self.b)]
def cv(x):return x if isinstance(x,I) else I(x)
def sym(e):return I(e.b.copy_negate(),e.b)
def atan(q):
 z=I(1)/q; s=I(0)
 for k in range(120):s=s+((-1)**k)*(z**(2*k+1))/(2*k+1)
 return s+sym(z**241/241)
pi=16*atan(5)-4*atan(239)
def trig(t):
 mid=near.divide(near.add(t.a,t.b),D(2)); r=max(hi.subtract(mid,t.a),hi.subtract(t.b,mid))
 z=I(mid)/256; z2=z*z; c=I(1); s=z; tc=I(1); ts=z
 for k in range(1,17):
  tc=-tc*z2/((2*k-1)*(2*k)); ts=-ts*z2/((2*k)*(2*k+1))
  c=c+tc; s=s+ts
 err=I(1)/factorial(34); c=c+sym(err);s=s+sym(err)
 for _ in range(8):s,c=2*s*c,c*c-s*s
 return c+I(r.copy_negate(),r),s+I(r.copy_negate(),r)
def kernel(u):
 e2=(2*u).exp(); e45=(I('4.5')*u).exp();e25=(I('2.5')*u).exp()
 k=I(0)
 for n in range(1,5):k=k+(8*pi*pi*n**4*e45-12*pi*n*n*e25)*(-pi*n*n*e2).exp()
 def cosh(v):return (v.exp()+(-v).exp())/2
 q=8*pi*(2*pi*cosh(I('4.5')*u)-3*cosh(I('2.5')*u))*(-2*pi*cosh(2*u)).exp()
 return k,q
start=time.monotonic(); M=1024; cells=80; du=I(3)/M
# All real u-series and improper-integral tails, uniform in real x.
ntail=27*16*pi*pi*(I('13.5').exp())*625*(-25*pi).exp()
utail=16*pi*I('13.5').exp()*(-pi*I(6).exp()).exp()
errors=[ntail+utail]*3
bins=[]
for k in range(M):
 u=I(lo.divide(D(3*k),D(M)),hi.divide(D(3*(k+1)),D(M)))
 a,b=kernel(u);bins.append((u,a*du,b*du))
def evaluate(x):
 f=[I(0) for _ in range(3)];s=[I(0) for _ in range(3)]
 for u,a,b in bins:
  co,si=trig(x*u)
  for j,v in enumerate([co,-u*si,-u*u*co]):f[j]=f[j]+a*v;s[j]=s[j]+b*v
 return [v+sym(errors[j]) for j,v in enumerate(f)],[v+sym(utail) for v in s]
f0,s0=evaluate(I(0));normal=f0[0]/s0[0]
rows=[]
for k in range(cells):
 x=I(D(k)/2,D(k+1)/2);f,s=evaluate(x);g=[normal*v for v in s]
 w=f[0]*g[1]-g[0]*f[1];wp=f[0]*g[2]-g[0]*f[2]
 if (f[0].a>0 and g[0].a>0) or (f[0].b<0 and g[0].b<0):kind='same_sign_event_exclusion'
 elif w.a>0 or w.b<0:kind='W_event_exclusion'
 else:kind='unresolved'
 rows.append(dict(x=x.data(),kind=kind,F=[v.data() for v in f],G=[v.data() for v in g],W=w.data(),Wp=wp.data()))
 if k%20==19:print('completed cells',k+1,flush=True)
cover=rows[0]['x'][0]=='0' and rows[-1]['x'][1]=='40' and all(rows[k]['x'][1]==rows[k+1]['x'][0] for k in range(cells-1))
counts={kind:sum(r['kind']==kind for r in rows) for kind in sorted({r['kind'] for r in rows})}
cert=dict(step='579',backend=dict(python=platform.python_version(),decimal=decimal.__libmpdec_version__,precision=50,rounding='directed arithmetic; exp nearest expanded one ulp'),caps=dict(u_end=3,n_max=4,u_bins=M,x_cells=cells,x_width='0.5',adaptive_refinements=0),pi=pi.data(),n_tail_all_j=ntail.data(),u_tail_all_j=utail.data(),normalization=normal.data(),F0=f0[0].data(),S0=s0[0].data(),coverage=cover,counts=counts,events=[],cells=rows,failures=['No adaptive root isolation attempted: all nonexcluded cells retained.','No event or global sign certified.','Implementation and derived tail bounds await independent audit.'],seconds=time.monotonic()-start)
cert['input_sha256']={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for pattern in ['lemmas/L016-*.md','lemmas/L019-*.md','lemmas/L020-*.md','lemmas/L021-*.md','lemmas/L814-*.md','lemmas/L815-*.md','scripts/polya-census/census-579.py'] for p in Path('.').glob(pattern)}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(dict(counts=counts,coverage=cover,normalization=normal.data(),n_tail=ntail.data(),u_tail=utail.data(),certificate=str(path),seconds=cert['seconds'])))

"""Integer interval replay of every saved transformed column and trace sum.

Transcendental contracts and analytic source/remainder arguments are not
independently verified here. The output states this limited check scope.
"""
import hashlib
import json
from decimal import Decimal
from pathlib import Path

HERE=Path(__file__).resolve().parent
path=HERE/'distant-trace-469.json'
raw=path.read_bytes();out=json.loads(raw)
accepted=json.loads((HERE/'replay-466/audit.json').read_text())
core=json.loads((HERE/'refined-464.json').read_text())
first=json.loads((HERE/'distant-469.json').read_text())
base=json.loads((HERE/'certificate-455.json').read_text())
old=json.loads((HERE/'compression-463.json').read_text())
S=10**110
checks=0;failures=[]


def check(name,test):
    global checks
    checks+=1
    if not test:failures.append(name)


def fd(x):
    d=Decimal(x);t=d.as_tuple()
    n=int(''.join(map(str,t.digits)) or '0')*((-1)**t.sign)
    if t.exponent>=0:return n*10**t.exponent,1
    return n,10**(-t.exponent)


def ceildiv(a,b):return -((-a)//b)


class J:
    def __init__(self,lo,hi=None):self.lo=lo;self.hi=lo if hi is None else hi
    @staticmethod
    def dec(x):
        n,d=fd(x);return J(n*S//d,ceildiv(n*S,d))
    @staticmethod
    def saved(x):return J(J.dec(x['lo']).lo,J.dec(x['hi']).hi)
    def __add__(self,b):return J(self.lo+b.lo,self.hi+b.hi)
    def __neg__(self):return J(-self.hi,-self.lo)
    def __sub__(self,b):return self+-b
    def __mul__(self,b):
        z=[a*c for a in (self.lo,self.hi) for c in (b.lo,b.hi)]
        return J(min(z)//S,ceildiv(max(z),S))
    def __truediv__(self,b):
        assert b.lo>0
        z=[(a*S,c) for a in (self.lo,self.hi) for c in (b.lo,b.hi)]
        return J(min(a//c for a,c in z),max(ceildiv(a,c) for a,c in z))
    def sq(self):
        z=[self.lo*self.lo,self.hi*self.hi]
        return J(0 if self.lo<=0<=self.hi else min(z)//S,ceildiv(max(z),S))


one=J.dec(1);zero=J(0)
js=J.saved


def sumj(xs):
    v=zero
    for x in xs:v=v+x
    return v


def contains(saved,x):
    # Compare exact finite-decimal endpoints against integer/10^110.
    ln,ld=fd(saved['lo']);hn,hd=fd(saved['hi'])
    return ln*S<=x.lo*ld and hn*S>=x.hi*hd


check('accepted core file hash',hashlib.sha256((HERE/'refined-464.json').read_bytes()).hexdigest()==accepted['input_sha256']['refined-464.json'])
for name,sha in out['input_sha256'].items():
    check('input preserved '+name,hashlib.sha256((HERE/name).read_bytes()).hexdigest()==sha)
check('trace source hash',hashlib.sha256((HERE/'distant-trace-469.py').read_bytes()).hexdigest()==out['script_sha256'])
check('first source hash',hashlib.sha256((HERE/'distant-469.py').read_bytes()).hexdigest()==first['script_sha256'])
for name in ('certify-455.py','refined-464.json','compression-463.json','certificate-455.json'):
    check('same first-column input '+name,first['input_sha256'][name]==out['input_sha256'][name])
check('exact fixed parameters',out['parameters']=={'core':64,'distant_start':4096,'prefix_end':16384,'penalty':256,'geometric_terms':16})
check('every prefix index present',[row['q'] for row in out['prefix']]==list(range(4096,16384)))
check('ten moments retained',len(old['all_ten_moment_rows'])==10)
check('nine powers retained',[row['n'] for row in first['prime_components']]==[2,3,4,5,7,8,9,11,13])
A=js(core['parameters']['a']);PI=js(base['constants']['pi'])
# Use accepted saved squared-root factors, computed in the original interval
# library, as inputs to this integer replay. The core diagonal norm gives
# exactly the same n0/nq in old finite assembly; evaluate using Decimal's
# accepted correctly rounded sqrt separately and widen before integer use.
from decimal import Context, ROUND_HALF_EVEN, ROUND_FLOOR, ROUND_CEILING
ctx=Context(prec=100,rounding=ROUND_HALF_EVEN)
down=Context(prec=100,rounding=ROUND_FLOOR)
up=Context(prec=100,rounding=ROUND_CEILING)
def sqrtj(x):
    lo=down.divide(Decimal(x.lo),Decimal(S));hi=up.divide(Decimal(x.hi),Decimal(S))
    return J(J.dec(ctx.next_minus(ctx.sqrt(lo))).lo,J.dec(ctx.next_plus(ctx.sqrt(hi))).hi)
nq=sqrtj(J.dec(2)/A);sqrt2=sqrtj(J.dec(2))
u=[(J.dec(s)*PI/A).sq() for s in range(64)];U=u[-1]
cf=out['combined_coefficients']
am=[[js(x) for x in row] for row in cf['a']]
dm=[[js(x) for x in row] for row in cf['d']]
P=[js(x) for x in cf['P']]
ms=[[js(x) for x in row] for row in cf['moment_sin']]
mc=[[js(x) for x in row] for row in cf['moment_cos']]
ae=[J(-J.dec(x).hi,J.dec(x).hi) for x in cf['a_uniform_error']]
de=[J(-J.dec(x).hi,J.dec(x).hi) for x in cf['d_uniform_error']]
prefix=zero
for row in out['prefix']:
    q=row['q'];k=J.dec(q)*PI/A;v=k.sq();z=U/v;zz=js(row['Z'])
    ys=[]
    for r in range(64):
        ap,dp=am[r][-1],dm[r][-1]
        for m in range(14,-1,-1):ap=ap*z+am[r][m];dp=dp*z+dm[r][m]
        ap=ap/v+ae[r];dp=dp/v+de[r]
        y=nq*J.dec((-1)**q)*(zz*ap-dp+P[r]/(v+J.dec('.25')))
        y=y+nq/sqrt2*(k*ms[q%10][r]+mc[q%10][r])/(v+J.dec('.25'))
        check('complete integer column '+str(q)+' '+str(r),contains(row['B_column'][r],y))
        ys.append(js(row['B_column'][r]))
    norm=sumj(y.sq() for y in ys)
    check('norm '+str(q),contains(row['norm_squared'],norm))
    t=J.dec(row['weight_lower']);check('positive weight '+str(q),t.lo>0)
    contribution=js(row['norm_squared'])/t
    check('trace contribution '+str(q),contains(row['trace_contribution'],contribution))
    prefix=prefix+js(row['trace_contribution'])
check('entire prefix aggregation',contains(out['prefix_trace'],prefix))
tail=out['entire_tail']
at=js(tail['A_max']);bt=js(tail['B_max'])
ak=at*A/PI;bk=bt*(A/PI).sq()
for res in tail['residue_bounds']:
    check('tail A residue '+str(res['residue']),js(res['A']).hi<=at.lo)
    check('tail B residue '+str(res['residue']),js(res['B']).hi<=bt.lo)
for p in (2,3,4):
    n=16384
    val=J.dec(1)/J.dec(n**p)+J.dec(1)/J.dec((p-1)*n**(p-1))
    check('entire series '+str(p),contains(tail['series'][str(p)],val))
st={p:js(tail['series'][str(p)]) for p in (2,3,4)}
tail_expr=(ak.sq()*st[2]+J.dec(2)*ak*bk*st[3]+bk.sq()*st[4])/J.dec(tail['weight_lower'])
check('entire covariance tail upper',tail_expr.hi<=J.dec(tail['trace_upper']).lo)
total=js(out['prefix_trace'])+J.dec(tail['trace_upper'])
check('total trace upper',total.hi<=J.dec(out['total_trace_upper']).lo)
eps=J.dec(core['congruence']['norm_upper'])
check('strict threshold',J.dec(out['total_trace_upper']).hi<(one-eps).lo)
check('reported .290 coarsening',J.dec(out['total_trace_upper']).hi<J.dec('.290').lo)
check('positive status',out['status']=='CERTIFIED_POSITIVE_COMPLETE_DISTANT_COMPARISON')
check('certificate not changed while checking',path.read_bytes()==raw)
report={'status':'PASS' if not failures else 'FAIL','checks':checks,'failures':failures,
        'integer_scale_digits':110,'prefix_columns':12288,'column_entries':12288*64,
        'prefix_trace':out['prefix_trace'],'entire_tail_trace_upper':tail['trace_upper'],
        'total_trace_upper':out['total_trace_upper'],'required_upper':out['required_upper'],
        'scope':'same-step arithmetic consistency; analytic identities, scalar Z and tail-vector bound require conceptual audit',
        'certificate_sha256':hashlib.sha256(raw).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'distant-checks-469.json').write_text(json.dumps(report,indent=2)+'\n')
print(report['status'],'checks',checks,'failures',failures[:10],'; full failure list and bounds:',HERE/'distant-checks-469.json')

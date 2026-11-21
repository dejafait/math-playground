"""Independent exact-rational contractions and rank-recurrence checks.

No Decimal interval library or floating proposal is imported. Finite
certificate endpoints are exact rationals. Reassociate the complete
84-mode energy on (x,Yx), independently of the stored64-mode difference.
"""
import hashlib
import json
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as Q
from pathlib import Path

HERE=Path(__file__).resolve().parent
path=HERE/'neutral-certificate-473.json'
data=path.read_bytes(); c=json.loads(data)
checks=[]
def check(name,truth):
    checks.append({'name':name,'passed':bool(truth)})
    assert truth,name
class R:
    def __init__(self,lo,hi=None):
        self.lo=Q(lo); self.hi=self.lo if hi is None else Q(hi)
        assert self.lo<=self.hi
    @staticmethod
    def cast(x): return x if isinstance(x,R) else R(x)
    def __add__(self,x):
        x=R.cast(x); return R(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self):return R(-self.hi,-self.lo)
    def __sub__(self,x):return self+-R.cast(x)
    def __rsub__(self,x):return R.cast(x)+-self
    def __mul__(self,x):
        x=R.cast(x); ends=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return R(min(ends),max(ends))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=R.cast(x); assert not x.lo<=0<=x.hi
        return self*R(1/x.hi,1/x.lo)
    def sq(self):return R(0 if self.lo<=0<=self.hi else min(self.lo**2,self.hi**2),max(self.lo**2,self.hi**2))
    def contained(self,x):return x.lo<=self.lo and self.hi<=x.hi
    def record(self):
        def dec(x,mode):return str(Context(prec=42,rounding=mode).divide(Decimal(x.numerator),Decimal(x.denominator)))
        return {'lo':dec(self.lo,ROUND_FLOOR),'hi':dec(self.hi,ROUND_CEILING),
                'exact_lo':str(self.lo),'exact_hi':str(self.hi)}
sv=lambda x:R(x['lo'],x['hi'])
mat=lambda x:[[sv(y) for y in row] for row in x]
def form(m,z):
    return sum(((1 if r==s else 2)*z[r]*z[s]*m[r][s]
                for r in range(len(z)) for s in range(r,len(z))),R(0))

check('completed certificate status',c['status']=='CERTIFIED_NEGATIVE_HALF_ENERGY_DIRECTION')
check('source hash matches',hashlib.sha256((HERE/'neutral-certificate-473.py').read_bytes()).hexdigest()==c['source_sha256'])
for name,digest in c['input_sha256'].items():
    check('input hash '+name,hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest)
C=mat(c['range']['all_ten_rows']); G=mat(c['range']['restricted_gram'])
L=mat(c['range']['unit_lower']); piv=[sv(x) for x in c['range']['positive_pivots']]
for i in range(5):
    for j in range(5):
        value=sum((C[i][q]*C[j][q] for q in range(64,84)),R(0))
        check('exact rational Gram containment '+str((i,j)),value.contained(G[i][j]))
for j in range(5):
    value=G[j][j]-sum((L[j][t].sq()*piv[t] for t in range(j)),R(0))
    check('exact rational pivot recurrence '+str(j),value.contained(piv[j]) and piv[j].lo>0)
    for i in range(j+1,5):
        value=(G[i][j]-sum((L[i][t]*L[j][t]*piv[t] for t in range(j)),R(0)))/piv[j]
        check('exact rational LDL entry '+str((i,j)),value.contained(L[i][j]))
Y=mat(c['range']['minimum_L2_map'])
def solve(rhs):
    z=[]
    for j in range(5):z.append(rhs[j]-sum((L[j][t]*z[t] for t in range(j)),R(0)))
    z=[z[j]/piv[j] for j in range(5)]
    for j in range(4,-1,-1):z[j]-=sum((L[t][j]*z[t] for t in range(j+1,5)),R(0))
    return z
inv=mat(c['range']['gram_inverse'])
for q in range(5):
    column=solve([R(int(i==q)) for i in range(5)])
    check('exact rational inverse column '+str(q),all(column[j].contained(inv[j][q]) for j in range(5)))
for q in range(64):
    column=solve([C[j][q] for j in range(5)])
    expected=[-sum((C[j][64+t]*column[j] for j in range(5)),R(0)) for t in range(20)]
    check('exact rational minimum-L2 map column '+str(q),all(expected[t].contained(Y[t][q]) for t in range(20)))
check('explicit map norm bound below37803',sum((x.sq().hi for row in Y for x in row),Q(0))<37803**2)
check('explicit symmetric inverse norm bound below2.58e9',
      max(sum((max(abs(x.lo),abs(x.hi)) for x in row),Q(0)) for row in inv)<Q('2.58e9'))
H=mat(c['energy']['core_H']); E=mat(c['energy']['complete_unpenalized_matrix'])
accepted=json.loads((HERE/'refined-464.json').read_text())
check('core H is unchanged accepted enclosure',c['energy']['core_H']==accepted['complete_matrix'])
components=c['energy']['nine_prime_components']
check('exact nine active prime powers',[(x['n'],x['base_prime']) for x in components]==
      [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(13,13)])
primes=[mat(x['matrix']) for x in components]
gram=mat(c['energy']['response_gram']); pole=[sv(x) for x in c['energy']['pole_row']]
h=[sv(x) for x in c['energy']['h']]
for r in range(84):
    for s in range(max(r,64),84):
        value=sum((m[r][s] for m in primes),R(0))+gram[r][s]+pole[r]*pole[s]+(h[r] if r==s else 0)
        check('complete new entry assembly '+str((r,s)),value.contained(E[r][s]))
for r in range(64):
    for s in range(r,64):
        penalty=sum((256*C[j][r]*C[j][s] for j in range(10)),R(0))
        value=H[r][s]-sv(c['energy']['core_penalty'][r][s])
        check('complete core entry assembly '+str((r,s)),value.contained(E[r][s]) and
              penalty.contained(sv(c['energy']['core_penalty'][r][s])))
F=mat(c['energy']['half_energy_difference'])
z=[R(x) for x in c['direction']['exact_decimal_coefficients']]
check('fixed nonzero core vector',len(z)==64 and z[8].lo==1 and z[8].hi==1)
check('last16 coefficients exactly zero',all(x.lo==x.hi==0 for x in z[48:]))
y=[sum((Y[j][q]*z[q] for q in range(64)),R(0)) for j in range(20)]
v=z+y
core=form(H,z); graph=form(E,v); direct=graph-core/2; stored=form(F,z)
check('exact rational difference contraction lies in saved directed bound',stored.contained(sv(c['direction']['half_energy_difference'])))
check('direct complete energy difference has strict negative upper',direct.hi<0)
check('stored difference has strict negative upper',stored.hi<0)
check('independent intervals overlap',max(direct.lo,stored.lo)<=min(direct.hi,stored.hi))
norm=sum((x.sq() for x in z),R(0)); ynorm=sum((x.sq() for x in y),R(0))
check('core norm in (2.659,2.660)',Q('2.659')<norm.lo and norm.hi<Q('2.660'))
out={'status':'EXACT_RATIONAL_CHECKS_PASSED','certificate_sha256':hashlib.sha256(data).hexdigest(),
     'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'checks':checks,'failures':[],
     'core_norm_squared':norm.record(),'correction_norm_squared':ynorm.record(),
     'core_penalized_energy':core.record(),'corrected_complete_energy':graph.record(),
     'independent_complete_difference':direct.record(),'stored_difference_contraction':stored.record(),
     'scope':'Independent rational scalar/rank checks, not an independent conceptual audit of imported identities or the full enclosure implementation.'}
dest=HERE/'neutral-checks-473.json'; dest.write_text(json.dumps(out,indent=2)+'\n')
for name in ('core_penalized_energy','corrected_complete_energy','independent_complete_difference','correction_norm_squared'):
    print(name,{k:out[name][k] for k in ('lo','hi')})
print('Checks:',len(checks),'passed; failures:',out['failures'],'; full evidence:',dest)

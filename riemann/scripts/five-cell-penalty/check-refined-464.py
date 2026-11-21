"""Independent exact-integer verification of complete saved congruence.

Checks every entry against the full interval matrix, all residual rows,
all power-sum block aggregations, and old scalar/diagonal consistency.
The analytic enclosure derivation still requires its separate audit.
"""
import hashlib
import json
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent
path=HERE/'refined-464.json'
d=json.loads(path.read_text())
old=json.loads((HERE/'compression-463.json').read_text())
base=json.loads((HERE/'certificate-455.json').read_text())
checks=[]
failures=[]
def check(name,c):
    checks.append({'name':name,'passed':bool(c)})
    if not c:failures.append(name)
def pair(x):return F(x['lo']),F(x['hi'])
def contains(x,y):return x[0]<=y[0]<=y[1]<=x[1]
check('same complete-assembly input hash',d['inputs']['old_assembly_sha256']==hashlib.sha256((HERE/'compression-463.json').read_bytes()).hexdigest())
check('unchanged target parameters',d['parameters']['dimension']==64 and d['parameters']['K_cells']==5 and d['parameters']['penalty']==256 and d['parameters']['a']==old['parameters']['a'])
for kind,sums in d['inverse_power_sums'].items():
    for p,x in sums.items():
        vals=[pair(b[kind][p]['sum']) for b in d['blocks']]
        t=pair(d['final_positive_tails'][kind][p])
        total=(sum(v[0] for v in vals),sum(v[1] for v in vals)+t[1])
        check(f'complete inverse sum aggregation {kind},{p}',contains(pair(x),total))
for q,x in enumerate(d['h']):
    a,b=pair(x),pair(base['all_h_enclosures'][q]['h'])
    check(f'refined diagonal agrees with accepted enclosure {q}',b[0]<=a[0]<=a[1]<=b[1])
check('current matrix source hash',d['matrix_source_sha256']==hashlib.sha256((HERE/'refined-464.py').read_bytes()).hexdigest())
check('current sign source hash',d['sign_source_sha256']==hashlib.sha256((HERE/'sign-464.py').read_bytes()).hexdigest())
check('all nine arithmetic components and all ten moments',len(old['prime_components'])==9 and len(old['all_ten_moment_rows'])==10)
M=d['complete_matrix']; B=d['congruence']['B']; R=d['congruence']['residual']
for i in range(64):
    for j in range(i,64):
        parts=[pair(old[key][i][j]) for key in ('prime_matrix','penalty_matrix','pole_matrix')]
        parts.append(pair(d['response_gram'][i][j]))
        if i==j:parts.append(pair(d['h'][i]))
        check(f'full exact matrix assembly {i},{j}',contains(pair(M[i][j]),(sum(x[0] for x in parts),sum(x[1] for x in parts))))
# Integer scaling represents every decimal endpoint exactly, with no rounding.
def integer_scale(values):
    digs=max(0,max(-Decimal(x).as_tuple().exponent for x in values))
    return 10**digs
dm=integer_scale([x[e] for row in M for x in row for e in ('lo','hi')])
db=integer_scale([x['lo'] for row in B for x in row])
def scaled(s,den):
    x=F(s)*den
    assert x.denominator==1
    return x.numerator
ml=[[scaled(x['lo'],dm) for x in row] for row in M]
mh=[[scaled(x['hi'],dm) for x in row] for row in M]
b=[[scaled(x['lo'],db) for x in row] for row in B]
for i in range(64):
    check(f'exact invertible lower triangular B row {i}',b[i][i]>0 and all(x['lo']==x['hi'] for x in B[i]) and all(b[i][j]==0 for j in range(i+1,64)))
bl=[[sum(b[i][k]*(ml[k][j] if b[i][k]>=0 else mh[k][j]) for k in range(i+1)) for j in range(64)] for i in range(64)]
bh=[[sum(b[i][k]*(mh[k][j] if b[i][k]>=0 else ml[k][j]) for k in range(i+1)) for j in range(64)] for i in range(64)]
den=dm*db**2
bounds=[[0]*64 for _ in range(64)]
for i in range(64):
    for j in range(i,64):
        lo=sum((bl[i][k] if b[j][k]>=0 else bh[i][k])*b[j][k] for k in range(j+1))-(den if i==j else 0)
        hi=sum((bh[i][k] if b[j][k]>=0 else bl[i][k])*b[j][k] for k in range(j+1))-(den if i==j else 0)
        check(f'full exact congruence entry {i},{j}',contains(pair(R[i][j]),(F(lo,den),F(hi,den))))
        check(f'saved symmetric complete entry {i},{j}',M[i][j]==M[j][i] and R[i][j]==R[j][i])
        bounds[i][j]=bounds[j][i]=max(abs(lo),abs(hi))
exact_rows=[F(sum(row),den) for row in bounds]
for i,x in enumerate(exact_rows):
    check(f'exact residual row bound {i}',x<=F(d['congruence']['row_bounds'][i]['hi']))
bound=max(exact_rows)
check('strict exact residual norm threshold',bound<F(1774,10**17) and bound<1)
check('saved directed norm bound',bound<=F(d['congruence']['norm_upper']))
bnorm2=F(sum(x*x for row in b for x in row),db**2)
lower=(1-bound)/bnorm2
check('strict uniform lower bound greater than 1e-43',lower>F(1,10**43))
# Whole scalar consistency with the separately accepted C744c direction.
z=[F(n,base['witness']['denominator']) for n in base['witness']['numerators']]
lo=hi=F(0)
for i in range(64):
    for j in range(64):
        w=z[i]*z[j]
        l,h=pair(M[i][j]);lo+=w*(l if w>=0 else h);hi+=w*(h if w>=0 else l)
scalar=pair(json.loads((HERE/'complete-response-459.json').read_text())['complete_penalized_energy'])
check('accepted positive scalar intersects complete refined matrix',max(lo,scalar[0])<=min(hi,scalar[1]))
out={'status':'CHECKS_PASS' if not failures else 'CHECKS_FAILED','input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
     'checks':checks,'failures':failures,'exact_residual_row_bounds':[str(x) for x in exact_rows],
     'exact_residual_norm_upper':str(bound),'B_frobenius_squared':str(bnorm2),'uniform_eigenvalue_lower_bound':str(lower),
     'required':'residual norm strictly below 1 and B invertible',
     'scope':'exact arithmetic verification of saved matrix certificate; analytic enclosures separately unaudited'}
(HERE/'refined-checks-464.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact checks:',len(checks),'; failures:',failures)
print('Residual norm upper < 1.774e-14:',bound<F(1774,10**17),'; required <1:',bound<1)
print('Uniform eigenvalue lower bound > 1e-43:',lower>F(1,10**43))
print('Full exact evidence:',HERE/'refined-checks-464.json')
assert not failures

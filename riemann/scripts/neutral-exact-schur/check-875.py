"""Exact-dyadic accounting and unshifted interval block test for attempt875.

Not an independent elementary-function or FFT implementation. No midpoint
or ordinary floating eigenvalue is a sign certificate. Full pivot intervals
and failures are saved, including inconclusive positivity tests.
"""
import json
from fractions import Fraction as F
from math import isqrt, nextafter, inf
from pathlib import Path
ROOT=Path(__file__).parent
c=json.loads((ROOT/'certificate-875.json').read_text())
checks={}
def iv(x): return tuple(F(v) for v in x)
def pt(x): return (F(x),F(x))
def neg(a): return -a[1],-a[0]
def add(a,b): return a[0]+b[0],a[1]+b[1]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    p=[x*y for x in a for y in b]
    return min(p),max(p)
def square(a): return (F(0) if a[0]<=0<=a[1] else min(x*x for x in a),max(x*x for x in a))
def div(a,b):
    assert b[0]*b[1]>0
    return mul(a,(1/b[1],1/b[0]))
def encl(a,b): return a[0]<=b[0] and b[1]<=a[1]
def sumiv(xs):
    s=pt(0)
    for x in xs: s=add(s,x)
    return s
def vadd(a,b): return [add(x,y) for x,y in zip(a,b)]
def sqrt_upper(x):
    assert x>=0
    n=1<<160
    k=isqrt(x.numerator*n*n//x.denominator)
    return F(k+1,n)
def exact_pair(x): return [str(t) for t in x]
def display_pair(x):
    lo,hi=map(float,x)
    if F(lo)>x[0]: lo=nextafter(lo,-inf)
    if F(hi)<x[1]: hi=nextafter(hi,inf)
    return [lo,hi]
m=[iv(x) for x in c['moments']]
H=[[iv(x) for x in r] for r in c['gram']]
def dot(a,b): return sumiv(mul(mul(a[i],H[i][j]),b[j]) for i in range(12) for j in range(12))
def neutral(i,p):
    a=[pt(0) for _ in range(12)]
    a[i]=pt(1);a[p]=div(neg(m[i]),m[p])
    return a
coordinates=[]
for s,sector in enumerate(c['sectors']):
    b,d=neutral(s+2,s),neutral(s+4,s)
    h00,h01,h11=dot(b,b),dot(b,d),dot(d,d)
    det=sub(mul(h00,h11),square(h01))
    checks[f'sector{s}_retained_L2_det_positive']=det[0]>0
    def project(r):
        p0,p1=dot(r,b),dot(r,d)
        a=div(sub(mul(h11,p0),mul(h01,p1)),det)
        e=div(sub(mul(h00,p1),mul(h01,p0)),det)
        return vadd(r,vadd([mul(neg(a),t) for t in b],[mul(neg(e),t) for t in d]))
    basis=[b,d]+[project(neutral(s+2*j+2,s)) for j in range(2,5)]
    coordinates.append([[[str(t) for t in x] for x in a] for a in basis])
    for j,a in enumerate(basis):
        stored=[iv(x) for x in sector['basis'][j]]
        checks[f'sector{s}_basis{j}_exact_coordinate_enclosure']=all(encl(x,y) for x,y in zip(stored,a))
        checks[f'sector{s}_basis{j}_L2_norm_enclosure']=encl(iv(sector['basis_norms'][j]),dot(stored,stored))
    checks[f'sector{s}_exactly_ten_pairs']=sorted((p['i'],p['j']) for p in sector['pairs'])==[(j,k) for j in range(5) for k in range(j)]
    energies=[(f'diag{j}',r) for j,r in enumerate(sector['diagonals'])]+[(f"pair{p['i']}_{p['j']}",p['sum']) for p in sector['pairs']]
    for name,r in energies:
        tag=f'sector{s}_{name}'
        q,eps,ew,qw,cp=(iv(r[k]) for k in ('q_norm_squared','error_L2_squared_bound','error_W_squared_bound','q_W_squared_bound','C_prime'))
        interp=2*sqrt_upper(qw[1]*ew[1])+ew[1]+cp[1]*(2*sqrt_upper(q[1]*eps[1])+eps[1])
        checks[tag+'_full_interpolation_upper']=iv(r['interpolation_energy_bound'])[1]>=interp
        checks[tag+'_L2_error_upper']=eps[1]>=F(1,4096)**4*iv(r['smooth_second_derivative_squared_bound'])[1]
        central=sub(iv(r['periodic_archimedean_head']),iv(r['all_prime_delays']))
        radius=sum(iv(r[k])[1] for k in ('fourier_tail_bound','periodic_images_bound','interpolation_energy_bound'))
        checks[tag+'_full_energy_accounting']=encl(iv(r['smooth_energy']),(central[0]-radius,central[1]+radius))
    mat=[[iv(x) for x in row] for row in sector['energy_matrix']]
    checks[f'sector{s}_matrix_symmetric']=all(mat[i][j]==mat[j][i] for i in range(5) for j in range(5))
    checks[f'sector{s}_diagonals_saved']=all(mat[j][j]==iv(r['smooth_energy']) for j,r in enumerate(sector['diagonals']))
    for p in sector['pairs']:
        i,j=p['i'],p['j']
        cross=div(sub(sub(iv(p['sum']['smooth_energy']),mat[i][i]),mat[j][j]),pt(2))
        checks[f'sector{s}_cross{i}_{j}_polarization']=encl(iv(p['cross']),cross) and mat[i][j]==iv(p['cross'])
def prime_power(n):
    p=next((j for j in range(2,isqrt(n)+1) if n%j==0),n)
    while n%p==0: n//=p
    return n==1
checks['all31_prime_powers']=c['prime_powers']==[n for n in range(2,81) if prime_power(n)] and len(c['prime_powers'])==31
# Test actual ENERGY G, neither L2 Gram nor finite covariance.
# Elimination after positive pivots is an exact congruence. If a pivot
# overlaps zero we stop without dividing and without declaring a kernel.
block_tests=[]
for s,sector in enumerate(c['sectors']):
    M=[[iv(x) for x in row] for row in sector['energy_matrix']]
    order=[2,3,4,0,1] # Eliminate Z first, then the unshifted Schur block.
    K=[[M[i][j] for j in order] for i in order]
    pivots=[];status='CERTIFIED_POSITIVE_DEFINITE'
    for j in range(5):
        pivot=K[j][j]
        pivots.append({'coordinate':order[j],'block':'Z' if j<3 else 'Schur','enclosure':display_pair(pivot),'exact_rational_calculation':exact_pair(pivot),'required_lower':0})
        if pivot[1]<0:
            status='CERTIFIED_NEGATIVE_DIRECTION';break
        if pivot[0]<=0:
            status='INCONCLUSIVE_G' if j<3 else 'INCONCLUSIVE_SCHUR';break
        for a in range(j+1,5):
            for b in range(a,5):
                term=square(K[a][j]) if a==b else mul(K[a][j],K[b][j])
                K[a][b]=K[b][a]=sub(K[a][b],div(term,pivot))
    block_tests.append({'sector':s,'status':status,'pivots':pivots,'singular_kernel':'NOT_ESTABLISHED','range_condition':'NOT_DECIDED' if status.startswith('INCONCLUSIVE') else 'Vacuous if G certified PD'})
failures=[k for k,v in checks.items() if not v]
positivity_failures=[f"sector{x['sector']}: {x['status']}; no exact singular kernel inferred" for x in block_tests if x['status'].startswith('INCONCLUSIVE')]
out={'accounting_status':'PASS' if not failures else 'FAIL','status':'INCONCLUSIVE' if positivity_failures else 'SIGNED_BLOCK_TEST','checks':checks,'block_tests':block_tests,'exact_coordinate_enclosures':coordinates,'accounting_failures':failures,'positivity_failures':positivity_failures,'certificate':'scripts/neutral-exact-schur/certificate-875.json','scope':'Exact dyadic accounting and one natural-order unshifted interval LDL test; not an independent FFT or a singular-rank certificate.'}
path=ROOT/'check-875.json';path.write_text(json.dumps(out,indent=2)+'\n')
print(out['accounting_status'],len(checks),'accounting checks;',out['status'],'; accounting failures:',failures)
for t in block_tests:
    p=t['pivots'][-1]
    print('sector',t['sector'],t['status'],'; final',p['block'],'pivot',p['enclosure'],'; required lower >0; kernel/range undecided')
print('Full certificate:',out['certificate'],'; block evidence:',path)
raise SystemExit(1 if failures else 0)

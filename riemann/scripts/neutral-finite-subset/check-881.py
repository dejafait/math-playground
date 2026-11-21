"""Exact dyadic coordinate/Gram accounting; not independent integration.

All uncertainties remain enclosed; box feasibility is not actual-root
feasibility. No midpoint spectrum, numerical root or negative form is used.
"""
import json
import hashlib
from fractions import Fraction as F
from pathlib import Path
from math import nextafter, inf

HERE=Path(__file__).parent
source=HERE.parent/'neutral-exact-schur/certificate-875.json'
old=json.loads(source.read_text())
c=json.loads((HERE/'certificate-881.json').read_text())
checks={}
def iv(a): return tuple(F(x) for x in a)
def pt(x): return F(x),F(x)
def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[1],-a[0]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    p=[x*y for x in a for y in b]
    return min(p),max(p)
def sq(a): return (F(0) if a[0]<=0<=a[1] else min(x*x for x in a),max(x*x for x in a))
def div(a,b):
    assert b[0]*b[1]>0
    return mul(a,(1/b[1],1/b[0]))
def sumiv(xs):
    r=pt(0)
    for x in xs: r=add(r,x)
    return r
def encl(a,b): return a[0]<=b[0] and b[1]<=a[1]
def zero(a): return a[0]<=0<=a[1]
def disp(a):
    l,h=map(float,a)
    if F(l)>a[0]: l=nextafter(l,-inf)
    if F(h)<a[1]: h=nextafter(h,inf)
    return [l,h]
def exact(a): return [str(x) for x in a]
mom=[iv(a) for a in old['moments']]
gram=[[iv(a) for a in row] for row in old['gram']]
def dot(a,b): return sumiv(mul(mul(a[i],gram[i][j]),b[j]) for i in range(12) for j in range(12))
def neutral(i,p):
    a=[pt(0) for _ in range(12)]
    a[i]=pt(1);a[p]=div(neg(mom[i]),mom[p])
    return a
def va(a,b): return [add(x,y) for x,y in zip(a,b)]
def vs(t,a): return [mul(t,x) for x in a]

printed=[['14.111328125','14.16015625'],['20.99609375','21.044921875'],['25','25.048828125'],['30.419921875','30.4443359375'],['32.91015625','32.958984375'],['37.548828125','37.59765625'],['40.91796875','40.966796875'],['43.310546875','43.3349609375'],['47.998046875','48.0224609375'],['49.755859375','49.7802734375']]
checks['fixed_workload']=c['full_window_panels']==32768 and c['half_window_panels']==16384
checks['transport_allowance']=encl(iv(c['transport_allowance']),pt(F(1,10**12)))
for z,(l,h) in enumerate(printed):
    checks[f'root{z}_transport']=encl(iv(c['frequencies'][z]),(F(l)-F(1,10**12),F(h)+F(1,10**12)))
checks['disjoint_positive_intervals_below_H']=all(iv(a)[0]>0 and iv(a)[1]<3*10**12 for a in c['frequencies']) and all(iv(c['frequencies'][j])[1]<iv(c['frequencies'][j+1])[0] for j in range(9))
checks['T_matches_source']=c['T']==old['T']
raw=[[iv(a) for a in row] for row in c['raw_centered_samples']]
H=3*10**12
epsilon=(36*10**9)**2*(F(91,27*H**3)+F(1687,50*H**4))
checks['epsilon_matches_C750d']=epsilon==F(4550000000015183,28125000000000000000000000000000)
tests=[]
for p,sector in enumerate(c['sectors']):
    b,d=neutral(p+2,p),neutral(p+4,p)
    h00,h01,h11=dot(b,b),dot(b,d),dot(d,d)
    det=sub(mul(h00,h11),sq(h01))
    checks[f'sector{p}_projection_det_positive']=det[0]>0
    def project(r):
        p0,p1=dot(r,b),dot(r,d)
        a=div(sub(mul(h11,p0),mul(h01,p1)),det)
        e=div(sub(mul(h00,p1),mul(h01,p0)),det)
        return va(r,va(vs(neg(a),b),vs(neg(e),d)))
    basis=[b,d]+[project(neutral(p+2*j+2,p)) for j in range(2,5)]
    stored=[[iv(x) for x in row] for row in sector['basis']]
    for j in range(5):
        checks[f'sector{p}_coordinate{j}']=all(encl(a,b) for a,b in zip(stored[j],basis[j]))
    samples=[[iv(x) for x in row] for row in sector['samples']]
    for z in range(10):
        for j in range(5):
            expected=sumiv(mul(stored[j][k],raw[z][k]) for k in range(12))
            checks[f'sector{p}_sample{z}_{j}']=encl(samples[z][j],expected)
    G=[[iv(x) for x in row] for row in sector['retained_gram']]
    for i in range(5):
        for j in range(5):
            entry=sumiv(mul(pt(2),sq(samples[z][i]) if i==j else mul(samples[z][i],samples[z][j])) for z in range(10))
            checks[f'sector{p}_gram{i}_{j}']=encl(G[i][j],entry)
    mid=[[(a[0]+a[1])/2 for a in row] for row in G]
    radius=[[(a[1]-a[0])/2 for a in row] for row in G]
    error=max(sum(row) for row in radius)
    center_lower=min(mid[i][i]-sum(abs(mid[i][j]) for j in range(5) if j!=i) for i in range(5))
    lower=center_lower-error
    # Fixed natural order LDL test: stop before any overlapping division.
    K=[[sub(G[i][j],pt(epsilon)) if i==j else G[i][j] for j in range(5)] for i in range(5)]
    pivots=[]
    status='CERTIFIED_PD'
    for j in range(5):
        pivot=K[j][j]
        pivots.append({'coordinate':j,'enclosure':disp(pivot),'exact':exact(pivot)})
        if pivot[0]<=0:
            status='INCONCLUSIVE';break
        for a in range(j+1,5):
            for b_ in range(a,5):
                term=sq(K[a][j]) if a==b_ else mul(K[a][j],K[b_][j])
                K[a][b_]=K[b_][a]=sub(K[a][b_],div(term,pivot))
    tests.append({'sector':p,'status':status,'sample_boxes_containing_zero':sum(zero(a) for row in samples for a in row),'total_samples':50,'zero_matrix_allowed_by_entry_boxes':all(zero(a) for row in G for a in row),'finite_matrix_error_norm_upper':str(error),'finite_matrix_error_norm_upper_display':disp(pt(error)),'center_gershgorin_lower':str(center_lower),'paid_lower_bound':str(lower),'paid_lower_bound_display':disp(pt(lower)),'required_strict_lower':str(epsilon),'shifted_LDL_pivots':pivots,'interpretation':'Enclosure failure only; no actual-root feasibility, exact rank, negative form or RH conclusion.'})

failures=[k for k,v in checks.items() if not v]
out={'accounting_status':'FAIL' if failures else 'PASS','status':'INCONCLUSIVE_FIXED_SUBSET_CERTIFICATE','checks':checks,'accounting_failures':failures,'positivity_failures':[f"sector{x['sector']}: shifted LDL inconclusive; paid lower <= epsilon" for x in tests if x['status']!='CERTIFIED_PD'],'epsilon_exact':str(epsilon),'epsilon_display':disp(pt(epsilon)),'source_certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'raw_samples_containing_zero':sum(zero(a) for row in raw for a in row),'total_raw_samples':120,'tests':tests,'scope':'Exact rational coordinate and matrix accounting, not independent integration or conceptual audit.'}
path=HERE/'check-881.json';path.write_text(json.dumps(out,indent=2)+'\n')
print(out['accounting_status'],len(checks),'accounting checks; failures:',failures)
print('Required strict lower >',out['epsilon_display'],'in original coefficient metric')
for t in tests:
    print('Sector',t['sector'],t['status'],'; zero-containing samples',t['sample_boxes_containing_zero'],'/50; paid lower',t['paid_lower_bound_display'],'; error norm upper',t['finite_matrix_error_norm_upper_display'],'; shifted pivot',t['shifted_LDL_pivots'][0]['enclosure'])
print('Full certificates:',HERE/'certificate-881.json',path)
raise SystemExit(bool(failures))

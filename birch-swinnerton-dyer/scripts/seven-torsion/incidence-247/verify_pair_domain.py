#!/usr/bin/env python3
"""Independent full coefficient replay of only the ordered-pair domain.

No producer import. This is deliberately not an incidence-map verifier.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys,time
ROOT=Path(__file__).resolve().parent
UP=ROOT.parent
sys.path.insert(0,str(UP))
import verify_certificate as V

def main():
    t=time.monotonic(); checks=[]
    def require(ok,label):
        if not ok:raise ValueError(label)
        checks.append(label)
    c=json.loads((ROOT/'ordered-pairs.json').read_text())
    a=json.loads((UP/'certificate.json').read_text())
    actions=json.loads((UP/'scalar-actions-243/actions.json').read_text())
    require(c['schema']=='389-ordered-pairs-v1','schema')
    for key,path in [('upstream_sha256',UP/'certificate.json'),('actions_sha256',UP/'scalar-actions-243/actions.json')]:
        require(c[key]==hashlib.sha256(path.read_bytes()).hexdigest(),key)
    f=V.readpoly(a['f'])
    require(V.readpoly(c['f'])==f,'complete_f_coefficients')
    require(V.readpoly(c['cubic'])==[46224,-3024,0,1],'complete_cubic_coefficients')
    zero=[];one=[F(1)];x=[F(0),F(1)]
    def read(p):return V.clean(V.readpoly(p))
    def add(p,q):return V.plus(p,q)
    def sub(p,q):return V.plus(p,q,-1)
    def mul(p,q):return V.remainder(V.times(p,q),f)
    def ot(p):
        p=list(p)
        while p and not p[-1]:p.pop()
        return p
    def oa(p,q):
        return ot([add(p[i] if i<len(p) else zero,q[i] if i<len(q) else zero)
                   for i in range(max(len(p),len(q)))])
    def om(p,q):
        r=[zero]*max(0,len(p)+len(q)-1)
        for i,v in enumerate(p):
            for j,w in enumerate(q):
                r[i+j]=add(r[i+j],mul(v,w))
        return ot(r)
    def ev(p,z):
        out=zero
        for v in reversed(p):out=add(mul(out,z),v)
        return out
    roots=[read(p) for p in c['excluded_x']]
    require(len(roots)==3,'all_three_excluded_x_coordinates')
    for j,r in enumerate(roots,1):
        geom=actions['maps'][str(j)]['X']
        require(not read(geom[1]) and r==read(geom[0]),'audited_geometric_scalar_X_'+str(j))
        require(not V.evalmod(f,r,f),'root_f_X_'+str(j))
    seen=set()
    for item in c['excluded_separation']:
        i,j=item['i'],item['j'];seen.add((i,j))
        require((i,j) in [(1,0),(2,0),(2,1)],'separation_indices_'+str((i,j)))
        z=sub(roots[i],roots[j])
        require(read(item['value'])==z,'separation_value_'+str((i,j)))
        require(mul(z,read(item['inverse']))==one,'separation_inverse_'+str((i,j)))
    require(seen=={(1,0),(2,0),(2,1)} and len(c['excluded_separation'])==3,'all_pairwise_separations')
    g=[read(p) for p in c['g']]
    require(len(g)==22 and g[-1]==one,'degree21_monic_complete_g')
    require(all(len(v)<=24 for v in g),'all_C_coefficients_reduced')
    prod=g
    for r in roots:prod=om(prod,[V.scalar(r,-1),one])
    require(prod==ot([[z] if z else zero for z in f]),'full_factorization_in_C_U')
    value=ev(g,x)
    require(value==read(c['g_at_X']),'complete_g_at_X')
    require(mul(value,read(c['g_at_X_inverse']))==one,'complete_g_at_X_unit')
    inv=[read(p) for p in c['secant_inverse']]
    require(len(inv)==21,'entire_secant_inverse_vector')
    product=om([V.scalar(x,-1),one],inv)
    # The raw product has degree 21; use its leading coefficient once.
    require(len(product)==22,'secant_product_degree')
    lead=product[-1]
    reduced=[sub(product[j],mul(lead,g[j])) for j in range(21)]
    require(ot(reduced)==[one],'whole_domain_secant_unit_identity')
    require(c['basis']=={'order':'X^i U^j Y^e V^d, i fastest, then j, e, d','ranges':[24,21,2,2]},'basis_specification')
    require(c['dimension']==24*21*2*2==2016,'monic_presentation_dimension')
    original=json.loads((ROOT/'upstream-manifest.json').read_text())
    changed=[p for p,h in original.items() if not (UP/p).is_file() or hashlib.sha256((UP/p).read_bytes()).hexdigest()!=h]
    require(not changed,'all_upstream_bytes_preserved')
    # Full slot/size statistics, not a mathematical bound on later coefficients.
    rationals=[z for p in c['g']+c['secant_inverse'] for z in map(F,p)]
    report={'schema':'389-pair-domain-replay-v1','passed':True,'checks':checks,
            'checks_count':len(checks),'failures':[],
            'actual_ordered_pair_dimension':2016,'required_ordered_pair_dimension':2016,
            'actual_g_degree':21,'required_g_degree':21,
            'max_coefficient_numerator_bits':max(abs(z.numerator).bit_length() for z in rationals),
            'max_coefficient_denominator_bits':max(z.denominator.bit_length() for z in rationals),
            'upstream_files_preserved':len(original),'seconds':round(time.monotonic()-t,3),
            'scope':'ordered-pair domain and secant unit only; no quotient, incidence, translation or norm replay'}
    (ROOT/'domain-verification.json').write_text(json.dumps(report,separators=(',',':'))+'\n')
    print(json.dumps({k:report[k] for k in ['passed','checks_count','failures','actual_ordered_pair_dimension','required_ordered_pair_dimension','max_coefficient_numerator_bits','max_coefficient_denominator_bits','scope']}))

if __name__=='__main__':main()

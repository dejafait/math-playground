"""Independent full coefficient and frozen zero-block contraction check."""
import hashlib
import json
import sys
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE=Path(__file__).parent
OUT=BASE/'fixed-cardinality-normalized-control-verification.json'
def enc(x):
    x=Q(x)
    return [x.numerator,x.denominator]
@lru_cache(None)
def choose(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k)) if 0<=k<=n else 0
def main():
    data=json.loads((BASE/'fixed-cardinality-normalized-control-results.json').read_text())
    full=json.loads((BASE/'full-zero-block-results.json').read_text())
    fail=[]
    def require(ok,tag):
        if not ok: fail.append(tag)
    for path,digest in data['input_sha256'].items():
        require(hashlib.sha256((BASE/path).read_bytes()).hexdigest()==digest,'unchanged input '+path)
    p=list(map(lambda x:Q(*x),data['p']))
    cp=list(map(lambda x:Q(*x),data['control_p']))
    a=Q(*data['alpha']); N=data['N']; M=Q(*data['M'])
    require(N==65537**28//2**128+1 and a==(N-1)/(M-1),'frozen alpha')
    require(all(cp[i]==a*p[i]+(1-a)*int(i==0) for i in range(69)),'all control pairs')
    require(sum(choose(68,i)*choose(956,i)*cp[i] for i in range(69))==N,'exact objective')
    rows={}; orbits=0; entry_checks=0
    yd=data['scalar_denominator_z']; cd=data['scalar_denominator_control']
    records={tuple(r['distances']):r for r in data['scalar_values']}
    control_matrix=[[Q(*x) for x in row] for row in data['PSD_convex_certificates'][-2]['control_matrix']]
    endpoint=[[Q(*x) for x in row] for row in full['families'][0]['matrix']]
    for e in data['coefficient_entries']:
        i,j=e['i'],e['j']; g=choose(68,i)*choose(956,i)
        require((i,j) not in rows,'unique ordered coefficient entry')
        ts=range(max(0,i+j-68),min(i,j)+1)
        ss=range(max(0,i+j-956),min(i,j)+1)
        require(e['t']==list(ts) and e['s']==list(ss),'complete orbit ranges')
        # Multinomial ratios are reconstructed from factorials, without
        # the generator's product-of-binomials coefficient routine.
        af=[factorial(68)//(factorial(i-t)*factorial(j-t)*factorial(t)*factorial(68-i-j+t)) for t in ts]
        bf=[factorial(956)//(factorial(i-s)*factorial(j-s)*factorial(s)*factorial(956-i-j+s)) for s in ss]
        require(af==e['source_inside_multinomials'] and bf==e['source_outside_multinomials'], 'all source factors')
        hc={}; mc={}
        for ti,t in enumerate(ts):
            for si,s in enumerate(ss):
                h=i+j-t-s
                product=af[ti]*bf[si]
                require(product%g==0 and product//g==e['inside_factors'][ti]*e['outside_factors'][si],
                        'every source coefficient')
                hc[h]=hc.get(h,0)+product//g
                mc[h]=mc.get(h,0)+1
                orbits+=1
        require(e['h_coefficients']==[[h,c] for h,c in sorted(hc.items())] and
                e['h_orbit_multiplicities']==[[h,c] for h,c in sorted(mc.items())], 'complete aggregated rows')
        total=Q(0); old=Q(0)
        for h,c in hc.items():
            value=Q(0) if any(0<k<5 for k in (i,j,h)) else p[sorted((i,j,h))[1]] if min(i,j,h)==0 else p[i]*p[j]*p[h]/p[68]
            control=a*value+(1-a)*int(i==j==h==0)
            r=records.pop((i,j,h))
            require(r['orbits']==mc[h] and Q(r['z_numerator'],yd)==value,'full numerical orbit record')
            slacks=[control,cp[i]-control,1+control-cp[i]-cp[j]]
            require([Q(x,cd) for x in r['control_slack_numerators']]==slacks and all(x>=0 for x in slacks),'all control scalar rows')
            total+=c*control; old+=c*value
        require(g*old==endpoint[i][j], 'independent frozen source beta entry')
        require(g*total==control_matrix[i][j], 'complete convex source entry')
        rows[i,j]=total; entry_checks+=1
    require(entry_checks==4761 and not records and orbits==1500625,'full exact coverage')
    independent=[]
    for i,r in enumerate(data['contractions']):
        g=choose(68,i)*choose(956,i)
        lhs=sum(rows[i,j] for j in range(69))
        matrix_lhs=(a*sum(endpoint[i])+(1-a)*int(i==0))/g
        rhs=N*cp[i]; residual=lhs-rhs
        require(lhs==matrix_lhs==Q(*r['lhs']) and rhs==Q(*r['rhs']) and residual==Q(*r['residual']),
                'all complete contraction residuals')
        require(r['holds']==(residual==0),'all equality decisions')
        if i>=5:
            require(residual>0 and Q(1383,1000)<lhs/rhs<Q(1384,1000),'positive residual and strict ratio bounds')
        else: require(residual==0,'zero and forbidden controls')
        independent.append({'i':i,'residual':enc(residual),'source_row_sum_lhs':enc(matrix_lhs)})
    out={'verified':not fail,'failures':fail,'coefficient_products':orbits,
         'complete_source_matrix_entries':entry_checks,'complete_rows':69,
         'independent_rows':independent,'nonzero_failures':64,
         'all_nonzero_lhs_over_rhs_interval':[1383,1384,1000],
         'inherited_controls_pass':data['summary']['inherited_controls_pass']}
    OUT.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print('Verified:',not fail,'; full coefficient products:',orbits,'; source matrix entries:',entry_checks)
    print('64/64 nonzero residuals > 0; each LHS/RHS strictly between 1.383 and 1.384; required 1.')
    print('Failures:',len(fail),'; full independent certificate:',OUT)
    if fail: raise SystemExit(1)
if __name__=='__main__': main()

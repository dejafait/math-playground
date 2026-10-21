"""Two unchanged necessary separators on the original L076 column family.

Exact arithmetic only. A common witness does not certify PSD completion.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, det, cramer, basis_solve, enc

sys.set_int_max_str_digits(0)
beta = lru_cache(None)(beta)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'eight-two-separator-intersection-results.json'
I1 = [1,2,3,4,7,9,10,11,12,14,15,18,19,20,21,22,23,24,27,28,29,30,31,32,33,36,37,38,39,40,45,46,47,48,49,54,55,56,57,64,72,73]
J1 = [-1,0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,39,41,42,43,44]
I2 = [0,1,2,5,6,9,10,11,12,13,14,15,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,36,37,38,39,40,45,46,47,48,54,55,56,57,63,64,72]
J2 = [-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,38,39,40,41,42,43,44]


def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def av(x): return [F(x)]+[F(0)]*4
def quadratic(M,z): return dot(z,[dot(r,z) for r in M])
def interval(v):
    k=v.numerator*10**6//v.denominator
    return [F(k,10**6),F(k+1,10**6)]


def main():
    names = ['eight-family-fixed-separator-results.json',
             'eight-family-fixed-separator-critical-audit.json',
             'eight-maximizer-joint-completion-results.json',
             'eight-maximizer-joint-completion-critical-audit.json',
             'eight-distance-full-base-kernel-results.json',
             'maximizer-excluded-anchor-results.json',
             'simultaneous-eight-shell-results.json']
    paths = [ROOT/n for n in names]
    family,fa,second,sa,col,old,first = [json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    def check(name,ok):
        checks.append(name)
        if not ok: failures.append(name)
    out={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def save(stage):
        out.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(out),indent=2)+'\n')
    for n,d in zip(names,[family,fa,second,sa,col,old,first]):
        check('clean_'+n,not d['failures'])
        for rel,h in d.get('input_hashes',{}).items():
            check('hash_'+n+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    fs=[[F(*v)]+[F(*x) for x in row] for v,row in zip(col['affine']['intercept'],col['affine']['slopes'])]
    check('identical_85_row_domain',enc(fs)==family['domain']['nonnegative_affine'] and col['affine']['free_indices']==[56,63,69,78])
    for j,(row,rhs) in enumerate(zip(col['equations'],col['rhs'])):
        check('original_affine_kernel_'+str(j),[sum(F(*v)*f[k] for v,f in zip(row,fs)) for k in range(5)]==av(F(*rhs)))
    p=[F(*v) for v in old['pairs_through_14']]
    check('original_normalization',F(*old['rho'])>0 and p[8]==F(16792471,1181138102168120460)>0)
    entries={tuple(r['type']):None if r['affine'] is None else [F(*x) for x in r['affine']] for r in family['records']}
    check('all_500_types_3000_presentations',len(entries)==500 and sum(len(r['presentations']) for r in family['records'])==3000)
    check('unchanged_full_key_domain',not family['domain']['key_equalities'] and not any(any(F(*v) for v in r) for r in family['domain']['all_key_residuals']))
    for rec in family['records']:
        y=entries[tuple(rec['type'])]
        for j,pr in enumerate(rec['presentations']):
            if pr['affine'] is not None:
                check('key_coefficients_'+str((rec['type'],j)),[F(*v) for v in pr['affine']]==y)
    check('270_unchanged_old_entries',all(entries[tuple(r['type'])]==av(F(*r['y'])) for r in old['entries']))
    free=[tuple(rq) for rq in family['free']]
    check('45_free_36_forced',free==[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8] and sum(l==m==8 and v is not None for (l,m,i,j),v in entries.items())==36)
    sizes={l:C(68,l)*C(956,l) for l in [5,6,7,8]}
    modes=[];matrix=[]
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b; layers=[l for l in [5,6,7] if max(a,b)<=l]
        def block(l,m):
            ll,mm=sorted([l,m]);v=av(0)
            for i,j in it.product(range(ll+1),repeat=2):
                coef=beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j)
                v=[x+coef*y for x,y in zip(v,entries[ll,mm,i,j])]
            if a==b==0:v[0]-=p[l]*p[m]*sizes[l]*sizes[m]
            return v
        B=[[block(l,m)[0] for m in layers] for l in layers]
        cross=[block(l,8) for l in layers];selected=[];minors=[]
        for k in range(1,len(B)+1):
            for inds in it.combinations(range(len(B)),k):
                d=det([[B[i][j] for j in inds] for i in inds]);minors.append(d)
                check('old_psd_'+str((a,b,inds)),d>=0)
                if d>0:selected=inds
        X=[[F(0)]*5 for _ in B]
        if selected:
            BB=[[B[i][j] for j in selected] for i in selected]
            for k in range(5):
                for j,v in zip(selected,cramer(BB,[cross[i][k] for i in selected])):X[j][k]=v
        residuals=[[sum(B[i][j]*X[j][k] for j in range(len(B)))-cross[i][k] for k in range(5)] for i in range(len(B))]
        check('all_affine_singular_ranges_'+str(idx),not any(any(r) for r in residuals))
        D8=C(68-2*a,8-a)*C(956-2*b,8-b)
        check('positive_normalization_'+str(idx),D8>0)
        cost=[[sum(cross[j][k]*X[j][h] for j in range(len(B)))/(p[8]*D8) for h in range(5)] for k in range(5)]
        fixed=av(0)
        for (l,m,i,j),y in entries.items():
            if l==m==8 and y is not None:
                coef=F(beta(68,8,8,a,i)*beta(956,8,8,b,j),p[8]*D8)
                fixed=[x+coef*v for x,v in zip(fixed,y)]
        if a==b==0:fixed[0]-=p[8]*sizes[8]
        row=[-F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),D8*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
        saved=family['modes'][idx]
        check('common_family_mode_'+str(idx),enc(cost)==saved['required_quadratic'] and enc(fixed)==saved['fixed_minus_anchor_affine'] and enc(cross)==saved['cross_affine'] and enc(B)==saved['base'])
        check('original_mode_row_'+str(idx),enc(row)==family['matrix'][idx]==first['matrix'][idx]==second['matrix'][idx])
        Q=[[-v for v in r] for r in cost];Q[0][0]+=fixed[0]
        for j in range(1,5):Q[0][j]+=fixed[j]/2;Q[j][0]+=fixed[j]/2
        check('symmetric_mode_quadratic_'+str(idx),Q==list(map(list,zip(*Q))))
        modes.append({'mode':[a,b],'base':B,'cross':cross,'inverse_affine':X,'range_residuals':residuals,'cost':cost,'fixed_minus_anchor':fixed,'quadratic':Q,'D8':D8})
        matrix.append(row)
    out.update(domain=fs,free=free,modes=modes,matrix=matrix)
    save('common_mode_system_rebuilt')
    print('Common system: 85 domain rows; 500 keys/3000 presentations; 81 modes; failures:',failures,flush=True)
    pairings=[]
    for label,I,J,saved,positive,rq in [('L078',I1,J1,first,27,(3,6)),('L080',I2,J2,second,38,(6,3))]:
        K=[[F(-1) if j==-1 else matrix[i][j] for j in J] for i in I]
        weights,pivots=basis_solve(list(map(list,zip(*K))),[F(-1) if j==-1 else F(0) for j in J])
        y=[F(0)]*81
        for i,v in zip(I,weights):y[i]=v
        check(label+'_canonical_weights',enc(y)==saved['exact']['dual'] and min(y)>=0 and sum(y)==1 and sum(v>0 for v in y)==positive and all(pivots))
        sums=[sum(w*r[j] for w,r in zip(y,matrix)) for j in range(45)]
        raw=[s*C(8,r)*C(60,r)*C(8,q)*C(948,q)/p[8] for s,(r,q) in zip(sums,free)]
        check(label+'_scaled_raw_signs',min(sums)>=0 and sum(s==0 for s in sums)==44 and [v for v,s in zip(free,sums) if s>0]==[rq])
        rawkey='raw_moment_column_sums' if label=='L078' else 'raw_sums'
        check(label+'_original_raw_sums',enc(raw)==saved['exact'][rawkey])
        M=[[sum(y[k]*modes[k]['quadratic'][i][j] for k in range(81)) for j in range(5)] for i in range(5)]
        H=[[-M[i][j] for j in range(1,5)] for i in range(1,5)];R=[r[:] for r in H];squares=[]
        for _ in range(4):
            j=next((j for j in range(4) if R[j][j]>0),None)
            if j is None:break
            pivot=R[j][j];v=[r[j] for r in R]
            squares.append({'coordinate':j,'pivot':pivot,'vector':v})
            R=[[x-v[i]*v[k]/pivot for k,x in enumerate(r)] for i,r in enumerate(R)]
        check(label+'_concave_quadratic',not any(any(r) for r in R))
        pp=[F(*v) for v in (family['original_point'] if label=='L078' else second['point'])]
        vv=quadratic(M,pp)
        check(label+'_original_fixed_pairing',enc(vv)==saved['exact']['fixed_value' if label=='L078' else 'value'])
        if label=='L078':check('L079_pairing_retained',enc(M)==family['objective_matrix'])
        pairings.append({'label':label,'I':I,'J':J,'pivots':pivots,'weights':y,'scaled_sums':sums,'raw_sums':raw,'M':M,'H':H,'square_decomposition':squares,'curvature_residual':R})
    out['pairings']=pairings;save('both_pairings_rebuilt')
    print('Both unchanged separators rebuilt; curvature ranks:',[len(x['square_decomposition']) for x in pairings],'; failures:',failures,flush=True)
    if failures:raise SystemExit(1)
    ends=[cramer([fs[j][1:] for j in inds],[-fs[j][0] for j in inds]) for inds in [[27,33,56,63],[5,26,33,56]]]
    endpoints=[[F(1)]+t for t in ends]
    check('admissible_line_endpoints',all(min(dot(f,z) for f in fs)>=0 for z in endpoints))
    trials=[];witness=None
    for k in range(257):
        alpha=F(k,256);z=[x+alpha*(y-x) for x,y in zip(*endpoints)]
        values=[quadratic(d['M'],z) for d in pairings]
        trials.append({'alpha':alpha,'pairings':values})
        if min(values)>=0:
            signs=[dot(f,z) for f in fs]
            check('witness_85_nonnegative',min(signs)>=0)
            bounds=[quadratic(m['quadratic'],z) for m in modes]
            check('witness_original_81_pairings',all(dot(d['weights'],bounds)==v for d,v in zip(pairings,values)))
            for j,(r,b) in enumerate(zip(col['equations'],col['rhs'])):
                check('witness_original_kernel_'+str(j),dot([F(*v) for v in r],signs)==F(*b))
            witness={'alpha':alpha,'point':z,'column_factors':signs,'mode_rhs':bounds,'pairings':values,'pairing_intervals':[interval(v) for v in values]}
            break
    out.update(endpoints=endpoints,line_trials=trials,witness=witness)
    out['summary']={'verdict':'COMMON_WITNESS' if witness else 'BOUNDED_LINE_INCONCLUSIVE','checks':len(checks),'failures':len(failures),'curvature_ranks':[len(x['square_decomposition']) for x in pairings],
                    'required_domain_minimum':0,'required_pairing_minimum':0,'line_trials':len(trials)}
    if witness:out['summary'].update(alpha=witness['alpha'],actual_domain_minimum=min(signs),positive_factors=sum(v>0 for v in signs),zero_factors=[j for j,v in enumerate(signs) if v==0],pairing_intervals=witness['pairing_intervals'])
    save('completed');print(enc(out['summary']),flush=True);print('Full certificate:',OUT.relative_to(NB),flush=True)
    if failures:raise SystemExit(1)


if __name__=='__main__':main()

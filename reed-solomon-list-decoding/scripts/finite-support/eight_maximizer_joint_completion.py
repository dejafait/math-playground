"""Approved fixed L079 maximizer: exact original-row joint completion.
Decimal simplex proposes a basis only; all verdicts use rational arithmetic.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
from simultaneous_five_six_shell import propose, solve, c, beta
from eight_distance_full_base_kernel import enc
from simultaneous_eight_shell import eliminate

sys.set_int_max_str_digits(0)
beta=lru_cache(None)(beta)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'eight-maximizer-joint-completion-results.json'

def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
def main():
    names=['eight-family-fixed-separator-results.json','eight-family-fixed-separator-verification.json',
           'eight-family-fixed-separator-critical-audit.json','maximizer-excluded-anchor-results.json',
           'eight-distance-full-base-kernel-results.json','simultaneous-eight-shell-results.json']
    paths=[ROOT/n for n in names]
    family,verified,audit,old,col,fixed=[json.loads(p.read_text()) for p in paths]
    checks=[];failures=[]
    def check(n,ok):
        checks.append(n)
        if not ok:failures.append(n)
    out={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def save(stage):
        out.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(out),indent=2)+'\n')
    for n,data in zip(names,[family,verified,audit,old,col,fixed]):
        check('clean_'+n,not data['failures'])
        for rel,h in data.get('input_hashes',{}).items():
            check('hash_'+n+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    p=[F(*v) for v in old['pairs_through_14']]
    fs=[[F(*a)]+[F(*v) for v in row] for a,row in zip(col['affine']['intercept'],col['affine']['slopes'])]
    M=[[F(*v) for v in r] for r in family['objective_matrix']]
    sstar=M[0][4]/(-M[4][4])
    I0=[27,33,56,63];J0=[5,26,33,56]
    ends=[solve([fs[j][1:] for j in inds],[-fs[j][0] for j in inds]) for inds in [I0,J0]]
    alpha=(sstar-ends[0][3])/(ends[1][3]-ends[0][3])
    point=[F(1)]+[x+alpha*(y-x) for x,y in zip(*ends)]
    check('exact_L079_interpolation',0<alpha<1 and enc(point)==family['optimization']['point'])
    signs=[dot(f,point) for f in fs]
    check('original_positive_normalization',F(*old['rho'])>0 and p[8]==F(16792471,1181138102168120460)>0)
    check('85_column_signs',min(signs)>=0)
    for i,(r,b) in enumerate(zip(col['equations'],col['rhs'])):
        check('original_kernel_'+str(i),dot([F(*v) for v in r],signs)==F(*b))
    entries={tuple(rec['type']):None if rec['affine'] is None else dot([F(*v) for v in rec['affine']],point) for rec in family['records']}
    check('270_immutable_entries',all(entries[tuple(r['type'])]==F(*r['y']) for r in old['entries']))
    free=[tuple(rq) for rq in family['free']]
    check('free_partition',free==[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8])
    check('36_forced_nonnegative',sum(l==m==8 and v is not None for (l,m,i,j),v in entries.items())==36 and all(v>=0 for v in entries.values() if v is not None))
    out.update(point=point,alpha=alpha,endpoints=ends,free=free,column_signs=signs)
    save('fixed_point_saved')
    sizes={l:c(68,l)*c(956,l) for l in [5,6,7,8]}
    modes=[];A=[];rhs=[]
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b;ls=[l for l in [5,6,7] if l>=max(a,b)]
        def block(l,m):
            ll,mm=sorted([l,m])
            v=sum(beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j)*entries[ll,mm,i,j] for i,j in it.product(range(ll+1),repeat=2))
            return v-p[l]*p[m]*sizes[l]*sizes[m] if a==b==0 else v
        B=[[block(l,m) for m in ls] for l in ls];cross=[block(l,8) for l in ls]
        cost,pivots,ranges=eliminate(B,cross)
        D8=c(68-2*a,8-a)*c(956-2*b,8-b)
        fixedpart=sum(beta(68,8,8,a,i)*beta(956,8,8,b,j)*v/(p[8]*D8) for (l,m,i,j),v in entries.items() if l==m==8 and v is not None)
        anchor=p[8]*sizes[8] if a==b==0 else F(0)
        bound=fixedpart-anchor-cost/(p[8]*D8)
        row=[-F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),D8*c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
        fm=family['modes'][idx]
        check('same_original_rows_'+str(idx),enc(row)==family['matrix'][idx])
        check('specialized_original_bound_'+str(idx),bound==dot([F(*v) for v in fm['fixed_minus_anchor_affine']],point)-dot(point,[dot([F(*v) for v in r],point) for r in fm['required_quadratic']]))
        check('positive_scale_'+str(idx),D8>0)
        modes.append({'mode':[a,b],'layers':ls,'base':B,'cross':cross,'pivots':pivots,'ranges':ranges,'D8':D8,'cost':cost,'fixed':fixedpart,'anchor':anchor})
        A.append(row);rhs.append(bound)
    out.update(matrix=A,rhs=rhs,modes=modes)
    save('original_system_saved')
    print('Original system: 81 modes, 45 nonnegative unknowns; fixed-point/range failures:',failures,flush=True)
    if failures:raise SystemExit(1)
    discovery=propose(A,rhs);out['discovery']=discovery;save('basis_proposal_saved')
    m,n=81,45
    rows=[i for i in range(m) if n+i not in discovery['basis']]
    columns=sorted(j for j in discovery['basis'] if j<n)
    exact={};verdict='INCONCLUSIVE'
    if discovery['status']=='feasible_proposal' and -1 not in columns:
        vals=solve([[A[i][j] for j in columns] for i in rows],[rhs[i] for i in rows])
        z=[F(0)]*n
        for j,v in zip(columns,vals):z[j]=v
        slacks=[v-dot(r,z) for r,v in zip(A,rhs)]
        valid=min(z+slacks)>=0
        exact={'kind':'PRIMAL','rows':rows,'columns':columns,'z':z,'slacks':slacks,'valid':valid}
        if valid:verdict='FEASIBLE'
    elif discovery['status']=='infeasible_proposal' and -1 in columns:
        K=[[F(-1) if j==-1 else A[i][j] for j in columns] for i in rows]
        vals=solve(list(map(list,zip(*K))),[F(-1) if j==-1 else F(0) for j in columns])
        y=[F(0)]*m
        for i,v in zip(rows,vals):y[i]=v
        sums=[sum(y[i]*A[i][j] for i in range(m)) for j in range(n)]
        value=dot(y,rhs);valid=min(y+sums)>=0 and value<0
        raw=[v*c(8,r)*c(60,r)*c(8,q)*c(948,q)/p[8] for v,(r,q) in zip(sums,free)]
        exact={'kind':'FARKAS','rows':rows,'columns':columns,'dual':y,'sums':sums,'raw_sums':raw,'value':value,'valid':valid}
        if valid:verdict='EXCLUDED'
    out['exact']=exact
    out['summary']={'verdict':verdict,'proposal':discovery['status'],'checks':len(checks),'failures':len(failures),'modes':81,'unknowns':45}
    if verdict=='FEASIBLE':out['summary'].update(positive_variables=sum(v>0 for v in z),positive_slacks=sum(v>0 for v in slacks),minimum_variable=min(z),minimum_slack=min(slacks))
    if verdict=='EXCLUDED':
        k=value.numerator*10**6//value.denominator
        out['summary'].update(positive_weights=sum(v>0 for v in y),zero_sums=sum(v==0 for v in sums),value_interval=[F(k,10**6),F(k+1,10**6)])
    save('completed')
    print(enc(out['summary']),flush=True);print('Full certificate:',OUT.relative_to(NB),flush=True)

if __name__=='__main__':main()

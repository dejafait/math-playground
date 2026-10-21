"""Independent fixed-L081 common-column verification; standard library only, no optimizer."""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'eight-common-column-joint-completion-verification.json'


def enc(x):
    if isinstance(x,Q):return [x.numerator,x.denominator]
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x


def C(n,k):return comb(n,k) if 0<=k<=n else 0


@lru_cache(None)
def beta(n,l,m,a,k):
    return sum((-1)**(u-k)*C(u,k)*C(n-2*a,u-a)*C(n-a-u,l-u)*C(n-a-u,m-u)
               for u in range(max(a,k),min(l,m,n-a)+1))


def solve(A,b):
    n=len(b);M=[[Q(x) for x in r]+[Q(v)] for r,v in zip(A,b)]
    for j in range(n):
        k=next(k for k in range(j,n) if M[k][j]);M[j],M[k]=M[k],M[j]
        d=M[j][j];M[j]=[x/d for x in M[j]]
        for k in range(n):
            if k!=j:
                d=M[k][j];M[k]=[x-d*y for x,y in zip(M[k],M[j])]
    return [r[-1] for r in M]


def determinant(A):
    M=[r[:] for r in A];d=Q(1)
    for j in range(len(M)):
        k=next((k for k in range(j,len(M)) if M[k][j]),None)
        if k is None:return Q(0)
        if k!=j:M[j],M[k]=M[k],M[j];d=-d
        v=M[j][j];d*=v
        for k in range(j+1,len(M)):
            q=M[k][j]/v
            for h in range(j+1,len(M)):M[k][h]-=q*M[j][h]
    return d


def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))


def av(x):return [Q(x)]+[Q(0)]*4


def main():
    names=['eight-common-column-joint-completion-results.json','eight-family-fixed-separator-results.json',
           'maximizer-excluded-anchor-results.json','eight-distance-full-base-kernel-results.json',
           'eight-family-fixed-separator-critical-audit.json','eight-two-separator-intersection-results.json',
           'eight-two-separator-critical-audit.json']
    paths=[ROOT/n for n in names]
    data,family,old,col,audit,assembly,common=[json.loads(p.read_text()) for p in paths]
    checks=[];failures=[]
    def check(n,ok):
        checks.append(n)
        if not ok:failures.append(n)
    for n,d in zip(names,[data,family,old,col,audit,assembly,common]):
        check('clean_'+n,not d['failures'])
        for rel,h in d.get('input_hashes',{}).items():
            check('hash_'+n+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    p=[Q(*v) for v in old['pairs_through_14']]
    nonpiv=[56,63,69,78]
    rr=[[Q(*v) for v in row] for row in col['equation_rref']]
    fs=[[Q(0)]*5 for _ in range(85)]
    for k,j in enumerate(nonpiv):fs[j][k+1]=Q(1)
    for i,j in enumerate(col['equation_pivots']):fs[j]=[rr[i][-1]]+[-rr[i][k] for k in nonpiv]
    check('original_RREF_family',enc([r[0] for r in fs])==col['affine']['intercept'] and enc([r[1:] for r in fs])==col['affine']['slopes'])
    Ms=[[[Q(*v) for v in r] for r in q['M']] for q in assembly['pairings']]
    sstar=-Ms[0][0][4]/Ms[0][4][4]
    G=[[Ms[1][i][j] for j in [2,3]] for i in [2,3]]
    g=[Ms[1][i][0]+Ms[1][i][4]*sstar for i in [2,3]]
    check('nonzero_stationary_determinant',determinant(G)!=0)
    u,v=solve(G,[-x for x in g]);point=[Q(1),Q(0),u,v,sstar]
    check('exact_original_L081_point',enc(point)==data['point']==common['point'])
    check('positive_original_scale',Q(*old['rho'])>0 and p[8]==Q(16792471,1181138102168120460)>0 and old['pairs_through_14']==col['pairs_through_14'])
    signs=[dot(f,point) for f in fs]
    for j,v in enumerate(signs):check('column_sign_'+str(j),v>=0)
    for i,(r,b) in enumerate(zip(col['equations'],col['rhs'])):
        check('original_compatibility_'+str(i),sum(Q(*v)*f for v,f in zip(r,signs))==Q(*b))
    base={tuple(r['type']):Q(*r['y']) for r in old['entries']}
    for r in col['column']:
        if r['orbit']!=[0,0,0]:
            base[r['orbit'][0],8,*r['orbit'][1:]]=p[8]*signs[r['variable']] if r['kind']=='free' else Q(*r['value'])
    column=[p[8]]+[base[tuple([r['orbit'][0],8,*r['orbit'][1:]])] for r in col['column'][1:]]
    W=[1]+[C(8,i)*C(60,l-i)*C(8,j)*C(948,l-j) for l,i,j in col['orbits'][1:]]
    weighted_residuals=[]
    for j,k in enumerate(col['kernel_basis']):
        residual=sum(Q(*x)*w*v for x,w,v in zip(k,W,column));weighted_residuals.append(residual)
        check('whole_weighted_kernel_'+str(j),residual==0)
    check('90_full_weighted_residuals',len(weighted_residuals)==90 and len(column)==150)
    entries={};dictionary={};records=[];free=[];free_keys=[]
    for l,m in it.combinations_with_replacement([5,6,7,8],2):
        for i,j in it.product(range(l+1),repeat=2):
            atoms=[956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
            sets=[set(),set(),set()];start=0
            for mask,count in enumerate(atoms):
                for k,bit in enumerate([4,2,1]):
                    if mask&bit:sets[k].update(range(start,start+count))
                start+=count
            check('valid_actual_supports_'+str((l,m,i,j)),min(atoms)>=0 and start==1024 and all(len(s)==68 for s in sets))
            orders=[];vals=[];prs=[]
            for kk,(D,E,G) in enumerate(it.permutations(sets)):
                aa=[0]*8
                for x in range(1024):aa[4*(x in D)+2*(x in E)+(x in G)]+=1
                ds=[len(D-E),len(D-G),len(E-G)];v=None
                if 0 in ds:v=p[max(ds)]
                elif any(0<d<5 for d in ds):v=Q(0)
                else:
                    typ=(*sorted(ds[:2]),len((D-E)&(D-G)),len((E-D)&(G-D)))
                    v=base.get(typ)
                orders.append(tuple(aa));prs.append({'atoms':aa,'distances':ds,'value':v})
                famrec=family['records'][len(records)]['presentations'][kk]
                fv=None if famrec['affine'] is None else dot([Q(*w) for w in famrec['affine']],point)
                check('original_presentation_'+str((l,m,i,j,kk)),aa==famrec['atoms'] and ds==famrec['distances'] and v==fv)
                if v is not None:vals.append(v)
            key=min(orders)
            if key in dictionary:vals.append(dictionary[key])
            value=vals[0] if vals else None
            check('all_shared_key_values_'+str((l,m,i,j)),all(v==value for v in vals))
            if value is not None:
                dictionary[key]=value;check('forced_sign_'+str((l,m,i,j)),value>=0)
            else:
                check('only_eight_eight_free_'+str((l,m,i,j)),l==m==8)
                free.append((8-i,8-j));free_keys.append(key)
            entries[l,m,i,j]=value
            records.append({'type':[l,m,i,j],'key':key,'value':value,'presentations':prs})
    free.sort()
    check('complete_500_types_45_free',len(entries)==500 and len(free_keys)==len(set(free_keys))==45 and free==list(map(tuple,data['free'])))
    for r,q in it.product(range(9),repeat=2):
        if r+q>=8:continue
        actual=entries[8,8,8-r,8-q]
        expected=p[8] if r+q==0 else Q(0) if r+q<=4 else entries[r+q,8,q,r]
        check('original_forced_88_'+str((r,q)),actual==expected)
    sizes={l:C(68,l)*C(956,l) for l in [5,6,7,8]}
    modes=[];matrix=[];rhs=[];old_minors=[]
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b;ls=[l for l in [5,6,7] if l>=max(a,b)]
        def block(l,m):
            ll,mm=sorted([l,m])
            v=sum(beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j)*entries[ll,mm,i,j] for i,j in it.product(range(ll+1),repeat=2))
            if a==b==0:v-=p[l]*p[m]*sizes[l]*sizes[m]
            return v
        B=[[block(l,m) for m in ls] for l in ls];t=[block(l,8) for l in ls];selected=[]
        for k in range(1,len(ls)+1):
            for inds in it.combinations(range(len(ls)),k):
                d=determinant([[B[i][j] for j in inds] for i in inds]);old_minors.append(d)
                check('old_minor_'+str((a,b,inds)),d>=0)
                if d>0:selected=inds
        x=[Q(0)]*len(ls)
        if selected:
            sub=[[B[i][j] for j in selected] for i in selected]
            for i,v in zip(selected,solve(sub,[t[i] for i in selected])):x[i]=v
        residuals=[dot(r,x)-v for r,v in zip(B,t)]
        check('whole_mode_range_'+str((a,b)),not any(residuals))
        cost=dot(t,x);d8=C(68-2*a,8-a)*C(956-2*b,8-b)
        fixed=sum(beta(68,8,8,a,i)*beta(956,8,8,b,j)*v/(p[8]*d8) for (l,m,i,j),v in entries.items() if l==m==8 and v is not None)
        anchor=p[8]*sizes[8] if a==b==0 else Q(0)
        bound=fixed-anchor-cost/(p[8]*d8)
        row=[-Q(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),d8*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
        check('all_original_entries_'+str((a,b)),enc(B)==data['modes'][idx]['base'] and enc(t)==data['modes'][idx]['cross'])
        check('all_original_bounds_'+str((a,b)),enc(bound)==data['rhs'][idx] and enc(cost)==data['modes'][idx]['cost'])
        check('all_45_original_coefficients_'+str((a,b)),enc(row)==data['matrix'][idx])
        check('positive_source_normalization_'+str((a,b)),d8>0 and (C(68,a)-C(68,a-1))*(C(956,b)-C(956,b-1))>0)
        modes.append({'mode':[a,b],'layers':ls,'base':B,'cross':t,'inverse':x,'residuals':residuals,'D8':d8,'fixed':fixed,'anchor':anchor,'required':cost/(p[8]*d8)})
        matrix.append(row);rhs.append(bound)
    # Exact certificate reconstruction from the proposed original-row basis.
    I=[0,1,2,3,4,5,6,7,9,10,11,12,13,15,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32,36,37,38,39,40,41,45,46,47,48,54,55,56,57,63,64,72]
    J=[-1]+list(range(45))
    check('canonical_original_basis',I==data['exact']['rows'] and J==data['exact']['columns'])
    if data['exact']['kind']=='FARKAS':
        K=[[Q(-1) if j==-1 else matrix[i][j] for j in J] for i in I]
        weights=solve(list(map(list,zip(*K))),[Q(-1) if j==-1 else Q(0) for j in J]);y=[Q(0)]*81
        for i,v in zip(I,weights):y[i]=v
        check('original_dual_basis',enc(y)==data['exact']['dual'])
        for i,v in enumerate(y):check('weight_sign_'+str(i),v>=0)
        check('normalization_sum_one',sum(y)==1)
        sums=[sum(y[i]*matrix[i][j] for i in range(81)) for j in range(45)]
        raw=[]
        for k,(r,q) in enumerate(free):
            rawsum=-sum(y[idx]*Q(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),p[8]*modes[idx]['D8']) for idx,(a,b) in enumerate(it.product(range(9),repeat=2)))
            raw.append(rawsum)
            check('original_raw_coefficient_'+str(k),rawsum==sums[k]*C(8,r)*C(60,r)*C(8,q)*C(948,q)/p[8] and rawsum>=0)
        check('scaled_sums',enc(sums)==data['exact']['sums'] and min(sums)>=0)
        check('raw_sums',enc(raw)==data['exact']['raw_sums'])
        fixed=dot(y,[m['fixed'] for m in modes]);anchor=dot(y,[m['anchor'] for m in modes]);required=dot(y,[m['required'] for m in modes]);value=dot(y,rhs)
        check('full_fixed_anchor_cost_pairing',value==fixed-anchor-required and enc(value)==data['exact']['value'])
        lo,hi=[Q(*v) for v in data['summary']['value_interval']]
        check('strict_negative_interval',lo<=value<hi<=0 and value<0)
        check('28_positive_weights_full_cancellation',sum(v>0 for v in y)==28 and sums==[0]*45 and raw==[0]*45)
        decimal_scale=1
        while -value*decimal_scale<1:decimal_scale*=10
        decimal_scale*=10**6
        lower=value.numerator*decimal_scale//value.denominator
        finer=[Q(lower,decimal_scale),Q(lower+1,decimal_scale)]
        check('fine_strict_interval',finer[0]<=value<finer[1]<0)
        positive=[rq for rq,v in zip(free,sums) if v>0]
        summary={'verdict':'EXCLUDED' if not failures else 'FAILED','positive_weights':sum(v>0 for v in y),'zero_sums':sum(v==0 for v in sums),'positive_moment_coordinates':positive,'required_pairing_lower_bound':0,'actual_pairing_interval':finer}
        report={'dual':y,'scaled_sums':sums,'raw_sums':raw,'weighted_fixed':fixed,'weighted_anchor':anchor,'weighted_required':required,'pairing':value}
    else:raise ValueError('No exact certificate; verdict remains inconclusive')
    summary.update(checks=len(checks),failures=len(failures),types=len(entries),presentations=6*len(entries),original_modes=81,signs=45,old_principal_minors=len(old_minors),weighted_kernel_rows=90)
    report.update(input_hashes={str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},point=point,records=records,modes=modes,matrix=matrix,rhs=rhs,old_principal_minors=old_minors,weighted_kernel_residuals=weighted_residuals,checks=checks,failures=failures,summary=summary)
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print(enc(summary));print('Full certificate:',OUT.relative_to(NB))
    if failures:raise SystemExit(1)

if __name__=='__main__':main()

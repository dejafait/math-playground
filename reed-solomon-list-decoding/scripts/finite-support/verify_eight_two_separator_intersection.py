"""Original-row verification of the common point; no numerical optimizer.

Rebuild fixed-point entries, ranges, raw/scaled separators, and pairings.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from verify_eight_maximizer_joint_completion import C, beta, solve, determinant, enc

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'eight-two-separator-intersection-verification.json'


def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def quad(M,z):return dot(z,[dot(r,z) for r in M])


def main():
    names=['eight-two-separator-slice-results.json','eight-two-separator-intersection-results.json',
           'eight-family-fixed-separator-results.json','eight-distance-full-base-kernel-results.json',
           'maximizer-excluded-anchor-results.json','simultaneous-eight-shell-results.json',
           'eight-maximizer-joint-completion-results.json']
    paths=[ROOT/n for n in names]
    witness,assembly,family,col,old,first,second=[json.loads(p.read_text()) for p in paths]
    checks=[];failures=[]
    def check(n,v):
        checks.append(n)
        if not v:failures.append(n)
    out={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def save(stage):
        out.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(out),indent=2)+'\n')
    for n,d in zip(names,[witness,assembly,family,col,old,first,second]):
        check('clean_'+n,not d['failures'])
        for rel,h in d.get('input_hashes',{}).items():
            check('hash_'+n+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    p=[F(*v) for v in old['pairs_through_14']]
    fs=[[F(*v)]+[F(*x) for x in r] for v,r in zip(col['affine']['intercept'],col['affine']['slopes'])]
    Ms=[[[F(*v) for v in r] for r in q['M']] for q in assembly['pairings']]
    s=-Ms[0][0][4]/Ms[0][4][4]
    G=[[Ms[1][i][j] for j in [2,3]] for i in [2,3]]
    g=[Ms[1][i][0]+Ms[1][i][4]*s for i in [2,3]]
    check('nonsingular_two_coordinate_system',determinant(G)!=0)
    u,v=solve(G,[-x for x in g]);point=[F(1),F(0),u,v,s]
    check('independent_point_recipe',enc(point)==witness['point'])
    check('original_rho_and_p8',F(*old['rho'])>0 and p[8]==F(16792471,1181138102168120460)>0)
    factors=[dot(r,point) for r in fs]
    check('85_original_domain_rows',len(factors)==85 and min(factors)>=0 and enc(factors)==witness['column_factors'])
    check('exactly_one_zero',[j for j,f in enumerate(factors) if not f]==[56] and sum(f>0 for f in factors)==84)
    for j,(r,b) in enumerate(zip(col['equations'],col['rhs'])):
        check('original_kernel_'+str(j),dot([F(*v) for v in r],factors)==F(*b))
    entries={tuple(r['type']):F(*r['y']) for r in old['entries']}
    for r in col['column']:
        if r['orbit']==[0,0,0]:continue
        l,i,j=r['orbit'];entries[l,8,i,j]=p[8]*factors[r['variable']] if r['kind']=='free' else F(*r['value'])
    free=[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    entries.update({(8,8,8-r,8-q):p[8] if r==q==0 else F(0) if r+q<5 else entries[r+q,8,q,r]
                    for r,q in it.product(range(9),repeat=2) if r+q<=7})
    # Actual point-by-point atom construction, all six anchor presentations.
    D=set(range(68));dictionary={};records=[]
    for l,m in it.combinations_with_replacement([5,6,7,8],2):
        for i,j in it.product(range(l+1),repeat=2):
            E=(D-(set(range(i))|set(range(m,m+l-i))))|set(range(68,68+j))|set(range(68+m,68+m+l-j))
            H=(D-set(range(m)))|set(range(68,68+m))
            vals=[];keys=[]
            for A,B,Gg in it.permutations([D,E,H]):
                atoms=[0]*8
                for x in range(1024):atoms[4*(x in A)+2*(x in B)+(x in Gg)]+=1
                keys.append(tuple(atoms));ds=[len(A-B),len(A-Gg),len(B-Gg)]
                val=None
                if 0 in ds:val=p[max(ds)]
                elif any(0<h<5 for h in ds):val=F(0)
                else:
                    typ=(*sorted(ds[:2]),len((A-B)&(A-Gg)),len((B-A)&(Gg-A)))
                    if typ in entries:val=entries[typ]
                if val is not None:vals.append(val)
            key=min(keys);typ=(l,m,i,j)
            if key in dictionary:vals.append(dictionary[key])
            expected=entries.get(typ)
            check('complete_key_'+str(typ),all(x==expected for x in vals))
            if expected is not None:dictionary[key]=expected
            saved=family['records'][len(records)]
            check('identical_affine_lookup_'+str(typ),key==tuple(saved['key']) and expected==(None if saved['affine'] is None else dot([F(*v) for v in saved['affine']],point)))
            records.append({'type':typ,'keys':keys,'value':expected})
    check('500_types_3000_presentations',len(records)==500 and sum(len(r['keys']) for r in records)==3000)
    out.update(point=point,factors=factors,records=records,stationary_2by2=G,stationary_rhs=[-x for x in g]);save('point_and_keys_checked')
    sizes={l:C(68,l)*C(956,l) for l in [5,6,7,8]};matrix=[];rhs=[];modes=[]
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b;ls=[l for l in [5,6,7] if l>=max(a,b)]
        def block(l,m):
            ll,mm=sorted([l,m])
            val=sum(beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j)*entries[ll,mm,i,j] for i,j in it.product(range(ll+1),repeat=2))
            return val-p[l]*p[m]*sizes[l]*sizes[m] if a==b==0 else val
        B=[[block(l,m) for m in ls] for l in ls];cross=[block(l,8) for l in ls];sel=[]
        for k in range(1,len(B)+1):
            for ii in it.combinations(range(len(B)),k):
                minor=determinant([[B[i][j] for j in ii] for i in ii]);check('base_minor_'+str((a,b,ii)),minor>=0)
                if minor>0:sel=ii
        x=[F(0)]*len(ls)
        if sel:
            for j,z in zip(sel,solve([[B[i][j] for j in sel] for i in sel],[cross[i] for i in sel])):x[j]=z
        residuals=[dot(r,x)-y for r,y in zip(B,cross)]
        check('full_singular_range_'+str(idx),not any(residuals))
        D8=C(68-2*a,8-a)*C(956-2*b,8-b)
        fixed=sum(F(beta(68,8,8,a,i)*beta(956,8,8,b,j),p[8]*D8)*y for (l,m,i,j),y in entries.items() if l==m==8)
        anchor=p[8]*sizes[8] if a==b==0 else F(0);cost=dot(cross,x)/(p[8]*D8)
        bound=fixed-anchor-cost
        check('original_rhs_'+str(idx),bound==quad([[F(*v) for v in r] for r in assembly['modes'][idx]['quadratic']],point))
        row=[-F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),D8*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
        check('original_rows_'+str(idx),enc(row)==assembly['matrix'][idx])
        matrix.append(row);rhs.append(bound);modes.append({'mode':[a,b],'base':B,'cross':cross,'inverse':x,'range_residuals':residuals,'fixed':fixed,'anchor':anchor,'cost':cost,'bound':bound,'D8':D8})
    out.update(modes=modes,matrix=matrix,rhs=rhs);save('81_original_bounds_checked')
    print('Original entries and all 81 singular-mode bounds checked; failures:',failures,flush=True)
    certificates=[]
    for k,data in enumerate(assembly['pairings']):
        I,J=data['I'],data['J'];K=[[F(-1) if j==-1 else matrix[i][j] for j in J] for i in I]
        weights=solve(list(map(list,zip(*K))),[F(-1) if j==-1 else F(0) for j in J])
        y=[F(0)]*81
        for i,v in zip(I,weights):y[i]=v
        check('independent_dual_'+str(k),enc(y)==data['weights'] and enc(y)==[first,second][k]['exact']['dual'] and min(y)>=0 and sum(y)==1)
        sums=[dot(y,[r[j] for r in matrix]) for j in range(45)]
        raw=[-sum(y[9*a+b]*F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),p[8]*C(68-2*a,8-a)*C(956-2*b,8-b)) for a,b in it.product(range(9),repeat=2)) for r,q in free]
        check('independent_scaled_raw_'+str(k),enc(sums)==data['scaled_sums'] and enc(raw)==data['raw_sums'] and min(sums+raw)>=0 and sum(s==0 for s in sums)==44)
        value=dot(y,rhs)
        check('exact_positive_pairing_'+str(k),value>0 and value==quad(Ms[k],point) and enc(value)==witness['pairings'][k])
        lo,hi=[F(*v) for v in witness['summary']['pairing_intervals'][k]]
        check('rational_pairing_interval_'+str(k),0<lo<=value<hi)
        parts={key:dot(y,[m[key] for m in modes]) for key in ['fixed','anchor','cost']}
        check('complete_pairing_parts_'+str(k),parts['fixed']-parts['anchor']-parts['cost']==value)
        certificates.append({'label':data['label'],'weights':y,'scaled_sums':sums,'raw_sums':raw,'parts':parts,'pairing':value})
    out['certificates']=certificates
    out['summary']={'verdict':'COMMON_WITNESS_VERIFIED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),
                    'actual_minimum_factor':min(factors),'required_factor_bound':0,'required_pairing_bound':0,
                    'positive_factors':sum(v>0 for v in factors),'zero_factors':[i for i,f in enumerate(factors) if f==0],
                    'pairing_intervals':witness['summary']['pairing_intervals']}
    save('completed');print(enc(out['summary']));print('Full certificate:',OUT.relative_to(NB))
    if failures:raise SystemExit(1)


if __name__=='__main__':main()

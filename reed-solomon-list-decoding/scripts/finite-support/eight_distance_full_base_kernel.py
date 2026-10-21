"""Approved immutable distance-eight necessary kernel test.

Block-polynomial exact action exhausts all 150 stabilizer invariants.
Decimal phase I can propose an active set, never certify a verdict.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
from seven_distance_full_base_kernel import rref, atom_orders, atoms

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'eight-distance-full-base-kernel-results.json'
LAYERS = [5,6,7]
DISTANCE = 8


def c(n,k):
    return comb(n,k) if 0 <= k <= n else 0


def enc(x):
    if isinstance(x,F):
        return [x.numerator,x.denominator]
    if isinstance(x,dict):
        return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [enc(v) for v in x]
    return x


@lru_cache(None)
def transition(n,l,m,i,u,k):
    return sum(c(i,s)*c(8-i,u-s)*c(l-i,k-s)*c(n-8-l+i,m-u-k+s)
               for s in range(9))


def main():
    names = ['maximizer-excluded-anchor-results.json',
             'maximizer-excluded-anchor-critical-audit.json',
             'maximizer-completion-verification.json',
             'maximizer-seven-seven-scalars-results.json']
    paths = [ROOT/name for name in names]
    src,audit,inc,scalar = [json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    for name,data in zip(names,[src,audit,inc,scalar]):
        check('clean_'+name,not data['failures'])
        for rel,digest in data.get('input_hashes',data.get('source_hashes',{})).items():
            check('hash_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==digest)
    p=[F(*x) for x in src['pairs_through_14']]
    rho=F(*src['rho'])
    check('positive_normalization',rho>0 and p[8]>0)
    base,dictionary={},{}
    for row in src['entries']:
        typ=tuple(row['type']); y=F(*row['y'])
        base[typ]=y
        orders=atom_orders(atoms(*typ))
        check('original_six_presentations_'+str(typ),orders==[r['atoms'] for r in row['presentations']])
        check('original_nonnegative_'+str(typ),y>=0)
        key=min(map(tuple,orders))
        check('original_unordered_'+str(typ),key not in dictionary or dictionary[key]==y)
        dictionary[key]=y
    check('all_270_original_types',len(base)==270)
    check('all_immutable_scalar_entries',base=={tuple(r['type']):F(*r['y']) for r in scalar['all_records']})
    check('same_original_parameters',src['parameters']==scalar['parameters'])
    check('same_original_RREF_column',src['original_column']==scalar['original_RREF_column'])
    check('same_original_completion',src['completion_z']==scalar['same_original_basis_z'])
    for l,m,i,j in list(base):
        base[m,l,i,j]=base[l,m,i,j]
    # Complete orbit enumeration, with fixed lookup at every presentation.
    orbits=[(0,0,0)]+[(l,i,j) for l in LAYERS for i in range(l+1) for j in range(l+1)]
    weights=[1]+[c(8,i)*c(60,l-i)*c(8,j)*c(948,l-j) for l,i,j in orbits[1:]]
    records,free_keys=[],[]
    for index,(l,i,j) in enumerate(orbits):
        if l==0:
            records.append({'orbit':(l,i,j),'kind':'anchor','value':p[8]})
            continue
        aa=atoms(l,8,i,j); orders=atom_orders(aa); key=min(map(tuple,orders))
        distances=[l,8,l+8-i-j]
        check('actual_regions_'+str(index),all(min(a)>=0 and sum(a)==1024 and all(
            sum(a[k] for k in range(8) if k&b)==68 for b in [4,2,1]) for a in orders))
        forbidden=any(1<=h<=4 for h in distances)
        hits=[dictionary.get(min(map(tuple,atom_orders(a)))) for a in orders]
        check('all_six_lookup_agree_'+str(index),all(v==hits[0] for v in hits))
        if 0 in distances:
            kind,y='Boolean',p[max(distances)]
            check('Boolean_lookup_'+str(index),key not in dictionary or dictionary[key]==y)
        elif key in dictionary:
            kind,y='represented',dictionary[key]
            check('represented_forbidden_'+str(index),not forbidden or y==0)
        elif forbidden:
            kind,y='forbidden',F(0)
        else:
            kind,y='free',None
            if key not in free_keys:
                free_keys.append(key)
        rec={'orbit':(l,i,j),'kind':kind,'key':key,'atoms':aa,'presentations':orders,
             'half_distances':distances,'weight':weights[index]}
        if y is None:
            rec['variable']=free_keys.index(key)
        else:
            rec['value']=y
        records.append(rec)
    for l in LAYERS:
        check('complete_weight_sum_'+str(l),sum(w for o,w in zip(orbits,weights) if o[0]==l)==c(68,l)*c(956,l))
    check('all_150_orbits_positive',len(orbits)==150 and min(weights)>0)
    out={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
         'rho':rho,'pairs_through_14':p,'orbits':orbits,'weights':weights,
         'column':records,'free_keys':free_keys,'stage':'column_domain_saved','checks':checks,'failures':failures}
    def save(stage):
        out.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(out),indent=2)+'\n')
    save('column_domain_saved')
    print('Column domain:',len(orbits),'orbits;',len(free_keys),'free keys',flush=True)
    if failures:
        raise SystemExit('Input/domain failure; see certificate')
    # Monic weighted polynomial bases in each factor/layer.
    bases,norms,gamma={},{},{}
    factors,transitions=[],[]
    for n in [68,956]:
        for l in LAYERS:
            wt=[c(8,i)*c(n-8,l-i) for i in range(l+1)]
            hs,ns=[],[]
            for a in range(l+1):
                h=[F(i**a) for i in range(l+1)]
                for v,norm in zip(hs,ns):
                    coef=sum(w*x*y for w,x,y in zip(wt,h,v))/norm
                    h=[x-coef*y for x,y in zip(h,v)]
                norm=sum(w*x*x for w,x in zip(wt,h))
                check('positive_factor_norm_'+str((n,l,a)),norm>0)
                hs.append(h);ns.append(norm)
            bases[n,l],norms[n,l]=hs,ns
            factors.append({'n':n,'layer':l,'weights':wt,'basis':hs,'norms':ns})
        for l,m in it.product(LAYERS,repeat=2):
            for k in range(min(l,m)+1):
                T=[[transition(n,l,m,i,u,k) for u in range(m+1)] for i in range(l+1)]
                check('transition_row_total_'+str((n,l,m,k)),all(sum(row)==c(l,k)*c(n-l,m-k) for row in T))
                for a in range(m+1):
                    action=[sum(x*y for x,y in zip(row,bases[n,m][a])) for row in T]
                    if a<=l:
                        coef=action[a]/bases[n,l][a][a] if bases[n,l][a][a] else next(
                            x/y for x,y in zip(action,bases[n,l][a]) if y)
                        check('whole_factor_action_'+str((n,l,m,k,a)),action==[coef*x for x in bases[n,l][a]])
                        gamma[n,l,m,a,k]=coef
                    else:
                        check('absent_factor_action_'+str((n,l,m,k,a)),not any(action))
                transitions.append({'indices':(n,l,m,k),'matrix':T})
    out.update(factor_bases=factors,complete_transitions=transitions)
    save('factor_actions_saved')
    # The tensor-product bases are a direct sum of all 150 invariants.
    blocks,kernel=[],[]
    rank=0
    for a,b in it.product(range(8),repeat=2):
        ls=([0] if a==b==0 else [])+[l for l in LAYERS if max(a,b)<=l]
        B=[]
        for l in ls:
            row=[]
            for m in ls:
                if l==m==0:
                    entry=F(1)
                elif l==0:
                    entry=p[m]*c(68,m)*c(956,m)
                elif m==0:
                    entry=p[l]
                else:
                    entry=sum(gamma[68,l,m,a,k]*gamma[956,l,m,b,h]*base[l,m,k,h]
                              for k,h in it.product(range(min(l,m)+1),repeat=2))
                row.append(entry)
            B.append(row)
        ns=[F(1) if l==0 else norms[68,l][a]*norms[956,l][b] for l in ls]
        check('weighted_block_symmetry_'+str((a,b)),all(ns[i]*B[i][j]==ns[j]*B[j][i] for i in range(len(ls)) for j in range(len(ls))))
        R,piv,ops=rref(B); rank+=len(piv)
        block_kernel=[]
        for j in range(len(ls)):
            if j in piv:
                continue
            v=[F(0)]*len(ls);v[j]=F(1)
            for r,k in enumerate(piv):
                v[k]=-R[r][j]
            check('block_kernel_residual_'+str((a,b,j)),all(sum(x*y for x,y in zip(row,v))==0 for row in B))
            vv=[]
            for l,i,h in orbits:
                vv.append(v[ls.index(l)]*(1 if l==0 else bases[68,l][a][i]*bases[956,l][b][h]) if l in ls else F(0))
            kernel.append(vv);block_kernel.append(v)
        blocks.append({'mode':(a,b),'layers':ls,'norms':ns,'action':B,'rref':R,'pivots':piv,
                       'operations':ops,'kernel':block_kernel})
    check('complete_invariant_dimension',sum(len(row['layers']) for row in blocks)==150)
    check('complete_rank_nullity',rank+len(kernel)==150)
    out.update(blocks=blocks,rank=rank,kernel_basis=kernel)
    save('full_kernel_saved')
    print('Complete invariant rank/kernel:',rank,len(kernel),flush=True)
    eq,rhs=[],[]
    for v in kernel:
        row=[F(0)]*len(free_keys);right=F(0)
        for w,x,rec in zip(weights,v,records):
            if rec['kind']=='free':
                row[rec['variable']]+=w*x*p[8]
            else:
                right-=w*x*rec['value']
        scale=max(map(abs,row))
        if scale:
            row=[x/scale for x in row];right/=scale
        eq.append(row);rhs.append(right)
    out.update(equations=eq,rhs=rhs)
    save('compatibility_system_saved')
    print('Solving exact compatibility:',len(eq),'rows x',len(free_keys),'free entries',flush=True)
    R,piv,ops=rref([row+[b] for row,b in zip(eq,rhs)])
    consistent=len(free_keys) not in piv
    out.update(equation_rref=R,equation_pivots=piv,equation_operations=ops,equation_consistent=consistent)
    save('compatibility_reduced')
    verdict='unfinished'
    if consistent:
        np=[j for j in range(len(free_keys)) if j not in piv]
        intercept=[F(0)]*len(free_keys);slopes=[[F(0)]*len(np) for _ in free_keys]
        for k,j in enumerate(np):
            slopes[j][k]=F(1)
        for i,j in enumerate(piv):
            intercept[j]=R[i][-1];slopes[j]=[-R[i][k] for k in np]
        out['affine']={'free_indices':np,'intercept':intercept,'slopes':slopes}
        save('affine_system_saved')
        print('Affine dimension:',len(np),flush=True)
        params=[F(0)]*len(np);active=[]
        if min(intercept)<0 and np:
            from simultaneous_five_six_shell import propose,solve
            proposal=propose([[-x for x in row] for row in slopes],intercept)
            out['decimal_proposal']=proposal
            save('proposal_saved')
            active=[j for j in range(len(free_keys)) if len(np)+j not in proposal['basis']]
            active += [np[k] for k in range(len(np)) if k not in proposal['basis'] and np[k] not in active]
            if proposal['status']=='feasible_proposal' and len(active)==len(np):
                params=solve([slopes[j] for j in active],[-intercept[j] for j in active])
        solution=[x+sum(a*t for a,t in zip(row,params)) for x,row in zip(intercept,slopes)]
        out.update(chosen_parameters=params,active_zero_indices=active,candidate=solution)
        if min(solution)>=0:
            check('every_original_equation',all(sum(a*x for a,x in zip(row,solution))==b for row,b in zip(eq,rhs)))
            column=[p[8]*solution[r['variable']] if r['kind']=='free' else r['value'] for r in records]
            for i,v in enumerate(kernel):
                check('whole_weighted_kernel_'+str(i),sum(w*x*y for w,x,y in zip(weights,v,column))==0)
            check('all_column_signs',min(column)>=0)
            out.update(solution=solution,complete_column=column)
            verdict='compatible_nonnegative_column'
        else:
            out['candidate_negative_indices']=[j for j,x in enumerate(solution) if x<0]
    else:
        verdict='inconsistent_equalities_needs_separator'
    out['summary']={'verdict':verdict,'orbits':150,'rank':rank,'kernel_dimension':len(kernel),
        'free_keys':len(free_keys),'equation_rank':len(piv),'consistent':consistent,
        'affine_dimension':len(free_keys)-len(piv) if consistent else None,
        'kinds':{kind:sum(r['kind']==kind for r in records) for kind in ['anchor','Boolean','represented','forbidden','free']},
        'checks':len(checks),'failures':len(failures)}
    save('completed' if verdict=='compatible_nonnegative_column' else 'unfinished_exact_system')
    print(json.dumps(out['summary'],sort_keys=True),flush=True)
    print('Required: all free entries >= 0; every whole weighted kernel residual = 0.')
    print('Full certificate:',OUT.relative_to(NB))
    if failures:
        raise SystemExit('Failed checks; see certificate')


if __name__=='__main__':
    main()

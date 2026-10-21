"""Independent exact verifier for the immutable distance-eight kernel column.

No constructor/optimizer imports; actual sets, convolution counts, moment
orthogonality bases, modular rank lower bounds and complete rational residuals.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from math import comb, factorial, gcd, isqrt, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'eight-distance-full-base-kernel-verification.json'


def c(n,k):
    return comb(n,k) if 0<=k<=n else 0


def encode(x):
    if isinstance(x,Q):
        return [x.numerator,x.denominator]
    if isinstance(x,dict):
        return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [encode(v) for v in x]
    return x


def dec(mat):
    return [[Q(*v) for v in row] for row in mat]


def solve(mat,rhs):
    rows=[[Q(x) for x in row]+[Q(v)] for row,v in zip(mat,rhs)]
    n=len(rows)
    for k in range(n):
        p=next(j for j in range(k,n) if rows[j][k])
        rows[k],rows[p]=rows[p],rows[k]
        pivot=rows[k][k]
        rows[k]=[x/pivot for x in rows[k]]
        for j in range(k+1,n):
            v=rows[j][k]
            rows[j]=[x-v*y for x,y in zip(rows[j],rows[k])]
    x=[Q(0)]*n
    for k in reversed(range(n)):
        x[k]=rows[k][-1]-sum(rows[k][j]*x[j] for j in range(k+1,n))
    return x


def rank_mod(mat,prime=2147483647):
    rows=[]
    for row in mat:
        den=lcm(*(Q(v).denominator for v in row))
        rr=[int(Q(v)*den) for v in row]
        common=gcd(*rr)
        if common:
            rr=[x//common for x in rr]
        rows.append([x%prime for x in rr])
    rank=0
    for k in range(len(rows[0])):
        s=next((s for s in range(rank,len(rows)) if rows[s][k]),None)
        if s is None:
            continue
        rows[rank],rows[s]=rows[s],rows[rank]
        inv=pow(rows[rank][k],-1,prime)
        rows[rank]=[x*inv%prime for x in rows[rank]]
        for j in range(rank+1,len(rows)):
            v=rows[j][k]
            if v:
                rows[j]=[(x-v*y)%prime for x,y in zip(rows[j],rows[rank])]
        rank+=1
        if rank==len(rows):
            break
    return rank


def actual(l,m,i,j):
    D=set(range(68));U=set(range(m));V=set(range(68,68+m))
    X=set(range(i))|set(range(m,m+l-i))
    Y=set(range(68,68+j))|set(range(68+m,68+m+l-j))
    supports=[D,(D-X)|Y,(D-U)|V]
    presentations=[]
    for ss in it.permutations(supports):
        aa=[0]*8
        for x in range(1024):
            aa[sum(bit for bit,s in zip([4,2,1],ss) if x in s)]+=1
        presentations.append(aa)
    return supports,presentations


def main():
    path=ROOT/'eight-distance-full-base-kernel-results.json'
    data=json.loads(path.read_text())
    src=json.loads((ROOT/'maximizer-excluded-anchor-results.json').read_text())
    scalar=json.loads((ROOT/'maximizer-seven-seven-scalars-results.json').read_text())
    lp=json.loads((ROOT/'delsarte-lp-results.json').read_text())
    checks,failures=[],[]
    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    check('clean_constructor',not data['failures'])
    for rel,digest in data['input_hashes'].items():
        check('immutable_hash_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==digest)
    check('prime_trial_division',all(2147483647%d for d in range(2,isqrt(2147483647)+1)))
    p=[Q(1)]+[Q(0)]*4+[Q(v['numerator'],v['denominator'])/(2*c(68,h)*c(956,h))
        for h,v in zip(range(5,69),lp['exact']['primal'])]
    rho=(Q(c(1024,64),c(68,64))+1)/(2*c(1024,68))
    check('original_rho_all_pairs',rho==Q(*data['rho'])==Q(*src['rho'])>0
          and encode(p[:15])==data['pairs_through_14']==src['pairs_through_14'] and p[8]>0)
    check('immutable_f_z_parameters',src['parameters']==scalar['parameters'] and
          src['original_column']==scalar['original_RREF_column'] and
          src['completion_z']==scalar['same_original_basis_z'])
    base,dictionary={},{}
    for row in src['entries']:
        typ=tuple(row['type']);y=Q(*row['y'])
        ss,orders=actual(*typ)
        check('actual_old_sizes_'+str(typ),all(len(s)==68 for s in ss))
        check('actual_old_six_'+str(typ),orders==[r['atoms'] for r in row['presentations']])
        key=min(map(tuple,orders))
        check('actual_old_key_'+str(typ),key not in dictionary or dictionary[key]==y)
        dictionary[key]=y;base[typ]=y
    check('all_270_immutable_values',base=={tuple(r['type']):Q(*r['y']) for r in scalar['all_records']})
    for l,m,i,j in list(base):
        base[m,l,i,j]=base[l,m,i,j]
    orbits=[(0,0,0)]+[(l,i,j) for l in [5,6,7] for i,j in it.product(range(l+1),repeat=2)]
    weights=[1]+[c(8,i)*c(60,l-i)*c(8,j)*c(948,l-j) for l,i,j in orbits[1:]]
    check('complete_orbits_weights',data['orbits']==list(map(list,orbits)) and data['weights']==weights and min(weights)>0)
    for l in [5,6,7]:
        check('whole_layer_weight_sum_'+str(l),sum(w for o,w in zip(orbits,weights) if o[0]==l)==c(68,l)*c(956,l))
    free_keys=[];records=data['column'];column=[Q(*x) for x in data['complete_column']]
    solution=[Q(*x) for x in data['solution']]
    check('complete_column_nonnegative',len(column)==150 and min(column)>=0 and len(solution)==85 and min(solution)>=0)
    for z,(l,i,j) in enumerate(orbits):
        rec=records[z]
        check('original_orbit_order_'+str(z),rec['orbit']==[l,i,j])
        if l==0:
            check('original_anchor',rec['kind']=='anchor' and Q(*rec['value'])==column[z]==p[8])
            continue
        ss,orders=actual(l,8,i,j)
        key=min(map(tuple,orders));distances=[len(ss[0]-ss[1]),len(ss[0]-ss[2]),len(ss[1]-ss[2])]
        check('actual_new_six_'+str(z),all(len(s)==68 for s in ss) and rec['presentations']==orders
              and rec['atoms']==orders[0] and rec['key']==list(key) and rec['half_distances']==distances)
        forbidden=any(1<=h<=4 for h in distances)
        for k,aa in enumerate(orders):
            # Independently recanonicalize this presentation's bit masks.
            permuted=[]
            for oldbits in it.permutations([4,2,1]):
                out=[0]*8
                for mask,size in enumerate(aa):
                    target=sum(new for new,old in zip([4,2,1],oldbits) if mask&old)
                    out[target]=size
                permuted.append(tuple(out))
            ownkey=min(permuted)
            a,b,h=aa[4]+aa[5],aa[4]+aa[6],aa[2]+aa[6]
            t,s=aa[4],aa[3]
            check('new_lookup_'+str((z,k)),ownkey==key and dictionary.get(ownkey)==dictionary.get(key)
                  and a+b-t-s==h and sorted([a,b,h])==sorted(distances)
                  and t-s==orders[0][4]-orders[0][3])
        if key in dictionary:
            check('fixed_lookup_'+str(z),rec['kind']=='represented' and column[z]==Q(*rec['value'])==dictionary[key]
                  and (not forbidden or column[z]==0))
        elif forbidden:
            check('forbidden_zero_'+str(z),rec['kind']=='forbidden' and column[z]==Q(*rec['value'])==0)
        else:
            if key not in free_keys:
                free_keys.append(key)
            check('free_unordered_key_'+str(z),rec['kind']=='free' and rec['variable']==free_keys.index(key)
                  and column[z]==p[8]*solution[rec['variable']])
    check('all_85_free_keys',data['free_keys']==list(map(list,free_keys)) and len(free_keys)==85)
    # Construct the monic polynomials by solving moment orthogonality, rather
    # than the constructor's sequential Gram-Schmidt algorithm.
    bases,norms,gamma={},{},{}
    factors={(r['n'],r['layer']):r for r in data['factor_bases']}
    transitions={tuple(r['indices']):r['matrix'] for r in data['complete_transitions']}
    for n in [68,956]:
        for l in [5,6,7]:
            wt=[c(8,i)*c(n-8,l-i) for i in range(l+1)]
            moments=[sum(w*i**a for i,w in enumerate(wt)) for a in range(2*l+1)]
            hs=[];ns=[]
            for a in range(l+1):
                coefficients=solve([[moments[i+j] for j in range(a)] for i in range(a)],[-moments[i+a] for i in range(a)]) if a else []
                h=[Q(i**a)+sum(x*i**k for k,x in enumerate(coefficients)) for i in range(l+1)]
                norm=sum(w*x*x for w,x in zip(wt,h));hs.append(h);ns.append(norm)
                check('monic_polynomial_orthogonality_'+str((n,l,a)),norm>0 and all(
                    sum(w*x*i**k for i,(w,x) in enumerate(zip(wt,h)))==0 for k in range(a)))
                differences=h[:]
                for k in range(a):
                    differences=[y-x for x,y in zip(differences,differences[1:])]
                check('monic_leading_difference_'+str((n,l,a)),all(x==factorial(a) for x in differences))
            check('whole_factor_basis_'+str((n,l)),encode(hs)==factors[n,l]['basis'] and encode(ns)==factors[n,l]['norms'] and wt==factors[n,l]['weights'])
            bases[n,l],norms[n,l]=hs,ns
        for l,m in it.product([5,6,7],repeat=2):
            for k in range(min(l,m)+1):
                T=[]
                for i in range(l+1):
                    row=[]
                    for u in range(m+1):
                        # Independent region-polynomial convolution.
                        head=[c(i,s)*c(8-i,u-s) for s in range(9)]
                        tail=[c(l-i,t)*c(n-8-l+i,m-u-t) for t in range(l-i+1)]
                        row.append(sum(x*tail[k-s] for s,x in enumerate(head) if 0<=k-s<len(tail)))
                    T.append(row)
                check('every_transition_'+str((n,l,m,k)),T==transitions[n,l,m,k] and all(sum(row)==c(l,k)*c(n-l,m-k) for row in T))
                for a in range(m+1):
                    action=[sum(x*y for x,y in zip(row,bases[n,m][a])) for row in T]
                    if a<=l:
                        coef=sum(w*x*y for w,x,y in zip(factors[n,l]['weights'],action,bases[n,l][a]))/norms[n,l][a]
                        check('complete_factor_action_'+str((n,l,m,k,a)),action==[coef*x for x in bases[n,l][a]])
                        gamma[n,l,m,a,k]=coef
                    else:
                        check('complete_absent_action_'+str((n,l,m,k,a)),not any(action))
    check('all_118_transitions',len(transitions)==118)
    # Independent rank lower bounds plus complete rational null vectors prove
    # exhaustion in each exact block; product bases exhaust the full quotient.
    kernel=[];total_rank=0;block_ranks=[];dimension=0
    for block in data['blocks']:
        a,b=block['mode'];ls=([0] if a==b==0 else [])+[l for l in [5,6,7] if max(a,b)<=l]
        B=[]
        for l in ls:
            B.append([Q(1) if l==m==0 else p[m]*c(68,m)*c(956,m) if l==0 else p[l] if m==0 else sum(
                gamma[68,l,m,a,k]*gamma[956,l,m,b,h]*base[l,m,k,h]
                for k,h in it.product(range(min(l,m)+1),repeat=2)) for m in ls])
        rank=rank_mod(B);total_rank+=rank;dimension+=len(ls)
        check('complete_actual_block_'+str((a,b)),encode(B)==block['action'] and block['layers']==ls)
        check('rank_lower_'+str((a,b)),rank==len(block['pivots']))
        nulls=dec(block['kernel']);nonpivots=[j for j in range(len(ls)) if j not in block['pivots']]
        check('independent_complete_local_kernel_'+str((a,b)),len(nulls)==len(ls)-rank==len(nonpivots) and all(
            v[j]==int(t==s) for t,v in enumerate(nulls) for s,j in enumerate(nonpivots)))
        for t,v in enumerate(nulls):
            check('every_block_null_residual_'+str((a,b,t)),all(sum(x*y for x,y in zip(row,v))==0 for row in B))
            full=[v[ls.index(l)]*(1 if l==0 else bases[68,l][a][i]*bases[956,l][b][j]) if l in ls else Q(0) for l,i,j in orbits]
            kernel.append(full)
        block_ranks.append({'mode':[a,b],'dimension':len(ls),'modular_rank':rank,'kernel_dimension':len(nulls)})
    check('all_64_modes',len(data['blocks'])==64 and {tuple(x['mode']) for x in data['blocks']}==set(it.product(range(8),repeat=2)))
    check('entire_invariant_kernel',total_rank==60 and dimension==150 and len(kernel)==90 and encode(kernel)==data['kernel_basis'])
    eq,rhs=[],[];weighted_residuals=[]
    for k,v in enumerate(kernel):
        row=[Q(0)]*85;right=Q(0)
        for w,x,rec in zip(weights,v,records):
            if rec['kind']=='free':
                row[rec['variable']]+=w*x*p[8]
            else:
                right-=w*x*Q(*rec['value'])
        scale=max(map(abs,row))
        if scale:
            row=[x/scale for x in row];right/=scale
        eq.append(row);rhs.append(right)
        residual=sum(w*x*y for w,x,y in zip(weights,v,column))
        weighted_residuals.append(residual)
        check('every_original_kernel_equation_'+str(k),encode(row)==data['equations'][k] and encode(right)==data['rhs'][k]
              and sum(x*y for x,y in zip(row,solution))==right and residual==0)
    affine=data['affine'];indices=affine['free_indices'];intercept=[Q(*x) for x in affine['intercept']];slopes=dec(affine['slopes'])
    check('equation_rank_lower_81',rank_mod(eq)==81)
    check('four_canonical_affine_parameters',indices==[56,63,69,78] and all(intercept[j]==0 and slopes[j]==[Q(t==s) for s in range(4)] for t,j in enumerate(indices)))
    for k,(row,b) in enumerate(zip(eq,rhs)):
        check('affine_particular_and_all_four_nulls_'+str(k),sum(x*y for x,y in zip(row,intercept))==b and all(
            sum(x*slopes[j][t] for j,x in enumerate(row))==0 for t in range(4)))
    active=[27,33,56,63]
    params=solve([slopes[j] for j in active],[-intercept[j] for j in active])
    fresh=[x+sum(a*t for a,t in zip(row,params)) for x,row in zip(intercept,slopes)]
    check('unique_rational_active_set',data['active_zero_indices']==active and encode(params)==data['chosen_parameters'] and fresh==solution)
    zeros=[j for j,x in enumerate(solution) if x==0]
    check('all_85_exact_signs',zeros==active and sum(x>0 for x in solution)==81)
    summary={'verdict':'RECONSTRUCTION_FAILURE' if failures else 'COMPATIBLE_NONNEGATIVE_COLUMN',
        'checks':len(checks),'failures':len(failures),'orbits':150,'invariant_rank':total_rank,
        'kernel_dimension':len(kernel),'equation_rank':81,'affine_dimension':4,
        'represented':45,'forbidden':19,'free':85,'positive_free':sum(x>0 for x in solution),
        'zero_free_indices':zeros,'all_weighted_kernel_residuals_zero':not any(weighted_residuals),
        'required_minimum_free':0,'actual_minimum_free':min(solution),'energy_tested':False}
    output={'summary':summary,'checks':checks,'failures':failures,
        'constructor_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'block_rank_certificates':block_ranks,'full_kernel':kernel,'equations':eq,'rhs':rhs,
        'fresh_active_parameters':params,'full_rational_solution':fresh,'complete_column':column,
        'whole_weighted_residuals':weighted_residuals,'zero_keys':[free_keys[j] for j in zeros]}
    OUT.write_text(json.dumps(encode(output),indent=2)+'\n')
    print(json.dumps(encode(summary),sort_keys=True))
    print('Required: every free sign >= 0 and all 90 complete weighted kernel residuals = 0.')
    print('Full evidence:',OUT.relative_to(NB))
    if failures:
        print('Failures:',failures)
        raise SystemExit(1)


if __name__=='__main__':
    main()

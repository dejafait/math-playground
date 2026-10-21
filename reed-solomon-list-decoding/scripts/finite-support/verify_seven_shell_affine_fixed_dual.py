"""Independent exact substitution of the L068 affine-family certificate.

No notebook module imports, optimizer or floating arithmetic. Actual subsets
check every presentation; determinant inverse formulas reconstruct the full
quadratic independently of the constructor's affine-square elimination.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'seven-shell-affine-fixed-dual-verification.json'


def C(n,k):
    return comb(n,k) if 0 <= k <= n else 0


@lru_cache(None)
def beta(n,l,m,a,i):
    # Independently summed source beta, with all impossible terms zero.
    return sum((-1)**(u-i)*C(u,i)*C(n-2*a,u-a)*C(n-a-u,l-u)*C(n-a-u,m-u)
               for u in range(a,min(l,m,n-a)+1) if u >= i)


def eigen(n,a,r):
    return sum((-1)**s*C(a,s)*C(7-a,r-s)*C(n-7-a,r-s) for s in range(r+1))


def encode(x):
    if isinstance(x,Q):
        return [x.numerator,x.denominator]
    if isinstance(x,dict):
        return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [encode(v) for v in x]
    return x


def dot(x,y):
    return sum((a*b for a,b in zip(x,y)),Q(0))


def const(x):
    return [Q(x),Q(0),Q(0),Q(0)]


def region_order(supports):
    counts = [0]*8
    for point in range(1024):
        counts[sum(bit for bit,S in zip([4,2,1],supports) if point in S)] += 1
    return tuple(counts)


def main():
    paths = [ROOT/'seven-shell-affine-fixed-dual-results.json',
             ROOT/'simultaneous-shell-ordinary-scalars-results.json',
             ROOT/'seven-distance-full-base-kernel-results.json',
             ROOT/'simultaneous-seven-shell-results.json']
    data,old,col,fixed = [json.loads(p.read_text()) for p in paths]
    checks,failures = [],[]

    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('prior_failures_empty',all(not x['failures'] for x in [data,old,col,fixed]))
    for j,x in enumerate([data,old,col,fixed]):
        check(f'input_hashes_{j}',all(hashlib.sha256((NB/p).read_bytes()).hexdigest() == h
              for p,h in x.get('input_hashes',x.get('source_hashes',{})).items()))
    pairs = [Q(*x) for x in old['pairs_through_12']]
    p7 = pairs[7]
    check('original_normalization',Q(*old['rho']) > 0 and p7 == Q(3539,248922676958508))
    fs = [[Q(*c)]+[Q(*a) for a in ss] for c,ss in zip(col['affine']['intercept'],col['affine']['slopes'])]
    check('all_domain_inequalities',encode(fs) == data['domain']['nonnegative_free'])
    for i,(row,rhs) in enumerate(zip(col['equations'],col['rhs'])):
        check(f'all_original_kernel_equations_{i}',
              [sum(Q(*e)*f[j] for e,f in zip(row,fs)) for j in range(4)] == const(Q(*rhs)))
    base = {tuple(r['type']):const(Q(*r['y'])) for r in old['types']}
    for row in col['column'][1:]:
        l,i,j = row['orbit']
        base[l,7,i,j] = [p7*x for x in fs[row['variable']]] if row['kind'] == 'free' else const(Q(*row['value']))
    allkeys = {}
    D = set(range(68))
    presentations = []
    for saved in data['records']:
        l,m,i,j = saved['type']
        E = (D-(set(range(i))|set(range(m,m+l-i))))|set(range(68,68+j))|set(range(68+m,68+m+l-j))
        G = (D-set(range(m)))|set(range(68,68+m))
        check(f'actual_supports_{l}_{m}_{i}_{j}',len(E) == len(G) == 68)
        actual = [region_order(ordered) for ordered in it.permutations([D,E,G])]
        key = min(actual)
        check(f'actual_key_{l}_{m}_{i}_{j}',list(key) == saved['key'])
        prescribed = []
        for aa in actual:
            ab,ac,bc = aa[4]+aa[5],aa[4]+aa[6],aa[2]+aa[6]
            value = None
            if 0 in [ab,ac,bc]:
                value = const(pairs[max(ab,ac,bc)])
            elif any(1 <= h <= 4 for h in [ab,ac,bc]):
                value = const(0)
            else:
                kk = (*sorted([ab,ac]),aa[4],aa[3])
                if kk in base:
                    value = base[kk]
            if value is not None:
                prescribed.append(value)
            # Match every actual support ordering to the saved full region.
            matches = [v for v in saved['presentations'] if v['atoms'] == list(aa)]
            check(f'presentation_{len(checks)}',bool(matches) and all(v['affine'] == encode(value) for v in matches))
        value = prescribed[0] if prescribed else None
        check(f'full_affine_consistency_{l}_{m}_{i}_{j}',all(v == value for v in prescribed))
        check(f'full_affine_entry_{l}_{m}_{i}_{j}',encode(value) == saved['affine'])
        if key in allkeys:
            check(f'shared_actual_key_{l}_{m}_{i}_{j}',allkeys[key] == value)
        allkeys[key] = value
        if value is not None:
            base[l,m,i,j] = value
        presentations.append({'type':[l,m,i,j],'actual_regions':actual,'value':value})
    check('no_hidden_affine_equalities',data['domain']['equality_rows'] == []
          and all(not any(Q(*x) for x in row) for row in data['domain']['all_equality_residuals']))
    S = {l:C(68,l)*C(956,l) for l in [5,6,7]}
    h = [Q(1),Q(20435,441),Q(13481000,13671),Q(2688040,217),Q(1307664259,13671),Q(5294968393,13671),Q(0),Q(0)]
    k = [Q(49,100880416043264),Q(7665,38718903137024),Q(17301,551968803584),Q(5461349,2754064239872)]+[Q(0)]*4
    weights = [x*y for x,y in it.product(h,k)]
    check('unchanged_24_weights',encode(weights) == data['dual'] == fixed['exact']['dual']
          and sum(x>0 for x in weights) == 24 and min(weights) >= 0)
    ranges,mode_data = [],[]
    for idx,(a,b) in enumerate(it.product(range(8),repeat=2)):
        ls = [l for l in [5,6] if a <= l and b <= l]

        def block(l,m):
            value = [Q(0)]*4
            for i,j in it.product(range(min(l,m)+1),repeat=2):
                factor = beta(68,l,m,a,i)*beta(956,l,m,b,j)
                value = [x+factor*y for x,y in zip(value,base[min(l,m),max(l,m),i,j])]
            if a == b == 0:
                value[0] -= pairs[l]*pairs[m]*S[l]*S[m]
            return value

        B = [[block(l,m)[0] for m in ls] for l in ls]
        t = [block(l,7) for l in ls]
        check(f'cross_reconstruction_{a}_{b}',encode(t) == data['modes'][idx]['cross'])
        check(f'old_block_reconstruction_{a}_{b}',encode(B) == data['modes'][idx]['B'] == fixed['modes'][idx]['base'])
        d7 = C(68-2*a,7-a)*C(956-2*b,7-b)
        check(f'source_normalization_{a}_{b}',d7 == data['modes'][idx]['D7'] and d7 > 0)
        # Full affine range identities, using determinant cases rather than
        # the constructor's sequential elimination.
        rr = []
        if len(ls) == 2:
            x,y,z = B[0][0],B[0][1],B[1][1]
            det = x*z-y*y
            check(f'old_psd_{a}_{b}',x >= 0 and z >= 0 and det >= 0)
            if det == 0:
                if x > 0:
                    rr = [[x*v-y*u for u,v in zip(*t)]]
                elif z > 0:
                    rr = [t[0]]
                else:
                    rr = t
        elif ls and B[0][0] == 0:
            rr = t
        check(f'full_singular_range_{a}_{b}',all(not any(r) for r in rr))
        ranges.append(rr)
        fixed_aff = [Q(0)]*4
        for r in range(8):
            for q in range(8):
                if r+q <= 6:
                    factor = Q(eigen(68,a,r)*eigen(956,b,q),p7)
                    fixed_aff = [x+factor*y for x,y in zip(fixed_aff,base[7,7,7-r,7-q])]
                check(f'eigen_beta_{a}_{b}_{r}_{q}',
                      Q(beta(68,7,7,a,7-r)*beta(956,7,7,b,7-q),d7) == eigen(68,a,r)*eigen(956,b,q))
        if a == b == 0:
            fixed_aff[0] -= p7*S[7]
        check(f'fixed_affine_{a}_{b}',encode(fixed_aff) == data['modes'][idx]['fixed_minus_anchor_affine'])
        mode_data.append({'B':B,'cross':t,'d7':d7,'fixed':fixed_aff})
    cancellations = [sum(weights[8*a+b]*eigen(68,a,r)*eigen(956,b,q) for a,b in it.product(range(8),repeat=2))
                     for r in range(8) for q in range(8) if r+q >= 7]
    check('all_free_coefficients_cancel',not any(cancellations))

    def evaluate(parameters):
        point = [Q(1)]+list(parameters)
        results = []
        for w,md in zip(weights,mode_data):
            B,t = md['B'],[dot(v,point) for v in md['cross']]
            if len(B) == 2:
                x,y,z = B[0][0],B[0][1],B[1][1]
                u,v = t
                det = x*z-y*y
                if det > 0:
                    cost = (z*u*u-2*y*u*v+x*v*v)/det
                elif x > 0:
                    cost = u*u/x
                elif z > 0:
                    cost = v*v/z
                else:
                    cost = Q(0)
            elif B and B[0][0] > 0:
                cost = t[0]*t[0]/B[0][0]
            else:
                cost = Q(0)
            results.append(dot(md['fixed'],point)-cost/(p7*md['d7']))
        return dot(weights,results),results

    zero = [Q(0)]*3
    f0,_ = evaluate(zero)
    M = [[Q(0)]*4 for _ in range(4)]
    M[0][0] = f0
    evals = [{'parameters':zero,'value':f0}]
    plus = []
    for i in range(3):
        point = [Q(int(j == i)) for j in range(3)]
        fp,_ = evaluate(point)
        fm,_ = evaluate([-x for x in point])
        M[i+1][i+1] = (fp+fm)/2-f0
        M[0][i+1] = M[i+1][0] = (fp-fm)/4
        plus.append(fp)
        evals.extend([{'parameters':point,'value':fp},{'parameters':[-x for x in point],'value':fm}])
    for i,j in it.combinations(range(3),2):
        point = [Q(int(t in [i,j])) for t in range(3)]
        fp,_ = evaluate(point)
        M[i+1][j+1] = M[j+1][i+1] = (fp-plus[i]-plus[j]+f0)/2
        evals.append({'parameters':point,'value':fp})
    check('whole_quadratic_reconstructed',encode(M) == data['objective_matrix'])
    alpha,bet = -M[3][3],M[0][3]
    check('positive_curvature',alpha > 0)
    check('only_w_terms',all(M[i][j] == 0 for i in range(4) for j in range(4) if i in [1,2] or j in [1,2]))
    check('perfect_negative_square',alpha*M[0][0]+bet*bet == 0)
    star = [Q(0),Q(0),bet/alpha]
    check('exact_zero_witness_parameters',encode(star) == data['optimization']['stationary'])
    signs = [dot(f,[Q(1)]+star) for f in fs]
    check('every_free_nonnegative',min(signs) >= 0 and sum(x>0 for x in signs) == 47
          and [i for i,x in enumerate(signs) if x == 0] == [27,33])
    check('all_saved_free_values',encode(signs) == data['optimization']['free_values'])
    # Substitute in every original column coordinate and its entire weighted
    # base kernel, not only in the reduced quadratic.
    column = [p7*signs[r['variable']] if r['kind'] == 'free' else Q(*r['value']) for r in col['column']]
    weights_base = col['weights']
    original_kernel_residuals = []
    for n,v in enumerate(col['kernel_basis']):
        res = sum(Q(*x)*int(w)*b for x,w,b in zip(v,weights_base,column))
        original_kernel_residuals.append(res)
        check(f'weighted_full_kernel_witness_{n}',res == 0)
    value,rhs = evaluate(star)
    check('direct_exact_zero',value == 0 and encode(value) == data['optimization']['value'])
    check('all_prescribed_entries_nonnegative',min(column) >= 0)
    check('all_fixed_newnew_nonnegative',all(dot(md,[Q(1)]+star) >= 0 for key,md in base.items() if key[:2] == (7,7)))
    original = [Q(*x) for x in data['original_point']][1:]
    oldvalue,_ = evaluate(original)
    check('original_negative_point_retained',encode(oldvalue) == fixed['exact']['fixed_value'] and oldvalue < 0)
    summary = {'checks':len(checks),'failures':len(failures),'types':270,'presentations':1620,
               'modes':64,'free_positive':47,'free_zero':[27,33],'objective_at_witness':'0',
               'global_maximum':'0','verdict':'FIXED_DUAL_NOT_STRICT_OVER_FAMILY'}
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checks':checks,'failures':failures,'presentations':presentations,'ranges':ranges,
              'modes':mode_data,'quadratic_evaluations':evals,'objective_matrix':M,
              'alpha':alpha,'beta':bet,'w_star':star[2],'witness_parameters':star,
              'all_free_values':signs,'complete_column':column,'all_64_rhs_at_witness':rhs,
              'kernel_residuals':original_kernel_residuals,'dual_cancellations':cancellations,'summary':summary}
    OUT.write_text(json.dumps(encode(report),indent=2)+'\n')
    print(f'Verification: {len(checks)} checks; failures={failures}; achieved global maximum=0 at admissible point; required uniform sign <0.')
    print('Certificate:',OUT.relative_to(NB))


if __name__ == '__main__':
    main()

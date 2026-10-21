"""Independent L075 audit. Exact arithmetic; no notebook code imports.

Full certificates are consumed and reconstructed, never accepted from summaries.
The source decomposition and upstream input recipes are the cited lemma imports.
"""
import hashlib
import itertools as it
import json
import re
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'maximizer-excluded-anchor-critical-audit.json'
LS = [5, 6, 7]


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [enc(v) for v in x]
    return x


def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b)), F(0))


def solve(A, b):
    """Reverse columns, forward elimination and back substitution."""
    n = len(b)
    T = [list(reversed(row))+[v] for row, v in zip(A, b)]
    ps = []
    for j in range(n):
        i = next(i for i in range(j, n) if T[i][j])
        T[i], T[j] = T[j], T[i]
        ps.append(T[j][j])
        for i in range(j+1, n):
            q = T[i][j]/T[j][j]
            T[i] = [x-q*y for x, y in zip(T[i], T[j])]
    x = [F(0)]*n
    for i in reversed(range(n)):
        x[i] = (T[i][-1]-dot(T[i][i+1:n], x[i+1:]))/T[i][i]
    return list(reversed(x)), ps


def determinant(A):
    """Elimination, independent of the constructor's Laplace expansion."""
    A = [row[:] for row in A]
    d = F(1)
    for j in range(len(A)):
        i = next((i for i in range(j, len(A)) if A[i][j]), None)
        if i is None:
            return F(0)
        if i != j:
            A[i], A[j] = A[j], A[i]
            d = -d
        d *= A[j][j]
        for i in range(j+1, len(A)):
            q = A[i][j]/A[j][j]
            for k in range(j+1, len(A)):
                A[i][k] -= q*A[j][k]
    return d


@lru_cache(None)
def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*c(u,t)*c(n-2*a,u-a)*c(n-a-u,l-u)*c(n-a-u,m-u)
               for u in range(max(a,t), min(l,m,n-a)+1))


def eigen(n, l, a, r):
    return sum((-1)**s*c(a,s)*c(l-a,r-s)*c(n-l-a,r-s) for s in range(r+1))


def main():
    names = ['maximizer-excluded-anchor-results.json', 'maximizer-excluded-anchor-initial.json',
             'delsarte-lp-results.json', 'seven-distance-full-base-kernel-results.json',
             'seven-shell-affine-fixed-dual-results.json', 'alternative-product-zero-plane-results.json',
             'simultaneous-shell-ordinary-scalars-results.json', 'maximizer-completion-results.json',
             'maximizer-completion-verification.json', 'maximizer-seven-seven-scalars-results.json',
             'complemented-five-six-shell-results.json']
    paths = [ROOT/n for n in names]
    data,initial,lp,col,square,plane,old,inc,ver,scalar,small = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    for path, obj in zip(paths, [data,initial,lp,col,square,plane,old,inc,ver,scalar,small]):
        if obj is not initial:
            check('clean_'+path.name, obj['failures'] == [])
        for rel, digest in obj.get('input_hashes', obj.get('source_hashes', {})).items():
            check('hash_'+path.name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    check('preserved_initial_failure', initial['failures'] == ['original_defining_rows'])
    for key in data:
        if key not in ['summary','checks','failures']:
            check('initial_math_unchanged_'+key, initial[key] == data[key])
    a = [F(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    check('original_pair_domain', len(a) == 64 and lp['active_distances'] == list(range(5,69)))
    pair_residuals = []
    for j in range(1,65):
        res = 1+sum(F(eigen(1024,68,j,h),c(68,h)*c(956,h))*v for h,v in zip(range(5,69),a))
        pair_residuals.append(res)
        check('original_pair_equation_'+str(j), res == 0)
    p = [F(1)]+[F(0)]*4+[v/(2*c(68,h)*c(956,h)) for h,v in zip(range(5,69),a)]
    rho = (F(c(1024,64),c(68,64))+1)/(2*c(1024,68))
    check('rho_pairs', rho > 0 and enc(rho) == data['rho'] == scalar['rho']
          and enc(p[:15]) == data['pairs_through_14'] == scalar['pairs_through_14']
          and p[14] == F(2825730193896494219,198754391512280403438773149400))
    M = [[F(*v) for v in row] for row in square['objective_matrix']]
    N = [[F(*v) for v in row] for row in plane['plane_matrix']]
    pars = [F(0),-N[0][2]/N[2][2],-M[0][3]/M[3][3]]
    check('parameters', M[3][3] < 0 and N[2][2] < 0 and enc(pars) == data['parameters'] == inc['parameters'])
    rr = [[F(*v) for v in row] for row in col['equation_rref']]
    piv = col['equation_pivots']
    check('RREF_domain', len(rr) == 49 and all(len(row) == 50 for row in rr)
          and len(piv) == 46 and [j for j in range(49) if j not in piv] == [27,33,42])
    f = [F(0)]*49
    for j,v in zip([27,33,42],pars):
        f[j] = v
    for i,j in enumerate(piv):
        f[j] = rr[i][-1]-sum(rr[i][k]*f[k] for k in [27,33,42])
    check('column_identity', enc(f) == data['original_column'] == inc['free_column'] and min(f) == 0)
    for i,(row,b) in enumerate(zip(col['equations'],col['rhs'])):
        check('original_column_equation_'+str(i), dot([F(*v) for v in row],f) == F(*b))
    y = {tuple(row['type']):F(*row['y']) for row in old['types']}
    column, weights = [], []
    for row in col['column']:
        l,i,j = row['orbit']
        v = p[7]*f[row['variable']] if row['kind'] == 'free' else F(*row['value'])
        column.append(v)
        weights.append(c(7,i)*c(61,l-i)*c(7,j)*c(949,l-j) if l else 1)
        if l:
            y[l,7,i,j] = v
        else:
            check('column_anchor', v == p[7])
    residuals = [dot([F(*v)*wt for v,wt in zip(row,weights)],column) for row in col['kernel_basis']]
    check('weighted_whole_kernel', len(residuals) == 49 and residuals == [F(0)]*49
          and weights == col['weights'] and len(column) == 86)
    free = [(r,q) for r,q in it.product(range(8),repeat=2) if r+q >= 7]
    for r,q in it.product(range(8),repeat=2):
        h = r+q
        if h <= 6:
            y[7,7,7-r,7-q] = p[7] if h == 0 else F(0) if h <= 4 else y[h,7,q,r]
    sizes = {l:c(68,l)*c(956,l) for l in LS}
    def source(a,b,l,m,lookup):
        return sum(beta(68,l,m,a,i)*beta(956,l,m,b,j)*lookup[min(l,m),max(l,m),i,j]
                   for i,j in it.product(range(min(l,m)+1),repeat=2))
    # Independently recover the original defining right sides, including singular cases.
    A, bounds, completion_modes = [], [], []
    for a,b in it.product(range(8),repeat=2):
        layers = [l for l in [5,6] if max(a,b) <= l]
        def C(l,m):
            return source(a,b,l,m,y)-(p[l]*p[m]*sizes[l]*sizes[m] if a == b == 0 else 0)
        B = [[C(l,m) for m in layers] for l in layers]
        t = [C(l,7) for l in layers]
        cost = F(0)
        if len(layers) == 2:
            x,z,h = B[0][0],B[1][1],B[0][1]
            d = x*z-h*h
            check('old_PSD_'+str((a,b)), min(x,z,d) >= 0)
            if d:
                cost = (z*t[0]**2-2*h*t[0]*t[1]+x*t[1]**2)/d
            elif x:
                check('singular_range_'+str((a,b)), x*t[1] == h*t[0])
                cost = t[0]**2/x
            elif z:
                check('singular_range_'+str((a,b)), t[0] == 0 and h == 0)
                cost = t[1]**2/z
            else:
                check('zero_range_'+str((a,b)), t == [0,0] and h == 0)
        elif layers:
            check('one_old_PSD_'+str((a,b)), B[0][0] >= 0)
            if B[0][0]:
                cost = t[0]**2/B[0][0]
            else:
                check('one_zero_range_'+str((a,b)), t[0] == 0)
        D7 = c(68-2*a,7-a)*c(956-2*b,7-b)
        fixed = sum(beta(68,7,7,a,i)*beta(956,7,7,b,j)*v
                    for (l,m,i,j),v in y.items() if l == m == 7)
        fixed -= p[7]**2*sizes[7]**2 if a == b == 0 else 0
        bound = (fixed-cost)/(p[7]*D7)
        row = [-F(eigen(68,7,a,r)*eigen(956,7,b,q),c(7,r)*c(61,r)*c(7,q)*c(949,q)) for r,q in free]
        ix = 8*a+b
        check('original_completion_system_'+str(ix), enc(row) == inc['matrix'][ix] and enc(bound) == inc['rhs'][ix])
        A.append(row); bounds.append(bound)
        completion_modes.append({'mode':[a,b],'base':B,'cross':t,'cost':cost,'row':row,'bound':bound})
    manuscript = (NB/'lemmas/L073-maximizer-simultaneous-seven-shell-psd-completion.md').read_text()
    section = manuscript.split('whose first 35 rows are the rows A_i, in this order:')[1].split('The last row')[0]
    indices = list(map(int,re.findall(r'\d+',section)))
    check('defining_indices', len(indices) == len(set(indices)) == 35
          and inc['certificate']['defining_rows'] == [['mode',i] for i in indices]+[['sign',28]])
    z, basis_pivots = solve([A[i] for i in indices]+[[F(j == 28) for j in range(36)]],
                           [bounds[i] for i in indices]+[F(0)])
    check('original_solution', enc(z) == data['completion_z'] == inc['certificate']['z'] == ver['fresh_original_basis_solution']
          and all(v > 0 for j,v in enumerate(z) if j != 28) and z[28] == 0)
    for i in range(64):
        check('original_mode_slack_'+str(i), bounds[i]-dot(A[i],z) >= 0)
    for (r,q),v in zip(free,z):
        y[7,7,7-r,7-q] = p[7]*v/(c(7,r)*c(61,r)*c(7,q)*c(949,q))
    expected = {(l,m,i,j) for l,m in it.combinations_with_replacement(LS,2)
                for i,j in it.product(range(l+1),repeat=2)}
    check('complete_type_domain', set(y) == expected and len(y) == 270
          and {tuple(row['type']) for row in data['entries']} == expected and len(data['entries']) == 270)
    # Disjoint atom intervals instead of the constructor's removed/added subsets.
    entries, unordered, source_keys, affine = [], {}, {}, {}
    for saved in data['entries']:
        l,m,i,j = typ = tuple(saved['type'])
        atoms = [956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
        supports = [set(),set(),set()]
        offset = 0
        for mask,count in enumerate(atoms):
            for pos,bit in enumerate([4,2,1]):
                if mask & bit:
                    supports[pos].update(range(offset,offset+count))
            offset += count
        check('actual_type_'+str(typ), offset == 1024 and all(len(s) == 68 for s in supports)
              and min(atoms) >= 0 and F(*saved['y']) == y[typ] and F(*saved['affine']) == p[l+m-i-j]-y[typ])
        presentations, keys = [], []
        check('six_presentations_'+str(typ), len(saved['presentations']) == 6)
        for k,order in enumerate(it.permutations(range(3))):
            aa,bb,cc = [supports[t] for t in order]
            actual = [0]*8
            for x in range(1024):
                actual[4*(x in aa)+2*(x in bb)+(x in cc)] += 1
            a,b,h = len(aa-bb),len(aa-cc),len(bb-cc)
            t,s = len(aa-(bb|cc)),len((bb&cc)-aa)
            record = {'order':order,'atoms':actual,'source_indices':[a,b,t,s],
                      'h':h,'pair':p[h],'y':y[typ],'affine':p[h]-y[typ]}
            check('full_presentation_'+str((typ,k)), enc(record) == saved['presentations'][k]
                  and a+b-t-s == h and min(y[typ],p[a]-y[typ],1+y[typ]-p[a]-p[b]) >= 0)
            check('Boolean_forbidden_'+str((typ,k)), (0 not in [a,b,h] or y[typ] == p[max(a,b,h)])
                  and (not any(1 <= v <= 4 for v in [a,b,h]) or y[typ] == 0))
            key = (tuple(sorted([a,b,h])),t-s)
            check('source_equalities_'+str((typ,k)), key not in source_keys or source_keys[key] == y[typ])
            source_keys[key] = y[typ]
            keys.append(tuple(actual)); presentations.append(record)
        key = min(keys)
        check('full_unordered_key_'+str(typ), key not in unordered or unordered[key] == y[typ])
        unordered[key] = y[typ]
        affine[typ] = p[l+m-i-j]-y[typ]
        entries.append({'type':typ,'y':y[typ],'affine':affine[typ],'presentations':presentations})
    anchor = []
    for l,m in [(0,0),(0,5),(5,0),(0,6),(6,0),(0,7),(7,0)]:
        anchor.append({'layers':[l,m],'pair':p[l+m],'y':p[max(l,m)],'affine':p[l+m]-p[max(l,m)]})
    check('complete_zero_anchor', enc(anchor) == data['zero_anchor_cases'] and all(r['affine'] == 0 for r in anchor))
    # Reconstruct orthogonal polynomials by weighted normal equations, not Gram-Schmidt.
    bases,norms,factors = {},{},[]
    for saved in data['factor_bases']:
        n,l = saved['n'],saved['layer']
        wt = [c(7,i)*c(n-7,l-i) for i in range(l+1)]
        bs,ns,coefficients = [],[],[]
        for a in range(l+1):
            mom = [sum(w*i**k for i,w in enumerate(wt)) for k in range(2*a+1)]
            coeff = solve([[F(mom[i+j]) for j in range(a)] for i in range(a)],
                          [-F(mom[i+a]) for i in range(a)])[0] if a else []
            coeff.append(F(1)); coefficients.append(coeff)
            h = [sum(v*i**k for k,v in enumerate(coeff)) for i in range(l+1)]
            ns.append(sum(w*x*x for w,x in zip(wt,h))); bs.append(h)
            check('monic_orthogonal_'+str((n,l,a)), ns[-1] > 0 and all(sum(w*x*i**k for i,(w,x) in enumerate(zip(wt,h))) == 0 for k in range(a)))
        check('complete_basis_'+str((n,l)), enc(bs) == saved['basis'] and enc(ns) == saved['norms'] and wt == saved['weights'])
        check('distinct_Johnson_mode_labels_'+str((n,l)),
              len({eigen(n,l,a,1) for a in range(l+1)}) == l+1)
        bases[n,l],norms[n,l] = bs,ns
        factors.append({'n':n,'layer':l,'weights':wt,'basis':bs,'norms':ns,'polynomial_coefficients':coefficients})
    check('basis_domain', set(bases) == set(it.product([68,956],LS)) and len(factors) == 6)
    # Enumerate four occupancies to populate all relations simultaneously.
    transitions,gamma,ratios = [],{},{}
    saved_trans = {(r['n'],r['l'],r['m'],r['intersection']):r for r in data['complete_subset_transitions']}
    for n,l,m in it.product([68,956],LS,LS):
        qs = [[[0]*(m+1) for _ in range(l+1)] for _ in range(min(l,m)+1)]
        for i in range(l+1):
            sizes4 = [i,7-i,l-i,n-7-l+i]
            for u,v,w in it.product(range(m+1),repeat=3):
                z4 = m-u-v-w
                if z4 < 0:
                    continue
                val = c(sizes4[0],u)*c(sizes4[1],v)*c(sizes4[2],w)*c(sizes4[3],z4)
                if val:
                    qs[u+w][i][u+v] += val
        for t,Q in enumerate(qs):
            saved = saved_trans[n,l,m,t]
            check('full_transition_'+str((n,l,m,t)), Q == saved['matrix'] and all(sum(row) == c(l,t)*c(n-l,m-t) for row in Q))
            acts = []
            for a in range(m+1):
                act = [dot(row,bases[n,m][a]) for row in Q]; acts.append(act)
                check('saved_full_action_'+str((n,l,m,t,a)), enc(act) == saved['actions'][a])
                if a > l:
                    check('absent_mode_'+str((n,l,m,t,a)), not any(act))
                    continue
                h = bases[n,l][a]
                wt = [c(7,i)*c(n-7,l-i) for i in range(l+1)]
                g = sum(w*x*z for w,x,z in zip(wt,act,h))/norms[n,l][a]
                check('all_action_coordinates_'+str((n,l,m,t,a)), act == [g*x for x in h])
                gamma[n,l,m,a,t] = g
                B = beta(n,l,m,a,t)
                if l == m:
                    check('Johnson_mode_identity_'+str((n,l,a,t)), g == eigen(n,l,a,l-t))
                if B:
                    ratios.setdefault((n,l,m,a),[]).append(g/B)
                else:
                    check('zero_beta_'+str((n,l,m,a,t)), g == 0)
            transitions.append({'n':n,'l':l,'m':m,'intersection':t,'matrix':Q,'actions':acts})
    check('transition_domain', len(transitions) == len(data['complete_subset_transitions']) == len(saved_trans) == 118)
    scales = {}
    for key,rs in ratios.items():
        n,l,m,a = key
        check('signed_ratio_'+str(key), min(rs) > 0 and len(set(rs)) == 1 and enc(rs) == data['signed_beta_ratios'][str(key)])
        scales[key] = norms[n,l][a]*rs[0]
        for t in range(min(l,m)+1):
            g,back = gamma[n,l,m,a,t],gamma[n,m,l,a,t]
            check('adjoint_product_'+str((key,t)), norms[n,l][a]*g == norms[n,m][a]*back
                  and g*back == F(beta(n,l,m,a,t)**2,c(n-2*a,l-a)*c(n-2*a,m-a)))
    check('ratio_domain', len(ratios) == len(data['signed_beta_ratios']))
    for n,a in it.product([68,956],range(8)):
        layers = [l for l in LS if a <= l]
        for l,m in it.product(layers,repeat=2):
            check('coherent_triangle_'+str((n,a,l,m)), scales[n,l,m,a]*scales[n,7,7,a] == scales[n,l,7,a]*scales[n,m,7,a])
    blocks,minor_values,pivot_values = [],[],[]
    dims = dict.fromkeys(LS,0); traces = dict.fromkeys(LS,F(0)); split = {1:0,2:0,3:0}
    check('block_domain', len(data['blocks']) == 64 and {tuple(r['mode']) for r in data['blocks']} == set(it.product(range(8),repeat=2)))
    for saved in data['blocks']:
        a,b = saved['mode']
        layers = [l for l in LS if max(a,b) <= l]; split[len(layers)] += 1
        B = [[source(a,b,l,m,affine) for m in layers] for l in layers]
        G = [[sum(gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*affine[min(l,m),max(l,m),i,j]
                  for i,j in it.product(range(min(l,m)+1),repeat=2)) for m in layers] for l in layers]
        ns = [norms[68,l][a]*norms[956,l][b] for l in layers]
        ds = [c(68-2*a,l-a)*c(956-2*b,l-b) for l in layers]
        W = [[ns[i]*v for v in row] for i,row in enumerate(G)]
        base_scale = F(ns[-1],ds[-1])
        diagonal = [scales[68,l,7,a]*scales[956,l,7,b]/base_scale for l in layers]
        for i,l in enumerate(layers):
            for j,m in enumerate(layers):
                check('single_signed_congruence_'+str((a,b,l,m)), W[i][j] == W[j][i]
                      == base_scale*diagonal[i]*B[i][j]*diagonal[j] and min(diagonal) > 0)
        minors = []
        for size in range(1,len(layers)+1):
            for ind in it.combinations(range(len(layers)),size):
                d = determinant([[B[i][j] for j in ind] for i in ind])
                wd = determinant([[W[i][j] for j in ind] for i in ind])
                scale = F(1)
                for i in ind:
                    scale *= ns[i]/ds[i]
                check('strict_full_minor_'+str((a,b,ind)), d > 0 and wd == scale*d and scale > 0)
                minors.append({'indices':ind,'value':d,'weighted_value':wd,'positive_scale':scale})
                minor_values.append(d)
        pivots = []; previous = F(1)
        for k in range(1,len(layers)+1):
            d = determinant([row[:k] for row in B[:k]])
            pivots.append(d/previous/ds[k-1]); previous = d
        pivot_values.extend(pivots)
        mult = (c(68,a)-c(68,a-1))*(c(956,b)-c(956,b-1))
        check('positive_multiplicity_'+str((a,b)), mult > 0)
        for i,l in enumerate(layers):
            dims[l] += mult; traces[l] += mult*G[i][i]
        block = {'mode':[a,b],'layers':layers,'multiplicity':mult,'source_block':B,'actions':G,
                 'norms':ns,'D':ds,'weighted_block':W,'all_principal_minors':minors,
                 'normalized_pivots':pivots,'PSD':all(v['value'] >= 0 for v in minors)}
        check('every_saved_block_field_'+str((a,b)), enc(block) == saved)
        if max(a,b) <= 6:
            ss = small['complete_blocks'][7*a+b]; k = len(ss['layers'])
            check('L063_principal_restriction_'+str((a,b)), enc([r[:k] for r in B[:k]]) == ss['matrix'] and layers[:k] == ss['layers'])
        block['coherent_positive_diagonal'] = diagonal
        block['coherent_positive_prefactor'] = base_scale
        blocks.append(block)
    check('complete_dimensions', dims == sizes)
    check('complete_diagonal_traces', all(traces[l] == sizes[l]*(1-p[l]) for l in LS))
    check('block_split', split == {1:15,2:13,3:36})
    check('complete_minors_pivots', len(minor_values) == 306 and len(pivot_values) == 149 and min(pivot_values) == F(1,2))
    summary = {'verdict':'AUDIT_FAILURE' if failures else 'RETAIN_L075','checks':len(checks),
               'failures':len(failures),'types':len(entries),'presentations':sum(len(r['presentations']) for r in entries),
               'zero_anchor_cases':len(anchor),'source_blocks':len(blocks),'block_split':split,
               'transitions':len(transitions),'positive_principal_minors':sum(v > 0 for v in minor_values),
               'required_principal_minors':306,'normalized_pivots':len(pivot_values),
               'minimum_normalized_pivot':min(pivot_values),'required_pivot_lower_bound':0,
               'dimensions':dims,'diagonal_traces':traces}
    result = {'summary':summary,'checks':checks,'failures':failures,
              'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'rho':rho,'pairs':p[:15],'pair_residuals':pair_residuals,'parameters':pars,
              'column':f,'weighted_kernel_residuals':residuals,'completion_modes':completion_modes,
              'completion_basis_pivots':basis_pivots,'z':z,'entries':entries,'anchor':anchor,
              'factors':factors,'transitions':transitions,'signed_ratios':ratios,'blocks':blocks}
    OUT.write_text(json.dumps(enc(result),indent=2)+'\n')
    print(json.dumps(enc(summary),sort_keys=True))
    print('Full certificate and failures: '+str(OUT.relative_to(NB)))
    if failures:
        print('Failures: '+str(failures))
        raise SystemExit(1)


if __name__ == '__main__':
    main()

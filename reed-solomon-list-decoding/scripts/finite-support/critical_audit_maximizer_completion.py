"""Dedicated L073 audit: manuscript basis, direct weighted actions, full arrays.

Standard library only. Imports L065 kernel exhaustion and L067's proved
mixed-layer decomposition, independently checking its finite basis actions.
"""
import hashlib
import itertools as it
import json
import re
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'maximizer-completion-critical-audit.json'


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b)), F(0))


@lru_cache(None)
def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*c(u,t)*c(n-2*a,u-a)*c(n-a-u,l-u)*c(n-a-u,m-u)
               for u in range(max(a,t),min(l,m,n-a)+1))


def eigen(n, a, r):
    return sum((-1)**s*c(a,s)*c(7-a,r-s)*c(n-7-a,r-s) for s in range(r+1))


def determinant(M):
    return sum((-1)**j*M[0][j]*determinant([r[:j]+r[j+1:] for r in M[1:]])
               for j in range(len(M))) if M else F(1)


def main():
    names = ['maximizer-completion-results.json','maximizer-completion-verification.json',
             'seven-distance-full-base-kernel-results.json','simultaneous-shell-ordinary-scalars-results.json',
             'alternative-product-zero-plane-results.json','seven-shell-affine-fixed-dual-results.json',
             'simultaneous-seven-shell-critical-audit.json']
    paths = [ROOT/n for n in names]
    data,ver,col,old,point,square,algebra = [json.loads(p.read_text()) for p in paths]
    manuscript_path = NB/'lemmas/L073-maximizer-simultaneous-seven-shell-psd-completion.md'
    manuscript = manuscript_path.read_text()
    checks,failures = [],[]
    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    for path,obj in zip(paths,[data,ver,col,old,point,square,algebra]):
        check('clean_'+path.name, obj['failures'] == [])
        for rel,digest in obj.get('input_hashes',obj.get('source_hashes',{})).items():
            check('hash_'+path.name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p = [F(*x) for x in data['pairs']]
    rho = (F(c(1024,64),c(68,64))+1)/(2*c(1024,68))
    check('original_pairs', len(p) == 14 and p[:13] == [F(*x) for x in old['pairs_through_12']]
          and p[5:8] == [F(1,68881143660),F(133,9357995374380),F(3539,248922676958508)]
          and p[13] == F(26968792942808537,1896913598738625271419892200)
          and rho == F(*data['rho']) == F(*old['rho']) > 0)
    M = [[F(*x) for x in r] for r in square['objective_matrix']]
    N = [[F(*x) for x in r] for r in point['plane_matrix']]
    w,v = -M[0][3]/M[3][3],-N[0][2]/N[2][2]
    parameters = [F(0),v,w]
    check('exact_parameters', M[3][3] < 0 and N[2][2] < 0 and v > 0
          and enc(parameters) == data['parameters'] == ver['parameters'] == point['stationary']['parameters'])
    rr = [[F(*x) for x in r] for r in col['equation_rref']]
    piv = col['equation_pivots']
    check('rref_shape', len(rr) == 49 and all(len(r) == 50 for r in rr) and len(piv) == 46
          and [j for j in range(49) if j not in piv] == [27,33,42])
    f = [F(0)]*49
    f[27],f[33],f[42] = parameters
    for i,j in enumerate(piv):
        f[j] = rr[i][-1]-sum(rr[i][k]*f[k] for k in [27,33,42])
    check('full_column_values', enc(f) == data['free_column'] == ver['free_column'] and min(f) >= 0)
    for i,(r,b) in enumerate(zip(col['equations'],col['rhs'])):
        check('original_equation_'+str(i), len(r) == 49 and dot([F(*x) for x in r],f) == F(*b))
    entries = {tuple(r['type']):F(*r['y']) for r in old['types']}
    column,weights = [],[]
    for row in col['column']:
        l,i,j = row['orbit']
        y = p[7]*f[row['variable']] if row['kind'] == 'free' else F(*row['value'])
        column.append(y)
        weights.append(c(7,i)*c(61,l-i)*c(7,j)*c(949,l-j) if l else 1)
        if l:
            entries[l,7,i,j] = y
        else:
            check('anchor_column', y == p[7])
    check('all_weights', len(column) == 86 and weights == col['weights'] and min(weights) > 0)
    residuals = [dot([F(*x)*wt for x,wt in zip(r,weights)],column) for r in col['kernel_basis']]
    check('complete_kernel', len(col['kernel_basis']) == 49 and all(len(r) == 86 for r in col['kernel_basis'])
          and residuals == [F(0)]*49 and enc(residuals) == ver['weighted_kernel_residuals'])
    free = [(r,q) for r,q in it.product(range(8),repeat=2) if r+q >= 7]
    valencies = [c(7,r)*c(61,r)*c(7,q)*c(949,q) for r,q in free]
    check('original_variable_order', enc(free) == data['free'] and len(free) == 36 and free[28] == (7,0) and min(valencies) > 0)
    for r,q in it.product(range(8),repeat=2):
        h = r+q
        if h <= 6:
            entries[7,7,7-r,7-q] = p[7] if h == 0 else F(0) if h <= 4 else entries[h,7,q,r]
    # Independent direct subset actions using the already audited monic bases.
    norms,bases,gamma,scales,transitions = {},{},{},{},[]
    for row in algebra['factors']:
        n,l = row['n'],row['layer']
        wt = [c(7,i)*c(n-7,l-i) for i in range(l+1)]
        bs = [[F(*x) for x in r] for r in row['basis']]
        ns = [dot([w*x for w,x in zip(wt,h)],h) for h in bs]
        check('basis_'+str((n,l)), len(bs) == l+1 and all(len(h) == l+1 for h in bs)
              and wt == row['weights'] and enc(ns) == row['norms'] and min(ns) > 0
              and all(dot([w*x for w,x in zip(wt,bs[a])],bs[b]) == 0 for a in range(l+1) for b in range(a)))
        norms[n,l],bases[n,l] = ns,bs
    for row in algebra['transitions']:
        n,l,m,t = [row[k] for k in ['n','l','m','t']]
        Q = [[sum(c(i,x)*c(7-i,j-x)*c(l-i,t-x)*c(n-7-l+i,m-j-t+x) for x in range(8)) for j in range(m+1)] for i in range(l+1)]
        check('transition_'+str((n,l,m,t)), Q == row['matrix'])
        actions = []
        for a in range(m+1):
            actual = [dot(q,bases[n,m][a]) for q in Q]
            if a <= l:
                pivot = next(i for i,x in enumerate(bases[n,l][a]) if x)
                g = actual[pivot]/bases[n,l][a][pivot]
                gamma[n,l,m,a,t] = g
                check('action_'+str((n,l,m,t,a)), actual == [g*x for x in bases[n,l][a]] and enc(g) == row['actions'][a])
            else:
                g = F(0)
                check('absent_action_'+str((n,l,m,t,a)), not any(actual) and enc(g) == row['actions'][a])
            actions.append(g)
        transitions.append({'n':n,'l':l,'m':m,'t':t,'matrix':Q,'actions':actions})
    check('all_transitions', len(transitions) == 118 and set(gamma) == {(n,l,m,a,t) for n,l,m in it.product([68,956],[5,6,7],[5,6,7]) for a in range(min(l,m)+1) for t in range(min(l,m)+1)})
    for n,l,m in it.product([68,956],[5,6,7],[5,6,7]):
        for a in range(min(l,m)+1):
            ratios = []
            for t in range(min(l,m)+1):
                B,g,back = beta(n,l,m,a,t),gamma[n,l,m,a,t],gamma[n,m,l,a,t]
                check('adjoint_beta_'+str((n,l,m,a,t)), norms[n,l][a]*g == norms[n,m][a]*back
                      and g*back == F(B*B,c(n-2*a,l-a)*c(n-2*a,m-a)))
                if B:
                    ratios.append(g/B)
                else:
                    check('zero_beta_'+str((n,l,m,a,t)), g == back == 0)
            check('positive_scale_'+str((n,l,m,a)), len(set(ratios)) == 1 and ratios[0] > 0)
            scales[n,l,m,a] = norms[n,l][a]*ratios[0]
    for n,a in it.product([68,956],range(8)):
        layers = [l for l in [5,6,7] if a <= l]
        for l,m in it.product(layers,repeat=2):
            check('triangle_'+str((n,a,l,m)), scales[n,l,m,a]*scales[n,7,7,a] == scales[n,l,7,a]*scales[n,m,7,a])
    sizes = {l:c(68,l)*c(956,l) for l in [5,6,7]}
    rows,bounds,modes,ranks = [],[],[],{}
    for ix,(a,b) in enumerate(it.product(range(8),repeat=2)):
        layers = [l for l in [6,5] if max(a,b) <= l]
        ns = {l:norms[68,l][a]*norms[956,l][b] for l in layers+[7]}
        d7 = c(68-2*a,7-a)*c(956-2*b,7-b)
        def action(l,m):
            return sum(gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*entries[min(l,m),max(l,m),i,j]
                       for i,j in it.product(range(min(l,m)+1),repeat=2))-(p[l]*p[m]*sizes[m] if ix == 0 else 0)
        K = [[ns[l]*action(l,m) for m in layers] for l in layers]
        cross = [ns[l]*action(l,7) for l in layers]
        scales_here = {l:scales[68,l,7,a]*scales[956,l,7,b]/(ns[7]/d7) for l in layers}
        saved = ver['mode_evidence'][ix]
        for i,l in enumerate(layers):
            si = sorted(layers).index(l)
            check('both_cross_'+str((ix,l)), cross[i] == ns[7]*action(7,l)
                  == ns[7]/d7*scales_here[l]*F(*saved['cross'][si]) and scales_here[l] > 0)
            for j,m in enumerate(layers):
                sj = sorted(layers).index(m)
                check('coherent_base_'+str((ix,l,m)), K[i][j] == K[j][i]
                      == ns[7]/d7*scales_here[l]*scales_here[m]*F(*saved['B'][si][sj]))
        work,rhs,cost,pivots,ranges = [r[:] for r in K],cross[:],F(0),[],[]
        for i in range(len(layers)):
            pivot = work[i][i]
            pivots.append(pivot)
            check('pivot_'+str((ix,i)), pivot >= 0)
            if not pivot:
                residual = [rhs[i]]+work[i][i+1:]
                ranges.append(residual)
                check('singular_range_'+str((ix,i)), not any(residual))
            else:
                cost += rhs[i]**2/pivot
                for j in range(i+1,len(layers)):
                    rhs[j] -= work[j][i]*rhs[i]/pivot
                    for k in range(i+1,len(layers)):
                        work[j][k] -= work[j][i]*work[i][k]/pivot
        key = str((len(layers),sum(x > 0 for x in pivots)))
        ranks[key] = ranks.get(key,0)+1
        required = cost/(p[7]*ns[7])
        check('whole_energy_'+str(ix), required == F(*saved['energy'])/(p[7]*d7) == F(*data['modes'][ix]['required']))
        fixed = sum(beta(68,7,7,a,i)*beta(956,7,7,b,j)*y for (l,m,i,j),y in entries.items() if l == m == 7)
        fixed -= p[7]**2*sizes[7]**2 if ix == 0 else 0
        bound = fixed/(p[7]*d7)-required
        row = [-F(eigen(68,a,r)*eigen(956,b,q),val) for (r,q),val in zip(free,valencies)]
        for j,(r,q) in enumerate(free):
            check('source_row_'+str((ix,j)), row[j] == -F(beta(68,7,7,a,7-r)*beta(956,7,7,b,7-q),d7*valencies[j]))
        check('original_rows_bounds_'+str(ix), enc(row) == saved['row'] == data['matrix'][ix]
              and enc(bound) == saved['bound'] == data['rhs'][ix])
        rows.append(row); bounds.append(bound)
        modes.append({'mode':[a,b],'layers':layers,'weighted_base':K,'weighted_cross':cross,'norms':ns,
                      'scales':scales_here,'pivots':pivots,'ranges':ranges,'cost':cost,'row':row,'bound':bound})
    # Use the manuscript's 35 rows and e_28; solve by reverse-column elimination.
    section = manuscript.split('whose first 35 rows are the rows A_i, in this order:')[1].split('The last row')[0]
    indices = [int(x) for x in re.findall(r'\d+',section)]
    defining = [['mode',i] for i in indices]+[['sign',28]]
    check('manuscript_basis_indices', len(indices) == len(set(indices)) == 35 and defining == data['certificate']['defining_rows'])
    order = list(reversed(range(36)))
    mat = [[rows[i][j] for j in order]+[bounds[i]] for i in indices]+[[F(j == 28) for j in order]+[F(0)]]
    pivots = []
    for i in range(36):
        j = next((j for j in range(i,36) if mat[j][i]),None)
        check('basis_pivot_'+str(i), j is not None)
        if j is None:
            raise ArithmeticError('Manuscript basis singular')
        mat[i],mat[j] = mat[j],mat[i]
        pivot = mat[i][i]; pivots.append(pivot)
        for j in range(i+1,36):
            factor = mat[j][i]/pivot
            mat[j] = [x-factor*y for x,y in zip(mat[j],mat[i])]
    permuted = [F(0)]*36
    for i in reversed(range(36)):
        permuted[i] = (mat[i][-1]-sum(mat[i][j]*permuted[j] for j in range(i+1,36)))/mat[i][i]
    z = list(reversed(permuted))
    check('fresh_original_solution', enc(z) == data['certificate']['z'] == ver['fresh_original_basis_solution'])
    for j,value in enumerate(z):
        check('sign_'+str(j), value == 0 if j == 28 else value > 0)
    slacks = [b-dot(row,z) for row,b in zip(rows,bounds)]
    for i,x in enumerate(slacks):
        check('original_mode_'+str(i), x >= 0 and enc(x) == data['certificate']['mode_slacks'][i] == ver['mode_evidence'][i]['slack'])
    zeros = [i for i,x in enumerate(slacks) if not x]
    section = manuscript.split('mode indices are')[1].split('Every other variable')[0]
    check('manuscript_zero_modes', zeros == [int(x) for x in re.findall(r'\d+',section)] == ver['tight_mode_indices'])
    raw = [p[7]*x/val for x,val in zip(z,valencies)]
    check('all_raw_Y', enc(raw) == data['certificate']['raw_Y'])
    for (r,q),y in zip(free,raw):
        entries[7,7,7-r,7-q] = y
    expected_types = {(l,m,i,j) for l,m in [(5,5),(5,6),(6,6),(5,7),(6,7),(7,7)] for i,j in it.product(range(l+1),repeat=2)}
    check('complete_types', set(entries) == expected_types and len(entries) == 270 and min(entries.values()) >= 0)
    vr = {tuple(r['type']):r for r in ver['records']}
    cr = {tuple(r['type']):r for r in data['records']}
    groups,source_keys,records,scalar_slacks = {},{},{},[]
    for typ,y in entries.items():
        l,m,i,j = typ
        atom = (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i)
        orders = []
        for perm in it.permutations([4,2,1]):
            at = [0]*8
            for mask,count in enumerate(atom):
                at[sum(new for old,new in zip([4,2,1],perm) if mask & old)] += count
            orders.append(tuple(at))
        check('all_presentations_'+str(typ), sorted(orders) == sorted(tuple(at) for at in vr[typ]['regions'])
              == sorted(tuple(at) for at in cr[typ]['regions']) and enc(y) == vr[typ]['value']
              and (cr[typ]['value'] is None or enc(y) == cr[typ]['value']) and min(atom) >= 0)
        key = min(orders)
        check('full_key_'+str(typ), key not in groups or groups[key] == y)
        groups[key] = y
        for at in orders:
            a,b,h,t,s = at[4]+at[5],at[4]+at[6],at[2]+at[6],at[4],at[3]
            skey = (tuple(sorted([a,b,h])),t-s)
            check('source_key_'+str((typ,at)), skey not in source_keys or source_keys[skey] == key)
            source_keys[skey] = key
            if 0 in [a,b,h]:
                check('boolean_'+str((typ,at)), y == p[max(a,b,h)])
            elif any(1 <= d <= 4 for d in [a,b,h]):
                check('forbidden_'+str((typ,at)), y == 0)
            if typ[:2] != (7,7):
                scalar_slacks.extend([y,p[a]-y,1+y-p[a]-p[b]])
        records[typ] = {'value':y,'orders':orders,'key':key}
    # Presentation order differs by inverse permutation; compare complete multisets.
    check('all_inherited_scalars', len(scalar_slacks) == 3708 and min(scalar_slacks) == 0
          and sorted(scalar_slacks) == sorted(F(*x) for x in ver['all_inherited_scalar_slacks']))
    all_minors = []
    for ix,(a,b) in enumerate(it.product(range(8),repeat=2)):
        layers = [l for l in [5,6,7] if max(a,b) <= l]
        def source_entry(l,m):
            return sum(beta(68,l,m,a,i)*beta(956,l,m,b,j)*entries[min(l,m),max(l,m),i,j]
                       for i,j in it.product(range(min(l,m)+1),repeat=2))-(p[l]*p[m]*sizes[l]*sizes[m] if ix == 0 else 0)
        block = [[source_entry(l,m) for m in layers] for l in layers]
        saved = ver['mode_evidence'][ix]
        check('entire_source_block_'+str(ix), enc(block) == saved['full_block']
              and enc(block[-1][-1]) == saved['raw_new_anchor_corrected'])
        minors = []
        for count in range(1,len(layers)+1):
            for subset in it.combinations(range(len(layers)),count):
                value = determinant([[block[i][j] for j in subset] for i in subset])
                check('principal_minor_'+str((ix,subset)), value >= 0)
                minors.append({'indices':subset,'value':value}); all_minors.append(value)
        check('complete_minor_array_'+str(ix), enc(minors) == saved['all_principal_minors'])
        md = modes[ix]; norm7 = md['norms'][7]
        # New/new direct action completes the already checked coherent congruence.
        new_action = sum(gamma[68,7,7,a,i]*gamma[956,7,7,b,j]*entries[7,7,i,j] for i,j in it.product(range(8),repeat=2))
        new_action -= p[7]**2*sizes[7] if ix == 0 else 0
        check('new_block_normalization_'+str(ix), new_action == block[-1][-1]/(c(68-2*a,7-a)*c(956-2*b,7-b))
              and (norm7*new_action-md['cost'])/(p[7]*norm7) == slacks[ix])
        md.update({'full_source_block':block,'minors':minors,'weighted_new':norm7*new_action,'slack':slacks[ix]})
    for l in [5,6,7]:
        total = sum((c(68,a)-c(68,a-1))*(c(956,b)-c(956,b-1)) for a,b in it.product(range(l+1),repeat=2))
        check('multiplicity_exhaustion_'+str(l), total == sizes[l])
    check('all_rank_cases', ranks == {'(2, 1)':8,'(2, 0)':19,'(2, 2)':9,'(1, 1)':10,'(1, 0)':3,'(0, 0)':15})
    initial_path = ROOT/'maximizer-completion-critical-audit-initial.json'
    initial = json.loads(initial_path.read_text())
    stable = {'parameters':parameters,'column':column,'weights':weights,'kernel_residuals':residuals,
              'transitions':transitions,'scales':scales,'reverse_basis_pivots':pivots,'z':z,
              'records':records,'modes':modes,'inherited_scalar_slacks':scalar_slacks,'all_principal_minors':all_minors}
    check('initial_tag_mismatch_only', initial['failures'] == ['manuscript_basis_indices']
          and initial['defining_rows'][:-1] == defining[:-1]
          and initial['defining_rows'][-1] == ['nonnegative',28]
          and all(initial[k] == enc(value) for k,value in stable.items()))
    summary = {'checks':len(checks),'failures':len(failures),'basis_rank':36,'original_modes':64,
               'positive_variables':sum(x > 0 for x in z),'zero_variable_indices':[j for j,x in enumerate(z) if not x],
               'positive_modes':sum(x > 0 for x in slacks),'zero_modes':len(zeros),'principal_minors':len(all_minors),
               'types':len(entries),'presentations':6*len(entries),'inherited_scalar_rows':len(scalar_slacks),
               'kernel_residuals':len(residuals),'transitions':len(transitions),'mode_ranks':ranks,
               'actual_minimum_slack':min(slacks),'required_minimum_slack':0,
               'verdict':'RETAIN L073' if not failures else 'AUDIT_FAILED'}
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checks':checks,'failures':failures,'summary':summary,'parameters':parameters,'column':column,
              'weights':weights,'kernel_residuals':residuals,'transitions':transitions,'scales':scales,
              'defining_rows':defining,'reverse_basis_pivots':pivots,'z':z,'records':records,'modes':modes,
              'inherited_scalar_slacks':scalar_slacks,'all_principal_minors':all_minors}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print(json.dumps(enc(summary),sort_keys=True))
    print('Failures='+str(failures)+'; full certificate='+str(OUT.relative_to(NB)))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

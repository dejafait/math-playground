"""L072 critical audit. Exact arithmetic; no optimizer or notebook imports.

Import L065 kernel exhaustion and L067's audited mixed-layer decomposition.
Reconstruct the RREF family, all domains, and coefficientwise weighted costs.
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
OUT = ROOT/'alternative-product-zero-plane-critical-audit.json'


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
    return sum((-1)**(u-t)*c(u, t)*c(n-2*a, u-a)*c(n-a-u, l-u)*c(n-a-u, m-u)
               for u in range(max(a, t), min(l, m, n-a)+1))


def eigen(n, a, r):
    return sum((-1)**s*c(a, s)*c(7-a, r-s)*c(n-7-a, r-s) for s in range(r+1))


def main():
    names = ['alternative-product-zero-plane-results.json', 'alternative-product-zero-plane-verification.json',
             'alternative-product-zero-plane-initial.json', 'alternative-product-zero-plane-verification-initial.json',
             'seven-distance-full-base-kernel-results.json', 'seven-shell-affine-fixed-dual-results.json',
             'simultaneous-shell-ordinary-scalars-results.json', 'zero-dual-plane-scalars-results.json',
             'zero-point-remaining-modes-results.json', 'simultaneous-seven-shell-critical-audit.json',
             'seven-shell-affine-fixed-dual-critical-audit.json']
    paths = [ROOT/n for n in names]
    data, ver, initial, iv, col, square, old, scalar, fixed, algebra, affine_audit = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for index, (path, obj) in enumerate(zip(paths, [data, ver, initial, iv, col, square, old, scalar, fixed, algebra, affine_audit])):
        if index not in [2, 3]:
            check('clean_'+path.name, obj['failures'] == [])
        # Initial reports intentionally retain old provenance, inspected separately below.
        if index not in [2, 3]:
            for rel, digest in obj.get('input_hashes', obj.get('source_hashes', {})).items():
                check('hash_'+path.name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p = [F(*x) for x in scalar['pairs_through_13']]
    rho = (F(c(1024, 64), c(68, 64))+1)/(2*c(1024, 68))
    check('original_pairs_normalization', rho == F(*data['rho']) == F(*old['rho']) > 0
          and p[:13] == [F(*x) for x in old['pairs_through_12']]
          and p[5:8] == [F(1,68881143660), F(133,9357995374380), F(3539,248922676958508)]
          and p[13] == F(26968792942808537,1896913598738625271419892200))
    rr = [[F(*x) for x in r] for r in col['equation_rref']]
    piv = col['equation_pivots']
    check('original_RREF_shape', len(rr) == 49 and all(len(r) == 50 for r in rr)
          and len(piv) == 46 and [i for i in range(49) if i not in piv] == [27,33,42])
    fs = [[F(0)]*4 for _ in range(49)]
    for j, free in enumerate([27,33,42], 1):
        fs[free][j] = F(1)
    for i, j in enumerate(piv):
        fs[j] = [rr[i][-1]]+[-rr[i][k] for k in [27,33,42]]
    check('all_affine_coordinates', enc(fs) == affine_audit['domain']
          and all(enc(f) == [x]+y for f,x,y in zip(fs,col['affine']['intercept'],col['affine']['slopes'])))
    for i, (row, rhs) in enumerate(zip(col['equations'], col['rhs'])):
        check('affine_equation_'+str(i), [dot([F(*x) for x in row], [f[j] for f in fs]) for j in range(4)] == [F(*rhs),0,0,0])
    oldM = [[F(*x) for x in r] for r in square['objective_matrix']]
    w = oldM[0][3]/(-oldM[3][3])
    check('exact_old_zero_plane', oldM[3][3] < 0 and -oldM[3][3]*oldM[0][0]+oldM[0][3]**2 == 0
          and all(oldM[i][j] == 0 for i,j in it.product(range(4),repeat=2) if i in [1,2] or j in [1,2])
          and w == F(*data['w_star']) == F(*scalar['w_star']))
    plane = [[f[0]+w*f[3],f[1],f[2]] for f in fs]
    check('complete_plane', enc(plane) == data['plane_nonnegativity'] == scalar['plane_free'])
    av = lambda x: [F(x),F(0),F(0),F(0)]
    entries = {tuple(r['type']):av(F(*r['y'])) for r in old['types']}
    columns, orbit_weights = [], []
    for index, row in enumerate(col['column']):
        val = [p[7]*x for x in fs[row['variable']]] if row['kind'] == 'free' else av(F(*row['value']))
        columns.append(val)
        if index == 0:
            check('anchor', row['orbit'] == [0,0,0] and val == av(p[7]))
            orbit_weights.append(1)
        else:
            l,i,j = row['orbit']
            entries[l,7,i,j] = val
            orbit_weights.append(c(7,i)*c(61,l-i)*c(7,j)*c(949,l-j))
    check('all_86_orbit_weights', orbit_weights == col['weights'] and len(orbit_weights) == 86 and min(orbit_weights) > 0)
    kernel_residuals = []
    for i, row in enumerate(col['kernel_basis']):
        res = [dot([F(*x)*wt for x,wt in zip(row,orbit_weights)], [v[j] for v in columns]) for j in range(4)]
        kernel_residuals.append(res)
        check('full_affine_kernel_'+str(i), res == [0]*4)
    check('49_kernel_rows', len(kernel_residuals) == 49)
    for r,q in it.product(range(8), repeat=2):
        h = r+q
        entries[7,7,7-r,7-q] = av(p[7]) if h == 0 else av(0) if h <= 4 else entries[h,7,q,r] if h <= 6 else None
    types = [(l,m,i,j) for l,m in [(5,5),(5,6),(6,6),(5,7),(6,7),(7,7)] for i,j in it.product(range(l+1),repeat=2)]
    check('complete_types', set(entries) == set(types) and [list(t) for t in types] == [r['type'] for r in data['records']])
    lookup_names = [n for n in iv['checks'] if n.startswith('full_unordered_presentation_')]
    expected_initial_failures, missing, records, scalar_rows, old_slacks = [], [], [], [], []
    groups, source_groups = {}, {}
    for index, typ in enumerate(types):
        l,m,i,j = typ
        atoms = [956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
        orders, value = [], entries[typ]
        for order_index, bits in enumerate(it.permutations([4,2,1])):
            at = [0]*8
            for mask, count in enumerate(atoms):
                at[sum(new for new,bit in zip([4,2,1],bits) if mask & bit)] = count
            a,b,h = at[4]+at[5],at[4]+at[6],at[2]+at[6]
            lookup = av(p[max(a,b,h)]) if min(a,b,h) == 0 else av(0) if min(a,b,h) <= 4 else entries.get((*sorted([a,b]),at[4],at[3]))
            check('presentation_'+str((typ,order_index)), min(at) >= 0 and sum(at) == 1024
                  and all(sum(x for mask,x in enumerate(at) if mask & bit) == 68 for bit in [1,2,4])
                  and (lookup is None or lookup == value))
            if lookup is None and value is not None:
                expected_initial_failures.append(lookup_names[6*index+order_index])
                missing.append({'type':typ,'order':order_index,'incident_layers':sorted([a,b]),'lookup_key':(*sorted([a,b]),at[4],at[3])})
                check('unavailable_outside_retained_'+str((typ,order_index)), tuple(sorted([a,b])) not in [(5,5),(5,6),(6,6),(5,7),(6,7),(7,7)])
            orders.append(at)
            source_groups.setdefault((*sorted([a,b,h]),at[4]-at[3]),set()).add(typ)
            if l in [5,6] and m == 7:
                val = [value[0]+w*value[3],value[1],value[2]]
                slacks = [val,[p[a]-val[0],-val[1],-val[2]],[1+val[0]-p[a]-p[b],val[1],val[2]]]
                for s in slacks:
                    check('scalar_affine_'+str(len(scalar_rows)), enc(s) == scalar['inequalities'][len(scalar_rows)]['affine'])
                    scalar_rows.append(s)
            elif m <= 6:
                yy = value[0]
                slacks = [yy,p[a]-yy,1+yy-p[a]-p[b]]
                saved = old['types'][index]['presentations'][order_index]
                check('old_presentation_'+str((typ,order_index)), saved['atoms'] == at and saved['slacks'] == enc(slacks) and min(slacks) >= 0)
                old_slacks.extend(slacks)
        key = tuple(min(orders))
        check('full_record_'+str(typ), data['records'][index] == {'type':list(typ),'regions':orders,'affine':enc(value)})
        check('shared_key_'+str(typ), key not in groups or groups[key] == value)
        groups[key] = value
        records.append({'type':typ,'key':key,'orders':orders,'affine':value})
    keys_by_type = {tuple(r['type']):r['key'] for r in records}
    for key, group in source_groups.items():
        check('source_equality_'+str(key), len({keys_by_type[t] for t in group}) == 1)
    free = [(r,q) for r,q in it.product(range(8),repeat=2) if r+q >= 7]
    check('36_distinct_free_28_forced', len({keys_by_type[7,7,7-r,7-q] for r,q in free}) == 36
          and sum(entries[7,7,i,j] is not None for i,j in it.product(range(8),repeat=2)) == 28)
    check('all_domain_rows', len(scalar_rows) == 1530 and len(old_slacks) == 2178)
    check('all_268_initial_failures_explained', expected_initial_failures == iv['failures'] and len(missing) == 268)
    stable_iv = [k for k in iv if k not in ['input_hashes','checks','failures','summary']]
    check('initial_verifier_all_mathematics_unchanged', all(iv[k] == ver[k] for k in stable_iv))
    stable_initial = [k for k in initial if k not in ['input_hashes','checks','failures','stage','summary']]
    check('initial_constructor_all_coefficients_unchanged', initial['failures'] == ['plane_strict_concavity'] and all(initial[k] == data[k] for k in stable_initial))

    # Import the audited direct subset actions, verify their complete basis actions.
    factors = {(r['n'],r['layer']):r for r in algebra['factors']}
    norms,bases,gamma = {},{},{}
    for (n,l),row in factors.items():
        weights = [c(7,i)*c(n-7,l-i) for i in range(l+1)]
        basis = [[F(*v) for v in r] for r in row['basis']]
        ns = [dot([wt*x for wt,x in zip(weights,h)],h) for h in basis]
        check('factor_'+str((n,l)), weights == row['weights'] and enc(ns) == row['norms'] and min(ns) > 0)
        norms[n,l],bases[n,l] = ns,basis
    for row in algebra['transitions']:
        n,l,m,t = [row[k] for k in ['n','l','m','t']]
        Q = [[sum(c(i,x)*c(7-i,j-x)*c(l-i,t-x)*c(n-7-l+i,m-j-t+x) for x in range(8)) for j in range(m+1)] for i in range(l+1)]
        check('direct_transition_'+str((n,l,m,t)), Q == row['matrix'])
        for a in range(m+1):
            g = F(*row['actions'][a])
            target = [g*v for v in bases[n,l][a]] if a <= l else [F(0)]*(l+1)
            check('full_action_'+str((n,l,m,t,a)), [dot(q,bases[n,m][a]) for q in Q] == target)
            if a <= min(l,m):
                gamma[n,l,m,a,t] = g
    check('transition_exhaustion', set(gamma) == {(n,l,m,a,t) for n,l,m in it.product([68,956],[5,6,7],[5,6,7]) for a in range(min(l,m)+1) for t in range(min(l,m)+1)})
    manuscript = (NB/'lemmas/L072-alternative-product-zero-plane-positive-maximum.md').read_text()
    parse = lambda label: [F(x.strip()) for x in re.search(r'    '+label+r'=\((.*?)\),',manuscript,re.S).group(1).split(',')]
    head,tail = parse('h'),parse('k')
    dual = [a*b for a,b in it.product(head,tail)]
    check('unchanged_product_weights', enc(dual) == data['weights'] == fixed['certificate']['mode_weights'] and min(dual) >= 0 and sum(v > 0 for v in dual) == 24)
    scales = {k:F(*v) for k,v in algebra['signed_scales'].items()}
    sizes = {l:c(68,l)*c(956,l) for l in [5,6,7]}
    modes, ranks, M = [],{},[[F(0)]*4 for _ in range(4)]
    scaled_rows, raw_rows = [],[]
    for index,(a,b) in enumerate(it.product(range(8),repeat=2)):
        layers = [l for l in [6,5] if max(a,b) <= l]
        norm = {l:norms[68,l][a]*norms[956,l][b] for l in layers+[7]}
        d7 = c(68-2*a,7-a)*c(956-2*b,7-b)
        check('positive_mode_scaling_'+str(index), d7 > 0 and norm[7] > 0)
        def action(l,m):
            out = [sum(gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*entries[min(l,m),max(l,m),i,j][z]
                       for i,j in it.product(range(min(l,m)+1),repeat=2)) for z in range(4)]
            if index == 0:
                out[0] -= p[l]*p[m]*sizes[m]
            return out
        B = [[norm[l]*action(l,m)[0] for m in layers] for l in layers]
        cross = [[norm[l]*x for x in action(l,7)] for l in layers]
        saved = data['modes'][index]
        s = {l:scales[str((68,l,7,a))]*scales[str((956,l,7,b))]/(norm[7]/d7) for l in layers}
        for i,l in enumerate(layers):
            si = sorted(layers).index(l)
            check('both_cross_directions_'+str((index,l)), s[l] > 0 and cross[i] == [norm[7]*x for x in action(7,l)]
                  == [norm[7]/d7*s[l]*F(*x) for x in saved['cross'][si]])
            for j,m in enumerate(layers):
                sj = sorted(layers).index(m)
                check('whole_congruence_'+str((index,l,m)), B[i][j] == B[j][i] == norm[7]/d7*s[l]*s[m]*F(*saved['B'][si][sj]))
        work, rhs = [r[:] for r in B],[r[:] for r in cross]
        cost,pivots,ranges = [[F(0)]*4 for _ in range(4)],[],[]
        for i in range(len(layers)):
            pivot = work[i][i]
            pivots.append(pivot)
            check('positive_pivot_'+str((index,i)), pivot >= 0)
            if not pivot:
                residual = rhs[i]+work[i][i+1:]
                ranges.append(residual)
                check('whole_affine_singular_range_'+str((index,i)), not any(residual))
                continue
            for j,k in it.product(range(4),repeat=2):
                cost[j][k] += rhs[i][j]*rhs[i][k]/pivot
            for j in range(i+1,len(layers)):
                rhs[j] = [x-work[j][i]*y/pivot for x,y in zip(rhs[j],rhs[i])]
                for k in range(i+1,len(layers)):
                    work[j][k] -= work[j][i]*work[i][k]/pivot
        category = str((len(layers),sum(x > 0 for x in pivots)))
        ranks[category] = ranks.get(category,0)+1
        cost = [[x/(p[7]*norm[7]) for x in r] for r in cost]
        check('all_energy_coefficients_'+str(index), enc(cost) == saved['cost'] == affine_audit['modes'][index]['energy_quadratic'])
        raw_fixed = [sum(beta(68,7,7,a,i)*beta(956,7,7,b,j)*entries[7,7,i,j][z]
                         for i,j in it.product(range(8),repeat=2) if entries[7,7,i,j] is not None) for z in range(4)]
        if index == 0:
            raw_fixed[0] -= p[7]**2*sizes[7]**2
        fixed_part = [x/(p[7]*d7) for x in raw_fixed]
        check('full_raw_anchor_'+str(index), enc(fixed_part) == saved['fixed_minus_anchor'])
        for i,j in it.product(range(4),repeat=2):
            M[i][j] -= dual[index]*cost[i][j]
        M[0][0] += dual[index]*fixed_part[0]
        for i in range(1,4):
            M[0][i] += dual[index]*fixed_part[i]/2
            M[i][0] += dual[index]*fixed_part[i]/2
        sr,ur = [],[]
        for r,q in free:
            valency = c(7,r)*c(61,r)*c(7,q)*c(949,q)
            e = eigen(68,a,r)*eigen(956,b,q)
            raw = F(beta(68,7,7,a,7-r)*beta(956,7,7,b,7-q),p[7]*d7)
            check('source_Johnson_'+str((index,r,q)), valency > 0 and raw == e/p[7])
            sr.append(-F(e,valency)); ur.append(raw)
        check('original_36_columns_'+str(index), enc(sr) == fixed['matrix'][index])
        scaled_rows.append(sr); raw_rows.append(ur)
        modes.append({'mode':[a,b],'layers':layers,'B':B,'cross':cross,'norms':norm,'pivots':pivots,'ranges':ranges,'cost':cost,'fixed':fixed_part})
    check('all_rank_cases', ranks == {'(2, 1)':8,'(2, 0)':19,'(2, 2)':9,'(1, 1)':10,'(1, 0)':3,'(0, 0)':15})
    cancellations = [[dot(dual,[row[j] for row in matrix]) for j in range(36)] for matrix in [scaled_rows,raw_rows]]
    check('all_scaled_raw_cancellations', not any(cancellations[0]+cancellations[1]))
    check('complete_objective_matrix', enc(M) == data['objective_matrix'])
    T = [[F(1),0,0],[0,F(1),0],[0,0,F(1)],[w,0,0]]
    N = [[sum(T[a][i]*M[a][b]*T[b][j] for a,b in it.product(range(4),repeat=2)) for j in range(3)] for i in range(3)]
    check('complete_plane_matrix', enc(N) == data['plane_matrix'] == ver['plane_matrix'])
    alpha,bv = -N[2][2],N[0][2]
    check('rank_one_square', alpha > 0 and bv > 0 and all(N[1][j] == N[j][1] == 0 for j in range(3)))
    v = bv/alpha
    maximum = N[0][0]+bv*bv/alpha
    lo,hi = 174659686133710,174659686133711
    check('attained_maximum_bounds', lo*maximum.denominator <= maximum.numerator < hi*maximum.denominator
          and maximum > 0 and enc(maximum) == data['stationary']['value'] == ver['maximum'])
    point = [F(1),F(0),v,w]
    check('exact_parameters', enc(point[1:]) == data['stationary']['parameters'] == ver['parameters'])
    free_values = [dot(f,point) for f in fs]
    for i,x in enumerate(free_values):
        check('attaining_free_sign_'+str(i), x == 0 if i == 27 else x > 0)
    slacks = [dot(row,point[:3]) for row in scalar_rows]
    check('all_attaining_scalar_slacks', min(slacks) >= 0 and enc(slacks) == data['stationary']['scalar_slacks'] == ver['new_scalar_slacks'])
    full_column = [dot(row,point) for row in columns]
    check('full_column', enc(full_column) == ver['complete_column'] and min(full_column) >= 0)
    res = [dot([F(*x)*wt for x,wt in zip(row,orbit_weights)],full_column) for row in col['kernel_basis']]
    check('all_attaining_weighted_kernel_residuals', res == [F(0)]*49 and enc(res) == ver['kernel_residuals'])
    check('all_forced_signs', all(dot(val,point) >= 0 for typ,val in entries.items() if typ[:2] == (7,7) and val is not None))
    mode_rhs = [dot(m['fixed'],point)-dot(point,[dot(r,point) for r in m['cost']]) for m in modes]
    check('all_original_witness_modes', enc(mode_rhs) == [r['rhs'] for r in ver['witness_modes']] and dot(dual,mode_rhs) == maximum)
    check('fixed_point_obstruction_preserved', N[0][0] == F(*fixed['certificate']['rhs_pairing']) < 0)
    summary = {'checks':len(checks),'failures':len(failures),'types':len(types),'presentations':6*len(types),
               'column_scalar_rows':len(slacks),'old_scalar_rows':len(old_slacks),'mode_ranks':ranks,
               'initial_lookup_failures_explained':len(missing),'free_positive':sum(x > 0 for x in free_values),
               'free_zero':[i for i,x in enumerate(free_values) if not x], 'maximum_interval':[lo,hi],
               'required_strict_exclusion':'pairing < 0 throughout domain','verdict':'RETAIN L072' if not failures else 'AUDIT_FAILED'}
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checks':checks,'failures':failures,'summary':summary,'records':records,'missing_lookups':missing,
              'initial_failure_names':expected_initial_failures,'unchanged_initial_constructor_fields':stable_initial,
              'unchanged_initial_verifier_fields':stable_iv,'affine_column':columns,'kernel_affine_residuals':kernel_residuals,
              'scalar_affine_rows':scalar_rows,'old_scalar_slacks':old_slacks,'modes':modes,'dual':dual,'cancellations':cancellations,
              'objective_matrix':M,'plane_matrix':N,'alpha':alpha,'beta':bv,'parameters':point[1:],'maximum':maximum,
              'bound_slacks':[maximum-lo,hi-maximum],'free_values':free_values,'new_scalar_slacks':slacks,
              'full_column':full_column,'kernel_residuals':res,'mode_rhs_at_maximum':mode_rhs}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))
    print('Failures:',failures)
    print('Certificate:',OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

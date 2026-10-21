"""L068 critical audit: complete domain and weighted affine inverse action.

Standard library only. Import the audited L067 direct action data as an
established input; check its full actions and transport all affine coefficients.
No optimization, new dual, completion search or scalar upper-row test.
"""
import hashlib
import itertools as it
import json
import re
import sys
from fractions import Fraction as F
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'seven-shell-affine-fixed-dual-critical-audit.json'


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


def av(x):
    return [F(x), F(0), F(0), F(0)]


def add(x, y, scale=F(1)):
    return [a+scale*b for a, b in zip(x, y)]


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def orders(typ):
    l, m, i, j = typ
    atoms = [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]
    out = []
    for bits in it.permutations([4, 2, 1]):
        aa = [0]*8
        for mask, count in enumerate(atoms):
            aa[sum(new for new, old in zip([4, 2, 1], bits) if mask & old)] = count
        out.append(aa)
    return out


def main():
    names = ['seven-shell-affine-fixed-dual-results.json',
             'seven-shell-affine-fixed-dual-verification.json',
             'seven-shell-affine-fixed-dual-initial.json',
             'simultaneous-shell-ordinary-scalars-results.json',
             'seven-distance-full-base-kernel-results.json',
             'simultaneous-seven-shell-results.json',
             'simultaneous-seven-shell-critical-audit.json']
    paths = [ROOT/name for name in names]
    data, verified, initial, old, col, fixed, prior = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for path, obj in zip(paths, [data, verified, initial, old, col, fixed, prior]):
        if obj is not initial:
            check('input_pass_'+path.name, obj['failures'] == [])
        for rel, digest in obj.get('input_hashes', obj.get('source_hashes', {})).items():
            check('input_hash_'+path.name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    check('preserved_initial_failure', initial['failures'] == ['hessian_positive_semidefinite'])
    for key in ['domain', 'affine_column', 'records', 'free_new', 'modes', 'dual',
                'cancellations', 'total_cost_quadratic', 'total_fixed_affine',
                'objective_matrix', 'original_point', 'original_value', 'singular_hessian']:
        check('initial_unchanged_'+key, initial[key] == data[key])
    for key in ['H', 'g', 'stationary', 'value', 'free_values']:
        check('initial_optimization_unchanged_'+key, initial['optimization'][key] == data['optimization'][key])
    p = [F(*x) for x in old['pairs_through_12']]
    U = F(c(1024,64), c(68,64))
    check('positive_original_rho', F(*old['rho']) == (U+1)/(2*c(1024,68)) > 0)
    check('original_pairs', p[5:8] == [F(1,68881143660), F(133,9357995374380), F(3539,248922676958508)])
    fs = [[F(*v)]+[F(*s) for s in row] for v, row in zip(col['affine']['intercept'], col['affine']['slopes'])]
    check('full_parameter_domain', len(fs) == 49 and all(len(v) == 4 for v in fs)
          and enc(fs) == data['domain']['nonnegative_free'] and col['affine']['free_indices'] == [27,33,42])
    for j, index in enumerate([27,33,42]):
        check('parameter_identity_'+str(index), fs[index] == [F(0)]+[F(k == j) for k in range(3)])
    check('complete_column_orbits', [r['orbit'] for r in col['column']] == [[0,0,0]]+
          [[l,i,j] for l in [5,6] for i,j in it.product(range(l+1),repeat=2)])
    entries = {tuple(r['type']): av(F(*r['y'])) for r in old['types']}
    check('complete_old_types', len(old['types']) == len(entries) == 121 and set(entries) ==
          {(l,m,i,j) for l,m in [(5,5),(5,6),(6,6)] for i,j in it.product(range(l+1),repeat=2)})
    columns = []
    for index, row in enumerate(col['column']):
        value = [p[7]*x for x in fs[row['variable']]] if row['kind'] == 'free' else av(F(*row['value']))
        columns.append(value)
        check('affine_column_'+str(index), enc(value) == data['affine_column'][index])
        if row['kind'] != 'free':
            check('fixed_sign_'+str(index), value[0] >= 0 and not any(value[1:]))
        if index:
            l,i,j = row['orbit']
            entries[l,7,i,j] = value
        else:
            check('full_anchor', value == av(p[7]))
    kernel_residuals = []
    check('complete_kernel_dimensions', len(col['kernel_basis']) == 49 and len(col['weights']) == 86)
    for index, null in enumerate(col['kernel_basis']):
        check('kernel_vector_length_'+str(index), len(null) == 86)
        res = [sum(F(*n)*int(w)*v[k] for n,w,v in zip(null,col['weights'],columns)) for k in range(4)]
        kernel_residuals.append(res)
        check('whole_original_kernel_affine_'+str(index), not any(res))
    for index, (row, rhs) in enumerate(zip(col['equations'],col['rhs'])):
        check('original_affine_equation_'+str(index), len(row) == 49 and
              [sum(F(*a)*v[k] for a,v in zip(row,fs)) for k in range(4)] == av(F(*rhs)))
    # Complete unordered key dictionary BEFORE adding any seven/seven rows.
    dictionary = {}
    for typ, value in entries.items():
        key = min(map(tuple,orders(typ)))
        check('immutable_key_agreement_'+str(typ), key not in dictionary or dictionary[key] == value)
        dictionary[key] = value
    for r,q in it.product(range(8),repeat=2):
        h = r+q
        entries[7,7,7-r,7-q] = (av(p[7]) if h == 0 else av(0) if h <= 4 else
                                entries[h,7,q,r] if h <= 6 else None)
    expected = [(l,m,i,j) for l,m in [(5,5),(5,6),(6,6),(5,7),(6,7),(7,7)]
                for i,j in it.product(range(l+1),repeat=2)]
    check('exhaustive_record_order', [r['type'] for r in data['records']] == list(map(list,expected)))
    groups, free_keys, presentations = {}, [], []
    for typ, saved in zip(expected, data['records']):
        aa = orders(typ)
        key = min(map(tuple,aa))
        val = entries[typ]
        check('complete_key_'+str(typ), saved['key'] == list(key) and enc(val) == saved['affine'])
        check('complete_six_presentations_'+str(typ), len(saved['presentations']) == 6
              and [r['atoms'] for r in saved['presentations']] == aa)
        if val is None:
            free_keys.append(key)
            check('new_free_key_'+str(typ), key not in dictionary)
        elif key in dictionary:
            check('old_dictionary_lookup_'+str(typ), dictionary[key] == val)
        if key in groups:
            check('whole_unordered_identity_'+str(typ), groups[key] == val)
        groups[key] = val
        for index, (atoms, row) in enumerate(zip(aa, saved['presentations'])):
            a,b,h = atoms[4]+atoms[5], atoms[4]+atoms[6], atoms[2]+atoms[6]
            check('valid_atoms_'+str((typ,index)), min(atoms) >= 0 and sum(atoms) == 1024
                  and all(sum(v for mask,v in enumerate(atoms) if mask & bit) == 68 for bit in [1,2,4]))
            check('complete_distances_'+str((typ,index)), row['distances'] == [a,b,h])
            lookup = (*sorted([a,b]),atoms[4],atoms[3])
            v = av(p[max(a,b,h)]) if min(a,b,h) == 0 else av(0) if min(a,b,h) < 5 else entries.get(lookup)
            check('all_reanchorings_'+str((typ,index)), v is None or v == val)
            check('saved_prescription_'+str((typ,index)), row['affine'] is None or row['affine'] == enc(val))
        presentations.append({'type':typ,'orders':aa,'key':key,'affine':val})
    check('36_independent_newnew_keys', len(free_keys) == len(set(free_keys)) == 36
          and data['free_new'] == [[r,q] for r,q in it.product(range(8),repeat=2) if r+q >= 7])
    check('no_extra_equalities', data['domain']['equality_rows'] == []
          and all(not any(F(*v) for v in row) for row in data['domain']['all_equality_residuals']))
    # Established direct-action data, not a new source-theorem computation.
    factors = {(r['n'],r['layer']):r for r in prior['factors']}
    norms = {k:[F(*v) for v in row['norms']] for k,row in factors.items()}
    gamma = {}
    for row in prior['transitions']:
        n,l,m,t = (row[k] for k in ['n','l','m','t'])
        for a, saved_action in enumerate(row['actions']):
            g = F(*saved_action)
            h = [F(*v) for v in factors[n,m]['basis'][a]]
            image = [dot(q,h) for q in row['matrix']]
            target = [g*F(*v) for v in factors[n,l]['basis'][a]] if a <= l else [F(0)]*(l+1)
            check('complete_imported_action_'+str((n,l,m,t,a)), image == target)
            if a <= min(l,m):
                gamma[n,l,m,a,t] = g
    scales = {key:F(*v) for key,v in prior['signed_scales'].items()}
    manuscript = (NB/'lemmas/L067-simultaneous-seven-shell-fixed-column-obstruction.md').read_text()
    h = [F(v.strip()) for v in re.search(r'  h=\((.*?)\),', manuscript,re.S).group(1).split(',')]
    k = [F(v.strip()) for v in re.search(r'  k=\((.*?)\)\.', manuscript,re.S).group(1).split(',')]
    dual = [a*b for a in h for b in k]
    check('unchanged_dual', enc(dual) == data['dual'] == fixed['exact']['dual'] == prior['dual']
          and len(dual) == 64 and min(dual) >= 0 and sum(v>0 for v in dual) == 24)
    sizes = {l:c(68,l)*c(956,l) for l in [5,6,7]}
    modes, ranks, total_fixed = [], {}, av(0)
    total_cost = [[F(0)]*4 for _ in range(4)]
    for a,b in it.product(range(8),repeat=2):
        index = 8*a+b
        saved = data['modes'][index]
        layers = [l for l in [6,5] if max(a,b) <= l]
        norm = {l:norms[68,l][a]*norms[956,l][b] for l in layers+[7]}
        d7 = c(68-2*a,7-a)*c(956-2*b,7-b)
        check('positive_normalization_'+str(index), d7 == saved['D7'] and d7 > 0 and min(norm.values()) > 0)

        def action(l,m):
            ans = av(0)
            for i,j in it.product(range(min(l,m)+1),repeat=2):
                ans = add(ans,entries[min(l,m),max(l,m),i,j],gamma[68,l,m,a,i]*gamma[956,l,m,b,j])
            if a == b == 0:
                ans[0] -= p[l]*p[m]*sizes[m]
            return ans

        B = [[norm[l]*action(l,m)[0] for m in layers] for l in layers]
        cross = [[norm[l]*v for v in action(l,7)] for l in layers]
        s = {l:scales[str((68,l,7,a))]*scales[str((956,l,7,b))]/(norm[7]/d7) for l in layers}
        for i,l in enumerate(layers):
            si = saved['layers'].index(l)
            check('positive_scale_'+str((index,l)), s[l] > 0)
            check('affine_both_directions_'+str((index,l)), cross[i] == [norm[7]*v for v in action(7,l)])
            check('affine_congruence_'+str((index,l)), cross[i] ==
                  [norm[7]/d7*s[l]*F(*v) for v in saved['cross'][si]])
            for j,m in enumerate(layers):
                sj = saved['layers'].index(m)
                check('base_congruence_'+str((index,l,m)), B[i][j] == B[j][i]
                      == norm[7]/d7*s[l]*s[m]*F(*saved['B'][si][sj]))
        work, rhs = [r[:] for r in B], [r[:] for r in cross]
        cost, pivots, ranges = [[F(0)]*4 for _ in range(4)], [], []
        for i in range(len(layers)):
            pivot = work[i][i]
            pivots.append(pivot)
            check('reverse_pivot_'+str((index,i)), pivot >= 0)
            if not pivot:
                ranges.append(rhs[i][:])
                check('whole_affine_zero_range_'+str((index,i)), not any(rhs[i])
                      and all(work[i][j] == 0 for j in range(i+1,len(layers))))
                continue
            for j,z in it.product(range(4),repeat=2):
                cost[j][z] += rhs[i][j]*rhs[i][z]/pivot
            for j in range(i+1,len(layers)):
                rhs[j] = add(rhs[j],rhs[i],-work[j][i]/pivot)
                for z in range(i+1,len(layers)):
                    work[j][z] -= work[j][i]*work[i][z]/pivot
        rank = sum(v>0 for v in pivots)
        category = str((len(layers),rank))
        ranks[category] = ranks.get(category,0)+1
        cost = [[v/(p[7]*norm[7]) for v in row] for row in cost]
        check('complete_energy_quadratic_'+str(index), enc(cost) == saved['required_quadratic'])
        fixed_aff = av(0)
        for r,q in it.product(range(8),repeat=2):
            if r+q <= 6:
                fixed_aff = add(fixed_aff,entries[7,7,7-r,7-q],
                                gamma[68,7,7,a,7-r]*gamma[956,7,7,b,7-q]/p[7])
        if a == b == 0:
            fixed_aff[0] -= p[7]*sizes[7]
        check('fixed_and_anchor_'+str(index), enc(fixed_aff) == saved['fixed_minus_anchor_affine'])
        total_fixed = add(total_fixed,fixed_aff,dual[index])
        for i,j in it.product(range(4),repeat=2):
            total_cost[i][j] += dual[index]*cost[i][j]
        modes.append({'mode':[a,b],'layers':layers,'base':B,'cross':cross,'norms':norm,
                      'scales':s,'pivots':pivots,'range_residuals':ranges,'rank':rank,
                      'energy_quadratic':cost,'fixed_minus_anchor':fixed_aff})
    check('all_rank_cases', ranks == {'(2, 1)':8,'(2, 0)':19,'(2, 2)':9,'(1, 1)':10,'(1, 0)':3,'(0, 0)':15})
    cancellations = []
    for r,q in it.product(range(8),repeat=2):
        if r+q < 7:
            continue
        valency = c(7,r)*c(61,r)*c(7,q)*c(949,q)
        residual = sum(-dual[8*a+b]*gamma[68,7,7,a,7-r]*gamma[956,7,7,b,7-q]/valency
                       for a,b in it.product(range(8),repeat=2))
        cancellations.append(residual)
        check('original_normalized_cancellation_'+str((r,q)), valency > 0 and residual == 0)
    check('whole_weighted_affine', enc(total_fixed) == data['total_fixed_affine'])
    check('whole_weighted_energy', enc(total_cost) == data['total_cost_quadratic'])
    M = [[-v for v in row] for row in total_cost]
    M[0][0] += total_fixed[0]
    for i in range(1,4):
        M[0][i] += total_fixed[i]/2
        M[i][0] += total_fixed[i]/2
    check('complete_objective', enc(M) == data['objective_matrix'] == verified['objective_matrix'])
    alpha, beta = -M[3][3], M[0][3]
    check('exact_global_square', alpha > 0 and alpha*M[0][0]+beta*beta == 0
          and all(M[i][j] == 0 for i,j in it.product(range(4),repeat=2) if i in [1,2] or j in [1,2]))
    star = [F(1),F(0),F(0),beta/alpha]
    check('stationary_parameters', enc(star[1:]) == data['optimization']['stationary'] == verified['witness_parameters'])
    full_column = [dot(v,star) for v in columns]
    free_values = [dot(v,star) for v in fs]
    for i,v in enumerate(free_values):
        check('exact_free_sign_'+str(i), v == 0 if i in [27,33] else v > 0)
    check('complete_saved_free_witness', enc(free_values) == data['optimization']['free_values'] == verified['all_free_values'])
    check('complete_original_column', enc(full_column) == verified['complete_column'] and min(full_column) >= 0)
    original_residuals = []
    for i,v in enumerate(col['kernel_basis']):
        res = sum(F(*n)*int(w)*b for n,w,b in zip(v,col['weights'],full_column))
        original_residuals.append(res)
        check('witness_original_kernel_'+str(i), res == 0)
    rhs_at_star = []
    for index, mode in enumerate(modes):
        cost = dot(star,[dot(row,star) for row in mode['energy_quadratic']])
        rhs = dot(mode['fixed_minus_anchor'],star)-cost
        rhs_at_star.append(rhs)
        check('original_rhs_witness_'+str(index), enc(rhs) == verified['all_64_rhs_at_witness'][index])
    check('attained_exact_zero', dot(dual,rhs_at_star) == dot(star,[dot(row,star) for row in M]) == 0)
    w0 = -fs[4][0]/fs[4][3]
    oldpoint = [F(1),F(0),F(0),w0]
    oldvalue = dot(oldpoint,[dot(row,oldpoint) for row in M])
    check('immutable_negative_retained', enc(oldvalue) == fixed['exact']['fixed_value']
          and F(-53503520,10**6) <= oldvalue < F(-53503519,10**6))
    # Reconcile the initial failure by checking the entire corrected curvature decomposition.
    H = [[-M[i][j] for j in range(1,4)] for i in range(1,4)]
    factors_new = data['optimization']['square_factors']
    decomposition = [[F(0)]*3 for _ in range(3)]
    for item in factors_new:
        pivot = F(*item['pivot'])
        v = [F(*x) for x in item['vector']]
        check('positive_curvature_pivot', pivot > 0)
        for i,j in it.product(range(3),repeat=2):
            decomposition[i][j] += v[i]*v[j]/pivot
    check('full_corrected_curvature', decomposition == H and H[0][0] == H[1][1] == 0 and H[2][2] > 0)
    summary = {'checks':len(checks),'failures':len(failures),'types':len(expected),'presentations':6*len(expected),
               'modes':len(modes),'mode_base_ranks':ranks,'affine_inequalities':len(fs),
               'positive_free':sum(v>0 for v in free_values),'zero_free':[i for i,v in enumerate(free_values) if not v],
               'attained_maximum':'0','required_uniform_strict_sign':'<0',
               'verdict':'RETAIN L068' if not failures else 'FAILED'}
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checks':checks,'failures':failures,'presentations':presentations,'domain':fs,
              'full_affine_column':columns,'whole_kernel_affine_residuals':kernel_residuals,
              'modes':modes,'dual':dual,'normalized_dual_cancellations':cancellations,
              'total_fixed':total_fixed,'total_cost':total_cost,'objective_matrix':M,'alpha':alpha,'beta':beta,
              'w_star':star[3],'witness_parameters':star[1:],'free_values':free_values,'complete_column':full_column,
              'original_kernel_residuals':original_residuals,'all_64_rhs_at_witness':rhs_at_star,
              'attained_value':dot(dual,rhs_at_star),'old_value':oldvalue,'corrected_curvature':decomposition,'summary':summary}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print(summary)
    print('Failures:',failures)
    print('Certificate:',OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

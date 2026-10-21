"""L069 critical audit: actual sets, complete scalar rows, original kernel.

Standard library only. L062's values, L065's complete kernel/RREF and
L068's objective matrix are established inputs, not re-proved here.
Every relevant coordinate is consumed; no numerical solver is used.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from math import comb, factorial, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'zero-dual-plane-scalars-critical-audit.json'


def enc(x):
    if isinstance(x, Q):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {k: enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def main():
    names = ['zero-dual-plane-scalars-results.json',
             'zero-dual-plane-scalars-verification.json',
             'delsarte-lp-results.json',
             'simultaneous-shell-ordinary-scalars-results.json',
             'seven-distance-full-base-kernel-results.json',
             'seven-shell-affine-fixed-dual-results.json']
    paths = [ROOT / n for n in names]
    data, verified, lp, old, kernel, square = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, truth):
        checks.append(name)
        if not truth:
            failures.append(name)

    for n, obj in enumerate([data, verified, lp, old, kernel, square]):
        check(f'input_failures_{n}', obj['failures'] == [])
        for path, digest in obj.get('input_hashes', obj.get('source_hashes', {})).items():
            check(f'input_hash_{n}_{path}', hashlib.sha256((NB / path).read_bytes()).hexdigest() == digest)

    # All original pair coordinates: integer polynomial expansion of L021.
    primal = [Q(x['numerator'], x['denominator']) for x in lp['exact']['primal']]
    check('pair_domain', len(primal) == 64 and lp['active_distances'] == list(range(5, 69)))
    pair_residuals = []
    for j in range(1, 65):
        poly = [comb(68-j, k)*comb(956-j, k) for k in range(69-j)]
        for _ in range(j):
            poly = [poly[0]]+[poly[k]-poly[k-1] for k in range(1, len(poly))]+[-poly[-1]]
        residual = 1+sum(Q(poly[h], comb(68, h)*comb(956, h))*primal[h-5] for h in range(5, 69))
        pair_residuals.append(residual)
        check(f'original_pair_equation_{j}', residual == 0)
    p = [Q(1)]+[Q(0)]*4+[primal[h-5]/(2*comb(68, h)*comb(956, h)) for h in range(5, 69)]
    N = comb(1024, 68)
    M = (Q(comb(1024, 64), comb(68, 64))+1)/2
    rho = M/N
    check('full_pair_positivity', all(x > 0 for x in primal))
    check('original_pair_thirteen', primal[8] == Q(808753696404081487284494974858496, 11)
          and p[13] == Q(26968792942808537, 1896913598738625271419892200))
    check('pair_dictionaries', data['pairs_through_13'] == enc(p[:14]) and old['pairs_through_12'] == enc(p[:13]))
    check('positive_original_rho_p7', rho > 0 and p[7] > 0 and data['rho'] == old['rho'] == kernel['rho'] == enc(rho)
          and kernel['p7'] == enc(p[7]) and data['normalization'] == enc({'N': N, 'M': M}))
    check('lower_bound', all(0 <= x <= p[5] for x in p[1:14])
          and 1-2*p[5] == Q(34440571829, 34440571830))

    # Regenerate affine coordinates from the canonical nonpivot prescription.
    pivots = kernel['equation_pivots']
    nonpivots = [j for j in range(49) if j not in pivots]
    R = [[Q(*x) for x in row] for row in kernel['equation_rref']]
    check('rref_shapes', len(R) == 49 and all(len(row) == 50 for row in R)
          and len(pivots) == 46 and nonpivots == [27, 33, 42])
    fs = [[Q(0)]*4 for _ in range(49)]
    for k, j in enumerate(nonpivots):
        fs[j][k+1] = Q(1)
    for row, j in enumerate(pivots):
        fs[j] = [R[row][-1]]+[-R[row][k] for k in nonpivots]
        check(f'rref_pivot_identity_{row}', all(R[row][k] == (k == j) for k in pivots))
    check('rref_zero_rows', all(x == 0 for row in R[46:] for x in row))
    check('full_affine_import', enc([f[0] for f in fs]) == kernel['affine']['intercept']
          and enc([f[1:] for f in fs]) == kernel['affine']['slopes']
          and kernel['affine']['free_indices'] == nonpivots)
    A = [[Q(*x) for x in row] for row in square['objective_matrix']]
    check('symmetric_square_shape', len(A) == 4 and all(len(row) == 4 for row in A)
          and all(A[i][j] == A[j][i] for i in range(4) for j in range(4)))
    alpha, beta = -A[3][3], A[0][3]
    w = beta/alpha
    check('complete_square_identity', alpha > 0 and alpha*A[0][0]+beta*beta == 0
          and all(A[i][j] == 0 for i in range(4) for j in range(4) if i in [1, 2] or j in [1, 2]))
    check('identical_stationary_point', data['w_star'] == enc(w)
          and data['point_test']['parameters'] == square['optimization']['stationary'] == enc([Q(0), Q(0), w]))
    plane = [[f[0]+w*f[3], f[1], f[2]] for f in fs]
    free = [f[0] for f in plane]
    check('identical_plane', data['plane_free'] == enc(plane))
    check('identical_free_witness', data['point_test']['free_values'] == square['optimization']['free_values'] == enc(free))
    check('all_free_signs', sum(x > 0 for x in free) == 47 and [j for j, x in enumerate(free) if x == 0] == [27, 33])

    orders = list(it.permutations(range(3)))
    universe = set(range(1024))
    D = set(range(68))

    def presentations(l, m, i, j):
        U, V = set(range(m)), set(range(68, 68+m))
        X = set(range(i)) | set(range(m, m+l-i))
        Y = set(range(68, 68+j)) | set(range(68+m, 68+m+l-j))
        supports = [D, (D-X) | Y, (D-U) | V]
        result = []
        for order in orders:
            B, C, E = [supports[k] for k in order]
            regions = [universe-B-C-E, E-B-C, C-B-E, (C&E)-B,
                       B-C-E, (B&E)-C, (B&C)-E, B&C&E]
            atoms = list(map(len, regions))
            a, b, h = len(B-C), len(B-E), len(C-E)
            t, s = len(B-(C|E)), len((C&E)-B)
            numerator, denominator = factorial(68)*factorial(956), prod(factorial(z) for z in atoms)
            O, remainder = divmod(numerator, denominator)
            check(f'actual_regions_{l}_{m}_{i}_{j}_{order}', set.union(*regions) == universe
                  and sum(atoms) == 1024 and all(len(S) == 68 for S in supports)
                  and remainder == 0 and O > 0 and h == a+b-t-s and t-s == i-j
                  and atoms == [956-a-b+s,b-s,a-s,s,t,a-t,b-t,68-a-b+t])
            result.append({'order': list(order), 'atoms': atoms, 'source_indices': [a,b,t,s],
                           'third_distance': h, 't_minus_s': t-s, 'orbit_size': O})
        return result

    old_domain = [(l,m,i,j) for l,m in [(5,5),(5,6),(6,6)] for i,j in it.product(range(l+1), repeat=2)]
    new_domain = [(l,7,i,j) for l in [5,6] for i,j in it.product(range(l+1), repeat=2)]
    check('old_exhaustion', [r['type'] for r in old['types']] == list(map(list, old_domain)))
    check('new_exhaustion', [r['type'] for r in data['records']] == list(map(list, new_domain))
          and len(kernel['column']) == 86 and len(data['inequalities']) == 1530)
    dictionary, source_keys = {}, {}
    old_records, new_records, old_slacks, new_slacks = [], [], [], []
    affine_column = [[p[7], Q(0), Q(0), Q(0)]]
    weights = [1]
    free_keys, variable_columns, extrema = [], [], []
    partition = {'represented': 0, 'forbidden': 0, 'free': 0}
    old_boolean, old_forbidden = 0, 0
    for is_new, domain, source in [(False, old_domain, old['types']), (True, new_domain, data['records'])]:
        for index, typ in enumerate(domain):
            l,m,i,j = typ
            saved = source[index]
            pres = presentations(*typ)
            key = min(tuple(x['atoms']) for x in pres)
            distances = [l,m,l+m-i-j]
            if not is_new:
                val = [Q(*saved['y']), Q(0), Q(0), Q(0)]
                kind = 'old'
            else:
                if key in dictionary:
                    kind, val = 'represented', dictionary[key]
                elif any(1 <= h <= 4 for h in distances):
                    kind, val = 'forbidden', [Q(0)]*4
                else:
                    kind = 'free'
                    var = len(free_keys)
                    check(f'free_unique_{var}', key not in free_keys)
                    free_keys.append(key)
                    variable_columns.append(index+1)
                    val = [p[7]*x for x in fs[var]]
                    check(f'free_coordinate_{var}', kernel['column'][index+1]['variable'] == var)
                partition[kind] += 1
                wt = comb(7,i)*comb(61,l-i)*comb(7,j)*comb(949,l-j)
                weights.append(wt)
                affine_column.append(val)
                inp = kernel['column'][index+1]
                check(f'original_column_{index}', inp['orbit'] == [l,i,j] and inp['kind'] == kind
                      and inp['key'] == list(key) and inp['atoms'] == pres[0]['atoms']
                      and inp['presentations'] == [r['atoms'] for r in pres] and inp['weight'] == wt
                      and inp['half_distances'] == distances)
                if kind != 'free':
                    check(f'original_fixed_value_{index}', val == [Q(*inp['value']),Q(0),Q(0),Q(0)])
            check(f'common_unordered_value_{is_new}_{index}', key not in dictionary or dictionary[key] == val)
            dictionary[key] = val
            vp = [val[0]+w*val[3], val[1], val[2]]
            check(f'nonnegative_coordinate_{is_new}_{index}', vp[0] >= 0)
            if any(1 <= h <= 4 for h in distances):
                check(f'forbidden_identity_{is_new}_{index}', val == [Q(0)]*4)
            record = {'type': list(typ), 'key': list(key), 'affine': val, 'plane_y': vp, 'presentations': []}
            for order_index, original in enumerate(pres):
                a,b,t,s = original['source_indices']
                h = original['third_distance']
                identity = (tuple(sorted([a,b,h])),t-s)
                check(f'source_key_{is_new}_{index}_{order_index}', identity not in source_keys or source_keys[identity] == (key, val))
                source_keys[identity] = (key, val)
                slacks = [vp, [p[a]-vp[0],-vp[1],-vp[2]], [1+vp[0]-p[a]-p[b],vp[1],vp[2]]]
                check(f'scalar_signs_{is_new}_{index}_{order_index}', all(x[0] >= 0 for x in slacks))
                check(f'normalization_{is_new}_{index}_{order_index}', all(N*original['orbit_size']*rho*x/(M*original['orbit_size']) == x for x in vp))
                if 0 in [a,b,h]:
                    check(f'Boolean_{index}_{order_index}', not is_new and vp == [p[max(a,b,h)],Q(0),Q(0)])
                    old_boolean += 1
                else:
                    check(f'lower_slack_{is_new}_{index}_{order_index}', slacks[2][0] >= 1-2*p[5] > 0)
                    if not is_new and any(1 <= x <= 4 for x in [a,b,h]):
                        old_forbidden += 1
                    if is_new and all(x >= 5 for x in [a,b,h]):
                        extrema.append((vp[0]/min(p[x] for x in [a,b,h]),list(typ),order_index))
                if is_new:
                    actual = dict(original, plane_slacks=slacks)
                    check(f'new_full_presentation_{index}_{order_index}', saved['presentations'][order_index] == enc(actual))
                    for label, slack in zip(['nonnegative','upper','lower'],slacks):
                        row = {'type':list(typ),'order':original['order'],'row':label,'affine':slack}
                        check(f'new_affine_inequality_{len(new_slacks)}', data['inequalities'][len(new_slacks)] == enc(row))
                        new_slacks.append(slack[0])
                else:
                    actual = dict(original, pairs=[p[a],p[b],p[h]], slacks=[x[0] for x in slacks])
                    check(f'old_full_presentation_{index}_{order_index}', saved['presentations'][order_index] == enc(actual))
                    old_slacks.extend(x[0] for x in slacks)
                record['presentations'].append(actual)
            if is_new:
                check(f'new_record_{index}', saved['key'] == list(key) and saved['kind'] == kind and saved['plane_y'] == enc(vp))
                new_records.append(record)
            else:
                old_records.append(record)

    check('partition_and_all_free_keys', partition == data['partition'] == {'represented':20,'forbidden':16,'free':49}
          and len(free_keys) == 49 and kernel['free_keys'] == list(map(list,free_keys)))
    check('full_original_weights', kernel['weights'] == weights and len(weights) == 86 and all(wt > 0 for wt in weights)
          and sum(weights[1:37]) == comb(68,5)*comb(956,5) and sum(weights[37:]) == comb(68,6)*comb(956,6))
    check('same_L068_affine_column', square['affine_column'] == enc(affine_column))
    complete = [v[0]+w*v[3] for v in affine_column]
    check('same_complete_column', verified['complete_column'] == enc(complete))
    check('complete_slack_lists', len(new_slacks) == 1530 and len(old_slacks) == 2178
          and enc(new_slacks) == data['point_test']['all_slacks'] == verified['all_new_slacks']
          and enc(old_slacks) == verified['all_old_slacks'] and old_boolean == 12 and old_forbidden == 228)

    # Rebuild every weighted compatibility row, retaining the anchor.
    basis = [[Q(*x) for x in row] for row in kernel['kernel_basis']]
    check('complete_kernel_shapes', len(basis) == 49 and all(len(row) == 86 for row in basis)
          and len(kernel['equations']) == len(kernel['rhs']) == 49)
    equations, rhs_values, affine_residuals, point_residuals = [], [], [], []
    fixed = [i for i in range(86) if i not in variable_columns]
    for row_index, null in enumerate(basis):
        coeff = [weights[i]*null[i]*p[7] for i in variable_columns]
        rhs = -sum(weights[i]*null[i]*affine_column[i][0] for i in fixed)
        scale = max(map(abs,coeff)) or Q(1)
        eq, r = [x/scale for x in coeff], rhs/scale
        check(f'original_weighted_equation_{row_index}', kernel['equations'][row_index] == enc(eq) and kernel['rhs'][row_index] == enc(r))
        residues = [sum(weights[i]*null[i]*affine_column[i][k] for i in range(86)) for k in range(4)]
        check(f'full_affine_kernel_{row_index}', residues == [Q(0)]*4)
        check(f'original_affine_equation_{row_index}', [sum(eq[j]*fs[j][k] for j in range(49)) for k in range(4)] == [r,Q(0),Q(0),Q(0)])
        residual = sum(weights[i]*null[i]*complete[i] for i in range(86))
        check(f'full_point_kernel_{row_index}', residual == 0)
        equations.append(eq)
        rhs_values.append(r)
        affine_residuals.append(residues)
        point_residuals.append(residual)
    check('same_kernel_residuals', verified['original_kernel_residuals'] == enc(point_residuals))
    maximum = max(x[0] for x in extrema)
    maximizers = [x[1:] for x in extrema if x[0] == maximum]
    check('exact_extremum', data['maximum_upper_ratio'] == verified['maximum_upper_ratio'] == enc(maximum)
          and 0 <= maximum < Q(1,10**9) < 1 and {tuple(x[0]) for x in maximizers} == {(5,7,1,5),(6,7,2,6)}
          and verified['maximizing_type'] == [6,7,2,6])
    check('zero_minimum', min(new_slacks) == 0 and data['point_test']['violating_rows'] == [])
    summary = {'checks':len(checks),'failures':len(failures),'old_types':121,'new_types':85,
               'direct_set_presentations':1236,'old_scalar_rows':len(old_slacks),'new_scalar_rows':len(new_slacks),
               'weighted_kernel_equations':len(equations),'affine_kernel_coefficients':196,
               'free_positive':47,'free_zero_indices':[27,33], 'minimum_new_slack':min(new_slacks),
               'maximum_ratio_below_1e_minus_9':maximum < Q(1,10**9),
               'verdict':'RETAIN_L069' if not failures else 'AUDIT_FAILED'}
    result = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checks':checks,'failures':failures,'summary':summary,'pair_residuals':pair_residuals,
              'pairs_through_13':p[:14],'rho':rho,'w_star':w,'objective_matrix':A,'free_affine':fs,'plane_free':plane,
              'free_values':free,'old_records':old_records,'new_records':new_records,'weights':weights,
              'complete_affine_column':affine_column,'complete_column':complete,'compatibility_equations':equations,
              'compatibility_rhs':rhs_values,'all_affine_kernel_residuals':affine_residuals,
              'original_kernel_residuals':point_residuals,'all_old_slacks':old_slacks,'all_new_slacks':new_slacks,
              'maximum_upper_ratio':maximum,'maximizing_presentations':maximizers,'partition':partition}
    OUT.write_text(json.dumps(enc(result),indent=2)+'\n')
    print(json.dumps(enc(summary),sort_keys=True))
    print('Actual maximum y/min(pair) < 1/1000000000; required <= 1. Minimum slack = 0.')
    print('Failures:', failures)
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

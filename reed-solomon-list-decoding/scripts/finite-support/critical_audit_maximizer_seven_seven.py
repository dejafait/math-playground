"""L074 critical audit: independent source-domain reconstruction, exact arithmetic.

Imports L073's reviewed PSD theorem only after full assignment identity checks.
No notebook-code imports, optimization, floating point, or altered input files.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from math import comb, factorial, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'maximizer-seven-seven-critical-audit.json'


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b)), F(0))


def main():
    names = ['maximizer-seven-seven-scalars-results.json',
             'maximizer-completion-critical-audit.json', 'maximizer-completion-results.json',
             'maximizer-completion-verification.json', 'delsarte-lp-results.json',
             'seven-distance-full-base-kernel-results.json',
             'simultaneous-shell-ordinary-scalars-results.json',
             'alternative-product-zero-plane-results.json', 'seven-shell-affine-fixed-dual-results.json']
    paths = [ROOT/n for n in names]
    data, audit, completion, verified, lp, col, old, plane, square = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(label, condition):
        checks.append(label)
        if not condition:
            failures.append(label)

    for path, obj in zip(paths, [data, audit, completion, verified, lp, col, old, plane, square]):
        check('clean_'+path.name, obj['failures'] == [])
        for rel, digest in obj.get('input_hashes', obj.get('source_hashes', {})).items():
            check('hash_'+path.name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)

    # Use L021's direct finite-sum definition, rather than the polynomial expansion.
    primal = [F(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    check('original_pair_domain', lp['active_distances'] == list(range(5, 69)) and len(primal) == 64)
    residuals = []
    for j in range(1, 65):
        row = [F(sum((-1)**s*C(j, s)*C(68-j, h-s)*C(956-j, h-s)
                     for s in range(h+1)), C(68, h)*C(956, h)) for h in range(5, 69)]
        residuals.append(1+dot(row, primal))
        check('L021_defining_equation_'+str(j), residuals[-1] == 0)
    U = F(C(1024, 64), C(68, 64))
    N, M = C(1024, 68), (U+1)/2
    rho = M/N
    p = [F(1)]+[F(0)]*4+[a/(2*C(68, h)*C(956, h)) for h, a in zip(range(5, 69), primal)]
    check('pair_objective_and_signs', min(primal) > 0 and sum(primal) == U-1)
    check('pair_import_identity', enc(p[:15]) == data['pairs_through_14']
          and enc(p[:14]) == completion['pairs'] and enc(p[:13]) == old['pairs_through_12'])
    check('original_a14_p14', primal[9] == F(136188345662330137488768632668073280, 7)
          and p[14] == F(2825730193896494219, 198754391512280403438773149400)
          and enc(primal[9]) == data['original_a14'])
    check('positive_normalization', 0 < rho and enc(rho) == data['rho'] == completion['rho'] == old['rho'])
    check('distinct_pair_bounds', p[5] == F(1, 68881143660) and all(0 <= x <= p[5] for x in p[1:15]))
    check('saved_pair_residuals', enc(residuals) == data['pair_system_residuals'])

    w = -F(*square['objective_matrix'][0][3])/F(*square['objective_matrix'][3][3])
    v = -F(*plane['plane_matrix'][0][2])/F(*plane['plane_matrix'][2][2])
    parameters = [F(0), v, w]
    check('same_parameters', enc(parameters) == data['parameters'] == audit['parameters']
          == completion['parameters'] == verified['parameters'] == plane['stationary']['parameters'])
    f = [F(0)]*49
    f[33], f[42] = v, w
    check('nonpivots', set(range(49))-set(col['equation_pivots']) == {27, 33, 42})
    for row, pivot in zip(col['equation_rref'], col['equation_pivots']):
        f[pivot] = F(*row[-1])-sum(F(*row[j])*f[j] for j in [27, 33, 42])
    check('all_column_coordinates', enc(f) == data['original_RREF_column'] == completion['free_column'] == verified['free_column'])
    for k, (row, rhs) in enumerate(zip(col['equations'], col['rhs'])):
        check('original_compatibility_'+str(k), dot([F(*x) for x in row], f) == F(*rhs))
    values = {tuple(row['type']): F(*row['y']) for row in old['types']}
    column, weights = [], []
    for row in col['column']:
        l, i, j = row['orbit']
        y = p[7]*f[row['variable']] if row['kind'] == 'free' else F(*row['value'])
        column.append(y)
        weights.append(C(7, i)*C(61, l-i)*C(7, j)*C(949, l-j) if l else 1)
        if l:
            values[l, 7, i, j] = y
        else:
            check('anchor_column', y == p[7])
    check('audited_column_and_weights', len(column) == 86 and enc(column) == audit['column'] and weights == audit['weights'] == col['weights'])
    kernels = [dot([F(*x)*weight for x, weight in zip(row, weights)], column) for row in col['kernel_basis']]
    check('whole_kernel_identity', len(kernels) == 49 and kernels == [0]*49
          and enc(kernels) == audit['kernel_residuals'] == data['weighted_kernel_residuals'])

    # PSD is an imported reviewed theorem, with every defining coordinate checked.
    z = [F(*x) for x in audit['z']]
    check('same_completed_vector', len(z) == 36 and enc(z) == data['same_original_basis_z']
          == completion['certificate']['z'] == verified['fresh_original_basis_solution']
          and min(z) == 0 and [k for k, x in enumerate(z) if not x] == [28])
    defining = [0,1,2,3,4,5,8,9,10,11,12,13,14,16,17,18,19,20,22,
                24,25,26,27,28,29,32,33,34,35,40,41,42,48,49,56]
    check('same_defining_rows', completion['certificate']['defining_rows']
          == audit['defining_rows'] == [['mode', k] for k in defining]+[['sign', 28]])
    check('imported_basis_invertible', len(audit['reverse_basis_pivots']) == 36
          and all(F(*x) != 0 for x in audit['reverse_basis_pivots']))
    mode_slacks = []
    for k, mode in enumerate(audit['modes']):
        row, bound = [F(*x) for x in mode['row']], F(*mode['bound'])
        slack = bound-dot(row, z)
        check('same_PSD_mode_'+str(k), mode['row'] == completion['matrix'][k]
              and mode['bound'] == completion['rhs'][k]
              and enc(slack) == mode['slack'] == completion['certificate']['mode_slacks'][k]
              and slack >= 0 and (k not in defining or slack == 0)
              and mode['full_source_block'] == verified['mode_evidence'][k]['full_block']
              and mode['minors'] == verified['mode_evidence'][k]['all_principal_minors'])
        mode_slacks.append(slack)
    check('all_PSD_modes_and_minors', len(mode_slacks) == 64
          and len(audit['all_principal_minors']) == 306 and all(F(*x) >= 0 for x in audit['all_principal_minors']))
    free = [(r, q) for r in range(8) for q in range(8) if r+q >= 7]
    raw = []
    for r in range(8):
        for q in range(8):
            h = r+q
            if h < 7:
                y = p[7] if h == 0 else F(0) if h < 5 else values[h, 7, q, r]
            else:
                y = p[7]*z[free.index((r, q))]/(C(7, r)*C(61, r)*C(7, q)*C(949, q))
                raw.append(y)
            values[7, 7, 7-r, 7-q] = y
    check('all_completed_raw_values', enc(raw) == data['same_raw_Y'] == completion['certificate']['raw_Y'])

    # Exhaust the domain independently of any saved record list.
    domain = [(l, m, i, j) for l in [5,6,7] for m in [5,6,7] if l <= m
              for i in range(l+1) for j in range(l+1)]
    saved = {tuple(row['type']): row for row in data['all_records']}
    check('complete_domain', len(domain) == len(saved) == len(data['all_records']) == 270 and set(domain) == set(saved) == set(values))
    records, full_keys, source_keys, all_slacks, inherited, new_slacks, ratios = [], {}, {}, [], [], [], []
    counts = {'boolean': 0, 'forbidden': 0, 'permitted_distinct': 0}
    orbits, distances = [], set()
    for typ in domain:
        l, m, i, j = typ
        # Fix E first. Select G independently in each of E's four regions.
        D = set(range(68))
        X, Y = set(range(l)), set(range(68, 68+l))
        U0 = set(range(i)) | set(range(l, l+m-i))
        V0 = set(range(68, 68+j)) | set(range(68+l, 68+l+m-j))
        supports = [D, (D-X)|Y, (D-U0)|V0]
        y = values[typ]
        check('audited_moment_'+str(typ), enc(y) == saved[typ]['y'] == audit['records'][str(typ)]['value'])
        check('support_sizes_'+str(typ), all(len(s) == 68 for s in supports))
        orders = list(it.permutations(range(3)))
        atoms_list = []
        for order in orders:
            A, B, C0 = [supports[k] for k in order]
            atoms = [0]*8
            for x in range(1024):
                atoms[4*(x in A)+2*(x in B)+(x in C0)] += 1
            atoms_list.append(atoms)
        key = min(map(tuple, atoms_list))
        check('full_key_'+str(typ), list(key) == saved[typ]['key'] == audit['records'][str(typ)]['key']
              and (key not in full_keys or full_keys[key] == y))
        full_keys[key] = y
        presentations = []
        for order, atoms, sr in zip(orders, atoms_list, saved[typ]['presentations']):
            A, B, C0 = [supports[k] for k in order]
            a, b, h = len(A-B), len(A-C0), len(B-C0)
            t, s = len(A-(B|C0)), len((B&C0)-A)
            label = str((typ, order))
            recipe = [956-a-b+s, b-s, a-s, s, t, a-t, b-t, 68-a-b+t]
            check('atoms_source_'+label, atoms == recipe == sr['atoms'] and list(order) == sr['order']
                  and [a,b,t,s] == sr['source_indices'] and h == sr['third_distance'] == a+b-t-s
                  and t-s == i-j == sr['t_minus_s'] and min(atoms) >= 0 and sum(atoms) == 1024)
            # First choose B relative to A, then C independently in four regions.
            orbit = C(68,a)*C(956,a)*C(a,t)*C(68-a,b-t)*C(a,s)*C(956-a,b-s)
            orbit2, rem = divmod(factorial(68)*factorial(956), prod(factorial(x) for x in atoms))
            check('positive_source_multiplicity_'+label, orbit == orbit2 == sr['orbit_size'] > 0 and rem == 0
                  and F(N*orbit)*rho*y/(M*orbit) == y)
            skey = (tuple(sorted([a,b,h])), t-s)
            check('source_equality_'+label, skey not in source_keys or source_keys[skey] == (key,y))
            source_keys[skey] = (key,y)
            boolean = len({frozenset(S) for S in [A,B,C0]}) < 3
            forbidden = not boolean and any(1 <= d <= 4 for d in [a,b,h])
            check('Boolean_forbidden_'+label, boolean == sr['boolean'] and forbidden == sr['forbidden']
                  and (not boolean or y == p[max(a,b,h)]) and (not forbidden or y == 0))
            slacks = [y, p[a]-y, 1+y-p[a]-p[b]]
            check('all_exact_saved_scalars_'+label, enc(slacks) == sr['slacks'] and enc(y) == sr['y']
                  and enc([p[a],p[b],p[h]]) == sr['pairs'])
            for k, slack in enumerate(slacks):
                check('scalar_sign_'+label+'_'+str(k), slack >= 0)
            if not boolean:
                check('distinct_lower_bound_'+label, slacks[2] >= 1-2*p[5] > 0)
            all_slacks.extend(slacks)
            if l == m == 7:
                new_slacks.extend(slacks)
                counts['boolean' if boolean else 'forbidden' if forbidden else 'permitted_distinct'] += 1
                distances.update([a,b,h]); orbits.append(orbit)
                if not boolean and not forbidden:
                    ratios.append((y/min(p[a],p[b],p[h]), typ, order))
            else:
                inherited.extend(slacks)
            presentations.append({'order':order, 'atoms':atoms, 'source_indices':[a,b,t,s],
                                  'third_distance':h, 'orbit_size':orbit, 'y':y, 'slacks':slacks})
        check('six_presentations_'+str(typ), len(saved[typ]['presentations']) == len(presentations) == 6)
        records.append({'type':typ, 'key':key, 'y':y, 'presentations':presentations})
    maximum = max(x[0] for x in ratios)
    maximizers = sorted(set(x[1] for x in ratios if x[0] == maximum))
    ratio_from_z = z[free.index((6,1))]/(C(7,6)*C(61,6)*C(7,1)*C(949,1))
    check('exact_ratio_and_manuscript_interval', maximum == F(*data['summary']['maximum_distinct_upper_ratio'])
          == ratio_from_z and (7,7,1,6) in maximizers and F(211,10**12) <= maximum < F(212,10**12) < F(1,10**9) < 1)
    check('new_counts', counts == {'boolean':6,'forbidden':84,'permitted_distinct':294}
          and len(new_slacks) == 1152 and len(orbits) == 384 and distances == set(range(15)))
    check('complete_inherited_rows', len(inherited) == 3708 and sorted(inherited)
          == sorted(F(*x) for x in verified['all_inherited_scalar_slacks'])
          == sorted(F(*x) for x in audit['inherited_scalar_slacks']))
    check('all_rows_and_extrema', len(all_slacks) == 4860 and min(new_slacks) == min(all_slacks) == 0
          and enc(min(new_slacks)) == data['summary']['minimum_new_slack']
          and min(orbits) == data['minimum_new_orbit_size'] and data['failed_rows'] == [])
    summary = {'verdict':'RETAIN L074' if not failures else 'AUDIT_FAILED', 'checks':len(checks),
               'failures':len(failures), 'types':len(domain), 'presentations':len(records)*6,
               'scalar_rows':len(all_slacks), 'new_scalar_rows':len(new_slacks), 'inherited_scalar_rows':len(inherited),
               'new_cases':counts, 'actual_minimum_slack':min(all_slacks), 'required_minimum_slack':0,
               'ratio_interval_numerator':[211,212], 'ratio_interval_denominator':10**12, 'required_maximum_ratio':1,
               'same_PSD_assignment':True, 'maximizing_types':maximizers}
    report = {'summary':summary, 'checks':checks, 'failures':failures,
              'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'original_pairs':p, 'pair_system_residuals':residuals, 'rho':rho, 'parameters':parameters,
              'free_column':f, 'column':column, 'weights':weights, 'kernel_residuals':kernels,
              'completed_z':z, 'raw_Y':raw, 'mode_slacks':mode_slacks, 'records':records,
              'maximum_distinct_upper_ratio':maximum, 'inherited_scalar_slacks':inherited}
    OUT.write_text(json.dumps(enc(report), indent=2)+'\n')
    print(json.dumps(enc(summary), sort_keys=True))
    print('Failures='+str(failures)+'; full certificate='+str(OUT.relative_to(NB)))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

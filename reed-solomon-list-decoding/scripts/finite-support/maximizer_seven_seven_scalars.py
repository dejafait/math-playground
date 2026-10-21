"""Approved fixed L073 scalar substitution. Standard library, exact rationals.

No search, optimizer, changed moment, or new matrix. Complete rows go to disk.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'maximizer-seven-seven-scalars-results.json'


def enc(x):
    if isinstance(x, Q):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def dot(x, y):
    assert len(x) == len(y)
    return sum((a*b for a, b in zip(x, y)), Q(0))


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def permute(atoms, order):
    result = [0]*8
    for mask, count in enumerate(atoms):
        dest = sum(bit for bit, old in zip([4, 2, 1], order) if mask & [4, 2, 1][old])
        result[dest] += count
    return result


def main():
    names = ['maximizer-completion-results.json', 'maximizer-completion-verification.json',
             'delsarte-lp-results.json', 'alternative-product-zero-plane-results.json',
             'seven-distance-full-base-kernel-results.json',
             'simultaneous-shell-ordinary-scalars-results.json',
             'zero-dual-plane-scalars-results.json', 'seven-shell-affine-fixed-dual-results.json']
    paths = [ROOT/name for name in names]
    result, verified, lp, point, col, old, scalar, square = [json.loads(p.read_text()) for p in paths]
    checks, failures, failed_rows = [], [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for k, data in enumerate([result, verified, lp, point, col, old, scalar, square]):
        check(f'clean_input_{k}', not data['failures'])
        for name, digest in data.get('input_hashes', data.get('source_hashes', {})).items():
            check(f'original_input_hash_{k}_{name}', hashlib.sha256((NB/name).read_bytes()).hexdigest() == digest)

    primal = [Q(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    check('complete_original_pair_domain', lp['active_distances'] == list(range(5, 69)) and len(primal) == 64)
    # Independently expand (1-Z)^j sum_s C(68-j,s) C(956-j,s) Z^s.
    pair_residuals = []
    for j in range(1, 65):
        poly = [0]*69
        for s in range(69-j):
            for t in range(min(j, 68-s)+1):
                poly[s+t] += comb(68-j, s)*comb(956-j, s)*(-1)**t*comb(j, t)
        residual = 1+sum(Q(poly[h], comb(68, h)*comb(956, h))*a for h, a in zip(range(5, 69), primal))
        pair_residuals.append(residual)
        check(f'original_L021_equation_{j}', residual == 0)
    p = [Q(1)]+[Q(0)]*4+[a/(2*comb(68, h)*comb(956, h)) for h, a in zip(range(5, 69), primal)]
    check('original_a14', primal[9] == Q(136188345662330137488768632668073280, 7))
    check('all_original_pairs_retained', enc(p[:14]) == result['pairs'] == scalar['pairs_through_13']
          and enc(p[:13]) == old['pairs_through_12'] and all(0 <= x <= p[5] for x in p[1:15]))
    N = comb(1024, 68)
    M = (Q(comb(1024, 64), comb(68, 64))+1)/2
    rho = M/N
    check('original_positive_rho', rho > 0 and enc(rho) == result['rho'] == old['rho'])

    square_matrix = [[Q(*v) for v in row] for row in square['objective_matrix']]
    plane = [[Q(*v) for v in row] for row in point['plane_matrix']]
    w = square_matrix[0][3]/(-square_matrix[3][3])
    v = plane[0][2]/(-plane[2][2])
    parameters = [Q(0), v, w]
    check('unchanged_exact_maximizer', enc(parameters) == result['parameters']
          == verified['parameters'] == point['stationary']['parameters']
          and v > 0 and enc(w) == scalar['w_star'])
    pivots = col['equation_pivots']
    rref = [[Q(*v) for v in row] for row in col['equation_rref']]
    f = [Q(0)]*49
    f[33], f[42] = v, w
    check('original_RREF_nonpivots', [j for j in range(49) if j not in pivots] == [27, 33, 42])
    for k, j in enumerate(pivots):
        f[j] = rref[k][-1]-sum(rref[k][t]*f[t] for t in [27, 33, 42])
    check('unchanged_49_column_coordinates', enc(f) == result['free_column'] == verified['free_column'])
    for k, (row, rhs) in enumerate(zip(col['equations'], col['rhs'])):
        check(f'original_column_equation_{k}', dot([Q(*x) for x in row], f) == Q(*rhs))
    base = {tuple(row['type']): Q(*row['y']) for row in old['types']}
    column = []
    for row in col['column']:
        y = p[7]*f[row['variable']] if row['kind'] == 'free' else Q(*row['value'])
        column.append(y)
        if row['orbit'] != [0, 0, 0]:
            l, i, j = row['orbit']
            base[l, 7, i, j] = y
    kernel_residuals = []
    for k, vec in enumerate(col['kernel_basis']):
        residual = sum(Q(weight)*Q(*x)*y for weight, x, y in zip(col['weights'], vec, column))
        kernel_residuals.append(residual)
        check(f'whole_base_kernel_{k}', residual == 0)

    # Reconstruct every completed coordinate from the unchanged original basis.
    A = [[Q(*x) for x in row] for row in result['matrix']]
    rhs = [Q(*x) for x in result['rhs']]
    cert = result['certificate']
    mat = []
    for kind, k in cert['defining_rows']:
        row, bound = (A[k], rhs[k]) if kind == 'mode' else ([Q(k == j) for j in range(36)], Q(0))
        mat.append(row+[bound])
    check('complete_original_basis', len(mat) == 36)
    for j in range(36):
        k = next(k for k in range(j, 36) if mat[k][j])
        mat[j], mat[k] = mat[k], mat[j]
        divisor = mat[j][j]
        mat[j] = [x/divisor for x in mat[j]]
        for k in range(36):
            if k != j:
                multiplier = mat[k][j]
                mat[k] = [x-multiplier*y for x, y in zip(mat[k], mat[j])]
    z = [row[-1] for row in mat]
    check('same_all_36_completed_coordinates', enc(z) == cert['z'] == verified['fresh_original_basis_solution']
          and min(z) >= 0 and [j for j, x in enumerate(z) if x == 0] == [28])
    for k, (row, bound) in enumerate(zip(A, rhs)):
        slack = bound-dot(row, z)
        ev = verified['mode_evidence'][k]
        check(f'same_original_PSD_mode_{k}', enc(row) == ev['row'] and enc(bound) == ev['bound']
              and enc(slack) == cert['mode_slacks'][k] == ev['slack'] and slack >= 0
              and all(Q(*m['value']) >= 0 for m in ev['all_principal_minors']))
    free = [(r, q) for r, q in it.product(range(8), repeat=2) if r+q >= 7]
    raw = []
    for r, q in it.product(range(8), repeat=2):
        h = r+q
        if h <= 6:
            y = p[7] if h == 0 else Q(0) if h <= 4 else base[h, 7, q, r]
        else:
            y = p[7]*z[free.index((r, q))]/(comb(7, r)*comb(61, r)*comb(7, q)*comb(949, q))
            raw.append(y)
        base[7, 7, 7-r, 7-q] = y
    check('unchanged_original_raw_Y', enc(raw) == cert['raw_Y'] and result['free'] == enc(free))

    original_records = {tuple(rec['type']): rec for rec in result['records']}
    verified_records = {tuple(rec['type']): rec for rec in verified['records']}
    rows, key_values, source_values, ratios, all_slacks, inherited_slacks = [], {}, {}, [], [], []
    new_counts = {'types': 0, 'presentations': 0, 'boolean': 0, 'forbidden': 0, 'permitted_distinct': 0}
    new_distances, multiplicities = set(), []
    for typ, y in base.items():
        l, m, i, j = typ
        atom_recipe = [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]
        D = set(range(68))
        U, V = set(range(m)), set(range(68, 68+m))
        X = set(range(i)) | set(range(m, m+l-i))
        Y = set(range(68, 68+j)) | set(range(68+m, 68+m+l-j))
        supports = [D, (D-X)|Y, (D-U)|V]
        is_new = (l, m) == (7, 7)
        new_counts['types'] += is_new
        presentations = []
        orders = list(it.permutations(range(3)))
        canonical = min(tuple(permute(atom_recipe, order)) for order in orders)
        check(f'full_unordered_key_{typ}', canonical not in key_values or key_values[canonical] == y)
        key_values[canonical] = y
        fixed = original_records[typ]['value']
        check(f'all_fixed_and_completed_entries_{typ}', (fixed is None or Q(*fixed) == y)
              and Q(*verified_records[typ]['value']) == y)
        for k, order in enumerate(orders):
            AA, BB, CC = [supports[t] for t in order]
            atoms = [0]*8
            for x in range(1024):
                atoms[4*(x in AA)+2*(x in BB)+(x in CC)] += 1
            a, b, h = len(AA-BB), len(AA-CC), len(BB-CC)
            t, s = len(AA-(BB|CC)), len((BB&CC)-AA)
            check(f'complete_actual_atoms_{typ}_{k}', all(len(S) == 68 for S in [AA, BB, CC])
                  and atoms == permute(atom_recipe, order) == original_records[typ]['regions'][k]
                  == verified_records[typ]['regions'][k]
                  and h == a+b-t-s and t-s == i-j
                  and min(atoms) >= 0 and sum(atoms) == 1024)
            reconstructed = [956-a-b+s, b-s, a-s, s, t, a-t, b-t, 68-a-b+t]
            check(f'ordered_source_indices_{typ}_{k}', atoms == reconstructed)
            denominator = 1
            for x in atoms:
                denominator *= factorial(x)
            orbit, remainder = divmod(factorial(68)*factorial(956), denominator)
            counted = (choose(68, t)*choose(68-t, a-t)*choose(68-a, b-t)
                       *choose(956, s)*choose(956-s, a-s)*choose(956-a, b-s))
            check(f'positive_orbit_normalization_{typ}_{k}', remainder == 0 and orbit == counted > 0
                  and (N*orbit*rho*y)/(M*orbit) == y)
            source_key = (tuple(sorted([a, b, h])), t-s)
            check(f'all_source_equalities_{typ}_{k}', source_key not in source_values
                  or source_values[source_key] == (canonical, y))
            source_values[source_key] = (canonical, y)
            boolean = 0 in [a, b, h]
            forbidden = not boolean and any(1 <= d <= 4 for d in [a, b, h])
            expected = p[max(a, b, h)] if boolean else Q(0) if forbidden else y
            check(f'Boolean_forbidden_and_lookup_{typ}_{k}', y == expected
                  and (base.get((*sorted([a, b]), t, s), y) == y))
            slacks = [y, p[a]-y, 1+y-p[a]-p[b]]
            row = {'order': order, 'atoms': atoms, 'source_indices': [a, b, t, s],
                   'third_distance': h, 't_minus_s': t-s, 'orbit_size': orbit,
                   'y': y, 'pairs': [p[a], p[b], p[h]], 'slacks': slacks,
                   'boolean': boolean, 'forbidden': forbidden}
            if min(slacks) < 0:
                failed_rows.append({'type': typ, **row})
            check(f'ordinary_scalar_rows_{typ}_{k}', min(slacks) >= 0)
            all_slacks.extend(slacks)
            if not is_new:
                inherited_slacks.extend(slacks)
            else:
                new_counts['presentations'] += 1
                new_counts['boolean' if boolean else 'forbidden' if forbidden else 'permitted_distinct'] += 1
                new_distances.update([a, b, h])
                multiplicities.append(orbit)
                if not boolean and not forbidden:
                    ratios.append((y/min(p[a], p[b], p[h]), typ, k))
            presentations.append(row)
        rows.append({'type': typ, 'y': y, 'key': canonical, 'presentations': presentations})
    check('complete_new_domain', new_counts['types'] == 64 and new_counts['presentations'] == 384
          and new_distances == set(range(15)))
    check('complete_all_domain', len(rows) == 270 and len(all_slacks) == 4860
          and len(inherited_slacks) == 3708 and enc(inherited_slacks) == verified['all_inherited_scalar_slacks'])
    maximum, maximizing_type, maximizing_order = max(ratios)
    minimum_new = min(s for row in rows if row['type'][:2] == (7, 7)
                      for pres in row['presentations'] for s in pres['slacks'])
    check('strict_distinct_upper_bound', 0 < maximum < Q(1, 10**9))
    ratio_floor = maximum.numerator*10**12//maximum.denominator
    summary = {'verdict': 'ALL_SCALAR_ROWS_PASS' if not failures else 'FAILED',
               'checks': len(checks), 'failures': len(failures), 'failed_presentations': len(failed_rows),
               'all_types': len(rows), 'all_presentations': len(rows)*6, 'all_scalar_rows': len(all_slacks),
               'new': new_counts, 'new_scalar_rows': new_counts['presentations']*3,
               'inherited_scalar_rows': len(inherited_slacks), 'minimum_new_slack': minimum_new,
               'required_minimum_slack': 0, 'maximum_distinct_upper_ratio': maximum,
               'required_maximum_ratio': 1, 'ratio_interval_numerator': [ratio_floor, ratio_floor+1],
               'ratio_interval_denominator': 10**12, 'maximizing_type': maximizing_type,
               'maximizing_order': maximizing_order}
    out = {'summary': summary, 'checks': checks, 'failures': failures, 'failed_rows': failed_rows,
           'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'parameters': parameters, 'rho': rho, 'pairs_through_14': p[:15], 'original_a14': primal[9],
           'pair_system_residuals': pair_residuals, 'original_RREF_column': f,
           'weighted_kernel_residuals': kernel_residuals, 'same_original_basis_z': z,
           'same_raw_Y': raw, 'all_records': rows, 'minimum_new_orbit_size': min(multiplicities)}
    OUT.write_text(json.dumps(enc(out), indent=2)+'\n')
    brief = {k: val for k, val in summary.items() if k != 'maximum_distinct_upper_ratio'}
    print(json.dumps(enc(brief), sort_keys=True))
    print(f'Full exact rows and failures: {OUT.relative_to(NB)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

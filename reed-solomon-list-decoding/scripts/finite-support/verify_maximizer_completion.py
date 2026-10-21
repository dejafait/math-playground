"""Independent exact original-row/PSD check. No notebook imports or optimizer."""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'maximizer-completion-verification.json'


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {k: enc(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [enc(v) for v in x]
    return x


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


@lru_cache(None)
def source(n, l, m, a, t):
    return sum((-1)**(u-t)*choose(u, t)*choose(n-2*a, u-a)
               *choose(n-a-u, l-u)*choose(n-a-u, m-u)
               for u in range(a, min(l, m, n-a)+1) if u >= t)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def det(M):
    if not M:
        return F(1)
    return sum((-1)**j*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(len(M)))


def regions(sets):
    atoms = [0]*8
    for x in range(1024):
        atoms[sum(bit for bit, support in zip([4, 2, 1], sets) if x in support)] += 1
    return tuple(atoms)


def supports(l, m, i, j):
    D = set(range(68))
    U, V = set(range(m)), set(range(68, 68+m))
    X = set(range(i)) | set(range(m, m+l-i))
    Y = set(range(68, 68+j)) | set(range(68+m, 68+m+l-j))
    return D, (D-X)|Y, (D-U)|V


def main():
    names = ['maximizer-completion-results.json', 'alternative-product-zero-plane-results.json',
             'seven-distance-full-base-kernel-results.json',
             'simultaneous-shell-ordinary-scalars-results.json',
             'zero-dual-plane-scalars-results.json', 'seven-shell-affine-fixed-dual-results.json']
    paths = [ROOT/n for n in names]
    result, point, col, old, scalar, square = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for k, data in enumerate([result, point, col, old, scalar, square]):
        check(f'clean_input_{k}', not data['failures'])
        for path, digest in data.get('input_hashes', data.get('source_hashes', {})).items():
            check(f'input_hash_{k}_{path}', hashlib.sha256((NB/path).read_bytes()).hexdigest() == digest)
    p = [F(*v) for v in scalar['pairs_through_13']]
    rho = (F(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    check('rho_pairs_unchanged', rho == F(*old['rho']) == F(*result['rho']) > 0
          and p[:13] == [F(*v) for v in old['pairs_through_12']]
          and enc(p) == result['pairs'] and p[7] == F(3539, 248922676958508) > 0)
    M = [[F(*v) for v in row] for row in square['objective_matrix']]
    w = M[0][3]/(-M[3][3])
    N = [[F(*v) for v in row] for row in point['plane_matrix']]
    v = N[0][2]/(-N[2][2])
    check('exact_maximizer', w == F(*scalar['w_star']) and N[2][2] < 0
          and enc([F(0), v, w]) == point['stationary']['parameters'] == result['parameters'])
    piv = col['equation_pivots']
    R = [[F(*v) for v in row] for row in col['equation_rref']]
    f = [F(0)]*49
    f[33], f[42] = v, w
    check('original_rref_nonpivots', [j for j in range(49) if j not in piv] == [27, 33, 42])
    for i, j in enumerate(piv):
        f[j] = R[i][-1]-sum(R[i][k]*f[k] for k in [27, 33, 42])
    check('all_49_original_column_coordinates', enc(f) == result['free_column'] and min(f) >= 0
          and [j for j, x in enumerate(f) if x == 0] == [27])
    for i, (row, b) in enumerate(zip(col['equations'], col['rhs'])):
        check(f'original_column_equation_{i}', dot([F(*x) for x in row], f) == F(*b))
    base = {tuple(row['type']): F(*row['y']) for row in old['types']}
    column = []
    for row in col['column']:
        y = p[7]*f[row['variable']] if row['kind'] == 'free' else F(*row['value'])
        column.append(y)
        if row['orbit'] != [0, 0, 0]:
            l, i, j = row['orbit']
            base[l, 7, i, j] = y
    kernel = []
    for j, vec in enumerate(col['kernel_basis']):
        residual = sum(F(weight)*F(*x)*y for weight, x, y in zip(col['weights'], vec, column))
        kernel.append(residual)
        check(f'whole_weighted_kernel_{j}', residual == 0)
    free = [(r, q) for r, q in it.product(range(8), repeat=2) if r+q >= 7]
    cert = result['certificate']
    check('rational_witness_kind', cert['kind'] == 'RATIONAL_WITNESS' and len(cert['z']) == 36
          and result['free'] == [list(t) for t in free])
    z = [F(*x) for x in cert['z']]
    raw = []
    for r, q in it.product(range(8), repeat=2):
        h = r+q
        if h <= 6:
            y = p[7] if h == 0 else F(0) if h <= 4 else base[h, 7, q, r]
        else:
            j = free.index((r, q))
            y = p[7]*z[j]/(choose(7, r)*choose(61, r)*choose(7, q)*choose(949, q))
            raw.append(y)
            check(f'original_sign_{j}', z[j] >= 0)
        base[7, 7, 7-r, 7-q] = y
    check('36_raw_entries', enc(raw) == cert['raw_Y'])
    dictionary, records, scalar_slacks = {}, [], []
    saved_records = {tuple(row['type']): row for row in result['records']}
    for typ, y in base.items():
        sets = supports(*typ)
        orders = [regions(ss) for ss in it.permutations(sets)]
        key = min(orders)
        check(f'actual_support_sizes_{typ}', all(len(s) == 68 for s in sets))
        check(f'all_six_regions_{typ}', [list(at) for at in orders] == saved_records[typ]['regions'])
        fixed = saved_records[typ]['value']
        check(f'fixed_value_retained_{typ}', fixed is None or y == F(*fixed))
        check(f'one_value_per_full_key_{typ}', key not in dictionary or dictionary[key] == y)
        dictionary[key] = y
        for k, at in enumerate(orders):
            a, b, h = at[4]+at[5], at[4]+at[6], at[2]+at[6]
            lookup = None
            if min(a, b, h) == 0:
                lookup = p[max(a, b, h)]
            elif any(1 <= t <= 4 for t in [a, b, h]):
                lookup = F(0)
            else:
                lookup = base.get((*sorted([a, b]), at[4], at[3]))
            check(f'every_unordered_lookup_{typ}_{k}', lookup is None or lookup == y)
            # Only inherited old/column scalar rows, not seven/seven upper rows.
            if typ[:2] != (7, 7):
                slacks = [y, p[a]-y, 1+y-p[a]-p[b]]
                scalar_slacks.extend(slacks)
                check(f'inherited_scalar_rows_{typ}_{k}', min(slacks) >= 0)
        records.append({'type': typ, 'value': y, 'regions': orders})
    check('all_270_types_1620_presentations', len(records) == 270 and len(scalar_slacks) == 3708)
    S = {l: choose(68, l)*choose(956, l) for l in [5, 6, 7]}
    mode_evidence, slacks, minors, rows, bounds = [], [], [], [], []
    for ix, (a, b) in enumerate(it.product(range(8), repeat=2)):
        layers = [l for l in [5, 6] if max(a, b) <= l]
        d7 = choose(68-2*a, 7-a)*choose(956-2*b, 7-b)

        def block(l, m):
            l, m = min(l, m), max(l, m)
            ans = sum(source(68, l, m, a, i)*source(956, l, m, b, j)*base[l, m, i, j]
                      for i, j in it.product(range(l+1), repeat=2))
            return ans-(p[l]*p[m]*S[l]*S[m] if ix == 0 else 0)

        B = [[block(l, m) for m in layers] for l in layers]
        cross = [block(l, 7) for l in layers]
        cost, ranges = F(0), []
        if len(B) == 2:
            x, t, zz = B[0][0], B[0][1], B[1][1]
            c, d = cross
            delta = x*zz-t*t
            check(f'old_PSD_{ix}', min(x, zz, delta) >= 0)
            if delta > 0:
                cost = (zz*c*c-2*t*c*d+x*d*d)/delta
            elif x > 0:
                ranges.append(x*d-t*c)
                cost = c*c/x
            elif zz > 0:
                ranges.append(c)
                cost = d*d/zz
            else:
                ranges.extend(cross)
        elif B:
            check(f'old_PSD_{ix}', B[0][0] >= 0)
            if B[0][0] > 0:
                cost = cross[0]**2/B[0][0]
            else:
                ranges.extend(cross)
        check(f'singular_range_{ix}', not any(ranges) and d7 > 0)
        rawnew = block(7, 7)
        slack = (rawnew-cost)/(p[7]*d7)
        row = [-F(source(68, 7, 7, a, 7-r)*source(956, 7, 7, b, 7-q),
                  d7*choose(7, r)*choose(61, r)*choose(7, q)*choose(949, q)) for r, q in free]
        fixednew = sum(source(68, 7, 7, a, i)*source(956, 7, 7, b, j)*base[7, 7, i, j]
                       for i, j in it.product(range(8), repeat=2) if 14-i-j <= 6)
        fixednew -= p[7]**2*S[7]**2 if ix == 0 else 0
        bound = (fixednew-cost)/(p[7]*d7)
        check(f'original_64_by_36_row_{ix}', enc(row) == result['matrix'][ix]
              and enc(bound) == result['rhs'][ix] and slack == bound-dot(row, z))
        check(f'full_anchor_cost_{ix}', enc(B) == result['modes'][ix]['B']
              and enc(cross) == result['modes'][ix]['cross']
              and enc(cost) == result['modes'][ix]['energy'])
        check(f'original_mode_pass_{ix}', slack >= 0 and enc(slack) == cert['mode_slacks'][ix])
        rows.append(row)
        bounds.append(bound)
        full = [row+[c] for row, c in zip(B, cross)]+[cross+[rawnew]]
        localminors = []
        for size in range(1, len(full)+1):
            for ind in it.combinations(range(len(full)), size):
                value = det([[full[i][j] for j in ind] for i in ind])
                localminors.append({'indices': ind, 'value': value})
                check(f'whole_mode_principal_minor_{ix}_{ind}', value >= 0)
                minors.append(value)
        slacks.append(slack)
        mode_evidence.append({'mode': [a, b], 'B': B, 'cross': cross, 'ranges': ranges,
                              'energy': cost, 'raw_new_anchor_corrected': rawnew,
                              'row': row, 'bound': bound, 'slack': slack, 'full_block': full,
                              'all_principal_minors': localminors})
    defining = cert['defining_rows']
    check('36_defining_original_rows', len(defining) == 36)
    mat = []
    for kind, index in defining:
        rr, bb = (rows[index], bounds[index]) if kind == 'mode' else ([F(index == j) for j in range(36)], F(0))
        check(f'defining_row_tight_{kind}_{index}', dot(rr, z) == bb)
        mat.append(rr+[bb])
    # Independent full Gauss-Jordan reconstruction from the original rows.
    basis_pivots = []
    for j in range(36):
        k = next((k for k in range(j, 36) if mat[k][j]), None)
        check(f'defining_basis_nonsingular_{j}', k is not None)
        if k is None:
            raise RuntimeError('Singular original defining basis')
        mat[j], mat[k] = mat[k], mat[j]
        pivot = mat[j][j]
        basis_pivots.append(pivot)
        mat[j] = [x/pivot for x in mat[j]]
        for k in range(36):
            if k != j:
                multiplier = mat[k][j]
                mat[k] = [x-multiplier*y for x, y in zip(mat[k], mat[j])]
    recovered = [row[-1] for row in mat]
    check('fresh_original_basis_solution', recovered == z)
    check('positive_scaling_all_entries', min(base.values()) >= 0 and rho > 0)
    summary = {'checks': len(checks), 'failures': len(failures), 'original_modes': 64,
               'signs': len(z), 'types': len(records), 'presentations': 6*len(records),
               'inherited_scalar_rows': len(scalar_slacks), 'principal_minors': len(minors),
               'positive_z': sum(x > 0 for x in z), 'zero_z': sum(x == 0 for x in z),
               'positive_modes': sum(x > 0 for x in slacks), 'zero_modes': sum(x == 0 for x in slacks),
               'minimum_mode_slack': min(slacks), 'required_minimum': 0,
               'verdict': 'EXACT_COMPLETION_VERIFIED' if not failures else 'CHECK_FAILED'}
    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'checks': checks, 'failures': failures, 'summary': summary, 'parameters': [F(0), v, w],
           'free_column': f, 'weighted_kernel_residuals': kernel, 'records': records,
           'mode_evidence': mode_evidence, 'all_inherited_scalar_slacks': scalar_slacks}
    out['defining_basis_pivots'] = basis_pivots
    out['fresh_original_basis_solution'] = recovered
    out['tight_mode_indices'] = [i for i, x in enumerate(slacks) if x == 0]
    out['zero_variable_indices'] = [j for j, x in enumerate(z) if x == 0]
    OUT.write_text(json.dumps(enc(out), indent=2)+'\n')
    print(json.dumps(enc(summary), sort_keys=True))
    print(f'Failures={failures}; full certificate={OUT.relative_to(NB)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

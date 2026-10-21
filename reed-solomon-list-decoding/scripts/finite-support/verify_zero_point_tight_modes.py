"""Independent reconstruction/substitution, no notebook code or optimizer."""
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
OUT = ROOT/'zero-point-tight-modes-verification.json'


def encode(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [encode(v) for v in x]
    return x


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


@lru_cache(None)
def source(n, l, m, a, t):
    return sum((-1)**(u-t)*choose(u, t)*choose(n-2*a, u-a)
               *choose(n-a-u, l-u)*choose(n-a-u, m-u)
               for u in range(a, min(l, m, n-a)+1) if u >= t)


def regions(sets):
    # Complete actual supports, independently of the constructor's mask map.
    return tuple(sum(1 for x in range(1024)
                     if sum(bit for bit, support in zip([4, 2, 1], sets) if x in support) == k)
                 for k in range(8))


def supports(l, m, i, j):
    D = set(range(68))
    U, V = set(range(m)), set(range(68, 68+m))
    X = set(range(i)) | set(range(m, m+l-i))
    Y = set(range(68, 68+j)) | set(range(68+m, 68+m+l-j))
    return D, (D-X)|Y, (D-U)|V


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def main():
    paths = [ROOT/n for n in ['zero-point-tight-modes-results.json',
                              'simultaneous-shell-ordinary-scalars-results.json',
                              'seven-distance-full-base-kernel-results.json',
                              'seven-shell-affine-fixed-dual-results.json',
                              'zero-dual-plane-scalars-results.json']]
    data, old, col, square, point = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for k, d in enumerate([data, old, col, square, point]):
        check(f'input_clean_{k}', not d['failures'])
        for path, digest in d.get('input_hashes', d.get('source_hashes', {})).items():
            check(f'input_hash_{k}_{path}', hashlib.sha256((NB/path).read_bytes()).hexdigest() == digest)
    p = [F(*v) for v in point['pairs_through_13']]
    rho = (F(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    check('rho_original', rho > 0 and rho == F(*old['rho']) == F(*data['rho']) == F(*point['rho']))
    check('original_pairs', p[:13] == [F(*v) for v in old['pairs_through_12']]
          and p[7] == F(3539, 248922676958508) == F(*data['p7']))
    # Recover the specified RREF solution independently of the saved affine rows.
    c = [F(0)]*49
    direction = [F(j == 42) for j in range(49)]
    pivots = col['equation_pivots']
    R = [[F(*v) for v in row] for row in col['equation_rref']]
    check('original_nonpivots', [j for j in range(49) if j not in pivots] == [27, 33, 42])
    for i, j in enumerate(pivots):
        c[j], direction[j] = R[i][-1], -R[i][42]
    M = [[F(*v) for v in row] for row in square['objective_matrix']]
    w = M[0][3]/(-M[3][3])
    check('zero_square', M[3][3] < 0 and (-M[3][3])*M[0][0]+M[0][3]**2 == 0)
    check('same_w_star', w == F(*point['w_star']) == F(*data['w_star']))
    f = [a+w*b for a, b in zip(c, direction)]
    check('all_49_coordinates', encode(f) == data['free_column'])
    check('column_nonnegative', all(v >= 0 for v in f)
          and [j for j, v in enumerate(f) if v == 0] == [27, 33])
    base = {tuple(row['type']): F(*row['y']) for row in old['types']}
    column = []
    for row in col['column']:
        y = p[7]*f[row['variable']] if row['kind'] == 'free' else F(*row['value'])
        column.append(y)
        if row['orbit'] != [0, 0, 0]:
            l, i, j = row['orbit']
            base[l, 7, i, j] = y
    check('all_86_column_entries', encode(column) == data['column'])
    weights = [F(x) for x in col['weights']]
    original_kernel_residuals = []
    for j, v in enumerate(col['kernel_basis']):
        residual = sum(weights[i]*F(*v[i])*column[i] for i in range(86))
        original_kernel_residuals.append(residual)
        check(f'weighted_original_kernel_{j}', residual == 0)

    dictionary = {}
    for typ, value in base.items():
        key = min(regions(ordered) for ordered in it.permutations(supports(*typ)))
        check(f'base_key_{typ}', key not in dictionary or dictionary[key] == value)
        dictionary[key] = value
    count, free_keys, reconstructed_records = 0, {}, []
    for l, m in [(5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (7, 7)]:
        for i, j in it.product(range(l+1), repeat=2):
            typ = (l, m, i, j)
            sets = supports(*typ)
            check(f'support_sizes_{typ}', all(len(s) == 68 for s in sets))
            orders = [regions(ss) for ss in it.permutations(sets)]
            key = min(orders)
            choices = []
            for aa in orders:
                ab, ac, bc = aa[4]+aa[5], aa[4]+aa[6], aa[2]+aa[6]
                if min(ab, ac, bc) == 0:
                    value = p[max(ab, ac, bc)]
                elif any(1 <= h <= 4 for h in [ab, ac, bc]):
                    value = F(0)
                else:
                    value = base.get((*sorted([ab, ac]), aa[4], aa[3]))
                if value is not None:
                    choices.append(value)
            if key in dictionary:
                choices.append(dictionary[key])
            check(f'unordered_consistency_{typ}', len(set(choices)) <= 1)
            value = choices[0] if choices else None
            if value is not None:
                base[typ] = dictionary[key] = value
            else:
                check(f'unassigned_only77_{typ}', l == m == 7)
                rq = (7-i, 7-j)
                check(f'free_no_extra_identification_{typ}', key not in free_keys or free_keys[key] == rq)
                free_keys[key] = rq
            record = {'type': list(typ), 'key': list(key), 'presentations': orders, 'value': value}
            check(f'complete_record_{count}', encode(record) == data['records'][count])
            reconstructed_records.append(record)
            count += 1
    free = sorted(free_keys.values())
    check('exact_36_free_keys', len(free_keys) == 36 and encode(free) == data['free']
          and free == [(r, q) for r in range(8) for q in range(8) if r+q >= 7])
    for r in range(8):
        for q in range(8):
            if r+q <= 6:
                expected = p[7] if r+q == 0 else F(0) if r+q <= 4 else base[r+q, 7, q, r]
                check(f'forced_entry_{r}_{q}', base[7, 7, 7-r, 7-q] == expected)

    h = [F(1), F(20435, 441), F(13481000, 13671), F(2688040, 217),
         F(1307664259, 13671), F(5294968393, 13671), F(0), F(0)]
    k = [F(49, 100880416043264), F(7665, 38718903137024),
         F(17301, 551968803584), F(5461349, 2754064239872)]+[F(0)]*4
    selected = [8*a+b for a in range(6) for b in range(4)]
    lam = [h[a]*k[b] for a in range(6) for b in range(4)]
    check('positive_unchanged_weights', all(v > 0 for v in lam)
          and encode(lam) == data['weights'] and data['selected_indices'] == selected)
    A, rhs, modes = [], [], []
    sizes = {l: comb(68, l)*comb(956, l) for l in [5, 6, 7]}
    for a, b in it.product(range(8), repeat=2):
        ix = 8*a+b
        layers = [l for l in [5, 6] if a <= l and b <= l]
        d7 = comb(68-2*a, 7-a)*comb(956-2*b, 7-b)

        def block(l, m):
            l, m = min(l, m), max(l, m)
            value = sum(source(68, l, m, a, i)*source(956, l, m, b, j)*base[l, m, i, j]
                        for i, j in it.product(range(l+1), repeat=2))
            return value-(p[l]*p[m]*sizes[l]*sizes[m] if ix == 0 else 0)

        B = [[block(l, m) for m in layers] for l in layers]
        cross = [block(l, 7) for l in layers]
        range_values, cost = [], F(0)
        if len(layers) == 2:
            x, y, z = B[0][0], B[0][1], B[1][1]
            u, v = cross
            delta = x*z-y*y
            check(f'old_psd_{ix}', x >= 0 and z >= 0 and delta >= 0)
            if delta > 0:
                cost = (z*u*u-2*y*u*v+x*v*v)/delta
            elif x > 0:
                range_values.append(x*v-y*u)
                cost = u*u/x
            elif z > 0:
                range_values.extend([y, u])
                cost = v*v/z
            else:
                range_values.extend([y, u, v])
        elif layers:
            x, u = B[0][0], cross[0]
            check(f'old_psd_{ix}', x >= 0)
            if x > 0:
                cost = u*u/x
            else:
                range_values.append(u)
        check(f'full_singular_ranges_{ix}', not any(range_values))
        fixed = sum(base[7, 7, 7-r, 7-q]*F(source(68, 7, 7, a, 7-r)*source(956, 7, 7, b, 7-q), d7)/p[7]
                    for r in range(8) for q in range(8) if r+q <= 6)
        anchor = p[7]*sizes[7] if ix == 0 else F(0)
        bound = fixed-anchor-cost/(p[7]*d7)
        saved = data['modes'][ix]
        check(f'full_mode_{ix}', encode(B) == saved['B'] and encode(cross) == saved['cross']
              and d7 == saved['D7'] and encode(fixed) == saved['F']
              and encode(anchor) == saved['anchor'] and encode(cost/(p[7]*d7)) == saved['required']
              and encode(bound) == saved['rhs'])
        modes.append({'mode': [a, b], 'B': B, 'cross': cross, 'range_residuals': range_values,
                      'required': cost/(p[7]*d7), 'F': fixed, 'anchor': anchor, 'rhs': bound})
        if ix in selected:
            row = [-F(source(68, 7, 7, a, 7-r)*source(956, 7, 7, b, 7-q),
                      d7*comb(7, r)*comb(61, r)*comb(7, q)*comb(949, q)) for r, q in free]
            check(f'original_scaled_row_{ix}', encode(row) == data['matrix'][len(A)]
                  and encode(bound) == data['rhs'][len(A)])
            A.append(row)
            rhs.append(bound)
    cancellations = [dot(lam, col) for col in zip(*A)]
    check('36_full_cancellations', not any(cancellations))
    check('weighted_rhs_zero', dot(lam, rhs) == 0)
    check('saved_zero_identities', encode(cancellations) == data['cancellations']
          and data['weighted_rhs'] == [0, 1])
    check('certificate_is_solution', data['certificate']['kind'] == 'SOLUTION')
    z = [F(*v) for v in data['certificate']['z']]
    residuals = [dot(row, z)-bound for row, bound in zip(A, rhs)]
    for i, residual in enumerate(residuals):
        check(f'original_equality_{i}', residual == 0)
    check('saved_residuals', encode(residuals) == data['certificate']['original_row_residuals'])
    # Check the same equalities in raw Y, without relying on the z scaling.
    for (r, q), value in zip(free, z):
        base[7, 7, 7-r, 7-q] = p[7]*value/(comb(7, r)*comb(61, r)*comb(7, q)*comb(949, q))
    raw_residuals = []
    for ix in selected:
        a, b = divmod(ix, 8)
        d7 = comb(68-2*a, 7-a)*comb(956-2*b, 7-b)
        newblock = sum(source(68, 7, 7, a, i)*source(956, 7, 7, b, j)*base[7, 7, i, j]
                       for i, j in it.product(range(8), repeat=2))
        if ix == 0:
            newblock -= p[7]**2*sizes[7]**2
        residual = newblock/(p[7]*d7)-modes[ix]['required']
        raw_residuals.append(residual)
        check(f'raw_Y_schur_equality_{ix}', residual == 0)
    # Independent rank calculation on coefficients only, using forward elimination.
    work, row_index, pivot_columns = [row[:] for row in A], 0, []
    for j in range(36):
        nonzero = next((i for i in range(row_index, 24) if work[i][j]), None)
        if nonzero is None:
            continue
        work[row_index], work[nonzero] = work[nonzero], work[row_index]
        for i in range(row_index+1, 24):
            if work[i][j]:
                factor = work[i][j]/work[row_index][j]
                work[i] = [x-factor*y for x, y in zip(work[i], work[row_index])]
        pivot_columns.append(j)
        row_index += 1
        if row_index == 24:
            break
    check('rank_23', row_index == 23 and data['summary']['rank'] == 23)
    check('same_pivot_columns', pivot_columns == data['pivots'])
    check('consistent_summary', data['summary']['verdict'] == 'CONSISTENT'
          and data['summary']['augmented_rank'] == 23 and data['summary']['nullity'] == 13)
    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'checks': checks, 'failures': failures, 'records': reconstructed_records,
           'modes': modes, 'matrix': A, 'rhs': rhs, 'weights': lam,
           'cancellations': cancellations, 'weighted_rhs': dot(lam, rhs),
           'original_kernel_residuals': original_kernel_residuals, 'z': z,
           'original_row_residuals': residuals, 'raw_Y_schur_residuals': raw_residuals,
           'rank_echelon': work, 'rank_pivots': pivot_columns,
           'summary': {'verdict': 'CONSISTENT' if not failures else 'VERIFICATION_FAILED',
                       'rank': row_index, 'equations': 24, 'variables': 36,
                       'substituted_equalities': len(residuals), 'raw_equalities': len(raw_residuals),
                       'types': count, 'presentations': 6*count,
                       'checks': len(checks), 'failures': len(failures)}}
    OUT.write_text(json.dumps(encode(out), indent=2)+'\n')
    print(f'Independent equality verdict={out["summary"]["verdict"]}; rank={row_index}; original substitutions={sum(v == 0 for v in residuals)}/24; raw Schur substitutions={sum(v == 0 for v in raw_residuals)}/24; required=24/24 in both; checks={len(checks)}; failures={failures}')
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

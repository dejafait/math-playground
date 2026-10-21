"""L070 audit: complete original-data checks and independent exact ranks.

No notebook code or numerical solver is imported. Earlier decomposition and
kernel theorems are inputs; no omitted completion inequalities are tested.
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
OUT = ROOT/'zero-point-tight-modes-critical-audit.json'


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


def dot(x, y):
    assert len(x) == len(y)
    return sum((a*b for a, b in zip(x, y)), F(0))


@lru_cache(None)
def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*c(u, t)*c(n-2*a, u-a)
               *c(n-a-u, l-u)*c(n-a-u, m-u)
               for u in range(max(a, t), min(l, m)+1))


def eigen(n, a, r):
    return sum((-1)**s*c(a, s)*c(7-a, r-s)*c(n-7-a, r-s)
               for s in range(r+1))


def eliminate(matrix, reverse=False):
    """Fresh exact forward elimination; record invertible row operations."""
    work = [row[:] for row in matrix]
    if reverse:
        work.reverse()
    nr, nc = len(work), len(work[0])
    operations, pivots, at = [], [], 0
    for j in (reversed(range(nc)) if reverse else range(nc)):
        pivot = next((i for i in range(at, nr) if work[i][j]), None)
        if pivot is None:
            continue
        work[at], work[pivot] = work[pivot], work[at]
        operations.append(['swap', at, pivot])
        for i in range(at+1, nr):
            if work[i][j]:
                scale = work[i][j]/work[at][j]
                work[i] = [x-scale*y for x, y in zip(work[i], work[at])]
                operations.append(['subtract', i, at, scale])
        pivots.append(j)
        at += 1
        if at == nr:
            break
    return {'rank': at, 'pivots': pivots, 'echelon': work,
            'initial_rows_reversed': reverse, 'operations': operations}


def main():
    names = ['zero-point-tight-modes-results.json',
             'zero-point-tight-modes-verification.json',
             'simultaneous-shell-ordinary-scalars-results.json',
             'seven-distance-full-base-kernel-results.json',
             'seven-shell-affine-fixed-dual-results.json',
             'zero-dual-plane-scalars-results.json',
             'simultaneous-seven-shell-results.json']
    paths = [ROOT/n for n in names]
    data, verified, old, col, square, point, original = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, good):
        checks.append(name)
        if not good:
            failures.append(name)

    for path, obj in zip(paths, [data, verified, old, col, square, point, original]):
        check('clean_'+path.name, obj['failures'] == [])
        for rel, digest in obj.get('input_hashes', obj.get('source_hashes', {})).items():
            check('hash_'+path.name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p = [F(*v) for v in point['pairs_through_13']]
    rho = (F(c(1024, 64), c(68, 64))+1)/(2*c(1024, 68))
    check('positive_original_normalizations', rho > 0 and p[7] == F(3539, 248922676958508) > 0
          and all(F(*obj['rho']) == rho for obj in [data, old, point])
          and p[:13] == [F(*v) for v in old['pairs_through_12']])
    rr = [[F(*v) for v in row] for row in col['equation_rref']]
    piv = col['equation_pivots']
    check('rref_dimensions', len(rr) == 49 and all(len(r) == 50 for r in rr)
          and len(piv) == 46 and [j for j in range(49) if j not in piv] == [27, 33, 42])
    M = [[F(*v) for v in row] for row in square['objective_matrix']]
    alpha, bet = -M[3][3], M[0][3]
    w = bet/alpha
    check('square_and_exact_point', alpha > 0 and alpha*M[0][0]+bet**2 == 0
          and all(M[i][j] == 0 for i in range(4) for j in range(4) if i in [1, 2] or j in [1, 2])
          and w == F(*point['w_star']) == F(*data['w_star']))
    f = [F(0)]*49
    f[42] = w
    for i, j in enumerate(piv):
        f[j] = rr[i][-1]-rr[i][42]*w
    check('all_fixed_point_coordinates', enc(f) == data['free_column']
          and all(x >= 0 for x in f) and [i for i, x in enumerate(f) if not x] == [27, 33])
    old_w = -F(*col['affine']['intercept'][4])/F(*col['affine']['slopes'][4][2])
    check('distinct_immutable_point', w != old_w)
    for i, (row, rhs) in enumerate(zip(col['equations'], col['rhs'])):
        check('original_equation_'+str(i), dot([F(*v) for v in row], f) == F(*rhs))
    entries = {tuple(r['type']): F(*r['y']) for r in old['types']}
    check('complete_old_domain', set(entries) == {(l, m, i, j) for l, m in [(5, 5), (5, 6), (6, 6)]
                                                for i, j in it.product(range(l+1), repeat=2)})
    column, orbit_weights = [], []
    for i, r in enumerate(col['column']):
        value = p[7]*f[r['variable']] if r['kind'] == 'free' else F(*r['value'])
        column.append(value)
        if i == 0:
            check('anchor_entry', r['orbit'] == [0, 0, 0] and value == p[7])
            orbit_weights.append(1)
        else:
            l, s, t = r['orbit']
            entries[l, 7, s, t] = value
            orbit_weights.append(c(7, s)*c(61, l-s)*c(7, t)*c(949, l-t))
    check('complete_column_and_weights', len(column) == 86 and enc(column) == data['column']
          and orbit_weights == col['weights'] and all(x > 0 for x in orbit_weights))
    kernels = [dot([F(*x)*weight for x, weight in zip(v, orbit_weights)], column)
               for v in col['kernel_basis']]
    check('all_49_original_weighted_residuals', len(kernels) == 49 and not any(kernels)
          and enc(kernels) == verified['original_kernel_residuals'])

    free = [(r, q) for r, q in it.product(range(8), repeat=2) if r+q >= 7]
    check('original_variable_order', list(map(list, free)) == data['free'] == original['free'])
    for r, q in it.product(range(8), repeat=2):
        h = r+q
        entries[7, 7, 7-r, 7-q] = (p[7] if h == 0 else F(0) if h <= 4
                                   else entries[h, 7, q, r] if h <= 6 else None)
    presentations, groups, source_groups = [], {}, {}
    types = [(l, m, i, j) for l, m in [(5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (7, 7)]
             for i, j in it.product(range(l+1), repeat=2)]
    check('complete_domain_sizes', len(types) == len(data['records']) == len(verified['records']) == 270)
    for idx, typ in enumerate(types):
        l, m, i, j = typ
        atoms = [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]
        orders = []
        for order, bits in enumerate(it.permutations([4, 2, 1])):
            moved = [0]*8
            for mask, count in enumerate(atoms):
                target = sum(new for new, bit in zip([4, 2, 1], bits) if mask & bit)
                moved[target] = count
            a, b, h = moved[4]+moved[5], moved[4]+moved[6], moved[2]+moved[6]
            val = p[max(a, b, h)] if min(a, b, h) == 0 else F(0) if min(a, b, h) < 5 else entries.get((*sorted([a, b]), moved[4], moved[3]))
            check('presentation_'+str((idx, order)), min(moved) >= 0 and sum(moved) == 1024
                  and all(sum(x for mask, x in enumerate(moved) if mask & bit) == 68 for bit in [1, 2, 4])
                  and (val is None or val == entries[typ]))
            orders.append(moved)
            source_groups.setdefault((*sorted([a, b, h]), moved[4]-moved[3]), set()).add(typ)
        key = tuple(min(orders))
        groups.setdefault(key, []).append(typ)
        record = {'type': typ, 'key': key, 'presentations': orders, 'value': entries[typ]}
        check('full_saved_record_'+str(idx), enc(record) == data['records'][idx] == verified['records'][idx])
        presentations.append(record)
    canonical = {typ: tuple(record['key']) for typ, record in zip(types, presentations)}
    for key, group in source_groups.items():
        check('source_equalities_'+str(key), len({canonical[t] for t in group}) == 1)
    free_keys = [canonical[7, 7, 7-r, 7-q] for r, q in free]
    check('no_free_identifications', len(set(free_keys)) == 36
          and all(len(groups[key]) == 1 for key in free_keys))

    manuscript = (NB/'lemmas/L067-simultaneous-seven-shell-fixed-column-obstruction.md').read_text()
    h = [F(v.strip()) for v in re.search(r'  h=\((.*?)\),', manuscript, re.S).group(1).split(',')]
    k = [F(v.strip()) for v in re.search(r'  k=\((.*?)\)\.', manuscript, re.S).group(1).split(',')]
    dual = [x*y for x in h for y in k]
    selected = [i for i, v in enumerate(dual) if v > 0]
    check('unchanged_dual', enc(dual) == original['exact']['dual'] == square['dual']
          and selected == data['selected_indices'] == [8*a+b for a in range(6) for b in range(4)]
          and all(v >= 0 for v in dual))
    lam = [dual[i] for i in selected]
    check('selected_weights', enc(lam) == data['weights'] == verified['weights'])
    sizes = {l: c(68, l)*c(956, l) for l in [5, 6, 7]}
    modes, A, rhs, rank_cases = [], [], [], {}
    for a, b in it.product(range(8), repeat=2):
        ix = 8*a+b
        layers = [l for l in [6, 5] if max(a, b) <= l]
        d7 = c(68-2*a, 7-a)*c(956-2*b, 7-b)

        def block(l, m):
            l, m = min(l, m), max(l, m)
            return sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*entries[l, m, i, j]
                       for i, j in it.product(range(l+1), repeat=2))-(p[l]*p[m]*sizes[l]*sizes[m] if ix == 0 else 0)

        B = [[block(l, m) for m in layers] for l in layers]
        cross = [block(l, 7) for l in layers]
        saved = data['modes'][ix]
        check('original_old_block_'+str(ix), enc(B) == [list(reversed(row)) for row in reversed(saved['B'])]
              and enc(cross) == list(reversed(saved['cross'])) and d7 == saved['D7'] > 0)
        work, vec, cost, pivots, rank = [row[:] for row in B], cross[:], F(0), [], 0
        ranges = []
        for i in range(len(layers)):
            pivot = work[i][i]
            pivots.append(pivot)
            check('reverse_pivot_'+str((ix, i)), pivot >= 0)
            if pivot == 0:
                residual = [vec[i]]+work[i][i+1:]
                ranges.extend(residual)
                check('reverse_singular_range_'+str((ix, i)), not any(residual))
                continue
            rank += 1
            cost += vec[i]**2/pivot
            for j in range(i+1, len(layers)):
                vec[j] -= work[j][i]*vec[i]/pivot
                for t in range(i+1, len(layers)):
                    work[j][t] -= work[j][i]*work[i][t]/pivot
        rank_cases[str((len(layers), rank))] = rank_cases.get(str((len(layers), rank)), 0)+1
        required = cost/(p[7]*d7)
        fixed = sum(entries[7, 7, 7-r, 7-q]*eigen(68, a, r)*eigen(956, b, q)/p[7]
                    for r, q in it.product(range(8), repeat=2) if r+q <= 6)
        anchor = p[7]*sizes[7] if ix == 0 else F(0)
        bound = fixed-anchor-required
        check('original_mode_scalars_'+str(ix), enc([fixed, anchor, required, bound])
              == [saved['F'], saved['anchor'], saved['required'], saved['rhs']])
        modes.append({'mode': [a, b], 'layers': layers, 'B': B, 'cross': cross,
                      'D7': d7, 'pivots': pivots, 'range_residuals': ranges, 'rank': rank,
                      'cost': cost, 'required': required, 'F': fixed, 'anchor': anchor, 'rhs': bound})
        if ix in selected:
            row = []
            for r, q in free:
                v = c(7, r)*c(61, r)*c(7, q)*c(949, q)
                source_product = F(beta(68, 7, 7, a, 7-r)*beta(956, 7, 7, b, 7-q), d7)
                check('source_scale_'+str((ix, r, q)), v > 0 and source_product == eigen(68, a, r)*eigen(956, b, q))
                row.append(-source_product/v)
            row_index = len(A)
            check('complete_original_scaled_row_'+str(ix), enc(row) == data['matrix'][row_index]
                  == verified['matrix'][row_index] == original['matrix'][ix]
                  and enc(bound) == data['rhs'][row_index] == verified['rhs'][row_index])
            A.append(row)
            rhs.append(bound)
    cancellations = [dot(lam, list(column)) for column in zip(*A)]
    check('full_dual_cancellation_and_zero', len(cancellations) == 36 and not any(cancellations)
          and dot(lam, rhs) == 0 and enc(cancellations) == data['cancellations']
          and data['weighted_rhs'] == [0, 1])
    z = [F(*v) for v in data['certificate']['z']]
    check('complete_signed_witness', len(z) == 36 and data['certificate']['kind'] == 'SOLUTION'
          and enc(z) == verified['z'])
    scaled = [dot(row, z)-bound for row, bound in zip(A, rhs)]
    for i, v in enumerate(scaled):
        check('scaled_substitution_'+str(i), v == 0)
    for (r, q), value in zip(free, z):
        entries[7, 7, 7-r, 7-q] = p[7]*value/(c(7, r)*c(61, r)*c(7, q)*c(949, q))
    raw = []
    for ix in selected:
        a, b = divmod(ix, 8)
        c77 = sum(beta(68, 7, 7, a, i)*beta(956, 7, 7, b, j)*entries[7, 7, i, j]
                  for i, j in it.product(range(8), repeat=2))-(p[7]**2*sizes[7]**2 if ix == 0 else 0)
        residual = c77/(p[7]*modes[ix]['D7'])-modes[ix]['required']
        raw.append(residual)
        check('raw_Y_substitution_'+str(ix), residual == 0)
    check('complete_residual_records', enc(raw) == verified['raw_Y_schur_residuals']
          and enc(scaled) == verified['original_row_residuals'] == data['certificate']['original_row_residuals'])

    augmented = [row+[v] for row, v in zip(A, rhs)]
    L = [[F(*v) for v in row] for row in data['left_row_transform']]
    R = [[F(*v) for v in row] for row in data['rref']]
    check('full_transform_shapes', len(L) == len(R) == 24
          and all(len(row) == 24 for row in L) and all(len(row) == 37 for row in R))
    for i in range(24):
        for j in range(37):
            check('left_transform_identity_'+str((i, j)), dot(L[i], [row[j] for row in augmented]) == R[i][j])
    expected_pivots = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 21, 22, 23, 28, 29]
    check('specified_pivots', expected_pivots == data['pivots'] == verified['rank_pivots'])
    for i, pivot in enumerate(expected_pivots):
        check('rref_leading_and_unit_column_'+str(i), not any(R[i][:pivot]) and R[i][pivot] == 1
              and all(R[j][pivot] == (i == j) for j in range(24)))
    check('zero_augmented_final_row', not any(R[23]))
    reconstructed = [F(0)]*36
    for i, j in enumerate(expected_pivots):
        reconstructed[j] = R[i][-1]
    check('specified_witness_recipe', reconstructed == z)
    coefficient_rank = eliminate(A, reverse=True)
    augmented_rank = eliminate(augmented, reverse=True)
    transform_rank = eliminate(L, reverse=True)
    check('fresh_both_ranks_and_invertible_transform', coefficient_rank['rank'] == augmented_rank['rank'] == 23
          and transform_rank['rank'] == 24 and data['summary']['rank'] == data['summary']['augmented_rank'] == 23
          and data['summary']['nullity'] == 36-23 == 13)
    report = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checks': checks, 'failures': failures, 'w_star': w, 'old_w': old_w,
              'free_column': f, 'column': column, 'orbit_weights': orbit_weights,
              'weighted_kernel_residuals': kernels, 'presentations': presentations,
              'modes': modes, 'matrix': A, 'rhs': rhs, 'weights': lam, 'cancellations': cancellations,
              'weighted_rhs': dot(lam, rhs), 'z': z, 'raw_Y': [entries[7, 7, i, j] for i, j in it.product(range(8), repeat=2)],
              'scaled_residuals': scaled, 'raw_residuals': raw,
              'left_transform': L, 'rref': R, 'coefficient_rank': coefficient_rank,
              'augmented_rank': augmented_rank, 'transform_rank': transform_rank,
              'summary': {'verdict': 'RETAIN L070' if not failures else 'FAILED',
                          'rank': coefficient_rank['rank'], 'augmented_rank': augmented_rank['rank'],
                          'left_transform_rank': transform_rank['rank'], 'nullity': 13,
                          'types': len(types), 'presentations': 6*len(types), 'mode_base_ranks': rank_cases,
                          'scaled_equalities': len(scaled), 'raw_equalities': len(raw),
                          'checks': len(checks), 'failures': len(failures)}}
    OUT.write_text(json.dumps(enc(report), indent=2)+'\n')
    print(report['summary'])
    print('Actual/required: original equalities', sum(v == 0 for v in scaled), '/24; raw equalities', sum(v == 0 for v in raw), '/24; weighted RHS', dot(lam, rhs), '(required 0).')
    print('Failures:', failures)
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

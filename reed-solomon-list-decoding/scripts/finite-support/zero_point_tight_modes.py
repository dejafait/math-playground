"""One equality-only test at L069's point; exact rational certificates."""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'zero-point-tight-modes-results.json'


def enc(x):
    if isinstance(x, Q):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {k: enc(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [enc(v) for v in x]
    return x


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


@lru_cache(None)
def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*C(u, t)*C(n-2*a, u-a)
               * C(n-a-u, l-u)*C(n-a-u, m-u)
               for u in range(max(a, t), min(l, m, n-a)+1))


def eigen(n, a, r):
    return sum((-1)**s*C(a, s)*C(7-a, r-s)*C(n-7-a, r-s)
               for s in range(r+1))


def orders(at):
    result = []
    for perm in it.permutations(range(3)):
        moved = [0]*8
        for mask, size in enumerate(at):
            newmask = sum(((mask >> (2-old)) & 1) << (2-new)
                          for new, old in enumerate(perm))
            moved[newmask] = size
        result.append(tuple(moved))
    return result


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def main():
    names = ['simultaneous-shell-ordinary-scalars-results.json',
             'seven-distance-full-base-kernel-results.json',
             'simultaneous-seven-shell-results.json',
             'seven-shell-affine-fixed-dual-results.json',
             'zero-dual-plane-scalars-results.json']
    paths = [ROOT/n for n in names]
    old, col, original, square, point = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in paths}, 'checks': checks, 'failures': failures}

    def save(stage):
        out['stage'] = stage
        OUT.write_text(json.dumps(enc(out), indent=2)+'\n')

    for i, d in enumerate([old, col, original, square, point]):
        check(f'input_clean_{i}', not d['failures'])
        for path, digest in d.get('input_hashes', d.get('source_hashes', {})).items():
            check(f'input_hash_{i}_{path}', hashlib.sha256((NB/path).read_bytes()).hexdigest() == digest)
    pairs = [Q(*v) for v in point['pairs_through_13']]
    rho = (Q(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    p7 = pairs[7]
    check('original_normalizations', rho > 0 and rho == Q(*old['rho']) == Q(*point['rho'])
          and p7 == Q(3539, 248922676958508)
          and pairs[:13] == [Q(*v) for v in old['pairs_through_12']])
    R = [[Q(*v) for v in row] for row in col['equation_rref']]
    piv = col['equation_pivots']
    nonpiv = [j for j in range(49) if j not in piv]
    check('affine_dimensions', len(R) == 49 and len(piv) == 46
          and nonpiv == [27, 33, 42] and all(len(r) == 50 for r in R))
    fs = [[Q(0)]*4 for _ in range(49)]
    for k, j in enumerate(nonpiv):
        fs[j][k+1] = Q(1)
    for i, j in enumerate(piv):
        check(f'rref_pivot_{i}', all(R[i][k] == (k == j) for k in piv))
        fs[j] = [R[i][-1]]+[-R[i][k] for k in nonpiv]
    check('rref_zero_rows', all(not any(row) for row in R[len(piv):]))
    check('same_affine_family', enc([x[0] for x in fs]) == col['affine']['intercept']
          and enc([x[1:] for x in fs]) == col['affine']['slopes'])
    for i, (row, rhs) in enumerate(zip(col['equations'], col['rhs'])):
        check(f'original_affine_equation_{i}',
              [dot([Q(*x) for x in row], [f[k] for f in fs]) for k in range(4)]
              == [Q(*rhs), Q(0), Q(0), Q(0)])
    M = [[Q(*x) for x in row] for row in square['objective_matrix']]
    alpha, bet = -M[3][3], M[0][3]
    check('square_identity', alpha > 0 and alpha*M[0][0]+bet**2 == 0
          and all(M[i][j] == 0 for i in range(4) for j in range(4) if i in [1, 2] or j in [1, 2]))
    w = bet/alpha
    parameter = [Q(1), Q(0), Q(0), w]
    check('same_point', w == Q(*point['w_star']))
    f = [dot(x, parameter) for x in fs]
    check('column_signs', [j for j, v in enumerate(f) if not v] == [27, 33]
          and all(v >= 0 for v in f))
    base = {tuple(row['type']): Q(*row['y']) for row in old['types']}
    column = []
    for row in col['column']:
        value = p7*f[row['variable']] if row['kind'] == 'free' else Q(*row['value'])
        column.append(value)
        if row['orbit'] != [0, 0, 0]:
            l, i, j = row['orbit']
            base[l, 7, i, j] = value
    for j, (row, rhs) in enumerate(zip(col['equations'], col['rhs'])):
        check(f'point_kernel_equation_{j}', dot([Q(*x) for x in row], f) == Q(*rhs))

    # Check every unordered presentation before selecting spectral rows.
    dictionary, records, free = {}, [], []
    for typ, value in base.items():
        l, m, i, j = typ
        at = (956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i)
        key = min(orders(at))
        check(f'base_key_{typ}', key not in dictionary or dictionary[key] == value)
        dictionary[key] = value
    for l, m in [(5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (7, 7)]:
        for i, j in it.product(range(l+1), repeat=2):
            typ = (l, m, i, j)
            at = (956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i)
            oo = orders(at)
            key, assigned = min(oo), []
            for aa in oo:
                ab, ac, bc = aa[4]+aa[5], aa[4]+aa[6], aa[2]+aa[6]
                check(f'valid_atoms_{len(checks)}', min(aa) >= 0 and sum(aa) == 1024
                      and all(sum(v for k, v in enumerate(aa) if k & bit) == 68 for bit in [1, 2, 4]))
                value = None
                if 0 in [ab, ac, bc]:
                    value = pairs[max(ab, ac, bc)]
                elif any(1 <= h <= 4 for h in [ab, ac, bc]):
                    value = Q(0)
                else:
                    value = base.get((*sorted([ab, ac]), aa[4], aa[3]))
                if value is not None:
                    assigned.append(value)
            if key in dictionary:
                assigned.append(dictionary[key])
            check(f'consistent_{typ}', len(set(assigned)) <= 1)
            if assigned:
                value = assigned[0]
                base[typ] = dictionary[key] = value
            else:
                value = None
                check(f'only_free77_{typ}', l == m == 7)
                free.append((7-i, 7-j))
            saved = square['records'][len(records)]
            check(f'unchanged_affine_lookup_{typ}', list(typ) == saved['type']
                  and (value is None and saved['affine'] is None or value is not None
                       and value == dot([Q(*x) for x in saved['affine']], parameter)))
            records.append({'type': typ, 'key': key, 'presentations': oo, 'value': value})
    free.sort()
    check('36_original_variables', free == [(r, q) for r in range(8) for q in range(8) if r+q >= 7])
    for r in range(8):
        for q in range(8-r):
            if r+q <= 6:
                expect = p7 if r+q == 0 else Q(0) if r+q <= 4 else base[r+q, 7, q, r]
                check(f'forced77_{r}_{q}', base[7, 7, 7-r, 7-q] == expect)
    out.update({'rho': rho, 'p7': p7, 'w_star': w, 'free_column': f,
                'column': column, 'records': records, 'free': free})
    save('entries_checked')
    if failures:
        raise RuntimeError(f'Entry checks failed: {failures}')

    h = [Q(1), Q(20435, 441), Q(13481000, 13671), Q(2688040, 217),
         Q(1307664259, 13671), Q(5294968393, 13671), Q(0), Q(0)]
    k = [Q(49, 100880416043264), Q(7665, 38718903137024),
         Q(17301, 551968803584), Q(5461349, 2754064239872)]+[Q(0)]*4
    weights = [x*y for x, y in it.product(h, k)]
    check('unchanged_weights', enc(weights) == original['exact']['dual'] == square['dual'])
    sizes = {l: C(68, l)*C(956, l) for l in [5, 6, 7]}
    modes, A, rhs = [], [], []
    for a, b in it.product(range(8), repeat=2):
        index = 8*a+b
        layers = [l for l in [5, 6] if max(a, b) <= l]
        d7 = C(68-2*a, 7-a)*C(956-2*b, 7-b)

        def block(l, m):
            value = sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*base[l, m, i, j]
                        for i, j in it.product(range(l+1), repeat=2))
            return value-pairs[l]*pairs[m]*sizes[l]*sizes[m] if a == b == 0 else value

        B = [[block(min(l, m), max(l, m)) for m in layers] for l in layers]
        cross = [block(l, 7) for l in layers]
        cost, residuals, pivots = Q(0), [], []
        if len(layers) == 2:
            x, t, z = B[0][0], B[0][1], B[1][1]
            u, v = cross
            pivots.append(x)
            if x > 0:
                cost += u*u/x
                z, v = z-t*t/x, v-t*u/x
            else:
                residuals.extend([t, u])
        elif layers:
            z, v = B[0][0], cross[0]
        else:
            z, v = Q(0), Q(0)
        pivots.append(z)
        check(f'old_psd_{a}_{b}', all(x >= 0 for x in pivots))
        if z > 0:
            cost += v*v/z
        else:
            residuals.append(v)
        check(f'singular_range_{a}_{b}', not any(residuals))
        required = cost/(p7*d7)
        fixed = sum(base[7, 7, 7-r, 7-q]*eigen(68, a, r)*eigen(956, b, q)/p7
                    for r in range(8) for q in range(8) if r+q <= 6)
        anchor = p7*sizes[7] if a == b == 0 else Q(0)
        row = [-Q(eigen(68, a, r)*eigen(956, b, q),
                  C(7, r)*C(61, r)*C(7, q)*C(949, q)) for r, q in free]
        bound = fixed-anchor-required
        saved = square['modes'][index]
        check(f'affine_mode_import_{a}_{b}', enc(B) == saved['B']
              and cross == [dot([Q(*x) for x in v], parameter) for v in saved['cross']]
              and required == dot(parameter, [dot([Q(*x) for x in row], parameter)
                                               for row in saved['required_quadratic']])
              and fixed-anchor == dot([Q(*x) for x in saved['fixed_minus_anchor_affine']], parameter))
        modes.append({'mode': [a, b], 'layers': layers, 'B': B, 'cross': cross,
                      'D7': d7, 'pivots': pivots, 'range_residuals': residuals,
                      'F': fixed, 'anchor': anchor, 'required': required, 'rhs': bound})
        if weights[index] > 0:
            A.append(row)
            rhs.append(bound)
    selected = [i for i, value in enumerate(weights) if value > 0]
    selected_weights = [weights[i] for i in selected]
    cancellations = [dot(selected_weights, [row[j] for row in A]) for j in range(36)]
    weighted_rhs = dot(selected_weights, rhs)
    check('24_positive_modes', selected == [8*a+b for a in range(6) for b in range(4)])
    check('36_exact_cancellations', not any(cancellations))
    check('exact_weighted_zero', weighted_rhs == 0)
    out.update({'modes': modes, 'selected_indices': selected, 'weights': selected_weights,
                'matrix': A, 'rhs': rhs, 'cancellations': cancellations, 'weighted_rhs': weighted_rhs})
    save('system_saved')
    print(f'Original entries: 270 types/1620 presentations; all 64 ranges; 24 rows/36 signed variables; weighted RHS={weighted_rhs}; cancellations={sum(x == 0 for x in cancellations)}/36; failures={failures}', flush=True)
    if failures:
        raise RuntimeError('Pre-elimination checks failed')

    # Exact Gauss-Jordan, carrying full left row multipliers.
    augmented = [row+[bound] for row, bound in zip(A, rhs)]
    left = [[Q(i == j) for j in range(24)] for i in range(24)]
    pivots, r = [], 0
    for j in range(36):
        chosen = next((i for i in range(r, 24) if augmented[i][j]), None)
        if chosen is None:
            continue
        for mat in [augmented, left]:
            mat[r], mat[chosen] = mat[chosen], mat[r]
        scale = augmented[r][j]
        augmented[r] = [x/scale for x in augmented[r]]
        left[r] = [x/scale for x in left[r]]
        for i in range(24):
            if i != r and augmented[i][j]:
                scale = augmented[i][j]
                augmented[i] = [x-scale*y for x, y in zip(augmented[i], augmented[r])]
                left[i] = [x-scale*y for x, y in zip(left[i], left[r])]
        pivots.append(j)
        r += 1
        if r == 24:
            break
    for i in range(24):
        check(f'full_row_identity_{i}', [dot(left[i], [A[t][j] for t in range(24)]) for j in range(36)]
              + [dot(left[i], rhs)] == augmented[i])
    contradiction = next((i for i in range(r, 24) if augmented[i][-1]), None)
    if contradiction is not None:
        ell = [x/augmented[contradiction][-1] for x in left[contradiction]]
        residuals = [dot(ell, [row[j] for row in A]) for j in range(36)]
        value = dot(ell, rhs)
        check('left_null_contradiction', not any(residuals) and value == 1)
        certificate = {'kind': 'LEFT_NULL', 'left': ell, 'column_residuals': residuals, 'rhs_pairing': value}
        verdict = 'INCONSISTENT'
    else:
        z = [Q(0)]*36
        for i, j in enumerate(pivots):
            z[j] = augmented[i][-1]
        residuals = [dot(row, z)-bound for row, bound in zip(A, rhs)]
        check('substituted_solution', not any(residuals))
        certificate = {'kind': 'SOLUTION', 'z': z, 'original_row_residuals': residuals}
        verdict = 'CONSISTENT'
    out.update({'rref': augmented, 'left_row_transform': left, 'pivots': pivots,
                'certificate': certificate,
                'summary': {'verdict': verdict, 'rank': r, 'augmented_rank': r+(contradiction is not None),
                            'equations': 24, 'variables': 36, 'nullity': 36-r,
                            'checks': len(checks), 'failures': len(failures),
                            'weighted_rhs_zero': weighted_rhs == 0,
                            'certificate_valid': not any(residuals)}})
    save('completed')
    print(f'Equality verdict={verdict}; ranks={r}/{r+(contradiction is not None)}; exact certificate={certificate["kind"]}; residuals zero={not any(residuals)}; checks={len(checks)}; failures={failures}')
    print('Threshold: 24/24 original equalities required; certificate:', OUT.relative_to(NB))


if __name__ == '__main__':
    main()

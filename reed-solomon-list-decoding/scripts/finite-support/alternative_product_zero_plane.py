"""L071's unchanged product pairing on L069's complete scalar plane.

Exact rational certificates only. A cached affine decomposition is checked
against fresh source sums before the two-variable optimization is attempted.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

from verify_seven_shell_affine_fixed_dual import C, beta, eigen, region_order

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'alternative-product-zero-plane-results.json'


def enc(x):
    if isinstance(x, Q):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {k: enc(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [enc(v) for v in x]
    return x


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), Q(0))


def interval(x, d=10**6):
    k = x.numerator*d//x.denominator
    return [str(Q(k, d)), str(Q(k+1, d))]


def main():
    names = ['seven-shell-affine-fixed-dual-results.json',
             'zero-dual-plane-scalars-results.json',
             'zero-point-remaining-modes-results.json',
             'seven-distance-full-base-kernel-results.json',
             'simultaneous-shell-ordinary-scalars-results.json']
    paths = [ROOT/n for n in names]
    family, scalar, fixed, col, old = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in paths}, 'checks': checks, 'failures': failures}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        out['stage'] = stage
        OUT.write_text(json.dumps(enc(out), indent=2)+'\n')

    for k, data in enumerate([family, scalar, fixed, col, old]):
        check(f'clean_input_{k}', not data['failures'])
        for path, digest in data.get('input_hashes', data.get('source_hashes', {})).items():
            check(f'input_hash_{k}_{path}', hashlib.sha256((NB/path).read_bytes()).hexdigest() == digest)
    p = [Q(*x) for x in scalar['pairs_through_13']]
    rho, wstar = Q(*scalar['rho']), Q(*scalar['w_star'])
    check('positive_original_scaling', rho > 0 and p[7] == Q(3539, 248922676958508) > 0
          and scalar['w_star'] == fixed['w_star'])
    fs = [[Q(*c)]+[Q(*v) for v in a] for c, a in zip(col['affine']['intercept'], col['affine']['slopes'])]
    check('original_rref_coordinates', col['affine']['free_indices'] == [27, 33, 42])
    for i, (row, rhs) in enumerate(zip(col['equations'], col['rhs'])):
        check(f'original_affine_kernel_{i}',
              [sum(Q(*e)*f[k] for e, f in zip(row, fs)) for k in range(4)] == [Q(*rhs), 0, 0, 0])
    plane = [[f[0]+wstar*f[3], f[1], f[2]] for f in fs]
    check('complete_nonnegative_plane', enc(plane) == scalar['plane_free'])
    base = {tuple(r['type']): [Q(*r['y']), Q(0), Q(0), Q(0)] for r in old['types']}
    for row in col['column'][1:]:
        l, i, j = row['orbit']
        base[l, 7, i, j] = [p[7]*x for x in fs[row['variable']]] if row['kind'] == 'free' else [Q(*row['value']), Q(0), Q(0), Q(0)]
    keys, records = {}, []
    D = set(range(68))
    for row in family['records']:
        l, m, i, j = typ = tuple(row['type'])
        E = (D-(set(range(i))|set(range(m, m+l-i))))|set(range(68, 68+j))|set(range(68+m, 68+m+l-j))
        G = (D-set(range(m)))|set(range(68, 68+m))
        actual = [region_order(s) for s in it.permutations([D, E, G])]
        check(f'actual_regions_{typ}', len(E) == len(G) == 68 and list(min(actual)) == row['key']
              and [list(a) for a in actual] == [r['atoms'] for r in row['presentations']])
        assigned = []
        for aa in actual:
            ab, ac, bc = aa[4]+aa[5], aa[4]+aa[6], aa[2]+aa[6]
            value = None
            if 0 in [ab, ac, bc]:
                value = [p[max(ab, ac, bc)], Q(0), Q(0), Q(0)]
            elif any(1 <= h <= 4 for h in [ab, ac, bc]):
                value = [Q(0)]*4
            elif (*sorted([ab, ac]), aa[4], aa[3]) in base:
                value = base[*sorted([ab, ac]), aa[4], aa[3]]
            if value is not None:
                assigned.append(value)
        value = assigned[0] if assigned else None
        key = min(actual)
        check(f'complete_unordered_affine_{typ}', all(v == value for v in assigned)
              and (key not in keys or keys[key] == value) and enc(value) == row['affine'])
        keys[key] = value
        if value is not None:
            base[typ] = value
        records.append({'type': typ, 'regions': actual, 'affine': value})
    free = [(r, q) for r in range(8) for q in range(8) if r+q >= 7]
    check('36_free_and_28_forced', family['free_new'] == [list(t) for t in free]
          and sum(t[:2] == (7, 7) for t in base) == 28 and len(base) == 234)
    h = [Q(1), Q(12261, 455), Q(15555, 56), Q(4099261, 3640)]+[Q(0)]*4
    k = [Q(1), Q(4531475, 6657), Q(136607358056, 632415), Q(27321109096, 665),
         Q(1028453048809043, 210805), Q(9295091464315239, 30115), Q(0), Q(0)]
    weights = [a*b for a, b in it.product(h, k)]
    check('unchanged_L071_weights', enc(weights) == fixed['certificate']['mode_weights']
          and min(weights) >= 0 and sum(x > 0 for x in weights) == 24)
    S = {l: C(68, l)*C(956, l) for l in [5, 6, 7]}
    M = [[Q(0)]*4 for _ in range(4)]
    modes = []
    for ix, (a, b) in enumerate(it.product(range(8), repeat=2)):
        layers = [l for l in [5, 6] if max(a, b) <= l]
        d7 = C(68-2*a, 7-a)*C(956-2*b, 7-b)

        def block(l, m):
            l, m = min(l, m), max(l, m)
            v = [sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*base[l, m, i, j][z]
                     for i, j in it.product(range(l+1), repeat=2)) for z in range(4)]
            if a == b == 0:
                v[0] -= p[l]*p[m]*S[l]*S[m]
            return v

        B = [[block(l, m)[0] for m in layers] for l in layers]
        cross = [block(l, 7) for l in layers]
        saved = family['modes'][ix]
        check(f'original_block_and_cross_{ix}', enc(B) == saved['B'] and enc(cross) == saved['cross'] and d7 == saved['D7'])
        cost, ranges = [[Q(0)]*4 for _ in range(4)], []
        if len(B) == 2:
            x, y, z = B[0][0], B[0][1], B[1][1]
            det = x*z-y*y
            t, s = cross
            check(f'old_PSD_{ix}', x >= 0 and z >= 0 and det >= 0)
            if det > 0:
                cost = [[(z*t[i]*t[j]-y*(t[i]*s[j]+s[i]*t[j])+x*s[i]*s[j])/det for j in range(4)] for i in range(4)]
            elif x > 0:
                ranges = [[x*v-y*u for u, v in zip(t, s)]]
                cost = [[t[i]*t[j]/x for j in range(4)] for i in range(4)]
            elif z > 0:
                ranges = [t]
                cost = [[s[i]*s[j]/z for j in range(4)] for i in range(4)]
            else:
                ranges = cross
        elif B:
            x, t = B[0][0], cross[0]
            check(f'old_PSD_{ix}', x >= 0)
            if x > 0:
                cost = [[t[i]*t[j]/x for j in range(4)] for i in range(4)]
            else:
                ranges = cross
        check(f'whole_affine_singular_range_{ix}', all(not any(r) for r in ranges))
        cost = [[v/(p[7]*d7) for v in row] for row in cost]
        F = [sum(base[7, 7, 7-r, 7-q][j]*eigen(68, a, r)*eigen(956, b, q)/p[7]
                 for r in range(8) for q in range(8) if r+q <= 6) for j in range(4)]
        anchor = p[7]*S[7] if ix == 0 else Q(0)
        F[0] -= anchor
        check(f'original_full_cost_and_fixed_{ix}', enc(cost) == saved['required_quadratic'] and enc(F) == saved['fixed_minus_anchor_affine'])
        for i, j in it.product(range(4), repeat=2):
            M[i][j] -= weights[ix]*cost[i][j]
        M[0][0] += weights[ix]*F[0]
        for j in range(1, 4):
            M[0][j] += weights[ix]*F[j]/2
            M[j][0] += weights[ix]*F[j]/2
        modes.append({'mode': [a, b], 'B': B, 'cross': cross, 'D7': d7,
                      'range_residuals': ranges, 'cost': cost, 'fixed_minus_anchor': F})
    cancel, raw_cancel = [], []
    for r, q in free:
        cancel.append(sum(weights[8*a+b]*eigen(68, a, r)*eigen(956, b, q)
                          for a, b in it.product(range(8), repeat=2)))
        raw_cancel.append(sum(weights[8*a+b]*Q(beta(68, 7, 7, a, 7-r)*beta(956, 7, 7, b, 7-q),
                                  p[7]*C(68-2*a, 7-a)*C(956-2*b, 7-b))
                              for a, b in it.product(range(8), repeat=2)))
    check('all_original_and_raw_cancellations', not any(cancel+raw_cancel))
    T = [[Q(1), 0, 0], [0, Q(1), 0], [0, 0, Q(1)], [wstar, 0, 0]]
    N = [[sum(T[a][i]*M[a][b]*T[b][j] for a, b in it.product(range(4), repeat=2))
          for j in range(3)] for i in range(3)]
    check('original_fixed_point_pairing', N[0][0] == Q(*fixed['certificate']['rhs_pairing']))
    out.update({'rho': rho, 'p7': p[7], 'w_star': wstar, 'weights': weights,
                'records': records, 'modes': modes, 'free': free, 'scaled_cancellations': cancel,
                'raw_cancellations': raw_cancel, 'objective_matrix': M, 'plane_matrix': N,
                'plane_nonnegativity': plane, 'scalar_rows': scalar['inequalities']})
    save('exact_quadratic_reconstructed')
    A, B, D2 = -N[1][1], -N[1][2], -N[2][2]
    det = A*D2-B*B
    check('plane_concavity', A >= 0 and D2 >= 0 and det >= 0)
    check('u_flat_and_v_strict', A == B == N[0][1] == 0 and D2 > 0)
    if not failures:
        g1, g2 = N[0][1], N[0][2]
        u, v = Q(0), g2/D2
        point = [Q(1), u, v]
        value = dot(point, [dot(row, point) for row in N])
        check('stationarity_and_square', N[0][1] == 0 and D2*v == g2
              and value == N[0][0]+g2*v)
        nonneg = [dot(f, point) for f in plane]
        scalar_slacks = [dot([Q(*x) for x in r['affine']], point) for r in scalar['inequalities']]
        out['stationary'] = {'parameters': [u, v, wstar], 'value': value,
                             'value_interval': interval(value), 'nonnegative_slacks': nonneg,
                             'scalar_slacks': scalar_slacks,
                             'violating_nonnegative': [j for j, x in enumerate(nonneg) if x < 0],
                             'violating_scalar': [j for j, x in enumerate(scalar_slacks) if x < 0]}
        check('attained_positive_maximum', value > 0 and g2 > 0 and min(nonneg+scalar_slacks) >= 0)
        out['square_certificate'] = {'alpha': D2, 'beta': g2, 'maximum': value,
                                     'v_star': v, 'u_independent': True}
        print('Unconstrained maximum interval:', interval(value), '; admissible:', min(nonneg+scalar_slacks) >= 0, flush=True)
    out['summary'] = {'checks': len(checks), 'failures': len(failures),
                      'strict_concavity': A > 0 and det > 0,
                      'rank_one_concavity': A == B == 0 and D2 > 0,
                      'verdict': 'ADMISSIBLE_POSITIVE_MAXIMUM' if not failures else 'CHECK_FAILED',
                      'required_sign': '<0 at every admissible point',
                      'stage': 'completed'}
    save('completed')
    print('Checks:', len(checks), '; failures:', failures, '; certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

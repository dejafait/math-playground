"""Exact frozen L076 column energy; retain the full anchor and actual weights.

No optimization. Complete staged certificates include the original action,
fixed column, modal inverse and every lifted residual/energy term. The
original direct selected solve remains available as an optional method.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from math import comb, gcd, lcm
from pathlib import Path
from seven_distance_fixed_column_energy import solve

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'eight-distance-fixed-column-energy-results.json'
LAYERS = [5, 6, 7]


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


def primitive(row):
    d = lcm(*(F(x).denominator for x in row))
    a = [int(x*d) for x in row]
    g = gcd(*a)
    return [x//g for x in a] if g else a


def column_pivots(matrix, prime=2147483647):
    rows = [[v % prime for v in primitive(row)] for row in matrix]
    pivots = []
    for j in range(len(rows[0])):
        r = len(pivots)
        s = next((s for s in range(r, len(rows)) if rows[s][j]), None)
        if s is None:
            continue
        rows[r], rows[s] = rows[s], rows[r]
        inv = pow(rows[r][j], -1, prime)
        rows[r] = [x*inv % prime for x in rows[r]]
        for s in range(r+1, len(rows)):
            v = rows[s][j]
            if v:
                rows[s] = [(x-v*y) % prime for x, y in zip(rows[s], rows[r])]
        pivots.append(j)
    return pivots


def main():
    names = ['eight-distance-full-base-kernel-results.json',
             'eight-distance-full-base-kernel-verification.json',
             'eight-distance-full-base-kernel-critical-audit.json',
             'maximizer-excluded-anchor-results.json',
             'maximizer-excluded-anchor-critical-audit.json',
             'maximizer-completion-verification.json',
             'maximizer-seven-seven-scalars-results.json']
    paths = [ROOT/n for n in names]
    data, ver, audit, src, old, included, scalar = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in paths}}

    def save(stage):
        out.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(out), indent=2)+'\n')

    for path, obj in zip(paths, [data, ver, audit, src, old, included, scalar]):
        check('clean_'+path.name, obj['failures'] == [])
        for rel, digest in obj.get('input_hashes', obj.get('source_hashes', {})).items():
            check('immutable_'+path.name+'_'+rel,
                  hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p = [F(*x) for x in src['pairs_through_14']]
    rho = F(*src['rho'])
    check('original_normalization', rho > 0 and rho == F(*data['rho'])
          and p[8] == F(16792471, 1181138102168120460) > 0
          and src['pairs_through_14'] == data['pairs_through_14'])
    check('unchanged_upstream_parameters_column_completion',
          src['parameters'] == old['parameters'] == scalar['parameters']
          and src['original_column'] == old['column'] == scalar['original_RREF_column']
          and src['completion_z'] == old['z'] == scalar['same_original_basis_z'])
    base = {tuple(r['type']): F(*r['y']) for r in src['entries']}
    check('all_270_immutable_base_types', len(base) == 270
          and base == {tuple(r['type']): F(*r['y']) for r in old['entries']}
          == {tuple(r['type']): F(*r['y']) for r in scalar['all_records']})
    out.update(rho=rho, pairs=p, base_entries=[{'type': k, 'value': v} for k, v in base.items()])
    for l, m, k, h in list(base):
        base[m, l, k, h] = base[l, m, k, h]
    orbits = [(0, 0, 0)]+[(l, i, j) for l in LAYERS for i, j in it.product(range(l+1), repeat=2)]
    W = [1]+[c(8, i)*c(60, l-i)*c(8, j)*c(948, l-j) for l, i, j in orbits[1:]]
    check('complete_actual_orbits_and_weights', list(map(list, orbits)) == data['orbits']
          and W == data['weights'] and min(W) > 0)
    for l in LAYERS:
        check('weight_sum_'+str(l), sum(w for o, w in zip(orbits, W) if o[0] == l) == c(68, l)*c(956, l))
    affine = data['affine']
    intercept = [F(*v) for v in affine['intercept']]
    slopes = [[F(*v) for v in row] for row in affine['slopes']]
    active = [27, 33, 56, 63]
    params, _, _ = solve([slopes[j] for j in active], [-intercept[j] for j in active])
    sol = [x+sum(a*t for a, t in zip(row, params)) for x, row in zip(intercept, slopes)]
    check('fixed_active_column', active == data['active_zero_indices']
          and enc(params) == data['chosen_parameters'] == ver['fresh_active_parameters']
          and enc(sol) == data['solution'] == ver['full_rational_solution'] == audit['solution']
          and [j for j, x in enumerate(sol) if not x] == active and min(sol) == 0)
    b = [p[8]*sol[r['variable']] if r['kind'] == 'free' else F(*r['value']) for r in data['column']]
    check('all_fixed_column_entries', len(b) == 150 and b[0] == p[8] and min(b) >= 0
          and enc(b) == data['complete_column'] == ver['complete_column'])
    K = [[F(*v) for v in row] for row in data['kernel_basis']]
    kres = [sum(w*x*y for w, x, y in zip(W, v, b)) for v in K]
    check('all_90_full_kernel_residuals', len(kres) == 90 and not any(kres)
          and enc(kres) == audit['original_weighted_residuals'])
    T = {(n, l, m, k): [[sum(c(i, s)*c(8-i, u-s)*c(l-i, k-s)*c(n-8-l+i, m-u-k+s)
          for s in range(9)) for u in range(m+1)] for i in range(l+1)]
         for n in [68, 956] for l, m in it.product(LAYERS, repeat=2) for k in range(min(l, m)+1)}
    check('all_118_transition_arrays', T == {tuple(r['indices']): r['matrix'] for r in data['complete_transitions']})
    Q = [[F(0) for _ in orbits] for _ in orbits]
    index = {o: a for a, o in enumerate(orbits)}
    Q[0][0] = F(1)
    for a, (l, i, j) in enumerate(orbits[1:], 1):
        Q[0][a], Q[a][0] = p[l]*W[a], p[l]
    for l, m in it.product(LAYERS, repeat=2):
        d = lcm(*(base[l, m, k, h].denominator for k, h in it.product(range(min(l, m)+1), repeat=2)))
        Y = [[int(base[l, m, k, h]*d) for h in range(min(l, m)+1)] for k in range(min(l, m)+1)]
        for i, u in it.product(range(l+1), range(m+1)):
            partial = [sum(T[68, l, m, k][i][u]*Y[k][h] for k in range(min(l, m)+1)) for h in range(min(l, m)+1)]
            for j, v in it.product(range(l+1), range(m+1)):
                Q[index[l, i, j]][index[m, u, v]] = F(sum(partial[h]*T[956, l, m, h][j][v] for h in range(min(l, m)+1)), d)
    for a, row in enumerate(Q):
        check('whole_original_action_'+str(a), enc(row) == audit['direct_orbit_action'][a])
        check('weighted_symmetry_'+str(a), all(W[a]*x == W[j]*Q[j][a] for j, x in enumerate(row)))
    selected = column_pivots(Q)
    check('selected_60_columns', len(selected) == 60 and data['rank'] == 60)
    out.update(orbits=orbits, weights=W, action=Q, parameters=params, free_solution=sol,
               column=b, selected=selected, kernel_residuals=kres)
    save('full_inputs_before_exact_solve')
    print('Rebuilt full 150-coordinate action; rank lower bound', len(selected), '. Checking exact inverse.', flush=True)
    if failures:
        raise SystemExit('Input reconstruction failures; inspect certificate.')
    if '--prepare-only' in sys.argv:
        print('Complete fixed inputs saved; no inverse or energy verdict attempted.')
        return
    if '--direct' in sys.argv:
        zz, echelon, operations = solve([[Q[a][j] for j in selected] for a in selected], [b[a] for a in selected])
        z = [F(0)]*150
        for a, x in zip(selected, zz):
            z[a] = x
        out.update(solve_method='direct_selected', selected_echelon=echelon, solve_operations=operations)
    else:
        mode_path = ROOT/'eight-distance-modal-inverse-results.json'
        mode = json.loads(mode_path.read_text())
        z = [F(*v) for v in mode['inverse_action']]
        check('complete_modal_proposal', len(z) == 150 and not mode['failures'])
        out.update(solve_method='modal_range_inverse', modal_evidence=mode['modes'],
                   modal_certificate_sha256=hashlib.sha256(mode_path.read_bytes()).hexdigest())
    # Clear vector and row denominators separately; this avoids intermediate
    # Fraction denominator growth while retaining every original equation.
    zd = lcm(*(x.denominator for x in z))
    zi = [int(x*zd) for x in z]
    products = []
    for row in Q:
        d = lcm(*(x.denominator for x in row))
        products.append(F(sum(int(x*d)*y for x, y in zip(row, zi)), d*zd))
    residuals = [x-bb for x, bb in zip(products, b)]
    for a, x in enumerate(residuals):
        check('all_original_inverse_rows_'+str(a), x == 0)
    terms = [w*bb*x for w, bb, x in zip(W, b, z)]
    energy = sum(terms)
    bilinear = sum(w*x*y for w, x, y in zip(W, z, products))
    check('bilinear_identity_and_nonnegative_energy', energy == bilinear and energy >= 0)
    ratio, remainder = energy/p[8], p[8]-energy
    unit = 10**12
    lo = F(ratio.numerator*unit//ratio.denominator, unit)
    hi = lo+F(1, unit)
    check('integer_exact_ratio_interval', lo <= ratio < hi)
    verdict = 'PSD_EXTENSION' if remainder >= 0 else 'FIXED_COLUMN_REJECTED'
    out.update(inverse_action=z,
               inverse_residuals=residuals, weighted_energy_contributions=terms,
               bilinear_energy=bilinear, energy=energy, energy_ratio=ratio,
               required_diagonal=p[8], schur_remainder=remainder,
               summary={'checks': len(checks), 'failures': len(failures), 'verdict': verdict,
                        'action_rank': 60, 'all_150_inverse_residuals_zero': not any(residuals),
                        'all_90_kernel_residuals_zero': not any(kres),
                        'ratio_interval': [lo, hi], 'required_ratio_upper_bound': 1,
                        'energy_nonnegative': energy >= 0, 'remainder_nonnegative': remainder >= 0})
    save('completed')
    print('Exact checks:', len(checks), '; failures:', failures)
    print('Energy/p8 in [', lo, ',', hi, '); required <= 1; verdict:', verdict)
    print('All 150 original inverse residuals zero:', not any(residuals))
    print('Full certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

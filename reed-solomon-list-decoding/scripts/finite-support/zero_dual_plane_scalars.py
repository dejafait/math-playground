"""One exact scalar-feasibility test on L068's zero plane.

Full presentations, affine rows and rational witness are saved. No PSD
completion or pair retuning is performed. Imports no notebook mathematics.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'zero-dual-plane-scalars-results.json'


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {k: enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def orders(at):
    ans = []
    for order in it.permutations(range(3)):
        aa = [0]*8
        for mask, size in enumerate(at):
            new = sum(4 >> k for k, j in enumerate(order) if mask & (4 >> j))
            aa[new] = size
        ans.append(aa)
    return ans


def atoms(l, m, i, j):
    return [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]


def main():
    names = ['delsarte-lp-results.json', 'simultaneous-shell-ordinary-scalars-results.json',
             'seven-distance-full-base-kernel-results.json', 'seven-shell-affine-fixed-dual-results.json']
    paths = [ROOT/n for n in names]
    lp, old, col, zero = [json.loads(p.read_text()) for p in paths]
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

    check('inputs_without_failures', all(not d['failures'] for d in [lp, old, col, zero]))
    primal = [F(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    check('L021_domain', lp['active_distances'] == list(range(5, 69)) and len(primal) == 64)
    for j in range(1, 65):
        val = sum(F(sum((-1)**h*choose(j, h)*choose(68-j, i-h)*choose(956-j, i-h)
                        for h in range(i+1)), choose(68, i)*choose(956, i))*x
                  for i, x in zip(range(5, 69), primal))
        check(f'L021_equation_{j}', val == -1)
    pairs = [F(1)]+[F(0)]*4+[x/(2*choose(68, i)*choose(956, i))
                            for i, x in zip(range(5, 69), primal)]
    check('original_a13', primal[8] == F(808753696404081487284494974858496, 11))
    check('old_pairs_unchanged', pairs[:13] == [F(*x) for x in old['pairs_through_12']])
    check('p7', pairs[7] == F(3539, 248922676958508) > 0)
    check('pairs_through_13_bounded', all(0 <= x <= pairs[5] for x in pairs[1:14]))
    N = comb(1024, 68)
    M = (F(comb(1024, 64), comb(68, 64))+1)/2
    rho = M/N
    check('rho', rho == F(*old['rho']) > 0)
    matrix = [[F(*x) for x in row] for row in zero['objective_matrix']]
    alpha, beta = -matrix[3][3], matrix[0][3]
    check('rank_one_square', alpha > 0 and alpha*matrix[0][0]+beta**2 == 0
          and all(matrix[i][j] == 0 for i in [1, 2] for j in range(4))
          and all(matrix[j][i] == 0 for i in [1, 2] for j in range(4)))
    wstar = beta/alpha
    check('unchanged_zero', zero['optimization']['stationary'] == enc([F(0), F(0), wstar]))
    cs = [F(*x) for x in col['affine']['intercept']]
    slopes = [[F(*x) for x in row] for row in col['affine']['slopes']]
    fs = [[c]+a for c, a in zip(cs, slopes)]
    check('full_affine_domain', len(fs) == 49 and col['affine']['free_indices'] == [27, 33, 42])
    for n, (row, rhs) in enumerate(zip(col['equations'], col['rhs'])):
        got = [sum(F(*e)*f[k] for e, f in zip(row, fs)) for k in range(4)]
        check(f'affine_original_equation_{n}', got == [F(*rhs), F(0), F(0), F(0)])
    plane = [[f[0]+wstar*f[3], f[1], f[2]] for f in fs]
    out.update({'pairs_through_13': pairs[:14], 'rho': rho, 'w_star': wstar,
                'plane_free': plane, 'normalization': {'N': N, 'M': M}})
    save('inputs_and_plane')

    dictionary = {}
    for row in old['types']:
        key = min(map(tuple, orders(atoms(*row['type']))))
        value = [F(*row['y']), F(0), F(0)]
        check(f'old_shared_key_{row["type"]}', key not in dictionary or dictionary[key] == value)
        dictionary[key] = value
    check('old_scalar_rows_unchanged', len(old['types']) == 121 and all(
          all(F(*s) >= 0 for s in pres['slacks'])
          for row in old['types'] for pres in row['presentations']))
    records, inequalities, seen = [], [], set()
    counts = {'represented': 0, 'forbidden': 0, 'free': 0}
    new_dictionary = dict(dictionary)
    D = set(range(68))
    distances_seen = set()
    for index, row in enumerate(col['column'][1:]):
        l, i, j = row['orbit']
        at = atoms(l, 7, i, j)
        presentations = orders(at)
        key = min(map(tuple, presentations))
        distances = [l, 7, l+7-i-j]
        if key in dictionary:
            kind, value = 'represented', dictionary[key]
        elif any(1 <= h <= 4 for h in distances):
            kind, value = 'forbidden', [F(0)]*3
        else:
            kind = 'free'
            variable = row['variable']
            value = [pairs[7]*x for x in plane[variable]]
            check(f'free_first_occurrence_{index}', variable == len(seen) and key not in seen)
            seen.add(key)
        counts[kind] += 1
        check(f'classification_{index}', row['kind'] == kind and row['atoms'] == at
              and row['key'] == list(key) and row['presentations'] == presentations)
        if kind != 'free':
            check(f'fixed_lookup_{index}', value == [F(*row['value']), F(0), F(0)])
        check(f'shared_plane_equality_{index}', key not in new_dictionary or new_dictionary[key] == value)
        new_dictionary[key] = value
        U, V = set(range(7)), set(range(68, 75))
        X, Y = set(range(i))|set(range(7, 7+l-i)), set(range(68, 68+j))|set(range(75, 75+l-j))
        E, G = (D-X)|Y, (D-U)|V
        supports = [D, E, G]
        rec = {'type': [l, 7, i, j], 'kind': kind, 'key': key,
               'plane_y': value, 'presentations': []}
        for order_index, order in enumerate(it.permutations(range(3))):
            A, B, C = [supports[k] for k in order]
            actual = [sum(4*(x in A)+2*(x in B)+(x in C) == mask
                          for x in range(1024)) for mask in range(8)]
            a, b, h = len(A-B), len(A-C), len(B-C)
            t, s = len(A-(B|C)), len((B&C)-A)
            distances_seen.update([a, b, h])
            O = comb(68, t)*comb(68-t, a-t)*comb(68-a, b-t)*comb(956, s)*comb(956-s, a-s)*comb(956-a, b-s)
            # Equivalent multinomials with residual parts; all domains are actual.
            check(f'actual_source_orbit_{index}_{order_index}', actual == presentations[order_index]
                  and min(actual) >= 0 and sum(actual) == 1024 and all(len(S) == 68 for S in supports)
                  and len({frozenset(S) for S in supports}) == 3 and O > 0
                  and h == a+b-t-s and t-s == i-j)
            slacks = [value, [pairs[a]-value[0], -value[1], -value[2]],
                      [1+value[0]-pairs[a]-pairs[b], value[1], value[2]]]
            check(f'positive_source_normalization_{index}_{order_index}',
                  all(F(N*O)*rho*x/(M*O) == x for x in value))
            if any(1 <= d <= 4 for d in [a, b, h]):
                check(f'forbidden_zero_{index}_{order_index}', value == [F(0)]*3)
            for k, affine in enumerate(slacks):
                inequalities.append({'type': rec['type'], 'order': list(order),
                                     'row': ['nonnegative', 'upper', 'lower'][k], 'affine': affine})
            rec['presentations'].append({'order': list(order), 'atoms': actual,
                'source_indices': [a, b, t, s], 'third_distance': h,
                't_minus_s': t-s, 'orbit_size': O, 'plane_slacks': slacks})
        records.append(rec)
    check('complete_85_domain', [r['type'] for r in records] == [
          [l, 7, i, j] for l in [5, 6] for i, j in it.product(range(l+1), repeat=2)])
    check('partition', counts == {'represented': 20, 'forbidden': 16, 'free': 49})
    check('through_thirteen', max(distances_seen) == 13)
    check('row_count', len(inequalities) == 1530)
    out.update({'records': records, 'inequalities': inequalities, 'partition': counts})
    save('full_two_variable_rows')

    # An exact point suffices for feasibility of the entire plane. If this
    # natural point fails, the full two-variable system remains available.
    u, v = F(0), F(0)
    slacks = [r['affine'][0]+u*r['affine'][1]+v*r['affine'][2] for r in inequalities]
    bad = [k for k, x in enumerate(slacks) if x < 0]
    free_values = [f[0]+u*f[1]+v*f[2] for f in plane]
    out['point_test'] = {'parameters': [u, v, wstar], 'free_values': free_values,
                         'all_slacks': slacks, 'violating_rows': bad}
    if not bad:
        check('point_nonnegative_domain', min(free_values) >= 0)
        ratios = [r['plane_y'][0]/min(pairs[d] for d in [r['type'][0], 7,
                    r['type'][0]+7-r['type'][2]-r['type'][3]]) for r in records
                  if r['kind'] != 'forbidden' and min(pairs[d] for d in [r['type'][0], 7,
                    r['type'][0]+7-r['type'][2]-r['type'][3]]) > 0]
        out['maximum_upper_ratio'] = max(ratios)
    out['summary'] = {'checks': len(checks), 'failures': len(failures),
        'types': len(records), 'presentations': 6*len(records), 'scalar_rows': len(slacks),
        'minimum_slack_sign': int(min(slacks) > 0)-int(min(slacks) < 0),
        'violating_rows': len(bad), 'point_nonnegative_free': sum(x >= 0 for x in free_values),
        'verdict': 'EXACT_FEASIBLE_POINT' if not bad and not failures else 'POINT_FAILED_PLANE_UNDECIDED'}
    save('completed_point_test')
    print(json.dumps(out['summary'], sort_keys=True))
    if not bad:
        ratio = out['maximum_upper_ratio']
        print('Actual maximum y/min(pair) in', F(ratio.numerator*10**9//ratio.denominator,10**9),
              'to', F(ratio.numerator*10**9//ratio.denominator+1,10**9), '; required <=1')
    print('Failures:', failures, '; certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

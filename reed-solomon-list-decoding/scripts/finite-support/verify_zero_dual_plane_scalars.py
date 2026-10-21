"""Independent exact substitution for the zero-plane scalar certificate.

No constructor imports or floating arithmetic. Rebuilds source orbits by
atom permutations, factorial multinomials, and complete saved local inputs.
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
OUT = ROOT/'zero-dual-plane-scalars-verification.json'


def enc(v):
    if isinstance(v, Q):
        return [v.numerator, v.denominator]
    if isinstance(v, dict):
        return {k: enc(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [enc(x) for x in v]
    return v


def multinomial(parts):
    numerator = factorial(sum(parts))
    for p in parts:
        numerator //= factorial(p)
    return numerator


def main():
    paths = [ROOT/n for n in ['zero-dual-plane-scalars-results.json', 'delsarte-lp-results.json',
             'seven-distance-full-base-kernel-results.json', 'seven-shell-affine-fixed-dual-results.json',
             'simultaneous-shell-ordinary-scalars-results.json']]
    data, lp, column, square, old = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('all_inputs_without_failures', all(not x['failures'] for x in [data, lp, column, square, old]))
    check('pinned_input_hashes', all(hashlib.sha256((NB/n).read_bytes()).hexdigest() == h
                                   for n, h in data['input_hashes'].items()))
    primal = [Q(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    # Polynomial-coefficient reconstruction of every defining L021 equation.
    for j in range(1, 65):
        polynomial = [0]*69
        for s in range(69-j):
            for t in range(min(j, 68-s)+1):
                polynomial[s+t] += comb(68-j, s)*comb(956-j, s)*(-1)**t*comb(j, t)
        val = sum(Q(polynomial[h], comb(68, h)*comb(956, h))*a
                  for h, a in zip(range(5, 69), primal))
        check(f'polynomial_L021_{j}', val == -1)
    p = [Q(1)]+[Q(0)]*4+[a/Q(2*comb(68, h)*comb(956, h))
                          for h, a in zip(range(5, 69), primal)]
    check('all_thirteen_pairs', data['pairs_through_13'] == enc(p[:14])
          and primal[8] == Q(808753696404081487284494974858496, 11))
    N = comb(1024, 68)
    M = (Q(comb(1024, 64), comb(68, 64))+1)/2
    rho = M/N
    check('positive_original_normalization', rho > 0 and p[7] > 0 and data['rho'] == enc(rho)
          and old['rho'] == enc(rho) and data['normalization'] == enc({'N': N, 'M': M}))
    A = [[Q(*x) for x in row] for row in square['objective_matrix']]
    w = A[0][3]/(-A[3][3])
    check('square_zero_on_entire_uv_plane', A[3][3] < 0 and A[0][0]+2*A[0][3]*w+A[3][3]*w*w == 0
          and all(A[i][j] == A[j][i] == 0 for i in [1, 2] for j in range(4)))
    check('w_star', data['w_star'] == enc(w) and square['optimization']['stationary'] == enc([Q(0), Q(0), w]))
    intercept = [Q(*x) for x in column['affine']['intercept']]
    slopes = [[Q(*x) for x in row] for row in column['affine']['slopes']]
    plane = [[c+w*s[2], s[0], s[1]] for c, s in zip(intercept, slopes)]
    check('all_49_plane_entries', enc(plane) == data['plane_free'])
    free = [row[0] for row in plane]
    check('nonnegative_free', all(x >= 0 for x in free) and [i for i, x in enumerate(free) if x == 0] == [27, 33])
    for n, (row, rhs) in enumerate(zip(column['equations'], column['rhs'])):
        vals = [sum(Q(*e)*f[k] for e, f in zip(row, plane)) for k in range(3)]
        check(f'complete_plane_kernel_equation_{n}', vals == [Q(*rhs), Q(0), Q(0)])

    permutations = list(it.permutations([4, 2, 1]))

    def reorder(at):
        result = []
        for perm in permutations:
            target = [0]*8
            for mask, number in enumerate(at):
                dest = sum(bit for bit, original in zip([4, 2, 1], perm) if mask & original)
                target[dest] = number
            result.append(target)
        return result

    immutable = {}
    old_slacks = []
    for n, rec in enumerate(old['types']):
        # The complete old values and their scalar pass are imported from L062;
        # check all saved source rows against their original pair normalization.
        value = Q(*rec['y'])
        for k, pres in enumerate(rec['presentations']):
            a, b, t, s = pres['source_indices']
            slacks = [value, p[a]-value, 1+value-p[a]-p[b]]
            check(f'old_scalar_rows_{n}_{k}', pres['slacks'] == enc(slacks) and min(slacks) >= 0)
            old_slacks.extend(slacks)
        key = min(map(tuple, reorder(rec['presentations'][0]['atoms'])))
        val = [value, Q(0), Q(0)]
        check(f'immutable_old_key_{n}', key not in immutable or immutable[key] == val)
        immutable[key] = val

    records, complete_column, residuals = [], [p[7]], []
    keys, source_equalities = {}, {}
    partition = {'represented': 0, 'forbidden': 0, 'free': 0}
    all_slacks, unique_free_keys, inequality_index = [], [], 0
    extrema, orbit_sizes, seen_distances = [], [], set()
    for n, (l, i, j) in enumerate((l, i, j) for l in [5, 6] for i, j in it.product(range(l+1), repeat=2)):
        rec, inputrec = data['records'][n], column['column'][n+1]
        at = [949-l+j, 7-j, l-j, j, i, l-i, 7-i, 61-l+i]
        presentations = reorder(at)
        key = min(map(tuple, presentations))
        distances = [l, 7, l+7-i-j]
        if key in immutable:
            kind, val = 'represented', immutable[key]
        elif any(1 <= d <= 4 for d in distances):
            kind, val = 'forbidden', [Q(0)]*3
        else:
            kind = 'free'
            check(f'new_free_key_{n}', key not in unique_free_keys)
            unique_free_keys.append(key)
            val = [p[7]*x for x in plane[len(unique_free_keys)-1]]
            check(f'original_free_order_{n}', inputrec['variable'] == len(unique_free_keys)-1)
        partition[kind] += 1
        check(f'complete_record_{n}', rec['type'] == [l, 7, i, j] and rec['kind'] == inputrec['kind'] == kind
              and rec['key'] == inputrec['key'] == list(key) and rec['plane_y'] == enc(val)
              and inputrec['atoms'] == at and inputrec['presentations'] == presentations)
        check(f'shared_full_key_{n}', key not in keys or keys[key] == val)
        keys[key] = val
        complete_column.append(val[0])
        for k, aa in enumerate(presentations):
            a, b = aa[4]+aa[5], aa[4]+aa[6]
            t, s = aa[4], aa[3]
            h = aa[2]+aa[6]
            seen_distances.update([a, b, h])
            O = multinomial([t, a-t, b-t, 68-a-b+t])*multinomial([s, a-s, b-s, 956-a-b+s])
            orbit_sizes.append(O)
            check(f'actual_atom_orbit_{n}_{k}', min(aa) >= 0 and sum(aa) == 1024 and O > 0
                  and all(sum(v for mask, v in enumerate(aa) if mask & bit) == 68 for bit in [1, 2, 4])
                  and h == a+b-t-s and t-s == i-j and 0 not in [a, b, h])
            identity = (tuple(sorted([a, b, h])), t-s)
            check(f'full_source_equality_{n}_{k}', identity not in source_equalities or source_equalities[identity] == val)
            source_equalities[identity] = val
            slacks = [val, [p[a]-val[0], -val[1], -val[2]],
                      [1+val[0]-p[a]-p[b], val[1], val[2]]]
            pres = rec['presentations'][k]
            check(f'every_original_source_row_{n}_{k}', pres == enc({'order': list(it.permutations(range(3)))[k],
                'atoms': aa, 'source_indices': [a, b, t, s], 'third_distance': h,
                't_minus_s': t-s, 'orbit_size': O, 'plane_slacks': slacks}))
            check(f'normalization_{n}_{k}', all(Q(N*O)*rho*x/(M*O) == x for x in val))
            for label, slack in zip(['nonnegative', 'upper', 'lower'], slacks):
                check(f'original_inequality_{inequality_index}', data['inequalities'][inequality_index] == enc({
                    'type': [l, 7, i, j], 'order': list(it.permutations(range(3)))[k], 'row': label, 'affine': slack}))
                check(f'exact_slack_sign_{inequality_index}', slack[0] >= 0)
                check(f'saved_point_slack_{inequality_index}', data['point_test']['all_slacks'][inequality_index] == enc(slack[0]))
                all_slacks.append(slack[0])
                inequality_index += 1
            check(f'distinct_lower_bound_{n}_{k}', slacks[2][0] >= 1-2*p[5] > 0)
            if any(1 <= d <= 4 for d in [a, b, h]):
                check(f'forbidden_{n}_{k}', val == [Q(0)]*3)
            elif min(p[d] for d in [a, b, h]) > 0:
                ratio = val[0]/min(p[d] for d in [a, b, h])
                extrema.append((ratio, [l, 7, i, j]))
        records.append({'type': [l, 7, i, j], 'y': val[0]})
    weights = [1]+[comb(7, i)*comb(61, l-i)*comb(7, j)*comb(949, l-j)
                   for l in [5, 6] for i, j in it.product(range(l+1), repeat=2)]
    check('all_original_orbit_weights', weights == column['weights'])
    for n, vec in enumerate(column['kernel_basis']):
        value = sum(wt*Q(*entry)*b for wt, entry, b in zip(weights, vec, complete_column))
        residuals.append(value)
        check(f'weighted_original_whole_kernel_{n}', value == 0)
    maximum, maximizing_type = max(extrema)
    check('all_three_pair_bounds', 0 <= maximum < Q(1, 10**9)
          and data['maximum_upper_ratio'] == enc(maximum))
    check('exhaustion', len(records) == 85 and inequality_index == 1530 and len(all_slacks) == 1530
          and len(old_slacks) == 2178 and len(unique_free_keys) == 49 and max(seen_distances) == 13
          and partition == data['partition'] == {'represented': 20, 'forbidden': 16, 'free': 49})
    check('saved_point', data['point_test']['parameters'] == enc([Q(0), Q(0), w])
          and data['point_test']['free_values'] == enc(free) and data['point_test']['violating_rows'] == [])
    check('zero_minimum', min(all_slacks) == 0)
    summary = {'checks': len(checks), 'failures': len(failures), 'types': 85,
               'presentations': 510, 'new_scalar_rows': len(all_slacks), 'retained_old_rows': len(old_slacks),
               'kernel_residuals': len(residuals), 'maximum_upper_ratio_below_1e_minus_9': maximum < Q(1, 10**9),
               'minimum_scalar_slack': min(all_slacks), 'partition': partition,
               'zero_free_indices': [i for i, x in enumerate(free) if x == 0],
               'verdict': 'EXACT_FEASIBLE_POINT' if not failures else 'VERIFICATION_FAILED'}
    OUT.write_text(json.dumps(enc({'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in paths}, 'checks': checks, 'failures': failures, 'summary': summary,
                         'all_new_slacks': all_slacks, 'all_old_slacks': old_slacks,
                         'complete_column': complete_column, 'original_kernel_residuals': residuals,
                         'maximum_upper_ratio': maximum, 'maximizing_type': maximizing_type,
                         'minimum_source_orbit_size': min(orbit_sizes), 'reconstructed_values': records}), indent=2)+'\n')
    print(json.dumps(enc(summary), sort_keys=True))
    print('Actual max y/min(pair) < 1/1000000000; required <=1; failures:', failures)
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

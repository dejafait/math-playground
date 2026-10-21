"""Independent reconstruction and full exact certificate verification.

No constructor, optimizer or decimal arithmetic imported. Kernel exhaustion
uses modular rank lower bounds and full rational nullspace upper bounds.
"""
import hashlib
import itertools
import json
import re
import sys
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, gcd, isqrt, lcm
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'seven-distance-full-base-kernel-verification.json'
sys.set_int_max_str_digits(0)


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(v):
    v = Q(v)
    return [v.numerator, v.denominator]


def orders(a):
    out = []
    for order in itertools.permutations([4, 2, 1]):
        row = [0]*8
        for mask in range(8):
            new = sum(bit for bit, old in zip([4, 2, 1], order) if mask & old)
            row[new] = a[mask]
        out.append(row)
    return out


@lru_cache(None)
def overlap_counts(n, l, m, i, u):
    # Convolve distinguished and undistinguished region generating functions.
    a = [c(i, s)*c(7-i, u-s) for s in range(8)]
    b = [c(l-i, t)*c(n-7-l+i, m-u-t) for t in range(l+1)]
    return [sum(a[s]*b[k-s] for s in range(8) if 0 <= k-s < len(b))
            for k in range(min(l, m)+1)]


def modular_rank(matrix, prime):
    a = []
    for row in matrix:
        den = lcm(*(Q(x).denominator for x in row))
        rr = [int(Q(x)*den) for x in row]
        g = gcd(*rr)
        if g:
            rr = [x//g for x in rr]
        a.append([x % prime for x in rr])
    rank, pivots = 0, []
    for j in range(len(a[0])):
        r = next((r for r in range(rank, len(a)) if a[r][j]), None)
        if r is None:
            continue
        a[r], a[rank] = a[rank], a[r]
        inv = pow(a[rank][j], -1, prime)
        a[rank] = [x*inv % prime for x in a[rank]]
        for s in range(rank+1, len(a)):
            v = a[s][j]
            if v:
                a[s] = [(x-v*y) % prime for x, y in zip(a[s], a[rank])]
        pivots.append(j)
        rank += 1
        if rank == len(a):
            break
    return rank, pivots


def main():
    path = ROOT / 'seven-distance-full-base-kernel-results.json'
    data = json.loads(path.read_text())
    source = json.loads((ROOT / 'simultaneous-shell-ordinary-scalars-results.json').read_text())
    old = json.loads((ROOT / 'full-shell-nullspace-results.json').read_text())
    six = json.loads((ROOT / 'simultaneous-five-six-shell-results.json').read_text())
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('constructor_and_prior_failures_empty', all(not v['failures'] for v in [data, source, old, six]))
    check('all_immutable_source_hashes', all(hashlib.sha256((NB/name).read_bytes()).hexdigest() == h
                                         for name, h in data['source_hashes'].items()))
    check('prior_source_hashes', all(hashlib.sha256((NB/name).read_bytes()).hexdigest() == h
                                   for name, h in source['source_hashes'].items()))
    text5 = (NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md').read_text()
    text60 = (NB / 'lemmas/L060-full-shell-one-column-psd-extension.md').read_text()
    poly = {k: Q(v) for k, v in re.findall(r'^\| (A|B0|C0) \| (-?[0-9]+/[0-9]+) \|$', text60, re.M)}
    star = -poly['B0']/(2*poly['A'])
    d5 = {(int(r), int(q)): Q(v)/(c(5, int(r))*c(63, int(r))*c(5, int(q))*c(951, int(q)))
          for r, q, v in re.findall(r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', text5, re.M)}
    d5[0, 0] = Q(1)
    p = [Q(*v) for v in source['pairs_through_12']]
    check('original_p7', p[7] == Q(*data['p7']) == Q(3539, 248922676958508))
    free_old = [tuple(v) for v in old['free']]
    intercept = dict(zip(free_old, [Q(*x) for x in old['nonnegative_test']['intercept']]))
    slope = dict(zip(free_old, [Q(*x) for x in old['nonnegative_test']['slope']]))
    t = {(i, j): intercept[i, j]+star*slope[i, j] if i+j <= 5
         else d5[6-i, i] if i+j == 6 else Q(0)
         for i, j in itertools.product(range(6), repeat=2)}
    rel = [(r, q) for r in range(7) for q in range(7) if r+q >= 6]
    d6 = {(r, q): Q(*v)/(c(6, r)*c(62, r)*c(6, q)*c(950, q))
          for (r, q), v in zip(rel, six['exact']['z'])}
    d6[0, 0] = Q(1)
    for r in range(6):
        d6[r, 5-r] = p[5]*t[5-r, r]/p[6]
    base, dictionary = {}, {}
    for row in source['types']:
        l, m, i, j = row['type']
        y = p[5]*d5.get((5-i, 5-j), Q(0)) if (l, m) == (5, 5) else (
            p[5]*t[i, j] if (l, m) == (5, 6) else p[6]*d6.get((6-i, 6-j), Q(0)))
        aa = [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]
        presentations = orders(aa)
        check('base_value_'+str(row['type']), y == Q(*row['y']))
        check('base_six_presentations_'+str(row['type']), presentations == [r['atoms'] for r in row['presentations']])
        key = min(map(tuple, presentations))
        check('base_unordered_lookup_'+str(row['type']), key not in dictionary or dictionary[key] == y)
        dictionary[key] = y
        base[l, m, i, j] = y
    check('whole_base_domain', len(base) == 121)
    orbits = [(0, 0, 0)]+[(l, i, j) for l in [5, 6] for i in range(l+1) for j in range(l+1)]
    weights = [1]+[c(7, i)*c(61, l-i)*c(7, j)*c(949, l-j) for l, i, j in orbits[1:]]
    check('complete_orbits_weights', data['orbits'] == list(map(list, orbits)) and data['weights'] == weights)
    scale = data['scale']
    action = []
    for a, (l, i, j) in enumerate(orbits):
        row = []
        for b, (m, u, v) in enumerate(orbits):
            if not l:
                y = Q(1) if not m else p[m]*weights[b]
            elif not m:
                y = p[l]
            else:
                hh = overlap_counts(68, l, m, i, u)
                tt = overlap_counts(956, l, m, j, v)
                y = sum(x*z*base[min(l, m), max(l, m), k, h]
                        for k, x in enumerate(hh) for h, z in enumerate(tt))
            check(f'action_entry_{a}_{b}', y*scale == data['integer_action'][a][b])
            row.append(int(y*scale))
        action.append(row)
    prime = 2147483647  # The classical Mersenne prime 2^31-1.
    check('rank_modulus_prime_by_trial_division', all(prime % d for d in range(2, isqrt(prime)+1)))
    rank, pivots = modular_rank(action, prime)
    check('modular_rank_lower_37', rank == 37)
    kernel = [[Q(*x) for x in row] for row in data['kernel_basis']]
    nonpiv = [j for j in range(86) if j not in data['pivots']]
    check('49_independent_kernel_columns', len(kernel) == len(nonpiv) == 49 and all(
        kernel[i][j] == int(i == k) for i in range(49) for k, j in enumerate(nonpiv)))
    for k, v in enumerate(kernel):
        for r, row in enumerate(action):
            check(f'full_kernel_residual_{k}_{r}', sum(x*z for x, z in zip(row, v)) == 0)
    eq, rhs = [], []
    free_keys = []
    complete = [Q(*v) for v in data['complete_column']]
    check('whole_column_domain_nonnegative', len(complete) == 86 and all(x >= 0 for x in complete))
    for z, (l, i, j) in enumerate(orbits):
        rec = data['column'][z]
        check('column_order_'+str(z), rec['orbit'] == [l, i, j])
        if not l:
            check('original_anchor_transport', complete[z] == p[7])
            continue
        aa = [949-l+j, 7-j, l-j, j, i, l-i, 7-i, 61-l+i]
        permutations = orders(aa)
        key = min(map(tuple, permutations))
        check('column_atoms_'+str(z), rec['atoms'] == aa and rec['presentations'] == permutations
              and rec['key'] == list(key))
        h = l+7-i-j
        if key in dictionary:
            check('represented_lookup_'+str(z), rec['kind'] == 'represented' and complete[z] == dictionary[key])
        elif 1 <= h <= 4:
            check('forbidden_zero_'+str(z), rec['kind'] == 'forbidden' and complete[z] == 0)
        else:
            if key not in free_keys:
                free_keys.append(key)
            check('full_free_key_'+str(z), rec['kind'] == 'free' and rec['variable'] == free_keys.index(key))
    check('all_49_free_keys', data['free_keys'] == list(map(list, free_keys)) and len(free_keys) == 49)
    for k, v in enumerate(kernel):
        row = [Q(0)]*49
        b = Q(0)
        for w, h, rec in zip(weights, v, data['column']):
            if rec['kind'] == 'free':
                row[rec['variable']] += w*h*p[7]
            else:
                b -= w*h*Q(*rec['value'])
        norm = max(map(abs, row))
        if norm:
            row, b = [x/norm for x in row], b/norm
        eq.append(row)
        rhs.append(b)
        check('original_kernel_equation_'+str(k), data['equations'][k] == list(map(enc, row)) and data['rhs'][k] == enc(b))
        check('weighted_column_residual_'+str(k), sum(w*x*z for w, x, z in zip(weights, v, complete)) == 0)
    erank, _ = modular_rank(eq, prime)
    check('equation_rank_lower_46', erank == 46)
    affine = data['affine']
    ci = [Q(*v) for v in affine['intercept']]
    cs = [[Q(*v) for v in row] for row in affine['slopes']]
    check('three_independent_affine_directions', affine['free_indices'] == [27, 33, 42] and all(
        cs[j] == [Q(k == s) for k in range(3)] for s, j in enumerate([27, 33, 42])))
    for k, (row, b) in enumerate(zip(eq, rhs)):
        check('affine_intercept_'+str(k), sum(x*z for x, z in zip(row, ci)) == b)
        for s in range(3):
            check(f'affine_direction_{k}_{s}', sum(x*v[s] for x, v in zip(row, cs)) == 0)
    params = [Q(0), Q(0), -ci[4]/cs[4][2]]
    check('explicit_unique_parameter', cs[4][2] != 0 and params[2] > 0
          and data['chosen_parameters'] == list(map(enc, params)))
    solution = [b+sum(x*z for x, z in zip(row, params)) for b, row in zip(ci, cs)]
    check('exact_witness_all_49_coordinates', data['solution'] == list(map(enc, solution))
          and all(v >= 0 for v in solution))
    check('three_prescribed_witness_zeros', [j for j, v in enumerate(solution) if not v] == [4, 27, 33])
    for k, (row, b) in enumerate(zip(eq, rhs)):
        check('exact_witness_equation_'+str(k), sum(x*z for x, z in zip(row, solution)) == b)
    for z, rec in enumerate(data['column']):
        if rec['kind'] == 'free':
            check('actual_free_column_'+str(z), complete[z] == p[7]*solution[rec['variable']])
    summary = {'checks': len(checks), 'failures': len(failures), 'base_rank': rank,
               'full_invariant_kernel_dimension': 49, 'equation_rank': erank,
               'nonnegative_free_coordinates': len(solution), 'strictly_positive_free_coordinates': sum(v > 0 for v in solution),
               'min_free_coordinate': enc(min(solution)), 'max_free_coordinate': enc(max(solution)),
               'all_original_weighted_kernel_residuals_zero': all(sum(w*x*z for w, x, z in zip(weights, v, complete)) == 0 for v in kernel)}
    out = {'constructor_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
           'modular_rank_prime': prime, 'modular_rank_pivots': pivots,
           'complete_column': list(map(enc, complete)), 'solution': list(map(enc, solution)),
           'parameters': list(map(enc, params)), 'checks': checks, 'failures': failures, 'summary': summary}
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print('Independent exact checks:', len(checks), '; failures:', failures)
    print('Base rank/kernel:', rank, 49, '; equation rank:', erank)
    print('Free signs: 46 positive, 3 zero; required: all >=0. All 49 whole-kernel residuals are zero.')
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit('Verification failures')


if __name__ == '__main__':
    main()

"""Independent exact verification of L076 fixed-column inverse/energy.

No notebook module, optimizer or floating arithmetic. Actual subset
histograms reconstruct every action entry; all full-space lift residuals,
weighted contributions and the whole-anchor transport are checked.
"""
import hashlib
import itertools as it
import json
import sys
from collections import Counter
from fractions import Fraction as F
from math import comb, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'eight-distance-fixed-column-energy-verification.json'
LAYERS = [5, 6, 7]


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def solve(A, rhs):
    a = [[F(x) for x in row]+[F(y)] for row, y in zip(A, rhs)]
    for k in range(len(a)):
        s = next(j for j in range(k, len(a)) if a[j][k])
        a[k], a[s] = a[s], a[k]
        pivot = a[k][k]
        a[k] = [x/pivot for x in a[k]]
        for j in range(k+1, len(a)):
            v = a[j][k]
            a[j] = [x-v*y for x, y in zip(a[j], a[k])]
    z = [F(0)]*len(a)
    for k in reversed(range(len(a))):
        z[k] = a[k][-1]-sum(a[k][j]*z[j] for j in range(k+1, len(a)))
    return z


def actual(l, m, i, j):
    D = set(range(68))
    X = set(range(i)) | set(range(m, m+l-i))
    Y = set(range(68, 68+j)) | set(range(68+m, 68+m+l-j))
    G = (D-set(range(m))) | set(range(68, 68+m))
    out = []
    for ss in it.permutations([D, (D-X) | Y, G]):
        aa = [0]*8
        for x in range(1024):
            aa[sum(bit for bit, s in zip([4, 2, 1], ss) if x in s)] += 1
        out.append(aa)
    return out


def subset_counts(n, l, i):
    # U has eight actual points; X meets it in precisely i points.
    U = (1 << 8)-1
    X = (1 << i)-1 | ((1 << (l-i))-1) << 8
    size = 8+l-i
    histogram = Counter(((mask & U).bit_count(), (mask & X).bit_count(), mask.bit_count())
                        for mask in range(1 << size))
    return {(m, u, k): sum(histogram[u, k, s]*c(n-size, m-s) for s in range(m+1))
            for m in LAYERS for u in range(m+1) for k in range(min(l, m)+1)}


def main():
    path = ROOT/'eight-distance-fixed-column-energy-results.json'
    got = json.loads(path.read_text())
    data = json.loads((ROOT/'eight-distance-full-base-kernel-results.json').read_text())
    src = json.loads((ROOT/'maximizer-excluded-anchor-results.json').read_text())
    old = json.loads((ROOT/'maximizer-excluded-anchor-critical-audit.json').read_text())
    lp = json.loads((ROOT/'delsarte-lp-results.json').read_text())
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('all_input_failure_lists_empty', all(v['failures'] == [] for v in [got, data, src, old, lp]))
    for rel, digest in got['input_hashes'].items():
        check('frozen_input_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p = [F(1)]+[F(0)]*4+[F(v['numerator'], v['denominator'])/(2*c(68, h)*c(956, h))
                           for h, v in zip(range(5, 69), lp['exact']['primal'])]
    rho = (F(c(1024, 64), c(68, 64))+1)/(2*c(1024, 68))
    check('original_rho_pairs_and_p8', rho == F(*src['rho']) == F(*got['rho']) > 0
          and enc(p[:15]) == src['pairs_through_14'] == got['pairs']
          and p[8] == F(16792471, 1181138102168120460))
    check('all_immutable_upstream_prescriptions', src['parameters'] == old['parameters']
          and src['original_column'] == old['column'] and src['completion_z'] == old['z'])
    base, dictionary = {}, {}
    for row in src['entries']:
        typ = tuple(row['type'])
        y = F(*row['y'])
        orders = actual(*typ)
        key = min(map(tuple, orders))
        check('actual_base_six_'+str(typ), orders == [r['atoms'] for r in row['presentations']])
        check('complete_key_consistency_'+str(typ), key not in dictionary or dictionary[key] == y)
        dictionary[key], base[typ] = y, y
    check('all_270_frozen_base_values', len(base) == 270
          and base == {tuple(r['type']): F(*r['value']) for r in got['base_entries']}
          == {tuple(r['type']): F(*r['y']) for r in old['entries']})
    for l, m, i, j in list(base):
        base[m, l, i, j] = base[l, m, i, j]
    affine = data['affine']
    intercept = [F(*v) for v in affine['intercept']]
    slopes = [[F(*v) for v in row] for row in affine['slopes']]
    active = [27, 33, 56, 63]
    params = solve([slopes[j] for j in active], [-intercept[j] for j in active])
    sol = [x+sum(a*t for a, t in zip(row, params)) for x, row in zip(intercept, slopes)]
    check('fixed_active_solution', enc(params) == got['parameters'] == data['chosen_parameters']
          and enc(sol) == got['free_solution'] == data['solution']
          and [j for j, x in enumerate(sol) if not x] == active and min(sol) == 0)
    for t, (row, rhs) in enumerate(zip(data['equations'], data['rhs'])):
        check('original_affine_equation_'+str(t), sum(F(*a)*b for a, b in zip(row, sol)) == F(*rhs))
    orbits = [(0, 0, 0)]+[(l, i, j) for l in LAYERS for i, j in it.product(range(l+1), repeat=2)]
    W = [1]+[c(8, i)*c(60, l-i)*c(8, j)*c(948, l-j) for l, i, j in orbits[1:]]
    check('all_actual_weights', list(map(list, orbits)) == got['orbits'] == data['orbits']
          and W == got['weights'] == data['weights'] and min(W) > 0)
    b, free_keys = [p[8]], []
    for a, (l, i, j) in enumerate(orbits[1:], 1):
        orders = actual(l, 8, i, j)
        key = min(map(tuple, orders))
        rec = data['column'][a]
        check('all_actual_column_presentations_'+str(a), orders == rec['presentations'] and list(key) == rec['key'])
        if key in dictionary:
            value = dictionary[key]
            check('represented_column_'+str(a), rec['kind'] == 'represented' and value == F(*rec['value']))
        elif 1 <= l+8-i-j <= 4:
            value = F(0)
            check('forbidden_column_'+str(a), rec['kind'] == 'forbidden')
        else:
            if key not in free_keys:
                free_keys.append(key)
            variable = free_keys.index(key)
            value = p[8]*sol[variable]
            check('free_column_'+str(a), rec['kind'] == 'free' and variable == rec['variable'])
        b.append(value)
    check('entire_fixed_nonnegative_column', enc(b) == got['column'] == data['complete_column']
          and min(b) >= 0 and list(map(list, free_keys)) == data['free_keys'])
    counts = {(n, l, i): subset_counts(n, l, i) for n in [68, 956] for l in LAYERS for i in range(l+1)}
    print('Independent actual-subset histograms and all fixed column keys reconstructed.', flush=True)
    Q = [[F(0) for _ in orbits] for _ in orbits]
    index = {o: a for a, o in enumerate(orbits)}
    Q[0][0] = F(1)
    for a, (l, i, j) in enumerate(orbits[1:], 1):
        Q[0][a], Q[a][0] = p[l]*W[a], p[l]
    for l, m in it.product(LAYERS, repeat=2):
        d = lcm(*(base[l, m, k, h].denominator for k, h in it.product(range(min(l, m)+1), repeat=2)))
        Y = [[int(base[l, m, k, h]*d) for h in range(min(l, m)+1)] for k in range(min(l, m)+1)]
        for i, u in it.product(range(l+1), range(m+1)):
            partial = [sum(counts[68, l, i][m, u, k]*Y[k][h] for k in range(min(l, m)+1)) for h in range(min(l, m)+1)]
            for j, v in it.product(range(l+1), range(m+1)):
                Q[index[l, i, j]][index[m, u, v]] = F(sum(partial[h]*counts[956, l, j][m, v, h]
                    for h in range(min(l, m)+1)), d)
    for a, row in enumerate(Q):
        for j, x in enumerate(row):
            check('independent_action_'+str((a, j)), enc(x) == got['action'][a][j] and W[a]*x == W[j]*Q[j][a])
    # A complete original-row residual check independently certifies the
    # inverse-action vector; no trust in the selected solve is required.
    z = [F(*v) for v in got['inverse_action']]
    check('inverse_domain', len(z) == 150)
    zd = lcm(*(x.denominator for x in z))
    zi = [int(x*zd) for x in z]
    products = []
    for row in Q:
        d = lcm(*(x.denominator for x in row))
        products.append(F(sum(int(x*d)*y for x, y in zip(row, zi)), d*zd))
    residuals = [x-bb for x, bb in zip(products, b)]
    for a, v in enumerate(residuals):
        check('all_original_residuals_'+str(a), v == 0 and enc(v) == got['inverse_residuals'][a])
    K = [[F(*x) for x in row] for row in data['kernel_basis']]
    kres = [sum(w*x*y for w, x, y in zip(W, v, b)) for v in K]
    for t, x in enumerate(kres):
        check('all_weighted_kernel_residuals_'+str(t), x == 0 and enc(x) == got['kernel_residuals'][t])
    r = [b[a]-p[l]*p[8] for a, (l, i, j) in enumerate(orbits) if a]
    transported = []
    for a, (l, i, h) in enumerate(orbits[1:], 1):
        row = [Q[a][j]-p[l]*p[m]*W[j] for j, (m, u, v) in enumerate(orbits) if j]
        d = lcm(*(x.denominator for x in row))
        transported.append(F(sum(int(x*d)*y for x, y in zip(row, zi[1:])), d*zd)-r[a-1])
    for a, x in enumerate(transported):
        check('whole_anchor_transport_residual_'+str(a+1), x == 0)
    terms = [w*bb*x for w, bb, x in zip(W, b, z)]
    energy = sum(terms)
    anchor_terms = [p[8]**2]+[w*x*y for w, x, y in zip(W[1:], r, z[1:])]
    bilinear = sum(w*x*y for w, x, y in zip(W, z, products))
    check('full_energy_and_anchor_identity', enc(terms) == got['weighted_energy_contributions']
          and energy == sum(anchor_terms) == bilinear == F(*got['energy']) == F(*got['bilinear_energy']) >= 0)
    ratio, slack = energy/p[8], p[8]-energy
    check('entire_rational_ratio_and_remainder', enc(ratio) == got['energy_ratio']
          and enc(slack) == got['schur_remainder'] and enc(p[8]) == got['required_diagonal'])
    lo, hi = [F(*x) for x in got['summary']['ratio_interval']]
    check('manuscript_ratio_interval', lo == F(1461591, 10**12) and hi == F(1461592, 10**12))
    interval_gaps = [ratio.numerator*lo.denominator-lo.numerator*ratio.denominator,
                     hi.numerator*ratio.denominator-ratio.numerator*hi.denominator]
    check('exact_integer_ratio_bounds', interval_gaps[0] >= 0 and interval_gaps[1] > 0)
    verdict = 'PSD_EXTENSION' if slack >= 0 else 'FIXED_COLUMN_REJECTED'
    check('exact_singular_schur_verdict', got['summary']['verdict'] == verdict)
    summary = {'checks': len(checks), 'failures': len(failures), 'verdict': verdict,
               'all_150_original_residuals_zero': not any(residuals),
               'all_149_transported_residuals_zero': not any(transported),
               'all_90_weighted_kernel_residuals_zero': not any(kres),
               'ratio_interval': [lo, hi], 'required_ratio_upper_bound': 1,
               'energy_nonnegative': energy >= 0, 'remainder_nonnegative': slack >= 0}
    out = {'constructor_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
           'summary': summary, 'checks': checks, 'failures': failures, 'rho': rho, 'pairs': p[:15],
           'weights': W, 'column': b, 'action': Q, 'inverse_action': z, 'inverse_residuals': residuals,
           'kernel_residuals': kres, 'transported_column': r, 'transported_residuals': transported,
           'weighted_energy_contributions': terms, 'anchor_energy_contributions': anchor_terms,
           'energy': energy, 'energy_ratio': ratio, 'required_diagonal': p[8], 'schur_remainder': slack,
           'integer_ratio_comparison_gaps': interval_gaps}
    OUT.write_text(json.dumps(enc(out), indent=2)+'\n')
    print('Independent checks:', len(checks), '; failures:', failures)
    print('Actual energy/p8 in [', lo, ',', hi, '); required <= 1; verdict:', verdict)
    print('All 150 original and 149 transported inverse residuals zero:', not any(residuals+transported))
    print('Full certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

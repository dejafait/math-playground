"""Independent full exact residual/energy verification, no constructor imports.

Rebuild old entries from manuscript inputs, count subset transitions by
actual subset enumeration, and check the full lifted inverse equation.
"""
import hashlib
import itertools
import json
import re
import sys
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'seven-distance-fixed-column-energy-verification.json'
sys.set_int_max_str_digits(0)


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def orders(atoms):
    rows = []
    for order in itertools.permutations([4, 2, 1]):
        row = [0]*8
        for mask in range(8):
            row[sum(bit for bit, old in zip([4, 2, 1], order) if mask & old)] = atoms[mask]
        rows.append(row)
    return rows


def subset_counts(n, l, i):
    u = set(range(7))
    x = set(range(i)) | set(range(7, 7+l-i))
    points = sorted(u | x)
    out = {(m, a, k): 0 for m in (5, 6) for a in range(m+1) for k in range(min(l, m)+1)}
    for mask in range(1 << len(points)):
        chosen = {point for j, point in enumerate(points) if mask >> j & 1}
        a, k, s = len(chosen & u), len(chosen & x), len(chosen)
        for m in (5, 6):
            if s <= m:
                out[m, a, k] += c(n-len(points), m-s)
    return out


def main():
    path = ROOT/'seven-distance-fixed-column-energy-results.json'
    got = json.loads(path.read_text())
    data = json.loads((ROOT/'seven-distance-full-base-kernel-results.json').read_text())
    source = json.loads((ROOT/'simultaneous-shell-ordinary-scalars-results.json').read_text())
    old = json.loads((ROOT/'full-shell-nullspace-results.json').read_text())
    six = json.loads((ROOT/'simultaneous-five-six-shell-results.json').read_text())
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('all_input_and_constructor_failure_lists_empty', all(not v['failures'] for v in [got, data, source, old, six]))
    for name, h in got['input_hashes'].items():
        check('complete_input_hash_'+name, hashlib.sha256((NB/name).read_bytes()).hexdigest() == h)
    for v in [data, source]:
        for name, h in v['source_hashes'].items():
            check('immutable_'+name, hashlib.sha256((NB/name).read_bytes()).hexdigest() == h)
    rho = (F(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    check('original_positive_rho', rho == F(*source['rho']) == F(*data['rho']) > 0)
    p = [F(*x) for x in source['pairs_through_12']]
    check('original_pairs', p[5:8] == [F(1, 68881143660), F(133, 9357995374380), F(3539, 248922676958508)])
    text5 = (NB/'lemmas/L056-released-zero-five-shell-nonexclusion.md').read_text()
    text60 = (NB/'lemmas/L060-full-shell-one-column-psd-extension.md').read_text()
    poly = {k: F(v) for k, v in re.findall(r'^\| (A|B0|C0) \| (-?[0-9]+/[0-9]+) \|$', text60, re.M)}
    star = -poly['B0']/(2*poly['A'])
    d5 = {(int(r), int(q)): F(v)/(c(5, int(r))*c(63, int(r))*c(5, int(q))*c(951, int(q)))
          for r, q, v in re.findall(r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', text5, re.M)}
    d5[0, 0] = F(1)
    free = [tuple(x) for x in old['free']]
    intercept = dict(zip(free, [F(*x) for x in old['nonnegative_test']['intercept']]))
    slope = dict(zip(free, [F(*x) for x in old['nonnegative_test']['slope']]))
    t = {(i, j): intercept[i, j]+star*slope[i, j] if i+j <= 5 else
         d5[6-i, i] if i+j == 6 else F(0) for i, j in itertools.product(range(6), repeat=2)}
    rel = [(r, q) for r in range(7) for q in range(7) if r+q >= 6]
    d6 = {(r, q): F(*v)/(c(6, r)*c(62, r)*c(6, q)*c(950, q))
          for (r, q), v in zip(rel, six['exact']['z'])}
    d6[0, 0] = F(1)
    for r in range(6):
        d6[r, 5-r] = p[5]*t[5-r, r]/p[6]
    base, dictionary = {}, {}
    stored_base = {tuple(row['type']): F(*row['value']) for row in got['base_entries']}
    for row in source['types']:
        l, m, i, j = row['type']
        y = p[5]*d5.get((5-i, 5-j), F(0)) if (l, m) == (5, 5) else (
            p[5]*t[i, j] if (l, m) == (5, 6) else p[6]*d6.get((6-i, 6-j), F(0)))
        atoms = [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]
        key = min(map(tuple, orders(atoms)))
        check('unchanged_base_'+str(row['type']), y == F(*row['y']) == stored_base[l, m, i, j])
        check('unordered_consistency_'+str(row['type']), key not in dictionary or dictionary[key] == y)
        dictionary[key] = y
        base[l, m, i, j] = y
    orbits = [(0, 0, 0)]+[(l, i, j) for l in [5, 6] for i in range(l+1) for j in range(l+1)]
    weights = [1]+[c(7, i)*c(61, l-i)*c(7, j)*c(949, l-j) for l, i, j in orbits[1:]]
    check('full_86_orbit_domain', got['orbits'] == list(map(list, orbits)) and got['weights'] == weights)
    affine = data['affine']
    ci = [F(*v) for v in affine['intercept']]
    slopes = [[F(*v) for v in row] for row in affine['slopes']]
    params = [F(0), F(0), -ci[4]/slopes[4][2]]
    solution = [x+sum(a*b for a, b in zip(row, params)) for x, row in zip(ci, slopes)]
    check('prescribed_parameters', got['parameters'] == list(map(enc, params)) == data['chosen_parameters'])
    check('all_49_free_coordinates', got['free_solution'] == list(map(enc, solution)) == data['solution'])
    column, free_keys = [p[7]], []
    for l, i, j in orbits[1:]:
        key = min(map(tuple, orders([949-l+j, 7-j, l-j, j, i, l-i, 7-i, 61-l+i])))
        h = l+7-i-j
        if key in dictionary:
            y = dictionary[key]
        elif 1 <= h <= 4:
            y = F(0)
        else:
            check('distinct_free_key_'+str((l, i, j)), key not in free_keys)
            free_keys.append(key)
            y = p[7]*solution[len(free_keys)-1]
        column.append(y)
    check('entire_exact_column', got['column'] == data['complete_column'] == list(map(enc, column)))
    check('all_fixed_and_free_signs', all(x >= 0 for x in column))
    counts = {(n, l, i): subset_counts(n, l, i) for n in [68, 956] for l in [5, 6] for i in range(l+1)}
    action = []
    for a, (l, i, j) in enumerate(orbits):
        row = []
        for b, (m, u, v) in enumerate(orbits):
            if l == 0:
                y = F(1) if m == 0 else p[m]*weights[b]
            elif m == 0:
                y = p[l]
            else:
                y = sum(counts[68, l, i][m, u, k]*counts[956, l, j][m, v, h]
                        *base[min(l, m), max(l, m), k, h]
                        for k in range(min(l, m)+1) for h in range(min(l, m)+1))
            check(f'every_action_entry_{a}_{b}', enc(y) == got['action'][a][b]
                  and y*data['scale'] == data['integer_action'][a][b])
            row.append(y)
        action.append(row)
    z = [F(*x) for x in got['inverse_action']]
    check('full_inverse_vector_domain', len(z) == 86)
    residuals = [sum(x*y for x, y in zip(row, z))-b for row, b in zip(action, column)]
    for a, x in enumerate(residuals):
        check('full_lifted_inverse_residual_'+str(a), x == 0 and enc(x) == got['inverse_residuals'][a])
    contributions = [w*b*x for w, b, x in zip(weights, column, z)]
    energy = sum(contributions)
    check('all_86_weighted_contributions', list(map(enc, contributions)) == got['weighted_energy_contributions'])
    # Apply the anchor change to the ENTIRE enlarged block, never to C^dagger.
    r = [column[a]-p[l]*p[7] for a, (l, i, j) in enumerate(orbits) if a]
    transported = []
    for a, (l, i, j) in enumerate(orbits[1:], start=1):
        x = sum((action[a][b]-p[l]*p[m]*weights[b])*z[b]
                for b, (m, u, v) in enumerate(orbits[1:], start=1))-r[a-1]
        check('anchor_transported_inverse_residual_'+str(a), x == 0)
        transported.append(x)
    anchor_energy = p[7]**2+sum(w*b*x for w, b, x in zip(weights[1:], r, z[1:]))
    check('anchor_retained_energy_identity', anchor_energy == energy)
    kernel = [[F(*x) for x in row] for row in data['kernel_basis']]
    for a, v in enumerate(kernel):
        check('weighted_kernel_orthogonality_'+str(a), sum(w*x*b for w, x, b in zip(weights, v, column)) == 0)
    summary = got['summary']
    ratio, slack = energy/p[7], p[7]-energy
    check('exact_energy_ratio_and_remainder', summary['energy'] == enc(energy)
          and summary['energy_ratio'] == enc(ratio) and summary['schur_remainder'] == enc(slack)
          and summary['required_diagonal'] == enc(p[7]))
    lo, hi = [F(*x) for x in summary['ratio_interval']]
    check('strict_exact_interval_upper_bound', lo <= ratio < hi)
    verdict = 'PSD_EXTENSION' if slack >= 0 else 'FIXED_COLUMN_REJECTED'
    check('exact_singular_schur_verdict', summary['verdict'] == verdict and energy >= 0)
    out = {'constructor_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
           'rho': enc(rho), 'column': list(map(enc, column)), 'weights': weights,
           'action': [[enc(x) for x in row] for row in action],
           'inverse_action': list(map(enc, z)), 'inverse_residuals': list(map(enc, residuals)),
           'transported_column': list(map(enc, r)), 'transported_residuals': list(map(enc, transported)),
           'anchor_retained_energy': enc(anchor_energy), 'energy': enc(energy), 'energy_ratio': enc(ratio),
           'required_diagonal': enc(p[7]), 'schur_remainder': enc(slack),
           'checks': checks, 'failures': failures,
           'summary': {'checks': len(checks), 'failures': len(failures), 'verdict': verdict,
                       'ratio_interval': [enc(lo), enc(hi)], 'all_full_and_transported_residuals_zero':
                       all(x == 0 for x in residuals+transported)}}
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print('Independent exact checks:', len(checks), '; failures:', failures)
    print('Energy/required diagonal in [', lo, ',', hi, '); required <= 1; verdict:', verdict)
    print('Full certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

"""Exact fixed L065 column energy against the unchanged anchored L061 base.

No optimization or floating point. The complete inverse-action vector,
original row residuals and weighted energy comparison are saved to disk.
"""
import hashlib
import itertools
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import comb, gcd, lcm
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'seven-distance-fixed-column-energy-results.json'
sys.set_int_max_str_digits(0)


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


@lru_cache(None)
def transition(n, l, m, i, u, k):
    return sum(c(i, s)*c(7-i, u-s)*c(l-i, k-s)
               *c(n-7-l+i, m-u-k+s) for s in range(8))


def solve(matrix, rhs):
    """Square exact solve with fraction-free row elimination and back solve."""
    n = len(rhs)
    a = []
    for row, b in zip(matrix, rhs):
        rr = list(row)+[b]
        den = lcm(*(F(x).denominator for x in rr))
        rr = [int(F(x)*den) for x in rr]
        g = gcd(*rr)
        a.append([x//g for x in rr])
    operations = []
    for j in range(n):
        p = next((s for s in range(j, n) if a[s][j]), None)
        if p is None:
            raise ValueError('Singular selected block at column '+str(j))
        if p != j:
            a[j], a[p] = a[p], a[j]
            operations.append(['swap', j, p])
        for s in range(j+1, n):
            if a[s][j]:
                x, y = a[j][j], a[s][j]
                g = gcd(x, y)
                x, y = x//g, y//g
                rr = [x*v-y*w for v, w in zip(a[s], a[j])]
                gg = gcd(*rr)
                a[s] = [v//gg for v in rr]
                operations.append(['eliminate', s, j, x, y, gg])
    z = [F(0)]*n
    for j in reversed(range(n)):
        z[j] = (F(a[j][-1])-sum(a[j][k]*z[k] for k in range(j+1, n)))/a[j][j]
    return z, a, operations


def main():
    paths = [ROOT/'seven-distance-full-base-kernel-results.json',
             ROOT/'seven-distance-full-base-kernel-critical-audit.json',
             ROOT/'simultaneous-shell-ordinary-scalars-results.json']
    data, audit, source = [json.loads(path.read_text()) for path in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for label, old in zip(['kernel', 'kernel_audit', 'dictionary'], [data, audit, source]):
        check(label+'_no_failures', not old['failures'])
    for old in [data, source]:
        for path, h in old['source_hashes'].items():
            check('immutable_'+path, hashlib.sha256((NB/path).read_bytes()).hexdigest() == h)
    p = [F(*v) for v in source['pairs_through_12']]
    check('unchanged_p7', p[7] == F(3539, 248922676958508) == F(*data['p7']))
    orbits = [(0, 0, 0)]+[(l, i, j) for l in [5, 6] for i in range(l+1) for j in range(l+1)]
    weights = [1]+[c(7, i)*c(61, l-i)*c(7, j)*c(949, l-j) for l, i, j in orbits[1:]]
    check('all_original_orbits_and_weights', list(map(list, orbits)) == data['orbits'] == audit['orbits']
          and weights == data['weights'] == audit['weights'])
    base = {tuple(row['type']): F(*row['y']) for row in source['types']}
    check('complete_121_base_entries', len(base) == 121)
    action = []
    for a, (l, i, j) in enumerate(orbits):
        row = []
        for b, (m, u, v) in enumerate(orbits):
            if not l:
                x = F(1) if not m else p[m]*weights[b]
            elif not m:
                x = p[l]
            else:
                x = sum(transition(68, l, m, i, u, k)*transition(956, l, m, j, v, h)
                        *base[min(l, m), max(l, m), k, h]
                        for k in range(min(l, m)+1) for h in range(min(l, m)+1))
            check(f'unchanged_action_{a}_{b}', x*data['scale'] == data['integer_action'][a][b]
                  == audit['integer_action'][a][b])
            row.append(x)
        action.append(row)
    for a in range(86):
        for b in range(a+1):
            check(f'weighted_symmetry_{a}_{b}', weights[a]*action[a][b] == weights[b]*action[b][a])
    affine = data['affine']
    intercept = [F(*x) for x in affine['intercept']]
    slopes = [[F(*x) for x in row] for row in affine['slopes']]
    params = [F(0), F(0), -intercept[4]/slopes[4][2]]
    solution = [v+sum(a*s for a, s in zip(row, params)) for v, row in zip(intercept, slopes)]
    check('fixed_witness_no_parameter_change', list(map(enc, params)) == data['chosen_parameters'])
    check('complete_49_free_coordinates', list(map(enc, solution)) == data['solution'])
    column = []
    for a, rec in enumerate(data['column']):
        x = p[7]*solution[rec['variable']] if rec['kind'] == 'free' else F(*rec['value'])
        check('unchanged_column_'+str(a), enc(x) == data['complete_column'][a] == audit['complete_column'][a])
        column.append(x)
    check('original_anchor_and_signs', column[0] == p[7] and all(x >= 0 for x in column))
    kernel = [[F(*x) for x in row] for row in data['kernel_basis']]
    kernel_residuals = [sum(w*v*b for w, v, b in zip(weights, row, column)) for row in kernel]
    for a, x in enumerate(kernel_residuals):
        check('whole_kernel_compatibility_'+str(a), x == 0)
    selected = data['pivots']
    check('selected_37_coordinates', len(selected) == 37 and len(set(selected)) == 37)
    small = [[action[a][b] for b in selected] for a in selected]
    zz, echelon, operations = solve(small, [column[a] for a in selected])
    z = [F(0)]*86
    for a, x in zip(selected, zz):
        z[a] = x
    residuals = [sum(x*y for x, y in zip(row, z))-b for row, b in zip(action, column)]
    for a, x in enumerate(residuals):
        check('full_anchored_inverse_action_'+str(a), x == 0)
    contributions = [w*b*x for w, b, x in zip(weights, column, z)]
    energy = sum(contributions)
    bilinear = sum(weights[a]*z[a]*action[a][b]*z[b] for a in selected for b in selected)
    check('independent_bilinear_energy_identity', energy == bilinear)
    check('energy_nonnegative', energy >= 0)
    ratio = energy/p[7]
    lower = F(ratio.numerator*10**9//ratio.denominator, 10**9)
    upper = lower+F(1, 10**9)
    check('exact_ratio_interval', lower <= ratio < upper)
    verdict = 'PSD_EXTENSION' if energy <= p[7] else 'FIXED_COLUMN_REJECTED'
    summary = {'checks': len(checks), 'failures': len(failures), 'selected_rank': 37,
               'all_86_inverse_residuals_zero': all(x == 0 for x in residuals),
               'all_49_weighted_kernel_residuals_zero': all(x == 0 for x in kernel_residuals),
               'energy': enc(energy), 'required_diagonal': enc(p[7]), 'energy_ratio': enc(ratio),
               'ratio_interval': [enc(lower), enc(upper)], 'schur_remainder': enc(p[7]-energy),
               'verdict': verdict}
    out = {'input_hashes': {str(path.relative_to(NB)): hashlib.sha256(path.read_bytes()).hexdigest()
                            for path in paths},
           'orbits': list(map(list, orbits)), 'weights': weights,
           'base_entries': [{'type': list(k), 'value': enc(v)} for k, v in base.items()],
           'action': [[enc(v) for v in row] for row in action],
           'parameters': list(map(enc, params)), 'free_solution': list(map(enc, solution)),
           'column': list(map(enc, column)), 'selected': selected,
           'selected_echelon': echelon, 'solve_operations': operations,
           'inverse_action': list(map(enc, z)), 'inverse_residuals': list(map(enc, residuals)),
           'kernel_residuals': list(map(enc, kernel_residuals)),
           'weighted_energy_contributions': list(map(enc, contributions)),
           'bilinear_energy': enc(bilinear), 'summary': summary, 'checks': checks, 'failures': failures}
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print('Exact checks:', len(checks), '; failures:', failures)
    print('Energy/required diagonal lies in [', lower, ',', upper, '); required <= 1.')
    print('Verdict:', verdict, '; all 86 inverse residuals zero:', summary['all_86_inverse_residuals_zero'])
    print('Full certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

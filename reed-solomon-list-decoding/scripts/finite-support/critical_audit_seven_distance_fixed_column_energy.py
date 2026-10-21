"""L066 audit: complete exact trace, actual-set dictionary, weighted lift.

No notebook module or numerical solver imported. The separate verifier
reconstructs all action entries from subset enumeration and manuscript inputs.
This consumes both complete energy certificates and independently replays
the square solve, including each claimed integer division.
"""
import hashlib
import itertools
import json
import sys
from fractions import Fraction as F
from math import comb, gcd, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'seven-distance-fixed-column-energy-critical-audit.json'


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def actual(l, m, i, j):
    d = set(range(68))
    u, v = set(range(m)), set(range(68, 68+m))
    x = set(range(i)) | set(range(m, m+l-i))
    y = set(range(68, 68+j)) | set(range(68+m, 68+m+l-j))
    return d, (d-x) | y, (d-u) | v


def presentations(sets):
    return [[sum(sum(bit for bit, s in zip((4, 2, 1), order) if x in s)
                 == mask for x in range(1024)) for mask in range(8)]
            for order in itertools.permutations(sets)]


def main():
    names = ['seven-distance-fixed-column-energy-results.json',
             'seven-distance-fixed-column-energy-verification.json',
             'seven-distance-full-base-kernel-results.json',
             'seven-distance-full-base-kernel-critical-audit.json',
             'simultaneous-shell-ordinary-scalars-results.json']
    paths = [ROOT / n for n in names]
    a, v, k, ka, source = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('all_failure_lists', all(d['failures'] == [] for d in (a, v, k, ka, source)))
    check('verifier_binding', v['constructor_sha256'] == hashlib.sha256(paths[0].read_bytes()).hexdigest())
    for name, digest in a['input_hashes'].items():
        check('input_'+name, hashlib.sha256((NB/name).read_bytes()).hexdigest() == digest)
    p = [F(*x) for x in source['pairs_through_12']]
    p7 = F(3539, 248922676958508)
    rho = (F(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    check('positive_original_normalization', rho == F(*v['rho']) == F(*source['rho']) == F(*k['rho']) > 0)
    check('original_pairs', p[5:8] == [F(1, 68881143660), F(133, 9357995374380), p7])
    expected_types = [(l, m, i, j) for l, m in ((5, 5), (5, 6), (6, 6))
                      for i in range(l+1) for j in range(l+1)]
    check('complete_base_domain', [tuple(r['type']) for r in source['types']] == expected_types)
    base = {tuple(r['type']): F(*r['value']) for r in a['base_entries']}
    check('complete_certificate_base_domain', set(base) == set(expected_types) and len(a['base_entries']) == 121)
    dictionary, saved_presentations = {}, []
    for row in source['types']:
        typ = tuple(row['type'])
        sets = actual(*typ)
        atoms = presentations(sets)
        value = F(*row['y'])
        check('base_value_'+str(typ), value == base[typ])
        for h, aa in enumerate(atoms):
            check('base_actual_presentation_'+str((typ, h)), aa == row['presentations'][h]['atoms'])
            key = min(map(tuple, atoms))
            check('base_consistency_'+str((typ, h)), key not in dictionary or dictionary[key] == value)
        dictionary[key] = value
        ds = [len(s-t) for s, t in itertools.combinations(sets, 2)]
        if any(1 <= h <= 4 for h in ds):
            check('base_forbidden_'+str(typ), value == 0)
        if len(set(map(frozenset, sets))) < 3:
            check('base_boolean_'+str(typ), value == p[max(ds)])
        saved_presentations.append({'type': list(typ), 'atoms': atoms, 'value': enc(value)})
    orbits = [(0, 0, 0)]+[(l, i, j) for l in (5, 6) for i in range(l+1) for j in range(l+1)]
    weights = [1]+[comb(7, i)*comb(61, l-i)*comb(7, j)*comb(949, l-j) for l, i, j in orbits[1:]]
    check('all_orbits', a['orbits'] == k['orbits'] == ka['orbits'] == list(map(list, orbits)))
    check('all_actual_weights', a['weights'] == v['weights'] == k['weights'] == ka['weights'] == weights and min(weights) > 0)
    for l in (5, 6):
        check('complete_layer_weight_'+str(l), sum(w for o, w in zip(orbits, weights) if o[0] == l) == comb(68, l)*comb(956, l))
    ci = [F(*x) for x in k['affine']['intercept']]
    slopes = [[F(*x) for x in row] for row in k['affine']['slopes']]
    check('active_nonzero', slopes[4][2] != 0)
    params = [F(0), F(0), -ci[4]/slopes[4][2]]
    free = [x+sum(t*s for t, s in zip(params, row)) for x, row in zip(ci, slopes)]
    check('exact_fixed_parameters', a['parameters'] == k['chosen_parameters'] == list(map(enc, params)))
    check('exact_free_values', a['free_solution'] == k['solution'] == list(map(enc, free)))
    column, free_keys, column_presentations = [p7], [], []
    for l, i, j in orbits[1:]:
        atoms = presentations(actual(l, 7, i, j))
        expected = [949-l+j, 7-j, l-j, j, i, l-i, 7-i, 61-l+i]
        check('column_actual_atoms_'+str((l, i, j)), atoms[0] == expected)
        key = min(map(tuple, atoms))
        h = l+7-i-j
        if key in dictionary:
            value = dictionary[key]
        elif 1 <= h <= 4:
            value = F(0)
        else:
            check('distinct_free_'+str((l, i, j)), key not in free_keys)
            free_keys.append(key)
            value = p7*free[len(free_keys)-1]
        if 1 <= h <= 4:
            check('all_forbidden_'+str((l, i, j)), value == 0)
        column.append(value)
        column_presentations.append({'orbit': [l, i, j], 'atoms': atoms, 'value': enc(value)})
    check('entire_fixed_column', len(free_keys) == 49 and list(map(enc, column)) == a['column'] == v['column'] == k['complete_column'] == ka['complete_column'])
    check('column_nonnegative', min(column) >= 0)
    Q = [[F(*x) for x in row] for row in a['action']]
    check('action_shape', len(Q) == 86 and all(len(row) == 86 for row in Q))
    for i in range(86):
        for j in range(86):
            check(f'action_binding_{i}_{j}', enc(Q[i][j]) == v['action'][i][j] and Q[i][j]*k['scale'] == k['integer_action'][i][j] == ka['integer_action'][i][j])
            check(f'weighted_symmetry_{i}_{j}', weights[i]*Q[i][j] == weights[j]*Q[j][i])
    P = [0,1,2,3,4,5,7,8,9,10,13,14,15,19,20,21,25,37,38,39,40,44,45,46,47,51,52,53,54,58,59,60,65,66,72,73,79]
    check('manuscript_selection', a['selected'] == P)
    rows, scaling = [], []
    for i in P:
        row = [Q[i][j] for j in P]+[column[i]]
        d = lcm(*(x.denominator for x in row))
        ints = [int(x*d) for x in row]
        g = gcd(*ints)
        check('initial_scaling_'+str(i), d > 0 and g > 0 and all(x % g == 0 for x in ints))
        rows.append([x//g for x in ints])
        scaling.append([d, g])
    for n, op in enumerate(a['solve_operations']):
        if op[0] == 'swap':
            _, i, j = op
            check('swap_indices_'+str(n), 0 <= i < 37 and 0 <= j < 37 and i != j)
            rows[i], rows[j] = rows[j], rows[i]
        else:
            tag, s, j, x, y, g = op
            check('elimination_invertible_'+str(n), tag == 'eliminate' and 0 <= j < s < 37 and x != 0 and g > 0)
            rr = [x*b-y*c for b, c in zip(rows[s], rows[j])]
            check('exact_division_'+str(n), gcd(*rr) == g and all(b % g == 0 for b in rr) and rr[j] == 0)
            rows[s] = [b//g for b in rr]
    check('complete_echelon', rows == a['selected_echelon'])
    zz = [F(0)]*37
    for i in reversed(range(37)):
        check('nonzero_triangular_pivot_'+str(i), rows[i][i] != 0 and all(rows[i][j] == 0 for j in range(i)))
        zz[i] = (F(rows[i][-1])-sum(F(rows[i][j])*zz[j] for j in range(i+1, 37)))/F(rows[i][i])
    z = [F(0)]*86
    for i, val in zip(P, zz):
        z[i] = val
    check('independent_backsolve', list(map(enc, z)) == a['inverse_action'] == v['inverse_action'])
    residuals, transported = [], []
    r = [column[i]-p[o[0]]*p7 for i, o in enumerate(orbits) if i]
    for i, row in enumerate(Q):
        res = sum(x*y for x, y in zip(row, z))-column[i]
        residuals.append(res)
        check('original_row_'+str(i), res == 0 and enc(res) == a['inverse_residuals'][i] == v['inverse_residuals'][i])
        if i:
            res = sum((Q[i][j]-p[orbits[i][0]]*p[orbits[j][0]]*weights[j])*z[j] for j in range(1, 86))-r[i-1]
            transported.append(res)
            check('transported_row_'+str(i), res == 0 and enc(res) == v['transported_residuals'][i-1])
    check('complete_transported_column', list(map(enc, r)) == v['transported_column'])
    kr = []
    for i, row in enumerate(k['kernel_basis']):
        res = sum(w*F(*t)*b for w, t, b in zip(weights, row, column))
        kr.append(res)
        check('kernel_row_'+str(i), res == 0 and enc(res) == a['kernel_residuals'][i])
    terms = [w*b*x for w, b, x in zip(weights, column, z)]
    E = sum(terms)
    anchor_terms = [p7*p7]+[w*b*x for w, b, x in zip(weights[1:], r, z[1:])]
    check('all_energy_terms', list(map(enc, terms)) == a['weighted_energy_contributions'])
    check('anchor_energy_identity', sum(anchor_terms) == E and enc(E) == v['anchor_retained_energy'])
    bilinear = sum(weights[i]*z[i]*Q[i][j]*z[j] for i in P for j in P)
    check('bilinear', E == bilinear and enc(E) == a['bilinear_energy'])
    ratio, remainder = E/p7, p7-E
    for label, value in [('energy', E), ('energy_ratio', ratio), ('required_diagonal', p7), ('schur_remainder', remainder)]:
        check('full_fraction_'+label, enc(value) == a['summary'][label] == v[label])
    lower_gap = 10**9*ratio.numerator-3*ratio.denominator
    upper_gap = 4*ratio.denominator-10**9*ratio.numerator
    check('lower_cross_product', lower_gap >= 0)
    check('strict_upper_cross_product', upper_gap > 0)
    check('positive_schur_remainder', E >= 0 and remainder > 0)
    interval = [enc(F(3, 10**9)), enc(F(4, 10**9))]
    check('reported_interval', a['summary']['ratio_interval'] == v['summary']['ratio_interval'] == interval)
    check('reported_verdict', a['summary']['verdict'] == v['summary']['verdict'] == 'PSD_EXTENSION')
    summary = {'checks': len(checks), 'failures': len(failures), 'solve_operations_replayed': len(a['solve_operations']),
               'original_rows': 86, 'transported_rows': 85, 'ratio_interval': interval,
               'required_ratio_upper_bound': 1, 'verdict': 'RETAIN_L066' if not failures else 'AUDIT_FAILED'}
    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'base_presentations': saved_presentations, 'column_presentations': column_presentations,
           'orbits': list(map(list, orbits)), 'weights': weights, 'action': a['action'],
           'initial_row_scalings': scaling, 'replayed_echelon': rows, 'selected': P,
           'inverse_action': list(map(enc, z)), 'column': list(map(enc, column)),
           'inverse_residuals': list(map(enc, residuals)), 'transported_residuals': list(map(enc, transported)),
           'kernel_residuals': list(map(enc, kr)), 'energy_contributions': list(map(enc, terms)),
           'anchor_energy_contributions': list(map(enc, anchor_terms)), 'energy': enc(E),
           'required_diagonal': enc(p7), 'energy_ratio': enc(ratio), 'schur_remainder': enc(remainder),
           'lower_cross_product_gap': lower_gap, 'upper_cross_product_gap': upper_gap,
           'summary': summary, 'checks': checks, 'failures': failures}
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print('Checks:', len(checks), '; failures:', failures)
    print('Full trace operations:', len(a['solve_operations']), '; original/transported zero residuals: 86/85')
    print('Actual E/p7 in [3/10^9,4/10^9); required <= 1; verdict:', summary['verdict'])
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

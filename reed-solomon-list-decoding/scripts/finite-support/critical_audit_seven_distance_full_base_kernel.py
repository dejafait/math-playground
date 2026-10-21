"""L065 critical audit: actual sets, subset counts, exact row operations.

Consumes both complete certificates. No notebook implementation, optimizer,
decimal arithmetic or mathematical package is imported. Energy is not tested.
"""
import hashlib
import itertools
import json
import sys
from collections import Counter
from fractions import Fraction as F
from math import comb, gcd, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'seven-distance-full-base-kernel-critical-audit.json'


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def decode(rows):
    return [[F(*x) for x in row] for row in rows]


def actual_presentations(sets):
    return [[sum(sum(bit for bit, support in zip((4, 2, 1), order)
                     if x in support) == mask for x in range(1024))
             for mask in range(8)] for order in itertools.permutations(sets)]


def actual_triple(l, m, i, j):
    d = set(range(68))
    u, v = set(range(m)), set(range(68, 68+m))
    x = set(range(i)) | set(range(m, m+l-i))
    y = set(range(68, 68+j)) | set(range(68+m, 68+m+l-j))
    return d, (d-x) | y, (d-u) | v


def subset_counts(n, l, i):
    """Enumerate actual subsets of X union U, then choose outside points.

    This independently evaluates every T(n,l,m,i,u,k) for m=5,6.
    There are at most 2^13 explicitly enumerated subsets.
    """
    u, x = set(range(7)), set(range(i)) | set(range(7, 7+l-i))
    points = sorted(u | x)
    counts = {(m, a, k): 0 for m in (5, 6)
              for a in range(m+1) for k in range(min(l, m)+1)}
    for mask in range(1 << len(points)):
        chosen = {point for j, point in enumerate(points) if mask >> j & 1}
        a, k, s = len(chosen & u), len(chosen & x), len(chosen)
        for m in (5, 6):
            if s <= m:
                counts[m, a, k] += comb(n-len(points), m-s)
    return counts


def main():
    paths = [ROOT / name for name in (
        'seven-distance-full-base-kernel-results.json',
        'seven-distance-full-base-kernel-verification.json',
        'simultaneous-shell-ordinary-scalars-results.json')]
    data, verification, source = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('both_complete_certificates_no_failures',
          data['failures'] == verification['failures'] == [])
    check('verification_binds_complete_constructor', verification['constructor_sha256']
          == hashlib.sha256(paths[0].read_bytes()).hexdigest())
    for name, digest in data['source_hashes'].items():
        check('immutable_'+name, hashlib.sha256((NB/name).read_bytes()).hexdigest() == digest)
    check('reported_check_counts', len(data['checks']) == 4412
          and len(verification['checks']) == 12638)
    pairs = [F(*p) for p in source['pairs_through_12']]
    rho = (F(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    check('original_positive_rho', F(*data['rho']) == F(*source['rho']) == rho > 0)
    check('original_retained_pairs', pairs[5:8] == [F(1, 68881143660),
          F(133, 9357995374380), F(3539, 248922676958508)])

    dictionary, base, base_presentations = {}, {}, []
    required = [(l, m, i, j) for l, m in ((5, 5), (5, 6), (6, 6))
                for i in range(min(l, m)+1) for j in range(min(l, m)+1)]
    check('exact_base_domain_order', [tuple(r['type']) for r in source['types']] == required)
    for row in source['types']:
        typ = tuple(row['type'])
        sets = actual_triple(*typ)
        aa = actual_presentations(sets)
        y = F(*row['y'])
        for order, (got, saved) in enumerate(zip(aa, row['presentations'])):
            check(f'actual_base_atoms_{typ}_{order}', got == saved['atoms'])
        key = min(map(tuple, aa))
        check('unordered_base_consistency_'+str(typ), key not in dictionary or dictionary[key] == y)
        check('base_nonnegative_'+str(typ), y >= 0)
        distances = [len(a-b) for a, b in itertools.combinations(sets, 2)]
        if any(1 <= h <= 4 for h in distances):
            check('base_forbidden_'+str(typ), y == 0)
        if len(set(map(frozenset, sets))) == 2:
            check('base_boolean_'+str(typ), y == pairs[max(distances)])
        dictionary[key], base[typ] = y, y
        base_presentations.append({'type': list(typ), 'presentations': aa, 'value': enc(y)})

    orbits = [(0, 0, 0)]+[(l, i, j) for l in (5, 6)
                         for i in range(l+1) for j in range(l+1)]
    weights = [1]+[comb(7, i)*comb(61, l-i)*comb(7, j)*comb(949, l-j)
                   for l, i, j in orbits[1:]]
    check('every_orbit_and_weight', data['orbits'] == list(map(list, orbits))
          and data['weights'] == weights and min(weights) > 0)
    for l in (5, 6):
        check('layer_weight_sum_'+str(l), sum(w for (m, _, _), w in zip(orbits, weights) if m == l)
              == comb(68, l)*comb(956, l))
    complete = [F(*v) for v in data['complete_column']]
    solution = [F(*v) for v in data['solution']]
    free_keys, kinds, column_presentations = [], Counter(), []
    for z, (l, i, j) in enumerate(orbits):
        rec = data['column'][z]
        check('column_orbit_'+str(z), rec['orbit'] == [l, i, j])
        if l == 0:
            check('anchor_fixed', rec['kind'] == 'anchor' and F(*rec['value']) == complete[z] == pairs[7])
            kinds['anchor'] += 1
            continue
        sets = actual_triple(l, 7, i, j)
        aa = actual_presentations(sets)
        key = min(map(tuple, aa))
        distances = [len(sets[0]-sets[1]), len(sets[0]-sets[2]), len(sets[1]-sets[2])]
        check('column_sizes_distinct_'+str(z), all(len(s) == 68 for s in sets)
              and len(set(map(frozenset, sets))) == 3)
        check('column_all_presentations_'+str(z), aa == rec['presentations'] and aa[0] == rec['atoms'])
        check('column_key_weight_distances_'+str(z), list(key) == rec['key']
              and weights[z] == rec['weight'] and distances == rec['half_distances'])
        forbidden = any(1 <= h <= 4 for h in distances)
        if key in dictionary:
            kind, value = 'represented', dictionary[key]
            check('all_fixed_lookup_values_'+str(z), F(*rec['value']) == value == complete[z])
        elif forbidden:
            kind, value = 'forbidden', F(0)
            check('all_forbidden_values_'+str(z), F(*rec['value']) == value == complete[z])
        else:
            kind = 'free'
            check('free_keys_distinct_'+str(z), key not in free_keys)
            free_keys.append(key)
            check('free_variable_entry_'+str(z), rec['variable'] == len(free_keys)-1
                  and complete[z] == pairs[7]*solution[len(free_keys)-1])
        if forbidden:
            check('forbidden_including_represented_'+str(z), complete[z] == 0)
        check('column_kind_nonnegative_'+str(z), kind == rec['kind'] and complete[z] >= 0)
        kinds[kind] += 1
        column_presentations.append({'orbit': [l, i, j], 'presentations': aa, 'key': list(key)})
    check('exact_kind_counts', dict(kinds) == {'anchor': 1, 'represented': 20, 'forbidden': 16, 'free': 49})
    check('free_key_order', list(map(list, free_keys)) == data['free_keys'])

    transitions = {(n, l, i): subset_counts(n, l, i) for n in (68, 956)
                   for l in (5, 6) for i in range(l+1)}
    for (n, l, i), table in transitions.items():
        for m in (5, 6):
            for u in range(m+1):
                check(f'count_orbit_total_{n}_{l}_{i}_{m}_{u}',
                      sum(table[m, u, k] for k in range(min(l, m)+1)) == comb(7, u)*comb(n-7, m-u))
    scale = lcm(*(v.denominator for v in list(base.values())+pairs))
    check('exact_integer_scale', scale == data['scale'] and scale > 0)
    action = []
    for a, (l, i, j) in enumerate(orbits):
        rr = []
        for b, (m, u, v) in enumerate(orbits):
            if l == 0:
                value = F(1) if m == 0 else pairs[m]*weights[b]
            elif m == 0:
                value = pairs[l]
            else:
                value = sum(transitions[68, l, i][m, u, k]*transitions[956, l, j][m, v, h]
                            *base[min(l, m), max(l, m), k, h]
                            for k in range(min(l, m)+1) for h in range(min(l, m)+1))
            check(f'actual_subset_action_{a}_{b}', value*scale == data['integer_action'][a][b])
            rr.append(int(value*scale))
        action.append(rr)
    for a in range(86):
        for b in range(a+1):
            check(f'weighted_self_adjoint_{a}_{b}', weights[a]*action[a][b] == weights[b]*action[b][a])

    def replay(matrix, operations, pivots, saved, label):
        rows = []
        for row in matrix:
            den = lcm(*(F(v).denominator for v in row))
            rows.append([int(F(v)*den) for v in row])
        for step, operation in enumerate(operations):
            tag, *args = operation
            if tag == 'swap':
                a, b = args
                rows[a], rows[b] = rows[b], rows[a]
                ok = a != b
            elif tag == 'divide':
                a, divisor = args
                ok = divisor != 0 and all(v % divisor == 0 for v in rows[a])
                rows[a] = [v//divisor for v in rows[a]]
            else:
                assert tag == 'eliminate'
                a, b, x, y, divisor = args
                fresh = [x*v-y*w for v, w in zip(rows[a], rows[b])]
                ok = a != b and x != 0 and (divisor == 0 and not any(fresh)
                        or divisor != 0 and all(v % divisor == 0 for v in fresh))
                rows[a] = [v//divisor for v in fresh] if divisor else fresh
            check(f'{label}_invertible_operation_{step}', ok)
        reduced = [[F(v) for v in row] for row in rows]
        check(label+'_pivots_increasing', pivots == sorted(set(pivots)))
        for r, j in enumerate(pivots):
            check(f'{label}_echelon_{r}', all(reduced[r][k] == 0 for k in range(j)) and reduced[r][j] != 0)
        check(label+'_zero_tail', all(not any(row) for row in reduced[len(pivots):]))
        for r in reversed(range(len(pivots))):
            j = pivots[r]
            divisor = reduced[r][j]
            reduced[r] = [v/divisor for v in reduced[r]]
            for a in range(r):
                value = reduced[a][j]
                reduced[a] = [v-value*w for v, w in zip(reduced[a], reduced[r])]
        for a, (got, wanted) in enumerate(zip(reduced, decode(saved))):
            check(f'{label}_entire_rref_row_{a}', got == wanted)
        return reduced

    rr = replay(action, data['echelon_operations'], data['pivots'], data['rref'], 'base')
    check('base_rank_exact', len(data['pivots']) == data['rank'] == 37)
    nonpivots = [j for j in range(86) if j not in data['pivots']]
    kernel = []
    for j in nonpivots:
        vector = [F(k == j) for k in range(86)]
        for r, p in enumerate(data['pivots']):
            vector[p] = -rr[r][j]
        kernel.append(vector)
    check('entire_canonical_kernel', kernel == decode(data['kernel_basis']) and len(kernel) == 49)
    equations, rhs, weighted_residuals = [], [], []
    for k, vector in enumerate(kernel):
        check('kernel_action_'+str(k), all(sum(a*b for a, b in zip(row, vector)) == 0 for row in action))
        row, value = [F(0)]*49, F(0)
        for z, rec in enumerate(data['column']):
            coefficient = weights[z]*vector[z]
            if rec['kind'] == 'free':
                row[rec['variable']] += coefficient*pairs[7]
            else:
                value -= coefficient*complete[z]
        normalizer = max(map(abs, row))
        if normalizer:
            row, value = [v/normalizer for v in row], value/normalizer
        equations.append(row)
        rhs.append(value)
        check('complete_original_equation_'+str(k), row == decode([data['equations'][k]])[0]
              and value == F(*data['rhs'][k]))
        residual = sum(w*v*b for w, v, b in zip(weights, vector, complete))
        weighted_residuals.append(enc(residual))
        check('complete_weighted_residual_'+str(k), residual == 0)
    er = replay([row+[b] for row, b in zip(equations, rhs)], data['equation_operations'],
                data['equation_pivots'], data['equation_rref'], 'compatibility')
    free = [j for j in range(49) if j not in data['equation_pivots']]
    check('rank_46_three_parameters', len(data['equation_pivots']) == 46
          and free == data['affine']['free_indices'] == [27, 33, 42])
    ci, cs = [F(0)]*49, [[F(j == k) for k in free] for j in range(49)]
    for r, j in enumerate(data['equation_pivots']):
        ci[j], cs[j] = er[r][-1], [-er[r][k] for k in free]
    check('complete_canonical_affine_intercept', ci == [F(*x) for x in data['affine']['intercept']])
    check('complete_canonical_affine_slopes', cs == decode(data['affine']['slopes']))
    check('active_denominator_nonzero', cs[4][2] != 0)
    params = [F(0), F(0), -ci[4]/cs[4][2]]
    fresh_solution = [b+sum(a*t for a, t in zip(row, params)) for b, row in zip(ci, cs)]
    check('exact_active_set_witness', fresh_solution == solution and params[2] > 0)
    for j, v in enumerate(solution):
        check('every_exact_free_sign_'+str(j), v == 0 if j in (4, 27, 33) else v > 0)
    zero_keys = [list(free_keys[j]) for j in (4, 27, 33)]
    check('manuscript_zero_keys', zero_keys == [[948,0,1,7,3,5,4,56],
          [949,0,0,7,1,6,6,55], [948,1,1,6,2,5,5,56]])
    basis = data['decimal_proposal']['basis']
    active = [j for j in range(49) if 3+j not in basis]
    active += [free[j] for j in range(3) if j not in basis and free[j] not in active]
    check('corrected_active_extraction', active == data['active_zero_indices'] == [4, 27, 33])
    # The decimal status/value/trace is not mathematical evidence.
    for k, (row, value) in enumerate(zip(equations, rhs)):
        check('fresh_active_solution_equation_'+str(k), sum(a*b for a, b in zip(row, fresh_solution)) == value)
        check('canonical_intercept_equation_'+str(k), sum(a*b for a, b in zip(row, ci)) == value)
        for s in range(3):
            check(f'canonical_affine_null_{k}_{s}', sum(a*b[s] for a, b in zip(row, cs)) == 0)
    check('both_certificates_complete_column', data['complete_column'] == verification['complete_column'])
    check('both_certificates_complete_solution', data['solution'] == verification['solution'])
    check('both_certificates_parameters', data['chosen_parameters'] == verification['parameters'] == list(map(enc, params)))
    check('verification_rank_and_signs', verification['summary']['base_rank'] == 37
          and verification['summary']['equation_rank'] == 46
          and verification['summary']['strictly_positive_free_coordinates'] == 46
          and verification['summary']['all_original_weighted_kernel_residuals_zero'])
    summary = {'checks': len(checks), 'failures': len(failures), 'base_orbits': 86,
               'base_rank': 37, 'kernel_dimension': 49, 'equation_rank': 46,
               'affine_dimension': 3, 'positive_free_entries': 46, 'zero_free_entries': 3,
               'all_weighted_residuals_zero': all(r == [0, 1] for r in weighted_residuals),
               'base_operations': len(data['echelon_operations']),
               'equation_operations': len(data['equation_operations']),
               'energy_tested': False}
    out = {'source_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'summary': summary, 'checks': checks, 'failures': failures,
           'base_actual_presentations': base_presentations,
           'column_actual_presentations': column_presentations,
           'subset_transitions': [{'n_l_i': list(key), 'counts': [[*k, v] for k, v in table.items()]}
                                  for key, table in transitions.items()],
           'orbits': list(map(list, orbits)), 'weights': weights, 'integer_action': action,
           'complete_column': list(map(enc, complete)), 'fresh_solution': list(map(enc, fresh_solution)),
           'active_parameter': list(map(enc, params)), 'active_denominator': enc(cs[4][2]),
           'zero_keys': zero_keys, 'whole_kernel_residuals': weighted_residuals}
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Required: all free signs >= 0; every original weighted kernel residual = 0. No energy verdict.')
    print('Failures:', failures)
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit('Critical audit failed')


if __name__ == '__main__':
    main()

"""Whole-base prescribed distance-seven kernel diagnostic.

Exact orbit action and full kernel certificates; decimal phase I, if needed,
only proposes a rational active set. Writes all evidence before printing.
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
OUT = ROOT / 'seven-distance-full-base-kernel-results.json'
sys.set_int_max_str_digits(0)


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def atom_orders(atoms):
    result = []
    for order in itertools.permutations(range(3)):
        out = [0]*8
        for mask, size in enumerate(atoms):
            bits = [(mask >> k) & 1 for k in [2, 1, 0]]
            new = sum(bits[old] << (2-new) for new, old in enumerate(order))
            out[new] = size
        result.append(out)
    return result


def atoms(l, m, i, j):
    return [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]


@lru_cache(None)
def transition(n, l, m, i, u, k):
    return sum(c(i, s)*c(7-i, u-s)*c(l-i, k-s)
               *c(n-7-l+i, m-u-k+s) for s in range(8))


def rref(matrix):
    """Fraction-free echelon, rational back reduction; row identities saved."""
    a = []
    for row in matrix:
        den = lcm(*(F(v).denominator for v in row))
        a.append([int(F(v)*den) for v in row])
    pivots, operations = [], []
    r = 0
    for j in range(len(a[0])):
        p = next((s for s in range(r, len(a)) if a[s][j]), None)
        if p is None:
            continue
        if p != r:
            a[r], a[p] = a[p], a[r]
            operations.append(['swap', r, p])
        g = gcd(*a[r])
        if g:
            a[r] = [v//g for v in a[r]]
            operations.append(['divide', r, g])
        for s in range(r+1, len(a)):
            if a[s][j]:
                x, y = a[r][j], a[s][j]
                g = gcd(x, y)
                x, y = x//g, y//g
                a[s] = [x*v-y*w for v, w in zip(a[s], a[r])]
                gg = gcd(*a[s])
                if gg:
                    a[s] = [v//gg for v in a[s]]
                operations.append(['eliminate', s, r, x, y, gg])
        pivots.append(j)
        r += 1
        if r == len(a):
            break
    a = [[F(v) for v in row] for row in a]
    for r in reversed(range(len(pivots))):
        j = pivots[r]
        v = a[r][j]
        a[r] = [x/v for x in a[r]]
        for s in range(r):
            v = a[s][j]
            if v:
                a[s] = [x-v*y for x, y in zip(a[s], a[r])]
    return a, pivots, operations


def main():
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    paths = [ROOT / 'simultaneous-shell-ordinary-scalars-results.json',
             ROOT / 'simultaneous-shell-ordinary-scalars-verification.json',
             ROOT / 'simultaneous-five-six-shell-verification.json']
    source, scalar_ver, psd = [json.loads(p.read_text()) for p in paths]
    check('input_failures_empty', all(not v['failures'] for v in [source, scalar_ver, psd]))
    check('input_hashes_match', all(hashlib.sha256((NB/name).read_bytes()).hexdigest() == h
                                  for name, h in source['source_hashes'].items()))
    pairs = [F(*v) for v in source['pairs_through_12']]
    rho = F(*source['rho'])
    check('unchanged_positive_rho_p7', rho > 0 and pairs[7] == F(3539, 248922676958508))
    dictionary, base = {}, {}
    for row in source['types']:
        key = min(tuple(p['atoms']) for p in row['presentations'])
        value = F(*row['y'])
        check('immutable_key_'+str(row['type']), key not in dictionary or dictionary[key] == value)
        dictionary[key] = value
        base[tuple(row['type'])] = value
    check('complete_121_type_input', len(base) == 121)

    orbits = [(0, 0, 0)]+[(l, i, j) for l in [5, 6]
                         for i in range(l+1) for j in range(l+1)]
    weights = [1]+[c(7, i)*c(61, l-i)*c(7, j)*c(949, l-j)
                   for l, i, j in orbits[1:]]
    for l in [5, 6]:
        check('orbit_weight_sum_'+str(l), sum(w for o, w in zip(orbits, weights) if o[0] == l)
              == c(68, l)*c(956, l))

    def value(l, m, k, h):
        return base[l, m, k, h] if l <= m else base[m, l, k, h]

    scale = lcm(*(v.denominator for v in list(base.values())+pairs))
    ibase = {key: int(v*scale) for key, v in base.items()}

    def ivalue(l, m, k, h):
        return ibase[l, m, k, h] if l <= m else ibase[m, l, k, h]

    action = []
    for l, i, j in orbits:
        row = []
        for z, (m, u, v) in enumerate(orbits):
            if not l:
                entry = scale if not m else int(scale*pairs[m])*weights[z]
            elif not m:
                entry = int(scale*pairs[l])
            else:
                entry = sum(transition(68, l, m, i, u, k)
                            *transition(956, l, m, j, v, h)*ivalue(l, m, k, h)
                            for k in range(min(l, m)+1) for h in range(min(l, m)+1))
            row.append(entry)
        action.append(row)
    for a in range(86):
        for b in range(a+1):
            check(f'weighted_symmetry_{a}_{b}', weights[a]*action[a][b] == weights[b]*action[b][a])
    for n in [68, 956]:
        for l in [5, 6]:
            for m in [5, 6]:
                for i in range(l+1):
                    for u in range(m+1):
                        check(f'transition_total_{n}_{l}_{m}_{i}_{u}',
                              sum(transition(n, l, m, i, u, k) for k in range(min(l, m)+1))
                              == c(7, u)*c(n-7, m-u))
    records, free_keys = [], []
    for z, (l, i, j) in enumerate(orbits):
        if not l:
            records.append({'orbit': [l, i, j], 'kind': 'anchor', 'value': enc(pairs[7])})
            continue
        aa = atoms(l, 7, i, j)
        orders = atom_orders(aa)
        key = min(map(tuple, orders))
        check(f'all_column_presentations_{l}_{i}_{j}', all(
            sum(v) == 1024 and min(v) >= 0
            and all(sum(v[k] for k in range(8) if k & bit) == 68 for bit in [1, 2, 4])
            for v in orders))
        h = l+7-i-j
        forbidden = 1 <= h <= 4
        if key in dictionary:
            kind, y = 'represented', dictionary[key]
            check(f'forbidden_lookup_consistent_{l}_{i}_{j}', not forbidden or y == 0)
        elif forbidden:
            kind, y = 'forbidden', F(0)
        else:
            kind, y = 'free', None
            if key not in free_keys:
                free_keys.append(key)
        rec = {'orbit': [l, i, j], 'kind': kind, 'key': list(key),
               'atoms': aa, 'presentations': orders, 'half_distances': [l, 7, h],
               'weight': weights[z]}
        if y is not None:
            rec['value'] = enc(y)
        else:
            rec['variable'] = free_keys.index(key)
        records.append(rec)

    out = {'source_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'rho': enc(rho), 'p7': enc(pairs[7]), 'scale': scale,
           'orbits': [list(v) for v in orbits], 'weights': weights,
           'column': records, 'free_keys': list(map(list, free_keys)),
           'integer_action': action, 'checks': checks, 'failures': failures,
           'stage': 'action_constructed'}
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print('Full invariant action constructed:', len(action), 'coordinates;', len(free_keys), 'free keys', flush=True)
    rr, pivots, ops = rref(action)
    nonpivots = [j for j in range(86) if j not in pivots]
    kernel = []
    for j in nonpivots:
        v = [F(0)]*86
        v[j] = F(1)
        for r, k in enumerate(pivots):
            v[k] = -rr[r][j]
        check('kernel_residual_'+str(j), all(sum(x*y for x, y in zip(row, v)) == 0 for row in action))
        kernel.append(v)
    check('full_echelon_zero_rows', all(not any(row) for row in rr[len(pivots):]))
    # Scale free column entries by p7, a strictly positive known input.
    eq, rhs = [], []
    for v in kernel:
        row = [F(0)]*len(free_keys)
        b = F(0)
        for w, k, rec in zip(weights, v, records):
            if rec['kind'] == 'free':
                row[rec['variable']] += w*k*pairs[7]
            else:
                b -= w*k*F(*rec['value'])
        norm = max(map(abs, row))
        if norm:
            row, b = [x/norm for x in row], b/norm
        eq.append(row)
        rhs.append(b)
    out.update({'stage': 'kernel_constructed', 'rank': len(pivots), 'pivots': pivots,
                'echelon_operations': ops, 'rref': [[enc(x) for x in row] for row in rr],
                'kernel_basis': [[enc(x) for x in row] for row in kernel],
                'equations': [[enc(x) for x in row] for row in eq], 'rhs': list(map(enc, rhs))})
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print('Exact invariant rank/kernel:', len(pivots), len(kernel), flush=True)
    reduced, epiv, eops = rref([row+[b] for row, b in zip(eq, rhs)])
    consistent = len(free_keys) not in epiv
    out.update({'equation_pivots': epiv, 'equation_rref': [[enc(x) for x in row] for row in reduced],
                'equation_operations': eops, 'equation_consistent': consistent})
    verdict = 'unfinished'
    if consistent:
        epfree = [j for j in range(len(free_keys)) if j not in epiv]
        intercept = [F(0)]*len(free_keys)
        slopes = [[F(0)]*len(epfree) for _ in free_keys]
        for a, j in enumerate(epfree):
            slopes[j][a] = F(1)
        for r, j in enumerate(epiv):
            intercept[j] = reduced[r][-1]
            slopes[j] = [-reduced[r][k] for k in epfree]
        out['affine'] = {'free_indices': epfree, 'intercept': list(map(enc, intercept)),
                         'slopes': [[enc(x) for x in row] for row in slopes]}
        params = [F(0)]*len(epfree)
        active = []
        if any(v < 0 for v in intercept) and epfree:
            from simultaneous_five_six_shell import propose, solve
            proposal = propose([[-x for x in row] for row in slopes], intercept)
            out['decimal_proposal'] = proposal
            active = [j for j in range(len(free_keys)) if len(epfree)+j not in proposal['basis']]
            active += [epfree[j] for j in range(len(epfree)) if j not in proposal['basis']
                       and epfree[j] not in active]
            if proposal['status'] == 'feasible_proposal' and len(active) == len(epfree):
                params = solve([slopes[j] for j in active], [-intercept[j] for j in active])
        solution = [b+sum(a*t for a, t in zip(row, params)) for b, row in zip(intercept, slopes)]
        if all(v >= 0 for v in solution):
            verdict = 'compatible_nonnegative_column'
            check('all_original_equations', all(sum(a*t for a, t in zip(row, solution)) == b
                  for row, b in zip(eq, rhs)))
            column = [pairs[7]*solution[rec['variable']] if rec['kind'] == 'free'
                      else F(*rec['value']) for rec in records]
            for j, v in enumerate(kernel):
                check('complete_weighted_column_kernel_'+str(j), sum(w*k*b for w, k, b in zip(weights, v, column)) == 0)
            check('whole_column_nonnegative', all(v >= 0 for v in column))
            out.update({'solution': list(map(enc, solution)), 'complete_column': list(map(enc, column)),
                        'chosen_parameters': list(map(enc, params)), 'active_zero_indices': active})
        else:
            out['failed_candidate'] = list(map(enc, solution))
            out['candidate_negative_indices'] = [j for j, v in enumerate(solution) if v < 0]
    out.update({'stage': 'completed' if verdict != 'unfinished' else 'exact_system_saved',
                'verdict': verdict, 'checks': checks, 'failures': failures,
                'summary': {'orbits': 86, 'rank': len(pivots), 'kernel_dimension': len(kernel),
                            'free_keys': len(free_keys), 'equation_rank': len(epiv),
                            'affine_dimension': len(free_keys)-len(epiv) if consistent else None,
                            'kinds': {k: sum(v['kind'] == k for v in records) for k in ['anchor','represented','forbidden','free']},
                            'checks': len(checks), 'failures': len(failures), 'verdict': verdict}})
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out['summary'], sort_keys=True))
    print('Required bound: every free entry >= 0; every complete weighted kernel residual = 0.')
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit('Failures: '+str(failures))


if __name__ == '__main__':
    main()

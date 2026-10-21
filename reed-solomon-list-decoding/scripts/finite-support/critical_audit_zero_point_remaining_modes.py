"""L071 critical audit: manuscript, actual subset actions and original separator.

Standard library only. Ancestral decomposition/kernel theorems are imported;
their finite data are checked at the prescribed point, without an optimizer.
"""
import hashlib
import itertools as it
import json
import re
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'zero-point-remaining-modes-critical-audit.json'


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [enc(v) for v in x]
    return x


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def dot(x, y):
    assert len(x) == len(y)
    return sum((a*b for a, b in zip(x, y)), F(0))


@lru_cache(None)
def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*c(u, t)*c(n-2*a, u-a)
               *c(n-a-u, l-u)*c(n-a-u, m-u)
               for u in range(max(a, t), min(l, m, n-a)+1))


def eigen(n, a, r):
    return sum((-1)**s*c(a, s)*c(7-a, r-s)*c(n-7-a, r-s)
               for s in range(r+1))


def main():
    names = ['zero-point-remaining-modes-results.json',
             'zero-point-remaining-modes-verification.json',
             'zero-point-tight-modes-results.json',
             'simultaneous-shell-ordinary-scalars-results.json',
             'seven-distance-full-base-kernel-results.json',
             'seven-shell-affine-fixed-dual-results.json',
             'zero-dual-plane-scalars-results.json',
             'simultaneous-seven-shell-critical-audit.json']
    paths = [ROOT/n for n in names]
    result, verified, tight, old, col, square, point, prior = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for path, obj in zip(paths, [result, verified, tight, old, col, square, point, prior]):
        check('clean_'+path.name, obj['failures'] == [])
        for rel, digest in obj.get('input_hashes', obj.get('source_hashes', {})).items():
            check('hash_'+path.name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p = [F(*v) for v in point['pairs_through_13']]
    rho = (F(c(1024, 64), c(68, 64))+1)/(2*c(1024, 68))
    check('original_positive_normalizations', rho > 0 and p[5:8] ==
          [F(1, 68881143660), F(133, 9357995374380), F(3539, 248922676958508)]
          and all(F(*o['rho']) == rho for o in [old, tight, point])
          and p[:13] == [F(*v) for v in old['pairs_through_12']])
    rr = [[F(*v) for v in row] for row in col['equation_rref']]
    piv = col['equation_pivots']
    check('rref_shape', len(rr) == 49 and all(len(row) == 50 for row in rr)
          and len(piv) == 46 and [j for j in range(49) if j not in piv] == [27, 33, 42])
    M = [[F(*v) for v in row] for row in square['objective_matrix']]
    alpha, bet = -M[3][3], M[0][3]
    w = bet/alpha
    check('original_zero_point', alpha > 0 and alpha*M[0][0]+bet**2 == 0
          and all(M[i][j] == 0 for i, j in it.product(range(4), repeat=2) if i in [1, 2] or j in [1, 2])
          and w == F(*point['w_star']) == F(*tight['w_star']))
    f = [F(0)]*49
    f[42] = w
    for i, j in enumerate(piv):
        f[j] = rr[i][-1]-rr[i][42]*w
    check('complete_point', enc(f) == tight['free_column'] and all(v >= 0 for v in f)
          and [i for i, v in enumerate(f) if not v] == [27, 33])
    old_w = -F(*col['affine']['intercept'][4])/F(*col['affine']['slopes'][4][2])
    check('distinct_old_point', w != old_w)
    for i, (row, bound) in enumerate(zip(col['equations'], col['rhs'])):
        check('original_compatibility_'+str(i), dot([F(*v) for v in row], f) == F(*bound))
    entries = {tuple(row['type']): F(*row['y']) for row in old['types']}
    check('old_domain', set(entries) == {(l, m, i, j) for l, m in [(5, 5), (5, 6), (6, 6)]
                                       for i, j in it.product(range(l+1), repeat=2)})
    column, weights = [], []
    for index, row in enumerate(col['column']):
        val = p[7]*f[row['variable']] if row['kind'] == 'free' else F(*row['value'])
        column.append(val)
        if index == 0:
            check('full_anchor', row['orbit'] == [0, 0, 0] and val == p[7])
            weights.append(1)
        else:
            l, i, j = row['orbit']
            entries[l, 7, i, j] = val
            weights.append(c(7, i)*c(61, l-i)*c(7, j)*c(949, l-j))
    check('whole_column_weights', len(column) == 86 and enc(column) == tight['column']
          and weights == col['weights'] and min(weights) > 0)
    kernels = []
    for index, null in enumerate(col['kernel_basis']):
        value = dot([F(*v)*wi for v, wi in zip(null, weights)], column)
        kernels.append(value)
        check('whole_kernel_'+str(index), value == 0)
    check('kernel_count', len(kernels) == 49)
    free = [(r, q) for r, q in it.product(range(8), repeat=2) if r+q >= 7]
    check('36_original_variables', list(map(list, free)) == tight['free'] and len(free) == 36)
    for r, q in it.product(range(8), repeat=2):
        h = r+q
        entries[7, 7, 7-r, 7-q] = (p[7] if h == 0 else F(0) if h <= 4
                                   else entries[h, 7, q, r] if h <= 6 else None)
    records, groups, source_groups = [], {}, {}
    types = [(l, m, i, j) for l, m in [(5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (7, 7)]
             for i, j in it.product(range(l+1), repeat=2)]
    check('complete_type_domain', set(types) == set(entries))
    for typ in types:
        value = entries[typ]
        l, m, i, j = typ
        atoms = [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]
        orders = []
        for ix, bits in enumerate(it.permutations([4, 2, 1])):
            moved = [0]*8
            for mask, count in enumerate(atoms):
                moved[sum(new for new, bit in zip([4, 2, 1], bits) if mask & bit)] = count
            a, b, h = moved[4]+moved[5], moved[4]+moved[6], moved[2]+moved[6]
            val = (p[max(a, b, h)] if min(a, b, h) == 0 else F(0) if min(a, b, h) <= 4
                   else entries.get((*sorted([a, b]), moved[4], moved[3])))
            check('presentation_'+str((typ, ix)), min(moved) >= 0 and sum(moved) == 1024
                  and all(sum(v for mask, v in enumerate(moved) if mask & bit) == 68 for bit in [1, 2, 4])
                  and (val is None or val == value))
            orders.append(moved)
            source_groups.setdefault((*sorted([a, b, h]), moved[4]-moved[3]), set()).add(typ)
        key = tuple(min(orders))
        groups.setdefault(key, []).append(typ)
        records.append({'type': typ, 'key': key, 'presentations': orders, 'value': value})
    check('all_records', len(records) == 270 and enc(records) == verified['records'] == tight['records'])
    canonical = {row['type']: row['key'] for row in records}
    for key, group in source_groups.items():
        check('source_equality_'+str(key), len({canonical[t] for t in group}) == 1)
    free_keys = [canonical[7, 7, 7-r, 7-q] for r, q in free]
    check('no_free_identifications', len(set(free_keys)) == 36 and all(len(groups[k]) == 1 for k in free_keys))
    check('28_forced_entries', sum(entries[7, 7, i, j] is not None for i, j in it.product(range(8), repeat=2)) == 28)

    # Import the audited bases, then reconstruct every actual subset action.
    factors = {(row['n'], row['layer']): row for row in prior['factors']}
    norms, bases, gamma, transitions = {}, {}, {}, []
    for (n, l), row in factors.items():
        ww = [c(7, i)*c(n-7, l-i) for i in range(l+1)]
        hh = [[F(*v) for v in h] for h in row['basis']]
        ns = [dot([wi*v for wi, v in zip(ww, h)], h) for h in hh]
        check('factor_'+str((n, l)), ww == row['weights'] and enc(ns) == row['norms']
              and len(hh) == l+1 and min(ns) > 0)
        for a in range(l+1):
            for b in range(a):
                check('orthogonality_'+str((n, l, a, b)), dot([wi*v for wi, v in zip(ww, hh[a])], hh[b]) == 0)
        norms[n, l], bases[n, l] = ns, hh
    check('six_factors', set(factors) == set(it.product([68, 956], [5, 6, 7])))
    for row in prior['transitions']:
        n, l, m, t = (row[k] for k in ['n', 'l', 'm', 't'])
        Q = [[sum(c(i, x)*c(7-i, j-x)*c(l-i, t-x)*c(n-7-l+i, m-j-t+x)
                  for x in range(8)) for j in range(m+1)] for i in range(l+1)]
        check('transition_'+str((n, l, m, t)), Q == row['matrix']
              and all(sum(q) == c(l, t)*c(n-l, m-t) for q in Q))
        for a in range(m+1):
            g = F(*row['actions'][a])
            target = [g*v for v in bases[n, l][a]] if a <= l else [F(0)]*(l+1)
            check('action_'+str((n, l, m, t, a)), [dot(q, bases[n, m][a]) for q in Q] == target)
            if a <= min(l, m):
                gamma[n, l, m, a, t] = g
        transitions.append({'n': n, 'l': l, 'm': m, 't': t, 'matrix': Q, 'actions': row['actions']})
    check('complete_transition_domain', {(v['n'], v['l'], v['m'], v['t']) for v in transitions}
          == {(n, l, m, t) for n, l, m in it.product([68, 956], [5, 6, 7], [5, 6, 7]) for t in range(min(l, m)+1)})
    scales = {key: F(*v) for key, v in prior['signed_scales'].items()}
    manuscript_path = NB/'lemmas/L071-zero-point-remaining-mode-obstruction.md'
    manuscript = manuscript_path.read_text()
    parse = lambda s: [F(v.strip()) for v in s.split(',')]
    head = parse(re.search(r'    h=\((.*?)\),', manuscript, re.S).group(1))
    tail = parse(re.search(r'    k=\((.*?)\),', manuscript, re.S).group(1))
    transforms = [[sum(v*eigen(n, a, r) for a, v in enumerate(factor)) for r in range(8)]
                  for n, factor in [(68, head), (956, tail)]]
    displayed = [parse(re.search(r'=\((.*?)\)', manuscript.split(marker, 1)[1], re.S).group(1))
                 for marker in ['sum_a h_a E_(68,a)(r)', 'sum_b k_b E_(956,b)(q)']]
    check('complete_displayed_transforms', transforms == displayed)
    dual = [x*y for x in head for y in tail]
    cert = result['certificate']
    check('all_product_factors', len(head) == len(tail) == 8 and enc(head) == cert['h']
          and enc(tail) == cert['k'] and enc(dual) == cert['mode_weights'] == verified['mode_weights'])
    check('nonnegative_product_support', min(dual) >= 0 and [i for i, v in enumerate(dual) if v > 0]
          == [8*a+b for a in range(4) for b in range(6)] and cert['nonnegative_weights'] == [[0, 1]]*36)
    check('16_tight_8_remaining', sum(dual[i] > 0 for i in result['selected']) == 16
          and sum(dual[i] > 0 for i in result['remaining']) == 8
          and sorted(result['selected']+result['remaining']) == list(range(64)))
    sizes = {l: c(68, l)*c(956, l) for l in [5, 6, 7]}
    modes, A, raw_A, rhs, ranks = [], [], [], [], {}
    for a, b in it.product(range(8), repeat=2):
        ix = 8*a+b
        layers = [l for l in [6, 5] if max(a, b) <= l]
        norm = {l: norms[68, l][a]*norms[956, l][b] for l in layers+[7]}
        d7 = c(68-2*a, 7-a)*c(956-2*b, 7-b)
        check('positive_normalization_'+str(ix), d7 > 0 and min(norm.values()) > 0)

        def action(l, m):
            return sum(gamma[68, l, m, a, i]*gamma[956, l, m, b, j]*entries[min(l, m), max(l, m), i, j]
                       for i, j in it.product(range(min(l, m)+1), repeat=2))-(p[l]*p[m]*sizes[m] if ix == 0 else 0)

        B = [[norm[l]*action(l, m) for m in layers] for l in layers]
        cross = [norm[l]*action(l, 7) for l in layers]
        saved = tight['modes'][ix]
        s = {l: scales[str((68, l, 7, a))]*scales[str((956, l, 7, b))]/(norm[7]/d7) for l in layers}
        for i, l in enumerate(layers):
            si = sorted(layers).index(l)
            check('both_cross_directions_'+str((ix, l)), s[l] > 0 and cross[i] == norm[7]*action(7, l)
                  == norm[7]/d7*s[l]*F(*saved['cross'][si]))
            for j, m in enumerate(layers):
                sj = sorted(layers).index(m)
                check('full_base_congruence_'+str((ix, l, m)), B[i][j] == B[j][i]
                      == norm[7]/d7*s[l]*s[m]*F(*saved['B'][si][sj]))
        work, vec, cost, pivots, ranges = [row[:] for row in B], cross[:], F(0), [], []
        for i in range(len(layers)):
            pivot = work[i][i]
            pivots.append(pivot)
            check('reverse_positive_pivot_'+str((ix, i)), pivot >= 0)
            if not pivot:
                residual = [vec[i]]+work[i][i+1:]
                ranges.extend(residual)
                check('complete_singular_range_'+str((ix, i)), not any(residual))
                continue
            cost += vec[i]**2/pivot
            for j in range(i+1, len(layers)):
                vec[j] -= work[j][i]*vec[i]/pivot
                for k in range(i+1, len(layers)):
                    work[j][k] -= work[j][i]*work[i][k]/pivot
        rank = sum(v > 0 for v in pivots)
        category = str((len(layers), rank))
        ranks[category] = ranks.get(category, 0)+1
        required = cost/(p[7]*norm[7])
        forced = sum(beta(68, 7, 7, a, i)*beta(956, 7, 7, b, j)*entries[7, 7, i, j]
                     for i, j in it.product(range(8), repeat=2) if i+j >= 8)
        raw_fixed = (forced-(p[7]**2*sizes[7]**2 if ix == 0 else 0))/(p[7]*d7)-required
        check('weighted_cost_and_raw_rhs_'+str(ix), enc(required) == saved['required'] == verified['modes'][ix]['required']
              and enc(raw_fixed) == result['rhs'][ix] == verified['rhs'][ix] == verified['raw_mode_fixed_terms'][ix])
        row, raw_row = [], []
        for r, q in free:
            valency = c(7, r)*c(61, r)*c(7, q)*c(949, q)
            e = eigen(68, a, r)*eigen(956, b, q)
            check('source_Johnson_normalization_'+str((ix, r, q)), valency > 0
                  and beta(68, 7, 7, a, 7-r)*beta(956, 7, 7, b, 7-q) == d7*e)
            row.append(-F(e, valency))
            raw_row.append(F(e, p[7]))
        check('all_original_row_'+str(ix), enc(row) == result['matrix'][ix] == verified['matrix'][ix])
        A.append(row)
        raw_A.append(raw_row)
        rhs.append(raw_fixed)
        modes.append({'mode': [a, b], 'layers': layers, 'norms': norm, 'D7': d7, 'base': B,
                      'cross': cross, 'scales': s, 'pivots': pivots, 'range_residuals': ranges,
                      'required': required, 'raw_fixed': raw_fixed})
    check('all_rank_cases', ranks == {'(2, 2)': 9, '(2, 1)': 8, '(2, 0)': 19, '(1, 1)': 10, '(1, 0)': 3, '(0, 0)': 15})
    for l in [5, 6, 7]:
        check('full_space_exhaustion_'+str(l), sum((c(68, a)-c(68, a-1))*(c(956, b)-c(956, b-1))
              for a, b in it.product(range(l+1), repeat=2)) == sizes[l])
    cancellations, raw_cancellations = [], []
    for j, (r, q) in enumerate(free):
        val, raw = dot(dual, [row[j] for row in A]), dot(dual, [row[j] for row in raw_A])
        check('original_and_raw_cancellation_'+str((r, q)), val == raw == transforms[0][r]*transforms[1][q] == 0)
        cancellations.append(val)
        raw_cancellations.append(raw)
    pairing = dot(dual, rhs)
    lo, hi = -1927568495789246, -1927568495789245
    check('full_exact_pairing', pairing == F(*cert['rhs_pairing']) == F(*verified['rhs_pairing'])
          == F(*verified['raw_fixed_pairing']))
    check('strict_integer_bounds', lo*pairing.denominator <= pairing.numerator < hi*pairing.denominator < 0
          and f'[{lo},{hi})' in manuscript and cert['rhs_interval'] == [lo, hi])
    out = {'input_hashes': {str(path.relative_to(NB)): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
           'checks': checks, 'failures': failures, 'rho': rho, 'w_star': w, 'free_column': f,
           'column': column, 'orbit_weights': weights, 'original_kernel_residuals': kernels,
           'records': records, 'transitions': transitions, 'head': head, 'tail': tail,
           'transforms': transforms, 'mode_weights': dual, 'modes': modes, 'matrix': A,
           'raw_matrix': raw_A, 'rhs': rhs, 'scaled_cancellations': cancellations,
           'raw_cancellations': raw_cancellations, 'rhs_pairing': pairing,
           'rhs_interval': [lo, hi], 'integer_bound_slacks': [pairing.numerator-lo*pairing.denominator,
                                                           hi*pairing.denominator-pairing.numerator],
           'summary': {'verdict': 'RETAINED_FIXED_POINT_OBSTRUCTION' if not failures else 'AUDIT_FAILED',
                       'checks': len(checks), 'failures': len(failures), 'types': len(records),
                       'presentations': len(records)*6, 'modes': len(modes), 'rank_cases': ranks,
                       'transition_matrices': len(transitions), 'positive_mode_weights': sum(v > 0 for v in dual),
                       'scaled_cancellations': len(cancellations), 'raw_cancellations': len(raw_cancellations)}}
    OUT.write_text(json.dumps(enc(out), indent=2)+'\n')
    print(f'{out["summary"]["verdict"]}; checks={len(checks)}; failures={failures}')
    print(f'Actual pairing in [{lo},{hi}); required >= 0; 64 modes, 36 scaled and 36 raw cancellations.')
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

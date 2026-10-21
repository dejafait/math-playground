"""L067 critical audit: direct subset actions and complete exact application.

No notebook code, optimizer or floating arithmetic is imported. Prior lemma
inputs are imported as exact data, not silently re-proved. All comparisons
consume complete relevant arrays; the output contains full rational evidence.
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
OUT = ROOT/'simultaneous-seven-shell-critical-audit.json'


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(v):
    if isinstance(v, F):
        return [v.numerator, v.denominator]
    if isinstance(v, dict):
        return {str(k): enc(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [enc(x) for x in v]
    return v


@lru_cache(None)
def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*c(u, t)*c(n-2*a, u-a)
               *c(n-a-u, l-u)*c(n-a-u, m-u)
               for u in range(max(a, t), min(l, m)+1))


def eigen(n, l, a, r):
    return sum((-1)**s*c(a, s)*c(l-a, r-s)*c(n-l-a, r-s)
               for s in range(r+1))


def main():
    paths = [ROOT/name for name in [
        'simultaneous-seven-shell-results.json',
        'simultaneous-seven-shell-verification.json',
        'simultaneous-shell-ordinary-scalars-results.json',
        'seven-distance-full-base-kernel-results.json',
        'seven-distance-fixed-column-energy-results.json']]
    data, verified, old, column, energy = [json.loads(p.read_text()) for p in paths]
    manuscript = NB/'lemmas/L067-simultaneous-seven-shell-fixed-column-obstruction.md'
    text = manuscript.read_text()
    checks, failures = [], []

    def check(name, good):
        checks.append(name)
        if not good:
            failures.append(name)

    for path, obj in zip(paths, [data, verified, old, column, energy]):
        check('input_failures_'+path.name, obj['failures'] == [])
        for rel, digest in obj.get('source_hashes', obj.get('input_hashes')).items():
            check('input_hash_'+path.name+'_'+rel,
                  hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p = [F(*v) for v in old['pairs_through_12']]
    U = F(c(1024, 64), c(68, 64))
    check('original_rho', F(*old['rho']) == (U+1)/(2*c(1024, 68)) > 0)
    check('original_pairs', p[5:8] == [F(1, 68881143660), F(133, 9357995374380),
                                       F(3539, 248922676958508)])
    entries = {tuple(row['type']): F(*row['y']) for row in old['types']}
    check('old_domain', set(entries) == {(l, m, i, j) for l, m in [(5, 5), (5, 6), (6, 6)]
                                        for i, j in it.product(range(l+1), repeat=2)})
    affine = column['affine']
    w = -F(*affine['intercept'][4])/F(*affine['slopes'][4][2])
    check('exact_parameters', affine['free_indices'] == [27, 33, 42]
          and column['chosen_parameters'] == enc([F(0), F(0), w]) and w > 0)
    f = [F(*v)+w*F(*s[2]) for v, s in zip(affine['intercept'], affine['slopes'])]
    for index, row in enumerate(column['column']):
        value = p[7]*f[row['variable']] if row['kind'] == 'free' else F(*row['value'])
        check('column_'+str(index), value == F(*column['complete_column'][index]) and value >= 0)
        if index:
            l, i, j = row['orbit']
            entries[l, 7, i, j] = value
        else:
            check('anchor_column', value == p[7])
    for r, q in it.product(range(8), repeat=2):
        h = r+q
        entries[7, 7, 7-r, 7-q] = (p[7] if h == 0 else F(0) if h <= 4 else
                                   entries[h, 7, q, r] if h <= 6 else None)

    # Full atom permutations, source equalities, and uniqueness of free keys.
    free = [(r, q) for r, q in it.product(range(8), repeat=2) if r+q >= 7]
    canonical, source_keys, presentations = {}, {}, []
    type_order = [(l, m, i, j) for l, m in [(5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (7, 7)]
                  for i, j in it.product(range(l+1), repeat=2)]
    check('270_types', len(type_order) == len(data['records']) == 270)
    for key, saved in zip(type_order, data['records']):
        l, m, i, j = key
        atoms = (956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i)
        check('region_feasibility_'+str(key), min(atoms) >= 0 and sum(atoms) == 1024)
        orders = []
        for order, bits in enumerate(it.permutations([4, 2, 1])):
            aa = [0]*8
            for mask, count in enumerate(atoms):
                out = sum(new for new, oldbit in zip([4, 2, 1], bits) if mask & oldbit)
                aa[out] = count
            A, B, H = aa[4]+aa[5], aa[4]+aa[6], aa[2]+aa[6]
            lookup = (*sorted([A, B]), aa[4], aa[3])
            value = p[max(A, B, H)] if min(A, B, H) == 0 else F(0) if min(A, B, H) < 5 else entries.get(lookup)
            check('presentation_'+str((key, order)), saved['presentations'][order]['atoms'] == aa
                  and saved['presentations'][order]['distances'] == [A, B, H]
                  and (value is None or value == entries[key]))
            sk = (*sorted([A, B, H]), aa[4]-aa[3])
            orders.append(tuple(aa))
            source_keys.setdefault(sk, set()).add(key)
        canon = min(orders)
        check('saved_moment_'+str(key), saved['type'] == list(key)
              and saved['key'] == list(canon) and saved['value'] == enc(entries[key]))
        canonical.setdefault(canon, []).append(key)
        presentations.append({'type': key, 'atoms': atoms, 'orders': orders,
                              'key': canon, 'value': entries[key]})
    for canon, group in canonical.items():
        check('unordered_group_'+str(group[0]), len({entries[k] for k in group}) == 1)
    for sk, group in source_keys.items():
        check('source_equality_'+str(sk), len({min(pres['orders']) for pres in presentations
                                              if pres['type'] in group}) == 1)
    freekeys = [min(pres['orders']) for pres in presentations if pres['value'] is None]
    check('36_distinct_free_keys', len(freekeys) == len(set(freekeys)) == 36
          and data['free'] == list(map(list, free)))

    # Independent four-occupancy count with a distinguished seven-set.
    bases, norms, weights, gamma, factors, transitions = {}, {}, {}, {}, [], []
    for n in [68, 956]:
        for l in [5, 6, 7]:
            weights[n, l] = W = [c(7, i)*c(n-7, l-i) for i in range(l+1)]
            hs, ns = [], []
            for a in range(l+1):
                v = [F(i**a) for i in range(l+1)]
                for h, N in zip(hs, ns):
                    projection = sum(wi*x*y for wi, x, y in zip(W, v, h))/N
                    v = [x-projection*y for x, y in zip(v, h)]
                norm = sum(wi*x*x for wi, x in zip(W, v))
                check('norm_'+str((n, l, a)), norm > 0)
                hs.append(v)
                ns.append(norm)
            bases[n, l], norms[n, l] = hs, ns
            factors.append({'n': n, 'layer': l, 'weights': W, 'basis': hs, 'norms': ns})
        for l, m in it.product([5, 6, 7], repeat=2):
            for t in range(min(l, m)+1):
                Q = [[sum(c(i, x)*c(7-i, j-x)*c(l-i, t-x)*c(n-7-l+i, m-j-t+x)
                          for x in range(8)) for j in range(m+1)] for i in range(l+1)]
                check('row_sums_'+str((n, l, m, t)),
                      all(sum(row) == c(l, t)*c(n-l, m-t) for row in Q))
                scales = []
                for a in range(m+1):
                    image = [sum(q*x for q, x in zip(row, bases[n, m][a])) for row in Q]
                    if a > l:
                        scale = F(0)
                        check('absent_mode_'+str((n, l, m, t, a)), not any(image))
                    else:
                        h = bases[n, l][a]
                        scale = sum(wi*x*y for wi, x, y in zip(weights[n, l], image, h))/norms[n, l][a]
                        check('whole_action_'+str((n, l, m, t, a)), image == [scale*x for x in h])
                        gamma[n, l, m, a, t] = scale
                        if l == m:
                            check('diagonal_'+str((n, l, t, a)), scale == eigen(n, l, a, l-t)
                                  and c(n-2*a, l-a)*scale == beta(n, l, l, a, t))
                    scales.append(scale)
                transitions.append({'n': n, 'l': l, 'm': m, 't': t, 'matrix': Q, 'actions': scales})

    # Check common SIGNED scale across all relations and coherent triangles.
    scale = {}
    for n in [68, 956]:
        for l, m in it.product([5, 6, 7], repeat=2):
            for a in range(min(l, m)+1):
                ratios = []
                for t in range(min(l, m)+1):
                    B = beta(n, l, m, a, t)
                    g, back = gamma[n, l, m, a, t], gamma[n, m, l, a, t]
                    check('adjoint_'+str((n, l, m, a, t)), norms[n, l][a]*g == norms[n, m][a]*back)
                    check('beta_product_'+str((n, l, m, a, t)),
                          g*back == F(B*B, c(n-2*a, l-a)*c(n-2*a, m-a)))
                    if B:
                        ratios.append(g/B)
                    else:
                        check('beta_zero_'+str((n, l, m, a, t)), g == back == 0)
                check('signed_scale_'+str((n, l, m, a)), len(set(ratios)) == 1 and ratios[0] > 0)
                scale[n, l, m, a] = norms[n, l][a]*ratios[0]
        for a in range(8):
            layers = [l for l in [5, 6, 7] if a <= l]
            for l, m in it.product(layers, repeat=2):
                check('coherent_congruence_'+str((n, a, l, m)),
                      scale[n, l, m, a]*scale[n, 7, 7, a]
                      == scale[n, l, 7, a]*scale[n, m, 7, a])

    # Read all displayed dual entries from the manuscript, not the constructor.
    h = [F(v.strip()) for v in re.search(r'  h=\((.*?)\),', text, re.S).group(1).split(',')]
    k = [F(v.strip()) for v in re.search(r'  k=\((.*?)\)\.', text, re.S).group(1).split(',')]
    transforms = [[sum(v*eigen(n, 7, a, r) for a, v in enumerate(vec)) for r in range(8)]
                  for n, vec in [(68, h), (956, k)]]
    for idx, n in enumerate([68, 956]):
        pattern = r'sum_[ab] [hk]_[ab] E_\('+str(n)+r',[ab]\)\([rq]\)\s*=\((.*?)\)'
        displayed = [F(v.strip()) for v in re.search(pattern, text, re.S).group(1).split(',')]
        check('complete_displayed_transform_'+str(n), transforms[idx] == displayed
              and enc(displayed) == verified['dual_transforms'][idx])
    dual = [x*y for x in h for y in k]
    check('24_positive_weights', len(dual) == 64 and sum(v > 0 for v in dual) == 24
          and all(v >= 0 for v in dual) and enc(dual) == data['exact']['dual'])
    totals = [F(0)]*3
    residuals = [F(0)]*36
    modes, trace, ranks = [], p[7]**2, {}
    sizes = {l: c(68, l)*c(956, l) for l in [5, 6, 7]}
    for a, b in it.product(range(8), repeat=2):
        index = 8*a+b
        layers = [l for l in [6, 5] if max(a, b) <= l]  # reverse elimination order
        norm = {l: norms[68, l][a]*norms[956, l][b] for l in layers+[7]}

        def action(l, m):
            val = sum(entries[min(l, m), max(l, m), i, j]
                      *gamma[68, l, m, a, i]*gamma[956, l, m, b, j]
                      for i, j in it.product(range(min(l, m)+1), repeat=2))
            return val-p[l]*p[m]*sizes[m] if a == b == 0 else val

        K = [[norm[l]*action(l, m) for m in layers] for l in layers]
        cross = [norm[l]*action(l, 7) for l in layers]
        saved = data['modes'][index]
        D7 = c(68-2*a, 7-a)*c(956-2*b, 7-b)
        s = {l: scale[68, l, 7, a]*scale[956, l, 7, b]/(norm[7]/D7) for l in layers}
        for i, l in enumerate(layers):
            si = saved['layers'].index(l)
            check('cross_bilinear_'+str((a, b, l)),
                  cross[i] == norm[7]/D7*s[l]*F(*saved['cross'][si])
                  and cross[i] == norm[7]*action(7, l))
            for j, m in enumerate(layers):
                sj = saved['layers'].index(m)
                check('base_bilinear_'+str((a, b, l, m)), K[i][j] == K[j][i]
                      and K[i][j] == norm[7]/D7*s[l]*s[m]*F(*saved['base'][si][sj]))
        # Direct reverse-order exact elimination of the weighted bilinear form.
        work, rhs = [row[:] for row in K], cross[:]
        cost, rank, pivots = F(0), 0, []
        for i in range(len(layers)):
            pivot = work[i][i]
            check('bilinear_pivot_'+str((a, b, i)), pivot >= 0)
            pivots.append(pivot)
            if not pivot:
                check('bilinear_zero_range_'+str((a, b, i)), rhs[i] == 0
                      and all(work[i][j] == 0 for j in range(i+1, len(layers))))
                continue
            rank += 1
            cost += rhs[i]**2/pivot
            for j in range(i+1, len(layers)):
                rhs[j] -= work[j][i]*rhs[i]/pivot
                for z in range(i+1, len(layers)):
                    work[j][z] -= work[j][i]*work[i][z]/pivot
        ranks[str((len(layers), rank))] = ranks.get(str((len(layers), rank)), 0)+1
        required = cost/(p[7]*norm[7])
        check('required_'+str(index), required == F(*saved['required'])
              == F(*verified['mode_rows'][index]['required']))
        fixed = sum(entries[7, 7, 7-r, 7-q]*gamma[68, 7, 7, a, 7-r]
                    *gamma[956, 7, 7, b, 7-q]/p[7]
                    for r, q in it.product(range(8), repeat=2) if r+q <= 6)
        anchor = p[7]*sizes[7] if a == b == 0 else F(0)
        bound = fixed-anchor-required
        check('all_fixed_terms_'+str(index), enc([fixed, anchor, required])
              == [saved['fixed'], saved['anchor'], saved['required']] and enc(bound) == data['rhs'][index])
        for j, (r, q) in enumerate(free):
            coefficient = -gamma[68, 7, 7, a, 7-r]*gamma[956, 7, 7, b, 7-q]/(
                c(7, r)*c(61, r)*c(7, q)*c(949, q))
            check('full_system_'+str((index, j)), enc(coefficient) == data['matrix'][index][j])
            residuals[j] += dual[index]*coefficient
        totals = [total+dual[index]*v for total, v in zip(totals, [fixed, anchor, required])]
        multiplicity = (c(68, a)-c(68, a-1))*(c(956, b)-c(956, b-1))
        check('multiplicity_'+str(index), multiplicity > 0)
        trace += p[7]*multiplicity*required/sizes[7]
        modes.append({'mode': [a, b], 'layers': layers, 'norms': norm, 'base': K,
                      'cross': cross, 'congruence_scales': s, 'pivots': pivots,
                      'rank': rank, 'cost': cost, 'required': required,
                      'fixed': fixed, 'anchor': anchor, 'bound': bound})
    for l in [5, 6, 7]:
        check('dimension_'+str(l), sum((c(68, a)-c(68, a-1))*(c(956, b)-c(956, b-1))
                                      for a, b in it.product(range(l+1), repeat=2)) == sizes[l])
    for j, (r, q) in enumerate(free):
        check('dual_cancellation_'+str((r, q)), residuals[j] == 0
              and transforms[0][r]*transforms[1][q] == 0)
    check('energy_trace', enc(trace) == energy['summary']['energy'] == data['trace_energy'])
    for total, lower in zip(totals, [1897002902, 948289785, 1002216636]):
        check('strict_interval_'+str(lower), F(lower, 10**6) <= total < F(lower+1, 10**6))
    value = totals[0]-totals[1]-totals[2]
    check('strict_contradiction', F(-53503520, 10**6) <= value < F(-53503519, 10**6) < 0
          and enc(value) == verified['fixed_value'] == data['exact']['fixed_value'])
    report = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'manuscript_path': str(manuscript.relative_to(NB)),
              'manuscript_sha256': hashlib.sha256(manuscript.read_bytes()).hexdigest(),
              'presentations': presentations, 'factors': factors, 'transitions': transitions,
              'signed_scales': scale, 'modes': modes, 'dual': dual, 'transforms': transforms,
              'dual_residuals': residuals, 'totals': totals, 'fixed_value': value,
              'energy_trace': trace, 'checks': checks, 'failures': failures,
              'summary': {'checks': len(checks), 'failures': len(failures), 'modes': len(modes),
                          'mode_base_ranks': ranks, 'transition_matrices': len(transitions),
                          'free_keys': len(freekeys), 'verdict': 'RETAIN L067' if not failures else 'FAILED'}}
    OUT.write_text(json.dumps(enc(report), indent=2)+'\n')
    print(report['summary'])
    print('Actual fixed dual value in [-53.503520,-53.503519); required >= 0.')
    print('Full free cancellations:', sum(v == 0 for v in residuals), '/36; failures:', failures)
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

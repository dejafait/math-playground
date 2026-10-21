"""Independent exact reconstruction of the joint seven-shell dual obstruction.

No constructor, optimizer or floating arithmetic imports. Full point sets,
source beta formula, determinant inverse and all dual identities are checked.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'simultaneous-seven-shell-verification.json'


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(v):
    v = Q(v)
    return [v.numerator, v.denominator]


@lru_cache(None)
def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*C(u, t)*C(n-2*a, u-a)*C(n-a-u, l-u)*C(n-a-u, m-u)
               for u in range(a, min(l, m, n-a)+1) if u >= t)


def interval(v, denominator=10**6):
    k = v.numerator*denominator//v.denominator
    return [enc(Q(k, denominator)), enc(Q(k+1, denominator))]


def main():
    paths = [ROOT/'simultaneous-seven-shell-results.json',
             ROOT/'simultaneous-shell-ordinary-scalars-results.json',
             ROOT/'seven-distance-full-base-kernel-results.json',
             ROOT/'seven-distance-fixed-column-energy-results.json']
    data, old, col, energy = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('prior_failures_empty', all(not s['failures'] for s in [data, old, col, energy]))
    check('input_hashes', all(hashlib.sha256((NB/p).read_bytes()).hexdigest() == h
          for p, h in data['source_hashes'].items()))
    p = [Q(*v) for v in old['pairs_through_12']]
    check('positive_normalization', Q(*old['rho']) > 0 and p[7] == Q(3539, 248922676958508))
    base = {tuple(row['type']): Q(*row['y']) for row in old['types']}
    intercept = list(map(lambda v: Q(*v), col['affine']['intercept']))
    slopes = [[Q(*v) for v in row] for row in col['affine']['slopes']]
    w = -intercept[4]/slopes[4][2]
    f = [v+w*s[2] for v, s in zip(intercept, slopes)]
    check('immutable_affine_parameter_order', col['affine']['free_indices'] == [27, 33, 42])
    for row, saved in zip(col['column'][1:], col['complete_column'][1:]):
        value = p[7]*f[row['variable']] if row['kind'] == 'free' else Q(*row['value'])
        check('column_'+str(row['orbit']), value == Q(*saved))
        l, i, j = row['orbit']
        base[l, 7, i, j] = value

    D = set(range(68))
    allkeys, records, keys, entries = {}, [], [], {}
    free = [(r, q) for r in range(8) for q in range(8) if r+q >= 7]
    check('free_domain', data['free'] == list(map(list, free)))
    for l, m in [(5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (7, 7)]:
        for i, j in it.product(range(l+1), repeat=2):
            E = (D-(set(range(i))|set(range(m, m+l-i)) )) | set(range(68, 68+j)) | set(range(68+m, 68+m+l-j))
            G = (D-set(range(m))) | set(range(68, 68+m))
            check('actual_cardinalities_'+str((l, m, i, j)), len(E) == len(G) == 68)
            values, presentations = [], []
            saved = data['records'][len(records)]
            for order, (A, B, Cset) in enumerate(it.permutations([D, E, G])):
                atoms = [0]*8
                for point in range(1024):
                    atoms[4*(point in A)+2*(point in B)+(point in Cset)] += 1
                ds = [len(A-B), len(A-Cset), len(B-Cset)]
                value, origin = None, None
                if min(ds) == 0:
                    value, origin = p[max(ds)], 'Boolean'
                elif any(0 < d < 5 for d in ds):
                    value, origin = Q(0), 'forbidden'
                else:
                    key = (*sorted(ds[:2]), len((A-B)&(A-Cset)), len((B-A)&(Cset-A)))
                    if key in base:
                        value, origin = base[key], 'immutable'
                if value is not None:
                    values.append(value)
                record = {'atoms': atoms, 'distances': ds, 'origin': origin,
                          'value': enc(value) if value is not None else None}
                check('actual_presentation_'+str((l, m, i, j, order)), record == saved['presentations'][order])
                presentations.append(record)
            check('all_presentations_agree_'+str((l, m, i, j)), len(set(values)) <= 1)
            key = min(tuple(v['atoms']) for v in presentations)
            check('saved_key_'+str((l, m, i, j)), saved['key'] == list(key))
            value = values[0] if values else None
            check('complete_value_'+str((l, m, i, j)), saved['value'] == (enc(value) if value is not None else None))
            if key in allkeys:
                check('equal_unions_'+str((l, m, i, j)), allkeys[key] == value)
            allkeys[key] = value
            entries[l, m, i, j] = value
            records.append({'type': [l, m, i, j], 'key': list(key), 'value': enc(value) if value is not None else None})
            if value is None:
                keys.append((7-i, 7-j))
    check('free_keys_complete', sorted(keys) == free and len(keys) == 36)

    size = {l: C(68, l)*C(956, l) for l in [5, 6, 7]}
    dual = [Q(*v) for v in data['exact']['dual']]
    check('all_dual_nonnegative', len(dual) == 64 and all(v >= 0 for v in dual))
    head = [Q(1), Q(20435, 441), Q(13481000, 13671), Q(2688040, 217),
            Q(1307664259, 13671), Q(5294968393, 13671), Q(0), Q(0)]
    tail = [Q(49, 100880416043264), Q(7665, 38718903137024),
            Q(17301, 551968803584), Q(5461349, 2754064239872), Q(0), Q(0), Q(0), Q(0)]
    check('explicit_product_dual', all(dual[8*a+b] == head[a]*tail[b]
          for a, b in it.product(range(8), repeat=2)))
    transforms = [[sum(v*Q(beta(n, 7, 7, a, 7-r), C(n-2*a, 7-a))
                       for a, v in enumerate(factors)) for r in range(8)]
                  for n, factors in [(68, head), (956, tail)]]
    check('factor_cancellation_on_free_domain', all(transforms[0][r]*transforms[1][q] == 0 for r, q in free))
    residuals = [Q(0)]*36
    totals = {'fixed': Q(0), 'anchor': Q(0), 'required': Q(0)}
    mode_rows, trace = [], p[7]**2
    for a, b in it.product(range(8), repeat=2):
        index = 8*a+b
        layers = [l for l in [5, 6] if max(a, b) <= l]

        def block(l, m):
            value = sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*entries[l, m, i, j]
                        for i, j in it.product(range(l+1), repeat=2))
            if a == b == 0:
                value -= p[l]*p[m]*size[l]*size[m]
            return value

        oldblock = [[block(min(l, m), max(l, m)) for m in layers] for l in layers]
        cross = [block(l, 7) for l in layers]
        check('oldblock_'+str(index), [list(map(enc, row)) for row in oldblock] == data['modes'][index]['base'])
        check('cross_'+str(index), list(map(enc, cross)) == data['modes'][index]['cross'])
        cost = Q(0)
        if len(layers) == 2:
            x, t, z = oldblock[0][0], oldblock[0][1], oldblock[1][1]
            u, v = cross
            det = x*z-t*t
            check('old_PSD_'+str(index), x >= 0 and z >= 0 and det >= 0)
            if det > 0:
                cost = (z*u*u-2*t*u*v+x*v*v)/det
            elif x > 0:
                check('singular_range_'+str(index), x*v == t*u)
                cost = u*u/x
            elif z > 0:
                check('singular_range_'+str(index), u == t == 0)
                cost = v*v/z
            else:
                check('zero_range_'+str(index), t == u == v == 0)
        elif len(layers) == 1:
            z, v = oldblock[0][0], cross[0]
            check('one_layer_range_'+str(index), z >= 0 and (z > 0 or v == 0))
            cost = v*v/z if z else Q(0)
        D7 = C(68-2*a, 7-a)*C(956-2*b, 7-b)
        required = cost/(p[7]*D7)
        # Direct source beta, without an Eberlein or Schur implementation.
        coeff = {(r, q): Q(beta(68, 7, 7, a, 7-r)*beta(956, 7, 7, b, 7-q), D7)
                 for r, q in it.product(range(8), repeat=2)}
        fixed = sum(entries[7, 7, 7-r, 7-q]*v/p[7] for (r, q), v in coeff.items()
                    if entries[7, 7, 7-r, 7-q] is not None)
        anchor = p[7]*size[7] if a == b == 0 else Q(0)
        bound = fixed-anchor-required
        check('complete_rhs_'+str(index), enc(bound) == data['rhs'][index])
        for j, (r, q) in enumerate(free):
            v = -coeff[r, q]/(C(7, r)*C(61, r)*C(7, q)*C(949, q))
            check('dual_coefficient_'+str((index, j)), enc(v) == data['matrix'][index][j])
            residuals[j] += dual[index]*v
        for name, v in [('fixed', fixed), ('anchor', anchor), ('required', required)]:
            totals[name] += dual[index]*v
        mu = (C(68, a)-C(68, a-1))*(C(956, b)-C(956, b-1))
        trace += p[7]*mu*required/size[7]
        mode_rows.append({'mode': [a, b], 'dual': enc(dual[index]),
                          'fixed': enc(fixed), 'anchor': enc(anchor), 'required': enc(required)})
    value = totals['fixed']-totals['anchor']-totals['required']
    check('every_free_coefficient_cancels', all(v == 0 for v in residuals))
    check('saved_dual_column_sums', list(map(enc, residuals)) == data['exact']['column_sums'])
    check('strict_negative_fixed_term', value < 0)
    check('saved_fixed_value', enc(value) == data['exact']['fixed_value'])
    check('whole_energy_trace', enc(trace) == energy['summary']['energy'] == data['trace_energy'])
    report = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'records': records, 'mode_rows': mode_rows, 'dual_column_sums': list(map(enc, residuals)),
              'totals': {k: enc(v) for k, v in totals.items()}, 'fixed_value': enc(value),
              'dual_factors': [list(map(enc, v)) for v in [head, tail]],
              'dual_transforms': [list(map(enc, v)) for v in transforms],
              'intervals': {k: interval(v) for k, v in {**totals, 'contradiction': value}.items()},
              'checks': checks, 'failures': failures,
              'summary': {'checks': len(checks), 'failures': len(failures), 'dual_positive': sum(v > 0 for v in dual),
                          'all_36_columns_cancel': all(v == 0 for v in residuals),
                          'strict_negative': value < 0, 'verdict': 'EXCLUDED' if not failures else 'FAILED'}}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(report['summary'])
    for name, bounds in report['intervals'].items():
        print(name, 'in', [str(Q(*v)) for v in bounds])
    print('Required contradiction >= 0; actual < 0. Failures:', failures)
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

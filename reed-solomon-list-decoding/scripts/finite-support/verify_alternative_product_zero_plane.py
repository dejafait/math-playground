"""Independent source-sum and complete scalar verification for L072.

No notebook imports, optimizer or floating arithmetic. Reconstruct the
quadratic by polarization of direct inverse-on-range evaluations.
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
OUT = ROOT/'alternative-product-zero-plane-verification.json'


def enc(x):
    if isinstance(x, Q):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {k: enc(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [enc(v) for v in x]
    return x


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


@lru_cache(None)
def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*C(u, t)*C(n-2*a, u-a)*C(n-a-u, l-u)*C(n-a-u, m-u)
               for u in range(max(a, t), min(l, m, n-a)+1))


def eigen(n, a, r):
    return sum((-1)**s*C(a, s)*C(7-a, r-s)*C(n-7-a, r-s) for s in range(r+1))


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), Q(0))


def main():
    names = ['alternative-product-zero-plane-results.json',
             'seven-distance-full-base-kernel-results.json',
             'simultaneous-shell-ordinary-scalars-results.json',
             'zero-dual-plane-scalars-results.json', 'zero-point-remaining-modes-results.json']
    paths = [ROOT/n for n in names]
    data, col, old, scalar, fixed = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for j, d in enumerate([data, col, old, scalar, fixed]):
        check(f'clean_input_{j}', not d['failures'])
        for path, digest in d.get('input_hashes', d.get('source_hashes', {})).items():
            check(f'input_hash_{j}_{path}', hashlib.sha256((NB/path).read_bytes()).hexdigest() == digest)
    p = [Q(*x) for x in scalar['pairs_through_13']]
    w = Q(*scalar['w_star'])
    fs = [[Q(*c)+w*Q(*a[2]), Q(*a[0]), Q(*a[1])]
          for c, a in zip(col['affine']['intercept'], col['affine']['slopes'])]
    oldbase = {tuple(r['type']): [Q(*r['y']), Q(0), Q(0)] for r in old['types']}
    base = dict(oldbase)
    for row in col['column'][1:]:
        l, i, j = row['orbit']
        base[l, 7, i, j] = [p[7]*x for x in fs[row['variable']]] if row['kind'] == 'free' else [Q(*row['value']), Q(0), Q(0)]
    for r, q in it.product(range(8), repeat=2):
        h = r+q
        if h == 0:
            base[7, 7, 7-r, 7-q] = [p[7], Q(0), Q(0)]
        elif h <= 4:
            base[7, 7, 7-r, 7-q] = [Q(0)]*3
        elif h <= 6:
            base[7, 7, 7-r, 7-q] = base[h, 7, q, r]
    check('28_forced_36_free', sum(t[:2] == (7, 7) for t in base) == 28 and len(base) == 234)
    check('positive_original_normalization', Q(*data['rho']) == Q(*old['rho']) ==
          (Q(C(1024, 64), C(68, 64))+1)/(2*C(1024, 68)) > 0
          and p[7] == Q(3539, 248922676958508) > 0
          and enc(p[:13]) == old['pairs_through_12'])
    check('unchanged_p13', p[13] == Q(26968792942808537, 1896913598738625271419892200))
    # Every full presentation, with Boolean/forbidden and unordered lookup.
    D, keyvalues, scalar_rows, scalar_evidence = set(range(68)), {}, [], []
    for row in data['records']:
        l, m, i, j = typ = tuple(row['type'])
        E = (D-(set(range(i))|set(range(m, m+l-i))))|set(range(68, 68+j))|set(range(68+m, 68+m+l-j))
        G = (D-set(range(m)))|set(range(68, 68+m))
        presentations = []
        value = base.get(typ)
        for order, supports in zip(it.permutations(range(3)), it.permutations([D, E, G])):
            A, B, Cset = supports
            at = [0]*8
            for x in range(1024):
                at[4*(x in A)+2*(x in B)+(x in Cset)] += 1
            a, b, h = len(A-B), len(A-Cset), len(B-Cset)
            lookup = None
            if 0 in [a, b, h]:
                lookup = [p[max(a, b, h)], Q(0), Q(0)]
            elif any(1 <= t <= 4 for t in [a, b, h]):
                lookup = [Q(0)]*3
            else:
                lookup = base.get((*sorted([a, b]), at[4], at[3]))
            # A presentation outside the retained layer set gives no lookup.
            # Every available prescribed lookup must equal the full-key value.
            check(f'full_unordered_presentation_{len(checks)}', lookup is None or lookup == value)
            presentations.append(tuple(at))
            if m == 7 and l in [5, 6]:
                t, s = at[4], at[3]
                O = C(68, t)*C(68-t, a-t)*C(68-a, b-t)*C(956, s)*C(956-s, a-s)*C(956-a, b-s)
                check(f'actual_scalar_orbit_{len(checks)}', O > 0 and h == a+b-t-s and max(a, b, h) <= 13)
                slacks = [value, [p[a]-value[0], -value[1], -value[2]],
                          [1+value[0]-p[a]-p[b], value[1], value[2]]]
                for kind, slack in zip(['nonnegative', 'upper', 'lower'], slacks):
                    saved = scalar['inequalities'][len(scalar_rows)]
                    check(f'exact_scalar_affine_{len(scalar_rows)}', saved['type'] == list(typ)
                          and saved['order'] == list(order) and saved['row'] == kind and saved['affine'] == enc(slack))
                    scalar_rows.append(slack)
                scalar_evidence.append({'type': typ, 'order': order, 'atoms': at, 'orbit_size': O, 'slacks': slacks})
        check(f'actual_regions_{typ}', [list(t) for t in presentations] == row['regions'])
        key = min(presentations)
        check(f'shared_key_{typ}', key not in keyvalues or keyvalues[key] == value)
        keyvalues[key] = value
    check('complete_new_scalar_domain', len(scalar_rows) == 1530)
    old_slacks = []
    for row in old['types']:
        y = Q(*row['y'])
        for pres in row['presentations']:
            at = pres['atoms']
            a, b = at[4]+at[5], at[4]+at[6]
            slacks = [y, p[a]-y, 1+y-p[a]-p[b]]
            check(f'old_scalar_{len(old_slacks)}', enc(slacks) == pres['slacks'] and min(slacks) >= 0)
            old_slacks.extend(slacks)
    check('all_old_rows', len(old_slacks) == 2178)
    h = [Q(1), Q(12261, 455), Q(15555, 56), Q(4099261, 3640)]+[Q(0)]*4
    k = [Q(1), Q(4531475, 6657), Q(136607358056, 632415), Q(27321109096, 665),
         Q(1028453048809043, 210805), Q(9295091464315239, 30115), Q(0), Q(0)]
    weights = [x*y for x, y in it.product(h, k)]
    check('unchanged_weights', enc(weights) == data['weights'] == fixed['certificate']['mode_weights'])
    free = [(r, q) for r, q in it.product(range(8), repeat=2) if r+q >= 7]
    cancellations, raw_cancellations = [], []
    for r, q in free:
        cancellations.append(sum(weights[8*a+b]*Q(-eigen(68, a, r)*eigen(956, b, q),
                 C(7, r)*C(61, r)*C(7, q)*C(949, q)) for a, b in it.product(range(8), repeat=2)))
        raw_cancellations.append(sum(weights[8*a+b]*Q(beta(68, 7, 7, a, 7-r)*beta(956, 7, 7, b, 7-q),
                 p[7]*C(68-2*a, 7-a)*C(956-2*b, 7-b)) for a, b in it.product(range(8), repeat=2)))
    check('original_scaled_and_raw_cancellation', not any(cancellations+raw_cancellations))
    S = {l: C(68, l)*C(956, l) for l in [5, 6, 7]}

    def evaluate(u, v):
        point = [Q(1), u, v]
        rhs, raw_rhs, modes = [], [], []
        for ix, (a, b) in enumerate(it.product(range(8), repeat=2)):
            ls = [l for l in [5, 6] if max(a, b) <= l]
            d7 = C(68-2*a, 7-a)*C(956-2*b, 7-b)

            def block(l, m):
                l, m = min(l, m), max(l, m)
                ans = sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*dot(base[l, m, i, j], point)
                          for i, j in it.product(range(l+1), repeat=2))
                return ans-(p[l]*p[m]*S[l]*S[m] if ix == 0 else 0)

            B = [[block(l, m) for m in ls] for l in ls]
            cross = [block(l, 7) for l in ls]
            energy, residuals = Q(0), []
            if len(B) == 2:
                x, y, z = B[0][0], B[0][1], B[1][1]
                t, s = cross
                check(f'old_PSD_{len(checks)}', x >= 0 and x*z-y*y >= 0 and z >= 0)
                if x > 0:
                    energy += t*t/x
                    z, s = z-y*y/x, s-y*t/x
                else:
                    residuals.extend([y, t])
            elif B:
                z, s = B[0][0], cross[0]
            else:
                z, s = Q(0), Q(0)
            if z > 0:
                energy += s*s/z
            else:
                residuals.append(s)
            check(f'whole_range_{len(checks)}', not any(residuals))
            F = sum(dot(base[7, 7, 7-r, 7-q], point)*eigen(68, a, r)*eigen(956, b, q)/p[7]
                    for r in range(8) for q in range(8) if r+q <= 6)
            anchor = p[7]*S[7] if ix == 0 else 0
            bound = F-anchor-energy/(p[7]*d7)
            raw = sum(beta(68, 7, 7, a, i)*beta(956, 7, 7, b, j)*dot(base[7, 7, i, j], point)
                      for i, j in it.product(range(8), repeat=2) if (7, 7, i, j) in base)
            raw -= p[7]**2*S[7]**2 if ix == 0 else 0
            raw = (raw-energy)/(p[7]*d7)
            check(f'raw_full_anchor_pairing_{len(checks)}', raw == bound)
            rhs.append(bound)
            raw_rhs.append(raw)
            modes.append({'mode': [a, b], 'B': B, 'cross': cross, 'energy': energy,
                          'range': residuals, 'rhs': bound, 'raw_rhs': raw})
        return dot(weights, rhs), modes

    points = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1)]
    values = [evaluate(Q(u), Q(v))[0] for u, v in points]
    c, pu, mu, pv, mv, both = values
    M = [[c, (pu-mu)/4, (pv-mv)/4], [(pu-mu)/4, (pu+mu)/2-c, (both-pu-pv+c)/2],
         [(pv-mv)/4, (both-pu-pv+c)/2, (pv+mv)/2-c]]
    check('whole_plane_quadratic', enc(M) == data['plane_matrix'])
    check('u_flat_v_concave', all(M[1][i] == M[i][1] == 0 for i in range(3)) and M[2][2] < 0)
    alpha, beta_v = -M[2][2], M[0][2]
    vstar = beta_v/alpha
    maximum = c+beta_v**2/alpha
    check('exact_attained_maximum', maximum > 0 and beta_v > 0 and enc([Q(0), vstar, w]) == data['stationary']['parameters']
          and enc(maximum) == data['stationary']['value'] and Q(174659686133710) <= maximum < Q(174659686133711))
    point = [Q(1), Q(0), vstar]
    free_values = [dot(f, point) for f in fs]
    new_slacks = [dot(row, point) for row in scalar_rows]
    check('all_49_free_signs', min(free_values) >= 0 and enc(free_values) == data['stationary']['nonnegative_slacks'])
    check('all_1530_new_scalar_rows', min(new_slacks) >= 0 and enc(new_slacks) == data['stationary']['scalar_slacks'])
    complete_column = [p[7]*free_values[r['variable']] if r['kind'] == 'free' else Q(*r['value']) for r in col['column']]
    residuals = [sum(Q(*x)*wt*b for x, wt, b in zip(vec, col['weights'], complete_column)) for vec in col['kernel_basis']]
    check('all_49_weighted_original_kernel_residuals', len(residuals) == 49 and not any(residuals))
    check('all_forced_signs', min(complete_column) >= 0 and all(dot(v, point) >= 0 for key, v in base.items() if key[:2] == (7, 7)))
    direct_value, witness_modes = evaluate(Q(0), vstar)
    check('direct_full_pairing_at_witness', direct_value == maximum)
    summary = {'checks': len(checks), 'failures': len(failures), 'types': 270, 'presentations': 1620,
               'new_scalar_rows': len(new_slacks), 'old_scalar_rows': len(old_slacks), 'modes': 64,
               'minimum_new_slack': min(new_slacks), 'positive_free': sum(x > 0 for x in free_values),
               'zero_free': [i for i, x in enumerate(free_values) if x == 0],
               'maximum_integer_interval': [174659686133710, 174659686133711],
               'verdict': 'ADMISSIBLE_POSITIVE_MAXIMUM' if not failures else 'VERIFICATION_FAILED'}
    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'checks': checks, 'failures': failures, 'summary': summary, 'plane_matrix': M,
           'alpha': alpha, 'beta': beta_v, 'parameters': [Q(0), vstar, w], 'maximum': maximum,
           'polarization_points': points, 'polarization_values': values, 'witness_modes': witness_modes,
           'new_scalar_evidence': scalar_evidence, 'new_scalar_slacks': new_slacks, 'old_scalar_slacks': old_slacks,
           'free_values': free_values, 'complete_column': complete_column, 'kernel_residuals': residuals,
           'scaled_cancellations': cancellations, 'raw_cancellations': raw_cancellations}
    OUT.write_text(json.dumps(enc(out), indent=2)+'\n')
    print(json.dumps(enc(summary), sort_keys=True))
    print('Required pairing <0 everywhere; attained maximum in [174659686133710,174659686133711).')
    print('Failure count:', len(failures), '; first failures:', failures[:10], '; certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

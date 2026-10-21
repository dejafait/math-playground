"""L072's exact maximizer: original rational LP, numerical basis discovery only."""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

from zero_point_remaining_modes import C, beta, eigen, dot, enc
from simultaneous_five_six_shell import propose, solve

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'maximizer-completion-results.json'


def main():
    names = ['alternative-product-zero-plane-results.json',
             'seven-distance-full-base-kernel-results.json',
             'simultaneous-shell-ordinary-scalars-results.json',
             'zero-dual-plane-scalars-results.json', 'zero-point-tight-modes-results.json']
    paths = [ROOT/n for n in names]
    point, col, old, scalar, tight = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in paths}, 'checks': checks, 'failures': failures}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        out['stage'] = stage
        OUT.write_text(json.dumps(enc(out), indent=2)+'\n')

    for k, data in enumerate([point, col, old, scalar, tight]):
        check(f'clean_input_{k}', not data['failures'])
        for name, digest in data.get('input_hashes', data.get('source_hashes', {})).items():
            check(f'input_hash_{k}_{name}', hashlib.sha256((NB/name).read_bytes()).hexdigest() == digest)
    p = [Q(*x) for x in scalar['pairs_through_13']]
    rho, w = Q(*point['rho']), Q(*point['w_star'])
    N = [[Q(*v) for v in row] for row in point['plane_matrix']]
    vstar = N[0][2]/(-N[2][2])
    parameter = [Q(1), Q(0), vstar, w]
    check('exact_L072_maximizer', enc(parameter[1:]) == point['stationary']['parameters']
          and vstar == Q(*point['square_certificate']['v_star']) > 0
          and rho == (Q(C(1024, 64), C(68, 64))+1)/(2*C(1024, 68)) > 0
          and p[7] == Q(3539, 248922676958508) > 0)
    f = [Q(*c)+dot([Q(*v) for v in a], parameter[1:])
         for c, a in zip(col['affine']['intercept'], col['affine']['slopes'])]
    check('49_column_signs', len(f) == 49 and min(f) >= 0)
    for k, (row, b) in enumerate(zip(col['equations'], col['rhs'])):
        check(f'original_kernel_{k}', dot([Q(*v) for v in row], f) == Q(*b))
    base = {tuple(r['type']): Q(*r['y']) for r in old['types']}
    for row in col['column'][1:]:
        l, i, j = row['orbit']
        base[l, 7, i, j] = p[7]*f[row['variable']] if row['kind'] == 'free' else Q(*row['value'])
    for r, q in it.product(range(8), repeat=2):
        h = r+q
        if h <= 6:
            base[7, 7, 7-r, 7-q] = p[7] if h == 0 else Q(0) if h <= 4 else base[h, 7, q, r]
    records = []
    for row in point['records']:
        typ = tuple(row['type'])
        y = None if row['affine'] is None else dot([Q(*v) for v in row['affine']], parameter)
        check(f'exact_fixed_entry_{typ}', y == base.get(typ))
        records.append({'type': typ, 'value': y, 'regions': row['regions']})
    check('270_types_28_forced', len(records) == 270 and len(base) == 234
          and sum(t[:2] == (7, 7) for t in base) == 28 and min(base.values()) >= 0)
    free = [(r, q) for r, q in it.product(range(8), repeat=2) if r+q >= 7]
    check('36_original_variables', enc(free) == point['free'] == tight['free'])
    S = {l: C(68, l)*C(956, l) for l in [5, 6, 7]}
    A, rhs, modes = [], [], []
    for ix, (a, b) in enumerate(it.product(range(8), repeat=2)):
        layers = [l for l in [5, 6] if max(a, b) <= l]
        d7 = C(68-2*a, 7-a)*C(956-2*b, 7-b)

        def block(l, m):
            l, m = min(l, m), max(l, m)
            value = sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*base[l, m, i, j]
                        for i, j in it.product(range(l+1), repeat=2))
            return value-(p[l]*p[m]*S[l]*S[m] if ix == 0 else 0)

        B = [[block(l, m) for m in layers] for l in layers]
        cross = [block(l, 7) for l in layers]
        cost, ranges, pivots = Q(0), [], []
        if len(B) == 2:
            x, y, z = B[0][0], B[0][1], B[1][1]
            t, s = cross
            pivots.append(x)
            if x > 0:
                cost += t*t/x
                z, s = z-y*y/x, s-y*t/x
            else:
                ranges.extend([y, t])
        elif B:
            z, s = B[0][0], cross[0]
        else:
            z, s = Q(0), Q(0)
        pivots.append(z)
        if z > 0:
            cost += s*s/z
        else:
            ranges.append(s)
        check(f'old_PSD_and_range_{ix}', min(pivots) >= 0 and not any(ranges) and d7 > 0)
        required = cost/(p[7]*d7)
        F = sum(base[7, 7, 7-r, 7-q]*eigen(68, a, r)*eigen(956, b, q)/p[7]
                for r, q in it.product(range(8), repeat=2) if r+q <= 6)
        anchor = p[7]*S[7] if ix == 0 else Q(0)
        bound = F-anchor-required
        row = [-Q(eigen(68, a, r)*eigen(956, b, q),
                  C(7, r)*C(61, r)*C(7, q)*C(949, q)) for r, q in free]
        saved = point['modes'][ix]
        check(f'changed_point_full_cost_{ix}', enc(B) == saved['B'] and
              cross == [dot([Q(*v) for v in rr], parameter) for rr in saved['cross']]
              and required == dot(parameter, [dot([Q(*v) for v in rr], parameter) for rr in saved['cost']])
              and F-anchor == dot([Q(*v) for v in saved['fixed_minus_anchor']], parameter))
        for j, (r, q) in enumerate(free):
            check(f'original_beta_scaling_{ix}_{j}', row[j] == -Q(
                beta(68, 7, 7, a, 7-r)*beta(956, 7, 7, b, 7-q),
                d7*C(7, r)*C(61, r)*C(7, q)*C(949, q)))
        A.append(row)
        rhs.append(bound)
        modes.append({'mode': [a, b], 'B': B, 'cross': cross, 'D7': d7,
                      'pivots': pivots, 'ranges': ranges, 'energy': cost,
                      'F': F, 'anchor': anchor, 'required': required, 'rhs': bound})
    selected = tight['selected_indices']
    weights = [Q(*v) for v in tight['weights']]
    E = [A[i] for i in selected]
    eb = [rhs[i] for i in selected]
    check('old_zero_dual_here', min(weights) > 0 and dot(weights, eb) == 0
          and not any(dot(weights, cc) for cc in zip(*E)))
    L = [[Q(*v) for v in row] for row in tight['left_row_transform']]
    R = [[dot(l, cc) for cc in zip(*E)] for l in L]
    rb = [dot(l, eb) for l in L]
    piv = tight['pivots']
    check('coefficient_transform_only', R == [[Q(*v) for v in row[:-1]] for row in tight['rref']]
          and len(piv) == 23 and all(not any(row) for row in R[23:]))
    check('fresh_rhs_consistency', not any(rb[23:]))
    nonpiv = [j for j in range(36) if j not in piv]
    c, T = [Q(0)]*36, [[Q(0)]*13 for _ in range(36)]
    for k, j in enumerate(nonpiv):
        T[j][k] = Q(1)
    for i, j in enumerate(piv):
        c[j], T[j] = rb[i], [-R[i][k] for k in nonpiv]
    for i in selected:
        check(f'fresh_affine_system_{i}', dot(A[i], c) == rhs[i]
              and not any(dot(A[i], v) for v in zip(*T)))
    remaining = [i for i in range(64) if i not in selected]
    G = [[dot(A[i], v) for v in zip(*T)] for i in remaining]+[[-v for v in row] for row in T]
    g = [rhs[i]-dot(A[i], c) for i in remaining]+c
    labels = [('mode', i) for i in remaining]+[('nonnegative', j) for j in range(36)]
    scale = Q(10**18)
    scales = [max([abs(b)]+[abs(v*scale) for v in row]) or Q(1) for row, b in zip(G, g)]
    H = [[v*scale/s for v in row] for row, s in zip(G, scales)]
    h = [b/s for b, s in zip(g, scales)]
    out.update({'parameters': parameter[1:], 'rho': rho, 'pairs': p, 'free_column': f,
                'records': records, 'free': free, 'modes': modes, 'matrix': A, 'rhs': rhs,
                'selected': selected, 'zero_dual_weights': weights, 'transformed_rhs': rb,
                'affine_constant': c, 'affine_matrix': T, 'nonpivots': nonpiv,
                'reduced_matrix': G, 'reduced_rhs': g, 'reduced_labels': labels,
                'variable_scale': scale, 'row_scales': scales})
    save('full_original_and_fresh_reduced_system_saved')
    print(f'64 original rows/36 signs; fresh equality reduction rank 23; failures={failures}', flush=True)
    if failures:
        raise RuntimeError('Reconstruction failed; complete evidence saved')
    proposal = propose(H, h)
    out['proposal'] = proposal
    save('basis_proposal_saved')
    print(f'Proposal={proposal["status"]}; {len(proposal["trace"])} pivots; no numerical verdict used', flush=True)
    basis = proposal['basis']
    n, m = 13, len(G)
    certificate, verdict = {'kind': 'NONE'}, 'UNRESOLVED'
    if proposal['status'] == 'feasible_proposal':
        basic = set(basis)
        eq = [H[i] for i in range(m) if n+i not in basic]
        bs = [h[i] for i in range(m) if n+i not in basic]
        for j in range(n):
            if j not in basic:
                eq.append([Q(j == k) for k in range(n)])
                bs.append(Q(0))
        check('square_vertex', len(eq) == n)
        x = [scale*v for v in solve(eq, bs)]
        z = [v+dot(row, x) for v, row in zip(c, T)]
        slacks = [b-dot(row, z) for row, b in zip(A, rhs)]
        for i, v in enumerate(slacks):
            check(f'original_mode_slack_{i}', v >= 0 and (i not in selected or v == 0))
        for j, v in enumerate(z):
            check(f'original_sign_{j}', v >= 0)
        # Give a compact exact definition of the witness by original rows,
        # independent of discovery's reduced basis and old particular point.
        active = [('mode', i, A[i], rhs[i]) for i, s in enumerate(slacks) if s == 0]
        active += [('sign', j, [Q(j == k) for k in range(36)], Q(0))
                   for j, v in enumerate(z) if v == 0]
        echelon, defining = [], []
        for kind, index, row, bound in active:
            rr = list(row)
            for pivot, erow in echelon:
                rr = [a-rr[pivot]*b for a, b in zip(rr, erow)]
            pivot = next((j for j, v in enumerate(rr) if v), None)
            if pivot is not None:
                divisor = rr[pivot]
                echelon.append((pivot, [v/divisor for v in rr]))
                defining.append((kind, index, row, bound))
        check('36_independent_original_defining_rows', len(defining) == 36)
        fresh = solve([row for _, _, row, _ in defining], [b for _, _, _, b in defining])
        check('original_basis_uniquely_recovers_witness', fresh == z)
        certificate = {'kind': 'RATIONAL_WITNESS', 'z': z, 'x': x, 'mode_slacks': slacks,
                       'defining_rows': [(kind, index) for kind, index, _, _ in defining],
                       'raw_Y': [p[7]*zj/(C(7, r)*C(61, r)*C(7, q)*C(949, q))
                                 for zj, (r, q) in zip(z, free)]}
        verdict = 'FEASIBLE'
    elif proposal['status'] == 'infeasible_proposal':
        def column(j):
            return [Q(-1)]*m if j == -1 else [H[i][j] for i in range(m)] if j < n else [Q(i == j-n) for i in range(m)]
        lam0 = solve([column(j) for j in basis], [Q(-1 if j == -1 else 0) for j in basis])
        lam = [v/s for v, s in zip(lam0, scales)]
        redco = [dot(lam, v) for v in zip(*G)]
        check('phase_one_exact_separator', min(lam) >= 0 and min(redco) >= 0 and dot(lam, g) < 0)
        for k, j in enumerate(nonpiv):
            lam[40+j] += redco[k]
        mode, signs = [Q(0)]*64, [Q(0)]*36
        for value, (kind, j) in zip(lam, labels):
            (mode if kind == 'mode' else signs)[j] += value
        co = [dot(mode, cc)-signs[j] for j, cc in enumerate(zip(*A))]
        eta = [dot([-co[j] for j in piv]+[Q(0)], cc) for cc in zip(*L)]
        for i, v in zip(selected, eta):
            mode[i] += v
        tau = max([Q(0)]+[-mode[i]/v for i, v in zip(selected, weights)])
        for i, v in zip(selected, weights):
            mode[i] += tau*v
        norm = max(mode+signs)
        mode, signs = [v/norm for v in mode], [v/norm for v in signs]
        cancel = [dot(mode, cc)-signs[j] for j, cc in enumerate(zip(*A))]
        value = dot(mode, rhs)
        check('all_original_separator_signs', min(mode+signs) >= 0)
        check('all_36_original_cancellations', not any(cancel))
        check('strict_original_pairing', value < 0 and value == dot(lam, g)/norm)
        lo = value.numerator//value.denominator
        certificate = {'kind': 'RATIONAL_SEPARATOR', 'mode_weights': mode,
                       'sign_weights': signs, 'cancellations': cancel, 'rhs_pairing': value,
                       'integer_interval': [lo, lo+1], 'equality_zero_dual_shift': tau}
        verdict = 'INFEASIBLE'
    if failures:
        verdict = 'CERTIFICATE_FAILED'
    out['certificate'] = certificate
    out['summary'] = {'verdict': verdict, 'checks': len(checks), 'failures': len(failures),
                      'original_modes': 64, 'sign_rows': 36, 'forced_entries': 28,
                      'required': 'all original rows/signs, or nonnegative exact separator with pairing <0'}
    if certificate['kind'] == 'RATIONAL_WITNESS':
        out['summary'].update({'positive_z': sum(v > 0 for v in z), 'zero_z': sum(v == 0 for v in z),
                               'positive_modes': sum(v > 0 for v in slacks), 'zero_modes': sum(v == 0 for v in slacks)})
    if certificate['kind'] == 'RATIONAL_SEPARATOR':
        out['summary'].update({'pairing_interval': certificate['integer_interval'],
                              'positive_mode_weights': sum(v > 0 for v in mode),
                              'positive_sign_weights': sum(v > 0 for v in signs)})
    save('completed')
    print(json.dumps(out['summary'], sort_keys=True), flush=True)
    print(f'Failures={failures}; full certificate={OUT.relative_to(NB)}', flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

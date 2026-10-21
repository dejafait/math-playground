"""Fixed-point finite LP: Decimal basis discovery, original rational checks.

No mathematical verdict is taken from the numerical proposal. All rows,
affine transformations and complete rational evidence are saved to disk.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from pathlib import Path

from simultaneous_five_six_shell import propose, solve

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'zero-point-remaining-modes-results.json'


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
    return sum((-1)**(u-t)*C(u, t)*C(n-2*a, u-a)
               *C(n-a-u, l-u)*C(n-a-u, m-u)
               for u in range(max(a, t), min(l, m, n-a)+1))


def eigen(n, a, r):
    return sum((-1)**s*C(a, s)*C(7-a, r-s)*C(n-7-a, r-s)
               for s in range(r+1))


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), Q(0))


def main():
    paths = [ROOT/n for n in ['zero-point-tight-modes-results.json',
                              'zero-point-tight-modes-critical-audit.json',
                              'simultaneous-shell-ordinary-scalars-results.json',
                              'zero-dual-plane-scalars-results.json']]
    tight, audit, old, point = [json.loads(p.read_text()) for p in paths]
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

    for ix, d in enumerate([tight, audit, old, point]):
        check(f'clean_input_{ix}', not d['failures'])
        for path, digest in d.get('input_hashes', d.get('source_hashes', {})).items():
            check(f'input_hash_{ix}_{path}', hashlib.sha256((NB/path).read_bytes()).hexdigest() == digest)
    rho = (Q(C(1024, 64), C(68, 64))+1)/(2*C(1024, 68))
    p = [Q(*v) for v in point['pairs_through_13']]
    check('original_positive_scaling', rho > 0 and rho == Q(*tight['rho']) == Q(*old['rho'])
          and p[7] == Q(3539, 248922676958508) == Q(*tight['p7']) > 0)
    check('unchanged_fixed_point', tight['w_star'] == point['w_star'])
    base = {tuple(r['type']): Q(*r['value']) for r in tight['records'] if r['value'] is not None}
    free = [tuple(v) for v in tight['free']]
    check('exact_36_original_variables', free == [(r, q) for r in range(8) for q in range(8) if r+q >= 7])
    check('270_original_types', len(tight['records']) == 270 and len(base) == 234)
    check('28_forced_entries', sum(t[:2] == (7, 7) for t in base) == 28)
    check('fixed_nonnegative', all(v >= 0 for v in base.values()))
    sizes = {l: C(68, l)*C(956, l) for l in [5, 6, 7]}
    A, rhs, modes = [], [], []
    for a, b in it.product(range(8), repeat=2):
        ix = 8*a+b
        layers = [l for l in [5, 6] if max(a, b) <= l]
        d7 = C(68-2*a, 7-a)*C(956-2*b, 7-b)

        def block(l, m):
            value = sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*base[l, m, i, j]
                        for i, j in it.product(range(l+1), repeat=2))
            return value-(p[l]*p[m]*sizes[l]*sizes[m] if ix == 0 else 0)

        B = [[block(min(l, m), max(l, m)) for m in layers] for l in layers]
        cross = [block(l, 7) for l in layers]
        cost, residuals, pivots = Q(0), [], []
        if len(layers) == 2:
            x, t, z = B[0][0], B[0][1], B[1][1]
            u, v = cross
            pivots.append(x)
            if x > 0:
                cost += u*u/x
                z, v = z-t*t/x, v-t*u/x
            else:
                residuals.extend([t, u])
        elif layers:
            z, v = B[0][0], cross[0]
        else:
            z, v = Q(0), Q(0)
        pivots.append(z)
        check(f'old_psd_{ix}', all(x >= 0 for x in pivots))
        if z > 0:
            cost += v*v/z
        else:
            residuals.append(v)
        check(f'whole_singular_range_{ix}', not any(residuals))
        required = cost/(p[7]*d7)
        fixed = sum(base[7, 7, 7-r, 7-q]*eigen(68, a, r)*eigen(956, b, q)/p[7]
                    for r in range(8) for q in range(8) if r+q <= 6)
        anchor = p[7]*sizes[7] if ix == 0 else Q(0)
        bound = fixed-anchor-required
        row = [-Q(eigen(68, a, r)*eigen(956, b, q),
                  C(7, r)*C(61, r)*C(7, q)*C(949, q)) for r, q in free]
        saved = tight['modes'][ix]
        check(f'original_mode_{ix}', enc(B) == saved['B'] and enc(cross) == saved['cross']
              and enc(required) == saved['required'] and enc(fixed) == saved['F']
              and enc(anchor) == saved['anchor'] and enc(bound) == saved['rhs'] and d7 == saved['D7'])
        for j, (r, q) in enumerate(free):
            check(f'beta_scaling_{ix}_{j}', row[j] == -Q(beta(68, 7, 7, a, 7-r)*beta(956, 7, 7, b, 7-q),
                  d7*C(7, r)*C(61, r)*C(7, q)*C(949, q)))
        A.append(row)
        rhs.append(bound)
        modes.append({'mode': [a, b], 'B': B, 'cross': cross, 'D7': d7,
                      'pivots': pivots, 'range_residuals': residuals,
                      'required': required, 'F': fixed, 'anchor': anchor, 'rhs': bound})
    selected = tight['selected_indices']
    remaining = [i for i in range(64) if i not in selected]
    check('unchanged_24_equalities', [enc(A[i]) for i in selected] == tight['matrix']
          and [enc(rhs[i]) for i in selected] == tight['rhs'] and len(remaining) == 40)
    # z=c+T*x. The coordinates x are the original 13 nonpivot z's.
    rref = [[Q(*v) for v in row] for row in tight['rref']]
    piv = tight['pivots']
    nonpiv = [j for j in range(36) if j not in piv]
    c, T = [Q(0)]*36, [[Q(0)]*13 for _ in range(36)]
    check('rank_23_nullity_13', len(piv) == 23 and len(nonpiv) == 13)
    for k, j in enumerate(nonpiv):
        T[j][k] = Q(1)
    for i, j in enumerate(piv):
        c[j] = rref[i][-1]
        T[j] = [-rref[i][k] for k in nonpiv]
    for i in selected:
        check(f'affine_constant_{i}', dot(A[i], c) == rhs[i])
        check(f'affine_null_{i}', all(dot(A[i], v) == 0 for v in zip(*T)))
    # Remaining modes and all sign rows, before any positive row scaling.
    G, g, labels = [], [], []
    for i in remaining:
        G.append([dot(A[i], v) for v in zip(*T)])
        g.append(rhs[i]-dot(A[i], c))
        labels.append(['mode', i])
    for j in range(36):
        G.append([-v for v in T[j]])
        g.append(c[j])
        labels.append(['nonnegative', j])
    # Uniform positive variable scaling keeps discovery magnitudes moderate.
    scale = Q(10**18)
    row_scales = [max([abs(b)]+[abs(v*scale) for v in row]) or Q(1) for row, b in zip(G, g)]
    H = [[v*scale/s for v in row] for row, s in zip(G, row_scales)]
    h = [b/s for b, s in zip(g, row_scales)]
    out.update({'rho': rho, 'p7': p[7], 'w_star': Q(*tight['w_star']),
                'free': free, 'modes': modes, 'matrix': A, 'rhs': rhs,
                'selected': selected, 'remaining': remaining, 'nonpivots': nonpiv,
                'affine_constant': c, 'affine_matrix': T, 'reduced_matrix': G,
                'reduced_rhs': g, 'reduced_labels': labels, 'variable_scale': scale,
                'row_scales': row_scales, 'discovery_matrix': H, 'discovery_rhs': h})
    save('original_and_reduced_system_saved')
    print(f'Reconstructed 64 modes, 24 equalities, 40 remaining inequalities, 36 signs; reduced dimension=13; failures={failures}', flush=True)
    if failures:
        raise RuntimeError('Original system reconstruction failed')
    proposal = propose(H, h)
    out['proposal'] = proposal
    save('proposal_saved')
    print(f'Basis proposal={proposal["status"]}; pivots={len(proposal["trace"])}; numerical phase-I is discovery only (full value saved)', flush=True)
    # Tight constraints are the nonbasic slack variables; absent original
    # variables are fixed to zero. Reconstruct a rational point from that basis.
    B = proposal['basis']
    n, m = 13, len(G)
    if proposal['status'] == 'feasible_proposal':
        basic = set(B)
        equations = [H[i] for i in range(m) if n+i not in basic]
        bounds = [h[i] for i in range(m) if n+i not in basic]
        for j in range(n):
            if j not in basic:
                equations.append([Q(k == j) for k in range(n)])
                bounds.append(Q(0))
        check('square_proposed_vertex', len(equations) == n)
        y = solve(equations, bounds)
        x = [scale*v for v in y]
        z = [cc+dot(row, x) for cc, row in zip(c, T)]
        slacks = [b-dot(row, z) for row, b in zip(A, rhs)]
        for i in selected:
            check(f'original_equality_{i}', slacks[i] == 0)
        for i in remaining:
            check(f'original_remaining_inequality_{i}', slacks[i] >= 0)
        for j, value in enumerate(z):
            check(f'original_nonnegativity_{j}', value >= 0)
        reduced_slacks = [b-dot(row, x) for row, b in zip(G, g)]
        check('all_reduced_rows', all(v >= 0 for v in reduced_slacks))
        certificate = {'kind': 'RATIONAL_WITNESS', 'x': x, 'z': z,
                       'original_mode_slacks': slacks, 'reduced_slacks': reduced_slacks,
                       'vertex_matrix': equations, 'vertex_rhs': bounds}
        verdict = 'FEASIBLE' if not failures else 'CERTIFICATE_FAILED'
    elif proposal['status'] == 'infeasible_proposal':
        # In the phase-I basis, optimize -t with columns H*y+s-t=h.
        # Solve M^T*lambda=c_B for dual weights, then undo row scaling.
        def column(j):
            if j == -1:
                return [Q(-1)]*m
            if j < n:
                return [H[i][j] for i in range(m)]
            return [Q(i == j-n) for i in range(m)]
        lam_scaled = solve([column(j) for j in B], [Q(-1 if j == -1 else 0) for j in B])
        lam = [v/s for v, s in zip(lam_scaled, row_scales)]
        red_co = [dot(lam, col) for col in zip(*G)]
        val = dot(lam, g)
        check('reduced_separator_signs', all(v >= 0 for v in lam))
        check('reduced_separator_coefficients', all(v >= 0 for v in red_co))
        check('reduced_strict_contradiction', val < 0)
        # x>=0 is already among the sign rows; cancel the residual coefficients.
        for k, j in enumerate(nonpiv):
            lam[40+j] += red_co[k]
        check('reduced_free_cancellation', all(dot(lam, col) == 0 for col in zip(*G)))
        original = [Q(0)]*64
        signs = [Q(0)]*36
        for weight, (kind, index) in zip(lam, labels):
            if kind == 'mode':
                original[index] += weight
            else:
                signs[index] += weight
        combo = [dot(original, col)-signs[j] for j, col in enumerate(zip(*A))]
        # Add unrestricted selected equalities to cancel pivot coefficients.
        eta_rref = [-combo[j] for j in piv]+[Q(0)]
        L = [[Q(*v) for v in row] for row in tight['left_row_transform']]
        eta = [dot(eta_rref, col) for col in zip(*L)]
        for i, value in zip(selected, eta):
            original[i] += value
        cancel = [dot(original, col)-signs[j] for j, col in enumerate(zip(*A))]
        value = dot(original, rhs)
        check('original_separator_cancellation', not any(cancel))
        check('original_separator_signs', all(original[i] >= 0 for i in remaining) and all(v >= 0 for v in signs))
        check('original_strict_contradiction', value < 0 and value == dot(lam, g))
        # A positive rescaling makes a compact, basis-independent product dual.
        normalization = original[0]
        check('positive_dual_normalization', normalization > 0)
        original = [v/normalization for v in original]
        signs = [v/normalization for v in signs]
        value /= normalization
        hf = [original[8*a] for a in range(8)]
        kf = original[:8]
        check('product_dual', all(original[8*a+b] == hf[a]*kf[b]
                                  for a, b in it.product(range(8), repeat=2)))
        check('all_64_mode_weights_nonnegative', all(v >= 0 for v in original))
        check('no_sign_weights_needed', not any(signs))
        ht = [sum(hf[a]*eigen(68, a, r) for a in range(8)) for r in range(8)]
        kt = [sum(kf[b]*eigen(956, b, q) for b in range(8)) for q in range(8)]
        check('transform_cancellations', all(ht[r]*kt[q] == 0 for r, q in free))
        check('normalized_original_cancellations', all(dot(original, col)-signs[j] == 0
                                                       for j, col in enumerate(zip(*A))))
        check('normalized_pairing', dot(original, rhs) == value < 0)
        lower = value.numerator//value.denominator
        check('strict_integer_interval', Q(lower) <= value < Q(lower+1) < 0)
        certificate = {'kind': 'RATIONAL_SEPARATOR', 'mode_weights': original,
                       'nonnegative_weights': signs, 'coefficient_residuals': cancel,
                       'rhs_pairing': value, 'reduced_weights': lam,
                       'normalization': normalization, 'h': hf, 'k': kf,
                       'head_transform': ht, 'tail_transform': kt,
                       'rhs_interval': [lower, lower+1]}
        verdict = 'INFEASIBLE' if not failures else 'CERTIFICATE_FAILED'
    else:
        certificate, verdict = {'kind': 'NONE'}, 'UNRESOLVED'
    out['certificate'] = certificate
    out['summary'] = {'verdict': verdict, 'checks': len(checks), 'failures': len(failures),
                      'equalities': 24, 'remaining_modes': 40, 'nonnegative_variables': 36}
    if certificate['kind'] == 'RATIONAL_WITNESS':
        out['summary'].update({'positive_z': sum(v > 0 for v in z), 'zero_z': sum(v == 0 for v in z),
                               'positive_modes': sum(v > 0 for v in slacks), 'zero_modes': sum(v == 0 for v in slacks)})
    save('completed')
    print(f'Exact verdict={verdict}; checks={len(checks)}; failures={failures}; required: every original mode/sign and all selected equalities; certificate={OUT.relative_to(NB)}')
    if certificate['kind'] == 'RATIONAL_SEPARATOR':
        print(f'Actual fixed pairing in [{lower},{lower+1}); required >= 0; 36/36 coefficients cancel; all original mode weights nonnegative; sign weights zero')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

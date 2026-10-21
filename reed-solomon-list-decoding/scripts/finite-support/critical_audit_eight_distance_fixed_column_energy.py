"""L077 critical audit: full certificates, modal prescription and weighted lift.

Run the standalone independent actual-subset verifier first. This audit
imports no notebook module and uses exact standard-library arithmetic.
It independently rebuilds the polynomial basis and checks Q S = S B in
all 22500 coordinates, then solves every singular block by forward
elimination/back substitution and checks the original/transported action.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from math import comb, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'eight-distance-fixed-column-energy-critical-audit.json'


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def solve(matrix, rhs):
    """Independent forward echelon solve, free variables zero; retain trace."""
    rows = [[F(x) for x in row]+[F(y)] for row, y in zip(matrix, rhs)]
    n = len(matrix[0])
    pivots, trace = [], []
    for j in range(n):
        r = len(pivots)
        s = next((s for s in range(r, len(rows)) if rows[s][j]), None)
        if s is None:
            continue
        rows[r], rows[s] = rows[s], rows[r]
        pivot = rows[r][j]
        assert pivot != 0
        rows[r] = [x/pivot for x in rows[r]]
        factors = []
        for t in range(r+1, len(rows)):
            factor = rows[t][j]
            factors.append(factor)
            rows[t] = [x-factor*y for x, y in zip(rows[t], rows[r])]
        trace.append({'column': j, 'row': r, 'swap_row': s,
                      'nonzero_pivot': pivot, 'factors': factors,
                      'result': [row[:] for row in rows]})
        pivots.append(j)
    consistent = all(not any(row) for row in rows[len(pivots):])
    z = [F(0)]*n
    for r, j in reversed(list(enumerate(pivots))):
        z[j] = rows[r][-1]-sum(rows[r][k]*z[k] for k in range(j+1, n))
    return z, pivots, rows, trace, consistent


def integer_rows(Q):
    return [(d, [int(x*d) for x in row])
            for row in Q for d in [lcm(*(x.denominator for x in row))]]


def action(rows, z):
    zd = lcm(*(x.denominator for x in z))
    zi = [int(x*zd) for x in z]
    return [F(sum(x*y for x, y in zip(row, zi)), d*zd) for d, row in rows]


def main():
    names = ['eight-distance-fixed-column-energy-results.json',
             'eight-distance-modal-inverse-results.json',
             'eight-distance-fixed-column-energy-verification.json',
             'eight-distance-full-base-kernel-results.json',
             'eight-distance-full-base-kernel-critical-audit.json',
             'maximizer-excluded-anchor-results.json']
    paths = [ROOT/n for n in names]
    got, modal, ver, kernel, ka, src = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('all_input_failure_lists', all(not x['failures'] for x in (got, modal, ver, kernel, ka, src)))
    check('verifier_exact_binding', ver['constructor_sha256'] == hashlib.sha256(paths[0].read_bytes()).hexdigest())
    check('modal_exact_binding', got['modal_certificate_sha256'] == hashlib.sha256(paths[1].read_bytes()).hexdigest())
    for path, digest in got['input_hashes'].items():
        check('frozen_'+path, hashlib.sha256((NB/path).read_bytes()).hexdigest() == digest)
    check('complete_modal_evidence', got['modal_evidence'] == modal['modes'])
    rho = (F(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    p = [F(*x) for x in src['pairs_through_14']]
    p8 = F(16792471, 1181138102168120460)
    check('original_normalization', rho == F(*got['rho']) == F(*ver['rho']) > 0 and p[8] == p8 > 0)
    os = [(0, 0, 0)]+[(l, i, j) for l in (5, 6, 7) for i, j in it.product(range(l+1), repeat=2)]
    W = [1]+[comb(8, i)*comb(60, l-i)*comb(8, j)*comb(948, l-j) for l, i, j in os[1:]]
    check('complete_150_orbits', len(os) == 150 and list(map(list, os)) == got['orbits'] == kernel['orbits'])
    check('all_actual_weights', W == got['weights'] == ver['weights'] == kernel['weights'] and min(W) > 0)
    for l in (5, 6, 7):
        check('complete_weight_sum_'+str(l), sum(w for w, o in zip(W, os) if o[0] == l) == comb(68, l)*comb(956, l))
    Q = [[F(*x) for x in row] for row in ver['action']]
    check('complete_action_dimensions', len(Q) == 150 and all(len(row) == 150 for row in Q))
    check('independent_action_agreement', ver['action'] == got['action'] == ka['direct_orbit_action'])
    for a in range(150):
        check('weighted_self_adjoint_'+str(a), all(W[a]*Q[a][j] == W[j]*Q[j][a] for j in range(150)))
        check('anchor_action_'+str(a), (Q[a][0] == Q[0][a] == 1) if a == 0
              else Q[a][0] == p[os[a][0]] and Q[0][a] == p[os[a][0]]*W[a])
    b = [F(*x) for x in ver['column']]
    check('entire_immutable_column', len(b) == 150 and enc(b) == got['column'] == kernel['complete_column'] and b[0] == p8)
    check('exact_active_set', kernel['active_zero_indices'] == [27, 33, 56, 63]
          and got['parameters'] == kernel['chosen_parameters'] and got['free_solution'] == kernel['solution'])

    # Build monic orthogonal polynomials from moment equations, not from
    # the constructor's Gram-Schmidt vectors or the inverse proposal.
    factors, norms, factor_records = {}, {}, []
    records = {(r['n'], r['layer']): r for r in kernel['factor_bases']}
    for n, l in it.product((68, 956), (5, 6, 7)):
        weights = [comb(8, i)*comb(n-8, l-i) for i in range(l+1)]
        moments = [sum(w*i**d for i, w in enumerate(weights)) for d in range(2*l+1)]
        basis, ns = [], []
        for a in range(l+1):
            coeff = [] if not a else solve([[F(moments[t+s]) for s in range(a)] for t in range(a)],
                                           [-F(moments[t+a]) for t in range(a)])[0]
            values = [F(i**a)+sum(x*i**s for s, x in enumerate(coeff)) for i in range(l+1)]
            norm = sum(w*x*x for w, x in zip(weights, values))
            check('monic_orthogonal_'+str((n, l, a)), norm > 0 and all(
                sum(w*x*i**t for i, (w, x) in enumerate(zip(weights, values))) == 0 for t in range(a)))
            basis.append(values)
            ns.append(norm)
        check('all_factor_values_'+str((n, l)), enc(basis) == records[n, l]['basis']
              and enc(ns) == records[n, l]['norms'] and weights == records[n, l]['weights'])
        factors[n, l], norms[n, l] = basis, ns
        factor_records.append({'n': n, 'layer': l, 'weights': weights, 'basis': basis, 'norms': ns})

    rows = integer_rows(Q)
    modes = list(it.product(range(8), repeat=2))
    check('complete_mode_domain', [r['mode'] for r in kernel['blocks']] == list(map(list, modes)))
    check('complete_modal_domain', [r['mode'] for r in modal['modes']] == list(map(list, modes)))
    z, audit_modes, dimension, rank = [F(0)]*150, [], 0, 0
    for block, saved, (a, h) in zip(kernel['blocks'], modal['modes'], modes):
        layers = ([0] if (a, h) == (0, 0) else [])+[l for l in (5, 6, 7) if l >= max(a, h)]
        check('mode_layers_'+str((a, h)), layers == block['layers'] == saved['layers'])
        basis = [[F(0) if m != l else F(1) if not l else factors[68, l][a][i]*factors[956, l][h][j]
                  for m, i, j in os] for l in layers]
        nn = [F(1) if not l else norms[68, l][a]*norms[956, l][h] for l in layers]
        check('mode_norms_'+str((a, h)), enc(nn) == block['norms'] and all(x > 0 for x in nn))
        B = [[F(*x) for x in row] for row in block['action']]
        transform_residuals = []
        for j, vector in enumerate(basis):
            values = action(rows, vector)
            residual = [x-sum(basis[k][t]*B[k][j] for k in range(len(layers))) for t, x in enumerate(values)]
            for t, value in enumerate(residual):
                check('direct_QS_SB_'+str((a, h, j, t)), value == 0)
            transform_residuals.append(residual)
        rhs = [sum(w*x*y for w, x, y in zip(W, vector, b))/norm for vector, norm in zip(basis, nn)]
        check('original_modal_rhs_'+str((a, h)), enc(rhs) == saved['rhs'])
        local, pivots, echelon, trace, consistent = solve(B, rhs)
        check('all_singular_zero_rows_'+str((a, h)), consistent)
        check('same_canonical_free_zero_solve_'+str((a, h)), enc(local) == saved['inverse'] and pivots == block['pivots'])
        residual = [sum(x*y for x, y in zip(row, local))-y for row, y in zip(B, rhs)]
        check('all_original_modal_rows_'+str((a, h)), not any(residual))
        for t in range(150):
            z[t] += sum(vector[t]*v for vector, v in zip(basis, local))
        audit_modes.append({'mode': (a, h), 'layers': layers, 'norms': nn,
                            'direct_action_residuals': transform_residuals, 'rhs': rhs,
                            'pivots': pivots, 'echelon': echelon, 'elimination': trace,
                            'inverse': local, 'original_residuals': residual})
        dimension += len(layers)
        rank += len(pivots)
    check('complete_dimensions_and_pivots', dimension == 150 and rank == 60)
    check('entire_reconstructed_inverse', enc(z) == got['inverse_action'] == modal['inverse_action'] == ver['inverse_action'])
    print('Rebuilt all 64 modal solves and checked all 22500 direct Q S = S B coordinates.', flush=True)
    products = action(rows, z)
    residuals = [x-y for x, y in zip(products, b)]
    for a, value in enumerate(residuals):
        check('original_inverse_'+str(a), value == 0 and enc(value) == got['inverse_residuals'][a]
              == modal['inverse_residuals'][a] == ver['inverse_residuals'][a])
    r = [b[t]-p[l]*p8 for t, (l, i, j) in enumerate(os) if t]
    H = [[Q[t][s]-p[l]*p[m]*W[s] for s, (m, u, v) in enumerate(os) if s]
         for t, (l, i, j) in enumerate(os) if t]
    transported = [x-y for x, y in zip(action(integer_rows(H), z[1:]), r)]
    check('entire_transported_column', enc(r) == ver['transported_column'])
    for a, value in enumerate(transported):
        check('transported_inverse_'+str(a+1), value == 0 and enc(value) == ver['transported_residuals'][a])
    terms = [w*x*y for w, x, y in zip(W, b, z)]
    anchor_terms = [p8*p8]+[w*x*y for w, x, y in zip(W[1:], r, z[1:])]
    for t, value in enumerate(terms):
        check('actual_weight_energy_'+str(t), enc(value) == got['weighted_energy_contributions'][t]
              == modal['weighted_energy_contributions'][t] == ver['weighted_energy_contributions'][t])
        check('anchor_energy_'+str(t), enc(anchor_terms[t]) == ver['anchor_energy_contributions'][t])
    E = sum(terms)
    bilinear = sum(w*x*y for w, x, y in zip(W, z, products))
    check('full_anchor_and_bilinear_identity', E == sum(anchor_terms) == bilinear and anchor_terms[0] > 0)
    ratio, slack = E/p8, p8-E
    gaps = [10**12*ratio.numerator-1461591*ratio.denominator,
            1461592*ratio.denominator-10**12*ratio.numerator]
    check('exact_manuscript_bounds', gaps[0] >= 0 and gaps[1] > 0 and F(1461592, 10**12) < 1)
    check('strict_singular_schur_slack', E >= 0 and slack > 0)
    for obj, name in ((got, 'constructor'), (modal, 'modal'), (ver, 'verifier')):
        check('full_ratio_and_energy_'+name, enc(E) == obj['energy'] and enc(ratio) == obj['energy_ratio']
              and enc(slack) == obj['schur_remainder'] and enc(p8) == obj['required_diagonal'])
        check('exact_interval_and_verdict_'+name, [F(*x) for x in obj['summary']['ratio_interval']]
              == [F(1461591, 10**12), F(1461592, 10**12)] and obj['summary']['verdict'] == 'PSD_EXTENSION')
    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'summary': {'checks': len(checks), 'failures': len(failures), 'verdict': 'RETAIN_L077' if not failures else 'AUDIT_FAILED',
                       'mode_count': len(audit_modes), 'dimension': dimension, 'nonzero_pivots': rank,
                       'direct_action_coordinates': 22500, 'ratio_interval': [F(1461591, 10**12), F(1461592, 10**12)],
                       'required_ratio_upper_bound': 1, 'strict_positive_remainder': slack > 0},
           'checks': checks, 'failures': failures, 'factor_reconstruction': factor_records, 'modes': audit_modes,
           'orbits': os, 'weights': W, 'inverse_action': z, 'original_residuals': residuals,
           'transported_column': r, 'transported_residuals': transported,
           'weighted_energy_contributions': terms, 'anchor_energy_contributions': anchor_terms,
           'energy': E, 'energy_ratio': ratio, 'required_diagonal': p8, 'schur_remainder': slack,
           'integer_ratio_comparison_gaps': gaps}
    OUT.write_text(json.dumps(enc(out), indent=2)+'\n')
    print('Exact audit checks:', len(checks), '; failures:', failures)
    print('Actual E/p8 in [1461591,1461592)/10^12; required <= 1; verdict:', out['summary']['verdict'])
    print('Full certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

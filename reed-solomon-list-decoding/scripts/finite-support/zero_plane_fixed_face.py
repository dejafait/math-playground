"""One exact fixed-face test; no optimizer, new weights or parameter scan.

All affine coefficients are checked, including zero and empty source modes.
The saved rank-one factorizations specify complete rational multipliers and
compressed pencils without repeating large outer products 45 times.
"""
import hashlib
import itertools as it
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, basis_solve, enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'zero-plane-fixed-face-results.json'


def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b)), F(0))


def tr(A):
    return list(map(list, zip(*A))) if A else []


def mm(A, B):
    return [[dot(r, c) for c in zip(*B)] for r in A]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def dec(A):
    return [[F(*v) for v in r] for r in A]


def pencil(B, c, f, j):
    """Coefficient j=0 constant, 1..3 plane parameters, 4..48 moments."""
    n = len(B)
    M = [[F(0)]*(n+1) for _ in range(n+1)]
    if j == 0:
        for a in range(n):
            for b in range(n):
                M[a][b] = B[a][b]
    if j < 4:
        for a in range(n):
            M[a][n] = M[n][a] = c[a][j]
    M[n][n] = f[j]
    return M


def main():
    names = ['zero-plane-joint-feasibility-results.json',
             'zero-plane-joint-feasibility-verification.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'fully-cancelling-separator-family-results.json',
             'fully-cancelling-separator-family-verification.json',
             'zero-plane-positive-mode-compatibility-results.json',
             'zero-plane-positive-mode-compatibility-verification.json',
             'eight-common-column-joint-completion-critical-audit.json',
             'eight-distance-full-base-kernel-results.json']
    paths = [ROOT/n for n in names]
    model, mv, audit, source, ver, eq, ev, a82, col = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'coefficient_order': ['constant', 't56', 't63', 't69']+['z_'+str(j) for j in range(45)],
           'blocks': []}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        out.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(out), indent=2)+'\n')

    for name, obj in zip(names, [model, mv, audit, source, ver, eq, ev, a82, col]):
        check('clean_'+name, not obj['failures'])
        for rel, digest in obj.get('input_hashes', {}).items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p8 = F(16792471, 1181138102168120460)
    s = F(*eq['stationary_t78'])
    free = list(it.product(range(9), repeat=2))
    free = [(r, q) for r, q in free if r+q >= 8]
    family = [[F(*v)]+[F(*x) for x in r] for v, r in zip(col['affine']['intercept'], col['affine']['slopes'])]
    domain = [[r[0]+s*r[4]]+r[1:4] for r in family]
    check('complete_domain', len(domain) == 85 and enc(domain) == model['domain'] == eq['domain'] == ev['domain'])
    check('unchanged_original_family', enc(family) == audit['family'] == source['domain'] == ver['domain'])
    check('all_90_original_equations', all([sum((F(*v)*f[j] for v, f in zip(row, family)), F(0)) for j in range(5)] == [F(*rhs)]+[F(0)]*4 for row, rhs in zip(col['equations'], col['rhs'])) and len(col['equations']) == 90)
    check('full_weighted_kernel_contract', source['weighted_kernel_residuals'] == audit['weighted_kernel_residuals'] == ver['weighted_kernel_residuals'] and len(audit['weighted_kernel_residuals']) == 90 and all(not any(F(*v) for v in r) for r in audit['weighted_kernel_residuals']))
    check('full_affine_column_contract', source['affine_column'] == audit['affine_column'])
    check('500_types_3000_presentations', len(audit['records']) == 500 and sum(len(r['presentations']) for r in ver['records']) == 3000)
    for k, (r, v) in enumerate(zip(audit['records'], ver['records'])):
        check('whole_key_'+str(k), r['key'] == v['key'] and r['type'] == v['type'] and r['affine'] == v['affine'])
    rows = []
    for k, m in enumerate(audit['modes']):
        a, b = divmod(k, 9)
        D = C(68-2*a, 8-a)*C(956-2*b, 8-b)
        row = [-F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q), D*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r, q in free]
        check('original_beta_'+str(k), enc(row) == m['row'] == model['matrix'][k] == a82['matrix'][k] == eq['full_matrix'][k])
        rows.append(row)
    manuscript = (NB/'lemmas/L082-common-column-joint-completion-obstruction.md').read_text()
    part = manuscript.split('**Canonical exact separator.**')[1].split('Let K_')[0]
    I = [int(v) for v in re.search(r'I=\((.*?)\)', part, re.S).group(1).replace('\n','').split(',')]
    Kt = [[F(-1) if j == -1 else rows[i][j] for i in I] for j in [-1]+list(range(45))]
    local, pivots = basis_solve(Kt, [F(-1)]+[F(0)]*45)
    y = [F(0)]*81
    for k, v in zip(I, local):
        y[k] = v
    check('canonical_system', len(pivots) == 46 and all(pivots) and [dot(r, local) for r in Kt] == [F(-1)]+[F(0)]*45)
    check('unchanged_weights', enc(y) == audit['dual'] == eq['weights'] == source['weights'] == ver['weights'] == a82['dual'] and min(y) == 0 and sum(y) == 1)
    selected = [i for i, v in enumerate(y) if v > 0]
    check('exact_28_support', selected == model['selected_modes'] == eq['selected_modes'] and len(selected) == 28)
    out.update(weights=y, selected_modes=selected, stationary_t78=s, domain=domain, free=free,
               moment_sign_rows='all 45 original z>=0, equivalently all raw Y>=0; unchanged',
               untouched_modes=[i for i in range(81) if i not in selected])
    save('before_fixed_multiplier_test')
    trace = [F(0)]*49
    original_trace = [F(0)]*49
    raw_trace = [F(0)]*45
    dimensions, reduced_dimensions = [], []
    total_rank = 0
    for k, (m, block) in enumerate(zip(audit['modes'], model['blocks'])):
        norm = F(*block['positive_original_norm'])
        check('positive_original_norm_'+str(k), norm == p8*C(68-2*(k//9), 8-k//9)*C(956-2*(k%9), 8-k%9) and norm > 0)
        B = [[v/norm for v in r] for r in dec(m['source_base'])]
        c5 = [[v/norm for v in r] for r in dec(m['source_cross'])]
        c = [[r[0]+s*r[4]]+r[1:4] for r in c5]
        f5 = [F(*v) for v in m['forced']]
        f5[0] -= F(*m['anchor'])
        f = [f5[0]+s*f5[4]]+f5[1:4]+[-v for v in rows[k]]
        check('original_affine_block_'+str(k), enc(B) == block['original_base'] and enc(c) == block['original_cross_plane'] and enc(f[:4]) == block['fixed_plane'])
        inv = dec(m['inverse_affine'])
        check('all_original_range_coefficients_'+str(k), mm(dec(m['source_base']), inv) == dec(m['source_cross']) if B else not c)
        T, R, TC = dec(block['congruence']), dec(block['diagonalized_base']), dec(block['transformed_cross_plane'])
        check('whole_fixed_congruence_'+str(k), mm(mm(T, B), tr(T)) == R and mm(T, c) == TC if B else not R and not TC)
        check('invertible_congruence_'+str(k), all(T[i][i] == 1 and all(T[i][j] == 0 for j in range(i+1,len(T))) for i in range(len(T))))
        check('diagonal_nonnegative_base_'+str(k), all(R[i][j] == 0 for i in range(len(R)) for j in range(len(R)) if i != j) and all(R[i][i] >= 0 for i in range(len(R))))
        active = [i for i in range(len(B)) if R[i][i] > 0]
        check('zero_rows_and_cross_identically_zero_'+str(k), all(not any(R[i]) and not any(TC[i]) for i in range(len(B)) if i not in active))
        d, c = [R[i][i] for i in active], [TC[i] for i in active]
        r = len(d)
        check('retained_source_blocks_'+str(k), active == block['retained_indices'] and enc(d) == block['positive_diagonal'] and enc(c) == block['cross_plane'])
        # Undo the prior base-kernel removal in every affine coefficient.
        # T is unit lower triangular, so its inverse is an exact finite series.
        n = len(B)
        Tinv = eye(n)
        for i in range(n):
            for j in range(i):
                Tinv[i][j] = -sum((T[i][h]*Tinv[h][j] for h in range(j,i)), F(0))
        check('prior_congruence_inverse_'+str(k), mm(T,Tinv) == mm(Tinv,T) == eye(n) if n else not Tinv)
        lift = [[Tinv[i][a] for a in active]+[F(0)] for i in range(n)]+[[F(0)]*r+[F(1)]]
        diag = [[d[i] if i == j else F(0) for j in range(r)] for i in range(r)]
        oc = [[row[0]+s*row[4]]+row[1:4] for row in c5]
        for j in range(49):
            check('complete_original_block_pullback_'+str((k,j)), mm(mm(lift,pencil(diag,c,f,j)),tr(lift)) == pencil(B,oc,f,j))
        dimensions.append(r+1)
        reduced_dimensions.append(r if k in selected else r+1)
        if k not in selected:
            out['blocks'].append({'mode': k, 'weight': F(0), 'kernel_basis': eye(r+1), 'complement_basis': [], 'compressed_pencil': 'unchanged step-298 retained block', 'face_equations': []})
            continue
        check('constant_cross_on_whole_plane_'+str(k), all(not any(row[1:]) for row in c))
        if any(any(row[1:]) for row in c):
            save('failed_constancy')
            raise SystemExit('Fixed multiplier fails: cross depends on plane parameters')
        x = [row[0]/v for row, v in zip(c, d)]
        v = [-u for u in x]+[F(1)]
        # S_i = y_i v_i v_i^T; positive rank one by y_i>0, v_i[-1]=1.
        S = [[y[k]*a*b for b in v] for a in v]
        U = eye(r)+[x[:]] if r else [[]]
        H = [row+[v[i]] for i, row in enumerate(U)]
        h = F(1)+dot(x, x)
        Hinv = [[F(i == j)-x[i]*x[j]/h for j in range(r)]+[x[i]/h] for i in range(r)]+[[-u/h for u in x]+[F(1)/h]]
        check('PSD_nontrivial_multiplier_'+str(k), y[k] > 0 and v[-1] == 1 and S == tr(S) and S[-1][-1] > 0)
        check('complete_kernel_and_complement_'+str(k), [dot(v, col) for col in zip(*U)] == [F(0)]*r and mm(H, Hinv) == mm(Hinv, H) == eye(r+1))
        check('all_kernel_directions_'+str(k), mm(S, U) == [[F(0)]*r for _ in range(r+1)] if r else all(not row for row in U))
        ov = [sum((T[a][j]*v[h] for h, a in enumerate(active)), F(0)) for j in range(len(B))]+[F(1)]
        # The original normalized block uses c5 restricted to the plane.
        oc = [[row[0]+s*row[4]]+row[1:4] for row in c5]
        diag = [[d[i] if i == j else F(0) for j in range(r)] for i in range(r)]
        local_trace, face_vectors, compressed_first = [], [], []
        slack = f[:]
        slack[0] -= sum((row[0]**2/vv for row, vv in zip(c, d)), F(0))
        for j in range(49):
            L = pencil(diag, c, f, j)
            original = pencil(B, oc, f, j)
            value = dot(v, [dot(row, v) for row in L])
            direct = dot(ov, [dot(row, ov) for row in original])
            trace[j] += y[k]*value
            original_trace[j] += y[k]*direct
            check('original_multiplier_transport_'+str((k,j)), value == direct == slack[j])
            local_trace.append(y[k]*value)
            if j >= 4:
                rr, qq = free[j-4]
                raw_trace[j-4] += y[k]*direct*C(8,rr)*C(60,rr)*C(8,qq)*C(948,qq)/p8
            # Check every mixed and removed coefficient, not compressed PSD alone.
            transformed = mm(mm(tr(H), L), H)
            compressed = [row[:r] for row in transformed[:r]]
            mixed = [row[-1] for row in transformed[:r]]
            removed = transformed[-1][-1]
            check('complete_face_equations_'+str((k,j)), mixed == [u*slack[j] for u in x] and removed == slack[j])
            check('full_coefficient_pullback_'+str((k,j)), mm(mm(tr(Hinv), transformed), Hinv) == L)
            check('compressed_affine_formula_'+str((k,j)), compressed == [[(d[a] if j == 0 and a == b else F(0))+((dot([row[0] for row in c],x) if j == 0 else F(0))+slack[j])*x[a]*x[b]+(c[a][0]*x[b]+x[a]*c[b][0] if j == 0 else F(0)) for b in range(r)] for a in range(r)])
            if j < 4:
                compressed_first.append(compressed)
            face_vectors.append(mixed+[removed])
        check('selected_bound_becomes_affine_'+str(k), [F(*v) for v in eq['rhs_coefficients'][selected.index(k)]] == slack[:4]+[F(0)]*6)
        out['blocks'].append({'mode': k, 'weight': y[k], 'rank': 1,
                              'multiplier_vector': v, 'original_multiplier_vector': ov,
                              'kernel_basis': U, 'complement_vector': v,
                              'basis_inverse': Hinv, 'positive_base_diagonal': d,
                              'constant_cross': [row[0] for row in c],
                              'face_equation_coefficients': face_vectors,
                              'scalar_face_equation': slack,
                              'compressed_first_four_coefficients': compressed_first,
                              'compressed_moment_coefficients': '(-A_i,j) * x*x^T; x=last row of kernel_basis',
                              'weighted_trace_coefficients': local_trace,
                              'PSD_after_face_equations': 'U^T*[I;x^T]*diag(d)*[I,x]*U, positive definite when r>0; empty when r=0'})
        total_rank += 1
    check('all_81_blocks_retained', len(out['blocks']) == 81)
    check('all_49_trace_coefficients_zero', trace == original_trace == [F(0)]*49)
    check('all_45_raw_trace_coefficients_zero', raw_trace == [F(0)]*45)
    check('nontrivial_after_prior_kernel_removal', total_rank == 28 and sum(dimensions)-sum(reduced_dimensions) == 28)
    out.update(trace_coefficients=trace, original_trace_coefficients=original_trace,
               raw_moment_trace_coefficients=raw_trace,
               retained_dimensions=dimensions, reduced_dimensions=reduced_dimensions)
    out['summary'] = {'verdict': 'FIXED_PARTIAL_FACE_VERIFIED' if not failures else 'FAILED',
                      'checks': len(checks), 'failures': len(failures), 'modes': 81,
                      'positive_rank_one_blocks': total_rank, 'old_retained_total_size': sum(dimensions),
                      'new_total_size': sum(reduced_dimensions), 'trace_coefficient_actual': trace,
                      'trace_coefficient_required': 0, 'parameter_count': 3, 'moment_count': 45,
                      'domain_rows': 85, 'all_mixed_and_removed_equations_retained': True,
                      'new_numerical_solves': 0, 'full_plane_feasibility': 'UNDECIDED',
                      'minimal_face_asserted': False, 'strict_feasibility_asserted': False}
    save('completed_fixed_face_test')
    print('Fixed face:', out['summary']['verdict'], '; checks', len(checks), '; failures', failures, flush=True)
    print('Rank', total_rank, '; retained sizes', sum(dimensions), '->', sum(reduced_dimensions),
          '; all 49 trace coefficients actual=0 required=0; 45 raw coefficients actual=0 required=0', flush=True)
    print('Full-plane feasibility UNDECIDED; no solve. Certificate:', OUT.relative_to(NB), flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

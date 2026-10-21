"""Check the fixed certificate directly in original source coordinates.

No constructor, optimizer or generalized-inverse algorithm is invoked.
This arithmetic verification is not the later separate critical proof audit.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'zero-plane-fixed-face-verification.json'


def dec(M):
    return [[F(*v) for v in row] for row in M]


def dot(a,b):
    assert len(a) == len(b)
    return sum((u*v for u,v in zip(a,b)), F(0))


def mul(A,B):
    assert not A or len(A[0]) == len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]) if B else 0)] for i in range(len(A))]


def main():
    names = ['zero-plane-fixed-face-results.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'zero-plane-positive-mode-compatibility-results.json',
             'zero-plane-joint-feasibility-results.json']
    paths = [ROOT/n for n in names]
    face, source, eq, old = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for name, data in zip(names, [face,source,eq,old]):
        check('clean_'+name, not data['failures'])
        for rel, digest in data['input_hashes'].items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    y = [F(*v) for v in face['weights']]
    check('unchanged_weights', face['weights'] == source['dual'] == eq['weights'] and min(y) == 0 and sum(y) == 1)
    s = F(*face['stationary_t78'])
    p8 = F(16792471,1181138102168120460)
    check('unchanged_plane_and_domain', face['stationary_t78'] == source['stationary_t78'] == eq['stationary_t78'] and face['domain'] == eq['domain'] == old['domain'])
    selected = [k for k in range(81) if y[k] > 0]
    check('complete_positive_support', selected == face['selected_modes'] == eq['selected_modes'] and len(selected) == 28)
    totals, rawtotals, records = [F(0)]*49, [F(0)]*45, []
    sizes, reduced = [], []
    for k, (m,b) in enumerate(zip(source['modes'],face['blocks'])):
        r = len(old['blocks'][k]['positive_diagonal'])
        sizes.append(r+1)
        reduced.append(r if k in selected else r+1)
        check('mode_index_'+str(k), b['mode'] == k)
        if k not in selected:
            check('untouched_full_block_'+str(k), F(*b['weight']) == 0 and dec(b['kernel_basis']) == [[F(i==j) for j in range(r+1)] for i in range(r+1)] and b['face_equations'] == [])
            continue
        a,q = divmod(k,9)
        norm = p8*C(68-2*a,8-a)*C(956-2*q,8-q)
        B = [[v/norm for v in row] for row in dec(m['source_base'])]
        cross5 = [[v/norm for v in row] for row in dec(m['source_cross'])]
        cross = [[row[0]+s*row[4]]+row[1:4] for row in cross5]
        ov = [F(*v) for v in b['original_multiplier_vector']]
        x0 = [-v for v in ov[:-1]]
        check('original_constancy_'+str(k), all(not any(row[1:]) for row in cross))
        check('original_kernel_equation_'+str(k), [dot(row,x0) for row in B] == [row[0] for row in cross] and ov[-1] == 1)
        forced = [F(*v) for v in m['forced']]
        forced[0] -= F(*m['anchor'])
        f = [forced[0]+s*forced[4]]+forced[1:4]
        A = [-F(beta(68,8,8,a,8-u)*beta(956,8,8,q,8-v),
                C(68-2*a,8-a)*C(956-2*q,8-q)*C(8,u)*C(60,u)*C(8,v)*C(948,v)) for u,v in face['free']]
        f += [-v for v in A]
        # Direct original-coordinate v^T L_j v, with both cross directions.
        coeff = f[:]
        coeff[0] += sum((x0[i]*B[i][j]*x0[j] for i in range(len(B)) for j in range(len(B))),F(0))
        for j in range(4):
            coeff[j] -= 2*sum((x0[i]*cross[i][j] for i in range(len(B))),F(0))
        for j in range(49):
            totals[j] += y[k]*coeff[j]
        check('all_original_trace_coefficients_'+str(k), enc([y[k]*v for v in coeff]) == b['weighted_trace_coefficients'])
        check('all_original_scalar_face_coefficients_'+str(k), enc(coeff) == b['scalar_face_equation'] and enc(coeff[:4]+[F(0)]*6) == eq['rhs_coefficients'][selected.index(k)])
        for j,(u,v) in enumerate(face['free']):
            rawtotals[j] += y[k]*coeff[j+4]*C(8,u)*C(60,u)*C(8,v)*C(948,v)/p8
        U, Hi = dec(b['kernel_basis']), dec(b['basis_inverse'])
        vv = [F(*v) for v in b['multiplier_vector']]
        x = U[-1]
        H = [row+[vv[i]] for i,row in enumerate(U)]
        identity = [[F(i==j) for j in range(r+1)] for i in range(r+1)]
        check('full_rank_kernel_complement_'+str(k), mul(H,Hi) == mul(Hi,H) == identity and vv == [-v for v in x]+[F(1)] and all(dot(vv,col) == 0 for col in zip(*U)))
        d = [F(*v) for v in b['positive_base_diagonal']]
        c = [F(*v) for v in b['constant_cross']]
        check('retained_positive_base_'+str(k), all(v>0 for v in d) and c == [v*w for v,w in zip(d,x)] and y[k]>0)
        # On the face the compressed block is (I+xx^T) D (I+xx^T).
        K = [[F(i==j)+x[i]*x[j] for j in range(r)] for i in range(r)]
        positive_compressed = [[sum((K[h][i]*d[h]*K[h][j] for h in range(r)),F(0)) for j in range(r)] for i in range(r)]
        actual = dec(b['compressed_first_four_coefficients'][0])
        check('compressed_PSD_factorization_'+str(k), actual == [[positive_compressed[i][j]+coeff[0]*x[i]*x[j] for j in range(r)] for i in range(r)])
        for j in range(1,4):
            check('compressed_parameter_'+str((k,j)), dec(b['compressed_first_four_coefficients'][j]) == [[coeff[j]*x[h]*x[l] for l in range(r)] for h in range(r)])
        check('all_mixed_and_removed_equations_'+str(k), dec(b['face_equation_coefficients']) == [[v*t for v in x]+[t] for t in coeff])
        records.append({'mode':k, 'original_trace_coefficients':coeff, 'positive_compressed_on_face':positive_compressed})
    check('complete_zero_affine_trace', totals == [F(0)]*49 and enc(totals) == face['trace_coefficients'] == face['original_trace_coefficients'])
    check('complete_zero_raw_trace', rawtotals == [F(0)]*45 and enc(rawtotals) == face['raw_moment_trace_coefficients'])
    check('nontrivial_28_rank_reduction', sum(sizes) == 140 and sum(reduced) == 112 and len(records) == 28)
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checks':checks,'failures':failures,'selected_original_records':records,
              'original_trace_coefficients':totals,'raw_trace_coefficients':rawtotals,
              'summary':{'verdict':'VERIFIED_FIXED_PARTIAL_FACE' if not failures else 'FAILED',
                         'checks':len(checks),'failures':len(failures),'original_trace_actual':0,
                         'required_trace':0,'removed_rank':28,'retained_size':140,'reduced_size':112,
                         'full_plane_feasibility':'UNDECIDED','critical_proof_audit':'PENDING'}}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print(report['summary'], flush=True)
    print('Failures:',failures,'; evidence:',OUT.relative_to(NB),flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

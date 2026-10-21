"""L086 critical audit: original rows plus replay of a fixed saved trace.

No optimizer invocation, new pivot search, or omitted-mode feasibility test.
Ancestor reconstruction and original-row verification write separate artifacts.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import critical_audit_zero_plane_positive_mode_compatibility as ancestral
import verify_affine_sign_phase_one as original

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'affine-sign-phase-one-critical-audit.json'


def dec(M):
    return [[F(*v) for v in row] for row in M]


def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b) if x and y), F(0))


def mul(A, B):
    assert not A or len(A[0]) == len(B)
    return [[dot(r, c) for c in zip(*B)] for r in A]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def main():
    ancestral.OUT = ROOT / 'affine-sign-critical-ancestor-reconstruction.json'
    ancestral.main()
    original.OUT = ROOT / 'affine-sign-critical-original-verification.json'
    original.main()
    names = ['affine-sign-phase-one-results.json',
             'affine-sign-phase-one-initial-state.json',
             'affine-sign-phase-one-state.json',
             'affine-sign-phase-one-verification.json',
             ancestral.OUT.name, original.OUT.name,
             'zero-plane-positive-mode-compatibility-results.json']
    paths = [ROOT/n for n in names]
    data, initial, final, saved_ver, source, fresh, eq = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    report = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        report.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(original.enc(report), indent=2)+'\n')

    check('all_original_checks_pass', not source['failures'] and not fresh['failures'] and not saved_ver['failures'])
    for field in ['original_point', 'raw_point', 'domain_values', 'original_equality_residuals', 'raw_equality_residuals', 'domain', 'equalities', 'raw_equalities', 'bounds', 'summary']:
        check('complete_fresh_saved_verifier_'+field, fresh[field] == saved_ver[field])
    p8 = F(16792471, 1181138102168120460)
    E = dec(source['original_matrix'])
    B = dec(source['rhs_coefficients'])
    P, N = dec(source['particular']), dec(source['kernel'])
    check('selected_rhs_affine', all(r[4:] == [0]*6 for r in B))
    check('particular_affine', all(r[4:] == [0]*6 for r in P))
    G = [[-v for v in b[:4]]+e for b, e in zip(B, E)]
    L = [r+[F(0)]*18 for r in eye(4)]+[r[:4]+n for r,n in zip(P,N)]
    R = [eye(49)[i] for i in list(range(4))+[4+j for j in eq['nonpivot_columns']]]
    K = [[F(0)]*28 for _ in range(49)]
    for i, j in enumerate(eq['pivot_columns']):
        K[4+j] = [-F(*v) for v in eq['row_transform'][i]]
    check('all_lift_data_match', original.enc([G,L,R,K]) == [data['equalities'],data['lift'],data['reverse'],data['reverse_identity_multipliers']])
    check('forward_equality_lift', mul(G,L) == [[0]*22 for _ in range(28)])
    check('reduced_coordinate_inverse', mul(R,L) == eye(22))
    reverse = [[x-y for x,y in zip(r,t)] for r,t in zip(mul(L,R),eye(49))]
    check('reverse_equality_lift', reverse == mul(K,G))
    scales = [F(1)]*4+[F(*v) for v in source['raw_scales']]
    check('positive_raw_scales', len(scales)==49 and min(scales)>0)
    rawL = [[s*x for x in r] for s,r in zip(scales,L)]
    rawR = [[x/s for x,s in zip(r,scales)] for r in R]
    rawG = dec(fresh['raw_equalities'])
    norms = [p8*F(*b['D']) for b in fresh['bounds']]
    rawK = [[-s*x/d for x,d in zip(r,norms)] for s,r in zip(scales,K)]
    check('raw_forward_equality_lift', mul(rawG,rawL)==[[0]*22 for _ in range(28)])
    check('raw_reduced_coordinate_inverse',mul(rawR,rawL)==eye(22))
    check('raw_reverse_equality_lift',mul(rawK,rawG)==[[x-y for x,y in zip(r,t)] for r,t in zip(mul(rawL,rawR),eye(49))])
    report.update(lift=L, reverse=R, equality_multipliers=K,
                  raw_lift=rawL,raw_reverse=rawR,raw_equality_multipliers=rawK)

    # The original verifier rebuilt every oriented row. Check the complete
    # initial tableau and identity artificial basis against that model.
    A=dec(data['standard_matrix']); rhs=[F(*v) for v in data['standard_rhs']]
    T=[r+e for r,e in zip(A,eye(130))]
    basis=list(range(172,302))
    check('exact_standard_dimensions',len(A)==130 and all(len(r)==172 for r in A))
    check('initial_tableau',T==dec(initial['tableau']) and rhs==[F(*v) for v in initial['rhs']])
    check('initial_basis_transform_trace',basis==initial['basis'] and dec(initial['row_transform'])==eye(130) and initial['pivots']==[])
    check('initial_nonnegative_rhs',min(rhs)>=0)
    trace=data['phase_one']['trace']
    check('complete_trace_binding',trace==final['pivots'] and len(trace)==230==data['phase_one']['pivots'])
    report['replay']=[]
    save('original_raw_rows_and_lifts_checked_before_trace')
    for step, event in enumerate(trace):
        enter,leave,row=event['entering'],event['leaving'],event['row']
        cb=[F(j>=172) for j in basis]
        objective=dot(cb,rhs)
        check('positive_pre_pivot_objective_'+str(step),objective>0 and objective==F(*event['objective_before']))
        nonbasic=sorted(set(range(302))-set(basis))
        # Audit the declared choice; the next pivot comes only from the saved
        # trace, never from this test. No new continuation is generated.
        reduced={j:F(j>=172)-dot(cb,[r[j] for r in T]) for j in nonbasic if j<=enter}
        check('least_negative_entering_'+str(step),enter in reduced and reduced[enter]<0 and all(v>=0 for j,v in reduced.items() if j<enter))
        candidates=[(rhs[i]/r[enter],basis[i],i) for i,r in enumerate(T) if r[enter]>0]
        ratio=F(*event['ratio']); pivot=T[row][enter]
        check('minimum_ratio_and_tie_'+str(step),bool(candidates) and min(candidates)==(ratio,leave,row))
        check('positive_saved_pivot_'+str(step),pivot>0 and pivot==F(*event['pivot']) and basis[row]==leave)
        prow=[v/pivot for v in T[row]]; prhs=rhs[row]/pivot
        for i in range(130):
            if i==row:
                continue
            f=T[i][enter]
            if f:
                T[i]=[x-f*y if y else x for x,y in zip(T[i],prow)]
                rhs[i]-=f*prhs
        T[row]=prow;rhs[row]=prhs;basis[row]=enter
        check('nonnegative_basic_values_'+str(step),min(rhs)>=0)
        check('basis_identity_'+str(step),len(set(basis))==130 and all(T[i][j]==F(i==k) for k,j in enumerate(basis) for i in range(130)))
        after=dot([F(j>=172) for j in basis],rhs)
        check('objective_identity_'+str(step),after==objective+ratio*reduced[enter] and after>=0)
        report['replay'].append({'step':step,'objective_before':objective,'objective_after':after,'entering_reduced_cost':reduced[enter],'ratio':ratio,'pivot':pivot})
        if (step+1)%25==0:
            save('trace_replayed_through_'+str(step+1))
            print('Saved trace audited:',step+1,'of 230; failures:',len(failures),flush=True)
    check('complete_final_tableau',T==dec(final['tableau']))
    check('complete_final_rhs_basis',rhs==[F(*v) for v in final['rhs']] and basis==final['basis'])
    check('final_artificial_transform',[r[172:] for r in T]==dec(final['row_transform']))
    values=[F(0)]*302
    for j,v in zip(basis,rhs): values[j]=v
    check('final_standard_point',values==[F(*v) for v in data['witness']['standard_values']] and min(values)>=0 and values[172:]==[0]*130)
    check('direct_original_standard_residual',[dot(r,values[:172]) for r in A]==[F(*v) for v in data['standard_rhs']])
    reduced=[F(1)]+[values[i]-values[21+i] for i in range(21)]
    w=[dot(r,reduced) for r in L]
    check('standard_reduced_original_point_link',original.enc(reduced)==data['witness']['reduced'] and original.enc(w)==data['witness']['original']==fresh['original_point'])
    check('raw_point_link',original.enc([v*s for v,s in zip(w,scales)])==fresh['raw_point'])
    check('construction_limits_record',data['limits']=={'pivots':10000,'seconds':300,'runs':1} and 0<=final['elapsed_seconds']<=data['phase_one']['elapsed_seconds']<=300)
    # Exact trace replay establishes these tableaux arise by invertible
    # elementary row operations; their artificial columns therefore give
    # the entire row transform, without a large redundant matrix product.
    manuscript=(NB/'lemmas/L086-zero-plane-sign-equality-subsystem-is-feasible.md').read_text()
    check('manuscript_scope',all(s in manuscript for s in ['No inequality from the other 53 modes','All three coordinates of u remain free','scalar upper','positive singleton rho']))
    summary=fresh['summary']
    check('manuscript_zero_indices',summary['zero_domain_indices']==[26,27,56] and summary['zero_moment_indices']==[2,4,5,10,15,16,21,22,23,28,29,30,31,36,37,38,39,40])
    report.update(standard_values=values,reduced_point=reduced,original_point=w,raw_point=[v*s for v,s in zip(w,scales)],domain_values=fresh['domain_values'],original_residuals=fresh['original_equality_residuals'],raw_residuals=fresh['raw_equality_residuals'])
    report['summary']={'verdict':'RETAINED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),'ancestor_reconstruction_checks':len(source['checks']),'original_verification_checks':len(fresh['checks']),'pivots_replayed':len(trace),'required_pivots':230,'domain_positive':summary['domain_positive'],'moment_positive':summary['moments_positive'],'actual_domain_minimum':summary['actual_domain_minimum'],'actual_raw_moment_minimum':summary['actual_raw_moment_minimum'],'required_minimum':0,'nonzero_original_raw_residuals':summary['equality_residuals_nonzero'],'other_53_modes':'NOT_TESTED','ancestor_contracts':'IMPORTED_WITH_EXISTING_QUALIFICATIONS','rs_boundary':[955,957]}
    save('completed')
    print(original.enc(report['summary']),flush=True)
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB),flush=True)
    if failures: raise SystemExit(1)


if __name__=='__main__':
    main()

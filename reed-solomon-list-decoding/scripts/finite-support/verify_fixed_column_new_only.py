"""Independent original/raw reconstruction and certificate check; no solver.

Does not invoke the constructor or replay/search a new pivot sequence.
The algebraic certificate, rather than a saved status, supplies the verdict.
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
OUT = ROOT/'fixed-column-new-only-verification.json'


def dot(a,b):
    assert len(a) == len(b)
    return sum((x*y for x,y in zip(a,b) if x and y),F(0))


def dec(M):
    return [[F(*v) for v in row] for row in M]


def mul(A,B):
    return [[dot(r,c) for c in zip(*B)] for r in A]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def main():
    names = ['fixed-column-new-only-results.json',
             'fixed-column-new-only-original-reconstruction.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'zero-plane-positive-mode-compatibility-results.json',
             'affine-sign-phase-one-results.json',
             'eight-distance-full-base-kernel-results.json']
    paths = [ROOT/n for n in names]
    data,recon,src,eq,old,col = [json.loads(p.read_text()) for p in paths]
    checks,failures = [],[]
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths+[Path(__file__)]}}

    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for name,obj in zip(names,[data,recon,src,eq,old,col]):
        check('clean_'+name,not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest() == h)
    p8 = F(16792471,1181138102168120460)
    point = [F(*v) for v in old['witness']['original'][:4]]+[F(*src['stationary_t78'])]
    check('same_frozen_columns',enc(point) == data['point'] == recon['point'] and point[4] == F(*eq['stationary_t78']))
    factors = [dot([F(*v) for v in row],point) for row in src['family']]
    check('all_85_original_domain_rows',len(factors) == 85 and min(factors) >= 0 and enc(factors) == recon['domain_factors'])
    family = [[F(*v)]+[F(*x) for x in r] for v,r in zip(col['affine']['intercept'],col['affine']['slopes'])]
    check('original_affine_family',enc(family) == src['family'])
    original_kernel = dec(col['equations'])
    check('all_90_original_kernel_equations',len(original_kernel) == 90 and all(
          [dot(row,c) for c in zip(*family)] == [F(*b)]+[F(0)]*4 for row,b in zip(original_kernel,col['rhs'])))
    check('all_90_weighted_kernel_equations',len(recon['kernel_residuals']) == 90
          and all(r == [0]*5 for r in dec(recon['kernel_residuals'])))
    check('complete_500_types_3000_presentations',len(recon['records']) == 500
          and sum(len(r['presentations']) for r in recon['records']) == 3000)
    free = [(r,q) for r in range(9) for q in range(9) if r+q >= 8]
    volumes = [F(C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
    scales = [p8/v for v in volumes]
    check('positive_original_scaling',min(scales) > 0 and enc(scales) == data['scales'] and enc(volumes) == data['volumes'])
    selected = [9*a+b for a in range(7) for b in range(4)]
    newonly = [i for i in range(81) if max(divmod(i,9)) == 8]
    check('complete_selected_row_sets',selected == data['selected_modes'] == eq['selected_modes'] and newonly == data['new_only_modes'])
    A,b,norms,rawcoeff,rawfixed = [],[],[],[],[]
    bounds = []
    # Reconstruct every bound before selecting rows; do not test omitted modes.
    for idx,m in enumerate(src['modes']):
        a,bmode = divmod(idx,9)
        B = dec(m['source_base'])
        cross = [dot([F(*v) for v in r],point) for r in m['source_cross']]
        inverse = [dot([F(*v) for v in r],point) for r in m['inverse_affine']]
        residual = [dot(r,inverse)-v for r,v in zip(B,cross)]
        check('original_full_range_'+str(idx),residual == [0]*len(B))
        D = F(C(68-2*a,8-a)*C(956-2*bmode,8-bmode))
        norm = p8*D
        forced = dot([F(*v) for v in m['forced']],point)
        anchor = p8*C(68,8)*C(956,8) if idx == 0 else F(0)
        cost = dot(cross,inverse)
        bound = forced-anchor-cost/norm
        coeff = [F(beta(68,8,8,a,8-r)*beta(956,8,8,bmode,8-q)) for r,q in free]
        row = [-v/(D*V) for v,V in zip(coeff,volumes)]
        check('original_bound_and_row_'+str(idx),norm > 0 and enc(row) == m['row'] == recon['rows'][idx]['original_row']
              and enc(bound) == recon['rows'][idx]['bound'] and enc(anchor) == m['anchor'])
        if idx in newonly:
            check('empty_block_no_anchor_'+str(idx),B == [] and cross == inverse == [] and anchor == cost == 0)
        A.append(row); b.append(bound); norms.append(norm)
        rawcoeff.append(coeff); rawfixed.append(norm*(forced-anchor)-cost)
        bounds.append({'index':idx,'bound':bound,'forced':forced,'anchor':anchor,'cost':cost,
                       'D':D,'raw_norm':norm,'range_residuals':residual})
    E = [A[i] for i in selected]
    eb = [b[i] for i in selected]
    Q = [[-v]+r for v,r in zip(eb,E)]
    rawQ = [[rawfixed[i]]+rawcoeff[i] for i in selected]
    H = [[b[i]]+[-v for v in A[i]] for i in newonly]+[[F(0)]+r for r in eye(45)]
    rawH = [[rawfixed[i]]+rawcoeff[i] for i in newonly]+[[F(0)]+r for r in eye(45)]
    check('complete_original_raw_model',enc([Q,H,rawQ,rawH]) == [data['original_equalities'],data['original_inequalities'],data['raw_equalities'],data['raw_inequalities']])
    Pcoef,N,U = map(dec,[eq['particular_coefficients'],eq['right_kernel'],eq['row_transform']])
    u = point[1:4]
    mon = [F(1)]+u+[u[i]*u[j] for i in range(3) for j in range(i,3)]
    P = [dot(r,mon) for r in Pcoef]
    selector = [eye(45)[j] for j in eq['nonpivot_columns']]
    G = [[F(0)]*28 for _ in range(45)]
    for k,j in enumerate(eq['pivot_columns']):
        G[j] = U[k][:]
    check('particular_and_homogeneous_complete',enc([P,N,selector,G]) == [data['particular'],data['homogeneous'],data['selector'],data['reverse_multipliers']]
          and [dot(r,P) for r in E] == eb and mul(E,N) == [[0]*18 for _ in range(28)]
          and mul(selector,N) == eye(18) and [dot(r,P) for r in selector] == [0]*18
          and [dot(r,eb) for r in G] == P
          and [[x+y for x,y in zip(r,t)] for r,t in zip(mul(G,E),mul(N,selector))] == eye(45))
    L = [[F(1)]+[F(0)]*18]+[[v]+r for v,r in zip(P,N)]
    rawL = [L[0]]+[[s*v for v in row] for s,row in zip(scales,L[1:])]
    R = [[F(1)]+[F(0)]*45]+[[F(0)]+r for r in selector]
    rawR = [R[0]]+[[r[0]]+[v/s for v,s in zip(r[1:],scales)] for r in R[1:]]
    K = [[F(0)]*28]+[[-v for v in r] for r in G]
    rawK = [[F(0)]*28]+[[s*v/norms[i] for i,v in zip(selected,r)] for s,r in zip(scales,G)]
    check('scaled_augmented_both_directions',mul(Q,L) == [[0]*19 for _ in range(28)] and mul(R,L) == eye(19)
          and mul(K,Q) == [[x-y for x,y in zip(r,t)] for r,t in zip(mul(L,R),eye(46))])
    check('raw_augmented_both_directions',mul(rawQ,rawL) == [[0]*19 for _ in range(28)] and mul(rawR,rawL) == eye(19)
          and mul(rawK,rawQ) == [[x-y for x,y in zip(r,t)] for r,t in zip(mul(rawL,rawR),eye(46))])
    pulled = mul(H,L)
    check('all_62_pulled_rows_no_deletion',len(pulled) == 62 and enc(pulled) == data['pulled_inequalities'])
    verdict = data['summary']['verdict']
    if verdict == 'RATIONAL_FEASIBLE_WITNESS':
        z = [F(*v) for v in data['witness']['z']]
        raw = [s*v for s,v in zip(scales,z)]
        h = [F(*v) for v in data['witness']['h']]
        eqres = [dot(r,[F(1)]+z) for r in Q]
        raweq = [dot(r,[F(1)]+raw) for r in rawQ]
        slacks = [dot(r,[F(1)]+z) for r in H]
        rawslacks = [dot(r,[F(1)]+raw) for r in rawH]
        check('full_rational_witness_lift',len(z) == 45 and len(h) == 18 and z == [v+dot(r,h) for v,r in zip(P,N)])
        check('28_original_and_raw_equalities',not any(eqres+raweq))
        check('17_original_and_raw_modes_and_45_signs',min(slacks) >= 0 and min(rawslacks) >= 0
              and rawslacks[:17] == [norms[i]*v for i,v in zip(newonly,slacks[:17])])
        check('saved_entire_certificate_residuals',enc([raw,eqres,raweq,slacks,rawslacks]) == [data['witness']['raw_moments'],
              data['witness']['original_equality_residuals'],data['witness']['raw_equality_residuals'],
              data['witness']['original_slacks'],data['witness']['raw_slacks']])
        report['witness'] = {'z':z,'raw_moments':raw,'original_equalities':eqres,'raw_equalities':raweq,
                             'original_slacks':slacks,'raw_slacks':rawslacks}
        details = {'positive_new_only_slacks':sum(v > 0 for v in slacks[:17]),
                   'zero_new_only_slacks':sum(v == 0 for v in slacks[:17]),
                   'positive_moments':sum(v > 0 for v in z),'zero_moments':sum(v == 0 for v in z),
                   'actual_minimum_original_slack':min(slacks),'actual_minimum_raw_slack':min(rawslacks),
                   'nonzero_original_raw_equalities':sum(v != 0 for v in eqres+raweq)}
    elif verdict == 'RATIONAL_ORIGINAL_FARKAS_CERTIFICATE':
        lam = [F(*v) for v in data['separator']['inequality_weights']]
        mu = [F(*v) for v in data['separator']['equality_multipliers']]
        aggregate = [dot(lam,c)+dot(mu,d) for c,d in zip(zip(*H),zip(*Q))]
        rawlam = [v/norms[i] for i,v in zip(newonly,lam[:17])]+[v/s for v,s in zip(lam[17:],scales)]
        rawmu = [-v/norms[i] for i,v in zip(selected,mu)]
        rawaggregate = [dot(rawlam,c)+dot(rawmu,d) for c,d in zip(zip(*rawH),zip(*rawQ))]
        check('all_original_inequality_weights_nonnegative',len(lam) == 62 and min(lam) >= 0 and len(mu) == 28)
        check('original_strict_lifted_separator',aggregate[0] < 0 and not any(aggregate[1:])
              and enc(aggregate) == data['separator']['original_certificate'])
        check('raw_strict_lifted_separator',min(rawlam) >= 0 and not any(rawaggregate[1:]) and rawaggregate[0] == aggregate[0]
              and enc(rawaggregate) == data['separator']['raw_certificate'])
        check('objective_pairing',aggregate[0] == -F(*data['phase_one']['objective']))
        report['separator'] = {'inequality_weights':lam,'free_equality_multipliers':mu,'original_certificate':aggregate,
                               'raw_inequality_weights':rawlam,'raw_free_equality_multipliers':rawmu,'raw_certificate':rawaggregate}
        details = {'pairing':aggregate[0],'nonzero_original_raw_variable_coefficients':sum(v != 0 for v in aggregate[1:]+rawaggregate[1:]),
                   'positive_inequality_weights':sum(v > 0 for v in lam),'required_pairing':'strictly negative'}
    else:
        check('honest_inconclusive_verdict',verdict == 'UNDECIDED' and 'witness' not in data and 'separator' not in data)
        state = json.loads((ROOT/'fixed-column-new-only-state.json').read_text())
        rhs = [F(*v) for v in state['rhs']]
        obj = sum((v for j,v in zip(state['basis'],rhs) if j >= data['artificial_start']),F(0))
        check('complete_saved_cap_state',len(rhs) == len(state['basis']) == 62 and len(set(state['basis'])) == 62
              and min(rhs) >= 0 and enc(obj) == data['phase_one']['objective'] and state['pivots'] == data['phase_one']['trace'])
        details = {'stop':data['phase_one']['stop'],'pivots':data['phase_one']['pivots'],
                   'elapsed_seconds':data['phase_one']['elapsed_seconds'],'objective':obj}
    report.update(bounds=bounds,domain_factors=factors,checks=checks,failures=failures)
    report['summary'] = {'verdict':'VERIFIED_'+verdict if not failures else 'FAILED','checks':len(checks),
                         'failures':len(failures),'equalities':28,'new_only_modes':17,'signs':45,
                         'required_slack_lower_bound':0,'omitted_mixed_modes':'NOT_TESTED','rs_boundary':[955,957],**details}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print('Summary:',enc(report['summary']),flush=True)
    print('Failures:',failures,'; full original/raw evidence:',OUT.relative_to(NB),flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

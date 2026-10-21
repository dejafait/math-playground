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
OUT = ROOT/'two-mixed-row-verification.json'


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
    names = ['two-mixed-row-results.json',
             'two-mixed-row-original-reconstruction.json',
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
    retained = []
    membership = []
    for i,m in enumerate(src['modes']):
        B = dec(m['source_base'])
        cross = [dot([F(*v) for v in r],point) for r in m['source_cross']]
        zero = all(v==0 for row in B for v in row)
        membership.append({'index':i,'empty':not B,'zero_old_block':zero,'base':B,'cross':cross})
        if zero:
            retained.append(i)
            check('selected_entire_zero_cross_'+str(i),not any(cross))
        saved = data['membership'][i]
        check('complete_membership_'+str(i),saved['index']==i and saved['empty']==(not B)
              and saved['zero_old_block']==zero and saved['base']==m['source_base']
              and saved['cross']==enc(cross))
    zero_modes = retained[:]
    added_indices=[23,31]
    check('exact_two_added_modes',len(zero_modes)==43
          and all(i not in zero_modes+selected and len(membership[i]['base'])==3 for i in added_indices))
    retained=sorted(zero_modes+added_indices)
    report['added_modes']=[]
    nz=len(retained); nr=nz+45
    check('complete_selected_row_sets',selected == data['selected_modes'] == eq['selected_modes']
          and newonly == data['new_only_modes'] and zero_modes==data['zero_old_block_modes']
          and retained==data['retained_modes']
          and set(newonly).issubset(retained) and 66 in retained)
    report.update(membership=membership,zero_old_block_modes=zero_modes,retained_modes=retained)
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
        if idx in zero_modes:
            check('zero_block_entire_cross_no_anchor_'+str(idx),all(v==0 for row in B for v in row) and not any(cross) and anchor == cost == 0)
        if idx in added_indices:
            from verify_simultaneous_eight_shell import det, cramer
            from itertools import combinations
            chosen=()
            minors=[]
            for k in range(1,len(B)+1):
                for inds in combinations(range(len(B)),k):
                    value=det([[B[i][j] for j in inds] for i in inds])
                    minors.append({'indices':inds,'determinant':value})
                    if value:
                        chosen=inds
            fresh=[F(0)]*len(B)
            if chosen:
                for j,v in zip(chosen,cramer([[B[i][j] for j in chosen] for i in chosen],[cross[i] for i in chosen])):
                    fresh[j]=v
            check('added_entire_PSD_range_cost_'+str(idx),len(B)==3 and all(m['determinant']>=0 for m in minors)
                  and [dot(r,fresh)-v for r,v in zip(B,cross)]==[0]*3
                  and dot(cross,fresh)==cost)
            added={'index':idx,'mode':list(divmod(idx,9)),'base':B,'cross':cross,'fresh_inverse':fresh,
                   'minors':minors,'energy':cost,'bound':bound,'normalization':norm}
            check('entire_added_constructor_block_'+str(idx),enc(added)==data['added_modes'][added_indices.index(idx)])
            report['added_modes'].append(added)
        A.append(row); b.append(bound); norms.append(norm)
        rawcoeff.append(coeff); rawfixed.append(norm*(forced-anchor)-cost)
        bounds.append({'index':idx,'bound':bound,'forced':forced,'anchor':anchor,'cost':cost,
                       'D':D,'raw_norm':norm,'range_residuals':residual})
    E = [A[i] for i in selected]
    eb = [b[i] for i in selected]
    Q = [[-v]+r for v,r in zip(eb,E)]
    rawQ = [[rawfixed[i]]+rawcoeff[i] for i in selected]
    H = [[b[i]]+[-v for v in A[i]] for i in retained]+[[F(0)]+r for r in eye(45)]
    rawH = [[rawfixed[i]]+rawcoeff[i] for i in retained]+[[F(0)]+r for r in eye(45)]
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
    check('all_retained_pulled_rows_no_deletion',len(pulled) == nr and enc(pulled) == data['pulled_inequalities'])
    labels=[{'kind':'added_nonzero_old_block_mode' if i in added_indices else 'zero_old_block_mode',
             'index':i,'mode':list(divmod(i,9))} for i in retained]
    labels += [{'kind':'moment_sign','index':i,'rq':list(free[i])} for i in range(45)]
    signs=[F(1) if row[0]>=0 else F(-1) for row in pulled]
    standard=[[sg*v for v in [-x for x in row[1:]]+row[1:]+eye(nr)[i]]
              for i,(row,sg) in enumerate(zip(pulled,signs))]
    srhs=[sg*row[0] for sg,row in zip(signs,pulled)]
    check('all_90_labels_orientations_and_standard_rows',labels==data['row_labels']
          and enc(signs)==data['row_signs'] and enc(standard)==data['standard_matrix']
          and enc(srhs)==data['standard_rhs'] and len(pulled)==90)
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
        check('zero_block_original_and_raw_modes_and_45_signs',min(slacks) >= 0 and min(rawslacks) >= 0
              and rawslacks[:nz] == [norms[i]*v for i,v in zip(retained,slacks[:nz])])
        check('saved_entire_certificate_residuals',enc([raw,eqres,raweq,slacks,rawslacks]) == [data['witness']['raw_moments'],
              data['witness']['original_equality_residuals'],data['witness']['raw_equality_residuals'],
              data['witness']['original_slacks'],data['witness']['raw_slacks']])
        sv=[F(*v) for v in data['witness']['standard_values']]
        art=data['artificial_start']
        check('full_nonnegative_standard_witness',len(sv)==216 and art==126 and min(sv)>=0
              and not any(sv[art:]) and [dot(r,sv[:art]) for r in standard]==srhs
              and h==[sv[j]-sv[18+j] for j in range(18)])
        report['witness'] = {'z':z,'raw_moments':raw,'original_equalities':eqres,'raw_equalities':raweq,
                             'original_slacks':slacks,'raw_slacks':rawslacks}
        check('manuscript_two_added_remainder_bounds',slacks[retained.index(23)]==0
              and 153320960 <= slacks[retained.index(31)] < 153320961)
        details = {'positive_mode_slacks':sum(v > 0 for v in slacks[:nz]),
                   'zero_mode_slacks':sum(v == 0 for v in slacks[:nz]),
                   'added_scaled_slacks':[slacks[retained.index(i)] for i in added_indices],
                   'added_raw_remainders':[rawslacks[retained.index(i)] for i in added_indices],
                   'positive_moments':sum(v > 0 for v in z),'zero_moments':sum(v == 0 for v in z),
                   'actual_minimum_original_slack':min(slacks),'actual_minimum_raw_slack':min(rawslacks),
                   'nonzero_original_raw_equalities':sum(v != 0 for v in eqres+raweq),
                   'added_31_original_interval':[153320960,153320961]}
    elif verdict == 'RATIONAL_ORIGINAL_FARKAS_CERTIFICATE':
        lam = [F(*v) for v in data['separator']['inequality_weights']]
        mu = [F(*v) for v in data['separator']['equality_multipliers']]
        aggregate = [dot(lam,c)+dot(mu,d) for c,d in zip(zip(*H),zip(*Q))]
        rawlam = [v/norms[i] for i,v in zip(retained,lam[:nz])]+[v/s for v,s in zip(lam[nz:],scales)]
        rawmu = [-v/norms[i] for i,v in zip(selected,mu)]
        rawaggregate = [dot(rawlam,c)+dot(rawmu,d) for c,d in zip(zip(*rawH),zip(*rawQ))]
        check('all_original_inequality_weights_nonnegative',len(lam) == nr and min(lam) >= 0 and len(mu) == 28)
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
        state = json.loads((ROOT/'two-mixed-row-state.json').read_text())
        rhs = [F(*v) for v in state['rhs']]
        obj = sum((v for j,v in zip(state['basis'],rhs) if j >= data['artificial_start']),F(0))
        check('complete_saved_cap_state',len(rhs) == len(state['basis']) == nr and len(set(state['basis'])) == nr
              and min(rhs) >= 0 and enc(obj) == data['phase_one']['objective'] and state['pivots'] == data['phase_one']['trace'])
        details = {'stop':data['phase_one']['stop'],'pivots':data['phase_one']['pivots'],
                   'elapsed_seconds':data['phase_one']['elapsed_seconds'],'objective':obj}
    report.update(bounds=bounds,domain_factors=factors,checks=checks,failures=failures)
    report['summary'] = {'verdict':'VERIFIED_'+verdict if not failures else 'FAILED','checks':len(checks),
                         'failures':len(failures),'equalities':28,'zero_old_block_modes':len(zero_modes),'added_modes':added_indices,'inequalities':nr,'signs':45,
                         'required_slack_lower_bound':0,'omitted_nonzero_old_block_modes':28,'rs_boundary':[955,957],**details}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print('Verdict:',report['summary']['verdict'],'; checks:',len(checks),'; failures:',len(failures),flush=True)
    print('Retained modes:',nz,'; equalities:',28,'; signs:',45,'; required slack >= 0',flush=True)
    if 'witness' in report:
        print('Positive/zero mode slacks:',details['positive_mode_slacks'],details['zero_mode_slacks'],
              '; positive/zero moments:',details['positive_moments'],details['zero_moments'],
              '; added mode slack signs:',[(v>0)-(v<0) for v in details['added_scaled_slacks']],flush=True)
    print('Failures:',failures,'; full original/raw evidence:',OUT.relative_to(NB),flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

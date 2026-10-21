"""One equality-reduced exact Phase I; original/raw certificates are decisive.

All column parameters are immutable. This is a fresh zero-old-block subsystem,
not a resumed full-system solve. No earlier certificate is overwritten.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction as F
from pathlib import Path

import affine_sign_remaining_modes as original
from verify_simultaneous_eight_shell import C, beta, enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'fixed-column-zero-old-block-results.json'
RECON = ROOT/'fixed-column-zero-old-block-original-reconstruction.json'
INITIAL = ROOT/'fixed-column-zero-old-block-initial-state.json'
STATE = ROOT/'fixed-column-zero-old-block-state.json'
PIVOT_CAP, SECONDS = 10000, 300


def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b) if x and y), F(0))


def dec(M):
    return [[F(*v) for v in row] for row in M]


def mul(A, B):
    return [[dot(row, col) for col in zip(*B)] for row in A]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def write(path, obj):
    path.write_text(json.dumps(enc(obj), indent=2)+'\n')


def main():
    original.OUT = RECON
    original.main()  # All full keys, kernel equations, ranges and original bounds.
    names = ['fixed-sign-column-full-completion-results.json',
             'fixed-sign-column-full-completion-initial-state.json',
             'fixed-sign-column-full-completion-state.json',
             'fixed-sign-column-full-completion-verification.json',
             'zero-plane-positive-mode-compatibility-results.json',
             'affine-sign-phase-one-results.json',
             'affine-sign-phase-one-critical-audit.json',
             'affine-sign-remaining-modes-critical-audit.json']
    paths = [ROOT/n for n in names]
    full, initial, stopped, fullver, eq, old, oldaudit, modeaudit = [json.loads(p.read_text()) for p in paths]
    recon = json.loads(RECON.read_text())
    checks, failures = [], []
    report = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in paths+[RECON, Path(__file__)]},
              'limits': {'runs': 1, 'pivots': PIVOT_CAP, 'seconds': SECONDS}}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        report.update(stage=stage, checks=checks, failures=failures)
        write(OUT, report)

    for name, obj in zip(names, [full, initial, stopped, fullver, eq, old, oldaudit, modeaudit]):
        check('clean_'+name, not obj.get('failures', []))
        for rel, h in obj.get('input_hashes', {}).items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == h)
    check('fresh_original_reconstruction', not recon['failures'] and len(recon['rows']) == 81)
    check('full_stopped_state_consumed', stopped['pivots'] == full['phase_one']['trace']
          and len(stopped['tableau']) == len(initial['tableau']) == 126)
    p8 = F(16792471, 1181138102168120460)
    point = [F(*v) for v in recon['point']]
    check('frozen_columns', enc(point) == full['point'] and point[:4] == [F(*v) for v in old['witness']['original'][:4]]
          and point[4] == F(*eq['stationary_t78']))
    free = [(r,q) for r in range(9) for q in range(9) if r+q >= 8]
    volumes = [F(C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
    scales = [p8/v for v in volumes]
    check('positive_coordinate_scales', len(scales) == 45 and min(scales) > 0)
    allA = dec([r['original_row'] for r in recon['rows']])
    allb = [F(*r['bound']) for r in recon['rows']]
    norms = [F(*r['positive_raw_normalization']) for r in recon['rows']]
    check('complete_step316_original_system', enc(allA) == full['original_matrix'][:81]
          and enc(allb) == full['original_rhs'][:81])
    rawA = [[v/s for v,s in zip(row,scales)] for row in allA]
    check('complete_step316_raw_system', enc(rawA) == full['raw_matrix'][:81] and min(norms) > 0)
    for idx, row in enumerate(recon['rows']):
        a,b = divmod(idx,9)
        coeff = [F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        check('direct_raw_beta_'+str(idx), enc(coeff) == row['raw_beta']
              and [-v*norms[idx] for v in rawA[idx]] == coeff)
    selected = eq['selected_modes']
    newonly = [i for i in range(81) if max(divmod(i,9)) == 8]
    # Membership is entrywise on the original anchor-transported block.
    membership = []
    for i,row in enumerate(recon['rows']):
        B,cv = dec(row['base']),[F(*v) for v in row['cross']]
        zero = all(v == 0 for r in B for v in r)
        membership.append({'index':i,'mode':list(divmod(i,9)),'layers':row['layers'],
                           'base':B,'cross':cv,'empty':not B,'zero_old_block':zero,
                           'affine_range_residuals':row['affine_inverse_residuals'],
                           'point_range_residuals':row['point_range_residuals']})
        check('membership_dimensions_'+str(i),len(B)==len(cv)==len(row['layers'])
              and all(len(r)==len(B) for r in B))
        if zero:
            check('zero_block_whole_cross_'+str(i),not any(cv)
                  and F(*row['energy'])==0
                  and all(not any(r) for r in dec(row['affine_inverse_residuals']))
                  and not any(F(*v) for v in row['point_range_residuals']))
    zero_modes = [r['index'] for r in membership if r['zero_old_block']]
    check('empty_modes_included',all(i in zero_modes for i in newonly))
    check('index66_regression',66 in zero_modes and membership[66]['base']==[[0]]
          and membership[66]['cross']==[0])
    evidence_names = ['fixed-column-new-only-results.json','fixed-column-new-only-original-reconstruction.json',
        'fixed-column-new-only-verification.json','fixed-column-new-only-critical-source.json',
        'fixed-column-new-only-critical-verification.json','fixed-column-new-only-critical-audit.json',
        'new-only-witness-mixed-modes-results.json','new-only-witness-mixed-modes-verification.json',
        'new-only-witness-mixed-modes-critical-source.json',
        'new-only-witness-mixed-modes-critical-verification.json','new-only-witness-mixed-modes-critical-audit.json']
    evidence = [json.loads((ROOT/n).read_text()) for n in evidence_names]
    for name,obj in zip(evidence_names,evidence):
        report['input_hashes'][str((ROOT/name).relative_to(NB))] = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        check('clean_prior_'+name,not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('prior_binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
        if 'records' in obj:
            check('complete_prior_records_'+name,obj['records']==recon['records'])
        if 'kernel_residuals' in obj:
            check('complete_prior_kernel_'+name,obj['kernel_residuals']==recon['kernel_residuals'])
        if 'rows' in obj:
            for i,row in enumerate(obj['rows']):
                normfield = 'positive_raw_normalization' if 'positive_raw_normalization' in row else 'norm'
                check('complete_prior_original_row_'+name+'_'+str(i),
                      ('base' not in row or row['base']==recon['rows'][i]['base'])
                      and ('cross' not in row or row['cross']==recon['rows'][i]['cross'])
                      and ('original_row' not in row or row['original_row']==recon['rows'][i]['original_row'])
                      and ('bound' not in row or row['bound']==recon['rows'][i]['bound'])
                      and ('raw_beta' not in row or row['raw_beta']==recon['rows'][i]['raw_beta'])
                      and row[normfield]==recon['rows'][i]['positive_raw_normalization'])
    for j in [7,9,10]:
        obj=evidence[j]
        for i,row in enumerate(obj['rows']):
            check('complete_322_324_witness_row_'+str(j)+'_'+str(i),
                  all(row[k]==evidence[6]['rows'][i][k] for k in ['scaled_slack','raw_remainder']))
    report.update(membership=membership,zero_old_block_modes=zero_modes,
                  zero_old_block_mixed_modes=[i for i in zero_modes if i not in newonly])
    retained = zero_modes
    E = [allA[i] for i in selected]
    b = [allb[i] for i in selected]
    check('selected_and_newonly_sets', selected == [9*a+b for a in range(7) for b in range(4)]
          and len(newonly) == 17 and not set(selected).intersection(newonly))
    Pcoef, N, U = map(dec, [eq['particular_coefficients'], eq['right_kernel'], eq['row_transform']])
    u = point[1:4]
    mon = [F(1)]+u+[u[i]*u[j] for i in range(3) for j in range(i,3)]
    P = [dot(row,mon) for row in Pcoef]
    selector = [eye(45)[j] for j in eq['nonpivot_columns']]
    G = [[F(0)]*28 for _ in range(45)]
    for k,j in enumerate(eq['pivot_columns']):
        G[j] = U[k][:]
    check('saved_l086_specialized_lift', [r[4:] for r in dec(old['lift'])[4:]] == N
          and [dot(r[:4],point[:4]) for r in dec(old['lift'])[4:]] == P
          and [[-v for v in r] for r in dec(old['reverse_identity_multipliers'])[4:]] == G)
    check('forward_particular', [dot(r,P) for r in E] == b)
    check('forward_homogeneous', mul(E,N) == [[0]*18 for _ in range(28)])
    check('selector_left_inverse', mul(selector,N) == eye(18) and [dot(r,P) for r in selector] == [0]*18)
    check('reverse_complete_locus', [[x+y for x,y in zip(r,t)] for r,t in zip(mul(G,E),mul(N,selector))] == eye(45)
          and [dot(r,b) for r in G] == P)
    # Unnormalized raw equalities: rawE*Y = rawb, with rawE=-norm*E/S.
    rawE = [[-norms[i]*v/s for v,s in zip(row,scales)] for i,row in zip(selected,E)]
    rawb = [-norms[i]*v for i,v in zip(selected,b)]
    rawP = [s*v for s,v in zip(scales,P)]
    rawN = [[s*v for v in row] for s,row in zip(scales,N)]
    rawF = [[v/s for v,s in zip(row,scales)] for row in selector]
    rawG = [[-s*v/norms[i] for i,v in zip(selected,row)] for s,row in zip(scales,G)]
    check('raw_forward_lift', [dot(r,rawP) for r in rawE] == rawb
          and mul(rawE,rawN) == [[0]*18 for _ in range(28)])
    check('raw_reverse_lift', mul(rawF,rawN) == eye(18) and [dot(r,rawP) for r in rawF] == [0]*18
          and [[x+y for x,y in zip(r,t)] for r,t in zip(mul(rawG,rawE),mul(rawN,rawF))] == eye(45)
          and [dot(r,rawb) for r in rawG] == rawP)
    # Augmented >=0 rows; all signs are retained, including duplicates/zero pulls.
    H = [[allb[i]]+[-v for v in allA[i]] for i in retained]+[[F(0)]+r for r in eye(45)]
    Q = [[-v]+r for v,r in zip(b,E)]  # equality rows Q*(1,z)=0
    L = [[F(1)]+[F(0)]*18]+[[v]+r for v,r in zip(P,N)]
    pulled = mul(H,L)
    K = [[F(0)]*28]+[[-v for v in row] for row in G]
    R = [[F(1)]+[F(0)]*45]+[[F(0)]+r for r in selector]
    check('augmented_both_lift_directions', mul(Q,L) == [[0]*19 for _ in range(28)]
          and mul(R,L) == eye(19)
          and [[v-w for v,w in zip(r,t)] for r,t in zip(mul(L,R),eye(46))] == mul(K,Q))
    rawH = [[norms[i]*allb[i]]+[-norms[i]*v for v in rawA[i]] for i in retained]+[[F(0)]+r for r in eye(45)]
    rawQ = [[-v]+r for v,r in zip(rawb,rawE)]
    labels = [{'kind':'zero_old_block_mode','index':i,'mode':list(divmod(i,9))} for i in retained]
    labels += [{'kind':'moment_sign','index':i,'rq':list(free[i])} for i in range(45)]
    n,m = 18,len(retained)+45
    nz = len(retained)
    signs = [F(1) if row[0] >= 0 else F(-1) for row in pulled]
    standard = [[sg*v for v in [-x for x in row[1:]]+row[1:]+eye(m)[i]] for i,(row,sg) in enumerate(zip(pulled,signs))]
    rhs0 = [sg*row[0] for sg,row in zip(signs,pulled)]
    artificial_start = 2*n+m
    T = [row+e for row,e in zip(standard,eye(m))]
    rhs = rhs0[:]
    basis = list(range(artificial_start,artificial_start+m))
    report.update(point=point, p8=p8, free=free, volumes=volumes, scales=scales,
                  selected_modes=selected, new_only_modes=newonly, norms=norms,
                  equality_matrix=E, equality_rhs=b, particular=P, homogeneous=N,
                  selector=selector, reverse_multipliers=G, raw_equality_matrix=rawE,
                  raw_equality_rhs=rawb, raw_particular=rawP, raw_homogeneous=rawN,
                  raw_selector=rawF, raw_reverse_multipliers=rawG,
                  original_equalities=Q, original_inequalities=H,
                  raw_equalities=rawQ, raw_inequalities=rawH, row_labels=labels,
                  lift=L, reverse=R, equality_multipliers=K, pulled_inequalities=pulled,
                  row_signs=signs, standard_matrix=standard, standard_rhs=rhs0,
                  artificial_start=artificial_start,
                  column_order=['18 positive parts','18 negative parts','all retained slacks','all retained artificials'])
    check('all_28_equalities_and_retained_inequalities', len(Q) == 28 and len(H) == len(pulled) == m)
    check('new_only_empty_old_blocks_and_no_anchor', all(recon['rows'][i]['layers'] == []
          and F(*recon['rows'][i]['anchor']) == F(*recon['rows'][i]['energy']) == 0 for i in newonly))
    save('full_original_raw_system_and_lift_before_pivots')
    if failures:
        raise SystemExit('Pre-pivot failure: '+repr(failures))
    trace = []
    started = time.monotonic()
    last_print = started

    def state(stage, path=STATE):
        write(path, {'stage':stage, 'tableau':T, 'rhs':rhs, 'basis':basis,
                     'row_transform':[r[artificial_start:] for r in T],
                     'pivots':trace, 'elapsed_seconds':time.monotonic()-started})

    state('initialized_before_any_pivot', INITIAL)
    verdict, stop, pi = 'UNDECIDED', '', []
    try:
        while True:
            cb = [F(j >= artificial_start) for j in basis]
            objective = dot(cb,rhs)
            if objective == 0:
                verdict,stop = 'RATIONAL_FEASIBLE_WITNESS','zero_artificial_objective'
                break
            if time.monotonic()-started >= SECONDS or len(trace) >= PIVOT_CAP:
                stop = 'time_limit' if time.monotonic()-started >= SECONDS else 'pivot_limit'
                break
            nonbasic = set(range(len(T[0])))-set(basis)
            entering = next((j for j in sorted(nonbasic) if F(j >= artificial_start)-dot(cb,[r[j] for r in T]) < 0),None)
            if entering is None:
                pi = [dot(cb,c) for c in zip(*[r[artificial_start:] for r in T])]
                verdict,stop = 'POSITIVE_PHASE_ONE_OPTIMUM','all_reduced_costs_nonnegative'
                break
            choices = [(rhs[i]/r[entering],basis[i],i) for i,r in enumerate(T) if r[entering] > 0]
            if not choices:
                stop = 'exceptional_no_leaving_row'
                break
            ratio,leaving,row = min(choices)
            pivot = T[row][entering]
            pr,pb = [v/pivot for v in T[row]],rhs[row]/pivot
            newT,newrhs = [],[]
            for i,r in enumerate(T):
                factor = r[entering]
                if i == row:
                    newT.append(pr); newrhs.append(pb)
                elif factor:
                    newT.append([v-factor*w if w else v for v,w in zip(r,pr)])
                    newrhs.append(rhs[i]-factor*pb)
                else:
                    newT.append(r); newrhs.append(rhs[i])
                if time.monotonic()-started >= SECONDS:
                    stop = 'time_limit_during_atomic_pivot'
                    break
            if stop:
                break  # Last complete tableau remains unchanged.
            T,rhs = newT,newrhs
            basis[row] = entering
            trace.append({'entering':entering,'leaving':leaving,'row':row,'pivot':pivot,
                          'ratio':ratio,'objective_before':objective})
            if min(rhs) < 0:
                stop = 'exceptional_negative_basic_coordinate'
                break
            if len(trace)%10 == 0:
                state('running_checkpoint')
            if time.monotonic()-last_print >= 25:
                print('Zero-old-block Phase I:',len(trace),'pivots;',round(time.monotonic()-started,1),
                      'seconds; objective positive',flush=True)
                last_print = time.monotonic()
    except (KeyboardInterrupt,Exception) as exc:
        verdict,stop = 'UNDECIDED','interruption_or_exception: '+repr(exc)
    state('terminated_'+stop)
    cb = [F(j >= artificial_start) for j in basis]
    objective = dot(cb,rhs)
    report['phase_one'] = {'stop':stop,'pivots':len(trace),'objective':objective,
                           'elapsed_seconds':time.monotonic()-started,'trace':trace}
    if verdict == 'RATIONAL_FEASIBLE_WITNESS':
        values = [F(0)]*len(T[0])
        for j,v in zip(basis,rhs):
            values[j] = v
        h = [values[j]-values[n+j] for j in range(n)]
        z = [v+dot(r,h) for v,r in zip(P,N)]
        raw = [s*v for s,v in zip(scales,z)]
        eqres = [dot(r,[F(1)]+z) for r in Q]
        rawres = [dot(r,[F(1)]+raw) for r in rawQ]
        slacks = [dot(r,[F(1)]+z) for r in H]
        rawslacks = [dot(r,[F(1)]+raw) for r in rawH]
        check('standard_nonnegative_witness', min(values) >= 0 and not any(values[artificial_start:])
              and [dot(r,values[:artificial_start]) for r in standard] == rhs0)
        check('original_28_equalities_and_retained_inequalities', not any(eqres) and min(slacks) >= 0)
        check('raw_28_equalities_and_retained_inequalities', not any(rawres) and min(rawslacks) >= 0
              and rawslacks[:nz] == [norms[i]*v for i,v in zip(retained,slacks[:nz])])
        report['witness'] = {'standard_values':values,'h':h,'z':z,'raw_moments':raw,
                             'original_equality_residuals':eqres,'raw_equality_residuals':rawres,
                             'original_slacks':slacks,'raw_slacks':rawslacks}
    elif verdict == 'POSITIVE_PHASE_ONE_OPTIMUM':
        lam = [-v*sg for v,sg in zip(pi,signs)]
        aggregate = [dot(lam,c) for c in zip(*H)]
        mu = [dot(aggregate,c) for c in zip(*K)]
        cert = [a+dot(mu,c) for a,c in zip(aggregate,zip(*Q))]
        rawlam = [v/norms[i] for i,v in zip(retained,lam[:nz])]+[v/s for v,s in zip(lam[nz:],scales)]
        rawmu = [-v/norms[i] for i,v in zip(selected,mu)]
        rawcert = [dot(rawlam,c)+dot(rawmu,d) for c,d in zip(zip(*rawH),zip(*rawQ))]
        check('nonnegative_retained_original_weights', min(lam) >= 0)
        check('original_lifted_strict_separator', cert[0] == -objective < 0 and not any(cert[1:]))
        check('raw_lifted_strict_separator', min(rawlam) >= 0 and rawcert[0] == cert[0] and not any(rawcert[1:]))
        check('all_reduced_costs_nonnegative', all(F(j >= artificial_start)-dot(cb,[r[j] for r in T]) >= 0 for j in range(len(T[0]))))
        report['separator'] = {'phase_one_dual':pi,'inequality_weights':lam,'equality_multipliers':mu,
                               'original_aggregate':aggregate,'original_certificate':cert,
                               'raw_inequality_weights':rawlam,'raw_equality_multipliers':rawmu,
                               'raw_certificate':rawcert}
        verdict = 'RATIONAL_ORIGINAL_FARKAS_CERTIFICATE'
    report['summary'] = {'verdict':verdict if not failures else 'FAILED_CERTIFICATE_UNDECIDED',
                         'stop':stop,'pivots':len(trace),'checks':len(checks),'failures':len(failures),
                         'objective_sign':(objective > 0)-(objective < 0),'required_objective':0,
                         'pivot_cap':PIVOT_CAP,'seconds_cap':SECONDS,
                         'zero_old_block_modes':len(retained),'inequalities':m,'omitted_nonzero_old_block_modes':len([i for i in range(81) if i not in selected and i not in retained]),'rs_boundary':[955,957]}
    save('completed')
    print('Summary:',report['summary'],flush=True)
    print('Failures:',failures,'; certificate:',OUT.relative_to(NB),'; state:',STATE.relative_to(NB),flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

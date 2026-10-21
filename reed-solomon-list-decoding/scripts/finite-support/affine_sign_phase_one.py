"""One bounded exact rational Phase I on the approved sign/equality subsystem.

Artificial columns retain the complete row transformation. No floating solve,
warm start, point scan, variable bounds, row deletion or remaining-mode solve.
"""
import hashlib
import itertools as it
import json
import sys
import time
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'affine-sign-phase-one-results.json'
STATE = ROOT/'affine-sign-phase-one-state.json'
INITIAL = ROOT/'affine-sign-phase-one-initial-state.json'
PIVOT_CAP = 10000
SECONDS = 300


def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b) if x and y), F(0))


def dec(a):
    return [[F(*v) for v in r] for r in a]


def mm(a, b):
    return [[dot(r, c) for c in zip(*b)] for r in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def write(path, obj):
    path.write_text(json.dumps(enc(obj), indent=2)+'\n')


def main():
    names = ['reduced-zero-plane-joint-results.json',
             'zero-plane-positive-mode-compatibility-results.json',
             'zero-plane-positive-mode-compatibility-critical-audit.json',
             'zero-plane-fixed-face-results.json',
             'zero-plane-fixed-face-critical-audit.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'fully-cancelling-separator-family-verification.json',
             'eight-distance-full-base-kernel-results.json']
    paths = [ROOT/n for n in names]
    old, eq, ea, face, fa, src, ver, col = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'limits': {'pivots': PIVOT_CAP, 'seconds': SECONDS, 'runs': 1},
           'column_order': ['21 positive parts', '21 negative parts', '130 slacks', '130 artificials']}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        out.update(stage=stage, checks=checks, failures=failures)
        write(OUT, out)

    for name, obj in zip(names, [old, eq, ea, face, fa, src, ver, col]):
        check('clean_'+name, not obj['failures'])
        for rel, h in obj.get('input_hashes', {}).items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == h)
    p8 = F(16792471, 1181138102168120460)
    s = F(*eq['stationary_t78'])
    family = [[F(*v)]+[F(*x) for x in r] for v, r in zip(col['affine']['intercept'], col['affine']['slopes'])]
    domain = [[r[0]+s*r[4]]+r[1:4] for r in family]
    check('all_original_domain_rows', len(domain) == 85 and enc(domain) == old['domain'] == face['domain'] == eq['domain'])
    check('all_90_kernel_equations', len(col['equations']) == 90 and all(
        [dot([F(*v) for v in row], c) for c in zip(*family)] == [F(*b)]+[F(0)]*4
        for row, b in zip(col['equations'], col['rhs'])))
    check('whole_kernel_contract', src['weighted_kernel_residuals'] == ver['weighted_kernel_residuals'] and
          len(src['weighted_kernel_residuals']) == 90 and all(not any(F(*v) for v in row) for row in src['weighted_kernel_residuals']))
    check('500_types_3000_presentations', len(src['records']) == len(ver['records']) == 500 and sum(len(r['presentations']) for r in ver['records']) == 3000)
    for i, (a, b) in enumerate(zip(src['records'], ver['records'])):
        check('full_key_'+str(i), all(a[k] == b[k] for k in ['key', 'type', 'affine']) and all(
            p['affine'] is None or p['affine'] == b['affine'] for p in b['presentations']))
    free = list(it.filterfalse(lambda rq: sum(rq) < 8, it.product(range(9), repeat=2)))
    volumes = [F(C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
    check('positive_raw_scaling', len(free) == 45 and min(volumes) > 0 and p8 > 0)
    selected = eq['selected_modes']
    E, rhs, originals, rawrows = [], [], [], []
    pairs = list(it.combinations_with_replacement(range(4), 2))
    for idx, m in enumerate(src['modes']):
        a,b = divmod(idx,9)
        D = F(C(68-2*a,8-a)*C(956-2*b,8-b))
        cross, inverse, base = map(dec, [m['source_cross'], m['inverse_affine'], m['source_base']])
        check('all_original_singular_ranges_'+str(idx), mm(base, inverse) == cross)
        if idx not in selected:
            continue
        cost = [[dot([r[i] for r in cross], [r[j] for r in inverse])/(p8*D) for j in range(5)] for i in range(5)]
        fixed = [F(*v) for v in m['forced']]
        fixed[0] -= F(*m['anchor'])
        Q = [[-(cost[i][j]+cost[j][i])/2 for j in range(5)] for i in range(5)]
        Q[0][0] += fixed[0]
        for i in range(1,5):
            Q[0][i] += fixed[i]/2
            Q[i][0] += fixed[i]/2
        check('full_original_quadratic_'+str(idx), enc(Q) == m['quadratic'] == eq['full_quadratics'][idx])
        H = eye(4)+[[s,F(0),F(0),F(0)]]
        qp = mm(list(map(list,zip(*H))), mm(Q,H))
        bb = [qp[i][j]*(1 if i == j else 2) for i,j in pairs]
        check('six_selected_quadratic_terms_zero_'+str(idx), bb[4:] == [0]*6)
        raw = [F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        ee = [-v/(D*V) for v,V in zip(raw,volumes)]
        cross_plane = [[r[0]+s*r[4]]+r[1:4] for r in cross]
        check('selected_cross_constant_'+str(idx), all(not any(r[1:]) for r in cross_plane))
        E.append(ee); rhs.append(bb); rawrows.append(raw)
        originals.append({'mode':idx, 'D':D, 'plane_quadratic':qp, 'coefficients':bb, 'raw_beta':raw})
    check('all_28_original_rows', len(E) == 28 and enc(E) == eq['original_equalities'] and enc(rhs) == eq['rhs_coefficients'])
    P,N,U = map(dec, [eq['particular_coefficients'], eq['right_kernel'], eq['row_transform']])
    check('all_particular_quadratic_coefficients_zero', all(not any(r[4:]) for r in P))
    L = [r+[F(0)]*18 for r in eye(4)]+[p[:4]+n for p,n in zip(P,N)]
    R = [eye(49)[i] for i in list(range(4))+[4+j for j in eq['nonpivot_columns']]]
    G = [[-v for v in b[:4]]+e for e,b in zip(E,rhs)]
    K = [[F(0)]*28 for _ in range(49)]
    for k,p in enumerate(eq['pivot_columns']):
        K[4+p] = [-v for v in U[k]]
    check('forward_all_equalities', mm(G,L) == [[F(0)]*22 for _ in range(28)])
    check('reverse_left_inverse', mm(R,L) == eye(22))
    check('original_reverse_modulo_equalities', [[v-w for v,w in zip(r,t)] for r,t in zip(mm(L,R),eye(49))] == mm(K,G))
    check('unchanged_saved_lift_reverse', enc(L) == old['lift'] and enc(R) == old['reverse'] and enc(K) == old['reverse_identity_multipliers'])
    original_rows = [r+[F(0)]*45 for r in domain]+[eye(49)[j+4] for j in range(45)]
    pulled = mm(original_rows,L)
    check('all_130_rows_no_deletion', len(pulled) == 130 and enc(pulled) == old['scalar_rows'])
    signs = [F(1) if row[0] >= 0 else F(-1) for row in pulled]
    n,m = 21,130
    # c+a*x >= 0 becomes -a*x_plus+a*x_minus+slack=c.
    standard = [[sg*v for v in [-x for x in row[1:]]+row[1:]+eye(m)[i]] for i,(row,sg) in enumerate(zip(pulled,signs))]
    b0 = [sg*row[0] for sg,row in zip(signs,pulled)]
    T = [r+e for r,e in zip(standard,eye(m))]
    b = b0[:]
    artificial_start = 2*n+m
    basis = list(range(artificial_start,artificial_start+m))
    out.update(p8=p8, stationary_t78=s, free=free, volumes=volumes, domain=domain,
               selected_modes=selected, originals=originals, equalities=G, lift=L, reverse=R,
               reverse_identity_multipliers=K, original_inequalities=original_rows,
               pulled_inequalities=pulled, row_signs=signs, standard_matrix=standard,
               standard_rhs=b0, artificial_start=artificial_start)
    save('full_exact_model_before_phase_one')
    if failures:
        raise SystemExit('Model failure before any simplex run: '+repr(failures))
    trace=[]
    started=time.monotonic()

    def state(stage, path=STATE):
        write(path, {'stage':stage, 'tableau':T, 'rhs':b, 'basis':basis,
                     'row_transform':[r[artificial_start:] for r in T],
                     'pivots':trace, 'elapsed_seconds':time.monotonic()-started})

    state('initialized_before_any_pivot',INITIAL)
    last_print=started
    verdict='UNDECIDED'
    stop=''
    pi=[]
    objective=None
    try:
        while True:
            cb=[F(j >= artificial_start) for j in basis]
            objective=dot(cb,b)
            if objective == 0:
                verdict='RATIONAL_FEASIBLE_WITNESS'; stop='zero_artificial_objective'; break
            if time.monotonic()-started >= SECONDS or len(trace) >= PIVOT_CAP:
                stop='time_limit' if time.monotonic()-started >= SECONDS else 'pivot_limit'; break
            nonbasic=set(range(len(T[0])))-set(basis)
            entering=next((j for j in sorted(nonbasic) if F(j >= artificial_start)-dot(cb,[r[j] for r in T]) < 0),None)
            if entering is None:
                pi=[dot(cb,c) for c in zip(*[r[artificial_start:] for r in T])]
                verdict='POSITIVE_PHASE_ONE_OPTIMUM'; stop='all_reduced_costs_nonnegative'; break
            choices=[(b[i]/r[entering],basis[i],i) for i,r in enumerate(T) if r[entering] > 0]
            if not choices:
                stop='exceptional_no_leaving_row'; break
            ratio,leaving,row=min(choices)
            pivot=T[row][entering]
            pr=[v/pivot for v in T[row]]
            pb=b[row]/pivot
            newT=[]; newb=[]
            for i,r in enumerate(T):
                factor=r[entering]
                if i == row:
                    newT.append(pr); newb.append(pb)
                elif factor:
                    newT.append([v-factor*w if w else v for v,w in zip(r,pr)])
                    newb.append(b[i]-factor*pb)
                else:
                    newT.append(r); newb.append(b[i])
                if time.monotonic()-started >= SECONDS:
                    stop='time_limit_during_atomic_pivot'; break
            if stop:
                break  # T,b,basis still the preceding complete state.
            T,b=newT,newb
            basis[row]=entering
            trace.append({'entering':entering, 'leaving':leaving, 'row':row, 'pivot':pivot,
                          'ratio':ratio, 'objective_before':objective})
            if min(b) < 0:
                stop='exceptional_negative_basic_coordinate'; break
            if len(trace)%10 == 0:
                state('running_checkpoint')
            if time.monotonic()-last_print >= 25:
                print('Phase I:',len(trace),'pivots; elapsed',round(time.monotonic()-started,1),'s; exact objective positive',flush=True)
                last_print=time.monotonic()
    except (KeyboardInterrupt, Exception) as exc:
        stop='interruption_or_exception: '+repr(exc)
        verdict='UNDECIDED'
    state('terminated_'+stop)
    cb=[F(j >= artificial_start) for j in basis]
    objective=dot(cb,b)
    out.update(phase_one={'stop':stop, 'pivots':len(trace), 'objective':objective,
                          'elapsed_seconds':time.monotonic()-started, 'trace':trace,
                          'state_path':str(STATE.relative_to(NB))})
    if verdict == 'RATIONAL_FEASIBLE_WITNESS':
        values=[F(0)]*len(T[0])
        for j,v in zip(basis,b):
            values[j]=v
        reduced=[F(1)]+[values[j]-values[n+j] for j in range(n)]
        lifted=[dot(r,reduced) for r in L]
        raw=[p8*z/V for z,V in zip(lifted[4:],volumes)]
        domain_values=[dot(r,lifted[:4]) for r in domain]
        eqres=[dot(r,lifted) for r in G]
        rawres=[dot(o['raw_beta'],raw)+p8*o['D']*dot(o['coefficients'][:4],lifted[:4]) for o in originals]
        check('zero_artificial_point_standard', min(values)>=0 and objective==0 and all(v==0 for v in values[artificial_start:]) and [dot(r,values[:artificial_start]) for r in standard]==b0)
        check('all_85_original_domain_rows', min(domain_values)>=0)
        check('all_45_original_and_raw_signs', min(lifted[4:])>=0 and min(raw)>=0)
        check('all_28_original_equalities', not any(eqres))
        check('all_28_raw_equalities', not any(rawres))
        out['witness']={'standard_values':values, 'reduced':reduced, 'original':lifted, 'raw_moments':raw,
                        'domain_values':domain_values, 'original_equality_residuals':eqres, 'raw_equality_residuals':rawres}
    elif verdict == 'POSITIVE_PHASE_ONE_OPTIMUM':
        lam=[-v*sg for v,sg in zip(pi,signs)]
        aggregate=[dot(lam,c) for c in zip(*original_rows)]
        mu=[dot(aggregate,c) for c in zip(*K)]
        certificate=[a+b for a,b in zip(aggregate,[dot(mu,c) for c in zip(*G)])]
        rawcertificate=certificate[:4]+[v*V/p8 for v,V in zip(certificate[4:],volumes)]
        check('strict_positive_phase_one_optimum', objective>0)
        check('all_standard_reduced_costs_nonnegative', all(F(j>=artificial_start)-dot(cb,[r[j] for r in T])>=0 for j in range(len(T[0]))))
        check('all_130_inequality_weights_nonnegative', min(lam)>=0)
        check('lifted_original_strict_farkas', certificate[0]<0 and not any(certificate[1:]) and certificate[0]==-objective)
        check('raw_strict_farkas', rawcertificate[0]<0 and not any(rawcertificate[1:]))
        out['separator']={'phase_one_dual':pi, 'inequality_weights':lam, 'equality_multipliers':mu,
                          'equality_positive_orientation_weights':[max(v,0) for v in mu],
                          'equality_negative_orientation_weights':[max(-v,0) for v in mu],
                          'original_aggregate':aggregate, 'original_certificate':certificate,
                          'raw_certificate':rawcertificate}
        verdict='RATIONAL_ORIGINAL_FARKAS_CERTIFICATE'
    out['summary']={'verdict':verdict if not failures else 'FAILED_CERTIFICATE_UNDECIDED',
                    'stop':stop, 'pivots':len(trace), 'checks':len(checks), 'failures':len(failures),
                    'phase_one_objective':objective, 'required_objective_for_feasibility':0,
                    'full_joint_psd_decided':False, 'rs_boundary':[955,957]}
    save('completed')
    print('Summary:',enc(out['summary']),flush=True)
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB),'; tableau:',STATE.relative_to(NB),flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

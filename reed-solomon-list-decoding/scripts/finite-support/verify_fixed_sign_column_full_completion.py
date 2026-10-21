"""Independent original/raw certificate substitution; never invokes a solver."""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_eight_shell import C,beta,enc

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'fixed-sign-column-full-completion-verification.json'


def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b) if x and y),F(0))


def main():
    names=['fixed-sign-column-full-completion-results.json',
           'fixed-sign-column-original-reconstruction.json',
           'fully-cancelling-separator-family-critical-audit.json',
           'affine-sign-phase-one-results.json',
           'affine-sign-remaining-modes-critical-audit.json']
    paths=[ROOT/n for n in names]
    data,recon,src,old,audit=[json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    report={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def check(name,ok):
        checks.append(name)
        if not ok: failures.append(name)
    for name,obj in zip(names,[data,recon,src,old,audit]):
        check('clean_'+name,not obj['failures'])
        for rel,h in obj['input_hashes'].items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    point=[F(*v) for v in old['witness']['original'][:4]]+[F(*src['stationary_t78'])]
    check('frozen_columns',enc(point)==data['point']==recon['point'])
    p8=F(16792471,1181138102168120460)
    free=[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    V=[F(C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
    factors=[dot([F(*v) for v in row],point) for row in src['family']]
    check('all_85_fixed_domain_rows',len(factors)==85 and min(factors)>=0 and enc(factors)==recon['domain_factors'])
    kernel=[[F(*v) for v in row] for row in recon['kernel_residuals']]
    check('all_90_kernel_equations',len(kernel)==90 and all(row==[0]*5 for row in kernel))
    check('500_types_3000_presentations',len(recon['records'])==500 and sum(len(r['presentations']) for r in recon['records'])==3000)
    A=[]; b=[]; norms=[]; rawbetas=[]; rawfixed=[]; rows=[]
    for idx,m in enumerate(src['modes']):
        a,bmode=divmod(idx,9)
        B=[[F(*v) for v in row] for row in m['source_base']]
        cross=[dot([F(*v) for v in row],point) for row in m['source_cross']]
        inv=[dot([F(*v) for v in row],point) for row in m['inverse_affine']]
        residual=[dot(row,inv)-v for row,v in zip(B,cross)]
        check('full_original_range_'+str(idx),residual==[0]*len(B))
        D=F(C(68-2*a,8-a)*C(956-2*bmode,8-bmode)); norm=p8*D
        coeff=[F(beta(68,8,8,a,8-r)*beta(956,8,8,bmode,8-q)) for r,q in free]
        forced=dot([F(*v) for v in m['forced']],point)
        anchor=p8*C(68,8)*C(956,8) if idx==0 else F(0)
        cost=dot(cross,inv); bound=forced-anchor-cost/norm
        row=[-v/(D*vol) for v,vol in zip(coeff,V)]
        check('full_fixed_bound_'+str(idx),norm>0 and enc(anchor)==m['anchor'] and enc(row)==m['row']==data['original_matrix'][idx] and enc(bound)==data['original_rhs'][idx]==recon['rows'][idx]['bound'])
        A.append(row); b.append(bound); norms.append(norm)
        rawbetas.append(coeff); rawfixed.append(norm*(forced-anchor)-cost)
        rows.append({'index':idx,'D':D,'norm':norm,'anchor':anchor,'energy':cost,'bound':bound,'inverse_residuals':residual})
    A += [[F(-int(i==j)) for j in range(45)] for i in range(45)]
    b += [F(0)]*45
    rawA=[[v*vol/p8 for v,vol in zip(row,V)] for row in A]
    check('entire_original_and_raw_system',len(A)==126 and enc(A)==data['original_matrix'] and enc(b)==data['original_rhs']==data['raw_rhs'] and enc(rawA)==data['raw_matrix'])
    verdict=data['summary']['verdict']
    if verdict=='RATIONAL_ORIGINAL_FARKAS_CERTIFICATE':
        lam=[F(*v) for v in data['separator']['original_weights']]
        cancellation=[dot(lam,c) for c in zip(*A)]
        rawcancellation=[dot(lam,c) for c in zip(*rawA)]
        pairing=dot(lam,b)
        # Raw Schur inequalities are -coeff*Y <= rawfixed. Normalize their
        # weights by norm; explicit sign rows retain their positive scaling.
        weights=[v/norm for v,norm in zip(lam[:81],norms)]+lam[81:]
        raw_unscaled_A=[[-v for v in row] for row in rawbetas]+rawA[81:]
        raw_unscaled_b=rawfixed+[F(0)]*45
        raw_direct=[dot(weights,c) for c in zip(*raw_unscaled_A)]
        raw_pairing=dot(weights,raw_unscaled_b)
        check('all_126_nonnegative_weights',len(lam)==126 and min(lam)>=0)
        check('original_strict_Farkas',not any(cancellation) and pairing<0 and enc(pairing)==data['separator']['pairing'])
        check('raw_strict_Farkas',not any(rawcancellation) and not any(raw_direct) and raw_pairing==pairing)
        check('phase_one_pairing',pairing==-F(*data['phase_one']['objective']))
        report['separator']={'weights':lam,'original_cancellation':cancellation,
                             'raw_cancellation':rawcancellation,'raw_unnormalized_weights':weights,
                             'raw_unnormalized_cancellation':raw_direct,'pairing':pairing,
                             'raw_pairing':raw_pairing}
    elif verdict=='RATIONAL_FEASIBLE_WITNESS':
        z=[F(*v) for v in data['witness']['z']]; raw=[p8*v/vol for v,vol in zip(z,V)]
        slack=[v-dot(row,z) for row,v in zip(A,b)]
        rawslack=[v-dot(row,raw) for row,v in zip(rawA,b)]
        rawremainders=[v+dot(row,raw) for row,v in zip(rawbetas,rawfixed)]
        check('all_original_signs_and_modes',len(z)==45 and min(z)>=0 and min(slack)>=0)
        check('all_raw_Schur_remainders',min(raw)>=0 and slack==rawslack and rawremainders==[norm*v for norm,v in zip(norms,slack)] and min(rawremainders)>=0)
        report['witness']={'z':z,'raw':raw,'slacks':slack,'raw_remainders':rawremainders}
    else:
        check('honest_inconclusive_result',verdict=='UNDECIDED')
        state=json.loads((ROOT/'fixed-sign-column-full-completion-state.json').read_text())
        rhs=[F(*v) for v in state['rhs']]
        objective=sum((v for j,v in zip(state['basis'],rhs) if j>=data['artificial_start']),F(0))
        check('saved_complete_nonnegative_basic_state',len(rhs)==len(state['basis'])==126 and min(rhs)>=0 and len(set(state['basis']))==126)
        check('saved_objective_and_trace',enc(objective)==data['phase_one']['objective'] and state['pivots']==data['phase_one']['trace'] and len(state['pivots'])==data['phase_one']['pivots'])
        check('recorded_cap_exit',data['phase_one']['stop'] in ['time_limit','time_limit_during_atomic_pivot','pivot_limit'] and (data['phase_one']['elapsed_seconds']>=300 or data['phase_one']['pivots']>=10000))
        check('no_certificate_claim',objective>0 and 'separator' not in data and 'witness' not in data)
        report['inconclusive_state']={'objective':objective,'pivots':len(state['pivots']),
                                      'elapsed_seconds':data['phase_one']['elapsed_seconds'],
                                      'stop':data['phase_one']['stop']}
    report.update(rows=rows,domain_values=factors,checks=checks,failures=failures)
    report['summary']={'verdict':'VERIFIED_'+verdict if not failures else 'FAILED',
                       'checks':len(checks),'failures':len(failures),'original_modes':81,
                       'sign_rows':45,'required_pairing_for_infeasibility':'strictly negative',
                       'rs_boundary':[955,957]}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print('Summary:',report['summary'])
    if 'separator' in report:
        value=report['separator']['pairing']; scale=10**12
        floor=value.numerator*scale//value.denominator
        print('Exact pairing in [',floor,',',floor+1,') /',scale,'; required: <0')
    print('Failures:',failures,'; full original/raw evidence:',OUT.relative_to(NB))
    if failures: raise SystemExit(1)


if __name__=='__main__': main()

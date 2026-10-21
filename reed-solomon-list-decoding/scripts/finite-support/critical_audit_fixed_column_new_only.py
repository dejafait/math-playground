"""Conditional L088 audit: reconstruct coefficients and replay a saved trace.

No constructor or optimizer is called. The reused ancestral audit evaluates
the OLD L086 moments only; no omitted mixed row is tested at the L088 point.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import critical_audit_affine_sign_remaining_modes as ancestor
import verify_fixed_column_new_only as verifier
from verify_fixed_column_new_only import dec, dot, enc, eye, mul

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'fixed-column-new-only-critical-audit.json'


def main():
    ancestor.OUT = ROOT/'fixed-column-new-only-critical-source.json'
    ancestor.main()
    verifier.OUT = ROOT/'fixed-column-new-only-critical-verification.json'
    verifier.main()
    names = ['fixed-column-new-only-results.json',
             'fixed-column-new-only-original-reconstruction.json',
             'fixed-column-new-only-initial-state.json',
             'fixed-column-new-only-state.json',
             'fixed-column-new-only-verification.json',
             ancestor.OUT.name, verifier.OUT.name,
             'fixed-sign-column-full-completion-results.json',
             'affine-sign-phase-one-results.json']
    paths = [ROOT/n for n in names]
    objects = [json.loads(p.read_text()) for p in paths]
    data, recon, initial, final, saved, source, fresh, full, old = objects
    checks, failures = [], []
    report = {'input_hashes': {str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in paths+[Path(__file__)]}}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        report.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(report), indent=2)+'\n')

    for name, obj in zip(names, objects):
        check('clean_'+name, not obj.get('failures', []))
        for rel, h in obj.get('input_hashes', {}).items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    for field in ['bounds','domain_factors','witness','summary']:
        check('complete_fresh_verifier_'+field, saved[field]==fresh[field])
    check('frozen_point', data['point']==source['point']==recon['point']==full['point']
          and data['point'][:4]==old['witness']['original'][:4])
    check('all_presentations_and_kernel_rows', source['records']==recon['records']
          and source['kernel_residuals']==recon['kernel_residuals']
          and source['domain_factors']==recon['domain_factors']==enc(fresh['domain_factors']))
    p8=F(16792471,1181138102168120460)
    point=[F(*v) for v in data['point']]
    selected=[9*a+b for a in range(7) for b in range(4)]
    newonly=[i for i in range(81) if max(divmod(i,9))==8]
    check('partition',data['selected_modes']==selected and data['new_only_modes']==newonly
          and len(set(selected+newonly))==45)
    rows, bounds, norms, rawcoeff, rawfixed = [], [], [], [], []
    for i,(s,r,v) in enumerate(zip(source['rows'],recon['rows'],fresh['bounds'])):
        check('complete_original_row_'+str(i), s['index']==i and s['original_row']==r['original_row']==full['original_matrix'][i]
              and s['raw_beta']==r['raw_beta'] and s['bound']==r['bound']==full['original_rhs'][i]==v['bound'])
        norm=F(*s['norm']); cost=F(*s['energy'])
        forced=dot([F(*x) for x in s['forced_raw']],point)
        anchor=F(*s['raw_anchor']); bound=(forced-anchor-cost)/norm
        check('full_anchor_range_cost_'+str(i),norm>0 and bound==F(*s['bound'])
              and cost==F(*v['cost']) and anchor/norm==F(*v['anchor'])
              and forced/norm==F(*v['forced']))
        if i in newonly:
            check('empty_new_only_'+str(i),s['layers']==[] and s['base']==[] and cost==anchor==0)
        rows.append([F(*x) for x in s['original_row']]); bounds.append(bound)
        norms.append(norm);rawcoeff.append([F(*x) for x in s['raw_beta']]);rawfixed.append(forced-anchor-cost)
    check('all_81_coefficient_rows',len(rows)==81)
    Q=[[-bounds[i]]+rows[i] for i in selected]
    H=[[bounds[i]]+[-v for v in rows[i]] for i in newonly]+[[F(0)]+r for r in eye(45)]
    rawQ=[[rawfixed[i]]+rawcoeff[i] for i in selected]
    rawH=[[rawfixed[i]]+rawcoeff[i] for i in newonly]+[[F(0)]+r for r in eye(45)]
    check('reconstructed_original_raw_system',enc([Q,H,rawQ,rawH])==[data['original_equalities'],data['original_inequalities'],data['raw_equalities'],data['raw_inequalities']])
    L,R,K=map(dec,[data['lift'],data['reverse'],data['equality_multipliers']])
    scales=[F(1)]+[F(*v) for v in data['scales']]
    rawL=[[s*v for v in r] for s,r in zip(scales,L)]
    rawR=[[v/s for v,s in zip(r,scales)] for r in R]
    rawK=[[-s*v/norms[i] for i,v in zip(selected,r)] for s,r in zip(scales,K)]
    for tag,q,l,r,k in [('original',Q,L,R,K),('raw',rawQ,rawL,rawR,rawK)]:
        check(tag+'_forward',mul(q,l)==[[0]*19 for _ in range(28)])
        check(tag+'_left_inverse',mul(r,l)==eye(19))
        check(tag+'_reverse',mul(k,q)==[[x-y for x,y in zip(a,b)] for a,b in zip(mul(l,r),eye(46))])
    pulled=mul(H,L)
    signs=[F(1) if row[0]>=0 else F(-1) for row in pulled]
    A=[[sg*v for v in [-x for x in row[1:]]+row[1:]+eye(62)[i]] for i,(row,sg) in enumerate(zip(pulled,signs))]
    rhs0=[sg*row[0] for sg,row in zip(signs,pulled)]
    labels=[{'kind':'new_only_mode','index':i,'mode':list(divmod(i,9))} for i in newonly]
    labels += [{'kind':'moment_sign','index':i,'rq':[r,q]} for i,(r,q) in enumerate((r,q) for r in range(9) for q in range(9) if r+q>=8)]
    check('all_62_labels_pulls_orientations',enc([pulled,signs,A,rhs0])==[data['pulled_inequalities'],data['row_signs'],data['standard_matrix'],data['standard_rhs']] and labels==data['row_labels'])
    T=[r+e for r,e in zip(A,eye(62))]; rhs=rhs0[:]; basis=list(range(98,160))
    check('standard_dimensions',len(T)==62 and all(len(r)==160 for r in T) and data['artificial_start']==98)
    check('entire_initial_tableau',T==dec(initial['tableau']) and rhs==[F(*v) for v in initial['rhs']] and min(rhs)>=0)
    check('initial_basis_and_transform',basis==initial['basis'] and dec(initial['row_transform'])==eye(62) and initial['pivots']==[])
    trace=data['phase_one']['trace']
    check('complete_trace',trace==final['pivots'] and len(trace)==233==data['phase_one']['pivots'])
    report.update(original_equalities=Q,original_inequalities=H,raw_equalities=rawQ,raw_inequalities=rawH,
                  lift=L,reverse=R,equality_multipliers=K,raw_lift=rawL,raw_reverse=rawR,raw_multipliers=rawK,
                  pulled=pulled,standard_matrix=A,standard_rhs=rhs0,replay=[])
    save('complete_model_checked_before_saved_trace')
    for step,event in enumerate(trace):
        enter,leave,row=event['entering'],event['leaving'],event['row']
        cb=[F(j>=98) for j in basis]; objective=dot(cb,rhs)
        reduced={j:F(j>=98)-dot(cb,[r[j] for r in T]) for j in range(enter+1) if j not in basis}
        check('pre_objective_'+str(step),objective>0 and objective==F(*event['objective_before']))
        check('declared_entering_'+str(step),enter in reduced and reduced[enter]<0 and all(v>=0 for j,v in reduced.items() if j<enter))
        choices=[(rhs[i]/r[enter],basis[i],i) for i,r in enumerate(T) if r[enter]>0]
        ratio=F(*event['ratio']);pivot=T[row][enter]
        check('minimum_ratio_tie_'+str(step),bool(choices) and min(choices)==(ratio,leave,row))
        check('saved_pivot_'+str(step),pivot>0 and pivot==F(*event['pivot']) and basis[row]==leave)
        prow=[v/pivot for v in T[row]];prhs=rhs[row]/pivot
        for i in range(62):
            if i==row:continue
            f=T[i][enter]
            if f:
                T[i]=[x-f*y if y else x for x,y in zip(T[i],prow)];rhs[i]-=f*prhs
        T[row]=prow;rhs[row]=prhs;basis[row]=enter
        check('nonnegative_rhs_'+str(step),min(rhs)>=0)
        check('basis_identity_'+str(step),len(set(basis))==62 and all(T[i][j]==F(i==k) for k,j in enumerate(basis) for i in range(62)))
        after=dot([F(j>=98) for j in basis],rhs)
        check('objective_update_'+str(step),after==objective+ratio*reduced[enter] and after>=0)
        report['replay'].append({'step':step,'objective_before':objective,'objective_after':after,'reduced_cost':reduced[enter],'ratio':ratio,'pivot':pivot})
        if (step+1)%50==0:save('replayed_'+str(step+1))
    check('entire_final_tableau',T==dec(final['tableau']) and rhs==[F(*v) for v in final['rhs']] and basis==final['basis'])
    U=[r[98:] for r in T]
    check('final_row_transform',U==dec(final['row_transform']) and mul(U,[r+e for r,e in zip(A,eye(62))])==T and [dot(r,rhs0) for r in U]==rhs)
    values=[F(0)]*160
    for j,v in zip(basis,rhs):values[j]=v
    check('standard_witness',enc(values)==data['witness']['standard_values'] and min(values)>=0 and not any(values[98:]) and [dot(r,values[:98]) for r in A]==rhs0)
    h=[values[i]-values[18+i] for i in range(18)]
    w=[dot(r,[F(1)]+h) for r in L];raw=[v*s for v,s in zip(w,scales)]
    check('complete_witness_link',w[0]==raw[0]==1 and enc(h)==data['witness']['h'] and enc(w[1:])==data['witness']['z']==fresh['witness']['z'] and enc(raw[1:])==data['witness']['raw_moments'])
    eqres=[dot(r,w) for r in Q];raweq=[dot(r,raw) for r in rawQ]
    slacks=[dot(r,w) for r in H];rawslacks=[dot(r,raw) for r in rawH]
    check('every_original_raw_retained_row',not any(eqres+raweq) and min(slacks)==min(rawslacks)==0 and rawslacks[:17]==[norms[i]*v for i,v in zip(newonly,slacks[:17])])
    check('canonical_counts',sum(v>0 for v in slacks[:17])==11 and sum(v==0 for v in slacks[:17])==6 and sum(v>0 for v in w[1:])==31 and sum(v==0 for v in w[1:])==14)
    check('recorded_limits',data['limits']=={'runs':1,'pivots':10000,'seconds':300} and 0<=final['elapsed_seconds']<=data['phase_one']['elapsed_seconds']<=300)
    check('zero_objective',sum(values[98:])==F(*data['phase_one']['objective'])==0 and data['phase_one']['stop']=='zero_artificial_objective')
    report.update(witness=w,raw_witness=raw,original_residuals=eqres,raw_residuals=raweq,original_slacks=slacks,raw_slacks=rawslacks,final_tableau=T,final_rhs=rhs,final_basis=basis,row_transform=U)
    report['summary']={'verdict':'RETAINED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),
       'source_checks':len(source['checks']),'original_raw_verifier_checks':len(fresh['checks']),
       'pivots_replayed':len(trace),'required_pivots':233,'new_only_positive':11,'new_only_zero':6,
       'moments_positive':31,'moments_zero':14,'actual_minimum_original':min(slacks),'actual_minimum_raw':min(rawslacks),
       'required_minimum':0,'nonzero_equality_residuals':sum(v!=0 for v in eqres+raweq),
       'omitted_mixed_modes_at_new_witness':'NOT_TESTED','ancestor_contracts':'IMPORTED_WITH_EXISTING_QUALIFICATIONS','rs_boundary':[955,957]}
    save('completed')
    print('Summary:',enc(report['summary']),flush=True)
    print('Failures:',failures,'; certificate:',OUT.relative_to(NB),flush=True)
    if failures:raise SystemExit(1)


if __name__=='__main__':main()

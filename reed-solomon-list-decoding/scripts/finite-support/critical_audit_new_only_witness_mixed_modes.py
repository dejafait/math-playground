"""Dedicated conditional L089 audit; no optimizer or candidate variation.

Rebuild the fixed source via the inspected L087 audit, then independently
substitute L088's complete moments in original, raw and weighted coordinates.
Old L086 residuals in that source rebuild are regression controls only.
"""
import hashlib
import itertools as it
import json
import re
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

import critical_audit_affine_sign_remaining_modes as source_audit
import verify_new_only_witness_mixed_modes as verifier

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'new-only-witness-mixed-modes-critical-audit.json'


def enc(x):
    if isinstance(x,F): return [x.numerator,x.denominator]
    if isinstance(x,dict): return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [enc(v) for v in x]
    return x


def dot(x,y):
    assert len(x)==len(y)
    return sum((a*b for a,b in zip(x,y)),F(0))


def C(n,k):
    from math import comb
    return comb(n,k) if 0<=k<=n else 0


def eigen(n,a,r):
    return sum((-1)**h*C(a,h)*C(8-a,r-h)*C(n-8-a,r-h) for h in range(r+1))


def main():
    source_audit.OUT=ROOT/'new-only-witness-mixed-modes-critical-source.json'
    if '--reuse-reconstruction' not in sys.argv: source_audit.main()
    verifier.OUT=ROOT/'new-only-witness-mixed-modes-critical-verification.json'
    if '--reuse-reconstruction' not in sys.argv: verifier.main()
    names=['fixed-column-new-only-results.json',
           'fixed-column-new-only-original-reconstruction.json',
           'fixed-column-new-only-verification.json',
           'fixed-column-new-only-critical-source.json',
           'fixed-column-new-only-critical-verification.json',
           'fixed-column-new-only-critical-audit.json',
           'new-only-witness-mixed-modes-results.json',
           'new-only-witness-mixed-modes-verification.json',
           source_audit.OUT.name,verifier.OUT.name]
    paths=[ROOT/n for n in names]
    data,recon,v318,s320,v320,a320,result,v322,source,fresh=[json.loads(p.read_text()) for p in paths]
    checks=[];failures=[]
    report={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths+[Path(__file__)]}}
    def check(name,ok):
        checks.append(name)
        if not ok: failures.append(name)
    def save(stage):
        report.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    for path,obj in zip(paths,[data,recon,v318,s320,v320,a320,result,v322,source,fresh]):
        check('clean_'+path.name,not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('binding_'+path.name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    for field in ['rows','negative_indices','positive_indices','zero_indices','load_bearing_81_terms','load_bearing_scaled','load_bearing_raw','summary']:
        check('full_verifier_reproduction_'+field,fresh[field]==v322[field])
    for field in ['bounds','domain_factors','witness','summary']:
        check('full_318_320_'+field,v318[field]==v320[field])
    for field in ['point','domain_factors','kernel_residuals','records']:
        check('complete_frozen_'+field,source[field]==s320[field]==recon[field]==result[field])
    for field in ['family','original_seven_column','completion','factors','transitions']:
        check('complete_source_regression_'+field,source[field]==s320[field])
    t=[F(*x) for x in data['point']]
    z=[F(*x) for x in data['witness']['z']]
    raw=[F(*x) for x in data['witness']['raw_moments']]
    p8=F(16792471,1181138102168120460)
    free=[(r,q) for r in range(9) for q in range(9) if r+q>=8]
    V=[C(8,r)*C(60,r)*C(8,q)*C(948,q) for r,q in free]
    check('entire_45_coordinate_binding',len(z)==len(raw)==45 and enc(z)==result['z']==v318['witness']['z']==a320['witness'][1:] and enc(raw)==result['raw_moments']==v318['witness']['raw_moments']==a320['raw_witness'][1:])
    check('full_parameter_binding',len(t)==5 and t[0]==1 and enc(t)==source['point']==result['point'])
    check('positive_raw_scale',p8>0 and min(V)>0 and raw==[p8*x/v for x,v in zip(z,V)] and enc(list(map(F,V)))==data['volumes'])
    check('all_sign_controls',sum(x>0 for x in z)==31 and sum(x==0 for x in z)==14 and min(z)==min(raw)==0)
    I=[9*a+b for a in range(7) for b in range(4)]
    J=[i for i in range(81) if max(divmod(i,9))==8]
    K=[i for i in range(81) if i not in I+J]
    check('full_partition',list(map(len,[I,J,K]))==[28,17,36] and sorted(I+J+K)==list(range(81)) and [I,J,K]==[result['selected'],result['new_only'],result['mixed']])
    entries={tuple(r['type']):dot([F(*x) for x in r['affine']],t) for r in source['records'] if r['affine'] is not None}
    for (r,q),x in zip(free,raw): entries[8,8,8-r,8-q]=x
    check('full_81_actual_moments',len([k for k in entries if k[:2]==(8,8)])==81 and sum(r['affine'] is None for r in source['records'][-81:])==45)
    gamma={}
    for tr in source['transitions']:
        n,l,m,j=tr['indices']
        for action in tr['actions']: gamma[n,l,m,action['degree'],j]=F(*action['coefficient'])
    norms={(r['n'],r['layer']):[F(*v) for v in r['norms']] for r in source['factors']}
    check('dimensions_before_substitution',len(source['rows'])==len(result['rows'])==len(v322['rows'])==81 and len(source['records'])==500 and sum(len(r['presentations']) for r in source['records'])==3000 and len(source['kernel_residuals'])==90)
    report.update(point=t,z=z,raw_moments=raw,selected=I,new_only=J,mixed=K)
    save('complete_frozen_data_checked')
    rows=[];term_records=[]
    for idx in range(81):
        a,b=divmod(idx,9);s=source['rows'][idx];r=result['rows'][idx]
        for field in ['layers','base','cross','affine_range_residuals','minors','energy','norm','raw_beta','original_row','forced_raw','raw_anchor','bound']:
            check('source_row_'+str(idx)+'_'+field,s[field]==r[field])
        for label,old,scale_key in [('318',recon['rows'][idx],'positive_raw_normalization'),('320',s320['rows'][idx],'norm')]:
            check('prior_complete_coefficients_'+str(idx)+'_'+label,all(old[k]==s[k] for k in ['base','cross','energy','raw_beta','original_row','forced_raw','raw_anchor','bound']) and old[scale_key]==s['norm'])
        D=F(C(68-2*a,8-a)*C(956-2*b,8-b));norm=p8*D
        N=norms[68,8][a]*norms[956,8][b]
        A=[F(-eigen(68,a,u)*eigen(956,b,v),vol) for (u,v),vol in zip(free,V)]
        check('all_independent_coefficients_'+str(idx),D>0 and N>0 and enc(A)==s['original_row'] and [F(*x) for x in s['raw_beta']]==[-D*vol*x for vol,x in zip(V,A)] and norm==F(*s['norm']))
        original=F(*s['bound'])-dot(A,z)
        terms=[];weighted_terms=[]
        for u,v in it.product(range(9),repeat=2):
            Y=entries[8,8,8-u,8-v]
            e=eigen(68,a,u)*eigen(956,b,v)
            terms.append(F(e)*Y)
            g=gamma[68,8,8,a,8-u]*gamma[956,8,8,b,8-v]
            weighted_terms.append(g*Y)
            check('independent_diagonal_coefficient_'+str((idx,u,v)),g==e)
        anchor=F(*s['raw_anchor']);cost=F(*s['energy'])
        raw_value=D*sum(terms,F(0))-anchor-cost
        weighted_anchor=p8*p8*C(68,8)*C(956,8) if idx==0 else F(0)
        weighted_value=N*(sum(weighted_terms,F(0))-weighted_anchor)-F(*s['weighted_energy'])
        check('full_anchor_'+str(idx),anchor==(p8*p8*(C(68,8)*C(956,8))**2 if idx==0 else 0) and weighted_anchor*N==anchor*N/D)
        check('all_three_reconstructions_'+str(idx),raw_value==norm*original and weighted_value/(p8*N)==original and enc(original)==r['scaled_slack']==v322['rows'][idx]['scaled_slack'] and enc(raw_value)==r['raw_remainder']==v322['rows'][idx]['raw_remainder'])
        if idx in I: check('selected_zero_'+str(idx),original==raw_value==0)
        if idx in J:
            j=J.index(idx)
            check('new_only_control_'+str(idx),s['base']==[] and s['cross']==[] and anchor==cost==0 and original>=0 and enc(original)==data['witness']['original_slacks'][j] and enc(raw_value)==data['witness']['raw_slacks'][j])
        rows.append({'index':idx,'mode':[a,b],'scaled_slack':original,'raw_remainder':raw_value,'weighted_remainder':weighted_value,'norm':norm,'weighted_norm':p8*N,'diagonal':D*sum(terms,F(0))})
        term_records.append({'index':idx,'eigen_terms':terms,'weighted_terms':weighted_terms})
    neg=[i for i in K if rows[i]['scaled_slack']<0];pos=[i for i in K if rows[i]['scaled_slack']>0]
    check('all_mixed_signs',neg==[6,15,23,25,31,32,34,42,49,50,52,60,64,66,67,68]==result['negative_indices']==v322['negative_indices'] and len(pos)==20 and not any(rows[i]['scaled_slack']==0 for i in K))
    check('retained_control_counts',sum(rows[i]['scaled_slack']>0 for i in J)==11 and sum(rows[i]['scaled_slack']==0 for i in J)==6)
    failing=[{k:rows[i][k] for k in ['index','mode','scaled_slack','raw_remainder']} for i in neg]
    check('every_full_reduced_failure',enc(failing)==result['failing_remainders'])
    s=source['rows'][66];v=rows[66]['scaled_slack'];D=rows[66]['norm']/p8
    load_terms=[D*x for x in term_records[66]['eigen_terms']]
    # Verifier orders source intersections (i,j), reverse of distance indices (r,q).
    check('all_81_load_terms',enc(load_terms)==list(reversed(v322['load_bearing_81_terms'])) and sum(load_terms,F(0))==rows[66]['raw_remainder']<0)
    check('zero_old_block_and_cross',s['layers']==[7] and s['base']==[[[0,1]]] and s['cross']==[[0,1]] and s['energy']==s['raw_anchor']==[0,1] and all(not any(F(*x) for x in row) for row in s['affine_range_residuals']))
    check('load_bearing_scaling',rows[66]['norm']==F(1782682793617737,363922042337)>0 and rows[66]['diagonal']==rows[66]['raw_remainder']==rows[66]['norm']*v)
    manuscript=(NB/'lemmas/L089-fixed-new-only-witness-fails-mixed-modes.md').read_text()
    numerator=int(re.search(r'^N=(-?\d+)$',manuscript,re.M)[1]);denominator=int(re.search(r'^Q=(\d+)$',manuscript,re.M)[1])
    check('every_digit_reduced_manuscript',numerator==v.numerator<0 and denominator==v.denominator>0)
    worst=min(K,key=lambda i:rows[i]['scaled_slack'])
    check('minimum_interval',worst==64 and F(-4587146655180994,10**6)<=rows[worst]['scaled_slack']<F(-4587146655180993,10**6)<0)
    check('all_old_cases',Counter(len(r['layers']) for r in source['rows'])=={3:36,2:13,1:15,0:17} and sum(len(r['minors']) for r in source['rows'])==306)
    lo=v.numerator*10**12//v.denominator
    report.update(rows=rows,diagonal_terms=term_records,negative_indices=neg,positive_indices=pos,failing_remainders=failing,load_bearing_raw_terms=load_terms,manuscript_rational=[numerator,denominator])
    report['summary']={'verdict':'RETAINED_FIXED_ASSIGNMENT_REJECTION' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),'source_checks':len(source['checks']),'verifier_checks':len(fresh['checks']),'mixed_negative':len(neg),'mixed_positive':len(pos),'selected_equalities':28,'new_only_positive':11,'new_only_zero':6,'positive_moments':31,'zero_moments':14,'original_raw_weighted_identities':81,'complete_diagonal_sums':81,'load_bearing_scaled_interval':[lo,lo+1,10**12],'required_lower_bound':0,'minimum_mixed_interval':[-4587146655180994,-4587146655180993,10**6],'ancestor_contracts':'IMPORTED_WITH_EXISTING_QUALIFICATIONS','rs_boundary':[955,957]}
    save('completed')
    print('Summary:',enc(report['summary']),flush=True)
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB),flush=True)
    if failures: raise SystemExit(1)


if __name__=='__main__': main()

"""Conditional L095 audit; no optimization or change of witness.

Reuse independent source reconstruction, with its L086 residuals only as
regression controls. Reconstruct every current source/raw/weighted row and
the complete offending block. Ancestor hypotheses remain conditional.
"""
import hashlib
import itertools as it
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path

import verify_l094_complementary_modes as verification
from critical_audit_simultaneous_eight_shell import c, dot, enc
from verify_simultaneous_eight_shell import beta, det, cramer

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'l095-critical-audit.json'


def dec(m):
    return [[F(*v) for v in row] for row in m]


def main():
    if OUT.exists():
        raise RuntimeError('Audit output exists; inspect before choosing another output path')
    verification.OUT = ROOT/'l095-critical-verification.json'
    verification.main()
    checks, failures = [], []
    report = {'input_hashes': {str(Path(__file__).relative_to(NB)):
                              hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def read(name, clean=True):
        path = ROOT/name
        obj = json.loads(path.read_text())
        report['input_hashes'][str(path.relative_to(NB))] = hashlib.sha256(path.read_bytes()).hexdigest()
        if clean:
            check('clean_'+name, not obj.get('failures', []))
        for rel, h in obj.get('input_hashes', {}).items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == h)
        return obj

    def save(stage):
        report.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(report), indent=2)+'\n')

    source = read('two-mixed-row-critical-source.json')
    fresh = read(verification.OUT.name)
    data = read('two-mixed-row-results.json')
    result = read('l094-complementary-modes-results.json')
    savedver = read('l094-complementary-modes-verification.json')
    source_affine = read('fully-cancelling-separator-family-critical-audit.json')
    for key in ['rows', 'negative_indices', 'positive_indices', 'zero_indices',
                'load_bearing_81_terms', 'load_bearing_block', 'load_bearing_vector',
                'load_bearing_scaled', 'load_bearing_raw', 'actual_congruence', 'summary']:
        check('entire_original_verifier_'+key, fresh[key] == savedver[key])
    t = [F(*v) for v in data['point']]
    z = [F(*v) for v in data['witness']['z']]
    raw = [F(*v) for v in data['witness']['raw_moments']]
    p8 = F(16792471, 1181138102168120460)
    free = list((r,q) for r,q in it.product(range(9), repeat=2) if r+q >= 8)
    volumes = [c(8,r)*c(60,r)*c(8,q)*c(948,q) for r,q in free]
    check('entire_frozen_point', enc(t) == source['point'] == result['point']
          and t[0] == 1 and t[4] == F(*source_affine['stationary_t78']))
    check('entire_frozen_witness', len(z) == len(raw) == 45 and enc(z) == result['z']
          and enc(raw) == result['raw_moments'] and raw == [p8*v/V for v,V in zip(z,volumes)]
          and p8 > 0 and min(volumes) > 0)
    for key in ['records', 'kernel_residuals', 'domain_factors']:
        check('current_full_'+key, source[key] == result[key])
    check('85_domain_rows', len(source['domain_factors']) == 85
          and min(F(*v) for v in source['domain_factors']) == 0)
    check('90_affine_kernel_rows', len(source['kernel_residuals']) == 90
          and all(len(row) == 5 and not any(F(*v) for v in row) for row in source['kernel_residuals']))
    check('500_3000_presentations', len(source['records']) == 500
          and all(len(r['presentations']) == 6 for r in source['records']))

    # Complete existing L094 and L091 contracts; no recursive ancestor proof audit.
    previous_audit = read('two-mixed-row-critical-audit.json')
    previous_verifier = read('two-mixed-row-critical-verification.json')
    check('complete_audited_witness', previous_audit['witness']==[[1,1]]+enc(z)
          and previous_audit['raw_witness']==[[1,1]]+enc(raw)
          and previous_verifier['witness']['z']==enc(z)
          and previous_verifier['witness']['raw_moments']==enc(raw))
    original_source = read('two-mixed-row-original-reconstruction.json')
    for field in ['point','records','kernel_residuals','domain_factors']:
        check('complete_original_source_'+field, source[field]==original_source[field])
    for path in [Path(verification.__file__)]:
        report['input_hashes'][str(path.relative_to(NB))]=hashlib.sha256(path.read_bytes()).hexdigest()

    selected = [9*a+b for a in range(7) for b in range(4)]
    retained = [i for i,r in enumerate(source['rows']) if all(F(*v)==0 for row in r['base'] for v in row)]
    tested=sorted(retained+[23,31])
    remaining = sorted(set(range(81))-set(selected)-set(tested))
    check('full_partition', selected == result['selected'] == data['selected_modes']
          and retained == result['zero_old_block'] == data['zero_old_block_modes']
          and remaining == result['remaining'] and len(remaining) == 28 and all(j not in selected+retained for j in [23,31]) and tested==data['retained_modes'] and len(retained) == 43
          and len(set(selected)&set(retained)) == 20
          and {i for i in range(81) if max(divmod(i,9)) == 8} <= set(retained))
    report.update(point=t, z=z, raw_moments=raw, selected=selected,
                  zero_old_block=retained, remaining=remaining)
    save('all_frozen_and_prior_arrays_checked')
    if failures:
        raise RuntimeError('Input discrepancy: inspect saved failures before a verdict')

    gamma = {(tr['indices'][0],tr['indices'][1],tr['indices'][2],a['degree'],tr['indices'][3]): F(*a['coefficient'])
             for tr in source['transitions'] for a in tr['actions']}
    norms = {(r['n'],r['layer']): [F(*v) for v in r['norms']] for r in source['factors']}
    entries = {tuple(r['type']): (None if r['affine'] is None else dot([F(*v) for v in r['affine']],t))
               for r in source['records']}
    for (r,q),v in zip(free,raw): entries[8,8,8-r,8-q] = v
    check('all_81_current_diagonal_moments', all(entries[8,8,i,j] is not None for i,j in it.product(range(9),repeat=2)))
    read_base=read('maximizer-excluded-anchor-results.json')
    check('positive_original_rho_p8',F(*read_base['rho'])>0 and F(*read_base['pairs_through_14'][8])==p8)
    rows = []
    for idx,s in enumerate(source['rows']):
        a,b = divmod(idx,9); B = dec(s['base']); cv = [F(*v) for v in s['cross']]
        ls=[l for l in [5,6,7] if l>=max(a,b)]
        pairs=[F(*v) for v in read_base['pairs_through_14']]
        def direct_entry(l,m):
            ll,mm=sorted([l,m])
            ans=sum(F(beta(68,l,m,a,i)*beta(956,l,m,b,j))*entries[ll,mm,i,j]
                    for i,j in it.product(range(ll+1),repeat=2))
            if idx==0:
                ans-=pairs[l]*pairs[m]*c(68,l)*c(956,l)*c(68,m)*c(956,m)
            return ans
        check('complete_current_old_cross_'+str(idx),
              B==[[direct_entry(l,m) for m in ls] for l in ls]
              and cv==[direct_entry(l,8) for l in ls]
              and cv==[direct_entry(8,l) for l in ls])
        m=source_affine['modes'][idx]
        ai=dec(m['inverse_affine']); ac=dec(m['source_cross'])
        check('complete_affine_range_'+str(idx),enc(B)==m['source_base']
              and all(sum(B[i][j]*ai[j][k] for j in range(len(B)))==ac[i][k]
                      for i in range(len(B)) for k in range(5)))
        chosen = (); minors = []
        for k in range(1,len(B)+1):
            for inds in it.combinations(range(len(B)),k):
                d = det([[B[i][j] for j in inds] for i in inds]); minors.append(d)
                if d: chosen=inds
        x = [F(0)]*len(B)
        if chosen:
            xx = cramer([[B[i][j] for j in chosen] for i in chosen],[cv[i] for i in chosen])
            for j,v in zip(chosen,xx): x[j]=v
        check('old_PSD_and_complete_range_'+str(idx), all(d>=0 for d in minors)
              and [dot(row,x)-v for row,v in zip(B,cv)] == [0]*len(B))
        D = F(c(68-2*a,8-a)*c(956-2*b,8-b)); norm = p8*D
        N = norms[68,8][a]*norms[956,8][b]
        A = [F(*v) for v in s['original_row']]
        rawbeta=[F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        check('independent_all_row_coefficients_'+str(idx),
              A==[-v/(D*vol) for v,vol in zip(rawbeta,volumes)]
              and enc(rawbeta)==s['raw_beta']==result['rows'][idx]['raw_beta'])
        anchor = p8*p8*(c(68,8)*c(956,8))**2 if idx==0 else F(0)
        terms = [F(beta(68,8,8,a,i)*beta(956,8,8,b,j))*entries[8,8,i,j]
                 for i,j in it.product(range(9),repeat=2)]
        weighted_terms = [gamma[68,8,8,a,i]*gamma[956,8,8,b,j]*entries[8,8,i,j]
                          for i,j in it.product(range(9),repeat=2)]
        diagonal = sum(terms,F(0))-anchor
        energy = dot(cv,x)
        rawvalue = diagonal-energy
        slack = F(*s['bound'])-dot(A,z)
        weighted_diagonal = N*(sum(weighted_terms,F(0))-(p8*p8*c(68,8)*c(956,8) if idx==0 else 0))
        weighted_value = weighted_diagonal-F(*s['weighted_energy'])
        check('all_original_raw_weighted_'+str(idx), norm>0 and N>0
              and rawvalue==norm*slack and weighted_value==p8*N*slack
              and weighted_diagonal==(N/D)*diagonal and energy==F(*s['energy'])
              and F(*s['bound'])==(diagonal-dot(rawbeta,raw)-energy)/norm)
        saved = result['rows'][idx]
        for key,value in [('base',B),('cross',cv),('fresh_inverse',x),('norm',norm),
                          ('energy',energy),('raw_anchor',anchor),('scaled_slack',slack),('raw_remainder',rawvalue)]:
            check('current_complete_'+str((idx,key)), enc(value)==saved[key])
        check('all_saved_old_minors_'+str(idx),enc(minors)==[v['determinant'] for v in saved['minors']])
        check('current_verifier_'+str(idx), enc(slack)==fresh['rows'][idx]['scaled_slack']
              and enc(rawvalue)==fresh['rows'][idx]['raw_remainder'])
        if idx in selected: check('retained_equality_'+str(idx), slack==rawvalue==0)
        if idx in tested:
            j=tested.index(idx)
            check('retained_zero_block_'+str(idx), (idx in [23,31] or (not any(cv) and energy==anchor==0)) and slack>=0
                  and enc(slack)==data['witness']['original_slacks'][j]
                  and enc(rawvalue)==data['witness']['raw_slacks'][j])
        check('membership_'+str(idx), saved['base']==data['membership'][idx]['base']
              and saved['cross']==data['membership'][idx]['cross']
              and (not B)==data['membership'][idx]['empty']
              and (idx in retained)==data['membership'][idx]['zero_old_block'])
        rows.append({'index':idx,'mode':[a,b],'base':B,'cross':cv,'inverse':x,'diagonal':diagonal,
                     'norm':norm,'energy':energy,'raw_anchor':anchor,'scaled_slack':slack,
                     'raw_remainder':rawvalue,'weighted_remainder':weighted_value,
                     'weighted_diagonal':weighted_diagonal,'all_81_raw_terms':terms,
                     'all_81_weighted_terms':weighted_terms})
    negative=[i for i in remaining if rows[i]['scaled_slack']<0]
    positive=[i for i in remaining if rows[i]['scaled_slack']>0]
    check('complete_14_14_signs',negative==[5,7,14,16,24,32,34,40,42,50,52,58,60,68]
          and negative==result['negative_indices']==fresh['negative_indices'] and len(positive)==14)
    check('all_retained_sign_counts',sum(v>0 for v in z)==33 and sum(v==0 for v in z)==12
          and min(raw)==min(z)==0 and sum(rows[i]['scaled_slack']>0 for i in retained)==13
          and sum(rows[i]['scaled_slack']==0 for i in retained)==30)
    worst=min(remaining,key=lambda i:rows[i]['scaled_slack']); r=rows[worst]
    block=[row+[v] for row,v in zip(r['base'],r['cross'])]+[r['cross']+[r['diagonal']]]
    vector=[-v for v in r['inverse']]+[F(1)]
    value=dot(vector,[dot(row,vector) for row in block])
    off=result['offending_block']
    check('full_negative_block_vector',worst==5 and len(block)==len(vector)==4
          and all(len(row)==4 for row in block) and all(block[i][j]==block[j][i] for i,j in it.product(range(4),repeat=2))
          and enc(block)==off['block']==fresh['load_bearing_block'] and enc(vector)==off['vector']
          and value==r['raw_remainder']==F(*off['quadratic_value'])==F(*fresh['load_bearing_raw'])<0
          and r['diagonal']==F(*off['diagonal']))
    # Actual positive scales, both weighted rectangular directions, and new diagonal.
    a,b=divmod(worst,9); ls=source['rows'][worst]['layers']; D=F(c(68-2*a,8-a)*c(956-2*b,8-b))
    N=norms[68,8][a]*norms[956,8][b]; alpha=N/D
    def sigma(n,l,m,degree):
        values=[]
        for k in range(min(l,m)+1):
            be=beta(n,l,m,degree,k); g=gamma[n,l,m,degree,k]
            if be: values.append(norms[n,l][degree]*g/be)
            else: check('zero_beta_action_'+str((n,l,m,degree,k)),g==0)
        check('positive_constant_ratio_'+str((n,l,m,degree)),bool(values) and min(values)>0
              and all(v==values[0] for v in values))
        return values[0]
    scales=[sigma(68,l,8,a)*sigma(956,l,8,b)/alpha for l in ls+[8]]
    check('positive_actual_scales',alpha>0 and min(scales)>0 and scales[-1]==1)
    def wentry(l,m):
        ll,mm=sorted([l,m])
        return norms[68,l][a]*norms[956,l][b]*sum(
            gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*entries[ll,mm,i,j]
            for i,j in it.product(range(ll+1),repeat=2))
    W=[[wentry(l,m) for m in ls+[8]] for l in ls+[8]]
    # This mode is nonconstant, so its anchor correction is exactly zero.
    check('nonconstant_full_anchor',worst!=0 and r['raw_anchor']==0)
    for i,j in it.product(range(4),repeat=2):
        check('actual_weighted_congruence_'+str((i,j)),W[i][j]==alpha*scales[i]*block[i][j]*scales[j]
              and W[i][j]==W[j][i])
    wvector=[v/s for v,s in zip(vector,scales)]
    wvalue=dot(wvector,[dot(row,wvector) for row in W])
    check('actual_weighted_negative_vector',wvalue==alpha*value==r['weighted_remainder']<0
          and wvector[-1]==1 and F(source['rows'][worst]['multiplicity'])>0)
    affine_x=[dot([F(*v) for v in row],t) for row in source_affine['modes'][worst]['inverse_affine']]
    affine_v=[-v for v in affine_x]+[F(1)]
    check('second_full_range_vector', [dot(row,affine_x) for row in r['base']]==r['cross']
          and enc(affine_v)==fresh['load_bearing_vector']
          and dot(affine_v,[dot(row,affine_v) for row in block])==value)
    affine_w=[v/s for v,s in zip(affine_v,scales)]
    ac=fresh['actual_congruence']
    multiplicity=(c(68,a)-c(68,a-1))*(c(956,b)-c(956,b-1))
    check('all_saved_weighted_evidence', enc(W)==ac['weighted_block']
          and enc(affine_w)==ac['weighted_vector'] and enc(alpha)==ac['alpha']
          and enc(scales)==ac['scales'] and multiplicity==ac['multiplicity']==6550452053781
          and dot(affine_w,[dot(row,affine_w) for row in W])==wvalue==F(*ac['weighted_quadratic_value']))
    check('manuscript_exact_transport_constants',alpha==F(76721335004160,97169059)
          and scales==[1,1,1,1] and D==c(68,8)*c(946,3))
    check('old_block_rank_one_singular',det(r['base'])==0
          and any(v for row in r['base'] for v in row)
          and all(det([[r['base'][i][j] for j in js] for i in inds])==0
                  for inds in it.combinations(range(3),2) for js in it.combinations(range(3),2)))
    manuscript=(NB/'lemmas/L095-l094-witness-fails-complementary-modes.md').read_text()
    failtext=manuscript.split('indices are\n\n',1)[1].split('\n\n',1)[0]
    jtext=manuscript.split('Its exact complement is\n\n',1)[1].split('\n\n',1)[0]
    check('manuscript_all_indices',[int(x) for x in re.findall(r'\d+',failtext)]==negative
          and [int(x) for x in re.findall(r'\d+',jtext)]==remaining)
    check('strict_manuscript_interval',F(-1055859074499109,10**6)<=r['scaled_slack']<F(-1055859074499108,10**6)<0)
    check('all_45_retained_counts',sum(rows[i]['scaled_slack']>0 for i in tested)==14
          and sum(rows[i]['scaled_slack']==0 for i in tested)==31 and rows[23]['scaled_slack']==0
          and F(153320960)<=rows[31]['scaled_slack']<F(153320961))
    report.update(rows=rows,negative_indices=negative,positive_indices=positive,
                  offending_block={'block':block,'vector':vector,'quadratic_value':value,
                    'alpha':alpha,'scales':scales,'multiplicity':multiplicity,'weighted_block':W,'weighted_vector':wvector,
                    'affine_vector':affine_v,'affine_weighted_vector':affine_w,
                    'weighted_quadratic_value':wvalue},
                  manuscript_minimum=r['scaled_slack'])
    report['summary']={'verdict':'RETAINED_CONDITIONAL_REJECTION' if not failures else 'FAILED',
        'checks':len(checks),'failures':len(failures),'source_checks':len(source['checks']),
        'verifier_checks':len(fresh['checks']),'remaining_negative':len(negative),'remaining_positive':len(positive),
        'original_raw_weighted_identities':81,'selected_equalities':28,'zero_block_modes':43,'retained_modes':45,
        'minimum_mode':[0,5],'minimum_interval':[-1055859074499109,-1055859074499108,10**6],
        'required_minimum':0,'full_negative_block_dimension':4,
        'ancestor_contracts':'IMPORTED_WITH_EXISTING_QUALIFICATIONS','rs_boundary':[955,957]}
    save('completed')
    print('Summary:',report['summary'],flush=True)
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB),flush=True)
    if failures: raise SystemExit(1)


if __name__=='__main__':
    main()

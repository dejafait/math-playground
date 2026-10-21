"""Conditional L091 audit; no optimization or change of witness.

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

import critical_audit_affine_sign_remaining_modes as reconstruction
import verify_zero_old_block_witness_remaining_modes as verification
from critical_audit_simultaneous_eight_shell import c, dot, enc
from verify_simultaneous_eight_shell import beta, det, cramer

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'zero-old-block-remaining-modes-critical-audit.json'


def dec(m):
    return [[F(*v) for v in row] for row in m]


def main():
    reconstruction.OUT = ROOT/'zero-old-block-remaining-modes-critical-source.json'
    reconstruction.main()
    verification.OUT = ROOT/'zero-old-block-remaining-modes-critical-verification.json'
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

    source = read(reconstruction.OUT.name)
    fresh = read(verification.OUT.name)
    data = read('fixed-column-zero-old-block-results.json')
    result = read('zero-old-block-witness-remaining-modes-results.json')
    savedver = read('zero-old-block-witness-remaining-modes-verification.json')
    source_affine = read('fully-cancelling-separator-family-critical-audit.json')
    manuscript_check = read('zero-old-block-witness-remaining-modes-manuscript-check.json')
    for key in ['rows', 'negative_indices', 'positive_indices', 'zero_indices',
                'load_bearing_81_terms', 'load_bearing_block', 'load_bearing_vector',
                'load_bearing_scaled', 'load_bearing_raw', 'summary']:
        check('entire_step330_verifier_'+key, fresh[key] == savedver[key])
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

    # Read full relevant prior arrays. Schema aliases are explicit, never truncation.
    prior_names = [prefix+suffix+'.json' for prefix, suffixes in [
        ('fixed-column-new-only', ['-results', '-original-reconstruction', '-verification',
          '-critical-source', '-critical-verification', '-critical-audit']),
        ('new-only-witness-mixed-modes', ['-results', '-verification', '-critical-source',
          '-critical-verification', '-critical-audit']),
        ('fixed-column-zero-old-block', ['-original-reconstruction', '-verification',
          '-critical-source', '-critical-verification', '-critical-audit'])]
        for suffix in suffixes]
    prior = {name: read(name) for name in prior_names}
    for name, obj in prior.items():
        for field in ['records', 'kernel_residuals', 'domain_factors', 'point']:
            if field in obj:
                check('prior_full_'+name+'_'+field, obj[field] == source[field])
        if 'rows' in obj:
            check('prior_length_'+name, len(obj['rows']) == 81)
            for i, row in enumerate(obj['rows']):
                for field in ['base', 'cross', 'original_row', 'raw_beta', 'forced_raw',
                              'raw_anchor', 'energy', 'bound']:
                    if field in row:
                        check('prior_coefficient_'+str((name,i,field)), row[field] == source['rows'][i][field])
                alias = next(f for f in ['norm', 'raw_norm', 'positive_raw_normalization'] if f in row)
                check('prior_scale_'+str((name,i)), row[alias] == source['rows'][i]['norm'])
    schema = read('zero-old-block-witness-remaining-modes-verifier-schema-failure.json', False)
    check('preserved_scale_exception', schema['exception'] == "KeyError: 'raw_norm'"
          and schema['stage'] == 'added_prior_array_comparison_before_residual_substitution'
          and schema['new_solve_runs'] == 0 and schema['witness_changed'] is False
          and schema['mathematical_verdict_from_failed_wrapper'] is None)
    report['preserved_schema_exception'] = schema
    # Freeze the old completed L088 rows as regression evidence, not the new witness.
    oldw = prior['fixed-column-new-only-results.json']['witness']
    oldz = [F(*v) for v in oldw['z']]
    oldraw = [F(*v) for v in oldw['raw_moments']]
    oldresult = prior['new-only-witness-mixed-modes-results.json']
    for name in ['new-only-witness-mixed-modes-verification.json',
                 'new-only-witness-mixed-modes-critical-verification.json',
                 'new-only-witness-mixed-modes-critical-audit.json']:
        for i,row in enumerate(prior[name]['rows']):
            check('old_complete_residuals_'+str((name,i)), all(row[k] == oldresult['rows'][i][k]
                  for k in ['scaled_slack','raw_remainder']))

    selected = [9*a+b for a in range(7) for b in range(4)]
    retained = [i for i,r in enumerate(source['rows']) if all(F(*v)==0 for row in r['base'] for v in row)]
    remaining = sorted(set(range(81))-set(selected)-set(retained))
    check('full_partition', selected == result['selected'] == data['selected_modes']
          and retained == result['zero_old_block'] == data['zero_old_block_modes']
          and remaining == result['remaining'] and len(remaining) == 30 and len(retained) == 43
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
    rows = []
    for idx,s in enumerate(source['rows']):
        a,b = divmod(idx,9); B = dec(s['base']); cv = [F(*v) for v in s['cross']]
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
              and weighted_diagonal==(N/D)*diagonal and energy==F(*s['energy']))
        saved = result['rows'][idx]
        for key,value in [('base',B),('cross',cv),('fresh_inverse',x),('norm',norm),
                          ('energy',energy),('raw_anchor',anchor),('scaled_slack',slack),('raw_remainder',rawvalue)]:
            check('current_complete_'+str((idx,key)), enc(value)==saved[key])
        check('current_verifier_'+str(idx), enc(slack)==fresh['rows'][idx]['scaled_slack']
              and enc(rawvalue)==fresh['rows'][idx]['raw_remainder'])
        oldslack=F(*s['bound'])-dot(A,oldz)
        oldvalue=dot([F(*v) for v in s['forced_raw']],t)-anchor-energy+dot([F(*v) for v in s['raw_beta']],oldraw)
        check('old_witness_regression_'+str(idx), enc(oldslack)==oldresult['rows'][idx]['scaled_slack']
              and enc(oldvalue)==oldresult['rows'][idx]['raw_remainder'] and oldvalue==norm*oldslack)
        if idx in selected: check('retained_equality_'+str(idx), slack==rawvalue==0)
        if idx in retained:
            j=retained.index(idx)
            check('retained_zero_block_'+str(idx), not any(cv) and energy==anchor==0 and slack>=0
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
    check('complete_14_16_signs',negative==[6,15,23,25,31,32,34,42,49,50,52,60,67,68]
          and negative==result['negative_indices']==fresh['negative_indices'] and len(positive)==16)
    check('all_retained_sign_counts',sum(v>0 for v in z)==35 and sum(v==0 for v in z)==10
          and min(raw)==min(z)==0 and sum(rows[i]['scaled_slack']>0 for i in retained)==10
          and sum(rows[i]['scaled_slack']==0 for i in retained)==33)
    worst=min(remaining,key=lambda i:rows[i]['scaled_slack']); r=rows[worst]
    block=[row+[v] for row,v in zip(r['base'],r['cross'])]+[r['cross']+[r['diagonal']]]
    vector=[-v for v in r['inverse']]+[F(1)]
    value=dot(vector,[dot(row,vector) for row in block])
    off=result['offending_block']
    check('full_negative_block_vector',worst==31 and len(block)==len(vector)==4
          and all(len(row)==4 for row in block) and all(block[i][j]==block[j][i] for i,j in it.product(range(4),repeat=2))
          and enc(block)==off['block']==fresh['load_bearing_block'] and enc(vector)==off['vector']
          and value==r['raw_remainder']==F(*off['quadratic_value'])==F(*fresh['load_bearing_raw'])<0
          and r['diagonal']==F(*off['diagonal']))
    manuscript=(NB/'lemmas/L091-fixed-zero-old-block-witness-fails-remaining-modes.md').read_text()
    numerator=int(re.search(r'^N=(-?\d+)$',manuscript,re.M)[1])
    denominator=int(re.search(r'^Q=(\d+)$',manuscript,re.M)[1])
    check('complete_manuscript_N_Q',numerator==r['scaled_slack'].numerator
          and denominator==r['scaled_slack'].denominator and numerator<0<denominator)
    check('strict_manuscript_interval',F(-260419060753567,10**6)<=r['scaled_slack']<F(-260419060753566,10**6)<0)
    failtext=manuscript.split('The failing indices are\n\n',1)[1].split('\n\n',1)[0]
    jtext=manuscript.split('J={',1)[1].split('}.',1)[0]
    check('manuscript_all_indices',[int(x) for x in re.findall(r'\d+',failtext)]==negative
          and [int(x) for x in re.findall(r'\d+',jtext)]==remaining)
    report.update(rows=rows,negative_indices=negative,positive_indices=positive,
                  offending_block={'block':block,'vector':vector,'quadratic_value':value},
                  manuscript_rational=[numerator,denominator])
    report['summary']={'verdict':'RETAINED_CONDITIONAL_REJECTION' if not failures else 'FAILED',
        'checks':len(checks),'failures':len(failures),'source_checks':len(source['checks']),
        'verifier_checks':len(fresh['checks']),'remaining_negative':len(negative),'remaining_positive':len(positive),
        'original_raw_weighted_identities':81,'selected_equalities':28,'zero_block_modes':43,
        'minimum_mode':[3,4],'minimum_interval':[-260419060753567,-260419060753566,10**6],
        'required_minimum':0,'full_negative_block_dimension':4,
        'ancestor_contracts':'IMPORTED_WITH_EXISTING_QUALIFICATIONS','rs_boundary':[955,957]}
    save('completed')
    print('Summary:',report['summary'],flush=True)
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB),flush=True)
    if failures: raise SystemExit(1)


if __name__=='__main__':
    main()

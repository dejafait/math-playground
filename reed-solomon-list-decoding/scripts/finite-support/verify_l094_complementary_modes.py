"""Independent fixed-witness substitution using eigen coefficients and inverse action.

No constructor, solver, candidate change or dedicated critical audit is invoked.
"""
import hashlib
import itertools as it
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'l094-complementary-modes-verification.json'


def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b)),F(0))


def main():
    names = ['two-mixed-row-results.json',
             'two-mixed-row-critical-verification.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'l094-complementary-modes-results.json']
    paths = [ROOT/n for n in names]
    data,old,src,result = [json.loads(p.read_text()) for p in paths]
    checks,failures = [],[]
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in paths+[Path(__file__)]}}
    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    for name,obj in zip(names,[data,old,src,result]):
        check('clean_'+name,not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    # Consume the complete relevant earlier arrays, preserving their different
    # witness residuals. Only the frozen columns and coefficient contracts agree.
    source = json.loads((ROOT/'two-mixed-row-critical-source.json').read_text())
    prior_names = ['two-mixed-row-original-reconstruction.json',
                   'two-mixed-row-critical-source.json']
    for name in prior_names:
        path=ROOT/name; obj=json.loads(path.read_text())
        report['input_hashes'][str(path.relative_to(NB))]=hashlib.sha256(path.read_bytes()).hexdigest()
        check('prior_clean_'+name,not obj['failures'])
        for field in ['point','records','kernel_residuals','domain_factors']:
            if field in obj:
                check('complete_prior_'+name+'_'+field,obj[field]==source[field])
        if 'rows' in obj:
            check('complete_prior_rows_'+name,len(obj['rows'])==81)
            for i,row in enumerate(obj['rows']):
                for field in ['original_row','raw_beta','bound','energy','base','cross','forced_raw','raw_anchor']:
                    if field in row:
                        check('prior_row_'+name+'_'+str(i)+'_'+field,row[field]==source['rows'][i][field])
                normfield=next(f for f in ['norm','raw_norm','positive_raw_normalization'] if f in row)
                check('prior_norm_'+name+'_'+str(i),row[normfield]==source['rows'][i]['norm'])
    p8 = F(16792471,1181138102168120460)
    t = [F(*v) for v in data['point']]
    z = [F(*v) for v in data['witness']['z']]
    raw = [F(*v) for v in data['witness']['raw_moments']]
    check('entire_immutable_witness',enc(t)==result['point'] and enc(z)==result['z']==old['witness']['z']
          and enc(raw)==result['raw_moments']==old['witness']['raw_moments'] and t[4]==F(*src['stationary_t78']))
    factors = [dot([F(*v) for v in r],t) for r in src['family']]
    check('85_domain_controls',len(factors)==85 and min(factors)>=0
          and enc(factors)==old['domain_factors']==result['domain_factors'])
    free = [(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    V = [C(8,r)*C(60,r)*C(8,q)*C(948,q) for r,q in free]
    check('45_sign_and_raw_controls',len(z)==len(raw)==45 and min(raw)==min(z)==0
          and raw==[p8*x/v for x,v in zip(z,V)] and all(v>0 for v in V))
    selected = [9*a+b for a in range(7) for b in range(4)]
    newonly = [i for i in range(81) if max(divmod(i,9))==8]
    retained = [i for i,m in enumerate(src['modes']) if all(F(*v)==0 for row in m['source_base'] for v in row)]
    tested = sorted(retained+[23,31])
    remaining = [i for i in range(81) if i not in set(selected+tested)]
    check('complete_partition',len(src['modes'])==len(result['rows'])==81
          and selected==result['selected'] and retained==result['zero_old_block']==data['zero_old_block_modes']
          and remaining==result['remaining'] and len(remaining)==28 and all(j not in selected+retained for j in [23,31])
          and tested==data['retained_modes']==result['retained'] and len(retained)==43
          and len(set(selected)&set(retained))==20 and set(newonly).issubset(retained)
          and sorted(set(selected+tested+remaining))==list(range(81)))
    def eigen(n,a,r):
        return F(sum((-1)**h*C(a,h)*C(8-a,r-h)*C(n-8-a,r-h) for h in range(r+1)))
    rows = []
    for idx,m in enumerate(src['modes']):
        a,b = divmod(idx,9)
        B = [[F(*v) for v in row] for row in m['source_base']]
        cv = [dot([F(*v) for v in row],t) for row in m['source_cross']]
        x = [dot([F(*v) for v in row],t) for row in m['inverse_affine']]
        residual = [dot(row,x)-v for row,v in zip(B,cv)]
        check('all_original_inverse_ranges_'+str(idx),residual==[0]*len(B))
        D = F(C(68-2*a,8-a)*C(956-2*b,8-b)); norm = p8*D
        e = [eigen(68,a,r)*eigen(956,b,q) for r,q in free]
        rawbeta = [F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        check('independent_beta_eigen_identity_'+str(idx),rawbeta==[D*v for v in e] and norm>0)
        A = [-v/vol for v,vol in zip(e,V)]
        forced = dot([F(*v) for v in m['forced']],t)
        anchor = p8*C(68,8)*C(956,8) if idx==0 else F(0)
        cost = dot(cv,x)
        bound = forced-anchor-cost/norm
        slack = bound-dot(A,z)
        rawvalue = norm*forced-norm*anchor+dot(rawbeta,raw)-cost
        saved = result['rows'][idx]
        check('original_row_and_full_anchor_'+str(idx),enc(A)==saved['original_row']==m['row']
              and enc(anchor)==m['anchor'] and enc(norm*anchor)==saved['raw_anchor']
              and enc(bound)==saved['bound'] and enc(cost)==saved['energy'])
        check('complete_original_raw_substitution_'+str(idx),rawvalue==norm*slack
              and enc(slack)==saved['scaled_slack'] and enc(rawvalue)==saved['raw_remainder'])
        if idx in selected:
            check('retained_equality_'+str(idx),slack==rawvalue==0)
        if idx in tested:
            j = tested.index(idx)
            check('retained_mode_'+str(idx),slack>=0
                  and (idx in [23,31] or (all(v==0 for row in B for v in row) and not any(cv) and anchor==cost==0))
                  and enc(slack)==data['witness']['original_slacks'][j]
                  and enc(rawvalue)==data['witness']['raw_slacks'][j])
        rows.append({'index':idx,'mode':[a,b],'range_residuals':residual,'bound':bound,'norm':norm,
                     'original_row':A,'scaled_slack':slack,'raw_remainder':rawvalue})
    negative = [i for i in remaining if rows[i]['scaled_slack']<0]
    positive = [i for i in remaining if rows[i]['scaled_slack']>0]
    zero = [i for i in remaining if rows[i]['scaled_slack']==0]
    check('complete_remaining_verdict',negative==result['negative_indices']
          and len(negative)+len(positive)+len(zero)==28)
    check('retained_counts',sum(rows[i]['scaled_slack']>0 for i in retained)==13
          and sum(rows[i]['scaled_slack']==0 for i in retained)==30
          and sum(rows[i]['scaled_slack']>0 for i in tested)==14
          and rows[23]['scaled_slack']==rows[23]['raw_remainder']==0
          and F(153320960)<=rows[31]['scaled_slack']<F(153320961)
          and sum(v>0 for v in z)==33 and sum(v==0 for v in z)==12)
    worst = min(remaining,key=lambda i:rows[i]['scaled_slack'])
    value = rows[worst]['scaled_slack']; lo = value.numerator*10**6//value.denominator
    check('exact_minimum_interval',worst==result['summary']['minimum_remaining_index']
          and [lo,lo+1]==result['summary']['minimum_interval_numerators']
          and F(lo,10**6)<=value<F(lo+1,10**6))
    # Complete diagonal sum, retaining every one of the 81 actual orbit values.
    idx = worst; a,b = divmod(idx,9); terms = []
    free_values = {(8-r,8-q):v for (r,q),v in zip(free,raw)}
    for record in result['records'][-81:]:
        l,m,i,j = record['type']
        check('diagonal_type_'+str((i,j)),l==m==8)
        Y = free_values[i,j] if record['affine'] is None else dot([F(*v) for v in record['affine']],t)
        terms.append(F(beta(68,8,8,a,i)*beta(956,8,8,b,j))*Y)
    mode=src['modes'][idx]
    B=[[F(*v) for v in row] for row in mode['source_base']]
    cross=[dot([F(*v) for v in row],t) for row in mode['source_cross']]
    inverse=[dot([F(*v) for v in row],t) for row in mode['inverse_affine']]
    anchor = p8*p8*C(68,8)**2*C(956,8)**2 if idx==0 else F(0)
    diagonal = sum(terms,F(0))-anchor
    block = [row+[v] for row,v in zip(B,cross)]+[cross+[diagonal]]
    vector=[-v for v in inverse]+[F(1)]
    qvalue=dot(vector,[dot(row,vector) for row in block])
    check('complete_81_term_schur_value',len(terms)==81
          and qvalue==diagonal-dot(cross,inverse)==rows[idx]['raw_remainder'])
    if negative:
        saved=result['offending_block']
        savedvector=[F(*v) for v in saved['vector']]
        check('explicit_negative_block',any(v!=0 for row in B for v in row)
              and idx==saved['index'] and enc(block)==saved['block']
              and qvalue==F(*saved['quadratic_value'])<0
              and dot(savedvector,[dot(row,savedvector) for row in block])==qvalue)
    # Direct subset-transition realization of the entire offending block.
    # These complete source arrays were independently audited at the same columns.
    gamma = {(tr['indices'][0],tr['indices'][1],tr['indices'][2],v['degree'],tr['indices'][3]): F(*v['coefficient'])
             for tr in source['transitions'] for v in tr['actions']}
    norms = {(r['n'],r['layer']): [F(*v) for v in r['norms']] for r in source['factors']}
    entries = {tuple(r['type']): (None if r['affine'] is None else dot([F(*v) for v in r['affine']],t))
               for r in source['records']}
    for (r,q),v in zip(free,raw):
        entries[8,8,8-r,8-q] = v
    ls = result['rows'][idx]['layers']
    D = F(C(68-2*a,8-a)*C(956-2*b,8-b))
    N = norms[68,8][a]*norms[956,8][b]
    alpha = N/D
    def sigma(n,l,m,degree):
        ratios = []
        for k in range(min(l,m)+1):
            be = beta(n,l,m,degree,k)
            action = gamma[n,l,m,degree,k]
            if be:
                ratios.append(norms[n,l][degree]*action/be)
            else:
                check('zero_beta_action_'+str((n,l,m,degree,k)),action==0)
        check('positive_constant_ratio_'+str((n,l,m,degree)),bool(ratios) and min(ratios)>0
              and all(v==ratios[0] for v in ratios))
        return ratios[0]
    scales = [sigma(68,l,8,a)*sigma(956,l,8,b)/alpha for l in ls+[8]]
    check('positive_actual_scales',alpha>0 and min(scales)>0 and scales[-1]==1)
    def weighted_entry(l,m):
        ll,mm = sorted([l,m])
        return norms[68,l][a]*norms[956,l][b]*sum(
            gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*entries[ll,mm,i,j]
            for i,j in it.product(range(ll+1),repeat=2))
    weighted_block = [[weighted_entry(l,m) for m in ls+[8]] for l in ls+[8]]
    check('nonconstant_full_anchor',idx!=0 and anchor==0)
    for i,j in it.product(range(len(block)),repeat=2):
        check('actual_weighted_congruence_'+str((i,j)),
              weighted_block[i][j]==alpha*scales[i]*block[i][j]*scales[j]
              and weighted_block[i][j]==weighted_block[j][i])
    weighted_vector = [v/s for v,s in zip(vector,scales)]
    weighted_value = dot(weighted_vector,[dot(row,weighted_vector) for row in weighted_block])
    multiplicity = (C(68,a)-C(68,a-1))*(C(956,b)-C(956,b-1))
    check('transported_quadratic_identity',weighted_value==alpha*qvalue
          and multiplicity>0 and weighted_vector[-1]==1)
    if negative:
        check('transported_strict_negative_vector',weighted_value<0)
    report.update(actual_congruence={'alpha':alpha,'scales':scales,'multiplicity':multiplicity,
                  'weighted_block':weighted_block,'weighted_vector':weighted_vector,
                  'weighted_quadratic_value':weighted_value})
    report.update(rows=rows,negative_indices=negative,positive_indices=positive,zero_indices=zero,
                  load_bearing_81_terms=terms,load_bearing_block=block,load_bearing_vector=vector,
                  load_bearing_scaled=value,load_bearing_raw=qvalue,checks=checks,failures=failures)
    report['summary'] = {'verdict':('VERIFIED_FIXED_WITNESS_REJECTION' if negative else 'VERIFIED_FIXED_WITNESS_PASS') if not failures else 'FAILED',
                         'checks':len(checks),'failures':len(failures),'remaining_negative':len(negative),
                         'remaining_positive':len(positive),'remaining_zero':len(zero),
                         'selected_equalities':28,'zero_old_block_modes':43,'retained_modes':45,'retained_mode_positive':14,'retained_mode_zero':31,'original_raw_identities':81,
                         'minimum_mode':[a,b],'minimum_interval_numerators':[lo,lo+1],
                         'minimum_interval_denominator':10**6,'required_lower_bound':0,'rs_boundary':[955,957]}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print('Verdict:',report['summary']['verdict'],'; checks:',len(checks),'; failures:',failures)
    print('Remaining signs:',len(negative),'negative,',len(positive),'positive,',len(zero),'zero; minimum in [',lo,',',lo+1,') / 10^6; required >= 0; mode:',[a,b])
    print('Full original/raw substitution certificate:',OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()

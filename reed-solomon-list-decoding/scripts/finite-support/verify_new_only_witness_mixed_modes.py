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
OUT = ROOT/'new-only-witness-mixed-modes-verification.json'


def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b)),F(0))


def main():
    names = ['fixed-column-new-only-results.json',
             'fixed-column-new-only-critical-verification.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'new-only-witness-mixed-modes-results.json']
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
    mixed = [i for i in range(81) if i not in selected+newonly]
    check('complete_partition',len(src['modes'])==len(result['rows'])==81
          and selected==result['selected'] and newonly==result['new_only'] and mixed==result['mixed']
          and list(map(len,[selected,newonly,mixed]))==[28,17,36]
          and sorted(selected+newonly+mixed)==list(range(81)))
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
        if idx in newonly:
            j = newonly.index(idx)
            check('retained_new_only_'+str(idx),slack>=0 and B==[] and anchor==cost==0
                  and enc(slack)==data['witness']['original_slacks'][j]
                  and enc(rawvalue)==data['witness']['raw_slacks'][j])
        rows.append({'index':idx,'mode':[a,b],'range_residuals':residual,'bound':bound,'norm':norm,
                     'original_row':A,'scaled_slack':slack,'raw_remainder':rawvalue})
    negative = [i for i in mixed if rows[i]['scaled_slack']<0]
    positive = [i for i in mixed if rows[i]['scaled_slack']>0]
    zero = [i for i in mixed if rows[i]['scaled_slack']==0]
    check('complete_mixed_verdict',negative==result['negative_indices']
          and len(negative)==16 and len(positive)==20 and not zero)
    worst = min(mixed,key=lambda i:rows[i]['scaled_slack'])
    value = rows[worst]['scaled_slack']; lo = value.numerator*10**6//value.denominator
    check('exact_minimum_interval',worst==64 and [lo,lo+1]==result['summary']['minimum_interval_numerators']
          and F(lo,10**6)<=value<F(lo+1,10**6)<0)
    # An independent full diagonal sum at a zero old block: no inverse cost.
    idx = 66; a,b = divmod(idx,9); terms = []
    free_values = {(8-r,8-q):v for (r,q),v in zip(free,raw)}
    for record in result['records'][-81:]:
        l,m,i,j = record['type']
        check('diagonal_type_'+str((i,j)),l==m==8)
        Y = free_values[i,j] if record['affine'] is None else dot([F(*v) for v in record['affine']],t)
        terms.append(F(beta(68,8,8,a,i)*beta(956,8,8,b,j))*Y)
    check('load_bearing_zero_old_block',src['modes'][idx]['source_base']==[[[0,1]]]
          and not any(dot([F(*v) for v in r],t) for r in src['modes'][idx]['source_cross'])
          and result['rows'][idx]['energy']==[0,1] and result['rows'][idx]['raw_anchor']==[0,1])
    check('complete_81_term_negative_diagonal',len(terms)==81 and sum(terms,F(0))==rows[idx]['raw_remainder']<0
          and rows[idx]['norm']==F(1782682793617737,363922042337))
    selected_value = rows[idx]['scaled_slack']
    selected_floor = selected_value.numerator*10**12//selected_value.denominator
    lemma = NB/'lemmas/L089-fixed-new-only-witness-fails-mixed-modes.md'
    if lemma.exists():
        text = lemma.read_text()
        numerator = int(re.search(r'^N=(-?\d+)$',text,re.M).group(1))
        denominator = int(re.search(r'^Q=(\d+)$',text,re.M).group(1))
        check('entire_manuscript_rational',denominator>0 and F(numerator,denominator)==selected_value<0)
    report.update(rows=rows,negative_indices=negative,positive_indices=positive,zero_indices=zero,
                  load_bearing_81_terms=terms,load_bearing_scaled=selected_value,
                  load_bearing_raw=rows[idx]['raw_remainder'],checks=checks,failures=failures)
    report['summary'] = {'verdict':'VERIFIED_FIXED_WITNESS_REJECTION' if not failures else 'FAILED',
                         'checks':len(checks),'failures':len(failures),'mixed_negative':16,'mixed_positive':20,
                         'mixed_zero':0,'selected_equalities':28,'new_only_modes':17,'original_raw_identities':81,
                         'minimum_mode':[7,1],'minimum_interval_numerators':[lo,lo+1],
                         'minimum_interval_denominator':10**6,'required_lower_bound':0,'rs_boundary':[955,957]}
    report['summary'].update(load_bearing_mode=[7,3],load_bearing_norm=rows[idx]['norm'],
                             load_bearing_interval_numerators=[selected_floor,selected_floor+1],
                             load_bearing_interval_denominator=10**12)
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print('Verdict:',report['summary']['verdict'],'; checks:',len(checks),'; failures:',failures)
    print('Mixed signs: 16 negative, 20 positive; mode (7,1) in [',lo,',',lo+1,') / 10^6; required >= 0')
    print('Full original/raw substitution certificate:',OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()

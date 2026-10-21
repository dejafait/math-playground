"""Independent point substitution from ancestral original/raw mode data.

No constructor or optimizer invocation. Does not replace later critical review.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'affine-sign-remaining-modes-verification.json'


def dot(x,y):
    assert len(x)==len(y)
    return sum((v*w for v,w in zip(x,y)),F(0))


def main():
    names = ['affine-sign-phase-one-results.json',
             'affine-sign-critical-original-verification.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'affine-sign-remaining-modes-results.json']
    paths = [ROOT/n for n in names]
    data, old, src, result = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    for name,obj in zip(names,[data,old,src,result]):
        check('clean_'+name,not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    p8 = F(16792471,1181138102168120460)
    w = [F(*v) for v in data['witness']['original']]
    t = w[:4]+[F(*src['stationary_t78'])]
    raw = [F(*v) for v in data['witness']['raw_moments']]
    check('unchanged_point',enc(w)==old['original_point']==result['original_witness'] and enc(t)==result['point'])
    factors = [dot([F(*v) for v in row],t) for row in src['family']]
    check('domain_control',min(factors)>=0 and enc(factors)==old['domain_values']==result['domain_factors'])
    free = [(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    V = [C(8,r)*C(60,r)*C(8,q)*C(948,q) for r,q in free]
    check('raw_scaling_and_signs',raw==[p8*z/v for z,v in zip(w[4:],V)] and min(raw)>=0 and min(w[4:])>=0)
    selected = {9*a+b for a in range(7) for b in range(4)}
    check('complete_mode_records',len(src['modes'])==len(result['rows'])==81 and result['remaining_modes']==[i for i in range(81) if i not in selected])
    out = []
    for idx,m in enumerate(src['modes']):
        a,b = divmod(idx,9)
        B = [[F(*v) for v in r] for r in m['source_base']]
        cross = [dot([F(*v) for v in r],t) for r in m['source_cross']]
        inverse = [dot([F(*v) for v in r],t) for r in m['inverse_affine']]
        residual = [dot(r,inverse)-v for r,v in zip(B,cross)]
        check('full_original_range_'+str(idx),residual==[0]*len(B))
        D = F(C(68-2*a,8-a)*C(956-2*b,8-b))
        norm = p8*D
        coeff = [F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        fixed = dot([F(*v) for v in m['forced']],t)
        anchor = p8*C(68,8)*C(956,8) if idx==0 else F(0)
        cost = dot(cross,inverse)
        bound = fixed-anchor-cost/norm
        row = [-v/(D*vol) for v,vol in zip(coeff,V)]
        slack = bound-dot(row,w[4:])
        raw_value = norm*(fixed-anchor)+dot(coeff,raw)-cost
        saved = result['rows'][idx]
        check('original_source_and_normalization_'+str(idx),norm>0 and enc(anchor)==m['anchor']==saved['anchor'] and enc(row)==m['row']==saved['original_row'])
        check('entire_original_raw_residual_'+str(idx),enc(slack)==saved['scaled_slack'] and enc(raw_value)==saved['raw_Schur_remainder'] and raw_value==norm*slack and enc(bound)==saved['bound'] and enc(cost)==saved['energy'])
        if idx in selected:
            check('selected_zero_control_'+str(idx),slack==raw_value==0)
        out.append({'mode':[a,b],'index':idx,'scaled_slack':slack,'raw_remainder':raw_value,'inverse_residuals':residual})
    negative = [r['index'] for r in out if r['scaled_slack']<0]
    check('complete_negative_set',negative==result['negative_indices'] and len(negative)==19 and all(i not in selected for i in negative))
    # Exact source-free finite sum for one new-only block: no old inverse is needed.
    idx = 8
    check('load_bearing_new_only_mode_0_8',src['modes'][idx]['layers']==[] and out[idx]['scaled_slack']<0 and out[idx]['raw_remainder']<0)
    value = out[idx]['scaled_slack']; scale=10**12
    floor = value.numerator*scale//value.denominator
    report.update(rows=out,negative_indices=negative,checks=checks,failures=failures)
    report['summary']={'verdict':'VERIFIED_FIXED_POINT_REJECTION' if not failures else 'FAILED',
                       'checks':len(checks),'failures':len(failures),'original_raw_rows':81,'remaining_negative':19,
                       'remaining_positive':34,'selected_zero':28,'load_bearing_mode':[0,8],
                       'load_bearing_scaled_interval_numerators':[floor,floor+1],'interval_denominator':scale,
                       'required_lower_bound':0,'rs_boundary':[955,957]}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print('Verdict:',report['summary']['verdict'],'; checks:',len(checks),'; failures:',failures)
    print('Mode (0,8) scaled slack in [',floor,',',floor+1,') /',scale,'; required lower bound: 0')
    print('Full original/raw evidence:',OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()

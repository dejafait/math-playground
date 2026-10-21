"""Exact unchanged L086 point test; no optimizer, scan, or retuning.

Reconstruct full keys and original beta blocks. Fresh principal solves and
direct raw Schur remainders are compared with the saved affine inverse and
quadratic bounds. Full rational evidence is saved; summaries stay bounded.
"""
import hashlib
import itertools as it
import json
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

from critical_audit_simultaneous_eight_shell import c, beta, dot, enc, solve

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'affine-sign-remaining-modes-results.json'


def dec(M):
    return [[F(*x) for x in r] for r in M]


def det(M):
    n = len(M)
    return sum(((-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
                * product(M[i][p[i]] for i in range(n))
                for p in it.permutations(range(n))), F(0))


def product(xs):
    v = F(1)
    for x in xs:
        v *= x
    return v


def main():
    names = ['affine-sign-phase-one-results.json',
             'affine-sign-phase-one-critical-audit.json',
             'affine-sign-critical-original-verification.json',
             'affine-sign-critical-ancestor-reconstruction.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'eight-distance-full-base-kernel-results.json',
             'maximizer-excluded-anchor-results.json']
    paths = [ROOT/n for n in names]
    data, audit, original, ancestor, src, col, base = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    report = {'input_hashes': {str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    def save(stage):
        report.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(report), indent=2)+'\n')
    for name, obj in zip(names, [data,audit,original,ancestor,src,col,base]):
        check('clean_'+name, not obj['failures'])
        for rel, h in obj.get('input_hashes', {}).items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    p8 = F(16792471,1181138102168120460)
    s = F(*src['stationary_t78'])
    w = [F(*v) for v in data['witness']['original']]
    raw = [F(*v) for v in data['witness']['raw_moments']]
    check('immutable_audited_original_point', enc(w)==audit['original_point']==original['original_point'] and len(w)==49 and w[0]==1)
    check('immutable_audited_raw_point', enc(w[:4]+raw)==audit['raw_point']==original['raw_point'])
    point = w[:4]+[s]
    free = [(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    volumes = [F(c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
    check('positive_raw_scaling', p8>0 and min(volumes)>0 and raw==[p8*z/v for z,v in zip(w[4:],volumes)])
    check('45_original_and_raw_signs', min(raw)>=0 and min(w[4:])>=0)
    # Original four-parameter column from its RREF, without any new solve.
    rr = dec(col['equation_rref']); nonpiv = [56,63,69,78]
    family = [[F(0)]*5 for _ in range(85)]
    for j,k in enumerate(nonpiv):
        family[k][j+1] = F(1)
    for i,j in enumerate(col['equation_pivots']):
        family[j] = [rr[i][-1]]+[-rr[i][k] for k in nonpiv]
    check('original_RREF_family', enc(family)==src['family']==ancestor['family'])
    factors = [dot(r,point) for r in family]
    check('all_85_domain_rows', min(factors)>=0 and enc(factors)==data['witness']['domain_values']==original['domain_values'])
    pairs = [F(*v) for v in base['pairs_through_14']]
    check('original_rho_pairs_p8', enc(pairs)==col['pairs_through_14'] and pairs[8]==p8 and F(*base['rho'])>0)
    entries = {tuple(r['type']):[F(*r['y'])]+[F(0)]*4 for r in base['entries']}
    column = [[p8]+[F(0)]*4]
    for r in col['column'][1:]:
        v = [p8*x for x in family[r['variable']]] if r['kind']=='free' else [F(*r['value'])]+[F(0)]*4
        column.append(v)
        entries[r['orbit'][0],8,*r['orbit'][1:]] = v
    weights = [1]+[c(8,i)*c(60,l-i)*c(8,j)*c(948,l-j) for l,i,j in col['orbits'][1:]]
    kernel_residuals = []
    check('complete_150_and_90_dimensions', len(column)==len(weights)==150 and len(col['equations'])==len(col['kernel_basis'])==90)
    for i,(kr,row,rhs) in enumerate(zip(col['kernel_basis'],col['equations'],col['rhs'])):
        residual = [sum(F(*v)*W*f[j] for v,W,f in zip(kr,weights,column)) for j in range(5)]
        eq = [sum(F(*v)*f[j] for v,f in zip(row,family)) for j in range(5)]
        check('all_affine_kernel_and_original_equations_'+str(i),residual==[0]*5 and eq==[F(*rhs)]+[F(0)]*4)
        kernel_residuals.append(residual)
    check('complete_ancestor_column_and_kernel', enc(column)==src['affine_column'] and enc(kernel_residuals)==src['weighted_kernel_residuals']==ancestor['weighted_kernel_residuals'])
    # Exhaust all 500 types and all six presentations, including outside-layer reanchorings.
    records = []
    types = [(l,m,i,j) for l,m in it.combinations_with_replacement([5,6,7,8],2) for i,j in it.product(range(l+1),repeat=2)]
    check('complete_500_types', len(types)==len(src['records'])==500)
    for k,typ in enumerate(types):
        l,m,i,j = typ
        atoms = [956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
        presentations, values = [], []
        for order in it.permutations([2,1,0]):
            aa = [0]*8
            for mask,n in enumerate(atoms):
                dest = sum(((mask>>bit)&1)<<(2-h) for h,bit in enumerate(order))
                aa[dest] = n
            ds = [aa[4]+aa[5],aa[4]+aa[6],aa[2]+aa[6]]
            value = None
            if 0 in ds:
                value = [pairs[max(ds)]]+[F(0)]*4
            elif any(0<h<5 for h in ds):
                value = [F(0)]*5
            else:
                value = entries.get((*sorted(ds[:2]),aa[4],aa[3]))
            if value is not None:
                values.append(value)
            presentations.append({'atoms':aa,'distances':ds,'affine':value})
        value = values[0] if values else None
        key = min(v['atoms'] for v in presentations)
        check('all_six_presentations_'+str(k), all(v==value for v in values) and key==src['records'][k]['key'] and enc(value)==src['records'][k]['affine'] and list(typ)==src['records'][k]['type'])
        entries[typ] = value
        records.append({'type':typ,'key':key,'presentations':presentations,'affine':value})
    check('36_forced_45_distinct_free',sum(v is None for v in entries.values())==45 and all((entries[8,8,8-r,8-q] is None)==(r+q>=8) for r,q in it.product(range(9),repeat=2)) and len({tuple(records[-81+9*(8-r)+(8-q)]['key']) for r,q in free})==45)
    selected = [9*a+b for a in range(7) for b in range(4)]
    remaining = [i for i in range(81) if i not in selected]
    check('exact_partition_28_and_53', selected==data['selected_modes'] and len(remaining)==53 and sorted(selected+remaining)==list(range(81)))
    sizes = {l:c(68,l)*c(956,l) for l in [5,6,7,8]}
    rows = []
    report.update(point=point,original_witness=w,raw_moments=raw,domain_factors=factors,
                  selected_modes=selected,remaining_modes=remaining,records=records,kernel_residuals=kernel_residuals)
    save('point_keys_and_ranges_staged_before_residual_test')
    for idx in range(81):
        a,b = divmod(idx,9); ls = [l for l in [5,6,7] if l>=max(a,b)]
        D = F(c(68-2*a,8-a)*c(956-2*b,8-b)); norm = p8*D
        def source(l,m):
            ll,mm = sorted([l,m])
            v = [sum(beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j)*entries[ll,mm,i,j][k] for i,j in it.product(range(ll+1),repeat=2)) for k in range(5)]
            if idx==0:
                v[0] -= pairs[l]*pairs[m]*sizes[l]*sizes[m]
            return v
        B = [[source(l,m)[0] for m in ls] for l in ls]
        cross = [source(l,8) for l in ls]
        cv = [dot(r,point) for r in cross]
        saved = src['modes'][idx]
        check('all_original_source_entries_'+str(idx), enc(B)==saved['source_base'] and enc(cross)==saved['source_cross'] and list((a,b))==saved['mode'])
        check('both_rectangular_directions_'+str(idx),all(source(l,8)==source(8,l) for l in ls))
        inv = dec(saved['inverse_affine'])
        residuals = [[dot(row,coeff)-v for coeff,v in zip(zip(*inv),cr)] for row,cr in zip(B,cross)]
        check('every_affine_inverse_residual_'+str(idx), all(r==[0]*5 for r in residuals))
        xv_saved = [dot(r,point) for r in inv]
        # A fresh largest nonsingular principal solve, including singular and empty cases.
        minors = []
        chosen = ()
        for n in range(1,len(ls)+1):
            for inds in it.combinations(range(len(ls)),n):
                minor = det([[B[i][j] for j in inds] for i in inds])
                minors.append({'indices':inds,'determinant':minor})
                if minor:
                    chosen = inds
        check('old_PSD_principal_minors_'+str(idx),all(m['determinant']>=0 for m in minors))
        xv = [F(0)]*len(ls)
        if chosen:
            solution,_ = solve([[B[i][j] for j in chosen] for i in chosen],[cv[i] for i in chosen])
            for j,v in zip(chosen,solution):
                xv[j] = v
        direct_ranges = [dot(row,xv)-v for row,v in zip(B,cv)]
        check('every_point_inverse_range_'+str(idx),direct_ranges==[0]*len(ls) and [dot(row,xv_saved)-v for row,v in zip(B,cv)]==[0]*len(ls))
        energy = dot(cv,xv)
        check('fresh_and_saved_inverse_energy_'+str(idx),energy==dot(cv,xv_saved))
        forced_raw = [sum(beta(68,8,8,a,i)*beta(956,8,8,b,j)*v[k] for (l,m,i,j),v in entries.items() if l==m==8 and v is not None) for k in range(5)]
        forced = [v/norm for v in forced_raw]
        anchor = p8*sizes[8] if idx==0 else F(0)
        check('full_forced_anchor_contract_'+str(idx),enc(forced)==saved['forced'] and enc(anchor)==saved['anchor'] and D>0)
        bound = dot(forced,point)-anchor-energy/norm
        Q = dec(saved['quadratic'])
        check('complete_original_quadratic_bound_'+str(idx),bound==dot(point,[dot(r,point) for r in Q]))
        raw_beta = [F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        row = [-v/(D*V) for v,V in zip(raw_beta,volumes)]
        check('all_45_original_coefficients_'+str(idx),enc(row)==saved['row'])
        slack = bound-dot(row,w[4:])
        raw_anchor = p8*p8*sizes[8]*sizes[8] if idx==0 else F(0)
        raw_schur = dot(forced_raw,point)+dot(raw_beta,raw)-raw_anchor-energy
        check('positive_raw_anchor_scaling_'+str(idx),norm>0 and raw_anchor==norm*anchor)
        check('original_and_raw_Schur_agree_'+str(idx),raw_schur==norm*slack)
        if idx in selected:
            check('selected_equality_control_'+str(idx),slack==raw_schur==0)
        rows.append({'index':idx,'mode':[a,b],'selected':idx in selected,'layers':ls,
                     'base':B,'cross':cv,'fresh_inverse':xv,'saved_inverse':xv_saved,
                     'affine_inverse_residuals':residuals,'point_range_residuals':direct_ranges,
                     'minors':minors,'D':D,'positive_raw_normalization':norm,'raw_anchor':raw_anchor,
                     'forced_raw':forced_raw,'forced':dot(forced,point),'anchor':anchor,
                     'energy':energy,'bound':bound,'original_row':row,'raw_beta':raw_beta,
                     'scaled_slack':slack,'raw_Schur_remainder':raw_schur})
    negative = [r['index'] for r in rows if r['scaled_slack']<0]
    counts = Counter('negative' if r['scaled_slack']<0 else 'positive' if r['scaled_slack']>0 else 'zero' for r in rows if not r['selected'])
    worst = min(remaining,key=lambda i:rows[i]['scaled_slack'])
    minimum = rows[worst]['scaled_slack']
    scale = 10**6
    interval_floor = minimum.numerator*scale//minimum.denominator
    check('no_selected_failures', all(i in remaining for i in negative))
    report.update(rows=rows,negative_indices=negative,most_negative_index=worst)
    report['summary'] = {'verdict': 'RECONSTRUCTION_FAILED' if failures else 'FIXED_POINT_REJECTED' if negative else 'FIXED_POINT_PASSES_ALL_MODES',
                         'checks':len(checks),'failures':len(failures),'original_modes':81,'selected_zero_modes':28,
                         'remaining_modes':53,'remaining_counts':dict(counts),'negative_indices':negative,
                         'most_negative_mode':rows[worst]['mode'],'actual_minimum_scaled_slack':rows[worst]['scaled_slack'],
                         'minimum_interval_numerators':[interval_floor,interval_floor+1],'minimum_interval_denominator':scale,
                         'required_minimum':0,'raw_identities_checked':81,'old_minors':sum(len(r['minors']) for r in rows),
                         'ancestor_contracts':'IMPORTED_WITH_EXISTING_QUALIFICATIONS','rs_boundary':[955,957]}
    save('completed')
    print('Verdict:', report['summary']['verdict'],'; checks:',len(checks),'; failures:',failures)
    print('Remaining 53 signs:',dict(counts),'; negative original indices:',negative)
    print('Actual minimum scaled slack at mode',rows[worst]['mode'],'in [',interval_floor,',',interval_floor+1,') /',scale,'; required lower bound: 0')
    print('Full exact minimum: /rows/'+str(worst)+'/scaled_slack; full certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()

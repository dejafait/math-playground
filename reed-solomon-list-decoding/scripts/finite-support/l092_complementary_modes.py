"""One exact immutable L092 witness evaluation; no solver or retuning.

Rebuild original keys, beta rows, full-anchor costs and all ranges.
Compare complete L092 construction and separate audit evidence; save every original/raw remainder.
"""
import hashlib
import itertools as it
import json
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

from critical_audit_affine_sign_remaining_modes import cramer, det
from critical_audit_simultaneous_eight_shell import c, beta, dot, enc
from verify_simultaneous_eight_shell import beta as independent_beta

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'l092-complementary-modes-results.json'


def dec(M):
    return [[F(*v) for v in row] for row in M]


def main():
    names = ['zero-block-plus-3-4-results.json',
             'zero-block-plus-3-4-original-reconstruction.json',
             'zero-block-plus-3-4-verification.json',
             'zero-block-plus-3-4-critical-source.json',
             'zero-block-plus-3-4-critical-verification.json',
             'zero-block-plus-3-4-critical-audit.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'eight-distance-full-base-kernel-results.json',
             'maximizer-excluded-anchor-results.json',
             'affine-sign-phase-one-results.json']
    paths = [ROOT/n for n in names]
    objects = [json.loads(p.read_text()) for p in paths]
    data,recon,ver,source,fresh,audit,src,col,base,old = objects
    checks,failures = [],[]
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in paths+[Path(__file__)]}}

    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        report.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(report),indent=2)+'\n')

    for name,obj in zip(names,objects):
        check('clean_'+name,not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    for field in ['bounds','domain_factors','witness','summary']:
        check('entire_318_320_verification_'+field,ver[field]==fresh[field])
    p8 = F(16792471,1181138102168120460)
    point = [F(*v) for v in old['witness']['original'][:4]]+[F(*src['stationary_t78'])]
    z = [F(*v) for v in data['witness']['z']]
    raw = [F(*v) for v in data['witness']['raw_moments']]
    check('entire_immutable_witness',len(z)==len(raw)==45 and enc(z)==ver['witness']['z']
          and enc(raw)==ver['witness']['raw_moments'])
    check('immutable_original_columns',enc(point)==data['point']==recon['point']==source['point'])
    free = [(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    volumes = [F(c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
    check('all_positive_raw_scalings',p8>0 and min(volumes)>0
          and raw==[p8*v/V for v,V in zip(z,volumes)]
          and enc(volumes)==data['volumes'])
    check('retained_45_signs',min(z)==min(raw)==0
          and sum(v>0 for v in z)==35 and sum(v==0 for v in z)==10)
    rr = dec(col['equation_rref']); nonpiv = [56,63,69,78]
    family = [[F(0)]*5 for _ in range(85)]
    for j,k in enumerate(nonpiv):
        family[k][j+1] = F(1)
    for i,j in enumerate(col['equation_pivots']):
        family[j] = [rr[i][-1]]+[-rr[i][k] for k in nonpiv]
    factors = [dot(r,point) for r in family]
    check('original_85_domain_rows',enc(family)==src['family'] and len(factors)==85
          and min(factors)>=0 and enc(factors)==source['domain_factors']==recon['domain_factors']==ver['domain_factors'])
    pairs = [F(*v) for v in base['pairs_through_14']]
    check('rho_pairs_p8',F(*base['rho'])>0 and enc(pairs)==col['pairs_through_14'] and pairs[8]==p8)
    entries = {tuple(r['type']):[F(*r['y'])]+[F(0)]*4 for r in base['entries']}
    column = [[p8]+[F(0)]*4]
    for r in col['column'][1:]:
        value = [p8*x for x in family[r['variable']]] if r['kind']=='free' else [F(*r['value'])]+[F(0)]*4
        column.append(value)
        entries[r['orbit'][0],8,*r['orbit'][1:]] = value
    weights = [1]+[c(8,i)*c(60,l-i)*c(8,j)*c(948,l-j) for l,i,j in col['orbits'][1:]]
    check('full_150_90_dimensions',len(column)==len(weights)==150
          and len(col['kernel_basis'])==len(col['equations'])==90)
    kernel = []
    for i,(kr,row,rhs) in enumerate(zip(col['kernel_basis'],col['equations'],col['rhs'])):
        residual = [sum(F(*v)*W*f[j] for v,W,f in zip(kr,weights,column)) for j in range(5)]
        equation = [sum(F(*v)*f[j] for v,f in zip(row,family)) for j in range(5)]
        check('weighted_and_original_kernel_'+str(i),residual==[0]*5 and equation==[F(*rhs)]+[F(0)]*4)
        kernel.append(residual)
    check('entire_audited_affine_column',enc(column)==src['affine_column']
          and enc(kernel)==source['kernel_residuals']==recon['kernel_residuals'])
    records = []
    types = [(l,m,i,j) for l,m in it.combinations_with_replacement([5,6,7,8],2)
             for i,j in it.product(range(l+1),repeat=2)]
    check('complete_500_types',len(types)==500)
    for k,typ in enumerate(types):
        l,m,i,j = typ
        atoms = [956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
        presentations,values = [],[]
        for order in it.permutations([2,1,0]):
            aa = [0]*8
            for mask,n in enumerate(atoms):
                dest = sum(((mask>>bit)&1)<<(2-h) for h,bit in enumerate(order))
                aa[dest] = n
            ds = [aa[4]+aa[5],aa[4]+aa[6],aa[2]+aa[6]]
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
        check('six_presentations_'+str(k),all(v==value for v in values)
              and list(typ)==src['records'][k]['type'] and key==src['records'][k]['key']
              and enc(value)==src['records'][k]['affine'])
        entries[typ] = value
        records.append({'type':typ,'key':key,'presentations':presentations,'affine':value})
    check('complete_318_320_records',enc(records)==source['records']==recon['records'])
    check('36_forced_45_unique_free',sum(v is None for v in entries.values())==45
          and all((entries[8,8,8-r,8-q] is None)==(r+q>=8) for r,q in it.product(range(9),repeat=2))
          and len({tuple(records[-81+9*(8-r)+8-q]['key']) for r,q in free})==45)
    selected = [9*a+b for a in range(7) for b in range(4)]
    newonly = [i for i in range(81) if max(divmod(i,9))==8]
    retained = [i for i,m in enumerate(src['modes'])
                if all(F(*v)==0 for row in m['source_base'] for v in row)]
    tested = sorted(retained+[31])
    remaining = [i for i in range(81) if i not in set(selected+tested)]
    check('exact_28_44_29_partition',selected==data['selected_modes'] and newonly==data['new_only_modes']
          and retained==data['zero_old_block_modes'] and len(retained)==43
          and len(set(selected)&set(retained))==20 and len(remaining)==29 and 31 not in selected+retained and tested==data['retained_modes']
          and set(newonly).issubset(retained) and sorted(set(selected+tested+remaining))==list(range(81)))
    report.update(point=point,z=z,raw_moments=raw,free_indices=free,domain_factors=factors,
                  kernel_residuals=kernel,records=records,selected=selected,new_only=newonly,
                  zero_old_block=retained,retained=tested,remaining=remaining)
    save('frozen_contracts_saved_before_remaining_substitution')
    if failures: raise RuntimeError('Frozen input discrepancy; no residual sign verdict permitted')
    rows = []; sizes = {l:c(68,l)*c(956,l) for l in [5,6,7,8]}
    for idx in range(81):
        a,b = divmod(idx,9); ls = [l for l in [5,6,7] if l>=max(a,b)]
        D = F(c(68-2*a,8-a)*c(956-2*b,8-b)); norm = p8*D
        def source_entry(l,m):
            ll,mm = sorted([l,m])
            v = [sum(beta(68,l,m,a,i)*beta(956,l,m,b,j)*entries[ll,mm,i,j][k]
                     for i,j in it.product(range(ll+1),repeat=2)) for k in range(5)]
            if idx==0:
                v[0] -= pairs[l]*pairs[m]*sizes[l]*sizes[m]
            return v
        B = [[source_entry(l,m)[0] for m in ls] for l in ls]
        cross = [source_entry(l,8) for l in ls]; cv = [dot(r,point) for r in cross]
        inv = dec(src['modes'][idx]['inverse_affine'])
        ranges = [[dot(row,coeff)-v for coeff,v in zip(zip(*inv),cr)] for row,cr in zip(B,cross)]
        check('source_and_every_affine_range_'+str(idx),enc(B)==src['modes'][idx]['source_base']
              and enc(cross)==src['modes'][idx]['source_cross'] and all(r==[0]*5 for r in ranges)
              and all(source_entry(l,8)==source_entry(8,l) for l in ls))
        minors = []; chosen = ()
        for n in range(1,len(ls)+1):
            for inds in it.combinations(range(len(ls)),n):
                value = det([[B[i][j] for j in inds] for i in inds])
                minors.append({'indices':inds,'determinant':value})
                if value:
                    chosen = inds
        xv = [F(0)]*len(ls)
        if chosen:
            vals = cramer([[B[i][j] for j in chosen] for i in chosen],[cv[i] for i in chosen])
            for j,v in zip(chosen,vals):
                xv[j] = v
        saved = source['rows'][idx]; previous = recon['rows'][idx]
        energy = dot(cv,xv)
        check('fresh_principal_inverse_all_rows_'+str(idx),all(m['determinant']>=0 for m in minors)
              and [dot(row,xv)-v for row,v in zip(B,cv)]==[0]*len(ls)
              and energy==dot(cv,[dot(r,point) for r in inv])==F(*saved['energy'])
              and enc(B)==saved['base'] and enc(cv)==saved['cross'])
        forced = [sum(beta(68,8,8,a,i)*beta(956,8,8,b,j)*v[k]
                      for (l,m,i,j),v in entries.items() if l==m==8 and v is not None) for k in range(5)]
        anchor = p8*p8*sizes[8]*sizes[8] if idx==0 else F(0)
        coeff = [F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        coeff2 = [F(independent_beta(68,8,8,a,8-r)*independent_beta(956,8,8,b,8-q)) for r,q in free]
        A = [-v/(D*V) for v,V in zip(coeff,volumes)]
        bound = (dot(forced,point)-anchor-energy)/norm
        check('entire_318_320_original_raw_coefficients_'+str(idx),coeff==coeff2 and norm>0
              and enc(coeff)==saved['raw_beta']==previous['raw_beta']
              and enc(A)==saved['original_row']==previous['original_row']==src['modes'][idx]['row']
              and enc(forced)==saved['forced_raw'] and enc(anchor)==saved['raw_anchor']
              and enc(bound)==saved['bound']==previous['bound']==ver['bounds'][idx]['bound']
              and enc(norm)==saved['norm'] and bound==dot(point,[dot(r,point) for r in dec(src['modes'][idx]['quadratic'])]))
        slack = bound-dot(A,z)
        raw_remainder = dot(forced,point)+dot(coeff2,raw)-anchor-dot(cv,[dot(r,point) for r in inv])
        check('original_raw_identity_'+str(idx),raw_remainder==norm*slack)
        if idx in selected:
            check('retained_equality_'+str(idx),slack==raw_remainder==0)
        if idx in tested:
            j = tested.index(idx)
            check('retained_mode_'+str(idx),slack>=0
                  and (idx==31 or (all(v==0 for row in B for v in row) and not any(cv) and energy==anchor==0))
                  and enc(slack)==data['witness']['original_slacks'][j]
                  and enc(raw_remainder)==data['witness']['raw_slacks'][j])
        membership = data['membership'][idx]
        check('all_entrywise_membership_'+str(idx),membership['base']==enc(B)
              and membership['cross']==enc(cv) and membership['empty']==(not B)
              and membership['zero_old_block']==(idx in retained))
        rows.append({'index':idx,'mode':[a,b],'kind':'selected' if idx in selected else 'retained' if idx in tested else 'remaining',
                     'layers':ls,'base':B,'cross':cv,'fresh_inverse':xv,'affine_range_residuals':ranges,
                     'minors':minors,'D':D,'norm':norm,'forced_raw':forced,'raw_anchor':anchor,'energy':energy,
                     'original_row':A,'raw_beta':coeff,'bound':bound,'scaled_slack':slack,'raw_remainder':raw_remainder})
    negative = [i for i in remaining if rows[i]['scaled_slack']<0]
    counts = Counter('negative' if rows[i]['scaled_slack']<0 else 'positive' if rows[i]['scaled_slack']>0 else 'zero' for i in remaining)
    worst = min(remaining,key=lambda i:rows[i]['scaled_slack'])
    v = rows[worst]['scaled_slack']; scale = 10**6; lo = v.numerator*scale//v.denominator
    check('retained_counts',sum(rows[i]['scaled_slack']>0 for i in retained)==11
          and sum(rows[i]['scaled_slack']==0 for i in retained)==32
          and sum(rows[i]['scaled_slack']>0 for i in tested)==11
          and rows[31]['scaled_slack']==rows[31]['raw_remainder']==0)
    check('all_306_old_minors',sum(len(r['minors']) for r in rows)==306)
    report.update(rows=rows,negative_indices=negative,
                  failing_remainders=[{'index':i,'mode':rows[i]['mode'],'scaled_slack':rows[i]['scaled_slack'],
                                       'raw_remainder':rows[i]['raw_remainder']} for i in negative])
    if negative:
        r = rows[worst]; B = r['base']; cv = r['cross']; x = r['fresh_inverse']
        diagonal = dot(r['forced_raw'],point)+dot(r['raw_beta'],raw)-r['raw_anchor']
        block = [row+[v] for row,v in zip(B,cv)]+[cv+[diagonal]]
        vector = [-v for v in x]+[F(1)]
        value = dot(vector,[dot(row,vector) for row in block])
        check('explicit_negative_source_block',value==r['raw_remainder']<0
              and diagonal-r['energy']==value and all(block[i][j]==block[j][i]
                  for i in range(len(block)) for j in range(len(block))))
        report['offending_block'] = {'index':worst,'mode':r['mode'],'block':block,
                                    'vector':vector,'quadratic_value':value,'diagonal':diagonal}
    report['summary'] = {'verdict':'RECONSTRUCTION_FAILED' if failures else 'FIXED_WITNESS_REJECTED' if negative else 'FIXED_WITNESS_PASSES_ALL_81_MODES',
                         'checks':len(checks),'failures':len(failures),'remaining_counts':dict(counts),'negative_indices':negative,
                         'minimum_remaining_index':worst,'minimum_remaining_mode':rows[worst]['mode'],
                         'minimum_interval_numerators':[lo,lo+1],'minimum_interval_denominator':scale,
                         'required_lower_bound':0,'original_raw_identities':81,'old_minors':306,
                         'retained_equalities':28,'zero_old_block_positive':11,'zero_old_block_zero':32,'retained_modes':44,'retained_mode_positive':11,'retained_mode_zero':33,
                         'positive_moments':35,'zero_moments':10,'rs_boundary':[955,957],
                         'ancestor_contracts':'IMPORTED_WITH_EXISTING_QUALIFICATIONS'}
    save('completed')
    print('Verdict:',report['summary']['verdict'],'; checks:',len(checks),'; failures:',failures)
    print('Remaining signs:',dict(counts),'; negative indices:',negative)
    print('Actual minimum remaining slack in [',lo,',',lo+1,') /',scale,'; required >= 0; mode:',rows[worst]['mode'])
    print('Full exact failing original/raw remainders: /failing_remainders; certificate:',OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()

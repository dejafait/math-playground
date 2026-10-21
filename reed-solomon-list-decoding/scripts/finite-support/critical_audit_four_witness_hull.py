"""Conditional audit of L096; no constructor, optimizer or new hull search.

Reconstruct the fixed source using the existing independent recipe checker,
then audit all four complete inputs and every original/raw/weighted mode.
"""
import hashlib
import itertools as it
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path
import critical_audit_affine_sign_remaining_modes as source_audit
import verify_four_witness_hull as verifier
from critical_audit_simultaneous_eight_shell import c, enc, dot

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'four-witness-hull-critical-audit.json'


def main():
    source_path=ROOT/'four-witness-hull-critical-source.json'
    verify_path=ROOT/'four-witness-hull-critical-verification.json'
    if any(p.exists() for p in [OUT,source_path,verify_path]):
        raise RuntimeError('Preserve existing audit evidence; choose fresh output paths')
    source_audit.OUT=source_path
    source_audit.main()
    verifier.OUT=verify_path
    verifier.main()
    checks,failures=[],[]
    report={'input_hashes':{}}
    def check(name,ok):
        checks.append(name)
        if not ok:failures.append(name)
    def read(name,clean=True):
        path=ROOT/name
        data=json.loads(path.read_text())
        report['input_hashes'][str(path.relative_to(NB))]=hashlib.sha256(path.read_bytes()).hexdigest()
        if clean:check('clean_'+name,not data.get('failures',[]))
        # The preserved failure's implementation hash changed during its repair;
        # compare its mathematical arrays below, without treating it as clean.
        if clean:
            for rel,h in data.get('input_hashes',{}).items():
                check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
        return data
    def save(stage):
        report.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    data=read('four-witness-hull-results.json')
    savedver=read('four-witness-hull-verification.json')
    fresh=read(verify_path.name)
    src=read(source_path.name)
    oldsource=read('two-mixed-row-critical-source.json')
    recon=read('two-mixed-row-original-reconstruction.json')
    col=read('eight-distance-full-base-kernel-results.json')
    family=read('fully-cancelling-separator-family-critical-audit.json')
    old=read('affine-sign-phase-one-results.json')
    names=['fixed-column-new-only-results.json','fixed-column-zero-old-block-results.json',
           'zero-block-plus-3-4-results.json','two-mixed-row-results.json']
    vertices=[read(n) for n in names]
    for path in [Path(__file__),Path(source_audit.__file__),Path(verifier.__file__)]:
        report['input_hashes'][str(path.relative_to(NB))]=hashlib.sha256(path.read_bytes()).hexdigest()
    check('entire_verification_reproduced',all(savedver[k]==fresh[k] for k in ['point','rows','separator','summary','checks','failures']))
    check('all_records_kernel_domain_reconstructed',all(src[k]==oldsource[k]==recon[k] for k in ['records','kernel_residuals','domain_factors','point']))
    check('complete_source_normalization',len(src['transitions'])==220 and len(src['rows'])==81)
    p8=F(16792471,1181138102168120460)
    point=[F(*v) for v in old['witness']['original'][:4]]+[F(*family['stationary_t78'])]
    free=list((r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8)
    volumes=[F(c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
    scales=[p8/v for v in volumes]
    selected=[9*a+b for a in range(7) for b in range(4)]
    z=[[F(*v) for v in d['witness']['z']] for d in vertices]
    raw=[[F(*v) for v in d['witness']['raw_moments']] for d in vertices]
    check('frozen_parameters',point[0]==1 and enc(point)==data['point']==src['point'] and data['vertex_names']==names)
    check('dimensions_domain',len(src['domain_factors'])==85 and all(F(*v)>=0 for v in src['domain_factors'])
          and len(src['kernel_residuals'])==90 and len(src['records'])==500
          and sum(len(r['presentations']) for r in src['records'])==3000)
    for k,d in enumerate(vertices):
        check('all_metadata_'+str(k),d['point']==enc(point) and d['p8']==enc(p8) and d['free']==enc(free)
              and d['volumes']==enc(volumes) and d['scales']==enc(scales) and d['selected_modes']==selected)
        check('complete_array_dimensions_'+str(k),len(z[k])==len(raw[k])==45)
        for j in range(45):
            check('coordinate_binding_'+str((k,j)),z[k][j]>=0 and scales[j]>0 and raw[k][j]==scales[j]*z[k][j]
                  and enc(z[k][j])==data['z'][k][j] and enc(raw[k][j])==data['raw_moments'][k][j])
    zero=[i for i,r in enumerate(src['rows']) if not any(F(*v) for row in r['base'] for v in row)]
    newonly=[i for i in range(81) if max(divmod(i,9))==8]
    controls=[newonly,zero,sorted(zero+[31]),sorted(zero+[23,31])]
    check('control_counts',list(map(len,controls))==[17,43,44,45])
    for k,(d,ids,key) in enumerate(zip(vertices,controls,['new_only_modes','zero_old_block_modes','retained_modes','retained_modes'])):
        check('own_control_order_'+str(k),d[key]==ids)
    save('complete_input_bindings_checked')
    rows=[]
    entries={tuple(r['type']):r['affine'] for r in src['records']}
    check('forced_partition',sum(entries[8,8,i,j] is not None for i,j in it.product(range(9),repeat=2))==36)
    for i,r in enumerate(src['rows']):
        h=data['rows'][i];v=fresh['rows'][i]
        check('complete_source_row_'+str(i),all(r[k]==h[k] for k in
              ['index','mode','layers','base','cross','inverse','minors','norm','original_row','raw_beta','forced_raw','raw_anchor','energy','bound']))
        B=[[F(*v) for v in row] for row in r['base']]
        cross=[F(*v) for v in r['cross']]; x=[F(*v) for v in r['inverse']]
        A=[F(*v) for v in r['original_row']];b=F(*r['bound']); norm=F(*r['norm'])
        energy=F(*r['energy']); anchor=F(*r['raw_anchor'])
        check('whole_range_and_inverse_'+str(i),len(B)==len(cross)==len(x) and [dot(row,x) for row in B]==cross and dot(cross,x)==energy)
        a,bb=divmod(i,9)
        check('full_anchor_positive_norm_'+str(i),norm==p8*c(68-2*a,8-a)*c(956-2*bb,8-bb)>0
              and anchor==(p8*p8*(c(68,8)*c(956,8))**2 if i==0 else 0))
        WB=[[F(*v) for v in row] for row in r['weighted_base']]
        wc=[F(*v) for v in r['weighted_cross']]
        N=F(1)
        for n,degree in [(68,a),(956,bb)]:
            f=next(f for f in src['factors'] if f['n']==n and f['layer']==8)
            N*=F(*f['norms'][degree])
        D=norm/p8; transport=N/D
        layer_scales=[]
        # Reconstruct the same positive congruence from norms and signed actions.
        for l in r['layers']:
            ls=F(1)
            for n,degree in [(68,a),(956,bb)]:
                fl=next(f for f in src['factors'] if f['n']==n and f['layer']==l)
                nl=F(*fl['norms'][degree])
                tr=next(t for t in src['transitions'] if t['indices']==[n,l,8,l])
                action=next(q for q in tr['actions'] if q['degree']==degree)
                from critical_audit_simultaneous_eight_shell import beta
                ls*=nl*F(*action['coefficient'])/beta(n,l,8,degree,l)
            layer_scales.append(ls/transport)
        check('weighted_full_congruence_'+str(i),all(s>0 for s in layer_scales) and
              all(WB[j][k]==transport*layer_scales[j]*layer_scales[k]*B[j][k] for j in range(len(B)) for k in range(len(B)))
              and all(wc[j]==transport*layer_scales[j]*cross[j] for j in range(len(B))))
        coeff=[F(*v) for v in r['raw_beta']]
        forced=dot([F(*v) for v in r['forced_raw']],point)
        u=[-t for t in x]+[F(1)]
        uw=[-t/s for t,s in zip(x,layer_scales)]+[F(1)]
        vertex_rows=[]
        for k in range(4):
            diagonal=forced+dot(coeff,raw[k]); slack=b-dot(A,z[k]); rawrem=diagonal-anchor-energy
            K=[row+[cv] for row,cv in zip(B,cross)]+[cross+[diagonal-anchor]]
            WK=[row+[cv] for row,cv in zip(WB,wc)]+[wc+[transport*(diagonal-anchor)]]
            qform=dot(u,[dot(row,u) for row in K])
            wform=dot(uw,[dot(row,uw) for row in WK])
            check('full_original_raw_weighted_'+str((i,k)),rawrem==norm*slack==qform and wform==transport*rawrem
                  and enc(slack)==h['vertex_slacks'][k]==v['vertex_slacks'][k]
                  and enc(rawrem)==h['vertex_raw_remainders'][k]==v['vertex_raw_remainders'][k])
            if i in selected:check('equality_'+str((i,k)),slack==0)
            if i in controls[k]:
                j=controls[k].index(i)
                check('own_retained_control_'+str((i,k)),slack>=0 and enc(slack)==vertices[k]['witness']['original_slacks'][j]
                      and enc(rawrem)==vertices[k]['witness']['raw_slacks'][j])
            vertex_rows.append({'normalized':slack,'raw':rawrem,'quadratic_form':qform,'weighted_quadratic_form':wform})
        rows.append({'index':i,'fixed_inverse':x,'negative_test_vector':u,'weighted_test_vector':uw,
                     'positive_transport':transport,'layer_scales':layer_scales,'vertices':vertex_rows})
        if i==32:report['separator_blocks']={'source':[ [row+[cv] for row,cv in zip(B,cross)]+[cross+[forced+dot(coeff,rv)-anchor]] for rv in raw],
                                             'weighted':[ [row+[cv] for row,cv in zip(WB,wc)]+[wc+[transport*(forced+dot(coeff,rv)-anchor)]] for rv in raw]}
    weights=[F(*w) for w in data['separator']['weights']]
    check('entire_unit_separator',weights==[F(i==32) for i in range(81)] and data['separator']['support']==[32] and data['separator']['modes']==[[3,5]])
    values=[rows[32]['vertices'][k]['normalized'] for k in range(4)]
    expected=[[-20451752,-20451751],[-18663385,-18663384],[-2716330,-2716329],[-3232205,-3232204]]
    check('four_exact_strict_intervals',expected==data['separator']['integer_intervals'] and all(F(lo)<=v<F(hi)<=-2716329 for v,(lo,hi) in zip(values,expected)))
    check('all_separator_values',enc(values)==data['separator']['vertex_values'] and enc(max(values))==data['separator']['strict_uniform_upper_bound'] and max(values)<-2716329)
    # Coefficient proof on the simplex: b-A*sum(lambda*z) = sum(lambda*(b-A*z)).
    # Compare every coefficient, keeping sum(lambda)=1 as an explicit premise.
    affine_coeffs=[F(*data['rows'][32]['bound'])-dot([F(*v) for v in data['rows'][32]['original_row']],zz) for zz in z]
    check('simplex_affine_coefficients',affine_coeffs==values and all(-2716329-v>0 for v in values))
    bad=read('four-witness-hull-control-order-failure.json',False)
    initial=read('four-witness-hull-initial-binding.json',False)
    check('schema_failure_no_input_change',all(initial[k]==data[k]==bad[k] for k in
          ['vertex_names','vertex_ids','point','p8','free','volumes','scales','z','raw_moments','domain_factors']))
    check('failed_run_complete_rows_unchanged',bad['rows']==data['rows'] and bad['common_negative_modes']==data['common_negative_modes'])
    check('nine_control_order_failures_only',bad['failures']==['vertex_own_controls_(1, '+str(i)+')' for i in [17,44,53,62,71,76,77,79,80]])
    check('initial_schema_stage',initial['stage']=='full_four_vector_and_column_binding' and not initial['failures'])
    manuscript=(NB/'lemmas/L096-four-frozen-witness-convex-hull-is-excluded.md').read_text()
    intervals=[list(map(int,m)) for m in re.findall(r'\| L0(?:88|90|92|94) \| \[(-?\d+),(-?\d+)\)',manuscript)]
    check('manuscript_all_intervals',intervals==expected)
    check('negative_counts',data['summary']['vertex_negative_counts']==[16,14,13,14]==[sum(r['vertices'][k]['normalized']<0 for r in rows) for k in range(4)])
    check('complete_counts',len(rows)==81 and sum(len(r['minors']) for r in src['rows'])==306)
    report.update(rows=rows,separator={'weights':weights,'vertex_values':values,'intervals':expected,
                  'strict_margins_below_minus_2716329':[-2716329-v for v in values],
                  'simplex_premise':'lambda_k >= 0, sum lambda_k = 1; fixed columns and scales',
                  'required_lower_bound':0},summary={'verdict':'RETAINED_CONDITIONAL_HULL_EXCLUSION' if not failures else 'FAILED',
                  'checks':len(checks),'failures':len(failures),'source_checks':len(src['checks']),
                  'verifier_checks':len(fresh['checks']),'original_raw_weighted_identities':324,
                  'mode':[3,5],'vertex_intervals':expected,'strict_upper_bound':-2716329,'required_lower_bound':0,
                  'ancestral_contracts':'CONDITIONAL_UNCHANGED','rs_boundary':[955,957]})
    save('completed')
    print('Conditional hull audit:',report['summary']['verdict'],'checks:',len(checks),'failures:',failures)
    print('324 original/raw/weighted identities; actual intervals:',expected,'; all < -2716329; required >= 0')
    print('Full certificate:',OUT.relative_to(NB))
    if failures:raise SystemExit(1)

if __name__=='__main__':main()

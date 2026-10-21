"""Exact decision on just the four frozen moment witnesses; no free-row solve.

Bind full vectors and reconstruct every original/raw vertex remainder.
A single common negative mode, if present, is already a hull separator.
Never infer infeasibility merely from a failed search.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, det, cramer, enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'four-witness-hull-results.json'


def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b)),F(0))


def dec(a):
    return [[F(*v) for v in r] for r in a]


def main():
    if OUT.exists():
        raise RuntimeError('Inspect existing hull evidence before choosing a fresh path')
    checks,failures=[],[]
    report={'input_hashes':{str(Path(__file__).relative_to(NB)):
                           hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}

    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def read(name):
        path=ROOT/name
        obj=json.loads(path.read_text())
        report['input_hashes'][str(path.relative_to(NB))]=hashlib.sha256(path.read_bytes()).hexdigest()
        check('clean_'+name,not obj.get('failures',[]))
        for rel,h in obj.get('input_hashes',{}).items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
        return obj

    def save(stage):
        report.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(report),indent=2)+'\n')

    names=['fixed-column-new-only-results.json','fixed-column-zero-old-block-results.json',
           'zero-block-plus-3-4-results.json','two-mixed-row-results.json']
    vertices=[read(n) for n in names]
    source=read('two-mixed-row-critical-source.json')
    recon=read('two-mixed-row-original-reconstruction.json')
    affine=read('fully-cancelling-separator-family-critical-audit.json')
    col=read('eight-distance-full-base-kernel-results.json')
    base=read('maximizer-excluded-anchor-results.json')
    old=read('affine-sign-phase-one-results.json')
    p8=F(16792471,1181138102168120460)
    point=[F(*v) for v in old['witness']['original'][:4]]+[F(*affine['stationary_t78'])]
    free=[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    volumes=[F(C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
    scales=[p8/v for v in volumes]
    selected=[9*a+b for a in range(7) for b in range(4)]
    z=[list(map(lambda v:F(*v),d['witness']['z'])) for d in vertices]
    raw=[list(map(lambda v:F(*v),d['witness']['raw_moments'])) for d in vertices]
    for k,(name,d) in enumerate(zip(names,vertices)):
        check('full_vertex_binding_'+name,d['point']==enc(point)==source['point']==recon['point']
              and d['p8']==enc(p8) and d['free']==enc(free) and d['volumes']==enc(volumes)
              and d['scales']==enc(scales) and d['selected_modes']==selected
              and len(z[k])==len(raw[k])==45 and min(z[k])>=0 and min(raw[k])>=0
              and raw[k]==[s*v for s,v in zip(scales,z[k])])
    check('positive_scales',p8>0 and min(scales)>0 and len(free)==45)
    family=dec(affine['family'])
    factors=[dot(r,point) for r in family]
    check('85_original_domain_rows',len(family)==85 and min(factors)>=0
          and enc(factors)==source['domain_factors']==recon['domain_factors'])
    check('family_original_rref',family==[[F(*a)]+[F(*v) for v in r]
          for a,r in zip(col['affine']['intercept'],col['affine']['slopes'])])
    pairs=[F(*v) for v in base['pairs_through_14']]
    check('rho_and_original_pairs',F(*base['rho'])>0 and pairs[8]==p8
          and base['pairs_through_14']==col['pairs_through_14'])
    column=[[p8]+[F(0)]*4]
    for r in col['column'][1:]:
        column.append([p8*v for v in family[r['variable']]] if r['kind']=='free'
                      else [F(*r['value'])]+[F(0)]*4)
    weights=[1]+[C(8,i)*C(60,l-i)*C(8,j)*C(948,l-j) for l,i,j in col['orbits'][1:]]
    check('150_whole_kernel_coordinates',len(column)==len(weights)==150
          and enc(column)==affine['affine_column'] and len(col['equations'])==len(col['kernel_basis'])==90)
    for k,(row,rhs,kr) in enumerate(zip(col['equations'],col['rhs'],col['kernel_basis'])):
        residual=[sum(F(*v)*w*f[j] for v,w,f in zip(kr,weights,column)) for j in range(5)]
        check('full_original_weighted_kernel_'+str(k),residual==[0]*5
              and [sum(F(*v)*f[j] for v,f in zip(row,family)) for j in range(5)]==[F(*rhs)]+[F(0)]*4
              and enc(residual)==source['kernel_residuals'][k]==recon['kernel_residuals'][k])
    records=source['records']
    check('full_records_binding',len(records)==500 and records==recon['records'])
    entries={}
    for k,r in enumerate(records):
        vals=[p['affine'] for p in r['presentations'] if p['affine'] is not None]
        check('all_six_presentations_'+str(k),len(r['presentations'])==6
              and all(v==r['affine'] for v in vals)
              and all(r[f]==affine['records'][k][f] for f in ['type','key','affine']))
        entries[tuple(r['type'])]=None if r['affine'] is None else [F(*v) for v in r['affine']]
    check('36_forced_45_free',len(entries)==500 and
          sum(v is None for v in entries.values())==45 and
          all((entries[8,8,8-r,8-q] is None)==(r+q>=8) for r,q in it.product(range(9),repeat=2)))
    report.update(vertex_names=names,vertex_ids=['L088','L090','L092','L094'],point=point,p8=p8,
                  free=free,volumes=volumes,scales=scales,z=z,raw_moments=raw,domain_factors=factors)
    save('full_four_vector_and_column_binding')
    if failures:
        raise RuntimeError('Input discrepancy; no hull verdict')
    sizes={l:C(68,l)*C(956,l) for l in [5,6,7,8]}
    rows=[]
    for idx in range(81):
        a,b=divmod(idx,9)
        ls=[l for l in [5,6,7] if l>=max(a,b)]
        D=F(C(68-2*a,8-a)*C(956-2*b,8-b)); norm=p8*D

        def entry(l,m):
            ll,mm=sorted([l,m])
            v=[sum(beta(68,l,m,a,i)*beta(956,l,m,b,j)*entries[ll,mm,i,j][h]
                   for i,j in it.product(range(ll+1),repeat=2)) for h in range(5)]
            if idx==0:
                v[0]-=pairs[l]*pairs[m]*sizes[l]*sizes[m]
            return v

        B=[[entry(l,m)[0] for m in ls] for l in ls]
        cross=[entry(l,8) for l in ls]
        cv=[dot(r,point) for r in cross]
        mode=affine['modes'][idx]
        inv=dec(mode['inverse_affine'])
        check('whole_affine_ranges_'+str(idx),enc(B)==mode['source_base']
              and enc(cross)==mode['source_cross'] and all(entry(l,8)==entry(8,l) for l in ls)
              and all([dot(r,c) for c in zip(*inv)]==cr for r,cr in zip(B,cross)))
        minors=[]; chosen=()
        for n in range(1,len(ls)+1):
            for inds in it.combinations(range(len(ls)),n):
                value=det([[B[i][j] for j in inds] for i in inds])
                minors.append({'indices':inds,'determinant':value})
                if value:
                    chosen=inds
        x=[F(0)]*len(ls)
        if chosen:
            for j,v in zip(chosen,cramer([[B[i][j] for j in chosen] for i in chosen],[cv[i] for i in chosen])):
                x[j]=v
        energy=dot(cv,x)
        check('fresh_full_principal_inverse_'+str(idx),all(v['determinant']>=0 for v in minors)
              and [dot(r,x) for r in B]==cv and energy==dot(cv,[dot(r,point) for r in inv]))
        coeff=[F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        A=[-v/(D*V) for v,V in zip(coeff,volumes)]
        forced=[sum(beta(68,8,8,a,i)*beta(956,8,8,b,j)*v[h]
                    for (l,m,i,j),v in entries.items() if l==m==8 and v is not None) for h in range(5)]
        anchor=p8*p8*sizes[8]*sizes[8] if idx==0 else F(0)
        bound=(dot(forced,point)-anchor-energy)/norm
        for tag,obj in [('audited',source),('original',recon)]:
            saved=obj['rows'][idx]
            check(tag+'_entire_row_'+str(idx),enc(B)==saved['base'] and enc(cv)==saved['cross']
                  and enc(energy)==saved['energy'] and enc(coeff)==saved['raw_beta']
                  and enc(A)==saved['original_row'] and enc(forced)==saved['forced_raw']
                  and enc(anchor)==saved['raw_anchor'] and enc(bound)==saved['bound']
                  and enc(norm)==saved['norm' if tag=='audited' else 'positive_raw_normalization'])
        slacks=[bound-dot(A,v) for v in z]
        rawvalues=[]; terms=[]
        for k,rv in enumerate(raw):
            table={(8-r,8-q):v for (r,q),v in zip(free,rv)}
            diagonal=[F(beta(68,8,8,a,i)*beta(956,8,8,b,j))*(table[i,j] if v is None else dot(v,point))
                      for (l,m,i,j),v in entries.items() if l==m==8]
            value=sum(diagonal,F(0))-anchor-energy
            check('all_original_raw_vertex_'+str((idx,k)),len(diagonal)==81 and value==norm*slacks[k])
            if idx in selected:
                check('28_equalities_vertex_'+str((idx,k)),value==slacks[k]==0)
            rawvalues.append(value); terms.append(diagonal)
        rows.append({'index':idx,'mode':[a,b],'layers':ls,'base':B,'cross':cv,'inverse':x,'minors':minors,
                     'norm':norm,'original_row':A,'raw_beta':coeff,'forced_raw':forced,'raw_anchor':anchor,
                     'energy':energy,'bound':bound,'vertex_slacks':slacks,'vertex_raw_remainders':rawvalues,
                     'vertex_diagonal_terms':terms})
    for k,d in enumerate(vertices):
        retained=(d['new_only_modes'] if k==0 else d['zero_old_block_modes'] if k==1 else d['retained_modes'])
        for j,i in enumerate(retained):
            check('vertex_own_controls_'+str((k,i)),rows[i]['vertex_slacks'][k]>=0
                  and enc(rows[i]['vertex_slacks'][k])==d['witness']['original_slacks'][j]
                  and enc(rows[i]['vertex_raw_remainders'][k])==d['witness']['raw_slacks'][j])
    check('all_306_old_minors',sum(len(r['minors']) for r in rows)==306)
    common=[i for i,r in enumerate(rows) if max(r['vertex_slacks'])<0]
    report.update(rows=rows,common_negative_modes=common)
    save('complete_81_by_4_original_raw_remainders')
    if failures:
        raise RuntimeError('Row discrepancy; no hull verdict')
    if common:
        i=common[0]; weights=[F(j==i) for j in range(81)]
        values=[sum(w*r['vertex_slacks'][k] for w,r in zip(weights,rows)) for k in range(4)]
        check('separator_nonnegative',len(weights)==81 and min(weights)>=0 and sum(weights)==1)
        check('separator_strict_at_every_vertex',len(values)==4 and max(values)<0)
        intervals=[[v.numerator//v.denominator,v.numerator//v.denominator+1] for v in values]
        report['separator']={'weights':weights,'support':[i],'modes':[list(divmod(i,9))],
                             'vertex_values':values,'integer_intervals':intervals,
                             'strict_uniform_upper_bound':max(values),'required_lower_bound':0}
        verdict='EXACT_FOUR_VERTEX_HULL_EXCLUDED'
    else:
        verdict='INCONCLUSIVE_NO_SINGLE_ROW_SEPARATOR'
    report['summary']={'verdict':verdict,'checks':len(checks),'failures':len(failures),
                       'vertex_count':4,'mode_count':81,'common_negative_modes':common,
                       'vertex_negative_counts':[sum(r['vertex_slacks'][k]<0 for r in rows) for k in range(4)],
                       'required_lower_bound':0,'rs_boundary':[955,957]}
    save('completed')
    print('Verdict:',verdict,'checks:',len(checks),'failures:',failures)
    print('Common strictly negative modes:',common,'; required lower bound: 0')
    if common:
        print('Separator mode:',divmod(common[0],9),'; four exact integer intervals:',intervals)
    print('Certificate:',OUT.relative_to(NB))


if __name__=='__main__':
    main()

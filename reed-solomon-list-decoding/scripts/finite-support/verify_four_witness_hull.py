"""Independent exact original/raw verification of the frozen hull certificate.

No constructor, optimizer, pivot replay or expanded hull is invoked.
Recompute every vertex remainder with independent eigen coefficients and
direct full raw diagonals; check the entire rational separator.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from critical_audit_simultaneous_eight_shell import beta, c as C, enc
from critical_audit_affine_sign_remaining_modes import det

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'four-witness-hull-verification.json'


def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b)),F(0))


def dec(a):
    return [[F(*v) for v in r] for r in a]


def main():
    if OUT.exists():
        raise RuntimeError('Inspect existing verification before choosing a fresh output')
    report={'input_hashes':{str(Path(__file__).relative_to(NB)):
                           hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
    checks,failures=[],[]

    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def read(name):
        p=ROOT/name; obj=json.loads(p.read_text())
        report['input_hashes'][str(p.relative_to(NB))]=hashlib.sha256(p.read_bytes()).hexdigest()
        check('clean_'+name,not obj.get('failures',[]))
        for rel,h in obj.get('input_hashes',{}).items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
        return obj

    result=read('four-witness-hull-results.json')
    src=read('fully-cancelling-separator-family-critical-audit.json')
    source=read('two-mixed-row-critical-source.json')
    col=read('eight-distance-full-base-kernel-results.json')
    old=read('affine-sign-phase-one-results.json')
    data=[read(n) for n in result['vertex_names']]
    p8=F(16792471,1181138102168120460)
    point=[F(*v) for v in old['witness']['original'][:4]]+[F(*src['stationary_t78'])]
    free=[(r,q) for r in range(9) for q in range(9) if r+q>=8]
    V=[F(C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
    factors=[dot([F(*v) for v in r],point) for r in src['family']]
    check('full_frozen_columns_domain_scales',enc(point)==result['point']==source['point']
          and len(factors)==85 and min(factors)>=0 and enc(factors)==result['domain_factors']
          and min(V)>0 and p8>0 and enc(free)==result['free'] and enc(V)==result['volumes'])
    family=dec(src['family'])
    check('all_original_kernel_rows',len(col['equations'])==90 and all(
        [dot([F(*v) for v in r],cv) for cv in zip(*family)]==[F(*rhs)]+[F(0)]*4
        for r,rhs in zip(col['equations'],col['rhs'])))
    check('whole_weighted_kernel_contract',len(source['kernel_residuals'])==90
          and all(len(r)==5 and not any(F(*v) for v in r) for r in source['kernel_residuals']))
    z=[[F(*v) for v in d['witness']['z']] for d in data]
    raw=[[F(*v) for v in d['witness']['raw_moments']] for d in data]
    for k,d in enumerate(data):
        check('full_45_vertex_'+str(k),d['point']==enc(point) and len(z[k])==len(raw[k])==45
              and min(z[k])>=0 and raw[k]==[p8*x/v for x,v in zip(z[k],V)]
              and enc(z[k])==result['z'][k] and enc(raw[k])==result['raw_moments'][k])
    records=source['records']
    check('500_types_3000_presentations',len(records)==500 and sum(len(r['presentations']) for r in records)==3000
          and all(all(r[k]==s[k] for k in ['key','type','affine']) for r,s in zip(records,src['records'])))
    entries={tuple(r['type']):None if r['affine'] is None else [F(*v) for v in r['affine']] for r in records}
    check('36_forced_45_free',sum(entries[8,8,i,j] is None for i in range(9) for j in range(9))==45
          and all((entries[8,8,8-r,8-q] is None)==(r+q>=8) for r,q in it.product(range(9),repeat=2)))

    def eigen(n,a,r):
        return F(sum((-1)**h*C(a,h)*C(8-a,r-h)*C(n-8-a,r-h) for h in range(r+1)))

    rows=[]
    selected=[9*a+b for a in range(7) for b in range(4)]
    for i,m in enumerate(src['modes']):
        a,b=divmod(i,9)
        B=dec(m['source_base'])
        cross=[dot([F(*v) for v in r],point) for r in m['source_cross']]
        x=[dot([F(*v) for v in r],point) for r in m['inverse_affine']]
        check('entire_range_'+str(i),[dot(r,x) for r in B]==cross)
        minors=[]
        for n in range(1,len(B)+1):
            for inds in it.combinations(range(len(B)),n):
                minors.append(det([[B[j][k] for k in inds] for j in inds]))
        check('all_old_principal_minors_'+str(i),all(v>=0 for v in minors))
        D=F(C(68-2*a,8-a)*C(956-2*b,8-b)); norm=p8*D
        ev=[eigen(68,a,r)*eigen(956,b,q) for r,q in free]
        coeff=[F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        check('all_independent_eigen_beta_'+str(i),coeff==[D*v for v in ev] and norm>0)
        A=[-e/v for e,v in zip(ev,V)]
        forced=dot([F(*v) for v in m['forced']],point)
        anchor=p8*C(68,8)*C(956,8) if i==0 else F(0)
        energy=dot(cross,x)
        bound=forced-anchor-energy/norm
        saved=result['rows'][i]
        check('complete_original_row_'+str(i),enc(A)==saved['original_row']==m['row']
              and enc(bound)==saved['bound'] and enc(energy)==saved['energy']
              and enc(norm)==saved['norm'] and enc(norm*anchor)==saved['raw_anchor'])
        slacks=[bound-dot(A,v) for v in z]; rawvalues=[]; allterms=[]
        for k,rv in enumerate(raw):
            new={(8-r,8-q):v for (r,q),v in zip(free,rv)}
            terms=[F(beta(68,8,8,a,j)*beta(956,8,8,b,h))*(new[j,h] if v is None else dot(v,point))
                   for (l,m0,j,h),v in entries.items() if l==m0==8]
            value=sum(terms,F(0))-norm*anchor-energy
            check('81_term_original_raw_'+str((i,k)),len(terms)==81 and value==norm*slacks[k]
                  and enc(terms)==saved['vertex_diagonal_terms'][k]
                  and enc(value)==saved['vertex_raw_remainders'][k]
                  and enc(slacks[k])==saved['vertex_slacks'][k])
            if i in selected:
                check('selected_equality_'+str((i,k)),value==slacks[k]==0)
            rawvalues.append(value); allterms.append(terms)
        rows.append({'index':i,'original_row':A,'bound':bound,'norm':norm,'vertex_slacks':slacks,
                     'vertex_raw_remainders':rawvalues,'vertex_diagonal_terms':allterms})
    sep=result['separator']; weights=[F(*v) for v in sep['weights']]
    values=[sum(w*r['vertex_slacks'][k] for w,r in zip(weights,rows)) for k in range(4)]
    common=[i for i,r in enumerate(rows) if max(r['vertex_slacks'])<0]
    check('full_81_separator_weights',len(weights)==81 and min(weights)>=0 and sum(weights)==1
          and [i for i,w in enumerate(weights) if w]!=[]
          and [i for i,w in enumerate(weights) if w]==sep['support'])
    check('strict_full_separator',max(values)<0 and enc(values)==sep['vertex_values']
          and enc(max(values))==sep['strict_uniform_upper_bound'])
    intervals=[[v.numerator//v.denominator,v.numerator//v.denominator+1] for v in values]
    check('four_exact_integer_intervals',intervals==sep['integer_intervals']
          and all(F(lo)<=v<F(hi)<=0 for v,(lo,hi) in zip(values,intervals)))
    check('all_common_rows',common==result['common_negative_modes'])
    report.update(point=point,rows=rows,separator=sep,
                  summary={'verdict':'VERIFIED_FOUR_VERTEX_HULL_EXCLUSION' if not failures else 'FAILED',
                           'checks':len(checks),'failures':len(failures),'vertex_count':4,'mode_count':81,
                           'original_raw_identities':324,'required_lower_bound':0,
                           'separator_modes':sep['modes'],'vertex_integer_intervals':intervals,
                           'rs_boundary':[955,957]},checks=checks,failures=failures)
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print('Verdict:',report['summary']['verdict'],'checks:',len(checks),'failures:',failures)
    print('Separator modes:',sep['modes'],'; four exact integer intervals:',intervals,'; required lower bound: 0')
    print('Certificate:',OUT.relative_to(NB))


if __name__=='__main__':
    main()

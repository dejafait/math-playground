"""Independent full-orbit and fixed-point interval checker; no constructor import."""
import gzip
import hashlib
import json
import time
from collections import Counter,defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'positive-factor-enclosure.json.gz'
OUT=ROOT/'positive-factor-enclosure-verification.json'

def main():
    started=time.monotonic(); checks=Counter(); failures=[]
    report={'stage':'in_progress'}
    def save():
        report.update(checks_by_kind=dict(checks),checks=sum(checks.values()),failures=failures)
        OUT.write_text(json.dumps(report,indent=2)+'\n')
    def check(kind,ok,detail=None):
        checks[kind]+=1
        if not ok:
            failures.append({'kind':kind,'detail':detail}); report['stage']='failed'; save()
            raise AssertionError((kind,detail))
    with gzip.open(SRC,'rt') as f: z=json.load(f)
    report['input_sha256']=hashlib.sha256(SRC.read_bytes()).hexdigest()
    check('completed_enclosure',z['stage']=='exact_complete')
    lp=json.loads((ROOT/'delsarte-lp-results.json').read_text())
    av=[Fraction(x['numerator'],x['denominator']) for x in lp['exact']['primal']]
    n=65537**28//2**128+1; H=comb(1024,68)
    U=Fraction(comb(1024,64),comb(68,64))
    gs=[comb(68,k)*comb(956,k) for k in range(69)]
    cs=[Fraction(1)]+[Fraction(0)]*4+[(n-1)*av[k-5]/((U-1)*gs[k]) for k in range(5,69)]
    check('canonical_parameters',n==z['N'] and H==z['H'] and sum(av)==U-1 and min(av)>0)
    check('canonical_pairs',cs==[Fraction(*x) for x in z['c']] and sum(a*b for a,b in zip(gs,cs))==n)
    check('integer_threshold',(n-1)*2**128<=65537**28<n*2**128)
    scales=[Fraction(10)**p for p in z['scale_powers']]
    demands=[(n-2)*v for v in cs[5:]]
    check('demands',demands==[Fraction(*x) for x in z['demands']])
    K=z['K']; check('initial_cube_scale',K>0 and K**3*(n-1)<=H<(K+1)**3*(n-1))
    check('initial_values',[Fraction(*v) for v in z['initial']]==[cs[i+5]*K/scales[i] for i in range(64)])
    for i in range(64):
        check('diagonal_scaling',scales[i]>0 and scales[i]<=cs[i+5]*K<10*scales[i],i)
    # Four-region reconstruction, rather than constructor's (j,t,s) traversal.
    def choose(n,k): return comb(n,k) if 0<=k<=n else 0
    left={}; right={}
    for i in range(69):
        for j in range(69):
            left[i,j]=[choose(i,t)*choose(68-i,j-t) for t in range(min(i,j)+1)]
            right[i,j]=[choose(i,s)*choose(956-i,j-s) for s in range(min(i,j)+1)]
    coefficients=[defaultdict(int) for _ in range(64)]; counts=Counter()
    shell_records=[]
    for i in range(69):
        totals=[0]*69; repetitions=[]
        for common in range(69-i):
            for aonly in range(i+1):
                for bonly in range(i+1):
                    outside=68-common-aonly-bonly
                    if not 0<=outside<=956-i: continue
                    j=68-common-aonly; h=68-common-bonly
                    t=i-aonly; s=bonly
                    atoms=(956-i-outside,i-aonly,i-bonly,68-i-common,outside,aonly,bonly,common)
                    v=choose(68-i,common)*choose(i,aonly)*choose(i,bonly)*choose(956-i,outside)
                    check('complete_original_orbit',min(atoms)>=0 and sum(atoms)==1024 and
                          max(0,i+j-68)<=t<=min(i,j) and max(0,i+j-956)<=s<=min(i,j)
                          and h==i+j-t-s and v==left[i,j][t]*right[i,j][s]>0)
                    # Three anchors and the symmetric swap exhaust six presentations.
                    tb,sb=atoms[2],atoms[5]; tz,sz=atoms[4],atoms[3]
                    G=gs[i]*v
                    check('six_presentations',tb-sb==tz-sz==t-s and
                          G==gs[i]*left[i,h][tb]*right[i,h][sb] and
                          G==gs[j]*left[j,h][tz]*right[j,h][sz])
                    counts['original']+=1; totals[j]+=v
                    if min(i,j,h)==0:
                        counts['repeated']+=1
                        check('repetition_coefficients',v==(gs[j] if i==0 else 1))
                        if i: repetitions.append([j,t,s,v])
                    elif min(i,j,h)<5:
                        counts['null']+=1
                        check('null_edges',min(cs[i],cs[j],cs[h])==0)
                    else:
                        counts['permitted']+=1
                        coefficients[i-5][tuple(sorted((j-5,h-5)))]+=v
        check('full_coincident_row_and_sums',totals==gs and sum(totals)==H,i)
        check('both_repetitions',sorted(repetitions)==([] if i==0 else [[0,0,0,1],[i,i,i,1]]),i)
        shell_records.append(totals)
    check('source_partition',dict(counts)==z['counts']==dict(original=1500625,repeated=205,null=10220,permitted=1490200))
    rows=[[[j,h,v] for (j,h),v in sorted(r.items())] for r in coefficients]
    check('all_polynomial_coefficients',rows==z['coefficients'])
    report.update(counts=dict(counts),coefficient_count=sum(map(len,rows)),shell_coefficient_sums=shell_records)
    # Independent endpoint arithmetic. Division bounds are rational floor/ceil,
    # including negative endpoints; no floating-point arithmetic occurs below.
    q=z['Q']; radius=z['radius']; pt=z['point']; R=z['preconditioner']
    check('fixed_contract',q==10**70 and radius==10**25 and len(pt)==len(R)==64 and all(len(r)==64 for r in R))
    box=[(v-radius,v+radius) for v in pt]
    check('positive_box',min(a for a,b in box)>0 and [list(x) for x in box]==z['box'])
    def plus(a,b): return (a[0]+b[0],a[1]+b[1])
    def times(a,b):
        p=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]
        low=min(p)//q; high=(max(p)+q-1)//q
        check('outward_product',low*q<=min(p) and high*q>=max(p))
        return low,high
    residual=[]; derivative=[]
    for i,row in enumerate(rows):
        if time.monotonic()-started>300:
            report['stage']='incomplete_budget'; save(); print('independent budget exceeded',OUT); return
        r=(-q,-q); J=[(0,0)]*64
        for pos,(j,h,v) in enumerate(row):
            coeff=Fraction(v)*scales[i]*scales[j]*scales[h]/demands[i]
            bound=(coeff.numerator*q//coeff.denominator,
                   (coeff.numerator*q+coeff.denominator-1)//coeff.denominator)
            check('full_coefficient_enclosure',z['coefficient_bounds'][i][pos]==[j,h,*bound] and
                  Fraction(bound[0],q)<=coeff<=Fraction(bound[1],q))
            # Product rule on the original three factor occurrences, including repeats.
            indices=[i,j,h]; term=bound
            for k in indices: term=times(term,(pt[k],pt[k]))
            r=plus(r,term)
            for occurrence,k in enumerate(indices):
                deriv=bound
                for other,m in enumerate(indices):
                    if other!=occurrence: deriv=times(deriv,box[m])
                J[k]=plus(J[k],deriv)
        check('full_residual_row',list(r)==z['residual'][i],i)
        check('full_jacobian_row',[list(x) for x in J]==z['jacobian'][i],i)
        residual.append(r); derivative.append(J)
    margins=[]; images=[]; max_defect_rows=[]
    for i in range(64):
        center=(0,0)
        for k in range(64): center=plus(center,times((-R[i][k],)*2,residual[k]))
        check('preconditioned_residual',list(center)==z['negative_R_residual'][i],i)
        image=center; l1=0
        for j in range(64):
            entry=(q if i==j else 0,)*2
            for k in range(64): entry=plus(entry,times((-R[i][k],)*2,derivative[k][j]))
            check('full_defect_entry',list(entry)==z['defect'][i][j],[i,j])
            image=plus(image,times(entry,(-radius,radius)))
            l1+=max(abs(entry[0]),abs(entry[1]))
        margin=min(image[0]+radius,radius-image[1])
        check('complete_krawczyk_image',list(image)==z['krawczyk_image'][i],i)
        check('strict_inclusion_margin',margin==z['inclusion_margins'][i] and margin>0,i)
        margins.append(margin); images.append(image); max_defect_rows.append(l1)
    check('inclusion_verdict',z['inclusion'] and min(margins)>0)
    lower=Fraction(pt[0]-radius,q)*scales[0]
    upper=Fraction(pt[0]+radius,q)*scales[0]
    lr=lower**3/cs[5]; ur=upper**3/cs[5]
    verdict='pass' if ur<=1 else 'reject_enclosed_root' if lr>1 else 'straddles'
    check('entire_capacity_comparison',lr==Fraction(*z['capacity']['lower_cube_ratio']) and
          ur==Fraction(*z['capacity']['upper_cube_ratio']) and verdict==z['capacity']['verdict'])
    report.update(stage='verified',inclusion=True,minimum_margin_units=min(margins),
       required_margin_units='strictly greater than zero',inclusion_margins=margins,
       max_defect_row_l1=[max(max_defect_rows),q],capacity={
       'verdict':verdict,'lower_cube_ratio':[lr.numerator,lr.denominator],
       'upper_cube_ratio':[ur.numerator,ur.denominator]},seconds=time.monotonic()-started)
    save()
    print(json.dumps(dict(stage=report['stage'],checks=report['checks'],failures=len(failures),
       min_margin=min(margins),required_margin='>0',capacity=verdict,path=str(OUT))))

if __name__=='__main__': main()

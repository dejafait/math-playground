"""One lexicographic rational construction; no support or parameter search."""
import hashlib
import itertools
import json
import resource
import sys
import time
from fractions import Fraction as F
from math import comb, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
B=Path(__file__).parent
ROOT=B.parent.parent
OUT=B/'fixed-pair-shared-scalar-results.json'
START=time.time()
CAPS=dict(entries_per_pass=1501000,free_classes=1024,equations=69,
          scalar_rows_per_pass=4600000,presentation_visits_combined=20000000,
          elimination_updates=5000000,live_bytes=2**30,output_bytes=256*2**20,
          rational_bits=262144,seconds_combined=900)
PERMS=list(itertools.permutations(range(3)))
S=dict(stage='in_progress',started=START,caps=CAPS,implementation_failures=[],
       entries=0,presentation_visits=0,elimination_updates=0)


def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(2**20),b''): h.update(b)
    return h.hexdigest()


def enc(x): return [x.numerator,x.denominator]


def rss():
    x=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return x if sys.platform=='darwin' else x*1024


def bounded():
    assert time.time()-START<=CAPS['seconds_combined']
    assert rss()<=CAPS['live_bytes']
    assert S['entries']<=CAPS['entries_per_pass']
    assert S['presentation_visits']*2<=CAPS['presentation_visits_combined']
    assert S['elimination_updates']<=CAPS['elimination_updates']


def save():
    bounded()
    with OUT.open('w') as f: json.dump(S,f,separators=(',',':')); f.write('\n')
    assert sum(p.stat().st_size for p in B.glob('fixed-pair-shared-scalar-*.json'))<=CAPS['output_bytes']


def main():
    save()
    paths=['lemmas/L021-basic-delsarte-support-lp-optimum.md',
           'lemmas/L022-selected-triple-sdp-primal-limitation.md',
           'lemmas/L023-full-zero-block-extension-psd.md',
           'lemmas/L098-exact-cardinality-normalized-control-obstruction.md',
           'lemmas/L105-fixed-pair-independent-row-capacity-nonexclusion.md',
           'foundations/04-constant-weight-triple-sdp-source.md',
           'foundations/12-global-degree-three-moment-source.md',
           'foundations/13-fixed-cardinality-marginal-source.md',
           'scripts/finite-support/delsarte-lp-results.json',
           'scripts/finite-support/fixed-cardinality-normalized-control-results.json',
           'scripts/finite-support/fixed-pair-shared-scalar-construct.py',
           'scripts/finite-support/fixed-pair-shared-scalar-verify.py']
    S['input_sha256']={p:digest(ROOT/p) for p in paths}
    lp=json.loads((B/'delsarte-lp-results.json').read_text())
    # Read only selected complete values in the bounded prefix of L098's
    # 307 MiB certificate; hash the complete file above without loading it.
    with (B/'fixed-cardinality-normalized-control-results.json').open() as f:
        prefix=f.read(2**20)
    def field(k):
        text=prefix.split(json.dumps(k)+':',1)[1].lstrip()
        return json.JSONDecoder().raw_decode(text)[0]
    for name,h in field('input_sha256').items(): assert digest(B/name)==h
    g=[comb(68,i)*comb(956,i) for i in range(69)]
    p=[F(1)]+[F(0)]*4+[F(r['numerator'],r['denominator'])/(2*g[i])
           for i,r in zip(range(5,69),lp['exact']['primal'])]
    M=(F(comb(1024,64),comb(68,64))+1)/2
    N=65537**28//2**128+1
    alpha=F(N-1)/(M-1)
    cp=[alpha*x+(1-alpha)*int(i==0) for i,x in enumerate(p)]
    assert sum(g[i]*p[i] for i in range(69))==M
    assert len(cp)==69 and 0<alpha<1 and cp[0]==1 and cp[1:5]==[0]*4
    assert all(0<x<1 for x in cp[5:])
    assert sum(g[i]*cp[i] for i in range(69))==N
    assert p==[F(*x) for x in field('p')]
    assert cp==[F(*x) for x in field('control_p')]
    assert N==field('N') and alpha==F(*field('alpha'))
    S.update(N=N,M=enc(M),alpha=enc(alpha),pairs=list(map(enc,cp)),
             prescription='Only distinct source classes with sorted distances (i,68,68), 5<=i<=68; others zero.',
             source_class_rule='(sorted(i,j,i+j-t-s),t-s); source presentations retain t-s',
             code_rule='0: zero; 1+b: Boolean pair c_b; 70+r: retained class r',
             declared_live_bound_bytes=2**30)
    save()
    # Discover retained classes from all original orbits before allocating
    # their small coefficient matrix. No full-orbit dense matrix exists.
    retained=set()
    # Every proposed class can be presented with its least distance i
    # first and j=68. The actual range forces t=i, and h=68 forces s=0.
    # Enumerate that slice, then verify exhaustion in the one full pass.
    for i in range(5,69):
        j=68
        for t in range(max(0,i+j-68),min(i,j)+1):
            for s in range(max(0,i+j-956),min(i,j)+1):
                ds=tuple(sorted((i,j,i+j-t-s)))
                if ds[0]>=5 and ds[1:]==(68,68): retained.add((*ds,t-s))
    keys=sorted(retained)
    assert len(keys)<=CAPS['free_classes'] and 69<=CAPS['equations']
    index={k:r for r,k in enumerate(keys)}
    A=[[0]*len(keys) for _ in range(69)]
    fixed=[F(0)]*69
    entries=[]; scalar_patterns={}; classes=set()
    def code(ds,u):
        sd=tuple(sorted(ds))
        if any(0<k<5 for k in ds): return 0
        if sd[0]==0:
            assert sd[1]==sd[2] and u==0
            return 1+sd[1]
        if sd[0]>=5 and sd[1:]==(68,68):
            assert (*sd,u) in index
            return 70+index[(*sd,u)]
        return 0
    for i in range(69):
        row_count=0
        for j in range(69):
            ts=list(range(max(0,i+j-68),min(i,j)+1))
            ss=list(range(max(0,i+j-956),min(i,j)+1))
            inside=[comb(i,t)*comb(68-i,j-t) for t in ts]
            outside=[comb(i,s)*comb(956-i,j-s) for s in ss]
            codes=[]; total=0
            for ti,t in enumerate(ts):
                for si,s in enumerate(ss):
                    ds=(i,j,i+j-t-s); u=t-s
                    c=code(ds,u); codes.append(c)
                    classes.add((*sorted(ds),u))
                    for order in PERMS:
                        a,b,h=(ds[k] for k in order)
                        tp=(a+b-h+u)//2; sp=(a+b-h-u)//2
                        assert 2*tp==a+b-h+u and 2*sp==a+b-h-u
                        assert max(0,a+b-68)<=tp<=min(a,b)
                        assert max(0,a+b-956)<=sp<=min(a,b)
                        assert code((a,b,h),tp-sp)==c
                        S['presentation_visits']+=1
                    D=inside[ti]*outside[si]
                    total+=D
                    if c>=70: A[i][c-70]+=D
                    elif c: fixed[i]+=D*cp[c-1]
                    scalar_patterns[(i,j,c)]=scalar_patterns.get((i,j,c),0)+1
                    S['entries']+=1; row_count+=1
            assert total==g[j]
            entries.append(dict(i=i,j=j,t=ts,s=ss,inside=inside,outside=outside,codes=codes))
        bounded()
    assert S['entries']==1500625
    S.update(classes_count=len(classes),retained_classes=keys,coefficient_entries=entries,
             contraction_matrix=A,fixed_contributions=list(map(enc,fixed)))
    del classes
    b=[N*cp[i]-fixed[i] for i in range(69)]
    S['contraction_rhs']=list(map(enc,b))
    S['stage']='constructed_small_system'
    save()
    # One first-available-row rational forward elimination, increasing columns.
    R=[[F(x) for x in row]+[rhs] for row,rhs in zip(A,b)]
    pivots=[]; operations=[]; r=0
    for col in range(len(keys)):
        pivot=next((k for k in range(r,69) if R[k][col]),None)
        if pivot is None: continue
        if pivot!=r:
            R[r],R[pivot]=R[pivot],R[r]; operations.append(['swap',r,pivot])
        v=R[r][col]
        R[r]=[x/v for x in R[r]]; S['elimination_updates']+=len(R[r])
        operations.append(['divide',r,enc(v)])
        for k in range(r+1,69):
            v=R[k][col]
            if v:
                R[k]=[x-v*y for x,y in zip(R[k],R[r])]
                S['elimination_updates']+=len(R[k]); operations.append(['subtract',k,r,enc(v)])
        pivots.append(col); r+=1
        assert max(max(abs(x.numerator).bit_length(),x.denominator.bit_length())
                   for row in R for x in row)<=CAPS['rational_bits']
        bounded()
    inconsistent=[i for i,row in enumerate(R) if not any(row[:-1]) and row[-1]]
    S.update(rank=len(pivots),pivots=pivots,operations=operations,
             echelon=[list(map(enc,row)) for row in R],inconsistent_rows=inconsistent)
    if inconsistent:
        S['stage']='restricted_system_inconsistent'; save(); return
    x=[F(0)]*len(keys)
    for k in reversed(range(len(pivots))):
        col=pivots[k]; x[col]=R[k][-1]-sum(R[k][j]*x[j] for j in range(col+1,len(keys)))
    assert all(sum(a*v for a,v in zip(row,x))==rhs for row,rhs in zip(A,b))
    values=[F(0)]+cp+x
    q=lcm(*(v.denominator for v in values))
    nums=[int(q*v) for v in values]; P=nums[1:70]
    assert max(q.bit_length(),*(abs(v).bit_length() for v in nums))<=CAPS['rational_bits']
    patterns=[]; failures=[0,0,0]; first=None; checked=0
    for (i,j,c),count in sorted(scalar_patterns.items()):
        slacks=[nums[c],P[i]-nums[c],q+nums[c]-P[i]-P[j]]
        signs=[(z>0)-(z<0) for z in slacks]
        patterns.append([i,j,c,count,signs])
        for k,z in enumerate(slacks):
            failures[k]+=count*(z<0)
            if z<0 and first is None: first=dict(i=i,j=j,code=c,row=k,slack=enc(F(z,q)))
        checked+=3*count
    residuals=[sum(a*v for a,v in zip(row,x))+fixed[i]-N*cp[i] for i,row in enumerate(A)]
    S.update(stage='complete_candidate_substitution',candidate=list(map(enc,x)),
             value_denominator=q,value_numerators=nums,
             scalar_factoring='For each original code c at (i,j), the three slack numerators over q are nums[c], P[i]-nums[c], q+nums[c]-P[i]-P[j]; patterns save count and all three signs.',
             scalar_patterns=patterns,scalar_rows=checked,scalar_failures=failures,
             first_scalar_failure=first,contraction_residuals=list(map(enc,residuals)),
             max_value_bits=max(q.bit_length(),*(abs(v).bit_length() for v in nums)),
             elapsed_seconds=time.time()-START,peak_live_bytes=rss(),
             construction_feasible=not any(failures) and all(v==0 for v in residuals))
    assert checked<=CAPS['scalar_rows_per_pass']
    save()
    print('Retained classes/rank:',len(keys),len(pivots),'; equations:',len(A))
    print('Scalar failures [nonnegative,upper,lower]:',failures,'of',checked,'; contractions zero:',sum(v==0 for v in residuals),'/69')
    print('Entries:',S['entries'],'/1501000; combined reserved visits:',2*S['presentation_visits'],'/20000000')
    print('Elimination updates:',S['elimination_updates'],'/5000000; elapsed:',round(time.time()-START,2),'/900')
    print('First failure:',None if first is None else {k:v for k,v in first.items() if k!='slack'},'; full rational:',str(OUT)+'/first_scalar_failure/slack')
    print('Certificate:',OUT,'; bytes:',OUT.stat().st_size,'/268435456')


if __name__=='__main__':
    try: main()
    except BaseException as e:
        S['stage']='incomplete'; S['implementation_failures'].append(repr(e))
        with OUT.open('w') as f: json.dump(S,f,separators=(',',':')); f.write('\n')
        raise

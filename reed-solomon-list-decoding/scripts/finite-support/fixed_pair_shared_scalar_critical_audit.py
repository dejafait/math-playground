"""Step 396: independent complete L106 audit; no solver or constructor import."""
import hashlib
import itertools
import json
import resource
import sys
import time
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import comb, lcm
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'fixed-pair-shared-scalar-critical-audit.json'
START = time.monotonic()
R = dict(stage='in_progress', checks=0, failures=[], presentation_visits=0,
         elimination_updates=0)
sys.set_int_max_str_digits(0)


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def digest(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(2**20), b''):
            h.update(b)
    return h.hexdigest()


def check(ok, label):
    R['checks'] += 1
    if not ok:
        raise AssertionError(label)


def bounds():
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    mem *= 1 if sys.platform == 'darwin' else 1024
    R.update(peak_live_bytes=mem, elapsed_seconds=time.monotonic()-START)
    check(mem <= 2**30, 'memory <= 1 GiB')
    check(R['elapsed_seconds'] <= 900, 'audit time <= 900 s')
    check(R['presentation_visits'] <= 20000000, 'presentations <= 20 million')
    check(R['elimination_updates'] <= 5000000, 'elimination <= 5 million')


@lru_cache(None)
def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    data_path = B/'fixed-pair-shared-scalar-results.json'
    verify_path = B/'fixed-pair-shared-scalar-verification.json'
    d = json.loads(data_path.read_text())
    v = json.loads(verify_path.read_text())
    R['input_sha256'] = {str(p.relative_to(ROOT)): digest(p)
                         for p in (data_path, verify_path, Path(__file__).resolve())}
    check(v['certificate_sha256'] == digest(data_path), 'original verifier binding')
    check(d['stage'] == 'complete_candidate_substitution' and v['stage'] == 'complete', 'stages')
    check(not d['implementation_failures'] and not v['implementation_failures'], 'original failures')
    for p, h in d['input_sha256'].items():
        check(digest(ROOT/p) == h, 'original input hash: '+p)
    R['original_input_sha256'] = d['input_sha256']
    # Decode exact selected JSON values, never interpret a truncated value.
    with (B/'fixed-cardinality-normalized-control-results.json').open() as f:
        prefix = f.read(2**20)
    def field(name):
        return json.JSONDecoder().raw_decode(prefix.split(json.dumps(name)+':', 1)[1].lstrip())[0]
    endpoints = field('input_sha256')
    for p, h in endpoints.items():
        check(digest(B/p) == h, 'L098 endpoint hash: '+p)
    R['L098_endpoint_sha256'] = endpoints
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    a = [F(0)]*5 + [F(z['numerator'], z['denominator']) for z in lp['exact']['primal']]
    g = [C(68,i)*C(956,i) for i in range(69)]
    U = F(C(1024,64), C(68,64)); M = (U+1)/2
    N = 65537**28//2**128+1
    check(len(a)==69 and all(z>0 for z in a[5:]) and sum(a)==U-1, 'L021 vector and objective')
    # Check every defining equation of the imported uniquely specified L021 vector.
    for j in range(1,65):
        row = [F(sum((-1)**h*C(j,h)*C(68-j,i-h)*C(956-j,i-h)
                     for h in range(i+1)), g[i]) for i in range(5,69)]
        check(sum(q*z for q,z in zip(row,a[5:])) == -1, 'L021 defining equation')
    p = [F(1)]+[F(0)]*4+[a[i]/(2*g[i]) for i in range(5,69)]
    alpha = F(N-1)/(M-1)
    c = [F(1)]+[alpha*z for z in p[1:]]
    check(N>2 and 0<alpha<1 and all(0<z<1 for z in c[5:]), 'endpoint signs')
    check(sum(g[i]*c[i] for i in range(69))==N, 'objective N')
    check(N==d['N']==field('N') and enc(alpha)==d['alpha']==field('alpha'), 'N alpha recovered')
    check(enc(M)==d['M'] and list(map(enc,c))==d['pairs']==field('control_p'), 'all pair values')
    check(list(map(enc,p))==field('p'), 'original L098 pairs')
    keys = [(i,68,68,i) for i in range(5,69)]
    check(list(map(list,keys))==d['retained_classes'], '64 manuscript classes')
    x = [(N-2)*c[i]/C(956-i,68) for i in range(5,68)]
    x.append((N-2)*(3*c[68]-F(2*(N-1),g[68]))/C(888,68))
    check(list(map(enc,x))==d['candidate'], 'all 64 full signed values')
    rho = g[68]*c[68]/(N-1)
    manuscript_rho = F(999827353056294107002031770259284685411165837067392868070193840389936016500775876936698401230511,
                      126241790782674344390415873704003538302112683925274740089310694724316617167200847228172347907068912)
    check(rho==a[68]/(U-1)==manuscript_rho, 'exact manuscript rho')
    check(F(7919,10**6)<=rho<F(7920,10**6)<F(2,3) and x[-1]<0, 'strict sign threshold')
    values = [F(0)]+c+x
    q = lcm(*(z.denominator for z in values)); nums=[int(q*z) for z in values]
    check(q==d['value_denominator'] and nums==d['value_numerators'], 'entire scalar codebook')
    P = nums[1:70]
    # Build all six reanchorings directly from Boolean membership predicates.
    # atoms[m] counts points belonging to precisely the sets with bits in m.
    transforms=[]
    for ab,bb,cb in itertools.permutations((1,2,4)):
        transforms.append((tuple(m for m in range(8) if m&ab and not m&bb),
                           tuple(m for m in range(8) if m&ab and not m&cb),
                           tuple(m for m in range(8) if m&bb and not m&cb),
                           ab, bb|cb))
    allclasses=set(); retained=Counter(); patterns=Counter()
    entries=[]; A=[[0]*64 for _ in range(69)]; fixed=[0]*69; lhs=[0]*69
    total_orbits=repeats=forbidden=0; negative_rows=[]; failures=[0,0,0]
    for i in range(69):
        for j in range(69):
            ts=list(range(max(0,i+j-68),min(i,j)+1)); ss=list(range(min(i,j)+1))
            inside=[C(i,t)*C(68-i,j-t) for t in ts]
            outside=[C(i,s)*C(956-i,j-s) for s in ss]
            codes=[]; shell_total=0
            old=d['coefficient_entries'][69*i+j]
            check((old['i'],old['j'])==(i,j) and old['t']==ts and old['s']==ss, 'original index ranges')
            check(old['inside']==inside and old['outside']==outside, 'all coefficient factors')
            for ti,t in enumerate(ts):
                for si,s in enumerate(ss):
                    atoms=(956-i-j+s,t,i-s,j-t,j-s,i-t,s,68-i-j+t)
                    check(min(atoms)>=0 and sum(atoms)==1024, 'eight nonnegative atoms')
                    check(all(sum(atoms[m] for m in range(8) if m&bit)==68 for bit in (1,2,4)), 'three actual weights')
                    h=i+j-t-s; ds=tuple(sorted((i,j,h))); key=(*ds,t-s)
                    bad=any(0<z<5 for z in ds); rep=ds[0]==0
                    if bad:
                        code=0
                    elif rep:
                        check(ds[1]==ds[2] and t==s, 'Boolean repeated pair')
                        code=1+ds[1]
                    elif ds[1:]==(68,68):
                        check(key in keys and t-s==ds[0], 'retained invariant forced')
                        code=70+ds[0]-5; retained[(i,j,t,s)]+=1
                    else:
                        code=0
                    for ai,aj,ah,at,ass in transforms:
                        ii=sum(atoms[m] for m in ai); jj=sum(atoms[m] for m in aj)
                        hh=sum(atoms[m] for m in ah); tt=atoms[at]; s2=atoms[ass]
                        check(hh==ii+jj-tt-s2 and tt-s2==t-s and tuple(sorted((ii,jj,hh)))==ds, 'six membership reanchorings')
                        check(max(0,ii+jj-68)<=tt<=min(ii,jj) and 0<=s2<=min(ii,jj), 'reanchored actual range')
                        check(d['coefficient_entries'][69*ii+jj]['codes'][(tt-max(0,ii+jj-68))*(min(ii,jj)+1)+s2]==code, 'reanchored original lift')
                        R['presentation_visits']+=1
                    codes.append(code); allclasses.add(key)
                    D=inside[ti]*outside[si]; shell_total+=D
                    lhs[i]+=D*nums[code]
                    if code>=70:
                        A[i][code-70]+=D
                    else:
                        fixed[i]+=D*nums[code]
                    slacks=(nums[code],P[i]-nums[code],q+nums[code]-P[i]-P[j])
                    signs=tuple((z>0)-(z<0) for z in slacks)
                    patterns[(i,j,code,signs)]+=1
                    for k,z in enumerate(slacks):
                        if z<0:
                            failures[k]+=1
                            negative_rows.append(dict(orbit=[i,j,t,s],code=code,row=k,slack=enc(F(z,q))))
                    total_orbits+=1; repeats+=rep; forbidden+=bad
            check(codes==old['codes'], 'every original value code')
            check(shell_total==g[j], 'all third supports counted')
            entries.append(dict(i=i,j=j,t=ts,s=ss,inside=inside,outside=outside,codes=codes))
        bounds()
    check(len(d['coefficient_entries'])==4761 and total_orbits==1500625, 'complete original enumeration')
    check(repeats==205 and forbidden==10232 and len(allclasses)==271950, 'all source cases')
    expected_support={(r,68,r,0) for r in range(5,69)}|{(68,r,r,0) for r in range(5,69)}|{(68,68,68,68-r) for r in range(5,69)}
    check(set(retained)==expected_support and len(retained)==190 and set(retained.values())=={1}, 'exact support exhaustion')
    # Audit the triangular manuscript system independently of the saved elimination.
    fixedq=[F(z,q) for z in fixed]
    check(fixedq==[F(N)]+[2*z for z in c[1:]], 'row zero and both repetitions, null rows')
    expectedA=[[0]*64 for _ in range(69)]
    for i in range(5,69):
        expectedA[i][i-5]=C(956-i,68)
        if i<68:
            H=C(68,i)*C(888,i)
            expectedA[68][i-5]=2*H
            check(g[i]*C(956-i,68)==g[68]*H, 'binomial counting identity')
    check(A==expectedA==d['contraction_matrix'], 'all 4416 small coefficients')
    check(list(map(enc,fixedq))==d['fixed_contributions'], 'all fixed terms')
    rhs=[N*c[i]-fixedq[i] for i in range(69)]
    check(list(map(enc,rhs))==d['contraction_rhs'], 'all rhs')
    residuals=[F(lhs[i],q)-N*c[i] for i in range(69)]
    check(residuals==[0]*69 and list(map(enc,residuals))==d['contraction_residuals']==v['contraction_residuals'], 'all 69 original residuals')
    # Replay the exact saved algorithm, never obtain an alternative candidate.
    E=[[F(z) for z in row]+[rhs[i]] for i,row in enumerate(A)]
    ops=iter(d['operations']); pivots=[]; r=0; maxbits=max(q.bit_length(),*(abs(z).bit_length() for z in nums))
    for col in range(64):
        pr=next((k for k in range(r,69) if E[k][col]),None)
        check(pr is not None, 'positive triangular pivot')
        if pr!=r:
            check(next(ops)==['swap',r,pr], 'saved first pivot swap')
            E[r],E[pr]=E[pr],E[r]
        z=E[r][col]
        check(next(ops)==['divide',r,enc(z)], 'saved pivot divide')
        E[r]=[a/z for a in E[r]]; R['elimination_updates']+=65
        for k in range(r+1,69):
            z=E[k][col]
            if z:
                check(next(ops)==['subtract',k,r,enc(z)], 'saved elimination subtract')
                E[k]=[a-z*b for a,b in zip(E[k],E[r])]; R['elimination_updates']+=65
        maxbits=max(maxbits,*(max(abs(a.numerator).bit_length(),a.denominator.bit_length()) for row in E for a in row))
        pivots.append(col); r+=1
    check(next(ops,None) is None and d['inconsistent_rows']==[], 'all operations exhausted')
    check([[enc(z) for z in row] for row in E]==d['echelon'], 'all saved echelon entries')
    check(pivots==d['pivots'] and r==d['rank']==64, 'rank and uniqueness')
    check(R['elimination_updates']==d['elimination_updates']==8255, 'elimination work')
    check(all(sum(a*b for a,b in zip(row,x))==rhs[i] for i,row in enumerate(A)), 'complete unique solution substitution')
    rebuilt_patterns=[[i,j,c,n,list(sg)] for (i,j,c,sg),n in sorted(patterns.items())]
    check(rebuilt_patterns==d['scalar_patterns'] and failures==d['scalar_failures']==v['scalar_failures']==[1,0,0], 'all scalar slacks and signs')
    failure=negative_rows[0]
    check(len(negative_rows)==1 and failure['orbit']==[68,68,68,0] and failure['slack']==enc(x[-1]), 'sole mathematical failure')
    check(d['first_scalar_failure']==dict(i=68,j=68,code=133,row=0,slack=enc(x[-1])), 'constructor first failure')
    check(v['first_original_failure']==[68,68,68,0,133,0], 'verifier first failure')
    for name, val in dict(entries=total_orbits,scalar_rows=3*total_orbits,retained_classes=64,
                          retained_original_entries=190,rank=64,repeated_entries=repeats,
                          forbidden_entries=forbidden,source_classes=len(allclasses),
                          negative_coordinate=enc(x[-1]),pair68_fraction_of_nonzero_mass=enc(rho),
                          rho_bound_required=[2,3],rho_millionth_floor=7919,
                          negative_to_c68_millionth_floor=(x[-1]/c[68]).numerator*10**6//(x[-1]/c[68]).denominator,
                          construction_feasible=False,max_value_bits=d['max_value_bits'],
                          presentation_visits_combined=18007500).items():
        check(v[name]==val, 'complete original verifier mathematical field: '+name)
    check(not d['construction_feasible'], 'signed solution not feasible')
    check(d['entries']==total_orbits and d['classes_count']==len(allclasses) and d['scalar_rows']==3*total_orbits, 'constructor coverage counts')
    check(d['presentation_visits']==R['presentation_visits']==9003750, 'complete presentation work')
    valuebits=max(q.bit_length(),*(abs(z).bit_length() for z in nums))
    check(valuebits==d['max_value_bits'] and maxbits<=262144, 'value and elimination rational bounds')
    R.update(stage='complete',N=N,M=enc(M),alpha=enc(alpha),pairs=list(map(enc,c)),
             retained_classes=list(map(list,keys)),retained_original_entries=sorted(map(list,retained)),
             coefficient_entries=entries,contraction_matrix=A,fixed_contributions=list(map(enc,fixedq)),
             contraction_rhs=list(map(enc,rhs)),candidate=list(map(enc,x)),rank=64,
             contraction_residuals=list(map(enc,residuals)),value_denominator=q,value_numerators=nums,
             scalar_patterns=rebuilt_patterns,scalar_failures=failures,negative_rows=negative_rows,
             rho=enc(rho),rho_required=[2,3],entries=total_orbits,scalar_rows=3*total_orbits,
             source_classes=len(allclasses),repeated_entries=repeats,forbidden_entries=forbidden,
             max_value_bits=valuebits,max_elimination_and_value_bits=maxbits,
             verdict='L106 restricted obstruction retained; no unrestricted feasibility conclusion')
    bounds()
    OUT.write_text(json.dumps(R,separators=(',',':'))+'\n')
    output_bytes=OUT.stat().st_size
    check(output_bytes<=256*2**20, 'fresh certificate <= 256 MiB')
    print('Retained L106: 64 classes; rank 64; 190 original support entries.')
    print('Complete coverage:',total_orbits,'orbits;',3*total_orbits,'scalar rows; 69/69 contractions zero.')
    print('Mathematical failures [nonnegative,upper,lower]:',failures,'at (68,68,68,0).')
    print('rho in [7919,7920)/10^6; required >= 2/3; reconstruction failures:',len(R['failures']))
    print('Checks:',R['checks'],'; visits:',R['presentation_visits'],'/20000000; elimination:',R['elimination_updates'],'/5000000')
    print('Seconds:',round(R['elapsed_seconds'],2),'/900; peak bytes:',R['peak_live_bytes'],'/1073741824; bits:',maxbits,'/262144; output bytes:',output_bytes,'/268435456')
    print('Certificate:',OUT.relative_to(ROOT))


if __name__ == '__main__':
    try:
        main()
    except BaseException as e:
        R['stage']='incomplete'; R['failures'].append(repr(e))
        OUT.write_text(json.dumps(R,separators=(',',':'))+'\n')
        raise

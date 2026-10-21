"""Independent eight-region reconstruction; imports no construction routine."""
import hashlib
import itertools
import json
import resource
import sys
import time
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
B=Path(__file__).parent
ROOT=B.parent.parent
OUT=B/'fixed-pair-shared-scalar-verification.json'


@lru_cache(None)
def choose(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k)) if 0<=k<=n else 0


def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(2**20),b''): h.update(b)
    return h.hexdigest()


def enc(x): return [x.numerator,x.denominator]


def main():
    data=json.loads((B/'fixed-pair-shared-scalar-results.json').read_text())
    checks=0; implementation_failures=[]
    def check(ok,label,context=None):
        nonlocal checks
        checks+=1
        if not ok:
            implementation_failures.append([label,context])
            OUT.write_text(json.dumps(dict(stage='incomplete',checks=checks,
                implementation_failures=implementation_failures))+'\n')
            raise AssertionError((label,context))
    check(data['stage']=='complete_candidate_substitution','complete candidate')
    for p,h in data['input_sha256'].items(): check(digest(ROOT/p)==h,'frozen input',p)
    q=data['value_denominator']; nums=data['value_numerators']; P=nums[1:70]
    keys=[tuple(k) for k in data['retained_classes']]
    check(len(keys)<=1024 and keys==sorted(set(keys)),'bounded lexicographic classes')
    idx={k:r for r,k in enumerate(keys)}
    lp=json.loads((B/'delsarte-lp-results.json').read_text())
    g=[choose(68,i)*choose(956,i) for i in range(69)]
    N=65537**28//2**128+1
    original=[F(1)]+[F(0)]*4+[F(r['numerator'],r['denominator'])/(2*g[i])
              for i,r in zip(range(5,69),lp['exact']['primal'])]
    M=sum(g[i]*original[i] for i in range(69)); alpha=F(N-1)/(M-1)
    cp=[alpha*p+(1-alpha)*int(i==0) for i,p in enumerate(original)]
    check(M==(F(choose(1024,64),choose(68,64))+1)/2,'original objective')
    check(N==data['N'] and F(*data['M'])==M and F(*data['alpha'])==alpha,'N and mixture')
    check(q>0 and cp==[F(x,q) for x in P]==[F(*x) for x in data['pairs']],'all fixed pairs')
    check(cp[0]==1 and cp[1:5]==[0]*4 and sum(g[i]*P[i] for i in range(69))==q*N,
          'normalization forbidden pairs objective')
    x=[F(*v) for v in data['candidate']]
    check(len(nums)==70+len(keys) and nums[0]==0,'value codebook length')
    check([F(v,q) for v in nums[70:]]==x,'candidate codebook')
    # Verify every saved rational row operation, including pivot choices.
    A=data['contraction_matrix']; fixed=list(map(lambda v:F(*v),data['fixed_contributions']))
    rhs=[N*cp[i]-fixed[i] for i in range(69)]
    check([enc(v) for v in rhs]==data['contraction_rhs'],'complete rhs')
    R=[[F(a) for a in row]+[v] for row,v in zip(A,rhs)]
    opiter=iter(data['operations']); pivotcols=[]; row=0; updates=0
    for col in range(len(keys)):
        pivot=next((i for i in range(row,69) if R[i][col]),None)
        if pivot is None: continue
        if pivot!=row:
            check(next(opiter)==['swap',row,pivot],'first available pivot swap')
            R[row],R[pivot]=R[pivot],R[row]
        v=R[row][col]
        check(next(opiter)==['divide',row,enc(v)],'normalization operation')
        R[row]=[a/v for a in R[row]]; updates+=len(R[row])
        for i in range(row+1,69):
            v=R[i][col]
            if v:
                check(next(opiter)==['subtract',i,row,enc(v)],'subtraction operation')
                R[i]=[a-v*b for a,b in zip(R[i],R[row])]; updates+=len(R[i])
        pivotcols.append(col); row+=1
    check(next(opiter,None) is None,'all operations exhausted')
    check([list(map(enc,r)) for r in R]==data['echelon'],'complete echelon identity')
    check(pivotcols==data['pivots'] and row==data['rank'],'rank and pivots')
    check(updates==data['elimination_updates'] and updates<=5000000,'elimination work')
    check(all(x[k]==0 for k in range(len(keys)) if k not in pivotcols),'nonpivots fixed zero')
    for i in range(69): check(sum(a*v for a,v in zip(A[i],x))==rhs[i],'original small equation',i)
    visits=entries=repeated=forbidden=retained_entries=0
    patterns={}; seenclasses=set(); seenretained=set()
    lhs=[0]*69; rebuiltA=[[0]*len(keys) for _ in range(69)]; rebuiltFixed=[0]*69
    atoms_permutations=[(1<<a,1<<b,1<<c) for a,b,c in itertools.permutations(range(3))]
    expected_entries=iter(itertools.product(range(69),repeat=2))
    first=None; failures=[0,0,0]; rows=0
    for e in data['coefficient_entries']:
        i,j=e['i'],e['j']; check((i,j)==next(expected_entries),'complete ordered entry sequence')
        ts=range(max(0,i+j-68),min(i,j)+1)
        ss=range(max(0,i+j-956),min(i,j)+1)
        check(e['t']==list(ts) and e['s']==list(ss),'all original ranges')
        inside=[factorial(68)//(factorial(t)*factorial(i-t)*factorial(j-t)*factorial(68-i-j+t)) for t in ts]
        outside=[factorial(956)//(factorial(s)*factorial(i-s)*factorial(j-s)*factorial(956-i-j+s)) for s in ss]
        check(inside==[a*choose(68,i) for a in e['inside']],'inside multinomial coefficients')
        check(outside==[a*choose(956,i) for a in e['outside']],'outside multinomial coefficients')
        codes=iter(e['codes']); total=0
        for ti,t in enumerate(ts):
            for si,s in enumerate(ss):
                atoms=[956-i-j+s,t,i-s,j-t,j-s,i-t,s,68-i-j+t]
                check(min(atoms)>=0 and sum(atoms)==1024,'complete eight-region partition')
                c=next(codes)
                for a,b,z in atoms_permutations:
                    da=atoms[a]+atoms[a|z]; db=atoms[a]+atoms[a|b]
                    dh=atoms[b]+atoms[a|b]; tp=atoms[a]; sp=atoms[b|z]
                    check(dh==da+db-tp-sp and tp-sp==t-s,'actual presentation and invariant')
                    check(max(0,da+db-68)<=tp<=min(da,db) and
                          max(0,da+db-956)<=sp<=min(da,db),'presented actual ranges')
                    ds=tuple(sorted((da,db,dh))); key=(*ds,tp-sp)
                    if any(0<k<5 for k in ds): expected=0
                    elif ds[0]==0:
                        check(ds[1]==ds[2] and tp==sp,'Boolean repetition')
                        expected=1+ds[1]
                    elif ds[1:]==(68,68):
                        check(key in idx,'retained support exhausted',list(key))
                        expected=70+idx[key]
                    else: expected=0
                    check(c==expected,'complete original lift and source equality')
                    visits+=1
                h=i+j-t-s; ds=tuple(sorted((i,j,h))); seenclasses.add((*ds,t-s))
                if ds[0]==0: repeated+=1
                if any(0<k<5 for k in ds): forbidden+=1
                if c>=70:
                    retained_entries+=1; seenretained.add((*ds,t-s))
                product=inside[ti]*outside[si]
                check(product%g[i]==0,'integral original coefficient')
                D=product//g[i]
                check(D==e['inside'][ti]*e['outside'][si] and D>0,'each original D')
                total+=D
                if c: lhs[i]+=D*nums[c]
                if c>=70: rebuiltA[i][c-70]+=D
                elif c: rebuiltFixed[i]+=D*nums[c]
                # Every original scalar row is substituted; factored records
                # avoid repeated giant numerators without omitting any row.
                pattern=(i,j,c)
                if pattern not in patterns:
                    slacks=[nums[c],P[i]-nums[c],q+nums[c]-P[i]-P[j]]
                    signs=[(v>0)-(v<0) for v in slacks]
                    patterns[pattern]=[0,signs]
                patterns[pattern][0]+=1
                for k,sgn in enumerate(patterns[pattern][1]):
                    if sgn<0:
                        failures[k]+=1
                        if first is None: first=[i,j,t,s,c,k]
                rows+=3; entries+=1
        check(next(codes,None) is None,'every lift code read')
        check(total==g[j],'whole third-support shell count')
        check(entries<=1501000 and rows<=4600000,'entry and scalar caps')
        check(visits+data['presentation_visits']<=20000000,'combined presentation cap')
        check(time.time()-data['started']<=900,'combined wall cap')
        mem=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
        check(mem<=2**30,'live memory cap')
    check(next(expected_entries,None) is None,'all 4761 source entries')
    check(entries==data['entries']==1500625 and rows==data['scalar_rows']==4501875,'full orbit and scalar coverage')
    check(repeated==205 and forbidden==10232,'every repetition and forbidden entry')
    check(len(seenclasses)==data['classes_count'] and seenretained==set(keys),'all source classes and support')
    check(rebuiltA==A and [F(v,q) for v in rebuiltFixed]==fixed,'complete independently rebuilt system')
    rebuiltPatterns=[[i,j,c,n,signs] for (i,j,c),(n,signs) in sorted(patterns.items())]
    check(rebuiltPatterns==data['scalar_patterns'] and failures==data['scalar_failures'],'every factored scalar slack and verdict')
    residuals=[F(lhs[i],q)-N*cp[i] for i in range(69)]
    check(list(map(enc,residuals))==data['contraction_residuals'],'all original residuals')
    check(all(v==0 for v in residuals),'all 69 contractions')
    maxbits=max(q.bit_length(),*(abs(v).bit_length() for v in nums))
    check(maxbits==data['max_value_bits'] and maxbits<=262144,'complete value bits')
    check(data['construction_feasible']==(not any(failures)),'candidate verdict')
    # Independent closed-form sanity check, not a replacement for full lift.
    closed=[F(N-2)*cp[i]/choose(956-i,68) for i in range(5,68)]
    closed.append(F(N-2)*(3*cp[68]-F(2*(N-1),g[68]))/choose(888,68))
    check(keys==[(i,68,68,i) for i in range(5,69)] and x==closed,'all closed-form solution coordinates')
    rho=F(g[68],N-1)*cp[68]
    check(0<rho<F(2,3) and x[-1]<0,'strict restricted-support obstruction')
    result=dict(stage='complete',checks=checks,implementation_failures=[],
        certificate_sha256=digest(B/'fixed-pair-shared-scalar-results.json'),
        entries=entries,scalar_rows=rows,presentation_visits_combined=visits+data['presentation_visits'],
        retained_classes=len(keys),retained_original_entries=retained_entries,rank=row,
        repeated_entries=repeated,forbidden_entries=forbidden,source_classes=len(seenclasses),
        scalar_failures=failures,first_original_failure=first,
        contraction_residuals=list(map(enc,residuals)),construction_feasible=not any(failures),
        negative_coordinate=enc(x[-1]),pair68_fraction_of_nonzero_mass=enc(rho),
        negative_coordinate_formula='(N-2)*(3*c68-2*(N-1)/g68)/binomial(888,68)',
        rho_bound_required=enc(F(2,3)),rho_millionth_floor=rho.numerator*10**6//rho.denominator,
        negative_to_c68_millionth_floor=(x[-1]/cp[68]).numerator*10**6//(x[-1]/cp[68]).denominator,
        max_value_bits=maxbits,peak_live_bytes=mem,elapsed_seconds_combined=time.time()-data['started'])
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    check(sum(p.stat().st_size for p in B.glob('fixed-pair-shared-scalar-*.json'))<=256*2**20,'certificate output cap')
    print('Verified:',entries,'orbits;',rows,'scalar rows;',sum(v==0 for v in residuals),'/69 contractions')
    print('Source classes:',len(seenclasses),'; retained:',len(keys),'; rank:',row,'; retained original entries:',retained_entries)
    print('Scalar failures [nonnegative,upper,lower]:',failures,'; first original failure:',first)
    print('rho millionth floor:',result['rho_millionth_floor'],'; required rho >= 2/3; negative coordinate/c68 millionth floor:',result['negative_to_c68_millionth_floor'])
    print('Checks:',checks,'; reconstruction failures: 0; combined visits:',result['presentation_visits_combined'],'/20000000')
    print('Elapsed:',round(result['elapsed_seconds_combined'],2),'/900; peak bytes:',mem,'/1073741824; max value bits:',maxbits,'/262144')
    print('Certificate:',OUT)


if __name__=='__main__': main()

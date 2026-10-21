"""Rebuild every orbit from eight atoms; imports no construction routines."""
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
OUT=B/'fixed-pair-row-capacity-verification.json'


@lru_cache(None)
def choose(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k)) if 0<=k<=n else 0


def main():
    data=json.loads((B/'fixed-pair-row-capacity-results.json').read_text())
    failures=[]
    checks=0
    def check(ok,label,context=None):
        nonlocal checks
        checks+=1
        if not ok:
            failures.append([label,context])
            raise AssertionError((label,context))
    check(data['stage']=='complete','completed constructor')
    for path,expected in data['input_sha256'].items():
        h=hashlib.sha256()
        with (ROOT/path).open('rb') as f:
            for chunk in iter(lambda:f.read(2**20),b''): h.update(chunk)
        check(h.hexdigest()==expected,'frozen input',path)
    lp=json.loads((B/'delsarte-lp-results.json').read_text())
    g=[choose(68,i)*choose(956,i) for i in range(69)]
    endpoint=[F(1)]+[F(0)]*4+[
        F(r['numerator'],r['denominator'])/(2*g[i])
        for i,r in zip(range(5,69),lp['exact']['primal'])]
    N=65537**28//2**128+1
    M=sum(g[i]*endpoint[i] for i in range(69))
    alpha=F(N-1)/(M-1)
    q=data['denominator']; P=data['pair_numerators']
    cp=[alpha*p+(1-alpha)*int(i==0) for i,p in enumerate(endpoint)]
    check(M==(F(choose(1024,64),choose(68,64))+1)/2,'original objective')
    check(N==data['N'] and F(*data['M'])==M and F(*data['alpha'])==alpha,
          'exact N and mixture')
    check(endpoint==[F(*p) for p in data['endpoint_pairs']],'original pairs')
    check(q>0 and len(P)==69 and [F(x,q) for x in P]==cp,'all fixed pairs')
    check(sum(g[i]*P[i] for i in range(69))==N*q,'exact objective N')
    check(P[0]==q and P[1:5]==[0]*4 and all(0<=x<=q for x in P),'pair bounds')
    def endpoint_value(desc):
        if desc[0]=='z':
            check(desc==['z'],'zero descriptor'); return 0
        if desc[0]=='p':
            check(len(desc)==2,'pair descriptor'); return P[desc[1]]
        check(desc[0]=='l' and len(desc)==3,'lower-row descriptor')
        return P[desc[1]]+P[desc[2]]-q
    perms=list(itertools.permutations(range(3)))
    presentation_indices=[(1<<x,1<<y,1<<z) for x,y,z in perms]
    sums=[[0,0,0,0] for _ in range(69)]
    row_repeats=[[] for _ in range(69)]
    total=visits=repeated=forbidden=0
    expected_entries=iter(itertools.product(range(69),repeat=2))
    maxbits=q.bit_length()
    for e in data['coefficient_entries']:
        i,j=e['i'],e['j']
        check((i,j)==next(expected_entries),'complete ordered entries')
        ts=range(max(0,i+j-68),min(i,j)+1)
        ss=range(max(0,i+j-956),min(i,j)+1)
        check(e['t']==list(ts) and e['s']==list(ss),'complete t,s ranges',[i,j])
        # Source multinomials divided by the pair orbit sizes, independently
        # of the constructor's four binomial-choice factors.
        inside=[factorial(68)//(factorial(t)*factorial(i-t)*factorial(j-t)*
                  factorial(68-i-j+t)) for t in ts]
        outside=[factorial(956)//(factorial(s)*factorial(i-s)*factorial(j-s)*
                   factorial(956-i-j+s)) for s in ss]
        gi=choose(68,i); go=choose(956,i)
        check(all(a==b*gi for a,b in zip(inside,e['inside'])) and
              len(inside)==len(e['inside']),'inside source factors')
        check(all(a==b*go for a,b in zip(outside,e['outside'])) and
              len(outside)==len(e['outside']),'outside source factors')
        records={r[0]:r for r in e['h_records']}
        check(len(records)==len(e['h_records']),'unique h records')
        observed={}
        for ti,t in enumerate(ts):
            for si,s in enumerate(ss):
                atoms=[956-i-j+s,t,i-s,j-t,j-s,i-t,s,68-i-j+t]
                check(min(atoms)>=0 and sum(atoms)==1024,'eight atom partition')
                # Reconstruct all three words, all distances, t and s by
                # membership in these actual atoms, including every order.
                lower=0; upper=q
                distances=[]
                for x,y,z in presentation_indices:
                    a=atoms[x]+atoms[x|z]
                    b=atoms[x]+atoms[x|y]
                    c=atoms[y]+atoms[x|y]
                    tp=atoms[x]; sp=atoms[y|z]
                    check(c==a+b-tp-sp and tp-sp==t-s,'actual source reanchoring')
                    check(0<=a<=68 and 0<=b<=68 and
                          max(0,a+b-68)<=tp<=min(a,b) and
                          max(0,a+b-956)<=sp<=min(a,b),'permuted actual orbit')
                    lower=max(lower,P[a]+P[b]-q)
                    upper=min(upper,P[a])
                    distances.append((a,b,c))
                    visits+=1
                h=distances[0][2]
                check(distances[0]==(i,j,i+j-t-s),'original distance reconstruction')
                ds=(i,j,h)
                if any(0<k<5 for k in ds):
                    forbidden+=1
                    check(lower<=0<=upper,'forbidden zero scalar interval')
                    lower=upper=0
                elif min(ds)==0:
                    _,b,c=sorted(ds)
                    check(b==c and lower<=P[b]<=upper,'Boolean pair interval')
                    lower=upper=P[b]
                check(lower<=upper,'nonempty original scalar interval')
                r=records[h]
                check(endpoint_value(r[3])==lower and endpoint_value(r[4])==upper,
                      'exact endpoint intersection',[i,j,t,s])
                source=inside[ti]*outside[si]
                check(source%g[i]==0,'integer source coefficient')
                D=source//g[i]
                check(D==e['inside'][ti]*e['outside'][si] and D>0,
                      'each original D coefficient')
                a0,c0=observed.get(h,(0,0)); observed[h]=(a0+1,c0+D)
                sums[i][0]+=D*lower; sums[i][1]+=D*upper
                sums[i][2]+=D; sums[i][3]+=1
                if min(ds)==0:
                    repeated+=1
                    check(t==s and D==(g[j] if i==0 else 1),'repeated coefficient')
                    if i>0: row_repeats[i].append([j,t,s,D])
                total+=1
        check(set(observed)==set(records),'full lossless interval lift')
        check(all(observed[h]==(r[1],r[2]) for h,r in records.items()),
              'all factored endpoint multiplicities')
        check(sum(c for a,c in observed.values())==g[j],'complete shell count')
        check(time.time()-data['started']<data['caps']['seconds'],'combined time cap')
        check(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<2**30,'live memory cap')
    check(next(expected_entries,None) is None,'all ordered entries present')
    rows=[]
    for i,r in enumerate(data['rows']):
        lo,hi,count,number=sums[i]; rhs=N*P[i]
        check(r['i']==i and r['lower_numerator']==lo and r['upper_numerator']==hi
              and r['required_numerator']==rhs,'complete exact row',[i])
        check(count==choose(1024,68)==r['third_supports'] and number==r['entries'],
              'full row coverage',i)
        check(r['lower_slack']==rhs-lo and r['upper_slack']==hi-rhs,
              'both exact comparisons',i)
        check(r['repetitions']==row_repeats[i],'every repetition record',i)
        check(i==0 or row_repeats[i]==[[0,0,0,1],[i,i,i,1]],'both repeated words',i)
        check(r['passes']==(lo<=rhs<=hi),'row verdict',i)
        maxbits=max(maxbits,lo.bit_length(),hi.bit_length(),rhs.bit_length())
        rows.append(dict(i=i,lower_numerator=lo,required_numerator=rhs,
                         upper_numerator=hi,passes=lo<=rhs<=hi,
                         lower_slack=rhs-lo,upper_slack=hi-rhs))
    check(len(rows)==69 and total==data['entries']==1500625,'all rows and entries')
    check(repeated==data['repeated_entries']==205 and
          forbidden==data['forbidden_entries']==10232,'special entry counts')
    check(visits==data['visits']==9003750 and 2*visits<=20000000,'combined visits cap')
    check(maxbits<=262144,'integer bit cap')
    check(data['max_integer_bits']==maxbits,'maximum component bits')
    check(data['summary']==dict(rows=69,passing=sum(r['passes'] for r in rows),
                               failing=[r['i'] for r in rows if not r['passes']]),'summary')
    results=dict(verified=not failures,failures=failures,checks=checks,
                 entries=total,visits=visits,combined_visits=2*visits,
                 repeated_entries=repeated,forbidden_entries=forbidden,
                 rows=rows,denominator=q,max_integer_bits=maxbits,
                 peak_live_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                 total_elapsed_seconds=time.time()-data['started'],
                 construction_sha256=hashlib.sha256((B/'fixed-pair-row-capacity-results.json').read_bytes()).hexdigest())
    OUT.write_text(json.dumps(results,separators=(',',':'))+'\n')
    actual_bytes=OUT.stat().st_size+(B/'fixed-pair-row-capacity-results.json').stat().st_size
    check(actual_bytes<256*2**20,'combined output cap')
    print('Independent verification:',not failures,'; exact checks:',checks,
          '; rows passing:',sum(r['passes'] for r in rows),'/69')
    print('Original entries:',total,'/1501000; combined visits:',2*visits,'/20000000')
    print('Elapsed seconds:',round(results['total_elapsed_seconds'],2),'/900; peak bytes:',
          results['peak_live_bytes'],'/1073741824; output bytes:',actual_bytes,'/268435456')
    print('Maximum integer bits:',maxbits,'/262144; failures:',len(failures),'; certificate:',OUT)


if __name__=='__main__':
    main()

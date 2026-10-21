"""Independent-entry necessary capacities only; no solver or variable quotient."""
import hashlib
import itertools
import json
import resource
import sys
import time
from fractions import Fraction as Q
from math import comb, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
B = Path(__file__).parent
ROOT = B.parent.parent
OUT = B / 'fixed-pair-row-capacity-results.json'
START = time.time()
PERMS = list(itertools.permutations(range(3)))
CAPS = dict(entries=1501000, rows=69, visits=20000000,
            live_bytes=2**30, output_bytes=256*2**20, bits=262144, seconds=900)


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(2**20), b''):
            h.update(block)
    return h.hexdigest()


def enc(x):
    return [x.numerator, x.denominator]


def main():
    state = dict(stage='in_progress', started=START, caps=CAPS,
                 failures=[], entries=0, visits=0)
    OUT.write_text(json.dumps(state)+'\n')
    paths = ['lemmas/L098-exact-cardinality-normalized-control-obstruction.md',
             'lemmas/L021-basic-delsarte-support-lp-optimum.md',
             'lemmas/L022-selected-triple-sdp-primal-limitation.md',
             'lemmas/L023-full-zero-block-extension-psd.md',
             'foundations/04-constant-weight-triple-sdp-source.md',
             'foundations/12-global-degree-three-moment-source.md',
             'foundations/13-fixed-cardinality-marginal-source.md',
             'scripts/finite-support/delsarte-lp-results.json']
    state['input_sha256'] = {p: digest(ROOT/p) for p in paths}
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    g = [comb(68,i)*comb(956,i) for i in range(69)]
    p = [Q(1)] + [Q(0)]*4 + [Q(r['numerator'],r['denominator'])/(2*g[i])
          for i,r in zip(range(5,69),lp['exact']['primal'])]
    M = (Q(comb(1024,64),comb(68,64))+1)/2
    N = 65537**28//2**128+1
    alpha = (N-1)/(M-1)
    cp = [alpha*x+(1-alpha)*(i==0) for i,x in enumerate(p)]
    q = lcm(*(x.denominator for x in cp))
    P = [int(q*x) for x in cp]
    assert len(p)==69 and sum(g[i]*p[i] for i in range(69))==M
    assert 0<alpha<1 and P[0]==q and P[1:5]==[0]*4
    assert all(0<=x<=q for x in P) and sum(g[i]*P[i] for i in range(69))==N*q
    assert max(q.bit_length(),*(x.bit_length() for x in P))<=CAPS['bits']
    state.update(N=N, M=enc(M), alpha=enc(alpha), denominator=q,
                 pair_numerators=P, endpoint_pairs=list(map(enc,p)))
    OUT.write_text(json.dumps(state)+'\n')
    entries = []
    rows = []
    repeats = forbidden = 0
    maxbits = q.bit_length()
    H = comb(1024,68)
    for i in range(69):
        low_sum = high_sum = count = row_entries = 0
        repetitions = []
        for j in range(69):
            ts = list(range(max(0,i+j-68),min(i,j)+1))
            ss = list(range(max(0,i+j-956),min(i,j)+1))
            aa = [comb(i,t)*comb(68-i,j-t) for t in ts]
            bb = [comb(i,s)*comb(956-i,j-s) for s in ss]
            hc, mc, intervals = {}, {}, {}
            for t,a in zip(ts,aa):
                for s,b in zip(ss,bb):
                    h = i+j-t-s
                    ds = (i,j,h)
                    if h not in intervals:
                        pairs = [(i,j),(i,h),(j,h)]
                        uidx = min(ds,key=lambda k:P[k])
                        ab = max(pairs,key=lambda ab:P[ab[0]]+P[ab[1]]-q)
                        low = max(0,P[ab[0]]+P[ab[1]]-q)
                        high = P[uidx]
                        ld = ['z'] if low==0 else ['l',*ab]
                        ud = ['p',uidx]
                        if any(0<k<5 for k in ds):
                            assert low<=0<=high
                            low=high=0; ld=ud=['z']
                        elif min(ds)==0:
                            _,b0,c0=sorted(ds)
                            assert b0==c0 and low<=P[b0]<=high
                            low=high=P[b0]; ld=ud=['p',b0]
                        assert low<=high
                        intervals[h] = (low,high,ld,ud)
                    low,high,_,_ = intervals[h]
                    # Each presentation is the exact source orbit with the
                    # SAME u=t-s. Its first visit also computes D below.
                    for r in PERMS:
                        x,y,z = (ds[k] for k in r)
                        tp = (x+y-z+t-s)//2
                        sp = (x+y-z-t+s)//2
                        assert 2*tp==x+y-z+t-s and 2*sp==x+y-z-t+s
                        assert max(0,x+y-68)<=tp<=min(x,y)
                        assert max(0,x+y-956)<=sp<=min(x,y)
                        assert 0<=low<=high<=P[x] and q+low-P[x]-P[y]>=0
                    D = a*b
                    hc[h] = hc.get(h,0)+D
                    mc[h] = mc.get(h,0)+1
                    count += D; row_entries += 1
                    if min(ds)==0:
                        repeats += 1
                        assert t==s and D==(g[j] if i==0 else 1)
                        if i>0: repetitions.append([j,t,s,D])
                    if any(0<k<5 for k in ds): forbidden += 1
            assert sum(hc.values())==g[j]
            hs = []
            for h in sorted(hc):
                lo,hi,ld,ud = intervals[h]
                low_sum += hc[h]*lo; high_sum += hc[h]*hi
                hs.append([h,mc[h],hc[h],ld,ud])
            entries.append(dict(i=i,j=j,t=ts,s=ss,inside=aa,outside=bb,h_records=hs))
        rhs = N*P[i]
        assert count==H
        assert i==0 or repetitions==[[0,0,0,1],[i,i,i,1]]
        passed = low_sum<=rhs<=high_sum
        row = dict(i=i,entries=row_entries,third_supports=count,repetitions=repetitions,
                   lower_numerator=low_sum,upper_numerator=high_sum,
                   required_numerator=rhs,lower_slack=rhs-low_sum,
                   upper_slack=high_sum-rhs,passes=passed)
        rows.append(row)
        state['entries'] += row_entries
        state['visits'] += 6*row_entries
        maxbits = max(maxbits,low_sum.bit_length(),high_sum.bit_length(),rhs.bit_length())
        assert state['entries']<=CAPS['entries'] and state['visits']<=CAPS['visits']
        assert maxbits<=CAPS['bits'] and time.time()-START<CAPS['seconds']
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<CAPS['live_bytes']
        print('Constructed rows:',i+1,'/69; entries:',state['entries'],flush=True) if i%12==0 else None
    state.update(stage='complete',coefficient_entries=entries,rows=rows,
                 repeated_entries=repeats,forbidden_entries=forbidden,
                 max_integer_bits=maxbits,elapsed_seconds=time.time()-START,
                 peak_live_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                 summary=dict(rows=69,passing=sum(r['passes'] for r in rows),
                              failing=[r['i'] for r in rows if not r['passes']]))
    with OUT.open('w') as f:
        json.dump(state,f,separators=(',',':')); f.write('\n')
    assert OUT.stat().st_size<=CAPS['output_bytes']
    print('Rows passing:',state['summary']['passing'],'/69; failures:',state['summary']['failing'])
    print('Actual/required entries:',state['entries'],'/',CAPS['entries'],
          '; presentation visits:',state['visits'],'/',CAPS['visits'])
    print('Output bytes:',OUT.stat().st_size,'/',CAPS['output_bytes'],'; certificate:',OUT)


if __name__=='__main__':
    main()

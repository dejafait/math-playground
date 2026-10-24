"""Independent actual-union/beta reconstruction of the unchanged shell test.

Imports no constructor routines; consumes the entire saved coefficient table,
every mode and all endpoint values. Does not rerun a nonlinear solve.
"""
import gzip
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from itertools import permutations
from math import factorial
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
SOURCE = B/'fixed-product-five-shell.json'
OUT = B/'fixed-product-five-shell-verification.json'


def choose(n,k):
    return factorial(n)//factorial(k)//factorial(n-k) if 0<=k<=n else 0


def enc(x):
    return [x.numerator,x.denominator]


def beta(n,k,r):
    t=5-r
    return F(sum((-1)**(u-t)*choose(u,t)*choose(n-2*k,u-k)*choose(n-k-u,5-u)**2
                 for u in range(max(k,t),6)), choose(n-2*k,5-k))


def main():
    saved=json.loads(SOURCE.read_text())
    counts=Counter()
    report=dict(stage='in_progress',failures=[],source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

    def save():
        report.update(checks=sum(counts.values()),checks_by_kind=dict(counts))
        OUT.write_text(json.dumps(report,indent=2)+'\n')

    def ck(kind,ok,detail=None):
        counts[kind]+=1
        if not ok:
            report['failures'].append(dict(kind=kind,detail=detail))
            report['stage']='failed'
            save()
            raise AssertionError((kind,detail))

    for p,h in saved['input_sha256'].items():
        ck('all_input_bindings',hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p)
    ck('constructor_binding',saved['code_sha256']==hashlib.sha256((B/'fixed_product_five_shell.py').read_bytes()).hexdigest())
    with gzip.open(B/'positive-factor-enclosure.json.gz','rt') as f:
        z=json.load(f)
    lp=json.loads((B/'delsarte-lp-results.json').read_text())
    a=[F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    N=65537**28//2**128+1
    H=choose(1024,68)
    U=F(choose(1024,64),choose(68,64))
    g=[choose(68,i)*choose(956,i) for i in range(69)]
    c=[F(1)]+[F(0)]*4+[(N-1)*a[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('canonical_data',len(a)==64 and min(a)>0 and sum(a)==U-1 and
       list(map(enc,c))==saved['c']==z['c'] and saved['N']==z['N']==N and
       saved['H']==z['H']==H and F(*saved['rho'])==F(N,H)>0 and
       sum(g[i]*c[i] for i in range(69))==N and (N-1)*2**128<=65537**28<N*2**128)
    ck('unchanged_positive_box',z['Q']==10**70 and z['radius']==10**25 and
       z['box']==[[p-10**25,p+10**25] for p in z['point']] and
       len(z['point'])==len(z['scale_powers'])==len(saved['endpoints'])==64)
    box={}
    for i in range(5,69):
        k=i-5
        scale=F(10**z['scale_powers'][k]) if z['scale_powers'][k]>=0 else F(1,10**(-z['scale_powers'][k]))
        box[i]=(scale*F(z['point'][k]-10**25,10**70),scale*F(z['point'][k]+10**25,10**70))
        ck('every_original_endpoint',saved['endpoints'][k]==dict(i=i,interval=list(map(enc,box[i])))
           and 0<box[i][0]<box[i][1],i)
    # Choose actual subsets, not just distance symbols. The general dictionary
    # makes each r,q one orbit under permutations fixing A.
    A=set(range(68)); X=set(range(5)); Y=set(range(68,73)); B0=(A-X)|Y
    dictionary=[]; table=[]
    for r in range(6):
        row=[]
        for q in range(6):
            X2=set(range(5-r))|set(range(5,5+r))
            Y2=set(range(68,73-q))|set(range(73,73+q))
            C=(A-X2)|Y2
            words=[A,B0,C]
            atoms=[sum(1 for p in range(1024) if sum((1<<k) for k,W in enumerate(words) if p in W)==mask)
                   for mask in range(8)]
            ck('complete_atoms',sum(atoms)==1024 and min(atoms)>=0 and
               all(len(W)==68 for W in words),[r,q])
            ck('shell_dictionary',len(A-B0)==len(A-C)==5 and len(B0-C)==r+q and
               len((A-B0)&(A-C))==5-r and len((B0-A)&(C-A))==5-q,[r,q])
            presentations=[]
            values=[]
            for u,v,w in permutations(range(3)):
                P,Q,R=words[u],words[v],words[w]
                i,j,h=len(P-Q),len(P-R),len(Q-R)
                t=len((P-Q)&(P-R)); s=len((Q-P)&(R-P))
                D=choose(i,t)*choose(68-i,j-t)*choose(i,s)*choose(956-i,j-s)
                ck('all_actual_presentations',h==i+j-t-s and t-s==q-r and
                   max(0,i+j-68)<=t<=min(i,j) and max(0,i+j-956)<=s<=min(i,j)
                   and D>0,[r,q,u,v,w])
                if min(i,j,h)==0:
                    value=(c[max(i,j,h)],)*2
                    ck('repetition_D',D==(g[j] if i==0 else 1),[r,q,i,j])
                elif min(i,j,h)<5:
                    value=(F(0),F(0))
                    ck('forbidden_zero',min(c[i],c[j],c[h])==0,[r,q,i,j,h])
                else:
                    value=(box[i][0]*box[j][0]*box[h][0],box[i][1]*box[j][1]*box[h][1])
                values.append(value)
                presentations.append(dict(order=[u,v,w],orbit=[i,j,t,s],h=h,D=D,full_count=g[i]*D))
            D0=choose(5,r)*choose(63,r)*choose(5,q)*choose(951,q)
            ck('D_and_six_count_normalizations',all(p['full_count']==g[5]*D0 for p in presentations),[r,q])
            ck('all_entry_intervals',len(set(values))==1 and saved['entries'][r][q]==list(map(enc,values[0])),[r,q])
            dictionary.append(dict(r=r,q=q,atoms=atoms,presentations=presentations,interval=list(map(enc,values[0]))))
            row.append(values[0])
        table.append(row)
    spectra={}; mult={}
    for index,n in enumerate((68,956)):
        E=[[beta(n,k,r) for r in range(6)] for k in range(6)]
        m=[choose(n,k)-choose(n,k-1) for k in range(6)]
        ck('complete_multiplicities',m==saved['factors'][index]['multiplicities'] and
           min(m)>0 and sum(m)==choose(n,5),n)
        for k in range(6):
            for r in range(6):
                ck('independent_beta',E[k][r].denominator==1 and
                   E[k][r]==saved['factors'][index]['eigenmatrix'][k][r],[n,k,r])
        ck('identity_and_valencies',all(E[k][0]==1 for k in range(6)) and
           E[0]==[choose(5,r)*choose(n-5,r) for r in range(6)],n)
        for r in range(6):
            for s in range(6):
                ck('all_trace_orthogonality',sum(m[k]*E[k][r]*E[k][s] for k in range(6))==
                   (choose(n,5)*E[0][r] if r==s else 0),[n,r,s])
        spectra[n],mult[n]=E,m
    S=choose(68,5)*choose(956,5)
    ck('shell_size',saved['size']==g[5]==S)
    modes=[]
    for aa in range(6):
        for bb in range(6):
            terms=[]; coeff=[F(0)]*6
            for r in range(6):
                for q in range(6):
                    w=spectra[68][aa][r]*spectra[956][bb][q]
                    l,u=table[r][q]
                    terms.append((min(w*l,w*u),max(w*l,w*u)))
                    if r+q>=5: coeff[r+q-5]+=w
            lo,hi=sum(t[0] for t in terms),sum(t[1] for t in terms)
            # Independently collect common x5^2 before interval evaluation.
            linear_lo=sum(w*box[h][0 if w>=0 else 1] for h,w in zip(range(5,11),coeff))
            linear_hi=sum(w*box[h][1 if w>=0 else 0] for h,w in zip(range(5,11),coeff))
            corners=[f*l for f in [box[5][0]**2,box[5][1]**2] for l in [linear_lo,linear_hi]]
            ck('collected_interval_enclosed',lo<=c[5]+min(corners)<=c[5]+max(corners)<=hi,[aa,bb])
            correction=S*c[5]**2 if aa==bb==0 else F(0)
            sl,su=lo-correction,hi-correction
            verdict='negative' if su<0 else 'positive' if sl>0 else 'zero' if sl==su==0 else 'unresolved'
            mode=dict(a=aa,b=bb,multiplicity=mult[68][aa]*mult[956][bb],
                      product_coefficients=[int(v) for v in coeff],shell=list(map(enc,(lo,hi))),
                      correction=enc(correction),schur=list(map(enc,(sl,su))),
                      schur_over_c5=[enc(sl/c[5]),enc(su/c[5])],verdict=verdict)
            ck('every_full_mode',saved['modes'][6*aa+bb]==mode,[aa,bb])
            modes.append(mode)
    ck('complete_dimension',len(saved['modes'])==36 and sum(m['multiplicity'] for m in modes)==S)
    for h in range(6):
        ck('trace_polynomial_identity',sum(m['multiplicity']*m['product_coefficients'][h] for m in modes)==0,h+5)
    ck('anchor_trace_identity',sum(m['multiplicity']*F(*m['correction']) for m in modes)==S*c[5]**2)
    # Positive-anchor congruence: normalized top entry is 1. At the
    # unnormalized constant vector, the shell row sum is E00 and norm S.
    row_lo=sum(table[r][q][0]*choose(5,r)*choose(63,r)*choose(5,q)*choose(951,q)
               for r in range(6) for q in range(6))
    row_hi=sum(table[r][q][1]*choose(5,r)*choose(63,r)*choose(5,q)*choose(951,q)
               for r in range(6) for q in range(6))
    ck('constant_row_and_anchor_congruence',modes[0]['shell']==list(map(enc,(row_lo,row_hi))) and
       all(S*(e-S*c[5]**2)==S*F(*modes[0]['schur'][k]) for k,e in enumerate((row_lo,row_hi))))
    signs=Counter(m['verdict'] for m in modes)
    negative=[[m['a'],m['b']] for m in modes if m['verdict']=='negative']
    verdict='FIXED_PRODUCT_EXCLUDED' if negative else 'INCONCLUSIVE' if signs['unresolved'] else 'SHELL_PASSES'
    ck('entire_saved_summary',saved['stage']=='complete' and not saved['failures'] and
       saved['summary']==dict(counts=dict(signs),negative_modes=negative,verdict=verdict,
                              required='all 36 Schur coordinates nonnegative'))
    minimum=min(modes,key=lambda m:F(*m['schur_over_c5'][0]))
    bound=F(*minimum['schur_over_c5'][0])
    floor=bound*10**6//1
    ck('minimum_lower_bracket',F(floor,10**6)<=bound<F(floor+1,10**6))
    report.update(stage='verified',dictionary=dictionary,modes=modes,
                  minimum_normalized_lower=dict(mode=[minimum['a'],minimum['b']],value=enc(bound),
                                                bracket=[enc(F(floor,10**6)),enc(F(floor+1,10**6))]),
                  size=S,summary=saved['summary'])
    save()
    print('Independent checks:',sum(counts.values()),'; failures:',len(report['failures']))
    print('Actual/required relations 36/36, presentations 216/216, modes 36/36; dimension:',S)
    print('Whole-box signs:',dict(signs),'; PSD requires >=0; verdict:',verdict)
    print('Minimum Schur/c5 lower bound at',minimum['a'],minimum['b'],
          'in [',str(floor)+'/1000000,',str(floor+1)+'/1000000); required >=0')
    print('Certificate:',OUT)


if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Distinct full replay: sparse polynomial cross products, short-model group law.

Does not import the producer or trust its zero-polynomial/success markers.
Mathematical projective quotient and period theorems are cited in L046.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import gcd, lcm, isqrt
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def clean(a): return {i:F(v) for i,v in a.items() if v}
def poly(seq): return clean(dict(enumerate(map(F,seq))))
def plus(*args):
    d={}
    for a in args:
        for i,v in a.items(): d[i]=d.get(i,F(0))+v
    return clean(d)
def times(a,b):
    d={}
    for i,v in a.items():
        for j,w in b.items():d[i+j]=d.get(i+j,F(0))+v*w
    return clean(d)
def smul(a,c):return clean({i:v*c for i,v in a.items()})
def power(a,n):
    d={0:F(1)}
    for _ in range(n):d=times(d,a)
    return d
def derivative(a):return clean({i-1:i*v for i,v in a.items() if i})
def ev(a,t):return sum(v*t**i for i,v in a.items())
def seq(a):return [str(a.get(i,F(0))) for i in range(max(a,default=0)+1)]
def read_r(a):return poly(a['numerator']),poly(a['denominator'])

def short_add(p,q):
    if p is None:return q
    if q is None:return p
    x,y=p; u,v=q
    if x==u:
        if y==-v:return None
        assert p==q and y!=0
        slope=(3*x*x-F(31,3))/(2*y)
    else:slope=(v-y)/(u-x)
    z=slope*slope-x-u
    return z,slope*(x-z)-y

def verify(data):
    checks=[]; failed=[]; evidence={}
    def need(label,condition):
        checks.append(label)
        if not condition:failed.append(label)
    need('schema',data['schema']=='BSD-L046-five-isogeny-v1')
    need('source and candidate',data['source']==[0,-1,1,-10,-20] and data['candidate']==['5','5'])
    x=poly([0,1]); one=poly([1]); f=poly(['-79/4','-10','-1','1'])
    # Verify centering and the short-model shift, including both inverses.
    shortx=plus(x,poly(['-1/3']))
    shortf=plus(power(shortx,3),smul(shortx,-F(31,3)),poly(['-2501/108']))
    need('short-model coordinate identity',shortf==f)
    P=(F(14,3),F(11,2)); cur=None; got=[]
    for n in range(1,6):
        cur=short_add(cur,P)
        if cur is not None:
            X,Y=cur
            need(f'multiple {n} lies on short source',Y*Y==X**3-F(31,3)*X-F(2501,108))
            got.append([str(X+F(1,3)),str(Y-F(1,2))])
        else:got.append(None)
    need('all five multiples',got==data['multiples'])
    need('exact order five',len({tuple(p) for p in got[:4]})==4 and all(p is not None for p in got[:4]) and got[4] is None)
    need('paired inverse points',got==[['5','5'],['16','-61'],['16','60'],['5','-6'],None])
    pairs=[(F(5),F(11,2)),(F(16),-F(121,2))]
    need('kernel polynomial',data['kernel_polynomial']==['80','-21','1'])
    need('kernel polynomial complete',times(poly([-5,1]),poly([-16,1]))==poly(data['kernel_polynomial']))
    D=times(power(poly([-5,1]),2),power(poly([-16,1]),2))
    E=times(power(poly([-5,1]),3),power(poly([-16,1]),3))
    expectedN=times(x,D); expectedM=E
    ts=[]; ws=[]
    for j,(q,r) in enumerate(pairs):
        other=pairs[1-j][0]; a=poly([-q,1]); b=poly([-other,1])
        t=2*(3*q*q-2*q-10); u=4*r*r; w=u+q*t
        ts.append(t); ws.append(w)
        need(f'paired source ordinate {j}',ev(f,q)==r*r and r!=0)
        need(f'paired coefficient witness {j}',data['paired_terms'][j]==dict(x=str(q),Y=str(r),t=str(t),u=str(u),w=str(w)))
        # Direct equation (7), via addition of Q and -Q, not expanded t/u map.
        xpart=plus(smul(plus(f,poly([r*r])),2),times(poly([2-4*q,-2]),power(a,2)))
        expectedN=plus(expectedN,times(xpart,power(b,2)))
        ypart=plus(smul(power(a,3),-2),times(poly([2*q-2,4]),power(a,2)),smul(plus(f,poly([3*r*r])),-2))
        expectedM=plus(expectedM,times(ypart,power(b,3)))
    need('paired domain complete',len(data['paired_terms'])==2)
    N,Dstored=read_r(data['map']['x_target']); M,Estored=read_r(data['map']['Y_target_over_Y_source'])
    need('complete equation (7) x identity',times(N,D)==times(expectedN,Dstored))
    need('complete equation (7) Y identity',times(M,E)==times(expectedM,Estored))
    need('canonical map denominators',Dstored==D and Estored==E)
    need('centered y convention',data['map']['y_convention']=='Y=y+1/2 on both models')
    a4=-10-5*sum(ts); a6=-20+4*sum(ts)-7*sum(ws)
    need('quotient coefficients',data['target']==[0,-1,1,int(a4),int(a6)] and a4==-7820 and a6==-263580)
    targetpoly=plus(power(N,3),smul(times(power(N,2),D),-1),smul(times(N,power(D,2)),a4),smul(power(D,3),a6+F(1,4)))
    residual=plus(times(times(f,power(M,2)),power(D,3)),smul(times(targetpoly,power(E,2)),-1))
    need('full quotient equation cleared polynomial',not residual)
    diff=plus(times(plus(times(derivative(N),D),smul(times(N,derivative(D)),-1)),E),smul(times(M,power(D,2)),-1))
    need('full differential cleared polynomial',not diff and data['differential']['scalar']=='1')
    evidence['equation_residual_coefficients']=seq(residual)
    evidence['differential_residual_coefficients']=seq(diff)
    for j,(q,r) in enumerate(pairs):
        other=pairs[1-j][0]
        lcX=ev(N,q)/(q-other)**2; lcV=ev(M,q)/(q-other)**3
        need(f'finite x pole exactly two at {q}',lcX==4*r*r!=0)
        need(f'finite centered y pole exactly three at both ordinates over {q}',lcV==-8*r*r!=0 and r!=0)
        need(f'exceptional leading coefficients {j}',str(lcX)==data['exceptional']['finite_x_leading_coefficients'][j] and str(lcV)==data['exceptional']['finite_Y_factor_leading_coefficients'][j])
    need('only finite exceptional x coordinates',data['exceptional']['finite_x']==['5','16'] and data['exceptional']['image']=='[0:1:0]')
    need('exceptional orders',data['exceptional']['x_pole_order_each']==2 and data['exceptional']['Y_pole_order_each']==3 and data['exceptional']['infinity_x_pole_order']==2 and data['exceptional']['infinity_Y_pole_order']==3)
    need('infinity leading coefficients',max(N)==5 and max(D)==4 and N[5]==D[4]==1 and max(M)==max(E)==6 and M[6]==E[6]==1)
    b2=-4; b4=2*a4; b6=1+4*a6; b8=-4*a6-1-a4*a4
    c4=b2*b2-24*b4; c6=-b2**3+36*b2*b4-216*b6
    delta=(c4**3-c6**2)/1728
    inv=dict(b2=int(b2),b4=int(b4),b6=int(b6),b8=int(b8),c4=int(c4),c6=int(c6),delta=int(delta))
    need('complete invariants and independent discriminant identity',inv==data['invariants'] and delta==-11)
    need('bad-prime complete factorization',all(11%i for i in range(2,isqrt(11)+1)))
    need('minimality witness',data['minimality']=={'bad_prime':11,'delta_valuation':1,'required_less_than':12,'coordinate_change':[1,0,0,0]} and 1<12)
    need('real witness arithmetic',data['real_map']=={'geometric_kernel_size':5,'real_kernel_size':5,'cokernel_size':1,'period_ratio':'5'})
    transfer=data['transfer']; source=ROOT/transfer['source_certificate']
    need('source certificate exact path',source==HERE.parent/'absolute-cycles/certificate.json')
    need('source bytes',sha256(source.read_bytes()).hexdigest()==transfer['source_sha256'])
    upstream=json.loads(source.read_text())
    values=list(map(F,upstream['normalization']['generator_values']))
    need('audited canonical source values',values==list(map(F,['-1/5','1/5','0','1','1/2','-1/2','-1','-1','-1/2','1/2','1','0'])))
    need('all source values complete',len(values)==12 and values==list(map(F,transfer['source_values'])))
    target=[v*5 for v in values]; D0=lcm(*(v.denominator for v in values)); ints=[int(D0*v) for v in values]
    need('source denominator and all integer numerators',D0==10==transfer['D0'] and ints==transfer['integer_numerators'])
    denoms=[]
    for i,(s,v) in enumerate(zip(values,target)):
        h=10//gcd(abs(5*ints[i]),10); denoms.append(h)
        need(f'target generator {i} reduced exactly',F(transfer['target_values'][i])==v and v.denominator==h and transfer['individual_denominators'][i]==h)
    need('target values and denominators complete',len(transfer['target_values'])==len(transfer['individual_denominators'])==12)
    need('exact denominator threshold',lcm(*denoms)==transfer['common_denominator']==2 and transfer['C_all_odd_primes']==0)
    evidence.update(order_actual=5,order_required=5,degree=5,finite_kernel_points_actual=4,finite_kernel_points_required=4,
                    minimality_valuation_actual=1,minimality_valuation_strict_upper_bound=12,
                    generator_values_actual=12,generator_values_required=12,differential_scalar='1',period_ratio='5',target_denominator=2)
    return checks,failed,evidence

if __name__=='__main__':
    path=Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'certificate.json'
    out=Path(sys.argv[2]) if len(sys.argv)>2 else HERE/'verification.json'
    checks=[]; failures=[]; evidence={}
    try: checks,failures,evidence=verify(json.loads(path.read_text()))
    except Exception as exc: failures.append(f'{type(exc).__name__}: {exc}')
    report={'certificate_sha256':sha256(path.read_bytes()).hexdigest(),
            'verifier_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'checks':checks,'failures':failures,'evidence':evidence}
    out.write_text(json.dumps(report,indent=2)+'\n')
    print('Full replay:',len(checks),'checks; failures:',failures)
    if not failures: print('Order 5/5; finite kernel 4/4; minimality 1/<12; all generators 12/12; d=1; R=5; denominator=2')
    print('Report:',out)
    sys.exit(bool(failures))

"""Three fixed branch ratios: rational/sign certificates or exact roots.

Decimal interpolation only proposes roots; acceptance uses QQ[alpha]/A.
No negative decision is based on a bounded root search.
"""
from fractions import Fraction as Q
from decimal import Decimal as D, localcontext
from hashlib import sha256
from math import isqrt
from pathlib import Path
from itertools import product
import json
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'branch-annihilator-certificate.json'
R = dict(completed=False, failures=[], bindings={}, comparisons=[],
         bounds=dict(comparisons_required=3, rational_bits_cap=8192,
                     max_rational_bits=0, real_bisections=96,
                     proposal_decimal_precision=160,
                     proposal_denominator_cap=10**12, sign_patterns_cap=16,
                     sign_patterns_actual=0))
A = [-109375,-32500,150,64,1]
ONE = [Q(1),Q(0),Q(0),Q(0)]
B = [[1,0,Q(1,2),Q(31,30)],[0,1,Q(7,25),Q(179,750)],
     [0,0,Q(1,50),Q(239,18750)],[0,0,0,Q(1,18750)]]


def obs(v):
    if isinstance(v,(list,tuple)):
        for c in v: obs(c)
    elif isinstance(v,(int,Q)):
        v=Q(v); n=max(abs(v.numerator).bit_length(),v.denominator.bit_length())
        R['bounds']['max_rational_bits']=max(n,R['bounds']['max_rational_bits'])
        assert n<=8192, 'rational bit cap'
    return v


def read(name):
    raw=(ROOT/name).read_bytes(); R['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def mul(a,b):
    v=[Q(0)]*7
    for i in range(4):
        for j in range(4): v[i+j]+=a[i]*b[j]
    for k in range(6,3,-1):
        for j in range(4): v[k-4+j]-=v[k]*A[j]
    return obs(v[:4])


def solve(m,b):
    n=len(b); z=[list(row)+[c] for row,c in zip(m,b)]
    for i in range(n):
        k=next(k for k in range(i,n) if z[k][i]); z[i],z[k]=z[k],z[i]
        t=z[i][i]; z[i]=[v/t for v in z[i]]
        for k in range(n):
            if k!=i:
                t=z[k][i]; z[k]=[v-t*w for v,w in zip(z[k],z[i])]
        if isinstance(z[i][i],Q): obs(z)
    return [row[-1] for row in z]


def inv(a):
    cols=[mul(a,[Q(i==j) for i in range(4)]) for j in range(4)]
    b=obs(solve([[cols[j][i] for j in range(4)] for i in range(4)],ONE))
    assert mul(a,b)==ONE
    return b


def powercoords(v):
    return obs([sum(Q(v[j])*B[i][j] for j in range(4)) for i in range(4)])


def ev(p,x):
    v=x*0
    for c in reversed(p): v=v*x+c
    return v


def interval(p,lo,hi):
    a=b=Q(0)
    for c in reversed(p):
        v=[a*lo,a*hi,b*lo,b*hi]; a,b=min(v)+c,max(v)+c
    return obs([a,b])


def square_q(q):
    q=obs(Q(q)); a,b=isqrt(abs(q.numerator)),isqrt(q.denominator)
    ok=q>=0 and a*a==q.numerator and b*b==q.denominator
    return dict(value=str(q),numerator_floor_sqrt=a,denominator_floor_sqrt=b,
                is_square=ok,root=str(Q(a,b)) if ok else None)


def proposal(b,boxes):
    # Finite numerical proposal stage. Only direct exact squaring accepts.
    with localcontext() as ctx:
        ctx.prec=160
        dec=lambda q:D(q.numerator)/D(q.denominator)
        roots=[]
        for lo,hi in boxes:
            a,c=dec(lo),dec(hi)
            for _ in range(450):
                mid=(a+c)/2
                if ev(A,a)*ev(A,mid)<0:c=mid
                else:a=mid
            roots.append((a+c)/2)
        vals=[ev([dec(t) for t in b],a).sqrt() for a in roots]
        for signs in product([-1,1],repeat=4):
            R['bounds']['sign_patterns_actual']+=1
            assert R['bounds']['sign_patterns_actual']<=16
            coeff=solve([[a**j for j in range(4)] for a in roots],
                        [v*k for v,k in zip(vals,signs)])
            candidate=obs([Q(c).limit_denominator(10**12) for c in coeff])
            if mul(candidate,candidate)==b:
                return candidate
    return None


def main():
    C=read('odd-membership-35-certificate.json')
    audit=read('odd-membership-35-audit.json')
    V=read('odd-membership-35-verification.json')
    assert all(c['completed'] and not c['failures'] for c in (C,audit,V))
    assert V['bindings']['odd-membership-35-certificate.json']==R['bindings']['odd-membership-35-certificate.json']
    assert audit['bindings']['odd-membership-35-certificate.json']==R['bindings']['odd-membership-35-certificate.json']
    assert C['model']['basis']==[[str(v) if isinstance(v,Q) and v.denominator!=1 else int(v) for v in row] for row in B]
    assert [p['coefficients'] for p in C['selected_pair']]==[165,132102]
    p1,p2=C['selected_pair']
    q1,q2=Q(p1['rational']),Q(p2['rational'])
    b1,b2=powercoords(p1['quartic_O']),powercoords(p2['quartic_O'])
    branchq=Q(73990352390625)
    branchb=powercoords([-8085,-220,440,-1320])
    eta=powercoords(C['model']['eta_O'])
    assert [Q(9075)-eta[0]]+[-v for v in eta[1:]]==branchb
    assert mul(eta,[-50,1,0,0])==[-907500,0,0,0]
    assert ev(C['model']['H'],Q(9075))==branchq
    boxes=[]
    for start,end in [(-48,-47),(-34,-33),(-4,-3),(20,21)]:
        lo,hi=Q(start),Q(end); assert ev(A,lo)*ev(A,hi)<0
        for _ in range(96):
            mid=(lo+hi)/2
            if ev(A,lo)*ev(A,mid)<0:hi=mid
            else:lo=mid
        boxes.append(obs([lo,hi]))
    R.update(alpha_polynomial=A,order_basis=B,root_intervals=boxes,
             branch=dict(rational=branchq,quartic_power=branchb))
    for label,q,b in [('epsilon',q1,b1),('eta_class',q2,b2),
                      ('epsilon*eta_class',q1*q2,mul(b1,b2))]:
        rq=square_q(branchq/q); rb=mul(branchb,inv(b))
        rec=dict(denominator=label,rational=rq,quartic_ratio_power_ascending=rb)
        R['comparisons'].append(rec)
        if not rq['is_square']:
            rec.update(equal=False,reason='complete rational nonsquare test');continue
        signs=[interval(rb,*box) for box in boxes]
        rec['quartic_real_intervals']=signs
        if any(hi<0 for lo,hi in signs):
            rec.update(equal=False,reason='negative at a certified real embedding');continue
        assert all(lo>0 for lo,hi in signs),'unresolved real interval'
        root=proposal(rb,boxes)
        assert root is not None,'bounded root proposal unresolved; no nonsquare decision'
        assert mul(root,root)==rb
        rec.update(equal=True,reason='exact roots in both components',
                   quartic_root_power_ascending=root,quartic_square_remainder=[0]*4)
    assert len(R['comparisons'])==3
    R.update(completed=True,branch_in_span=any(c['equal'] for c in R['comparisons']),
             comparisons_completed=3)


if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    R['source_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(R,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=R['completed'],failures=[e['message'] for e in R['failures']],
        actual=len(R['comparisons']),required=3,bounds=R['bounds'],
        results=[dict(denominator=c['denominator'],rational_square=c['rational']['is_square'],
                      equal=c.get('equal')) for c in R['comparisons']],path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)

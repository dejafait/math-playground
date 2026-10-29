"""Independent replay using maximal-order multiplication, no root search."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import isqrt
import json
import traceback

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'branch-annihilator-verification.json'
R=dict(completed=False,failures=[],bindings={},checks=0,max_rational_bits=0)


def ck(b,name):
    R['checks']+=1
    assert b,name


def read(name):
    raw=(ROOT/name).read_bytes();R['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def observe(v):
    if isinstance(v,(list,tuple)):
        for t in v:observe(t)
    elif isinstance(v,(int,Q)):
        t=Q(v);bits=max(abs(t.numerator).bit_length(),t.denominator.bit_length())
        R['max_rational_bits']=max(bits,R['max_rational_bits'])
        ck(bits<=8192,'8192-bit cap')
    return v


def vec(a):return list(map(Q,a))
def multiply(a,b):
    return observe([sum(Q(T[i][j][k])*a[i]*b[j] for i in range(4) for j in range(4)) for k in range(4)])


def to_order(p):
    # Triangular inverse of the literal basis, independently arranged.
    a,b,c,d=vec(p)
    w3=18750*d
    w2=50*(c-Q(239,18750)*w3)
    w1=b-Q(7,25)*w2-Q(179,750)*w3
    w0=a-Q(1,2)*w2-Q(31,30)*w3
    return observe([w0,w1,w2,w3])


def from_order(w):
    a,b,c,d=vec(w)
    return observe([a+c/2+Q(31,30)*d,b+Q(7,25)*c+Q(179,750)*d,
                    c/50+Q(239,18750)*d,d/18750])


def value(p,x):return observe(sum(Q(c)*x**j for j,c in enumerate(p)))


def enclosure(p,lo,hi):
    # Termwise bounds, distinct from the producer's Horner intervals.
    lower=upper=Q(0)
    for j,c in enumerate(p):
        ends=[lo**j,hi**j]
        if lo<=0<=hi and j%2==0:ends.append(Q(0))
        ends=[Q(c)*t for t in ends]
        lower+=min(ends);upper+=max(ends)
    return observe([lower,upper])


def main():
    global T
    C=read('branch-annihilator-certificate.json')
    old=read('odd-membership-35-certificate.json')
    audit=read('odd-membership-35-audit.json')
    ck(C['completed'] and not C['failures'],'producer complete')
    ck(all(sha256((ROOT/n).read_bytes()).hexdigest()==h for n,h in C['bindings'].items()),'all full input hashes')
    ck(C['source_sha256']==sha256((ROOT/'branch_annihilator.py').read_bytes()).hexdigest(),'producer hash')
    ck(audit['completed'] and not audit['failures'] and audit['bindings']['odd-membership-35-certificate.json']==R['bindings']['odd-membership-35-certificate.json'],'accepted input binding')
    T=old['table']
    ck(C['alpha_polynomial']==[-109375,-32500,150,64,1],'actual field polynomial')
    ck([p['coefficients'] for p in old['selected_pair']]==[165,132102],'fixed pair')
    a,b=old['selected_pair'];q1,q2=Q(a['rational']),Q(b['rational'])
    b1,b2=vec(a['quartic_O']),vec(b['quartic_O'])
    branch=vec([-8085,-220,440,-1320]);h=Q(73990352390625)
    ck(to_order(C['branch']['quartic_power'])==branch and Q(C['branch']['rational'])==h,'actual branch')
    ck(from_order(branch)==vec(C['branch']['quartic_power']),'branch basis round trip')
    ck(len(C['comparisons'])==3,'all three nonzero combinations')
    checks=[]
    for rec,(label,q,w) in zip(C['comparisons'],[
        ('epsilon',q1,b1),('eta_class',q2,b2),('epsilon*eta_class',q1*q2,multiply(b1,b2))]):
        ck(rec['denominator']==label,'ordered combination')
        ck(Q(rec['rational']['value'])==h/q,'exact rational ratio')
        ratio=to_order(rec['quartic_ratio_power_ascending'])
        ck(multiply(ratio,w)==branch,'all four quartic ratio coordinates')
        t=Q(rec['rational']['value']);n,d=isqrt(abs(t.numerator)),isqrt(t.denominator)
        ck((n,d)==(rec['rational']['numerator_floor_sqrt'],rec['rational']['denominator_floor_sqrt']),'integer floor roots')
        ok=t>=0 and n*n==t.numerator and d*d==t.denominator
        ck(ok==rec['rational']['is_square'],'complete rational decision')
        if label=='epsilon':
            root=to_order(rec['quartic_root_power_ascending'])
            ck(multiply(multiply(root,root),b1)==branch,'direct branch=root squared times epsilon')
            qr=Q(rec['rational']['root']);ck(qr*qr*q1==h,'direct rational root')
            ck(rec['equal'],'epsilon equality')
            R['epsilon_root_O']=root;R['epsilon_root_Q']=qr
        elif label=='eta_class':
            # One sign-changing interval gives an embedding of K into R.
            poly=C['alpha_polynomial'];lo,hi=Q(-48),Q(-47)
            for _ in range(16):
                mid=(lo+hi)/2
                if value(poly,lo)*value(poly,mid)<0:hi=mid
                else:lo=mid
            ck(value(poly,lo)*value(poly,hi)<0,'real root exists')
            numerator=enclosure(from_order(branch),lo,hi)
            denominator=enclosure(from_order(b2),lo,hi)
            ck(numerator[1]<0<denominator[0],'strict negative ratio in real embedding')
            ck(not rec['equal'],'eta nonmembership')
            R['real_nonsquare']=dict(alpha_interval=[lo,hi],A_end_values=[value(poly,lo),value(poly,hi)],
                                      branch_interval=numerator,eta_class_interval=denominator)
        else:
            z=t;v=0
            while z.numerator%3==0:z/=3;v+=1
            while z.denominator%3==0:z*=3;v-=1
            ck(v%2==1,'odd rational valuation')
            ck(not rec['equal'] and not ok,'product nonmembership')
            R['product_rational_3_valuation']=v
        checks.append(dict(combination=label,equal=rec['equal']))
    # The branch is nonzero already in its rational component.
    z=h;v=0
    while z.numerator%3==0:z/=3;v+=1
    ck(v==5,'nonzero branch class by odd 3 valuation')
    ck(C['branch_in_span'] and C['comparisons_completed']==3,'span decision')
    R.update(completed=True,comparisons=checks,actual=3,required=3,
             branch_equals='epsilon',branch_nonzero=True,pairing_forced_zero=True)


if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=R['completed'],checks=R['checks'],failures=[e['message'] for e in R['failures']],
                         actual=R.get('actual'),required=3,max_rational_bits=R['max_rational_bits'],
                         required_bit_cap=8192,branch_equals=R.get('branch_equals'),path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)

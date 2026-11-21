"""Exact-rational finite-point separation of the approved coefficient box.

No diagnostic output is read. L936's entire accepted root bracket is
retained. All transcendental enclosures use rational series with tails.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

GRID=10**80
checks=[]
division_lower_bounds=[]


def floor_grid(x):return F((x*GRID).numerator//(x*GRID).denominator,GRID)
def ceil_grid(x):return -floor_grid(-x)


class I:
    def __init__(self,lo=0,hi=None):
        if isinstance(lo,I):self.lo,self.hi=lo.lo,lo.hi;return
        self.lo=floor_grid(F(lo))
        self.hi=ceil_grid(F(lo if hi is None else hi))
        assert self.lo<=self.hi
    def __add__(self,b):
        b=I(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-I(b)
    def __rsub__(self,b):return I(b)+-self
    def __mul__(self,b):
        b=I(b);xs=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return I(min(xs),max(xs))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I(b);assert not b.lo<=0<=b.hi
        division_lower_bounds.append(min(abs(b.lo),abs(b.hi)))
        return self*I(1/b.hi,1/b.lo)
    def __rtruediv__(self,b):return I(b)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        out=I(1)
        for _ in range(n):out=out*self
        return out
    def mid(self):return (self.lo+self.hi)/2
    def absbound(self):return max(abs(self.lo),abs(self.hi))
    def data(self):return dict(lower=str(self.lo),upper=str(self.hi))


def check(name,actual,relation,required):
    passed={'<':lambda:actual<required,'>':lambda:actual>required,
            '==':lambda:actual==required}[relation]()
    checks.append(dict(name=name,actual=str(actual),relation=relation,
                       required=str(required),passed=passed))


def atan_bounds(q):
    x=F(1,q)
    s=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(96)),F(0))
    return I(s,s+x**193/193)


def exponential(x):
    x=I(x);assert x.lo>=0
    k=0
    while x.hi>1:x=x/2;k+=1
    term=I(1);out=term
    for j in range(1,91):term=term*x/j;out=out+term
    out=out+I(0,F(2,factorial(91)))
    for _ in range(k):out=out*out
    return out


def exact_response():
    root=I('0.0000530387415958154365906397391693872935932598188',
           '0.00005303874159581543659063973916938729359325981881')
    raw=list(map(I,['0.497123021571','0.022972233662','0.002962906960',
                    '0.000599311666','0.000160971754']))+[root,I('0.000020475993')]
    y=[x/raw[0] for x in raw]
    q=[(-1)**j*y[j]/factorial(2*j) for j in range(7)]
    s=[I(0)]
    for n in range(1,7):s.append(-n*q[n]-sum((s[k]*q[n-k] for k in range(1,n)),I(0)))
    delta=s[2]*s[4]-s[3]**2
    p=(s[3]*s[5]-s[4]**2)/delta
    r=(s[3]*s[4]-s[2]*s[5])/delta
    vec=[p,r,I(1)]
    b={n:sum((vec[i]*vec[j] for i in range(3) for j in range(3)
               if i+j==n-2),I(0)) for n in range(2,7)}
    inv=[I(1)]
    for n in range(1,7):inv.append(-sum((q[j]*inv[n-j] for j in range(1,n+1)),I(0)))
    rr=[-sum((n*b[n]*inv[n-j]*(-1)**j/factorial(2*j)
              for n in range(max(2,j),7)),I(0)) for j in range(7)]
    return rr,dict(root=root,raw=raw,normalized=y,S=s,delta=delta,p=p,r=r,
                   inverse=inv,b=b,response=rr)


def solve(a,b):
    """Exact Gaussian elimination on midpoint rationals; not an interval solve."""
    a=[row[:]+[rhs] for row,rhs in zip(a,b)];n=len(b)
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        val=a[j][j];a[j]=[x/val for x in a[j]]
        for i in range(n):
            if i==j:continue
            val=a[i][j];a[i]=[x-val*y for x,y in zip(a[i],a[j])]
    out=[row[-1] for row in a]
    return out


def short(x):
    """Outward scientific text only; complete rational bounds stay on disk."""
    from decimal import Decimal,localcontext,ROUND_FLOOR,ROUND_CEILING
    ans=[]
    for v,mode in ((x.lo,ROUND_FLOOR),(x.hi,ROUND_CEILING)):
        with localcontext() as c:
            c.prec=12;c.rounding=mode
            ans.append(str(Decimal(v.numerator)/Decimal(v.denominator)))
    assert F(ans[0])<=x.lo<=x.hi<=F(ans[1])
    return dict(lower=ans[0],upper=ans[1])


def main():
    rr,response=exact_response()
    pi=16*atan_bounds(5)-4*atan_bounds(239)
    check('pi_lower',pi.lo,'>',F(3))
    check('pi_upper',pi.hi,'<',F(22,7))
    points=list(map(F,['0','.19','.195','.38','.385','.57','.575','.775','.78']))
    tail_a=F(4*9**4,2**240)
    tail_b=F(156*9**6,2**240)
    check('tail_ratio_four',F(10,9)**4/2**57,'<',F(1,2))
    check('tail_ratio_six',F(10,9)**6/2**57,'<',F(1,2))
    rows=[];offsets=[];score_records=[]
    for u in points:
        v=pi*exponential(2*u)
        check('v_upper_'+str(u),v.hi,'<',F(16))
        den=I(1);num=I(F(9,2))+6/(2*v-3)-2*v
        terms=[]
        for n in range(2,9):
            an=n*n*(2*v*n*n-3)/(2*v-3)/exponential((n*n-1)*v)
            sn=I(F(9,2))+6/(2*v*n*n-3)-2*v*n*n
            den=den+an;num=num+an*sn
            terms.append(dict(n=n,relative_mass=an,score=sn))
        full_den=den+I(0,tail_a)
        full_num=num+I(-tail_b,tail_b)
        h=full_num/full_den
        rv=sum((rr[j]*u**(2*j) for j in range(7)),I(0))
        dr=sum((2*j*rr[j]*u**(2*j) for j in range(1,7)),I(0))
        row=[I((2*j+1)*u**(2*j))+(I(u/F(5120))+h)*u**(2*j+1)
             for j in range(6)]+[rv,dr]
        rows.append(row);offsets.append(u*h*rv)
        score_records.append(dict(u=u,v=v,terms=terms,head_denominator=den,
            head_numerator=num,full_denominator=full_den,full_numerator=full_num,
            full_score=h))
    # Cancel only the six large operator columns. The box pays the two
    # small response-column residuals; no exact annihilation is assumed.
    fixed_weights=[F('0.000232732544813'),F('0.000129474634688')]
    full_a=[[row[j].mid() for row in rows] for j in range(6)]+[[F(1)]*9]
    a=[row[:7] for row in full_a]
    rhs=[F(1 if i==6 else 0)-sum(row[7+j]*fixed_weights[j] for j in range(2))
         for i,row in enumerate(full_a)]
    exact_weights=solve(a,rhs)+fixed_weights
    check('midpoint_system_replay',all(sum(full_a[i][j]*exact_weights[j] for j in range(9))
          == (1 if i==6 else 0) for i in range(7)),'==',True)
    # Rounding the nominated weights has no mathematical equality claim.
    scale=10**45
    weights=[F((w*scale).numerator//(w*scale).denominator,scale) for w in exact_weights]
    for i,w in enumerate(weights):check('weight_positive_'+str(i),w,'>',F(0))
    fsum=sum((w*x for w,x in zip(weights,offsets)),I(0))
    sums=[sum((w*row[j] for w,row in zip(weights,rows)),I(0)) for j in range(8)]
    box_error=16*sum((s.absbound() for s in sums),F(0))
    upper=fsum.hi+box_error
    check('weighted_offset_upper',fsum.hi,'<',-F(1,10**15))
    check('box_error_upper',box_error,'<',F(1,10**16))
    check('whole_box_residual_upper',upper,'<',-F(1,10**15))
    failures=[c['name'] for c in checks if not c['passed']]
    summary=dict(outcome='CERTIFIED COEFFICIENT-BOX INFEASIBILITY' if not failures else 'FAILED CERTIFICATE',
        points=len(points),checks=len(checks),failures=failures,
        weighted_offset=short(fsum),box_error=short(I(box_error)),
        whole_box_upper=short(I(upper)),required_upper='strictly < 0',
        accepted_threshold='strictly < -1e-15',
        weight_bounds=[short(I(w)) for w in weights],
        weighted_column_bounds=[short(s) for s in sums],
        score_bounds=[short(s['full_score']) for s in score_records],
        full_half_line_feasible=False if not failures else None,actual_contact_sign_decided=False)
    output=dict(scope='Unchanged L936 witness, lambda=1/10240, eight constants in [-16,16]',
        arithmetic='Exact Fraction with outward rounding to denominator 10^80; no floating or exp library input',
        response=response,pi=pi,tail=dict(relative_mass=tail_a,absolute_score_numerator=tail_b),
        score_records=score_records,points=points,rows=rows,offsets=offsets,
        midpoint_weights=exact_weights,weights=weights,
        separation=dict(weighted_offset=fsum,weighted_columns=sums,box_error=box_error,
                        whole_box_upper=upper),
        divisions=dict(count=len(division_lower_bounds),minimum_lower_bound=min(division_lower_bounds)),
        checks=checks,summary=summary)
    def encode(x):
        if isinstance(x,I):return x.data()
        if isinstance(x,F):return str(x)
        raise TypeError(type(x))
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(output,default=encode,indent=2)+'\n')
    print(json.dumps({k:summary[k] for k in ('outcome','checks','failures','weighted_offset',
          'box_error','whole_box_upper','required_upper')},indent=2))
    print('Certificate:',path)


if __name__=='__main__':main()

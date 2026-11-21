"""Rigorous dyadic-free integer interval certificate for the fixed phi_115.

No floating-point elementary function enters a certified bound. All
operations round outwards to multiples of 10^-40. Complete cell records
are written to disk; the console prints only the decision and checks.
"""
from fractions import Fraction
from math import isqrt, factorial
from pathlib import Path
import json

SCALE = 10**40


class I:
    def __init__(self, a=0, b=None, *, raw=False):
        if raw:
            self.lo, self.hi = a, b
        else:
            a = Fraction(a)
            b = a if b is None else Fraction(b)
            self.lo = a.numerator*SCALE // a.denominator
            self.hi = -((-b.numerator*SCALE)//b.denominator)
        assert self.lo <= self.hi

    @staticmethod
    def coerce(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        v = I.coerce(other)
        return I(self.lo+v.lo, self.hi+v.hi, raw=True)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo, raw=True)

    def __sub__(self, other):
        return self + (-I.coerce(other))

    def __rsub__(self, other):
        return I.coerce(other) + (-self)

    def __mul__(self, other):
        v = I.coerce(other)
        products = [a*b for a in (self.lo,self.hi) for b in (v.lo,v.hi)]
        return I(min(products)//SCALE, -((-max(products))//SCALE), raw=True)

    __rmul__ = __mul__

    def __truediv__(self, other):
        v = I.coerce(other)
        assert v.lo*v.hi > 0
        pairs = [(a*SCALE,b) for a in (self.lo,self.hi) for b in (v.lo,v.hi)]
        return I(min(a//b for a,b in pairs), max(-((-a)//b) for a,b in pairs), raw=True)

    def __rtruediv__(self, other):
        return I.coerce(other)/self

    def sqrt(self):
        assert self.lo >= 0
        a,b = isqrt(self.lo*SCALE),isqrt(self.hi*SCALE)
        return I(a,b+(b*b != self.hi*SCALE),raw=True)

    def abs_lower(self):
        return 0 if self.lo <= 0 <= self.hi else min(abs(self.lo),abs(self.hi))

    def record(self):
        return {"lo":str(self.lo),"hi":str(self.hi),"scale":str(SCALE)}


def arctan_reciprocal(n, count):
    # Alternating series through k=count-1; the next term bounds remainder.
    v = sum((Fraction((-1)**k,(2*k+1)*n**(2*k+1)) for k in range(count)),Fraction())
    e = Fraction(1,(2*count+1)*n**(2*count+1))
    return I(v-e,v+e)


# Machin's identity pi=16 arctan(1/5)-4 arctan(1/239).
PI = 16*arctan_reciprocal(5,40)-4*arctan_reciprocal(239,12)


def small_log(x):
    # x in [1,2]; q=(x-1)/(x+1) in [0,1/3].
    assert x.lo >= SCALE and x.hi <= 2*SCALE
    q = (x-1)/(x+1)
    q2 = q*q
    term=q
    total=I(0)
    count=50
    for k in range(count):
        total += term*Fraction(2,2*k+1)
        term = term*q2
    # Exact universal bound for all omitted positive terms.
    rem=Fraction(2,1)*Fraction(1,3)**(2*count+1)/((2*count+1)*(1-Fraction(1,9)))
    return total+I(0,rem)


LOG2=small_log(I(2))


def log_interval(x):
    x=I.coerce(x)
    assert x.lo > 0
    k=0
    while x.lo >= 2*SCALE:
        x=x/2
        k+=1
    while x.hi < SCALE:
        x=x*2
        k-=1
    assert x.lo >= SCALE and x.hi <= 2*SCALE
    return small_log(x)+k*LOG2


def sine_or_cosine(x, cosine=False):
    # Select any integer reduction, then VERIFY the Taylor domain exactly.
    # This integer quotient does not enter an approximation to sin/cos.
    k=(x.lo+x.hi+2*PI.lo)//(4*PI.lo)
    r=x-2*k*PI
    assert max(abs(r.lo),abs(r.hi)) <= 4*SCALE
    z=r*r
    count=26
    coeffs=[Fraction((-1)**k,factorial(2*k+(0 if cosine else 1))) for k in range(count)]
    val=I(coeffs[-1])
    for coefficient in reversed(coeffs[:-1]):
        val=val*z+coefficient
    if not cosine:
        val=val*r
    # Lagrange remainder: degree 51 (sin) / 50 (cos), derivative <=1.
    power=2*count if cosine else 2*count+1
    rem=Fraction(4**power,factorial(power))
    return val+I(-rem,rem)


def sinc_small(x):
    assert max(abs(x.lo),abs(x.hi)) <= 4*SCALE
    z=x*x
    count=26
    val=I(Fraction((-1)**(count-1),factorial(2*count-1)))
    for k in range(count-2,-1,-1):
        val=val*z+Fraction((-1)**k,factorial(2*k+1))
    # Integrate cos(ux) from u=0 to1 and its degree50 remainder.
    rem=Fraction(4**(2*count),factorial(2*count+1))
    return val+I(-rem,rem)


def qstr(a):
    return str(Fraction(a,SCALE))


def main():
    powers={}
    for p in range(2,101):
        if all(p%d for d in range(2,isqrt(p)+1)):
            n=p
            while n<101:
                powers[n]=p
                n*=p
    terms=[(n,p,2*log_interval(p)/I(n).sqrt(),log_interval(n))
           for n,p in sorted(powers.items())]
    assert len(terms)==35
    L=log_interval(101)
    b=L/2
    A=sum((c for n,p,c,ell in terms),I(0))
    D=1+sum((c*ell for n,p,c,ell in terms),I(0))
    beta0=I(Fraction(199999,100000))
    h=Fraction(1,1000)
    count=2000
    total=I(0)
    cells=[]
    for k in range(count):
        t=I(Fraction(77)+Fraction(2*k+1,2000))
        p=sum((c*sine_or_cosine(t*ell,cosine=True) for n,pr,c,ell in terms),I(0))
        v=beta0-log_interval(t/(2*PI))-2/(t*t)+p
        # |v'| <= 1 + sum c_n log n throughout [77,79].
        loss_lower=max(0,(v-109*I(h/2)).lo)
        # phi_115 transform /sqrt(b), up to an immaterial overall sign.
        u=b*t-Fraction(115,2)*PI
        z=b*t+Fraction(115,2)*PI
        transform=sinc_small(u)+sine_or_cosine(z)/z
        # |(F/sqrt(b))'| <= sqrt(2/3)*b <3 for b<5/2.
        amp_lower=max(0,transform.abs_lower()-I(3*h/2).hi)
        density_lower=b*I(amp_lower,amp_lower,raw=True)*I(amp_lower,amp_lower,raw=True)
        contribution=I(loss_lower,loss_lower,raw=True)*density_lower*I(h)/PI
        total += contribution
        cells.append({"k":k,"midpoint":qstr(t.lo),
                      "v":v.record(),"loss_cell_lower":qstr(loss_lower),
                      "transform_scaled":transform.record(),
                      "amplitude_cell_lower":qstr(amp_lower),
                      "contribution":contribution.record()})
    checks={"all35":len(terms)==35,"b_lt_5_over_2":b.hi<5*SCALE//2,
            "A_lt_34":A.hi<34*SCALE,"D_lt_109":D.hi<109*SCALE,
            "2000_cells_cover_77_79":count*h==2,
            "witness_lower_gt_27_over_10":10*total.lo>27*SCALE}
    cert={"scope":"Rigorous lower bound only; not a negative R or E direction.",
          "method":"Integer outward intervals; midpoint Lipschitz cell lower rectangles.",
          "scale":str(SCALE),"index":115,"unchanged_projection_rank":64,
          "frequency_interval_positive":[77,79],"mesh":str(h),
          "parameters":{"pi":PI.record(),"L":L.record(),"b":b.record(),
                        "A":A.record(),"D":D.record(),"beta0":beta0.record()},
          "prime_powers":[{"n":n,"p":p,"c":c.record(),"log_n":ell.record()}
                          for n,p,c,ell in terms],
          "complete_lower_integral":total.record(),
          "checks":checks,"failures":[key for key,ok in checks.items() if not ok],
          "cells":cells}
    path=Path(__file__).with_name("negative-loss-witness-1166.json")
    path.write_text(json.dumps(cert,indent=2)+"\n")
    print(f"Certified lower bound: {qstr(total.lo)} >27/10; required norm <beta<2.")
    print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {cert['failures']}")
    print(f"Full certificate: {path.relative_to(Path.cwd())}")
    raise SystemExit(bool(cert["failures"]))


if __name__=="__main__":
    main()

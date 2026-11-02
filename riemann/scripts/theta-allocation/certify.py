"""Real interval certificate for the first approved rational candidate.

Only Decimal directed arithmetic and correctly rounded Decimal.exp are used.
Mathematical bounds and normalization algebra are in L609 (when completed).
No floating quadrature output is imported into this computation.
"""
import json
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from pathlib import Path
from fractions import Fraction

PREC = 45
DN = Context(prec=PREC, rounding=ROUND_FLOOR, Emin=-999999999, Emax=999999999)
UP = Context(prec=PREC, rounding=ROUND_CEILING, Emin=-999999999, Emax=999999999)
RN = Context(prec=PREC, rounding=ROUND_HALF_EVEN, Emin=-999999999, Emax=999999999)

class I:
    def __init__(self, lo, hi=None):
        self.lo = D(lo)
        self.hi = D(lo if hi is None else hi)
        assert self.lo.is_finite() and self.hi.is_finite() and self.lo <= self.hi
    def __add__(self, other):
        other = cv(other)
        return I(DN.add(self.lo, other.lo), UP.add(self.hi, other.hi))
    __radd__ = __add__
    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())
    def __sub__(self, other):
        return self + (-cv(other))
    def __rsub__(self, other):
        return cv(other) - self
    def __mul__(self, other):
        other = cv(other)
        ps = [(a,b) for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return I(min(DN.multiply(a,b) for a,b in ps), max(UP.multiply(a,b) for a,b in ps))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = cv(other)
        assert other.lo > 0 or other.hi < 0, 'denominator contains zero'
        return self * I(DN.divide(D(1),other.hi), UP.divide(D(1),other.lo))
    def exp(self):
        # Decimal exp is correctly rounded to nearest, regardless of context rounding.
        return I(RN.next_minus(RN.exp(self.lo)), RN.next_plus(RN.exp(self.hi)))
    def square(self):
        if self.lo >= 0:
            return I(DN.multiply(self.lo,self.lo), UP.multiply(self.hi,self.hi))
        if self.hi <= 0:
            return (-self).square()
        return I(0,max(UP.multiply(self.lo,self.lo),UP.multiply(self.hi,self.hi)))
    def radius(self):
        return UP.divide(UP.subtract(self.hi,self.lo),D(2))
    def magnitude(self):
        return max(self.lo.copy_abs(),self.hi.copy_abs())
    def pair(self):
        return [str(self.lo),str(self.hi)]

def cv(x):
    return x if isinstance(x,I) else I(x)

def power(x,n):
    ans = I(1)
    for _ in range(n):
        ans = ans*x
    return ans

def atan_recip(q):
    # Alternating series at t=1/q, error <= t^(2N+1)/(2N+1).
    t=I(1)/q
    total=I(0)
    term=t
    for n in range(120):
        total += ((-1)**n)*term/(2*n+1)
        term *= t.square()
    error=(term/241).hi
    return total+I(error.copy_negate(),error)

PI=16*atan_recip(5)-4*atan_recip(239)
assert PI.lo>3 and PI.hi<4

def differentiated_polynomial(coefficients):
    # Exact operator P -> (1/2-2v)P+2vP'; coefficients in ascending order.
    out=[Fraction(0) for _ in range(len(coefficients)+1)]
    for degree,coefficient in enumerate(coefficients):
        out[degree] += (Fraction(1,2)+2*degree)*coefficient
        out[degree+1] -= 2*coefficient
    assert all(c.denominator==1 for c in out)
    return tuple(int(c) for c in out)

POLYS=[(0,-12,8)]
for _ in range(2):
    POLYS.append(differentiated_polynomial(POLYS[-1]))
COEFFICIENT_BOUNDS=[sum(abs(c) for c in p) for p in POLYS]
# n>=6, u in [0,8]: |term_j| <= exp(4) C_j (pi*n^2)^(j+2) exp(-pi*n^2).
# Consecutive ratio <=4 exp(-39)<1/2; first term <=C_j exp(4)144^(j+2)exp(-108).
TAILS=[(2*c*144**(j+2)*I(-104).exp()).hi for j,c in enumerate(COEFFICIENT_BOUNDS)]
assert (4*I(-39).exp()).hi < D('0.5')

def kernel(u, order=0):
    u=cv(u)
    assert 0<=u.lo and u.hi<=8
    e2=(2*u).exp()
    eh=(u/2).exp()
    sums=[I(0) for _ in range(order+1)]
    for n in range(1,6):
        v=PI*n*n*e2
        base=eh*(-v).exp()
        for j in range(order+1):
            polynomial=I(POLYS[j][-1])
            for coefficient in reversed(POLYS[j][:-1]):
                polynomial=polynomial*v+coefficient
            sums[j] += base*polynomial
    sums[0] += I(0,TAILS[0])
    for j in range(1,order+1):
        sums[j] += I(TAILS[j].copy_negate(),TAILS[j])
    return sums

def sincos(t):
    # Used only on |t|<=5. Taylor degree 99/98, each error <=5^100/100!.
    assert cv(t).magnitude() <= 5
    t=cv(t)
    sq=t.square()
    sn,cs=I(0),I(0)
    st,ct=t,I(1)
    for n in range(50):
        sn+=st
        cs+=ct
        st=-st*sq/((2*n+2)*(2*n+3))
        ct=-ct*sq/((2*n+1)*(2*n+2))
    fact=1
    for n in range(1,101):
        fact*=n
    err=(I(5**100)/fact).hi
    return sn+I(err.copy_negate(),err),cs+I(err.copy_negate(),err)

def main():
    a=I(7)/16
    x=11
    cutoff=I(8)
    ntail=2048
    nb=16384
    dt=(cutoff-a)/ntail
    ha=I(0)
    mass_tail_finite=I(0)
    ha_quad_error=I(0)
    z_quad_error=I(0)
    # Midpoint with real Taylor second-derivative bound, not analytic quadrature.
    for i in range(ntail):
        left=a+i*dt
        right=a+(i+1)*dt
        cell=I(left.lo,right.hi)
        mid=a+(I(i)+I(1)/2)*dt
        km=kernel(mid)[0]
        ks=kernel(cell,2)
        errh=(power(dt,3)/24*(2*ks[1]+cell*ks[2]).magnitude()).hi
        errz=(power(dt,3)/24*ks[2].magnitude()).hi
        ha += dt*mid*km+I(errh.copy_negate(),errh)
        mass_tail_finite += dt*km+I(errz.copy_negate(),errz)
        ha_quad_error += errh
        z_quad_error += errz
    # L564: k=2Phi_R<=20000exp(-u^2).
    spatial_h=(10000*I(-64).exp()).hi
    spatial_mass=(1250*I(-64).exp()).hi
    ha += I(0,spatial_h)
    ka,kpa=kernel(a,1)
    assert ka.lo>0
    q=a+ha*kpa/ka.square()
    db=a/nb
    cells=[]
    s=I(0)
    mass_head=I(0)
    sin_a,cos_a=sincos(x*a)
    sin_step,cos_step=sincos(x*db)
    sin_b,cos_b=sincos(x*db/2)
    lip=(x*db/2).hi
    for i in range(nb):
        left=i*db
        right=(i+1)*db
        b=I(left.lo,right.hi)
        kb=kernel(b)[0]
        cos_box=cos_b+I(lip.copy_negate(),lip)
        sin_box=sin_b+I(lip.copy_negate(),lip)
        # Exact trig addition simplification of all four original K terms.
        bigk=2*((cos_a+x*a*sin_a)*cos_box-x*b*cos_a*sin_box)
        cells.append((b,kb,bigk))
        s += db*kb*cos_box
        mass_head += db*kb
        sin_b,cos_b=(sin_b*cos_step+cos_b*sin_step,
                     cos_b*cos_step-sin_b*sin_step)
    # Descending accumulation H(b)=H(a)+int_b^a v k(v)dv.
    h_right=ha
    remainder=I(0)
    for b,kb,bigk in reversed(cells):
        cell_mass=db*b*kb
        # 0<=int_b^right v k(v)dv<=upper(cell_mass) on every real cell.
        hb=I(h_right.lo,UP.add(h_right.hi,cell_mass.hi))
        remainder += 2*db*(ka*hb-ha*kb)*bigk
        h_right += cell_mass
    layer=4*q*s.square()
    result=layer+remainder
    z=2*(mass_head+mass_tail_finite+I(0,spatial_mass))
    normalized=result/z.square()
    certificate={
        'status':'CERTIFIED_NEGATIVE' if result.hi<0 else 'UNCERTIFIED',
        'point':{'x':x,'a_numerator':7,'a_denominator':16},
        'arithmetic':{'precision':PREC,'method':'Decimal directed endpoints; nearest exp widened one ulp',
                      'derivative_polynomials_ascending':POLYS,'coefficient_bounds':COEFFICIENT_BOUNDS,
                      'pi':PI.pair(),'theta_terms':5,'theta_uniform_tails_j0_j1_j2':[str(t) for t in TAILS]},
        'quadrature':{'cutoff':8,'tail_midpoint_cells':ntail,'head_real_box_cells':nb,
                      'H_midpoint_error_upper':str(ha_quad_error.hi),
                      'one_side_mass_midpoint_error_upper':str(z_quad_error.hi),
                      'H_spatial_tail_upper':str(spatial_h),'one_side_mass_spatial_tail_upper':str(spatial_mass)},
        'enclosures':{'k_a':ka.pair(),'k_prime_a':kpa.pair(),'H_a':ha.pair(),
                      'q_a':q.pair(),'S':s.pair(),'positive_layer':layer.pair(),
                      'integrated_remainder':remainder.pair(),'Z':z.pair(),
                      'Z_squared_G':result.pair(),'G':normalized.pair()},
        'test':{'required_upper_bound':'0','actual_upper_bound':str(result.hi),
                'radius':str(result.radius()),'denominators_separated':ka.lo>0 and z.lo>0,
                'failures':[] if result.hi<0 else ['final interval does not prove negativity']},
        'distinct_rational_candidates_attempted':1,
        'certificate_evaluation_runs_including_corrected_versions':3,
        'preview_is_not_evidence':True}
    path=Path(__file__).with_name('certificate.json')
    path.write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps({'status':certificate['status'],'point':certificate['point'],
                      'Z_squared_G':result.pair(),'G':normalized.pair(),
                      'required_upper_bound':'0','radius':str(result.radius()),
                      'failures':certificate['test']['failures'],'certificate':str(path)},indent=2))

if __name__=='__main__':
    main()

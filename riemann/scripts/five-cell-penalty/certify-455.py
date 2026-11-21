"""Rigorous scalar obstruction to the fixed five-cell lower certificate.

Only Python's standard library is needed. Interval endpoints use Decimal
with directed basic arithmetic at 70 digits. Correctly rounded exp/log/sqrt
are widened by one neighboring Decimal. Trigonometry uses Machin's formula
and Taylor polynomials with explicit remainders. Digamma uses the imported
convergent response series and a monotone integral tail, not a float call.
The exact dyadic vector is frozen below; the float screen is not an input.
"""
import json
import math
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from fractions import Fraction
from pathlib import Path

PREC = 70
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
NEAR = Context(prec=PREC, rounding=ROUND_HALF_EVEN)


class I:
    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = self.lo if hi is None else Decimal(hi)
        assert self.lo <= self.hi

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, x):
        x = I.cast(x)
        return I(DOWN.add(self.lo, x.lo), UP.add(self.hi, x.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, x):
        return self + (-I.cast(x))

    def __rsub__(self, x):
        return I.cast(x) + (-self)

    def __mul__(self, x):
        x = I.cast(x)
        pairs = [(a,b) for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return I(min(DOWN.multiply(a,b) for a,b in pairs),
                 max(UP.multiply(a,b) for a,b in pairs))

    __rmul__ = __mul__

    def reciprocal(self):
        assert not self.lo <= 0 <= self.hi
        return I(DOWN.divide(Decimal(1),self.hi), UP.divide(Decimal(1),self.lo))

    def __truediv__(self, x):
        return self * I.cast(x).reciprocal()

    def __rtruediv__(self, x):
        return I.cast(x) / self

    def sq(self):
        ends = [self.lo,self.hi]
        low = Decimal(0) if self.lo <= 0 <= self.hi else min(DOWN.multiply(x,x) for x in ends)
        return I(low,max(UP.multiply(x,x) for x in ends))

    def elementary(self, name):
        if name in ('ln','sqrt'):
            assert self.lo > 0 or (name == 'sqrt' and self.lo == 0)
        fn = getattr(NEAR,name)
        return I(NEAR.next_minus(fn(self.lo)), NEAR.next_plus(fn(self.hi)))

    def ln(self): return self.elementary('ln')
    def exp(self): return self.elementary('exp')
    def sqrt(self): return self.elementary('sqrt')
    def json(self): return {'lo':str(self.lo),'hi':str(self.hi)}


def atan_inverse(n):
    # Alternating series, with a symmetric enclosure of the first unused term.
    ans = I(0)
    for j in range(100):
        ans += I((-1)**j) / ((2*j+1)*n**(2*j+1))
    err = I(1)/(201*n**201)
    return ans + I(err.hi.copy_negate(),err.hi)


PI = 16*atan_inverse(5)-4*atan_inverse(239)
TRIG_ERR = (I(4**100)/math.factorial(100)).hi


def sincos(x):
    x=I.cast(x)
    middle=NEAR.divide(NEAR.add(x.lo,x.hi),Decimal(2))
    period=NEAR.add(PI.lo,PI.hi)
    m=int(NEAR.divide(middle,period).to_integral_value(rounding=ROUND_HALF_EVEN))
    y=x-2*m*PI
    assert max(abs(y.lo),abs(y.hi)) < 4
    y2=y.sq()
    sine=y
    cosine=I(1)
    st=y
    ct=I(1)
    for j in range(1,50):
        st=-st*y2/((2*j)*(2*j+1))
        ct=-ct*y2/((2*j-1)*(2*j))
        sine+=st
        cosine+=ct
    error=I(TRIG_ERR.copy_negate(),TRIG_ERR)
    return sine+error,cosine+error


ELL=I(3).ln()/2
A=5*ELL/2
L=2*A
LN2=I(2).ln()
PRIMES=[(2,2,4),(3,3,3),(4,2,2),(5,5,2),(7,7,2),(8,2,2),(9,3,2),(11,11,2),(13,13,2)]


def gamma_interval():
    # psi(N)=H_N-1/N-gamma. The previously imported DLMF remainder
    # |psi(N)-log(N)+1/(2N)| <= 1/(12N^2) gives this enclosure.
    n=100000
    harmonic=I(0)
    for j in range(1,n+1):
        harmonic+=I(1)/j
    base=harmonic-I(n).ln()-I(1)/(2*n)
    err=(I(1)/(12*n*n)).hi
    return base+I(err.copy_negate(),err)


GAMMA=gamma_interval()
H0=-GAMMA-PI/2-3*LN2-PI.ln()
DIGAMMA_PREFIX=8192


def h_interval(k):
    # h(k)-h(0)=sum_j 2 k^2/[c_j(c_j^2+k^2)], c_j=2j+1/2.
    # For decreasing f, int_N^infty f <= sum_{j>=N} f(j)
    # <= int_N^infty f + f(N). Integral = log(1+k^2/c_N^2)/2.
    k2=k.sq()
    total=I(0)
    for j in range(DIGAMMA_PREFIX):
        c=I(4*j+1)/2
        total+=2*k2/(c*(c.sq()+k2))
    c=I(4*DIGAMMA_PREFIX+1)/2
    integral=(1+k2/c.sq()).ln()/2
    first=2*k2/(c*(c.sq()+k2))
    tail=I(integral.lo,(integral+first).hi)
    return H0+total+tail,tail,first


# Exact vector proposed by the float screen, rounded to denominator 2^44.
NUMERATORS = [-17872052310, 75171134711, -779589332438, -216395112806, 1634677879771, -6240440545252, 474513380674, -7380987806467, 3534606652904, 1338289351872, 3902925481134, -926004774320, 214768754178, 4164416820465, -3416436601858, 1764560752362, -3411484835569, 3896170618038, -345752118841, -171631769846, -5392559402793, 72903323675, -397128640889, 489314766534, -4285719135317, 2941429585406, -392370117284, 4645783360655, 5413934929566, -1629821844814, 1846643922840, -1934920464165, 2242788956108, 217698906301, 350470509376, -559968073737, -293513938222, 23737686482, -80058863291, -61913706192, -126262699439, 34393856121, 7303521917, 19035179137, -16558277082, 10031954378, -1625473696, -3641436496, -8229363291, -516079533, 165516102, -1348394095, 464019678, 320825487, 244238387, -1712625828, 674947070, -380212024, 703366489, -337751377, 1022435225, -654771221, 718104974, -848402577]
DENOMINATOR = 2**44


def certify():
    assert len(NUMERATORS)==64
    v=[I(n)/DENOMINATOR for n in NUMERATORS]
    k=[q*PI/A for q in range(64)]
    k2=[x.sq() for x in k]
    norm=[(I(1)/A).sqrt()]+[(I(2)/A).sqrt()]*63
    full=[x/I(2).sqrt() for x in norm]
    w=[v[q]*full[q] for q in range(64)]
    diag=I(0)
    hdata=[]
    tail_width=I(0)
    for q in range(64):
        h,tail,first=h_interval(k[q])
        diag+=v[q].sq()*h
        tail_width+=v[q].sq()*first
        hdata.append({'q':q,'h':h.json(),'tail':tail.json()})
    print('Digamma scalar enclosed; all 64 modes and infinite series tails included.',flush=True)
    prime_total=I(0)
    prime_terms=[]
    for n,p,index in PRIMES:
        delay=I(n).ln()
        half=A-delay/2
        factors=[]
        cosines=[]
        for s in range(127):
            freq=s*PI/A
            factors.append(half if s==0 else sincos(freq*half)[0]/freq)
            cosines.append(sincos(freq*delay/2)[1])
        corr=I(0)
        for r in range(64):
            for s in range(r,64):
                x=abs(r-s); y=r+s
                entry=factors[x]*cosines[y]+factors[y]*cosines[x]
                corr+=(1 if r==s else 2)*w[r]*w[s]*entry
        term=-2*I(p).ln()/I(n).sqrt()*corr
        prime_total+=term
        prime_terms.append({'n':n,'base_prime':p,'energy':term.json(),'correlation':corr.json()})
    responses=[]
    response_total=I(0)
    for j in range(128):
        c=I(4*j+1)/2
        factor=(1-(-2*A*c).exp()).sqrt()
        projection=sum((v[q]*norm[q]*((-1)**q)*c/(c.sq()+k2[q]) for q in range(64)),I(0))*factor
        energy=projection.sq()
        responses.append({'j':j,'projection':projection.json(),'energy':energy.json()})
        response_total+=energy
        if j==0:
            pole_projection=projection*(A/2).exp()*(1-(-A).exp()).sqrt()
    pole=pole_projection.sq()
    trig={}
    for q in range(64):
        for edge in [-5,-3,-1,1,3,5]:
            trig[q,edge]=sincos(q*edge*PI/5)
    moments=[]
    penalty=I(0)
    for cell in range(5):
        le=2*cell-5; re=2*cell-3
        for sigma in [1,-1]:
            beta=I(sigma)/2
            el=(-sigma*ELL/4).exp(); er=(sigma*ELL/4).exp()
            moment=I(0)
            for q in range(64):
                sl,cl=trig[q,le]; sr,cr=trig[q,re]
                integ=(er*(beta*cr+k[q]*sr)-el*(beta*cl+k[q]*sl))/(beta.sq()+k2[q])
                moment+=w[q]*integ
            cost=256*moment.sq()
            moments.append({'cell':cell,'sigma':sigma,'moment':moment.json(),'penalty':cost.json()})
            penalty+=cost
    total=diag+prime_total+response_total+pole+penalty
    norm_exact=sum((Fraction(n*n,DENOMINATOR**2) for n in NUMERATORS),Fraction(0))
    norm2=I(norm_exact.numerator)/norm_exact.denominator
    assert 15 < (9*I(3).sqrt()).lo and (9*I(3).sqrt()).hi < 16
    rho=I(0)
    for n,p,index in PRIMES:
        logn=I(n).ln()
        assert ((index-1)*logn).hi < L.lo and (index*logn).lo > L.hi
        rho+=2*I(p).ln()/I(n).sqrt()*sincos(PI/(index+1))[1]
    complement=[]
    for parity in [1,-1]:
        kt=(I(4096) if parity==1 else I(8193)/2)*PI/A
        ht,_,_=h_interval(kt)
        pole_cost=I(0) if parity==1 else A.exp()-(-A).exp()-2*A
        floor=ht-rho-pole_cost
        complement.append({'parity':parity,'d4096':ht.json(),'rho':(rho+pole_cost).json(),'floor':floor.json(),'strictly_positive':floor.lo>0})
    result={'status':'CERTIFIED_NEGATIVE_RETAINED_DIRECTION' if total.hi<0 else 'INCONCLUSIVE',
        'scope':'Fixed 128-response lower comparison only; no negative actual Weil energy or neutral test asserted.',
        'parameters':{'K':5,'penalty':256,'responses':128,'retained_modes_per_parity':4096,'covariance_prefix_end':16384},
        'arithmetic':{'decimal_precision':PREC,'trig_remainder':str(TRIG_ERR),'digamma_prefix':DIGAMMA_PREFIX,'gamma_harmonic_cutoff':100000},
        'constants':{'pi':PI.json(),'gamma':GAMMA.json(),'ell':ELL.json(),'a':A.json(),'C_nr':rho.json()},
        'witness':{'parity':1,'modes':64,'numerators':NUMERATORS,'denominator':DENOMINATOR,'norm2_exact':str(norm_exact),'norm2':norm2.json()},
        'terms':{'diagonal':diag.json(),'prime':prime_total.json(),'responses':response_total.json(),'pole':pole.json(),'penalty':penalty.json()},
        'energy':total.json(),'rayleigh':(total/norm2).json(),'required_energy_lower_bound':'>0 for every nonzero retained vector',
        'digamma_weighted_tail_width_bound':tail_width.json(),'all_h_enclosures':hdata,'prime_terms':prime_terms,
        'all_response_projections':responses,'all_physical_moments':moments,'complement_floors':complement,
        'schur_covariance_evaluated':False,'failure':'The retained matrix already has a negative exact dyadic direction; subtracting positive Schur costs cannot repair it.'}
    path=Path(__file__).with_name('certificate-455.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('Fixed lower-comparison energy:',total.json(),'; required >0')
    print('Norm squared:',norm2.json())
    for c in complement:
        print('Parity',c['parity'],'entire-complement floor:',c['floor'],'; required >0')
    print('Result:',result['status'],'; complete certificate:',path)
    assert total.hi < Decimal('-2e-8'), 'The desired strict negative witness bound failed.'
    assert all(c['strictly_positive'] for c in complement)


if __name__=='__main__':
    certify()

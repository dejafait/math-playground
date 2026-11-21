"""One fixed degree-two shared-variable H2 enclosure; L922 documents inclusion.

Run from riemann. No refinements or sweeps. L037 arithmetic is conditional.
"""
import hashlib
import importlib.util
import json
import platform
from decimal import DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal
from fractions import Fraction as F
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('p195', HERE/'low-time-h2-uniform-195.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
I, base = p.I, p.base
OUT = Path(__file__).with_suffix('.json')
ORDERS = tuple(range(0, 20, 2))
RADIUS = F(1, 10240)
TRACE = []
X = I(-1, 1)
X2 = I(0, 1)


def prange(c):
    return c[0] + c[1]*X + c[2]*X2


def dropped(c):
    return sum((c[j] * (X if j % 2 else X2) for j in range(3, len(c))), I(0))


class TM:
    def __init__(self, c, rem=None, op='seed', args=(), label=None, extra=None):
        self.c = [I.lift(a) for a in c]
        self.rem = I(0) if rem is None else rem
        self.id = len(TRACE)
        row = {'id':self.id, 'op':op, 'args':list(args),
               'coefficients':[a.data() for a in self.c], 'remainder':self.rem.data()}
        if label is not None:
            row['label'] = label
        if extra is not None:
            row['extra'] = extra
        TRACE.append(row)

    @staticmethod
    def lift(a):
        return a if isinstance(a, TM) else TM([a, 0, 0], op='constant', label=str(a))

    def __add__(self, other):
        other = TM.lift(other)
        return TM([a+b for a,b in zip(self.c,other.c)], self.rem+other.rem,
                  'add', (self.id,other.id))

    __radd__ = __add__

    def __neg__(self):
        return TM([-a for a in self.c], -self.rem, 'neg', (self.id,))

    def __sub__(self, other):
        return self + (-TM.lift(other))

    def __mul__(self, other):
        other = TM.lift(other)
        full = [sum((self.c[j]*other.c[n-j] for j in range(3)
                     if 0 <= n-j < 3), I(0)) for n in range(5)]
        rem = (dropped(full) + prange(self.c)*other.rem
               + prange(other.c)*self.rem + self.rem*other.rem)
        return TM(full[:3], rem, 'mul', (self.id,other.id))

    __rmul__ = __mul__

    def scale(self, value):
        value = F(value)
        a = I.rational(value)
        return TM([v*a for v in self.c],self.rem*a,'scale',(self.id,),
                  extra=str(value))

    def range(self):
        return prange(self.c) + self.rem

    def inverse(self):
        # v = f-a0, so 1/f = 1/a0-v/a0^2+v^2/a0^3-v^3/(a0^3*f).
        # The geometric identity is exact on any range excluding zero;
        # it requires no convergence or |v/a0|<1 assumption.
        a0 = self.c[0]
        whole = self.range()
        assert a0.lo > 0 and whole.lo > 0
        v = TM([0,self.c[1],self.c[2]],self.rem,'remove_constant',(self.id,))
        v2 = v*v
        inv = I(1)/a0
        c = [inv + v2.c[0]/a0**3,
             -v.c[1]/a0**2 + v2.c[1]/a0**3,
             -v.c[2]/a0**2 + v2.c[2]/a0**3]
        geometric = -(v.range()**3)/(a0**3*whole)
        rem = -v.rem/a0**2 + v2.rem/a0**3 + geometric
        return TM(c,rem,'inverse',(self.id,v.id,v2.id),
                  extra={'divisor_range':whole.data(), 'geometric_remainder':geometric.data()})


def tails():
    beta = I.rational(F(119,40))
    coefficient = sum((I(factorial(11)//factorial(11-j))*50**(11-j)
                       / beta**(j+1) for j in range(12)), I(0))
    space = 128 * (-50*beta).exp() * coefficient
    theta = (128*625*factorial(11)) * (1-25*beta).exp()
    return space,theta,space+theta


def quadrature(lam, pi, tail):
    h = I.rational(F(1,64))
    weights = {j:2*h**(j+1)/(j+1) for j in (0,2,4,6)}
    rw = 2*h**9/9
    total = {k:I(0) for k in ORDERS}
    errors = {k:I(0) for k in ORDERS}
    records = []
    for j in range(64):
        center = I.rational(F(2*j+1,64))
        domain = I(I.rational(F(2*j,64)).lo,I.rational(F(2*j+2,64)).hi)
        mk = base.multiply(base.theta_kernel_jet(center,pi),p.tilt_jet(center,lam))
        dk = base.multiply(base.theta_kernel_jet(domain,pi),p.tilt_jet(domain,lam))
        row = {'index':j,'center':center.data(),'domain':domain.data(),'orders':{}}
        for k in ORDERS:
            mid = base.moment_jet(center,k,mk)
            dom = base.moment_jet(domain,k,dk)
            poly = sum((mid[n]*weights[n] for n in weights),I(0))
            err = I(dom[8].magnitude())*rw
            total[k] = total[k] + poly + I(-err.hi,err.hi)
            errors[k] = errors[k] + err
            row['orders'][str(k)] = {'midpoint_coefficients':[a.data() for a in mid],
                                    'eighth_coefficient':dom[8].data(),
                                    'polynomial_integral':poly.data(),'error':err.data()}
        records.append(row)
    return {'lambda':lam.data(),'spatial_records':records,
            'moments':{str(k):(total[k]+I(0,tail.hi)).data() for k in ORDERS},
            'quadrature_error_bounds':{str(k):errors[k].data() for k in ORDERS}}


def read_i(v):
    return I(v['lower'],v['upper'])


def main():
    p.checks()
    assert sum((F(4)**j/factorial(j) for j in range(8)),F(0)) > 50
    assert sum((F(9)**j/factorial(j) for j in range(5)),F(0)) > 32
    pi = base.pi_bounds()
    spatial,theta,tail = tails()
    data = {'status':'running','scope':'original panel0 only; no RH or contact claim',
            'budget':{'parameter_degree':2,'lambda':['0','1/5120'],
                      'center':str(RADIUS),'radius':str(RADIUS),'spatial_panels':64,
                      'spatial_cutoff':2,'theta_terms':4,'spatial_order':8,'digits':100},
            'python':platform.python_version(),'pi':pi.data(),
            'tails':{'spatial':spatial.data(),'theta':theta.data(),'total':tail.data()},
            'input_sha256':{str(f.relative_to(HERE.parent.parent)):hashlib.sha256(f.read_bytes()).hexdigest()
                            for f in (Path(__file__),HERE/'low-time-h2-uniform-195.py',
                                      HERE.parent/'hankel/certify_hankel.py')},
            'quadrature':{}}
    for key,lam in (('center',F(1,10240)),('right',F(1,5120))):
        data['quadrature'][key] = quadrature(I.rational(lam),pi,tail)
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print(f'Completed all ten full moments at {key}',flush=True)
    center = {int(k):read_i(v) for k,v in data['quadrature']['center']['moments'].items()}
    right = {int(k):read_i(v) for k,v in data['quadrature']['right']['moments'].items()}
    moments = {}
    radius = I.rational(RADIUS)
    for k in range(0,14,2):
        c = [center[k+2*j]*radius**j/factorial(j) for j in range(3)]
        bound = (right[k+6]*radius**3/6).hi
        moments[k] = TM(c,I(-bound,bound),label=f'M{k}')
    inverse_mass = moments[0].inverse()
    q = [TM.lift(1)] + [(moments[2*n]*inverse_mass).scale(F((-1)**n,factorial(2*n)))
                        for n in range(1,7)]
    s = {}
    for n in range(1,7):
        s[n] = q[n].scale(-n) - sum((s[k]*q[n-k] for k in range(1,n)),TM.lift(0))
    a,b,c,d,e = (s[n] for n in range(2,7))
    minors = [a,a*c-b*b,a*(c*e-d*d)-b*(b*e-d*c)+c*(b*d-c*c)]
    final = minors[2].range()
    required = '>0 for the full determinant lower endpoint'
    summary = {'required':required,'determinant':final.data(),
               'final_polynomial_range':prange(minors[2].c).data(),
               'final_remainder':minors[2].rem.data(),
               'mass_range':moments[0].range().data(),
               'minor_ranges':[m.range().data() for m in minors],
               'strict_positive':final.lo>0,'strict_negative':final.hi<0,
               'zero_containing':final.lo<=0<=final.hi,
               'operation_count':len(TRACE),'failures':[] if final.lo>0 else ['determinant lower endpoint is not >0'],
               'budget_unchanged':True,'arithmetic_contract_conditional':True}
    signals = (DivisionByZero,InvalidOperation,Overflow,Underflow,Subnormal)
    data['arithmetic'] = {name:{'precision':ctx.prec,'rounding':ctx.rounding,
                               'traps':{s.__name__:ctx.traps[s] for s in signals},
                               'exceptional_flags':{s.__name__:ctx.flags[s] for s in signals}}
                          for name,ctx in (('DOWN',base.DOWN),('UP',base.UP),('NEAR',base.NEAR))}
    assert all(ctx.prec==100 and all(ctx.traps[s] and not ctx.flags[s] for s in signals)
               for ctx in (base.DOWN,base.UP,base.NEAR))
    data.update({'status':'certified_positive' if final.lo>0 else 'fixed_budget_inconclusive',
                 'trace':TRACE,'moment_models':{str(k):m.id for k,m in moments.items()},
                 'inverse_mass':inverse_mass.id,'q_models':[v.id for v in q],
                 'S_models':{str(n):v.id for n,v in s.items()},
                 'minor_models':[v.id for v in minors],'summary':summary})
    OUT.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    print(f'Full evidence: {OUT.relative_to(HERE.parent.parent)}')


if __name__ == '__main__':
    main()

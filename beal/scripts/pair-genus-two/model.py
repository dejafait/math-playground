"""Exact characteristic-zero pair-curve elimination; standard library only.

Full polynomial/rational-function residuals are saved, never sampled.
Coefficients throughout are in ascending degree order.
"""
from fractions import Fraction as Q
from math import comb, gcd as igcd, lcm
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / 'model-certificate.json'
SOURCE = HERE.parent / 'global-fiber-genus/forget-root-certificate.json'


def trim(p):
    p = list(map(Q, p))
    while p and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def neg(p):
    return tuple(-x for x in p)


def mul(p, q):
    r = [Q(0)] * max(0, len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return trim(r)


def scale(p, a):
    return trim([a*x for x in p])


def divrem(p, q):
    if not q:
        raise ZeroDivisionError
    p = trim(p)
    r = [Q(0)] * max(0, len(p)-len(q)+1)
    while p and len(p) >= len(q):
        k, a = len(p)-len(q), p[-1]/q[-1]
        r[k] += a
        p = add(p, neg((Q(0),)*k + scale(q, a)))
    return trim(r), p


def exact(p, q):
    d, r = divrem(p, q)
    assert not r, r
    return d


def gcd(p, q):
    # Primitive pseudo-remainders prevent coefficient explosion in Q[X].
    def primitive(a):
        den = lcm(*(x.denominator for x in a)) if a else 1
        a = [int(x*den) for x in a]
        content = 0
        for x in a:
            content = igcd(content, x)
        if not content:
            return ()
        if a[-1] < 0:
            content = -content
        return tuple(x//content for x in a)
    p,q=primitive(p),primitive(q)
    while q:
        r=p
        while r and len(r)>=len(q):
            k,a,b=len(r)-len(q),r[-1],q[-1]
            r=primitive(add(scale(r,b),neg((Q(0),)*k+scale(q,a))))
        p,q=q,r
    return scale(p, Q(1)/p[-1]) if p else ()


def derivative(p):
    return trim([i*p[i] for i in range(1, len(p))])


class Rat:
    def __init__(self, n=0, d=(1,)):
        n = trim(n if isinstance(n, (list, tuple)) else [n])
        d = trim(d)
        if not d:
            raise ZeroDivisionError
        g = gcd(n, d)
        n, d = exact(n, g), exact(d, g)
        self.n, self.d = scale(n, 1/d[-1]), scale(d, 1/d[-1])

    def __add__(self, b):
        b = rat(b)
        return Rat(add(mul(self.n, b.d), mul(b.n, self.d)), mul(self.d, b.d))

    __radd__ = __add__

    def __neg__(self):
        return Rat(neg(self.n), self.d)

    def __sub__(self, b):
        return self + -rat(b)

    def __rsub__(self, b):
        return rat(b) + -self

    def __mul__(self, b):
        b = rat(b)
        return Rat(mul(self.n, b.n), mul(self.d, b.d))

    __rmul__ = __mul__

    def __truediv__(self, b):
        b = rat(b)
        return Rat(mul(self.n, b.d), mul(self.d, b.n))

    def __rtruediv__(self, b):
        return rat(b) / self

    def __pow__(self, n):
        if n < 0:
            return (1/self)**(-n)
        a, b = Rat(1), self
        while n:
            if n % 2:
                a = a*b
            n //= 2
            if n:
                b = b*b
        return a

    def iszero(self):
        return not self.n

    def data(self):
        return {'numerator': [str(x) for x in self.n],
                'denominator': [str(x) for x in self.d]}


def rat(x):
    return x if isinstance(x, Rat) else Rat(x)


class Quad:
    """Q(X)[Y]/(Y²-relation), with its actual relation retained per element."""
    def __init__(self, a=0, b=0, relation=None):
        self.a, self.b, self.rel = rat(a), rat(b), rat(relation)

    def lift(self, x):
        if isinstance(x, Quad):
            assert (x.rel-self.rel).iszero()
            return x
        return Quad(x, 0, self.rel)

    def __add__(self, x):
        x = self.lift(x)
        return Quad(self.a+x.a, self.b+x.b, self.rel)

    __radd__ = __add__

    def __neg__(self):
        return Quad(-self.a, -self.b, self.rel)

    def __sub__(self, x):
        return self+-self.lift(x)

    def __rsub__(self, x):
        return self.lift(x)+-self

    def __mul__(self, x):
        x = self.lift(x)
        return Quad(self.a*x.a+self.b*x.b*self.rel,
                    self.a*x.b+self.b*x.a, self.rel)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.lift(x)
        norm = x.a*x.a-self.rel*x.b*x.b
        return self*Quad(x.a/norm, -x.b/norm, self.rel)

    def __rtruediv__(self, x):
        return self.lift(x)/self

    def __pow__(self, n):
        if n < 0:
            return (1/self)**(-n)
        a, b = self.lift(1), self
        while n:
            if n % 2:
                a = a*b
            n //= 2
            if n:
                b = b*b
        return a

    def iszero(self):
        return self.a.iszero() and self.b.iszero()

    def data(self):
        return {'constant': self.a.data(), 'quadratic': self.b.data()}


def evaluate(p, x):
    y = x*0
    for c in reversed(p):
        y = y*x+c
    return y


checks, evidence = {}, {}


def check(name, assertion, data=None):
    assert name not in checks
    checks[name] = bool(assertion)
    if data is not None:
        evidence[name] = data


def identity(name, value):
    check(name, value.iszero(), value.data())


raw = SOURCE.read_bytes()
source = json.loads(raw)
phi = [1]
for _ in range(5):
    phi = mul(phi, [1, 1, 3])
phi = mul(phi, [1, -5])
check('phi_all_coefficients', list(phi) == source['phi_coefficients_ascending'])
S6, S11 = (Q(1),)*6, (Q(1),)*11
Delta = add(scale(mul(S6, S6), 121), scale(S11, -396))
P8 = exact(Delta, (1, -2, 1))
check('ordered_discriminant_degree_eight', len(P8)-1 == 8)
check('P8_reciprocal', P8 == P8[::-1])
check('P8_squarefree',gcd(P8,derivative(P8))==(Q(1),))
# Recover R4 from P8/t^4 by the exact reciprocal recurrence C_(k+1)=T C_k-C_(k-1).
C = [(Q(2),), (Q(0), Q(1))]
for k in range(1, 5):
    C.append(add((Q(0),)+C[-1], neg(C[-2])))
R4 = (P8[4],)
for k in range(1, 5):
    R4 = add(R4, scale(C[k], P8[4+k]))
f6 = mul((-4, 0, 1), R4)
g = gcd(f6, derivative(f6))
check('sextic_degree', len(f6)-1 == 6)
check('sextic_squarefree', g == (Q(1),), [str(x) for x in g])
F = (1, 3, -3, -4, 1, 1)
K, L = (-1, -1, 1), (-1, 1, 1)


def from_model(T, W):
    ft, kt, lt = evaluate(F,T), evaluate(K,T), evaluate(L,T)
    u = (ft-11-kt*W)/(60*ft)
    M = 2-10*u
    z = -M*M*(T-2)*lt*lt/(300*(T+2)*kt*kt)
    return u,z


def to_model(u,z):
    d, e = 3*u*u+u+1-9*z, 6*u+1
    T = 2*(d*d-3*z*e*e)/(d*d+3*z*e*e)
    ft,kt = evaluate(F,T), evaluate(K,T)
    W = (ft-11-60*ft*u)/kt
    return T,W


T, W = Quad(Rat([0,1]), relation=Rat(f6)), Quad(0,1,Rat(f6))
u,z = from_model(T,W)
J=(T+2)*(T*T-1)
identity('F_plus_one_factor',evaluate(F,T)+1-evaluate(K,T)*J)
N=11*J+W
identity('z_removable_K_chart',z+N*N*(T-2)*evaluate(L,T)**2/
         (10800*(T+2)*evaluate(F,T)**2))
check('F_at_minus_two',evaluate(F,Rat(-2)).n==(Q(-1),))
check('R4_at_minus_two',evaluate(R4,Rat(-2)).n==(Q(-99),))
check('normalized_z_at_minus_two',-Q(396)*(-4)/10800==Q(11,75))
check('u_at_minus_two',Q(1,5)==(Q(-1)-11)/(60*(-1)))
check('u_z_at_plus_two',evaluate(F,Rat(2)).n==(Q(11),) and
      evaluate(K,Rat(2)).n==(Q(1),))
check('u_nonconstant', bool(u.b.n))
check('z_nonzero', not z.iszero())
# All H0,H1 coefficients reconstructed without trusting saved invariant data.
H = [{},{}]
for i,ci in enumerate(phi):
    for j in range(i+1):
        key = (i-j,j//2)
        H[j%2][key] = H[j%2].get(key,0)+ci*comb(i,j)*(-3)**(j//2)
H = [{m:c for m,c in h.items() if c} for h in H]
for name,h in zip(['H0','H1'],H):
    check(name+'_input_coefficients', source['invariant_polynomials'][name] ==
          [{'exponents_u_z':list(m),'coefficient':c} for m,c in sorted(h.items())])


def invariant(h,u,z):
    up = [u**i for i in range(12)]
    zp = [z**i for i in range(6)]
    return sum((c*up[i]*zp[j] for (i,j),c in h.items()),u*0)


print('Computing complete H1 substitution...', flush=True)
identity('H1_on_model', invariant(H[1],u,z))
print('Checking model-side inverse composition...', flush=True)
Tback,Wback=to_model(u,z)
identity('T_model_composition',Tback-T)
identity('W_model_composition',Wback-W)
s=invariant(H[0],u,z)
check('s_nonzero',not s.iszero())
check('s_minus_one_nonzero',not (s-1).iszero())

# Second composition in the ordered pair field; its invariant subfield is L109's B.
t,Y=Quad(Rat([0,1]),relation=Rat(P8)),Quad(0,1,Rat(P8))
x=(11*evaluate(S6,t)+(t-1)*Y)/(6*evaluate(S11,t))
y=t**5*x
aa,bb=(1-x)/5,(1-y)/5
uo,zo=(aa+bb)/2,-(aa-bb)**2/12
print('Checking ordered-pair identities and reverse composition...',flush=True)
identity('ordered_quadratic_equation',3*evaluate(S11,t)*x*x-11*evaluate(S6,t)*x+33)
qa,qb=3*aa*aa+aa+1,3*bb*bb+bb+1
identity('ordered_q_ratio',qa-t*qb)
identity('ordered_phi_equality',qa**5*(1-5*aa)-qb**5*(1-5*bb))
To,Wo=t+1/t,Y*(t*t-1)/t**3
identity('ordered_model_relation',Wo*Wo-evaluate(f6,To))
Tu,Wu=to_model(uo,zo)
identity('T_pair_map',Tu-To)
identity('W_pair_map',Wu-Wo)
ur,zr=from_model(Tu,Wu)
identity('u_pair_composition',ur-uo)
identity('z_pair_composition',zr-zo)
identity('s_ordered_transport',invariant(H[0],uo,zo)-qa**5*(1-5*aa))

failures=[k for k,v in checks.items() if not v]
result={
    'input':str(SOURCE.relative_to(HERE.parent.parent)),
    'input_sha256':sha256(raw).hexdigest(),
    'coefficients_ascending':{k:[str(c) for c in p] for k,p in
                              [('Delta',Delta),('P8',P8),('R4',R4),('f6',f6),('F',F),('K',K),('L',L)]},
    'model_maps':{'u':u.data(),'z':z.data(),'s':s.data()},
    'exact_residuals':evidence,
    'actual_degree':len(f6)-1,'required_degree':[5,6],
    'squarefree_gcd':[str(c) for c in g],
    'checks':checks,'check_count':len(checks),'failures':failures,
    'qualification':'Exact function-field checks. Proper normalization, dense-open nonvanishing and field identification are justified in the canonical lemma; no rational-point determination.'}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print('R4 coefficients:',result['coefficients_ascending']['R4'])
print('Sextic coefficients:',result['coefficients_ascending']['f6'])
print('Degree:',len(f6)-1,'required: 5 or 6; gcd(f,f\'):',result['squarefree_gcd'])
print('Checks:',len(checks),'failures:',failures,'certificate:',OUT)
assert not failures

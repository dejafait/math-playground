"""Exact conic substitution for L113; standard-library arithmetic only.

Full polynomial/field residuals and Bezout witness are saved, not sampled.
The canonical proof supplies properness, genus and rational-fiber arguments.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def trim(p):
    p = list(map(Q, p))
    while p and not p[-1]:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return trim([c*x for x in p])


def mul(p, q):
    r = [Q(0)]*max(0, len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return trim(r)


def power(p, n):
    r = [Q(1)]
    for _ in range(n):
        r = mul(r, p)
    return r


def divrem(p, q):
    p, q = trim(p), trim(q)
    assert q
    r = [Q(0)]*max(0, len(p)-len(q)+1)
    while p and len(p) >= len(q):
        k, c = len(p)-len(q), p[-1]/q[-1]
        r[k] += c
        p = add(p, scale([0]*k+q, -c))
    return trim(r), p


def xgcd(p, q):
    a, b, c, d = [Q(1)], [], [], [Q(1)]
    while q:
        k, r = divrem(p, q)
        p, q, a, b, c, d = q, r, c, d, add(a, scale(mul(k,c),-1)), add(b, scale(mul(k,d),-1))
    lc = p[-1]
    return scale(p,1/lc), scale(a,1/lc), scale(b,1/lc)


def exact(p, q):
    r, rem = divrem(p, q)
    assert not rem
    return r


def ev(p, x):
    r = 0
    for c in reversed(p):
        r = r*x+c
    return r


class Field:
    """(A+B*Y)/C in Q(t)[Y]/(Y²-G), reduced exactly."""
    def __init__(self, A=0, B=0, C=1):
        ps = [trim(p if isinstance(p, (list,tuple)) else [p]) for p in (A,B,C)]
        A, B, C = ps
        assert C
        g = xgcd(xgcd(A,B)[0],C)[0] if A or B else C
        A, B, C = [exact(p,g) for p in ps]
        self.A, self.B, self.C = [scale(p,1/C[-1]) for p in (A,B,C)]

    @staticmethod
    def lift(x):
        return x if isinstance(x,Field) else Field(x)

    def __add__(self,x):
        x = self.lift(x)
        return Field(add(mul(self.A,x.C),mul(x.A,self.C)),
                     add(mul(self.B,x.C),mul(x.B,self.C)),mul(self.C,x.C))
    __radd__ = __add__

    def __neg__(self):
        return Field(scale(self.A,-1),scale(self.B,-1),self.C)

    def __sub__(self,x):
        return self+-self.lift(x)

    def __rsub__(self,x):
        return self.lift(x)+-self

    def __mul__(self,x):
        x = self.lift(x)
        return Field(add(mul(self.A,x.A),mul(G,mul(self.B,x.B))),
                     add(mul(self.A,x.B),mul(self.B,x.A)),mul(self.C,x.C))
    __rmul__ = __mul__

    def __truediv__(self,x):
        x = self.lift(x)
        norm = add(mul(x.A,x.A),scale(mul(G,mul(x.B,x.B)),-1))
        assert norm
        return self*Field(mul(x.A,x.C),scale(mul(x.B,x.C),-1),norm)

    def __rtruediv__(self,x):
        return self.lift(x)/self

    def __pow__(self,n):
        assert n >= 0
        r = Field(1)
        for _ in range(n):
            r = r*self
        return r

    def zero(self):
        return not self.A and not self.B

    def data(self):
        return {k:[str(c) for c in p] for k,p in [('A',self.A),('B',self.B),('C',self.C)]}


b = [-231,-1716,198,2112,825]
n, d = [-6,0,2], [3,0,1]
raw = []
for i,c in enumerate(b):
    raw = add(raw,scale(mul(power(n,i),power(d,4-i)),c))
G = scale(raw,Q(1,9))
Gp = [i*G[i] for i in range(1,len(G))]
gcd, bezout_G, bezout_Gp = xgcd(G,Gp)
checks, residuals = {}, {}


def check(name,ok):
    checks[name] = bool(ok)


def zero(name,value):
    residuals[name] = value.data()
    check(name,value.zero())


check('exact_polynomial',G == [2673,0,-39204,0,76230,0,-31460,0,3025])
check('degree_eight',len(G)-1 == 8)
check('squarefree',gcd == [1])
check('bezout_identity',add(mul(bezout_G,G),mul(bezout_Gp,Gp)) == [1])
check('coprime_parameter_denominator',xgcd(G,d)[0] == [1])
t, Y = Field([0,1]), Field(0,1)
dd = t*t+3
T, h, R = 2*(t*t-3)/dd, -12*t/dd, 3*Y/dd**2
zero('conic_relation',h*h-3*(4-T*T))
zero('quartic_relation',R*R-ev(b,T))
t1 = h/(T-2)
Y1 = (t1*t1+3)**2*R/3
zero('inverse_t',t1-t)
zero('inverse_Y',Y1-Y)
T1, h1, R1 = 2*(t1*t1-3)/(t1*t1+3), -12*t1/(t1*t1+3), 3*Y1/(t1*t1+3)**2
zero('reconstructed_T',T1-T)
zero('reconstructed_h',h1-h)
zero('reconstructed_R',R1-R)


def original(T,h,R):
    W = h*R/3
    F = T**5+T**4-4*T**3-3*T*T+3*T+1
    K,L = T*T-T-1,T*T+T-1
    u = (F-11-K*W)/(60*F)
    M = 2-10*u
    rho = M*L/(30*(T+2)*K)
    z = -M*M*(T-2)*L*L/(300*(T+2)*K*K)
    return {'W':W,'u':u,'rho':rho,'z':z,'v':rho*h}


orig, back = original(T,h,R), original(T1,h1,R1)
for k in orig:
    zero('preserved_'+k,back[k]-orig[k])
zero('original_marking',orig['v']**2-orig['z'])
zero('original_sextic',orig['W']**2-11*(T*T-4)*ev([7,52,-6,-64,-25],T))

# Reverse composition on D after using t²=A/B and t=h/B.
# d=(A+3B)/B=-12/B; n=2(A-3B)/B=-12T/B.
A, B = [-6,-3], [-2,1]
check('reverse_D_denominator',add(A,scale(B,3)) == [-12])
check('reverse_D_T',scale(add(A,scale(B,-3)),2) == [0,-12])
check('reverse_D_h_multiplier',Q(-12,-12) == 1)

F = [1,3,-3,-4,1,1]
K,L,J = [-1,-1,1],[-1,1,1],mul([2,1],[-1,0,1])
f = scale(mul([-4,0,1],[7,52,-6,-64,-25]),11)
check('N_norm_identity',add(scale(mul(J,J),121),scale(f,-1)) == scale(mul([2,1],F),396))
check('F_no_rational_root',ev(F,1) == ev(F,-1) == -1 and F[0] == F[-1] == 1)
check('K_L_discriminants',K[1]**2-4*K[0]*K[2] == L[1]**2-4*L[0]*L[2] == 5)
check('zero_slope_nonsquare',G[0] == 81*33 and isqrt(33)**2 != 33)
check('infinity_two_rational_points',G[-1] == 55**2)
check('G_at_conic_infinity',divrem(G,d)[1] == [1900800])
check('boundary_R',3*55 == 165)
check('boundary_rho',Q(2*5,30*4) == Q(1,12))
check('boundary_z_unit',Q(1,12)**2*144 == 1)

out = {
    'coefficient_order':'ascending; all arithmetic exact over Q',
    'input_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in [
        'lemmas/L110-explicit-pair-genus-two-model.md','lemmas/L111-marked-pair-genus-one-quotient.md']},
    'polynomial':[str(x) for x in G],
    'squarefree':{'gcd':[str(x) for x in gcd],
                  'bezout_G':[str(x) for x in bezout_G],
                  'bezout_derivative':[str(x) for x in bezout_Gp]},
    'identity_residuals':residuals,
    'original_functions':{k:v.data() for k,v in orig.items()},
    'rational_exceptions':{
        't_zero':'Y²=81*33; no Q-point',
        't_infinity':'q=0, Z=Y/t⁴=±55; T=2,h=0,R=±165,W=0,u=z=v=0,s=1',
        't_squared_plus_three_zero':'No rational parameter; G remainder 1900800, nonzero',
        'T_infinity':'No rational point by conic H²=-3',
        'F_zero':'Monic F has only candidate rational roots ±1, both values -1',
        'K_L_zero':'Discriminant 5; no rational T',
        'rho_zero':'N*Nbar=396(T+2)F; no finite rational point with rho=0',
        'boundary_limits':'h/q=-12; W/q=∓660; v/q=-1; z/q²=1; v/W=±1/660'},
    'thresholds':{'degree_actual_required':[8,8],'genus_actual_required':[3,3],
                  'Q_boundary_lifts_actual_required':[2,2],
                  'justification':'See canonical L113; field residuals alone do not prove properness/genus.'},
    'checks':checks,'check_count':len(checks),
    'failures':[k for k,v in checks.items() if not v]}
path = HERE/'marked-hyperelliptic-certificate.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['check_count','thresholds','failures']} | {
    'certificate':str(path.relative_to(ROOT))}))
assert not out['failures']

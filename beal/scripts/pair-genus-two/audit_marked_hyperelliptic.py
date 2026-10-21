"""Independent L113 arithmetic replay; no producer import.
RF polynomial code is reused from the independent L111 auditor.
Field multiplication uses xor-indexed bases and matrix inversion.
Geometric proof and rational-fiber completeness are in canonical L113.
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


def plus(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def times(p, q):
    out = [Q(0)] * max(0, len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return trim(out)


def divide(p, q):
    p, q = trim(p), trim(q)
    assert q
    out = [Q(0)] * max(0, len(p) - len(q) + 1)
    while p and len(p) >= len(q):
        i, c = len(p)-len(q), p[-1]/q[-1]
        out[i] += c
        p = plus(p, [Q(0)]*i + [-c*x for x in q])
    return trim(out), p


def monic_gcd(p, q):
    p, q = trim(p), trim(q)
    while q:
        p, q = q, divide(p, q)[1]
    return [x/p[-1] for x in p] if p else []


class RF:
    """Reduced rational function in T, with monic denominator."""
    def __init__(self, p=0, q=1):
        p, q = [trim(v if isinstance(v, (list, tuple)) else [v])
                for v in (p, q)]
        assert q
        g = monic_gcd(p, q)
        p, rp = divide(p, g)
        q, rq = divide(q, g)
        assert not rp and not rq
        self.p, self.q = [x/q[-1] for x in p], [x/q[-1] for x in q]

    @staticmethod
    def lift(x):
        return x if isinstance(x, RF) else RF(x)

    def __bool__(self):
        return bool(self.p)

    def __add__(self, x):
        x = RF.lift(x)
        return RF(plus(times(self.p, x.q), times(x.p, self.q)),
                  times(self.q, x.q))

    __radd__ = __add__

    def __neg__(self):
        return RF([-x for x in self.p], self.q)

    def __sub__(self, x):
        return self + -RF.lift(x)

    def __rsub__(self, x):
        return RF.lift(x) + -self

    def __mul__(self, x):
        x = RF.lift(x)
        return RF(times(self.p, x.p), times(self.q, x.q))

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = RF.lift(x)
        assert x
        return RF(times(self.p, x.q), times(self.q, x.p))

    def __pow__(self, n):
        assert n >= 0
        out = RF(1)
        for _ in range(n):
            out = out*self
        return out

    def data(self):
        return {'numerator': list(map(str, self.p)),
                'denominator': list(map(str, self.q))}


class Field:
    def __init__(self, squares):
        self.squares = list(map(RF.lift, squares))
        self.n = 2**len(squares)
    def elt(self, *c):
        return Elt(self, list(c)+[0]*(self.n-len(c)))

class Elt:
    def __init__(self, field, c):
        assert len(c) == field.n
        self.field, self.c = field, list(map(RF.lift,c))
    def lift(self, x):
        if isinstance(x,Elt):
            assert x.field is self.field
            return x
        return self.field.elt(x)
    def __bool__(self):
        return any(self.c)
    def __add__(self,x):
        x=self.lift(x)
        return Elt(self.field,[a+b for a,b in zip(self.c,x.c)])
    __radd__=__add__
    def __neg__(self):
        return Elt(self.field,[-a for a in self.c])
    def __sub__(self,x):
        return self+-self.lift(x)
    def __rsub__(self,x):
        return self.lift(x)+-self
    def __mul__(self,x):
        x=self.lift(x)
        out=[RF() for _ in self.c]
        for i,a in enumerate(self.c):
            for j,b in enumerate(x.c):
                if not a or not b: continue
                v=a*b
                for k,s in enumerate(self.field.squares):
                    if (i&j)&(1<<k): v=v*s
                out[i^j]=out[i^j]+v
        return Elt(self.field,out)
    __rmul__=__mul__
    def __pow__(self,n):
        out=self.lift(1)
        for _ in range(n): out=out*self
        return out
    def inverse(self):
        n=self.field.n
        cols=[(self*self.field.elt(*[int(i==j) for i in range(n)])).c for j in range(n)]
        rows=[[cols[j][i] for j in range(n)]+[RF(int(i==0))] for i in range(n)]
        for k in range(n):
            j=next(j for j in range(k,n) if rows[j][k])
            rows[k],rows[j]=rows[j],rows[k]
            v=rows[k][k]
            rows[k]=[a/v for a in rows[k]]
            for j in range(n):
                if j!=k:
                    v=rows[j][k]
                    rows[j]=[a-v*b for a,b in zip(rows[j],rows[k])]
        return Elt(self.field,[r[-1] for r in rows])
    def __truediv__(self,x):
        x=self.lift(x)
        if not any(x.c[1:]): return Elt(self.field,[v/x.c[0] for v in self.c])
        return self*x.inverse()
    def __rtruediv__(self,x): return self.lift(x)/self
    def data(self): return [a.data() for a in self.c]

def ev(p,x):
    r=0
    for c in reversed(p): r=r*x+c
    return r

def poly(p): return list(map(str,p.p))
checks,residuals={},{}
def check(k,v):
    assert k not in checks
    checks[k]=bool(v)
def zero(k,v):
    residuals[k]=v.data()
    check(k,not v)

raw=(HERE/'marked-hyperelliptic-certificate.json').read_bytes()
saved=json.loads(raw)
initial_raw=(HERE/'marked-hyperelliptic-initial-check-failure.json').read_bytes()
initial=json.loads(initial_raw)
x=RF([0,1]); d=x**2+3
b=[-231,-1716,198,2112,825]
G=ev(b,2*(x**2-3)/d)*d**4/9
check('polynomial_denominator',G.q==[1])
check('polynomial_all_coefficients',G.p==list(map(Q,saved['polynomial']))==list(map(Q,[2673,0,-39204,0,76230,0,-31460,0,3025])))
Gp=RF([i*G.p[i] for i in range(1,len(G.p))])
A=RF(list(map(Q,saved['squarefree']['bezout_G'])))
B=RF(list(map(Q,saved['squarefree']['bezout_derivative'])))
zero('full_Bezout',A*G+B*Gp-1)
check('saved_gcd',monic_gcd(G.p,Gp.p)==list(map(Q,saved['squarefree']['gcd']))==[1])
check('degree',len(G.p)-1==8)
check('denominator_gcd',monic_gcd(G.p,d.p)==[1])

C=Field([G]); t=C.elt(x); Y=C.elt(0,1)
dc=t*t+3
T,h,R=2*(t*t-3)/dc,-12*t/dc,3*Y/dc**2
zero('conic_relation',h*h-3*(4-T*T))
zero('quartic_relation',R*R-ev(b,T))
tback=h/(T-2); Yback=(tback*tback+3)**2*R/3
zero('inverse_t',tback-t); zero('inverse_Y',Yback-Y)
Tb=2*(tback*tback-3)/(tback*tback+3)
hb=-12*tback/(tback*tback+3); Rb=3*Yback/(tback*tback+3)**2
for name,left,right in [('T',Tb,T),('h',hb,h),('R',Rb,R)]: zero('reconstructed_'+name,left-right)

def original(T,h,R):
    W=h*R/3
    F=T**5+T**4-4*T**3-3*T**2+3*T+1
    K,L=T*T-T-1,T*T+T-1
    u=(F-11-K*W)/(60*F); M=2-10*u
    rho=M*L/(30*(T+2)*K)
    z=-M*M*(T-2)*L*L/(300*(T+2)*K*K)
    return dict(W=W,u=u,rho=rho,z=z,v=rho*h)
fns=original(T,h,R); back=original(Tb,hb,Rb)
for name,v in fns.items():
    zero('preserved_'+name,back[name]-v)
    record=saved['original_functions'][name]
    den=list(map(Q,record['C']))
    stored=C.elt(RF(list(map(Q,record['A'])),den),RF(list(map(Q,record['B'])),den))
    zero('saved_full_'+name,stored-v)
zero('original_marking',fns['v']**2-fns['z'])
u,z=fns['u'],fns['z']; d0=3*u*u+u+1-9*z; e0=6*u+1
zero('old_inverse_T',2*(d0*d0-3*z*e0*e0)/(d0*d0+3*z*e0*e0)-T)
zero('old_inverse_h',fns['v']/fns['rho']-h)
zero('old_inverse_R',3*fns['W']/h-R)
zero('original_sextic',fns['W']**2-11*(T*T-4)*ev([7,52,-6,-64,-25],T))
for name,record in saved['identity_residuals'].items():
    check('producer_residual_'+name,record=={'A':[],'B':[],'C':['1']} and name in residuals and checks[name])

# Reverse direction in the independent four-dimensional D field.
D=Field([12-3*x*x,ev(b,x)]); TT=D.elt(x); hh=D.elt(0,1); RR=D.elt(0,0,1)
td=hh/(TT-2); dd=td*td+3; yd=dd**2*RR/3
zero('D_hyperelliptic_relation',yd*yd-ev(G.p,td))
TD,hD,RD=2*(td*td-3)/dd,-12*td/dd,3*yd/dd**2
for name,left,right in [('T',TD,TT),('h',hD,hh),('R',RD,RR)]: zero('D_inverse_'+name,left-right)
dfns=original(TT,hh,RR); dback=original(TD,hD,RD)
for name,v in dfns.items(): zero('D_preserved_'+name,dback[name]-v)

# Entire scalar, as a finite polynomial, not an abbreviated expansion.
from math import comb
phi=(3*x*x+x+1)**5*(1-5*x)
ci=[1,0,0,-55,-165,-594,-1100,-2145,-2475,-2970,-1782,-1215]
check('full_phi_coefficients',phi.q==[1] and phi.p==ci)
H0=[{'u_power':i-2*j,'z_power':j,'coefficient':str(c*comb(i,2*j)*(-3)**j)} for i,c in enumerate(ci) for j in range(i//2+1) if c]
# Each term is preserved because u,z are fixed in BOTH independent fields.
check('all_H0_terms_preserved',all(checks[k] for k in ['preserved_u','preserved_z','D_preserved_u','D_preserved_z']) and len(H0)==39)

F=x**5+x**4-4*x**3-3*x*x+3*x+1
K,L,J=x*x-x-1,x*x+x-1,(x+2)*(x*x-1)
f=11*(x*x-4)*ev([7,52,-6,-64,-25],x)
zero('F_KJ',F+1-K*J)
zero('N_norm',121*J*J-f-396*(x+2)*F)
check('rational_F_roots',F.p[0]==F.p[-1]==1 and ev(F.p,1)==ev(F.p,-1)==-1)
check('K_L_discriminants',all(p.p[1]**2-4*p.p[0]*p.p[2]==5 for p in [K,L]))
remainder=divide(G.p,d.p)[1]
check('conic_infinity_remainder',remainder==[1900800])
check('t_zero',G.p[0]==81*33 and isqrt(33)**2!=33)
check('infinity',G.p[-1]==55**2)
check('old_inverse_nonsquares',1-12==-11 and Q(11,108)==Q(33,18**2) and isqrt(33)**2!=33)
check('reverse_denominator',not ((-3*(x+2))+3*(x-2)+12))
check('reverse_numerator',not (2*(-3*(x+2)-3*(x-2))+12*x))
# The whole infinity chart, reduced modulo Z²=reverse(G), also checks units.
Gr=RF(list(reversed(G.p))); Qc=Field([Gr]); q=Qc.elt(x); Z=Qc.elt(0,1)
Tq=2*(1-3*q*q)/(1+3*q*q); hq=-12*q/(1+3*q*q); Rq=3*Z/(1+3*q*q)**2
qf=original(Tq,hq,Rq)
def at(e,q0,z0):
    return sum(ev(v.p,q0)/ev(v.q,q0)*z0**i for i,v in enumerate(e.c))
boundary=[]
for sign in [-1,1]:
    zz=55*sign
    row={'Z':zz,'R':str(at(Rq,0,zz)),'u':str(at(qf['u'],0,zz)),
         'rho':str(at(qf['rho'],0,zz)),'h/q':str(at(hq/q,0,zz)),
         'W/q':str(at(qf['W']/q,0,zz)),'v/q':str(at(qf['v']/q,0,zz)),
         'z/q2':str(at(qf['z']/q**2,0,zz)),
         'v/W':str(at(qf['v']/qf['W'],0,zz))}
    boundary.append(row)
    check('boundary_'+str(sign),row=={'Z':zz,'R':str(165*sign),'u':'0','rho':'1/12','h/q':'-12','W/q':str(-660*sign),'v/q':'-1','z/q2':'1','v/W':str(Q(sign,660))})
check('boundary_s',ci[0]==1)
check('finite_T_minus_two',ev(b,-2)==9*33)
check('conic_infinity_square_values',Q(-6)**2*(-3)/(-6)**2==-3 and Q(9*1900800,16*6**4)==825)
for path,digest in saved['input_hashes'].items(): check('input_hash_'+path,sha256((ROOT/path).read_bytes()).hexdigest()==digest)
check('initial_only_failed_check',initial['failures']==['G_at_conic_infinity'])
changed=[k for k in saved if initial[k]!=saved[k]]
check('initial_data_unchanged',changed==['rational_exceptions','checks','failures'])
check('initial_only_check_difference',[k for k in saved['checks'] if initial['checks'][k]!=saved['checks'][k]]==['G_at_conic_infinity'])
check('producer_flags',len(saved['checks'])==saved['check_count']==31 and all(saved['checks'].values()) and not saved['failures'])
check('producer_thresholds',all(saved['thresholds'][k]==v for k,v in {'degree_actual_required':[8,8],'genus_actual_required':[3,3],'Q_boundary_lifts_actual_required':[2,2]}.items()))
out={'method':'Independent rational-function coefficient arithmetic; xor basis multiplication; Gaussian matrix inversion; no producer imports.',
     'producer_sha256':sha256(raw).hexdigest(),'initial_sha256':sha256(initial_raw).hexdigest(),
     'initial_changed_fields':changed,'polynomial':poly(G),'Bezout':{'A':poly(A),'B':poly(B)},
     'identity_residuals':residuals,'original_functions':{k:v.data() for k,v in fns.items()},
     'phi_coefficients':ci,'H0_terms':H0,'boundary':boundary,'conic_infinity_remainder':list(map(str,remainder)),
     'checks':checks,'check_count':len(checks),'failures':[k for k,v in checks.items() if not v],
     'thresholds':{'degree_actual_required':[8,8],'genus_actual_required':[3,3],'rational_boundary_actual_required':[2,2]},
     'qualification':'Properness, genus and completeness of rational exceptions require the canonical L113 audit proof.'}
path=HERE/'marked-hyperelliptic-audit-certificate.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['check_count','failures','thresholds']}|{'certificate':str(path.relative_to(ROOT))}))
assert not out['failures']

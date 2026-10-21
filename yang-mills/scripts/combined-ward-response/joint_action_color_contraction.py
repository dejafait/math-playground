"""Exact complete local color contraction, not an actual-probe evaluation."""
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial
from pathlib import Path
import json

DIM = 12
ZERO = (0,) * DIM

def add(*ps):
    out = {}
    for p in ps:
        for e, v in p.items():
            out[e] = out.get(e, F(0)) + v
    return {e: v for e, v in out.items() if v}

def sc(c, p):
    return {e: c*v for e,v in p.items() if c*v}

def mul(p,q):
    out = {}
    for e,v in p.items():
        for f,w in q.items():
            h = tuple(a+b for a,b in zip(e,f))
            if sum(h) <= 4:
                out[h] = out.get(h,F(0)) + v*w
    return {e:v for e,v in out.items() if v}

def va(*vs):
    return tuple(add(*(v[c] for v in vs)) for c in range(3))

def vs(c,v):
    return tuple(sc(c,p) for p in v)

def dot(v,w):
    return add(*(mul(p,q) for p,q in zip(v,w)))

def br(v,w):
    return tuple(add(sc(-1,mul(v[(c+1)%3],w[(c+2)%3])),
                     mul(v[(c+2)%3],w[(c+1)%3])) for c in range(3))

y = [tuple({tuple(int(j==3*l+c) for j in range(DIM)):F(1)}
           for c in range(3)) for l in range(4)]
w1=w2=w3=({}, {}, {})
scalar={ZERO:F(1)}
vector=({}, {}, {})
for Y in y:
    old1,old2,old3=w1,w2,w3
    w1=va(old1,Y)
    w2=va(old2,vs(F(1,2),br(old1,Y)))
    w3=va(old3,vs(F(1,2),br(old2,Y)),
          vs(F(1,12),br(old1,br(old1,Y))),
          vs(F(1,12),br(Y,br(Y,old1))))
    yy=dot(Y,Y)
    es=add({ZERO:F(1)},sc(F(-1,8),yy),sc(F(1,384),mul(yy,yy)))
    ev=va(Y,tuple(sc(F(-1,24),mul(yy,z)) for z in Y))
    scalar,vector=(add(mul(scalar,es),sc(F(-1,4),dot(vector,ev))),
                   va(tuple(mul(scalar,z) for z in ev),
                      tuple(mul(es,z) for z in vector),vs(F(1,2),br(vector,ev))))
q=add(sc(F(1,2),dot(w2,w2)),dot(w1,w3))
q_ind=add(sc(-4,{e:v for e,v in scalar.items() if sum(e)==4}),
          sc(F(1,96),mul(dot(w1,w1),dot(w1,w1))))
failures=[]
if q != q_ind:
    failures.append('BCH versus independent exponential product')
signs=(1,1,-1,-1)
comp=(0,1,0,1)
labels=('mu_mu','nu_nu','mu_nu')
matrices={label:[[F(0) for _ in range(4)] for _ in range(4)] for label in labels}
full_tensor={}
for e,coeff in q.items():
    indices=tuple(j for j,n in enumerate(e) for _ in range(n))
    perms=set(permutations(indices))
    k=coeff/len(perms)
    for a,b,c,d in perms:
        full_tensor[(a,b,c,d)]=k
        la,ca=divmod(a,3); lb,cb=divmod(b,3)
        lc,cc=divmod(c,3); ld,cd=divmod(d,3)
        if ca != cb or cc != cd:
            continue
        label=('mu_mu' if comp[la]==comp[lb]==0 else
               'nu_nu' if comp[la]==comp[lb]==1 else 'mu_nu')
        matrices[label][lc][ld] += -24*k*signs[la]*signs[lb]

# Independent coefficient extraction by two formal color-diagonal
# contraction operators on the exponential-product polynomial. D_U D_V q
# equals 24 K:U:V and counts all repeated-variable multiplicities.
def differentiate(poly,i,j):
    out={}
    for e,v in poly.items():
        if e[i] < 1 or e[j] < 1+int(i==j):
            continue
        mult=e[i]*(e[j]-int(i==j))
        f=list(e); f[i]-=1; f[j]-=1
        out[tuple(f)]=out.get(tuple(f),F(0))+mult*v
    return out
checks=[]
for label in labels:
    du={}
    for la,lb,c in product(range(4),range(4),range(3)):
        typ=('mu_mu' if comp[la]==comp[lb]==0 else
             'nu_nu' if comp[la]==comp[lb]==1 else 'mu_nu')
        if typ==label:
            du=add(du,sc(signs[la]*signs[lb],differentiate(q_ind,3*la+c,3*lb+c)))
    for l,m in product(range(4),repeat=2):
        value=-sum(differentiate(du,3*l+c,3*m+c).get(ZERO,F(0)) for c in range(3))
        ok=value==matrices[label][l][m]
        checks.append({'label':label,'l':l+1,'m':m+1,'actual':str(value),
                       'required':str(matrices[label][l][m]),'passed':ok})
        if not ok: failures.append(checks[-1])

# Exact rational check of the permutation-averaged scalar integrand.
# The common denominator is 8*(X+Y+Z)^2; no quadrature is used.
X,Y,Z=({tuple(int(i==j) for i in range(3)):F(1)} for j in range(3))
lam=add(X,Y,Z)
sq=add(mul(X,X),mul(Y,Y),mul(Z,Z))
xy=mul(X,Y)
num=add(sc(2,mul(xy,add(mul(X,lam),sc(-1,sq)))),
        sc(2,mul(mul(add({(0,0,0):F(12)},sc(-4,X)),Y),
                     add(mul(Y,lam),sc(-1,sq)))),
        sc(-3,mul(xy,mul(add(X,sc(-1,Y)),add(X,sc(-1,Y))))))
sym={}
for perm in permutations(range(3)):
    sym=add(sym,{tuple(e[j] for j in perm):v for e,v in num.items()})
if sym: failures.append('Scalar permutation identity')
scalar_check={'common_denominator':'8*(X+Y+Z)^2',
              'unsymmetrized_numerator':[{'powers':e,'value':str(v)} for e,v in sorted(num.items())],
              'sum_over_all_six_permutations':[{'powers':e,'value':str(v)} for e,v in sorted(sym.items())],
              'passed':not sym}

# Independently assemble centered rows and both ordered mixed matrices
# using exact complex rational arithmetic on finite half-fibers.
class CQ:
    def __init__(self,r=0,i=0): self.r,self.i=F(r),F(i)
    def __add__(self,b):
        if not isinstance(b,CQ): b=CQ(b)
        return CQ(self.r+b.r,self.i+b.i)
    __radd__=__add__
    def __neg__(self): return CQ(-self.r,-self.i)
    def __sub__(self,b): return self+-b
    def __mul__(self,b):
        if not isinstance(b,CQ): b=CQ(b)
        return CQ(self.r*b.r-self.i*b.i,self.r*b.i+self.i*b.r)
    __rmul__=__mul__
    def conj(self): return CQ(self.r,-self.i)
    def __pow__(self,n):
        if n<0: return self.conj()**(-n) # used only for unit modulus
        out=CQ(1)
        for _ in range(n): out=out*self
        return out
    def zero(self): return self.r==self.i==0

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def pair(a,W,b):
    return sum(a[j]*W[j][k]*b[k].conj() for j in range(4) for k in range(4))

def rowcomp(j,z): return [z if k==j else CQ() for k in range(4)]

row_checks=[]
eta=[F(3,5),F(5,13),F(8,17),F(7,25)]
half_sin=[F(4,5),F(12,13),F(15,17),F(24,25)]
d=[2*t for t in half_sin]
f=[t*t for t in eta]
l4=sum(t*t for t in d)
P=[[F(j==k)-d[j]*d[k]/l4 for k in range(4)] for j in range(4)]
for ur in range(4):
    v=[eta[j]*int(j==ur) for j in range(4)]
    vd=sum(v[j]*d[j] for j in range(4))
    R=[[f[j]*(vd*int(j==k)-d[j]*v[k]) for k in range(4)] for j in range(4)]
    PR=mm(P,R)
    Q=[[(PR[j][k]-PR[k][j])/(2*l4) for k in range(4)] for j in range(4)]
    W=[[CQ(0,z) for z in row] for row in Q]
    for mu,nu in ((1,2),(1,3),(2,3)):
        dr=[rowcomp(mu,CQ(eta[nu],-half_sin[nu])),
            rowcomp(nu,CQ(eta[mu],half_sin[mu])),
            rowcomp(mu,-CQ(eta[nu],half_sin[nu])),
            rowcomp(nu,-CQ(eta[mu],-half_sin[mu]))]
        for count in (1,3):
            axial_phase=CQ(eta[0],half_sin[0])
            pref=sum(axial_phase**(-(2*r+1)) for r in range(count))
            wr=[rowcomp(0,sum(dr[l][j]*CQ(0,d[j]) for j in range(4))*pref)
                for l in range(4)]
            zQ=-d[nu]*Q[mu][0]+d[mu]*Q[nu][0]
            brackets=(d[mu]*d[nu]*zQ-12*f[mu]*d[nu]*Q[nu][0],
                      -d[mu]*d[nu]*zQ-12*f[nu]*d[mu]*Q[mu][0],
                      12*eta[mu]*eta[nu]*(d[nu]*Q[mu][0]+d[mu]*Q[nu][0]))
            defects=[]
            for label,bracket in zip(labels,brackets):
                H=matrices[label]
                direct=sum(H[l][m]*pair(dr[l],W,dr[m]) for l,m in product(range(4),repeat=2))
                mixed=-sum(H[l][m]*(pair(dr[l],W,wr[m])+pair(wr[l],W,dr[m]))
                           for l,m in product(range(4),repeat=2))
                defects.append(direct)
                defects.append(mixed-CQ(-2*pref.r*bracket))
            ok=all(z.zero() for z in defects)
            row_checks.append({'u_component':ur+1,'plane':[mu+1,nu+1],'prefix_length':count,
                               'six_exact_defects':[[str(z.r),str(z.i)] for z in defects],
                               'passed':ok})
            if not ok: failures.append(row_checks[-1])

cert={'scope':'Exact local tensor algebra only; no actual heat values or infinite kernel sums.',
      'polynomial_coefficients':[{'powers':e,'BCH':str(v),'product':str(q_ind.get(e,0))}
                                 for e,v in sorted(q.items())],
      'polynomial_identity':q==q_ind,'polynomial_difference':[
          {'powers':e,'value':str(v)} for e,v in sorted(add(q,sc(-1,q_ind)).items())],
      'matrices':{k:[[str(v) for v in row] for row in m] for k,m in matrices.items()},
      'checks':checks,'ordered_row_checks':row_checks,'scalar_identity':scalar_check,'failures':failures}
path=Path(__file__).with_name('joint-action-color-contraction-certificate.json')
path.write_text(json.dumps(cert,indent=2)+'\n')
print('Full quartic polynomial identity:',q==q_ind,'nonzero coefficients:',len(q))
for label,m in matrices.items():
    print(label,[[str(v) for v in row] for row in m])
print('Exact differential checks:',sum(c['passed'] for c in checks),'required:',len(checks))
print('Scalar permutation identity:',not sym,'required: zero polynomial')
print('Ordered finite-prefix checks:',sum(c['passed'] for c in row_checks),'required:',len(row_checks))
print('Failures:',failures)
print('Certificate:',path)
if failures: raise SystemExit(1)

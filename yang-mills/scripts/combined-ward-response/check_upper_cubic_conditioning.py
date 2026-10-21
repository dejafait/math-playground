"""Exact conditional-cumulant algebra; finite surrogate, no box asymptotics."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from pathlib import Path
import json

n = 5
m = 3*n
zero = (0,)*m

def add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0))+c
    return {e:c for e,c in out.items() if c}

def scale(c,p):
    return {e:c*v for e,v in p.items() if c*v}

def mul(p,q):
    out = {}
    for e,c in p.items():
        for h,d in q.items():
            t = tuple(a+b for a,b in zip(e,h))
            out[t] = out.get(t,F(0))+c*d
    return {e:c for e,c in out.items() if c}

def variable(i):
    return {tuple(int(j==i) for j in range(m)):F(1)}

C = [[F(0) for _ in range(n)] for _ in range(n)]
for i,v in enumerate([2,3,5,F(1,2),F(3,4)]):
    C[i][i] = F(v)
C[3][4] = C[4][3] = F(1,4)

@lru_cache(None)
def moment(e):
    if not any(e):
        return F(1)
    if any(sum(e[c*n:(c+1)*n])%2 for c in range(3)):
        return F(0)
    i = next(j for j,v in enumerate(e) if v)
    tail = list(e)
    tail[i] -= 1
    total = F(0)
    for j in range(i//n*n,(i//n+1)*n):
        if tail[j] and C[i%n][j%n]:
            h = tail.copy()
            h[j] -= 1
            total += tail[j]*C[i%n][j%n]*moment(tuple(h))
    return total

def expect(p):
    return sum((c*moment(e) for e,c in p.items()),F(0))

def derivative(p,j):
    color, edge = divmod(j,2)
    out = []
    for k in range(2):
        index = color*n+3+k
        for e,c in p.items():
            if e[index]:
                h = list(e)
                h[index] -= 1
                out.append({tuple(h):c*e[index]*C[3+edge][3+k]})
    return add(*out)

Q=[]
eta=[]
for color in range(3):
    for edge in range(2):
        terms=[]
        for perm in permutations(range(3)):
            if perm[0]!=color:
                continue
            sign=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
            terms.append(scale(sign,mul(variable(perm[1]*n+edge),variable(perm[2]*n+edge+1))))
        Q.append(add(*terms))
        eta.append(variable(color*n+3+edge))
S3=scale(F(1,2),add(*(mul(y,q) for y,q in zip(eta,Q))))
square=scale(F(1,2),mul(S3,S3))
Feff=scale(F(1,8),add(*(scale(C[3+j%2][3+k%2],mul(Q[j],Q[k]))
         for j in range(6) for k in range(6) if j//2==k//2)))

def H(p):
    return F(1,8)*sum((expect(mul(mul(Q[j],Q[k]),derivative(derivative(p,k),j)))
                     for j in range(6) for k in range(6)),F(0))

def quad(entries):
    return add(*(scale(F(v),mul(variable(c*n+i),variable(c*n+j)))
                 for c in range(3) for i,j,v in entries))

def kappa3(f,r,t):
    ef,er,et=expect(f),expect(r),expect(t)
    return (expect(mul(mul(f,r),t))-ef*expect(mul(r,t))-er*expect(mul(f,t))
            -expect(mul(f,r))*et+2*ef*er*et)

r=quad([(0,0,1),(1,4,3),(3,3,-2),(3,4,1),(2,2,-1)])
probes=[quad([(0,0,1),(1,1,-1),(2,2,2)]),
        quad([(0,3,2),(1,4,-1),(3,3,1),(4,4,2),(0,1,1)])]
checks=[]
for case,f in enumerate(probes):
    fr=mul(f,r)
    for label,h in [('1',{zero:F(1)}),('f',f),('r',r),('fr',fr)]:
        actual=expect(mul(h,square))
        required=expect(mul(h,Feff))+H(h)
        checks.append({'kind':'conditional_second_ibp','case':case,'polynomial':label,
                       'actual':str(actual),'required':str(required),'pass':actual==required})
    left=kappa3(f,r,square)
    correction=H(fr)-expect(f)*H(r)-expect(r)*H(f)
    right=kappa3(f,r,Feff)+correction
    checks.append({'kind':'complete_cumulant','case':case,'actual':str(left),'required':str(right),
                   'effective_quartic':str(kappa3(f,r,Feff)),
                   'observable_correction':str(correction),'pass':left==right})
failures=[x for x in checks if not x['pass']]
out=Path(__file__).with_name('upper-cubic-conditioning-certificate.json')
out.write_text(json.dumps({'scope':'Two adjacent-edge SU(2) Gaussian surrogate; correlated noise; not original box',
                          'one_color_covariance':[[str(v) for v in row] for row in C],
                          'checks':checks,'failures':failures,
                          'bounds':{'actual':'Exact finite conditional/cumulant identities; analytic lattice noise norm <=1 in L049',
                                    'required':'a^2-scaled complete response compensation, logarithm, reflected error <=c_box/2'}},indent=2)+'\n')
print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact checks; failures={len(failures)}")
print('Actual: finite algebra only; required: complete scaled response/log and reflected error <=c_box/2.')
print(f'Certificate: {out.relative_to(Path.cwd())}')
for x in checks:
    if x['kind']=='complete_cumulant':
        print(f"case {x['case']}: complete={x['actual']}; effective={x['effective_quartic']}; correction={x['observable_correction']}")
assert not failures

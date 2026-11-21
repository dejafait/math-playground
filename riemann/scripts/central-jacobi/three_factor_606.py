"""One compactified, all-tuples three-factor obstruction test.

Integer fixed-point intervals, outward after EVERY operation. No floating
point values enter the proof. The JSON contains every leaf of the exhaustive
binary subdivision, its interval evidence, and any unresolved leaves.
Run from the active riemann notebook; no existing artifact is overwritten.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / 'scripts/central-jacobi/three-factor-certificate-606.json'
GRID = 10**60


class I:
    def __init__(self, lo, hi=None, raw=False):
        if raw:
            self.lo, self.hi = lo, hi
        else:
            a, b = Fraction(lo), Fraction(lo if hi is None else hi)
            self.lo = a.numerator * GRID // a.denominator
            self.hi = -((-b.numerator * GRID) // b.denominator)
        assert self.lo <= self.hi

    def __add__(self, other):
        b = other if isinstance(other, I) else I(other)
        return I(self.lo+b.lo, self.hi+b.hi, raw=True)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo, raw=True)

    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        b = other if isinstance(other, I) else I(other)
        values = [self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi]
        return I(min(values)//GRID, -((-max(values))//GRID), raw=True)

    __rmul__ = __mul__

    def __pow__(self, n):
        out = I(1)
        for _ in range(n):
            out = out*self
        return out

    def excludes_zero(self):
        return self.lo > 0 or self.hi < 0

    def record(self):
        return [str(Fraction(self.lo, GRID)), str(Fraction(self.hi, GRID))]


def padd(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, I(0)) + c
    return out


def pscale(a, c):
    return {m: v*c for m, v in a.items()}


def pmul(a, b):
    out = {}
    for (i,j), c in a.items():
        for (k,l), d in b.items():
            m = i+k, j+l
            out[m] = out.get(m, I(0)) + c*d
    return out


def ppow(a, n):
    out = {(0,0): I(1)}
    for _ in range(n):
        out = pmul(out, a)
    return out


def deriv(a, axis):
    out = {}
    for m,c in a.items():
        if m[axis]:
            n = list(m)
            n[axis] -= 1
            out[tuple(n)] = c*m[axis]
    return out


def evaluate(a, x, y):
    # Bivariate Horner; every interval operation rounds outward.
    mx = max(m[0] for m in a)
    my = max(m[1] for m in a)
    out = I(0)
    for i in range(mx, -1, -1):
        row = I(0)
        for j in range(my, -1, -1):
            row = row*y + a.get((i,j), I(0))
        out = out*x + row
    return out


def centered(poly, dx, dy, x, y):
    mx = (x.lo+x.hi)//2
    my = (y.lo+y.hi)//2
    cx, cy = I(mx,mx,raw=True), I(my,my,raw=True)
    return (evaluate(poly,cx,cy) + evaluate(dx,x,y)*(x-cx)
            + evaluate(dy,x,y)*(y-cy))


q_strings = [
    ['1.07484394250019421126346157158','1.07484394250019421126346157162'],
    ['1.06274366627144916855311401273','1.06274366627144916855311401285'],
    ['1.05430333113463476927545484495','1.05430333113463476927545484516']]
Q,R,Z = [I(*v) for v in q_strings]
eps = Fraction(1,10**6)
T = I(0,eps)
V = 1-T
one = {(0,0): I(1)}
X = {(1,0): I(1)}
Y = {(0,1): I(1)}
U = padd(one, X)
W1 = padd(one, Y)
U2 = padd(one, pscale(X,2))
W2 = padd(one, pscale(Y,2))
U3 = padd(one, pscale(X,3))
W3 = padd(one, pscale(Y,3))
D = pmul(padd(one, pscale(ppow(X,2),-1)),
         padd(one, pscale(ppow(Y,2),-1)))
W = pscale(D,Q)
twoWminusV = padd(pscale(W,2),{(0,0):-V})
threeWminus2V = padd(pscale(W,3),{(0,0):-2*V})
F1 = padd(pmul(pmul(ppow(U,2),ppow(W1,2)),twoWminusV),
          pscale(pmul(pmul(U2,W2),W),-R*(1+T)))
F2 = padd(pscale(pmul(pmul(ppow(U2,2),ppow(W2,2)),threeWminus2V),1+T),
          pscale(pmul(pmul(pmul(U,U3),pmul(W1,W3)),twoWminusV),-Z*(1+2*T)))
polys = [F1,F2]
derivatives = [(deriv(f,0),deriv(f,1)) for f in polys]

# q0 >= (1-t)/(1-x^2) and similarly for y imply x,y<27/100.
# Verify the sufficient exact rational comparison without any division.
domain_check = ((Fraction(q_strings[0][1])*(1-Fraction(27,100)**2))
                < 1-eps)
assert domain_check
root = I(0,Fraction(27,100))
stack = [('',root,root)]
leaves = []
unresolved = []
nodes = 0
max_depth = 0
node_cap = 200000
depth_cap = 48
while stack:
    path,x,y = stack.pop()
    nodes += 1
    max_depth = max(max_depth,len(path))
    reason = None
    evidence = None
    if x.lo > y.hi:
        reason = 'symmetry_x_gt_y'
    else:
        b_numerator = evaluate(W,x,y)-V
        if b_numerator.hi < 0:
            reason,evidence = 'b_negative',b_numerator
        else:
            for index, (f,(dx,dy)) in enumerate(zip(polys,derivatives)):
                bound = centered(f,dx,dy,x,y)
                if bound.excludes_zero():
                    reason,evidence = 'F'+str(index+1),bound
                    break
    if reason:
        leaves.append({'path':path,'reason':reason,
                       'bound':None if evidence is None else evidence.record()})
        continue
    if len(path)>=depth_cap or nodes>=node_cap:
        unresolved.append({'path':path,'x':x.record(),'y':y.record()})
        if nodes>=node_cap:
            unresolved += [{'path':p,'x':a.record(),'y':b.record()} for p,a,b in stack]
            stack=[]
        continue
    axis = 0 if x.hi-x.lo>=y.hi-y.lo else 1
    a = x if axis==0 else y
    mid = (a.lo+a.hi)//2
    low,high = I(a.lo,mid,raw=True),I(mid,a.hi,raw=True)
    if axis==0:
        stack.append((path+'1',high,y));stack.append((path+'0',low,y))
    else:
        stack.append((path+'1',x,high));stack.append((path+'0',x,low))

# Exact Kraft sum plus prefix-free paths verifies exhaustive dyadic coverage.
paths = sorted([v['path'] for v in leaves+unresolved])
prefix_free = all(not b.startswith(a) for a,b in zip(paths,paths[1:]))
weight = sum((Fraction(1,2**len(p)) for p in paths),Fraction(0))
passed = domain_check and prefix_free and weight==1 and not unresolved
counts = {k:sum(v['reason']==k for v in leaves)
          for k in ['symmetry_x_gt_y','b_negative','F1','F2']}
result = {
    'pass':passed, 'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'input_path':'lemmas/L791-fixed-central-five-root-jacobi-model.md',
    'input_sha256':hashlib.sha256((BASE/'lemmas/L791-fixed-central-five-root-jacobi-model.md').read_bytes()).hexdigest(),
    'arithmetic':'integer fixed-point outward intervals', 'grid':str(GRID),
    'q':q_strings, 't':[str(0),str(eps)],'root_domain':[root.record(),root.record()],
    'domain_check':domain_check,'prefix_free':prefix_free,'kraft_sum':str(weight),
    'nodes':nodes,'max_depth':max_depth,'leaf_counts':counts,
    'required_unresolved':0,'actual_unresolved':len(unresolved),
    'polynomial_coefficients':[{str(m):c.record() for m,c in f.items()} for f in polys],
    'leaves':leaves,'unresolved':unresolved,
    'failures':[] if passed else ['exhaustive exclusion not established'],
    'qualification':'conditional on L791 inputs; new obstruction is not independently audited; no RH sign conclusion'}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print('PASS' if passed else 'INCONCLUSIVE', 'nodes',nodes,'max_depth',max_depth,
      'leaf_counts',counts,'unresolved',len(unresolved),'required',0)
print('tested 0<=t<=',eps,'required for degree cap: exhaustive exclusion')
print('certificate:',OUT.relative_to(BASE))

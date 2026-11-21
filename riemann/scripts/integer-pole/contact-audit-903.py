#!/usr/bin/env python3
"""C466e audit: independent rational arithmetic/evaluator on ALL saved cells.

Preserves 901. No floating point enters an acceptance decision. The analytic
same-law/endpoint/error audit is recorded in C466e, audit903. Full output
includes new enclosures, saved-cell replay and exact comparison evidence.
"""
import hashlib
import importlib.util
import json
import sys
from collections import defaultdict
from fractions import Fraction as R
from functools import cache
from itertools import permutations
from math import comb, factorial
from pathlib import Path

# The exact 128-factor complex residue has more than 4300 decimal digits.
# This only permits serializing the certificate, not approximate arithmetic.
sys.set_int_max_str_digits(50000)

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'contact-certificate-901.json'
OUT = Path(__file__).with_suffix('.json')
S = 2**512
failures = []


def check(ok, reason):
    if not ok:
        failures.append(reason)


def floor(q):
    return q.numerator // q.denominator


def ceil(q):
    return -floor(-q)


class Box:
    """Exact Fraction endpoint operations, then outward dyadic projection."""
    def __init__(self, lo, hi=None, raw=False):
        if raw:
            self.lo, self.hi = int(lo), int(hi)
        else:
            lo = R(lo)
            hi = lo if hi is None else R(hi)
            self.lo, self.hi = floor(lo*S), ceil(hi*S)
        assert self.lo <= self.hi

    @staticmethod
    def box(lo, hi):
        return Box(lo, hi)

    @property
    def endpoints(self):
        return (R(self.lo, S), R(self.hi, S))

    def __add__(self, other):
        other = lift(other)
        a, b = self.endpoints
        c, d = other.endpoints
        return Box(a+c, b+d)
    __radd__ = __add__

    def __neg__(self):
        a, b = self.endpoints
        return Box(-b, -a)

    def __sub__(self, other):
        return self + (-lift(other))

    def __rsub__(self, other):
        return lift(other) + (-self)

    def __mul__(self, other):
        other = lift(other)
        values = [a*b for a in self.endpoints for b in other.endpoints]
        return Box(min(values), max(values))
    __rmul__ = __mul__

    def scale(self, q):
        values = [R(q)*a for a in self.endpoints]
        return Box(min(values), max(values))

    def data(self):
        return [str(self.lo), str(self.hi)]


def lift(x):
    return x if isinstance(x, Box) else Box(x)


def cmul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def cdiv(a, b):
    norm = b[0]**2 + b[1]**2
    v = cmul(a, (b[0], -b[1]))
    return (v[0]/norm, v[1]/norm)


def residues(n):
    """Direct pole products, without 901's triangular product shortcut."""
    rates = [1] + [2**k for k in range(1, n+1)]
    real = []
    for i, r in enumerate(rates):
        a = R(10, (3-r)**2+1)
        # Each real factor is r_k/(s+r_k), including r_0=1.
        a *= r
        for j, t in enumerate(rates):
            if j != i:
                a *= R(t, t-r)
        real.append((r, a))
    # Residue of 10/((s+1)((s+3)^2+1)) at s=-3-i.
    z = cdiv((R(10), R(0)), cmul((R(-2), R(-1)), (R(0), R(-2))))
    for r in rates[1:]:
        z = cdiv(z, (1-R(3,r), -R(1,r)))
    return real, z


@cache
def expneg(t):
    """Exact alternating polynomial, then outward interval squaring."""
    t = R(t)
    assert t >= 0
    if t >= 512:
        return Box(0, R(1,S))
    shifts = 0
    while t > 1:
        t /= 2
        shifts += 1
    term = total = R(1)
    for k in range(1,101):
        term *= -t/k
        total += term
    err = t**101/factorial(101)
    v = Box(max(R(0), total-err), total)
    for _ in range(shifts):
        v = v*v
    return v


@cache
def trig(x):
    """Exact rational Taylor sums, not 901's termwise dyadic rounding."""
    x = R(x)
    si = sum(((-1)**k*x**(2*k+1)/factorial(2*k+1) for k in range(50)), R(0))
    co = sum(((-1)**k*x**(2*k)/factorial(2*k) for k in range(51)), R(0))
    err = abs(x)**101/factorial(101)
    return Box(si-err, si+err), Box(co-err, co+err)


def sign(perm):
    return (-1)**sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))


def determinant_polynomial(n):
    out = defaultdict(int)
    for perm in permutations(range(n)):
        out[tuple(sorted(i+perm[i] for i in range(n)))] += (-1)**(n*(n-1)//2)*sign(perm)
    return {k:v for k,v in out.items() if v}


def polyderiv(poly):
    out = defaultdict(int)
    for key, coeff in poly.items():
        for i in range(len(key)):
            k = list(key)
            k[i] += 1
            out[tuple(sorted(k))] += coeff
    return {k:v for k,v in out.items() if v}


def column_derivatives(n):
    """Differentiate columns; sort with sign and eliminate repeated columns."""
    rows = [{tuple(range(n)):(-1)**(n*(n-1)//2)}]
    for _ in range(3):
        out = defaultdict(int)
        for key, coeff in rows[-1].items():
            for i in range(n):
                k = list(key)
                k[i] += 1
                if len(set(k)) == n:
                    out[tuple(sorted(k))] += coeff*sign(k)
        rows.append({k:v for k,v in out.items() if v})
    return rows


def column_poly(key):
    n = len(key)
    out = defaultdict(int)
    for perm in permutations(range(n)):
        out[tuple(sorted(i+key[perm[i]] for i in range(n)))] += sign(perm)
    return {k:v for k,v in out.items() if v}


CD = {n:column_derivatives(n) for n in (2,3)}
for n in (2,3):
    poly = determinant_polynomial(n)
    for order, terms in enumerate(CD[n]):
        expanded = defaultdict(int)
        for cols, coeff in terms.items():
            for key, c in column_poly(cols).items():
                expanded[key] += coeff*c
        expanded = {k:v for k,v in expanded.items() if v}
        check(poly == expanded, f'D{n} derivative identity order {order}')
        poly = polyderiv(poly)


def detcols(q, cols):
    if len(cols) == 2:
        i,j = cols
        return q[i]*q[j+1]-q[j]*q[i+1]
    i,j,k = cols
    return (q[i]*(q[j+1]*q[k+2]-q[j+2]*q[k+1])
            -q[i+1]*(q[j]*q[k+2]-q[j+2]*q[k])
            +q[i+2]*(q[j]*q[k+1]-q[j+1]*q[k]))


REAL,Z = residues(128)
HEAD,HZ = residues(8)
M = [sum(abs(a)*r**j for r,a in HEAD)+2*(abs(HZ[0])+abs(HZ[1]))*4**j for j in range(1,9)]
ERROR = [R(729,2**128)*sum(comb(j,k)*M[k] for k in range(j+1)) for j in range(8)]
TAIL = [sum((expneg(R(r-1,4)).scale(abs(a)*(r-1)**j) for r,a in REAL[13:]), Box(0)) for j in range(8)]
ZDER = [Z]
for j in range(7):
    ZDER.append(cmul(ZDER[-1], (R(-2),R(-1))))


def jet(a,b):
    c, rad = (a+b)/2, (b-a)/2
    si,co = trig(c)
    si,co = si+Box(-rad,rad), co+Box(-rad,rad)
    osc = Box(expneg(2*b).lo,expneg(2*a).hi,True)
    reals = [(r,v,Box(expneg((r-1)*b).lo,expneg((r-1)*a).hi,True)) for r,v in REAL[:13]]
    values=[]
    for j in range(8):
        v = (co.scale(ZDER[j][0])+si.scale(ZDER[j][1]))*osc*2
        for r,coeff,ex in reals:
            v = v+ex.scale(coeff*(-(r-1))**j)
        bound = ERROR[j]+R(TAIL[j].hi,S)
        values.append(v+Box(-bound,bound))
    return values


def dvalues(q,n):
    return [sum((detcols(q,key).scale(coeff) for key,coeff in row.items()), Box(0)) for row in CD[n]]


def enclose(a,b):
    c, r = (a+b)/2,(b-a)/2
    center,whole = jet(c,c),jet(a,b)
    z,z2,z3 = Box(-r,r),Box(0,r*r),Box(-r**3,r**3)
    def tay(point,wide):
        return point[0]+point[1]*z+(point[2]*z2).scale(R(1,2))+(wide[3]*z3).scale(R(1,6))
    p = tay(center,whole)
    c2,w2,c3,w3 = dvalues(center,2),dvalues(whole,2),dvalues(center,3),dvalues(whole,3)
    dp = c3[1]+c3[2]*z+(w3[3]*z2).scale(R(1,2))
    return [p,tay(c2,w2),tay(c3,w3),dp]


def setup_replay():
    """Also replay the inspected 901 evaluator with the independent backend."""
    spec = importlib.util.spec_from_file_location('generator901',HERE/'contact-certificate-901.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    check(m.REAL == REAL and m.Z == Z, 'all N128 residues')
    check(m.HEAD == HEAD and m.HZ == HZ, 'all N8 residues')
    check(m.M == M, 'all eight derivative majorants')
    check(m.determinants([Box(j+1) for j in range(8)])[0][0].data() == dvalues([Box(j+1) for j in range(8)],2)[0].data(), 'determinant conventions')
    m.I = Box
    m.expminus.cache_clear()
    m.trigpoint.cache_clear()
    m.ERROR = [Box(e) for e in ERROR]
    m.TAIL = [sum((m.expminus(R(r-1,4)).scale(abs(a)*(r-1)**j) for r,a in REAL[13:]),Box(0)) for j in range(8)]
    m.COEFF = [tuple(Box(v) for v in z) for z in ZDER]
    m.RCOEFF = [(r,[Box(a*(-(r-1))**j) for j in range(8)]) for r,a in REAL[:13]]
    return m


def finite_head_algebra():
    """Exact complex exponential-polynomial expansion of D2, D3 and f at 0."""
    rates = [(R(1),R(0)),(R(3),R(1)),(R(3),R(-1))]
    coeff = [(R(2),R(0)),(R(-1),R(-2)),(R(-1),R(2))]
    def cpow(z,k):
        a=(R(1),R(0))
        for _ in range(k): a=cmul(a,z)
        return a
    def add(z,w): return (z[0]+w[0],z[1]+w[1])
    jets0=[]
    for j in range(3):
        jets0.append(tuple(sum(v[k] for v in [cmul(c,cpow((-r[0],-r[1]),j)) for r,c in zip(rates,coeff)]) for k in range(2)))
    check(jets0 == [(R(0),R(0)),(R(0),R(0)),(R(10),R(0))], 'finite head zero values 0,0,10')
    out2={}
    for i in range(3):
        for j in range(i+1,3):
            diff=(rates[i][0]-rates[j][0],rates[i][1]-rates[j][1])
            v=cmul(cmul(coeff[i],coeff[j]),cpow(diff,2))
            out2[add(rates[i],rates[j])]=(-v[0],-v[1])
    expected={(R(4),R(1)):(R(-10),R(20)),(R(4),R(-1)):(R(-10),R(-20)),(R(6),R(0)):(R(20),R(0))}
    check(out2 == expected,'finite head D2 identity')
    prod=(R(1),R(0))
    for c in coeff: prod=cmul(prod,c)
    for i in range(3):
        for j in range(i+1,3):
            prod=cmul(prod,cpow((rates[i][0]-rates[j][0],rates[i][1]-rates[j][1]),2))
    check(prod == (R(-1000),R(0)), 'finite head D3 identity')
    return dict(jets0=[[str(v) for v in z] for z in jets0],D2={str(k):str(v) for k,v in out2.items()},D3_coefficient=str(-prod[0]))


def main():
    data=json.loads(SOURCE.read_text())
    check((data['bits'],data['N'],data['K']) == (512,128,12),'saved parameters')
    check(len(data['cells'])==189 and len(data['endpoints'])==2,'saved row counts')
    check(len(data['true_law_error'])==8 and len(data['omitted_finite_modes'])==8,'saved error counts')
    head=finite_head_algebra()
    replay=setup_replay()
    check([str(v) for v in M]==data['head_derivative_bounds'],'saved M values')
    check([v.data() for v in replay.ERROR]==data['true_law_error'],'saved true-law error intervals')
    check([v.data() for v in replay.TAIL]==data['omitted_finite_modes'],'saved finite-mode tails')
    check(max(ERROR)<R(1,10**20),'true-law error threshold')
    check(max(R(v.hi,S) for v in TAIL)<R(1,10**100),'omitted-mode threshold')
    cells=[]
    keys=['Q','D2_Q','D3_Q','D3_Q_prime']
    counts={}
    domains=[('prefix',R(1,4),R(177,32)),('contact',R(177,32),R(89,16)),('lower',R(89,16),R(179,32))]
    for mode,left,right in domains:
        cursor=left
        rows=[v for v in data['cells'] if v['mode']==mode]
        counts[mode]=len(rows)
        for row in rows:
            a,b=R(row['left']),R(row['right'])
            label=f'{mode} [{a},{b}]'
            check(a==cursor and a<b<=right,label+' coverage')
            cursor=b
            old=replay.enclose(a,b)
            check(all(v.data()==row[k] for k,v in zip(keys,old)),label+' exact arithmetic replay')
            new=enclose(a,b)
            check(new[0].lo>0,label+' independent Q')
            check(R(new[1].lo,S)>R(1,50000),label+' independent D2')
            if mode=='prefix': check(R(new[2].lo,S)>R(1,50000),label+' independent D3')
            if mode=='contact': check(R(new[3].hi,S)<-R(1,200),label+' independent D3prime')
            cells.append(dict(left=str(a),right=str(b),mode=mode,
                              replay=[v.data() for v in old],independent=[v.data() for v in new]))
        check(cursor==right,mode+' complete coverage')
        print('Checked',mode,len(rows),'cells; failures',len(failures),flush=True)
    check(sum(counts.values())==len(data['cells']),'no hidden cell modes')
    endpoints=[]
    for row,x,sgn in zip(data['endpoints'],[R(177,32),R(89,16)],[1,-1]):
        check(R(row['x'])==x,'endpoint location')
        old=replay.enclose(x,x)
        check(all(v.data()==row[k] for k,v in zip(keys,old)),'endpoint exact replay '+str(x))
        new=enclose(x,x)
        check(new[2].lo>0 if sgn==1 else new[2].hi<0,'independent endpoint '+str(x))
        endpoints.append(dict(x=str(x),replay=[v.data() for v in old],independent=[v.data() for v in new]))
    def lower(index,mode=None):
        return min(R(int(c['independent'][index][0]),S) for c in cells if mode is None or c['mode']==mode)
    dp=max(R(int(c['independent'][3][1]),S) for c in cells if c['mode']=='contact')
    extrema=dict(Q_lower=str(lower(0)),D2_lower=str(lower(1)),prefix_D3_lower=str(lower(2,'prefix')),contact_D3prime_upper=str(dp))
    displays={k:dict(lower=str(floor(R(v)*10**16))+'/10^16',upper=str(ceil(R(v)*10**16))+'/10^16') for k,v in extrema.items()}
    summary=dict(status='PASS' if not failures else 'FAIL',cells=len(cells),counts=counts,endpoints=len(endpoints),
                 exact_replay=not any('replay' in f for f in failures),failure_count=len(failures),
                 required=dict(Q='>0',D2='>1/50000',prefix_D3='>1/50000',contact_D3prime='<-1/200',true_error='<1e-20',finite_tail='<1e-100'),
                 independent_extrema_decimal_brackets=displays)
    summary.update(status='PASS' if not failures else 'FAIL',failure_count=len(failures))
    report=dict(summary=summary,source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                source='scripts/integer-pole/contact-certificate-901.json',bits=512,N=128,K=12,
                finite_head=head,column_derivative_identities={str(n):[{str(k):v for k,v in r.items()} for r in rows] for n,rows in CD.items()},
                residues=[dict(rate=r,coefficient=str(a)) for r,a in REAL],complex_residue=[str(v) for v in Z],
                M=[str(v) for v in M],true_law_error=[str(v) for v in ERROR],finite_tail=[v.data() for v in TAIL],
                extrema=extrema,cells=cells,endpoints=endpoints,failures=failures,
                qualification='Independent rational backend and evaluator; analytic justification audited separately in C466e. No actual-Xi inference.')
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(summary['status'],'all',len(cells),'cells and',len(endpoints),'endpoints; failures',failures)
    print('Actual extrema (outward decimal brackets):',displays)
    print('Required:',summary['required'])
    print('Full audit:',OUT)


if __name__=='__main__':
    main()

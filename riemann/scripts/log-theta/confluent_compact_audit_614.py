#!/usr/bin/env python3
"""Independent exact-integer interval audit of the full L821 certificate.

No Decimal arithmetic in the independent verifier. See L821's audit section
for the fixed lattice, Taylor remainder and polynomial identity checks.
"""
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'confluent_compact_612.json'
OUT = HERE / 'confluent_compact_audit_614.json'
REPLAY = HERE / 'confluent_compact_replay_614.json'
BITS = 1024
S = 1 << BITS
TERMS = 240


def ceildiv(a, b):
    assert b > 0
    return -((-a) // b)


class Box:
    """Endpoints are integer multiples of 2**(-BITS)."""
    def __init__(self, lo, hi):
        assert isinstance(lo, int) and isinstance(hi, int) and lo <= hi
        self.lo, self.hi = lo, hi

    @classmethod
    def of(cls, value):
        if isinstance(value, cls):
            return value
        x = F(value)
        return cls((x.numerator*S)//x.denominator,
                   ceildiv(x.numerator*S, x.denominator))

    def __neg__(self):
        return Box(-self.hi, -self.lo)

    def __add__(self, other):
        b = Box.of(other)
        return Box(self.lo+b.lo, self.hi+b.hi)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-Box.of(other))

    def __rsub__(self, other):
        return Box.of(other) + (-self)

    def __mul__(self, other):
        b = Box.of(other)
        products = [x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return Box(min(products)//S, ceildiv(max(products), S))

    __rmul__ = __mul__

    def reciprocal(self):
        assert self.lo > 0 or self.hi < 0
        if self.hi < 0:
            return -(-self).reciprocal()
        return Box((S*S)//self.hi, ceildiv(S*S, self.lo))

    def __truediv__(self, other):
        # Exact integer division when available avoids needless widening.
        if isinstance(other, int) and other > 0:
            return Box(self.lo//other, ceildiv(self.hi, other))
        return self * Box.of(other).reciprocal()

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out, base = Box.of(1), self
        while n:
            if n & 1:
                out = out * base
            n //= 2
            if n:
                base = base * base
        return out

    def data(self):
        # Common denominator is stored once, never rounded for evidence.
        return [str(self.lo), str(self.hi)]


def exp_point(k):
    """Enclose exp(k/S) by a Taylor polynomial at |k|/(S*2**r)<=1."""
    if k == 0:
        return Box.of(1)
    r = max(0, (abs(k)-1).bit_length()-BITS)
    z = Box.of(F(abs(k), S*(1 << r)))
    assert 0 <= z.lo <= z.hi <= S
    term = total = Box.of(1)
    for j in range(1, TERMS+1):
        term = term*z/j
        total = total+term
    # For 0<=z<=1, remaining terms total <=2/(TERMS+1)!.
    remainder = ceildiv(2*S, math.factorial(TERMS+1))
    value = Box(total.lo, total.hi+remainder)
    if k < 0:
        value = value.reciprocal()
    for _ in range(r):
        value = value*value
    return value


def exp_box(x):
    return Box(exp_point(x.lo).lo, exp_point(x.hi).hi)


def atan(q, count):
    # Rational alternating-series evaluation; independent of Decimal.
    terms = [F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(count+1)]
    total = sum(terms[:-1], F(0))
    return min(total,total+terms[-1]), max(total,total+terms[-1])


def pi_box():
    a,b = atan(5,120)
    c,d = atan(239,40)
    return Box(Box.of(16*a-4*d).lo, Box.of(16*b-4*c).hi)


# Independent formal Taylor construction of R_j, not recurrence (3).
# A polynomial maps (u,a,c) powers to rational coefficients; a Taylor
# series is a length-five list of these polynomials, truncated mod t^5.
ZERO = (0,0,0)


def padd(p,q):
    out = dict(p)
    for key,value in q.items():
        out[key] = out.get(key,F(0))+value
        if not out[key]:
            del out[key]
    return out


def scale(p,k):
    return {x:v*k for x,v in p.items() if v*k}


def pmul(p,q):
    out = {}
    for a,x in p.items():
        for b,y in q.items():
            key = tuple(i+j for i,j in zip(a,b))
            out[key] = out.get(key,F(0))+x*y
    return {key:value for key,value in out.items() if value}


def smul(p,q):
    out = [{} for _ in range(5)]
    for i in range(5):
        for j in range(5-i):
            out[i+j] = padd(out[i+j],pmul(p[i],q[j]))
    return out


def sexp(p):
    assert not p[0]
    power = [{ZERO:F(1)},{},{},{},{}]
    out = [dict(x) for x in power]
    for j in range(1,5):
        power = smul(power,p)
        out = [padd(x,scale(y,F(1,math.factorial(j)))) for x,y in zip(out,power)]
    return out


def independent_polys():
    # Z(t)=exp(2u(exp(t)-1)); a(v+t)=a*Z(t), c(v+t)=c*Z(t).
    f = [{}]+[{(1,0,0):F(2,math.factorial(j))} for j in range(1,5)]
    z = sexp(f)
    az = [pmul({(0,1,0):F(1)},p) for p in z]
    prefactor = [padd(scale(p,8),scale(q,-12)) for p,q in zip(smul(az,az),az)]
    zm1 = [padd(z[0],{ZERO:F(-1)})]+z[1:]
    exponent = [pmul({(0,1,0):F(-1),(0,0,1):F(1)},p) for p in zm1]
    result = smul(prefactor,sexp(exponent))
    result = [scale(p,math.factorial(j)) for j,p in enumerate(result)]
    assert all(v.denominator == 1 for p in result for v in p.values())
    return [{k:int(v) for k,v in p.items()} for p in result]


def contained(box, saved):
    return F(saved[0]) <= F(box.lo,S) <= F(box.hi,S) <= F(saved[1])


def evaluate(left,right,pi,polys,tails):
    u = Box(Box.of(left).lo,Box.of(right).hi)
    c = pi*exp_box(2*u)
    jets = [Box.of(0) for _ in range(5)]
    for n in range(1,9):
        w = Box.of(1) if n == 1 else exp_box(-(n*n-1)*c)
        for j,p in enumerate(polys):
            if j == 0:
                value = 4*n*n*c*(2*n*n*c-3)
            else:
                specialized = {}
                for (i,h,k),b in p.items():
                    key = (i,h+k)
                    specialized[key] = specialized.get(key,0)+b*n**(2*h)
                value = sum((b*u**i*c**h for (i,h),b in sorted(specialized.items()) if b),Box.of(0))
            jets[j] = jets[j]+w*value
    finite = list(jets)
    jets = [x+Box(-t.hi,t.hi) for x,t in zip(jets,tails)]
    assert jets[0].lo > 0
    r = [x/jets[0] for x in jets]
    b2 = r[2]-r[1]**2
    b3 = r[3]-3*r[1]*r[2]+2*r[1]**3
    b4 = r[4]-4*r[1]*r[3]-3*r[2]**2+12*r[1]**2*r[2]-6*r[1]**4
    ell = [u/2-c*(2*u+4*u**2)+b2,
           u/2-c*(2*u+12*u**2+8*u**3)+b3,
           u/2-c*(2*u+28*u**2+48*u**3+16*u**4)+b4]
    q = ell[1]**2-ell[0]*ell[2]-2*ell[0]**3
    return {'c':c,'B_finite_jets':finite,'B_full_jets':jets,
            'logH_derivatives_2_3_4':ell,'Q3':q}


def main():
    original_bytes = SOURCE.read_bytes()
    cert = json.loads(original_bytes)
    report = {'source_sha256':hashlib.sha256(original_bytes).hexdigest(),
              'arithmetic':'exact integer endpoints / 2**1024; Taylor exp, no Decimal',
              'denominator':str(S),'Taylor_degree':TERMS,'runtime':sys.version,
              'failures':[],'rows':[],'checked_scalar_intervals':0}
    def require(ok, message):
        if not ok:
            report['failures'].append(message)

    try:
        pi = pi_box()
        require(contained(pi,cert['pi']),'pi containment')
        polys = independent_polys()
        saved_polys = [{tuple(t['powers']):int(t['coefficient']) for t in p}
                       for p in cert['derivative_polynomials']]
        require(polys == saved_polys,'formal Taylor polynomials differ')
        report['independent_derivative_polynomials'] = [
            [{'powers':list(k),'coefficient':str(v)} for k,v in sorted(p.items())]
            for p in polys]
        norms = [sum(abs(b)*2**i for (i,h,k),b in p.items()) for p in polys]
        majorants = [20,320,6720,174720,5416320]
        require(norms == cert['tail_coefficient_bounds'],'coefficient norms differ')
        require(majorants == cert['tail_analytic_coefficient_majorants'],'majorants differ')
        for j,p in enumerate(polys):
            require(all(i <= j and h+k <= j+2 for i,h,k in p),'polynomial degrees '+str(j))
            require(norms[j] <= majorants[j],'coefficient majorant '+str(j))
        global_c = pi*exp_box(Box.of(F(1,2)))
        c_top = pi*exp_box(Box.of(4))
        require(global_c.lo > 5*S and c_top.hi < 200*S,'global c thresholds')
        require(contained(Box(global_c.lo,c_top.hi),cert['global_c']),'global c containment')
        ratio = 2**12*exp_box(Box.of(-95))
        require(ratio.hi*2 < S,'geometric ratio threshold')
        require(contained(ratio,cert['tail_ratio_bound']),'ratio containment')
        tails = [2*b*200**6*9**12*exp_box(Box.of(-400)) for b in majorants]
        for j,t in enumerate(tails):
            require(contained(t,cert['tail_bounds'][j]),'tail enclosure '+str(j))
        report['constants'] = {'pi':pi.data(),'global_c':[str(global_c.lo),str(c_top.hi)],
                               'tail_ratio':ratio.data(),'tails':[t.data() for t in tails],
                               'coefficient_norms':norms,'coefficient_majorants':majorants}
        cells = cert['terminal_cells']
        require(len(cells) == 105 and len(cells) <= cert['cap'] == 2048,'cell count/cap')
        require(not cert['unresolved'] and cert['negative_point'] is None,'unresolved or negative')
        require(cert['N'] == 8 and cert['precision'] == 90,'source parameters')
        bounds = [(F(r['u'][0]),F(r['u'][1])) for r in cells]
        require(bounds[0][0] == F(1,4) and bounds[-1][1] == 2,'cover endpoints')
        require(all(a < b for a,b in bounds),'cell width')
        require(all(a[1] == b[0] for a,b in zip(bounds,bounds[1:])),'cover gaps/overlaps')
        report['exact_cover_checked'] = [list(map(str,b)) for b in bounds]
        point_rows = cert['point_tests']
        require([r['u'] for r in point_rows] == [[str(x),str(x)] for x in
                [F(1,4),F(1,2),F(1),F(3,2),F(2)]],'point-test inputs')
        minima = []
        for index,row in enumerate(cells+point_rows):
            values = evaluate(F(row['u'][0]),F(row['u'][1]),pi,polys,tails)
            stored = {'u':row['u'],'source_row':index,'intervals':{}}
            for field,value in values.items():
                boxes = value if isinstance(value,list) else [value]
                saved = row[field] if isinstance(value,list) else [row[field]]
                require(len(boxes) == len(saved),f'row {index} {field} length')
                for j,(box,interval) in enumerate(zip(boxes,saved)):
                    require(contained(box,interval),f'row {index} {field}[{j}] containment')
                    report['checked_scalar_intervals'] += 1
                stored['intervals'][field] = [b.data() for b in boxes] if isinstance(value,list) else value.data()
            require(values['Q3'].lo*5 > S,f'row {index} Q3 <=1/5')
            report['rows'].append(stored)
            if index < len(cells):
                minima.append(values['Q3'].lo)
        old_min = min(F(row['Q3'][0]) for row in cells)
        weak = min(cells,key=lambda r:F(r['Q3'][0]))
        require(old_min == F(cert['uniform_Q3_lower']),'saved minimum')
        require(weak == cert['weakest_cell'],'weakest cell duplicate')
        require(old_min > F('0.2180791770595388') > F(1,5),'strict reported threshold')
        report['minimum_Q3_numerator'] = str(min(minima))
        report['saved_uniform_Q3_lower'] = cert['uniform_Q3_lower']
        report['required_Q3_lower'] = '1/5'
        report['all_original_interval_enclosures_contain_independent_intervals'] = not report['failures']

        # Original implementation replay, with a different output path.
        spec = importlib.util.spec_from_file_location('original_612',HERE/'confluent_compact_612.py')
        original = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(original)
        original.OUT = REPLAY
        original.main()
        replay = json.loads(REPLAY.read_text())
        differences = [k for k in set(cert)|set(replay) if cert.get(k) != replay.get(k)]
        report['replay_different_top_level_fields'] = sorted(differences)
        require(not [k for k in differences if k != 'runtime'],'replay mathematical evidence differs')
        require(SOURCE.read_bytes() == original_bytes,'original certificate modified')
        report['original_preserved'] = SOURCE.read_bytes() == original_bytes
    except Exception as exc:
        report['failures'].append(type(exc).__name__+': '+str(exc))
    report['conclusion'] = 'PASS' if not report['failures'] else 'FAIL'
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print('Independent audit:',report['conclusion'])
    print('Rows:',len(report['rows']),'scalar intervals:',report['checked_scalar_intervals'])
    print('Saved Q3 lower:',report.get('saved_uniform_Q3_lower'),'; required: >1/5')
    print('Failures:',len(report['failures']))
    for failure in report['failures'][:12]:
        print('FAIL:',failure)
    print('Full audit:',OUT)
    print('Replay:',REPLAY)
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

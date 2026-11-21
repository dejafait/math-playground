"""One exact algebraic elimination test; all output certificates stay local."""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib
from dataclasses import dataclass


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += v
    return out


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b): out[i+j] += v*w
    return out


def scale(a, s): return [s*v for v in a]


def evaluate(a, x):
    out = F(0)
    for v in reversed(a): out = out*x+v
    return out


def shift(a, x):
    out = [F(0)]
    for v in reversed(a): out = add(mul(out, [x, F(1)]), [v])
    return out


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        if self.lo > self.hi: raise ValueError('Reversed interval')

    @staticmethod
    def lift(x):
        return x if isinstance(x, Interval) else Interval(F(x), F(x))

    def __add__(self, other):
        other = self.lift(other)
        return Interval(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self): return Interval(-self.hi, -self.lo)

    def __sub__(self, other): return self + -self.lift(other)

    def __rsub__(self, other): return self.lift(other) + -self

    def __mul__(self, other):
        other = self.lift(other)
        products = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return Interval(min(products),max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.lift(other)
        if other.lo <= 0 <= other.hi: raise ZeroDivisionError('Interval contains zero')
        return self * Interval(1/other.hi,1/other.lo)

    def __rtruediv__(self, other): return self.lift(other)/self


def exact_record(x):
    x = Interval.lift(x)
    return [str(x.lo),str(x.hi)]


def coefficients(q):
    Q, R, Z = q
    S = R*Z
    H = 3*R-2*S-1/Q
    J = 3*R-4*S+1/Q
    K = S-3*R+3-1/Q
    p0, p1 = K/H, -J/H
    t0 = ((Q*R-1)*p0-(2*Q-Q*R-1))/(2*Q)
    t1 = ((Q*R-1)*p1+(Q*R+1))/(2*Q)
    s0 = R*p0+R-1-t0
    s1 = R*p1+R-t1
    return dict(H=H, J=J, K=K, p0=p0, p1=p1,
                s0=s0, s1=s1, t0=t0, t1=t1)


def gap_polynomial(v, m):
    p0, p1, s0, s1, t0, t1 = [v[k] for k in
        ('p0','p1','s0','s1','t0','t1')]
    c, den, cr = [F(0),F(1)], [F(-1),p1], [F(0),-p0,F(1)]
    w = [F(1),F(-m)]
    sn = add(scale(den,s0),scale(cr,s1))
    tn = add(scale(den,t0),scale(cr,t1))
    return add(add(mul(mul(c,c),den),scale(mul(mul(c,w),sn),-1)),
               mul(mul(w,w),tn))


if __name__ == '__main__':
    q = [Interval(F(a),F(b)) for a,b in [
        ('1.07484394250019421126346157158','1.07484394250019421126346157162'),
        ('1.06274366627144916855311401273','1.06274366627144916855311401285'),
        ('1.05430333113463476927545484495','1.05430333113463476927545484516')]]
    v = coefficients(q)
    out = {'qualification':'Exact rational interval certificate, conditional on L791 input contracts.',
           'q':list(map(exact_record,q)),
           'affine':{k:exact_record(x) for k,x in v.items()},
           'polynomials':{},'cases':{},'checks':[]}

    def bound(name, value, lower, upper):
        value = Interval.lift(value)
        lower,upper = F(lower),F(upper)
        passed = lower < value.lo <= value.hi < upper
        out['checks'].append({'name':name,'required_open_interval':[str(lower),str(upper)],
            'pass':passed})
        if not passed: print('FAIL:',name,'approximate enclosure',
            (float(value.lo),float(value.hi)),'required',str(lower),str(upper))

    bound('H',v['H'],'0.01695','0.01696')
    bound('p0',v['p0'],'0.10944','0.10945')
    bound('p1',v['p1'],'21.422','21.423')
    bound('p0*p1',v['p0']*v['p1'],'2.34','2.35')
    bound('t0',v['t0'],'0.003799','0.003800')

    # Each row gives exact decimal outward bounds for coefficients in u=c-p0.
    coefficient_bounds = {
        1:[('-0.002811','-0.002810'),('0.0375','0.0376'),('0.723','0.724'),
           ('6.838','6.839'),('23.829','23.830')],
        2:[('-0.000923','-0.000922'),('0.0920','0.0921'),('1.659','1.660'),
           ('15.416','15.417'),('52.487','52.488')],
        3:[('0.001087','0.001088'),('0.1570','0.1571'),('2.814','2.815'),
           ('25.743','25.744'),('85.974','85.975')]}
    polys = {}
    for m in (1,2,3):
        poly = gap_polynomial(v,m)
        shifted = shift(poly,v['p0'])
        polys[m] = poly
        out['polynomials'][str(m)] = {'c_coefficients':list(map(exact_record,poly)),
            'c_minus_p0_coefficients':list(map(exact_record,shifted))}
        for i,(low,high) in enumerate(coefficient_bounds[m]):
            bound('P%d shifted coefficient %d'%(m,i),shifted[i],low,high)
        if any(Interval.lift(x).lo != 0 or Interval.lift(x).hi != 0 for x in shifted[5:]):
            raise AssertionError('Unexpected degree > 4')

    for m,low,high,other_low,other_high in [
        (1,'0.14677442','0.14677444','40.17','40.20'),
        (2,'0.11802777','0.11802778','149.38','149.40')]:
        c = Interval(F(low),F(high))
        left,right = evaluate(polys[m],F(low)),evaluate(polys[m],F(high))
        bound('P%d left endpoint'%m,left,'-0.0000001','0')
        bound('P%d right endpoint'%m,right,'0','0.0000001')
        denominator = v['p1']*c-1
        a = (c-v['p0'])/denominator
        t = v['t0']+v['t1']*a*c
        x = t*(1-m*c)/c
        other_gap = 1/a-1/x
        bound('m=%d c-p0'%m,c-v['p0'],'0.008','0.04')
        bound('m=%d p1*c-1'%m,denominator,'1.5','2.2')
        bound('m=%d 1-m*c'%m,1-m*c,'0.7','0.9')
        bound('m=%d a'%m,a,'0.005','0.02')
        bound('m=%d x'%m,x,'0.03','0.07')
        bound('m=%d other gap'%m,other_gap,other_low,other_high)
        out['cases'][str(m)] = {'c':exact_record(c),'endpoint_values':
            [exact_record(left),exact_record(right)],'a':exact_record(a),
            't':exact_record(t),'x':exact_record(x),'other_gap':exact_record(other_gap)}

    out['failures'] = [c['name'] for c in out['checks'] if not c['pass']]
    out['result'] = 'PASS' if not out['failures'] else 'FAIL'
    out['input_sha256'] = hashlib.sha256(Path('lemmas/L791-fixed-central-five-root-jacobi-model.md').read_bytes()).hexdigest()
    out['program_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    dest = Path(__file__).with_name('discrete-pairing-certificate-602.json')
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(out['result'],len(out['checks']),'checks; failures:',out['failures'])
    print('Required smaller-gap bound: < 3; P3 coefficients all > 0:',
          all(c['pass'] for c in out['checks'] if c['name'].startswith('P3 shifted')))
    print('Certified larger-gap bounds: m=1, (40.17,40.20); m=2, (149.38,149.40).')
    print('Threshold: mixed continuous gap > d-2; certified upper < 150 gives d <= 151.')
    print('Certificate:',dest)
    if out['failures']: raise SystemExit(1)

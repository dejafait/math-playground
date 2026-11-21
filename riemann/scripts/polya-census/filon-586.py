"""One fixed-cap three-node Filon inclusion attempt; justification: L816.

Never imports/runs the old census. No Decimal power calls or cap retries.
Full certificate includes every panel, moment, sum and unresolved cell.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from math import factorial
from pathlib import Path
from fractions import Fraction
import decimal
import hashlib
import json
import platform
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
lo = Context(prec=50, rounding=ROUND_FLOOR)
hi = Context(prec=50, rounding=ROUND_CEILING)
near = Context(prec=50, rounding=ROUND_HALF_EVEN)


class I:
    def __init__(self, a, b=None):
        self.a, self.b = D(a), D(a if b is None else b)
        assert self.a.is_finite() and self.b.is_finite() and self.a <= self.b

    def __add__(self, other):
        o = cv(other)
        return I(lo.add(self.a, o.a), hi.add(self.b, o.b))

    __radd__ = __add__

    def __neg__(self):
        return I(self.b.copy_negate(), self.a.copy_negate())

    def __sub__(self, other):
        return self + -cv(other)

    def __rsub__(self, other):
        return cv(other) + -self

    def __mul__(self, other):
        if isinstance(other, J):
            return NotImplemented
        o = cv(other)
        return I(min(lo.multiply(a, b) for a in (self.a, self.b) for b in (o.a, o.b)),
                 max(hi.multiply(a, b) for a in (self.a, self.b) for b in (o.a, o.b)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = cv(other)
        assert not o.a <= 0 <= o.b, 'zero-containing divisor'
        return self * I(lo.divide(D(1), o.b), hi.divide(D(1), o.a))

    def exp(self):
        return I(near.exp(self.a).next_minus(near), near.exp(self.b).next_plus(near))

    def data(self):
        return [str(self.a), str(self.b)]


def cv(x):
    return x if isinstance(x, I) else I(x)


def power(x, n):
    y = I(1)
    for _ in range(n):
        y = y * x
    return y


def absolute(x):
    return max(x.a.copy_abs(), x.b.copy_abs())


def sym(x):
    return I(x.b.copy_negate(), x.b)


def intersect(a, b):
    return I(max(a.a, b.a), min(a.b, b.b))


ARGUMENTS = []


def trig(t):
    ARGUMENTS.append(t)
    mid = near.divide(near.add(t.a, t.b), D(2))
    r = max(hi.subtract(mid, t.a), hi.subtract(t.b, mid))
    z = I(mid) / 256
    assert absolute(z) <= 1
    z2 = z*z
    c, s, tc, ts = I(1), z, I(1), z
    for k in range(1, 17):
        tc = -tc*z2/((2*k-1)*(2*k))
        ts = -ts*z2/((2*k)*(2*k+1))
        c, s = c+tc, s+ts
    err = I(1)/factorial(34)
    c, s = c+sym(err), s+sym(err)
    for _ in range(8):
        s, c = 2*s*c, c*c-s*s
    radius = I(r.copy_negate(), r)
    return c+radius, s+radius


class J:
    """Enclosures of f^(r)/r!, r=0,...,3 on one full interval."""
    def __init__(self, v):
        self.v = v if isinstance(v, list) else [cv(v), I(0), I(0), I(0)]

    def __add__(self, other):
        o = jv(other)
        return J([a+b for a, b in zip(self.v, o.v)])

    __radd__ = __add__

    def __neg__(self):
        return J([-a for a in self.v])

    def __sub__(self, other):
        return self+-jv(other)

    def __mul__(self, other):
        o = jv(other)
        return J([sum((self.v[k]*o.v[r-k] for k in range(r+1)), I(0))
                  for r in range(4)])

    __rmul__ = __mul__

    def exp(self):
        result = [self.v[0].exp()]
        for r in range(1, 4):
            result.append(sum((k*self.v[k]*result[r-k] for k in range(1, r+1)), I(0))/r)
        return J(result)


def jv(x):
    return x if isinstance(x, J) else J(x)


def kernels(u):
    e2, e45, e25 = (2*u).exp(), (D('4.5')*u).exp(), (D('2.5')*u).exp()
    k = u*0
    for n in range(1, 5):
        k = k+(u*0+8*pi*pi*(n*n*n*n))*e45*(-pi*(n*n)*e2).exp() \
            -(u*0+12*pi*(n*n))*e25*(-pi*(n*n)*e2).exp()
    def cosh(v):
        return D('0.5')*(v.exp()+(-v).exp())
    q = (u*0+8*pi)*(2*pi*cosh(D('4.5')*u)-3*cosh(D('2.5')*u)) \
        *(-2*pi*cosh(2*u)).exp()
    return k, q


def amplitudes(u):
    k, q = kernels(u)
    return [[k, u*k, u*u*k], [q, u*q, u*u*q]]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


start = time.monotonic()
old = json.loads((BASE/'census-579.json').read_text())
repair = json.loads((BASE/'exact-machin-583.json').read_text())
audit = json.loads((BASE/'audit-584.json').read_text())
assert all(repair['checks'].values()) and all(audit['checks'].values())
assert not repair['failures'] and not audit['failures']
assert sha(BASE/'census-579.json') == repair['provenance']['saved_certificate_sha256']
assert old['pi'] == repair['saved_pi']
pi, normal = I(*old['pi']), I(*old['normalization'])
assert normal.a > 0
M = 1024
h = I(3)/2048
ntail = 27*16*pi*pi*I('13.5').exp()*625*(-25*pi).exp()
utail = 16*pi*I('13.5').exp()*(-pi*I(6).exp()).exp()
nodes = [I(3*k)/2048 for k in range(2049)]
assert all(v.a == v.b and Fraction(v.a) == Fraction(3*k, 2048) for k, v in enumerate(nodes))
values = [amplitudes(u) for u in nodes]
panels = []
errors = [[I(0) for _ in range(3)] for _ in range(2)]
for p in range(M):
    a, mid, b = nodes[2*p:2*p+3]
    u = I(a.a, b.b)
    jets = amplitudes(J([u, I(1), I(0), I(0)]))
    coeffs, thirds, remainder = [], [], []
    for family in range(2):
        cf, td, er = [], [], []
        for j in range(3):
            left, center, right = (values[2*p+r][family][j] for r in range(3))
            cf.append([center, (right-left)/(2*h), (right+left-2*center)/(2*h*h)])
            third = 6*jets[family][j].v[3]
            error = I(absolute(third))*power(h, 4)/3
            td.append(third)
            er.append(error)
            errors[family][j] = errors[family][j]+error
        coeffs.append(cf)
        thirds.append(td)
        remainder.append(er)
    panels.append(dict(u=u, mid=mid, coefficients=coeffs, third=thirds, error=remainder))


def moments(x):
    z = x*h
    co, si = trig(z)
    assert 0 < z.a <= z.b < 1 and co.a > 0
    raw = [2*si/x, 2*(si-z*co)/power(x, 2),
           2*((z*z-2)*si+2*z*co)/power(x, 3)]
    # cos is decreasing on [0,1]; co.a <= cos(x*h) for all x in cell.
    # |sin(x*t)| <= x*|t|, and t*sin(x*t)>=0 here.
    h3 = power(h, 3)
    crude = [I((I(co.a)*2*h).a, (2*h).b),
             I(0, (2*I(x.b)*h3/3).b),
             I((I(co.a)*2*h3/3).a, (2*h3/3).b)]
    final = [intersect(a, b) for a, b in zip(raw, crude)]
    return final, dict(z=z.data(), cos=co.data(), sin=si.data(),
                       exact_formula_intervals=[v.data() for v in raw],
                       integral_bounds=[v.data() for v in crude],
                       final=[v.data() for v in final])


rows = []
for cell in range(13, 80):
    x = I(D(cell)/2, D(cell+1)/2)
    (m0, m1, m2), md = moments(x)
    sums = [[I(0) for _ in range(3)] for _ in range(2)]
    panel_integrals = []
    for panel in panels:
        co, si = trig(x*panel['mid'])
        out = []
        for family in range(2):
            vals = []
            for j in range(3):
                a, b, c = panel['coefficients'][family][j]
                even = a*m0+c*m2
                v = -si*even-co*b*m1 if j == 1 else co*even-si*b*m1
                if j == 2:
                    v = -v
                vals.append(v)
                sums[family][j] = sums[family][j]+v
            out.append(vals)
        panel_integrals.append([[v.data() for v in vals] for vals in out])
    full = [[sums[f][j]+sym(errors[f][j])+sym(ntail+utail if f == 0 else utail)
             for j in range(3)] for f in range(2)]
    fs, ss = full
    gs = [normal*v for v in ss]
    w, wp = fs[0]*gs[1]-gs[0]*fs[1], fs[0]*gs[2]-gs[0]*fs[2]
    if (fs[0].a > 0 and gs[0].a > 0) or (fs[0].b < 0 and gs[0].b < 0):
        kind = 'same_sign_event_exclusion'
    elif w.a > 0 or w.b < 0:
        kind = 'W_event_exclusion'
    else:
        kind = 'unresolved'
    previous = old['cells'][cell]
    assert previous['kind'] == 'unresolved' and previous['x'] == x.data()
    rows.append(dict(x=x.data(), kind=kind, unresolved=kind == 'unresolved',
                     F=[v.data() for v in fs], S=[v.data() for v in ss],
                     G=[v.data() for v in gs], W=w.data(), Wp=wp.data(),
                     finite_sums=[[v.data() for v in vs] for vs in sums],
                     moments=md, panel_integrals=panel_integrals,
                     comparison579=dict(kind=previous['kind'],
                                        F=previous['F'], G=previous['G'],
                                        W=previous['W'], Wp=previous['Wp'],
                                        F0_width_ratio=(I(hi.subtract(fs[0].b, fs[0].a))/I(hi.subtract(D(previous['F'][0][1]), D(previous['F'][0][0])))).data())))
    if (cell-12) % 10 == 0:
        print('completed fixed cells', cell-12, 'of 67', flush=True)

coverage = (len(rows) == 67 and rows[0]['x'][0] == '6.5' and rows[-1]['x'][1] == '40'
            and all(rows[k]['x'][1] == rows[k+1]['x'][0] for k in range(66)))
assert coverage
counts = {kind: sum(r['kind'] == kind for r in rows) for kind in sorted({r['kind'] for r in rows})}
exclusions = [dict(index=k, x=r['x'], kind=r['kind'], F=r['F'][0], G=r['G'][0], W=r['W'])
              for k, r in enumerate(rows) if not r['unresolved']]
report = dict(step='586', backend=dict(python=platform.python_version(),
              decimal=decimal.__libmpdec_version__, precision=50,
              rounding='directed basic arithmetic; nearest exp expanded one neighbor',
              execution_qualification='correct execution/backend contracts assumed; independent audit pending'),
              caps=dict(u_panels=M, u_end=3, n_max=4, x_cells=67, x_width='0.5', retries=0),
              pi=pi.data(), normalization=normal.data(),
              provenance={str(p.relative_to(ROOT)): sha(p) for p in
                          [BASE/'census-579.json', BASE/'audit-581.json',
                           BASE/'exact-machin-583.json', BASE/'audit-584.json', Path(__file__).resolve()]},
              input_sha256={str(p.relative_to(ROOT)): sha(p) for pat in
                            ['L016-*', 'L019-*', 'L020-*', 'L021-*', 'L814-*', 'L815-*']
                            for p in (ROOT/'lemmas').glob(pat)},
              trig_argument_range=[str(min(v.a for v in ARGUMENTS)), str(max(v.b for v in ARGUMENTS))],
              interpolation_errors=[[v.data() for v in vs] for vs in errors],
              n_tail=ntail.data(), u_tail=utail.data(),
              arithmetic_error='Enclosed in all node/coefficient/moment/panel/sum intervals; not a separately estimated scalar.',
              nodes=[dict(u=u.data(), values=[[v.data() for v in vs] for vs in val]) for u, val in zip(nodes, values)],
              panels=[dict(u=p['u'].data(), mid=p['mid'].data(),
                           coefficients=[[[v.data() for v in cf] for cf in family] for family in p['coefficients']],
                           third_derivative=[[v.data() for v in vs] for vs in p['third']],
                           integrated_remainder=[[v.data() for v in vs] for vs in p['error']]) for p in panels],
              coverage=coverage, counts=counts, exclusions=exclusions,
              unresolved_cover=[r['x'] for r in rows if r['unresolved']], cells=rows,
              actual_new_exclusions=len(exclusions), required_new_exclusions=1,
              decision='audit before reuse' if exclusions else 'park fixed variant; no cap retry',
              failures=['No event root, parameter or orientation certified.',
                        'Common/multiple/degenerate possibilities in unresolved cells and outside the box persist.',
                        'Signed compensation, infinity and all-degree mixed positivity remain unpaid.',
                        'New code and numerical output require independent audit.'],
              seconds=time.monotonic()-start)
out = BASE/'filon-586.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(dict(counts=counts, coverage=coverage, actual_new_exclusions=len(exclusions),
                      required_new_exclusions=1, decision=report['decision'],
                      interpolation_errors=report['interpolation_errors'],
                      certificate=str(out.relative_to(ROOT)), seconds=report['seconds'])))

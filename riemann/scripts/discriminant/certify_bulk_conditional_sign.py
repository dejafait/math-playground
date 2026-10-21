"""Step 194: branchwise validated angular trapezoids; exact integer intervals.

Every selector and every state Q/derivative evaluation is a counted callback.
Print only summaries; save all terminal cells and endpoint evidence to JSON.
"""
import heapq
import json
from fractions import Fraction as F
from pathlib import Path
import enclose_bulk_haar_integral as b

I = b.I
S = b.SCALE
INITIAL_CAP = 65536
TOTAL_CAP = 262144
LEAF_CAP = 4096
prior = json.loads((Path(__file__).parent/'bulk-haar-conditional-sign-194-failed.json').read_text())
calls = {'failed_execution_callbacks': prior['total_callbacks'], 'selector': 0, 'state_value_and_angular_derivatives': 0,
         'state_response_derivative': 0}


def count():
    return sum(calls.values())


def absupper(x):
    return max(abs(x.lo), abs(x.hi))


def sym(n):
    return I(-n, n, True)


class J:
    """Real value, first and second angular derivatives (not Taylor coefficients)."""
    __slots__ = ('v', 'd', 'e')

    def __init__(self, v, d=0, e=0):
        self.v, self.d, self.e = [I.lift(x) for x in (v, d, e)]

    @staticmethod
    def lift(x):
        return x if isinstance(x, J) else J(x)

    def __add__(self, x):
        x = J.lift(x)
        return J(self.v+x.v, self.d+x.d, self.e+x.e)

    __radd__ = __add__

    def __neg__(self):
        return J(-self.v, -self.d, -self.e)

    def __sub__(self, x):
        return self+-J.lift(x)

    def __rsub__(self, x):
        return J.lift(x)+-self

    def __mul__(self, x):
        x = J.lift(x)
        return J(self.v*x.v, self.d*x.v+self.v*x.d,
                 self.e*x.v+2*self.d*x.d+self.v*x.e)

    __rmul__ = __mul__

    def inv(self):
        if self.v.hi < 0:
            return -(-self).inv()
        assert self.v.lo > 0, 'reciprocal includes zero'
        r = I(1)/self.v
        return J(r, -self.d*r.square(),
                 2*self.d.square()*r.power(3)-self.e*r.square())

    def __truediv__(self, x):
        return self*J.lift(x).inv()

    def __rtruediv__(self, x):
        return J.lift(x)*self.inv()

    def square(self):
        return J(self.v.square(), 2*self.v*self.d,
                 2*(self.d.square()+self.v*self.e))

    def sqrt(self):
        r = self.v.sqrt()
        assert r.lo > 0, 'sqrt derivative includes zero'
        return J(r, self.d/(2*r), self.e/(2*r)-self.d.square()/(4*r.power(3)))

    def bounded(self, radius):
        return J(self.v.intersect(sym(radius)), self.d, self.e)

    def enc(self):
        return {'value': self.v.enc(), 'first': self.d.enc(), 'second': self.e.enc()}


def dot(a, c):
    return sum((x*y for x, y in zip(a, c)), J(0))


def mv(a, v):
    return [dot(row, v) for row in a]


def matmul(a, c):
    return [[dot(row, col) for col in zip(*c)] for row in a]


P = [[J(x) for x in row] for row in b.P]
COORD = [[J(int(i == j)) for j in range(3)] for i in range(3)]


def rotate(a, basis, gaps):
    if any(g.v.lo <= 0 <= g.v.hi for g in gaps):
        raise ValueError('unresolved original/complementary equality')
    i, j = next((i, j) for i in range(len(a)) for j in range(len(a))
                if gaps[i].v.hi < 0 < gaps[j].v.lo)
    low, high, off = -gaps[i], gaps[j], a[i][j]
    rad = (off.square()+high*low).sqrt()
    eta = low/(rad+off) if off.v.lo >= 0 else (rad-off)/high
    norm = (1+eta.square()).sqrt()
    first = [((basis[i][k]+eta*basis[j][k])/norm).bounded(S) for k in range(3)]
    second = [((-eta*basis[i][k]+basis[j][k])/norm).bounded(S) for k in range(3)]
    return first, [second]+[basis[k] for k in range(len(a)) if k not in (i, j)], (i, j)


geometry_cache = {}


def geometry(left, right):
    key = (left, right)
    if key in geometry_cache:
        return geometry_cache[key]
    calls['selector'] += 1
    angle = I((2*b.PI*left).lo, (2*b.PI*right).hi, True)
    cv, sv = b.trig(angle, True), b.trig(angle)
    c, s = J(cv, -sv, -cv), J(sv, cv, -sv)
    c2, s2, cs = c.square(), s.square(), c*s
    js = [[c2/16, -cs/4, c2/4+s2/2], [-cs/4, -c2, cs],
          [c2/4+s2/2, cs, c2]]
    a = matmul(matmul(P, js), P)
    tau = sum((a[k][k] for k in range(3)), J(0))/3
    gaps = [a[k][k]-tau for k in range(3)]
    try:
        first, rest, pair = rotate(a, COORD, gaps)
        unused = next(k for k in range(3) if k not in pair)
        comp = [[dot(v, mv(a, w)) for w in rest] for v in rest]
        second, final, pair2 = rotate(comp, rest, [-gaps[unused], gaps[unused]])
        out = [[v.bounded(b.ROW_BOUNDS[k].hi) for k, v in enumerate(mv(P, u))]
               for u in [first, second, final[0]]]
        result = (out, {'pairs': [pair, pair2], 'gaps': [x.v.enc() for x in gaps]})
    except (AssertionError, ValueError, StopIteration) as exc:
        result = (None, {'reason': str(exc), 'gaps': [x.v.enc() for x in gaps]})
    geometry_cache[key] = result
    return result


def q(g, v):
    calls['state_value_and_angular_derivatives'] += 1
    x, y, z = v
    t, p, c = 3*(x.square()+y.square()), 3*(y.square()+x*z), -18*y.square()*(x.square()+x*z)
    w = t*g
    ev = b.exp_negative(w.v)
    ex = J(ev, -w.d*ev, (w.d.square()-w.e)*ev)
    return ex*(p*g+c*g.square())


def fallback(g):
    # L426 (13): |Q| <= (1+sqrt(3g/80))/2 on every selected unit vector.
    return sym(((1+(3*g/80).sqrt())/2).hi)


points = {}


def point(x, gs):
    if x not in points:
        vectors, meta = geometry(x, x)
        values = []
        for g in gs:
            f = fallback(g)
            values.append(f if vectors is None else
                          (sum((q(g, v).v for v in vectors), I(0))/3).intersect(f))
        points[x] = values
    return points[x]


def cell(left, right, gs):
    vectors, meta = geometry(left, right)
    mass = right-left
    rec = {'left': str(left), 'right': str(right), 'mass': str(mass),
           'selector': meta, 'values': []}
    if vectors is not None:
        # These full jet ranges certify the real C^2 hypotheses on this closed cell.
        rec['state_jets'] = [[x.enc() for x in v] for v in vectors]
        lv, rv = point(left, gs), point(right, gs)
    outputs = []
    for k, g in enumerate(gs):
        f = fallback(g)
        if vectors is None:
            result = f*mass
            val = {'kind': 'unresolved', 'integral': result.enc(),
                   'unresolved_radius': str(F(absupper(result), S))}
        else:
            jets = [q(g, v) for v in vectors]
            ran = (sum((j.v for j in jets), I(0))/3).intersect(f)
            e = sum((j.e for j in jets), I(0))/3
            m2 = I(absupper(e), absupper(e), True)
            # Normalized angular integral: h^3/(24*pi) = mass*h^2/12.
            h = 2*b.PI*mass
            err = (mass*h.square()*m2/12).hi
            trap = (lv[k]+rv[k])*mass/2
            result = I(trap.lo-err, trap.hi+err, True).intersect(ran*mass)
            val = {'kind': 'strict', 'range': ran.enc(), 'second': e.enc(),
                   'endpoint_values': [lv[k].enc(), rv[k].enc()],
                   'trapezoid': trap.enc(), 'quadrature_radius': str(F(err, S)),
                   'integral': result.enc()}
        outputs.append(result)
        rec['values'].append(val)
    return rec, outputs


def main():
    directory = Path(__file__).parent
    source = json.loads((directory/'bulk-haar-integral-enclosure-188.json').read_text())
    ends = source['g_full_range']
    a, z = [F(ends[k]) for k in ('lower', 'upper')]
    centers = [a, (a+z)/2, z]
    gs = [I(g) for g in centers]
    totals = [I(0) for _ in gs]
    leaves, heap, serial = {}, [], 0

    def add(left, right):
        nonlocal serial
        rec, vals = cell(left, right, gs)
        leaves[serial] = (rec, vals)
        score = max(v.hi-v.lo for v in vals)
        heapq.heappush(heap, (-score, serial))
        for k, v in enumerate(vals):
            totals[k] = totals[k]+v
        serial += 1

    add(F(0), F(1))
    reason = None
    # A split costs <= 2 selector + 6 endpoint selector + 27 state callbacks
    # in the absence of all cache hits. Reserve 64, safely above this bound.
    while len(leaves) < LEAF_CAP and count()+64 <= INITIAL_CAP:
        signs = [1 if v.lo > 0 else -1 if v.hi < 0 else 0 for v in totals]
        if 1 in signs and -1 in signs:
            reason = 'CERTIFIED_OPPOSITE_POINT_SIGNS'
            break
        if all(s != 0 for s in signs) and max(v.hi-v.lo for v in totals) <= S//5000:
            reason = 'INITIAL_STRICT_POINT_SIGNS_REQUESTED_RADIUS'
            break
        _, idx = heapq.heappop(heap)
        rec, vals = leaves.pop(idx)
        for k, v in enumerate(vals):
            # Exact subtraction of prior accumulated endpoints, not interval subtraction.
            totals[k] = I(totals[k].lo-v.lo, totals[k].hi-v.hi, True)
        left, right = F(rec['left']), F(rec['right'])
        mid = (left+right)/2
        add(left, mid)
        add(mid, right)
    reason = reason or ('ANGULAR_LEAF_CAP' if len(leaves) == LEAF_CAP else 'INITIAL_CALLBACK_CAP')
    records = sorted((r for r, _ in leaves.values()), key=lambda r: F(r['left']))
    assert F(records[0]['left']) == 0 and F(records[-1]['right']) == 1
    assert all(x['right'] == y['left'] for x, y in zip(records, records[1:]))
    assert sum((F(r['mass']) for r in records), F(0)) == 1
    sums = []
    for k in range(3):
        lo = sum(F(r['values'][k]['integral']['lower']) for r in records)
        hi = sum(F(r['values'][k]['integral']['upper']) for r in records)
        assert F(totals[k].lo, S) == lo and F(totals[k].hi, S) == hi
        strict = [r['values'][k] for r in records if r['values'][k]['kind'] == 'strict']
        unresolved = [r['values'][k] for r in records if r['values'][k]['kind'] == 'unresolved']
        sums.append({'g': str(centers[k]), 'value': totals[k].enc(),
                     'strict_integral_width': str(sum((F(v['integral']['upper'])-F(v['integral']['lower']) for v in strict), F(0))),
                     'quadrature_radius_sum': str(sum((F(v['quadrature_radius']) for v in strict), F(0))),
                     'unresolved_radius_sum': str(sum((F(v['unresolved_radius']) for v in unresolved), F(0))),
                     'strict_sign': 'positive' if totals[k].lo > 0 else 'negative' if totals[k].hi < 0 else 'unresolved'})
    out = {'step': 194, 'reason': reason, 'g_full_range': ends,
           'precision_places': 24, 'callback_counts': calls, 'callback_total': count(),
           'initial_callback_cap': INITIAL_CAP, 'total_callback_cap': TOTAL_CAP,
           'leaves': len(records), 'leaf_cap': LEAF_CAP,
           'centers': sums, 'requested_initial_radius': '1/10000',
           'unresolved_mass': str(sum((F(r['mass']) for r in records if r['values'][0]['kind'] == 'unresolved'), F(0))),
           'cells': records,
           'checks': {'full_partition': True, 'exact_endpoint_sums': True,
                      'callback_cap': count() <= INITIAL_CAP, 'leaf_cap': len(records) <= LEAF_CAP,
                      'precision_cap': 24 <= 160, 'same_literal_two_stage_selector': True},
           'failures': [] if reason == 'CERTIFIED_OPPOSITE_POINT_SIGNS' else [reason]}
    path = directory/'bulk-haar-conditional-sign-194.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Stop:', reason)
    print('Callbacks actual/initial/total:', count(), INITIAL_CAP, TOTAL_CAP)
    print('Leaves actual/required cap:', len(records), LEAF_CAP)
    for s in sums:
        print('g / A enclosure / sign:', float(F(s['g'])), [float(F(s['value'][k])) for k in ('lower', 'upper')], s['strict_sign'])
    print('Unresolved angular mass:', out['unresolved_mass'])
    print('Failures:', out['failures'])
    print('Certificate:', path)


if __name__ == '__main__':
    main()

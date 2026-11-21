"""One fixed-box rational sign pass for C030z; no quadrature or sweep.

Complete Laurent identities, parameter boxes, cell bounds, exceptional
branch and strict witness evidence are saved. No midpoint coefficients.
"""
import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'actual-sign-certificate-1309.json'
SOURCE = HERE / 'actual-singleton-certificate-1307.json'
REPLAY = HERE / 'actual-singleton-replay-1307.json'
ALGEBRA = HERE / 'positive-diagonal-degree-six-1304.py'
BOUNDS = {
    'A': ('3.7172599285e-5', '3.7172599286e-5'),
    'B': ('1.4417393139e-7', '1.4417393141e-7'),
    'C': ('6.6303168020e-10', '6.6303168031e-10'),
    'D': ('3.2136641485e-12', '3.2136641527e-12'),
    'E': ('1.5876934435e-14', '1.5876934595e-14'),
}


class I:
    def __init__(self, lo=0, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def lift(v):
        return v if isinstance(v, I) else I(v)

    def __add__(self, v):
        v = I.lift(v)
        return I(self.lo+v.lo, self.hi+v.hi)
    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, v):
        return self + -I.lift(v)

    def __rsub__(self, v):
        return I.lift(v) + -self

    def __mul__(self, v):
        v = I.lift(v)
        products = [a*b for a in (self.lo, self.hi) for b in (v.lo, v.hi)]
        return I(min(products), max(products))
    __rmul__ = __mul__

    def __truediv__(self, v):
        v = I.lift(v)
        assert v.lo*v.hi > 0, 'zero-containing divisor'
        return self*I(1/v.hi, 1/v.lo)

    def __pow__(self, n):
        assert n >= 0
        result = I(1)
        for _ in range(n):
            result = result*self
        return result

    def data(self):
        return {'lower': str(self.lo), 'upper': str(self.hi)}

    def sign(self):
        return 1 if self.lo > 0 else -1 if self.hi < 0 else 0


def add(p, q):
    return [(p[i] if i < len(p) else I())+(q[i] if i < len(q) else I())
            for i in range(max(len(p), len(q)))]


def scale(p, a):
    return [c*a for c in p]


def mul(p, q):
    result = [I() for _ in range(len(p)+len(q)-1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i+j] = result[i+j]+a*b
    return result


def evaluate(p, value):
    result = I()
    for c in reversed(p):
        result = result*value+c
    return result


def bernstein(p, a, b):
    # p(a+(b-a)t)=sum q_j t^j; q_j=sum c_i binom(i,j)a^(i-j)(b-a)^j.
    d = len(p)-1
    q = [sum((p[i]*comb(i, j)*a**(i-j)*(b-a)**j for i in range(j, d+1)), I())
         for j in range(d+1)]
    beta = [sum((q[j]*F(comb(i, j), comb(d, j)) for j in range(i+1)), I())
            for i in range(d+1)]
    return I(min(c.lo for c in beta), max(c.hi for c in beta)), beta


def identities():
    spec = importlib.util.spec_from_file_location('formal1304', ALGEBRA)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.NAMES = ('A', 'B', 'C', 'D', 'E', 'z', 'w')
    A, B, C, D, E, z, w = (module.var(i) for i in range(7))
    k = A/(2*C)
    l0 = -E*k+B**2/(2*A)
    l1 = -E*k+E*B/D-B**2/(2*A)
    n0 = A/3-E*k**2
    n1 = A/3-2*E*k**2
    n2 = n0
    x = 2-module.P(1)/z
    L = -E*k*(1+x)+E*x*B/D+(1-x)*B**2/(2*A)
    N = A*(x*x+x+1)/3-E*k**2*(1+x)**2
    ell = -l1+(l0+2*l1)*z
    n = n2+(-4*n2-n1)*z+(4*n2+2*n1+n0)*z*z
    p = n/(z*w)
    V = p-k*(1+x)
    J = V-x*B/D
    H = p*J-x*V*C/E+(1-x)*p*B**2/(2*A*E)
    v = n-k*(3*z-1)*w
    j = v-(B/D)*(2*z-1)*w
    h = n*j-(C/E)*(2*z-1)*v*w+(1-z)*(B**2/(2*A*E))*n*w
    residuals = {'zL-l': z*L-ell, 'z2N-n': z*z*N-n,
                 'zwV-v': z*w*V-v, 'zwJ-j': z*w*J-j,
                 'z2w2H-h': z*z*w*w*H-h}
    assert all(not v.t for v in residuals.values())
    return {'variables': list(module.NAMES),
            'w_interpretation': 'independent nonzero variable; then specialize w=l(z)',
            'residuals': {k: v.record() for k, v in residuals.items()},
            'l': ell.record(), 'n': n.record(),
            'v_with_w': v.record(), 'j_with_w': j.record(), 'h_with_w': h.record()}


def main():
    source, replay = (json.loads(f.read_text()) for f in (SOURCE, REPLAY))
    assert source['status'] == 'completed' and replay['status'] == 'passed'
    assert not replay['failures']
    assert replay['source_sha256'] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    parameters = {k: I(*v) for k, v in BOUNDS.items()}
    for n, name in enumerate(BOUNDS, 2):
        box = parameters[name]
        assert 0 < box.lo < F(source['S'][str(n)]['lower'])
        assert F(source['S'][str(n)]['upper']) < box.hi
    report = {'status': 'running', 'failures': [],
              'scope': 'finite formal degree-six compatibility only; no RH or univalence',
              'arithmetic': 'exact Fraction endpoints; conditional1307 actual-input inclusion',
              'inputs': {str(f.relative_to(ROOT)): hashlib.sha256(f.read_bytes()).hexdigest()
                         for f in (SOURCE, REPLAY, ALGEBRA, Path(__file__))},
              'parameters': {k: v.data() for k, v in parameters.items()},
              'limits': {'max_cells': 256, 'max_depth': 16},
              'map': 'z=1/(2-x); 0<z<1 bijective with x<1; x=2-1/z',
              'formal': identities()}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    A, B, C, D, E = parameters.values()
    k = A/(2*C)
    l0, l1 = -E*k+B**2/(2*A), -E*k+E*B/D-B**2/(2*A)
    n0, n1 = A/3-E*k**2, A/3-2*E*k**2
    ell = [-l1, l0+2*l1]
    n = [n0, -4*n0-n1, 5*n0+2*n1]
    v = add(n, scale(mul([I(-1), I(3)], ell), -k))
    j = add(v, scale(mul([I(-1), I(2)], ell), -(B/D)))
    h = add(add(mul(n, j), scale(mul(mul([I(-1), I(2)], v), ell), -(C/E))),
            scale(mul(mul([I(1), I(-1)], n), ell), B**2/(2*A*E)))
    polynomials = {'l': ell, 'n': n, 'v': v, 'j': j, 'h': h}
    report['constants'] = {name: val.data() for name, val in
                           {'k': k, 'l0': l0, 'l1': l1, 'n0': n0, 'n1': n1}.items()}
    report['polynomials'] = {name: [c.data() for c in poly] for name, poly in polynomials.items()}

    # l is linear. This interval encloses its exact unique root for every
    # parameter tuple; evaluate n on that whole interval before dividing.
    assert ell[1].sign() != 0
    root = -ell[0]/ell[1]
    nr = evaluate(n, root)
    assert ell[0].lo > 0 > ell[1].hi
    assert F('0.065') < root.lo <= root.hi < F('0.066') and nr.lo > F('6e-7')
    report['descartes'] = {'polynomial': 'l', 'coefficient_signs_ascending': [1, -1],
                           'sign_variations': 1, 'positive_roots_with_multiplicity': 1,
                           'source': 'Basu-Pollack-Roy2006 second edition Theorem2.33 p43',
                           'qualification': 'linear nonzero leading coefficient for every tuple; no square-free oracle'}
    report['exceptional'] = {'l_slope': ell[1].data(), 'unique_l_root_z': root.data(),
                             'n_at_every_possible_l_root': nr.data(),
                             'L_zero_N_nonzero': 'rejected by pL=N' if nr.sign() else 'unresolved',
                             'L_zero_N_zero': 'empty uniformly in boxes' if nr.sign() else 'retain free p'}

    cells = [(F(0), F(1), 0)]
    # One adaptive uniform sign pass, no point sampling. Coefficient-box
    # dependence is enlarged by inclusion, so certified signs hold for all tuples.
    index = 0
    while index < len(cells):
        a, b, depth = cells[index]
        ranges = {name: bernstein(poly, a, b)[0] for name, poly in polynomials.items()}
        signs = {name: val.sign() for name, val in ranges.items()}
        excluded = []
        if signs['l']:
            excluded += [name for name in ('n', 'v', 'j') if signs[name] == -signs['l']]
        if signs['h'] == -1:
            excluded.append('h')
        feasible = bool(signs['l'] and signs['h'] == 1 and
                        all(signs[name] == signs['l'] for name in ('n', 'v', 'j')))
        if not excluded and not feasible and depth < 16 and len(cells) < 256:
            mid = (a+b)/2
            cells[index:index+1] = [(a, mid, depth+1), (mid, b, depth+1)]
            continue
        index += 1

    records = []
    for a, b, depth in cells:
        bern = {name: bernstein(poly, a, b) for name, poly in polynomials.items()}
        ranges = {name: val[0] for name, val in bern.items()}
        signs = {name: val.sign() for name, val in ranges.items()}
        excluded = []
        if signs['l']:
            excluded += [name for name in ('n', 'v', 'j') if signs[name] == -signs['l']]
        if signs['h'] == -1:
            excluded.append('h')
        feasible = bool(signs['l'] and signs['h'] == 1 and
                        all(signs[name] == signs['l'] for name in ('n', 'v', 'j')))
        records.append({'z': [str(a), str(b)], 'depth': depth,
                        'status': 'excluded' if excluded else 'feasible' if feasible else 'unresolved',
                        'failed_numerators': excluded,
                        'signs': signs, 'ranges': {name: val.data() for name, val in ranges.items()},
                        'bernstein': {name: [v.data() for v in row[1]] for name, row in bern.items()}})
    assert len(records) <= 256 and max(r['depth'] for r in records) <= 16
    assert cells[0][0] == 0 and cells[-1][1] == 1
    assert all(cells[i][1] == cells[i+1][0] for i in range(len(cells)-1))
    report['cells'] = records
    report['coverage_summary'] = [{k: row[k] for k in ('z', 'depth', 'status', 'failed_numerators', 'signs')}
                                  for row in records]
    report['tails'] = {'x_to_minus_infinity': records[0], 'x_to_one_from_below': records[-1],
                       'endpoints': 'z=0 and z=1 excluded; closed-cell polynomial bounds cover both limits'}
    feasible_cells = [r for r in records if r['status'] == 'feasible']
    if feasible_cells:
        cell = feasible_cells[0]
        z = sum(map(F, cell['z']))/2
        x = 2-1/z
        X = I(x)
        L = -E*k*(1+X)+E*X*B/D+(1-X)*B**2/(2*A)
        N = A*(X**2+X+1)/3-E*k**2*(1+X)**2
        assert L.sign() != 0
        p = N/L
        V = p-k*(1+X)
        J = V-X*B/D
        H = p*J-X*V*C/E+(1-X)*p*B**2/(2*A*E)
        tau = (1-X)/A
        values = {'p': p, 'V': V, 'J': J, 'H': H, 'tau': tau}
        assert x < 1 and all(v.lo > 0 for v in values.values())
        report['witness'] = {'selection': 'rational center of first uniformly feasible sign cell; no sweep',
                             'z': str(z), 'x': str(x), 'cell': cell['z'],
                             'L': L.data(), 'N': N.data(),
                             'values': {k: v.data() for k, v in values.items()},
                             'exact_definition': 'p=N(x)/L(x) in actual constants; d2=sqrt(p),d3=V,d4=sqrt(p)J,d5=H',
                             'equality': 'pL=N by definition, never by rounded residual'}
        margins = {'p': F(11509), 'V': F(4000000), 'J': F(10000000),
                   'H': F(24800000000000), 'tau': F(3940000)}
        assert all(values[name].lo > bound for name, bound in margins.items())
        report['witness']['strict_rational_lower_margins'] = {name: str(v) for name, v in margins.items()}
    report['summary'] = {'cells': len(records), 'max_depth': max(r['depth'] for r in records),
                         'cell_counts': dict(Counter(r['status'] for r in records)),
                         'strict_actual_witness': bool(feasible_cells),
                         'common_L_N_zero_excluded': bool(nr.sign()),
                         'both_tails_have_sign_certificate': all(r['status'] != 'unresolved' for r in (records[0], records[-1])),
                         'full_solution_set_classified': not any(r['status'] == 'unresolved' for r in records),
                         'required': 'one strict actual witness OR branch-complete exhaustive obstruction',
                         'result': 'feasible' if feasible_cells else 'inconclusive'}
    report['status'] = 'completed'
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report['summary'], sort_keys=True))
    if feasible_cells:
        print('WITNESS x='+report['witness']['x']+'; required p,V,J,H,tau>0; exact p=N/L')
        for name, val in values.items():
            print(f'{name}: [{float(val.lo):.9g}, {float(val.hi):.9g}] (display only; exact fractions on disk)')
    print('FAILURES:', report['failures'], 'CERTIFICATE:', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()

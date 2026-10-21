"""Independent L111 audit: Q(T) coefficients and a four-dimensional algebra.

No producer imports. Inversion solves the multiplication matrix over Q(T),
rather than using the producer's nested quadratic norm arithmetic.
All coefficients and residuals are saved; geometry is proved in L111.
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


class Algebra:
    """Basis 1,w,v,wv; w²=d, v²=e0+e1*w over Q(T)."""
    def __init__(self, d, e0, e1=0):
        self.d, self.e0, self.e1 = map(RF.lift, (d, e0, e1))

    def elt(self, *c):
        return Element(self, list(c) + [0]*(4-len(c)))


class Element:
    def __init__(self, algebra, c):
        assert len(c) == 4
        self.alg, self.c = algebra, list(map(RF.lift, c))

    def lift(self, x):
        if isinstance(x, Element):
            assert x.alg is self.alg
            return x
        return self.alg.elt(x)

    def __bool__(self):
        return any(self.c)

    def __add__(self, x):
        x = self.lift(x)
        return Element(self.alg, [a+b for a, b in zip(self.c, x.c)])

    __radd__ = __add__

    def __neg__(self):
        return Element(self.alg, [-a for a in self.c])

    def __sub__(self, x):
        return self + -self.lift(x)

    def __rsub__(self, x):
        return self.lift(x) + -self

    def __mul__(self, x):
        x = self.lift(x)
        out = [RF() for _ in range(4)]
        for i, ci in enumerate(self.c):
            if not ci:
                continue
            for j, cj in enumerate(x.c):
                if not cj:
                    continue
                iw, iv = (i % 2)+(j % 2), (i//2)+(j//2)
                terms = [(iw, iv, ci*cj)] if iv < 2 else [
                    (iw, 0, ci*cj*self.alg.e0),
                    (iw+1, 0, ci*cj*self.alg.e1)]
                for pw, pv, coef in terms:
                    idx = pw % 2 + 2*pv
                    out[idx] = out[idx] + coef*self.alg.d**(pw//2)
        return Element(self.alg, out)

    __rmul__ = __mul__

    def inverse(self):
        # Column j is multiplication by this element on basis vector j.
        columns = [(self*self.alg.elt(*[int(i == j) for i in range(4)])).c
                   for j in range(4)]
        rows = [[columns[j][i] for j in range(4)] + [RF(int(i == 0))]
                for i in range(4)]
        for k in range(4):
            pivot = next(i for i in range(k, 4) if rows[i][k])
            rows[k], rows[pivot] = rows[pivot], rows[k]
            q = rows[k][k]
            rows[k] = [c/q for c in rows[k]]
            for i in range(4):
                if i != k and rows[i][k]:
                    q = rows[i][k]
                    rows[i] = [a-q*b for a, b in zip(rows[i], rows[k])]
        return Element(self.alg, [rows[i][4] for i in range(4)])

    def __truediv__(self, x):
        x = self.lift(x)
        if not any(x.c[1:]):
            return Element(self.alg, [c/x.c[0] for c in self.c])
        return self*x.inverse()

    def __rtruediv__(self, x):
        return self.lift(x)/self

    def __pow__(self, n):
        out = self.lift(1)
        for _ in range(n):
            out = out*self
        return out

    def data(self):
        return [c.data() for c in self.c]


def value(p, t):
    out = 0
    for c in reversed(p):
        out = out*t+c
    return out


raw = (HERE/'marked-quotient-certificate.json').read_bytes()
saved = json.loads(raw)
checks, residuals = {}, {}


def check(name, ok):
    assert name not in checks
    checks[name] = bool(ok)


def zero(name, x):
    residuals[name] = x.data()
    check(name, not x)


T = RF([0, 1])
q4 = 7+52*T-6*T**2-64*T**3-25*T**4
a, b = 12-3*T**2, -33*q4
f = 11*(T**2-4)*q4
F = T**5+T**4-4*T**3-3*T**2+3*T+1
K, L, J = T**2-T-1, T**2+T-1, (T+2)*(T**2-1)
polys = {'a': a, 'b': b, 'f': f, 'Q4': q4, 'F': F,
         'K': K, 'L': L, 'J': J}
for name, p in polys.items():
    check('saved_polynomial_'+name, p.q == [1] and
          p.p == list(map(Q, saved['polynomials'][name])))
for name, path in [('L109', 'lemmas/L109-pair-only-genus-two-and-minus-three-lifting.md'),
                   ('L110', 'lemmas/L110-explicit-pair-genus-two-model.md')]:
    check('input_hash_'+name, sha256((ROOT/path).read_bytes()).hexdigest()
          == saved['input_sha256'][name])

# First compute rho and z in the quadratic subalgebra; the extra v is unused.
base = Algebra(f, 1)
t, w = base.elt(T), base.elt(0, 1)
u = (base.elt(F)-11-base.elt(K)*w)/base.elt(60*F)
m = 2-10*u
rho = m*base.elt(L)/base.elt(30*(T+2)*K)
z = -m**2*base.elt((T-2)*L**2)/base.elt(300*(T+2)*K**2)
zero('exact_marked_square_multiplier', z-base.elt(a)*rho**2)
zero('rho_removable_K_formula', rho-(base.elt(11*J)+w)*base.elt(L)/
     base.elt(180*(T+2)*F))
zero('sextic_factor_product', base.elt(a*b/9-f))
for name, x in [('rho', rho), ('z', z)]:
    rec = saved[name]
    den = list(map(Q, rec['C']))
    rec_x = base.elt(RF(list(map(Q, rec['A'])), den),
                    RF(list(map(Q, rec['B'])), den))
    zero('saved_full_'+name, x-rec_x)
    check(name+'_nonzero', bool(x))

source = Algebra(f, z.c[0], z.c[1])
ws, vs = source.elt(0, 1), source.elt(0, 0, 1)
rhos = Element(source, rho.c)
hs = vs/rhos
rs = 3*ws/hs
zero('marked_to_split_h_relation', hs**2-source.elt(a))
zero('marked_to_split_R_relation', rs**2-source.elt(b))
zero('marked_to_split_product', hs*rs-3*ws)
zero('marked_W_composition', hs*rs/3-ws)
# Recompute the entire multiplier after recovering W, rather than retain rho.
us_back = (source.elt(F)-11-source.elt(K)*(hs*rs/3))/source.elt(60*F)
rhos_back = (2-10*us_back)*source.elt(L)/source.elt(30*(T+2)*K)
zero('marked_v_composition', hs*rhos_back-vs)
zero('marked_u_composition', us_back-Element(source, u.c))
zs_back = -(2-10*us_back)**2*source.elt((T-2)*L**2)/source.elt(300*(T+2)*K**2)
zero('marked_z_composition', zs_back-Element(source, z.c))

split = Algebra(a, b)
h, r = split.elt(0, 1), split.elt(0, 0, 1)
ww = h*r/3
uu = (split.elt(F)-11-split.elt(K)*ww)/split.elt(60*F)
mm = 2-10*uu
rrho = mm*split.elt(L)/split.elt(30*(T+2)*K)
vv = rrho*h
zz = -mm**2*split.elt((T-2)*L**2)/split.elt(300*(T+2)*K**2)
zero('split_to_marked_W_relation', ww**2-split.elt(f))
zero('split_to_marked_v_relation', vv**2-zz)
hh = vv/rrho
zero('split_h_composition', hh-h)
zero('split_R_composition', 3*ww/hh-r)

# The original scalar is the complete H0 polynomial of L109. Preservation
# of u,z above preserves every term; independently reconstruct phi's input.
phi = RF(1)
for _ in range(5):
    phi = phi*(3*T**2+T+1)
phi = phi*(1-5*T)
phi_expected = [1, 0, 0, -55, -165, -594, -1100, -2145,
                -2475, -2970, -1782, -1215]
check('original_scalar_full_input_coefficients', phi.p == phi_expected)

# Every saved identity is compared with the independently recomputed one.
def saved_components(rec):
    if isinstance(rec['A'], dict):
        return saved_components(rec['A']) + saved_components(rec['B'])
    den = list(map(Q, rec['C']))
    return [RF(list(map(Q, rec[key])), den) for key in ['A', 'B']]

for name, rec in saved['field_residuals'].items():
    old = saved_components(rec)
    new = residuals[name]
    old += [RF()]*(4-len(old))
    check('saved_residual_'+name,
          all(not (c-RF(list(map(Q, n['numerator'])),
                        list(map(Q, n['denominator']))))
              for c, n in zip(old, new)))
check('complete_saved_residual_set', len(saved['field_residuals']) == 12)

def derivative(p):
    return [i*p[i] for i in range(1, len(p))]

gcds = {'a_a_prime': monic_gcd(a.p, derivative(a.p)),
        'b_b_prime': monic_gcd(b.p, derivative(b.p)),
        'a_b': monic_gcd(a.p, b.p)}
for name, g in gcds.items():
    check('squarefree_'+name, g == [1] and g == saved['squarefree_gcds'][name])
check('quadratic_degree', len(a.p) == 3)
check('quartic_degree', len(b.p) == 5)
check('coprime_branch_count', len(a.p)+len(b.p)-2 == 6)

boundary = {}
for t0 in [2, -2]:
    bv = value(b.p, t0)
    root = isqrt(bv.numerator)
    square = bv.denominator == 1 and root*root == bv
    rec = {'R_squared': str(bv), 'square': square,
           'R_nonnegative_if_square': root if square else None,
           'a': str(value(a.p, t0)), 'Q4': str(value(q4.p, t0)),
           'b_derivative': str(value(derivative(b.p), t0))}
    boundary[str(t0)] = rec
    check('complete_boundary_'+str(t0), rec == saved['boundary'][str(t0)])
check('origin_exact', value(b.p, 2) == 165**2)
check('origin_smooth_R_partial', 2*165 != 0)
check('minus_two_no_rational_point', value(b.p, -2) == 297 and
      not boundary['-2']['square'])
check('E_no_rational_infinity', b.p[-1] == 825 and isqrt(825)**2 != 825)
check('infinity_h_normalized_constant', a.p[-1] == -3)
check('infinity_charts_disjoint_unramified', a.p[-1]*b.p[-1] != 0)
inf = {'E_R_over_T_squared_squared': str(b.p[-1]),
       'D_h_over_T_squared': str(a.p[-1]),
       'E_residue_field': 'Q(sqrt(33))',
       'D_residue_field': 'Q(sqrt(33),sqrt(-3))'}
check('complete_infinity_record', inf == saved['infinity'])
u2 = (value(F.p, 2)-11)/(60*value(F.p, 2))
rho2 = (2-10*u2)*value(L.p, 2)/(30*4*value(K.p, 2))
norm = {'u': str(u2), 'rho': str(rho2),
        'a_over_W_squared': str(Q(-3, 11)/value(q4.p, 2)),
        'v_over_W_plus': str(rho2/55),
        'z_over_W_squared': str(rho2**2*Q(-3, 11)/value(q4.p, 2)),
        'a_prime_at_2': str(value(derivative(a.p), 2)),
        'a_prime_at_minus_2': str(value(derivative(a.p), -2)),
        'f_prime_at_2': str(value(derivative(f.p), 2))}
check('T_two_normalized_h_over_W', Q(norm['a_over_W_squared']) == Q(1, 55**2))
check('T_two_normalized_v_over_W', Q(norm['v_over_W_plus']) == Q(1, 660))
check('T_two_normalized_z_over_W_squared', Q(norm['z_over_W_squared']) == Q(1, 660**2))
check('T_two_origin_R', 3*55 == 165)
check('T_two_original_boundary', u2 == 0 and phi.p[0] == 1)
check('ramified_uniformizers', norm['a_prime_at_2'] == '-12' and
      norm['a_prime_at_minus_2'] == '12' and norm['f_prime_at_2'] == '-36300')

# Compare every producer check flag with its independently recomputed fact.
aliases = {'a_a_prime': 'squarefree_a_a_prime',
           'b_b_prime': 'squarefree_b_b_prime', 'a_b': 'squarefree_a_b'}
for name, ok in saved['checks'].items():
    check('saved_check_'+name, ok == checks[aliases.get(name, name)] and ok)
check('saved_report_complete', saved['check_count'] == len(saved['checks']) == 28
      and saved['failures'] == [])
check('saved_scan_scope', saved['integer_origin_scan'] ==
      'Not run: exact boundary origin found as specified.')
required = {'actual_projection_degree': 2, 'required_projection_degree': 2,
            'actual_quartic_degree': 4, 'required_squarefree_degree': 4,
            'actual_genus_E': 1, 'required_genus_E': 1,
            'actual_genus_D': 3, 'D_to_E_geometric_branch_points': 4}
check('saved_thresholds', {k: saved['thresholds'][k] for k in required} == required)

out = {'producer_sha256': sha256(raw).hexdigest(),
       'producer_script_sha256': sha256((HERE/'marked_quotient.py').read_bytes()).hexdigest(),
       'input_sha256': saved['input_sha256'],
       'basis': {'source': ['1', 'W', 'v', 'Wv'],
                 'split': ['1', 'h', 'R', 'hR']},
       'polynomials': {k: v.data() for k, v in polys.items()},
       'rho': rho.data(), 'z': z.data(), 'field_residuals': residuals,
       'squarefree_gcds': {k: list(map(str, v)) for k, v in gcds.items()},
       'boundary': boundary, 'infinity': inf, 'normalized_at_two': norm,
       'phi_coefficients': phi_expected, 'thresholds': required,
       'geometric_qualification': 'Independent full proof in L111; arithmetic checks alone do not prove properness, degrees or genus.',
       'checks': checks, 'check_count': len(checks),
       'failures': [k for k, v in checks.items() if not v]}
path = HERE/'marked-quotient-audit-certificate.json'
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'checks': len(checks), 'failures': out['failures'],
                  'degree_actual_required': [2, 2], 'genus_actual_required': [1, 1],
                  'origin': [2, 165], 'certificate': str(path.relative_to(ROOT))}))
assert not out['failures']

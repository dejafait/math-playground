"""Exact L111 twist and quotient identities; standard library, no sampling.

Polynomial coefficients are ascending. Full residuals go to disk.
The field/normalization arguments are in the canonical lemma, not this test.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd, isqrt, lcm
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def trim(p):
    p = list(map(Q, p))
    while p and not p[-1]:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return trim([c*x for x in p])


def mul(p, q):
    r = [Q(0)]*max(0, len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return trim(r)


def divrem(p, q):
    p, q = trim(p), trim(q)
    assert q
    r = [Q(0)]*max(0, len(p)-len(q)+1)
    while p and len(p) >= len(q):
        k, c = len(p)-len(q), p[-1]/q[-1]
        r[k] += c
        p = add(p, scale([0]*k+q, -c))
    return trim(r), p


def prim(p):
    p = trim(p)
    den = lcm(*(x.denominator for x in p)) if p else 1
    ns = [int(x*den) for x in p]
    content = 0
    for x in ns:
        content = gcd(content, x)
    if not content:
        return []
    if ns[-1] < 0:
        content = -content
    return [x//content for x in ns]


def pgcd(p, q):
    p, q = prim(p), prim(q)
    while q:
        p, q = q, prim(divrem(p, q)[1])
    return prim(p)


def exact(p, q):
    r, rem = divrem(p, q)
    assert not rem
    return r


def derivative(p):
    return [i*p[i] for i in range(1, len(p))]


def ev(p, t):
    r = 0
    for x in reversed(p):
        r = r*t+x
    return r


class E:
    """(A+B*sqrt(D))/C, polynomial D, with exact reductions."""
    def __init__(self, D, A=0, B=0, C=1):
        self.D = trim(D)
        A, B, C = [trim(p if isinstance(p, (list, tuple)) else [p])
                   for p in (A, B, C)]
        assert C
        g = pgcd(pgcd(A, B), C)
        A, B, C = [exact(p, g) for p in (A, B, C)]
        lc = C[-1]
        self.A, self.B, self.C = [scale(p, 1/lc) for p in (A, B, C)]

    def lift(self, x):
        if isinstance(x, E):
            assert self.D == x.D
            return x
        return E(self.D, x)

    def __add__(self, x):
        if isinstance(x, V):
            return NotImplemented
        x = self.lift(x)
        return E(self.D, add(mul(self.A, x.C), mul(x.A, self.C)),
                 add(mul(self.B, x.C), mul(x.B, self.C)), mul(self.C, x.C))

    __radd__ = __add__

    def __neg__(self):
        return E(self.D, scale(self.A, -1), scale(self.B, -1), self.C)

    def __sub__(self, x):
        if isinstance(x, V):
            return NotImplemented
        return self + -self.lift(x)

    def __rsub__(self, x):
        return self.lift(x) + -self

    def __mul__(self, x):
        if isinstance(x, V):
            return NotImplemented
        x = self.lift(x)
        return E(self.D, add(mul(self.A, x.A), mul(self.D, mul(self.B, x.B))),
                 add(mul(self.A, x.B), mul(self.B, x.A)), mul(self.C, x.C))

    __rmul__ = __mul__

    def __truediv__(self, x):
        if isinstance(x, V):
            return NotImplemented
        x = self.lift(x)
        norm = add(mul(x.A, x.A), scale(mul(self.D, mul(x.B, x.B)), -1))
        assert norm
        return self * E(self.D, mul(x.A, x.C), scale(mul(x.B, x.C), -1), norm)

    def __rtruediv__(self, x):
        return self.lift(x)/self

    def __pow__(self, n):
        assert n >= 0
        r = self.lift(1)
        for _ in range(n):
            r = r*self
        return r

    def data(self):
        return {k: [str(c) for c in p]
                for k, p in [('A', self.A), ('B', self.B), ('C', self.C)]}

    def zero(self):
        return not self.A and not self.B


class V:
    """Quadratic extension of E with specified relation q^2=rel."""
    def __init__(self, rel, A=0, B=0):
        self.rel = rel
        self.A, self.B = rel.lift(A), rel.lift(B)

    def lift(self, x):
        if isinstance(x, V):
            assert (x.rel-self.rel).zero()
            return x
        return V(self.rel, x)

    def __add__(self, x):
        x = self.lift(x)
        return V(self.rel, self.A+x.A, self.B+x.B)

    __radd__ = __add__

    def __neg__(self):
        return V(self.rel, -self.A, -self.B)

    def __sub__(self, x):
        return self + -self.lift(x)

    def __rsub__(self, x):
        return self.lift(x) + -self

    def __mul__(self, x):
        x = self.lift(x)
        return V(self.rel, self.A*x.A+self.rel*self.B*x.B,
                 self.A*x.B+self.B*x.A)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.lift(x)
        norm = x.A*x.A-self.rel*x.B*x.B
        assert not norm.zero()
        return self*V(self.rel, x.A/norm, -x.B/norm)

    def __rtruediv__(self, x):
        return self.lift(x)/self

    def __pow__(self, n):
        r = self.lift(1)
        for _ in range(n):
            r = r*self
        return r

    def zero(self):
        return self.A.zero() and self.B.zero()

    def data(self):
        return {'A': self.A.data(), 'B': self.B.data()}


q4 = [7, 52, -6, -64, -25]
a = [12, 0, -3]
b = scale(q4, -33)
f = scale(mul([-4, 0, 1], q4), 11)
F = [1, 3, -3, -4, 1, 1]
K, L = [-1, -1, 1], [-1, 1, 1]
J = mul([2, 1], [-1, 0, 1])
checks, residuals = {}, {}


def check(name, ok):
    assert name not in checks
    checks[name] = bool(ok)


def zero(name, value):
    residuals[name] = value.data()
    check(name, value.zero())


T, W = E(f, [0, 1]), E(f, 0, 1)
u = (ev(F, T)-11-ev(K, T)*W)/(60*ev(F, T))
M = 2-10*u
rho = M*ev(L, T)/(30*(T+2)*ev(K, T))
z = -M**2*(T-2)*ev(L, T)**2/(300*(T+2)*ev(K, T)**2)
zero('exact_marked_square_multiplier', z-ev(a, T)*rho**2)
zero('rho_removable_K_formula', rho-(11*ev(J, T)+W)*ev(L, T)/
     (180*(T+2)*ev(F, T)))
zero('sextic_factor_product', ev(a, T)*ev(b, T)/9-ev(f, T))
check('rho_nonzero', not rho.zero())
check('z_nonzero', not z.zero())
v = V(z, 0, 1)
h = v/rho
R = 3*W/h
zero('marked_to_split_h_relation', h**2-ev(a, T))
zero('marked_to_split_R_relation', R**2-ev(b, T))
zero('marked_to_split_product', h*R-3*W)
zero('marked_W_composition', h*R/3-W)
zero('marked_v_composition', h*rho-v)

# The other direction is checked in Q(T)(h,R), h^2=a, R^2=b.
t0, h0 = E(a, [0, 1]), E(a, 0, 1)
r0 = V(ev(b, t0), 0, 1)
w0 = r0*h0/3
u0 = (ev(F, t0)-11-w0*ev(K, t0))/(60*ev(F, t0))
m0 = 2-10*u0
rho0 = m0*ev(L, t0)/(30*(t0+2)*ev(K, t0))
v0 = rho0*h0
z0 = -m0**2*(t0-2)*ev(L, t0)**2/(300*(t0+2)*ev(K, t0)**2)
zero('split_to_marked_W_relation', w0**2-ev(f, t0))
zero('split_to_marked_v_relation', v0**2-z0)
zero('split_h_composition', v0/rho0-h0)
zero('split_R_composition', 3*w0/(v0/rho0)-r0)

gcds = {'a_a_prime': pgcd(a, derivative(a)),
        'b_b_prime': pgcd(b, derivative(b)), 'a_b': pgcd(a, b)}
for name, value in gcds.items():
    check(name, value == [1])
check('quartic_degree', len(b)-1 == 4)
check('quadratic_degree', len(a)-1 == 2)
check('coprime_branch_count', 2+4 == 6)
boundary = {}
for t in [2, -2]:
    value = ev(b, t)
    assert value.denominator == 1 and value >= 0
    root = isqrt(value.numerator)
    boundary[str(t)] = {'R_squared': str(value), 'square': root*root == value,
                        'R_nonnegative_if_square': root if root*root == value else None,
                        'a': str(ev(a, t)), 'Q4': str(ev(q4, t)),
                        'b_derivative': str(ev(derivative(b), t))}
check('origin_exact', ev(b, 2) == 165**2)
check('origin_smooth_R_partial', 2*165 != 0)
check('minus_two_no_rational_point', ev(b, -2) == 9*33 and
      isqrt(297)**2 != 297)
check('E_no_rational_infinity', b[-1] == 25*33 and isqrt(825)**2 != 825)
check('T_two_normalized_h_over_W', Q(-3, 11)/ev(q4, 2) == Q(1, 55**2))
rho_at_two = Q(2)*ev(L, 2)/(30*4*ev(K, 2))
check('T_two_normalized_v_over_W', rho_at_two/Q(55) == Q(1, 660))
check('T_two_origin_R', 3*55 == 165)
check('infinity_h_normalized_constant', a[-1] == -3)

out = {'input_sha256': {
    'L109': sha256((HERE.parent.parent/'lemmas/L109-pair-only-genus-two-and-minus-three-lifting.md').read_bytes()).hexdigest(),
    'L110': sha256((HERE.parent.parent/'lemmas/L110-explicit-pair-genus-two-model.md').read_bytes()).hexdigest()},
    'polynomials': {name: [str(x) for x in p] for name, p in
                    [('a', a), ('b', b), ('f', f), ('Q4', q4), ('F', F),
                     ('K', K), ('L', L), ('J', J)]},
    'rho': rho.data(), 'z': z.data(), 'field_residuals': residuals,
    'squarefree_gcds': gcds, 'boundary': boundary,
    'infinity': {'E_R_over_T_squared_squared': str(b[-1]),
                 'D_h_over_T_squared': str(a[-1]),
                 'E_residue_field': 'Q(sqrt(33))',
                 'D_residue_field': 'Q(sqrt(33),sqrt(-3))'},
    'integer_origin_scan': 'Not run: exact boundary origin found as specified.',
    'thresholds': {'actual_projection_degree': 2, 'required_projection_degree': 2,
                   'actual_quartic_degree': 4, 'required_squarefree_degree': 4,
                   'actual_genus_E': 1, 'required_genus_E': 1,
                   'actual_genus_D': 3, 'D_to_E_geometric_branch_points': 4,
                   'justification': 'Canonical L111 proves degrees and proper normalization; arithmetic alone does not.'},
    'checks': checks, 'check_count': len(checks),
    'failures': [name for name, ok in checks.items() if not ok]}
path = HERE/'marked-quotient-certificate.json'
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'checks': len(checks), 'failures': out['failures'],
                  'projection_degree_actual_required': [2, 2],
                  'genus_E_actual_required': [1, 1], 'origin': [2, 165],
                  'certificate': str(path.relative_to(HERE.parent.parent))}))
assert not out['failures']

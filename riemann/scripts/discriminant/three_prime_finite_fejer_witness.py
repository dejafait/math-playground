#!/usr/bin/env python3
"""L436: one fixed Fejer witness; exact rational bounds and rounded operation tape.

No floating arithmetic is used. See the canonical proof for convergence,
nonnegativity, coefficient extraction, and the fixed-character application.
"""
from fractions import Fraction as F
from math import isqrt, prod
from pathlib import Path
import json

N = 2**17 - 1  # Selected once from the a priori moment bound, not a degree search.
BITS = 96
UNIT = 2**BITS
checks, local_records, tape = {}, {}, []


def poly_mul(*polys):
    out = [F(1)]
    for poly in polys:
        new = [F(0)] * (len(out) + len(poly) - 1)
        for i, a in enumerate(out):
            for j, b in enumerate(poly):
                new[i+j] += a*b
        out = new
    return out


def local(p):
    # Q_p(u) = K u^3 / product_a (u-a)^m.
    K = -F(p**3*(p-1)**2)
    roots = {F(1): 1, F(p): 2, F(1, p*p): 2, F(p**3): 1}
    parts = {}
    for a, m in roots.items():
        H = K*a**3 / prod((a-b)**mb for b, mb in roots.items() if b != a)
        parts[a] = (H,) if m == 1 else (
            H*(3/a-sum(F(mb)/(a-b) for b, mb in roots.items() if b != a)), H)
    # Verify the entire partial-fraction identity after clearing denominators.
    residual = [F(0)] * 6
    residual[3] = -K
    for a, cs in parts.items():
        for order, coefficient in enumerate(cs, 1):
            factors = [[-b, F(1)] for b, mb in roots.items()
                       for _ in range(mb-(order if b == a else 0))]
            term = poly_mul(*factors)
            for j, value in enumerate(term):
                residual[j] += coefficient*value
    checks[f'p{p}_partial_fraction_identity'] = all(x == 0 for x in residual)
    O, T = parts[F(p)]
    J = parts[F(p**3)][0]
    D = parts[F(1)][0]
    U, V = parts[F(1, p*p)]
    a = F(1, p*p)
    A, B, C = -O/p+T/p**2, T/p**2, -J/p**3
    E, G = U/a-V/a**2, V/a**2
    B0 = A+C
    # Independently compare the convergent valuation constant-term formula.
    delta, z, alpha = 1-F(1, p**5), F(1, p**3), 1-F(1, p)
    s0, s1, s2 = 1/(1-z), z/(1-z)**2, z*(1+z)/(1-z)**3
    independent_B0 = (s0+(delta+alpha)*s1+delta*alpha*s2+z/(1-z))/delta**2
    checks[f'p{p}_B0_matches'] = B0 == independent_B0 > 0
    lo, hi = {2: (141421, 141422), 3: (173205, 173206),
              5: (223606, 223607)}[p]
    lo, hi = F(lo, 100000), F(hi, 100000)
    checks[f'p{p}_radii'] = 1 < lo < hi < p and lo*lo < p < hi*hi
    zp, wp, zm = hi/p, hi/p**3, a/lo
    pos = A/(1-zp)+B*zp/(1-zp)**2+C/(1-wp)
    neg = D/(lo-1)+E*zm/(1-zm)+G*zm/(1-zm)**2
    pm = A*zp/(1-zp)**2+B*zp*(1+zp)/(1-zp)**3+C*wp/(1-wp)**2
    nm = D*lo/(lo-1)**2+E*zm/(1-zm)**2+G*zm*(1+zm)/(1-zm)**3
    S, M = (pos+neg)/B0, (pm+nm)/B0
    sb, mb = {2: (F(103, 10), F(42)), 3: (F(61, 10), F(151, 10)),
              5: (F(39, 10), F(62, 10))}[p]
    checks[f'p{p}_mass_bound'] = 0 < S < sb
    checks[f'p{p}_first_moment_bound'] = 0 < M < mb
    record = {
        'partial_fractions': {str(a): [str(x) for x in cs] for a, cs in parts.items()},
        'cleared_residual': [str(x) for x in residual],
        'positive_coefficients_A_B_C': [str(x) for x in (A, B, C)],
        'negative_coefficients_D_E_G': [str(x) for x in (D, E, G)],
        'B0': str(B0), 'independent_B0': str(independent_B0),
        'radius_lower': str(lo), 'radius_upper': str(hi),
        'normalized_mass_upper_exact': str(S), 'normalized_mass_upper_simple': str(sb),
        'normalized_first_moment_upper_exact': str(M),
        'normalized_first_moment_upper_simple': str(mb),
    }
    return (A, B, C, D, E, G, B0), record


class Interval:
    """Every operation encloses its exact result on the same dyadic grid."""
    def __init__(self, lo, hi=None, op='constant', args=()):
        lo, hi = F(lo), F(lo if hi is None else hi)
        assert lo <= hi
        self.lo = (lo*UNIT).__floor__()
        self.hi = (hi*UNIT).__ceil__()
        self.index = len(tape)
        entry = {'op': op, 'args': list(args), 'lo_units': str(self.lo), 'hi_units': str(self.hi)}
        if op in ('constant', 'sqrt2_bracket'):
            entry['exact_input_bounds'] = [str(lo), str(hi)]
        tape.append(entry)

    @property
    def bounds(self):
        return F(self.lo, UNIT), F(self.hi, UNIT)

    def __add__(self, other):
        a, b = self.bounds
        c, d = other.bounds
        return Interval(a+c, b+d, 'add', (self.index, other.index))

    def __neg__(self):
        a, b = self.bounds
        return Interval(-b, -a, 'negate', (self.index,))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        a, b = self.bounds
        c, d = other.bounds
        values = (a*c, a*d, b*c, b*d)
        return Interval(min(values), max(values), 'multiply', (self.index, other.index))

    def inverse(self):
        a, b = self.bounds
        assert a*b > 0, 'division interval contains zero'
        return Interval(1/b, 1/a, 'inverse', (self.index,))


class Complex:
    def __init__(self, re, im=0):
        self.re = re if isinstance(re, Interval) else Interval(re)
        self.im = im if isinstance(im, Interval) else Interval(im)

    def __add__(self, other):
        return Complex(self.re+other.re, self.im+other.im)

    def __neg__(self):
        return Complex(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Complex(self.re*other.re-self.im*other.im,
                       self.re*other.im+self.im*other.re)

    def inverse(self):
        denom = self.re*self.re+self.im*self.im
        inv = denom.inverse()
        return Complex(self.re*inv, (-self.im)*inv)

    def scale(self, x):
        v = Interval(x)
        return Complex(self.re*v, self.im*v)

    def power(self, n):
        assert n >= 0
        value, base = Complex(1), self
        while n:
            if n % 2:
                value = value*base
            n //= 2
            if n:
                base = base*base
        return value

    def summary(self):
        return {'re': [str(x) for x in self.re.bounds], 'im': [str(x) for x in self.im.bounds],
                'tape_indices': [self.re.index, self.im.index]}


def finite_weighted_sums(z):
    # F_n=sum_(j=0)^n (1-j/(n+1))z^j, G_n=z F_n'(z).
    one = Complex(1)
    inv = (one-z).inverse()
    zn1 = z.power(N+1)
    zn2 = zn1*z
    numerator = Complex(N+1)-z.scale(N+2)+zn2
    f = (numerator*inv*inv).scale(F(1, N+1))
    g = (z*((zn1-one).scale(N+2)*inv*inv
            +numerator*inv*inv*inv.scale(2))).scale(F(1, N+1))
    return f, g


def smoothed_local(p, u, coefficients):
    A, B, C, D, E, G, B0 = coefficients
    fp, gp = finite_weighted_sums(u.scale(F(1, p)))
    fw, _ = finite_weighted_sums(u.scale(F(1, p**3)))
    inverse = u.inverse()
    fm, _ = finite_weighted_sums(inverse)
    ft, gt = finite_weighted_sums(inverse.scale(F(1, p*p)))
    return (fp.scale(A)+gp.scale(B)+fw.scale(C)
            +(fm-Complex(1)).scale(D)+(ft-Complex(1)).scale(E)+gt.scale(G)).scale(1/B0)


coefficients = {}
for p in (2, 3, 5):
    coefficients[p], local_records[str(p)] = local(p)

mass_bounds = [F(local_records[str(p)]['normalized_mass_upper_simple']) for p in (2, 3, 5)]
moment_bounds = [F(local_records[str(p)]['normalized_first_moment_upper_simple']) for p in (2, 3, 5)]
moment_upper = sum(moment_bounds[i]*prod(mass_bounds[j] for j in range(3) if j != i)
                   for i in range(3))
checks['joint_first_moment_upper'] = moment_upper == F(1995293, 1000) < 2000
# L435's independently audited exact negative-point upper bound.
point_upper = -F(2845531063062452632131264, 92613754219265544503359375)
checks['point_upper_below_minus_3_over_100'] = point_upper < -F(3, 100)
apriori_upper = -F(3, 100)+moment_upper/(N+1)
checks['selected_degree_suffices'] = apriori_upper == -F(1936867, 131072000) < -F(1, 100)

root = isqrt(2*UNIT*UNIT)
checks['sqrt2_exact_bracket'] = root*root < 2*UNIT*UNIT < (root+1)*(root+1)
sqrt2 = Interval(F(root, UNIT), F(root+1, UNIT), 'sqrt2_bracket')
points = {2: Complex(1, 1), 3: Complex(1, sqrt2), 5: Complex(1, 2)}
smoothed = {p: smoothed_local(p, points[p], coefficients[p]) for p in (2, 3, 5)}
integral = smoothed[2]*smoothed[3]*smoothed[5]
upper = integral.re.bounds[1]
checks['complete_finite_integral_upper'] = upper < -F(1, 100)
checks['finite_interval_width'] = integral.re.bounds[1]-integral.re.bounds[0] < F(1, 10**20)

# Replay all recorded real interval operations from their integer endpoints.
# The replay checks the certificate independently of its operator dispatch.
replay_failures = []
for i, entry in enumerate(tape):
    op, args = entry['op'], entry['args']
    get = lambda j: (F(int(tape[j]['lo_units']), UNIT), F(int(tape[j]['hi_units']), UNIT))
    if op in ('constant', 'sqrt2_bracket'):
        lo, hi = map(F, entry['exact_input_bounds'])
    elif op == 'add':
        a, b = get(args[0]); c, d = get(args[1]); lo, hi = a+c, b+d
    elif op == 'negate':
        a, b = get(args[0]); lo, hi = -b, -a
    elif op == 'multiply':
        a, b = get(args[0]); c, d = get(args[1]); v = (a*c, a*d, b*c, b*d); lo, hi = min(v), max(v)
    elif op == 'inverse':
        a, b = get(args[0]); assert a*b > 0; lo, hi = 1/b, 1/a
    else:
        raise ValueError(op)
    if not (F(int(entry['lo_units']), UNIT) <= lo <= hi <= F(int(entry['hi_units']), UNIT)):
        replay_failures.append(i)
checks['interval_tape_replay'] = not replay_failures

failures = [key for key, value in checks.items() if not value]
certificate = {
    'scope': 'Complete finite contraction at one fixed degree; proof/nonnegativity and physical transfer are in L436.',
    'degree_each_coordinate': N, 'kernel_terms_each_coordinate': N+1,
    'local': local_records,
    'effective_bound': {'joint_absolute_first_moment_upper': str(moment_upper),
                        'point_upper_imported_L435': str(point_upper),
                        'apriori_integral_upper': str(apriori_upper),
                        'required_integral_upper': '-1/100'},
    'finite_contraction': {'local_smoothed_factors': {str(p): smoothed[p].summary() for p in (2, 3, 5)},
                           'complete_product': integral.summary(),
                           'required_real_upper': '-1/100'},
    'interval_arithmetic': {'bits': BITS, 'sqrt2_floor_units': str(root),
                            'tape': tape, 'replay_failures': replay_failures},
    'checks': checks, 'failures': failures,
}
path = Path(__file__).with_name('three_prime_finite_fejer_witness_certificate.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Exact checks: {sum(checks.values())}/{len(checks)}; failures={failures}')
print(f'Fixed degree n={N}; joint first-moment upper={moment_upper} < 2000.')
print(f'A priori integral upper={apriori_upper}; required < -1/100.')
print('Complete finite integral real interval:', [str(x) for x in integral.re.bounds])
print(f'Full certificate: {path}; interval operations={len(tape)}; replay failures={replay_failures}')
if failures:
    raise SystemExit(1)

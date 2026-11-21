#!/usr/bin/env python3
"""One certified algebraic candidate; no search over slices or new data.

Run: python3 scripts/heat/contact-s7-root-slice-39.py
The selected real root is proved to exist by exact opposite endpoint
signs. Arithmetic modulo its quadratic certifies equalities; rational
intervals certify strict signs. Full evidence is written to disk.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, permutations
from math import factorial, lcm, gcd
from functools import reduce
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'scripts/heat/low-time-h2-uniform-195.json'
OUTPUT = ROOT / 'scripts/heat/contact-s7-root-slice-39.json'
checks = {}


def check(name, value):
    checks[name] = bool(value)


def padd(a, b):
    c = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    while len(c) > 1 and c[-1] == 0: c.pop()
    return c


def pscale(a, k):
    return padd([x*k for x in a], [F(0)])


def pmul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return padd(c, [F(0)])


def peval(a, x):
    v = F(0)
    for c in reversed(a): v = v*x+c
    return v


def imul(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def iadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def display(bounds):
    out = []
    for x, mode in zip(bounds, (ROUND_FLOOR, ROUND_CEILING)):
        with localcontext() as ctx:
            ctx.prec = 10
            ctx.rounding = mode
            out.append(str(Decimal(x.numerator)/Decimal(x.denominator)))
    assert F(out[0]) <= bounds[0] <= bounds[1] <= F(out[1])
    return dict(lower=out[0], upper=out[1])


def midpoint(b):
    x = sum(b)*10**12/2+F(1, 2)
    return F(x.numerator//x.denominator, 10**12)


source_bytes = SOURCE.read_bytes()
panel = json.loads(source_bytes)['panels'][0]
boxes = [(F(panel['moments'][str(2*j)]['lower']),
          F(panel['moments'][str(2*j)]['upper'])) for j in range(7)]
fixed = [midpoint(b) for b in boxes]
check('panel_endpoints', F(panel['lambda']['lower']) == 0
      and F(panel['lambda']['upper']) == F(1, 5120))
check('fixed_mass_positive', fixed[0] > 0)

# Exact formal coefficients in the raw m5 variable X, before quotienting.
yp = [[mj/fixed[0]] if j != 5 else [F(0), 1/fixed[0]]
      for j, mj in enumerate(fixed)]
qp = [pscale(yj, F((-1)**j, factorial(2*j))) for j, yj in enumerate(yp)]
sp = [[F(0)]]
for n in range(1, 7):
    z = pscale(qp[n], -n)
    for k in range(1, n): z = padd(z, pscale(pmul(sp[k], qp[n-k]), -1))
    sp.append(z)
dp = padd(pmul(sp[2], sp[4]), pscale(pmul(sp[3], sp[3]), -1))
check('delta_constant', len(dp) == 1)
check('S5_S6_affine', len(sp[5]) <= 2 and len(sp[6]) <= 2)
P = padd(pmul(dp, sp[6]), pscale(pmul(pmul(sp[4], sp[4]), sp[4]), -1))
P = padd(P, pscale(pmul(pmul(sp[3], sp[4]), sp[5]), 2))
P = padd(P, pscale(pmul(sp[2], pmul(sp[5], sp[5])), -1))
check('contact_polynomial_quadratic', len(P) == 3 and P[2] != 0)
common_denominator = lcm(*(z.denominator for z in P))
integer_coefficients = [int(z*common_denominator) for z in P]
common_factor = reduce(gcd, integer_coefficients)
integer_coefficients = [z//common_factor for z in integer_coefficients]
positive_polynomial_scale = F(common_denominator, common_factor)
check('positive_integer_polynomial_scale', positive_polynomial_scale > 0
      and all(F(integer_coefficients[j]) == P[j]*positive_polynomial_scale for j in range(3)))
initial_lo, initial_hi = boxes[5]
initial_values = [peval(P, initial_lo), peval(P, initial_hi)]
check('initial_opposite_signs', initial_values[0]*initial_values[1] < 0)
if not all(checks.values()):
    raise RuntimeError('Stopped before root construction: '+repr(checks))
lo, hi = initial_lo, initial_hi
# This refines one sign bracket, not a parameter-family sweep.
bisections = 160
for _ in range(bisections):
    mid = (lo+hi)/2
    value = peval(P, mid)
    if value == 0:
        lo = hi = mid
        break
    if value*peval(P, lo) > 0: lo = mid
    else: hi = mid
# Replace the unwieldy bisection endpoints by enclosing terminating
# decimals, then independently recheck signs before using this bracket.
bisected_bracket = [lo, hi]
scale = 10**50
lo = F((lo*scale).numerator//(lo*scale).denominator, scale)
hi_scaled = hi*scale
hi = F(-((-hi_scaled.numerator)//hi_scaled.denominator), scale)
final_values = [peval(P, lo), peval(P, hi)]
check('root_exists_by_IVT', lo == hi and final_values[0] == 0
      or final_values[0]*final_values[1] < 0)
check('root_inside_original_m5_box', initial_lo <= lo <= hi <= initial_hi)

# Every real root alpha in [lo,hi] has alpha^2=A+B*alpha.
# Quotient equality proves identities at all such roots. An inverse is
# used only when its exact conjugate product is nonzero.
A, BB = -P[0]/P[2], -P[1]/P[2]
inverse_records = []


class Q:
    def __init__(self, a=0, b=0):
        if isinstance(a, Q): self.a, self.b = a.a, a.b
        else: self.a, self.b = F(a), F(b)

    def __add__(self, other):
        o = Q(other)
        return Q(self.a+o.a, self.b+o.b)
    __radd__ = __add__

    def __neg__(self): return Q(-self.a, -self.b)
    def __sub__(self, other): return self+-Q(other)
    def __rsub__(self, other): return Q(other)+-self

    def __mul__(self, other):
        o = Q(other)
        return Q(self.a*o.a+self.b*o.b*A,
                 self.a*o.b+self.b*o.a+self.b*o.b*BB)
    __rmul__ = __mul__

    def inverse(self):
        norm = self.a**2+self.a*self.b*BB-self.b**2*A
        if norm == 0: raise ZeroDivisionError('No justified quotient inverse')
        v = Q((self.a+self.b*BB)/norm, -self.b/norm)
        assert self*v == Q(1)
        if self.b:
            inverse_records.append(dict(denominator=self, conjugate_product=norm,
                                        enclosure=self.bounds(), inverse=v))
        return v

    def __truediv__(self, other): return self*Q(other).inverse()
    def __rtruediv__(self, other): return Q(other)*self.inverse()

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = Q(1)
        for _ in range(n): out = out*self
        return out

    def __eq__(self, other):
        o = Q(other)
        return self.a == o.a and self.b == o.b

    def bounds(self): return iadd((self.a, self.a), imul((self.b, self.b), (lo, hi)))


def positive(x): return Q(x).bounds()[0] > 0
def nonnegative(x): return Q(x).bounds()[0] >= 0


def determinant(matrix):
    n, out = len(matrix), Q(0)
    for perm in permutations(range(n)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        term = Q(sign)
        for i in range(n): term = term*matrix[i][perm[i]]
        out += term
    return out


def principal_minors(matrix):
    return {','.join(map(str, ids)): determinant([[matrix[i][j] for j in ids] for i in ids])
            for k in range(1, len(matrix)+1) for ids in combinations(range(len(matrix)), k)}


def matvec(matrix, v): return [sum((a*b for a,b in zip(row,v)), Q(0)) for row in matrix]
def dot(a, b): return sum((x*y for x,y in zip(a,b)), Q(0))


def log_coefficients(y):
    q = [(-1)**j*z/factorial(2*j) for j,z in enumerate(y)]
    s = [Q(0)]
    for n in range(1, len(y)):
        s.append(-n*q[n]-sum((s[k]*q[n-k] for k in range(1,n)), Q(0)))
    return q, s


def independent_log(q):
    def multiply(a, b):
        out = [Q(0) for _ in range(8)]
        for i,x in enumerate(a):
            for j,z in enumerate(b):
                if i+j <= 7: out[i+j] += x*z
        return out
    h = list(q); h[0] = Q(0)
    power = [Q(1)]+[Q(0) for _ in range(7)]
    out = [Q(0) for _ in range(8)]
    for k in range(1,8):
        power = multiply(power, h)
        for n in range(8): out[n] += F((-1)**(k+1), k)*power[n]
    return [-n*out[n] for n in range(8)]


m = [Q(z) if j != 5 else Q(0,1) for j,z in enumerate(fixed)]
y = [z/m[0] for z in m]
q, s = log_coefficients(y)
delta = s[2]*s[4]-s[3]**2
check('delta_positive_before_division', positive(delta))
if not checks['delta_positive_before_division']: raise RuntimeError('Stopped: Delta sign')
p = (s[3]*s[5]-s[4]**2)/delta
r = (s[3]*s[4]-s[2]*s[5])/delta
vector = [p, r, Q(1)]
check('contact_polynomial_exact_zero', sum((P[j]*Q(0,1)**j for j in range(3)), Q(0)) == 0)
check('contact_row3_residual_identity', delta*(p*s[4]+r*s[5]+s[6]) == 0)
membership = {}
for j, (mj, (lower, upper)) in enumerate(zip(m, boxes)):
    membership[str(j)] = dict(m=mj, enclosure=mj.bounds(),
                             lower_slack=mj-lower, upper_slack=upper-mj,
                             relative_box_position=(mj-lower)/(upper-lower))
    check(f'm{j}_in_complete_interval', nonnegative(mj-lower) and nonnegative(upper-mj))
    check(f'common_mass_y{j}', mj == m[0]*y[j])
check('y0_equals_one', y[0] == 1)

W = [[y[i+j+1] for j in range(3)] for i in range(3)]
wminors = principal_minors(W)
for key, z in wminors.items(): check('W_minor_positive_'+key, positive(z))
if not all(positive(z) for z in wminors.values()): raise RuntimeError('Stopped: W positivity')
v = y[4:7]
wd = determinant(W)
av = []
for j in range(3):
    replaced = [row.copy() for row in W]
    for i in range(3): replaced[i][j] = v[i]
    av.append(determinant(replaced)/wd)
y.append(dot(v, av))
check('raw_W_inverse_exact', matvec(W, av) == v)
q, s = log_coefficients(y)
independent = independent_log(q)
check('finite_log_all_coefficients_independent', independent == s)
check('formal_S1_through_S6_match', all(sum((sp[n][j]*Q(0,1)**j for j in range(len(sp[n]))), Q(0)) == s[n] for n in range(1,7)))

M3 = [[y[i+j] for j in range(4)] for i in range(4)]
N3 = [[y[i+j+1] for j in range(4)] for i in range(4)]
H2 = [[s[i+j+2] for j in range(3)] for i in range(3)]
minors = {name:principal_minors(matrix) for name,matrix in [('M3',M3),('N3',N3),('H2',H2)]}
for name, data in minors.items():
    for key, z in data.items(): check(name+'_principal_minor_nonnegative_'+key, nonnegative(z))
for key,z in minors['M3'].items(): check('M3_principal_minor_positive_'+key, positive(z))
check('N3_determinant_exact_zero', determinant(N3) == 0)
check('H2_determinant_exact_zero', determinant(H2) == 0)
null_rows = matvec(H2, vector)
for j,z in enumerate(null_rows): check('H2_null_row_exact_'+str(j), z == 0)
norm = dot(vector, vector)
check('normalization_positive', positive(norm))
products = [[a*b/norm for b in vector] for a in vector]
check('unit_c_exact', sum((products[i][i] for i in range(3)),Q(0)) == 1)
check('c2_nonzero', positive(products[2][2]))
b = {n:sum((products[i][j] for i in range(3) for j in range(3) if i+j == n-2),Q(0)) for n in range(2,7)}
B = (-2*sum((n*(2*n+1)*b[n]*s[n+1] for n in range(2,6)),Q(0))
     +4*sum((n*b[n]*sum((s[k]*s[n+1-k] for k in range(2,n)),Q(0)) for n in range(2,7)),Q(0)))
phi = -156*products[2][2]*s[7]+B
full_flux = sum((b[n]*(-2*n*(2*n+1)*s[n+1]+4*n*sum((s[k]*s[n+1-k] for k in range(1,n+1)),Q(0))) for n in range(2,7)),Q(0))
check('L874_full_heat_flux_identity_exact', phi == full_flux)
check('strict_S2_lower', positive(s[2]-F('3.714e-5')))
check('strict_delta_lower', positive(delta-F('9.7e-16')))
check('strict_delta_upper', positive(F('7.026e-15')-delta))
check('strict_flux_positive', positive(phi))
for j,rec in enumerate(inverse_records):
    check('nonconstant_denominator_separated_'+str(j), rec['enclosure'][0] > 0 or rec['enclosure'][1] < 0)

quantities = {'m5':m[5], 'm6':m[6], 'm5_box_position':membership['5']['relative_box_position'],
              'S2':s[2], 'delta':delta, 'c2_squared':products[2][2], 'Phi':phi, 'y7':y[7]}
compact = {key:display(z.bounds()) for key,z in quantities.items()}
sign_evidence = dict(
    initial_P=[display((z,z)) for z in initial_values],
    final_P=[display((z,z)) for z in final_values],
    membership_slacks={j:{key:display(data[key].bounds()) for key in ('lower_slack','upper_slack')}
                       for j,data in membership.items()},
    W_principal_minors={key:display(z.bounds()) for key,z in wminors.items()},
    principal_minors={name:{key:display(z.bounds()) for key,z in data.items()} for name,data in minors.items()},
    inverse_denominators=[display(rec['enclosure']) for rec in inverse_records],
    norm_squared=display(norm.bounds()), quantities=compact)


def encode(obj):
    if isinstance(obj,Q): return {'a':str(obj.a),'b':str(obj.b)}
    if isinstance(obj,F): return str(obj)
    if isinstance(obj,dict): return {str(k):encode(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)): return [encode(x) for x in obj]
    return obj


failures = [key for key,passed in checks.items() if not passed]
certificate = dict(
    schema='one algebraic contact candidate with exact quadratic reduction and rational sign isolation',
    source=dict(path=str(SOURCE.relative_to(ROOT)), sha256=sha256(source_bytes).hexdigest(),
                panel=0, lambda_interval=panel['lambda'], complete_moment_intervals=panel['moments']),
    root=dict(variable='raw m5', polynomial_low_to_high=P,
              integer_polynomial_low_to_high=integer_coefficients,
              positive_integer_polynomial_scale=positive_polynomial_scale,
              polynomial_construction='Delta*S6-S4^3+2*S3*S4*S5-S2*S5^2',
              formal_q0_through_q6=qp, formal_S1_through_S6=sp[1:],
              initial_bracket=boxes[5], initial_values=initial_values,
              bisected_bracket=bisected_bracket,
              final_bracket=[lo,hi], final_values=final_values, bisections=bisections,
              relation_A=A, relation_B=BB,
              existence='Polynomial continuity and opposite signs; every bracket root satisfies all certified bounds.'),
    construction=dict(fixed_rounded_midpoints=fixed, rounding_denominator=10**12,
                      rule='fix m0..m4,m6 at nearest 10^-12 to exact interval midpoint, half ties upward; solve only m5',
                      m0_through_m6=m, y0_through_y7=y, q0_through_q7=q, S1_through_S7=s[1:],
                      contact_vector_unnormalized=vector, norm_squared=norm,
                      normalized_pair_products=products,
                      c_definition='(p,r,1)/sqrt(norm_squared), positive real square root',
                      raw_v=v, raw_W_inverse_v=av),
    membership=membership, matrices=dict(W=W,M3=M3,N3=N3,H2=H2),
    W_principal_minors=wminors, principal_minors=minors,
    principal_minor_enclosures={name:{key:z.bounds() for key,z in data.items()} for name,data in minors.items()},
    null_rows_unnormalized=null_rows,
    independent_finite_log_residuals=[a-bb for a,bb in zip(s,independent)],
    inverse_records=inverse_records,
    strict_required=dict(S2_lower=F('3.714e-5'),delta_lower=F('9.7e-16'),delta_upper=F('7.026e-15'),Phi_lower=F(0)),
    flux=dict(b2_through_b6=b,B=B,Phi=phi,full_heat_flux=full_flux),
    compact_rational_enclosures=compact, complete_outward_sign_evidence=sign_evidence,
    checks=checks, failures=failures,
    result='CERTIFIED_VIOLATING_FINITE_TUPLE' if not failures else 'INCONCLUSIVE_SINGLE_ROOT_SLICE',
    qualifications=['Finite relaxed tuple only; no actual theta tilt/realization, RH counterexample or complete solution.',
                    'No quadrature, extra moment, box change, coefficient-family sweep or representing-measure converse.',
                    'Raw invertibility proved for this candidate only; singular members of the target class are not excluded.',
                    'Actual-law inclusion retains L917/L037 arithmetic contracts; finite endpoint membership is exact.',
                    'No independent later critical proof audit has yet accepted this certificate.'])
OUTPUT.write_text(json.dumps(encode(certificate),indent=2)+'\n')
print(certificate['result'])
for key,z in compact.items(): print(f'{key}: [{z["lower"]}, {z["upper"]}]')
print('Required: 0<=m5_box_position<=1; S2>3.714e-5; 9.7e-16<delta<7.026e-15; Phi>0')
print('Exact checks:',len(checks),'failures:',failures)
print('Certificate:',OUTPUT.relative_to(ROOT))
raise SystemExit(bool(failures))

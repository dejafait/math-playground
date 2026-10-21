"""Independent exact replay for L087. No construction code is executed.

Read literal source coefficients and certificate witnesses as data. Complete
factor products plus independently checked irreducibility prove exhaustion;
separate Euclidean arithmetic verifies all recorded residue computations.
"""
import ast
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = 13
ZERO, ONE = (), (1,)
checks, evidence = {}, {}


def ck(name, value):
    checks[name] = bool(value)


def poly(values):
    values = [int(c) % P for c in values]
    while values and not values[-1]:
        values.pop()
    return tuple(values)


def plus(*args):
    out = [0] * max((len(a) for a in args), default=0)
    for a in args:
        for i, c in enumerate(a):
            out[i] += c
    return poly(out)


def times(a, b):
    if not a or not b:
        return ZERO
    out = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            out[i+j] += a[i] * b[j]
    return poly(out)


def scale(a, c):
    return poly(c*x for x in a)


def divrem(a, b):
    assert b
    r = list(a)
    q = [0] * max(0, len(a)-len(b)+1)
    while r and len(r) >= len(b):
        k = len(r)-len(b)
        c = r[-1] * pow(b[-1], -1, P) % P
        q[k] = c
        for j in range(len(b)):
            r[k+j] = (r[k+j]-c*b[j]) % P
        while r and not r[-1]:
            r.pop()
    return poly(q), tuple(r)


def rem(a, b):
    return divrem(a, b)[1]


def gcd(a, b):
    while b:
        a, b = b, rem(a, b)
    return scale(a, pow(a[-1], -1, P)) if a else ZERO


def inv(a, f):
    # Extended Euclid, independent of the construction's Fermat inverse.
    r0, r1, s0, s1 = f, rem(a, f), ZERO, ONE
    while r1:
        q, r = divrem(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, plus(s0, scale(times(q, s1), -1))
    assert len(r0) == 1
    out = rem(scale(s0, pow(r0[0], -1, P)), f)
    assert rem(times(a, out), f) == ONE
    return out


def power(a, exponent, f=None):
    result = ONE
    # Left-to-right square/multiply rather than the construction loop.
    for bit in bin(exponent)[2:]:
        result = times(result, result)
        if f:
            result = rem(result, f)
        if bit == '1':
            result = times(result, a)
            if f:
                result = rem(result, f)
    return result


def derivative(a):
    return poly(i*a[i] for i in range(1, len(a)))


def value(a, x, f):
    result = ZERO
    for c in reversed(a):
        result = rem(plus(times(result, x), (c,)), f)
    return result


def listed(a):
    return list(a) if a else [0]


def irreducible(record, name):
    f = poly(record['factor'])
    n = len(f)-1
    ck(name+'_monic', n > 0 and f[-1] == 1)
    x = rem((0, 1), f)
    sequence = [x]
    for _ in range(n):
        sequence.append(power(sequence[-1], P, f))
    primes = [q for q in range(2, n+1)
              if n % q == 0 and all(q % j for j in range(2, q))]
    tests = []
    for q in primes:
        diff = plus(sequence[n//q], (0, -1))
        divisor = gcd(f, diff)
        ck(name+'_rabin_'+str(q), divisor == ONE)
        tests.append(dict(prime=q, remainder_minus_x=listed(diff), gcd=listed(divisor)))
    ck(name+'_frobenius_closure', sequence[-1] == x)
    replay = dict(factor=list(f), degree=n,
                  frobenius_remainders=[listed(v) for v in sequence], gcd_tests=tests)
    ck(name+'_complete_record', replay == record)
    return f, replay


original = json.loads((ROOT/'scripts/primitive-thirteen-two-descent/image-certificate.json').read_text())
source = {}
for node in ast.parse((ROOT/'scripts/five-isogeny-modular-norm/check_norm.py').read_text()).body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        if node.targets[0].id in {'a', 'b1', 'b2', 'h', 'jcoef', 'g'}:
            source[node.targets[0].id] = ast.literal_eval(node.value)
a = poly(source['a'])
b = times(poly(source['b1']), poly(source['b2']))
h = poly(source['h'])
d = power(poly([-16, 1]), 11)
J = plus(scale(a, 2), scale(b, -1))
g = poly(source['g'])
coeff = json.loads((ROOT/'scripts/five-isogeny-modular-norm/norm-certificate.json').read_text())['polynomials_ascending']
for name, computed in dict(a=a, b=b, h=h, d=d, g=g).items():
    ck('source_coefficients_'+name, poly(coeff[name]) == computed)
ck('source_J', J == poly(source['jcoef']))
ck('full_map_identity_mod13', plus(times(a, a), scale(times(a, b), -1),
   scale(times(times(b, b), g), -1), times(d, power(h, 3))) == ZERO)
evidence['source_coefficients_mod13'] = {key: listed(v) for key, v in dict(a=a,b=b,h=h,d=d,J=J,g=g).items()}


def fiber(s):
    return plus(power(h, 3), scale(J, s), scale(d, -s*s))


def reconstruct(f, s, old, name):
    x = rem((0, 1), f)
    bv = value(b, x, f)
    y = rem(times(plus(scale(value(d, x, f), s), scale(value(a, x, f), -1)), inv(bv, f)), f)
    residual = rem(plus(times(y, y), y, scale(value(g, x, f), -1)), f)
    conjugate = rem(plus(value(a, x, f), scale(times(bv, plus(y, ONE)), -1)), f)
    jval = rem(times(scale(value(power(h, 3), x, f), -1), inv(conjugate, f)), f)
    ck(name+'_curve_and_chart', residual == ZERO and jval == poly([s]))
    result = dict(x=listed(x), y=listed(y), curve_residual=listed(residual),
                  regular_conjugate_numerator=listed(conjugate), regular_j_value=listed(jval))
    ck(name+'_reconstruction_record', result == old)
    return result


def characters(f, old, expected, name):
    root = poly(old['sqrt_two']['root'])
    q = P**(len(f)-1)
    ck(name+'_sqrt2_identity', power(root, 2, f) == (2,) and
       old['sqrt_two']['square'] == [2])
    seed = poly(old['sqrt_two']['nonsquare_seed'])
    seed_char = power(seed, (q-1)//2, f)
    ck(name+'_seed_record', seed_char == (12,) and old['sqrt_two']['seed_character'] == [12])
    tables = []
    for r in (root, scale(root, -1)):
        roots = [(8,), plus((-2,), r), plus((-2,), scale(r, -1))]
        vals = [rem(plus((0, 4), scale(t, -1)), f) for t in roots]
        chars = [power(v, (q-1)//2, f) for v in vals]
        ck(name+'_nonzero_characters_'+str(len(tables)), all(vals) and chars == [poly([c]) for c in expected])
        tables.append(dict(sqrt_two=listed(r), theta_residues=[listed(t) for t in roots],
                           values_4x_minus_theta=[listed(v) for v in vals],
                           characters=[listed(c) for c in chars]))
    for key in ('theta_residues', 'values_4x_minus_theta', 'characters'):
        ck(name+'_full_'+key, old[key] == tables[0][key])
    return tables


required_degrees = [[12],[1,1,10],[12],[4,4,4],[1,1,2,2,2,2,2],
                    [4,4,4],[12],[1,1,10],[1,1,10],[12],[4,4,4]]
expected_chars = {1: [1,1,1], 3: [1,1,1], 7: [1,12,12], 10: [1,12,12]}
ck('all_regular_residues_once', [r['scalar_residue'] for r in original['regular_fibers']] == list(range(1,12)))
regular = []
for s, row in enumerate(original['regular_fibers'], 1):
    name = 'regular_'+str(s)
    F = fiber(s)
    ck(name+'_polynomial', F == poly(row['polynomial']) and len(F) == 13 and F[-1] == 1)
    gcds = {key: listed(gcd(F, v)) for key, v in dict(b_gcd=b,d_gcd=d,derivative_gcd=derivative(F)).items()}
    ck(name+'_gcd_records', all(row[key] == v for key, v in gcds.items()))
    ck(name+'_simple_and_b_unit', gcds['derivative_gcd'] == [1] and gcds['b_gcd'] == [1])
    product, fs, results = ONE, [], []
    for index, entry in enumerate(row['factors']):
        label = name+'_factor_'+str(index)
        f, record = irreducible(entry['irreducibility'], label)
        product = times(product, f)
        fs.append(f)
        data = dict(irreducibility=record, reconstruction=reconstruct(f,s,entry['reconstruction'],label))
        if s in expected_chars:
            data['both_sqrt2_character_tables'] = characters(f,entry['two_descent'],expected_chars[s],label)
        results.append(data)
    degrees = [len(f)-1 for f in fs]
    ck(name+'_full_product', product == F)
    ck(name+'_degrees', degrees == row['degrees'] == required_degrees[s-1] and sum(degrees) == 12)
    regular.append(dict(scalar=s, polynomial=list(F), gcds=gcds, degrees=degrees, factors=results))
evidence['regular_fibers'] = regular

g4 = poly([-1264,-640,-64,64])
branches = []
for key, s, degree, mult in [('branch_zero',0,4,3),('branch_1728',12,6,2)]:
    old = original[key]
    f, record = irreducible(old['factor'], key)
    ck(key+'_full_identity', len(f)-1 == degree and power(f,mult) == fiber(s) and old['power_identity'] is True)
    gcds = {key: listed(gcd(f,v)) for key,v in dict(b_gcd=b,d_gcd=d,two_torsion_gcd=g4).items()}
    ck(key+'_all_unit_records', all(old[key] == v == [1] for key,v in gcds.items()))
    result = dict(scalar=s, factor=record, complete_power=list(power(f,mult)), gcds=gcds,
                  reconstruction=reconstruct(f,s,old['reconstruction'],key))
    if s == 0:
        result['both_sqrt2_character_tables'] = characters(f,old['two_descent'],[1,1,1],key)
        ck('hbar_exact', list(f) == [9,10,8,12,1])
    else:
        quotient = (P**12-1)//(P**6-1)
        ck('degree6_even_extension', old['extension_degree_to_U12'] == 2 and
           old['unit_square_exponent_quotient'] == quotient == P**6+1 and quotient % 2 == 0)
        result['even_extension_quotient'] = quotient
        ck('G_exact', list(f) == [10,0,1,12,5,9,1])
    branches.append(result)
evidence['branches'] = branches

# The complete base field is independently checked against L033's literal m.
m = poly([-380,-774,-1062,-456,258,468,104,-126,-6,6,-6,0,1])
n = 12
xs = [rem((0,1),m)]
for _ in range(n):
    xs.append(power(xs[-1],13,m))
tests = [listed(gcd(m,plus(xs[n//q],(0,-1)))) for q in (2,3)]
ck('entire_U12_irreducible', xs[-1] == xs[0] and tests == [[1],[1]])
evidence['base_field'] = dict(polynomial=list(m),frobenius=[listed(v) for v in xs],gcd_tests=tests)

# Directly check the cubic model and discriminants, not just their nonvanishing.
cubic = (-1264,-160,-4,1)
A,B,C = cubic[2],cubic[1],cubic[0]
disc = A*A*B*B-4*B**3-4*A**3*C-27*C*C+18*A*B*C
ck('cubic_discriminant_exact',disc == -256*11**5 and disc % 13 != 0)
b2,b4,b6,b8 = -4,-20,-79,-21
delta = -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
ck('curve_discriminant_exact',delta == -11**5 and delta % 13 != 0)
ck('fixed_cubic_factorization',times(poly([-8,1]),poly([2,4,1])) == poly(cubic) == poly(original['fixed_cubic_mod13']))
ck('sqrt2_genuinely_quadratic',pow(2,6,13) == 12)
evidence['discriminants'] = dict(curve=delta,cubic=disc)

# Explicit differential of the conjugate chart at 2T, in F13.
ev = lambda f,x: sum(c*pow(x,i,13) for i,c in enumerate(f)) % 13
x,y = 3,4
dy = ev(derivative(g),x)*pow(2*y+1,-1,13) % 13
Nprime = (ev(a,x)-ev(b,x)*(y+1)) % 13
dNprime = (ev(derivative(a),x)-ev(derivative(b),x)*(y+1)-ev(b,x)*dy) % 13
hv = ev(h,x)
dj = (-3*hv*hv*ev(derivative(h),x)*Nprime+hv**3*dNprime)*pow(Nprime*Nprime,-1,13) % 13
ck('removable_chart_etale', (y*y+y-ev(g,x)) % 13 == 0 and ev(b,x) != 0 and
   2*y+1 != 0 and Nprime != 0 and (-hv**3*pow(Nprime,-1,13)) % 13 == 9 and dj != 0)
ck('removable_F_simple',ev(fiber(9),x) == 0 and ev(derivative(fiber(9)),x) != 0)
evidence['removable_chart'] = dict(x=x,y=y,dy_dx=dy,Nprime=Nprime,dNprime_dx=dNprime,dj_dx=dj)

# The audited L066 origin formulas: implicit w derivative 1, Q(0,1)=-b10,
# H(0,1)=1. These give u(t)=-t+O(t^2) on the integral formal disk.
ck('origin_leading_coefficients', source['b1'][-1]*source['b2'][-1] == 1 and len(source['a']) == 12 and len(b) == 11)
evidence['origin_lift'] = dict(w_implicit_derivative=1,Q_at_origin=-1,H_at_origin=1,
                            u_linear_coefficient=-1,finite_fiber_degree=12,
                            qualification='Uniform formal inverse and rational-point contradiction proved in L087 audit prose.')

witnesses = []
ck('realization_scalars', [w['scalar'] for w in original['primitive_realizations']] == [1,7])
for old, (s,ar,cr) in zip(original['primitive_realizations'],[(1,7,5),(7,4,7)]):
    ac, ce = Fraction(16*s,1728-s),Fraction(27648,1728-s)
    residues = lambda q: q.numerator*pow(q.denominator,-1,13) % 13
    assertions = dict(cube_root_residue=residues(ac) == ar**3 % 13,
                      eleventh_root_residue=residues(ce) == cr**11 % 13,
                      cube_derivative_unit=3*ar**2 % 13 != 0,
                      eleventh_derivative_unit=11*cr**10 % 13 != 0,
                      same_c_sum=ac+16 == ce, same_c_scalar=1728*ac == s*ce)
    replay = dict(scalar=s,b=2,a_cubed=[ac.numerator,ac.denominator],
                  c_eleventh=[ce.numerator,ce.denominator],a_start=ar,c_start=cr,checks=assertions)
    ck('witness_'+str(s)+'_full_record',replay == old)
    ck('witness_'+str(s)+'_hensel_and_primitive',all(assertions.values()) and residues(ac) != 0 and residues(ce) != 0 and ar % 13 != 0 and cr % 13 != 0 and 2 % 13 != 0)
    witnesses.append(replay)
evidence['primitive_realizations'] = witnesses
ck('reported_sizes_match_verified_lists',original['restricted_image_size_actual'] == 2 and original['unrestricted_image_size_required_comparison'] == 4)
ck('original_base_metadata', original['prime'] == 13 and original['base_field_degree'] == 12)

cert = dict(task='Independent critical audit of L087',
            provenance='No construction code imported or executed; literal L034 source coefficients and stored witnesses only.',
            checks=checks,failures=[k for k,v in checks.items() if not v],evidence=evidence,
            actual_restricted_size=2,required_unrestricted_comparison=4,
            qualification='Finite arithmetic verified here; uniform lifting, field identifications and source applications are proved in the canonical L087 audit. No global independence or integer exclusion.')
out = Path(__file__).with_name('audit-certificate.json')
out.write_text(json.dumps(cert,indent=2)+'\n')
print(f'Independent checks: {sum(checks.values())}/{len(checks)}; failures: {cert["failures"]}')
print('Actual restricted size=2; unrestricted comparison=4; global dimension bounds unchanged.')
print('Certificate:',out.relative_to(ROOT))
if cert['failures']:
    raise SystemExit(1)

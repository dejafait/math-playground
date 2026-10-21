"""Independent complete arithmetic replay for L090; imports no prior code.

Integer coefficients are transcribed from L034's source coefficient input.
Finite polynomial arithmetic is implemented here independently. Uniform
geometry and theorem applicability are audited in L090, not by this script.
"""
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
old = json.loads((HERE / 'image-certificate.json').read_text())
checks = {}
records = {}


def check(name, condition):
    checks[name] = bool(condition)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def neg(a):
    return [-v for v in a]


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i+j] += v*w
    return trim(c)


def red(a):
    return trim([v % 7 for v in a])


def rem(a, f):
    a, f = red(a), red(f)
    while a != [0] and len(a) >= len(f):
        c = a[-1] * pow(f[-1], -1, 7) % 7
        a = red(add(a, [0]*(len(a)-len(f)) + [-c*v for v in f]))
    return a


def power(a, n, f=None):
    r = [1]
    while n:
        if n & 1:
            r = mul(r, a)
            if f is not None:
                r = rem(r, f)
        n //= 2
        if n:
            a = mul(a, a)
            if f is not None:
                a = rem(a, f)
    return r


def gcd(a, b):
    a, b = red(a), red(b)
    while b != [0]:
        a, b = b, rem(a, b)
    return red([v * pow(a[-1], -1, 7) for v in a])


def ev(a, x, f):
    r = [0]
    for v in reversed(a):
        r = rem(add(mul(r, x), [v]), f)
    return r


def scalar(a, x):
    return sum(v*x**i for i, v in enumerate(a))


def irred(rec):
    f = rec['factor']
    n = len(f)-1
    seq = [rem([0, 1], f)]
    for _ in range(n):
        seq.append(power(seq[-1], 7, f))
    primes = [p for p in range(2, n+1) if n % p == 0
              and all(p % d for d in range(2, p))]
    tests = []
    for p in primes:
        z = red(add(seq[n//p], neg([0, 1])))
        tests.append({'prime': p, 'remainder_minus_x': z, 'gcd': gcd(f, z)})
    result = {'factor': f, 'degree': n, 'frobenius_remainders': seq, 'gcd_tests': tests}
    assert result == rec
    assert seq[-1] == seq[0] and all(t['gcd'] == [1] for t in tests)
    return result


A = [-39176677684144739,108160113602504237,74593328129816300,
     420015065507429,-14545268641576841,-1895608370650736,
     576036867160006,82165362766027,2536749758583,19162005343,21559874,743]
B1 = [-707351591,271927184,65058492,1304157,4518,1]
B2 = [-37315543,-37789861,-3406817,3626752,192189,1]
B = mul(B1, B2)
h = [9789217,4971236,1333262,-52820,1]
d = power([-16, 1], 11)
curve = [-20, -10, -1, 1]
g = [-1264, -160, -4, 1]
K = [-380,-774,-1062,-456,258,468,104,-126,-6,6,-6,0,1]
J = add(add(A, A), neg(B))
source = json.loads((HERE.parent / 'five-isogeny-modular-norm/norm-certificate.json').read_text())['polynomials_ascending']
check('all_source_coefficients', all(source[n] == v for n, v in
      [('a', A), ('b1', B1), ('b2', B2), ('b', B), ('g', curve), ('d', d), ('h', h), ('jcoef', J)]))
identity = add(add(mul(A, A), neg(mul(A, B))), add(neg(mul(mul(B, B), curve)), mul(d, power(h, 3))))
check('integer_product_identity', identity == old['integral_map']['integer_product_residual'] == [0])
# Independently recover the coordinate change and cubic discriminant.
check('coordinate_change', add([16], [64*v for v in curve]) == g[:1] + [v*4**i for i, v in enumerate(g) if i > 0])
a, b, c = g[2], g[1], g[0]
disc = a*a*b*b - 4*b**3 - 4*a**3*c - 27*c*c + 18*a*b*c
check('good_reduction_and_maximal_cubic', disc == -256*11**5 and disc % 7 != 0 and old['integral_map']['curve_discriminant'] == -11**5)
check('whole_K_coefficients', old['K_polynomial_mod7'] == red(K) and old['base_field_degrees'] == [12])
check('whole_K_irreducibility', len(old['K_factors']) == 1 and irred(old['K_factors'][0])['factor'] == red(K))
check('fixed_cubic_factorization', red(g) == red(mul([3, 1], [1, 0, 1])) == old['fixed_cubic_mod7'] and pow(6, 3, 7) == 6)
charts = []
for name, y in [('2T', -61), ('3T', 60)]:
    n, nc = scalar(A,16)+scalar(B,16)*y, scalar(A,16)-scalar(B,16)*(1+y)
    charts.append({'point': name, 'y': y, 'N': n, 'N_conjugate': nc,
                   'derivative': 2*y+1, 'residues': [n%7,nc%7,(2*y+1)%7]})
check('complete_x16_charts', charts == old['integral_map']['x16_charts'] and charts[0]['N'] == charts[1]['N_conjugate'] == 0 and charts[1]['N'] == charts[0]['N_conjugate'] == 11**22)
check('cancelled_chart', scalar(h,16) == old['integral_map']['h16'] == 11**8 and Fraction(-scalar(h,16)**3, 11**22) == -121)
qterms = [[23-2*i,11-i,v] for i,v in enumerate(A)] + [[20-2*i,10-i,-v] for i,v in enumerate(B)]
check('all_origin_monomials', qterms == old['integral_map']['origin_Q_terms_t_V_coefficient'] and all(t >= 0 and v >= 0 for t,v,c in qterms) and sum(c for t,v,c in qterms if t == 0) == -1)
check('polar_divisor_data', old['integral_map']['polar_orders'] == [1,11] and old['integral_map']['degree_actual'] == old['integral_map']['degree_required'] == 12 and old['integral_map']['origin_reciprocal_linear_coefficient'] == -1 and old['integral_map']['origin_H'] == '(1-16*t^2*V)^11')
records['integer_map'] = {'identity': identity, 'cubic_discriminant': disc, 'charts': charts, 'origin_monomials': qterms}


def F(s):
    return red(add(add(power(h,3), [s*v for v in J]), [-s*s*v for v in d]))


def reconstruct(f, s):
    x = rem([0,1], f)
    bv = ev(B,x,f)
    bi = power(bv,7**(len(f)-1)-2,f)
    assert rem(mul(bv,bi),f) == [1]
    y = rem(mul(add([s*v for v in ev(d,x,f)],neg(ev(A,x,f))),bi),f)
    residual = rem(add(add(mul(y,y),y),neg(ev(curve,x,f))),f)
    nc = rem(add(ev(A,x,f),neg(mul(bv,add(y,[1])))),f)
    ni = power(nc,7**(len(f)-1)-2,f)
    assert rem(mul(nc,ni),f) == [1]
    j = rem(mul(neg(ev(power(h,3),x,f)),ni),f)
    assert residual == [0] and j == [s]
    return {'x': x, 'y': y, 'curve_residual': residual,
            'conjugate_numerator': nc, 'regular_j_value': j, 'd_value': ev(d,x,f)}


def characters(rec, f, wanted):
    n = len(f)-1
    e = (7**n-1)//2
    I = rec['sqrt_minus_one']
    vals = [red(add([0,4],[-4])),red(add([0,4],neg(I))),red(add([0,4],I))]
    assert power(rec['nonsquare_seed'],e,f) == rec['seed_character'] == [6]
    assert power(rec['nonsquare_seed'],e//2,f) == I
    assert power(I,2,f) == rec['root_square'] == [6]
    assert rec['theta_residues'] == [[4], I, red(neg(I))]
    assert vals == rec['values_4x_minus_theta']
    assert [power(v,e,f) for v in vals] == rec['characters'] == wanted
    conjugates = []
    for j in range(n):
        xj = power([0,1],7**j,f)
        row = []
        for sign in (1,-1):
            vv = [add([4*v for v in xj],[-4]), add([4*v for v in xj],[-sign*v for v in I]),add([4*v for v in xj],[sign*v for v in I])]
            chars = [power(v,e,f) for v in vv]
            assert chars == wanted
            row.append(chars)
        conjugates.append(row)
    return conjugates


regular_records = []
for s,row in enumerate(old['regular_fibers'],1):
    fs = [r['irreducibility']['factor'] for r in row['factors']]
    product = [1]
    for f in fs:
        product = red(mul(product,f))
    check(f'regular_{s}_full_product', row['scalar_residue'] == s and product == row['polynomial'] == F(s))
    deriv = [i*v for i,v in enumerate(F(s))][1:]
    check(f'regular_{s}_all_gcds', gcd(F(s),deriv) == row['derivative_gcd'] == [1] and gcd(B,F(s)) == row['b_gcd'] == [1] and gcd(d,F(s)) == row['d_gcd'])
    rr = []
    for fr in row['factors']:
        irr = irred(fr['irreducibility'])
        reco = reconstruct(irr['factor'],s)
        assert reco == fr['reconstruction']
        rr.append({'irreducibility':irr, 'reconstruction':reco})
    check(f'regular_{s}_complete_records', rr == row['factors'] and row['degrees'] == [len(f)-1 for f in fs] and sum(row['degrees']) == 12)
    entry = {'scalar':s, 'full_factors':rr}
    if s in (2,3):
        entry['all_frobenius_characters_both_orders'] = characters(row['two_descent'], fs[0], [[1],[1],[1]])
        check(f'regular_{s}_all_characters', True)
    regular_records.append(entry)
check('all_five_degree_patterns', [r['degrees'] for r in old['regular_fibers']] == [[1,1,10],[12],[12],[1,1,10],[1,1,10]])
records['regular_fibers'] = regular_records
z = old['branch_zero']
zi = irred(z['factor'])
check('zero_complete_polynomial', zi['factor'] == red(h) and F(0) == red(power(h,3)) == z['polynomial'] and z['power_identity'])
check('zero_all_gcds', gcd(B,h) == z['b_gcd'] == [1] and gcd(d,h) == z['d_gcd'] == [1] and gcd(h,[v*4**i for i,v in enumerate(g)]) == z['two_torsion_gcd'] == [1])
check('zero_reconstruction', reconstruct(red(h),0) == z['reconstruction'])
zc = characters(z['two_descent'],red(h),[[1],[6],[6]])
check('zero_all_characters_and_extension', z['extension_degree_to_U12'] == 3 and z['quadratic_character_exponent_quotient'] == (7**12-1)//(7**4-1) == 5767203)
records['zero_branch'] = {'irreducibility':zi,'all_frobenius_characters_both_orders':zc,'reconstruction':reconstruct(red(h),0)}
r = old['branch_1728']
product = [1]
br = []
for fr in r['factors']:
    br.append(irred(fr))
    product = red(mul(product,fr['factor']))
check('1728_complete_product', product == r['square_factor'] and red(power(product,2)) == r['polynomial'] == F(6) and r['power_identity'])
check('1728_all_gcds', gcd(product,[i*v for i,v in enumerate(product)][1:]) == [1] and gcd(B,product) == r['b_gcd'] == [1] and gcd(d,product) == r['d_gcd'])
check('1728_all_block_degrees', r['coprime_hensel_block_degrees'] == [2*(x['degree']) for x in br] == [2,2,4,4] and max(r['coprime_hensel_block_degrees']) < 12)
records['1728_branch'] = br
choices = old['primitive_ratio_choices']
check('all_primitive_ratio_choices', [x['ratio_unit'] for x in choices] == list(range(1,7)) and all(1 <= x['a_start'] <= 6 and 1 <= x['b_start'] <= 6 and (x['a_start']**3-x['ratio_unit']*x['b_start']**4)%7 == 0 and x['cube_derivative'] == 3*x['a_start']**2%7 != 0 for x in choices))
check('eleventh_unit_bijection', sorted(pow(x,11,7) for x in range(1,7)) == list(range(1,7)))
w0,w1 = old['primitive_realizations']
ac,cc = Fraction(*w0['a_cubed']),Fraction(*w0['c_eleventh'])
check('regular_shared_witness', w0['scalar'] == [2,1] and w0['b'] == 2 and ac == Fraction(16,863) and cc == Fraction(13824,863) and ac+2**4 == cc and 1728*ac == 2*cc)
res = lambda v: v.numerator*pow(v.denominator,-1,7)%7
check('regular_root_conditions', w0['a_start'] == 1 and w0['c_start'] == 5 and res(ac) == 1 and res(cc) == pow(5,11,7) and 3%7 != 0 and 11*5**10%7 != 0)
check('canonical_shared_witness', w1['scalar'] == [9261,8] and w1['a'] == 7 and w1['b_fourth'] == 169 and w1['c_eleventh'] == 512 and 343+169 == 512 and Fraction(1728*343,512) == Fraction(9261,8))
check('canonical_root_conditions', w1['b_start'] == w1['c_start'] == 1 and 169%7 == 512%7 == 1 and 4%7 != 0 and 11%7 != 0 and 9261%7 == 0)
check('image_sizes', old['restricted_image_size_actual'] == 2 and old['unrestricted_image_size_comparison'] == 4)
records['primitive_ratio_choices'] = choices
records['primitive_realizations'] = old['primitive_realizations']
out = {'checks':checks,'failures':[n for n,v in checks.items() if not v],
       'records':records,'bounds':{'full_degree_actual':12,'full_degree_required':12,
       'branch_block_degree_maximum':4,'required_compatible_point_degree':12,
       'restricted_image':2,'unrestricted_image':4},
       'qualification':'Arithmetic replay only; uniform arguments and source applicability audited in L090. No new global restriction.'}
path = HERE / 'audit-certificate.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(f'Independent checks: {sum(checks.values())}/{len(checks)}; failures: {out["failures"]}')
print('All factor, Frobenius, gcd, reconstruction and character records replayed.')
print('Full degree actual/required: 12/12; branch degree at most 4 < required 12.')
print('Image actual/comparison: 2/4; global dimension bounds unchanged.')
print('Certificate:',path.relative_to(HERE.parents[1]))
if out['failures']:
    raise SystemExit(1)

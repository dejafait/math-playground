#!/usr/bin/env python3
"""Independent exact audit of L112; no imports from the producer.

Uses sparse polynomial differentiation and tangent intersection, not the
producer's coefficient tables or general point-addition implementation.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations
import json
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / 'elliptic-rank-witness-certificate.json'
OUT = HERE / 'elliptic-rank-audit-certificate.json'
checks = {}


def test(name, value):
    checks[name] = bool(value)


def poly(cs):
    return {i: Q(c) for i, c in enumerate(cs) if c}


def add(*ps):
    keys = set().union(*ps)
    return {i: v for i in keys if (v := sum(p.get(i, 0) for p in ps))}


def mul(p, q):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            out[i+j] = out.get(i+j, 0) + a*b
    return {i: c for i, c in out.items() if c}


def sc(p, c):
    return {i: c*a for i, a in p.items() if c*a}


def diff(p):
    return {i-1: i*c for i, c in p.items() if i}


def at(p, x):
    return sum(c*x**i for i, c in p.items())


def coeffs(p, degree):
    return [p.get(i, Q(0)) for i in range(degree+1)]


def integer_coeffs(p, degree):
    cs = coeffs(p, degree)
    assert all(c.denominator == 1 for c in cs)
    return [int(c) for c in cs]


def pack(obj):
    if isinstance(obj, Q):
        return {'numerator': obj.numerator, 'denominator': obj.denominator}
    if isinstance(obj, dict):
        return {str(k): pack(v) for k, v in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [pack(v) for v in obj]
    return obj


# Start with L111's factor and its actual twist, not producer input.
f = sc(poly([7, 52, -6, -64, -25]), -33)
e, d, c, b, a = coeffs(f, 4)
I = int(c*c - 3*b*d + 12*a*e)
# The catalecticant determinant is an independent evaluation of J.
mat = [[a,b/4,c/6], [b/4,c/6,d/4], [c/6,d/4,e]]
det = Q(0)
for perm in permutations(range(3)):
    inv = sum(perm[i] > perm[j] for i in range(3) for j in range(i+1,3))
    det += (-1)**inv * mat[0][perm[0]]*mat[1][perm[1]]*mat[2][perm[2]]
assert (432*det).denominator == 1
J = int(432*det)
test('invariants_match_display', (I,J) == (8624880,-46962471600))
qd = 4*I**3-J**2
A0, B0 = -27*I, -27*J
A, B = -2874960, 1739350800
delta0 = -16*(4*A0**3+27*B0**2)
delta = -16*(4*A**3+27*B**2)
test('all_models_nonsingular', qd != 0 and delta0 != 0 and delta != 0)
test('rational_scaling_both_coefficients', A0 == 81*A and B0 == 729*B)
test('discriminant_scaling', delta0 == 3**12*delta)

# Differential expressions expand to Cremona (3.6.4).
fp = diff(f)
h = add(sc(mul(fp,fp),3), sc(mul(f,diff(fp)),-4))
k = sc(add(mul(f,diff(h)),sc(mul(fp,h),-1)),Q(1,3))
test('covariant_degrees', max(h) == 4 and max(k) == 6)
test('g4_display', integer_coeffs(h,4) ==
     [9199872,10349856,31049568,35649504,12074832])
test('g6_display', integer_coeffs(k,6) ==
     [4465387872,-5996016576,-46108608480,-69194537280,
      -48765071520,-15483384576,-1302931872])
syzygy = add(mul(mul(h,h),h),sc(mul(mul(f,f),h),-48*I),
             sc(mul(mul(f,f),f),-64*J),sc(mul(k,k),-27))
test('all_syzygy_coefficients', not syzygy)
test('origin_smooth', at(f,2) == 165**2 and 2*165 != 0)

def residual(point, aa=A, bb=B):
    x,y = point
    return y*y-x**3-aa*x-bb


images = []
for r in [165,-165]:
    image = (3*at(h,2)/Q((2*r)**2),27*at(k,2)/Q((2*r)**3))
    scaled = (image[0]/9,image[1]/27)
    test(f'image_equation_{r}', residual(image,A0,B0) == 0)
    test(f'scaled_equation_{r}', residual(scaled) == 0)
    test(f'image_scaling_inverse_{r}', (9*scaled[0],27*scaled[1]) == image)
    images.append({'quartic_point':[2,r],'original_image':image,'scaled_image':scaled})

# Independently start from the displayed point; intersect its tangent.
x,y = Q(1936),Q(-58564)
P = (x,y)
test('displayed_point_equation', residual(P) == 0)
test('covariant_point_is_displayed', images[0]['scaled_image'] == P)
m = (3*x*x+A)/(2*y)
tangent = poly([y-m*x,m])
cubic = poly([B,A,0,1])
intersection = add(cubic,sc(mul(tangent,tangent),-1))
xthird = m*m-2*x
factorized = mul(mul(poly([-x,1]),poly([-x,1])),poly([-xthird,1]))
intersection_residual = add(intersection,sc(factorized,-1))
test('full_tangent_intersection', not intersection_residual)
double = (xthird,-at(tangent,xthird))
test('double_equation', residual(double) == 0)
test('double_display', double == (Q(149284,121),Q(11160692,1331)))
test('slope_display', m == Q(-786,11))
test('double_affine', 2*y != 0)
test('double_reduced_nonintegral', double[0].denominator == 121 and
     gcd(double[0].numerator,121) == 1)

# Reconstruct every producer field, including each flag's mathematical test.
pc = {
    'quartic_nonsingular':qd != 0, 'original_jacobian_nonsingular':delta0 != 0,
    'full_covariant_syzygy':not syzygy, 'scaled_model_integral':True,
    'scaled_model_nonsingular':delta != 0,
    'discriminant_scaling':delta0 == 3**12*delta,
    'forward_model_scaling':A0 == 81*A and B0 == 729*B,
    'inverse_model_scaling':Q(A0,81) == A and Q(B0,729) == B}
for row in images:
    r = row['quartic_point'][1]
    pc[f'quartic_point_{r}'] = r*r == at(f,2)
    pc[f'covariant_image_{r}'] = residual(row['original_image'],A0,B0) == 0
    pc[f'scaled_image_{r}'] = residual(row['scaled_image']) == 0
    xx,yy = row['scaled_image']
    pc[f'inverse_point_scaling_{r}'] = (9*xx,27*yy) == row['original_image']
pc.update({'multiple_1_on_curve':residual(P) == 0,
           'multiple_2_on_curve':residual(double) == 0,
           'nonintegral_nonzero_multiple_within_cap':2 <= 16 and double[0].denominator > 1,
           'exact_double':checks['double_display'],'exact_tangent':checks['slope_display'],
           'double_x_fraction_reduced':gcd(149284,121) == 1,
           'opposite_images':images[1]['scaled_image'] == (x,-y)})
expected = {
    'target':"Determine whether L111's elliptic quotient has Mordell–Weil rank zero over Q.",
    'inputs':{'L111_sha256':sha256((ROOT/'lemmas/L111-marked-pair-genus-one-quotient.md').read_bytes()).hexdigest()},
    'coefficients_ascending':integer_coeffs(f,4),'I':I,'J':J,
    'quartic_invariant_discriminant':qd,
    'original_jacobian':{'A':A0,'B':B0,'discriminant':delta0},
    'scaling':{'u':3,'forward':'X=u^2*x, Y=u^3*y','inverse':'x=X/u^2, y=Y/u^3'},
    'scaled_jacobian':{'A':A,'B':B,'discriminant':delta},
    'covariants':{'g4':integer_coeffs(h,4),'g6':integer_coeffs(k,6),
                  'syzygy_residual':integer_coeffs(syzygy,12),
                  'g4_at_2':int(at(h,2)),'g6_at_2':int(at(k,2))},
    'images':images,'multiples':[{'n':1,'point':P},{'n':2,'point':double}],'tangent':m,
    'bounds':{'multiples_actual':2,'multiples_cap':16,'search_box_invoked':False,
              'finite_field_counts_invoked':False,'fallback_box':{'m_abs_max':4096,'n_max':64}},
    'conclusion':{'rank_lower_bound':1,'exact_rank':None,'rank_zero':False,
                  'criterion':'Cremona III Proposition 3.3.1: nonintegral nonzero 2P',
                  'quartic_origin_image_need_not_be_identity':True,
                  'marked_lift_or_integer_exclusion_claimed':False},
    'checks':pc,'failures':[name for name,value in pc.items() if not value]}
saved = json.loads(SOURCE.read_text())
encoded = pack(expected)
test('producer_field_set', saved.keys() == encoded.keys())
for field,value in encoded.items():
    test('producer_complete_'+field, saved.get(field) == value)
test('all_recomputed_producer_checks', all(pc.values()))
failures = [name for name,value in checks.items() if not value]
report = {
    'target':"Critically audit L112's exact Jacobian identification and non-torsion certificate.",
    'producer_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
    'independent_reconstruction':encoded,
    'tangent_intersection_residual':integer_coeffs(intersection_residual,3),
    'point_equation_residuals':[residual(P),residual(double)],
    'bounds':{'rank_lower_actual':1,'rank_zero_required':0,
              'double_x_denominator_actual':double[0].denominator,
              'nonintegrality_requires_denominator_greater_than':1,
              'new_point_search':False},
    'checks':checks,'failures':failures}
OUT.write_text(json.dumps(pack(report),indent=2)+'\n')
print(f'audit checks={sum(checks.values())}/{len(checks)}; failures={failures}')
print('complete producer fields compared: 17; rank >= 1 versus rank-zero threshold 0')
print('double x denominator: 121 > 1; no new point search or rank upper bound')
print(f'certificate={OUT.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)

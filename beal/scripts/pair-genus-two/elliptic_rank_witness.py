#!/usr/bin/env python3
"""Exact bounded L111 rank test; standard-library arithmetic only.

Cremona III.3.3 and III.3.6 (3.6.4)--(3.6.8); Fisher (2022) §2.
This is a non-torsion certificate, not an exact-rank computation.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('elliptic-rank-witness-certificate.json')
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def plus(*polys):
    result = [0] * max(map(len, polys))
    for p in polys:
        for i, c in enumerate(p):
            result[i] += c
    return result


def times(p, q):
    result = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return result


def scale(p, c):
    return [c * x for x in p]


def ev(p, t):
    value = 0
    for c in reversed(p):
        value = value * t + c
    return value


def serialize(value):
    if isinstance(value, F):
        return {'numerator': value.numerator, 'denominator': value.denominator}
    if isinstance(value, dict):
        return {k: serialize(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(x) for x in value]
    return value


# Ascending coefficient order throughout.
a, b, c, d, e = 825, 2112, 198, -1716, -231
g = [e, d, c, b, a]
I = 12*a*e - 3*b*d + c*c
J = 72*a*c*e - 27*a*d*d - 27*b*b*e + 9*b*c*d - 2*c**3
quartic_delta = 4*I**3 - J**2
A0, B0 = -27*I, -27*J
delta0 = -16*(4*A0**3 + 27*B0**2)
check('quartic_nonsingular', quartic_delta != 0)
check('original_jacobian_nonsingular', delta0 != 0)
g4 = [3*d*d-8*c*e, 4*(c*d-6*b*e),
      2*(2*c*c-24*a*e-3*b*d), 4*(b*c-6*a*d), 3*b*b-8*a*c]
g6 = [-(d**3+8*b*e*e-4*c*d*e),
      -2*(16*a*e*e+2*b*d*e-4*c*c*e+c*d*d),
      -5*(8*a*d*e+b*d*d-4*b*c*e),
      20*(b*b*e-a*d*d), 5*(8*a*b*e+b*b*d-4*a*c*d),
      2*(16*a*a*e+2*a*b*d-4*a*c*c+b*b*c), b**3+8*a*a*d-4*a*b*c]
g2 = times(g, g)
g3 = times(g2, g)
syzygy_residual = plus(times(times(g4, g4), g4),
                        scale(times(g2, g4), -48*I),
                        scale(g3, -64*J), scale(times(g6, g6), -27))
check('full_covariant_syzygy', all(v == 0 for v in syzygy_residual))

# Keep the original model; use only the explicit invertible scaling u=3.
u = 3
A, B = F(A0, u**4), F(B0, u**6)
check('scaled_model_integral', A.denominator == B.denominator == 1)
A, B = int(A), int(B)
delta = -16*(4*A**3 + 27*B**2)
check('scaled_model_nonsingular', delta != 0)
check('discriminant_scaling', delta0 == u**12 * delta)
check('forward_model_scaling', A0 == u**4*A and B0 == u**6*B)
# Y^2-X^3-A0*X-B0 = u^6*(y^2-x^3-A*x-B),
# and the inverse substitutes x=X/u^2,y=Y/u^3.
check('inverse_model_scaling', F(A0,u**4) == A and F(B0,u**6) == B)


def on_curve(P, aa=A, bb=B):
    return P is None or P[1]**2 == P[0]**3 + aa*P[0] + bb


def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    xx, yy = Q
    if x == xx and y == -yy:
        return None
    slope = (3*x*x+A)/(2*y) if P == Q else (yy-y)/(xx-x)
    xxx = slope*slope-x-xx
    return xxx, slope*(x-xxx)-y


images = []
for r in [165, -165]:
    t = 2
    check(f'quartic_point_{r}', r*r == ev(g,t))
    X = F(3*ev(g4,t), (2*r)**2)
    Y = F(27*ev(g6,t), (2*r)**3)
    check(f'covariant_image_{r}', on_curve((X,Y), A0, B0))
    P = X/u**2, Y/u**3
    check(f'scaled_image_{r}', on_curve(P))
    check(f'inverse_point_scaling_{r}', (u**2*P[0], u**3*P[1]) == (X,Y))
    images.append({'quartic_point':[t,r], 'original_image':[X,Y], 'scaled_image':P})

P = tuple(images[0]['scaled_image'])
multiples = []
Q = None
nonintegral_n = None
for n in range(1,17):
    Q = add(Q,P)
    check(f'multiple_{n}_on_curve', on_curve(Q))
    multiples.append({'n':n, 'point':Q})
    if Q is None:
        break
    if any(x.denominator != 1 for x in Q):
        nonintegral_n = n
        break
check('nonintegral_nonzero_multiple_within_cap', nonintegral_n is not None)
double = add(P,P)
tangent = (3*P[0]**2+A)/(2*P[1])
check('exact_double', double == (F(149284,121), F(11160692,1331)))
check('exact_tangent', tangent == F(-786,11))
check('double_x_fraction_reduced', gcd(149284,121) == 1)
check('opposite_images', images[1]['scaled_image'] == (P[0],-P[1]))

cert = {
    'target': "Determine whether L111's elliptic quotient has Mordell–Weil rank zero over Q.",
    'inputs': {'L111_sha256': sha256((ROOT/'lemmas/L111-marked-pair-genus-one-quotient.md').read_bytes()).hexdigest()},
    'coefficients_ascending':g, 'I':I, 'J':J,
    'quartic_invariant_discriminant':quartic_delta,
    'original_jacobian':{'A':A0,'B':B0,'discriminant':delta0},
    'scaling':{'u':u,'forward':'X=u^2*x, Y=u^3*y','inverse':'x=X/u^2, y=Y/u^3'},
    'scaled_jacobian':{'A':A,'B':B,'discriminant':delta},
    'covariants':{'g4':g4,'g6':g6,'syzygy_residual':syzygy_residual,
                  'g4_at_2':ev(g4,2),'g6_at_2':ev(g6,2)},
    'images':images, 'multiples':multiples, 'tangent':tangent,
    'bounds':{'multiples_actual':len(multiples),'multiples_cap':16,
              'search_box_invoked':False,'finite_field_counts_invoked':False,
              'fallback_box':{'m_abs_max':4096,'n_max':64}},
    'conclusion':{'rank_lower_bound':1,'exact_rank':None,'rank_zero':False,
                  'criterion':'Cremona III Proposition 3.3.1: nonintegral nonzero 2P',
                  'quartic_origin_image_need_not_be_identity':True,
                  'marked_lift_or_integer_exclusion_claimed':False},
    'checks':checks,'failures':[k for k,v in checks.items() if not v]
}
OUT.write_text(json.dumps(serialize(cert),indent=2)+'\n')
print(f'checks={sum(checks.values())}/{len(checks)} failures={cert["failures"]}')
print(f'rank>=1; rank-zero threshold=0; multiples={len(multiples)}/16; search box not invoked')
print('P=(1936,-58564); 2P=(149284/121,11160692/1331) is nonintegral')
print(f'certificate={OUT.relative_to(ROOT)}')
if cert['failures']:
    raise SystemExit(1)

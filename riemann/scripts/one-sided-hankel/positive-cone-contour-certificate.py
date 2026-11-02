"""Exact compact certificate for the positive-cone phase construction.

Adapted from L672's preserved certificate; finite-n/sign transfer is in L673.

No floating arithmetic enters a bound or pass/fail decision. All sampled
values have proved power-series remainders. The separate analytic proof
supplies the interpolation, derivative, and finite-n estimates.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

SCALE = 10**40
SAVE_SCALE = 10**12
DEGREE = 100
d, U, r = Q(5, 4), Q(121, 64), Q(9, 20)
width, height, gamma = Q(3, 50), Q(1, 2), Q(3, 5)
required = -Q(1, 200)
failures = []


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    return (a[0]*b, a[1]*b) if b >= 0 else (a[1]*b, a[0]*b)


def log_unit(v):
    """Exact log enclosure for 1 <= v <= 2 by the atanh series."""
    assert 1 <= v <= 2
    z = (v-1)/(v+1)
    term, total = z, Q(0)
    for j in range(32):
        total += 2*term/(2*j+1)
        term *= z*z
    tail = 2*term/(65*(1-z*z))
    return total, total+tail


LOG2 = log_unit(Q(2))


def logq(v):
    assert v > 0
    k = 0
    while v < 1:
        v *= 2
        k -= 1
    while v > 2:
        v /= 2
        k += 1
    return add(log_unit(v), mul(LOG2, k))


def atan_small(v):
    assert abs(v) <= Q(1, 2)
    term, total = v, Q(0)
    for j in range(60):
        total += term/(2*j+1)
        term *= -v*v
    error = abs(term)/121
    return total-error, total+error


PI = add(mul(atan_small(Q(1, 5)), 16), mul(atan_small(Q(1, 239)), -4))
C_INTERVAL = mul(PI, Q(10, 27))


def atanq(v):
    if v < 0:
        return neg(atanq(-v))
    if v > 1:
        return add(mul(PI, Q(1, 2)), neg(atanq(1/v)))
    if v > Q(1, 2):
        return add(mul(PI, Q(1, 4)), atan_small((v-1)/(v+1)))
    return atan_small(v)


def primitive(s, v):
    assert s >= 0 and s*s+v*v > 0
    result = add(mul(logq(s*s+v*v), v/2), (-v, -v))
    return add(result, mul(atanq(v/s), s)) if s else result


BASE_KERNEL = mul(add(logq(r), (-Q(1), -Q(1))), 2*r)


def kernel(s, y):
    s = abs(s)
    ans = add(BASE_KERNEL, neg(primitive(s, y+r)))
    ans = add(ans, primitive(s, y-r))
    return mul(ans, Q(10, 27))


def floor_scaled(v, scale=SCALE):
    return (v.numerator*scale)//v.denominator


def ceil_scaled(v, scale=SAVE_SCALE):
    return -((-v.numerator*scale)//v.denominator)


def complex_mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def series_fixed(z):
    """Approximate Re sum z^k/[k(k+1)], using exact integer floors."""
    assert z[0]*z[0]+z[1]*z[1] <= Q(81, 100)
    zr, zi = floor_scaled(z[0]), floor_scaled(z[1])
    pr, pi, total = SCALE, 0, 0
    for k in range(1, DEGREE+1):
        nr = (pr*zr-pi*zi)//SCALE
        ni = (pr*zi+pi*zr)//SCALE
        pr, pi = nr, ni
        total += pr//(k*(k+1))
    return total


# Each complex power has coordinate error <=6*((3/2)^k-1)/SCALE.
# Flooring each of DEGREE summands contributes at most DEGREE/SCALE.
round_error = (6*(Q(3, 2)**DEGREE-1)+DEGREE)/SCALE
tail_error = Q(9, 10)**(DEGREE+1)/(Q((DEGREE+1)*(DEGREE+2), 10))
four_series_error = 4*(round_error+tail_error)
assert round_error < Q(1, 10**20)
assert four_series_error < Q(1, 10**6)


def circle_points(den):
    result = []
    for j in range(-den, den+1):
        v = Q(j, den)
        result.append(((1-v*v)/(1+v*v), 2*v/(1+v*v)))
    return result


points = {240: circle_points(240), 30: circle_points(30)}
rows = []
global_upper = None
max_witness = None


def certify_line(kind, s, y, v_den, interpolation_error):
    global global_upper, max_witness
    a = (-d+s, y)
    a2 = a[0]*a[0]+a[1]*a[1]
    inverse_a = (a[0]/a2, -a[1]/a2)
    constant = add(mul(logq(d*d/a2), Q(1, 2)), kernel(s, y))
    constant = add(constant, mul(C_INTERVAL, -s))
    quadratic = -gamma*(s*s-y*y)
    constant = add(constant, (quadratic, quadratic))
    const_upper = constant[1]+four_series_error
    for sign in (-1, 1):
        saved = []
        for index, (ur0, ui) in enumerate(points[v_den]):
            ur = sign*ur0
            uv = (ur, ui)
            z1 = complex_mul(uv, inverse_a)
            z2 = (-ur/d, -ui/d)
            z3 = (-d*ur/U, d*ui/U)
            z4 = complex_mul(a, (ur/U, -ui/U))
            approximation = (series_fixed(z1)-series_fixed(z2)
                             +series_fixed(z3)-series_fixed(z4))
            upper = const_upper+Q(approximation, SCALE)
            saved.append(ceil_scaled(upper))
        sampled_upper = Q(max(saved), SAVE_SCALE)
        certified_upper = sampled_upper+interpolation_error
        row = dict(kind=kind, s=str(s), y=str(y), real_part_sign=sign,
                   v_denominator=v_den, sample_upper_numerators=saved,
                   sample_scale=SAVE_SCALE,
                   sampled_max_upper=str(sampled_upper),
                   interpolation_error=str(interpolation_error),
                   certified_upper=str(certified_upper))
        rows.append(row)
        if global_upper is None or certified_upper > global_upper:
            global_upper = certified_upper
            max_witness = dict(row_index=len(rows)-1,
                               v_numerator=saved.index(max(saved))-v_den,
                               s=str(s), y=str(y), real_part_sign=sign,
                               sampled_max_upper=str(sampled_upper),
                               interpolation_error=str(interpolation_error),
                               certified_upper=str(certified_upper))
        if certified_upper > required:
            failures.append(f'row {len(rows)-1}: contour threshold failed')


# Tensor-product linear interpolation errors: M_y*h_y^2/8+M_v*h_v^2/8.
side_error = Q(17, 8)*Q(1, 100)**2+Q(100, 8)*Q(1, 240)**2
for s in (-width, width):
    for k in range(51):
        certify_line('vertical', s, Q(k, 100), 240, side_error)
    print(f'Vertical side s={s} checked.', flush=True)

# On the top, |d_s^2(F+K-gamma*Re(z^2))|<18.
top_error = Q(18, 8)*Q(1, 50)**2+Q(100, 8)*Q(1, 30)**2
for k in range(7):
    certify_line('horizontal', -width+Q(k, 50), height, 30, top_error)

checks = [
    ('parameter modulus squared < (3/2)^2', (d+width)**2+height**2, '<', Q(9, 4)),
    ('reciprocal parameter modulus < 9/10', 1/(d-width), '<', Q(9, 10)),
    ('parameter/U < 4/5', Q(3, 2)/U, '<', Q(4, 5)),
    ('d/U < 2/3', d/U, '<', Q(2, 3)),
    ('product t derivative < 17', 4+Q(25, 4)+Q(96, 25)+Q(80, 41), '<', Q(17)),
    ('F second y or s derivative < 8', Q(625, 116)+Q(4096, 1875), '<', Q(8)),
    ('vertical K second y derivative < 7', Q(10, 27)/width, '<', Q(7)),
    ('vertical exponent second y derivative < 17', Q(625, 116)+Q(4096, 1875)+Q(10, 27)/width+2*gamma, '<', Q(17)),
    ('horizontal exponent second s derivative < 18', Q(625, 116)+Q(4096, 1875)+Q(10, 27)*(20-Q(20, 19))+2*gamma, '<', Q(18)),
    ('horizontal K second s derivative < 8', Q(10, 27)*(20-Q(20, 19)), '<', Q(8)),
    ('F second v derivative < 100', 4*(2+Q(16, 5)+2+Q(625, 116)+2+Q(16, 5)+Q(6, 5)+Q(4, 3)), '<', Q(100)),
    ('contour maximum < required', global_upper, '<', required),
]
recorded_checks = []
for name, value, relation, bound in checks:
    passed = value < bound
    recorded_checks.append(dict(name=name, actual=str(value), relation=relation,
                                required=str(bound), passed=passed))
    if not passed:
        failures.append(name)

out = Path(__file__).with_suffix('.json')
report = dict(
    kind='exact rational series and integer fixed-point certificate',
    parameters=dict(d=str(d), U=str(U), r=str(r), phase_center='10*pi/27',
                    phase_center_interval=[str(v) for v in C_INTERVAL], gamma=str(gamma),
                    width=str(width), height=str(height)),
    series=dict(degree=DEGREE, scale=SCALE, round_error=str(round_error),
                single_tail_error=str(tail_error), total_error=str(four_series_error),
                log_terms=32, atan_terms=60),
    grids=dict(vertical_y_step='1/100', vertical_v_step='1/240',
               horizontal_s_step='1/50', horizontal_v_step='1/30',
               vertical_interpolation_error=str(side_error),
               horizontal_interpolation_error=str(top_error)),
    sample_count=sum(len(row['sample_upper_numerators']) for row in rows),
    required_upper=str(required), maximum_upper=str(global_upper),
    strict_margin=str(required-global_upper), maximum_witness=max_witness,
    checks=recorded_checks, failures=failures, rows=rows,
    scope='Compact continuum contour inequality only; finite-n transfer, nonnegative coefficients, and distance consequences require L673 proof.')
out.write_text(json.dumps(report, indent=2)+'\n')
print(f'Contour upper bound: {float(global_upper):.12f}; required < {float(required):.12f}')
print(f'Exact upper bound: {global_upper}; strict margin: {required-global_upper}')
print(f'Samples: {report["sample_count"]}; failures: {failures}; certificate: {out}')
if failures:
    raise SystemExit(1)

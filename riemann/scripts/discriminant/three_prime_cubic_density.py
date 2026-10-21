#!/usr/bin/env python3
"""L435 finite exact algebra only; physical limits/convergence are in its proof."""
from fractions import Fraction as F
from pathlib import Path
import json


def add(*polys):
    out = {}
    for poly in polys:
        for degree, value in poly.items():
            out[degree] = out.get(degree, F(0)) + value
    return {degree: value for degree, value in out.items() if value}


def scale(poly, value):
    return {degree: value*coeff for degree, coeff in poly.items() if value*coeff}


def mul(*polys):
    out = {0: F(1)}
    for poly in polys:
        new = {}
        for d, v in out.items():
            for e, w in poly.items():
                new[d+e] = new.get(d+e, F(0)) + v*w
        out = {d: v for d, v in new.items() if v}
    return out


def power(poly, degree):
    return mul(*([poly]*degree))


def serial(poly):
    return {str(d): str(v) for d, v in sorted(poly.items())}


def local(prime):
    p = F(prime)
    one, u = {0: F(1)}, {1: F(1)}
    X = scale(add(u, {-1: p}), F(1, 2))
    iY = scale(add(u, {-1: -p}), F(1, 2))
    f1, fp = add(u, {0: -1}), add(u, {0: -p})
    fp2, fp3 = add(scale(u, p*p), {0: -1}), add({0: p**3}, scale(u, -1))
    A = add({0: p+1}, scale(X, -2))
    B = add({0: p**3+p**(-2)}, scale(X, -2))
    C = add({0: p**3+1}, scale(X, -(p*p+1)))
    iD = scale(iY, p*p-1)
    numerator = scale(power(u, 3), p**7*(p-1)**2)
    denominator = mul(f1, power(fp, 2), power(fp2, 2), fp3)
    circle_num = scale(add(C, iD), p**3*(p-1)**2)
    circle_den = mul(power(A, 2), power(B, 2))
    geometric_residual = add(mul(u, power(fp, 2)), scale(mul(u, f1, fp), -1),
                             scale(mul(u, f1), p-1), scale(u, -(p-1)**2))
    residual = add(mul(numerator, circle_den), scale(mul(circle_num, denominator), -1))
    modulus_residual = add(power(C, 2), scale(power(iD, 2), -1), scale(mul(A, B), -p*p))
    delta, z, a = 1-p**(-5), p**(-3), 1-1/p
    S0, S1, S2 = 1/(1-z), z/(1-z)**2, z*(1+z)/(1-z)**3
    B0 = (S0+(delta+a)*S1+delta*a*S2+z/(1-z))/delta**2
    # At X=1, D is d_times_sqrt_y2 * sqrt(y2).
    C_point, y2 = p**3+1-(p*p+1), p-1
    D_scale = p*p-1
    R_point = p**3*(p-1)**2*C_point/((p-1)**2*(p**3+p**(-2)-2)**2)
    return {
        'geometric_residual': serial(geometric_residual),
        'circle_residual': serial(residual), 'modulus_residual': serial(modulus_residual),
        'Q_numerator': serial(numerator), 'Q_denominator': serial(denominator),
        'circle_numerator': serial(circle_num), 'circle_denominator': serial(circle_den),
        'B0': str(B0), 'point_C': str(C_point), 'point_Y_squared': str(y2),
        'point_D_scale': str(D_scale), 'point_R_over_B0': str(R_point/B0),
    }


records = {str(p): local(p) for p in (2, 3, 5)}
checks = {}
for p, record in records.items():
    for key in ('geometric_residual', 'circle_residual', 'modulus_residual'):
        checks[f'p{p}_{key}_zero'] = not record[key]
    checks[f'p{p}_positive_point_real_factor'] = F(record['point_R_over_B0']) > 0
# Q(sqrt(2)) arithmetic represented as (rational, sqrt(2) coefficient).
def qadd(a, b):
    return a[0]+b[0], a[1]+b[1]

def qmul(a, b):
    return a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0]

ratios = [(F(3,4), F(0)), (F(0), F(4,9)), (F(12,25), F(0))]
pair_sum = (F(0), F(0))
for i, j in ((0,1), (0,2), (1,2)):
    pair_sum = qadd(pair_sum, qmul(ratios[i], ratios[j]))
phase_factor = F(1)-pair_sum[0], -pair_sum[1]
lo, hi = F(7,5), F(10,7)
upper = phase_factor[0]+phase_factor[1]*lo
lower = phase_factor[0]+phase_factor[1]*hi
checks.update({
    'point_C_values': [records[str(p)]['point_C'] for p in (2,3,5)] == ['4','18','100'],
    'phase_factor_exact': phase_factor == (F(16,25), -F(41,75)),
    'sqrt2_lower_squared': lo*lo < 2,
    'sqrt2_upper_squared': hi*hi > 2,
    'factor_upper_negative': upper == -F(47,375) < 0,
    'factor_lower': lower == -F(74,525) < upper,
    'p5_global_C_positive_squared': F(126)**2 > F(26)**2*5,
})
product_R = F(1)
for record in records.values():
    product_R *= F(record['point_R_over_B0'])
point = {
    'u': ['1+i', '1+i*sqrt(2)', '1+2*i'],
    'ratios_D_over_C': ['3/4', '4*sqrt(2)/9', '12/25'],
    'phase_factor': {'rational': str(phase_factor[0]), 'sqrt2_coefficient': str(phase_factor[1])},
    'strict_factor_lower': str(lower), 'strict_factor_upper': str(upper),
    'required_factor_upper': '0', 'positive_real_product': str(product_R),
    'density_exact': {'rational': str(product_R*phase_factor[0]),
                      'sqrt2_coefficient': str(product_R*phase_factor[1])},
    'strict_density_upper': str(product_R*upper),
}
failures = [key for key, value in checks.items() if not value]
certificate = {'scope': 'Finite exact algebra; see L435 for physical transfer, infinite sums and measure argument.',
               'checks': checks, 'failures': failures, 'local': records, 'negative_point': point}
path = Path(__file__).with_name('three_prime_cubic_density_certificate.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Exact checks: {sum(checks.values())}/{len(checks)}; failures={failures}')
print('Full complex phase factor: (48-41*sqrt(2))/75 < -47/375 < 0; required <0.')
print('Normalized density upper bound:', point['strict_density_upper'], '< 0.')
print('Full certificate:', path)
if failures:
    raise SystemExit(1)

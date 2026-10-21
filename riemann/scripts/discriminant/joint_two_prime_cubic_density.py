#!/usr/bin/env python3
"""Exact finite algebra for L434; infinite sums and physical limits are written proofs."""
from fractions import Fraction as F
from pathlib import Path
import json


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: c*v for k, v in p.items() if c*v}


def mul(*ps):
    out = {0: F(1)}
    for p in ps:
        new = {}
        for k, v in out.items():
            for j, w in p.items():
                new[k+j] = new.get(k+j, F(0)) + v*w
        out = {k: v for k, v in new.items() if v}
    return out


def power(p, n):
    return mul(*([p]*n))


def serial(p):
    return {str(k): str(v) for k, v in sorted(p.items())}


def local(p):
    p = F(p)
    u, one = {1: F(1)}, {0: F(1)}
    ubar = {-1: p}
    X = scale(add(u, ubar), F(1, 2))
    iY = scale(add(u, scale(ubar, -1)), F(1, 2))
    f1 = add(u, scale(one, -1))
    fp = add(u, scale(one, -p))
    fp2 = add(scale(u, p*p), scale(one, -1))
    fp3 = add(scale(one, p**3), scale(u, -1))
    geometric = add(mul(u, power(fp, 2)), scale(mul(u, f1, fp), -1),
                    scale(mul(u, f1), p-1), scale(u, -(p-1)**2))
    num = scale(power(u, 3), p**7*(p-1)**2)
    den = mul(f1, power(fp, 2), power(fp2, 2), fp3)
    A = add(scale(one, p+1), scale(X, -2))
    B = add(scale(one, p**3+p**(-2)), scale(X, -2))
    C = add(scale(one, p**3+1), scale(X, -(p*p+1)))
    iD = scale(iY, p*p-1)
    real_num = scale(C, p**3*(p-1)**2)
    complex_num = scale(add(C, iD), p**3*(p-1)**2)
    circle_den = mul(power(A, 2), power(B, 2))
    residual = add(mul(num, circle_den), scale(mul(complex_num, den), -1))
    modulus = add(power(C, 2), scale(power(iD, 2), -1),
                  scale(mul(A, B), -p*p))
    d0, z, a = 1-p**(-5), p**(-3), 1-1/p
    S0, S1, S2 = 1/(1-z), z/(1-z)**2, z*(1+z)/(1-z)**3
    B0 = (S0+(d0+a)*S1+d0*a*S2+z/(1-z))/d0**2
    majorant = 1/((1-p**(-2))**2*(1-p**(-3)))
    # For C=a0-b0 cos(t), D=d sin(t), the squared maximum is d^2/(a0^2-b0^2).
    a0, b0sq, dsq = p**3+1, p*(p*p+1)**2, p*(p*p-1)**2
    ratio_sq = dsq/(a0*a0-b0sq)
    return {
        'geometric_residual': serial(geometric),
        'complex_circle_identity_residual': serial(residual),
        'modulus_identity_residual': serial(modulus),
        'Q_numerator': serial(num), 'Q_denominator': serial(den),
        'circle_complex_numerator_in_u': serial(complex_num),
        'circle_real_numerator_in_u': serial(real_num),
        'circle_denominator_in_u': serial(circle_den),
        'B0': str(B0), 'B0_upper_majorant': str(majorant),
        'phase_ratio_squared': str(ratio_sq),
    }


records = {str(p): local(p) for p in (2, 3)}
checks = {}
for p, record in records.items():
    for key in ('geometric_residual', 'complex_circle_identity_residual', 'modulus_identity_residual'):
        checks[f'p{p}_{key}_zero'] = not record[key]
    checks[f'p{p}_B0_positive_below_majorant'] = 0 < F(record['B0']) < F(record['B0_upper_majorant'])
checks.update({
    'prime2_B0_matches_audited_marginal': records['2']['B0'] == '571520/329623',
    'prime2_phase_ratio_squared': F(records['2']['phase_ratio_squared']) == F(18,31),
    'prime3_phase_ratio_squared': F(records['3']['phase_ratio_squared']) == F(48,121),
    'joint_phase_product_squared_below_quarter': F(18,31)*F(48,121) == F(864,3751) < F(1,4),
    'prime3_B0_majorant_below_two': F(records['3']['B0_upper_majorant']) < 2,
    'sqrt3_less_than_seven_fourths_squared': F(3) < F(49,16),
    'prime3_C_lower_above_ten': 28-10*F(7,4) > 10,
    'prime3_A_upper_below_eight': 4+2*F(7,4) < 8,
    'prime3_B_upper_below_32': 27+F(1,9)+2*F(7,4) < 32,
    'prime3_density_bound_above_1_over_128': F(108)*10/(2*8**2*32**2) > F(1,128),
    'joint_density_bound': F(1,2)*F(8,6075)*F(1,128) == F(1,194400),
})
failures = [k for k, passed in checks.items() if not passed]
certificate = {
    'scope': 'Exact algebra only; L434 proves physical limits, joint convergence, normalization and measure scope.',
    'checks': checks, 'failures': failures, 'local': records,
    'joint_phase_product_squared': '864/3751',
    'density_bound': {'actual_strict_lower': '1/194400', 'required_lower': '0'},
}
path = Path(__file__).with_name('joint_two_prime_cubic_density_certificate.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Exact checks: {sum(checks.values())}/{len(checks)}; failures={failures}')
print('Joint phase product squared: 864/3751 < 1/4; density >1/194400; required >=0.')
print(f'Full certificate: {path}')
if failures:
    raise SystemExit(1)

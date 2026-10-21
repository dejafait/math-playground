"""Original nonintegral-x coverage via t=-x/y; proof in L081.

All roots are certified by a unit derivative and an exact residual in
O_H/64. No completed affine/standard reciprocal enumeration is rerun.
"""
from collections import Counter
from pathlib import Path
import json
import check_arithmetic as a
from check_reciprocal_disks import fixed_theta

HM = 64
HZ = (0,) * 11
HO = (1,) + (0,) * 10


def ha(x, y):
    return tuple((c+d) % HM for c, d in zip(x, y))


def hs(c, x):
    return tuple(c*d % HM for d in x)


def hm(x, y):
    out = [0] * 11
    for i, c in enumerate(x):
        if c:
            for j, d in enumerate(y):
                if d:
                    out[(i+j) % 11] += c*d*(2 if i+j >= 11 else 1)
    return tuple(c % HM for c in out)


def hi(x):
    v = HO
    for _ in range(7):
        v = hm(v, ha(hs(2, HO), hs(-1, hm(x, v))))
    assert hm(x, v) == HO
    return v


def embed(x):
    return tuple(x[i//3] if i % 3 == 0 else 0 for i in range(33))


def t_center(mask):
    out = [0] * 11
    for i in range(1, 15):
        if mask & (1 << i):
            out[i % 11] += 2 ** (i // 11)
    return tuple(c % HM for c in out)


def coefficients(t):
    t2 = hm(t, t)
    t3 = hm(t2, t)
    t4 = hm(t2, t2)
    t6 = hm(t3, t3)
    return t2, ha(hs(10, t4), hs(-1, t3)), hs(20, t6)


def polynomial(v, coeff):
    t2, b, c = coeff
    v2 = hm(v, v)
    f = ha(ha(ha(v, hs(-1, HO)), hm(t2, v)), ha(hm(b, v2), hm(c, hm(v2, v))))
    df = ha(ha(HO, t2), ha(hs(2, hm(b, v)), hs(3, hm(c, v2))))
    return f, df


def root(t):
    coeff = coefficients(t)
    v = HO
    for _ in range(6):
        f, df = polynomial(v, coeff)
        v = ha(v, hs(-1, hm(f, hi(df))))
    f, df = polynomial(v, coeff)
    assert f == HZ and df[0] % 2 == 1
    return v, f, df


def normalized_unit(t, v, k, theta):
    # Embed exact integer coefficient lifts, before any J reduction.
    te, ve = embed(t), embed(v)
    from fractions import Fraction
    q = a.add(ve, a.scale(Fraction(-1, 4),
        a.mul(theta, a.mul(a.mul(te, te, None), a.mul(ve, ve, None), None), None), None), None)
    m = min(0, 6*k-22)
    qn = a.mul(q, a.power(a.RHO, -m, None), None)
    assert all(Fraction(c).denominator == 1 for c in qn)
    unit = tuple(int(c) % 8 for c in qn)
    assert a.valuation(unit) == 0
    return unit, m


def bounds(k):
    beta = min(15+11+k, 30)
    d = min(beta, 15+2*k)
    m = min(0, 6*k-22)
    return {'k': k, 't_square_difference_H': beta, 'root_difference_H': d,
            'q_J_valuation': m, 'relative_difference_J': min(3*d, 3*beta-22)-m}


def main():
    folder = Path(__file__).parent
    affine = json.loads((folder/'affine-certificate.json').read_text())
    theta = fixed_theta()
    histogram, annuli = Counter(), Counter()
    records_path = folder/'parameter-disks.json'
    least_residual = 99
    with records_path.open('w') as stream:
        stream.write('[\n')
        for number, mask in enumerate(range(0, 1 << 15, 2)):
            t = t_center(mask) if mask else tuple(2**(15//11) if i == 15 % 11 else 0 for i in range(11))
            k = (mask & -mask).bit_length()-1 if mask else 15
            v, residual, df = root(t)
            unit, m = normalized_unit(t, v, k, theta)
            nf = a.unit_label(unit)
            label = nf['bits']
            assert str(label) in affine['representative_masks']
            least_residual = min(least_residual, nf['residual_minus_one_valuation_lower_bound'])
            rec = {'t_pi_binary_digits': mask, 'depth_H': 15, 'decision': 'REALIZED',
                   'realization_t_mod_64': t, 'realization_t_valuation_H': k,
                   'v_mod_64': v, 'F_residual_mod_64': residual, 'derivative_mod_64': df,
                   'point': 'v=unique Hensel root; x=1/(t^2*v), y=-1/(t^3*v)',
                   'q_valuation_J': m, 'normalizing_square_rho_exponent': m,
                   'normalized_unit_mod_8': unit, 'normal_form': nf, 'label': label,
                   'affine_representative_mask': affine['representative_masks'][str(label)]}
            if number:
                stream.write(',\n')
            json.dump(rec, stream, separators=(',', ':'))
            histogram[label] += 1
            annuli[k] += 1
        stream.write('\n]\n')
    table = [bounds(k) for k in range(1, 15)]
    checks = {
        'all_parameter_disks_processed': sum(histogram.values()) == 16384,
        'all_middle_annulus_disks_processed': sum(annuli[k] for k in range(1, 12)) == 16376,
        'fixed_theta_matches_existing_certificate': list(theta) == affine['exact_normalizers']['theta'],
        'all_implicit_roots_and_unit_derivatives_verified': True,
        'all_exact_normalizations_integral_units': True,
        'all_normal_forms_reconstructed': True,
        'all_labels_in_existing_image': all(str(label) in affine['representative_masks'] for label in histogram),
        'all_normal_form_residuals_square': least_residual > 66,
        'all_disk_constancy_bounds_strict': min(r['relative_difference_J'] for r in table) > 66,
        'zero_disk_constancy_strict': min(3*30, 6*15-22) == 68 and 68 > 66,
        'root_error_after_denominators_sufficient': 3*66-66 == 132 and 132 >= 99,
        'all_normalizing_exponents_even': all(r['q_J_valuation'] % 2 == 0 for r in table),
        'identity_infinity_label_present': 0 in histogram,
    }
    failures = [name for name, ok in checks.items() if not ok]
    cert = {'purpose': 'exhaustive original nonintegral-x parameter disks, including all middle annuli',
        'inputs': {'parameter': 't=-x/y', 'implicit_equation': 'v-1+t^2*v+(10*t^4-t^3)*v^2+20*t^6*v^3',
                   'kummer_evaluation': 'q=v-(theta/4)*t^2*v^2', 'theta_exact': theta},
        'precision': {'H_modulus': 64, 'H_error': 66, 'conservative_normalized_J_error': 132,
                      'J_modulus': 8, 'J_error': 99, 'square_threshold_J': 66, 'disk_depth_H': 15},
        'constancy_bounds': table, 'zero_disk_relative_error_J': 68,
        'coverage': {'parameter_disks_actual': sum(histogram.values()), 'required': 16384,
                     'middle_annulus_parameter_disks': sum(annuli[k] for k in range(1, 12)),
                     'realized_disks': sum(histogram.values()), 'rejected_parameter_disks': 0,
                     'distinct_labels': len(histogram), 'original_nonintegral_x_exhausted': True,
                     'uncovered_original_x_valuations': 'none after L079 and these parameter disks',
                     'original_x_annuli_odd_negative_valuation': 'empty by 2*v(y)=3*v(x)',
                     'literal_Bruin_Stoll_X_disk_partition': False},
        'parameter_valuation_histogram': {str(k): v for k, v in sorted(annuli.items())},
        'collision_histogram': {str(k): v for k, v in sorted(histogram.items())},
        'exceptions': {'zero_parameter': 'infinity, label 0; zero disk realized also by t=pi^15',
                       'finite_weierstrass': 'none by L078 full cubic field'},
        'disk_records': str(records_path.relative_to(Path.cwd())), 'checks': checks, 'failures': failures}
    path = folder/'parameter-certificate.json'
    path.write_text(json.dumps(cert, indent=2)+'\n')
    print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
    print(f'Parameter disks actual/required: {sum(histogram.values())}/16384; middle disks 16376')
    print(f'Distinct labels: {len(histogram)}; all match L079')
    print(f'Relative constancy J bound/threshold: {min(r["relative_difference_J"] for r in table)}/>66; zero: 68/>66')
    print('Coverage: all original x after L079; parameter partition, not literal cubic-X algorithm trace')
    print(f'Certificates: {path.relative_to(Path.cwd())}; {records_path.relative_to(Path.cwd())}')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()

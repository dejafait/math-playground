"""Replay all implicit roots, disk labels, matches and collisions of L081."""
from collections import Counter
from pathlib import Path
import json
import check_arithmetic as a
from check_parameter_disks import (HZ, HO, ha, hs, hm, t_center,
                                    normalized_unit, bounds)
from check_reciprocal_disks import fixed_theta


def main():
    folder = Path(__file__).parent
    cert = json.loads((folder/'parameter-certificate.json').read_text())
    records = json.loads((folder/'parameter-disks.json').read_text())
    affine = json.loads((folder/'affine-certificate.json').read_text())
    theta = fixed_theta()
    assert cert['inputs']['theta_exact'] == list(theta) == affine['exact_normalizers']['theta']
    seen, histogram, annuli = set(), Counter(), Counter()
    zero_label = None
    for rec in records:
        mask = rec['t_pi_binary_digits']
        assert mask not in seen and mask in range(0, 1 << 15, 2)
        assert rec['depth_H'] == 15 and rec['decision'] == 'REALIZED'
        seen.add(mask)
        t, v = tuple(rec['realization_t_mod_64']), tuple(rec['v_mod_64'])
        k = (mask & -mask).bit_length()-1 if mask else 15
        wanted = t_center(mask) if mask else tuple(2 if i == 4 else 0 for i in range(11))
        assert t == wanted and k == rec['realization_t_valuation_H']
        assert v[0] % 2 == 1
        # Horner substitution, rather than rerunning Newton or trusting its status.
        t2, t3 = hm(t, t), hm(hm(t, t), t)
        t4, t6 = hm(t2, t2), hm(t3, t3)
        b, c = ha(hs(10, t4), hs(-1, t3)), hs(20, t6)
        f = ha(hm(ha(hm(ha(hm(c, v), b), v), ha(HO, t2)), v), hs(-1, HO))
        df = ha(ha(HO, t2), ha(hs(2, hm(b, v)), hs(3, hm(c, hm(v, v)))))
        assert f == HZ == tuple(rec['F_residual_mod_64'])
        assert df == tuple(rec['derivative_mod_64']) and df[0] % 2 == 1
        unit, m = normalized_unit(t, v, k, theta)
        assert tuple(rec['normalized_unit_mod_8']) == unit
        assert m == rec['q_valuation_J'] == rec['normalizing_square_rho_exponent'] and m % 2 == 0
        nf, label = rec['normal_form'], rec['label']
        assert nf['bits'] == label
        digits = [n for n in a.CLASS_DIGITS if label & (1 << a.BIT[n])]
        assert nf['digits'] == digits
        representative = a.ONE
        for n in digits:
            representative = a.mul(representative, a.GENERATORS[n])
        assert tuple(nf['representative']) == representative
        square_root, residual = tuple(nf['square_root_factor']), tuple(nf['residual'])
        assert a.valuation(square_root) == 0
        residual_bound = a.valuation(a.add(residual, a.scale(-1, a.ONE)))
        assert residual_bound == nf['residual_minus_one_valuation_lower_bound'] and residual_bound > 66
        assert unit == a.mul(a.mul(representative, a.mul(square_root, square_root)), residual)
        assert rec['affine_representative_mask'] == affine['representative_masks'][str(label)]
        if mask == 0:
            zero_label = label
        histogram[label] += 1
        annuli[k] += 1
    assert seen == set(range(0, 1 << 15, 2))
    assert cert['constancy_bounds'] == [bounds(k) for k in range(1, 15)]
    assert min(r['relative_difference_J'] for r in cert['constancy_bounds']) == 67
    assert dict(histogram) == {int(k): v for k, v in cert['collision_histogram'].items()}
    assert dict(annuli) == {int(k): v for k, v in cert['parameter_valuation_histogram'].items()}
    assert sum(annuli[k] for k in range(1, 12)) == 16376
    assert zero_label == 0 and cert['zero_disk_relative_error_J'] == 68
    assert cert['coverage']['literal_Bruin_Stoll_X_disk_partition'] is False
    checks = {'fixed_generator_retained': True, 'all_16384_disks_once': True,
              'all_actual_parameter_centers_verified': True, 'all_implicit_polynomials_replayed': True,
              'all_derivatives_units': True, 'all_exact_normalizations_replayed': True,
              'all_full_class_reconstructions_replayed': True, 'all_existing_label_matches_replayed': True,
              'all_collisions_and_annulus_counts_replayed': True, 'all_constancy_bounds_replayed': True,
              'zero_disk_identity_and_infinity': True, 'parameter_partition_scope_retained': True}
    result = {'checks': checks, 'failures': [], 'disks_verified': len(seen),
              'middle_annulus_disks_verified': 16376, 'distinct_labels_verified': len(histogram),
              'actual_required': {'parameter_disks': [len(seen), 16384],
                                  'relative_J_error_and_strict_threshold': [67, 66],
                                  'normalized_arithmetic_J_error_and_required': [132, 99]},
              'scope': 'full stored parameter evidence; not independent audits of L078-L081 or literal X-disk trace'}
    path = folder/'parameter-verification.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Replay checks: {len(checks)}/{len(checks)}; failures: []')
    print(f'Disks actual/required: {len(seen)}/16384; middle disks: 16376; distinct labels: {len(histogram)}')
    print('Constancy actual/strict threshold: 67/>66; normalized arithmetic: 132/99')
    print(f'Certificate: {path.relative_to(Path.cwd())}')


if __name__ == '__main__':
    main()

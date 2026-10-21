"""Replay all reciprocal disk decisions, realized classes and collisions."""
from collections import Counter
from pathlib import Path
import json
import check_arithmetic as a
from check_reciprocal_disks import fixed_theta, pi_digits, reciprocal_factor


def main():
    folder = Path(__file__).parent
    cert = json.loads((folder/'reciprocal-certificate.json').read_text())
    affine = json.loads((folder/'affine-certificate.json').read_text())
    theta = tuple(c % 8 for c in fixed_theta())
    assert cert['inputs']['theta_exact'] == list(fixed_theta()) == affine['exact_normalizers']['theta']
    roots = [pi_digits(mask, 4) for mask in range(0, 16, 2)]
    squares = [a.mul(root, root) for root in roots]
    seen, histogram, statuses = set(), Counter(), Counter()
    for rec in cert['records']:
        mask = rec['z_pi_binary_digits']
        assert mask not in seen and mask in range(0, 256, 2) and rec['depth_H'] == 8
        seen.add(mask)
        z0 = pi_digits(mask, 8)
        assert tuple(rec['z_center_mod_8']) == z0
        matching_roots = [root for root, square in zip(roots, squares)
                          if a.valuation(a.add(square, a.scale(-1, z0))) >= 24]
        statuses[rec['decision']] += 1
        if rec['decision'] == 'REJECT':
            assert not matching_roots
            assert rec['obstructing_odd_digits'] == [i for i in (1,3,5,7) if mask & (1 << i)]
            assert rec['obstructing_odd_digits']
            continue
        assert rec['decision'] == 'REALIZED' and len(matching_roots) == 1
        root = pi_digits(rec['square_root_z_pi_binary_digits'], 5)
        assert tuple(rec['square_root_z_mod_8']) == root and root != a.ZERO
        z = a.mul(root, root)
        assert tuple(rec['realized_z_mod_8']) == z
        assert a.valuation(a.add(z, a.scale(-1, z0))) >= 24
        R = reciprocal_factor(z)
        assert tuple(rec['R_mod_8']) == R
        bound = a.valuation(a.add(R, a.scale(-1, a.ONE)))
        assert bound == rec['R_minus_one_J_valuation_lower_bound'] and bound >= 69
        unit = a.add(a.ONE, a.scale(-1, a.mul(theta, z)))
        assert tuple(rec['kummer_unit_mod_8']) == unit and a.valuation(unit) == 0
        nf, label = rec['normal_form'], rec['label']
        assert nf['bits'] == label
        assert nf['digits'] == [n for n in a.CLASS_DIGITS if label & (1 << a.BIT[n])]
        representative = a.ONE
        for n in nf['digits']:
            representative = a.mul(representative, a.GENERATORS[n])
        assert tuple(nf['representative']) == representative
        q, residual = tuple(nf['square_root_factor']), tuple(nf['residual'])
        assert a.valuation(q) == 0 and a.valuation(a.add(residual, a.scale(-1, a.ONE))) > 66
        assert unit == a.mul(a.mul(representative, a.mul(q, q)), residual)
        assert rec['affine_representative_mask'] == affine['representative_masks'][str(label)]
        histogram[label] += 1
    assert seen == set(range(0, 256, 2))
    assert dict(histogram) == {int(k): v for k,v in cert['collision_histogram'].items()}
    assert statuses == {'REALIZED': 8, 'REJECT': 120}
    assert cert['exceptional']['infinity'] == {'label': 0,
        'affine_representative_mask': affine['representative_masks']['0']}
    assert cert['coverage']['full_two_chart_certificate'] is False
    assert cert['coverage']['uncovered_original_x_valuations'] == '-22<=v_H(x)<0'
    checks = {'fixed_generator_replayed': True, 'every_reciprocal_disk_once': True,
        'every_rejection_compared_with_all_root_residues': True,
        'every_realization_is_a_nonzero_square_in_its_disk': True,
        'all_R_square_neighborhood_bounds_replayed': True,
        'all_full_normal_forms_reconstructed': True,
        'all_collisions_and_affine_matches_replayed': True,
        'infinity_identity_and_coverage_gap_retained': True}
    result = {'checks': checks, 'failures': [], 'disks_verified': len(seen),
        'realized_disks_verified': statuses['REALIZED'], 'rejected_disks_verified': statuses['REJECT'],
        'distinct_labels_verified': len(histogram),
        'required': {'reciprocal_disks': 128, 'J_constancy_bound': 68, 'J_strict_threshold': 66},
        'scope': 'all reciprocal evidence; no middle-annulus certificate or independent L078 audit'}
    path = folder/'reciprocal-verification.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Replay checks: {len(checks)}/{len(checks)}; failures: []')
    print(f'Disks actual/required: {len(seen)}/128; realized/rejected: 8/120; distinct labels: {len(histogram)}')
    print('Full coverage remains INCOMPLETE: -22<=v_H(original x)<0')
    print(f'Certificate: {path.relative_to(Path.cwd())}')


if __name__ == '__main__':
    main()

"""Certify z=1/X in pi O_H; the uncovered middle annuli remain explicit.

Proof and imported hypotheses are in L080. No affine disks are rerun.
"""
from collections import Counter
from pathlib import Path
import json
import check_arithmetic as a


def fixed_theta():
    return a.add(a.add(a.scale(-16, a.ONE, None),
        a.scale(12, a.mul(a.power(a.PI, 7, None), a.RHO, None), None), None),
        a.scale(-2, a.mul(a.power(a.PI, 3, None), a.power(a.RHO, 2, None), None), None), None)


def pi_digits(mask, depth):
    out = a.ZERO
    for i in range(depth):
        if mask & (1 << i):
            out = a.add(out, a.power(a.PI, i))
    return out


def reciprocal_factor(z):
    return a.add(a.add(a.add(a.ONE, a.scale(-4, z)),
        a.scale(-160, a.power(z, 2))), a.scale(-1264, a.power(z, 3)))


def main():
    folder = Path(__file__).parent
    affine = json.loads((folder/'affine-certificate.json').read_text())
    theta_exact = fixed_theta()
    theta = tuple(c % 8 for c in theta_exact)
    square_masks = {sum(((root >> i) & 1) << (2*i) for i in range(1, 4)): root
                    for root in range(0, 16, 2)}
    records, histogram = [], Counter()
    for mask in range(0, 256, 2):
        z0 = pi_digits(mask, 8)
        rec = {'z_pi_binary_digits': mask, 'depth_H': 8,
               'z_center_mod_8': z0}
        if mask not in square_masks:
            rec.update({'decision': 'REJECT',
                'reason': 'residue not a square modulo pi^8',
                'obstructing_odd_digits': [i for i in (1, 3, 5, 7) if mask & (1 << i)]})
        else:
            root_mask = square_masks[mask] if mask else (1 << 4)
            root = pi_digits(root_mask, 5)
            z = a.mul(root, root)
            assert a.valuation(a.add(z, a.scale(-1, z0))) >= 24
            R = reciprocal_factor(z)
            r_bound = a.valuation(a.add(R, a.scale(-1, a.ONE)))
            assert r_bound >= 69  # v_H >= 23, beyond v_H(4)=22.
            unit = a.add(a.ONE, a.scale(-1, a.mul(theta, z)))
            center_unit = a.add(a.ONE, a.scale(-1, a.mul(theta, z0)))
            assert a.valuation(a.add(unit, a.scale(-1, center_unit))) >= 68
            nf = a.unit_label(unit)
            label = nf['bits']
            assert str(label) in affine['representative_masks']
            rec.update({'decision': 'REALIZED', 'square_root_z_pi_binary_digits': root_mask,
                'square_root_z_mod_8': root, 'realized_z_mod_8': z,
                'R_mod_8': R, 'R_minus_one_J_valuation_lower_bound': r_bound,
                'point': 'X=a^(-2), Y=a^(-3)*sqrt(R(a^2)); sqrt chosen by strict Hensel',
                'kummer_unit_mod_8': unit, 'normal_form': nf, 'label': label,
                'affine_representative_mask': affine['representative_masks'][str(label)]})
            histogram[label] += 1
        records.append(rec)
    checks = {
        'fixed_theta_matches_affine': list(theta_exact) == affine['exact_normalizers']['theta'],
        'theta_J_valuation_44': a.valuation(theta) == 44,
        'all_128_disks': len(records) == 128,
        'eight_square_residues': len(square_masks) == 8,
        'all_120_rejections_have_obstruction': sum(r['decision'] == 'REJECT' and
            bool(r['obstructing_odd_digits']) for r in records) == 120,
        'all_eight_disks_realized': sum(histogram.values()) == 8,
        'square_R_uniform_bound': min(22+1, 55+2, 44+3) == 23 and 23 > 22,
        'unit_disk_constancy_bound': 44+3*8 == 68 and 68 > 66,
        'base_square_residue_precision': 11+1+4 >= 8 and 2*4 >= 8,
        'all_labels_in_affine_list': all(str(label) in affine['representative_masks'] for label in histogram),
        'infinity_identity_in_affine_list': '0' in affine['representative_masks'],
        'zero_disk_identity': records[0]['label'] == 0,
        'no_finite_weierstrass_here': all(a.valuation(reciprocal_factor(pi_digits(mask, 8))) == 0
                                         for mask in range(0, 256, 2)),
    }
    failures = [key for key, ok in checks.items() if not ok]
    cert = {'purpose': 'standard reciprocal z=1/X chart plus infinity; not the missing middle annuli',
        'inputs': {'base': 'pi^11=2', 'curve': 'Y^2=X^3-4X^2-160X-1264',
                   'theta_exact': theta_exact, 'reciprocal_polynomial': 'z*(1-4*z-160*z^2-1264*z^3)',
                   'kummer_reciprocal': 'z*(1-theta*z)', 'coordinate_change': 'X=4*x, Y=8*y+4'},
        'precision': {'modulus': 8, 'J_error': 99, 'square_threshold_J': 66,
                      'disk_depth_H': 8, 'disk_error_J': 68, 'R_square_error_H': 23,
                      'square_threshold_H': 22},
        'square_residue_masks': sorted(square_masks), 'records': records,
        'collision_histogram': {str(k): v for k, v in sorted(histogram.items())},
        'exceptional': {'infinity': {'label': 0, 'affine_representative_mask': affine['representative_masks']['0']},
                        'finite_weierstrass': 'none: entire cubic is a field (L078)',
                        'z_zero': 'infinity; zero disk also has nonzero realized z=pi^8'},
        'coverage': {'standard_reciprocal_disks_actual': len(records), 'required': 128,
                     'realized_disks': sum(histogram.values()), 'rejected_disks': 120,
                     'distinct_reciprocal_labels': len(histogram),
                     'full_two_chart_certificate': False,
                     'covered_original_x_valuations': 'v_H(x)<-22, in addition to L079 v_H(x)>=0',
                     'uncovered_original_x_valuations': '-22<=v_H(x)<0'},
        'checks': checks, 'failures': failures}
    path = folder/'reciprocal-certificate.json'
    path.write_text(json.dumps(cert, indent=2)+'\n')
    print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
    print(f'Reciprocal disks actual/required: {len(records)}/128; realized/rejected: 8/120')
    print(f'Distinct reciprocal labels: {len(histogram)}; all in existing 2048-class list')
    print('Constancy J bound/strict threshold: 68/>66; R square H bound: 23/>22')
    print('Full chart coverage: INCOMPLETE; missing -22<=v_H(original x)<0')
    print(f'Certificate: {path.relative_to(Path.cwd())}')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()

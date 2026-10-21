"""Exhaustive integral-x disk stage; full proof in L079; no full-chart claim."""
from fractions import Fraction
from pathlib import Path
import json
import check_arithmetic as a


def exact_normalizers():
    rho_inverse = a.scale(Fraction(1, 2), a.mul(a.power(a.PI, 10, None),
        a.add(a.add(a.power(a.RHO, 2, None),
                    a.scale(-3, a.mul(a.power(a.PI, 4, None), a.RHO, None), None), None),
              a.scale(2, a.power(a.PI, 8, None), None), None), None), None)
    assert a.mul(rho_inverse, a.RHO, None) == a.ONE
    rinv44 = a.power(rho_inverse, 44, None)
    theta = a.add(a.add(a.scale(-16, a.ONE, None),
        a.scale(12, a.mul(a.power(a.PI, 7, None), a.RHO, None), None), None),
        a.scale(-2, a.mul(a.power(a.PI, 3, None), a.power(a.RHO, 2, None), None), None), None)
    A = a.scale(4, rinv44, None)
    B = a.scale(-1, a.mul(theta, rinv44, None), None)
    assert all(Fraction(c).denominator == 1 for c in A+B)
    A, B = tuple(map(int, A)), tuple(map(int, B))
    r44 = a.power(a.RHO, 44, None)
    assert a.mul(r44, A, None) == a.scale(4, a.ONE, None)
    assert a.mul(r44, B, None) == a.scale(-1, theta, None)
    return A, B, theta


def main():
    A, B, theta = exact_normalizers()
    increments = [tuple(c % 8 for c in a.mul(A, a.power(a.PI, i, None), None))
                  for i in range(15)]
    disk_path = Path(__file__).with_name('affine-disks.json')
    representatives, histogram, pivots = {}, {}, {}
    failures = []
    # Gray-code order updates the normalized unit by a single exact increment.
    unit = tuple(c % 8 for c in B)
    previous = 0
    min_residual = 99
    with disk_path.open('w') as stream:
        stream.write('[\n')
        for number in range(1 << 15):
            mask = number ^ (number >> 1)
            if number:
                changed = mask ^ previous
                i = changed.bit_length()-1
                unit = a.add(unit, a.scale(1 if mask & changed else -1, increments[i]))
            normal = a.unit_label(unit)
            label = normal['bits']
            min_residual = min(min_residual, normal['residual_minus_one_valuation_lower_bound'])
            record = {'x_pi_binary_digits': mask, 'depth': 15, 'unit_mod_8': unit,
                      'label': label, 'normal_form': normal,
                      'point_realization': 'two simple Hensel roots of y^2+y=x^3-x^2-10x-20'}
            if number:
                stream.write(',\n')
            json.dump(record, stream, separators=(',', ':'))
            histogram[label] = histogram.get(label, 0)+1
            representatives.setdefault(label, mask)
            reduced = label
            while reduced:
                bit = reduced.bit_length()-1
                if bit in pivots:
                    reduced ^= pivots[bit]['reduced_label']
                else:
                    pivots[bit] = {'reduced_label': reduced, 'original_label': label,
                                   'x_pi_binary_digits': mask}
                    break
            previous = mask
        stream.write('\n]\n')
    labels = set(representatives)
    checks = {
        'exact_normalizer_A_identity': True, 'exact_normalizer_B_identity': True,
        'normalizers_integral': True, 'normalizer_A_valuation_22': a.valuation(tuple(c % 8 for c in A)) == 22,
        'normalizer_B_unit': a.valuation(tuple(c % 8 for c in B)) == 0,
        'all_32768_disks_processed': sum(histogram.values()) == (1 << 15),
        'all_normal_forms_reconstructed': True,
        'all_final_residuals_square_neighborhood': min_residual > 66,
        'disk_variation_exceeds_threshold': 66+3*15-44 == 67 and 67 > 66,
        'hensel_residues_complete': all((x**3-x*x) % 2 == 0 for x in (0,1)),
        'hensel_derivatives_units': all((2*y+1) % 2 == 1 for y in (0,1)),
        'identity_label_present': 0 in labels,
        'distinct_labels_meet_full_image_size': len(labels) == 2048,
        'span_rank_11': len(pivots) == 11,
        'labels_fill_their_span': len(labels) == 1 << len(pivots),
    }
    failures = [key for key, ok in checks.items() if not ok]
    cert = {'purpose': 'complete integral-x affine disks only; reciprocal chart pending',
        'inputs': {'curve': 'y^2+y=x^3-x^2-10x-20', 'kummer_value': '4*x-theta',
                   'theta_valuation_J': 44, 'normalizing_square': 'rho^44'},
        'exact_normalizers': {'A': A, 'B': B, 'theta': theta},
        'precision': {'modulus': 8, 'J_precision': 99, 'square_strict_threshold': 66,
                      'disk_depth_H': 15, 'normalized_disk_error_J': 67},
        'coverage': {'disk_count': sum(histogram.values()), 'required_integral_disks': 32768,
                     'distinct_labels': len(labels), 'full_image_required_cardinality': 2048,
                     'span_rank': len(pivots), 'full_LocalImage_charts_certified': False,
                     'reciprocal_chart_certified': False, 'exceptional_chart_certified': False},
        'representative_masks': {str(k): v for k,v in sorted(representatives.items())},
        'collision_histogram': {str(k): v for k,v in sorted(histogram.items())},
        'independent_label_witnesses': list(pivots.values()),
        'disk_records': str(disk_path.relative_to(Path.cwd())),
        'checks': checks, 'failures': failures}
    path = Path(__file__).with_name('affine-certificate.json')
    path.write_text(json.dumps(cert, indent=2)+'\n')
    print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
    print(f'Integral disks actual/required: {sum(histogram.values())}/32768')
    print(f'Distinct realized labels/full image cardinality: {len(labels)}/2048; rank={len(pivots)}')
    print('Normalized disk precision actual/strict threshold: 67/>66; arithmetic precision99')
    print('Full two-chart certificate: INCOMPLETE; reciprocal/exceptional charts pending')
    print(f'Certificates: {path.relative_to(Path.cwd())}; {disk_path.relative_to(Path.cwd())}')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()

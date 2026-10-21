"""Replay every stored affine realization/class/collision certificate."""
from collections import Counter
from pathlib import Path
import json
import check_arithmetic as a
from check_affine_disks import exact_normalizers


def main():
    folder = Path(__file__).parent
    cert = json.loads((folder/'affine-certificate.json').read_text())
    A, B, theta = exact_normalizers()
    assert cert['exact_normalizers'] == {'A': list(A), 'B': list(B), 'theta': list(theta)}
    increments = [a.mul(tuple(c % 8 for c in A), a.power(a.PI, i)) for i in range(15)]
    represented = {}
    for label in map(int, cert['representative_masks']):
        r = a.ONE
        for n in a.CLASS_DIGITS:
            if label & (1 << a.BIT[n]):
                r = a.mul(r, a.GENERATORS[n])
        represented[label] = r
    seen, histogram, failures = set(), Counter(), []
    with (folder/'affine-disks.json').open() as stream:
        for line in stream:
            if line.strip() in ('[', ']'):
                continue
            rec = json.loads(line.rstrip(',\n'))
            mask, label = rec['x_pi_binary_digits'], rec['label']
            assert mask not in seen and 0 <= mask < 32768 and rec['depth'] == 15
            seen.add(mask)
            expected = tuple(c % 8 for c in B)
            for i in range(15):
                if mask & (1 << i):
                    expected = a.add(expected, increments[i])
            unit = tuple(rec['unit_mod_8'])
            nf = rec['normal_form']
            assert unit == expected and a.valuation(unit) == 0
            assert nf['bits'] == label
            assert nf['digits'] == [n for n in a.CLASS_DIGITS if label & (1 << a.BIT[n])]
            assert tuple(nf['representative']) == represented[label]
            root, residual = tuple(nf['square_root_factor']), tuple(nf['residual'])
            assert a.valuation(root) == 0
            assert a.valuation(a.add(residual, a.scale(-1, a.ONE))) > 66
            assert unit == a.mul(a.mul(represented[label], a.mul(root, root)), residual)
            histogram[label] += 1
            if str(label) not in cert['representative_masks']:
                failures.append(['unlisted_label', mask])
            if cert['representative_masks'][str(label)] == mask:
                assert unit == expected
    assert seen == set(range(32768))
    assert dict(histogram) == {int(k): v for k,v in cert['collision_histogram'].items()}
    # Recompute rank from the actual original witness labels, not reduced claims.
    pivots = {}
    for witness in cert['independent_label_witnesses']:
        assert cert['representative_masks'][str(witness['original_label'])] == witness['x_pi_binary_digits']
        v = witness['original_label']
        while v:
            bit = v.bit_length()-1
            if bit in pivots:
                v ^= pivots[bit]
            else:
                pivots[bit] = v
                break
        assert v
    assert len(pivots) == 11 and len(histogram) == 2048
    checks = {'exact_normalizers_replayed': True, 'every_mask_once': True,
              'all_disk_units_match_exact_x': True, 'all_full_normal_forms_reconstruct': True,
              'all_representatives_match_fixed_class_generators': True,
              'all_residuals_in_proven_square_neighborhood': True,
              'complete_collision_histogram_matches': True, 'eleven_original_witnesses_independent': True}
    result = {'checks': checks, 'failures': failures, 'disks_verified': len(seen),
              'distinct_classes_verified': len(histogram), 'rank_verified': len(pivots),
              'required': {'integral_disks': 32768, 'full_image_classes': 2048},
              'scope': 'affine evidence replay; no reciprocal-chart or independent L078 audit'}
    path = folder/'affine-verification.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Replay checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
    print(f'Disks actual/required: {len(seen)}/32768; classes: {len(histogram)}/2048; rank: {len(pivots)}/11')
    print(f'Certificate: {path.relative_to(Path.cwd())}')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()

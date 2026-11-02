"""Exact-rational coverage and aggregate checks, without rerunning quadrature.

This checks every stored cell, its parameter domain and the final sums.
It does not independently recompute theta, exponential or trig enclosures.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def pair(v):
    lo, hi = map(F, v)
    assert lo <= hi
    return lo, hi


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def multiply(a, b):
    corners = [x*y for x in a for y in b]
    return min(corners), max(corners)


def main():
    directory = Path(__file__).parent
    path = directory/'first-period-certificate.json'
    with path.open() as stream:
        c = json.load(stream)
    a = pair(c['arithmetic']['endpoint_A'])
    d = pair(c['arithmetic']['outer_width'])
    td = pair(c['arithmetic']['tail_width'])
    n, m = c['caps']['outer_cells'], c['caps']['tail_midpoint_cells']
    assert contains(d, (a[0]/n, a[1]/n))
    assert contains(td, ((8-a[1])/m, (8-a[0])/m))
    head = c['cells']['head']
    tail = c['cells']['tail']
    assert len(head) == n and len(tail) == m
    sums = {name: [F(0), F(0)] for name in ('layer', 'remainder', 'raw', 'head_mass')}
    for i, row in enumerate(head):
        boxes = list(map(pair, row))
        assert len(boxes) == 14
        cell, k = boxes[:2]
        assert contains(cell, (a[0]*i/n, a[1]*(i+1)/n))
        assert 0 <= cell[0] <= cell[1] <= 8 and k[0] > 0
        for name, box in [('layer', boxes[11]), ('remainder', boxes[12]),
                          ('raw', boxes[13]), ('head_mass', k)]:
            contribution = multiply(d, box)
            sums[name][0] += contribution[0]
            sums[name][1] += contribution[1]
    enc = c['enclosures']
    for name, key in [('layer', 'integrated_layer_raw'),
                      ('remainder', 'integrated_remainder_raw'),
                      ('raw', 'Z_squared_integral_G'),
                      ('head_mass', 'one_sided_head_mass')]:
        assert contains(pair(enc[key]), sums[name]), f'Exact aggregate failure: {key}'
    tail_sums = [[F(0), F(0)], [F(0), F(0)]]
    for j, row in enumerate(tail):
        cell, mid = pair(row[0]), pair(row[1])
        left_min = a[0]*(m-j)/m + F(8*j, m)
        right_max = a[1]*(m-j-1)/m + F(8*(j+1), m)
        assert contains(cell, (left_min, right_max))
        assert contains(cell, mid) and 0 <= cell[0] <= cell[1] <= 8
        for which, index in enumerate((7, 8)):
            part = pair(row[index])
            tail_sums[which][0] += part[0]
            tail_sums[which][1] += part[1]
    for which, key, allowance in [(0, 'H_A', 'H_spatial_tail_upper'),
                                   (1, 'one_sided_tail_mass', 'one_sided_mass_spatial_tail_upper')]:
        tail_sums[which][1] += F(c['error_budget'][allowance])
        assert contains(pair(enc[key]), tail_sums[which]), key
    z = pair(enc['Z'])
    hm, tm = pair(enc['one_sided_head_mass']), pair(enc['one_sided_tail_mass'])
    assert contains(z, (2*(hm[0]+tm[0]), 2*(hm[1]+tm[1]))) and z[0] > 0
    raw = pair(enc['Z_squared_integral_G'])
    normalized = pair(enc['integral_G'])
    assert raw[0] > 0
    assert contains(normalized, (raw[0]/(z[1]**2), raw[1]/(z[0]**2)))
    assert F(c['error_budget']['total_normalized_radius_upper']) >= (normalized[1]-normalized[0])/2
    for name, flagset in c['runtime']['signals'].items():
        assert not any(value for key, value in flagset.items() if key not in ('Rounded', 'Inexact')), name
    assert c['telemetry']['head_cells_completed'] == n
    assert c['telemetry']['tail_cells_completed'] == m
    assert c['telemetry']['kernel_calls_by_order'] == [m, n, m]
    assert hashlib.sha256((directory/'certify.py').read_bytes()).hexdigest() == c['sources']['core_sha256']
    assert hashlib.sha256((directory/'first_period.py').read_bytes()).hexdigest() == c['sources']['script_sha256']
    output = directory/'first-period-certificate-check.json'
    report = {'status': 'EXACT_RATIONAL_DOMAIN_AND_AGGREGATE_CHECK_PASS',
              'head_cells_checked': n, 'tail_cells_checked': m,
              'integral_G': enc['integral_G'], 'required_upper_bound': '0',
              'selected_negative_test_passed': False,
              'actual_lower_bound': enc['integral_G'][0], 'failures': [],
              'scope': 'Every saved parameter cell and exact rational sum/normalization; no quadrature rerun or independent theta/trig audit',
              'certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    print(f'Check artifact: {output}')


if __name__ == '__main__':
    main()

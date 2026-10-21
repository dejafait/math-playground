"""Audit all saved root/weight records and all 898 comparison bounds.

This recomputes signs, weights, panels and comparisons, not transform sums.
The transform enclosures rely on the generating script's outward arithmetic.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from check_stored_fourier_enclosure import (
    I, S, ONE, TWO, DEGREE, legendre, sign_at, rho, arctan_enclosure,
    compare_component, record, upper_display, Integrals)


def interval(row):
    return I(int(row['lo']), int(row['hi']))


def main():
    source = Path(__file__).with_name('stored-fourier-enclosure-certificate.json')
    data = json.loads(source.read_text())
    assert data['scale'] == str(S) and data['degree'] == DEGREE and data['cutoff'] == 112
    pi = I.rational(16)*arctan_enclosure(F(1, 5))-I.rational(4)*arctan_enclosure(F(1, 239))
    assert data['pi'] == record(pi)
    rows = data['roots_and_weights']
    assert len(rows) == DEGREE
    previous, weight_sum = -S, I(0)
    for j, row in enumerate(rows):
        z, w = interval(row['root']), interval(row['weight'])
        assert row['index'] == j and previous < z.lo < z.hi < S
        assert z.hi-z.lo <= S//10**90 and z.lo > -S
        assert sign_at(z.lo) == row['sign_lo'] and sign_at(z.hi) == row['sign_hi']
        assert row['sign_lo'] != row['sign_hi']
        p, pm = legendre(z)
        derivative = I.rational(DEGREE)*(pm-z*p)/(ONE-z*z)
        assert record(TWO/((ONE-z*z)*derivative*derivative)) == row['weight']
        assert w.lo > 0
        previous, weight_sum = z.hi, weight_sum+w
    assert weight_sum.lo <= 2*S <= weight_sum.hi
    assert len(data['positive_panels']) == 2
    for panel, (a, b) in zip(data['positive_panels'], [(F(0), F(5, 2)), (F(5, 2), F(3))]):
        assert panel['a'] == str(a) and panel['b'] == str(b) and len(panel['nodes']) == DEGREE
        for root, node in zip(rows, panel['nodes']):
            z, w = interval(root['root']), interval(root['weight'])
            x = I.rational((a+b)/2)+I.rational((b-a)/2)*z
            assert node['x'] == record(x)
            assert node['weight'] == record(I.rational((b-a)/2)*w)
            assert node['rho'] == record(rho(x, a == F(5, 2)))
    actual = Integrals((0, 2), 112, DEGREE)
    maxima, seen = [F(0), F(0)], set()
    table = {(r['h'], r['n']): r for r in data['transforms']}
    for row in data['transforms']:
        h, n = row['h'], row['n']
        assert h in (0, 1) and -224 <= n <= 224 and (h, n) not in seen
        seen.add((h, n))
        stored = actual.transforms[h][n]
        assert float(stored.real).hex() == row['stored_real_hex']
        assert float(stored.imag).hex() == row['stored_imag_hex']
        real, imag = interval(row['exact_rule_real']), interval(row['exact_rule_imag'])
        opposite = table[h, -n]
        assert row['exact_rule_real'] == opposite['exact_rule_real']
        if n:
            assert record(-imag) == opposite['exact_rule_imag']
        assert record(real if h == 1 else imag) == record(I(0))
        error = compare_component(stored.real, real)+compare_component(stored.imag, imag)
        saved = row['error_upper']
        assert error == F(int(saved['num']), int(saved['den']))
        maxima[h] = max(maxima[h], error)
    assert seen == {(h, n) for h in (0, 1) for n in range(-224, 225)}
    margins, quadrature, required = [F(593, 10**14), F(879, 10**14)], [F(7, 10**14), F(21, 10**14)], [F(6, 10**12), F(9, 10**12)]
    for h, summary in enumerate(data['bounds']):
        assert maxima[h] < margins[h] and maxima[h]+quadrature[h] < required[h]
        assert summary['stored_minus_rule_upper'] == upper_display(maxima[h])
        assert summary['total_with_L036_upper'] == upper_display(maxima[h]+quadrature[h])
        assert summary['margin_pass'] and summary['total_pass']
    integrals_source = source.with_name('check_continuum_pure_sectors.py')
    assert hashlib.sha256(integrals_source.read_bytes()).hexdigest() == data['integrals_source_sha256']
    assert data['status'] == 'PASS' and data['failure_count'] == 0 and not data['failures']
    audit = {'status': 'PASS', 'root_and_weight_records_checked': len(rows),
             'panel_records_checked': 288, 'all_transform_comparisons_checked': len(seen),
             'bounds': data['bounds'], 'failures': [],
             'certificate_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
             'qualification': 'The generating script, not this audit, encloses all exact-rule transform sums.'}
    path = source.with_name('stored-fourier-enclosure-audit.json')
    path.write_text(json.dumps(audit, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'roots': len(rows), 'transforms': len(seen),
                      'failures': [], 'path': str(path)}))


if __name__ == '__main__':
    main()
